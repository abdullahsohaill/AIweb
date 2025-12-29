import pandas as pd
import time
from urllib.parse import urlparse, urlunparse
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# --- CONFIGURATION ---
OUTPUT_FILE = "futurepedia_complete.csv"

# Complete list of categories
CATEGORY_URLS = [
    "https://www.futurepedia.io/ai-tools/personal-assistant",
    "https://www.futurepedia.io/ai-tools/research-assistant",
    "https://www.futurepedia.io/ai-tools/spreadsheet-assistant",
    "https://www.futurepedia.io/ai-tools/translators",
    "https://www.futurepedia.io/ai-tools/presentations",
    "https://www.futurepedia.io/ai-tools/productivity",
    "https://www.futurepedia.io/ai-tools/video-enhancer",
    "https://www.futurepedia.io/ai-tools/video-editing",
    "https://www.futurepedia.io/ai-tools/video-generators",
    "https://www.futurepedia.io/ai-tools/text-to-video",
    "https://www.futurepedia.io/ai-tools/video",
    "https://www.futurepedia.io/ai-tools/prompt-generators",
    "https://www.futurepedia.io/ai-tools/writing-generators",
    "https://www.futurepedia.io/ai-tools/paraphrasing",
    "https://www.futurepedia.io/ai-tools/storyteller",
    "https://www.futurepedia.io/ai-tools/copywriting-assistant",
    "https://www.futurepedia.io/ai-tools/text-generators",
    "https://www.futurepedia.io/ai-tools/website-builders",
    "https://www.futurepedia.io/ai-tools/marketing",
    "https://www.futurepedia.io/ai-tools/finance",
    "https://www.futurepedia.io/ai-tools/project-management",
    "https://www.futurepedia.io/ai-tools/social-media",
    "https://www.futurepedia.io/ai-tools/business",
    "https://www.futurepedia.io/ai-tools/design-generators",
    "https://www.futurepedia.io/ai-tools/image-generators",
    "https://www.futurepedia.io/ai-tools/image-editing",
    "https://www.futurepedia.io/ai-tools/text-to-image",
    "https://www.futurepedia.io/ai-tools/image",
    "https://www.futurepedia.io/ai-tools/workflows",
    "https://www.futurepedia.io/ai-tools/ai-agents",
    "https://www.futurepedia.io/ai-tools/automations",
    "https://www.futurepedia.io/ai-tools/cartoon-generators",
    "https://www.futurepedia.io/ai-tools/portrait-generators",
    "https://www.futurepedia.io/ai-tools/avatar-generator",
    "https://www.futurepedia.io/ai-tools/logo-generator",
    "https://www.futurepedia.io/ai-tools/3D-generator",
    "https://www.futurepedia.io/ai-tools/art",
    "https://www.futurepedia.io/ai-tools/audio-editing",
    "https://www.futurepedia.io/ai-tools/text-to-speech",
    "https://www.futurepedia.io/ai-tools/music-generator",
    "https://www.futurepedia.io/ai-tools/transcriber",
    "https://www.futurepedia.io/ai-tools/audio-generators",
    "https://www.futurepedia.io/ai-tools/fitness",
    "https://www.futurepedia.io/ai-tools/religion",
    "https://www.futurepedia.io/ai-tools/students",
    "https://www.futurepedia.io/ai-tools/fashion-assistant",
    "https://www.futurepedia.io/ai-tools/gift-ideas",
    "https://www.futurepedia.io/ai-tools/misc-tools",
    "https://www.futurepedia.io/ai-tools/code-assistant",
    "https://www.futurepedia.io/ai-tools/no-code",
    "https://www.futurepedia.io/ai-tools/sql-assistant",
    "https://www.futurepedia.io/ai-tools/code"
]

def clean_url(url):
    """Removes UTM parameters to keep links clean."""
    if not url: return ""
    try:
        parsed = urlparse(url)
        clean = urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))
        return clean
    except:
        return url

def save_csv(data):
    """Saves data incrementally."""
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "description", "pricing", "external_link", "category_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def check_block(page):
    """Checks for Cloudflare or Access Denied titles."""
    try:
        title = page.title()
        if "Just a moment" in title or "Access denied" in title or "Cloudflare" in title:
            return True
        return False
    except:
        return True

def run_crawler():
    print("--- 🚀 Starting Futurepedia Crawler (Robust Sync Mode) ---")
    
    with sync_playwright() as p:
        # VISIBLE BROWSER to reduce blocks
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        global_tools = []
        seen_ids = set() # To prevent duplicates

        for index, cat_url in enumerate(CATEGORY_URLS):
            cat_name = cat_url.split('/')[-1]
            print(f"\n👉 [{index+1}/{len(CATEGORY_URLS)}] Processing: {cat_name}")
            
            page = context.new_page()
            
            try:
                # 1. GO TO BASE URL (Category Home)
                print(f"      🔗 Visiting Base URL: {cat_url}")
                try:
                    page.goto(cat_url, timeout=45000, wait_until="domcontentloaded")
                except Exception as e:
                    print(f"      ❌ Network Error loading base URL. Skipping category.")
                    page.close()
                    continue

                # 2. CHECK BLOCK
                if check_block(page):
                    print("      🛑 Cloudflare Blocked. Skipping category.")
                    page.close()
                    continue

                page_num = 1
                
                # --- PAGINATION LOOP ---
                while True:
                    # Scroll to trigger lazy loads
                    try:
                        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        time.sleep(2)
                    except:
                        pass # Ignore scroll errors

                    # Extract Data
                    page_tools = page.evaluate("""() => {
                        const results = [];
                        const cards = document.querySelectorAll('div.bg-card');
                        
                        cards.forEach(card => {
                            try {
                                const nameEl = card.querySelector('p.text-xl');
                                const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                
                                const descEl = card.querySelector('p.text-muted-foreground');
                                const desc = descEl ? descEl.innerText.trim() : "";
                                
                                const pricingEl = card.querySelector('div.flex.justify-between > span');
                                const pricing = pricingEl ? pricingEl.innerText.trim() : "";

                                // Find 'Visit' button link
                                let extLink = "";
                                const visitBtn = card.querySelector('button');
                                if (visitBtn) {
                                    // Check parent 'a' tag
                                    const parentA = visitBtn.closest('a');
                                    if (parentA) extLink = parentA.getAttribute('href');
                                }
                                // Fallback: Direct link not internal
                                if (!extLink) {
                                    const directLink = card.querySelector('a[href^="http"]:not([href*="futurepedia.io/tool/"])');
                                    if (directLink) extLink = directLink.getAttribute('href');
                                }
                                
                                if (name !== "Unknown") {
                                    results.push({
                                        tool_name: name,
                                        description: desc,
                                        pricing: pricing,
                                        external_link: extLink
                                    });
                                }
                            } catch (e) {}
                        });
                        return results;
                    }""")

                    # Process Results
                    new_count = 0
                    for t in page_tools:
                        raw_link = t['external_link']
                        
                        # Filter bad links
                        if raw_link and "futurepedia.io/tool/" not in raw_link:
                            t['external_link'] = clean_url(raw_link)
                        else:
                            t['external_link'] = "" # Mark empty if internal only

                        # Dedup
                        uid = t['tool_name'] + cat_name
                        if uid not in seen_ids:
                            t['category_url'] = cat_url
                            global_tools.append(t)
                            seen_ids.add(uid)
                            new_count += 1

                    print(f"      Pg {page_num}: Found {len(page_tools)} tools (+{new_count} new). Total: {len(global_tools)}")
                    save_csv(global_tools)

                    # --- NEXT BUTTON HANDLING ---
                    try:
                        # Look for 'Next' button
                        next_btn = page.locator('a[title="Next"]').first
                        
                        if next_btn.count() == 0:
                            print("      ✅ No 'Next' button found. Category finished.")
                            break
                        
                        # Check if disabled
                        classes = next_btn.get_attribute("class") or ""
                        if "opacity-50" in classes or "pointer-events-none" in classes:
                            print("      ✅ 'Next' button is disabled. Category finished.")
                            break
                        
                        # Click Next
                        next_btn.click()
                        
                        # Wait for URL to change or content to load
                        try:
                            page.wait_for_load_state("domcontentloaded", timeout=10000)
                            time.sleep(2)
                            page_num += 1
                        except:
                            print("      ⚠️ Timeout waiting for next page. Stopping category.")
                            break
                            
                    except Exception as e:
                        print(f"      ⚠️ Pagination error: {e}. Stopping category.")
                        break

            except Exception as e:
                print(f"      ❌ Critical Error on {cat_url}: {e}")
            
            finally:
                page.close()
                time.sleep(1) # Cooldown between categories

    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run_crawler()