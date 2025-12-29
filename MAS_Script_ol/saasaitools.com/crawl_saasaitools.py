import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://saasaitools.com"
START_URL = "https://saasaitools.com/"
OUTPUT_FILE = "saasaitools_complete.csv"

MAX_CLICKS = 1000       
EXTRACT_INTERVAL = 5    
MAX_RETRIES = 5
MAX_CONCURRENT_TABS = 8

async def resolve_external_link(context, item, semaphore):
    """
    Visits internal page, finds 'Check out' button, follows redirect.
    """
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            # Visit Internal
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Check out" button
            # Selector: a.brxe-button or with text "Check out"
            visit_link = ""
            try:
                # Try specific ID from snippet first
                btn = page.locator("a#brxe-pdloqn").first
                if await btn.count() > 0:
                    visit_link = await btn.get_attribute('href')
                else:
                    # Fallback text selector
                    btn = page.locator("a:has-text('Check out')").first
                    if await btn.count() > 0:
                        visit_link = await btn.get_attribute('href')
            except:
                pass

            # Resolve the tracking link
            if visit_link:
                # If it's a tracking link, follow it
                if "saasaitools.com/go" in visit_link:
                    try:
                        await page.goto(visit_link, timeout=20000, wait_until="commit")
                        
                        # Wait for URL to change away from tracking domain
                        try:
                            await page.wait_for_url(lambda u: "saasaitools.com" not in u.href, timeout=8000)
                            final_url = page.url
                        except:
                            # If timed out, check if we are at least not on the tracking url
                            if "saasaitools.com/go" not in page.url:
                                final_url = page.url
                            else:
                                final_url = visit_link # Keep raw if fail
                    except:
                        final_url = visit_link
                else:
                    final_url = visit_link

            # Cleanup
            if "?" in final_url and "saasaitools.com" not in final_url:
                final_url = final_url.split("?")[0]

        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = final_url
    return item

async def extract_visible_tools(page):
    """
    Extracts tool data directly from DOM using JavaScript.
    """
    return await page.evaluate("""() => {
        const results = [];
        // Select tool cards
        // Based on snippet: <li class="brxe-mlkwec ...">
        const cards = document.querySelectorAll('li.brxe-mlkwec');
        
        cards.forEach(card => {
            try {
                // Internal Link & Name
                const titleLink = card.querySelector('h4 a');
                const name = titleLink ? titleLink.innerText.trim() : "Unknown";
                const href = titleLink ? titleLink.getAttribute('href') : "";
                
                // Description (Tagline)
                const descEl = card.querySelector('p.landing__listing-tagline--featured');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                if (href) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        internal_slug: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_saasaitools():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting SaaSAITools.com ---")
        
        browser = await p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        await page.goto(START_URL, timeout=90000, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        unique_tools_map = {}
        click_count = 0
        retries = 0
        
        while True:
            try:
                # 1. Get Count
                current_count = await page.locator('li.brxe-mlkwec').count()
                
                # 2. Find "Load More" Button
                load_more_btn = page.locator('button.wpgb-load-more')
                
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
                            f"document.querySelectorAll('li.brxe-mlkwec').length > {current_count}",
                            timeout=10000
                        )
                        retries = 0
                    except:
                        retries += 1
                        print(f"      ⚠️ Clicked but count ({current_count}) didn't rise (Strike {retries}/{MAX_RETRIES})")
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
                            if tool['internal_slug'] not in unique_tools_map:
                                unique_tools_map[tool['internal_slug']] = tool
                                new_added += 1
                        
                        print(f"      ⬇️  Click {click_count}: Scraped {new_added} NEW (Total Unique: {len(unique_tools_map)})")
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
                item['internal_detail_url'] = item['internal_slug'] # Already full URL from extraction

            tasks = [resolve_external_link(context, item, semaphore) for item in all_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 20 == 0:
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
    
    for col in ["external_link", "internal_detail_url", "description"]:
        if col not in df.columns: df[col] = ""
    
    cols = ["tool_name", "external_link", "description", "internal_detail_url"]
    existing = [c for c in cols if c in df.columns]
    df = df[existing]
    
    df.to_csv(OUTPUT_FILE, index=False)

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(harvest_saasaitools())