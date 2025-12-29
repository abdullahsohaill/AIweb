import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
OUTPUT_FILE = "thataicollection_complete.csv"

# Subcategories to scrape
CATEGORY_URLS = [
    "https://thataicollection.com/en/categories/speech/",
    "https://thataicollection.com/en/categories/ecommerce/",
    "https://thataicollection.com/en/categories/translation-and-transcript/",
    "https://thataicollection.com/en/categories/content-generation-and-seo/",
    "https://thataicollection.com/en/categories/logo-generator/",
    "https://thataicollection.com/en/categories/avatars/",
    "https://thataicollection.com/en/categories/plugins-and-extensions/",
    "https://thataicollection.com/en/categories/chat-bot/",
    "https://thataicollection.com/en/categories/social-networks-and-dating/"
]

MAX_CONCURRENT_CATEGORIES = 3
SCROLL_DELAY = 2.0

def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

async def harvest_category(context, url, semaphore, global_tools_map):
    async with semaphore:
        page = await context.new_page()
        cat_name = url.split('/')[-2]
        print(f"   🚀 Started Category: {cat_name}")
        
        try:
            await page.goto(url, timeout=60000, wait_until="domcontentloaded")
            await asyncio.sleep(2)

            # --- SCROLL TO BOTTOM ---
            # We need to scroll until height stops changing to load all items
            last_height = await page.evaluate("document.body.scrollHeight")
            
            while True:
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(SCROLL_DELAY)
                
                new_height = await page.evaluate("document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            
            # --- EXTRACT DATA ---
            # Based on snippet: <div class="m-auto" q:key="...">
            # We look for the card container
            
            tools = await page.evaluate("""() => {
                const results = [];
                // Select cards. They have class 'm-auto' and contain 'shadow-one'
                const cards = document.querySelectorAll('div.m-auto > div.shadow-one');
                
                cards.forEach(card => {
                    try {
                        // Name (h3 > a)
                        const nameEl = card.querySelector('h3 a');
                        const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                        
                        // Internal Link
                        const href = nameEl ? nameEl.getAttribute('href') : "";
                        
                        // Description (p tag with border-b)
                        const descEl = card.querySelector('p.border-b');
                        const desc = descEl ? descEl.innerText.trim() : "";
                        
                        // External Link (VISIT button)
                        // Look for anchor containing button with text VISIT
                        const visitBtn = card.querySelector('a:has(button)');
                        let external_link = "";
                        
                        if (visitBtn && visitBtn.innerText.includes("VISIT")) {
                            external_link = visitBtn.getAttribute('href');
                        } else {
                            // Fallback: any link with target _blank inside the button area
                            const blankLink = card.querySelector('div.flex.justify-between a[target="_blank"]');
                            if (blankLink) external_link = blankLink.getAttribute('href');
                        }

                        if (href) {
                            results.push({
                                tool_name: name,
                                description: desc,
                                external_link: external_link,
                                internal_slug: href
                            });
                        }
                    } catch (e) {}
                });
                return results;
            }""")
            
            # Add to global map
            new_count = 0
            for t in tools:
                full_internal = f"https://thataicollection.com{t['internal_slug']}"
                
                # Clean external link
                ext = t['external_link']
                if ext and "?ref=" in ext:
                    ext = ext.split("?")[0]

                if full_internal not in global_tools_map:
                    global_tools_map[full_internal] = {
                        "tool_name": t['tool_name'],
                        "description": t['description'],
                        "external_link": ext,
                        "internal_detail_url": full_internal,
                        "category_url": url
                    }
                    new_count += 1
            
            print(f"   ✅ Finished {cat_name}: Found {len(tools)} tools ({new_count} new).")

        except Exception as e:
            print(f"      ❌ Error in {cat_name}: {e}")
        finally:
            await page.close()

async def harvest_thataicollection():
    print("--- 🚀 Starting ThatAICollection Crawler ---")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        
        global_tools_map = {}
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_CATEGORIES)
        
        tasks = [harvest_category(context, url, semaphore, global_tools_map) for url in CATEGORY_URLS]
        await asyncio.gather(*tasks)
        
        all_tools = list(global_tools_map.values())
        print(f"   ✨ Crawl Complete. Total Unique Tools: {len(all_tools)}")
        
        save_chunk_to_csv(all_tools)
        print(f"🎉 DONE! Saved to {OUTPUT_FILE}")
        
        await browser.close()

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    asyncio.run(harvest_thataicollection())