import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
OUTPUT_FILE = "aitoolhouse_complete.csv"

# Full list of categories to scrape
TARGET_URLS = [
    "https://www.aitoolhouse.com/category/text/summarizer",
    "https://www.aitoolhouse.com/category/text/general-writing",
    "https://www.aitoolhouse.com/category/text/social-media-assistant",
    "https://www.aitoolhouse.com/category/text/copywriting",
    "https://www.aitoolhouse.com/category/text/story-teller",
    "https://www.aitoolhouse.com/category/image/image-generator",
    "https://www.aitoolhouse.com/category/image/design-assistant",
    "https://www.aitoolhouse.com/category/image/logo-generator",
    "https://www.aitoolhouse.com/category/image/art",
    "https://www.aitoolhouse.com/category/image/image-editing",
    "https://www.aitoolhouse.com/category/code/low-codeno-code",
    "https://www.aitoolhouse.com/category/code/developer-tools",
    "https://www.aitoolhouse.com/category/code/code-assistant",
    "https://www.aitoolhouse.com/category/code/spreadsheets",
    "https://www.aitoolhouse.com/category/code/sql",
    "https://www.aitoolhouse.com/category/audio/transcriber",
    "https://www.aitoolhouse.com/category/audio/text-to-speech",
    "https://www.aitoolhouse.com/category/audio/audio-editing",
    "https://www.aitoolhouse.com/category/audio/music",
    "https://www.aitoolhouse.com/category/video/video-generator",
    "https://www.aitoolhouse.com/category/video/video-editing",
    "https://www.aitoolhouse.com/category/video/personalized-videos",
    "https://www.aitoolhouse.com/category/video/video-enhancer",
    "https://www.aitoolhouse.com/category/video/video-generators",
    "https://www.aitoolhouse.com/category/3d/3d",
    "https://www.aitoolhouse.com/category/business/e-commerce",
    "https://www.aitoolhouse.com/category/business/productivity",
    "https://www.aitoolhouse.com/category/business/education-assistant",
    "https://www.aitoolhouse.com/category/business/human-resources",
    "https://www.aitoolhouse.com/category/business/sales",
    "https://www.aitoolhouse.com/category/others/search-engine",
    "https://www.aitoolhouse.com/category/others/life-assistant",
    "https://www.aitoolhouse.com/category/others/fun-tools",
    "https://www.aitoolhouse.com/category/others/research",
    "https://www.aitoolhouse.com/category/others/gaming"
]

# Limits
MAX_CONCURRENT_CATEGORIES = 5
MAX_CONCURRENT_DETAILS = 10

# --- HELPER: LIVE SAVE ---
def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

# --- PHASE 1: HARVEST CATEGORY ---
async def harvest_category(context, url, semaphore, global_tools_map):
    async with semaphore:
        page = await context.new_page()
        cat_name = url.split('/')[-1]
        print(f"   🚀 Started Category: {cat_name}")
        
        try:
            await page.goto(url, timeout=60000, wait_until="domcontentloaded")
            await asyncio.sleep(2)

            while True:
                # 1. Extract Tools
                tools = await page.evaluate("""() => {
                    const results = [];
                    const cards = document.querySelectorAll('div.MuiGrid-item .MuiCard-root');
                    
                    cards.forEach(card => {
                        try {
                            const linkEl = card.querySelector('a');
                            const href = linkEl ? linkEl.getAttribute('href') : "";
                            
                            const nameEl = card.querySelector('h3');
                            const name = nameEl ? nameEl.innerText.trim() : "Unknown";

                            if (href) {
                                results.push({
                                    tool_name: name,
                                    internal_slug: href
                                });
                            }
                        } catch (e) {}
                    });
                    return results;
                }""")
                
                # 2. Add to Global Map
                new_count = 0
                for t in tools:
                    full_url = f"https://www.aitoolhouse.com{t['internal_slug']}"
                    if full_url not in global_tools_map:
                        t['internal_detail_url'] = full_url
                        t['category_url'] = url
                        global_tools_map[full_url] = t
                        new_count += 1
                
                # 3. Pagination
                next_btn = page.locator('button[title="Next"]')
                
                if await next_btn.count() > 0:
                    # Check if disabled
                    is_disabled = await next_btn.is_disabled()
                    if is_disabled:
                        break 
                    
                    await next_btn.click()
                    await asyncio.sleep(2) # Wait for load
                else:
                    break

        except Exception as e:
            print(f"      ❌ Error in {cat_name}: {e}")
        finally:
            await page.close()
            print(f"   ✅ Finished Category: {cat_name}")

# --- PHASE 2: RESOLVE DETAILS ---
async def resolve_details(context, item, semaphore):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    async with semaphore:
        page = await context.new_page()
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # 1. Get Description
            try:
                desc_tag = page.locator("h2:has-text('What is') + p")
                if await desc_tag.count() > 0:
                    item['description'] = await desc_tag.inner_text()
            except:
                pass

            # 2. Get External Link
            # Targeted selector based on your snippet:
            # <a href="..." class="Tools_tools-main-data-title__WnzeG"><h1 ...>Gnomi App</h1><svg ... OpenInNewIcon ...></a>
            external_link = ""
            try:
                # Look for the specific class from your snippet
                link_el = page.locator('a[class*="Tools_tools-main-data-title"]').first
                
                if await link_el.count() > 0:
                    external_link = await link_el.get_attribute('href')
                
                # Fallback: Look for any H1 inside an Anchor tag
                if not external_link:
                    h1_link = page.locator('a:has(h1)').first
                    if await h1_link.count() > 0:
                        external_link = await h1_link.get_attribute('href')
                
                # Cleanup
                if external_link:
                    if "?utm" in external_link:
                        external_link = external_link.split("?")[0]
                    if "&utm" in external_link:
                        external_link = external_link.split("&")[0]

            except:
                pass
            
            item['external_link'] = external_link

        except Exception:
            pass
        finally:
            await page.close()
    
    return item

async def main():
    print("--- 🚀 Starting AIToolHouse Crawler ---")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        
        # --- PHASE 1 ---
        print(f"--- 📂 Phase 1: Crawling {len(TARGET_URLS)} categories... ---")
        global_tools_map = {}
        sem_phase1 = asyncio.Semaphore(MAX_CONCURRENT_CATEGORIES)
        
        tasks = [harvest_category(context, url, sem_phase1, global_tools_map) for url in TARGET_URLS]
        await asyncio.gather(*tasks)
        
        all_tools = list(global_tools_map.values())
        print(f"   ✨ Phase 1 Complete. Found {len(all_tools)} unique tools.")
        save_chunk_to_csv(all_tools)

        # --- PHASE 2 ---
        if all_tools:
            print(f"--- 🕵️‍♀️ Phase 2: Resolving External Links... ---")
            
            sem_phase2 = asyncio.Semaphore(MAX_CONCURRENT_DETAILS)
            detail_tasks = [resolve_details(context, item, sem_phase2) for item in all_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(detail_tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 50 == 0:
                    print(f"      Processed {i+1}/{len(all_tools)} tools...", end="\r")
                    save_chunk_to_csv(final_results + all_tools[len(final_results):])
            
            save_chunk_to_csv(final_results)
            print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

        await browser.close()

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())