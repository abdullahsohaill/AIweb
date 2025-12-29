import pandas as pd
import requests
import concurrent.futures
from tqdm import tqdm
import time

# --- CONFIGURATION ---
INPUT_FILE = "foundr_extracted.csv"
OUTPUT_FILE = "foundr_final_resolved.csv"
MAX_THREADS = 20  # Resolve 20 links at the same time for speed

# Headers to look like a real browser so redirects don't block us
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def resolve_url(row):
    """
    Takes a row, checks the external_url.
    If it's a redirect (go.foundr.ai), resolves it to the final URL.
    """
    url = row.get('external_url')
    
    # If empty or already resolved, skip
    if not url or "go.foundr.ai" not in str(url):
        return row

    try:
        # We verify=False to ignore SSL errors on some sketchy AI tool sites
        # timeout=5 prevents hanging on dead sites
        response = requests.head(url, headers=HEADERS, allow_redirects=True, timeout=10, verify=False)
        row['real_website_url'] = response.url
    except Exception as e:
        # If HEAD fails (some servers block it), try GET stream
        try:
            response = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=10, stream=True, verify=False)
            row['real_website_url'] = response.url
            response.close()
        except:
            row['real_website_url'] = "failed_to_resolve"
            
    return row

def main():
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"--- Loaded {len(df)} tools. Starting Link Resolution... ---")
    except FileNotFoundError:
        print(f"Error: Could not find {INPUT_FILE}. Run the scraper first.")
        return

    # Add new column if it doesn't exist
    if 'real_website_url' not in df.columns:
        df['real_website_url'] = None

    # Filter rows that need resolution to save time on re-runs
    # We only target rows where external_url exists AND real_website_url is empty
    # But for simplicity, we iterate all list items
    rows = df.to_dict('records')
    resolved_rows = []

    # Use ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # Wrap in tqdm for a progress bar
        results = list(tqdm(executor.map(resolve_url, rows), total=len(rows), unit="links"))
        
        # Update data
        df_final = pd.DataFrame(results)
        
        # Clean up: If resolution failed, maybe fallback to the original redirect link or leave empty
        # (This script marks them as 'failed_to_resolve' so you can filter them later)

        df_final.to_csv(OUTPUT_FILE, index=False)
        print(f"✅ Resolution Complete. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    # Suppress SSL warnings for cleaner output
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()