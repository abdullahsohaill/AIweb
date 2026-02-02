import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FILE = "content_metadata.csv"
OUTPUT_FILE = "annotated_results.csv"

def main():
    print("--- 📝 SETTING UP ANNOTATION SHEET ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file '{INPUT_FILE}' not found.")
        return
        
    if os.path.exists(OUTPUT_FILE):
        print(f"⚠️  Warning: '{OUTPUT_FILE}' already exists.")
        choice = input("Overwrite it? (y/n): ").lower()
        if choice != 'y':
            print("Aborted.")
            return

    # 1. Load Data
    df = pd.read_csv(INPUT_FILE)
    print(f"   Loaded {len(df)} rows.")

    # 2. Prepare Output DataFrame
    output_df = pd.DataFrame()
    output_df['Tool Name'] = df.get('Tool Name', df.get('tool_name'))
    output_df['URL'] = df.get('Extracted URL', df.get('url'))
    output_df['FQDN'] = df.get('Domain (FQDN)', df.get('fqdn'))
    
    # Manual Annotation Columns
    output_df['Abdullah_Annotation'] = ""  # Fill this: 1 (Yes) or 0 (No)
    output_df['Abdullah_Notes'] = ""       # Optional comments
    
    # LLM Columns (To be filled by script later)
    output_df['LLM_Decision'] = ""
    output_df['LLM_Reasoning'] = ""
    
    # Metadata for processing
    output_df['content_file'] = df['content_file']

    # 3. Save
    output_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✅ Created '{OUTPUT_FILE}'.")
    print("   👉 Action: Open this file, fill 'Abdullah_Annotation' with 1 or 0, and save.")

if __name__ == "__main__":
    main()