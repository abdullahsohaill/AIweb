import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FILE = "FINAL_VETTING_LIST.csv"
OUTPUT_FILE = "FINAL_RANKED_SERVICES_CLEANED.csv"

# --- EXCLUSION LIST (The "Noise" List) ---
# Organized for O(1) lookup speed.
# Includes: News/Media, Big Tech, Gov/Edu, Retail, Adult, Spam, and Generic Consumer Sites.

EXCLUDED_DOMAINS = {
    # --- News, Media, Magazines & Blogs ---
    "11alive.com", "20minutes.fr", "404media.co", "9to5google.com", "aa.com.tr",
    "abc7.com", "aljazeera.com", "allocine.fr", "asahi.com", "axios.com",
    "bbc.co.uk", "news.bbc.co.uk", "billboard.com", "bloomberg.com", "bostonglobe.com",
    "businessinsider.com", "businessinsider.com.au", "buzzfeed.com",
    "cnbc.com", "cnet.com", "cnn.com", "articles.cnn.com", "dailymail.co.uk",
    "economictimes.indiatimes.com", "economist.com", "engadget.com",
    "financialtimes.com", "forbes.com", "councils.forbes.com", "fortune.com",
    "foxbusiness.com", "foxnews.com", "ft.com", "gizmodo.com", "guardian.co.uk",
    "hindustantimes.com", "huffingtonpost.in", "independent.co.uk", "latimes.com",
    "lefigaro.fr", "leparisien.fr", "lepoint.fr", "lequipe.fr", "mashable.com",
    "medium.com", "mirror.co.uk", "msnbc.com", "nationalgeographic.com",
    "nbcnews.com", "newrepublic.com", "news.google.com", "news.sky.com",
    "news.yahoo.com", "newsweek.pl", "nytimes.com", "static01.nyt.com",
    "pcmag.com", "politico.eu", "project-syndicate.org", "propublica.org",
    "psychologytoday.com", "reuters.com", "rollingstone.com", "scientificamerican.com",
    "techcrunch.com", "techradar.com", "theguardian.com", "theonion.com",
    "thestreet.com", "thesun.co.uk", "theverge.com", "time.com", "usatoday.com",
    "variety.com", "vice.com", "vox.com", "wallstreetcn.com", "washingtonexaminer.com",
    "washingtonpost.com", "wired.com", "wired.co.uk", "wsj.com", "zdnet.com",

    # --- Big Tech, Platforms & Infrastructure (Non-Tools) ---
    "abc.xyz", "about.google", "aboutamazon.com", "adobe.com", "amazon.com",
    "amazon.ca", "amazon.co.jp", "amazon.co.uk", "amazon.com.au", "amazon.com.br",
    "amazon.com.mx", "amazon.com.tr", "amazon.de", "amazon.es", "amazon.fr",
    "amazon.in", "amazon.it", "amazon.nl", "amazon.science", "android.com",
    "aol.com", "apple.com", "apple.co", "aws.amazon.com", "bing.com", "box.com",
    "chrome.google.com", "chromewebstore.google.com", "cisco.com", "cloudflare.com",
    "dell.com", "discord.com", "docker.com", "dropbox.com", "facebook.com",
    "github.com", "github.blog", "gitlab.com", "gmail.com", "godaddy.com",
    "google.com", "ibm.com", "icloud.com", "intel.com", "linkedin.com", "live.com",
    "microsoft.com", "mozilla.org", "msn.com", "netflix.com", "nvidia.com",
    "office.com", "oracle.com", "paypal.com", "pinterest.com", "play.google.com",
    "reddit.com", "salesforce.com", "samsung.com", "slack.com", "snapchat.com",
    "spotify.com", "stripe.com", "telegram.org", "tiktok.com", "trello.com",
    "twitch.tv", "twitter.com", "x.com", "uber.com", "vimeo.com", "whatsapp.com",
    "yahoo.com", "youtube.com", "zoom.us", "zoom.com",

    # --- Government, Education & NGOs ---
    "aclu.org", "cdc.gov", "cia.gov", "congress.gov", "consumerfinance.gov",
    "coursera.org", "ed.gov", "epa.gov", "europa.eu", "fbi.gov", "fda.gov",
    "gov.uk", "harvard.edu", "irs.gov", "loc.gov", "mit.edu", "nasa.gov",
    "nih.gov", "noaa.gov", "nps.gov", "stanford.edu", "un.org", "whitehouse.gov",
    "who.int", "yale.edu", "australia.gov.au", "canada.ca", "gov.ca.gov",
    "house.gov", "senate.gov", "usgs.gov", "worldbank.org",

    # --- Retail, E-commerce & Job Boards ---
    "airbnb.com", "bestbuy.com", "booking.com", "craigslist.org", "ebay.com",
    "etsy.com", "expedia.com", "fiverr.com", "glassdoor.com", "homedepot.com",
    "indeed.com", "ikea.com", "kickstarter.com", "lowes.com", "macys.com",
    "nike.com", "target.com", "tripadvisor.com", "upwork.com", "walmart.com",
    "wayfair.com", "zillow.com", "99designs.com", "gumroad.com", "appsumo.com",

    # --- Adult Content (Tube sites / Not tools) ---
    "321sexchat.com", "pornhub.com", "xhamster.com", "xnxx.com", "xvideos.com",
    "youporn.com", "onlyfans.com",

    # --- Spam / Affiliate / Broken / Placeholder ---
    "clickbank.net", "jvzoo.com", "warriorplus.com", "tinyurl.com", "bit.ly",
    "t.ly", "goo.gle", "g.co", "amzn.to", "youtu.be",

    # --- Miscellaneous Noise (Stock, Encyclopedias, Games, etc.) ---
    "1010clipart.com", "123homeschool4me.com", "123rf.com", "1happybirthday.com",
    "2-spyware.com", "500px.com", "abcmouse.com", "abcya.com", "accountable.de",
    "accuweather.com", "acdsystems.go2cloud.org", "ace-eco.org", "acfr.usyd.edu.au",
    "achieved-bellflower-4d6.notion.site", "acin.tuwien.ac.at", "actcast.io",
    "adac.de", "allrecipes.com", "almanac.com", "almowafir.com", "archive.org",
    "arxiv.org", "asplos-conference.org", "avma.org", "bank-security.medium.com",
    "bedtimemath.org", "behance.net", "britannica.com", "coolmathgames.com",
    "dictionary.com", "doi.org", "fantasynamegenerators.com", "flickr.com",
    "goodreads.com", "healthline.com", "howstuffworks.com", "imdb.com",
    "issuu.com", "jstor.org", "merriam-webster.com", "patreon.com",
    "producthunt.com", "quora.com", "rottentomatoes.com", "scribd.com",
    "shutterstock.com", "si.edu", "slideshare.net", "soundcloud.com",
    "sourceforge.net", "stackoverflow.com", "statista.com", "steampowered.com",
    "ted.com", "tumblr.com", "unsplash.com", "webmd.com", "wikihow.com",
    "wikipedia.org", "wix.com", "wordpress.com", "wordpress.org", "yelp.com"
}

def is_blacklisted(fqdn):
    """
    Checks if an FQDN matches the exact exclusion list OR
    contains specific spam patterns (like clickbank subdomains).
    """
    if pd.isna(fqdn):
        return False
    
    fqdn = str(fqdn).lower().strip()
    
    # 1. Direct match against the set
    if fqdn in EXCLUDED_DOMAINS:
        return True
    
    # 2. Pattern Matching for dynamic spam/affiliate subdomains
    spam_patterns = [
        "hop.clickbank.net",
        "go2cloud.org",
        "p.aws",
        "redirectingat.com",
        "awin1.com",
        "anrdoezrs.net",
        "tkqlhce.com",
        "pxf.io",
        "sjv.io",
        "grsm.io"
    ]
    
    for pattern in spam_patterns:
        if pattern in fqdn:
            return True
            
    return False

def main():
    print("--- 🧹 STARTING NOISE DOMAIN CLEANUP ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file '{INPUT_FILE}' not found.")
        return

    # 1. Load Data
    print("\n1️⃣  Loading Dataset...")
    try:
        df = pd.read_csv(INPUT_FILE)
        initial_count = len(df)
        print(f"   ✅ Loaded {initial_count:,} rows.")
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    # 2. Filtering
    print("\n2️⃣  Filtering Noise Domains...")
    
    # Identify rows to remove
    # We use the 'Domain (FQDN)' column. If not present, try 'fqdn' or 'domain'.
    fqdn_col = None
    possible_cols = ['Domain (FQDN)', 'fqdn', 'domain', 'url']
    for col in possible_cols:
        if col in df.columns:
            fqdn_col = col
            break
            
    if not fqdn_col:
        print(f"❌ Error: Could not find a domain column. Checked: {possible_cols}")
        return

    print(f"   ℹ️  Using column: '{fqdn_col}'")

    # Create a boolean mask for rows that ARE blacklisted
    noise_mask = df[fqdn_col].apply(is_blacklisted)
    
    # Separate data
    noise_df = df[noise_mask]
    clean_df = df[~noise_mask]
    
    # 3. Statistics
    removed_count = len(noise_df)
    remaining_count = len(clean_df)
    
    print("\n📊 --- CLEANUP STATISTICS ---")
    print(f"   Total Rows Processed:   {initial_count:,}")
    print(f"   Rows Removed (Noise):   {removed_count:,} (-{(removed_count/initial_count)*100:.1f}%)")
    print(f"   Rows Remaining:         {remaining_count:,}")
    
    # Top removed domains (to verify)
    if removed_count > 0:
        print("\n   🗑️  Top 15 Removed Domains:")
        print(noise_df[fqdn_col].value_counts().head(15).to_string())

    # 4. Save
    print(f"\n3️⃣  Saving cleaned list to '{OUTPUT_FILE}'...")
    clean_df.to_csv(OUTPUT_FILE, index=False)
    print("   ✅ Done.")

if __name__ == "__main__":
    main()