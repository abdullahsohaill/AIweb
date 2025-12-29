import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
INPUT_FILE = "aitoolnet_complete.csv"
OUTPUT_FILE = "aitoolnet_final_fixed.csv"
MAX_CONCURRENT_TABS = 6

async def fix_link(context, row, semaphore):
    current_link = str(row.get('external_link', '')).strip()
    
    # Identify if this row needs fixing
    needs_fix = (
        pd.isna(row.get('external_link')) or 
        current_link == "" or 
        current_link == "nan" or 
        current_link.startswith("/")  # <--- KEY FIX
    )

    if not needs_fix:
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Visit" button
            try:
                # Wait for button
                try:
                    await page.wait_for_selector("a.button.is-success", timeout=4000)
                except:
                    pass

                # Strategy 1: The specific green 'Visit website' button
                btn = page.locator("a.button.is-success").first
                if await btn.count() > 0:
                    final_url = await btn.get_attribute('href')
                
                # Strategy 2: Any button with 'Visit' text
                if not final_url:
                    btn = page.locator("a:has-text('Visit website')").first
                    if await btn.count() > 0:
                        final_url = await btn.get_attribute('href')

            except:
                pass
            
            if final_url:
                if "?ref=" in final_url:
                    final_url = final_url.split("?")[0]
                row['external_link'] = final_url
                # print(f"   ✅ Fixed: {row['tool_name']} -> {final_url}")

        except Exception:
            pass
        finally:
            await page.close()
    
    return row

async def main():
    print(f"--- 🔧 STARTING AITOOLNET REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Identify rows to fix (Empty or Internal Paths)
    rows_to_fix = []
    rows_good = []
    
    for r in data:
        link = str(r.get('external_link', '')).strip()
        is_bad = pd.isna(r.get('external_link')) or link == "" or link == "nan" or link.startswith("/")
        
        if is_bad:
            rows_to_fix.append(r)
        else:
            rows_good.append(r)
    
    print(f"   ⚠️ Found {len(rows_to_fix)} tools with missing/internal links.")
    print(f"   🚀 Starting background repair ({MAX_CONCURRENT_TABS} concurrent)...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False, # Visible Mode is safer
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
                print(f"      Processed {i+1}/{total} tools...", end="\r")
        
        await browser.close()

    # Save
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "likes", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
    
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())