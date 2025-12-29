import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import os

# --- CONFIGURATION ---
BASE_URL = "https://toolai.io"
START_URL = "https://toolai.io/"
OUTPUT_FILE = "toolai_complete.csv"

# Settings
MAX_CLICKS = 1000       # Infinite Scroll limit
EXTRACT_INTERVAL = 5    # Save every X clicks
MAX_RETRIES = 5         # Retry logic for button
MAX_CONCURRENT_TABS = 8

def save_chunk_to_csv(data):
    """Saves data to disk immediately."""
    if not data: return
    df = pd.DataFrame(data)
    
    # Normalize columns
    cols = ["tool_name", "external_link", "description", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

async def resolve_external_link(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Visit Site" button
            # Selector: a.btn-main.ms-3 or text "Visit Site"
            try:
                btn = page.locator("a:has-text('Visit Site')").first
                
                if await btn.count() > 0:
                    # It's a redirect link (/link/wyd), so we must visit or capture target
                    raw_href = await btn.get_attribute('href')
                    
                    # If it starts with /link/, we might need to follow it to get real URL
                    if raw_href and raw_href.startswith("/link/"):
                        try:
                            # Click and wait for new page or redirect
                            async with context.expect_page(timeout=10000) as new_page_info:
                                await btn.click()
                            
                            new_page = await new_page_info.value
                            await new_page.wait_for_load_state("domcontentloaded")
                            final_url = new_page.url
                            await new_page.close()
                        except:
                            # If popup blocked or failed, just construct full link
                            final_url = f"{BASE_URL}{raw_href}"
                    else:
                        final_url = raw_href
            except:
                pass

            # Cleanup
            if final_url and "?" in final_url and "toolai.io" not in final_url:
                final_url = final_url.split("?")[0]

        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = final_url
    return item

async def extract_visible_tools(page):
    """
    Extracts data from list using JS.
    """
    return await page.evaluate("""() => {
        const results = [];
        // Select tool cards
        // Based on snippet: <div class="col ailist">
        const cards = document.querySelectorAll('div.col.ailist');
        
        cards.forEach(card => {
            try {
                // Name (h2 > a)
                const nameEl = card.querySelector('h2 a');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Internal Link
                const href = nameEl ? nameEl.getAttribute('href') : "";
                
                // Description (p.aidesc)
                const descEl = card.querySelector('p.aidesc');
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

async def harvest_toolai():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting ToolAI.io ---")
        
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(START_URL, timeout=90000, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        unique_tools_map = {}
        click_count = 0
        retries = 0
        
        while True:
            try:
                # 1. Count items
                current_count = await page.locator('div.col.ailist').count()
                
                # 2. Find Load More
                load_more_btn = page.locator('#load-more')
                
                if await load_more_btn.count() > 0 and await load_more_btn.is_visible():
                    
                    await load_more_btn.scroll_into_view_if_needed()
                    await asyncio.sleep(0.5)
                    
                    try:
                        await load_more_btn.click(force=True)
                    except:
                        await load_more_btn.evaluate("node => node.click()")
                    
                    click_count += 1
                    
                    # 3. Smart Wait
                    try:
                        await page.wait_for_function(
                            f"document.querySelectorAll('div.col.ailist').length > {current_count}",
                            timeout=10000
                        )
                        retries = 0
                    except:
                        retries += 1
                        print(f"      ⚠️ Clicked but count didn't rise (Strike {retries}/{MAX_RETRIES})")
                        await asyncio.sleep(3)
                        if retries >= MAX_RETRIES:
                            print("      🛑 List stuck or finished.")
                            break
                        continue

                    # 4. Incremental Save
                    if click_count % EXTRACT_INTERVAL == 0:
                        batch = await extract_visible_tools(page)
                        new_added = 0
                        for tool in batch:
                            if tool['internal_detail_url'] not in unique_tools_map:
                                unique_tools_map[tool['internal_detail_url']] = tool
                                new_added += 1
                        
                        print(f"      ⬇️  Click {click_count}: Scraped {new_added} NEW (Total: {len(unique_tools_map)})")
                        save_chunk_to_csv(list(unique_tools_map.values()))

                    if click_count >= MAX_CLICKS:
                        break
                else:
                    print("      ✅ 'Load More' button gone. List complete.")
                    break

            except Exception as e:
                print(f"      ⚠️ Loop Error: {e}")
                break

        # Final Sweep
        final_batch = await extract_visible_tools(page)
        for tool in final_batch:
            unique_tools_map[tool['internal_detail_url']] = tool
            
        await browser.close()
        
        all_tools = list(unique_tools_map.values())
        save_chunk_to_csv(all_tools)
        print(f"   ✨ Phase 1 Complete. Total: {len(all_tools)}")

        # --- PHASE 2 ---
        if all_tools:
            print(f"\n--- 🚀 PHASE 2: Resolving Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            
            # Add full internal URL
            for item in all_tools:
                if not item['internal_detail_url'].startswith("http"):
                    item['internal_detail_url'] = f"{BASE_URL}{item['internal_detail_url']}"

            tasks = [resolve_external_link(context, item, semaphore) for item in all_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 20 == 0:
                    print(f"      Processed {i+1}/{len(all_tools)} tools...", end="\r")
                    # Hybrid Save
                    save_chunk_to_csv(final_results + all_tools[len(final_results):])

            await browser.close()
            save_chunk_to_csv(final_results)
            print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")
            return final_results
        else:
            return []

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(harvest_toolai())