import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from tqdm import tqdm
import math

# --- CONFIGURATION ---
INPUT_CSV = "aitoptools_complete.csv"  # The file you currently have
OUTPUT_CSV = "aitoptools_fixed.csv" # The file we will save to
CONCURRENT_TABS = 5                 # How many tabs to open at once

async def get_external_link(context, row):
    """
    Visits the detail page and tries multiple selectors to find the external link.
    """
    url = row['internal_detail_url']
    
    # If we already have a link, skip
    if pd.notna(row['external_link']) and str(row['external_link']).strip() != "":
        return row

    page = await context.new_page()
    try:
        await page.goto(url, timeout=60000, wait_until="domcontentloaded")
        # Small wait to ensure buttons render
        await asyncio.sleep(1)

        external_link = None

        # --- STRATEGY 1: Look for "Visit Website" text match (Most likely) ---
        try:
            # This looks for any link that contains "Visit" text
            visit_btn = page.locator("a:has-text('Visit Website'), a:has-text('Visit Site')").first
            if await visit_btn.count() > 0:
                external_link = await visit_btn.get_attribute("href")
        except: pass

        # --- STRATEGY 2: Look for generic "Official Website" button classes ---
        if not external_link:
            try:
                # Common class for main buttons
                btn = page.locator("a.btn-primary").first 
                if await btn.count() > 0:
                    external_link = await btn.get_attribute("href")
            except: pass

        # --- STRATEGY 3: Look for the first external link in the sidebar/header ---
        if not external_link:
            try:
                # Get all links and filter in Python (Robust fallback)
                links = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('a')).map(a => a.href);
                }''')
                
                for link in links:
                    # Filter out internal links, social media, and garbage
                    if "aitoptools.com" not in link and "twitter" not in link and "facebook" not in link and link.startswith("http"):
                        external_link = link
                        break
            except: pass

        if external_link:
            row['external_link'] = external_link
            # print(f"   ✅ Found link for {row['tool_name']}: {external_link}")
        else:
            # print(f"   ❌ Could not find link for {row['tool_name']}")
            row['external_link'] = "Not Found"

    except Exception as e:
        # print(f"   ⚠️ Error on {url}: {e}")
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

    # 2. Identify rows that need fixing (empty external_link)
    # We treat NaN, None, and empty strings as needing fixing
    df['external_link'] = df['external_link'].fillna("")
    
    # Create a list of rows to process (only the empty ones)
    rows_to_process = df[df['external_link'] == ""].to_dict('records')
    completed_rows = df[df['external_link'] != ""].to_dict('records')
    
    print(f"--- Found {len(rows_to_process)} rows missing external links. Starting fix... ---")

    # 3. Launch Browser
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        # Process in chunks
        chunk_size = CONCURRENT_TABS
        pbar = tqdm(total=len(rows_to_process))

        for i in range(0, len(rows_to_process), chunk_size):
            chunk = rows_to_process[i:i + chunk_size]
            tasks = [get_external_link(context, row) for row in chunk]
            results = await asyncio.gather(*tasks)
            
            completed_rows.extend(results)
            pbar.update(len(chunk))
            
            # Intermediate save every 50 rows
            if i % 50 == 0:
                temp_df = pd.DataFrame(completed_rows)
                temp_df.to_csv(OUTPUT_CSV, index=False)

        await browser.close()
        pbar.close()

    # 4. Final Save
    final_df = pd.DataFrame(completed_rows)
    final_df.to_csv(OUTPUT_CSV, index=False)
    print(f"\n🎉 Fix Complete. Saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())