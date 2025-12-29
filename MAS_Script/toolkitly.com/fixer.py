import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys

# --- CONFIGURATION ---
INPUT_FILE = "toolkitly_complete.csv"
OUTPUT_FILE = "toolkitly_fixed.csv"

def resolve_link(browser, row):
    """
    Visits the internal page to find the external link.
    """
    # Skip if already valid
    current_link = str(row.get('external_link', '')).strip()
    if current_link and current_link != "nan":
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    context = browser.new_context()
    page = context.new_page()
    final_url = ""
    
    try:
        # Block media
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        try:
            page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        except:
            pass 

        # Find "Try [Tool]" button
        try:
            # Selector: a.custom-btn
            btn = page.locator("a.custom-btn").first
            if btn.count() > 0:
                final_url = btn.get_attribute('href')
        except:
            pass

    except Exception:
        pass
    finally:
        page.close()
        context.close()
    
    if final_url:
        row['external_link'] = final_url
        
    return row

def fix_toolkitly():
    print(f"--- 🔧 STARTING TOOLKITLY REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Identify missing
    missing_count = sum(1 for r in data if not str(r.get('external_link', '')).strip() or str(r.get('external_link', '')) == 'nan')
    print(f"   ⚠️ Found {missing_count} missing links.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        
        # Filter for rows needing fix
        rows_to_fix = [r for r in data if not str(r.get('external_link', '')).strip() or str(r.get('external_link', '')) == 'nan']
        rows_good = [r for r in data if str(r.get('external_link', '')).strip() and str(r.get('external_link', '')) != 'nan']
        
        fixed_results = []
        count = 0
        
        for row in rows_to_fix:
            fixed_row = resolve_link(browser, row)
            fixed_results.append(fixed_row)
            count += 1
            
            if count % 10 == 0:
                print(f"      Fixed {count}/{len(rows_to_fix)}...", end="\r")
        
        browser.close()
        
        # Combine
        final_data = rows_good + fixed_results

    # Save
    df_fixed = pd.DataFrame(final_data)
    cols = ["tool_name", "external_link", "description", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
        
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    fix_toolkitly()