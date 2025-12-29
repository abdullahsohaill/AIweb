import pandas as pd
import os

# --- CONFIGURATION ---
# The input file is the one that has been cleaned and re-ranked.
INPUT_FILE = "final_services_cleaned.csv" 
# The output will be a new, more refined file.
OUTPUT_FILE = "final_services.csv" 

# --- DOMAINS TO REMOVE (FQDN MATCH) ---
FQDN_BLOCKLIST = {
    "lobe.chat"
}

def main():
    print(f"--- 🎯 TARGETED CLEANUP FOR: {INPUT_FILE} ---")
    
    # --- 1. LOAD DATA ---
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file '{INPUT_FILE}' not found in the 'services_collection' directory.")
        return

    print("1️⃣  Loading dataset...")
    try:
        df = pd.read_csv(INPUT_FILE)
        initial_count = len(df)
        print(f"   ✅ Loaded {initial_count:,} rows.")
    except Exception as e:
        print(f"   ❌ Error reading CSV: {e}")
        return

    # --- 2. REMOVE GITHUB.COM URLS ---
    print("\n2️⃣  Filtering out entries where 'extracted_url' points to GitHub...")
    
    # Create a boolean mask for rows where the URL is NOT a GitHub link
    # We use .str.contains() which is robust and handles NaN values safely
    github_mask = df['extracted_url'].str.contains("github.com", na=False)
    df_no_github = df[~github_mask].copy() # Use .copy() to avoid SettingWithCopyWarning
    
    github_removed_count = initial_count - len(df_no_github)
    print(f"   🗑️  Removed {github_removed_count:,} GitHub URL entries.")

    # --- 3. REMOVE LOBE.CHAT FQDNS ---
    print("\n3️⃣  Filtering out entries where 'fqdn' is 'lobe.chat'...")
    
    # Create a boolean mask for rows where the FQDN is NOT in our blocklist
    fqdn_mask = df_no_github['fqdn'].isin(FQDN_BLOCKLIST)
    df_final = df_no_github[~fqdn_mask].copy()
    
    lobechat_removed_count = len(df_no_github) - len(df_final)
    print(f"   🗑️  Removed {lobechat_removed_count:,} 'lobe.chat' FQDN entries.")
    
    # --- 4. STATISTICS & SAVE ---
    final_count = len(df_final)
    total_removed = initial_count - final_count
    
    print("\n📊 --- FINAL STATISTICS ---")
    print(f"   Initial Rows:      {initial_count:,}")
    print(f"   Total Rows Removed:  {total_removed:,}")
    print(f"   Final Rows:          {final_count:,}")

    print(f"\n💾 Saving cleaned data to '{OUTPUT_FILE}'...")
    df_final.to_csv(OUTPUT_FILE, index=False)
    print("   ✅ Done.")


if __name__ == "__main__":
    main()