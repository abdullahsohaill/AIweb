# reddit_global_search_crawler.py
"""
Definitive, OPTIMIZED, and RESILIENT Reddit crawler for AI services discovery.

This final version is designed for speed, safety, and adherence to the final methodology:
1.  Parallel Processing: A ThreadPoolExecutor with 15 workers processes multiple Reddit
    posts concurrently for a significant speedup.
2.  Resumability: The script tracks completed search phrases. If interrupted, it will
    automatically resume where it left off, preventing data loss.
3.  No Pre-filtering: As per final requirements, the domain blocklist has been removed.
    All external links are collected for later processing.
4.  Graceful Rate-Limit Handling: Catches PRAW API exceptions, pauses to recover,
    and then continues the process.

Requirements:
  pip install praw python-dotenv tqdm

Usage:
  - Create a .env file with your Reddit API credentials.
  - Create a search_phrases.txt file with your final list of queries.
  - Run the script: python reddit_global_search_crawler.py
    (If it stops for any reason, simply run it again to resume).
"""

import os
import re
import csv
from pathlib import Path
import time
from datetime import datetime
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

import praw
from prawcore.exceptions import PrawcoreException
from dotenv import load_dotenv
from tqdm import tqdm

# --- Configuration ---
load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "web-measure-crawler/0.1 by u/your_username")

PHRASES_FILE = "search_phrases.txt"
LOG_FILE = 'crawler.log'

# --- Performance & Resiliency Tuning ---
# Set to 15 workers for high-speed parallel processing
MAX_WORKERS = 25

# Search parameters
POST_LIMIT_PER_PHRASE = 75
SORT_BY = "relevance"
START_TIMESTAMP = int(datetime(2022, 12, 1).timestamp())

# Output settings
OUTPUT_DIR = Path("reddit_output")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_CSV = OUTPUT_DIR / "reddit_extracted_links.csv"
PROGRESS_FILE = OUTPUT_DIR / "completed_phrases.txt"

# Regex for capturing link text and URL
MARKDOWN_URL_REGEX = r'\[(.*?)\]\((https?://[^\s)]+)\)'
RAW_URL_REGEX = r'(?<!\]\()(https?://[^\s()<>]+)' # Negative lookbehind to avoid re-capturing markdown URLs

# --- SETUP LOGGING ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_reddit():
    if not all([REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT]):
        raise ValueError("Reddit API credentials not found in .env file.")
    return praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

def load_search_phrases(file_path, progress_file_path):
    """Loads all phrases and filters out those that are already completed."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            all_phrases = {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

    completed_phrases = set()
    if progress_file_path.exists():
        with open(progress_file_path, 'r', encoding='utf-8') as f:
            completed_phrases = {line.strip() for line in f if line.strip()}
    
    phrases_to_run = list(all_phrases - completed_phrases)
    if completed_phrases:
        print(f"Resuming crawl. {len(completed_phrases)} phrases already completed.")
    return phrases_to_run

def mark_phrase_as_completed(phrase, progress_file_path):
    """Appends a successfully completed phrase to the progress file."""
    with open(progress_file_path, 'a', encoding='utf-8') as f:
        f.write(f"{phrase}\n")

def extract_all_links(text):
    """Extracts both Markdown-formatted and raw URLs from text without a blocklist."""
    if not text: 
        return []
    
    links = []
    # Find Markdown links first: [text](url)
    for link_text, url in re.findall(MARKDOWN_URL_REGEX, text):
        links.append({'text': link_text.strip(), 'url': url.rstrip(').,;!?"\'')})
        
    # Find raw URLs that were not part of a Markdown link
    for url in re.findall(RAW_URL_REGEX, text):
        links.append({'text': '', 'url': url.rstrip(').,;!?"\'')})

    return links

def process_submission(submission, search_phrase):
    """Processes a single Reddit submission, extracting all links from the post and all comments."""
    results = []
    try:
        # The main bottleneck: fetch all comments.
        submission.comments.replace_more(limit=None)
    except Exception as e:
        logging.warning(f"Could not expand comments for submission {submission.id}: {e}")
    
    # Process original post
    for link in extract_all_links(submission.selftext):
        results.append({"platform": "Reddit", "search_phrase": search_phrase, "source_url": f"https://www.reddit.com{submission.permalink}", "link_text": link['text'], "extracted_url": link['url']})
    
    # Process all comments
    for comment in submission.comments.list():
        for link in extract_all_links(comment.body):
            results.append({"platform": "Reddit", "search_phrase": search_phrase, "source_url": f"https://www.reddit.com{comment.permalink}", "link_text": link['text'], "extracted_url": link['url']})
            
    return results

def main():
    """Main execution function, parallelized for speed and designed for resumability."""
    reddit = initialize_reddit()
    search_phrases = load_search_phrases(PHRASES_FILE, PROGRESS_FILE)

    if not search_phrases:
        print("All phrases have been processed. Exiting.")
        return

    print(f"Starting definitive & OPTIMIZED Reddit search for {len(search_phrases)} phrases...")

    file_exists = OUTPUT_CSV.exists()
    with open(OUTPUT_CSV, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ["platform", "search_phrase", "source_url", "link_text", "extracted_url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        
        with tqdm(search_phrases, desc="Total Progress") as pbar:
            for phrase in pbar:
                try:
                    pbar.set_description(f"Searching for '{phrase}'")
                    full_query = f'{phrase} timestamp:{START_TIMESTAMP}..'
                    
                    search_results = list(reddit.subreddit("all").search(full_query, sort=SORT_BY, limit=POST_LIMIT_PER_PHRASE))
                    if not search_results:
                        mark_phrase_as_completed(phrase, PROGRESS_FILE)
                        continue
                    
                    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                        future_to_submission = {executor.submit(process_submission, sub, phrase): sub for sub in search_results}
                        
                        for future in tqdm(as_completed(future_to_submission), total=len(search_results), desc=f"Processing '{phrase}'", leave=False):
                            try:
                                extracted_data = future.result()
                                if extracted_data:
                                    writer.writerows(extracted_data)
                                    f.flush()
                            except Exception as exc:
                                logging.error(f"Error processing a submission: {exc}")
                    
                    mark_phrase_as_completed(phrase, PROGRESS_FILE)

                except PrawcoreException as e:
                    logging.error(f"PRAW API Rate Limit or other API error for '{phrase}': {e}")
                    pbar.set_description(f"API ERROR for '{phrase}'. Pausing 60s...")
                    time.sleep(60)
                except Exception as e:
                    logging.error(f"A major error occurred for phrase '{phrase}': {e}")
                    pbar.set_description(f"Major error for '{phrase}'. Pausing...")
                    time.sleep(10)

    print(f"\nExtraction complete. All raw links saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()