# process_reddit_data.py
"""
This script processes the raw data collected by the Reddit crawler.
It prepares the data for final aggregation by:
1.  Loading the raw extracted links from the Reddit crawl.
2.  Deduplicating the data based on the unique 'extracted_url'.
3.  Adding a new 'fqdn' column by extracting the domain from each URL.
4.  Saving the enriched data to a new CSV, ready for aggregation.

Requirements:
  pip install pandas tqdm

Usage:
  - Ensure 'reddit_output/reddit_extracted_links.csv' exists.
  - Run the script: python process_reddit_data.py
"""

import pandas as pd
from urllib.parse import urlparse
from pathlib import Path

# --- CONFIGURATION ---
INPUT_DIR = Path("reddit_output")
RAW_INPUT_FILE = INPUT_DIR / "reddit_extracted_links.csv"
PROCESSED_OUTPUT_FILE = INPUT_DIR / "reddit_processed_links.csv"

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

    print("--- Starting Reddit Data Processing (No Blocklisting) ---")

    # Load the raw data
    df = pd.read_csv(RAW_INPUT_FILE)
    print(f"Step 1: Loaded {len(df):,} raw link entries.")

    # Step 2: Deduplicate based on 'extracted_url', preserving the first entry's context
    df.drop_duplicates(subset=['extracted_url'], keep='first', inplace=True)
    print(f"   -> Found {len(df):,} unique URLs after deduplication.")

    # --- Step 3: Add the 'fqdn' column ---
    print("Step 3: Extracting FQDNs from URLs...")
    df['fqdn'] = df['extracted_url'].apply(get_fqdn)
    
    df.dropna(subset=['fqdn'], inplace=True)
    df = df[df['fqdn'] != '']
    print("   -> FQDN extraction complete.")
    
    # --- Step 4 (REMOVED): Domain blocklisting is now skipped. ---
    print("Step 4: Skipping domain blocklisting. This will be done on the aggregated dataset.")

    # --- Step 5: Prepare final dataset for aggregation ---
    print(f"Step 5: Preparing dataset with {len(df):,} entries for aggregation.")
    
    # Sort the data by FQDN
    df_sorted = df.sort_values(by='fqdn', ascending=True)

    # Ensure all original and new columns are present
    final_columns = [
        'platform', 'search_phrase', 'source_url', 
        'link_text', 'extracted_url', 'fqdn'
    ]
    df_final = df_sorted[final_columns]

    df_final.to_csv(PROCESSED_OUTPUT_FILE, index=False)

    print("\n--- Processing Complete ---")
    print(f"✅ Enriched dataset saved to: '{PROCESSED_OUTPUT_FILE}'")
    
    # --- Final Insights ---
    print("\n--- Data Insights (Pre-filtering) ---")
    print(f"Total unique FQDNs discovered: {df_final['fqdn'].nunique():,}")
    print("\nTop 15 Most Frequently Discovered Domains:")
    print(df_final['fqdn'].value_counts().head(15).to_string())