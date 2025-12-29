import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
BASE_URL = "https://bai.tools"
INPUT_FILE = "baitools_harvest.csv"
OUTPUT_FILE = "baitools_harvest_fixed.csv"

# How many pages to check at once
MAX_CONCURRENT_TABS = 10

async def fetch_external_link(context, row, semaphore):
    # If link already exists, skip
    if pd.notna(row['external_link']) and str(row['external_link']).strip() != "":
        return row

    internal_slug = row.get('internal_slug')
    if not internal_slug:
        return row

    full_url = f"{BASE_URL}{internal_slug}"
    
    async with semaphore:
        page = await context.new_page()
        try:
            # Block images/media to make it lightning fast
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(full_url, timeout=30000, wait_until="domcontentloaded")
            
            # Selector based on your HTML snippet: class "to-view-btn"
            # <a class="... to-view-btn" href="...">Open site</a>
            try:
                btn = page.locator("a.to-view-btn").first
                if await btn.count() > 0:
                    link = await btn.get_attribute("href")
                    if link:
                        row['external_link'] = link
                        # print(f"   ✅ Fixed: {row['tool_name']} -> {link}")
            except:
                pass

        except Exception:
            pass
        finally:
            await page.close()
    
    return row

async def main():
    print(f"--- 🔧 STARTING REPAIR JOB: {INPUT_FILE} ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Error: Could not find {INPUT_FILE}")
        return

    # Identify missing links
    # We check for NaN or Empty strings
    missing_mask = df['external_link'].isna() | (df['external_link'] == "")
    missing_count = missing_mask.sum()
    
    if missing_count == 0:
        print("🎉 No missing links found! Your CSV is already perfect.")
        return

    print(f"   ⚠️ Found {missing_count} tools with missing links.")
    print(f"   🚀 Resolving them in background ({MAX_CONCURRENT_TABS} concurrent)...")

    # Convert DataFrame to list of dicts for processing
    data = df.to_dict('records')
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fetch_external_link(context, row, semaphore) for row in data]
        
        # Run with progress bar
        results = []
        total = len(tasks)
        
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            results.append(res)
            if (i + 1) % 50 == 0:
                print(f"      Processed {i+1}/{total} tools...", end="\r")
        
        await browser.close()

    # Save updated data
    print(f"\n--- 💾 Saving Fixed CSV ---")
    df_fixed = pd.DataFrame(results)
    
    # Restore original column order
    cols = ["tool_name", "external_link", "description", "categories", "internal_slug"]
    existing_cols = [c for c in cols if c in df_fixed.columns]
    df_fixed = df_fixed[existing_cols]
    
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"🎉 SUCCESS! Saved to {OUTPUT_FILE}")
    print(f"   Filled {missing_count - (df_fixed['external_link'].isna() | (df_fixed['external_link'] == '')).sum()} previously missing links.")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())