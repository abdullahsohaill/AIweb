# ddgs_and_extract_crawler.py
"""
A robust, two-stage, parallel crawler for discovering and extracting AI service links.

This is a consolidated and corrected script that uses the most reliable methods identified:
- STAGE 1 (Discovery): Uses the DuckDuckGo Search (ddgs) library with a rotating,
  validated proxy pool to reliably fetch search engine results.
- STAGE 2 (Extraction): For each discovered URL, it performs a targeted crawl using the
  same proxy pool. It uses a BeautifulSoup-based method to remove common noise
  elements (headers, footers, navs, asides) before extracting hyperlinks.

This version explicitly fixes the flaw of not using proxies for content extraction.

Requirements:
  pip install ddgs requests beautifulsoup4 pandas tqdm python-dotenv lxml

Usage:
  - Create a .env file (can be empty).
  - Create a search_phrases.txt file with one search phrase per line.
  - Run the script: python ddgs_and_extract_crawler.py
"""

import csv
import logging
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
from tqdm import tqdm

# --- CONFIGURATION ---
PHRASES_FILE = 'search_phrases.txt'
OUTPUT_CSV_FILE = 'final_extracted_links.csv'
LOG_FILE = 'crawler.log'
# Focused search on top ~3 pages for higher quality results
MAX_RESULTS_PER_QUERY = 5
# Number of parallel threads to run. 5-8 is a safe starting point.
MAX_WORKERS = 8

# --- DIVERSE USER AGENTS (EXPANDED LIST from your script) ---
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edg/120.0.2210.61',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
]

# --- PROXY CONFIGURATION (from your script) ---
PROXIES = [
    'http://uzoyuxkg:3sqtyuonfa4x@142.111.48.253:7030',
    'http://uzoyuxkg:3sqtyuonfa4x@31.59.20.176:6754',
    'http://uzoyuxkg:3sqtyuonfa4x@38.170.176.177:5572',
    'http://uzoyuxkg:3sqtyuonfa4x@198.23.239.134:6540',
    'http://uzoyuxkg:3sqtyuonfa4x@45.38.107.97:6014',
    'http://uzoyuxkg:3sqtyuonfa4x@107.172.163.27:6543',
    'http://uzoyuxkg:3sqtyuonfa4x@64.137.96.74:6641',
    'http://uzoyuxkg:3sqtyuonfa4x@216.10.27.159:6837',
    'http://uzoyuxkg:3sqtyuonfa4x@142.111.67.146:5611',
    'http://uzoyuxkg:3sqtyuonfa4x@142.147.128.93:6593',
]

# --- SETUP LOGGING ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def validate_proxies(proxies_to_test):
    """Tests a list of proxies and returns only the ones that work."""
    if not proxies_to_test: return []
    print("Validating proxies... this may take a few minutes.")
    def test_proxy(p):
        try:
            res = requests.get("https://api.ipify.org?format=json", proxies={"http": p, "https": p}, timeout=10)
            if res.status_code == 200: return p
        except requests.exceptions.RequestException: pass
        return None
    with ThreadPoolExecutor(max_workers=len(proxies_to_test) or 1) as executor:
        valid_proxies = [p for p in executor.map(test_proxy, proxies_to_test) if p]
    print(f"\nValidation Complete: Found {len(valid_proxies)} working proxies.")
    return valid_proxies

def search_ddgs(query, max_results, proxy):
    """Performs a search using the 'ddgs' library and a proxy."""
    try:
        results = DDGS(proxy=proxy, timeout=30).text(query, max_results=max_results)
        return [r['href'] for r in results if 'href' in r]
    except Exception as e:
        logging.error(f"DDGS Search failed for query '{query}': {e}")
        return []

def extract_links_from_url(source_url, search_phrase, proxy):
    """Crawls a single URL using a proxy, removes noise with BeautifulSoup, and extracts links."""
    results = []
    session = requests.Session()
    session.headers.update({'User-Agent': random.choice(USER_AGENTS)})
    
    # ** THE CRITICAL FIX IS HERE: Use the proxy for the content request **
    proxy_dict = {"http": proxy, "https": proxy} if proxy else None

    try:
        response = session.get(source_url, timeout=20, proxies=proxy_dict)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Keep the page title before we start decomposing things
        page_title = (soup.title.string if soup.title else "").strip()

        # Your original, preferred noise removal method
        for tag in soup.find_all(['header', 'footer', 'nav', 'aside', 'script', 'style']):
            tag.decompose()
        for noisy_selector in soup.select('[role="navigation"], [role="banner"], [role="contentinfo"], #footer, .footer, #sidebar, .sidebar, #header, .header'):
            noisy_selector.decompose()
            
        # Extract all remaining links
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            if href and href.startswith(('http://', 'https://')):
                link_text = a_tag.get_text(strip=True)
                results.append({"platform": "DDGS", "search_phrase": search_phrase, "source_url": source_url, "link_text": link_text, "extracted_url": href})
        
        # Always add the "direct hit"
        results.append({"platform": "DDGS", "search_phrase": search_phrase, "source_url": "direct_hit", "link_text": page_title, "extracted_url": source_url})

    except requests.exceptions.HTTPError as e:
        logging.warning(f"BLOCKED/FAILED ({e.response.status_code}) for {source_url}")
    except requests.exceptions.RequestException as e:
        logging.warning(f"Crawl TIMEOUT/FAILED for {source_url}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error processing {source_url}: {e}")
        
    return results

def process_query(query, proxy_list):
    """The main worker function for a single query."""
    all_extracted_data = []
    proxy = random.choice(proxy_list) if proxy_list else None
    
    source_urls = search_ddgs(query, MAX_RESULTS_PER_QUERY, proxy)
    if not source_urls:
        logging.warning(f"Query '{query}' yielded no search results.")
        return []

    # Using tqdm here to see progress per query
    for url in tqdm(source_urls, desc=f"Crawling '{query}'", leave=False):
        # Pass the same proxy down to the extraction function
        extracted_data = extract_links_from_url(url, query, proxy)
        all_extracted_data.extend(extracted_data)
        time.sleep(random.uniform(1.0, 3.5)) # Increased polite delay

    logging.info(f"Query '{query}' yielded {len(all_extracted_data)} candidate links.")
    return all_extracted_data


if __name__ == "__main__":
    if not os.path.exists(PHRASES_FILE):
        print(f"ERROR: '{PHRASES_FILE}' not found. Please create it.")
        exit()
    with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
        queries_to_run = [line.strip() for line in f.readlines() if line.strip()]
    
    active_proxies = validate_proxies(PROXIES)
    if not active_proxies:
        print("\nWARNING: No working proxies found. Running on local IP is very likely to fail.")
    
    try:
        with open(OUTPUT_CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ["platform", "search_phrase", "source_url", "link_text", "extracted_url"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                future_to_query = {executor.submit(process_query, query, active_proxies): query for query in queries_to_run}
                for future in tqdm(as_completed(future_to_query), total=len(queries_to_run), desc="Processing All Queries"):
                    try:
                        results = future.result()
                        if results:
                            writer.writerows(results)
                    except Exception as exc:
                        logging.error(f"FATAL ERROR processing future for query '{future_to_query[future]}': {exc}")
    except KeyboardInterrupt:
        print("\nCrawl interrupted by user. Partial results are saved.")
    
    print(f"\nConsolidated Crawl Complete. All extracted links saved to '{OUTPUT_CSV_FILE}'.")