import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import os

# --- CONFIGURATION ---
if os.path.exists("easywithai_repaired.csv"):
    INPUT_FILE = "easywithai_repaired.csv"
else:
    INPUT_FILE = "easywithai_complete.csv"

OUTPUT_FILE = "easywithai_repaired.csv"
MAX_CONCURRENT_TABS = 6

async def fix_link(context, row, semaphore):
    # --- 1. Identify Bad Links ---
    # Bad if: Empty, NaN, or points to an internal /tools/ page
    current_link = str(row.get('external_link', '')).strip()
    is_bad = (not current_link) or (current_link.lower() == "nan") or ("easywithai.com/tools/" in current_link)

    if not is_bad:
        return row # Keep good rows

    internal_url = row.get('internal_detail_url')
    if not internal_url:
        return None # Can't fix, delete

    async with semaphore:
        page = await context.new_page()
        try:
            # Block heavy assets for speed
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())
            
            # --- 2. Visit Internal Page ---
            try:
                await page.goto(internal_url, timeout=45000, wait_until="domcontentloaded")
            except:
                print(f"      ⚠️ Timeout loading {internal_url} -> Deleting")
                await page.close()
                return None

            # --- 3. Check for Cloudflare ---
            title = await page.title()
            if "Just a moment" in title or "Access denied" in title:
                print(f"      ❌ Cloudflare blocked {internal_url} -> Deleting")
                await page.close()
                return None

            # --- 4. Find the Button ---
            final_url = ""
            try:
                # Strategy A: The specific class used by EasyWithAI
                btn = page.locator("a.wp-block-button__link").first
                
                # Strategy B: Text Fallback
                if await btn.count() == 0:
                    btn = page.locator("a:has-text('Visit Site')").first

                if await btn.count() > 0:
                    raw_href = await btn.get_attribute('href')
                    
                    # --- 5. Resolve Redirects if needed ---
                    # If the link is relative or points to easywithai, we must click/navigate to resolve it
                    if raw_href and ("easywithai.com" in raw_href or raw_href.startswith("/")):
                        try:
                            # Navigate to the redirect link
                            await page.goto(raw_href, timeout=30000, wait_until="commit")
                            # Wait for it to leave easywithai
                            await page.wait_for_url(lambda u: "easywithai.com" not in u.href, timeout=15000)
                            final_url = page.url
                        except:
                            # If waiting fails, check if we landed somewhere new anyway
                            if "easywithai.com" not in page.url:
                                final_url = page.url
                            else:
                                final_url = "" # Failed to resolve
                    else:
                        # It's already external (e.g. https://openai.com)
                        final_url = raw_href

            except:
                pass
            
            # --- 6. Final Validation ---
            if final_url and "easywithai.com/tools/" not in final_url:
                # Clean params
                if "?ref=" in final_url: final_url = final_url.split("?")[0]
                if "&ref=" in final_url: final_url = final_url.split("&")[0]
                
                row['external_link'] = final_url
                print(f"      ✅ Fixed: {row.get('tool_name')} -> {final_url}")
                return row
            else:
                print(f"      ❌ No valid external link for {row.get('tool_name')} -> Deleting")
                return None

        except Exception as e:
            # print(f"      ❌ Error: {e}")
            return None
        finally:
            if not page.is_closed():
                await page.close()

async def main():
    print(f"--- 🔧 FINAL FIXER: EASYWITHAI (REDIRECT RESOLVER) ---")
    print(f"--- 📂 Input File: {INPUT_FILE} ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    data = df.to_dict('records')
    
    # Filter rows that need fixing
    rows_to_fix = [
        r for r in data 
        if not str(r.get('external_link', '')).strip() 
        or "easywithai.com/tools/" in str(r.get('external_link', ''))
    ]
    rows_good = [r for r in data if r not in rows_to_fix]
    
    print(f"   📊 Total Rows: {len(data)}")
    print(f"   ✅ Good Rows:  {len(rows_good)}")
    print(f"   ⚠️  To Fix:    {len(rows_to_fix)}")
    
    if not rows_to_fix:
        print("   🎉 Nothing to fix! Exiting.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False, # Visible to handle redirects/blocks better
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [fix_link(context, row, semaphore) for row in rows_to_fix]
        
        fixed_results = []
        for i, task in enumerate(asyncio.as_completed(tasks)):
            res = await task
            if res:
                fixed_results.append(res)
            
            if (i + 1) % 10 == 0:
                print(f"      Processed {i+1}/{len(tasks)} tasks...", end='\r')
        
        await browser.close()

    # Save Results
    final_data = rows_good + fixed_results
    if final_data:
        df_fixed = pd.DataFrame(final_data)
        # Ensure column order
        cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
        for c in cols:
            if c not in df_fixed.columns: df_fixed[c] = ""
        df_fixed = df_fixed[cols]
        
        df_fixed.to_csv(OUTPUT_FILE, index=False)
        print(f"\n🎉 DONE! Saved {len(df_fixed)} rows to {OUTPUT_FILE}")
    else:
        print(f"\n🎉 DONE! All processed rows were deleted. {OUTPUT_FILE} is now empty.")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())