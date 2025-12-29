# deduplicate.py
import pandas as pd

INPUT_FILE = 'phase1_discovered_urls.csv'
OUTPUT_FILE = 'phase1_discovered_urls_unique.csv'

print(f"Reading raw crawl results from '{INPUT_FILE}'...")
df = pd.read_csv(INPUT_FILE)
original_count = len(df)
print(f"Found {original_count} total links.")

# Drop duplicate URLs, keeping the first query that found it
df_unique = df.drop_duplicates(subset=['discovered_url'], keep='first')
unique_count = len(df_unique)
duplicates_removed = original_count - unique_count

print(f"Removed {duplicates_removed} duplicate links.")
print(f"Saving {unique_count} unique links to '{OUTPUT_FILE}'...")
df_unique.to_csv(OUTPUT_FILE, index=False)
print("Deduplication complete.")