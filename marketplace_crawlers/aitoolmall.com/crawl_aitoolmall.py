import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://aitoolmall.com"
OUTPUT_FILE = "aitoolmall_complete.csv"
MAX_PAGES = 15  # 15 pages total

def save_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    
    # Ensure columns exist
    cols = ["tool_name", "external_link", "description", "pricing", "developer", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def resolve_link(context, item):
    """
    Visits the internal page to find the external link.
    """
    # Skip if we already found it (e.g. from the list view sometimes)
    if item.get('external_link'): return item

    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    page = context.new_page()
    final_url = ""
    
    try:
        # Block media to speed up
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        try:
            page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        except:
            pass 

        # Find "Visit [Tool]" button
        try:
            # Selector: a.elementor-button containing "Visit"
            btn = page.locator("a.elementor-button:has-text('Visit')").first
            if btn.count() > 0:
                final_url = btn.get_attribute('href')
            else:
                # Fallback: Any link in content with target blank?
                # Sometimes it's just an icon link
                pass
        except:
            pass

    except Exception:
        pass
    finally:
        page.close()
    
    if final_url:
        item['external_link'] = final_url
    return item

def harvest_aitoolmall():
    with sync_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting AIToolMall (Scroll-Stop-Scrape) ---")
        
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context()
        page = context.new_page()

        unique_tools_map = {}
        
        for page_num in range(1, MAX_PAGES + 1):
            current_url = f"{BASE_URL}/?_page={page_num}"
            print(f"   📄 Scraping Page {page_num}: {current_url}")
            
            try:
                page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
                
                # --- SCROLL & SCRAPE LOOP ---
                # We scroll down in small chunks, scraping at every stop
                last_height = 0
                no_change_count = 0
                
                while True:
                    # 1. SCRAPE VISIBLE ITEMS
                    tools = page.evaluate("""() => {
                        const results = [];
                        const cards = document.querySelectorAll('article.wpgb-card');
                        
                        cards.forEach(card => {
                            try {
                                // Name (.wpgb-block-7)
                                const nameEl = card.querySelector('.wpgb-block-7');
                                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                
                                // Description (.wpgb-block-3)
                                const descEl = card.querySelector('.wpgb-block-3');
                                const desc = descEl ? descEl.innerText.trim() : "";
                                
                                // Price (.wpgb-block-2)
                                const priceEl = card.querySelector('.wpgb-block-2');
                                const price = priceEl ? priceEl.innerText.replace('Price:', '').trim() : "";

                                // Developer (.wpgb-block-6)
                                const devEl = card.querySelector('.wpgb-block-6');
                                const dev = devEl ? devEl.innerText.replace('Developers:', '').trim() : "";

                                // Internal Link
                                const linkEl = card.querySelector('a.wpgb-card-layer-link');
                                const href = linkEl ? linkEl.getAttribute('href') : "";

                                if (href) {
                                    results.push({
                                        tool_name: name,
                                        description: desc,
                                        pricing: price,
                                        developer: dev,
                                        internal_detail_url: href
                                    });
                                }
                            } catch (e) {}
                        });
                        return results;
                    }""")
                    
                    # 2. MERGE INTO MAP
                    for t in tools:
                        key = t['internal_detail_url']
                        # Only update if we have better info (e.g. name isn't "Unknown")
                        if key not in unique_tools_map:
                            unique_tools_map[key] = t
                        else:
                            # If existing entry has missing name/desc, update it
                            if unique_tools_map[key]['tool_name'] == "Unknown" and t['tool_name'] != "Unknown":
                                unique_tools_map[key] = t

                    # 3. SCROLL DOWN
                    page.evaluate("window.scrollBy(0, 600)") # Scroll 600px
                    time.sleep(1.0) # Wait for render
                    
                    # Check if bottom reached
                    new_height = page.evaluate("window.scrollY + window.innerHeight")
                    doc_height = page.evaluate("document.body.scrollHeight")
                    
                    if new_height >= doc_height:
                        no_change_count += 1
                        if no_change_count >= 3: # Confirm bottom
                            break
                    else:
                        no_change_count = 0
                
                print(f"      ✅ Page {page_num} Done. Total Unique: {len(unique_tools_map)}")
                save_csv(list(unique_tools_map.values()))

            except Exception as e:
                print(f"      ❌ Error on page {page_num}: {e}")
        
        page.close()
        
        all_tools = list(unique_tools_map.values())
        print(f"   ✨ Phase 1 Complete. Total: {len(all_tools)}")

        # --- PHASE 2 ---
        if all_tools:
            print(f"\n--- 🚀 PHASE 2: Resolving Links (Sequential) ---")
            count = 0
            for item in all_tools:
                resolve_link(context, item)
                count += 1
                if count % 10 == 0:
                    print(f"      Processed {count}/{len(all_tools)} tools...", end="\r")
                    save_csv(all_tools)
            
            save_csv(all_tools)
            print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")
        
        context.close()
        browser.close()

if __name__ == "__main__":
    harvest_aitoolmall()