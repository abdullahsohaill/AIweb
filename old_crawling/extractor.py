# extractor.py (Definitive Final Version - Handles Direct Hits & Sources)
# Phase 2: Processes all source URLs. It adds the URL itself as a candidate
# AND crawls it to extract all outgoing links as additional candidates.

import csv
import logging
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from tldextract import extract

# --- CONFIGURATION ---
INPUT_URL_FILE = 'phase1_discovered_urls_unique.csv'
# This is a new, much larger output file
OUTPUT_RAW_CANDIDATES_FILE = 'phase2_all_candidate_links.csv' 
LOG_FILE = 'extractor.log'
MAX_WORKERS = 10

# A curated list of domains that are almost always SOURCES of links, not services themselves.
# This helps the logic decide if a URL might be a "Direct Hit".
SOURCE_DOMAINS_IGNORE_LIST = [
    'google.com', 'youtube.com', 'linkedin.com', 'facebook.com', 'twitter.com', 't.co',
    'wikipedia.org', 'wordpress.org', 'microsoft.com', 'apple.com', 'amazon.com',
    'github.com', 'medium.com', 'dev.to', 'stackoverflow.com', 'techcrunch.com', 
    'venturebeat.com', 'producthunt.com', 'towardsdatascience.com', 'analyticsvidhya.com',
    'indiehackers.com', 'reddit.com', 'forbes.com', 'nytimes.com', 'wsj.com'
]

# --- DIVERSE USER AGENTS ---
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0',
]

# --- SETUP LOGGING ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_source_url(url):
    """
    Processes a single source URL.
    1. Adds the URL itself as a candidate if it's not a known "source" domain.
    2. Crawls the URL to extract all outgoing links as additional candidates.
    Returns a list of tuples: (source_page_url, candidate_link_url)
    """
    candidates = []
    
    # --- Step 1: The "Direct Hit" Check ---
    try:
        source_domain = extract(url).registered_domain
        if source_domain not in SOURCE_DOMAINS_IGNORE_LIST:
            # This URL is not from a known blog/repo site, so it might be a service itself.
            # We add it to the list, noting it was a direct discovery.
            candidates.append(("direct_discovery", url))
    except Exception as e:
        logging.warning(f"Could not parse source URL for direct hit check: {url} | Error: {e}")

    # --- Step 2: The "Source Page" Extraction ---
    try:
        session = requests.Session()
        session.headers.update({'User-Agent': random.choice(USER_AGENTS)})
        response = session.get(url, timeout=20)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href and href.startswith(('http://', 'https://')):
                # Add the outgoing link, noting which source page it came from.
                candidates.append((url, href))
    except requests.exceptions.RequestException as e:
        logging.warning(f"Could not crawl {url} for outgoing links: {e}")
    
    return candidates

if __name__ == "__main__":
    if not os.path.exists(INPUT_URL_FILE):
        print(f"ERROR: Input file '{INPUT_URL_FILE}' not found.")
        exit()

    df_sources = pd.read_csv(INPUT_URL_FILE)
    source_urls = df_sources['discovered_url'].tolist()
    print(f"Found {len(source_urls)} unique source URLs to process.")

    # Prepare the output file with the correct header
    with open(OUTPUT_RAW_CANDIDATES_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['source_page', 'candidate_link'])

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_url = {executor.submit(process_source_url, url): url for url in source_urls}

            for future in tqdm(as_completed(future_to_url), total=len(source_urls), desc="Extracting All Candidates"):
                try:
                    results = future.result()
                    if results:
                        writer.writerows(results)
                except Exception as exc:
                    url = future_to_url[future]
                    logging.error(f"FATAL ERROR processing source URL {url}: {exc}")

    print(f"\nPhase 2 (Extraction) Complete. A massive, unfiltered list of all potential candidates has been saved to '{OUTPUT_RAW_CANDIDATES_FILE}'.")
    # You can get a rough count of lines, but it will be huge.
    # On macOS/Linux: !wc -l {OUTPUT_RAW_CANDIDATES_FILE}