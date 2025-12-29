import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
INPUT_FILE = "aitoolmall_complete.csv"   # The file with missing data
OUTPUT_FILE = "aitoolmall_repaired.csv"  # The fixed output
MAX_CONCURRENT_TABS = 8

async def fix_row(context, row, semaphore):
    # Check what is missing
    # We fix if Name is "Unknown" OR Link is missing
    missing_name = (row.get('tool_name') == "Unknown") or pd.isna(row.get('tool_name'))
    missing_link = pd.isna(row.get('external_link')) or str(row.get('external_link')).strip() == "" or str(row.get('external_link')) == "nan"

    if not missing_name and not missing_link:
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    async with semaphore:
        page = await context.new_page()
        
        try:
            # Visit page (Visible mode)
            # We block images to speed it up, but keep scripts/css for the button to render
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
            
            try:
                await page.goto(internal_url, timeout=45000, wait_until="domcontentloaded")
            except:
                pass 

            # 1. FIX NAME
            if missing_name:
                try:
                    # Specific selector from your HTML snippet
                    h1 = page.locator("h1.elementor-heading-title").first
                    if await h1.count() > 0:
                        row['tool_name'] = (await h1.inner_text()).strip()
                except:
                    pass

            # 2. FIX LINK
            if missing_link:
                final_url = ""
                try:
                    # Wait for the button wrapper to appear
                    try:
                        await page.wait_for_selector('.elementor-button-wrapper', timeout=4000)
                    except:
                        pass

                    # Strategy: Target the specific class 'elementor-button-link'
                    # Your HTML: <a class="elementor-button elementor-button-link ..." href="...">
                    btn = page.locator("a.elementor-button-link").first
                    
                    if await btn.count() > 0:
                        final_url = await btn.get_attribute("href")
                    else:
                        # Fallback: Look for text "Visit" inside any Elementor button
                        btn = page.locator("a.elementor-button:has-text('Visit')").first
                        if await btn.count() > 0:
                            final_url = await btn.get_attribute("href")
                except:
                    pass
                
                # Cleanup
                if final_url:
                    if "?ref=" in final_url:
                        final_url = final_url.split("?")[0]
                    row['external_link'] = final_url

            # 3. FIX DESCRIPTION (If missing)
            if pd.isna(row.get('description')) or str(row.get('description')).strip() == "":
                try:
                    # Try meta description
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
    print(f"--- 🔧 STARTING AITOOLMALL VISIBLE REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Filter rows that need fixing
    rows_to_fix = [r for r in data if (r.get('tool_name') == "Unknown") or (pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "" or str(r.get('external_link')) == "nan")]
    rows_good = [r for r in data if r not in rows_to_fix]
    
    print(f"   ⚠️ Found {len(rows_to_fix)} tools to repair.")
    print(f"   🚀 Launching {MAX_CONCURRENT_TABS} visible tabs...")

    async with async_playwright() as p:
        # HEADLESS = FALSE (Visible Browser)
        browser = await p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fix_row(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        total = len(tasks)
        
        # Run concurrently
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            fixed_results.append(res)
            
            if (i + 1) % 20 == 0:
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