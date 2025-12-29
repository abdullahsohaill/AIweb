import pandas as pd
from playwright.sync_api import sync_playwright
import sys
import time

# --- CONFIGURATION ---
INPUT_FILE = "aitoolhouse_complete.csv"
OUTPUT_FILE = "aitoolhouse_fixed.csv"
MAX_CONCURRENT_TABS = 8

def fix_row(browser, row):
    # We need to fix if Name is Unknown OR Link is missing/empty
    needs_fix = (row.get('tool_name') == "Unknown") or (pd.isna(row.get('external_link')) or str(row.get('external_link')).strip() == "")
    
    if not needs_fix:
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    context = browser.new_context()
    page = context.new_page()
    
    try:
        # Block media
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        try:
            page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        except:
            pass

        # 1. Fix Name (H1)
        # Selector: h1.MuiTypography-h3 (from your snippet) or just H1
        if row.get('tool_name') == "Unknown":
            try:
                h1 = page.locator('h1').first
                if h1.count() > 0:
                    row['tool_name'] = h1.inner_text().strip()
            except:
                pass

        # 2. Fix Description
        # Selector: "What is [Tool]?" section or generic paragraph
        try:
            # Try meta description first (fastest)
            meta_desc = page.locator('meta[name="description"]').get_attribute("content")
            if meta_desc:
                row['description'] = meta_desc
            else:
                # Fallback to first paragraph under H1
                desc_p = page.locator('h1 + p, h1 + div p').first
                if desc_p.count() > 0:
                    row['description'] = desc_p.inner_text().strip()
        except:
            pass

        # 3. Fix External Link
        # Selector: a containing "Visit"
        if pd.isna(row.get('external_link')) or str(row.get('external_link')).strip() == "":
            external_link = ""
            try:
                # Robust text search
                btn = page.locator('a:has-text("Visit Site"), a:has-text("Visit Website")').first
                if btn.count() > 0:
                    external_link = btn.get_attribute('href')
                
                # Cleanup
                if external_link:
                    if "?utm" in external_link:
                        external_link = external_link.split("?")[0]
                    row['external_link'] = external_link
            except:
                pass

    except Exception:
        pass
    finally:
        page.close()
        context.close()
    
    return row

def main():
    print(f"--- 🔧 STARTING AITOOLHOUSE REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Identify rows needing repair
    rows_to_fix = [r for r in data if (r.get('tool_name') == "Unknown") or (pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "")]
    rows_good = [r for r in data if (r.get('tool_name') != "Unknown") and (pd.notna(r.get('external_link')) and str(r.get('external_link')).strip() != "")]
    
    print(f"   ⚠️ Found {len(rows_to_fix)} tools needing data repair.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        fixed_results = []
        for i, row in enumerate(rows_to_fix):
            fixed_row = fix_row(browser, row)
            fixed_results.append(fixed_row)
            
            if (i + 1) % 20 == 0:
                print(f"      Fixed {i+1}/{len(rows_to_fix)} tools...", end="\r")
        
        browser.close()

    # Save
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
        
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()