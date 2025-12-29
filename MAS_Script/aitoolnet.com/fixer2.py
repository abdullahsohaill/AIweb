import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import os

# --- CONFIGURATION ---
# Prioritize the fixed file if it exists, otherwise fallback to complete
if os.path.exists("aitoolnet_final_fixed.csv"):
    INPUT_FILE = "aitoolnet_final_fixed.csv"
else:
    INPUT_FILE = "aitoolnet_complete.csv"

OUTPUT_FILE = "aitoolnet_final_fixed.csv"
MAX_CONCURRENT_TABS = 6

async def fix_link(context, row, semaphore):
    current_link = str(row.get('external_link', '')).strip()
    
    # Identify if this row needs fixing
    # A link is BAD if:
    # 1. It is NaN or empty
    # 2. It starts with "/" (Internal slug captured by mistake, e.g. /editpro-ai)
    needs_fix = (
        pd.isna(row.get('external_link')) or 
        current_link == "" or 
        current_link.lower() == "nan" or 
        current_link.startswith("/") 
    )

    # If it's good, return it as is
    if not needs_fix:
        return row

    internal_url = row.get('internal_detail_url')
    # If no internal URL to fix from, delete the row
    if not internal_url or str(internal_url) == 'nan':
        return None

    async with semaphore:
        page = await context.new_page()
        final_url = ""
        try:
            # Block media/css/font for speed
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())
            
            try:
                await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            except:
                print(f"      ⚠️ Timeout loading {internal_url} -> Deleting")
                await page.close()
                return None
            
            # --- FIND VISIT BUTTON ---
            try:
                # Wait briefly for button
                try:
                    await page.wait_for_selector("a.button.is-success", timeout=3000)
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
                # Clean referral params
                if "?ref=" in final_url:
                    final_url = final_url.split("?")[0]
                
                row['external_link'] = final_url
                # Optional: Update tool name if it was missing/unknown
                if row.get('tool_name') == "Unknown":
                    try:
                        name_el = page.locator("h1").first
                        if await name_el.count() > 0:
                            row['tool_name'] = await name_el.inner_text()
                    except: pass
                
                print(f"      ✅ Fixed: {final_url}")
                return row
            else:
                print(f"      ❌ No link found for {internal_url} -> Deleting")
                return None

        except Exception as e:
            return None
        finally:
            await page.close()

async def main():
    print(f"--- 🔧 STARTING AITOOLNET REPAIR ---")
    print(f"--- 📂 Input File: {INPUT_FILE} ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    data = df.to_dict('records')
    
    # Identify rows to fix
    rows_to_fix = []
    rows_good = []
    
    for r in data:
        link = str(r.get('external_link', '')).strip()
        is_bad = pd.isna(r.get('external_link')) or link == "" or link.lower() == "nan" or link.startswith("/")
        
        if is_bad:
            rows_to_fix.append(r)
        else:
            rows_good.append(r)
    
    print(f"   ⚠️ Found {len(rows_to_fix)} tools with missing/internal links.")
    print(f"   🚀 Starting background repair ({MAX_CONCURRENT_TABS} concurrent)...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False, # Visible Mode is safer/better for finding buttons
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fix_link(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        total = len(tasks)
        
        # Process asynchronously
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            if res: # Only append if not None (deleted)
                fixed_results.append(res)
            
            if (i + 1) % 20 == 0:
                print(f"      Processed {i+1}/{total} tools...", end="\r")
        
        await browser.close()

    # Save
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "likes", "category_url", "internal_detail_url"]
    # Ensure columns exist
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
    
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 DONE! Saved {len(df_fixed)} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())