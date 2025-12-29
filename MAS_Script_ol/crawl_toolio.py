import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys

# --- CONFIGURATION ---
BASE_URL = "https://www.toolio.ai"
OUTPUT_FILE = "toolio_complete.csv"

# Concurrency for Phase 2 (Opening details pages)
MAX_CONCURRENT_TABS = 8 

async def get_external_link(context, item):
    """
    Visits the internal tool page and extracts the 'Open Tool' link.
    """
    page = await context.new_page()
    internal_full_url = f"{BASE_URL}{item['internal_slug']}"
    external_url = ""

    try:
        # Block images to load pages faster
        await page.route("**/*.{png,jpg,jpeg,svg,webp}", lambda route: route.abort())
        
        await page.goto(internal_full_url, timeout=30000, wait_until="domcontentloaded")
        
        # Selector for the "Open Tool" button
        try:
            # Sometimes it's an ID, sometimes a class. We look for the button with "Open Tool" text or ID
            button = page.locator('#button-tool')
            if await button.count() > 0:
                external_url = await button.get_attribute('href')
        except:
            pass

    except Exception as e:
        # print(f"      ⚠️ Error on {internal_full_url}: {e}")
        pass
    finally:
        await page.close()

    # Update item
    item['external_link'] = external_url
    return item

async def harvest_toolio():
    async with async_playwright() as p:
        # --- PHASE 1: HARVESTING THE LIST ---
        print("--- 🚀 PHASE 1: Harvesting Main List via Pagination ---")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print(f"   🌐 Visiting: {BASE_URL}")
        await page.goto(BASE_URL, timeout=60000, wait_until="domcontentloaded")

        # Scroll down to ensure list is active
        await page.evaluate("window.scrollBy(0, 1000)")
        await asyncio.sleep(2)

        all_tools = []
        page_num = 1
        
        while True:
            print(f"   📄 Scraping Page {page_num}...")
            
            # 1. Parse current content
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all tool cards (This might grab some 'Just Launched' ones too, but we deduplicate later)
            cards = soup.find_all('a', id='tool')
            
            current_page_count = 0
            for card in cards:
                try:
                    # Name
                    name_tag = card.find('h2', attrs={'fs-cmsfilter-field': 'name'})
                    name = name_tag.get_text(strip=True) if name_tag else "Unknown"
                    
                    # Description
                    desc_tag = card.find('p', attrs={'fs-cmsfilter-field': 'description'})
                    desc = desc_tag.get_text(strip=True) if desc_tag else ""
                    
                    # Internal Link
                    href = card.get('href')
                    
                    # Add to list
                    if href:
                        all_tools.append({
                            "tool_name": name,
                            "description": desc,
                            "internal_slug": href
                        })
                        current_page_count += 1
                except:
                    continue
            
            print(f"      ✅ Found {current_page_count} tools on this page.")

            # 2. Handle Pagination
            
            # Capture the current page text (e.g. "1 / 152") to check for changes
            # We use .last because the "All Tools" list is usually at the bottom
            try:
                # Trying to find the counter text associated with the main list
                counter_element = page.locator("text= / 152").last
                if await counter_element.count() > 0:
                    old_counter_text = await counter_element.text_content()
                else:
                    old_counter_text = "unknown"
            except:
                old_counter_text = "unknown"

            # --- THE FIX: SPECIFIC SELECTOR ---
            # We select the Next button that does NOT have the class 'just-launched'
            next_button = page.locator("a.w-pagination-next:not(.just-launched)")
            
            if await next_button.count() > 0 and await next_button.is_visible():
                await next_button.click()
                
                # Wait for page update
                try:
                    await asyncio.sleep(1.5) # Short wait for animation
                    # Optional: Wait for the specific list to update if possible, 
                    # but simple sleep is usually reliable for Webflow paginations
                except:
                    pass
                
                page_num += 1
            else:
                print("   🛑 'Next' button not found or end of list reached.")
                break
        
        # Deduplicate list (removes duplicates if 'Just Launched' tools were grabbed repeatedly)
        df_temp = pd.DataFrame(all_tools)
        if not df_temp.empty:
            df_temp = df_temp.drop_duplicates(subset=['internal_slug'])
            unique_tools = df_temp.to_dict('records')
        else:
            unique_tools = []
            
        print(f"   ✨ Phase 1 Complete. Total Unique Tools: {len(unique_tools)}")

        # --- PHASE 2: EXTRACTING EXTERNAL LINKS ---
        if unique_tools:
            print(f"\n--- 🚀 PHASE 2: Extracting External Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)

            async def safe_process(item):
                async with semaphore:
                    return await get_external_link(context, item)

            tasks = [safe_process(item) for item in unique_tools]
            
            final_results = []
            total_tasks = len(tasks)
            
            # Run and show progress
            for i, task in enumerate(asyncio.as_completed(tasks)):
                result = await task
                final_results.append(result)
                if (i + 1) % 20 == 0:
                    print(f"      Processed {i+1}/{total_tasks} tools...")

            await browser.close()
            return final_results
        else:
            await browser.close()
            return []

def save_to_csv(data):
    if not data:
        print("❌ No data harvested.")
        return

    df = pd.DataFrame(data)
    
    # Create Full Internal URL column
    df['internal_full_url'] = df['internal_slug'].apply(lambda x: f"{BASE_URL}{x}")
    
    # Reorder columns
    cols = ["tool_name", "external_link", "description", "internal_full_url"]
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS!")
    print(f"   Saved {len(df)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_toolio())
    save_to_csv(data)