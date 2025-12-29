import asyncio
import pandas as pd
import random
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from tqdm import tqdm

# --- CONFIGURATION ---
INPUT_FILE = "toolify_harvest.csv"
OUTPUT_FILE = "toolify_final_enriched.csv"
CONCURRENT_TABS = 5  # Number of pages to scrape at the same time (speed vs. safety)

async def scrape_details(context, row):
    """
    Visits the internal detail page to extract deep metadata.
    """
    internal_url = row.get('internal_detail_url')
    
    # Default result combines old data with new empty fields
    result = row.copy()
    result.update({
        "external_url": None,
        "monthly_visits": None,
        "active_users": None,
        "reviews_count": 0,
        "saved_count": 0,
        "pricing_model": None,
        "categories_tags": None
    })

    if not internal_url or not isinstance(internal_url, str):
        return result

    page = await context.new_page()
    
    try:
        # Random small delay to stagger requests
        await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # Navigate
        await page.goto(internal_url, timeout=45000, wait_until="domcontentloaded")
        
        # 1. EXTRACT EXTERNAL LINK (The "Open site" / "Visit Website" button)
        # The class 'to-view-btn' is the most reliable selector based on your HTML
        try:
            ext_link_element = page.locator("a.to-view-btn").first
            if await ext_link_element.count() > 0:
                result['external_url'] = await ext_link_element.get_attribute("href")
        except:
            pass

        # --- PARSE PAGE CONTENT ---
        # We grab HTML to parse the complex table/text structures easily with BS4
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        # 2. EXTRACT TABLE DATA (Monthly Visitors, Active Users, Pricing)
        # Look for the div that acts as a table
        table_rows = soup.find_all('div', class_='table-row')
        
        for r in table_rows:
            cells = r.find_all('div', class_='table-cell')
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True).lower()
                value = cells[1].get_text(strip=True)
                
                if "monthly visit" in key:
                    result['monthly_visits'] = value
                elif "active users" in key:
                    result['active_users'] = value
                elif "introduction" in key and not result.get('short_description'):
                    # Fallback if we missed description in Phase 1
                    result['short_description'] = value
        
        # 3. EXTRACT REVIEWS & SAVED
        # These are usually in the '.tool-detail-info' section
        # We look for text patterns like "5 Saved" or "1 Reviews"
        info_text = soup.get_text() 
        
        # Regex for Saved
        saved_match = re.search(r'(\d+)\s*Saved', info_text)
        if saved_match:
            result['saved_count'] = saved_match.group(1)
            
        # Regex for Reviews
        reviews_match = re.search(r'(\d+)\s*Reviews', info_text)
        if reviews_match:
            result['reviews_count'] = reviews_match.group(1)

        # 4. EXTRACT TAGS/PRICING LABELS
        # Usually in class 't-label'
        tags = [t.get_text(strip=True) for t in soup.find_all(class_='t-label')]
        if tags:
            result['categories_tags'] = ", ".join(tags)
            # Simple heuristic for pricing model
            for t in tags:
                if t.lower() in ['free', 'freemium', 'paid', 'free trial']:
                    result['pricing_model'] = t
                    break

    except Exception as e:
        # print(f"Error scraping {internal_url}: {e}")
        pass
    finally:
        await page.close()
        
    return result

async def main():
    # Load the list we harvested in Phase 1
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"--- Loaded {len(df)} tools from {INPUT_FILE} ---")
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found. Run Phase 1 script first.")
        return

    # Prepare output list
    enriched_data = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Use a standard browser user agent to avoid blocking
        context = await browser.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        # Convert dataframe to list of dicts
        rows = df.to_dict('records')
        
        # Process in chunks to manage resources
        chunk_size = CONCURRENT_TABS
        pbar = tqdm(total=len(rows), desc="Enriching Data")
        
        for i in range(0, len(rows), chunk_size):
            chunk = rows[i:i + chunk_size]
            tasks = [scrape_details(context, row) for row in chunk]
            results = await asyncio.gather(*tasks)
            enriched_data.extend(results)
            pbar.update(len(chunk))
            
            # Save periodically in case of crash
            if i % 100 == 0:
                pd.DataFrame(enriched_data).to_csv(OUTPUT_FILE, index=False)
        
        await browser.close()
        pbar.close()

    # Final Save
    final_df = pd.DataFrame(enriched_data)
    final_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✅ Enrichment Complete. Saved to {OUTPUT_FILE}")
    print(f"Total Tools: {len(final_df)}")
    print(f"External Links Found: {final_df['external_url'].notna().sum()}")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())