import pandas as pd
import os
import tldextract
from tqdm import tqdm
from urllib.parse import urlparse, urlunparse

# --- CONFIGURATION ---
# Input Files (Relative paths based on your execution)
FILE_GOOGLE = "google/local_ai_google_processed_links.csv"
FILE_REDDIT = "reddit/reddit_output/local_ai_reddit_processed_links.csv"
FILE_GITHUB = "github/github_output/local_ai_github_processed_links.csv"

# Tranco List (Pointing to the one in services_collection)
TRANCO_FILE = "../services_collection/Tranco/tranco_temporal_intersection_master.csv"

# Output Files
OUTPUT_FILENAME = "local_ai_master_ranked.csv"

# --- HELPER FUNCTIONS ---
def clean_url(url):
    """Removes query parameters and fragments."""
    try:
        if not isinstance(url, str): return ""
        parsed = urlparse(url)
        cleaned = urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))
        return cleaned.strip().rstrip('/')
    except:
        return url

def get_domain_parts(fqdn):
    """Extracts domain parts for 3-stage ranking."""
    try:
        if not isinstance(fqdn, str): return {}
        ext = tldextract.extract(fqdn)
        parts = {
            'fqdn': fqdn.lower(),
            'etld_p_2': f"{ext.subdomain}.{ext.registered_domain}".lower() if ext.subdomain else None,
            'etld_p_1': ext.registered_domain.lower() if ext.registered_domain else None
        }
        return parts
    except:
        return {}

def get_smart_rank(row, tranco_map):
    """3-stage lookup: FQDN -> eTLD+2 -> eTLD+1."""
    domain_parts = get_domain_parts(str(row['fqdn']))
    
    if domain_parts.get('fqdn') and domain_parts['fqdn'] in tranco_map:
        return tranco_map[domain_parts['fqdn']]
    
    if domain_parts.get('etld_p_2') and domain_parts['etld_p_2'] in tranco_map:
        return tranco_map[domain_parts['etld_p_2']]

    if domain_parts.get('etld_p_1') and domain_parts['etld_p_1'] in tranco_map:
        return tranco_map[domain_parts['etld_p_1']]
        
    return -1

def main():
    print("--- 🧬 LOCAL AI: MERGE, RANK & FILTER ---")

    # --- 1. LOAD SOURCES ---
    print("\n1️⃣  Loading Source Files...")
    dfs = []
    for fpath in [FILE_GOOGLE, FILE_REDDIT, FILE_GITHUB]:
        if os.path.exists(fpath):
            try:
                df = pd.read_csv(fpath)
                # Standardize column names if needed, though process_*.py scripts should have unified them
                # We expect: platform, search_phrase, source_url, link_text, extracted_url, fqdn
                dfs.append(df)
                print(f"   ✅ Loaded {fpath}: {len(df)} rows")
            except Exception as e:
                print(f"   ❌ Error loading {fpath}: {e}")
        else:
            print(f"   ⚠️ File not found: {fpath}")
    
    if not dfs:
        print("No data found.")
        return

    # --- 2. MERGE & CLEAN ---
    print("\n2️⃣  Merging and Cleaning...")
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Rename for consistency
    merged_df.rename(columns={'extracted_url': 'url', 'link_text': 'tool_name'}, inplace=True)
    
    # Clean URLs
    merged_df['url'] = merged_df['url'].apply(clean_url)
    
    # Deduplicate
    deduplicated_df = merged_df.drop_duplicates(subset=['url'], keep='first').copy()
    print(f"   -> Total Unique Local AI Tools: {len(deduplicated_df):,}")

    # --- 3. RANKING ---
    print(f"\n3️⃣  Loading Tranco Ranker...")
    try:
        tranco_df = pd.read_csv(TRANCO_FILE, usecols=["domain", "median_rank"], dtype={"domain": "string", "median_rank": "int32"})
        tranco_map = pd.Series(tranco_df.median_rank.values, index=tranco_df.domain.str.lower()).to_dict()
        del tranco_df
        print(f"   ✅ Tranco Map Ready.")
    except Exception as e:
        print(f"   ❌ Error loading Tranco: {e}")
        return

    print("\n4️⃣  Applying Smart Ranking...")
    tqdm.pandas(desc="   -> Ranking")
    deduplicated_df["tranco_rank"] = deduplicated_df.progress_apply(lambda row: get_smart_rank(row, tranco_map), axis=1)

    # --- 5. SORT & SAVE ---
    print("\n5️⃣  Saving...")
    # Separate Ranked vs Unranked for sorting
    ranked = deduplicated_df[deduplicated_df['tranco_rank'] != -1].sort_values('tranco_rank')
    unranked = deduplicated_df[deduplicated_df['tranco_rank'] == -1]
    
    final_df = pd.concat([ranked, unranked])
    
    final_df.to_csv(OUTPUT_FILENAME, index=False)
    
    print(f"   📊 Ranked Tools:   {len(ranked):,}")
    print(f"   📊 Unranked Tools: {len(unranked):,}")
    print(f"   💾 Saved to: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()