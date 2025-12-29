import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://goodaitools.com"
START_URL = "https://goodaitools.com/latest"
OUTPUT_FILE = "goodaitools_complete.csv"

MAX_PAGES = 200  # Safety limit
MAX_RETRIES = 3  # Retry looking for next button

async def extract_tools_from_page(page):
    """
    Extracts data directly from the DOM using JS.
    """
    return await page.evaluate("""() => {
        const results = [];
        // Select card containers
        // Based on snippet: <div class="flex transform flex-col ...">
        // We look for the specific border/hover classes to identify cards
        const cards = document.querySelectorAll('div.flex.transform.flex-col.rounded-sm.border');
        
        cards.forEach(card => {
            try {
                // Name (h3 > a)
                const nameEl = card.querySelector('h3 a');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Internal Link
                const internalLink = nameEl ? nameEl.getAttribute('href') : "";
                
                // External Link (Visit button)
                // Look for anchor with text "Visit" inside the card
                // The snippet shows it's absolutely positioned at top right
                const visitBtn = card.querySelector('a[href^="http"]:not([href*="goodaitools.com"])');
                let external_link = "";
                
                // Sometimes visit button has "Visit" text explicitly
                if (!visitBtn) {
                     const explicitVisit = Array.from(card.querySelectorAll('a')).find(a => a.innerText.includes('Visit'));
                     if (explicitVisit) external_link = explicitVisit.getAttribute('href');
                } else {
                    external_link = visitBtn.getAttribute('href');
                }

                // Description (p tag)
                const descEl = card.querySelector('p.line-clamp-3');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // Category & Pricing
                // They are in spans at bottom
                const badges = card.querySelectorAll('div.mt-auto span');
                let category = "";
                let pricing = "";
                
                badges.forEach(span => {
                    const text = span.innerText.trim();
                    if (text.includes('Paid') || text.includes('Free') || text.includes('Trial')) {
                        pricing = text;
                    } else {
                        category = text;
                    }
                });

                results.push({
                    tool_name: name,
                    description: desc,
                    category: category,
                    pricing: pricing,
                    external_link: external_link,
                    internal_slug: internalLink
                });
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_goodaitools():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting GoodAITools.com ---")
        
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        current_url = START_URL
        all_tools = []
        page_num = 1
        
        await page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
        await asyncio.sleep(2)

        while page_num <= MAX_PAGES:
            print(f"   📄 Scraping Page {page_num}...")
            
            # 1. Extract Tools
            try:
                # Wait for cards to appear
                await page.wait_for_selector('div.flex.transform.flex-col', timeout=5000)
                
                tools = await extract_tools_from_page(page)
                print(f"      ✅ Found {len(tools)} tools.")
                
                if not tools:
                    print("      🛑 No tools found. End of list?")
                    break
                    
                all_tools.extend(tools)
                
            except Exception as e:
                print(f"      ⚠️ Error extracting: {e}")
                break

            # 2. Pagination (Find Next Button)
            # Selector: a containing text "Next"
            try:
                next_btn = page.locator('a:has-text("Next")')
                
                if await next_btn.count() > 0 and await next_btn.is_visible():
                    # Get URL just in case
                    next_href = await next_btn.get_attribute('href')
                    
                    # Click
                    await next_btn.click()
                    await asyncio.sleep(2) # Wait for load
                    
                    # Check if URL changed (simple verification)
                    if f"page={page_num}" in page.url and next_href:
                         # If URL didn't auto-update, force go
                         await page.goto(f"{BASE_URL}{next_href}" if next_href.startswith("/") else next_href)
                    
                    page_num += 1
                else:
                    print("      ✅ 'Next' button not found. Crawl complete.")
                    break
            except:
                print("      ✅ 'Next' button error (likely end of list).")
                break
        
        await browser.close()
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        if not df.empty:
            df = df.drop_duplicates(subset=['tool_name', 'external_link'])
            unique_tools = df.to_dict('records')
        else:
            unique_tools = []

        print(f"   ✨ Crawl Complete. Total Unique Tools: {len(unique_tools)}")
        return unique_tools

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    # Add full internal URL
    if 'internal_slug' in df.columns:
        df['internal_detail_url'] = df['internal_slug'].apply(lambda x: f"{BASE_URL}{x}" if x else "")
    
    cols = ["tool_name", "external_link", "description", "category", "pricing", "internal_detail_url"]
    existing = [c for c in cols if c in df.columns]
    df = df[existing]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS! Saved {len(df)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_goodaitools())
    save_to_csv(data)