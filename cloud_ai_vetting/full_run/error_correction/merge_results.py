#!/usr/bin/env python3
"""
Merge the original final_cloud_ai_web_integrable.csv with error_correction_integrable.csv.
Deduplicates by domain and sorts by median tranco rank.

Usage:
    python merge_results.py
"""

import pandas as pd
import os


def main():
    print("--- 🔗 MERGING FINAL CSVs ---")
    
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    
    original_csv = os.path.join(parent_dir, "final_cloud_ai_web_integrable.csv")
    error_correction_csv = os.path.join(script_dir, "error_correction_integrable.csv")
    output_csv = os.path.join(parent_dir, "final_cloud_ai_web_integrable_merged.csv")
    
    # Load both CSVs
    print(f"Loading original: {original_csv}")
    df_original = pd.read_csv(original_csv)
    print(f"   ✅ {len(df_original):,} entries")
    
    print(f"Loading error correction: {error_correction_csv}")
    df_error = pd.read_csv(error_correction_csv)
    print(f"   ✅ {len(df_error):,} entries")
    
    # Merge (concatenate)
    df_merged = pd.concat([df_original, df_error], ignore_index=True)
    print(f"\nCombined: {len(df_merged):,} entries")
    
    # Deduplicate by URL (keep first occurrence)
    url_col = None
    for col in df_merged.columns:
        if 'url' in col.lower():
            url_col = col
            break
    
    if url_col:
        before_dedup = len(df_merged)
        df_merged = df_merged.drop_duplicates(subset=[url_col], keep='first')
        print(f"After deduplication by {url_col}: {len(df_merged):,} entries (removed {before_dedup - len(df_merged)} duplicates)")
    
    # Sort by median tranco rank
    rank_col = None
    for col in df_merged.columns:
        if 'median' in col.lower() and 'tranco' in col.lower():
            rank_col = col
            break
    
    if rank_col:
        df_merged[rank_col] = pd.to_numeric(df_merged[rank_col], errors='coerce')
        df_merged = df_merged.sort_values(by=rank_col, ascending=True).reset_index(drop=True)
        print(f"Sorted by: {rank_col}")
    else:
        print("⚠️ No median tranco rank column found, keeping original order")
    
    # Save
    df_merged.to_csv(output_csv, index=False)
    print(f"\n✅ Saved merged file to: {output_csv}")
    print(f"   Total entries: {len(df_merged):,}")


if __name__ == "__main__":
    main()
