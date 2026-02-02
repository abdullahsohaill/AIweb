#!/usr/bin/env python3
"""
Extract all entries from top 100 FQDNs (by rank) for manual vetting.
Outputs: tool name, URL, domain, and rank columns.

Usage:
    python extract_top100_for_vetting.py
"""

import pandas as pd
import os


def main():
    print("--- 🔝 EXTRACTING TOP 100 FQDNs FOR VETTING ---")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "final_cloudAI.csv")
    output_csv = os.path.join(script_dir, "top100_fqdns_for_vetting.csv")
    
    if not os.path.exists(input_csv):
        print(f"❌ Input file not found: {input_csv}")
        return
    
    # Load CSV
    df = pd.read_csv(input_csv)
    print(f"✅ Loaded {len(df):,} entries")
    
    # Find relevant columns
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
    
    domain_col = col_mapping['domain']
    rank_col = col_mapping['rank']
    
    if domain_col is None or rank_col is None:
        print("❌ Could not find required columns!")
        return
    
    # Exclude huggingface.co and github.io
    df = df[~df[domain_col].str.lower().str.contains('huggingface.co', na=False)]
    df = df[~df[domain_col].str.lower().str.endswith('github.io', na=False)]
    print(f"\nAfter excluding huggingface.co and github.io: {len(df):,} entries")
    
    # Convert rank to numeric
    df[rank_col] = pd.to_numeric(df[rank_col], errors='coerce')
    
    # Get unique FQDNs with their best (lowest) rank
    fqdn_ranks = df.groupby(domain_col)[rank_col].min().reset_index()
    fqdn_ranks = fqdn_ranks.sort_values(by=rank_col, ascending=True)
    
    # Take top 100 FQDNs
    top_100_fqdns = fqdn_ranks.head(100)[domain_col].tolist()
    print(f"Top 100 unique FQDNs selected")
    
    # Filter to include ALL entries from those 100 FQDNs
    df_filtered = df[df[domain_col].isin(top_100_fqdns)]
    
    # Sort by rank
    df_filtered = df_filtered.sort_values(by=rank_col, ascending=True)
    
    # Select only the relevant columns
    cols_to_keep = [v for v in col_mapping.values() if v is not None]
    df_output = df_filtered[cols_to_keep].copy()
    
    # Save
    df_output.to_csv(output_csv, index=False)
    
    print(f"\n✅ Saved to: {output_csv}")
    print(f"   Unique FQDNs: 100")
    print(f"   Total entries: {len(df_output):,}")
    
    # Preview
    print(f"\n📋 Preview (first 10):")
    print(df_output.head(10).to_string(index=False))


if __name__ == "__main__":
    main()

