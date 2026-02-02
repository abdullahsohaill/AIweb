import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from tqdm import tqdm
import sys
import os

# --- CONFIGURATION ---
INPUT_FILE = "final_tools_1M_reduced.csv"
OUTPUT_FILE = "final_tools_1M_corrected.csv"
MAX_CONCURRENT_TABS = 10
TIMEOUT_MS = 20000 

def normalize_url(u):
    """Standardize URL for strict comparison to ensure skip logic works."""
    if pd.isna(u) or not u: return ""
    return str(u).strip().lower().rstrip('/')

async def check_url(context, row, semaphore):
    url = row.get('Extracted URL') or row.get('url')
    if not url or pd.isna(url): 
        return None 

    async with semaphore:
        page = await context.new_page()
        try:
            # Block heavy assets
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())
            response = await page.goto(url, timeout=TIMEOUT_MS, wait_until="commit")
            
            if response:
                status = response.status
                # Success if 200-399 or specific bot blocks
                if 200 <= status < 400 or status in [403, 429, 406]:
                    return row
            return None 
        except Exception:
            return None
        finally:
            await page.close()

async def main():
    print(f"--- 🕵️‍♀️ DELTA VERIFICATION (Rank & FQDN Sort) ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file {INPUT_FILE} not found.")
        return

    df_input = pd.read_csv(INPUT_FILE)
    existing_valid_rows = []
    
    # --- STEP 1: DELTA IDENTIFICATION ---
    if os.path.exists(OUTPUT_FILE):
        df_output = pd.read_csv(OUTPUT_FILE)
        existing_valid_rows = df_output.to_dict('records')
        
        # Build set of normalized URLs already in the corrected file
        processed_urls = set()
        for col in ['Extracted URL', 'url']:
            if col in df_output.columns:
                processed_urls.update(df_output[col].apply(normalize_url).tolist())
        
        def needs_checking(row):
            u = normalize_url(row.get('Extracted URL') or row.get('url'))
            return u != "" and u not in processed_urls

        df_to_check = df_input[df_input.apply(needs_checking, axis=1)]
        print(f"   📊 Already Verified: {len(existing_valid_rows)}")
        print(f"   🎯 Target to Check: {len(df_to_check)} (Skipped {len(df_input) - len(df_to_check)})")
    else:
        df_to_check = df_input
        print(f"   📊 No output found. Checking all {len(df_to_check)} URLs.")

    if not df_to_check.empty:
        # --- STEP 2: VERIFY MISSING ROWS ---
        newly_verified_rows = []
        rows_to_process = [row for _, row in df_to_check.iterrows()]

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
            tasks = [check_url(context, row, semaphore) for row in rows_to_process]
            
            for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Verifying New"):
                result = await f
                if result is not None:
                    newly_verified_rows.append(result)
            await browser.close()
        existing_valid_rows.extend(newly_verified_rows)

    # --- STEP 3: DEDUPLICATE, SORT & SAVE ---
    if existing_valid_rows:
        df_final = pd.DataFrame(existing_valid_rows)
        
        # Deduplicate on normalized URL
        df_final['temp_norm'] = (df_final['Extracted URL'].fillna(df_final.get('url', ''))).apply(normalize_url)
        df_final = df_final.drop_duplicates(subset=['temp_norm']).drop(columns=['temp_norm'])

        # Multi-level Sort Logic
        rank_col = 'Median Tranco Rank'
        fqdn_col = 'Domain (FQDN)'

        sort_cols = []
        if rank_col in df_final.columns:
            # Force numeric so 1, 2, 10, 100 sort correctly
            df_final[rank_col] = pd.to_numeric(df_final[rank_col], errors='coerce')
            sort_cols.append(rank_col)
        
        if fqdn_col in df_final.columns:
            df_final[fqdn_col] = df_final[fqdn_col].astype(str)
            sort_cols.append(fqdn_col)

        if sort_cols:
            print(f"   🔄 Sorting by {sort_cols}...")
            # Ascending rank (1 is top) and alphabetical FQDN
            df_final = df_final.sort_values(by=sort_cols, ascending=True)

        df_final.to_csv(OUTPUT_FILE, index=False)
        print(f"\n✅ Total Saved: {len(df_final)} to {OUTPUT_FILE}")
    else:
        print("❌ No valid rows found.")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())