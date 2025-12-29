import pandas as pd
from playwright.sync_api import sync_playwright
import sys
import time

# --- CONFIGURATION ---
INPUT_FILE = "aitoolmall_complete.csv"   # The file with broken data
OUTPUT_FILE = "aitoolmall_repaired.csv"  # The fixed output

def fix_row(context, row):
    # Determine if this row needs fixing
    # Fix if Name is "Unknown", missing, or empty
    missing_name = (row.get('tool_name') == "Unknown") or pd.isna(row.get('tool_name')) or str(row.get('tool_name')).strip() == ""
    
    # Fix if Link is missing, empty, or "nan"
    missing_link = pd.isna(row.get('external_link')) or str(row.get('external_link')).strip() == "" or str(row.get('external_link')) == "nan"

    # If row is perfect, skip it
    if not missing_name and not missing_link:
        return row

    internal_url = row.get('internal_detail_url')
    if not internal_url: 
        return row

    page = context.new_page()
    
    try:
        # Block images/media to speed up the fix
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
        
        try:
            # Go to the internal page
            page.goto(internal_url, timeout=45000, wait_until="domcontentloaded")
            
            # Wait a moment for Elementor JS to render the text
            try:
                page.wait_for_selector('h1.elementor-heading-title', timeout=5000)
            except:
                pass 
        except:
            pass 

        # --- 1. FIX NAME ---
        if missing_name:
            found_name = None
            try:
                # Primary Selector (Based on your snippet)
                h1 = page.locator("h1.elementor-heading-title").first
                if h1.count() > 0:
                    found_name = h1.inner_text().strip()
                
                # Fallback 1: Any H1
                if not found_name:
                    h1_generic = page.locator("h1").first
                    if h1_generic.count() > 0:
                        found_name = h1_generic.inner_text().strip()

                # Fallback 2: Page Title tag
                if not found_name:
                    title_text = page.title()
                    if title_text:
                        # Clean up title like "MidJourney - AI Tool Mall"
                        found_name = title_text.split("-")[0].strip()

                if found_name:
                    row['tool_name'] = found_name
                    print(f"      🔹 Fixed Name: {found_name}")
            except Exception as e:
                print(f"      ⚠️ Name Error: {e}")

        # --- 2. FIX EXTERNAL LINK ---
        if missing_link:
            final_url = ""
            try:
                # Selector based on your snippet: a.elementor-button-link
                btn = page.locator("a.elementor-button-link").first
                
                if btn.count() > 0:
                    final_url = btn.get_attribute("href")
                else:
                    # Fallback: Find button containing text "Visit"
                    btn_text = page.locator("a:has-text('Visit')").first
                    if btn_text.count() > 0:
                        final_url = btn_text.get_attribute("href")
            except:
                pass
            
            # Cleanup Link
            if final_url:
                if "?ref=" in final_url:
                    final_url = final_url.split("?")[0]
                
                # Ensure we didn't grab the internal link by accident
                if "aitoolmall.com" not in final_url:
                    row['external_link'] = final_url
                    print(f"      🔹 Fixed Link: {final_url}")

        # --- 3. FIX DESCRIPTION (Optional) ---
        if pd.isna(row.get('description')) or str(row.get('description')).strip() == "":
            try:
                meta = page.locator('meta[name="description"]')
                if meta.count() > 0:
                    desc = meta.get_attribute("content")
                    if desc:
                        row['description'] = desc
            except:
                pass

    except Exception as e:
        print(f"      ❌ Page Error: {e}")
    finally:
        page.close()
    
    return row

def save_csv(data):
    """Helper to save safely"""
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "pricing", "developer", "internal_detail_url", "category_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    
    # Reorder columns nicely
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def main():
    print(f"--- 🔧 STARTING ROBUST REPAIR (SYNC) ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    data = df.to_dict('records')
    
    # Separate rows
    rows_to_fix = []
    rows_good = []

    for r in data:
        # Define Missing Criteria
        is_missing_name = (r.get('tool_name') == "Unknown") or pd.isna(r.get('tool_name'))
        is_missing_link = (pd.isna(r.get('external_link')) or str(r.get('external_link')).strip() == "" or str(r.get('external_link')) == "nan")
        
        if is_missing_name or is_missing_link:
            rows_to_fix.append(r)
        else:
            rows_good.append(r)
    
    print(f"   ⚠️ Found {len(rows_to_fix)} rows to repair.")
    print(f"   ✅ {len(rows_good)} rows are already complete.")
    
    if not rows_to_fix:
        print("   Nothing to do!")
        return

    # Start Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, # Visible so you can see it work
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        fixed_results = []
        
        for i, row in enumerate(rows_to_fix):
            print(f"   👉 [{i+1}/{len(rows_to_fix)}] Fixing: {row.get('internal_detail_url', 'No URL')}...")
            
            updated_row = fix_row(context, row)
            fixed_results.append(updated_row)
            
            # Save frequently (every 5 items)
            if (i + 1) % 5 == 0:
                current_data = rows_good + fixed_results + rows_to_fix[i+1:]
                save_csv(current_data)
        
        browser.close()

    # Final Save
    final_data = rows_good + fixed_results
    save_csv(final_data)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()