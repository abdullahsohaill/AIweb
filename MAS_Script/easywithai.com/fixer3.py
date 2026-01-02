import pandas as pd
from playwright.sync_api import sync_playwright
import os
import time

# --- CONFIGURATION ---
# We always work on the repaired file to incrementally improve it
if os.path.exists("easywithai_repaired.csv"):
    INPUT_FILE = "easywithai_repaired.csv"
else:
    INPUT_FILE = "easywithai_complete.csv"

OUTPUT_FILE = "easywithai_repaired.csv"
SAVE_INTERVAL = 10  # Save progress every 10 items

def save_data(data_list):
    """Saves the current state of the data to the output file."""
    if not data_list:
        df = pd.DataFrame(columns=["tool_name", "external_link", "description", "category_url", "internal_detail_url"])
    else:
        df = pd.DataFrame(data_list)
    
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def fix_row(context, row):
    # --- Determine if a fix is needed ---
    # A link is bad if it's empty, NaN, or an internal /tools/ link
    link = str(row.get('external_link', ''))
    is_bad_link = not link or link.lower() == 'nan' or "easywithai.com/tools/" in link

    if not is_bad_link:
        return row # This row is already good

    crawl_url = row.get('internal_detail_url')
    if not crawl_url:
        return None # Can't fix without an internal URL, delete

    page = context.new_page()
    try:
        # Navigate to the page
        try:
            page.goto(crawl_url, timeout=45000, wait_until="domcontentloaded")
        except:
            print(f"      ⚠️ Timeout loading {crawl_url}. Deleting row.")
            page.close()
            return None

        # --- CLOUDFLARE CHECK ---
        title = page.title()
        if "Just a moment" in title or "Access denied" in title:
            print(f"      ❌ Cloudflare blocked {crawl_url}. You may need to solve CAPTCHA manually. Deleting for now.")
            page.close()
            return None

        # --- FIND EXTERNAL LINK ---
        final_url = ""
        try:
            # Strategy A: WordPress Block Button (Most reliable)
            btn = page.locator('a.wp-block-button__link').first
            if btn.count() > 0:
                final_url = btn.get_attribute('href')
            
            # Strategy B: Generic "Visit" text search
            if not final_url:
                btn = page.locator("a:has-text('Visit Site'), a:has-text('Visit Website')").first
                if btn.count() > 0:
                    final_url = btn.get_attribute('href')
        except:
            pass
        
        # If no link is found after trying, delete the row.
        if not final_url:
            print(f"      ❌ Link not found for {crawl_url} -> Deleting row.")
            return None
            
        # If we found a link, clean and assign it.
        if "?ref=" in final_url:
            final_url = final_url.split("?")[0]
        row['external_link'] = final_url
        print(f"      ✅ Fixed Link: {final_url}")
        
        return row

    except Exception as e:
        print(f"      ❌ Error on {crawl_url}: {e}. Deleting row.")
        return None
    finally:
        page.close()

def main():
    print(f"--- 🔧 STARTING EASYWITHAI FIXER (WITH DELETIONS) ---")
    print(f"--- 📂 Input File: {INPUT_FILE} ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    data = df.to_dict('records')
    
    # Separate rows into 'good' and 'to-fix'
    rows_to_fix = []
    rows_good = []
    for r in data:
        link = str(r.get('external_link', ''))
        is_bad = not link or link.lower() == 'nan' or "easywithai.com/tools/" in link
        if is_bad:
            rows_to_fix.append(r)
        else:
            rows_good.append(r)
    
    print(f"   📊 Total Rows: {len(data)}")
    print(f"   ✅ Good Rows:  {len(rows_good)}")
    print(f"   ⚠️  To Fix:    {len(rows_to_fix)}")
    
    if not rows_to_fix:
        print("   🎉 Nothing to fix! Exiting.")
        return

    # Start Playwright in visible mode
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        fixed_results = []
        for i, row in enumerate(rows_to_fix):
            print(f"\n   👉 [{i+1}/{len(rows_to_fix)}] Processing: {row.get('internal_detail_url')}")
            
            updated_row = fix_row(context, row)
            if updated_row:
                fixed_results.append(updated_row)
            
            # Save progress incrementally
            if (i + 1) % SAVE_INTERVAL == 0:
                save_data(rows_good + fixed_results)
                print(f"      💾 Progress saved. ({i+1} rows processed)")
        
        browser.close()

    # Final Save
    final_data = rows_good + fixed_results
    save_data(final_data)
    print(f"\n🎉 DONE! All rows processed. Final data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()