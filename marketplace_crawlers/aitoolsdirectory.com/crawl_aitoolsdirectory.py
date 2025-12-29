import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://aitoolsdirectory.com"
START_URL = "https://aitoolsdirectory.com/?page=1"
OUTPUT_FILE = "aitoolsdirectory_complete.csv"

# Phase 2 Settings
MAX_CONCURRENT_TABS = 8
TIMEOUT_MS = 20000

async def resolve_link(context, item, semaphore):
    """
    Resolves tracking links. Skips if the link is already direct.
    """
    tracking_url = item.get('tracking_url')
    
    # If it's already a real website (not a redirector), keep it.
    if not tracking_url or "aitoolsdirectory.com" not in tracking_url:
        item['real_website_url'] = tracking_url
        return item

    async with semaphore:
        page = await context.new_page()
        final_url = tracking_url
        
        try:
            # Allow redirects
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
            
            try:
                await page.goto(tracking_url, timeout=TIMEOUT_MS, wait_until="commit")
            except:
                pass

            # Wait for URL change
            try:
                await page.wait_for_url(lambda u: "aitoolsdirectory.com" not in u.href, timeout=10000)
                final_url = page.url
            except:
                if "aitoolsdirectory.com" not in page.url and page.url != "about:blank":
                    final_url = page.url
            
            # Cleanup
            if "?" in final_url and "aitoolsdirectory.com" not in final_url:
                final_url = final_url.split("?")[0]

        except Exception:
            pass
        finally:
            await page.close()
    
    item['real_website_url'] = final_url
    return item

async def extract_tools_from_page(page):
    """
    Extracts data directly from the DOM using JS.
    """
    return await page.evaluate("""() => {
        const results = [];
        const cards = document.querySelectorAll('.sv-tile');
        
        cards.forEach(card => {
            try {
                // Name
                const nameEl = card.querySelector('.sv-tile__title');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Description
                const descEl = card.querySelector('.sv-tile__description');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // Price
                const priceEl = card.querySelector('.sv-tile__price');
                const price = priceEl ? priceEl.innerText.trim() : "";
                
                // Categories (Badges)
                const badges = card.querySelectorAll('.sv-badge');
                let categories = [];
                badges.forEach(b => categories.push(b.innerText.trim()));
                
                // Link (Details Button)
                const btn = card.querySelector('a.sv-tile__btn');
                const href = btn ? btn.getAttribute('href') : "";

                results.push({
                    tool_name: name,
                    description: desc,
                    categories: categories.join(', '),
                    pricing: price,
                    tracking_url: href
                });
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_aitoolsdirectory():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting Main List ---")
        
        browser = await p.chromium.launch(headless=False) # Visible to debug
        context = await browser.new_context()
        page = await context.new_page()

        # Start at page 1
        current_url = START_URL
        all_tools = []
        page_num = 1
        
        while True:
            print(f"   📄 Scraping Page {page_num}: {current_url}")
            try:
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
                
                # CRITICAL FIX: Wait for the cards to render
                try:
                    await page.wait_for_selector('.sv-tile', timeout=10000)
                except:
                    print("      ⚠️ No tools found on page (Timeout waiting for .sv-tile).")
                    break

                # Extract
                tools = await extract_tools_from_page(page)
                print(f"      ✅ Found {len(tools)} tools.")
                
                if not tools:
                    print("      🛑 List appears empty. Stopping.")
                    break
                    
                all_tools.extend(tools)

                # Pagination Logic
                # 1. Try to find Next button via Selector
                next_btn = page.locator('.sv-pagination__next:not(.disabled)')
                
                if await next_btn.count() > 0:
                    # If it has an anchor with href, use it
                    next_link = next_btn.locator('a')
                    href = await next_link.get_attribute('href')
                    
                    if href:
                        if href.startswith("/"):
                            current_url = f"{BASE_URL}{href}"
                        else:
                            current_url = href
                        page_num += 1
                        await asyncio.sleep(1) # Polite wait
                    else:
                        # JS Pagination? Try manual URL increment
                        page_num += 1
                        current_url = f"{BASE_URL}/?page={page_num}"
                else:
                    # No next button, but maybe we just need to try the URL manually?
                    # Let's check if we scraped a full page.
                    if len(tools) > 0:
                        # Try forcing next page URL just in case button is hidden
                        page_num += 1
                        current_url = f"{BASE_URL}/?page={page_num}"
                    else:
                        print("      🛑 End of list reached.")
                        break
            except Exception as e:
                print(f"      ❌ Page Error: {e}")
                break
        
        await browser.close()
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        if not df.empty:
            df = df.drop_duplicates(subset=['tracking_url'])
            unique_tools = df.to_dict('records')
        else:
            unique_tools = []

        print(f"   ✨ Phase 1 Complete. Total Unique Tools: {len(unique_tools)}")

        # --- PHASE 2: RESOLVE LINKS ---
        if unique_tools:
            print(f"\n--- 🚀 PHASE 2: Resolving Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            
            tasks = [resolve_link(context, item, semaphore) for item in unique_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 20 == 0:
                    print(f"      Processed {i+1}/{len(unique_tools)} tools...", end="\r")
            
            await browser.close()
            return final_results
        else:
            return []

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    cols = ["tool_name", "real_website_url", "description", "categories", "pricing", "tracking_url"]
    existing = [c for c in cols if c in df.columns]
    df = df[existing]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS! Saved {len(df)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_aitoolsdirectory())
    save_to_csv(data)