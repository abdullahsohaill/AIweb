import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import random

# --- CONFIGURATION ---
OUTPUT_FILE = "taaft_complete.csv"

TARGET_YEARS = [
    "https://theresanaiforthat.com/period/2025/",
    "https://theresanaiforthat.com/period/2024/",
    "https://theresanaiforthat.com/period/2023/",
    "https://theresanaiforthat.com/period/2022/"
]

# Limits
MAX_PAGES_PER_YEAR = 500  
MAX_CONCURRENT_TABS = 8  # 8 Tabs for Phase 2

# --- HELPER: LIVE SAVE ---
def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "likes", "category", "year_source", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

async def get_external_link(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        external_url = ""
        try:
            # Block media for speed
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Use tool" / "Visit" button
            # Selector based on your snippet: id="ai_top_link"
            try:
                btn = page.locator('#ai_top_link')
                if await btn.count() > 0:
                    external_url = await btn.get_attribute('href')
            except:
                pass

            # Cleanup
            if external_url:
                if "?ref=" in external_url:
                    external_url = external_url.split("?")[0]
                if "&ref=" in external_url:
                    external_url = external_url.split("&")[0]

        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = external_url
    return item

async def extract_tools_from_list(page, year_url):
    """
    Extracts data from the list items (li.li).
    """
    return await page.evaluate("""(year_url) => {
        const results = [];
        // Select all list items
        const items = document.querySelectorAll('li.li');
        
        items.forEach(li => {
            try {
                // Name
                const nameEl = li.querySelector('.ai_link');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Internal Link
                const href = nameEl ? nameEl.getAttribute('href') : "";
                
                // Description
                const descEl = li.querySelector('.short_desc');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // Category
                const catEl = li.querySelector('.task_label');
                const cat = catEl ? catEl.innerText.trim() : "";
                
                // Likes/Saves
                const likesEl = li.querySelector('.saves');
                const likes = likesEl ? likesEl.innerText.trim() : "0";

                if (href) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        category: cat,
                        likes: likes,
                        year_source: year_url,
                        internal_slug: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""", year_url)

async def harvest_year(context, start_url, global_tools):
    page = await context.new_page()
    year_label = start_url.split('/')[-2]
    print(f"   🚀 Starting Year: {year_label}")
    
    current_url = start_url
    page_num = 1
    
    try:
        while page_num <= MAX_PAGES_PER_YEAR:
            try:
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
                
                # 1. Scroll to bottom to trigger lazy loading images (optional but good practice)
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(1)

                # 2. Extract
                tools = await extract_tools_from_list(page, start_url)
                
                # 3. Add to global list
                new_count = 0
                for t in tools:
                    full_internal = f"https://theresanaiforthat.com{t['internal_slug']}"
                    if full_internal not in global_tools:
                        global_tools[full_internal] = {
                            "tool_name": t['tool_name'],
                            "description": t['description'],
                            "category": t['category'],
                            "likes": t['likes'],
                            "year_source": t['year_source'],
                            "internal_detail_url": full_internal,
                            "external_link": "" # To be filled
                        }
                        new_count += 1
                
                print(f"      📅 {year_label} Page {page_num}: Found {len(tools)} ({new_count} new).")
                
                # Save Live
                save_chunk_to_csv(list(global_tools.values()))

                # 4. Pagination
                # Find "Next" button in pagination
                # Selector: .pagination a containing "Next"
                next_btn = page.locator('.pagination a:has-text("Next")')
                
                if await next_btn.count() > 0:
                    next_href = await next_btn.get_attribute('href')
                    if next_href:
                        current_url = f"https://theresanaiforthat.com{next_href}"
                        page_num += 1
                        await asyncio.sleep(1)
                    else:
                        print(f"      ✅ {year_label}: End of list (No href).")
                        break
                else:
                    print(f"      ✅ {year_label}: End of list (No Next button).")
                    break

            except Exception as e:
                print(f"      ❌ Error on {year_label} page {page_num}: {e}")
                break
    finally:
        await page.close()

async def main():
    print("--- 🚀 Starting TAAFT Crawler ---")
    
    async with async_playwright() as p:
        # Headless=False is SAFER for TAAFT (Cloudflare protection)
        browser = await p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        
        global_tools = {}
        
        # --- PHASE 1: HARVEST ALL YEARS ---
        # We run years sequentially to avoid opening too many visible windows
        for url in TARGET_YEARS:
            await harvest_year(context, url, global_tools)
        
        all_data = list(global_tools.values())
        print(f"   ✨ Phase 1 Complete. Total Unique Tools: {len(all_data)}")
        save_chunk_to_csv(all_data)

        # --- PHASE 2: RESOLVE EXTERNAL LINKS ---
        if all_data:
            print(f"\n--- 🚀 PHASE 2: Resolving Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            tasks = [get_external_link(context, item, semaphore) for item in all_data]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 50 == 0:
                    print(f"      Processed {i+1}/{len(all_data)} tools...", end="\r")
                    # Live Save
                    current_data = final_results + all_data[len(final_results):]
                    save_chunk_to_csv(current_data)

            save_chunk_to_csv(final_results)
            print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

        await browser.close()

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())