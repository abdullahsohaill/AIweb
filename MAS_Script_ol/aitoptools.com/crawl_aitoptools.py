import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import os

# --- CONFIGURATION ---
BASE_URL = "https://aitoptools.com"
START_URL = "https://aitoptools.com/"
OUTPUT_FILE = "aitoptools_complete.csv"

# Settings
MAX_CLICKS = 1000       
EXTRACT_INTERVAL = 5    
MAX_RETRIES = 3         
MAX_CONCURRENT_TABS = 8

def save_chunk_to_csv(data):
    """Saves data to disk immediately."""
    if not data: return
    df = pd.DataFrame(data)
    
    # Ensure columns exist
    cols = ["tool_name", "external_link", "short_description", "pricing", "category", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
        
    # Reorder
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    
    df.to_csv(OUTPUT_FILE, index=False)
    # print(f"      💾 Data Saved ({len(df)} rows)")

async def get_external_link(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            try:
                # Try text selector
                btn = page.locator("a:has-text('Visit Site')").first
                if await btn.count() > 0:
                    visit_link = await btn.get_attribute('href')
                else:
                    # Fallback class selector
                    btn = page.locator(".jet-listing-dynamic-link__link").first
                    if await btn.count() > 0:
                        visit_link = await btn.get_attribute('href')
                
                if visit_link:
                    try:
                        await page.goto(visit_link, timeout=15000, wait_until="commit")
                        await asyncio.sleep(1)
                        final_url = page.url
                    except:
                        final_url = visit_link
            except:
                pass
        except:
            pass
        finally:
            await page.close()
    
    item['external_link'] = final_url
    return item

async def extract_visible_data(page):
    return await page.evaluate("""() => {
        const data = [];
        const cards = document.querySelectorAll('.custom-listing');
        
        cards.forEach(card => {
            try {
                const nameTag = card.querySelector('h2');
                let name = nameTag ? nameTag.innerText.trim() : "Unknown";
                name = name.replace('verified', '').trim();

                const linkTag = card.querySelector('a.tool-link-tool-loop');
                const internalSlug = linkTag ? linkTag.getAttribute('href') : "";

                const descTag = card.querySelector('.custom-listing-content p');
                const desc = descTag ? descTag.innerText.trim() : "";

                const priceTag = card.querySelector('.payment-term');
                const price = priceTag ? priceTag.innerText.trim() : "";

                const catTag = card.querySelector('.tool-tag');
                const category = catTag ? catTag.innerText.trim() : "";

                if(internalSlug) {
                    data.push({
                        tool_name: name,
                        short_description: desc,
                        pricing: price,
                        category: category,
                        internal_detail_url: internalSlug
                    });
                }
            } catch(e) {}
        });
        return data;
    }""")

async def harvest_aitoptools():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Incremental Harvesting (Live Saving) ---")
        
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(START_URL, timeout=60000, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        unique_tools_map = {}
        click_count = 0
        retries = 0
        
        while True:
            try:
                current_count = await page.locator('.custom-listing').count()
                load_more_btn = page.locator('#loadMore')
                
                if await load_more_btn.count() > 0 and await load_more_btn.is_visible():
                    await load_more_btn.scroll_into_view_if_needed()
                    await asyncio.sleep(0.5)
                    await page.evaluate("document.getElementById('loadMore').click()")
                    click_count += 1
                    
                    try:
                        await page.wait_for_function(
                            f"document.querySelectorAll('.custom-listing').length > {current_count}",
                            timeout=10000
                        )
                        retries = 0
                    except:
                        retries += 1
                        print(f"      ⚠️ Clicked but no new items (Strike {retries}/{MAX_RETRIES}). Waiting...")
                        await asyncio.sleep(5)
                        new_check = await page.locator('.custom-listing').count()
                        if new_check == current_count:
                            if retries >= MAX_RETRIES:
                                print("      🛑 Max retries reached.")
                                break
                            else:
                                continue
                        else:
                            retries = 0

                    # SAVE EVERY 5 CLICKS
                    if click_count % EXTRACT_INTERVAL == 0:
                        batch = await extract_visible_data(page)
                        new_added = 0
                        for tool in batch:
                            if tool['internal_detail_url'] not in unique_tools_map:
                                unique_tools_map[tool['internal_detail_url']] = tool
                                new_added += 1
                        
                        print(f"      ⬇️  Click {click_count}: Scraped {new_added} NEW (Total: {len(unique_tools_map)})")
                        # LIVE SAVE
                        save_chunk_to_csv(list(unique_tools_map.values()))

                    if click_count >= MAX_CLICKS:
                        break
                else:
                    print("      ✅ 'Explore More' button gone.")
                    break

            except Exception as e:
                print(f"      ⚠️ Error: {e}")
                break

        # Final Sweep Phase 1
        final_batch = await extract_visible_data(page)
        for tool in final_batch:
            unique_tools_map[tool['internal_detail_url']] = tool
        
        await browser.close()
        
        all_tools = list(unique_tools_map.values())
        save_chunk_to_csv(all_tools) # Save end of Phase 1
        print(f"   ✨ Phase 1 Complete. Total Tools: {len(all_tools)}")

        # --- PHASE 2 ---
        if all_tools:
            print(f"\n--- 🚀 PHASE 2: Extracting Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            
            tasks = [get_external_link(context, item, semaphore) for item in all_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 20 == 0:
                    print(f"      Processed {i+1}/{len(all_tools)} tools...", end="\r")
                    # LIVE SAVE HYBRID (Completed + Pending)
                    current_data = final_results + all_tools[len(final_results):]
                    save_chunk_to_csv(current_data)

            await browser.close()
            # Final Save
            save_chunk_to_csv(final_results)
            print(f"\n🎉 DONE! Final CSV saved.")
            return final_results
        else:
            return []

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # The saving happens INSIDE the function now, so this line just runs it.
    asyncio.run(harvest_aitoptools())