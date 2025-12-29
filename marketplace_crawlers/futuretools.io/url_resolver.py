import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import sys
import time

# --- CONFIGURATION ---
INPUT_FILE = "futuretools_complete.csv"
OUTPUT_FILE = "futuretools_resolved_final.csv"

# SETTINGS
CONCURRENT_TABS = 8       # Process 8 links at once (Safe for background)
MAX_WAIT_TIME = 90        # Wait up to 90s per link to allow slow redirects

async def resolve_link(context, original_url, semaphore):
    # Skip if already resolved or empty
    if pd.isna(original_url) or "futuretools.link" not in str(original_url):
        return original_url

    async with semaphore:
        page = await context.new_page()
        final_url = original_url
        
        try:
            # 1. NON-BLOCKING NAVIGATION
            # Initiate loading but don't freeze waiting for it
            try:
                await page.goto(original_url, timeout=5000, wait_until="commit")
            except:
                pass 

            # 2. POLLING LOOP (Watchdog)
            start_time = time.time()
            
            while True:
                elapsed = time.time() - start_time
                
                # A. Timeout Check
                if elapsed > MAX_WAIT_TIME:
                    break

                # B. Check URL Change
                current_url = page.url
                
                # If URL is no longer futuretools (and not blank)
                if "futuretools.link" not in current_url and current_url != "about:blank":
                    final_url = current_url
                    break
                
                # If Chrome Error (Dead Link)
                if "chrome-error" in current_url:
                    final_url = "Dead Link"
                    break

                # C. Sleep
                await asyncio.sleep(2)
            
            # 3. CLEANUP & FORMATTING
            # Remove referral params to make it clean (e.g. ?ref=futuretools)
            if "?" in final_url and "futuretools.link" not in final_url:
                final_url = final_url.split("?")[0]

        except Exception:
            pass
        finally:
            # Close the page to free up RAM
            await page.close()
            
        return final_url

async def main():
    print(f"--- 🕵️‍♀️ STARTING FULL BACKGROUND RESOLVER ---")
    print(f"--- 📂 Reading {INPUT_FILE} ---")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except:
        print("❌ CSV not found.")
        return

    links = df['website_url'].tolist()
    total = len(links)
    print(f"--- 🚀 Resolving {total} links in background ({CONCURRENT_TABS} concurrent)...")

    async with async_playwright() as p:
        # STEALTH LAUNCH (The configuration that worked)
        browser = await p.chromium.launch(
            headless=True, # Background Mode
            args=[
                "--disable-blink-features=AutomationControlled", 
                "--no-sandbox",
                "--disable-infobars"
            ]
        )
        
        # Configure context to look real
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            locale="en-US"
        )
        
        semaphore = asyncio.Semaphore(CONCURRENT_TABS)
        
        # Create Tasks
        tasks = [resolve_link(context, link, semaphore) for link in links]
        
        # Run with Progress Bar
        print("    ... Processing (This will take time) ...")
        
        chunk_size = 20
        results = []
        
        for i in range(0, total, chunk_size):
            chunk = tasks[i : i + chunk_size]
            chunk_results = await asyncio.gather(*chunk)
            results.extend(chunk_results)
            
            # Print status
            print(f"    ✅ Processed {len(results)}/{total} links...", end="\r")

        await browser.close()

    # Save Results
    print(f"\n--- 💾 Saving Data ---")
    df['real_website_url'] = results
    
    # Reorder columns
    cols = list(df.columns)
    if 'website_url' in cols:
        target_index = cols.index('website_url') + 1
        if 'real_website_url' in cols: cols.remove('real_website_url')
        cols.insert(target_index, 'real_website_url')
        df = df[cols]

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"🎉 DONE! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())