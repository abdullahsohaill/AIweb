import pandas as pd
import os
from urllib.parse import urlparse

# --- CONFIGURATION: MAPPING FOLDERS & COLUMNS ---
# Format: 
# folder: Subdirectory name
# file: Filename (I added .csv extensions where implied)
# name_col: The column name for the Tool Name in that CSV
# link_col: The column name for the External URL in that CSV
SOURCES = [
    {"folder": "aitoolguru", "file": "aitoolguru_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoolhouse.com", "file": "aitoolhouse_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitools.fyi", "file": "aitoolsfyi_complete.csv", "name_col": "tool_name", "link_col": "clean_website_url"},
    {"folder": "aitoolsdirectory.com", "file": "aitoolsdirectory_complete.csv", "name_col": "tool_name", "link_col": "real_website_url"},
    {"folder": "aitoolnet.com", "file": "aitoolnet_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoptools.com", "file": "aitoptools_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "awesomeaitools.com", "file": "awesomeaitools_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "bai.tools", "file": "baitools_harvest_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "bestofai.com", "file": "bestofai_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "dang.ai", "file": "dang_harvest.csv", "name_col": "tool_name", "link_col": "final_website_url"},
    {"folder": "findr.ai", "file": "foundr_extracted.csv", "name_col": "tool_name", "link_col": "external_url"},
    {"folder": "futuretools.io", "file": "futuretools_resolved_final.csv", "name_col": "tool_name", "link_col": "real_website_url"},
    {"folder": "goodaitools.com", "file": "goodaitools_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "thataicollection.com", "file": "thataicollection_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "toolio.ai", "file": "toolio_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "toolai.io", "file": "toolai_final_links.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "whattheai.tech", "file": "whattheai_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "marketlaunch.net", "file": "microlaunch_final_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "saasaitools.com", "file": "saasaitools_final_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "toolkitly.com", "file": "toolkitly_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "easywithai.com", "file": "easywithai_complete.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "aitoolmall.com", "file": "aitoolmall_final_fixed.csv", "name_col": "tool_name", "link_col": "external_link"},
    {"folder": "openfuture.ai", "file": "openfuture_complete.csv", "name_col": "tool_name", "link_col": "final_website_url"},
]

OUTPUT_FILENAME = "MASTER_AI_TOOLS_LIST.csv"

def get_fqdn(url):
    """Extracts the Fully Qualified Domain Name from a URL."""
    try:
        if pd.isna(url) or url == "":
            return None
        # Add http if missing for parsing
        if not url.startswith("http"):
            url = "http://" + url
        parsed = urlparse(url)
        domain = parsed.netloc
        # Remove www. for cleaner aggregation
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except:
        return None

def normalize_url(url):
    """Normalizes URL for deduplication (lowercase, strip slash)."""
    try:
        if pd.isna(url) or str(url).strip() == "":
            return None
        url = str(url).strip().lower()
        if url.endswith("/"):
            url = url[:-1]
        return url
    except:
        return None

def main():
    print("--- 🧬 STARTING DATA FUSION ---")
    
    all_dataframes = []
    
    # 1. Load and Standardize Data
    for source in SOURCES:
        file_path = os.path.join(source["folder"], source["file"])
        
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path)
                
                # check if columns exist
                if source['name_col'] not in df.columns or source['link_col'] not in df.columns:
                    print(f"   ⚠️  Skipping {source['folder']}: Missing columns.")
                    continue

                # Select and Rename
                temp_df = df[[source['name_col'], source['link_col']]].copy()
                temp_df.columns = ["Tool Name", "Tool Link"]
                
                # Add Metadata
                temp_df["Source"] = source['folder']
                
                all_dataframes.append(temp_df)
                print(f"   ✅ Loaded {len(temp_df)} tools from {source['folder']}")
                
            except Exception as e:
                print(f"   ❌ Error loading {file_path}: {e}")
        else:
            print(f"   ⚠️  File not found: {file_path}")

    if not all_dataframes:
        print("No data loaded. Exiting.")
        return

    # 2. Combine
    print("\n--- 🔄 COMBINING DATA ---")
    master_df = pd.concat(all_dataframes, ignore_index=True)
    total_raw = len(master_df)
    print(f"   Total Raw Rows: {total_raw}")

    # 3. Cleaning
    print("\n--- 🧹 CLEANING ---")
    
    # Remove rows with empty links
    master_df = master_df.dropna(subset=["Tool Link"])
    master_df = master_df[master_df["Tool Link"].str.strip() != ""]
    
    # Normalize Link for Deduplication
    master_df["Normalized Link"] = master_df["Tool Link"].apply(normalize_url)
    
    # 4. Deduplication
    # We keep the first occurrence, but you could sort by 'Source' priority if you wanted
    unique_df = master_df.drop_duplicates(subset=["Normalized Link"])
    
    # 5. Analysis
    print("\n--- 📊 ANALYSIS ---")
    unique_count = len(unique_df)
    duplicates_removed = total_raw - unique_count
    
    print(f"   Total Unique Tools: {unique_count}")
    print(f"   Duplicates Removed: {duplicates_removed}")
    
    # FQDN Stats
    unique_df["FQDN"] = unique_df["Tool Link"].apply(get_fqdn)
    top_domains = unique_df["FQDN"].value_counts().head(10)
    
    print("\n   🏆 Top 10 Domains (Most Frequent Tools):")
    print(top_domains)

    # 6. Save
    print(f"\n--- 💾 SAVING ---")
    
    # Save Master List (Clean)
    final_output = unique_df[["Tool Name", "Tool Link", "Source", "FQDN"]]
    final_output.to_csv(OUTPUT_FILENAME, index=False)
    
    print(f"   🎉 Success! Combined list saved to: {OUTPUT_FILENAME}")
    print(f"   (Contains {len(final_output)} rows)")

if __name__ == "__main__":
    main()