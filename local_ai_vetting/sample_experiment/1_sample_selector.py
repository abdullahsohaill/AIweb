import pandas as pd
import os
import random

# --- CONFIGURATION ---
# Adjust path to your final local AI list
INPUT_MASTER_FILE = "../../local_ai_collection/local_ai_final_complete.csv"
OUTPUT_FILE = "sampled_50.csv"
SAMPLE_SIZE = 50
SEED = 42

def main():
    if not os.path.exists(INPUT_MASTER_FILE):
        print(f"❌ Error: Master file not found at {INPUT_MASTER_FILE}")
        return

    print(f"Loading Local AI master file...")
    df = pd.read_csv(INPUT_MASTER_FILE)
    print(f"   Total rows: {len(df):,}")

    if len(df) < SAMPLE_SIZE:
        sample_df = df
    else:
        sample_df = df.sample(n=SAMPLE_SIZE, random_state=SEED)

    sample_df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Saved {len(sample_df)} random samples to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()