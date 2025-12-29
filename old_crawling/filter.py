# filter.py
# Phase 2.5: Applies a series of powerful heuristics to purge noise from the
# massive raw extracted links file, creating a much smaller, higher-quality
# list of candidates for the next phase.

import pandas as pd
from tqdm import tqdm
from tldextract import extract
import os

# --- CONFIGURATION ---
INPUT_RAW_LINKS_FILE = 'phase2_all_candidate_links.csv'
OUTPUT_FILTERED_CANDIDATES_FILE = 'phase3_filtered_candidates.csv'

# A list of common domains to purge. These are almost never AI services.
PURGE_DOMAINS = {
    'google.com', 'youtube.com', 'linkedin.com', 'facebook.com', 'twitter.com', 't.co',
    'wikipedia.org', 'wordpress.org', 'microsoft.com', 'apple.com', 'amazon.com', 'wa.me',
    'github.com', 'medium.com', 'dev.to', 'stackoverflow.com', 'techcrunch.com', 'vimeo.com',
    'venturebeat.com', 'producthunt.com', 'towardsdatascience.com', 'analyticsvidhya.com',
    'indiehackers.com', 'reddit.com', 'forbes.com', 'nytimes.com', 'wsj.com', 'w3.org',
    'ietf.org', 'whatwg.org', 'archive.org', 'mozilla.org', 'apache.org', 'docker.com',
    'instagram.com', 'pinterest.com', 'telegram.org', 'discord.com', 'adobe.com'
}

# File extensions to purge.
PURGE_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.css', '.js', '.pdf', '.zip', 
    '.gz', '.tar', '.ico', '.xml', '.rss', '.woff', '.woff2', '.ttf', '.eot', '.mp4',
    '.mp3', '.webm', '.txt'
}

if __name__ == "__main__":
    if not os.path.exists(INPUT_RAW_LINKS_FILE):
        print(f"ERROR: Raw links file '{INPUT_RAW_LINKS_FILE}' not found. Run extractor.py first.")
        exit()

    print(f"Starting the filtering process on '{INPUT_RAW_LINKS_FILE}'. This may take a while.")

    # We will process the large file in chunks to manage memory usage.
    chunk_size = 100000  # Process 100,000 rows at a time
    final_candidates = []
    
    # Use tqdm to show progress while iterating through chunks
    # First, get the total number of lines for the progress bar
    total_lines = sum(1 for line in open(INPUT_RAW_LINKS_FILE)) - 1 # a bit slow but good for UX

    for chunk in tqdm(pd.read_csv(INPUT_RAW_LINKS_FILE, chunksize=chunk_size), total=total_lines // chunk_size, desc="Filtering Chunks"):
        
        # --- Filter 1: The File Extension & Domain Purge ---
        # Create boolean masks for rows to drop
        has_bad_extension = chunk['candidate_link'].str.lower().str.contains('|'.join(f'\\{ext}$' for ext in PURGE_EXTENSIONS), regex=True, na=False)
        
        # Extract domains for further filtering
        chunk['candidate_domain'] = chunk['candidate_link'].apply(lambda url: extract(str(url)).registered_domain)
        is_bad_domain = chunk['candidate_domain'].isin(PURGE_DOMAINS)
        
        # Apply the filters
        filtered_chunk = chunk[~has_bad_extension & ~is_bad_domain]

        # --- Filter 2: The Internal Link Purge ---
        # We need to handle the 'direct_discovery' case carefully
        def is_internal_link(row):
            if row['source_page'] == 'direct_discovery':
                return False # Never purge a direct discovery
            try:
                source_domain = extract(str(row['source_page'])).registered_domain
                return source_domain == row['candidate_domain']
            except:
                return True # Treat parse errors as internal/bad links
        
        is_internal = filtered_chunk.apply(is_internal_link, axis=1)
        
        # Final chunk for this iteration
        clean_chunk = filtered_chunk[~is_internal]
        
        final_candidates.append(clean_chunk)

    # --- Combine all processed chunks into a single DataFrame ---
    print("\nCombining filtered chunks...")
    df_clean = pd.concat(final_candidates, ignore_index=True)
    
    print(f"Initial raw links (approx): {total_lines}")
    print(f"Remaining high-potential candidates after filtering: {len(df_clean)}")
    
    # --- Final Step: Create the Canonical Domain List for the Next Phase ---
    print("Deduplicating to create the final list of unique candidate domains...")
    # We only care about the unique candidate domains now
    unique_domains = df_clean.drop_duplicates(subset=['candidate_domain'])
    
    print(f"Found {len(unique_domains)} unique candidate domains to investigate in the next phase.")
    
    # Save the cleaned, unique list
    unique_domains[['candidate_link', 'candidate_domain', 'source_page']].to_csv(OUTPUT_FILTERED_CANDIDATES_FILE, index=False)
    
    print(f"\nPhase 2.5 (Filtering) Complete. Your high-quality candidate list is in '{OUTPUT_FILTERED_CANDIDATES_FILE}'.")
    print("This file is now ready for the final, heuristic-based classification phase.")