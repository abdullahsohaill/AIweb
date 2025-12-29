import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys

# --- CONFIGURATION ---
INPUT_FILE = "aitoolguru_complete.csv"
OUTPUT_FILE = "aitoolguru_fixed.csv"
MAX_CONCURRENT_TABS = 8

async def fix_link(context, row, semaphore):
    current_link = str(row.get('external_link', '')).strip()
    if current_link and current_link != "nan":
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    async with semaphore:
        page = await context.new_page()
        try:
            # Block media
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
            
            await page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
            
            # Find "Visit" button
            final_url = ""
            try:
                # Selector 1: Standard structure
                btn = page.locator("a.btn-primary:has(span.icon-earth)").first
                if await btn.count() > 0:
                    final_url = await btn.get_attribute('href')
                
                # Selector 2: Text match fallback
                if not final_url:
                    btn = page.locator("a.btn-primary:has-text('Visit')").first
                    if await btn.count() > 0:
                        final_url = await btn.get_attribute('href')

            except:
                pass
            
            if final_url:
                row['external_link'] = final_url

        except Exception:
            pass
        finally:
            await page.close()
    
    return row

async def main():
    print(f"--- 🔧 STARTING AITOOLGURU REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Identify missing
    rows_to_fix = [r for r in data if not str(r.get('external_link', '')).strip() or str(r.get('external_link', '')) == 'nan']
    rows_good = [r for r in data if str(r.get('external_link', '')).strip() and str(r.get('external_link', '')) != 'nan']
    
    if not rows_to_fix:
        print("🎉 No missing links found!")
        return

    print(f"   ⚠️ Found {len(rows_to_fix)} links to fix.")
    print(f"   🚀 Starting background repair ({MAX_CONCURRENT_TABS} concurrent)...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context()
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fix_link(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            fixed_results.append(res)
            
            if (i + 1) % 50 == 0:
                print(f"      Fixed {i+1}/{len(rows_to_fix)} tools...", end="\r")
        
        await browser.close()

    # Save
    print(f"\n--- 💾 Saving Fixed CSV ---")
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "pricing", "likes", "tags", "internal_detail_url"]
    # Ensure cols exist
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
        
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"🎉 SUCCESS! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())