import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FILE = "local_ai_simple.csv"
BLOCKLIST_FILE = "blocklist_local.txt"
OUTPUT_FILE = "local_ai_final_cleaned.csv"

def load_blocklist(filepath):
    """
    Loads blocklist, ignoring comments (#) and empty lines.
    Returns a set for O(1) exact matching.
    """
    if not os.path.exists(filepath):
        print(f"❌ Error: Blocklist '{filepath}' not found.")
        return None
        
    blockset = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            blockset.add(line.lower())
            
    return blockset

def main():
    print(f"--- 🧹 LOCAL AI: EXACT MATCH CLEANER & DEDUPLICATOR ---")

    # 1. Load Blocklist
    print(f"\n1️⃣  Loading Blocklist ({BLOCKLIST_FILE})...")
    blocklist = load_blocklist(BLOCKLIST_FILE)
    if blocklist is None: return
    print(f"   ✅ Loaded {len(blocklist)} domains to block.")

    # 2. Load CSV
    print(f"\n2️⃣  Loading Input CSV ({INPUT_FILE})...")
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file not found.")
        return
        
    df = pd.read_csv(INPUT_FILE)
    initial_count = len(df)
    print(f"   ✅ Loaded {initial_count:,} rows.")

    # 3. Filter (Blocklist)
    print(f"\n3️⃣  Applying Exact Match Filter...")
    
    if 'fqdn' not in df.columns:
        print("❌ Error: 'fqdn' column missing.")
        return

    # Create a mask: True if FQDN is in blocklist
    mask = df['fqdn'].str.lower().isin(blocklist)
    
    df_clean = df[~mask].copy()
    df_removed = df[mask]
    
    removed_count = len(df_removed)
    print(f"   -> Blocked {removed_count:,} noise domains.")

    # 4. Sort & Deduplicate (Group by FQDN)
    print(f"\n4️⃣  Sorting and Deduplicating by FQDN...")
    
    # Helper to handle -1 ranks (treat them as infinity so they go to the bottom)
    df_clean['sort_rank'] = df_clean['tranco_rank'].apply(lambda x: float('inf') if x <= 0 else x)
    
    # Sort: Best Rank (1) -> Worst Rank -> Unranked (inf)
    df_sorted = df_clean.sort_values(by=['sort_rank', 'tool_name'], ascending=[True, True])
    
    # Deduplicate: Keep only one entry per FQDN (the one with the best rank/position)
    df_final = df_sorted.drop_duplicates(subset=['fqdn'], keep='first').copy()
    
    # Drop temp column
    df_final = df_final.drop(columns=['sort_rank'])
    
    dedupe_removed = len(df_clean) - len(df_final)
    print(f"   -> Merged {dedupe_removed:,} duplicate FQDN entries.")

    # 5. Save
    print(f"\n5️⃣  Saving Results...")
    df_final.to_csv(OUTPUT_FILE, index=False)
    
    # 6. Stats
    print(f"\n📊 --- FINAL STATS ---")
    print(f"   Initial Rows:      {initial_count:,}")
    print(f"   Blocked (Noise):   {removed_count:,}")
    print(f"   Deduped (FQDN):    {dedupe_removed:,}")
    print(f"   ---------------------------")
    print(f"   Final Rows:        {len(df_final):,}")
    print(f"   💾 Saved to:       {OUTPUT_FILE}")

    if removed_count > 0:
        print("\n   🗑️  Top 5 Blocked Domains:")
        print(df_removed['fqdn'].value_counts().head(5).to_string())

if __name__ == "__main__":
    main()