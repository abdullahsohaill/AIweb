#!/usr/bin/env python3
"""
Extract top 100 entries by rank for manual vetting.
Outputs: tool name, URL, domain, and rank columns.

Usage:
    python extract_top100_for_vetting.py
"""

import pandas as pd
import os


def main():
    print("--- 🔝 EXTRACTING TOP 100 FOR VETTING ---")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "final_cloudAI.csv")
    output_csv = os.path.join(script_dir, "top100_for_vetting.csv")
    
    if not os.path.exists(input_csv):
        print(f"❌ Input file not found: {input_csv}")
        return
    
    # Load CSV
    df = pd.read_csv(input_csv)
    print(f"✅ Loaded {len(df):,} entries")
    
    # Find relevant columns (case-insensitive matching)
    col_mapping = {
        'tool_name': None,
        'url': None,
        'domain': None,
        'rank': None
    }
    
    for col in df.columns:
        col_lower = col.lower()
        if 'tool' in col_lower and 'name' in col_lower:
            col_mapping['tool_name'] = col
        elif 'url' in col_lower and col_mapping['url'] is None:
            col_mapping['url'] = col
        elif 'domain' in col_lower and 'fqdn' in col_lower:
            col_mapping['domain'] = col
        elif 'median' in col_lower and 'tranco' in col_lower:
            col_mapping['rank'] = col
    
    print(f"\nDetected columns:")
    for key, val in col_mapping.items():
        print(f"   {key}: {val}")
    
    # Ensure rank column exists for sorting
    if col_mapping['rank'] is None:
        print("❌ Could not find rank column!")
        return
    
    # Sort by rank (ascending = best rank first)
    df[col_mapping['rank']] = pd.to_numeric(df[col_mapping['rank']], errors='coerce')
    df_sorted = df.sort_values(by=col_mapping['rank'], ascending=True)
    
    # Take top 100
    df_top100 = df_sorted.head(100)
    
    # Select only the relevant columns
    cols_to_keep = [v for v in col_mapping.values() if v is not None]
    df_output = df_top100[cols_to_keep].copy()
    
    # Save
    df_output.to_csv(output_csv, index=False)
    
    print(f"\n✅ Saved top 100 entries to: {output_csv}")
    print(f"   Columns: {cols_to_keep}")
    
    # Preview
    print(f"\n📋 Preview (first 5):")
    print(df_output.head().to_string(index=False))


if __name__ == "__main__":
    main()
