import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys

# --- CONFIGURATION ---
BASE_URL = "https://www.toolpilot.ai"
START_URL = "https://www.toolpilot.ai/collections/all?page=1"
OUTPUT_FILE = "toolpilot_complete.csv"

# Phase 2 Settings
MAX_CONCURRENT_TABS = 10 

async def get_tool_details(context, item, semaphore):
    """
    Visits the internal tool page to get Description and External Link.
    """
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        external_url = ""
        description = ""
        
        try:
            # Block media to speed up loading
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # 1. Get External Link (Visit Site button)
            # Selector based on your snippet: <a id="AddToCart" ...>Visit Site</a>
            try:
                visit_btn = page.locator('#AddToCart')
                if await visit_btn.count() > 0:
                    external_url = await visit_btn.get_attribute('href')
            except:
                pass

            # 2. Get Description
            # Usually in a div with class 'product-description' or similar, 
            # but based on your text content, it's likely under the title or in a specific block.
            # We'll grab the first paragraph after the H1 or a common description container.
            try:
                # Fallback attempt to find description text if specific class is missing
                # ToolPilot descriptions often appear in a block below the "Visit Site" button
                # We'll try to grab meta description or main content text
                meta_desc = await page.locator('meta[name="description"]').get_attribute('content')
                if meta_desc:
                    description = meta_desc
                else:
                    # Try grabbing the first paragraph in the main content area
                    description = await page.locator('.product-description p').first.inner_text()
            except:
                pass

        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = external_url
    item['description'] = description
    return item

async def harvest_toolpilot():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting Main List (Pagination) ---")
        
        # Headless=True is fine here usually
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        current_url = START_URL
        all_tools = []
        page_num = 1
        
        while True:
            print(f"   📄 Scraping Page {page_num}...")
            try:
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
            except:
                print("      ⚠️ Timeout loading page. Retrying...")
                await asyncio.sleep(2)
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")

            # Parse
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find tool cards
            # <li class="column"><product-card ...>
            cards = soup.find_all('product-card')
            print(f"      ✅ Found {len(cards)} tools.")

            for card in cards:
                try:
                    # Name & Link
                    title_link = card.find('a', class_='product-card-title')
                    if title_link:
                        name = title_link.get_text(strip=True)
                        href = title_link['href']
                        full_internal = f"{BASE_URL}{href}"
                        
                        # Price
                        price_tag = card.find(class_='price-item')
                        price = price_tag.get_text(strip=True) if price_tag else "Free/Unknown"

                        all_tools.append({
                            "tool_name": name,
                            "price": price,
                            "internal_detail_url": full_internal
                        })
                except:
                    continue

            # PAGINATION LOGIC
            # Look for <span class="next"><a href="...">
            next_span = soup.find('span', class_='next')
            if next_span:
                next_link = next_span.find('a')
                if next_link and next_link.get('href'):
                    # Build next URL
                    next_href = next_link['href']
                    current_url = f"{BASE_URL}{next_href}"
                    page_num += 1
                    await asyncio.sleep(1) # Polite delay
                else:
                    print("      🛑 End of list (No next link).")
                    break
            else:
                print("      🛑 End of list (No next span).")
                break
        
        await browser.close()
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        if not df.empty:
            df = df.drop_duplicates(subset=['internal_detail_url'])
            unique_tools = df.to_dict('records')
        else:
            unique_tools = []

        print(f"   ✨ Phase 1 Complete. Unique Tools: {len(unique_tools)}")

        # --- PHASE 2: DEEP EXTRACTION ---
        if unique_tools:
            print(f"\n--- 🚀 PHASE 2: Extracting Details ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            
            tasks = [get_tool_details(context, item, semaphore) for item in unique_tools]
            
            final_results = []
            total = len(tasks)
            
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 50 == 0:
                    print(f"      Processed {i+1}/{total} tools...", end="\r")
            
            await browser.close()
            return final_results
        else:
            return []

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    cols = ["tool_name", "external_link", "price", "description", "internal_detail_url"]
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS!")
    print(f"   Saved {len(df)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_toolpilot())
    save_to_csv(data)