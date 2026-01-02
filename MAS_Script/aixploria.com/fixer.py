import pandas as pd
from playwright.sync_api import sync_playwright
import os
import time

# --- CONFIGURATION ---
INPUT_FILE = "aixploria_complete.csv"
OUTPUT_FILE = "aixploria_complete.csv" # Overwrite the file in-place

def fix_link_and_name(context, row):
    # --- Check if the row needs fixing ---
    link = str(row.get('external_link', ''))
    name = str(row.get('tool_name', ''))

    # A row needs fixing if the link is an internal redirect OR the name is missing.
    needs_fix = "/out/" in link or name in ["", "Unknown"]

    if not needs_fix:
        return row # This row is already good.

    # Determine which URL to visit for crawling
    # Prioritize the internal redirect link if it exists.
    crawl_url = ""
    if "/out/" in link:
        crawl_url = link
    elif row.get('internal_detail_url'):
        crawl_url = row.get('internal_detail_url')
    
    # If there's no URL to visit, we can't fix it. Delete the row.
    if not crawl_url:
        return None

    # Ensure the URL is absolute
    if not crawl_url.startswith("http"):
        crawl_url = f"https://www.aixploria.com{crawl_url}"
    
    page = context.new_page()
    try:
        # Block heavy resources for speed
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())

        # Navigate. Use 'commit' to catch the start of a redirect.
        try:
            page.goto(crawl_url, timeout=20000, wait_until="commit")
        except Exception:
            # If the initial navigation fails, it's a dead link.
            print(f"      ⚠️ Initial navigation failed for {crawl_url}. Deleting row.")
            page.close()
            return None
        
        # --- WAIT FOR REDIRECT ---
        # Wait until the URL no longer contains 'aixploria.com'
        try:
            page.wait_for_url(lambda url: "aixploria.com" not in url, timeout=15000)
            final_url = page.url
            
            # Clean tracking parameters
            if "?" in final_url:
                final_url = final_url.split("?")[0]
            
            row['external_link'] = final_url
            print(f"      ✅ Fixed Link: {final_url}")
            
        except Exception:
            # If it times out, it means the redirect failed. The link is bad.
            print(f"      ❌ Redirect timed out for {crawl_url}. Deleting row.")
            page.close()
            return None

        # --- FIX NAME (if it was missing) ---
        if name in ["", "Unknown"]:
            try:
                # The final page title is often a good source for the name
                page_title = page.title()
                if page_title:
                    # Simple cleaning (e.g., "ToolName | The Best AI Tool")
                    row['tool_name'] = page_title.split("|")[0].split("-")[0].strip()
                    print(f"      ✅ Fixed Name: {row['tool_name']}")
            except:
                pass # Name couldn't be fixed, but we keep the row for the link.

        return row

    except Exception as e:
        print(f"      ❌ Critical error on {crawl_url}: {e}. Deleting row.")
        return None
    finally:
        page.close()

def main():
    print(f"--- 🔧 STARTING AIXPLORIA FIXER (WITH DELETIONS) ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    data = df.to_dict('records')
    
    rows_to_fix = []
    rows_good = []

    for r in data:
        link = str(r.get('external_link', ''))
        if "/out/" in link or str(r.get('tool_name', '')) in ["", "Unknown"]:
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
            print(f"\n   👉 [{i+1}/{len(rows_to_fix)}] Processing: {row.get('tool_name')}")
            
            # The function now returns None for rows that should be deleted
            updated_row = fix_link_and_name(context, row)
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