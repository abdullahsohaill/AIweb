import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import os

# --- CONFIGURATION ---
BASE_URL = "https://bestofai.com"
START_URL = "https://bestofai.com/"
OUTPUT_FILE = "bestofai_complete.csv"

MAX_CLICKS = 1000       
EXTRACT_INTERVAL = 5    
MAX_RETRIES = 3
MAX_CONCURRENT_TABS = 6

def save_chunk_to_csv(data):
    """Helper to save data immediately to disk"""
    if not data: return
    df = pd.DataFrame(data)
    # Reorder nicely
    cols = ["tool_name", "external_link", "short_description", "categories", "upvotes", "internal_detail_url"]
    # Select only columns that exist
    existing = [c for c in cols if c in df.columns]
    df = df[existing]
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"      💾 Saved {len(df)} rows to {OUTPUT_FILE}")

async def get_external_link(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        external_url = ""
        try:
            # Fast blocking
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            try:
                element = page.locator('a:has-text("Visit Website")').first
                if await element.count() > 0:
                    external_url = await element.get_attribute('href')
            except:
                pass
        except:
            pass
        finally:
            await page.close()
    
    item['external_link'] = external_url
    return item

async def extract_visible_tools(page):
    return await page.evaluate("""() => {
        const results = [];
        const cards = document.querySelectorAll('a[href^="/tool/"]');
        cards.forEach(card => {
            try {
                const href = card.getAttribute('href');
                const nameEl = card.querySelector('h3');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                const descEl = card.querySelector('p');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                let categories = [];
                const btns = card.querySelectorAll('button');
                btns.forEach(btn => {
                    const text = btn.innerText.trim();
                    if (text !== 'Like' && text !== 'Save Tool' && !text.includes('likes')) {
                        categories.push(text);
                    }
                });
                
                let upvotes = "0";
                const spans = card.querySelectorAll('span');
                spans.forEach(span => {
                    if (span.innerText.includes('likes')) {
                        upvotes = span.innerText.replace('likes', '').replace('+', '').trim();
                    }
                });

                if (href) {
                    results.push({
                        tool_name: name,
                        short_description: desc,
                        categories: categories.join(', '),
                        upvotes: upvotes,
                        internal_slug: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_bestofai():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Tenacious Harvesting (Live Saving) ---")
        
        browser = await p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        await page.goto(START_URL, timeout=90000, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        unique_tools_map = {}
        click_count = 0
        button_missing_strikes = 0
        
        print("   🔄 Starting Loop...")
        
        while True:
            try:
                load_more_btn = page.locator('button:has-text("Load more")')
                is_visible = False
                try:
                    await load_more_btn.wait_for(state="visible", timeout=5000)
                    is_visible = True
                except:
                    is_visible = False

                if is_visible:
                    button_missing_strikes = 0
                    await load_more_btn.scroll_into_view_if_needed()
                    await asyncio.sleep(0.5)
                    try:
                        await load_more_btn.click(force=True)
                    except:
                        await load_more_btn.evaluate("node => node.click()")
                    
                    click_count += 1
                    await asyncio.sleep(3)
                else:
                    button_missing_strikes += 1
                    print(f"      ⏳ Button hidden. Waiting... ({button_missing_strikes}/3)")
                    await asyncio.sleep(3)
                    if button_missing_strikes >= 3:
                        print("      ✅ End of list.")
                        break

                # LIVE SAVE every 5 clicks
                if click_count % EXTRACT_INTERVAL == 0:
                    batch = await extract_visible_tools(page)
                    new = 0
                    for t in batch:
                        if t['internal_slug'] not in unique_tools_map:
                            unique_tools_map[t['internal_slug']] = t
                            new += 1
                    
                    print(f"      ⬇️  Click {click_count}: Scraped {new} NEW")
                    # Save to disk immediately
                    save_chunk_to_csv(list(unique_tools_map.values()))

                if click_count >= MAX_CLICKS:
                    break

            except Exception as e:
                print(f"      ⚠️ Error: {e}")
                break

        # Final Sweep Phase 1
        final = await extract_visible_tools(page)
        for t in final:
            unique_tools_map[t['internal_slug']] = t
        await browser.close()
        
        all_tools = list(unique_tools_map.values())
        save_chunk_to_csv(all_tools) # Save end of Phase 1
        print(f"   ✨ Phase 1 Done. Tools: {len(all_tools)}")

        # --- PHASE 2 ---
        if all_tools:
            print(f"\n--- 🚀 PHASE 2: Extracting Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            
            for item in all_tools:
                item['internal_detail_url'] = f"{BASE_URL}{item['internal_slug']}"

            tasks = [get_external_link(context, item, semaphore) for item in all_tools]
            
            # Process and SAVE LIVE
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 50 == 0:
                    print(f"      Processed {i+1}/{len(all_tools)} tools...", end="\r")
                    save_chunk_to_csv(final_results + all_tools[len(final_results):]) # Save mixed progress

            await browser.close()
            return final_results
        else:
            return []

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    # Capture data AND save at the very end too
    data = asyncio.run(harvest_bestofai())
    save_chunk_to_csv(data)