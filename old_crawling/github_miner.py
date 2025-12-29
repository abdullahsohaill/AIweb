# A script to systematically mine GitHub for AI service URLs
import github
import re
import pandas as pd
import time

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
g = github.Github(GITHUB_TOKEN)

# Use the same queries from Phase 1, but add GitHub-specific ones
with open('search_queries.txt', 'r') as f:
    queries = [line.strip() + " in:readme,description" for line in f.readlines()]

results = []
processed_repos = set()

for query in queries:
    print(f"Searching GitHub repos for: {query}")
    try:
        repos = g.search_repositories(query=query, sort='stars', order='desc')
        for repo in repos[:30]: # Get top 30 repos per query
            if repo.full_name in processed_repos: continue
            
            try:
                readme_content = repo.get_readme().decoded_content.decode('utf-8')
                urls = re.findall(r'https?://[^\s()<>"]+', readme_content)
                for url in urls:
                    results.append({'url': url, 'source_repo': repo.html_url})
                processed_repos.add(repo.full_name)
            except Exception:
                continue
    except Exception as e:
        print(f"GitHub API error: {e}")
        time.sleep(60) # Wait if rate limited

df = pd.DataFrame(results)
df.to_csv('github_search_results.csv', index=False)