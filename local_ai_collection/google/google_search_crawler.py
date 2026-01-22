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

load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
PHRASES_FILE = 'search_phrases.txt'
LOG_FILE = 'crawler.log'
# Outputting to a specific local_ai file
OUTPUT_CSV_FILE = 'local_ai_google_extracted_links.csv'

NUM_RESULTS_PER_QUERY = 30
MAX_WORKERS = 8 

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]
# Add your PROXIES list here if you want to use them, otherwise it defaults to direct
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

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def search_google_serpapi(query, num_results):
    if not SERPAPI_API_KEY: raise ValueError("SerpApi API key not found.")
    params = {
        "q": query, "api_key": SERPAPI_API_KEY, "num": num_results, "engine": "google",
        "tbs": "cdr:1,cd_min:12/1/2022",
    }
    try:
        search = GoogleSearch(params)
        return [res['link'] for res in search.get_dict().get("organic_results", []) if 'link' in res]
    except Exception as e:
        logging.error(f"SerpApi Search failed: {e}")
        return []

def extract_links_from_url(source_url, search_phrase, proxy):
    results = []
    session = requests.Session()
    session.headers.update({'User-Agent': random.choice(USER_AGENTS)})
    proxy_dict = {"http": proxy, "https": proxy} if proxy else None
    try:
        response = session.get(source_url, timeout=20, proxies=proxy_dict)
        soup = BeautifulSoup(response.content, 'lxml')
        page_title = (soup.title.string if soup.title else "").strip()
        
        # Simple extraction
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            if href and href.startswith(('http://', 'https://')):
                link_text = a_tag.get_text(strip=True)
                results.append({"platform": "Google", "search_phrase": search_phrase, "source_url": source_url, "link_text": link_text, "extracted_url": href})
        
        results.append({"platform": "Google", "search_phrase": search_phrase, "source_url": "direct_hit", "link_text": page_title, "extracted_url": source_url})
    except: pass
    return results

def process_query(query, proxy_list):
    all_extracted_data = []
    source_urls = search_google_serpapi(query, NUM_RESULTS_PER_QUERY)
    for url in source_urls:
        proxy = random.choice(proxy_list) if proxy_list else None
        all_extracted_data.extend(extract_links_from_url(url, query, proxy))
    return all_extracted_data

if __name__ == "__main__":
    with open(PHRASES_FILE, 'r') as f: queries = [line.strip() for line in f if line.strip()]
    
    with open(OUTPUT_CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["platform", "search_phrase", "source_url", "link_text", "extracted_url"])
        writer.writeheader()
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(process_query, q, PROXIES): q for q in queries}
            for future in tqdm(as_completed(futures), total=len(queries)):
                if future.result(): writer.writerows(future.result())