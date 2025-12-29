import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys
import time

# --- CONFIGURATION ---
BASE_URL = "https://www.insidr.ai/ai-tools/"
OUTPUT_FILE = "insidr_complete.csv"

# Phase 2: How many tabs to open in background to resolve links
CONCURRENT_TABS = 6 
MAX_WAIT_TIME = 60 # Wait up to 60s for a redirect

async def resolve_link(context, item, semaphore):
    """
    Visits the affiliate link (insidr.ai/aff/...) and waits for it 
    to redirect to the real website.
    """
    tracking_url = item.get('tracking_url')
    
    # Skip if invalid
    if not tracking_url or "insidr.ai" not in tracking_url:
        item['real_website_url'] = tracking_url
        return item

    async with semaphore:
        page = await context.new_page()
        final_url = tracking_url
        
        try:
            # 1. Visit the tracking link
            # We use a try/except block for goto because sometimes the redirect 
            # happens so fast it triggers a navigation error, which is actually good.
            try:
                await page.goto(tracking_url, timeout=10000, wait_until="commit")
            except:
                pass

            # 2. Polling Loop (Watchdog)
            # Check every 2 seconds if the URL has changed away from insidr.ai
            start_time = time.time()
            
            while True:
                elapsed = time.time() - start_time
                if elapsed > MAX_WAIT_TIME:
                    break
                
                current_url = page.url
                
                # CONDITION: URL is no longer an internal insidr link
                if "insidr.ai/aff" not in current_url and "about:blank" not in current_url:
                    final_url = current_url
                    break
                
                await asyncio.sleep(1.5)
            
            # 3. Clean URL (Remove UTM params if needed)
            if "?" in final_url and "insidr.ai" not in final_url:
                final_url = final_url.split("?")[0]

        except Exception as e:
            pass
        finally:
            await page.close()
    
    item['real_website_url'] = final_url
    return item

async def harvest_insidr():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting List (Pages 1-42+) ---")
        
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        current_url = BASE_URL
        all_tools = []
        page_num = 1
        
        while True:
            print(f"   📄 Scraping Page {page_num}...")
            
            try:
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
            except:
                print(f"      ⚠️ Error loading page {page_num}. Retrying once...")
                await asyncio.sleep(3)
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")

            # Parse HTML
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find tool cards
            # Based on your snippet: <div class="aitools-item" ...>
            cards = soup.find_all('div', class_='aitools-item')
            
            if not cards:
                print("      🛑 No cards found. Ending crawl.")
                break
                
            print(f"      ✅ Found {len(cards)} tools.")

            for card in cards:
                try:
                    # Name
                    name_tag = card.find(class_='aitools-tool-title')
                    name = name_tag.get_text(strip=True) if name_tag else "Unknown"
                    
                    # Description
                    desc_tag = card.find(class_='aitools-tool-description')
                    desc = desc_tag.get_text(strip=True) if desc_tag else ""
                    
                    # Categories
                    # <span class="aitools-category">#AI Social Media</span>
                    cats = []
                    cat_tags = card.find_all(class_='aitools-category')
                    for c in cat_tags:
                        cats.append(c.get_text(strip=True).replace("#", ""))
                    cat_str = ", ".join(cats)
                    
                    # Pricing
                    price_tag = card.find(class_='pricing-price')
                    pricing = price_tag.get_text(strip=True) if price_tag else ""

                    # Tracking Link (External)
                    # <a href="https://www.insidr.ai/aff/..." class="aitools-visit-link">
                    visit_link = card.find('a', class_='aitools-visit-link')
                    tracking_url = visit_link['href'] if visit_link else ""

                    all_tools.append({
                        "tool_name": name,
                        "description": desc,
                        "categories": cat_str,
                        "pricing": pricing,
                        "tracking_url": tracking_url,
                        "source_page": page_num
                    })
                except:
                    continue

            # PAGINATION LOGIC
            # Find the "Next" button: <a class="next page-numbers" href="...">
            next_btn = soup.find('a', class_='next page-numbers')
            
            if next_btn and next_btn.get('href'):
                current_url = next_btn['href']
                page_num += 1
                # Small polite delay
                await asyncio.sleep(1)
            else:
                print("   🛑 End of pagination reached.")
                break
        
        # Close phase 1 browser
        await browser.close()
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        if not df.empty:
            df = df.drop_duplicates(subset=['tracking_url'])
            unique_tools = df.to_dict('records')
        else:
            unique_tools = []
            
        print(f"   ✨ Phase 1 Complete. Collected {len(unique_tools)} unique tools.")

        # --- PHASE 2: RESOLVING LINKS ---
        if unique_tools:
            print(f"\n--- 🚀 PHASE 2: Resolving Redirects ({CONCURRENT_TABS} concurrent) ---")
            print("    (This opens background tabs to follow the 'insidr.ai/aff' links)")
            
            # Re-launch browser for Phase 2
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            )
            
            semaphore = asyncio.Semaphore(CONCURRENT_TABS)

            # Create tasks
            tasks = [resolve_link(context, item, semaphore) for item in unique_tools]
            
            final_results = []
            total = len(tasks)
            
            # Run with progress
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 10 == 0:
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
    
    # Reorder columns
    cols = ["tool_name", "real_website_url", "description", "categories", "pricing", "tracking_url"]
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS!")
    print(f"   Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_insidr())
    save_to_csv(data)