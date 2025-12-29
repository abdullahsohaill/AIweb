import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys

# --- CONFIGURATION ---
OUTPUT_FILE = "aixploria_complete.csv"
MAX_PAGES_PER_CATEGORY = 50 # Adjust as needed
SAVE_INTERVAL = 5

CATEGORY_URLS = [
    "https://www.aixploria.com/en/category/3d-model/",
    "https://www.aixploria.com/en/category/best-ai-agents/",
    "https://www.aixploria.com/en/category/best-ai-characters-chatbots-lists/",
    "https://www.aixploria.com/en/category/ai-chat-assistant/",
    "https://www.aixploria.com/en/category/ai-detection-en/",
    "https://www.aixploria.com/en/category/ai-simulation-3d-world/",
    "https://www.aixploria.com/en/category/ia-useful/",
    "https://www.aixploria.com/en/category/featured-en/",
    "https://www.aixploria.com/en/category/amazing/",
    "https://www.aixploria.com/en/category/art-en/",
    "https://www.aixploria.com/en/category/assistant-code-en/",
    "https://www.aixploria.com/en/category/ai-assistive-technology-at/",
    "https://www.aixploria.com/en/category/audio-editing/",
    "https://www.aixploria.com/en/category/automation-ai-workflows/",
    "https://www.aixploria.com/en/category/avatars-en/",
    "https://www.aixploria.com/en/list-best-ai-discord-servers/",
    "https://www.aixploria.com/en/best-ai-girlfriend-apps-websites/",
    "https://www.aixploria.com/en/list-best-mcp-servers-directory-ai/",
    "https://www.aixploria.com/en/category/business-study/",
    "https://www.aixploria.com/en/category/chatbot-ai/",
    "https://www.aixploria.com/en/category/customer-support/",
    "https://www.aixploria.com/en/category/data-analytics-ai/",
    "https://www.aixploria.com/en/category/dating-relationships-ai/",
    "https://www.aixploria.com/en/category/developer-tools/",
    "https://www.aixploria.com/en/category/e-commerce-en/",
    "https://www.aixploria.com/en/category/e-mail-en/",
    "https://www.aixploria.com/en/category/education-en/",
    "https://www.aixploria.com/en/category/extensions-chatgpt/",
    "https://www.aixploria.com/en/category/face-swap-deepfake-en/",
    "https://www.aixploria.com/en/category/fashion-en/",
    "https://www.aixploria.com/en/category/files-spreadsheets/",
    "https://www.aixploria.com/en/category/finance-en/",
    "https://www.aixploria.com/en/category/future-tools-ai/",
    "https://www.aixploria.com/en/category/games-en/",
    "https://www.aixploria.com/en/category/github-project-ai/",
    "https://www.aixploria.com/en/gpts-list-ai-directory/",
    "https://www.aixploria.com/en/category/healthcare/",
    "https://www.aixploria.com/en/hubspot-ai-tools-enterprises/",
    "https://www.aixploria.com/en/category/human-resources-ai/",
    "https://www.aixploria.com/en/category/image-editing/",
    "https://www.aixploria.com/en/category/image-ai-en/",
    "https://www.aixploria.com/en/category/last-ai-en/",
    "https://www.aixploria.com/en/category/legal-assistants/",
    "https://www.aixploria.com/en/category/life-assistants/",
    "https://www.aixploria.com/en/category/llm-model-ai-en/",
    "https://www.aixploria.com/en/category/best-ai-logo-generators/",
    "https://www.aixploria.com/en/category/marketing-ai/",
    "https://www.aixploria.com/en/category/memory-en/",
    "https://www.aixploria.com/en/category/music/",
    "https://www.aixploria.com/en/category/no-code-en/",
    "https://www.aixploria.com/en/category/presentation-en/",
    "https://www.aixploria.com/en/category/productivity-en/",
    "https://www.aixploria.com/en/category/prompts-help/",
    "https://www.aixploria.com/en/category/real-estate/",
    "https://www.aixploria.com/en/category/research-science-en/",
    "https://www.aixploria.com/en/category/ai-rip-en/",
    "https://www.aixploria.com/en/category/robots-devices-ai/",
    "https://www.aixploria.com/en/category/sales-conversion-leads/",
    "https://www.aixploria.com/en/category/search-engine/",
    "https://www.aixploria.com/en/category/seo-ai-tools/",
    "https://www.aixploria.com/en/category/social-assistants-en/",
    "https://www.aixploria.com/en/category/storytelling-generator/",
    "https://www.aixploria.com/en/category/ai-summarizer/",
    "https://www.aixploria.com/en/category/ai-supertools/",
    "https://www.aixploria.com/en/category/ai-text-generators/",
    "https://www.aixploria.com/en/category/voice-reading/",
    "https://www.aixploria.com/en/category/text-to-video-en/",
    "https://www.aixploria.com/en/top-100-ai/",
    "https://www.aixploria.com/en/category/transcriber/",
    "https://www.aixploria.com/en/category/translation-ai/",
    "https://www.aixploria.com/en/category/travel/",
    "https://www.aixploria.com/en/category/video-edition/",
    "https://www.aixploria.com/en/category/video-generators/",
    "https://www.aixploria.com/en/category/ai-voice-cloning/",
    "https://www.aixploria.com/en/category/websites-ai/",
    "https://www.aixploria.com/en/category/writing-web-seo/"
]

def save_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "likes", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def resolve_link(browser, item):
    """
    Visits the internal page to find the external link (Sync).
    """
    # Skip if we already have a good link
    curr = item.get('external_link', '')
    needs_resolve = False
    if not curr: needs_resolve = True
    if "/out/" in curr: needs_resolve = True
    if "aixploria.com" in curr and "/en/" in curr: needs_resolve = True 

    if not needs_resolve: return item

    context = browser.new_context()
    page = context.new_page()
    
    try:
        # Block media for speed
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        target = curr if curr else item.get('internal_detail_url')
        if not target: return item
        if not target.startswith("http"): target = f"https://www.aixploria.com{target}"

        try:
            page.goto(target, timeout=30000, wait_until="domcontentloaded")
        except:
            pass 

        # Check internal page for button
        if "aixploria.com/en/" in page.url:
            try:
                btn = page.locator("a.visit-site-button4").first
                if btn.count() > 0:
                    href = btn.get_attribute("href")
                    if href:
                        if href.startswith("/out/"):
                            # Follow redirect
                            try:
                                page.goto(f"https://www.aixploria.com{href}", timeout=30000, wait_until="domcontentloaded")
                            except:
                                pass
                        else:
                            item['external_link'] = href
                            return item
            except:
                pass

        # Capture final URL
        final = page.url
        if "aixploria.com" not in final and final != "about:blank":
            if "?ref" in final: final = final.split("?")[0]
            item['external_link'] = final

    except Exception:
        pass
    finally:
        page.close()
        context.close()
    
    return item

def harvest_aixploria():
    # SYNC PLAYWRIGHT MODE
    with sync_playwright() as p:
        print("--- 🚀 Starting AIxploria Crawler (Sync Mode) ---")
        
        # Headless=True for background. 
        # args=["--disable-blink-features=AutomationControlled"] helps avoid blocks.
        browser = p.chromium.launch(
            headless=True, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context()
        page = context.new_page()

        global_tools = {}
        
        # --- PHASE 1: CRAWL CATEGORIES ---
        print(f"--- 📂 Phase 1: Crawling {len(CATEGORY_URLS)} categories... ---")
        
        for cat_url in CATEGORY_URLS:
            cat_name = cat_url.strip('/').split('/')[-1]
            print(f"   👉 Category: {cat_name}")
            
            current_page = 1
            while current_page <= MAX_PAGES_PER_CATEGORY:
                if current_page == 1:
                    url = cat_url
                else:
                    url = f"{cat_url.rstrip('/')}/page/{current_page}/"
                
                try:
                    response = page.goto(url, timeout=60000, wait_until="domcontentloaded")
                    if response.status == 404: break
                    
                    # Wait for items
                    try:
                        page.wait_for_selector('div.post-item', timeout=5000)
                    except:
                        break # No items

                    # Scroll for lazy load
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(1)

                    # Extract
                    tools = page.evaluate("""() => {
                        const results = [];
                        const cards = document.querySelectorAll('div.post-item');
                        cards.forEach(card => {
                            try {
                                const nameEl = card.querySelector('.post-title a');
                                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                const descEl = card.querySelector('.post-excerpt');
                                const desc = descEl ? descEl.innerText.trim().replace('«', '').replace('»', '').trim() : "";
                                const likeEl = card.querySelector('.numbers-upvote');
                                const likes = likeEl ? likeEl.innerText.trim() : "0";
                                const visitBtn = card.querySelector('a.visit-site-button4');
                                const visitHref = visitBtn ? visitBtn.getAttribute('href') : "";
                                const detailHref = nameEl ? nameEl.getAttribute('href') : "";

                                if (visitHref || detailHref) {
                                    results.push({
                                        tool_name: name,
                                        description: desc,
                                        likes: likes,
                                        raw_visit_link: visitHref,
                                        internal_detail_url: detailHref
                                    });
                                }
                            } catch (e) {}
                        });
                        return results;
                    }""")

                    new_count = 0
                    for t in tools:
                        key = t['internal_detail_url']
                        if key not in global_tools:
                            global_tools[key] = {
                                "tool_name": t['tool_name'],
                                "description": t['description'],
                                "likes": t['likes'],
                                "internal_detail_url": t['internal_detail_url'],
                                "category_url": cat_url,
                                "external_link": t['raw_visit_link']
                            }
                            new_count += 1
                    
                    if new_count == 0: break
                    
                    # Check Next Button
                    if page.locator('a.next.page-numbers').count() == 0:
                        break
                    
                    current_page += 1
                    
                except Exception as e:
                    print(f"      ❌ Error: {e}")
                    break
            
            # Save progress
            save_csv(list(global_tools.values()))
        
        page.close()
        context.close()

        # --- PHASE 2: RESOLVE LINKS ---
        all_tools = list(global_tools.values())
        print(f"   ✨ Phase 1 Complete. Total Tools: {len(all_tools)}")
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
    harvest_aixploria()