# analyze_master_list.py
"""
An exploratory data analysis (EDA) script for the final aggregated dataset.

This script loads the 'master_ai_services_list.csv' and provides key insights
to help understand the collected data, including:
1.  An overall summary of the data size.
2.  A check for any remaining duplicate URLs.
3.  An analysis of Tranco ranks (ranked vs. unranked statistics).
4.  A list of the highest-ranked (most popular) domains found.
5.  A list of the most frequently discovered domains in the dataset.
6.  A breakdown of how many links were contributed by each platform.

Requirements:
  pip install pandas

Usage:
  - Ensure 'master_ai_services_list.csv' is in the same directory.
  - Run the script: python analyze_master_list.py
"""

import pandas as pd
from pathlib import Path

# --- CONFIGURATION ---
MASTER_FILE = Path("master_ai_services_list.csv")

if __name__ == "__main__":
    if not MASTER_FILE.exists():
        print(f"ERROR: Master file not found at '{MASTER_FILE}'. Please run the aggregation script first.")
        exit()

    print(f"--- Analyzing Final Dataset: {MASTER_FILE} ---")

    # Load the master dataset
    df = pd.read_csv(MASTER_FILE)

    # --- 1. Initial Data Overview ---
    print("\n--- Initial Data Overview ---")
    total_entries = len(df)
    print(f"Total candidate links in the master list: {total_entries:,}")

    # --- 2. Duplicate Analysis ---
    print("\n--- Duplicate URL Analysis ---")
    unique_urls = df['extracted_url'].nunique()
    duplicate_count = total_entries - unique_urls
    print(f"Total unique URLs found across all platforms: {unique_urls:,}")
    if duplicate_count > 0:
        print(f"NOTE: Found {duplicate_count:,} duplicate URLs. This means the same URL was discovered via different platforms or search queries.")
    else:
        print("Excellent! No duplicate URLs found in the final dataset.")

    # Let's work with a deduplicated version for further analysis
    df_unique = df.drop_duplicates(subset=['extracted_url'], keep='first').copy()


    # --- 3. Tranco Rank Analysis ---
    print("\n--- Tranco Rank Analysis ---")
    unranked_count = len(df_unique[df_unique['domain_tranco_rank'] == -1])
    ranked_count = len(df_unique[df_unique['domain_tranco_rank'] != -1])
    
    if total_entries > 0:
        unranked_percentage = (unranked_count / len(df_unique)) * 100
        print(f"Unranked Domains (not in Tranco Top 1M): {unranked_count:,} ({unranked_percentage:.2f}%)")
        print(f"Ranked Domains (in Tranco Top 1M):     {ranked_count:,}")
    else:
        print("No data to analyze.")

    # --- 4. Top-Ranked Domains (Highest Popularity) ---
    print("\n--- Top 15 Highest-Ranked Domains Found (Most Popular Overall) ---")
    # Filter for ranked domains, sort by rank, then drop duplicates to show each domain once
    top_ranked = df_unique[df_unique['domain_tranco_rank'] != -1].sort_values('domain_tranco_rank').drop_duplicates(subset=['fqdn'])
    print(top_ranked[['fqdn', 'domain_tranco_rank']].head(15).to_string(index=False))

    # --- 5. Most Frequently Discovered Domains ---
    print("\n--- Top 15 Most Frequently Discovered Domains (Most Relevant to Our Search) ---")
    print(df_unique['fqdn'].value_counts().head(15).to_string())

    # --- 6. Platform Contribution Analysis ---
    print("\n--- Contribution by Platform ---")
    # Use the original dataframe (with duplicates) to see the total contribution
    print(df['platform'].value_counts().to_string())

    print("\n--- Analysis Complete ---")