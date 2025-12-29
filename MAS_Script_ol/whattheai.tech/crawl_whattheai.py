import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://whattheai.tech"
START_URL = "https://whattheai.tech/tools"
OUTPUT_FILE = "whattheai_complete.csv"

# Max pages to scrape (Set to 2000 to cover all 1276 pages)
MAX_PAGES = 2000 
SAVE_INTERVAL = 5 # Save every 5 pages

# Phase 2 Settings
MAX_CONCURRENT_TABS = 8

async def get_external_link(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        external_url = ""
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Visit Site" button
            try:
                # Selector based on snippet: <a><span>Visit Site</span></a>
                btn = page.locator("a:has-text('Visit Site')").first
                if await btn.count() > 0:
                    external_url = await btn.get_attribute('href')
            except:
                pass

            # Cleanup URL
            if external_url and "?" in external_url:
                external_url = external_url.split("?")[0]

        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = external_url
    return item

async def extract_tools_from_page(page):
    """
    Extracts data directly from the DOM using JS.
    """
    return await page.evaluate("""() => {
        const results = [];
        // Select tool cards: <a> block group with bg-white inside
        const cards = document.querySelectorAll('a.block.group');
        
        cards.forEach(card => {
            try {
                const href = card.getAttribute('href');
                
                // Name (h3)
                const nameEl = card.querySelector('h3');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Rating
                const ratingEl = card.querySelector('.text-yellow-400 + span');
                const rating = ratingEl ? ratingEl.innerText.trim() : "0";
                
                // Description
                const descEl = card.querySelector('p');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // Price (Free/Paid)
                // It's in the flex row below description
                const priceEl = card.querySelector('div.flex.items-center.justify-between span.text-gray-900');
                const price = priceEl ? priceEl.innerText.trim() : "";
                
                // Categories (Tags)
                const badges = card.querySelectorAll('div.flex.flex-wrap span');
                let tags = [];
                badges.forEach(b => tags.push(b.innerText.trim()));

                results.push({
                    tool_name: name,
                    description: desc,
                    rating: rating,
                    pricing: price,
                    tags: tags.join(', '),
                    internal_slug: href
                });
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_whattheai():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting WhatTheAI (Pagination) ---")
        
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(START_URL, timeout=60000, wait_until="domcontentloaded")
        
        # Select 100 per page for speed
        try:
            await page.select_option('select', '100')
            await page.wait_for_load_state('networkidle')
            print("   ✅ Selected 100 items per page.")
        except:
            print("   ⚠️ Could not select 100 per page.")

        all_tools = []
        page_num = 1
        
        while page_num <= MAX_PAGES:
            print(f"   📄 Scraping Page {page_num}...", end="\r")
            
            try:
                # Wait for cards
                await page.wait_for_selector('a.block.group', timeout=10000)
                
                # Extract
                tools = await extract_tools_from_page(page)
                all_tools.extend(tools)
                
                print(f"   📄 Page {page_num}: Found {len(tools)} tools. (Total: {len(all_tools)})")
                
                # Save periodically
                if page_num % SAVE_INTERVAL == 0:
                    save_chunk_to_csv(all_tools)

                # Next Page Logic
                # Look for button with text "Next"
                next_btn = page.locator('button:has-text("Next")')
                
                # Check if disabled
                if await next_btn.is_disabled():
                    print("      ✅ End of pagination reached.")
                    break
                
                # Click and wait
                await next_btn.click()
                await asyncio.sleep(2) # Wait for load
                page_num += 1

            except Exception as e:
                print(f"      ❌ Error on page {page_num}: {e}")
                break
        
        await browser.close()
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        if not df.empty:
            df = df.drop_duplicates(subset=['internal_slug'])
            unique_tools = df.to_dict('records')
        else:
            unique_tools = []

        print(f"   ✨ Phase 1 Complete. Unique Tools: {len(unique_tools)}")

        # --- PHASE 2: RESOLVE LINKS ---
        if unique_tools:
            print(f"\n--- 🚀 PHASE 2: Resolving External Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            
            # Add full URL
            for item in unique_tools:
                if item['internal_slug'].startswith("http"):
                    item['internal_detail_url'] = item['internal_slug']
                else:
                    item['internal_detail_url'] = f"{BASE_URL}{item['internal_slug']}"

            tasks = [get_external_link(context, item, semaphore) for item in unique_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 50 == 0:
                    print(f"      Processed {i+1}/{len(unique_tools)} tools...", end="\r")
                    # Live save
                    save_chunk_to_csv(final_results + unique_tools[len(final_results):])

            await browser.close()
            save_chunk_to_csv(final_results)
            return final_results
        else:
            return []

def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    
    # Ensure columns
    cols = ["tool_name", "external_link", "description", "pricing", "rating", "tags", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    data = asyncio.run(harvest_whattheai())
    save_chunk_to_csv(data)