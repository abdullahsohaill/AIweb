import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://aitoolguru.com"
START_URL = "https://aitoolguru.com/"
OUTPUT_FILE = "aitoolguru_complete.csv"

# Scroll Settings
MAX_SCROLLS = 1000      # How many times to scroll down
SCROLL_DELAY = 2.0      # Wait time after scrolling
EXTRACT_INTERVAL = 5    # Save data every X scrolls
MAX_RETRIES = 5         # Retries if no new items appear

# Phase 2 Concurrency
MAX_CONCURRENT_TABS = 8

async def get_external_link(context, item, semaphore):
    """
    Visits internal page to get the external 'Visit' link.
    """
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        external_url = ""
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Visit" button
            # Selector: a.btn.btn-primary with text "Visit" or icon icon-earth
            try:
                # Try finding the specific Visit button
                visit_btn = page.locator("a.btn-primary:has-text('Visit')").first
                if await visit_btn.count() > 0:
                    external_url = await visit_btn.get_attribute('href')
                else:
                    # Fallback: any link inside .info-btn area
                    visit_btn = page.locator(".info-btn a[target='_blank']").first
                    if await visit_btn.count() > 0:
                        external_url = await visit_btn.get_attribute('href')
            except:
                pass

        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = external_url
    return item

async def extract_visible_tools(page):
    """
    Extracts data directly from the DOM using JS.
    """
    return await page.evaluate("""() => {
        const results = [];
        // Select tool cards
        // Based on snippet: <div class="col-12 col-sm-6 col-lg-4 mb-4"> -> <div class="tool-box">
        const cards = document.querySelectorAll('div.tool-box');
        
        cards.forEach(card => {
            try {
                // Internal Link & Name
                const linkEl = card.querySelector('a.tb-img');
                const href = linkEl ? linkEl.getAttribute('href') : "";
                
                // Name (h4 inside tbox-content)
                const nameEl = card.querySelector('h4');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Description (p tag)
                const descEl = card.querySelector('p');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // Price / Badges
                const priceEl = card.querySelector('.t-price');
                const price = priceEl ? priceEl.innerText.trim() : "";
                
                // Tags (Freemium, etc)
                const tags = [];
                card.querySelectorAll('.tag').forEach(t => tags.push(t.innerText.trim()));
                
                // Likes
                const likesEl = card.querySelector('.likes');
                const likes = likesEl ? likesEl.innerText.trim() : "0";

                if (href) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        pricing: price,
                        tags: tags.join(', '),
                        likes: likes,
                        internal_slug: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_aitoolguru():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting AIToolGuru (Infinite Scroll) ---")
        
        # Headless=False to verify scrolling visual
        browser = await p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(START_URL, timeout=90000, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        unique_tools_map = {}
        scroll_count = 0
        retries = 0
        
        # Initial count
        try:
            await page.wait_for_selector('div.tool-box', timeout=15000)
        except:
            print("⚠️ No tools found initially.")

        print("   🔄 Starting Scroll Loop...")
        
        while True:
            try:
                # 1. Get current height and count
                prev_height = await page.evaluate("document.body.scrollHeight")
                prev_count = await page.locator('div.tool-box').count()
                
                # 2. Scroll to bottom
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                
                # 3. Wait for load (Infinite scroll usually needs a moment)
                await asyncio.sleep(SCROLL_DELAY)
                
                # 4. Check for new items
                new_count = await page.locator('div.tool-box').count()
                new_height = await page.evaluate("document.body.scrollHeight")
                
                # If no new items or height didn't change significantly
                if new_count == prev_count:
                    retries += 1
                    print(f"      ⚠️ No new items loaded (Strike {retries}/{MAX_RETRIES}). Waiting...")
                    
                    # Try wiggling scroll up and down
                    await page.evaluate("window.scrollBy(0, -500)")
                    await asyncio.sleep(1)
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(3)
                    
                    if retries >= MAX_RETRIES:
                        print("      🛑 Max retries reached. End of list.")
                        break
                else:
                    retries = 0 # Reset
                    
                scroll_count += 1

                # 5. Incremental Save
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
                    print("      🛑 Max scrolls reached.")
                    break

            except Exception as e:
                print(f"      ⚠️ Scroll Error: {e}")
                break

        # Final Sweep
        print("   📥 Performing Final Sweep...")
        final_batch = await extract_visible_tools(page)
        for tool in final_batch:
            unique_tools_map[tool['internal_slug']] = tool
            
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
            return final_results
        else:
            return []

def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    
    for col in ["external_link", "internal_detail_url", "pricing", "likes", "tags"]:
        if col not in df.columns: df[col] = ""
    
    cols = ["tool_name", "external_link", "description", "pricing", "likes", "tags", "internal_detail_url"]
    existing = [c for c in cols if c in df.columns]
    df = df[existing]
    
    df.to_csv(OUTPUT_FILE, index=False)

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    asyncio.run(harvest_aitoolguru())