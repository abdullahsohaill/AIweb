import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import random

# --- CONFIGURATION ---
OUTPUT_FILE = "easywithai_complete.csv"

CATEGORY_URLS = [
    "https://easywithai.com/ai-writers/",
    "https://easywithai.com/ai-marketing-tools/",
    "https://easywithai.com/ai-email-tools/",
    "https://easywithai.com/ai-social-media-tools/",
    "https://easywithai.com/ai-website-builders/",
    "https://easywithai.com/ai-paraphrasing-tools/",
    "https://easywithai.com/ai-ecommerce-tools/",
    "https://easywithai.com/ai-content-detectors/",
    "https://easywithai.com/ai-customer-service-tools/",
    "https://easywithai.com/free-ai-logo-generators/",
    "https://easywithai.com/ai-seo-tools/",
    "https://easywithai.com/ai-presentation-makers/",
    "https://easywithai.com/ai-image-generators/",
    "https://easywithai.com/ai-image-upscalers/",
    "https://easywithai.com/ai-image-editors/",
    "https://easywithai.com/ai-portrait-generators/",
    "https://easywithai.com/ai-product-images/",
    "https://easywithai.com/ai-qr-code-generators/",
    "https://easywithai.com/ai-video-tools/",
    "https://easywithai.com/ai-audio-tools/",
    "https://easywithai.com/ai-video-generators/",
    "https://easywithai.com/ai-music-generators/",
    "https://easywithai.com/ai-podcast-tools/",
    "https://easywithai.com/ai-voice-tools/",
    "https://easywithai.com/ai-design-tools/",
    "https://easywithai.com/ai-streaming-tools/",
    "https://easywithai.com/ai-chatbots/",
    "https://easywithai.com/ai-productivity-tools/",
    "https://easywithai.com/ai-educational-tools/",
    "https://easywithai.com/ai-mobile-apps/",
    "https://easywithai.com/resources/",
    "https://easywithai.com/ai-text-to-speech/",
    "https://easywithai.com/ai-developer-tools/",
    "https://easywithai.com/ai-coding-tools/",
    "https://easywithai.com/ai-business-tools/",
    "https://easywithai.com/ai-recruitment-tools/",
    "https://easywithai.com/ai-meeting-assistants/",
    "https://easywithai.com/ai-user-research-tools/",
    "https://easywithai.com/ai-lifestyle-tools/",
    "https://easywithai.com/fun-ai-tools/",
    "https://easywithai.com/ai-transcription-tools/",
    "https://easywithai.com/ai-data-management-tools/",
    "https://easywithai.com/ai-pdf-tools/",
    "https://easywithai.com/ai-architecture-tools/",
    "https://easywithai.com/ai-real-estate-tools/",
    "https://easywithai.com/ai-apis/",
    "https://easywithai.com/large-language-models/",
    "https://easywithai.com/ai-game-dev-tools/",
    "https://easywithai.com/ai-3d-assets-textures/",
    "https://easywithai.com/ai-story-generators/",
    "https://easywithai.com/ai-communication-tools/",
    "https://easywithai.com/ai-translation-tools/",
    "https://easywithai.com/ai-nsfw-tools/",
    "https://easywithai.com/ai-agents/",
    "https://easywithai.com/ai-prompt-tools/",
    "https://easywithai.com/ai-finance-tools/",
    "https://easywithai.com/chatgpt-extensions/",
    "https://easywithai.com/ai-test-automation-tools/",
    "https://easywithai.com/ai-language-learning/",
    "https://easywithai.com/stable-diffusion-ui/",
    "https://easywithai.com/ai-trading-tools/",
    "https://easywithai.com/health-and-fitness-ai-tools/",
    "https://easywithai.com/ai-legal-tools/",
    "https://easywithai.com/ai-voice-assistants/",
    "https://easywithai.com/ai-accessibility-tools/",
    "https://easywithai.com/ai-chrome-extensions/",
    "https://easywithai.com/ai-research-tools/",
    "https://easywithai.com/ai-cybersecurity-tools/",
    "https://easywithai.com/ai-devices/",
    "https://easywithai.com/ai-travel-planners/",
    "https://easywithai.com/ai-architecture-makers/"
]

SCROLL_DELAY = 1.0
MAX_PAGES_PER_CATEGORY = 150

def save_chunk_to_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

async def check_for_block(page):
    """Checks if Cloudflare has blocked us and asks user for help."""
    title = await page.title()
    content = await page.content()
    
    if "Just a moment" in title or "Attention Required" in title or "Security Check" in title or "been blocked" in content:
        print("\n\n🚨 CLOUDFLARE BLOCK DETECTED! 🚨")
        print("👉 Please solve the CAPTCHA in the browser window manually.")
        print("👉 Once the page loads normally, press ENTER here to continue...")
        input() # Pauses script
        print("✅ Resuming crawler...\n")
        return True
    return False

async def extract_tools(page):
    return await page.evaluate("""() => {
        const results = [];
        const cards = document.querySelectorAll('article.elementor-post');
        cards.forEach(card => {
            try {
                const nameEl = card.querySelector('h3.elementor-post__title a');
                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                const href = nameEl ? nameEl.getAttribute('href') : "";
                const descEl = card.querySelector('.elementor-post__excerpt p');
                const desc = descEl ? descEl.innerText.trim() : "";
                if (href) {
                    results.push({
                        tool_name: name,
                        description: desc,
                        internal_detail_url: href
                    });
                }
            } catch (e) {}
        });
        return results;
    }""")

async def get_external_link(page, internal_url):
    try:
        await page.goto(internal_url, timeout=6000000, wait_until="domcontentloaded")
        await check_for_block(page)
        
        # Find "Visit Site" button
        external_link = ""
        try:
            btn = page.locator('a.wp-block-button__link').first
            if await btn.count() > 0:
                external_link = await btn.get_attribute('href')
            
            if not external_link:
                btn = page.locator('a:has-text("Visit Site")').first
                if await btn.count() > 0:
                    external_link = await btn.get_attribute('href')
        except:
            pass
        
        if external_link and "?ref=" in external_link:
            external_link = external_link.split("?")[0]
            
        return external_link
    except:
        return ""

async def main():
    print("--- 🚀 Starting EasyWithAI Low-Profile Crawler ---")
    
    async with async_playwright() as p:
        # Visible browser (Headless=False)
        browser = await p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()
        global_tools = {}

        # --- PHASE 1: CATEGORIES (Sequential) ---
        print(f"--- 📂 Phase 1: Crawling Categories Sequentially... ---")
        
        for cat_url in CATEGORY_URLS:
            cat_name = cat_url.strip('/').split('/')[-1]
            print(f"   👉 Visiting: {cat_name}")
            
            current_page = 1
            while current_page <= MAX_PAGES_PER_CATEGORY:
                # Pagination URL logic
                url = cat_url if current_page == 1 else f"{cat_url.rstrip('/')}/page/{current_page}/"
                
                try:
                    await page.goto(url, timeout=60000, wait_until="domcontentloaded")
                    await check_for_block(page)
                    
                    # Check for 404 or Home redirect (End of list)
                    if page.url == "https://easywithai.com/" or (await page.title()) == "Page not found":
                        break
                        
                    # Scroll
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(1.5)
                    
                    # Extract
                    tools = await extract_tools(page)
                    if not tools: break
                    
                    new_count = 0
                    for t in tools:
                        if t['internal_detail_url'] not in global_tools:
                            t['category_url'] = cat_url
                            t['external_link'] = ""
                            global_tools[t['internal_detail_url']] = t
                            new_count += 1
                    
                    # print(f"      Pg {current_page}: +{new_count} tools")
                    if new_count == 0: break # No new tools found
                    
                    current_page += 1
                    save_chunk_to_csv(list(global_tools.values()))
                    
                except Exception as e:
                    print(f"      ❌ Error: {e}")
                    break
        
        all_tools = list(global_tools.values())
        print(f"   ✨ Phase 1 Complete. Total: {len(all_tools)}")

        # --- PHASE 2: SEQUENTIAL RESOLUTION ---
        # We must do this sequentially too to avoid triggering the block again
        print(f"--- 🕵️‍♀️ Phase 2: Resolving Links (Sequential) ---")
        
        for i, item in enumerate(all_tools):
            item['external_link'] = await get_external_link(page, item['internal_detail_url'])
            
            if (i + 1) % 10 == 0:
                print(f"      Processed {i+1}/{len(all_tools)}...", end="\r")
                save_chunk_to_csv(all_tools)
                
        save_chunk_to_csv(all_tools)
        print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")
        
        await browser.close()

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())