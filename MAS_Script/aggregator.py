import pandas as pd
import os
from urllib.parse import urlparse

# --- CONFIGURATION ---
TRANCO_FILE = "tranco_9WVY2.csv"
OUTPUT_FILENAME = "RANKED_AI_TOOLS_MASTER.csv"

# Combined Source List
# I have merged your previous list with the new requests.
SOURCES = [
    # --- NEW / UPDATED SOURCES (High Priority) ---
    {"folder": "aiagentslist", "file": "aiagentslist_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aiagentsdirectory", "file": "aiagentslist_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoolmall.com", "file": "aitoolmall_repaired.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitools.fyi", "file": "aitoolsfyi_complete.csv", "name_col": "tool_name", "link_col": "clean_website_url"},
    {"folder": "aitools.inc", "file": "aitoolsinc_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoolsdirectory.com", "file": "aitoolsdirectory_complete.csv", "name_col": "tool_name", "link_col": "real_website_url"},
    {"folder": "aixploria.com", "file": "aixploria_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "easywithai.com", "file": "easywithai_repaired.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "findmyaitool", "file": "findmyaitool_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "futurepedia.io", "file": "futurepedia_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "insidr.ai", "file": "insidr_complete.csv", "name_col": "tool_name", "link_col": "real_website_url"},
    {"folder": "marketlaunch.net", "file": "microlaunch_slow_fix.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "opentools.ai", "file": "openfuture_complete.csv", "name_col": "tool_name", "link_col": "final_website_url"}, # Was openfuture.ai
    {"folder": "saasaitools.com", "file": "saasaitools_final_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "siteefy", "file": "siteefy_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "theresanaiforthat", "file": "taaft_final_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "toolify", "file": "toolify_final_enriched.csv", "name_col": "tool_name", "link_col": "external_url"},
    {"folder": "toolkitly.com", "file": "toolkitly_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "toolpilot.ai", "file": "toolpilot_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "tools-ai.online", "file": "toolsai_online_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "topai.tools", "file": "topai_harvest.csv", "name_col": "tool_name", "link_col": "external_link"},

    # --- OLD SOURCES (Kept unique ones) ---
    {"folder": "aitoolguru", "file": "aitoolguru_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoolhouse", "file": "aitoolhouse_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoolnet.com", "file": "aitoolnet_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoptools.com", "file": "aitoptools_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "awesomeaitools.com", "file": "awesomeaitools_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "bai.tools", "file": "baitools_harvest_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "bestofai.com", "file": "bestofai_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "dang.ai", "file": "dang_harvest.csv", "name_col": "tool_name", "link_col": "final_website_url"},
    {"folder": "foundr.ai", "file": "foundr_extracted.csv", "name_col": "tool_name", "link_col": "external_url"},
    {"folder": "futuretools.io", "file": "futuretools_resolved_final.csv", "name_col": "tool_name", "link_col": "real_website_url"},
    {"folder": "goodaitools.com", "file": "goodaitools_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "thataicollection.com", "file": "thataicollection_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "toolio.ai", "file": "toolio_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "toolai.io", "file": "toolai_final_links.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "whattheai.tech", "file": "whattheai_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
]

def get_fqdn(url):
    """
    Extracts the Fully Qualified Domain Name (FQDN).
    Removes http/s, www, paths, and query params.
    Result: 'google.com', 'jasper.ai'
    """
    try:
        if pd.isna(url) or str(url).strip() == "":
            return None
        
        url_str = str(url).strip().lower()
        
        # Add scheme for parser if missing
        if not url_str.startswith("http"):
            url_str = "http://" + url_str
            
        parsed = urlparse(url_str)
        domain = parsed.netloc
        
        # Remove port if present
        if ':' in domain:
            domain = domain.split(':')[0]
            
        # Remove www prefix
        if domain.startswith("www."):
            domain = domain[4:]
            
        return domain if domain else None
    except:
        return None

def load_tranco_map():
    """Loads the Tranco CSV into a dictionary {domain: rank}."""
    print(f"\n⏳ Loading Tranco List ({TRANCO_FILE})...")
    try:
        # Assumes Tranco format is: Rank, Domain (1,google.com)
        tranco_df = pd.read_csv(TRANCO_FILE, header=None, names=["rank", "domain"])
        
        # Normalize domains in the list
        tranco_df['domain'] = tranco_df['domain'].astype(str).str.strip().str.lower()
        
        # Create Dict using bracket notation for 'rank' to avoid conflict with pandas method
        tranco_map = pd.Series(tranco_df['rank'].values, index=tranco_df['domain']).to_dict()
        
        print(f"   ✅ Loaded {len(tranco_map):,} Tranco domains.")
        return tranco_map
        
    except FileNotFoundError:
        print(f"   ❌ Tranco file '{TRANCO_FILE}' not found. Ranking will be skipped (all -1).")
        return {}
    except Exception as e:
        print(f"   ❌ Error loading Tranco: {e}")
        return {}

def main():
    print("--- 🧬 STARTING MASTER AI TOOL AGGREGATION ---")
    
    all_dfs = []
    
    # --- 1. AGGREGATE CSVs ---
    print("\n1️⃣  Aggregating Sources...")
    for source in SOURCES:
        path = os.path.join(source["folder"], source["file"])
        
        if os.path.exists(path):
            try:
                # Read CSV
                df = pd.read_csv(path)
                
                # Verify Columns
                if source["name_col"] not in df.columns or source["link_col"] not in df.columns:
                    print(f"   ⚠️  Skipping {source['folder']}: Columns missing.")
                    continue
                
                # Standardize DataFrame
                temp = df[[source["name_col"], source["link_col"]]].copy()
                temp.columns = ["tool_name", "original_url"]
                temp["source_directory"] = source["folder"]
                
                all_dfs.append(temp)
                # print(f"   ✅ {source['folder']}: Loaded {len(temp)} rows.")
            except Exception as e:
                print(f"   ❌ Error reading {path}: {e}")
        else:
            print(f"   ⚠️  File Not Found: {path}")
            
    if not all_dfs:
        print("No data loaded. Exiting.")
        return

    # Combine into one huge DataFrame
    master_df = pd.concat(all_dfs, ignore_index=True)
    total_raw_rows = len(master_df)
    
    # --- 2. CLEAN & EXTRACT FQDN ---
    print(f"\n2️⃣  Cleaning & Extracting FQDN (Raw Count: {total_raw_rows:,})...")
    
    # Remove empty original URLs
    master_df = master_df.dropna(subset=["original_url"])
    master_df = master_df[master_df["original_url"].astype(str).str.strip() != ""]
    count_after_empty_removal = len(master_df)
    
    # Generate FQDN Column
    master_df["fqdn"] = master_df["original_url"].apply(get_fqdn)
    
    # Remove rows where FQDN extraction failed (e.g. malformed URLs)
    master_df = master_df.dropna(subset=["fqdn"])
    master_df = master_df[master_df["fqdn"] != ""]
    
    # --- 3. DEDUPLICATE ---
    print("\n3️⃣  Deduplicating based on FQDN...")
    # Keep the first occurrence of every FQDN
    unique_df = master_df.drop_duplicates(subset=["fqdn"], keep="first").copy()
    unique_fqdn_count = len(unique_df)
    
    # --- 4. RANKING WITH TRANCO ---
    print("\n4️⃣  Ranking via Tranco...")
    tranco_map = load_tranco_map()
    
    if tranco_map:
        # Map rank. If not found in Tranco, fill with -1
        unique_df["tranco_rank"] = unique_df["fqdn"].map(tranco_map).fillna(-1).astype(int)
    else:
        unique_df["tranco_rank"] = -1

    # Sorting Logic:
    # 1. Tools with Rank > 0 (Ascending)
    # 2. Tools with Rank -1 (Unranked)
    
    ranked_tools = unique_df[unique_df["tranco_rank"] != -1].sort_values("tranco_rank", ascending=True)
    unranked_tools = unique_df[unique_df["tranco_rank"] == -1]
    
    final_df = pd.concat([ranked_tools, unranked_tools])
    
    # --- 5. STATISTICS & SAVE ---
    print("\n📊 --- FINAL STATISTICS ---")
    print(f"   Total Rows Loaded:          {total_raw_rows:,}")
    print(f"   Rows after Empty Link Rem:  {count_after_empty_removal:,}")
    print(f"   Total Unique Tools (FQDN):  {unique_fqdn_count:,}")
    print(f"   Duplicates Removed:         {count_after_empty_removal - unique_fqdn_count:,}")
    print(f"   ---------------------------")
    print(f"   🌍 Ranked in Tranco:        {len(ranked_tools):,} ({(len(ranked_tools)/unique_fqdn_count)*100:.1f}%)")
    print(f"   🌑 Unranked (Rank -1):      {len(unranked_tools):,} ({(len(unranked_tools)/unique_fqdn_count)*100:.1f}%)")
    
    if len(ranked_tools) > 0:
        top_tool = ranked_tools.iloc[0]
        print(f"   🏆 #1 Top Ranked Tool:      {top_tool['tool_name']} ({top_tool['fqdn']} - Rank {top_tool['tranco_rank']})")

    # Final Output Columns
    final_cols = ["tranco_rank", "tool_name", "fqdn", "original_url", "source_directory"]
    final_df = final_df[final_cols]
    
    final_df.to_csv(OUTPUT_FILENAME, index=False)
    print(f"\n💾 Saved result to: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()