import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
START_URL = "https://www.toolkitly.com/tools"
OUTPUT_FILE = "toolkitly_complete.csv"

# Settings
MAX_PAGES = 500         # Safety limit
MAX_CONCURRENT_TABS = 10 # For Phase 2

# Global list to store data
all_collected_tools = []

def save_chunk_to_csv(data):
    """Saves data to disk immediately."""
    if not data: return
    df = pd.DataFrame(data)
    
    # Ensure columns exist
    cols = ["tool_name", "external_link", "description", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
        
    # Reorder
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    
    df.to_csv(OUTPUT_FILE, index=False)

async def resolve_external_link(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block media for speed
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Try [Tool]" button
            # Selector: a.custom-btn
            try:
                btn = page.locator("a.custom-btn").first
                if await btn.count() > 0:
                    final_url = await btn.get_attribute('href')
            except:
                pass

            # If valid link found
            if final_url:
                # Cleanup UTM params if needed, but usually toolkitly links have them
                pass
                
        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = final_url
    return item

async def extract_tools_from_page(page):
    return await page.evaluate("""() => {
        const results = [];
        // Select tool cards
        const cards = document.querySelectorAll('div.coupons-code-item');
        
        cards.forEach(card => {
            try {
                // Name & Internal Link
                const linkEl = card.querySelector('.save-price a');
                const name = linkEl ? linkEl.innerText.trim() : "Unknown";
                const href = linkEl ? linkEl.getAttribute('href') : "";
                
                // Description
                const descEl = card.querySelector('.coupon-desc');
                const desc = descEl ? descEl.innerText.trim() : "";

                if (href) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        internal_detail_url: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_toolkitly():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting Toolkitly ---")
        
        # Use Headless=True for background, False for debug
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context()
        page = await context.new_page()

        current_url = START_URL
        
        # Master Map to prevent duplicates
        unique_tools_map = {}
        page_num = 1
        
        while page_num <= MAX_PAGES:
            print(f"   📄 Scraping Page {page_num}...", end="\r")
            try:
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
                
                # Wait for list
                try:
                    await page.wait_for_selector('div.coupons-code-item', timeout=10000)
                except:
                    print("      ⚠️ No items found on page. Retrying once...")
                    await asyncio.sleep(3)
                
                # Extract
                tools = await extract_tools_from_page(page)
                
                new_count = 0
                for t in tools:
                    if t['internal_detail_url'] not in unique_tools_map:
                        unique_tools_map[t['internal_detail_url']] = t
                        new_count += 1
                
                print(f"   📄 Page {page_num}: Found {len(tools)} tools ({new_count} new). Total: {len(unique_tools_map)}")
                
                # Save Progress
                save_chunk_to_csv(list(unique_tools_map.values()))

                # PAGINATION LOGIC
                # Look for <li class="pg-next"><a href="...">Next</a></li>
                next_btn = page.locator('li.pg-next a')
                
                if await next_btn.count() > 0:
                    next_href = await next_btn.get_attribute('href')
                    if next_href:
                        current_url = next_href
                        page_num += 1
                        await asyncio.sleep(1) # Polite wait
                    else:
                        print("      ✅ 'Next' button has no link. End of list.")
                        break
                else:
                    print("      ✅ 'Next' button not found. End of list.")
                    break

            except Exception as e:
                print(f"      ❌ Error on page {page_num}: {e}")
                break
        
        await browser.close()
        
        all_tools = list(unique_tools_map.values())
        print(f"   ✨ Phase 1 Complete. Total Tools: {len(all_tools)}")

        # --- PHASE 2: RESOLVE EXTERNAL LINKS ---
        if all_tools:
            print(f"\n--- 🚀 PHASE 2: Extracting External Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            
            tasks = [resolve_external_link(context, item, semaphore) for item in all_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 20 == 0:
                    print(f"      Processed {i+1}/{len(all_tools)} tools...", end="\r")
                    # Hybrid Save: Processed items + Unprocessed items
                    current_data = final_results + all_tools[len(final_results):]
                    save_chunk_to_csv(current_data)

            await browser.close()
            save_chunk_to_csv(final_results)
            print(f"\n🎉 DONE! Final CSV saved.")
            return final_results
        else:
            return []

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    asyncio.run(harvest_toolkitly())