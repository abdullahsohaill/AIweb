import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FILE = "FINAL_RANKED_SERVICES.csv"
OUTPUT_FILE = "unique_fqdns.txt"

def main():
    print(f"--- 📝 EXTRACTING UNIQUE FQDNS ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file '{INPUT_FILE}' not found.")
        return

    try:
        # Load the CSV
        df = pd.read_csv(INPUT_FILE)
        
        # Determine the correct column name (it was renamed in the last step)
        target_col = "Domain (FQDN)"
        if target_col not in df.columns:
            # Fallback if using an older version of the file
            target_col = "fqdn" 
        
        if target_col not in df.columns:
            print(f"❌ Error: Could not find FQDN column. Available columns: {list(df.columns)}")
            return

        # Get unique values, sort them, and remove empty ones
        unique_fqdns = sorted(df[target_col].dropna().unique())
        
        # Save to text file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            for domain in unique_fqdns:
                f.write(f"{domain}\n")
                
        print(f"   ✅ Successfully extracted {len(unique_fqdns):,} unique FQDNs.")
        print(f"   💾 Saved to: {OUTPUT_FILE}")

    except Exception as e:
        print(f"   ❌ An error occurred: {e}")

if __name__ == "__main__":
    main()