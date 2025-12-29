import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys

# --- CONFIGURATION ---
BASE_URL = "https://dang.ai"
OUTPUT_FILE = "dang_harvest.csv"

# Phase 2 Settings (External Link Resolution)
MAX_CONCURRENT_TABS = 8
TIMEOUT_MS = 20000

async def get_tool_details(context, item):
    """
    Visits the internal tool page, finds the tracking link,
    and then resolves it to the final URL.
    """
    # Skip if no internal slug
    if not item.get('internal_slug'):
        return item

    page = await context.new_page()
    internal_full_url = f"{BASE_URL}{item['internal_slug']}"
    
    tracking_url = ""
    final_url = ""
    
    try:
        # Block media to speed up
        await page.route("**/*.{png,jpg,jpeg,svg,webp,mp4,gif,woff,woff2}", lambda route: route.abort())
        
        # 1. Visit Internal Page
        await page.goto(internal_full_url, timeout=TIMEOUT_MS, wait_until="domcontentloaded")
        
        # 2. Find "View Tool" button to get tracking link
        # Selector: Look for the link that says "view tool" or has the visit class
        try:
            visit_btn = page.locator('a.visit-page_link').first
            if await visit_btn.count() > 0:
                tracking_url = await visit_btn.get_attribute('href')
        except:
            pass

        # 3. Resolve Tracking Link (if found)
        if tracking_url and "dang.ai" in tracking_url:
            try:
                # Navigate to tracking link and wait for redirect
                await page.goto(tracking_url, timeout=TIMEOUT_MS, wait_until="domcontentloaded")
                await asyncio.sleep(1.0) # Wait for JS redirects
                final_url = page.url
                
                # Cleanup UTM params
                if "?" in final_url:
                    final_url = final_url.split("?")[0]
            except:
                final_url = tracking_url
        else:
            final_url = tracking_url

    except Exception as e:
        pass
    finally:
        await page.close()

    # Update item
    item['tracking_url'] = tracking_url
    item['final_website_url'] = final_url
    return item

async def harvest_dang():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting Main List ---")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print(f"   🌐 Visiting: {BASE_URL}")
        await page.goto(BASE_URL, timeout=60000, wait_until="domcontentloaded")
        
        # Wait for list to load initially
        await asyncio.sleep(3)

        all_tools = []
        page_num = 1
        
        while True:
            print(f"   📄 Scraping Page {page_num}...")
            
            # 1. Parse Content
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            cards = soup.find_all('div', class_='voting-item_wrapper')
            current_count = len(cards)
            print(f"      ✅ Found {current_count} tools on this page.")

            for card in cards:
                try:
                    # Name & Internal Link
                    name_tag = card.find('a', class_='voting-item-name_text')
                    name = name_tag.get_text(strip=True) if name_tag else "Unknown"
                    href = name_tag['href'] if name_tag else ""
                    
                    # Description
                    desc_tag = card.find('div', class_='voting-item-description_text')
                    desc = desc_tag.get_text(strip=True) if desc_tag else ""
                    
                    # Upvotes
                    vote_tag = card.find(class_='item-upvote-count_text')
                    votes = vote_tag.get_text(strip=True) if vote_tag else "0"
                    
                    # Categories
                    cats = []
                    cat_links = card.find_all('a', class_='voting-categories_link')
                    for c in cat_links:
                        cats.append(c.get_text(strip=True))
                    cat_str = ", ".join(cats)

                    if href:
                        all_tools.append({
                            "tool_name": name,
                            "short_description": desc,
                            "upvotes": votes,
                            "categories": cat_str,
                            "internal_slug": href
                        })
                except:
                    continue

            # 2. CLICK "NEXT" BUTTON
            # We look for the button containing "Next". 
            # Note: We exclude 'w-condition-invisible' in case Webflow hides it.
            next_btn = page.locator("a.pagination-button_div:has-text('Next'):visible")
            
            if await next_btn.count() > 0:
                # Get current URL to check if it changes
                prev_url = page.url
                
                # Click and wait
                await next_btn.click()
                await asyncio.sleep(3) # Give it time to load new items
                
                # Check if we are still on the same page state
                # (Simple check: did the URL change? Or did content reload?)
                # For Dang.ai, the URL usually changes to ?page=2, ?page=3 etc.
                if page.url == prev_url and "?page=" not in page.url:
                    # If URL didn't change, maybe it's AJAX. 
                    # Let's check if the content changed by comparing first tool name?
                    # For now, we assume if the button was visible and clicked, we moved forward.
                    pass
                
                page_num += 1
            else:
                print("      🛑 'Next' button not found or hidden. End of list.")
                break
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        if not df.empty:
            df = df.drop_duplicates(subset=['internal_slug'])
            unique_tools = df.to_dict('records')
        else:
            unique_tools = []

        print(f"   ✨ Phase 1 Complete. Total Unique Tools: {len(unique_tools)}")
        await browser.close()

        # --- PHASE 2: RESOLVING LINKS ---
        if unique_tools:
            print(f"\n--- 🚀 PHASE 2: Resolving External Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)

            async def safe_process(item):
                async with semaphore:
                    return await get_tool_details(context, item)

            tasks = [safe_process(item) for item in unique_tools]
            
            final_results = []
            total = len(tasks)
            
            # Process in batches/stream
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 10 == 0:
                    print(f"      Processed {i+1}/{total} tools...")

            await browser.close()
            return final_results
        else:
            return []

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    # Create Full Internal URL
    df['internal_detail_url'] = df['internal_slug'].apply(lambda x: f"{BASE_URL}{x}" if x else "")
    
    # Reorder
    cols = ["tool_name", "final_website_url", "tracking_url", "short_description", "upvotes", "categories", "internal_detail_url"]
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS!")
    print(f"   Saved {len(df)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_dang())
    save_to_csv(data)