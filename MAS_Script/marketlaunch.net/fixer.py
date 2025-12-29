import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys

# --- CONFIGURATION ---
INPUT_FILE = "microlaunch_repaired.csv" 
OUTPUT_FILE = "microlaunch_slow_fix.csv"

def fix_link(browser, row):
    # Check if repair is needed
    if pd.notna(row.get('external_link')) and str(row.get('external_link')).strip() != "" and str(row.get('external_link')) != "nan":
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    context = browser.new_context()
    page = context.new_page()
    final_url = ""
    
    try:
        # Go to page
        try:
            page.goto(internal_url, timeout=60000, wait_until="domcontentloaded")
            time.sleep(5) # Hard wait for slow loading
        except:
            pass

        # Debug: Print all links on page
        # links = page.evaluate("Array.from(document.querySelectorAll('a')).map(a => a.href)")
        # print(f"   🔍 Scanning {internal_url}...")

        # Strategy 1: The indigo button class
        try:
            btn = page.locator(".bg-indigo-500").first
            # Click parent anchor if it's a span
            if btn.count() > 0:
                parent = btn.locator("..")
                final_url = parent.get_attribute("href")
        except:
            pass
        
        # Strategy 2: Text "Visit Website"
        if not final_url:
            try:
                btn = page.locator("a:has-text('Visit Website')").first
                if btn.count() > 0:
                    final_url = btn.get_attribute("href")
            except:
                pass
            
        # Strategy 3: Any Ref link
        if not final_url:
            try:
                btn = page.locator("a[href*='ref=microlaunch']").first
                if btn.count() > 0:
                    final_url = btn.get_attribute("href")
            except:
                pass

    except Exception as e:
        print(f"Error: {e}")
    finally:
        page.close()
        context.close()
    
    # Cleanup
    if final_url:
        if "?ref=" in final_url: final_url = final_url.split("?")[0]
        row['external_link'] = final_url
        print(f"   ✅ Fixed: {row['tool_name']} -> {final_url}")
        
    return row

def main():
    print(f"--- 🐢 STARTING SLOW REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    rows_to_fix = [r for r in data if pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "" or str(r.get('external_link')) == "nan"]
    rows_good = [r for r in data if r not in rows_to_fix]
    
    print(f"   ⚠️ Fixing {len(rows_to_fix)} links...")

    with sync_playwright() as p:
        # Visible browser
        browser = p.chromium.launch(headless=False)
        
        fixed_results = []
        for i, row in enumerate(rows_to_fix):
            res = fix_link(browser, row)
            fixed_results.append(res)
            
            if (i + 1) % 5 == 0:
                print(f"      Processed {i+1}/{len(rows_to_fix)}...", end="\r")
        
        browser.close()

    # Save
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "categories", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
        
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()