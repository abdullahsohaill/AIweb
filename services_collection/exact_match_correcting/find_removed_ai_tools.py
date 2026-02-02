#!/usr/bin/env python3
"""
Find Removed AI Tools Script

Extracts entries from final_tools_1M.csv that matched the blocklist.
Output has the exact same structure as the original CSV.

Usage:
    python find_removed_ai_tools.py
"""

import pandas as pd
import os
import sys


def main():
    print("🔍 Finding removed entries...")
    
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    
    input_csv = os.path.join(parent_dir, "final_tools_1M.csv")
    blocklist_txt = os.path.join(script_dir, "exact_match_blocklist_deduplicated.txt")
    output_csv = os.path.join(script_dir, "removed_entries_review.csv")
    
    # Load blocklist
    if not os.path.exists(blocklist_txt):
        print(f"❌ Blocklist not found: {blocklist_txt}")
        sys.exit(1)
    
    with open(blocklist_txt, 'r', encoding='utf-8') as f:
        blocklist_set = {line.strip().lower() for line in f if line.strip()}
    
    print(f"✅ Loaded {len(blocklist_set):,} blocklist entries")
    
    # Load original CSV
    if not os.path.exists(input_csv):
        print(f"❌ Input not found: {input_csv}")
        sys.exit(1)
    
    df = pd.read_csv(input_csv)
    print(f"✅ Loaded {len(df):,} entries from original CSV")
    
    # Find removed entries (domains that are IN the blocklist)
    domain_col = "Domain (FQDN)"
    removed_df = df[df[domain_col].str.lower().isin(blocklist_set)]
    
    print(f"✅ Found {len(removed_df):,} removed entries")
    
    # Save with exact same structure
    removed_df.to_csv(output_csv, index=False)
    
    print(f"✅ Saved to: {output_csv}")


if __name__ == "__main__":
    main()
