import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys

# --- CONFIGURATION ---
OUTPUT_FILE = "aiagentslist_complete.csv"
MAX_PAGES_PER_CATEGORY = 50

CATEGORY_URLS = [
    "https://aiagentslist.com/categories/search-engine-optimization",
    "https://aiagentslist.com/categories/ai-agent-builders",
    "https://aiagentslist.com/categories/coding",
    "https://aiagentslist.com/categories/productivity",
    "https://aiagentslist.com/categories/personal-assistant",
    "https://aiagentslist.com/categories/finance",
    "https://aiagentslist.com/categories/general-purpose",
    "https://aiagentslist.com/categories/research",
    "https://aiagentslist.com/categories/data-analysis",
    "https://aiagentslist.com/categories/marketing",
    "https://aiagentslist.com/categories/content-creation",
    "https://aiagentslist.com/categories/digital-workers",
    "https://aiagentslist.com/categories/design",
    "https://aiagentslist.com/categories/sales",
    "https://aiagentslist.com/categories/customer-service",
    "https://aiagentslist.com/categories/voice-ai-agents",
    "https://aiagentslist.com/categories/business-intelligence",
    "https://aiagentslist.com/categories/other",
    "https://aiagentslist.com/categories/hr",
    "https://aiagentslist.com/categories/science"
]

def save_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "tags", "pricing", "internal_detail_url", "category_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def resolve_link(browser, item):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    context = browser.new_context()
    page = context.new_page()
    
    try:
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
        page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        
        # Find Visit Button
        try:
            btn = page.locator('a:has-text("Visit")').first
            if btn.count() > 0:
                item['external_link'] = btn.get_attribute('href')
        except:
            pass
    except:
        pass
    finally:
        page.close()
        context.close()
    
    return item

def harvest_aiagentslist():
    with sync_playwright() as p:
        print("--- 🚀 Starting AIAgentsList Crawler (Sync Mode) ---")
        
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context()
        page = context.new_page()

        global_tools = {}

        # PHASE 1
        for url in CATEGORY_URLS:
            cat_name = url.split('/')[-1]
            print(f"   👉 Category: {cat_name}")
            
            current_page = 1
            try:
                page.goto(url, timeout=60000, wait_until="domcontentloaded")
                
                while current_page <= MAX_PAGES_PER_CATEGORY:
                    # Wait for items
                    try:
                        page.wait_for_selector('a[href^="/agent/"]', timeout=5000)
                    except:
                        break

                    # Extract
                    tools = page.evaluate("""() => {
                        const results = [];
                        const links = document.querySelectorAll('a[href^="/agent/"]');
                        links.forEach(link => {
                            try {
                                const card = link.querySelector('div.rounded-lg');
                                if (!card) return;
                                
                                const href = link.getAttribute('href');
                                const nameEl = card.querySelector('[role="heading"]');
                                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                const descEl = card.querySelector('p.line-clamp-2');
                                const desc = descEl ? descEl.innerText.trim() : "";
                                
                                const badges = card.querySelectorAll('span.inline-flex');
                                let pricing = "";
                                let tags = [];
                                badges.forEach(b => {
                                    const txt = b.innerText.trim();
                                    if (txt.includes("Free") || txt.includes("Paid")) pricing = txt;
                                    else tags.push(txt);
                                });

                                results.push({
                                    tool_name: name,
                                    description: desc,
                                    pricing: pricing,
                                    tags: tags.join(', '),
                                    internal_detail_url: href
                                });
                            } catch (e) {}
                        });
                        return results;
                    }""")

                    new_count = 0
                    for t in tools:
                        full_url = f"https://aiagentslist.com{t['internal_detail_url']}"
                        if full_url not in global_tools:
                            global_tools[full_url] = {
                                "tool_name": t['tool_name'],
                                "description": t['description'],
                                "pricing": t['pricing'],
                                "tags": t['tags'],
                                "internal_detail_url": full_url,
                                "category_url": url,
                                "external_link": ""
                            }
                            new_count += 1
                    
                    if new_count > 0:
                        save_csv(list(global_tools.values()))
                        # print(f"      Pg {current_page}: +{new_count} new")

                    # Pagination
                    next_btn = page.locator('button[data-pagination-next=""]')
                    if next_btn.count() > 0 and not next_btn.is_disabled():
                        next_btn.click()
                        time.sleep(2)
                        current_page += 1
                    else:
                        break
            except Exception as e:
                print(f"      ❌ Error: {e}")
        
        all_tools = list(global_tools.values())
        print(f"   ✨ Phase 1 Complete. Total: {len(all_tools)}")

        # PHASE 2
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
    harvest_aiagentslist()