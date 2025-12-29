import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import os

# --- CONFIGURATION ---
if os.path.exists("aitoptools_fixed.csv"):
    INPUT_CSV = "aitoptools_fixed.csv"
else:
    INPUT_CSV = "aitoptools_complete.csv"

OUTPUT_CSV = "aitoptools_fixed.csv"
CONCURRENT_TABS = 5

async def get_details(context, row, semaphore):
    # Determine if a fix is needed
    needs_link_fix = pd.isna(row.get('external_link')) or str(row.get('external_link', '')).strip() in ["", "Not Found"]
    needs_name_fix = str(row.get('tool_name', '')).strip() in ["", "Unknown"]

    # If the row is perfect, don't waste time crawling it
    if not needs_link_fix and not needs_name_fix:
        return row
    
    internal_url = row.get('internal_detail_url')
    if not internal_url:
        return row # Can't fix without internal URL

    async with semaphore:
        page = await context.new_page()
        try:
            # Block heavy resources
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=60000, wait_until="domcontentloaded")
            
            # --- FIX 1: EXTERNAL LINK ---
            if needs_link_fix:
                external_link = ""
                # Strategy A: Text match "Visit Site" or "Visit Website"
                try:
                    visit_btn = page.locator("a:has-text('Visit Site'), a:has-text('Visit Website')").first
                    if await visit_btn.count() > 0:
                        external_link = await visit_btn.get_attribute("href")
                except: pass

                # Strategy B: Dynamic Link class (from site's structure)
                if not external_link:
                    try:
                        btn = page.locator(".jet-listing-dynamic-link__link").first
                        if await btn.count() > 0:
                            external_link = await btn.get_attribute("href")
                    except: pass
                
                # Assign if found
                if external_link:
                    # Clean the link
                    if "?" in external_link:
                        external_link = external_link.split("?")[0]
                    row['external_link'] = external_link
                    print(f"      ✅ Fixed Link: {external_link}")
                else:
                    print(f"      ❌ Link not found for {row.get('tool_name')}")

            # --- FIX 2: TOOL NAME ---
            if needs_name_fix:
                try:
                    # The main title is usually in an H1
                    h1 = page.locator("h1").first
                    if await h1.count() > 0:
                        name = (await h1.inner_text()).replace('verified', '').strip()
                        row['tool_name'] = name
                        print(f"      ✅ Fixed Name: {name}")
                except: pass

        except Exception as e:
            print(f"      ⚠️ Error on {internal_url}: {e}")
            pass
        finally:
            await page.close()

    return row

async def main():
    # 1. Load Data
    try:
        df = pd.read_csv(INPUT_CSV)
        print(f"--- Loaded {len(df)} rows from {INPUT_CSV} ---")
    except FileNotFoundError:
        print(f"Error: Could not find {INPUT_CSV}")
        return

    # 2. Identify rows that need fixing
    df['external_link'] = df['external_link'].fillna("")
    df['tool_name'] = df['tool_name'].fillna("")

    rows_to_fix = []
    rows_good = []

    for index, row in df.iterrows():
        link_is_bad = row['external_link'].strip() in ["", "Not Found"]
        name_is_bad = row['tool_name'].strip() in ["", "Unknown"]
        if link_is_bad or name_is_bad:
            rows_to_fix.append(row.to_dict())
        else:
            rows_good.append(row.to_dict())
            
    print(f"   📊 Total Rows: {len(df)}")
    print(f"   ✅ Good Rows:  {len(rows_good)}")
    print(f"   ⚠️  To Fix:    {len(rows_to_fix)}")

    if not rows_to_fix:
        print("   🎉 Nothing to fix! Exiting.")
        return

    # 3. Launch Browser and Process
    async with async_playwright() as p:
        # VISIBLE BROWSER
        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        semaphore = asyncio.Semaphore(CONCURRENT_TABS)
        
        tasks = [get_details(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        # Use tqdm for a nice progress bar
        for task in asyncio.as_completed(tasks):
            result = await task
            fixed_results.append(result)
            print(f"      Processed {len(fixed_results)}/{len(rows_to_fix)}...", end="\r")

        await browser.close()

    # 4. Final Save
    final_data = rows_good + fixed_results
    final_df = pd.DataFrame(final_data)
    
    # Ensure all columns exist and are in order
    cols = ["tool_name", "external_link", "short_description", "pricing", "category", "internal_detail_url"]
    for c in cols:
        if c not in final_df.columns: final_df[c] = ""
    final_df = final_df[cols]

    final_df.to_csv(OUTPUT_CSV, index=False)
    print(f"\n🎉 Fix Complete. Saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())