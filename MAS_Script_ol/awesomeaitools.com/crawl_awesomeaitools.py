import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://awesomeaitools.com"
START_URL = "https://awesomeaitools.com/discover"
OUTPUT_FILE = "awesomeaitools_complete.csv"

MAX_PAGES = 2000  # Set high to cover all pages
SAVE_INTERVAL = 5 

def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "tags", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

async def extract_tools_from_page(page):
    return await page.evaluate("""() => {
        const results = [];
        const cards = document.querySelectorAll('div[data-slot="card"]');
        
        cards.forEach(card => {
            try {
                const titleLink = card.querySelector('a[href*="/ai-tool/"]');
                const name = titleLink ? titleLink.innerText.trim() : "Unknown";
                const internal_slug = titleLink ? titleLink.getAttribute('href') : "";
                
                const descEl = card.querySelector('p.text-muted-foreground');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                const visitBtn = card.querySelector('a[data-slot="button"]');
                let external_link = "";
                if (visitBtn) {
                    external_link = visitBtn.getAttribute('href');
                }

                const badges = [];
                card.querySelectorAll('span[data-slot="badge"]').forEach(b => badges.push(b.innerText.trim()));

                if (internal_slug) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        tags: badges.join(', '),
                        external_link: external_link,
                        internal_detail_url: internal_slug.startsWith('http') ? internal_slug : "https://awesomeaitools.com" + internal_slug
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_awesomeaitools():
    async with async_playwright() as p:
        print("--- 🚀 Harvesting AwesomeAITools.com ---")
        
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
                
                try:
                    await page.wait_for_selector('div[data-slot="card"]', timeout=10000)
                except:
                    print("      ⚠️ No cards found on page.")
                    # Don't break immediately, check pagination first

                # Extract
                tools = await extract_tools_from_page(page)
                all_tools.extend(tools)
                print(f"   📄 Page {page_num}: Found {len(tools)} tools. (Total: {len(all_tools)})")
                
                if page_num % SAVE_INTERVAL == 0:
                    save_chunk_to_csv(all_tools)

                # --- PAGINATION FIX ---
                # Find "Next" button link
                next_btn = page.locator('a[aria-label="Go to next page"]')
                
                if await next_btn.count() > 0:
                    # Get the HREF directly. 
                    # If it contains "?cursor", it is a valid next page.
                    next_href = await next_btn.get_attribute("href")
                    
                    # Check if it is a disabled link (usually "#" or empty)
                    if next_href and len(next_href) > 2 and "cursor=" in next_href:
                        if next_href.startswith("http"):
                            current_url = next_href
                        else:
                            current_url = BASE_URL + next_href
                        
                        page_num += 1
                        await asyncio.sleep(1) # Polite wait
                    else:
                        print("      ✅ Next button has no cursor link. Crawl complete.")
                        break
                else:
                    print("      ✅ No Next button found. Crawl complete.")
                    break

            except Exception as e:
                print(f"      ❌ Error on page {page_num}: {e}")
                break
        
        await browser.close()
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        if not df.empty:
            df = df.drop_duplicates(subset=['internal_detail_url'])
            unique_tools = df.to_dict('records')
        else:
            unique_tools = []

        print(f"   ✨ Crawl Complete. Unique Tools: {len(unique_tools)}")
        save_chunk_to_csv(unique_tools)

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(harvest_awesomeaitools())