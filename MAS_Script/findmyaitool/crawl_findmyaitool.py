import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys

# --- CONFIGURATION ---
OUTPUT_FILE = "findmyaitool_complete.csv"
MAX_PAGES = 100
SAVE_INTERVAL = 5

CATEGORY_URLS = [
    "https://findmyaitool.com/category/copywriting",
    "https://findmyaitool.com/category/email-assistant",
    "https://findmyaitool.com/category/general-writing",
    "https://findmyaitool.com/category/paraphrase",
    "https://findmyaitool.com/category/prompts",
    "https://findmyaitool.com/category/seo",
    "https://findmyaitool.com/category/social-media-assistant",
    "https://findmyaitool.com/category/story-teller",
    "https://findmyaitool.com/category/summarizer",
    "https://findmyaitool.com/category/ai-content-detectors",
    "https://findmyaitool.com/category/humanize-ai-content",
    "https://findmyaitool.com/category/art",
    "https://findmyaitool.com/category/avatars",
    "https://findmyaitool.com/category/design-assistant",
    "https://findmyaitool.com/category/image-editing",
    "https://findmyaitool.com/category/logo-generator",
    "https://findmyaitool.com/category/image-generator",
    "https://findmyaitool.com/category/nsfw-character",
    "https://findmyaitool.com/category/ai-face-swap-generator",
    "https://findmyaitool.com/category/anime-generator",
    "https://findmyaitool.com/category/code-assistant",
    "https://findmyaitool.com/category/developer-tools",
    "https://findmyaitool.com/category/low-codeno-code",
    "https://findmyaitool.com/category/spreadsheets",
    "https://findmyaitool.com/category/sql",
    "https://findmyaitool.com/category/audio-editing",
    "https://findmyaitool.com/category/music",
    "https://findmyaitool.com/category/text-to-speech",
    "https://findmyaitool.com/category/transcriber",
    "https://findmyaitool.com/category/personalized-videos",
    "https://findmyaitool.com/category/video-editing",
    "https://findmyaitool.com/category/video-generator",
    "https://findmyaitool.com/category/3d",
    "https://findmyaitool.com/category/customer-support",
    "https://findmyaitool.com/category/ecommerce",
    "https://findmyaitool.com/category/education-assistant",
    "https://findmyaitool.com/category/fashion",
    "https://findmyaitool.com/category/finance",
    "https://findmyaitool.com/category/legal-assistant",
    "https://findmyaitool.com/category/personalization",
    "https://findmyaitool.com/category/productivity",
    "https://findmyaitool.com/category/real-estate",
    "https://findmyaitool.com/category/sales",
    "https://findmyaitool.com/category/startup",
    "https://findmyaitool.com/category/memory",
    "https://findmyaitool.com/category/presentations",
    "https://findmyaitool.com/category/human-resources",
    "https://findmyaitool.com/category/website-builder",
    "https://findmyaitool.com/category/resources",
    "https://findmyaitool.com/category/experiments",
    "https://findmyaitool.com/category/fun",
    "https://findmyaitool.com/category/gaming",
    "https://findmyaitool.com/category/gift-ideas",
    "https://findmyaitool.com/category/health-care",
    "https://findmyaitool.com/category/life-assistant",
    "https://findmyaitool.com/category/research",
    "https://findmyaitool.com/category/search-engine",
    "https://findmyaitool.com/category/fitness",
    "https://findmyaitool.com/category/travel",
    "https://findmyaitool.com/category/ai-girlfrend-chat-dating",
    "https://findmyaitool.com/category/virtual-influencer"
]

def save_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def resolve_link(browser, item):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item
    
    if not internal_url.startswith("http"):
        internal_url = f"https://findmyaitool.com{internal_url}"

    context = browser.new_context()
    page = context.new_page()
    
    try:
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        try:
            page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        except:
            pass
            
        # 1. Get Description
        try:
            desc = page.locator('h2:has-text("What is") + p').first.inner_text()
            item['description'] = desc
        except:
            pass

        # 2. Get External Link
        external_link = ""
        try:
            btn = page.locator('button[aria-label="Explore Website"], button:has-text("Explore Website")').first
            if btn.count() == 0:
                btn = page.locator('a[aria-label="explore-website"]').first
            
            if btn.count() > 0:
                # If button wraps anchor or is anchor
                href = btn.get_attribute('href')
                if not href:
                    parent = btn.locator('..')
                    if parent.count() > 0 and parent.evaluate("el => el.tagName === 'A'"):
                        href = parent.get_attribute('href')
                
                external_link = href
        except:
            pass

        if external_link:
            if "?fpr=" in external_link: external_link = external_link.split("?")[0]
            item['external_link'] = external_link

    except:
        pass
    finally:
        page.close()
        context.close()

    return item

def harvest_findmyaitool():
    with sync_playwright() as p:
        print("--- 🚀 Starting FindMyAITool Crawler (Sync Mode) ---")
        
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context()
        page = context.new_page()

        global_tools = {}
        
        # --- PHASE 1 ---
        for cat_url in CATEGORY_URLS:
            cat_name = cat_url.strip('/').split('/')[-1]
            print(f"   👉 Category: {cat_name}")
            
            current_page = 1
            while current_page <= MAX_PAGES:
                try:
                    page.goto(cat_url, timeout=60000, wait_until="domcontentloaded")
                    
                    # Check for items
                    try:
                        page.wait_for_selector('a[href^="/tool/"]', timeout=5000)
                    except:
                        break

                    # Extract
                    tools = page.evaluate("""() => {
                        const results = [];
                        const cards = document.querySelectorAll('a[href^="/tool/"]');
                        cards.forEach(card => {
                            try {
                                const href = card.getAttribute('href');
                                const nameEl = card.querySelector('p');
                                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                if (href) {
                                    results.push({
                                        tool_name: name,
                                        internal_detail_url: href
                                    });
                                }
                            } catch (e) {}
                        });
                        return results;
                    }""")

                    new_count = 0
                    for t in tools:
                        full_url = f"https://findmyaitool.com{t['internal_detail_url']}"
                        if full_url not in global_tools:
                            global_tools[full_url] = {
                                "tool_name": t['tool_name'],
                                "description": "",
                                "internal_detail_url": full_url,
                                "category_url": cat_url,
                                "external_link": ""
                            }
                            new_count += 1
                    
                    if new_count > 0:
                        save_csv(list(global_tools.values()))
                    
                    # Pagination
                    next_arrow = page.locator('div.pagination_arrow___5499').last
                    if next_arrow.count() > 0 and next_arrow.is_visible():
                        next_arrow.click()
                        time.sleep(2)
                        current_page += 1
                    else:
                        break
                        
                except Exception as e:
                    print(f"      ❌ Error: {e}")
                    break
        
        all_tools = list(global_tools.values())
        print(f"   ✨ Phase 1 Complete. Total: {len(all_tools)}")
        
        # --- PHASE 2 ---
        print(f"--- 🕵️‍♀️ Phase 2: Resolving Links (Sequential) ---")
        count = 0
        for item in all_tools:
            resolve_link(browser, item)
            count += 1
            if count % 20 == 0:
                print(f"      Processed {count}/{len(all_tools)}...", end="\r")
                save_csv(all_tools)
        
        save_csv(all_tools)
        print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")
        
        browser.close()

if __name__ == "__main__":
    harvest_findmyaitool()