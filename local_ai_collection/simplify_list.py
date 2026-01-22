import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FILE = "local_ai_master_ranked.csv"
OUTPUT_FILE = "local_ai_simple.csv"

def main():
    print(f"--- ✂️ SIMPLIFYING CSV ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file '{INPUT_FILE}' not found.")
        return

    # 1. Load Data
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"   ✅ Loaded {len(df):,} rows.")
    except Exception as e:
        print(f"   ❌ Error reading CSV: {e}")
        return

    # 2. Select & Rename Columns
    # The aggregator saved them as: tool_name, url, fqdn, tranco_rank
    # We rename 'url' -> 'extracted_url' to match your request
    try:
        df_simple = df[["tool_name", "url", "fqdn", "tranco_rank"]].copy()
        df_simple = df_simple.rename(columns={"url": "extracted_url"})
        
        # 3. Save
        df_simple.to_csv(OUTPUT_FILE, index=False)
        print(f"   💾 Saved simplified list to: {OUTPUT_FILE}")
        
        # Preview
        print("\n   First 3 rows:")
        print(df_simple.head(3).to_string(index=False))
        
    except KeyError as e:
        print(f"   ❌ Column missing in input file: {e}")
        print(f"   Available columns: {list(df.columns)}")

if __name__ == "__main__":
    main()