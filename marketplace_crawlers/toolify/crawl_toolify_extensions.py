import asyncio
import pandas as pd
import os
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
# The base URLs for the extension sections
BASE_URLS = [
    "https://www.toolify.ai/browser-extension",
    "https://www.toolify.ai/browser-extension/most-installed"
]

# We will start at page 1 and increment until we find no tools
MAX_PAGES_TO_CHECK = 20  # Safety limit, increase if needed (you mentioned ~7 pages)
EXISTING_FILE = "toolify_harvest.csv"

async def harvest_paginated_category(page, base_url):
    collected_tools = []
    
    for i in range(1, MAX_PAGES_TO_CHECK + 1):
        # Construct URL: The first page is often just the base URL, page 2 is base/page/2
        if i == 1:
            target_url = base_url
        else:
            target_url = f"{base_url}/page/{i}"
            
        print(f"--- 📄 Visiting Page {i}: {target_url} ---")
        
        try:
            response = await page.goto(target_url, timeout=30000, wait_until="domcontentloaded")
            # Check if page exists (Toolify might redirect to home or 404 if page doesn't exist)
            if response.status == 404 or page.url == "https://www.toolify.ai/":
                print("   🛑 Page not found or redirected. Stopping this category.")
                break
            
            # Small wait for table render
            await asyncio.sleep(2)
            
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # --- EXTRACTION STRATEGY FOR TABLES ---
            # Based on your snippet, tools are in a table structure
            # We look for 'a' tags with class 'go-tool' or links containing '/tool/'
            
            # Strategy 1: Look for the specific row structure
            rows = soup.find_all('tr') # Assuming it's a table structure based on <td>
            
            # If standard <tr> tags aren't used for rows, we fallback to the "go-tool" class you identified
            if len(rows) < 2: 
                # Fallback: Find all tool links directly
                tool_links = soup.find_all('a', href=True)
                found_on_page = 0
                for link in tool_links:
                    href = link['href']
                    if "/tool/" in href and "toolify.ai" not in href: # Relative internal links
                        tool_name = link.get('title', link.get_text(strip=True))
                        if not tool_name: continue # Skip empty links
                        
                        full_url = f"https://www.toolify.ai{href}"
                        
                        collected_tools.append({
                            "tool_name": tool_name,
                            "internal_detail_url": full_url,
                            "short_description": "Browser Extension (See detail page)", # Table view often has less text
                            "source_list": base_url
                        })
                        found_on_page += 1
            else:
                # Table Strategy (Better for accuracy if structure exists)
                found_on_page = 0
                for row in rows:
                    # Try to find the link in the row
                    link = row.find('a', href=lambda x: x and '/tool/' in x)
                    if link:
                        href = link['href']
                        full_url = f"https://www.toolify.ai{href}"
                        
                        # Try to find name text
                        text_link = row.find('a', title=True)
                        name = text_link['title'] if text_link else link.get_text(strip=True)
                        
                        # Try to find description or category in the row cells
                        # (We keep it simple for now to match your previous schema)
                        
                        collected_tools.append({
                            "tool_name": name,
                            "internal_detail_url": full_url,
                            "short_description": "Browser Extension",
                            "source_list": base_url
                        })
                        found_on_page += 1

            print(f"   ✅ Found {found_on_page} tools on page {i}")
            
            if found_on_page == 0:
                print("   ⚠️ No tools found on this page. Assuming end of list.")
                break
                
        except Exception as e:
            print(f"   ❌ Error on page {i}: {e}")
            break
            
    return collected_tools

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        new_data = []
        
        # 1. Crawl the new Extension pages
        for base_url in BASE_URLS:
            tools = await harvest_paginated_category(page, base_url)
            new_data.extend(tools)
            
        await browser.close()
        
        # 2. Load Existing Data (if available)
        if os.path.exists(EXISTING_FILE):
            print(f"\n📂 Loading existing {EXISTING_FILE}...")
            df_existing = pd.read_csv(EXISTING_FILE)
            initial_count = len(df_existing)
        else:
            print(f"\n✨ Creating new {EXISTING_FILE}...")
            df_existing = pd.DataFrame()
            initial_count = 0
            
        # 3. Combine and Deduplicate
        if new_data:
            df_new = pd.DataFrame(new_data)
            
            # Combine
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            
            # Deduplicate based on 'internal_detail_url'
            # We keep 'first' so original data isn't overwritten, or 'last' if you want updates.
            # Let's keep 'last' to update metadata source info.
            df_final = df_combined.drop_duplicates(subset=['internal_detail_url'], keep='last')
            
            df_final.to_csv(EXISTING_FILE, index=False)
            
            added_count = len(df_final) - initial_count
            print(f"\n🎉 MERGE COMPLETE")
            print(f"   Previous Total: {initial_count}")
            print(f"   New Tools Found: {len(df_new)}")
            print(f"   Truly New Added: {added_count}")
            print(f"   New Grand Total: {len(df_final)}")
        else:
            print("No new data found to append.")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())