import pandas as pd
import os
import random

# --- CONFIGURATION ---
# Points to the CLEANED file you just made
INPUT_MASTER_FILE = "../../services_collection/final_tools_1M_vetting/final_tools_1M_corrected.csv"
OUTPUT_FILE = "sampled_100.csv"
SAMPLE_SIZE = 100
SEED = 100

def main():
    if not os.path.exists(INPUT_MASTER_FILE):
        print(f"❌ Error: Master file not found at {INPUT_MASTER_FILE}")
        return

    print(f"Loading verified master file...")
    df = pd.read_csv(INPUT_MASTER_FILE)
    print(f"   Total valid rows: {len(df):,}")

    if len(df) < SAMPLE_SIZE:
        sample_df = df
    else:
        sample_df = df.sample(n=SAMPLE_SIZE, random_state=SEED)

    sample_df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Saved 100 random samples to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()