import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import os

# --- CONFIGURATION ---
if os.path.exists("aitoolnet_final_fixed.csv"):
    INPUT_FILE = "aitoolnet_final_fixed.csv"
else:
    INPUT_FILE = "aitoolnet_complete.csv"

OUTPUT_FILE = "aitoolnet_final_fixed.csv"
MAX_CONCURRENT_TABS = 8

async def fix_link(context, row, semaphore):
    # Determine if a fix is needed
    current_link = str(row.get('external_link', '')).strip()
    is_bad = not current_link or current_link.lower() == "nan" or "aitoolnet.com" in current_link

    if not is_bad:
        return row

    internal_url = str(row.get('internal_detail_url', ''))
    if internal_url.count('https://') > 1:
        internal_url = "https://" + internal_url.split('https://')[-1]
    if not internal_url:
        return None # Can't fix, delete

    async with semaphore:
        page = await context.new_page()
        try:
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())
            
            try:
                await page.goto(internal_url, timeout=60000, wait_until="domcontentloaded")
            except Exception:
                print(f"      ⚠️ Timeout loading {internal_url} -> Deleting")
                await page.close()
                return None
            
            final_url = ""
            try:
                # --- STRATEGY 1: Exact Text Match ---
                btn = page.locator("a:has-text('Visit website')").first
                if await btn.count() > 0:
                    final_url = await btn.get_attribute('href')

                # --- STRATEGY 2: Class Match ---
                if not final_url:
                    btn = page.locator("a.button.is-success").first
                    if await btn.count() > 0:
                        final_url = await btn.get_attribute('href')

                # --- STRATEGY 3: Brute Force ---
                if not final_url:
                    all_links = await page.locator("a[href]").all()
                    for link in all_links:
                        href = await link.get_attribute("href")
                        if href and href.startswith("http"):
                            if any(x in href for x in ["facebook.com", "twitter.com", "linkedin.com", "discord", "google.com"]):
                                continue
                            final_url = href
                            break 
            except:
                pass
            
            if final_url:
                # 1. Clean the URL first
                if "?ref=" in final_url:
                    final_url = final_url.split("?")[0]
                if "&ref=" in final_url:
                    final_url = final_url.split("&")[0]
                
                # 2. Check if it's internal
                if "aitoolnet.com" not in final_url:
                    row['external_link'] = final_url
                    print(f"      ✅ Fixed: {row.get('tool_name')} -> {final_url}")
                    return row
                else:
                    # --- CHANGE: Delete if the found link is internal ---
                    print(f"      ❌ Found link was internal: {final_url} -> Deleting")
                    return None
            else:
                print(f"      ❌ No external link found for {row.get('tool_name')} -> Deleting")
                return None

        except Exception as e:
            if "Target page, context or browser has been closed" not in str(e):
                print(f"      ❌ Critical Error for {row.get('tool_name')}: {e} -> Deleting")
            return None
        finally:
            if not page.is_closed():
                await page.close()

async def main():
    print(f"--- 🔧 FINAL FIXER: AITOOLNET.COM (DELETE INTERNAL LINKS) ---")
    print(f"--- 📂 Input File: {INPUT_FILE} ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    data = df.to_dict('records')
    
    rows_to_fix = [r for r in data if not str(r.get('external_link', '')).strip() or "aitoolnet.com" in str(r.get('external_link', ''))]
    rows_good = [r for r in data if r not in rows_to_fix]
    
    print(f"   📊 Total Rows: {len(data)}")
    print(f"   ✅ Good Rows:  {len(rows_good)}")
    print(f"   ⚠️  To Fix:    {len(rows_to_fix)}")
    
    if not rows_to_fix:
        print("   🎉 Nothing to fix! Exiting.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fix_link(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            if res: # Only keep if not None
                fixed_results.append(res)
            
            if (i + 1) % 20 == 0:
                print(f"      Progress: {i+1}/{len(rows_to_fix)}", end='\r')
        
        await browser.close()

    final_data = rows_good + fixed_results
    if final_data:
        df_fixed = pd.DataFrame(final_data)
        
        cols = ["tool_name", "external_link", "description", "likes", "category_url", "internal_detail_url"]
        for c in cols:
            if c not in df_fixed.columns: df_fixed[c] = ""
        df_fixed = df_fixed[cols]
        
        df_fixed.to_csv(OUTPUT_FILE, index=False)
        print(f"\n🎉 DONE! Saved {len(df_fixed)} rows to {OUTPUT_FILE}")
    else:
        print(f"\n🎉 DONE! All processed rows were deleted. {OUTPUT_FILE} is now empty.")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())