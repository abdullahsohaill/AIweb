# web_crawler.py (Definitive Final Version - Bug Fixed)
# A robust, multithreaded crawler with explicit proxy validation and deep pagination.

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import unquote
import random
import csv
import re
import time
import logging
import os
import pandas as pd
from tqdm import tqdm

# --- CONFIGURATION ---
INPUT_QUERIES_FILE = 'exhaustive_search_queries.txt'
OUTPUT_CSV_FILE = 'phase1_discovered_urls.csv'
LOG_FILE = 'crawler.log'
# DuckDuckGo shows ~10-30 results per page load. 500 max_results aims for all available pages.
# The actual number will be less if a query has fewer total results.
MAX_RESULTS_PER_QUERY = 500
MAX_WORKERS = 8       # Number of parallel threads.

# --- DIVERSE USER AGENTS (EXPANDED LIST) ---
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edg/120.0.2210.61',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:118.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:117.0) Gecko/20100101 Firefox/117.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
]

# --- PROXY CONFIGURATION ---
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
    """(CORRECTED) Tests a list of proxies and returns only the ones that work."""
    if not proxies_to_test: return []
    print("Validating proxies... this may take a few minutes.")
    valid_proxies = []

    def test_proxy(p):
        display_ip = p.split('@')[-1]
        try:
            res = requests.get("https://api.ipify.org?format=json", proxies={"http": p, "https": p}, timeout=15)
            if res.status_code == 200:
                print(f"  [SUCCESS] Proxy {display_ip} is working.")
                return p
            else:
                print(f"  [FAILURE] Proxy {display_ip} returned status {res.status_code}.")
                return None
        except requests.exceptions.Timeout:
            print(f"  [TIMEOUT] Proxy {display_ip} failed to respond.")
            return None
        except requests.exceptions.RequestException:
            print(f"  [FAILURE] Proxy {display_ip} failed to connect.")
            return None

    with ThreadPoolExecutor(max_workers=len(proxies_to_test) or 1) as executor:
        future_to_proxy = {executor.submit(test_proxy, p): p for p in proxies_to_test}
        for future in as_completed(future_to_proxy):
            result = future.result()
            if result:
                valid_proxies.append(result)

    print(f"\nValidation Complete: Found {len(valid_proxies)} working proxies out of {len(proxies_to_test)}.")
    logging.info(f"Validated {len(valid_proxies)} working proxies.")
    return valid_proxies

def search_duckduckgo_for_query(query, max_results, available_proxies):
    """Performs a deep, paginated search on DuckDuckGo for a single query."""
    session = requests.Session()
    session.headers.update({'User-Agent': random.choice(USER_AGENTS)})
    if available_proxies:
        session.proxies = {'http': random.choice(available_proxies), 'https': random.choice(available_proxies)}

    found_links = set()
    vqd_token = None

    try:
        res = session.get('https://html.duckduckgo.com/html/', params={'q': query}, timeout=20)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        vqd_match = re.search(r"vqd=([\d-]+)\&", res.text)
        if not vqd_match:
            logging.warning(f"No VQD token for '{query}'. Only scraping one page.")
            max_results = 30
        else:
            vqd_token = vqd_match.group(1)

        for link_tag in soup.select('a.result__a'):
            href = link_tag.get('href')
            if href:
                try:
                    clean_url = unquote(href.split('uddg=')[1].split('&rut=')[0])
                    if clean_url.startswith('http'): found_links.add(clean_url)
                except (IndexError, KeyError): continue
        
        if vqd_token and max_results > 30:
            for s_param in range(30, max_results, 30):
                time.sleep(random.uniform(2, 6))
                data = {'q': query, 's': s_param, 'o': 'json', 'vqd': vqd_token}
                res = session.post('https://html.duckduckgo.com/html/', data=data, timeout=25)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, 'html.parser')
                
                page_results = soup.select('a.result__a')
                if not page_results:
                    logging.info(f"No more results for '{query}' after {len(found_links)} links.")
                    break
                
                for link_tag in page_results:
                    href = link_tag.get('href')
                    if href:
                        try:
                            clean_url = unquote(href.split('uddg=')[1].split('&rut=')[0])
                            if clean_url.startswith('http'): found_links.add(clean_url)
                        except (IndexError, KeyError): continue

    except requests.exceptions.RequestException as e:
        logging.error(f"NETWORK/HTTP ERROR on query '{query}': {e}")
        return []

    return list(found_links)

if __name__ == "__main__":
    if not os.path.exists(INPUT_QUERIES_FILE):
        print(f"ERROR: '{INPUT_QUERIES_FILE}' not found. Please run the seed_generator.py script first.")
        exit()

    with open(INPUT_QUERIES_FILE, 'r', encoding='utf-8') as f:
        queries = [line.strip() for line in f.readlines() if line.strip()]

    active_proxies = validate_proxies(PROXIES)
    if not active_proxies:
        print("\nWARNING: No working proxies found. Running on local IP. This is risky and may get blocked.")
        logging.warning("No working proxies found. Running on local IP.")

    processed_queries = set()
    if os.path.exists(OUTPUT_CSV_FILE):
        try:
            df_existing = pd.read_csv(OUTPUT_CSV_FILE)
            if not df_existing.empty:
                processed_queries = set(df_existing['source_query'].unique())
            print(f"Resuming crawl. Found {len(processed_queries)} already completed queries.")
        except (pd.errors.EmptyDataError, FileNotFoundError):
            pass
    
    if not processed_queries:
        with open(OUTPUT_CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['source_query', 'discovered_url'])

    queries_to_run = [q for q in queries if q not in processed_queries]

    with open(OUTPUT_CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_query = {executor.submit(search_duckduckgo_for_query, query, MAX_RESULTS_PER_QUERY, active_proxies): query for query in queries_to_run}

            for future in tqdm(as_completed(future_to_query), total=len(queries_to_run), desc="Crawling Queries"):
                query = future_to_query[future]
                try:
                    links = future.result()
                    if links:
                        for link in links:
                            writer.writerow([query, link])
                        f.flush()
                        logging.info(f"SUCCESS: Query '{query}' yielded {len(links)} links.")
                    else:
                        logging.warning(f"EMPTY: Query '{query}' yielded no links.")
                except Exception as exc:
                    logging.error(f"FATAL ERROR in main loop for query '{query}': {exc}")

    print(f"\nPhase 1 Discovery Crawl Complete. Results are in '{OUTPUT_CSV_FILE}'.")