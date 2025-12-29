import pandas as pd
from playwright.sync_api import sync_playwright
import os
import time

# --- CONFIGURATION ---
# We prioritize the repaired file to incrementally fix it
if os.path.exists("aitoolmall_repaired.csv"):
    INPUT_FILE = "aitoolmall_repaired.csv"
else:
    INPUT_FILE = "aitoolmall_complete.csv"

OUTPUT_FILE = "aitoolmall_repaired.csv"

def fix_row(context, row):
    # Check if the current link is "Bad" (Empty, NaN, or Internal)
    current_link = str(row.get('external_link', ''))
    is_internal = "aitoolmall.com" in current_link
    is_empty = (not current_link) or (current_link.lower() == 'nan') or (current_link.strip() == "")
    
    # If it's a good external link, we keep the row and return it (skips processing)
    if not is_internal and not is_empty:
        return row

    internal_url = row.get('internal_detail_url')
    # If no internal URL to check, we can't fix it, so we delete it.
    if not internal_url or str(internal_url) == 'nan':
        return None

    page = context.new_page()
    final_url = ""
    
    try:
        # Block heavy media to speed up loading
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        # Navigate to the tool's internal page
        try:
            page.goto(internal_url, timeout=60000, wait_until="domcontentloaded")
        except:
            print(f"      ⚠️ Timeout loading {internal_url} -> Deleting Row")
            page.close()
            return None

        
        # --- STRATEGY 1: Elementor Button (Most Common) ---
        try:
            btn = page.locator("a.elementor-button-link").first
            if btn.count() > 0:
                href = btn.get_attribute("href")
                if href and "aitoolmall.com" not in href:
                    final_url = href
        except: pass

        # --- STRATEGY 2: Generic "Visit" Text ---
        if not final_url:
            try:
                # Look for a button containing 'Visit'
                btn = page.locator("a:has-text('Visit')").first
                if btn.count() > 0:
                    href = btn.get_attribute("href")
                    if href and "aitoolmall.com" not in href:
                        final_url = href
            except: pass

        # --- STRATEGY 3: Widget Button Container ---
        if not final_url:
            try:
                btn = page.locator(".elementor-widget-button a").first
                if btn.count() > 0:
                    href = btn.get_attribute("href")
                    if href and "aitoolmall.com" not in href:
                        final_url = href
            except: pass

        # Validate and Assign
        if final_url:
            # Clean up tracking params (ref, utm, etc)
            if "?" in final_url:
                final_url = final_url.split("?")[0]
            
            row['external_link'] = final_url
            print(f"      ✅ Fixed Link: {final_url}")
            
            # --- FIX NAME (Only if we found a link) ---
            current_name = str(row.get('tool_name', ''))
            if not current_name or current_name == "Unknown" or current_name.lower() == 'nan':
                try:
                    h1 = page.locator("h1.elementor-heading-title").first
                    if h1.count() > 0:
                        name = h1.inner_text().strip()
                        row['tool_name'] = name
                        print(f"      ✅ Fixed Name: {name}")
                except: pass
            
            return row
            
        else:
            # --- DELETION LOGIC ---
            print(f"      ❌ Could not find external link for: {row.get('tool_name')} -> Deleting Row.")
            return None

    except Exception as e:
        print(f"      ❌ Error processing row: {e} -> Deleting Row.")
        return None
    finally:
        page.close()

def save_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "pricing", "developer", "internal_detail_url", "category_url"]
    
    # Ensure all columns exist
    for c in cols:
        if c not in df.columns: df[c] = ""
    
    # Reorder columns
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def main():
    print(f"--- 🔧 STARTING AITOOLMALL FIXER ---")
    print(f"--- 📂 Input File: {INPUT_FILE} ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    data = df.to_dict('records')
    
    # Identify rows that actually need fixing
    rows_to_fix = []
    rows_good = []

    for r in data:
        # Check Link: Is it missing? OR Is it pointing to aitoolmall.com?
        link = str(r.get('external_link', ''))
        is_internal = "aitoolmall.com" in link
        is_empty = (not link) or (link.lower() == 'nan') or (link.strip() == "")
        
        # Check Name
        name = str(r.get('tool_name', ''))
        is_bad_name = (not name) or (name == "Unknown") or (name.lower() == 'nan')

        if is_empty or is_internal or is_bad_name:
            rows_to_fix.append(r)
        else:
            rows_good.append(r)
    
    print(f"   📊 Total Rows: {len(data)}")
    print(f"   ✅ Good Rows:  {len(rows_good)}")
    print(f"   ⚠️  To Fix:    {len(rows_to_fix)} (Includes internal link errors)")
    
    if not rows_to_fix:
        print("   🎉 Nothing to fix! Exiting.")
        return

    # Start Playwright
    with sync_playwright() as p:
        # HEADLESS = FALSE to see the browser and avoid simple bot blocks
        browser = p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        fixed_results = []
        
        for i, row in enumerate(rows_to_fix):
            print(f"   👉 [{i+1}/{len(rows_to_fix)}] Visiting: {row.get('internal_detail_url')}")
            
            updated_row = fix_row(context, row)
            
            if updated_row: # Only append if the row was successfully fixed
                fixed_results.append(updated_row)
            
            # Save frequently (every 5 items)
            if (i + 1) % 5 == 0:
                current_data = rows_good + fixed_results + rows_to_fix[i+1:]
                save_csv(current_data)
                print("      💾 Progress saved.")
        
        browser.close()

    # Final Save
    final_data = rows_good + fixed_results
    save_csv(final_data)
    print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()