import asyncio
import pandas as pd
import os
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
TARGET_URL = "https://foundr.ai/"
OUTPUT_FILE = "foundr_extracted.csv"
MAX_LOOPS = 200  # Safety limit to prevent infinite running
SCROLL_PAUSE = 2.0

async def main():
    async with async_playwright() as p:
        print(f"--- 🚀 Starting Crawl for Foundr.ai ---")
        
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        # 1. Visit URL
        await page.goto(TARGET_URL, timeout=60000, wait_until="domcontentloaded")
        
        # 2. CRITICAL FIX: Wait for cards to actually render
        print("   ⏳ Waiting for tool cards to load...")
        try:
            await page.wait_for_selector("div.product.card", timeout=15000)
        except:
            print("   ❌ Error: Page loaded but no tools found. Possible Bot Block or changed layout.")
            await browser.close()
            return

        seen_ids = set()
        loop = 0
        consecutive_no_change = 0

        # Prepare CSV headers
        if not os.path.exists(OUTPUT_FILE):
            pd.DataFrame(columns=[
                "tool_name", "external_link", "description", "category", "likes", "internal_detail_url"
            ]).to_csv(OUTPUT_FILE, index=False)

        while loop < MAX_LOOPS:
            # --- EXTRACTION ---
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all cards based on your HTML snippet
            cards = soup.find_all("div", class_="product")
            
            new_items = []
            for card in cards:
                try:
                    # ID for deduplication
                    tid = card.get("data-id")
                    if tid in seen_ids:
                        continue
                    seen_ids.add(tid)

                    # Name
                    name_tag = card.find("h4", class_="title")
                    name = name_tag.get_text(strip=True) if name_tag else "Unknown"

                    # Description
                    desc_tag = card.find("p", class_="tagline")
                    desc = desc_tag.get_text(strip=True) if desc_tag else ""

                    # Internal Link
                    # Usually wrapping the top part
                    a_tag = card.find("a")
                    internal_link = ""
                    if a_tag and a_tag.get("href"):
                        if a_tag['href'].startswith("http"):
                            internal_link = a_tag['href']
                        else:
                            internal_link = f"https://foundr.ai{a_tag['href']}"

                    # Category
                    cat_tag = card.find("span", class_="category")
                    category = cat_tag.get_text(strip=True) if cat_tag else ""

                    # Likes
                    likes_tag = card.find("span", class_="likes")
                    likes = likes_tag.get_text(strip=True) if likes_tag else "0"

                    # EXTERNAL LINK (The "go.foundr.ai" link)
                    # It is inside footer-meta -> a.btn-primary
                    external_link = ""
                    ext_btn = card.find("a", class_="btn-primary")
                    if ext_btn:
                        external_link = ext_btn.get("href")

                    new_items.append({
                        "tool_name": name,
                        "external_link": external_link,
                        "description": desc,
                        "category": category,
                        "likes": likes,
                        "internal_detail_url": internal_link
                    })
                except:
                    continue

            # Save batch
            if new_items:
                pd.DataFrame(new_items).to_csv(OUTPUT_FILE, mode='a', header=False, index=False)
                print(f"   ⬇️  Loop {loop}: Found {len(new_items)} NEW tools (Total: {len(seen_ids)})")
                consecutive_no_change = 0
            else:
                consecutive_no_change += 1
                print(f"   ⚠️ Loop {loop}: No new items found ({consecutive_no_change}/5)")

            if consecutive_no_change >= 5:
                print("   🛑 No new items for 5 scrolls. Stopping.")
                break

            # --- SCROLLING LOGIC ---
            # 1. Get current height
            prev_height = await page.evaluate("document.body.scrollHeight")
            
            # 2. Scroll to bottom
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            
            # 3. Check for "Load More" button just in case
            try:
                load_more = page.locator("button:has-text('Load More'), a:has-text('Load More')")
                if await load_more.count() > 0 and await load_more.is_visible():
                    print("      🖱️ Clicking 'Load More' button...")
                    await load_more.click()
            except:
                pass

            # 4. Wait for new content
            await asyncio.sleep(SCROLL_PAUSE)
            
            loop += 1

        await browser.close()
        print(f"\n🎉 DONE! Saved {len(seen_ids)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    # Windows fix
    import sys
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    asyncio.run(main())