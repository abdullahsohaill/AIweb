import pandas as pd
import os
import tldextract
from tqdm import tqdm

# --- CONFIGURATION ---
# Input Files
FILE_1 = "DEDUPLICATED_AI_TOOLS_MASTER.csv"
# This now correctly points to the file you created
FILE_2 = "final_services.csv"
# CORRECTED: Pointing to the new Temporal Intersection Master
TRANCO_FILE = "Tranco/tranco_temporal_intersection_master.csv"

# Output Files
OUTPUT_FILENAME = "final_tools.csv"
# New conditional output file
OUTPUT_1M_FILENAME = "final_tools_1M.csv"

# --- HELPER FUNCTIONS ---
def get_domain_parts(fqdn):
    """
    Extracts multiple parts of the domain for staged ranking.
    Returns a dictionary with fqdn, etld_p_2, and etld_p_1.
    """
    try:
        if not isinstance(fqdn, str): return {}
        ext = tldextract.extract(fqdn)
        # e.g., for 'app.deel.com':
        # fqdn: 'app.deel.com'
        # etld+2: 'app.deel.com' (if subdomain exists)
        # etld+1: 'deel.com'
        
        parts = {
            'fqdn': fqdn.lower(),
            'etld_p_2': f"{ext.subdomain}.{ext.registered_domain}".lower() if ext.subdomain else None,
            'etld_p_1': ext.registered_domain.lower() if ext.registered_domain else None
        }
        return parts
    except:
        return {}

def get_smart_rank(row, tranco_map):
    """
    Tries to find a rank using a 3-stage lookup: FQDN -> eTLD+2 -> eTLD+1.
    Returns -1 if none are found.
    """
    domain_parts = get_domain_parts(str(row['fqdn']))
    
    # 1. Try Exact Match (FQDN)
    if domain_parts.get('fqdn') and domain_parts['fqdn'] in tranco_map:
        return tranco_map[domain_parts['fqdn']]
    
    # 2. Try eTLD+2 (e.g., 'app.deel.com')
    if domain_parts.get('etld_p_2') and domain_parts['etld_p_2'] in tranco_map:
        return tranco_map[domain_parts['etld_p_2']]

    # 3. Try Root Domain / eTLD+1 (e.g., 'deel.com')
    if domain_parts.get('etld_p_1') and domain_parts['etld_p_1'] in tranco_map:
        return tranco_map[domain_parts['etld_p_1']]
        
    return -1

def print_rank_breakdown(df, col_name="tranco_rank"):
    """Prints granular statistics about the rankings."""
    total = len(df)
    if total == 0:
        print("   No data to analyze.")
        return 0 # Return 0 for the count

    # Filter only ranked items (rank != -1)
    ranked = df[df[col_name] != -1]
    
    # Defined buckets
    top_1m = len(ranked[ranked[col_name] <= 1_000_000])
    top_5m = len(ranked[ranked[col_name] <= 5_000_000])
    top_10m = len(ranked[ranked[col_name] <= 10_000_000])
    over_10m = len(ranked[ranked[col_name] > 10_000_000])
    
    print("\n   📊 Ranking Breakdown (Cumulative):")
    print(f"      - Top 1 Million:      {top_1m:,} ({top_1m/total:.1%})")
    print(f"      - Top 5 Million:      {top_5m:,} ({top_5m/total:.1%})")
    print(f"      - Top 10 Million:     {top_10m:,} ({top_10m/total:.1%})")
    print(f"      - Long Tail (>10M):   {over_10m:,} ({over_10m/total:.1%})")
    
    return top_1m # Return the count for the conditional save

# --- MAIN SCRIPT ---
def main():
    print("--- 🧬 MERGE, 3-STAGE RANK, & FILTER ---")

    # --- 1. LOAD AI TOOLS ---
    print("\n1️⃣  Loading Tool Lists...")
    try:
        # Load File 1 (Marketplaces)
        df1 = pd.read_csv(FILE_1)
        df1_std = df1.rename(columns={"original_url": "url"})[["tool_name", "url", "fqdn"]]
        
        # Load File 2 (Crawlers)
        df2 = pd.read_csv(FILE_2)
        df2_std = df2.rename(columns={"link_text": "tool_name", "extracted_url": "url"})[["tool_name", "url", "fqdn"]]
        
        print(f"   ✅ Tools loaded: {len(df1_std) + len(df2_std):,}")
    except Exception as e:
        print(f"   ❌ Error loading tools: {e}")
        return

    # --- 2. MERGE & CLEAN ---
    print("\n2️⃣  Merging and Cleaning...")
    
    # Merge
    merged_df = pd.concat([df1_std, df2_std], ignore_index=True)
    
    # Filter "Unknown" / Generic names
    generic_terms = ['unknown', 'link', 'website', 'here', 'click here', 'source', 'home']
    merged_df = merged_df[~merged_df['tool_name'].astype(str).str.lower().isin(generic_terms)]
    merged_df = merged_df.dropna(subset=['tool_name', 'url'])
    
    # Deduplicate by URL
    deduplicated_df = merged_df.drop_duplicates(subset=['url'], keep='first').copy()
    
    count_unique = len(deduplicated_df)
    print(f"   -> Unique URLs to rank: {count_unique:,}")

    # --- 3. LOAD TRANCO (Memory Optimized) ---
    print(f"\n3️⃣  Loading Tranco Master List ({TRANCO_FILE})...")
    
    try:
        # Load only necessary columns from the NEW Temporal Master
        tranco_df = pd.read_csv(
            TRANCO_FILE, 
            usecols=["domain", "median_rank"],
            dtype={"domain": "string", "median_rank": "int32"}
        )
        
        # Create dictionary for O(1) lookups: domain -> median_rank
        tranco_map = pd.Series(
            tranco_df.median_rank.values, 
            index=tranco_df.domain.str.lower()
        ).to_dict()
        
        del tranco_df # Free memory
        print(f"   ✅ Tranco Lookup Map Ready ({len(tranco_map):,} domains)")

    except Exception as e:
        print(f"   ❌ Error loading Tranco: {e}")
        return

    # --- 4. RANKING (The 3-Stage Smart Logic) ---
    print("\n4️⃣  Applying 3-Stage Smart Ranking (FQDN -> eTLD+2 -> eTLD+1)...")
    tqdm.pandas(desc="   -> Ranking")
    
    # Apply the smart ranking function
    deduplicated_df["tranco_rank"] = deduplicated_df.progress_apply(
        lambda row: get_smart_rank(row, tranco_map), axis=1
    )

    # --- 5. STATS & FINAL FILTERING ---
    print("\n5️⃣  Calculating Stats & Filtering...")
    
    total_tools = len(deduplicated_df)
    ranked_df = deduplicated_df[deduplicated_df["tranco_rank"] != -1].copy()
    unranked_df = deduplicated_df[deduplicated_df["tranco_rank"] == -1].copy()
    
    ranked_count = len(ranked_df)
    unranked_count = len(unranked_df)
    
    print("\n📊 --- DATASET STATISTICS (Before Saving) ---")
    print(f"   Total Candidates:     {total_tools:,}")
    print(f"   ✅ Ranked (Kept):     {ranked_count:,} ({(ranked_count/total_tools)*100:.1f}%)")
    print(f"   ❌ Unranked (Cut):    {unranked_count:,} ({(unranked_count/total_tools)*100:.1f}%)")
    
    # Print detailed breakdown and get the Top 1M count
    top_1m_count = print_rank_breakdown(ranked_df, col_name="tranco_rank")

    # --- 6. FINAL SORT & SAVE ---
    print(f"\n6️⃣  Saving RANKED ONLY to '{OUTPUT_FILENAME}'...")
    
    # Sort by Rank (Ascending) -> Then FQDN
    ranked_df = ranked_df.sort_values(by=['tranco_rank', 'fqdn'], ascending=[True, True])
    
    # Rename columns for clarity
    final_ranked_df = ranked_df.rename(columns={
        "tool_name": "Tool Name",
        "url": "Extracted URL",
        "fqdn": "Domain (FQDN)",
        "tranco_rank": "Median Tranco Rank"
    })
    
    final_ranked_df.to_csv(OUTPUT_FILENAME, index=False)
    print(f"   💾 Saved {len(final_ranked_df):,} rows to {OUTPUT_FILENAME}")

    # --- 7. NEW: CONDITIONAL SAVE for TOP 1M ---
    if top_1m_count > 30000:
        print(f"\n⭐ Found {top_1m_count:,} tools in Top 1M (exceeds 30k threshold).")
        print(f"   -> Saving a separate file: '{OUTPUT_1M_FILENAME}'...")
        
        # Filter the final dataframe for top 1M ranks
        top_1m_df = final_ranked_df[final_ranked_df["Median Tranco Rank"] <= 1_000_000].copy()
        
        top_1m_df.to_csv(OUTPUT_1M_FILENAME, index=False)
        print(f"   💾 Saved {len(top_1m_df):,} rows to {OUTPUT_1M_FILENAME}")

if __name__ == "__main__":
    main()