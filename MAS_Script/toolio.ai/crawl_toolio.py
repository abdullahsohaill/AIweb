# import asyncio
# import pandas as pd
# from playwright.async_api import async_playwright
# from bs4 import BeautifulSoup
# import sys

# # --- CONFIGURATION ---
# BASE_URL = "https://www.toolio.ai"
# OUTPUT_FILE = "toolio_complete.csv"

# # Concurrency for Phase 2
# MAX_CONCURRENT_TABS = 10 

# async def get_external_link(context, item):
#     page = await context.new_page()
#     internal_full_url = f"{BASE_URL}{item['internal_slug']}"
#     external_url = ""

#     try:
#         # Block media for speed
#         await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
        
#         await page.goto(internal_full_url, timeout=30000, wait_until="domcontentloaded")
        
#         try:
#             button = page.locator('#button-tool')
#             if await button.count() > 0:
#                 external_url = await button.get_attribute('href')
#         except:
#             pass
#     except Exception:
#         pass
#     finally:
#         await page.close()

#     item['external_link'] = external_url
#     return item

# async def harvest_toolio():
#     async with async_playwright() as p:
#         print("--- 🚀 PHASE 1: Harvesting Main List (Background Mode) ---")
#         browser = await p.chromium.launch(headless=True)
#         context = await browser.new_context()
#         page = await context.new_page()

#         print(f"   🌐 Visiting: {BASE_URL}")
#         await page.goto(BASE_URL, timeout=60000, wait_until="domcontentloaded")

#         await page.evaluate("window.scrollBy(0, 1000)")
#         await asyncio.sleep(2)

#         all_tools = []
#         page_num = 1
        
#         while True:
#             print(f"   📄 Scraping Page {page_num}...", end="\r")
            
#             content = await page.content()
#             soup = BeautifulSoup(content, 'html.parser')
#             cards = soup.find_all('a', id='tool')
            
#             current_count = 0
#             for card in cards:
#                 try:
#                     name_tag = card.find('h2', attrs={'fs-cmsfilter-field': 'name'})
#                     name = name_tag.get_text(strip=True) if name_tag else "Unknown"
                    
#                     desc_tag = card.find('p', attrs={'fs-cmsfilter-field': 'description'})
#                     desc = desc_tag.get_text(strip=True) if desc_tag else ""
                    
#                     href = card.get('href')
                    
#                     if href:
#                         all_tools.append({
#                             "tool_name": name,
#                             "description": desc,
#                             "internal_slug": href
#                         })
#                         current_count += 1
#                 except:
#                     continue
            
#             print(f"   📄 Scraping Page {page_num}... Found {current_count} tools.")

#             # --- SAFELY CLICK NEXT ---
#             try:
#                 # Check for next button
#                 next_button = page.locator("a.w-pagination-next:not(.just-launched)")
                
#                 # ONLY try to click if it exists AND is visible
#                 if await next_button.count() > 0 and await next_button.is_visible():
#                     await next_button.click()
#                     await asyncio.sleep(1.5) 
#                     page_num += 1
#                 else:
#                     print("   ✅ End of list reached (Button not visible).")
#                     break
#             except Exception as e:
#                 print(f"   ✅ End of list reached (Click stopped: {e}).")
#                 break
        
#         # Deduplicate
#         df_temp = pd.DataFrame(all_tools)
#         if not df_temp.empty:
#             df_temp = df_temp.drop_duplicates(subset=['internal_slug'])
#             unique_tools = df_temp.to_dict('records')
#         else:
#             unique_tools = []
            
#         print(f"   ✨ Phase 1 Complete. Total Unique Tools: {len(unique_tools)}")

#         # --- PHASE 2 ---
#         if unique_tools:
#             print(f"\n--- 🚀 PHASE 2: Extracting External Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            
#             semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
#             async def safe_process(item):
#                 async with semaphore:
#                     return await get_external_link(context, item)

#             tasks = [safe_process(item) for item in unique_tools]
            
#             final_results = []
#             total = len(tasks)
            
#             for i, task in enumerate(asyncio.as_completed(tasks)):
#                 res = await task
#                 final_results.append(res)
#                 if (i + 1) % 50 == 0:
#                     print(f"      Processed {i+1}/{total} tools...", end="\r")

#             await browser.close()
#             return final_results
#         else:
#             await browser.close()
#             return []

# def save_to_csv(data):
#     if not data:
#         print("❌ No data harvested.")
#         return

#     df = pd.DataFrame(data)
#     df['internal_full_url'] = df['internal_slug'].apply(lambda x: f"{BASE_URL}{x}")
    
#     cols = ["tool_name", "external_link", "description", "internal_full_url"]
#     existing_cols = [c for c in cols if c in df.columns]
#     df = df[existing_cols]
    
#     df.to_csv(OUTPUT_FILE, index=False)
#     print(f"\n🎉 SUCCESS! Saved {len(df)} tools to {OUTPUT_FILE}")

# if __name__ == "__main__":
#     if sys.platform.startswith('win'):
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(harvest_toolio())

import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys

# --- CONFIGURATION ---
BASE_URL = "https://www.toolio.ai"
OUTPUT_FILE = "toolio_complete.csv"
MAX_CONCURRENT_TABS = 10 

async def get_external_link(context, item, semaphore):
    async with semaphore:
        page = await context.new_page()
        internal_full_url = f"{BASE_URL}{item['internal_slug']}"
        external_url = ""

        try:
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4}", lambda route: route.abort())
            await page.goto(internal_full_url, timeout=30000, wait_until="domcontentloaded")
            try:
                button = page.locator('#button-tool')
                if await button.count() > 0:
                    external_url = await button.get_attribute('href')
            except:
                pass
        except:
            pass
        finally:
            await page.close()

        item['external_link'] = external_url
        return item

async def harvest_toolio():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting Main List ---")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(BASE_URL, timeout=60000, wait_until="domcontentloaded")
        await page.evaluate("window.scrollBy(0, 1000)")
        await asyncio.sleep(2)

        all_tools = []
        page_num = 1
        
        while True:
            print(f"   📄 Scraping Page {page_num}...", end="\r")
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            cards = soup.find_all('a', id='tool')
            
            count = 0
            for card in cards:
                try:
                    name = card.find('h2', attrs={'fs-cmsfilter-field': 'name'}).get_text(strip=True)
                    desc = card.find('p', attrs={'fs-cmsfilter-field': 'description'}).get_text(strip=True)
                    href = card.get('href')
                    if href:
                        all_tools.append({"tool_name": name, "description": desc, "internal_slug": href})
                        count += 1
                except:
                    continue
            
            print(f"   📄 Page {page_num}: Found {count} tools.")

            try:
                next_button = page.locator("a.w-pagination-next:not(.just-launched)")
                if await next_button.count() > 0 and await next_button.is_visible():
                    await next_button.click()
                    await asyncio.sleep(1.5) 
                    page_num += 1
                else:
                    print("   ✅ End of list reached.")
                    break
            except:
                break
        
        # Deduplicate
        df = pd.DataFrame(all_tools)
        df = df.drop_duplicates(subset=['internal_slug'])
        unique_tools = df.to_dict('records')
        print(f"   ✨ Phase 1 Complete. Unique Tools: {len(unique_tools)}")

        # --- PHASE 2 ---
        if unique_tools:
            print(f"\n--- 🚀 PHASE 2: Extracting Links ({MAX_CONCURRENT_TABS} concurrent) ---")
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)

            tasks = [get_external_link(context, item, semaphore) for item in unique_tools]
            
            final_results = []
            for i, task in enumerate(asyncio.as_completed(tasks)):
                res = await task
                final_results.append(res)
                if (i + 1) % 50 == 0:
                    print(f"      Processed {i+1}/{len(unique_tools)} tools...", end="\r")

            await browser.close()
            return final_results
        else:
            await browser.close()
            return []

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    df['internal_full_url'] = df['internal_slug'].apply(lambda x: f"{BASE_URL}{x}")
    
    # Safely reorder columns (only if they exist)
    cols = ["tool_name", "external_link", "description", "internal_full_url"]
    existing = [c for c in cols if c in df.columns]
    df = df[existing]
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 SUCCESS! Saved {len(df)} tools to {OUTPUT_FILE}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    # FIX IS HERE: Capture the data!
    data = asyncio.run(harvest_toolio())
    save_to_csv(data)