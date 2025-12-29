# google_search_crawler.py
"""
Definitive Google Search crawler for AI services discovery, incorporating final methodology feedback.

This script executes the following process:
1.  Uses the SerpApi service to reliably perform Google searches without being blocked.
2.  For each search phrase, it queries for the top 30 results created after Dec 1, 2022.
3.  For each search result URL, it performs a targeted crawl using a rotating proxy pool
    to download the page content.
4.  It uses BeautifulSoup to remove common noise elements (headers, footers, navs) from the
    downloaded HTML.
5.  It extracts all external hyperlinks (including link text) from the cleaned main content.
6.  The entire process is parallelized for efficiency.

Requirements:
  pip install google-search-results requests beautifulsoup4 pandas tqdm python-dotenv lxml

Usage:
  - Sign up for a free account at serpapi.com to get an API key.
  - Create a .env file with your SerpApi key:
    SERPAPI_API_KEY="your_serpapi_key_here"
  - Create a search_phrases.txt file with your final list of queries.
  - Run the script: python google_search_crawler.py
"""

import csv
import logging
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch
from dotenv import load_dotenv
from tqdm import tqdm

# --- CONFIGURATION (Incorporating Feedback) ---
load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
PHRASES_FILE = 'search_phrases.txt'
LOG_FILE = 'crawler.log'
OUTPUT_CSV_FILE = 'google_extracted_links.csv'

# Search parameters per Yash's feedback
NUM_RESULTS_PER_QUERY = 30 # Approx. 3 pages
MAX_WORKERS = 8 # Parallel threads for crawling

# --- USER AGENTS & PROXIES (Still needed for the content crawling part) ---
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]
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
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_proxies(proxies_to_test):
    # This function remains the same as your previous script
    if not proxies_to_test: return []
    print("Validating proxies...")
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

def search_google_serpapi(query, num_results):
    """Performs a Google search using SerpApi and returns a list of URLs."""
    if not SERPAPI_API_KEY:
        raise ValueError("SerpApi API key not found in .env file (SERPAPI_API_KEY).")
    
    params = {
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results,
        "engine": "google",
        # --- NEW: Precise date filtering per feedback ---
        # tbs=cdr:1 -> custom date range, cd_min -> start date
        "tbs": "cdr:1,cd_min:12/1/2022",
    }
    
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])
        return [res['link'] for res in organic_results if 'link' in res]
    except Exception as e:
        logging.error(f"SerpApi Search failed for query '{query}': {e}")
        return []

def extract_links_from_url(source_url, search_phrase, proxy):
    """Crawls a single URL using a proxy, removes noise with BeautifulSoup, and extracts links."""
    # This function is the same as your robust DDGS version, just changing the platform name
    results = []
    session = requests.Session()
    session.headers.update({'User-Agent': random.choice(USER_AGENTS)})
    proxy_dict = {"http": proxy, "https": proxy} if proxy else None

    try:
        response = session.get(source_url, timeout=20, proxies=proxy_dict)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        page_title = (soup.title.string if soup.title else "").strip()

        for tag in soup.find_all(['header', 'footer', 'nav', 'aside', 'script', 'style']):
            tag.decompose()
        for noisy_selector in soup.select('[role="navigation"], [role="banner"], [role="contentinfo"], #footer, .footer, #sidebar, .sidebar, #header, .header'):
            noisy_selector.decompose()
            
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            if href and href.startswith(('http://', 'https://')):
                link_text = a_tag.get_text(strip=True)
                results.append({"platform": "Google", "search_phrase": search_phrase, "source_url": source_url, "link_text": link_text, "extracted_url": href})
        
        results.append({"platform": "Google", "search_phrase": search_phrase, "source_url": "direct_hit", "link_text": page_title, "extracted_url": source_url})

    except requests.exceptions.HTTPError as e:
        logging.warning(f"BLOCKED/FAILED ({e.response.status_code}) for {source_url}")
    except requests.exceptions.RequestException:
        logging.warning(f"Crawl TIMEOUT/FAILED for {source_url}")
    except Exception as e:
        logging.error(f"Unexpected error processing {source_url}: {e}")
        
    return results

def process_query(query, proxy_list):
    """Main worker function: searches Google, then crawls all results."""
    all_extracted_data = []
    
    # Stage 1: Discovery via SerpApi (does not need our proxies)
    source_urls = search_google_serpapi(query, NUM_RESULTS_PER_QUERY)
    if not source_urls:
        logging.warning(f"Query '{query}' yielded no Google search results.")
        return []

    # Stage 2: Extraction (uses our own proxy pool)
    for url in source_urls:
        proxy = random.choice(proxy_list) if proxy_list else None
        extracted_data = extract_links_from_url(url, query, proxy)
        all_extracted_data.extend(extracted_data)
        time.sleep(random.uniform(1.0, 3.5))

    logging.info(f"Query '{query}' processed, found {len(source_urls)} sources yielding {len(all_extracted_data)} candidate links.")
    return all_extracted_data

if __name__ == "__main__":
    if not os.path.exists(PHRASES_FILE):
        print(f"ERROR: '{PHRASES_FILE}' not found.")
        exit()

    with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
        queries_to_run = [line.strip() for line in f.readlines() if line.strip()]
    
    active_proxies = validate_proxies(PROXIES)
    if not active_proxies:
        print("\nWARNING: No working proxies found. Content crawling is very likely to fail.")
    
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
    
    print(f"\nConsolidated Crawl Complete. Raw links saved to '{OUTPUT_CSV_FILE}'.")
    print("\nNext Step: Run a separate script to perform the 5-step FQDN filtering on the final CSV.")