import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys
import os

# --- CONFIGURATION ---
INPUT_FILE = "easywithai_complete.csv"
OUTPUT_FILE = "easywithai_repaired.csv"
SAVE_INTERVAL = 10  # Save every 10 items

def save_data(fixed_list, remaining_list, good_list):
    """
    Combines fixed, remaining to be fixed, and originally good rows 
    to create a complete CSV backup.
    """
    combined = good_list + fixed_list + remaining_list
    df = pd.DataFrame(combined)
    
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    # Ensure columns exist
    for c in cols:
        if c not in df.columns: df[c] = ""
        
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)
    # print(f"      💾 Progress Saved ({len(df)} records)")

def fix_row(context, row):
    # Check what is missing
    missing_name = pd.isna(row.get('tool_name')) or str(row.get('tool_name')).strip() == "" or row.get('tool_name') == "Unknown"
    missing_link = pd.isna(row.get('external_link')) or str(row.get('external_link')).strip() == ""
    
    if not missing_name and not missing_link:
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: return row

    page = context.new_page()
    
    try:
        # Visit
        try:
            page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        except:
            pass 

        # --- CLOUDFLARE CHECK ---
        # Check if we are blocked
        title = page.title()
        if "Just a moment" in title or "Access denied" in title:
            # Wait briefly to see if it auto-solves
            time.sleep(5)
            if "Just a moment" in page.title():
                print(f"      ⚠️ Cloudflare Blocked {internal_url}. Skipping...")
                page.close()
                return row # Return unmodified row and move on

        # 1. FIX NAME
        if missing_name:
            try:
                # Try H1 Elementor title
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
                # Wait briefly for button
                try:
                    page.wait_for_selector('a.wp-block-button__link', timeout=3000)
                except:
                    pass

                # Strategy 1: WP Block Button
                btn = page.locator('a.wp-block-button__link').first
                if btn.count() > 0:
                    final_url = btn.get_attribute('href')
                
                # Strategy 2: Text Search
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

        # 3. FIX DESCRIPTION
        if pd.isna(row.get('description')) or str(row.get('description')).strip() == "":
            try:
                # Meta description is best fallback
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
    print(f"--- 🔧 STARTING EASYWITHAI REPAIR (Skipping Blocks) ---")
    
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
        # Visible browser to bypass simple bots protections
        browser = p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        fixed_results = []
        
        for i, row in enumerate(rows_to_fix):
            fixed = fix_row(context, row)
            fixed_results.append(fixed)
            
            # Progress Log
            if (i + 1) % 5 == 0:
                print(f"      Processed {i+1}/{len(rows_to_fix)}...", end="\r")
            
            # Live Save
            if (i + 1) % SAVE_INTERVAL == 0:
                # Remaining rows that haven't been processed yet
                remaining = rows_to_fix[i+1:]
                save_data(fixed_results, remaining, rows_good)
        
        browser.close()

    # Final Save
    save_data(fixed_results, [], rows_good)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()