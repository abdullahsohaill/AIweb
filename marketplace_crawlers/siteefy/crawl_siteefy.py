import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
MAIN_URL = "https://siteefy.com/ai-tools/"
OUTPUT_FILE = "siteefy_complete.csv"
MAX_CONCURRENT_TABS = 5  # How many detail pages to open at once (prevents crashing)

async def get_external_link(context, item):
    """
    Visits the internal URL (e.g., siteefy.com/ai-tools/durable-ai/)
    and extracts the actual external link from the 'View Website' button.
    """
    page = await context.new_page()
    internal_url = item['internal_detail_url']
    external_url = "Not Found"
    
    print(f"   Phase 2: Visiting internal page -> {item['tool_name']}...")

    try:
        # Block images to speed up loading since we only need the button link
        await page.route("**/*.{png,jpg,jpeg,svg,webp}", lambda route: route.abort())
        
        await page.goto(internal_url, timeout=60000, wait_until="domcontentloaded")
        
        # We are looking for: <a class="gb-button ..." href="...">View Website</a>
        # We use a text selector because class names might vary, but the text "View Website" is consistent.
        try:
            # Wait briefly for the button to be present
            button = page.locator("a:has-text('View Website')").first
            if await button.count() > 0:
                external_url = await button.get_attribute("href")
            else:
                # Fallback: sometimes it might be "Visit Site" or just a raw link in the Pros/Cons
                # Let's try to find the first link in the "Pros & Cons" section if the button fails
                pass 
        except Exception as e:
            print(f"      ⚠️ Could not find button for {item['tool_name']}")

    except Exception as e:
        print(f"      ❌ Error loading {internal_url}: {e}")
    finally:
        await page.close()
        
    # Return the item with the new data attached
    item['external_link'] = external_url
    return item

async def harvest_siteefy_list():
    async with async_playwright() as p:
        print("--- 🚀 PHASE 1: Harvesting Main List ---")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # 1. Go to Main Page
        await page.goto(MAIN_URL, timeout=90000, wait_until="domcontentloaded")
        
        # 2. Scroll to bottom to ensure all DOM elements render (Siteefy is long)
        print("   🔄 Scrolling to load all tools...")
        last_height = await page.evaluate("document.body.scrollHeight")
        while True:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await asyncio.sleep(2)
            new_height = await page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        print("   📥 Parsing Main Page HTML...")
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        # 3. Parse the Main List
        # Based on your HTML: <div class="gb-container ... toolbox-column-style ...">
        # We look for the specific class 'toolbox-column-style' which seems to wrap tool cards
        cards = soup.find_all('div', class_='toolbox-column-style')
        
        initial_data = []
        print(f"   ✅ Found {len(cards)} potential tool cards. extracting info...")

        for card in cards:
            try:
                # Extract Name & Internal Link
                # <h3 class="toolbox-column-heading"><a href="...">Name</a></h3>
                h3 = card.find('h3', class_='toolbox-column-heading')
                if not h3: continue
                
                a_tag = h3.find('a')
                if not a_tag: continue
                
                name = a_tag.get_text(strip=True)
                internal_link = a_tag['href']

                # Extract Description
                # <p class="toolbox-column-description">Description</p>
                desc_tag = card.find('p', class_='toolbox-column-description')
                description = desc_tag.get_text(strip=True) if desc_tag else ""

                initial_data.append({
                    "tool_name": name,
                    "short_description": description,
                    "internal_detail_url": internal_link
                })
            except:
                continue
        
        # Remove duplicates if any
        # Convert to dataframe temporarily to drop dupes based on url
        df_temp = pd.DataFrame(initial_data)
        if not df_temp.empty:
            df_temp = df_temp.drop_duplicates(subset=['internal_detail_url'])
            unique_tools = df_temp.to_dict('records')
        else:
            unique_tools = []

        print(f"   📝 Successfully identified {len(unique_tools)} unique tools.")
        
        # --- PHASE 2: Process Internal Pages ---
        print(f"\n--- 🚀 PHASE 2: extracting External Links ({MAX_CONCURRENT_TABS} at a time) ---")
        
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)

        async def safe_process(item):
            async with semaphore:
                return await get_external_link(context, item)

        # Create tasks for all tools
        tasks = [safe_process(item) for item in unique_tools]
        
        # Run them
        final_results = await asyncio.gather(*tasks)
        
        await browser.close()
        return final_results

def save_to_csv(data):
    if not data:
        print("❌ No data collected.")
        return

    df = pd.DataFrame(data)
    
    # Final Cleanup
    df = df.drop_duplicates(subset=['internal_detail_url'])
    
    # Reorder columns for neatness
    cols = ["tool_name", "external_link", "short_description", "internal_detail_url"]
    # Only select columns that actually exist in df
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 DONE!")
    print(f"   Total Tools: {len(df)}")
    print(f"   Saved to:    {OUTPUT_FILE}")

if __name__ == "__main__":
    # Fix for Windows asyncio
    import sys
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    data = asyncio.run(harvest_siteefy_list())
    save_to_csv(data)