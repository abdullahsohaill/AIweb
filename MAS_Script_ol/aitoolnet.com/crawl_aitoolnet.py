import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
OUTPUT_FILE = "aitoolnet_complete.csv"

CATEGORY_URLS = [
    "https://www.aitoolnet.com/productivity",
    "https://www.aitoolnet.com/spreadsheets",
    "https://www.aitoolnet.com/copywriting",
    "https://www.aitoolnet.com/startup-tools",
    "https://www.aitoolnet.com/video",
    "https://www.aitoolnet.com/text-to-speech",
    "https://www.aitoolnet.com/email-assistant",
    "https://www.aitoolnet.com/social-media-assistant",
    "https://www.aitoolnet.com/fun-tools",
    "https://www.aitoolnet.com/image-editing",
    "https://www.aitoolnet.com/avatars",
    "https://www.aitoolnet.com/image-generator",
    "https://www.aitoolnet.com/seo",
    "https://www.aitoolnet.com/code-assistant",
    "https://www.aitoolnet.com/music",
    "https://www.aitoolnet.com/presentations",
    "https://www.aitoolnet.com/education-assistant",
    "https://www.aitoolnet.com/art",
    "https://www.aitoolnet.com/gaming",
    "https://www.aitoolnet.com/sales",
    "https://www.aitoolnet.com/life-assistant",
    "https://www.aitoolnet.com/customer-support",
    "https://www.aitoolnet.com/developer-tools",
    "https://www.aitoolnet.com/search-engines",
    "https://www.aitoolnet.com/design-assistant",
    "https://www.aitoolnet.com/3d",
    "https://www.aitoolnet.com/legal-assistant",
    "https://www.aitoolnet.com/healthcare",
    "https://www.aitoolnet.com/prompts",
    "https://www.aitoolnet.com/research",
    "https://www.aitoolnet.com/audio",
    "https://www.aitoolnet.com/human-resources",
    "https://www.aitoolnet.com/story-teller",
    "https://www.aitoolnet.com/fashion",
    "https://www.aitoolnet.com/ecommerce",
    "https://www.aitoolnet.com/finance",
    "https://www.aitoolnet.com/meeting-assistant",
    "https://www.aitoolnet.com/chatbots",
    "https://www.aitoolnet.com/photo-editing",
    "https://www.aitoolnet.com/marketing",
    "https://www.aitoolnet.com/automation",
    "https://www.aitoolnet.com/large-language-models",
    "https://www.aitoolnet.com/data",
    "https://www.aitoolnet.com/business",
    "https://www.aitoolnet.com/machine-learning",
    "https://www.aitoolnet.com/slack",
    "https://www.aitoolnet.com/reading",
    "https://www.aitoolnet.com/qampa",
    "https://www.aitoolnet.com/grammar-checking",
    "https://www.aitoolnet.com/learning",
    "https://www.aitoolnet.com/ai-content-detection",
    "https://www.aitoolnet.com/speech-to-text",
    "https://www.aitoolnet.com/voice",
    "https://www.aitoolnet.com/deepfakes",
    "https://www.aitoolnet.com/paraphrasing",
    "https://www.aitoolnet.com/nsfw",
    "https://www.aitoolnet.com/homeworkifyai"
]

MAX_CONCURRENT_CATEGORIES = 5  
PAGE_LIMIT_PER_CATEGORY = 150 

# --- HELPER: LIVE SAVE ---
def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "likes", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

async def harvest_category(context, base_url, semaphore, global_tools):
    async with semaphore:
        page = await context.new_page()
        cat_name = base_url.split('/')[-1]
        print(f"   🚀 Started Category: {cat_name}")
        
        current_page_num = 1
        
        try:
            while current_page_num <= PAGE_LIMIT_PER_CATEGORY:
                # CORRECTED URL LOGIC:
                # Page 1 = base_url
                # Page 2+ = base_url/2
                if current_page_num == 1:
                    url = base_url
                else:
                    url = f"{base_url}/{current_page_num}"
                
                try:
                    # Block media to speed up
                    await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
                    
                    # High timeout as requested
                    response = await page.goto(url, timeout=300000, wait_until="domcontentloaded")
                    
                    # Check if blocked or empty
                    if response and response.status != 200:
                        print(f"      ⚠️ {cat_name} Page {current_page_num} Error: HTTP {response.status}")
                        if response.status == 404:
                             break # End of category
                    
                    # Wait for items
                    try:
                        await page.wait_for_selector('li.services-list__item', timeout=10000)
                    except:
                        # If no items found, verify content length to ensure it's not just slow loading
                        content_len = len(await page.content())
                        if content_len < 5000: # Arbitrary small size indicating empty/blocked page
                             # print(f"      ⚠️ {cat_name} Page {current_page_num}: No items found.")
                             break

                    # Extract using JS
                    tools = await page.evaluate("""() => {
                        const results = [];
                        const cards = document.querySelectorAll('li.services-list__item');
                        
                        cards.forEach(card => {
                            try {
                                // Name
                                const nameEl = card.querySelector('h3.title a');
                                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                const internal = nameEl ? nameEl.getAttribute('href') : "";
                                
                                // External Link (Visit Website icon)
                                const extEl = card.querySelector('div.shrink a');
                                let extLink = extEl ? extEl.getAttribute('href') : "";
                                
                                // Description
                                const descEl = card.querySelector('p.tagline');
                                const desc = descEl ? descEl.innerText.trim() : "";
                                
                                // Likes
                                const likesEl = card.querySelector('a.loginBtn span');
                                const likes = likesEl ? likesEl.innerText.trim() : "0";

                                if (internal) {
                                    results.push({
                                        tool_name: name,
                                        description: desc,
                                        external_link: extLink,
                                        likes: likes,
                                        internal_slug: internal
                                    });
                                }
                            } catch (e) {}
                        });
                        return results;
                    }""")

                    if not tools:
                        break

                    # Add to global list
                    count = 0
                    for t in tools:
                        full_internal = f"https://www.aitoolnet.com{t['internal_slug']}"
                        
                        # Clean external link
                        ext = t['external_link']
                        if ext and "?ref=" in ext:
                            ext = ext.split("?")[0]
                        
                        # Check duplicate
                        if full_internal not in global_tools:
                            global_tools[full_internal] = {
                                "tool_name": t['tool_name'],
                                "external_link": ext,
                                "description": t['description'],
                                "likes": t['likes'],
                                "internal_detail_url": full_internal,
                                "category_url": base_url
                            }
                            count += 1
                    
                    # LIVE SAVE
                    if count > 0:
                        save_chunk_to_csv(list(global_tools.values()))
                        # Log periodically
                        if current_page_num % 2 == 0:
                            print(f"      {cat_name} Page {current_page_num}: +{count} new.")

                    # Pagination Check
                    # Check if ">" button exists. If not, we are at end.
                    next_btn = page.locator('ul.pagination a:has-text(">")')
                    if await next_btn.count() == 0:
                        break
                    
                    current_page_num += 1
                    
                except Exception as e:
                    print(f"      ❌ Error on {cat_name} page {current_page_num}: {e}")
                    break

        finally:
            await page.close()
            print(f"   ✅ Finished Category: {cat_name}")

async def main():
    print("--- 🚀 Starting AIToolNet Crawler ---")
    
    async with async_playwright() as p:
        # Launch Headless=True for speed/background
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        global_tools = {}
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_CATEGORIES)
        
        tasks = [harvest_category(context, url, semaphore, global_tools) for url in CATEGORY_URLS]
        
        await asyncio.gather(*tasks)
        
        all_data = list(global_tools.values())
        save_chunk_to_csv(all_data)
        print(f"🎉 DONE! Saved {len(all_data)} tools to {OUTPUT_FILE}")
        
        await browser.close()

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())