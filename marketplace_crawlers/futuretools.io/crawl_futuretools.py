import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
TARGET_URL = "https://www.futuretools.io/?sort-asc=for-sorting"
OUTPUT_FILE = "futuretools_complete.csv"

# --- SCROLL SETTINGS ---
# FutureTools has ~3800+ items. 
# We need a robust loop to ensure we get them all.
SCROLL_DELAY = 2.0        # Time to wait after scrolling
MAX_NO_NEW_ITEMS = 5      # How many times to retry if no new items appear

async def harvest_futuretools():
    async with async_playwright() as p:
        print("--- 🚀 Launching Browser ---")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print(f"--- 🌐 Visiting: {TARGET_URL} ---")
        # Large timeout because loading 4000 items is heavy
        await page.goto(TARGET_URL, timeout=120000, wait_until="domcontentloaded")
        
        print("   ⏳ Waiting for initial list to load...")
        try:
            await page.wait_for_selector('div.tool-home', timeout=20000)
        except:
            print("   ⚠️ Warning: Initial selector wait timed out, proceeding anyway...")

        # --- INFINITE SCROLL LOOP ---
        print("   🔄 Starting Infinite Scroll...")
        previous_count = 0
        no_change_counter = 0
        
        while True:
            # 1. Scroll to bottom
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await asyncio.sleep(SCROLL_DELAY)

            # 2. Check how many tools are currently loaded
            current_count = await page.locator('div.tool-home').count()
            
            if current_count > previous_count:
                print(f"      ⬇️  Loaded {current_count} tools...")
                previous_count = current_count
                no_change_counter = 0 # Reset counter because we found new stuff
            else:
                # 3. No new items? Try to click "Load More" or wiggle the scroll
                no_change_counter += 1
                print(f"      ⚠️  No new items ({no_change_counter}/{MAX_NO_NEW_ITEMS})...")
                
                # Attempt to find/click a 'Load More' button (sometimes Jetboost uses one)
                try:
                    load_more = page.locator(".jetboost-load-more-button:visible")
                    if await load_more.count() > 0:
                        await load_more.click()
                        await asyncio.sleep(3)
                        continue
                except:
                    pass

                # Wiggle scroll up and down to trigger lazy loaders
                await page.evaluate("window.scrollBy(0, -1000)")
                await asyncio.sleep(0.5)
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(1.5)

                # 4. Break condition
                if no_change_counter >= MAX_NO_NEW_ITEMS:
                    print(f"      🛑 Stopped. It seems all {current_count} tools are loaded.")
                    break

        # --- PARSING CONTENT ---
        print("   📥 Parsing HTML content...")
        content = await page.content()
        await browser.close()

        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all tool cards
        cards = soup.find_all('div', class_='tool-home')
        print(f"   ✅ Found {len(cards)} items in HTML. Extracting data...")

        results = []
        for card in cards:
            try:
                # --- 1. Tool Name & INTERNAL Profile Link ---
                # Looking for: <a href="/tools/0cody" class="tool-item-link---new">
                profile_tag = card.find('a', class_='tool-item-link---new')
                
                tool_name = "Unknown"
                profile_url = ""
                
                if profile_tag:
                    tool_name = profile_tag.get_text(strip=True)
                    raw_href = profile_tag.get('href', '')
                    # Fix relative URL
                    if raw_href.startswith('/'):
                        profile_url = f"https://www.futuretools.io{raw_href}"
                    else:
                        profile_url = raw_href

                # --- 2. EXTERNAL Website Link ---
                # Looking for: <a href="https://futuretools.link/..." class="tool-item-new-window---new">
                external_tag = card.find('a', class_='tool-item-new-window---new')
                website_url = ""
                
                if external_tag:
                    website_url = external_tag.get('href', '')

                # --- 3. Description ---
                desc_tag = card.find(class_='tool-item-description-box---new')
                description = desc_tag.get_text(strip=True) if desc_tag else ""

                # --- 4. Categories/Tags ---
                tags = [t.get_text(strip=True) for t in card.find_all(class_='text-block-53')]
                tags_str = ", ".join(tags)

                # Save Data
                if tool_name:
                    results.append({
                        "tool_name": tool_name,
                        "description": description,
                        "profile_url": profile_url,      # The internal link (/tools/...)
                        "website_url": website_url,      # The external link (futuretools.link/...)
                        "categories": tags_str
                    })

            except Exception as e:
                # Skip bad items
                continue

        return results

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    # Remove duplicates based on the profile URL
    initial_len = len(df)
    df = df.drop_duplicates(subset=['profile_url'])
    
    print(f"\n📊 STATS:")
    print(f"   Raw Items: {initial_len}")
    print(f"   Unique:    {len(df)}")
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"   💾 Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    # Windows fix
    import sys
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_futuretools())
    save_to_csv(data)