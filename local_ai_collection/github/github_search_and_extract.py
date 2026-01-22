import os
import re
import csv
import base64
from pathlib import Path
import time
from github import Github, RateLimitExceededException
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
PHRASES_FILE = "search_phrases.txt"
OUTPUT_DIR = Path("github_output")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_CSV = OUTPUT_DIR / "local_ai_github_links.csv"

# Adjusted filters for libraries (stars usually indicate reliability for libs)
REPO_LIMIT_PER_PHRASE = 60
SORT_BY = "stars"
# Date filter to find more relevant, post-ChatGPT era repositories
DATE_FILTER = "created:>2022-11-01"
MARKDOWN_URL_REGEX = r'\[(.*?)\]\((https?://[^\s)]+)\)'

def initialize_github():
    if not GITHUB_TOKEN: raise ValueError("GITHUB_TOKEN not found.")
    return Github(GITHUB_TOKEN)

def extract_links(repo, phrase):
    results = []
    try:
        content = base64.b64decode(repo.get_readme().content).decode('utf-8', 'ignore')
        links = re.findall(MARKDOWN_URL_REGEX, content)
        for text, url in links:
            if 'github.com' not in url: # We want external docs/demos
                results.append({
                    "platform": "GitHub", "search_phrase": phrase,
                    "repository_name": repo.full_name, "stars": repo.stargazers_count,
                    "source_url": repo.html_url, "link_text": text.strip(),
                    "extracted_url": url
                })
    except: pass
    return results

def main():
    g = initialize_github()
    with open(PHRASES_FILE, 'r') as f: phrases = [l.strip() for l in f if l.strip()]
    
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["platform", "search_phrase", "repository_name", "stars", "source_url", "link_text", "extracted_url"])
        writer.writeheader()
        
        for phrase in tqdm(phrases):
            try:
                repos = g.search_repositories(query=f"{phrase} {DATE_FILTER}", sort=SORT_BY, order="desc")
                for i, repo in enumerate(repos):
                    if i >= REPO_LIMIT_PER_PHRASE: break
                    data = extract_links(repo, phrase)
                    if data: writer.writerows(data)
                    time.sleep(1)
            except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    main()