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
    cols = ["tool_name", "external_link", "description", "pricing", "tags", "internal_detail_url", "category_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def resolve_link(browser, item):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    # Skip if already valid or not a proper internal link
    if item.get('external_link'): return item
    if not internal_url.startswith("http"):
        internal_url = f"https://aiagentslist.com{internal_url}"

    context = browser.new_context()
    page = context.new_page()
    
    try:
        # Block media to speed up
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        
        final_url = ""
        
        # Find "Visit Website" Button
        try:
            # 1. Text Match
            btn = page.locator("a:has-text('Visit Website')").first
            if btn.count() > 0:
                final_url = btn.get_attribute("href")
            
            # 2. Fallback: Look for globe icon
            if not final_url:
                btn = page.locator("a:has(svg.lucide-globe)").first
                if btn.count() > 0:
                    final_url = btn.get_attribute("href")
        except:
            pass
        
        if final_url:
            if "?utm" in final_url: final_url = final_url.split("?")[0]
            item['external_link'] = final_url
            
    except:
        pass
    finally:
        page.close()
        context.close()

    return item

def harvest_aiagentslist():
    with sync_playwright() as p:
        print("--- 🚀 Starting AIAgentsList Crawler (Sync Mode) ---")
        
        # Headless=False helps ensure elements render properly
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context()
        page = context.new_page()

        global_tools = {}
        
        # --- PHASE 1 ---
        for url in CATEGORY_URLS:
            cat_name = url.split('/')[-1]
            print(f"   👉 Category: {cat_name}")
            
            current_page = 1
            try:
                page.goto(url, timeout=60000, wait_until="domcontentloaded")
                time.sleep(3) # Wait for list to render
                
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
                                const href = link.getAttribute('href');
                                
                                // NAME: h3 tag inside the link
                                const nameEl = link.querySelector('h3');
                                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                
                                // DESCRIPTION: p tag
                                const descEl = link.querySelector('p');
                                const desc = descEl ? descEl.innerText.trim() : "";
                                
                                // PRICING & TAGS: spans
                                const badges = link.querySelectorAll('span');
                                let pricing = "";
                                let tags = [];
                                badges.forEach(b => {
                                    const txt = b.innerText.trim();
                                    if (txt.includes("Free") || txt.includes("Paid")) {
                                        pricing = txt;
                                    } else if(txt && txt !== "Featured") {
                                        tags.push(txt);
                                    }
                                });

                                if (href) {
                                    results.push({
                                        tool_name: name,
                                        description: desc,
                                        pricing: pricing,
                                        tags: tags.join(', '),
                                        internal_detail_url: href
                                    });
                                }
                            } catch (e) {}
                        });
                        return results;
                    }""")

                    new_count = 0
                    for t in tools:
                        if t['internal_detail_url'] not in global_tools:
                            global_tools[t['internal_detail_url']] = t
                            t['external_link'] = "" # Placeholder
                            t['category_url'] = url
                            new_count += 1
                    
                    if new_count > 0:
                        save_csv(list(global_tools.values()))

                    # 3. Pagination (Next Arrow)
                    # Snippet: <button data-pagination-next="">
                    next_btn = page.locator('button[data-pagination-next=""]')
                    
                    if next_btn.count() > 0:
                        # Corrected: Removed await
                        if next_btn.is_disabled():
                             break
                        
                        next_btn.click()
                        time.sleep(3) # Give time for new items to load
                        current_page += 1
                    else:
                        break # No next button

            except Exception as e:
                print(f"      ❌ Error: {e}")
        
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
    harvest_aiagentslist()