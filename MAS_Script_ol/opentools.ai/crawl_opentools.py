import pandas as pd
import time
from playwright.sync_api import sync_playwright
import httpx
import concurrent.futures
import sys

# --- CONFIGURATION ---
START_URL = "https://openfuture.ai/"
OUTPUT_FILE = "openfuture_complete.csv"

# Limits
MAX_PAGES = 5000        # High limit for 40k tools
MAX_SHOW_MORE = 100     # Max times to click "Show More" per page
RESOLVE_THREADS = 20    # How many links to resolve at once (Speed!)

def save_csv(data):
    """Saves data immediately to disk."""
    if not data: return
    df = pd.DataFrame(data)
    
    cols = ["tool_name", "final_website_url", "description", "categories", "pricing", "internal_go_link", "source_page"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def resolve_redirect(go_url):
    """
    Follows the /go/ link using HTTP requests (Fast) to get the real URL.
    """
    if not go_url: return ""
    full_go_url = f"https://openfuture.ai{go_url}" if go_url.startswith("/") else go_url
    
    try:
        # We use a real user agent so the server doesn't block the HTTP request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        with httpx.Client(follow_redirects=True, headers=headers, timeout=10.0) as client:
            response = client.get(full_go_url)
            final = str(response.url)
            # Clean UTM params
            if "?" in final:
                final = final.split("?")[0]
            return final
    except:
        return full_go_url # Return original if resolution fails

def harvest_openfuture():
    with sync_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting OpenFuture.ai ---")
        
        # Launch Browser
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        current_url = START_URL
        unique_tools_map = {}
        page_num = 1
        
        while page_num <= MAX_PAGES:
            print(f"   📄 Scraping Page {page_num}: {current_url}")
            
            try:
                page.goto(current_url, timeout=60000, wait_until="domcontentloaded")
                
                # --- INNER LOOP: CLICK SHOW MORE ---
                show_more_count = 0
                while show_more_count < MAX_SHOW_MORE:
                    try:
                        # Check for "Show More" button
                        # Selector based on your snippet: button#button_load_more_tool
                        show_more_btn = page.locator("#button_load_more_tool")
                        
                        if show_more_btn.is_visible():
                            # Scroll to it
                            show_more_btn.scroll_into_view_if_needed()
                            time.sleep(0.5)
                            
                            # Get current count to verify load
                            prev_count = page.locator("div.tools-item").count()
                            
                            # Click
                            show_more_btn.click()
                            # print(f"      ⬇️  Clicked 'Show More' ({show_more_count+1})")
                            
                            # Wait for items to increase
                            try:
                                page.wait_for_function(f"document.querySelectorAll('div.tools-item').length > {prev_count}", timeout=5000)
                            except:
                                # If count didn't increase, maybe we reached end of this page section
                                print("      ⚠️ 'Show More' clicked but no new items. Moving on.")
                                break
                            
                            show_more_count += 1
                            time.sleep(1)
                        else:
                            # Button gone, inner loop done
                            break
                    except:
                        break

                # --- EXTRACT DATA ---
                print("      📥 Extracting tools from DOM...")
                raw_tools = page.evaluate("""() => {
                    const results = [];
                    const cards = document.querySelectorAll('div.tools-item');
                    
                    cards.forEach(card => {
                        try {
                            // Name
                            const nameEl = card.querySelector('.tool-title');
                            const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                            
                            // Description
                            const descEl = card.querySelector('p.card-text');
                            const desc = descEl ? descEl.innerText.trim() : "";
                            
                            // Category
                            const catEl = card.querySelector('.cate-tag a');
                            const category = catEl ? catEl.innerText.trim() : "";
                            
                            // Pricing
                            const priceEl = card.querySelector('.pricing-card-tag');
                            const pricing = priceEl ? priceEl.innerText.trim() : "";
                            
                            // Visit Link (/go/...)
                            const visitEl = card.querySelector('a.visit-button');
                            const goLink = visitEl ? visitEl.getAttribute('href') : "";

                            results.push({
                                tool_name: name,
                                description: desc,
                                categories: category,
                                pricing: pricing,
                                internal_go_link: goLink
                            });
                        } catch (e) {}
                    });
                    return results;
                }""")

                # --- PROCESS & RESOLVE LINKS (THREADED) ---
                new_items_batch = []
                
                # Identify tools we haven't processed yet
                unresolved_tools = []
                for t in raw_tools:
                    # Use go_link + name as unique key
                    key = f"{t['internal_go_link']}_{t['tool_name']}"
                    if key not in unique_tools_map:
                        t['key'] = key
                        t['source_page'] = page_num
                        unresolved_tools.append(t)
                
                if unresolved_tools:
                    print(f"      ⚡ Resolving {len(unresolved_tools)} links with {RESOLVE_THREADS} threads...")
                    
                    # Use ThreadPool to resolve HTTP redirects in parallel
                    with concurrent.futures.ThreadPoolExecutor(max_workers=RESOLVE_THREADS) as executor:
                        # Map tool to future
                        future_to_tool = {executor.submit(resolve_redirect, t['internal_go_link']): t for t in unresolved_tools}
                        
                        for future in concurrent.futures.as_completed(future_to_tool):
                            tool = future_to_tool[future]
                            try:
                                real_url = future.result()
                                tool['final_website_url'] = real_url
                            except:
                                tool['final_website_url'] = tool['internal_go_link']
                            
                            # Add to master map
                            unique_tools_map[tool['key']] = tool
                            new_items_batch.append(tool)
                
                print(f"   ✅ Page {page_num}: Added {len(new_items_batch)} new tools. Total Unique: {len(unique_tools_map)}")
                save_csv(list(unique_tools_map.values()))

                # --- PAGINATION ---
                # Look for the Next arrow
                # Selector based on your snippet: a.next with href
                try:
                    next_btn = page.locator("a.next[href]").first
                    if next_btn.count() > 0:
                        next_url = next_btn.get_attribute("href")
                        if next_url:
                            current_url = next_url
                            page_num += 1
                            time.sleep(2)
                        else:
                            print("      🛑 End of list (No href on next button).")
                            break
                    else:
                        print("      🛑 End of list (No next button found).")
                        break
                except:
                    print("      🛑 Error finding next button.")
                    break

            except Exception as e:
                print(f"      ❌ Error on page {page_num}: {e}")
                # Try to recover by going to next page manually if possible
                page_num += 1
                current_url = f"{START_URL}page/{page_num}"
        
        browser.close()
        print(f"\n🎉 CRAWL FINISHED. Total Tools: {len(unique_tools_map)}")

if __name__ == "__main__":
    harvest_openfuture()