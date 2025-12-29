# github_search_and_extract.py
"""
Definitive GitHub crawler for AI services discovery, incorporating final methodology feedback.

This script executes the following process:
1.  Authenticates with the GitHub API using a Personal Access Token (PAT).
2.  For each search phrase, it queries for the top 90 repositories (approximating 3 pages),
    sorted by stars, and created after November 2022.
3.  For each repository, it fetches the raw content of its README.md file.
4.  It uses a regular expression to parse all Markdown-formatted external hyperlinks,
    capturing both the visible link text and the target URL.
5.  All extracted data is saved to a CSV file without any domain-based pre-filtering.

Requirements:
  pip install PyGithub python-dotenv tqdm

Usage:
  - Create a .env file with your GitHub Personal Access Token:
    GITHUB_TOKEN="ghp_YourTokenHere"
  - Create a search_phrases.txt file with your final list of queries.
  - Run the script: python github_search_and_extract.py
"""

import os
import re
import csv
import base64
from pathlib import Path
import time

from github import Github, RateLimitExceededException
from dotenv import load_dotenv
from tqdm import tqdm

# --- CONFIGURATION (Incorporating Feedback) ---
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
PHRASES_FILE = "search_phrases.txt"

# Search parameters
# "3 pages" in the API roughly corresponds to 3 * 30 results/page = 90
REPO_LIMIT_PER_PHRASE = 90
SORT_BY = "stars"
ORDER = "desc"
# Date filter to find more relevant, post-ChatGPT era repositories
DATE_FILTER = "created:>2022-11-01"

# Output settings
OUTPUT_DIR = Path("github_output")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_CSV = OUTPUT_DIR / "github_extracted_links.csv"

# Regex that captures BOTH the link text and the URL
# Group 1: (.*?) -> The link text (non-greedy)
# Group 2: (https?://[^\s)]+) -> The URL
MARKDOWN_URL_REGEX = r'\[(.*?)\]\((https?://[^\s)]+)\)'

def initialize_github():
    """Initializes and returns a PyGithub instance."""
    if not GITHUB_TOKEN:
        raise ValueError("GitHub Personal Access Token not found in .env file (GITHUB_TOKEN).")
    return Github(GITHUB_TOKEN)

def extract_links_from_readme(repo, search_phrase):
    """Fetches and parses the README of a repository to extract link text and URLs."""
    results = []
    try:
        readme_content_b64 = repo.get_readme().content
        # The content is Base64 encoded, so we must decode it. Ignore errors for robustness.
        decoded_content = base64.b64decode(readme_content_b64).decode('utf-8', 'ignore')
        
        # Find all tuples of (link_text, url)
        found_links = re.findall(MARKDOWN_URL_REGEX, decoded_content)
        
        for link_text, url in found_links:
            # Per feedback, we no longer use a domain blocklist. We collect all external links.
            if 'github.com' not in url:
                results.append({
                    "platform": "GitHub",
                    "search_phrase": search_phrase,
                    "repository_name": repo.full_name,
                    "stars": repo.stargazers_count,
                    "source_url": repo.html_url,
                    "link_text": link_text.strip(),
                    "extracted_url": url,
                })

    except Exception:
        # This can happen if a repo has no README, is empty, or other API issues.
        # We can safely ignore these and move on.
        pass
        
    return results

def main():
    """Main execution function."""
    g = initialize_github()
    
    try:
        with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
            search_phrases = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {PHRASES_FILE} not found. Please create it.")
        return

    print(f"Starting definitive GitHub search for {len(search_phrases)} phrases...")

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["platform", "search_phrase", "repository_name", "stars", "source_url", "link_text", "extracted_url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for phrase in tqdm(search_phrases, desc="Processing All Phrases"):
            try:
                # Combine the phrase with the date filter for the final query
                full_query = f"{phrase} {DATE_FILTER}"
                
                repositories = g.search_repositories(
                    query=full_query, sort=SORT_BY, order=ORDER
                )
                
                # Use a counter to process up to our defined limit from the search results
                repo_count = 0
                for repo in repositories:
                    if repo_count >= REPO_LIMIT_PER_PHRASE:
                        break
                    
                    extracted_data = extract_links_from_readme(repo, phrase)
                    if extracted_data:
                        writer.writerows(extracted_data)
                    
                    repo_count += 1
                    time.sleep(1) # Be polite to the API to avoid secondary rate limits

            except RateLimitExceededException:
                print("\nGitHub rate limit exceeded. Waiting for 5 minutes...")
                time.sleep(300)
                continue # Retry the same phrase after waiting
            except Exception as e:
                print(f"\nAn unexpected error occurred for phrase '{phrase}': {e}")


    print(f"\nExtraction complete. All raw links saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()