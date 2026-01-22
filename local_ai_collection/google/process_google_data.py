import pandas as pd
from urllib.parse import urlparse
from pathlib import Path

# --- CONFIGURATION ---
# Matches the output from local_ai_collection/google/google_search_crawler.py
RAW_INPUT_FILE = Path("local_ai_google_extracted_links.csv")
PROCESSED_OUTPUT_FILE = Path("local_ai_google_processed_links.csv")

def get_fqdn(url):
    """Extracts the FQDN (e.g., 'openai.com') from a full URL."""
    try:
        netloc = urlparse(url).netloc
        if netloc.startswith('www.'):
            return netloc[4:]
        return netloc
    except Exception:
        return None

if __name__ == "__main__":
    if not RAW_INPUT_FILE.exists():
        print(f"ERROR: Raw input file not found at '{RAW_INPUT_FILE}'. Please run the crawler first.")
        exit()

    print("--- Starting Google Search Data Processing (Local AI) ---")

    # 1. Load Data
    df = pd.read_csv(RAW_INPUT_FILE)
    print(f"Step 1: Loaded {len(df):,} raw link entries.")

    # 2. Deduplicate
    df.drop_duplicates(subset=['extracted_url'], keep='first', inplace=True)
    print(f"   -> Found {len(df):,} unique URLs after deduplication.")

    # 3. Extract FQDN
    print("Step 3: Extracting FQDNs from URLs...")
    df['fqdn'] = df['extracted_url'].apply(get_fqdn)
    
    df.dropna(subset=['fqdn'], inplace=True)
    df = df[df['fqdn'] != '']

    # 4. Sort and Save
    print(f"Step 4: Saving processed data...")
    df_sorted = df.sort_values(by='fqdn', ascending=True)

    final_columns = [
        'platform', 'search_phrase', 'source_url', 
        'link_text', 'extracted_url', 'fqdn'
    ]
    df_final = df_sorted[final_columns]

    df_final.to_csv(PROCESSED_OUTPUT_FILE, index=False)
    print(f"✅ Enriched dataset saved to: '{PROCESSED_OUTPUT_FILE}'")