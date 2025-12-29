import pandas as pd
import numpy as np
from pathlib import Path
import os
import gc

# --- CONFIGURATION ---
TRANCO_DIR = Path("")
OUTPUT_FILE = "tranco_temporal_intersection_master.csv"

# Chronological Mapping (YYYY-MM-DD for proper sorting)
FILE_MAPPING = [
    ("2025-11-05", "tranco_NN2NW.csv"),
    ("2025-11-12", "tranco_W43L9.csv"),
    ("2025-11-19", "tranco_QW2W4.csv"),
    ("2025-11-26", "tranco_7N4ZX.csv"),
    ("2025-12-03", "tranco_JLZLY.csv"),
    ("2025-12-10", "tranco_KW98W.csv"),
    ("2025-12-17", "tranco_L75N4.csv") # The n-th list
]

def get_summary_stats(df, rank_col="median_rank"):
    """Calculates distribution of ranks."""
    total = len(df)
    stats = {
        "Total": total,
        "<= 1M": len(df[df[rank_col] <= 1_000_000]),
        "<= 5M": len(df[df[rank_col] <= 5_000_000]),
        "<= 10M": len(df[df[rank_col] <= 10_000_000]),
        "> 10M": len(df[df[rank_col] > 10_000_000]),
    }
    return stats

def main():
    print("--- 📊 STARTING TEMPORAL INTERSECTION AGGREGATION ---")
    
    if not TRANCO_DIR.exists():
        print(f"❌ Error: Directory '{TRANCO_DIR}' not found.")
        return

    # 1. Load Data
    print("\n1️⃣  Loading Snapshots...")
    dfs = []
    
    # Store date keys to ensure column order later
    date_keys = [x[0] for x in FILE_MAPPING]
    
    for date, fname in FILE_MAPPING:
        path = TRANCO_DIR / fname
        if not path.exists():
            print(f"   ⚠️  CRITICAL WARNING: Missing {fname}. Intersection logic may fail.")
            continue
        
        try:
            # Load only rank and domain to save memory
            # Assumes standard Tranco format: 1,google.com
            df = pd.read_csv(path, header=None, names=["rank", "domain"])
            df["domain"] = df["domain"].astype(str).str.strip().str.lower()
            
            # Reduce memory usage
            df["rank"] = pd.to_numeric(df["rank"], downcast="integer")
            df = df.set_index("domain")
            
            # Rename rank column to the date
            df = df.rename(columns={"rank": date})
            dfs.append(df)
            print(f"   ✅ Loaded {date} ({fname}): {len(df):,} rows")
        except Exception as e:
            print(f"   ❌ Error reading {fname}: {e}")

    # 2. Pivot / Merge into Wide Format
    print("\n2️⃣  Merging into Wide Format (Matrix)...")
    # Join all dataframes on the index (domain). Outer join to get all candidates first.
    # This creates a DataFrame where columns are dates, index is domain, values are ranks.
    master_matrix = pd.concat(dfs, axis=1)
    
    print(f"   -> Total unique domains observed: {len(master_matrix):,}")
    
    # Garbage collection to free up RAM from individual dfs
    del dfs
    gc.collect()

    # 3. Apply Temporal Intersection Logic
    print("\n3️⃣  Applying Temporal Intersection Logic...")
    
    # Convert to boolean matrix (True if present/Ranked, False if NaN)
    presence_matrix = master_matrix.notna()
    
    # A. Calculate the index (0 to 6) of the first appearance
    # idxmax returns the *label* of the first True. We need the integer position.
    # argmax gives integer position of first True.
    first_seen_idx = presence_matrix.values.argmax(axis=1)
    
    # B. Calculate how many times it *actually* appeared
    actual_counts = presence_matrix.sum(axis=1).values
    
    # C. Calculate how many times it *should* appear
    # If it starts at index 0 (Nov 5), it should appear 7 times.
    # If it starts at index 2 (Nov 19), it should appear 5 times.
    # Formula: Total_Cols - First_Seen_Index
    total_cols = len(date_keys)
    expected_counts = total_cols - first_seen_idx
    
    # D. Define the Filter Mask
    # Condition 1: Must appear in all subsequent lists (Actual == Expected)
    cond_persistence = (actual_counts == expected_counts)
    
    # Condition 2: Must NOT start in the last list (First_Seen_Index < Last_Index)
    # The last index is total_cols - 1
    cond_not_last = (first_seen_idx < (total_cols - 1))
    
    final_mask = cond_persistence & cond_not_last
    
    # Apply filter
    valid_domains = master_matrix[final_mask].copy()
    print(f"   -> Domains remaining after filtering: {len(valid_domains):,}")

    # 4. Calculate Median Rank
    print("\n4️⃣  Calculating Median Ranks...")
    
    # Calculate median across the columns (axis=1), ignoring NaNs (though there shouldn't be gaps)
    valid_domains["median_rank"] = valid_domains.median(axis=1).astype(int)
    
    # Also keep appearance count for reference
    valid_domains["appearance_count"] = actual_counts[final_mask]
    
    # Reset index to make 'domain' a column again
    final_output = valid_domains.reset_index()[["domain", "median_rank", "appearance_count"]]
    
    # Sort by Median Rank (Ascending) -> Most popular first
    final_output = final_output.sort_values(by="median_rank", ascending=True)

    # 5. Statistics
    print("\n📊 --- FINAL DATASET STATISTICS ---")
    stats = get_summary_stats(final_output)
    
    for category, count in stats.items():
        if category == "Total":
            print(f"   {category}: {count:,}")
        else:
            pct = (count / stats["Total"]) * 100
            print(f"   {category}: {count:,} ({pct:.2f}%)")

    # 6. Save
    output_path = TRANCO_DIR / OUTPUT_FILE
    final_output.to_csv(output_path, index=False)
    print(f"\n💾 Saved Temporal Master List to: {output_path}")

if __name__ == "__main__":
    main()