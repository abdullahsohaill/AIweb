import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import time

# --- CONFIGURATION ---
INPUT_FILE = "toolai_fixed.csv" 
OUTPUT_FILE = "toolai_final_links.csv"
BASE_URL = "https://toolai.io"

# Max tabs to open at once (High speed)
MAX_CONCURRENT_TABS = 15
TIMEOUT_MS = 30000

async def fix_link(context, row, semaphore):
    # Skip if link is already valid
    current_link = str(row.get('external_link', '')).strip()
    if current_link and current_link != "nan":
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block media/css/font for speed
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())
            
            # Visit internal page
            await page.goto(internal_url, timeout=TIMEOUT_MS, wait_until="domcontentloaded")
            
            # --- STRATEGY: FIND VISIT BUTTON ---
            raw_href = ""
            try:
                # Selector 1: Standard ToolAI button (btn-main)
                btn = page.locator("a.btn-main:has-text('Visit')").first
                if await btn.count() > 0:
                    raw_href = await btn.get_attribute("href")
                
                # Selector 2: Alternative button style (btn-primary)
                if not raw_href:
                    btn = page.locator("a.btn-primary:has-text('Visit')").first
                    if await btn.count() > 0:
                        raw_href = await btn.get_attribute("href")
                
                # Selector 3: Fallback text match
                if not raw_href:
                    btn = page.locator("a:has-text('Visit Site')").first
                    if await btn.count() > 0:
                        raw_href = await btn.get_attribute("href")

                # --- RESOLVE REDIRECT ---
                if raw_href:
                    # If it's a redirect link (/link/...), we must follow it
                    if raw_href.startswith("/link/") or "toolai.io/link" in raw_href:
                        full_redirect = f"{BASE_URL}{raw_href}" if raw_href.startswith("/") else raw_href
                        
                        try:
                            # Navigate to the redirect link
                            await page.goto(full_redirect, timeout=TIMEOUT_MS, wait_until="commit")
                            
                            # Wait loop: Wait until URL leaves toolai.io
                            start_time = time.time()
                            while time.time() - start_time < 10: # 10s timeout for redirect
                                if "toolai.io" not in page.url and page.url != "about:blank":
                                    final_url = page.url
                                    break
                                await asyncio.sleep(0.5)
                            
                            # If still stuck, take whatever current URL is (might have failed)
                            if not final_url: final_url = page.url
                        except:
                            final_url = full_redirect # Save raw redirect if nav fails
                    else:
                        # Direct link
                        final_url = raw_href
            except:
                pass

        except Exception:
            pass
        finally:
            await page.close()
    
    # Clean & Save
    if final_url:
        if "?utm" in final_url: final_url = final_url.split("?")[0]
        if "?ref" in final_url: final_url = final_url.split("?")[0]
        row['external_link'] = final_url
        
    return row

async def main():
    print(f"--- ⚡ STARTING LINK-ONLY REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Identify bad links
    rows_to_fix = [r for r in data if pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "" or str(r.get('external_link')) == "nan"]
    rows_good = [r for r in data if r not in rows_to_fix]
    
    print(f"   ⚠️ Found {len(rows_to_fix)} links to find.")
    print(f"   🚀 Launching {MAX_CONCURRENT_TABS} concurrent threads...")

    async with async_playwright() as p:
        # Headless=True with stealth args is faster
        browser = await p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fix_link(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        total = len(tasks)
        
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            fixed_results.append(res)
            
            if (i + 1) % 20 == 0:
                print(f"      Processed {i+1}/{total}...", end="\r")
        
        await browser.close()

    # Save
    print(f"\n--- 💾 Saving Final CSV ---")
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
        
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())