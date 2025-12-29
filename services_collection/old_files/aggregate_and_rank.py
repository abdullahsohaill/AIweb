# aggregate_and_rank.py
"""
This is the final processing script. It takes the cleaned data from all three
platforms (GitHub, Reddit, Google), enriches each entry with its Tranco rank
from the TOP 10 MILLION list, and aggregates them into a single master CSV.

This script performs the following steps:
1.  Downloads the latest Tranco top 10 million domains list.
2.  Loads the processed CSV files from the 'github/github_output', 'reddit/reddit_output',
    and 'google' directories.
3.  For each entry, it adds a 'domain_tranco_rank' column. A rank of -1 is assigned
    if the domain is not found in the Tranco list.
4.  Combines the three datasets into a single master list.
5.  Standardizes columns to a final, consistent format.
6.  Sorts the data by Tranco rank to prioritize review.
7.  Saves the final, aggregated dataset to the root 'services_collection' directory.

Requirements:
  pip install pandas tqdm requests

Usage:
  - Place this script in the 'services_crawlers' directory.
  - Ensure the processed CSV files exist in their respective output folders.
  - Run the script: python aggregate_and_rank.py
"""

import pandas as pd
import requests
from pathlib import Path
from tqdm import tqdm
import io
import zipfile
import logging

# --- CONFIGURATION ---
# Assumes this script is in the 'services_crawlers' root folder
GITHUB_PROCESSED_FILE = Path("github/github_output/github_processed_links.csv")
REDDIT_PROCESSED_FILE = Path("reddit/reddit_output/reddit_processed_links.csv")
GOOGLE_PROCESSED_FILE = Path("google/google_processed_links.csv")

FINAL_OUTPUT_FILE = "master_ai_services_list.csv"
LOG_FILE = 'aggregation.log'

# --- UPDATED: Using the Tranco Top 10 Million list ---
# TRANCO_URL = "https://tranco-list.eu/top-10m.csv.zip"
TRANCO_URL = "https://tranco-list.eu/top-1m.csv.zip"
# Default rank for domains not found in the Tranco Top 10M list
DEFAULT_RANK = -1 

# --- SETUP LOGGING ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_and_load_tranco_list():
    """
    Downloads the Tranco list, unzips it in memory,
    and returns a dictionary mapping domain to rank for fast lookups.
    """
    print(f"Downloading Tranco list from {TRANCO_URL}...")
    try:
        response = requests.get(TRANCO_URL, timeout=180) # Increased timeout for larger file
        response.raise_for_status()

        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            # --- UPDATED: File name inside the 10M zip is different ---
            with z.open('top-1m.csv') as f:
                tranco_df = pd.read_csv(f, header=None, names=['rank', 'fqdn'])
                tranco_map = pd.Series(tranco_df['rank'].values, index=tranco_df['fqdn']).to_dict()
        
        print(f"   -> Successfully loaded {len(tranco_map):,} domains from Tranco.")
        return tranco_map
    except Exception as e:
        logging.error(f"FAILED to download or process Tranco list: {e}")
        print(f"   -> FAILED to download Tranco list: {e}. Proceeding without ranks.")
        return {}

def process_and_enrich_file(file_path, tranco_map):
    """Loads a processed CSV, adds Tranco ranks, and returns the DataFrame."""
    if not file_path.exists():
        logging.warning(f"File not found, skipping: {file_path}")
        return None
        
    print(f"Processing {file_path}...")
    df = pd.read_csv(file_path)

    tqdm.pandas(desc=f"   -> Ranking {file_path.parts[0]}")
    df['domain_tranco_rank'] = df['fqdn'].progress_apply(lambda fqdn: tranco_map.get(str(fqdn), DEFAULT_RANK))
    
    return df

if __name__ == "__main__":
    tqdm.pandas()

    tranco_ranks = download_and_load_tranco_list()

    df_github = process_and_enrich_file(GITHUB_PROCESSED_FILE, tranco_ranks)
    df_reddit = process_and_enrich_file(REDDIT_PROCESSED_FILE, tranco_ranks)
    df_google = process_and_enrich_file(GOOGLE_PROCESSED_FILE, tranco_ranks)
    
    print("Aggregating all datasets...")
    all_dfs = [df for df in [df_github, df_reddit, df_google] if df is not None]
    
    if not all_dfs:
        print("No data found to aggregate. Exiting.")
        exit()
        
    master_df = pd.concat(all_dfs, ignore_index=True)
    print(f"   -> Master dataset created with {len(master_df):,} total entries.")

    # Standardize to the essential columns for the final report
    final_columns = [
        'platform', 'source_url', 'link_text', 
        'extracted_url', 'fqdn', 'domain_tranco_rank'
    ]
    
    # Select only the columns that exist in the final list, automatically dropping others
    existing_columns = [col for col in final_columns if col in master_df.columns]
    master_df_final = master_df[existing_columns]

    # Sort the final master list: ranked items first (ascending), then unranked items at the bottom
    master_df_final['sort_rank'] = master_df_final['domain_tranco_rank'].apply(lambda x: 10_000_001 if x == -1 else x)
    master_df_final = master_df_final.sort_values(by=['sort_rank', 'fqdn'], ascending=[True, True])
    master_df_final = master_df_final.drop(columns=['sort_rank'])

    # Save the final master file
    master_df_final.to_csv(FINAL_OUTPUT_FILE, index=False)
    
    print("\n--- Aggregation and Ranking Complete ---")
    print(f"✅ Final master dataset saved to: '{FINAL_OUTPUT_FILE}'")
    print(f"This file contains {len(master_df_final):,} cleaned, ranked, and aggregated candidates.")