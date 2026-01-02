import pandas as pd
from playwright.sync_api import sync_playwright
import os
import time

# --- CONFIGURATION ---
INPUT_FILE = "aitoolsdirectory_complete.csv"
OUTPUT_FILE = "aitoolsdirectory_complete.csv" # Overwrite in-place

def resolve_redirect(context, row):
    # --- Determine if a fix is needed ---
    # A fix is needed if the URL is empty, NaN, or contains 'aitoolsdirectory.com'
    url = str(row.get('real_website_url', ''))
    tracking_url_present = str(row.get('tracking_url', ''))
    
    needs_fix = not url or url.lower() == 'nan' or "aitoolsdirectory.com" in url

    if not needs_fix:
        return row # Already a good, external link

    # The URL we need to visit is in the 'tracking_url' column from the crawler
    crawl_url = row.get('tracking_url')
    if not crawl_url:
        print(f"      ⚠️ No tracking URL for {row.get('tool_name')}. Deleting row.")
        return None # Can't fix it without a URL to visit

    page = context.new_page()
    try:
        # Block heavy resources for speed
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())

        # Start navigation
        try:
            page.goto(crawl_url, timeout=20000, wait_until="commit")
        except Exception:
            print(f"      ⚠️ Initial navigation failed for {crawl_url}. Deleting row.")
            page.close()
            return None
        
        # --- WAIT FOR THE REDIRECT TO COMPLETE ---
        # We wait until the URL in the address bar is no longer the original domain
        try:
            page.wait_for_url(lambda url: "aitoolsdirectory.com" not in url, timeout=15000)
            final_url = page.url
            
            # Clean tracking parameters
            if "?" in final_url:
                final_url = final_url.split("?")[0]
            
            row['real_website_url'] = final_url
            print(f"      ✅ Fixed Link: {final_url}")
            return row
            
        except Exception:
            # If the wait times out, the redirect failed.
            print(f"      ❌ Redirect timed out for {crawl_url}. Deleting row.")
            return None

    except Exception as e:
        print(f"      ❌ Critical error on {crawl_url}: {e}. Deleting row.")
        return None
    finally:
        page.close()

def main():
    print(f"--- 🔧 STARTING AITOOLSDIRECTORY FIXER (WITH DELETIONS) ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    data = df.to_dict('records')
    
    rows_to_fix = []
    rows_good = []

    for r in data:
        url = str(r.get('real_website_url', ''))
        is_bad = not url or url.lower() == 'nan' or "aitoolsdirectory.com" in url
        if is_bad:
            rows_to_fix.append(r)
        else:
            rows_good.append(r)
    
    print(f"   📊 Total Rows: {len(data)}")
    print(f"   ✅ Good Rows:  {len(rows_good)}")
    print(f"   ⚠️  To Fix:    {len(rows_to_fix)}")

    if not rows_to_fix:
        print("   🎉 Nothing to fix!")
        return

    with sync_playwright() as p:
        # VISIBLE BROWSER
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context()
        
        fixed_results = []
        for i, row in enumerate(rows_to_fix):
            print(f"\n   👉 [{i+1}/{len(rows_to_fix)}] Resolving: {row.get('tracking_url')}")
            
            updated_row = resolve_redirect(context, row)
            if updated_row:
                fixed_results.append(updated_row)
        
        browser.close()

    # Combine the original 'good' rows with the newly 'fixed' rows
    final_data = rows_good + fixed_results
    
    # Save the cleaned data back to the same file
    if final_data:
        final_df = pd.DataFrame(final_data)
        final_df.to_csv(OUTPUT_FILE, index=False)
        print(f"\n🎉 DONE! Saved {len(final_df)} rows back to {OUTPUT_FILE}")
    else:
        # Handle case where all rows were deleted
        open(OUTPUT_FILE, 'w').close()
        print(f"\n🎉 DONE! All processed rows were deleted. {OUTPUT_FILE} is now empty.")


if __name__ == "__main__":
    main()