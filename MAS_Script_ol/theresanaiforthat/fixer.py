import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import time

# --- CONFIGURATION ---
INPUT_FILE = "taaft_complete.csv"
OUTPUT_FILE = "taaft_final_fixed.csv"
MAX_CONCURRENT_TABS = 6 # Visible tabs take memory, 6 is safe

async def fix_link(context, row, semaphore):
    # Skip valid
    current_link = str(row.get('external_link', '')).strip()
    if current_link and current_link != "nan":
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            # Visit internal page
            await page.goto(internal_url, timeout=40000, wait_until="domcontentloaded")
            
            # Find "Use tool" button (#ai_top_link)
            try:
                btn = page.locator('#ai_top_link')
                
                if await btn.count() > 0:
                    # Get href directly first (Faster)
                    raw_href = await btn.get_attribute('href')
                    
                    if raw_href and "theresanaiforthat.com" not in raw_href:
                        # It's already an external link!
                        final_url = raw_href
                    else:
                        # It might be a redirect or JS button. Click it.
                        async with context.expect_page(timeout=10000) as new_page_info:
                            await btn.click()
                        
                        new_page = await new_page_info.value
                        await new_page.wait_for_load_state("domcontentloaded")
                        final_url = new_page.url
                        await new_page.close()
            except:
                pass
            
            # Clean up
            if final_url:
                if "?ref=" in final_url:
                    final_url = final_url.split("?")[0]
                if "&ref=" in final_url:
                    final_url = final_url.split("&")[0]
                row['external_link'] = final_url

        except Exception:
            pass
        finally:
            await page.close()
    
    return row

async def main():
    print(f"--- 🔧 STARTING TAAFT REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    rows_to_fix = [r for r in data if pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "" or str(r.get('external_link')) == "nan"]
    rows_good = [r for r in data if str(r.get('external_link', '')).strip() and str(r.get('external_link', '')) != 'nan']
    
    print(f"   ⚠️ Found {len(rows_to_fix)} tools to repair.")

    async with async_playwright() as p:
        # Headless=False is mandatory for TAAFT
        browser = await p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fix_link(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            fixed_results.append(res)
            if (i + 1) % 20 == 0:
                print(f"      Processed {i+1}/{len(rows_to_fix)}...", end="\r")
        
        await browser.close()

    # Save
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "likes", "category", "year_source", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
    
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())