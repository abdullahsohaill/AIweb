import pandas as pd
import os
from urllib.parse import urlparse

# --- CONFIGURATION ---
OUTPUT_FILENAME = "DEDUPLICATED_AI_TOOLS_MASTER.csv"

# The source list remains the same
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
    {"folder": "aitoolnet.com", "file": "aitoolnet_final_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
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
        
        if not url_str.startswith("http"):
            url_str = "http://" + url_str
            
        parsed = urlparse(url_str)
        domain = parsed.netloc
        
        if ':' in domain:
            domain = domain.split(':')[0]
            
        if domain.startswith("www."):
            domain = domain[4:]
            
        return domain if domain else None
    except:
        return None

def main():
    print("--- 🧬 STARTING MASTER AI TOOL AGGREGATION & DIAGNOSTICS ---")
    
    all_dfs = []
    
    print("\n1️⃣  Aggregating Sources...")
    for source in SOURCES:
        path = os.path.join(source["folder"], source["file"])
        
        if os.path.exists(path):
            try:
                df = pd.read_csv(path)
                
                if source["name_col"] not in df.columns or source["link_col"] not in df.columns:
                    print(f"   ⚠️  Skipping {source['folder']}: Columns missing.")
                    continue
                
                temp = df[[source["name_col"], source["link_col"]]].copy()
                temp.columns = ["tool_name", "original_url"]
                temp["source_directory"] = source["folder"]
                
                all_dfs.append(temp)
            except Exception as e:
                print(f"   ❌ Error reading {path}: {e}")
        else:
            print(f"   ⚠️  File Not Found: {path}")
            
    if not all_dfs:
        print("No data loaded. Exiting.")
        return

    master_df = pd.concat(all_dfs, ignore_index=True)
    total_raw_rows = len(master_df)
    
    # --- NEW: DIAGNOSTIC FOR UNKNOWN TAGS ---
    print("\n🔍  Checking for sources with generic or 'unknown' tool names...")
    generic_names = ['link', 'website', 'visit', 'click here', 'a', 'source', 'download', 'logo', 'app', 'tool']
    master_df['normalized_name'] = master_df['tool_name'].str.strip().str.lower()
    problematic_rows = master_df[
        master_df['normalized_name'].isna() |
        (master_df['normalized_name'] == '')
    ]
    if not problematic_rows.empty:
        problematic_sources = sorted(problematic_rows['source_directory'].unique())
        print("   ❗️ Found generic tool names in the following sources (review these crawlers):")
        for source_dir in problematic_sources:
            print(f"      - {source_dir}")
    else:
        print("   ✅ No common generic tool names found.")
    master_df = master_df.drop(columns=['normalized_name'])
    
    print(f"\n2️⃣  Cleaning & Extracting FQDN (Raw Count: {total_raw_rows:,})...")
    master_df = master_df.dropna(subset=["original_url"])
    master_df = master_df[master_df["original_url"].astype(str).str.strip() != ""]
    count_after_empty_removal = len(master_df)
    master_df["fqdn"] = master_df["original_url"].apply(get_fqdn)
    master_df = master_df.dropna(subset=["fqdn"])
    master_df = master_df[master_df["fqdn"] != ""]
    
    # --- 3. DEDUPLICATE ---
    print("\n3️⃣  Deduplicating based on the full Original URL...")
    # Keep the first occurrence of every original_url
    final_df = master_df.drop_duplicates(subset=["original_url"], keep="first").copy()
    unique_url_count = len(final_df)
    
    # --- 4. STATISTICS & SAVE ---
    # Sort the final result alphabetically by URL for consistency
    final_df = final_df.sort_values(by="original_url").reset_index(drop=True)

    print("\n📊 --- FINAL STATISTICS ---")
    print(f"   Total Raw Rows Loaded:      {total_raw_rows:,}")
    print(f"   Rows After Cleaning Links:  {count_after_empty_removal:,}")
    print(f"   Total Unique URLs:          {unique_url_count:,}")
    print(f"   Duplicate URLs Removed:     {count_after_empty_removal - unique_url_count:,}")
    
    # Final Output Columns
    final_cols = ["tool_name", "fqdn", "original_url", "source_directory"]
    final_df = final_df[final_cols]
    
    final_df.to_csv(OUTPUT_FILENAME, index=False)
    print(f"\n💾 Saved result to: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()