import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://microlaunch.net"
START_URL = "https://microlaunch.net/category/ai"
OUTPUT_FILE = "microlaunch_complete.csv"

MAX_SCROLLS = 500 
SCROLL_DELAY = 2.5
MAX_CONCURRENT_TABS = 8
EXTRACT_INTERVAL = 5

def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "categories", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

async def get_external_link(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            try:
                # Look for "Visit Website" button
                btn = page.locator('a:has-text("Visit Website")').first
                if await btn.count() > 0:
                    final_url = await btn.get_attribute('href')
                    if final_url and "?ref=" in final_url:
                        final_url = final_url.split("?")[0]
            except:
                pass
        except:
            pass
        finally:
            await page.close()
    
    item['external_link'] = final_url
    return item

async def extract_visible_tools(page):
    return await page.evaluate("""() => {
        const results = [];
        // Select cards: Flex container with shadow + px-4
        // Or better: find links starting with /p/ that are NOT in nav
        // Based on snippet: <div class="flex-col xl:flex-row shadow px-4 ...">
        const cards = document.querySelectorAll('div.shadow.px-4.py-4.rounded-lg');
        
        cards.forEach(card => {
            try {
                const linkEl = card.querySelector('a[href^="/p/"]');
                const href = linkEl ? linkEl.getAttribute('href') : "";
                
                const nameEl = card.querySelector('span.font-medium');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                const descEl = card.querySelector('span.line-clamp-2');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // Tags/Badges
                const tags = [];
                card.querySelectorAll('span.rounded-full').forEach(t => {
                    const txt = t.innerText.trim();
                    if (txt !== "New" && txt !== "Featured") tags.push(txt);
                });

                if (href) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        categories: tags.join(', '),
                        internal_slug: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_microlaunch():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting MicroLaunch (Infinite Scroll) ---")
        
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(START_URL, timeout=90000, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        unique_tools_map = {}
        scroll_count = 0
        retries = 0
        
        # Initial check
        try:
            await page.wait_for_selector('div.shadow.px-4', timeout=10000)
        except:
            print("      ⚠️ No items found initially.")

        while True:
            try:
                prev_count = await page.locator('div.shadow.px-4.rounded-lg').count()
                
                # Scroll
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(SCROLL_DELAY)
                
                new_count = await page.locator('div.shadow.px-4.rounded-lg').count()
                
                if new_count == prev_count:
                    retries += 1
                    print(f"      ⚠️ No new items loaded (Strike {retries}/5)")
                    await page.evaluate("window.scrollBy(0, -500)") # Wiggle
                    await asyncio.sleep(1)
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(3)
                    
                    if retries >= 5:
                        print("      🛑 End of list.")
                        break
                else:
                    retries = 0
                
                scroll_count += 1

                if scroll_count % EXTRACT_INTERVAL == 0:
                    batch = await extract_visible_tools(page)
                    new_added = 0
                    for tool in batch:
                        if tool['internal_slug'] not in unique_tools_map:
                            unique_tools_map[tool['internal_slug']] = tool
                            new_added += 1
                    print(f"      ⬇️  Scroll {scroll_count}: Scraped {new_added} NEW (Total Unique: {len(unique_tools_map)})")
                    save_chunk_to_csv(list(unique_tools_map.values()))

                if scroll_count >= MAX_SCROLLS:
                    break

            except Exception as e:
                print(f"      ⚠️ Error: {e}")
                break

        # Final Sweep
        final = await extract_visible_tools(page)
        for t in final:
            unique_tools_map[t['internal_slug']] = t
            
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
            
            for item in all_tools:
                item['internal_detail_url'] = f"{BASE_URL}{item['internal_slug']}"

            tasks = [get_external_link(context, item, semaphore) for item in all_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 50 == 0:
                    print(f"      Processed {i+1}/{len(all_tools)} tools...", end="\r")
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
    asyncio.run(harvest_microlaunch())