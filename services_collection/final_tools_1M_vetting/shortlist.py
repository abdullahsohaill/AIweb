import pandas as pd

# 1. CONFIGURATION
INPUT_FILE = 'final_tools_1M_cleaned_sorted.csv' # The output from the previous script
OUTPUT_FILE = 'final_tools_1M_reduced.csv'

# The FQDNs you want to preserve completely (Keep ALL rows)
# Make sure these match the 'Domain (FQDN)' column exactly.
WHITELIST_DOMAINS = [
    'huggingface.co',
    'monica.im',
    'openrouter.ai',
    'cloud.google.com',
    'openai.com',
    'ai.google.dev', # Added based on your previous data, remove if unwanted
    'stability.ai'   # Added based on your previous data, remove if unwanted
]

# 2. EXECUTION
try:
    print("Loading dataset...")
    df = pd.read_csv(INPUT_FILE)
    
    print(f"Original Row Count: {len(df)}")

    # Ensure Rank is numeric for sorting later
    df['Median Tranco Rank'] = pd.to_numeric(df['Median Tranco Rank'], errors='coerce')

    # --- Step A: Separate Whitelist vs The Rest ---
    
    # Rows that match our whitelist
    df_whitelist = df[df['Domain (FQDN)'].isin(WHITELIST_DOMAINS)].copy()
    
    # Rows that DO NOT match our whitelist
    df_others = df[~df['Domain (FQDN)'].isin(WHITELIST_DOMAINS)].copy()

    print(f"Whitelisted Rows (Preserved): {len(df_whitelist)}")
    print(f"Other Rows (To be reduced): {len(df_others)}")

    # --- Step B: Reduce 'The Rest' to 1 per FQDN ---
    
    # Create a temporary column for URL length
    df_others['url_len'] = df_others['Extracted URL'].str.len()
    
    # Sort by URL length (Ascending). 
    # This ensures that when we pick 'first', we pick the shortest URL (usually the main home page/app root).
    df_others = df_others.sort_values('url_len', ascending=True)
    
    # Drop duplicates, keeping only the first (shortest) entry per FQDN
    df_others_reduced = df_others.drop_duplicates(subset=['Domain (FQDN)'], keep='first')
    
    # Remove temp column
    df_others_reduced = df_others_reduced.drop(columns=['url_len'])
    
    print(f"Other Rows after reduction: {len(df_others_reduced)}")

    # --- Step C: Combine and Final Sort ---
    
    df_final = pd.concat([df_whitelist, df_others_reduced])
    
    # Sort by Rank (Ascending), then by Domain (Alphabetical) to keep groups together
    df_final = df_final.sort_values(
        by=['Median Tranco Rank', 'Domain (FQDN)'], 
        ascending=[True, True],
        na_position='last'
    )

    # Export
    df_final.to_csv(OUTPUT_FILE, index=False)

    print("-" * 30)
    print(f"Final Row Count: {len(df_final)}")
    print(f"Saved to: {OUTPUT_FILE}")
    print("-" * 30)

except FileNotFoundError:
    print(f"Error: Could not find {INPUT_FILE}")
except Exception as e:
    print(f"Error: {e}")