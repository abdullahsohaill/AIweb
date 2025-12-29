import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys

# --- CONFIGURATION ---
START_URL = "https://bai.tools/explore"
OUTPUT_FILE = "baitools_harvest.csv"

# Safety settings
MAX_PAGES = 500         # Stop after this many pages to prevent infinite loops
RETRY_CHECKS = 3        # How many times to check for 'Next' button before quitting
RETRY_DELAY = 3.0       # Seconds to wait between checks

async def harvest_baitools():
    async with async_playwright() as p:
        print("--- 🚀 Harvesting Bai.tools ---")
        
        # Launch browser (Headless=False lets you monitor progress)
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        await page.goto(START_URL, timeout=60000, wait_until="domcontentloaded")
        await asyncio.sleep(2)

        all_tools = []
        page_num = 1
        
        while page_num <= MAX_PAGES:
            print(f"   📄 Scraping Page {page_num}...", end="\r")
            
            # 1. Parse Current Page
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find tool cards
            # We look for the specific structure based on your snippet
            # A good anchor is the 'h3' tag inside the card
            cards = soup.find_all('h3')
            
            current_count = 0
            for h3 in cards:
                try:
                    # The card container is usually a few parents up
                    # Let's traverse relative to the H3 to find siblings
                    
                    # 1. Name & Internal Link
                    name_link = h3.find('a')
                    if not name_link: continue
                    
                    tool_name = name_link.get_text(strip=True)
                    internal_slug = name_link.get('href')
                    
                    # Go up to the parent div that holds title + arrow button
                    header_div = h3.parent
                    
                    # 2. External Link (The arrow icon)
                    # It's a sibling of the H3: <a target="_blank" rel="dofollow" ...>
                    external_link = ""
                    ext_tag = header_div.find('a', attrs={'target': '_blank', 'rel': 'dofollow'})
                    if ext_tag:
                        external_link = ext_tag.get('href')
                    
                    # If we can't find it there, sometimes structure varies. 
                    # Let's assume we got it or it's empty.

                    # Go up to the main card container to find desc/tags
                    # Structure: div > div (header) ... div (desc) ... div (tags)
                    # H3 -> div -> div (wrapper)
                    card_body = header_div.parent.parent 
                    
                    # 3. Description
                    # Class: line-clamp-2
                    desc_tag = card_body.find(class_='line-clamp-2')
                    description = desc_tag.get_text(strip=True) if desc_tag else ""
                    
                    # 4. Categories
                    # Class: line-clamp-1 -> div -> a tags
                    tags = []
                    tags_wrapper = card_body.find(class_='line-clamp-1')
                    if tags_wrapper:
                        tag_links = tags_wrapper.find_all('a')
                        for t in tag_links:
                            tags.append(t.get_text(strip=True))
                    categories = ", ".join(tags)

                    all_tools.append({
                        "tool_name": tool_name,
                        "external_link": external_link,
                        "description": description,
                        "categories": categories,
                        "internal_slug": internal_slug
                    })
                    current_count += 1
                except Exception as e:
                    continue
            
            print(f"   📄 Page {page_num}: Found {current_count} tools.")

            # 2. Pagination Logic (Fault Tolerant)
            next_button_found = False
            for attempt in range(RETRY_CHECKS):
                # Selector: a[rel="next"] matches <a rel="next">Next »</a>
                next_btn = page.locator('a[rel="next"]')
                
                if await next_btn.count() > 0 and await next_btn.is_visible():
                    next_button_found = True
                    
                    # Click and wait for navigation
                    # We wait for URL to change to ensure we moved forward
                    current_url = page.url
                    try:
                        await next_btn.click()
                        # Wait for URL change or network idle
                        await page.wait_for_load_state("domcontentloaded")
                        await asyncio.sleep(2) # Safety buffer
                    except:
                        # Fallback: if click fails, just go to the href manually
                        href = await next_btn.get_attribute('href')
                        if href:
                            await page.goto(f"https://bai.tools{href}" if href.startswith("/") else href)
                            await asyncio.sleep(2)
                    
                    page_num += 1
                    break # Break retry loop, proceed to next page loop
                else:
                    # Not found yet, wait and check again
                    if attempt < RETRY_CHECKS - 1:
                        # Scroll down just in case it triggers visibility
                        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        await asyncio.sleep(RETRY_DELAY)
            
            if not next_button_found:
                print("      ✅ 'Next' button not found after retries. Crawl complete.")
                break
        
        await browser.close()
        return all_tools

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    # Deduplicate just in case
    df = df.drop_duplicates(subset=['tool_name', 'external_link'])
    
    # Reorder columns
    cols = ["tool_name", "external_link", "description", "categories", "internal_slug"]
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS!")
    print(f"   Total Unique Tools: {len(df)}")
    print(f"   Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_baitools())
    save_to_csv(data)