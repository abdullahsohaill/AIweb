import pandas as pd
from playwright.sync_api import sync_playwright
import sys
import time

# --- CONFIGURATION ---
INPUT_FILE = "easywithai_complete.csv"
OUTPUT_FILE = "easywithai_repaired.csv"

def fix_row(context, row):
    # Identify what needs fixing
    missing_name = pd.isna(row.get('tool_name')) or str(row.get('tool_name')).strip() == "" or row.get('tool_name') == "Unknown"
    missing_link = pd.isna(row.get('external_link')) or str(row.get('external_link')).strip() == ""
    
    if not missing_name and not missing_link:
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    page = context.new_page()
    
    try:
        # Visit (Visible mode is safer for Cloudflare sites)
        try:
            page.goto(internal_url, timeout=60000, wait_until="domcontentloaded")
        except:
            pass 

        # Check for block
        title = page.title()
        if "Just a moment" in title:
            print("\n🚨 CLOUDFLARE BLOCK! Please solve CAPTCHA manually in the window.")
            input("Press Enter after page loads...")

        # 1. FIX NAME
        if missing_name:
            try:
                # Usually H1 is the title
                h1 = page.locator('h1.elementor-heading-title').first
                if h1.count() == 0:
                    h1 = page.locator('h1').first
                
                if h1.count() > 0:
                    row['tool_name'] = h1.inner_text().strip()
            except:
                pass

        # 2. FIX LINK
        if missing_link:
            final_url = ""
            try:
                # Wait for button
                try:
                    page.wait_for_selector('a.wp-block-button__link', timeout=4000)
                except:
                    pass

                # Strategy 1: WP Block Button class
                btn = page.locator('a.wp-block-button__link').first
                if btn.count() > 0:
                    final_url = btn.get_attribute('href')
                
                # Strategy 2: Text
                if not final_url:
                    btn = page.locator("a:has-text('Visit Site')").first
                    if btn.count() > 0:
                        final_url = btn.get_attribute('href')

            except:
                pass
            
            if final_url:
                if "?ref=" in final_url:
                    final_url = final_url.split("?")[0]
                row['external_link'] = final_url

        # 3. FIX DESCRIPTION (Optional but good)
        if pd.isna(row.get('description')) or row.get('description') == "":
            try:
                # Try meta description or first paragraph
                desc = page.locator('meta[name="description"]').get_attribute("content")
                if desc:
                    row['description'] = desc
            except:
                pass

    except Exception:
        pass
    finally:
        page.close()
    
    return row

def main():
    print(f"--- 🔧 STARTING EASYWITHAI REPAIR ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    data = df.to_dict('records')
    
    # Filter
    rows_to_fix = [r for r in data if (r.get('tool_name') == "Unknown" or pd.isna(r.get('tool_name'))) or (pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "")]
    rows_good = [r for r in data if r not in rows_to_fix]
    
    print(f"   ⚠️ Found {len(rows_to_fix)} tools to repair.")

    with sync_playwright() as p:
        # Visible browser to handle Cloudflare
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        fixed_results = []
        for i, row in enumerate(rows_to_fix):
            fixed = fix_row(context, row)
            fixed_results.append(fixed)
            
            if (i + 1) % 10 == 0:
                print(f"      Processed {i+1}/{len(rows_to_fix)}...", end="\r")
        
        browser.close()

    # Save
    final_data = rows_good + fixed_results
    df_fixed = pd.DataFrame(final_data)
    
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df_fixed.columns: df_fixed[c] = ""
        
    df_fixed = df_fixed[cols]
    df_fixed.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()