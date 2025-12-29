# extract_unique_fqdns.py
"""
This script reads the master_ai_services_list.csv file, extracts all unique
values from the 'fqdn' column, sorts them alphabetically, and saves them
to a new single-column CSV file named 'fqdns.csv'.

Requirements:
  pip install pandas

Usage:
  - Ensure 'master_ai_services_list.csv' is in the same directory.
  - Run the script: python extract_unique_fqdns.py
"""

import pandas as pd
from pathlib import Path

# --- CONFIGURATION ---
MASTER_FILE = Path("final_services_cleaned.csv")
OUTPUT_FILE = Path("fqdns.csv")

if __name__ == "__main__":
    if not MASTER_FILE.exists():
        print(f"ERROR: Master file not found at '{MASTER_FILE}'. Please run the aggregation script first.")
        exit()

    print(f"--- Extracting Unique FQDNs from {MASTER_FILE} ---")

    # 1. Load the master dataset
    print("Loading master dataset...")
    df = pd.read_csv(MASTER_FILE)

    # 2. Get all unique, non-empty FQDNs
    print("Finding unique FQDNs...")
    unique_fqdns = df['fqdn'].dropna().unique()
    
    # 3. Create a new DataFrame from the unique FQDNs
    fqdn_df = pd.DataFrame(unique_fqdns, columns=['fqdn'])
    
    # 4. Sort the DataFrame alphabetically
    fqdn_df_sorted = fqdn_df.sort_values(by='fqdn', ascending=True)

    # 5. Save the sorted, unique FQDNs to a new CSV file
    print(f"Found {len(fqdn_df_sorted):,} unique FQDNs. Saving to {OUTPUT_FILE}...")
    fqdn_df_sorted.to_csv(OUTPUT_FILE, index=False)

    print("\n--- Process Complete ---")
    print(f"✅ Successfully saved all unique FQDNs to '{OUTPUT_FILE}'.")