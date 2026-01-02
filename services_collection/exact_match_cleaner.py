import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_CSV = "final_tools_1M.csv"
BLOCKLIST_TXT = "exact_match_blocklist.txt"
OUTPUT_CSV = "final_tools_1M_cleaned.csv"

def load_blocklist(filepath):
    """Loads a text file of domains into a set for fast lookups."""
    if not os.path.exists(filepath):
        print(f"   ❌ Blocklist file not found at '{filepath}'")
        return None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        # Use a set for O(1) lookup speed, stripping whitespace and ignoring empty lines
        blocklist = {line.strip().lower() for line in f if line.strip()}
        
    return blocklist

def main():
    print("--- 🔬 EXACT-MATCH DOMAIN CLEANER ---")

    # --- 1. LOAD BLOCKLIST ---
    print(f"\n1️⃣  Loading blocklist from '{BLOCKLIST_TXT}'...")
    blocklist_set = load_blocklist(BLOCKLIST_TXT)
    
    if blocklist_set is None:
        return # Stop if blocklist file is missing
        
    print(f"   ✅ Loaded {len(blocklist_set):,} unique domains to block.")

    # --- 2. LOAD DATASET ---
    if not os.path.exists(INPUT_CSV):
        print(f"\n❌ Error: Input file '{INPUT_CSV}' not found. Please ensure it is in the 'services_collection' directory.")
        return

    print(f"\n2️⃣  Loading dataset from '{INPUT_CSV}'...")
    df = pd.read_csv(INPUT_CSV)
    initial_count = len(df)
    print(f"   ✅ Initial entries: {initial_count:,}")

    # --- 3. APPLY EXACT-MATCH FILTER ---
    print("\n3️⃣  Applying exact-match filter...")
    
    # The column name from the previous script is "Domain (FQDN)"
    domain_col = "Domain (FQDN)"
    if domain_col not in df.columns:
        print(f"❌ Error: Column '{domain_col}' not found in the CSV!")
        return

    # The .isin() method performs an exact match for each item in the set.
    # The `~` inverts the selection, keeping only the rows that are NOT in the blocklist.
    cleaned_df = df[~df[domain_col].str.lower().isin(blocklist_set)].copy()

    # --- 4. CALCULATE AND DISPLAY STATS ---
    final_count = len(cleaned_df)
    removed_count = initial_count - final_count

    print("\n📊 --- CLEANUP STATISTICS ---")
    print(f"   Initial Entries:          {initial_count:,}")
    print(f"   Unique Domains in List:   {len(blocklist_set):,}")
    print(f"   Entries Removed:          {removed_count:,}")
    print(f"   ------------------------------------")
    print(f"   Final Entries Remaining:  {final_count:,}")

    # --- 5. SAVE FINAL CSV ---
    print(f"\n💾 Saving cleaned data to '{OUTPUT_CSV}'...")
    cleaned_df.to_csv(OUTPUT_CSV, index=False)
    print("   ✅ Done.")

if __name__ == "__main__":
    main()