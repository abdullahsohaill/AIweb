import os, re, csv, time, logging
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import praw
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
REDDIT = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="local-ai-crawler/1.0"
)

PHRASES_FILE = "search_phrases.txt"
OUTPUT_DIR = Path("reddit_output")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_CSV = OUTPUT_DIR / "local_ai_reddit_extracted_links.csv" # Specific name
PROGRESS_FILE = OUTPUT_DIR / "completed_phrases.txt"
START_TIMESTAMP = int(datetime(2022, 12, 1).timestamp())

MARKDOWN_URL_REGEX = r'\[(.*?)\]\((https?://[^\s)]+)\)'
RAW_URL_REGEX = r'(?<!\]\()(https?://[^\s()<>]+)'

def extract_all_links(text):
    if not text: return []
    links = []
    for link_text, url in re.findall(MARKDOWN_URL_REGEX, text):
        links.append({'text': link_text.strip(), 'url': url.rstrip(').,;!?"\'')})
    for url in re.findall(RAW_URL_REGEX, text):
        links.append({'text': '', 'url': url.rstrip(').,;!?"\'')})
    return links

def process_submission(submission, search_phrase):
    results = []
    try: submission.comments.replace_more(limit=0) # Speed up
    except: pass
    
    # Post body
    for link in extract_all_links(submission.selftext):
        results.append({"platform": "Reddit", "search_phrase": search_phrase, "source_url": f"https://www.reddit.com{submission.permalink}", "link_text": link['text'], "extracted_url": link['url']})
    
    # Comments (limit 20 for speed)
    for comment in submission.comments.list()[:20]:
        for link in extract_all_links(comment.body):
            results.append({"platform": "Reddit", "search_phrase": search_phrase, "source_url": f"https://www.reddit.com{comment.permalink}", "link_text": link['text'], "extracted_url": link['url']})
    return results

def main():
    with open(PHRASES_FILE, 'r') as f: phrases = [l.strip() for l in f if l.strip()]
    
    file_exists = OUTPUT_CSV.exists()
    with open(OUTPUT_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["platform", "search_phrase", "source_url", "link_text", "extracted_url"])
        if not file_exists: writer.writeheader()
        
        for phrase in tqdm(phrases):
            try:
                results = list(REDDIT.subreddit("all").search(f'{phrase} timestamp:{START_TIMESTAMP}..', limit=50, sort="relevance"))
                with ThreadPoolExecutor(max_workers=10) as ex:
                    futures = [ex.submit(process_submission, sub, phrase) for sub in results]
                    for fut in as_completed(futures):
                        if fut.result(): writer.writerows(fut.result())
            except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    main()