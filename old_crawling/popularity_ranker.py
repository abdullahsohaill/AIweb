# A script to rank services by popularity using the Tranco list
import pandas as pd
import tldextract

# Load the Tranco list (assuming it's in 'tranco_list.csv' with a 'rank' and 'domain' column)
tranco_df = pd.read_csv('tranco_top_1m.csv')
tranco_map = pd.Series(tranco_df.rank.values, index=tranco_df.domain).to_dict()

# Load our classified services
services_df = pd.read_csv('classified_ai_services.csv')

def get_rank(url):
    try:
        domain = tldextract.extract(url).registered_domain
        return tranco_map.get(domain, None) # Return None if not in Tranco list
    except:
        return None

services_df['tranco_rank'] = services_df['source_url'].apply(get_rank)

# Filter out non-popular ones, or simply use the rank for sorting
popular_services_df = services_df.dropna(subset=['tranco_rank'])
popular_services_df = popular_services_df.sort_values(by='tranco_rank')

popular_services_df.to_csv('final_ranked_ai_services.csv', index=False)