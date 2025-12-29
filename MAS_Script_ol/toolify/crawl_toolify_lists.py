import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import time

# --- CONFIGURATION ---
# The 3 specific pages you identified
TARGET_URLS = [
    "https://www.toolify.ai/new",
    "https://www.toolify.ai/most-saved",
    "https://www.toolify.ai/most-used"
]

OUTPUT_FILE = "toolify_harvest.csv"
SCROLL_LOOPS = 50       # How many times to scroll down (50 * ~20 tools = ~1000 tools per run)
SCROLL_DELAY = 2        # Seconds to wait for new tools to load

async def harvest_list(page, url):
    print(f"--- 🚀 Visiting: {url} ---")
    try:
        await page.goto(url, timeout=90000, wait_until="domcontentloaded")
        await asyncio.sleep(3) # Allow initial hydrate

        # --- INFINITE SCROLL LOOP ---
        print(f"   🔄 Starting infinite scroll ({SCROLL_LOOPS} loops)...")
        for i in range(SCROLL_LOOPS):
            # Scroll to the bottom of the page
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            
            # Wait for content to load
            await asyncio.sleep(SCROLL_DELAY)
            
            # Optional: Check for and click a "Load More" button if the scroll stops working
            # Toolify sometimes switches to a button at deep scroll depths
            try:
                load_more = page.locator("text='Load More'")
                if await load_more.is_visible():
                    await load_more.click()
                    await asyncio.sleep(2)
            except:
                pass

            if i % 5 == 0:
                print(f"      Scroll {i}/{SCROLL_LOOPS} complete...")

        # --- PARSE CONTENT ---
        print("   📥 Parsing HTML content...")
        # We grab the raw HTML and use BeautifulSoup because it's faster for thousands of items
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        # Based on your HTML dump, tools are inside 'div.tool-item'
        cards = soup.find_all('div', class_='tool-item')
        print(f"   ✅ Found {len(cards)} tools on this page.")

        page_results = []
        for card in cards:
            try:
                # 1. Extract Name
                name_tag = card.find(class_='tool-name')
                tool_name = name_tag.get_text(strip=True) if name_tag else "Unknown"

                # 2. Extract Description
                desc_tag = card.find(class_='tool-desc')
                description = desc_tag.get_text(strip=True) if desc_tag else ""

                # 3. Extract URL (Internal)
                # The link is usually on the anchor tag wrapping the content or inside it
                anchor = card.find('a')
                raw_link = anchor['href'] if anchor else ""
                
                # Normalize URL
                internal_url = ""
                if raw_link:
                    if raw_link.startswith("http"):
                        internal_url = raw_link # It's already an external/absolute link
                    else:
                        internal_url = f"https://www.toolify.ai{raw_link}" # Fix relative link

                # Only save if we found a valid link
                if internal_url:
                    page_results.append({
                        "tool_name": tool_name,
                        "short_description": description,
                        "internal_detail_url": internal_url,
                        "source_list": url  # Track which page we found it on
                    })
            except Exception as e:
                continue
        
        return page_results

    except Exception as e:
        print(f"   ❌ Error crawling {url}: {e}")
        return []

async def main():
    async with async_playwright() as p:
        # Launch browser (Headless=False lets you watch it work, change to True for background run)
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        all_data = []
        page = await context.new_page()

        # Iterate through the 3 URLs you provided
        for target in TARGET_URLS:
            data = await harvest_list(page, target)
            all_data.extend(data)

        await browser.close()

        # --- SAVE & DEDUPLICATE ---
        if all_data:
            df = pd.DataFrame(all_data)
            # Remove duplicates (a tool might appear in 'New' AND 'Most Saved')
            initial_len = len(df)
            df = df.drop_duplicates(subset=['internal_detail_url'])
            
            df.to_csv(OUTPUT_FILE, index=False)
            print(f"\n🎉 SUCCESS!")
            print(f"   Harvested: {initial_len} tools")
            print(f"   Unique:    {len(df)} tools")
            print(f"   Saved to:  {OUTPUT_FILE}")
        else:
            print("\n⚠️ No data found. Check internet connection or website layout changes.")

if __name__ == "__main__":
    # Fix for Windows asyncio loops if needed
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())