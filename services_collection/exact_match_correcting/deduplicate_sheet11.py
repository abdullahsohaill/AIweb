#!/usr/bin/env python3
"""
Deduplicate sheet11.csv by FQDN, keeping one entry per domain.
Outputs sorted list with same structure.

Usage:
    python deduplicate_sheet11.py
"""

import pandas as pd
import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "sheet11.csv")
    output_csv = os.path.join(script_dir, "sheet11_deduplicated.csv")
    
    # Load CSV
    df = pd.read_csv(input_csv)
    print(f"✅ Loaded {len(df):,} entries")
    
    # Deduplicate by FQDN (keep first occurrence, preserve original order)
    domain_col = "Domain (FQDN)"
    df_dedup = df.drop_duplicates(subset=[domain_col], keep='first')
    
    print(f"✅ Unique entries: {len(df_dedup):,}")
    print(f"✅ Removed {len(df) - len(df_dedup):,} duplicates")
    
    # Save (preserves original median tranco rank sort order)
    df_dedup.to_csv(output_csv, index=False)
    print(f"✅ Saved to: {output_csv}")


if __name__ == "__main__":
    main()
