import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
INPUT_FILE = "aitoolmall_final_fixed.csv" 
OUTPUT_FILE = "aitoolmall_repaired.csv"
MAX_CONCURRENT_TABS = 8

async def fix_row(context, row, semaphore):
    # Check what is missing
    missing_link = pd.isna(row.get('external_link')) or str(row.get('external_link')).strip() == "" or str(row.get('external_link')) == "nan"
    missing_name = row.get('tool_name') == "Unknown" or pd.isna(row.get('tool_name'))
    missing_desc = pd.isna(row.get('description')) or str(row.get('description')).strip() == ""

    # If nothing needed, return immediately
    if not missing_link and not missing_name:
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    # Limit concurrency with semaphore
    async with semaphore:
        page = await context.new_page()
        
        try:
            # Visit page (Visible mode)
            try:
                await page.goto(internal_url, timeout=45000, wait_until="domcontentloaded")
            except:
                pass 

            # 1. FIX NAME
            if missing_name:
                try:
                    h1 = page.locator("h1.elementor-heading-title").first
                    if await h1.count() > 0:
                        row['tool_name'] = (await h1.inner_text()).strip()
                except:
                    pass

            # 2. FIX LINK
            if missing_link:
                final_url = ""
                try:
                    # Wait for button
                    try:
                        await page.wait_for_selector('.elementor-button', state="attached", timeout=4000)
                    except:
                        pass

                    # Strategy: Find any elementor button that links out
                    # We look for common action words
                    btn = page.locator("a.elementor-button:has-text('Visit'), a.elementor-button:has-text('Try'), a.elementor-button:has-text('Open'), a.elementor-button:has-text('Get')").first
                    
                    if await btn.count() > 0:
                        final_url = await btn.get_attribute("href")
                    else:
                        # Fallback: Any elementor button that points to external site
                        # (Not pointing to aitoolmall)
                        buttons = await page.locator("a.elementor-button").all()
                        for b in buttons:
                            href = await b.get_attribute("href")
                            if href and "aitoolmall.com" not in href and href.startswith("http"):
                                final_url = href
                                break
                except:
                    pass
                
                if final_url:
                    if "?ref=" in final_url:
                        final_url = final_url.split("?")[0]
                    row['external_link'] = final_url

            # 3. FIX DESCRIPTION
            if missing_desc:
                try:
                    # Try meta desc
                    desc = await page.locator('meta[name="description"]').get_attribute("content")
                    if desc:
                        row['description'] = desc
                except:
                    pass

        except Exception:
            pass
        finally:
            await page.close()
    
    return row

async def main():
    print(f"--- 🔧 STARTING CONCURRENT REPAIR (8 Threads) ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    rows_to_fix = [r for r in data if (r.get('tool_name') == "Unknown") or (pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "" or str(r.get('external_link')) == "nan")]
    rows_good = [r for r in data if r not in rows_to_fix]
    
    print(f"   ⚠️ Found {len(rows_to_fix)} tools to repair.")

    async with async_playwright() as p:
        # Headless = False is key here for AIToolMall
        browser = await p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        # Create Tasks
        tasks = [fix_row(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        total = len(tasks)
        
        # Run concurrently
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            fixed_results.append(res)
            
            if (i + 1) % 10 == 0:
                print(f"      Processed {i+1}/{total}...", end="\r")
        
        await browser.close()

    # Save
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "pricing", "developer", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
        
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    # Windows Fix
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())