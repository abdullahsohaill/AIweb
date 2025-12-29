# filter_master_list.py
"""
This script applies a comprehensive, multi-stage filtering strategy to the
aggregated 'master_ai_services_list.csv'. It systematically removes known
non-service domains and URL patterns to significantly reduce noise and produce
a high-quality list of candidate AI services for the final manual review.

The filtering logic is based on a predefined categorization of exclusions.

Requirements:
  pip install pandas

Usage:
  - Ensure 'master_ai_services_list.csv' is in the same directory.
  - Run the script: python filter_master_list.py
"""

import pandas as pd
from pathlib import Path

# --- CONFIGURATION ---
MASTER_FILE = Path("master_ai_services_list.csv")
FILTERED_OUTPUT_FILE = Path("final_filtered_services.csv")

# ==============================================================================
# --- FILTERING STRATEGY: CATEGORIZATION OF EXCLUSIONS ---
# ==============================================================================

# 1. Content and Community Platforms
SOCIAL_MEDIA_DOMAINS = {
    'facebook.com', 'twitter.com', 'x.com', 'instagram.com', 'linkedin.com', 
    'reddit.com', 'pinterest.com', 'tumblr.com', 't.me', 'discord.com', 
    'discord.gg', 'bsky.app', 'threads.net', 'linktr.ee', 't.co', 'youtu.be', 
    'youtube.com', 'vimeo.com', 'tiktok.com', 'soundcloud.com', 'giphy.com', 
    'imgur.com', 'i.imgur.com', 'twitch.tv', 'redd.it'
}

NEWS_MEDIA_DOMAINS = {
    'forbes.com', 'techcrunch.com', 'wired.com', 'theverge.com', 'nytimes.com', 
    'bbc.com', 'bbc.co.uk', 'theguardian.com', 'cnn.com', 'reuters.com', 
    'wsj.com', 'bloomberg.com', 'businessinsider.com', 'arstechnica.com', 
    'venturebeat.com', 'zdnet.com', 'washingtonpost.com', 'cnbc.com', 'dailymail.co.uk', 'telegraph.co.uk',
    'independent.co.uk', 'thetimes.co.uk', 'economist.com', 'npr.org', 'huffpost.com', 'nypost.com', 'cnet.com',
    'news.yahoo.com', 'usatoday.com', 'abcnews.go.com', 'latimes.com', 'chicagotribune.com', 'newsweek.com',
    'cbsnews.com', 'foxnews.com', 'theatlantic.com', 'slate.com', 'motherjones.com', 'nbcnews.com', 'apnews.com',
    'cbc.ca', 'globalnews.ca', 'theglobeandmail.com', 'fortune.com', 'time.com', 'newyorker.com', 'economist.com',
    'politico.com', 'thehill.com', 'ucl.ac.uk', 'nydailynews.com', 'timesofisrael.com', 'seattletimes.com',
    'newgrounds.com', 'thenewstack.io'
}

BLOG_PLATFORM_DOMAINS = {
    'medium.com', 'substack.com', 'blogspot.com', 'wordpress.com', 'dev.to', 'dreamhost.com', 'ghost.org', 
    'huffpost.com', 'towardsdatascience.com', 'kdnuggets.com', 'analyticsvidhya.com', 'datafloq.com', 'dataconomy.com', 
    'becominghuman.ai', 'aitrends.com', 'syncedreview.com', 'machinelearningmastery.com', 'theconversation.com',
    'pewresearch.org', 'techpolicy.com', 'techdirt.com', 'technologyreview.com', 'github.blog',
    'nationalreview.com', 'investors.com', 'analyticsvidhya.com', 'verpex.com'
}

FORUM_DOMAINS = {
    'stackoverflow.com', 'quora.com', 'stackexchange.com', 'coursera.org', 'edx.org', 'udemy.com', 'edx.com',
    'kaggle.com', 'gitlab.com', 'bitbucket.org', 'livescience.com', 'scifi.stackexchange.com', 'academia.stackexchange.com'
}

# 2. Academic and Research Repositories
ACADEMIC_DOMAINS = {
    'arxiv.org', 'researchgate.net', 'sciencedirect.com', 'academia.edu', 
    'springer.com', 'nature.com', 'pnas.org', 'doi.org', 'mdpi.com', 'biorxiv.org',
    'aclanthology.org', 'openreview.net', 'science.org', 'justice.gov', 'nih.gov'
}

# 3. E-commerce and Retail
ECOMMERCE_DOMAINS = {
    'amazon.com', 'walmart.com', 'etsy.com', 'shopify.com', 'ebay.com'
}

# 4. Search, Redirects, and Web Infrastructure
INFRASTRUCTURE_DOMAINS = {
    'gstatic.com', 'img.shields.io', 'google.com', 'bing.com', 'duckduckgo.com',
    'bit.ly', 'amzn.to', 'wa.me', 'play.google.com', 'apps.apple.com'
}

# Patterns for infrastructure/asset URLs to remove
URL_EXCLUSION_PATTERNS = [
    '/search?q=', '/search?', '.svg', '.png', '.jpg', '.jpeg', '.gif', '.webp'
]


# Combine all domain blocklists into a single master set for efficient filtering
MASTER_DOMAIN_BLOCKLIST = (
    SOCIAL_MEDIA_DOMAINS | NEWS_MEDIA_DOMAINS | BLOG_PLATFORM_DOMAINS | 
    FORUM_DOMAINS | ACADEMIC_DOMAINS | ECOMMERCE_DOMAINS | INFRASTRUCTURE_DOMAINS
)

if __name__ == "__main__":
    if not MASTER_FILE.exists():
        print(f"ERROR: Master file not found at '{MASTER_FILE}'. Please run the aggregation script first.")
        exit()

    print(f"--- Applying Advanced Filtering to {MASTER_FILE} ---")

    df = pd.read_csv(MASTER_FILE)
    initial_count = len(df)
    print(f"Loaded {initial_count:,} total candidate links.")

    # --- Filtering Stage 1: Deduplication ---
    df.drop_duplicates(subset=['extracted_url'], keep='first', inplace=True)
    count_after_dedup = len(df)
    print(f"1. Removed {initial_count - count_after_dedup:,} duplicate URLs. Remaining: {count_after_dedup:,}")

    # --- Filtering Stage 2: Master Domain Blocklist ---
    df = df[~df['fqdn'].isin(MASTER_DOMAIN_BLOCKLIST)]
    count_after_domain_filter = len(df)
    print(f"2. Removed {count_after_dedup - count_after_domain_filter:,} links based on the master domain blocklist. Remaining: {count_after_domain_filter:,}")

    # --- Filtering Stage 3: URL Pattern Blocklist ---
    # Create a boolean mask for rows where the URL contains any of the exclusion patterns
    pattern_mask = df['extracted_url'].str.contains('|'.join(URL_EXCLUSION_PATTERNS), case=False, na=False)
    df = df[~pattern_mask]
    count_after_pattern_filter = len(df)
    print(f"3. Removed {count_after_domain_filter - count_after_pattern_filter:,} links based on URL patterns (e.g., images, search pages). Remaining: {count_after_pattern_filter:,}")

    # Final sorting
    df_final = df.sort_values(by=['domain_tranco_rank', 'fqdn'], ascending=[True, True])

    # Save the final, filtered dataset
    df_final.to_csv(FILTERED_OUTPUT_FILE, index=False)

    print("\n--- Filtering Complete ---")
    print(f"Initial candidates: {initial_count:,}")
    print(f"Final high-quality candidates: {len(df_final):,}")
    print(f"✅ Final filtered dataset saved to: '{FILTERED_OUTPUT_FILE}'")

    # --- Display Insights from the FINAL Filtered Data ---
    print("\n--- Insights from Filtered Dataset ---")
    print(f"Total unique FQDNs in final list: {df_final['fqdn'].nunique():,}")
    print("\nTop 20 Most Frequent Domains in the FINAL LIST:")
    print(df_final['fqdn'].value_counts().head(20).to_string())