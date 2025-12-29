import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://aitools.fyi"
START_URL = "https://aitools.fyi/"
OUTPUT_FILE = "aitoolsfyi_complete.csv"

# Max clicks (adjust as needed)
MAX_CLICKS = 1000
EXTRACT_INTERVAL = 5  # Extract data every X clicks
MAX_RETRIES = 5       # Retry clicking if no new items appear

async def extract_visible_tools(page):
    """
    Runs JS inside the browser to extract data from all visible cards.
    """
    return await page.evaluate("""() => {
        const results = [];
        // Select the outer container for each tool
        // Based on snippet: <div class="flex rounded text-start bg-white ...">
        // A specific unique class combo is safest.
        const cards = document.querySelectorAll('div.flex.rounded.text-start.bg-white');
        
        cards.forEach(card => {
            try {
                // Name
                const nameEl = card.querySelector('h2');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                
                // Description
                const descEl = card.querySelector('p');
                const desc = descEl ? descEl.innerText.trim() : "";
                
                // External Link
                // The anchor tag wrapping the content usually has the direct link
                const linkEl = card.querySelector('a[href^="http"]');
                let external_link = linkEl ? linkEl.getAttribute('href') : "";
                
                // Categories / Pricing
                // These are in divs at the bottom
                const badges = card.querySelectorAll('div.absolute.bottom-0 a, div.absolute.bottom-0 div.items-center');
                let categories = [];
                let pricing = "";
                
                badges.forEach(badge => {
                    const text = badge.innerText.trim();
                    if (['Free', 'Freemium', 'Paid', 'Free Trial'].includes(text)) {
                        pricing = text;
                    } else {
                        categories.push(text);
                    }
                });

                // Upvotes
                // Inside button with SVG icon
                const voteBtn = card.querySelector('button');
                const votes = voteBtn ? voteBtn.innerText.trim() : "0";

                if (name !== "Unknown") {
                    results.push({
                        tool_name: name,
                        description: desc,
                        external_link: external_link,
                        categories: categories.join(', '),
                        pricing: pricing,
                        upvotes: votes
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def harvest_aitools_fyi():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting AITools.fyi ---")
        
        # Headless=False allows you to see progress
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        print(f"   🌐 Visiting: {START_URL}")
        await page.goto(START_URL, timeout=90000, wait_until="domcontentloaded")
        await asyncio.sleep(3)

        # Master Dictionary to store tools (Key = external_link + name to ensure uniqueness)
        unique_tools_map = {}
        
        print("   🔄 Starting 'Load More' Loop...")
        click_count = 0
        retries = 0
        
        while True:
            try:
                # 1. Capture current count
                current_count = await page.locator('div.flex.rounded.text-start.bg-white').count()
                
                # 2. Locate Button
                # Selector based on text "Load More"
                load_more_btn = page.locator('button:has-text("Load More")')
                
                if await load_more_btn.count() > 0 and await load_more_btn.is_visible():
                    
                    # Scroll to button
                    await load_more_btn.scroll_into_view_if_needed()
                    await asyncio.sleep(0.5)
                    
                    # Click (Try standard, fallback to JS)
                    try:
                        await load_more_btn.click(force=True, timeout=3000)
                    except:
                        await load_more_btn.evaluate("node => node.click()")
                    
                    click_count += 1
                    
                    # 3. SMART WAIT
                    # Wait for count to increase
                    try:
                        await page.wait_for_function(
                            f"document.querySelectorAll('div.flex.rounded.text-start.bg-white').length > {current_count}",
                            timeout=15000 # Wait up to 15s for new items
                        )
                        retries = 0 # Reset retries on success
                    except:
                        # Timeout: No new items appeared
                        retries += 1
                        print(f"      ⚠️ Clicked but no new items (Strike {retries}/{MAX_RETRIES}). Waiting 5s...")
                        await asyncio.sleep(5)
                        
                        # Double check
                        new_check = await page.locator('div.flex.rounded.text-start.bg-white').count()
                        if new_check == current_count:
                            if retries >= MAX_RETRIES:
                                print("      🛑 Max retries reached. Assuming end of list.")
                                break
                            else:
                                # Retry loop
                                continue
                        else:
                            print("      ✅ Recovered! Items loaded.")
                            retries = 0

                    # 4. INCREMENTAL SAVE
                    if click_count % EXTRACT_INTERVAL == 0:
                        batch = await extract_visible_tools(page)
                        new_items = 0
                        for tool in batch:
                            key = tool['external_link']
                            if key not in unique_tools_map:
                                unique_tools_map[key] = tool
                                new_items += 1
                        
                        print(f"      ⬇️  Click {click_count}: Found {new_items} NEW tools (Total Unique: {len(unique_tools_map)})")

                    if click_count >= MAX_CLICKS:
                        print("      🛑 Max clicks reached.")
                        break
                else:
                    print("      ✅ 'Load More' button gone. End of list.")
                    break

            except Exception as e:
                print(f"      ⚠️ Loop Error: {e}")
                break

        # Final Sweep
        print("   📥 Performing Final Extraction...")
        final_batch = await extract_visible_tools(page)
        for tool in final_batch:
            unique_tools_map[tool['external_link']] = tool
            
        await browser.close()
        
        # Process Results
        all_tools = list(unique_tools_map.values())
        print(f"   ✨ Crawl Complete. Total Unique Tools: {len(all_tools)}")
        
        return all_tools

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    # Clean up URL (remove ?ref=...)
    # Safe apply
    if 'external_link' in df.columns:
        df['clean_website_url'] = df['external_link'].apply(lambda x: x.split('?')[0] if x and '?' in x else x)
    
    cols = ["tool_name", "clean_website_url", "description", "categories", "pricing", "upvotes", "external_link"]
    existing = [c for c in cols if c in df.columns]
    df = df[existing]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS! Saved {len(df)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_aitools_fyi())
    save_to_csv(data)