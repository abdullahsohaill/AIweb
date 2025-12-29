import pandas as pd
from urllib.parse import urlparse
from tqdm import tqdm

# --- CONFIGURATION ---
INPUT_SERVICES_FILE = "final_filtered_services.csv"
INPUT_TRANCO_FILE = "tranco_3Q5QL.csv"  # The new, full Tranco list
FINAL_OUTPUT_FILE = "final_services_cleaned.csv"

def get_fqdn(url):
    """A utility function to extract a clean FQDN from a URL."""
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception:
        return None

# --- PART 1: PROCESSING AND CLEANING THE DATA ---
def process_and_clean_data():
    """Main function to process, clean, re-rank, and save the data."""
    tqdm.pandas()

    # --- 1. Compile All Known Marketplace FQDNs ---
    print("Step 1: Compiling the master list of marketplace and directory FQDNs...")
    original_marketplace_urls = [
        "https://aimlapi.com/", "https://agent.ai/agents", "https://agentarcade.net/agent/",
        "https://theresanaiforthat.com/", "https://saasaitools.com/", "https://www.futuretools.io/",
        "https://appscribed.com/", "https://easywithai.com/", "https://www.futurepedia.io/ai-tools",
        "https://whattheai.tech/", "https://ai-hunter.io/", 
        "https://www.aitoolnet.com/", "https://dang.ai/", "https://www.aimarketing.directory/",
        "https://aitrendz.xyz/", "https://aitoolsarena.com/",
        "https://aitools.fyi/", "https://toolspedia.io/", "https://aiagentsdirectory.com/categories",
        "https://www.gptacademy.co/", "https://www.startupaitools.com/", "https://aitoolsdirectory.com/",
        "https://www.aitoolhunt.com/", "https://www.gptdemo.net/", "https://aitoolsguide.com/",
        "https://aitoptools.com/", "https://victrays.com/", "https://aitoolguru.com/",
        "https://aitoolboard.com/", "https://topai.tools/",
        "https://appsandwebsites.com/", "https://www.tenereteam.com/ai-tool", "https://aicenter.ai/",
        "https://www.insidr.ai/ai-tools/", "https://toolscout.ai/",
        "https://library.phygital.plus/", "https://www.aiwizard.ai/", "https://ai-search.io/",
        "https://aihunt.app/", "https://aitogrow.com/", "https://www.chataiapps.com/chat-ai-apps-latest-resources",
        "https://www.toolify.ai/ai-model", "https://nanai.tools/", "https://openfuture.ai/",
        "https://aitoolmall.com/", "https://ailib.ru/en/", "https://www.toolpilot.ai/",
        "https://aipediahub.com/", "https://nextgentools.me/", "https://poweredbyai.app/",
        "https://www.canopydirectory.com/", "https://saasbaba.com/", "https://lookaitools.com/",
        "https://aitoolsup.com/", "https://awesomeaitools.com/", "https://www.humanornot.co/",
        "https://infrabase.ai/", "https://www.thetoolbus.ai/",
        "https://aiagentslive.com/", "https://www.toolkitly.com/tools",
        "https://madgenius.co/"
    ]
    new_marketplace_fqdns = [
        "1000.tools", "100apps.org", "addaidirectory.com", "aeotools.space", "ai-findr.com",
        "ai-hunter.io", "ai-sites.net", "ai-tool-collection.vercel.app", "ai-tools-directory-seven-jade.vercel.app",
        "ai-tools.directory", "aiagentsdirectory.com", "aiagentslist.com", "aiai.tools", "aidirectory.org",
        "aidirectory.wiki", "aidirs.best", "aigotools.com", "aihubs.ai", "ailistz.com",
        "aimarketing.directory", "aipediahub.com", "aiplusyou.ai", "aiscout.tools", "aiscouts.org",
        "aisimplify.directory", "aitechviral.com", "aitoolboard.com", "aitoolbox.fyi", "aitoolbox.tools",
        "aitooldirectory.com", "aitooldr.com", "aitoolfinder.net", "aitoolguru.com", "aitoolhouse.com",
        "aitoolhunt.com", "aitoollist.org", "aitoolly.com", "aitoolmall.com", "aitoolnet.com", "aitools.directory",
        "aitools.fyi", "aitools.inc", "aitoolsarena.com", "aitoolsclub.com", "aitoolscorner.com",
        "aitoolsdirectory.com", "aitoolsexplorer.org", "aitoolsforme.com", "aitoolsguide.com", "aitoolslist.io",
        "aitoolslist.top", "aitoolsmagazine.com", "aitoolsmarketer.com", "aitoolspro.io", "aitoolsup.com",
        "aitoolswiki.com", "aitooltrek.com", "aitoolz.net", "aitoolzdir.com", "aitoolzs.com", "aitoprank.com",
        "aitoptools.com", "allaitools.tech", "allinai.tools", "alltheaitools.com", "appalist.com",
        "appsytools.com", "assistanthunt.com", "awesome-ai-writing.vercel.app",
        "awesomeai.cc", "awesomeaitools.com", "basedtools.ai", "best-ai-tools.org", "bestaiagents.directory",
        "bestaitoolsforthat.com", "bestofai.com", "bestofai.io", "bestofweb.site", "bestregards.app",
        "besttoolvault.com", "beyondaitools.com", "canopydirectory.com", "chataiapps.com", "clvrai.github.io",
        "coglist.com", "custom-ai-tool-directory-boilerplate.vercel.app", "devlibrary.withgoogle.com",
        "devtools.directory", "dir2ai.com", "directory.9d8.dev", "directory.llmstxt.cloud",
        "easywithai.com", "eliteai.tools", "findaitools.co", "findanaitools.com", "findcool.tools",
        "findmyaitool.com", "findsaastools.com", "free-ai-tools-directory.com", "freeaitool.ai",
        "freeaitools.fyi", "freeappsai.com", "freetopaitools.com", "futureagi.com", "futureagitools.com",
        "futurepedia.io", "futurepedia.wiki", "futuretools.io", "futuretools.link", "generativetools.io",
        "goodaibots.com", "goodaitools.com", "growthtoolz.com", "heybot.thesamur.ai", "huntfortools.com", "insanelycooltools.com", "insidr.ai",
        "launchdirectories.com", "learnaitools.io", "listyourtool.com", "llmstxt.directory", "lookaitools.com",
        "madgenius.co", "makerlist.io", "marketingtoolslist.com", "nextaitool.com",
        "nextgentools.me", "opensaas.directory", "opentools.ai", "poweruptools.com", "productlistdir.com",
        "saasaitools.com", "saashubdirectory.com",
        "saastoolsdir.com", "saaswheel.com", "searchaidirectory.com", "spaceofai.tools",
        "stackdirectory.com", "startaitools.com", "startupaitools.com", "startupcollections.com",
        "startuptoolchain.com", "startuptoolslist.com", "submitaitools.org",
        "supertools.therundown.ai", "thataicollection.com", "theaigeneration.com", "theailibrary.co",
        "thecoretools.com", "thekeytools.com", "themegatools.com", "thenextaidirectory.com", "thenextaitool.com",
        "theresanai.com", "theresanaiforthat.com", "thetoolbus.ai", "thetoolsverse.com", "tinytoolhub.com",
        "tool-url.com", "toolai.io", "toolbaz.org", "toolbuilder.ai", "toolcosmos.com", "tooldirectory.ai",
        "toolfinddir.com", "toolfinder.wiki", "toolfolio.io", "toolify.ai", "toolinsidr.com", "toolio.ai",
        "tooljourney.com", "toolkitly.com", "toollist.ai", "toolnest.ai",
        "toolpilot.ai", "toolprism.com", "toolpulse.ai", "tools-ai.online", "tools-ai.xyz", "toolsai.net",
        "toolsapp.cc", "toolscout.ai", "toolsfine.com", "toolsforcreators.com", "toolshubai.com",
        "toolsignal.com", "toolslisthq.com", "toolsnocode.com", "toolspedia.io", "toolss-eight.vercel.app",
        "toolsunderradar.com", "tooltips.ai", "toolwave.io", "top100aitools.com",
        "topai.tools", "topaitoolshub.com", "topapps.ai", "topcreator.com", "toptools.ai", "toptrendtools.com",
        "victrays.com", "webdirectorycenter.com", "whatisaitools.com",
        "whattheai.tech", "xcollection.com", "theresanaiforthat.com", "futurepedia.io", "futuretools.io", 
        "top.ai.tools", "aitoolsdirectory.com", "startupaitools.com", "saasaitools.com", "awesomeaitools.com", 
        "allaitools.tech", "findaitools.co", "aitoolnet.com", "aitoolmall.com", "toolpilot.ai", "poweredbyai.app", 
        "infrabase.ai", "thetoolbus.ai", "siteefy.com", "aixploria.com", "altern.ai", "appliedai.tools",
        "bai.tools", "directory.surf", "foundr.ai", "inventlist.com", "microlaunch.net", "saasfield.com", "saasroots.com",
        "theapptools.com", "weliketools.com"
    ]
    initial_fqdns = {get_fqdn(url) for url in original_marketplace_urls if get_fqdn(url)}
    combined_marketplace_set = set(initial_fqdns).union(set(new_marketplace_fqdns))
    print(f"   -> Compiled a total of {len(combined_marketplace_set)} unique marketplace/directory FQDNs.")

    try:
        print(f"\nStep 2: Loading '{INPUT_SERVICES_FILE}' and '{INPUT_TRANCO_FILE}'...")
        df_services = pd.read_csv(INPUT_SERVICES_FILE)
        df_tranco = pd.read_csv(INPUT_TRANCO_FILE, header=None, names=['rank', 'fqdn'])
        print(f"   -> Loaded {len(df_services):,} service candidates.")
        print(f"   -> Loaded {len(df_tranco):,} Tranco rank entries.")
    except FileNotFoundError as e:
        print(f"Error: Could not find a required file: {e.filename}. Aborting.")
        return

    print("\nStep 3: De-duplicating marketplace and directory entries...")
    marketplaces_df = df_services[df_services['fqdn'].isin(combined_marketplace_set)]
    non_marketplaces_df = df_services[~df_services['fqdn'].isin(combined_marketplace_set)]
    marketplaces_deduplicated_df = marketplaces_df.drop_duplicates(subset='fqdn', keep='first')
    df_processed = pd.concat([non_marketplaces_df, marketplaces_deduplicated_df], ignore_index=True)
    print(f"   -> Removed {len(marketplaces_df) - len(marketplaces_deduplicated_df)} duplicate marketplace rows. New total: {len(df_processed)}.")

    print("\nStep 4: Updating Tranco ranks for the entire dataset using the full list...")
    tranco_map = pd.Series(df_tranco['rank'].values, index=df_tranco['fqdn']).to_dict()
    df_processed['domain_tranco_rank'] = df_processed['fqdn'].progress_apply(lambda fqdn: tranco_map.get(str(fqdn), -1))
    print("   -> Tranco rank update complete.")

    print("\nStep 5: Re-sorting the data based on new Tranco ranks...")
    df_processed['sort_rank'] = df_processed['domain_tranco_rank'].apply(lambda x: 100_000_001 if x == -1 else x)
    df_processed = df_processed.sort_values(by=['sort_rank', 'fqdn'], ascending=[True, True])
    df_processed = df_processed.drop(columns=['sort_rank'])
    print("   -> Sorting complete.")

    print(f"\nStep 6: Saving the cleaned and updated data to '{FINAL_OUTPUT_FILE}'...")
    df_processed.to_csv(FINAL_OUTPUT_FILE, index=False)
    print("   -> Save successful.")
    return combined_marketplace_set


# --- PART 2: ANALYSIS OF THE NEWLY CREATED FILE ---
def analyze_cleaned_data(marketplace_set):
    """Loads the cleaned file and performs a full analysis."""
    print("\n--- Starting Analysis on the Cleaned Data ---")
    
    try:
        df_cleaned = pd.read_csv(FINAL_OUTPUT_FILE)
    except FileNotFoundError:
        print(f"Error: Could not find the newly created file '{FINAL_OUTPUT_FILE}'. Cannot perform analysis.")
        return

    # --- Overall Data Overview ---
    print("\n--- Overall Data Overview ---")
    total_entries = len(df_cleaned)
    unique_fqdns_df = df_cleaned.drop_duplicates(subset=['fqdn'])
    total_unique_fqdns = len(unique_fqdns_df)
    print(f"Total entries in the cleaned dataset: {total_entries:,}")
    print(f"Total unique FQDNs in the cleaned dataset: {total_unique_fqdns:,}")

    # --- Overall Tranco Rank Analysis ---
    print("\n--- Overall Tranco Rank Analysis (on Unique FQDNs) ---")
    ranked_fqdns_df = unique_fqdns_df[unique_fqdns_df['domain_tranco_rank'] > -1]
    ranked_count = len(ranked_fqdns_df)
    unranked_count = total_unique_fqdns - ranked_count
    ranked_percentage = (ranked_count / total_unique_fqdns) * 100 if total_unique_fqdns > 0 else 0
    
    print(f"Ranked Unique FQDNs (in Tranco List): {ranked_count:,} ({ranked_percentage:.2f}%)")
    print(f"Unranked Unique FQDNs (not in Tranco List): {unranked_count:,}")

    # --- Marketplace-Specific Analysis ---
    print("\n--- Marketplace & Directory Analysis ---")
    found_marketplaces_df = unique_fqdns_df[unique_fqdns_df['fqdn'].isin(marketplace_set)]
    total_marketplaces_found = len(found_marketplaces_df)
    
    if total_marketplaces_found > 0:
        ranked_marketplaces = found_marketplaces_df[found_marketplaces_df['domain_tranco_rank'] > -1].sort_values('domain_tranco_rank')
        unranked_marketplaces = found_marketplaces_df[found_marketplaces_df['domain_tranco_rank'] == -1].sort_values('fqdn')
        
        print(f"Total unique marketplaces/directories found in dataset: {total_marketplaces_found}")
        print(f"   -> Number of RANKED marketplaces: {len(ranked_marketplaces)}")
        print(f"   -> Number of UNRANKED marketplaces: {len(unranked_marketplaces)}")

        if not ranked_marketplaces.empty:
            print("\n--- List of RANKED Marketplaces Found ---")
            print(ranked_marketplaces[['fqdn', 'domain_tranco_rank']].to_string(index=False))
        
        if not unranked_marketplaces.empty:
            print("\n--- List of UNRANKED Marketplaces Found ---")
            print(unranked_marketplaces['fqdn'].to_string(index=False))
    else:
        print("No FQDNs from the marketplace list were found in the final dataset.")

    print("\n--- Analysis Complete ---")


if __name__ == "__main__":
    master_marketplace_list = process_and_clean_data()
    if master_marketplace_list:
        analyze_cleaned_data(master_marketplace_list)