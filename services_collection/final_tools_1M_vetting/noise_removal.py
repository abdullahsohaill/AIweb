import pandas as pd
from urllib.parse import urlparse

# 1. SETUP: Input and Output filenames
INPUT_FILE = 'final_tools_1M_vetting.csv'
OUTPUT_CLEAN_FILE = 'final_tools_1M_cleaned.csv'
OUTPUT_NOISE_FILE = 'final_tools_1M_removed_noise.csv'

# 2. DEFINING THE NOISE FILTERS

# PATH BLACKLIST: If the URL path contains these, it is likely info/marketing, not the tool.
# We include '/products/' specifically to catch the Google Cloud marketing pages you mentioned.
PATH_BLACKLIST = [
    '/blog', '/news', '/article', '/press', '/media', '/events', # Content
    '/contact', '/about', '/careers', '/jobs', '/investors', '/team', # Corporate
    '/privacy', '/terms', '/legal', '/gdpr', '/security', # Legal
    '/marketplace', '/store', '/integrations', '/extensions', # Directories (like Google Cloud Marketplace)
    '/case-studies', '/customers', '/whitepaper', '/webinars', # Marketing assets
    '/pricing', '/plans', # Sales pages
    '/faq', '/help', '/support', '/status', # Support pages
    '/docs', '/documentation', '/api-docs', '/guides', # Documentation (keeps the tool, removes the manual)
    '/products/', '/solutions/', # Marketing landing pages (e.g. google.com/products/...)
    'llms.txt', 'llms-full.txt', '.well-known', # Meta files
    'sitemap.xml', 'robots.txt' # Bot files
]

# DOMAIN BLACKLIST: Sites found in your list that are clearly NOT AI tools.
# This prevents manual review of celebrity sites or random news articles.
DOMAIN_BLACKLIST = [
    # Celebrities / Musicians
    'brunomars.com', 'edsheeran.com', 'katyperry.com', 'ladygaga.com', 
    'michaeljackson.com', 'taylorswift.com', 'beyonce.com', 'justinbiebermusic.com',
    'coldplay.com', 'adele.com', 'davidguetta.com', 'madonna.com',
    
    # News / Satire / Media / Archives
    'theonion.com', 'huffingtonpost.in', 'breakingnews.ie', 'unionleader.com', 
    'seacoastonline.com', 'wired.co.uk', 'businessofapps.com', 'techcrunch.com',
    'forbes.com', 'bloomberg.com', 'reuters.com', 'nytimes.com', 'wsj.com',
    'cjr.org', 'abc7.com', 'fox5dc.com', 'nbcnewyork.com', 'archive.md',
    'web.archive.org', 'explainshell.com',
    
    # Random / Shopping / Non-AI Utilities
    'uboat.net', 'mentalfloss.com', 'allaboutbirds.org', 'partzilla.com',
    'myanimelist.net', 'animenewsnetwork.com', 'lego.com', 'ikea.com',
    'amazon.com', 'ebay.com', 'etsy.com', 'walmart.com', # Retail (unless AWS/Azure)
    'link.xsolla.com', 'secure.2checkout.com', 'stripe.com', # Payment processors
    'files.pythonhosted.org', 'pypi.org', 'npmjs.com', # Code repos (libraries, not SaaS)
    '123homeschool4me.com', 'readingeggs.com', 'starfall.com', # General Kids Ed (often not AI)
    'gov.uk', 'usa.gov', 'europa.eu' # Government portals
]

# EXTENSION BLACKLIST: Remove direct file downloads
EXTENSION_BLACKLIST = ['.pdf', '.zip', '.tar.gz', '.xml', '.png', '.jpg', '.jpeg', '.mp4', '.css', '.js']

# 3. PROCESSING FUNCTION
def is_noise(url):
    # Handle empty or non-string URLs
    if pd.isna(url) or not isinstance(url, str):
        return True
        
    try:
        parsed = urlparse(url)
        path = parsed.path.lower()
        domain = parsed.netloc.lower()
        
        # A. Check Domain Blacklist
        # We strip 'www.' to ensure 'www.amazon.com' matches 'amazon.com'
        clean_domain = domain.replace('www.', '')
        if any(bad_domain in clean_domain for bad_domain in DOMAIN_BLACKLIST):
            return True
            
        # B. Check Path Blacklist
        # We iterate through the blacklist to see if the path contains these segments
        if any(bad_word in path for bad_word in PATH_BLACKLIST):
            return True

        # C. Check File Extensions
        if any(path.endswith(ext) for ext in EXTENSION_BLACKLIST):
            return True
            
        # D. Special Handling for Hugging Face (Preserve models, remove docs)
        if 'huggingface.co' in domain:
            if '/docs' in path or '/blog' in path or '/pricing' in path:
                return True
            return False # Keep models, datasets, spaces

        return False # If it passes all checks, it's potentially a valid AI service
    except:
        return True # Remove malformed URLs

# 4. EXECUTION
try:
    print("Loading dataset...")
    # Attempt to read with different encodings just in case
    try:
        df = pd.read_csv(INPUT_FILE, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(INPUT_FILE, encoding='latin1')
        
    print(f"Original Rows: {len(df)}")

    # Apply the filter
    print("Filtering noise...")
    df['is_noise'] = df['Extracted URL'].apply(is_noise)

    # Split the data
    df_clean = df[df['is_noise'] == False].drop(columns=['is_noise'])
    df_noise = df[df['is_noise'] == True].drop(columns=['is_noise'])

    # Save files
    df_clean.to_csv(OUTPUT_CLEAN_FILE, index=False)
    df_noise.to_csv(OUTPUT_NOISE_FILE, index=False)

    print("-" * 30)
    print(f"Process Complete.")
    print(f"Cleaned Data: {len(df_clean)} rows (Saved to {OUTPUT_CLEAN_FILE})")
    print(f"Removed Noise: {len(df_noise)} rows (Saved to {OUTPUT_NOISE_FILE})")
    print("-" * 30)
    print("Check 'final_tools_1M_removed_noise.csv' to ensure no valid tools were accidentally removed.")

except FileNotFoundError:
    print(f"Error: The file '{INPUT_FILE}' was not found. Please check the filename.")
except Exception as e:
    print(f"An error occurred: {e}")