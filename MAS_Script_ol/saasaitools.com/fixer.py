import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
INPUT_FILE = "saasaitools_fixed.csv" # Input file (we will overwrite it or create new)
OUTPUT_FILE = "saasaitools_final_fixed.csv"
MAX_CONCURRENT_TABS = 6

async def fix_link(context, row, semaphore):
    # Skip if valid
    current_link = str(row.get('external_link', '')).strip()
    if current_link and current_link != "nan":
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block images to speed up, but allow scripts so button renders
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=45000, wait_until="domcontentloaded")
            
            # 1. Wait for the button to actually render (give it up to 5s)
            # We look for the specific class 'brxe-button' OR text 'Check out'
            try:
                # This selector targets the button class found in your snippet
                btn_locator = page.locator(".brxe-button:has-text('Check out')")
                
                # Wait for it to appear
                await btn_locator.first.wait_for(state="attached", timeout=5000)
                
                if await btn_locator.count() > 0:
                    # Get href
                    raw_href = await btn_locator.first.get_attribute("href")
                    
                    # 2. Logic: Direct Link vs Tracking Link
                    if raw_href:
                        if "saasaitools.com/go" in raw_href:
                            # It's a tracking link -> Must visit to resolve
                            try:
                                await page.goto(raw_href, timeout=30000, wait_until="commit")
                                # Wait for redirect
                                await page.wait_for_url(lambda u: "saasaitools.com" not in u.href, timeout=10000)
                                final_url = page.url
                            except:
                                # If redirect hangs, check current URL
                                if "saasaitools.com/go" not in page.url:
                                    final_url = page.url
                                else:
                                    final_url = raw_href # Fail-safe
                        else:
                            # It's a direct link (e.g. dognames.top) -> Just use it
                            final_url = raw_href

            except:
                pass # Button never appeared

            # Cleanup tracking params
            if final_url and "?" in final_url and "saasaitools" not in final_url:
                final_url = final_url.split("?")[0]

        except Exception:
            pass
        finally:
            await page.close()
    
    if final_url:
        row['external_link'] = final_url
        
    return row

async def main():
    print(f"--- 🔧 STARTING FINAL REPAIR JOB ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Identify missing
    missing_count = sum(1 for r in data if not str(r.get('external_link', '')).strip() or str(r.get('external_link', '')) == 'nan')
    print(f"   ⚠️ Processing {len(data)} rows ({missing_count} missing links).")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        # Process ALL rows to be safe (or filter for missing only if you prefer)
        # Filtering is faster:
        rows_to_fix = [r for r in data if not str(r.get('external_link', '')).strip() or str(r.get('external_link', '')) == 'nan']
        rows_good = [r for r in data if str(r.get('external_link', '')).strip() and str(r.get('external_link', '')) != 'nan']
        
        if not rows_to_fix:
            print("   🎉 No missing links to fix!")
            return

        tasks = [fix_link(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            fixed_results.append(res)
            if (i + 1) % 10 == 0:
                print(f"      Fixed {i+1}/{len(rows_to_fix)}...", end="\r")
        
        await browser.close()
        
        # Combine
        final_data = rows_good + fixed_results

    # Save
    df_fixed = pd.DataFrame(final_data)
    # Restore columns
    cols = ["tool_name", "external_link", "description", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
    
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())