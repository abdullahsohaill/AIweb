import pandas as pd
from urllib.parse import urlparse

def get_fqdn(url):
    """Extracts the fully qualified domain name (fqdn) from a URL."""
    try:
        # Use urlparse to get the network location and remove 'www.'
        return urlparse(url).netloc.replace('www.', '')
    except Exception:
        return None

# 1. Define all the URLs from the marketplace/directory list
urls = [
    "https://aimlapi.com/", "https://agent.ai/agents", "https://agentarcade.net/agent/",
    "https://theresanaiforthat.com/", "https://saasaitools.com/", "https://www.futuretools.io/",
    "https://appscribed.com/", "https://easywithai.com/", "https://www.futurepedia.io/ai-tools",
    "https://whattheai.tech/", "https://ai-hunter.io/", "https://rapidapi.com/",
    "https://www.aitoolnet.com/", "https://dang.ai/", "https://www.aimarketing.directory/",
    "https://marsx.dev/ai-startups/", "https://aitrendz.xyz/", "https://aitoolsarena.com/",
    "https://aitools.fyi/", "https://toolspedia.io/", "https://aiagentsdirectory.com/categories",
    "https://www.gptacademy.co/", "https://www.startupaitools.com/", "https://aitoolsdirectory.com/",
    "https://www.aitoolhunt.com/", "https://www.gptdemo.net/", "https://aitoolsguide.com/",
    "https://aitoptools.com/", "https://victrays.com/", "https://aitoolguru.com/",
    "https://aitoolboard.com/", "https://uneedbest.com/", "https://topai.tools/",
    "https://appsandwebsites.com/", "https://www.tenereteam.com/ai-tool", "https://aicenter.ai/",
    "https://www.insidr.ai/ai-tools/", "https://toolscout.ai/", "https://domore.ai/",
    "https://library.phygital.plus/", "https://www.aiwizard.ai/", "https://ai-search.io/",
    "https://aihunt.app/", "https://aitogrow.com/", "https://www.chataiapps.com/chat-ai-apps-latest-resources",
    "https://www.toolify.ai/ai-model", "https://nanai.tools/", "https://openfuture.ai/",
    "https://aitoolmall.com/", "https://ailib.ru/en/", "https://www.toolpilot.ai/",
    "https://aipediahub.com/", "https://nextgentools.me/", "https://poweredbyai.app/",
    "https://www.canopydirectory.com/", "https://saasbaba.com/", "https://lookaitools.com/",
    "https://aitoolsup.com/", "https://awesomeaitools.com/", "https://www.humanornot.co/",
    "https://infrabase.ai/", "https://www.thetoolbus.ai/", "https://groupify.ai/",
    "https://aiagentslive.com/", "https://api.market/", "https://www.toolkitly.com/tools",
    "https://madgenius.co/"
]

# 2. Get the unique fqdn list from these URLs
marketplace_fqdns = sorted(list(set([get_fqdn(url) for url in urls if get_fqdn(url)])))

# --- Analysis ---
try:
    # Load your filtered data CSV
    df = pd.read_csv("final_filtered_services.csv")

    # --- NEW: Overall Analysis of the Filtered File ---
    # Get a dataframe of unique FQDNs and their first associated rank
    unique_fqdns_df = df[['fqdn', 'domain_tranco_rank']].drop_duplicates(subset='fqdn')
    total_unique_fqdns = len(unique_fqdns_df)
    
    # Count how many of those unique FQDNs have a rank greater than -1
    total_ranked_unique_fqdns = unique_fqdns_df[unique_fqdns_df['domain_tranco_rank'] > -1].shape[0]
    
    print("--- Overall Filtered Data Summary ---")
    print(f"Total unique FQDNs in 'final_filtered_services.csv': {total_unique_fqdns}")
    print(f"Number of unique FQDNs with a Tranco rank (> -1): {total_ranked_unique_fqdns}")
    # --- END NEW SECTION ---

    # Find the services in your data that are also in the marketplace list
    matched_services_df = df[df['fqdn'].isin(marketplace_fqdns)]

    if not matched_services_df.empty:
        # Get unique matched fqdns and their ranks
        unique_matches = matched_services_df[['fqdn', 'domain_tranco_rank']].drop_duplicates().sort_values(by='fqdn')

        # Filter for only those with a valid Tranco rank
        ranked_matches = unique_matches[unique_matches['domain_tranco_rank'] > -1]

        # --- Output the marketplace-specific results ---
        total_matched_count = len(unique_matches)
        ranked_matched_count = len(ranked_matches)

        print("\n--- Marketplace Match Summary ---")
        print(f"Total unique marketplaces/directories found in your data: {total_matched_count}")
        print(f"Number of matched marketplaces with a Tranco rank (> -1): {ranked_matched_count}")
        
        print("\n--- List of Ranked Marketplaces/Directories Found ---")
        if ranked_matched_count > 0:
            print(ranked_matches.to_string(index=False))
        else:
            print("None of the matched marketplaces had a Tranco rank.")

    else:
        print("\nNo exact matches found between the provided marketplace/directory list and your 'final_filtered_services.csv' data.")

except FileNotFoundError:
    print("Error: 'final_filtered_services.csv' not found. Please ensure the file is in the same directory as the script.")
except KeyError as e:
    print(f"Error: A required column ({e}) was not found in the CSV. Please check your file's column names.")