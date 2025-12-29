import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://www.tools-ai.online"
START_URL = "https://www.tools-ai.online/"
OUTPUT_FILE = "toolsai_online_complete.csv"

MAX_PAGES = 150 
MAX_CONCURRENT_TABS = 8

def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    
    cols = ["tool_name", "external_link", "description", "pricing", "likes", "categories", "internal_detail_url"]
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
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Visit Site" button
            try:
                # Look for the button with specific text or link structure
                btn = page.locator('a:has-text("Visit Site")').first
                
                if await btn.count() > 0:
                    raw_url = await btn.get_attribute('href')
                    if raw_url:
                        # Clean referral params
                        if "?ref=" in raw_url:
                            external_url = raw_url.split("?")[0]
                        else:
                            external_url = raw_url
            except:
                pass

        except Exception:
            pass
        finally:
            await page.close()
    
    item['external_link'] = external_url
    return item

async def extract_tools_from_page(page):
    """
    Extracts data using the 'role=button' selector which is robust.
    """
    return await page.evaluate("""() => {
        const results = [];
        // Select tool cards based on role="button" (matches your HTML)
        const cards = document.querySelectorAll('div[role="button"]');
        
        cards.forEach(card => {
            try {
                // Internal Link
                const linkEl = card.querySelector('a[href^="/tool/"]');
                const href = linkEl ? linkEl.getAttribute('href') : "";
                
                // Name (inside font-semibold div)
                const nameEl = card.querySelector('.font-semibold.text-theme-black');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Description
                const descEl = card.querySelector('.font-light');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // Pricing (Badge)
                const priceEl = card.querySelector('div.text-xs.rounded-sm.text-white');
                const price = priceEl ? priceEl.innerText.trim() : "";
                
                // Likes
                const likeEl = card.querySelector('button[title="Upvote"] div');
                const likes = likeEl ? likeEl.innerText.trim() : "0";
                
                // Categories
                const tags = [];
                card.querySelectorAll('a[href^="/tag/"]').forEach(t => tags.push(t.innerText.trim()));

                if (href) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        pricing: price,
                        likes: likes,
                        categories: tags.join(', '),
                        internal_slug: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_toolsai_online():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting Tools-AI.online ---")
        
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        current_url = START_URL
        all_tools = []
        page_num = 1
        
        while page_num <= MAX_PAGES:
            print(f"   📄 Scraping Page {page_num}...", end="\r")
            
            try:
                await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
                
                # Wait for cards (using role=button selector)
                try:
                    await page.wait_for_selector('div[role="button"]', timeout=10000)
                except:
                    print("\n      ⚠️ No tools found on page (Timeout). End of list?")
                    break

                # Extract
                tools = await extract_tools_from_page(page)
                all_tools.extend(tools)
                
                print(f"   📄 Page {page_num}: Found {len(tools)} tools. (Total: {len(all_tools)})")
                save_chunk_to_csv(all_tools)

                # Pagination Logic
                # Find the active "Next" button.
                # Your HTML: <a ... href="/?page=2"><svg ...></a>
                # We construct the URL manually because it's safer than clicking icons
                
                page_num += 1
                current_url = f"{BASE_URL}/?page={page_num}"
                
                # Optional: Check if next page actually exists by checking the button state
                # But manually incrementing URL is often faster and standard for query params.
                
                await asyncio.sleep(1)

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
                item['internal_detail_url'] = f"{BASE_URL}{item['internal_slug']}"

            tasks = [get_external_link(context, item, semaphore) for item in unique_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 20 == 0:
                    print(f"      Processed {i+1}/{len(unique_tools)} tools...", end="\r")
                    save_chunk_to_csv(final_results + unique_tools[len(final_results):])

            await browser.close()
            save_chunk_to_csv(final_results)
            print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")
            return final_results
        else:
            return []

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(harvest_toolsai_online())