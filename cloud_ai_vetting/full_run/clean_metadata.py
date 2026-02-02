import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FILE = "full_content_metadata.csv"
# We save to a new file to be safe, which you will use for the LLM step
OUTPUT_FILE = "full_content_metadata_cleaned.csv"

def main():
    print(f"--- 🧹 CLEANING METADATA: REMOVING MISSING FILES ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    initial_count = len(df)
    print(f"   Loaded {initial_count:,} rows.")

    # Function to check if file exists
    def file_exists(path):
        if pd.isna(path) or str(path).strip() == "":
            return False
        return os.path.exists(str(path))

    # Apply filter
    # We keep rows where 'file_exists' returns True
    valid_mask = df['content_file'].apply(file_exists)
    
    df_clean = df[valid_mask].copy()
    df_removed = df[~valid_mask]
    
    removed_count = len(df_removed)
    final_count = len(df_clean)

    # Save
    df_clean.to_csv(OUTPUT_FILE, index=False)

    print(f"\n📊 --- STATS ---")
    print(f"   Original Rows:     {initial_count:,}")
    print(f"   Rows Removed:      {removed_count:,} (No MD file found)")
    print(f"   Final Valid Rows:  {final_count:,}")
    print(f"   💾 Saved to:       {OUTPUT_FILE}")

    if removed_count > 0:
        print("\n   ℹ️  Note: Removed rows had extraction errors or timeouts.")

if __name__ == "__main__":
    main()