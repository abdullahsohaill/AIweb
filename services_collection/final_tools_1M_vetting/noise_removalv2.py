import pandas as pd
from urllib.parse import urlparse

# 1. SETUP
INPUT_FILE = 'final_tools_1M_vetting.csv'
OUTPUT_CLEAN_FILE = 'final_tools_1M_cleaned_sorted.csv' # Renamed for clarity
OUTPUT_NOISE_FILE = 'final_tools_1M_removed_v2.csv'

# 2. DEFINING NOISE PATTERNS
PATH_BLACKLIST = [
    # Content & Marketing
    '/blog', '/news', '/article', '/press', '/media', '/events', 
    '/case-studies', '/whitepaper', '/webinars', '/resources',
    '/guide', '/tutorial', '/hub', '/community', '/forum',
    
    # Corporate / Legal / Support
    '/contact', '/about', '/careers', '/jobs', '/investors', '/team',
    '/privacy', '/terms', '/legal', '/gdpr', '/security', '/support',
    '/status', '/faq', '/help',
    
    # Directories / Listings
    '/marketplace', '/store', '/integrations', '/extensions', 
    '/plugins', '/addons', '/apps', '/showcase',
    
    # Sales / Auth (Usually redundant if we have the main link)
    '/pricing', '/plans', '/buy', '/checkout', '/cart',
    '/login', '/signin', '/signup', '/register', '/auth', 
    '/join', '/subscribe', '/forgot-password',
    
    # Technical files
    'llms.txt', 'llms-full.txt', '.well-known', 'sitemap.xml', 'robots.txt'
]

# Domains that are definitely not AI service providers
DOMAIN_BLACKLIST = [
    'brunomars.com', 'edsheeran.com', 'katyperry.com', 'ladygaga.com', 
    'michaeljackson.com', 'taylorswift.com', 'beyonce.com', 
    'theonion.com', 'huffingtonpost.in', 'breakingnews.ie', 
    'archive.md', 'web.archive.org', 'wikipedia.org', 
    'amazon.com', 'ebay.com', 'etsy.com', 'walmart.com',
    'linkedin.com', 'facebook.com', 'twitter.com', 'instagram.com', 'youtube.com'
]

# 3. HELPER FUNCTIONS

def normalize_url(url):
    """
    Strips http/https, www, query parameters, and trailing slashes.
    Example: https://www.tool.com/app?ref=123 -> tool.com/app
    """
    if pd.isna(url) or not isinstance(url, str):
        return ""
    try:
        parsed = urlparse(url)
        clean_path = parsed.path.rstrip('/') # Remove trailing slash
        clean_netloc = parsed.netloc.replace('www.', '')
        return f"{clean_netloc}{clean_path}".lower()
    except:
        return ""

def is_noise(url):
    if pd.isna(url): return True
    try:
        parsed = urlparse(str(url))
        path = parsed.path.lower()
        domain = parsed.netloc.lower().replace('www.', '')
        
        if any(bad in domain for bad in DOMAIN_BLACKLIST):
            return True
            
        if any(bad in path for bad in PATH_BLACKLIST):
            return True
            
        if path.endswith(('.pdf', '.zip', '.xml', '.png', '.jpg')):
            return True

        return False
    except:
        return True

# 4. EXECUTION
try:
    print("Loading dataset...")
    try:
        df = pd.read_csv(INPUT_FILE, encoding='utf-8')
    except:
        df = pd.read_csv(INPUT_FILE, encoding='latin1')
    
    print(f"Original Count: {len(df)}")

    # --- STEP 1: Pattern Filtering ---
    print("Applying pattern filters...")
    df['is_noise'] = df['Extracted URL'].apply(is_noise)
    df_clean = df[df['is_noise'] == False].copy()
    df_noise = df[df['is_noise'] == True].copy()
    
    print(f"Post-Pattern Filter Count: {len(df_clean)}")

    # --- STEP 2: Normalization for Deduplication ---
    print("Normalizing URLs for deduplication...")
    df_clean['norm_url'] = df_clean['Extracted URL'].apply(normalize_url)

    # --- STEP 3: Deduplication ---
    # Sort by URL length first so we keep the shortest (root) URL when deduplicating
    df_clean['url_length'] = df_clean['Extracted URL'].str.len()
    df_clean = df_clean.sort_values('url_length', ascending=True)

    # Dedupe by Normalized URL
    df_deduped = df_clean.drop_duplicates(subset=['norm_url'], keep='first')
    
    # Dedupe by Tool Name + Domain
    df_final = df_deduped.drop_duplicates(subset=['Tool Name', 'Domain (FQDN)'], keep='first')

    # --- STEP 4: Final Sorting (Rank + Grouping) ---
    print("Applying Final Sorting...")
    
    # Ensure Rank is numeric (handle non-numeric errors by coercing to NaN)
    df_final['Median Tranco Rank'] = pd.to_numeric(df_final['Median Tranco Rank'], errors='coerce')
    
    # Sort by Rank (Ascending), then by Domain (Alphabetical)
    # This groups FQDNs together because they usually share the same Rank.
    df_final = df_final.sort_values(
        by=['Median Tranco Rank', 'Domain (FQDN)'], 
        ascending=[True, True],
        na_position='last'
    )

    # Cleanup temporary columns
    df_final = df_final.drop(columns=['is_noise', 'norm_url', 'url_length'])
    
    # Save
    df_final.to_csv(OUTPUT_CLEAN_FILE, index=False)
    
    removed_count = len(df) - len(df_final)
    df_noise.to_csv(OUTPUT_NOISE_FILE, index=False)

    print("-" * 30)
    print(f"Final Cleaned Count: {len(df_final)}")
    print(f"Total Rows Removed: {removed_count}")
    print(f"File Saved: {OUTPUT_CLEAN_FILE}")
    print("-" * 30)

except FileNotFoundError:
    print(f"Error: Could not find {INPUT_FILE}")
except Exception as e:
    print(f"Error: {e}")