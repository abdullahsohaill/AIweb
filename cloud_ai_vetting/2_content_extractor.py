import asyncio
import pandas as pd
import os
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm
import sys

# --- CONFIGURATION ---
INPUT_FILE = "sampled_100.csv"
OUTPUT_METADATA = "content_metadata.csv"
CONTENT_DIR = "extracted_content"
MAX_CONCURRENT_TABS = 6

if not os.path.exists(CONTENT_DIR):
    os.makedirs(CONTENT_DIR)

def sanitize_filename(name):
    clean = re.sub(r'[^\w\s-]', '', str(name)).strip().lower()
    return re.sub(r'[-\s]+', '_', clean)[:50]

async def process_url(context, row, semaphore):
    url = row.get('Extracted URL') or row.get('url')
    tool_name = row.get('Tool Name') or row.get('tool_name')
    
    if not url:
        return row.name, None, "No URL"

    async with semaphore:
        page = await context.new_page()
        try:
            # Block heavy assets
            await page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2,css}", lambda route: route.abort())
            
            try:
                await page.goto(url, timeout=45000, wait_until="domcontentloaded")
            except:
                print(f"   ⚠️ Timeout/Error loading {url}")
                await page.close()
                return row.name, None, "Timeout/NavError"

            # Get raw HTML
            html_content = await page.content()
            
            # --- CUSTOM CLEANING LOGIC ---
            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.title.string.strip() if soup.title else "No Title"

            # 1. Remove Junk Tags (Scripts, Styles, IFrames)
            # We keep 'nav' and 'footer' because sometimes "API" links are hidden there!
            for tag in soup(["script", "style", "iframe", "noscript", "svg", "button", "input", "form"]):
                tag.decompose()

            # 2. Extract Body
            body_html = str(soup.body) if soup.body else str(soup)

            # 3. Convert to Markdown (Preserves Links & Structure)
            # heading_style="ATX" ensures # Headers
            markdown_text = md(body_html, heading_style="ATX")
            
            # 4. Aggressive Whitespace Cleanup
            # Remove repeated newlines (more than 2)
            markdown_text = re.sub(r'\n\s*\n', '\n\n', markdown_text)
            # Remove lines that are just whitespace
            markdown_text = "\n".join([line.rstrip() for line in markdown_text.splitlines()])

            # Save
            filename = f"{sanitize_filename(tool_name)}_{row.name}.md"
            filepath = os.path.join(CONTENT_DIR, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {tool_name}\n")
                f.write(f"**URL:** {url}\n")
                f.write(f"**Page Title:** {title}\n\n")
                f.write("--- CONTENT START ---\n\n")
                f.write(markdown_text)
                f.write("\n\n--- CONTENT END ---")

            return row.name, filepath, "Success"

        except Exception as e:
            return row.name, None, f"Error: {str(e)[:50]}"
        finally:
            await page.close()

async def main():
    print(f"--- 📄 FULL LANDING PAGE EXTRACTOR (BS4 + Markdownify) ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file {INPUT_FILE} not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    print(f"   Loaded {len(df)} URLs to process.")
    
    df['content_file'] = None
    df['extract_status'] = "Pending"
    
    rows = [row for _, row in df.iterrows()]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [process_url(context, row, semaphore) for row in rows]
        
        for f in tqdm(asyncio.as_completed(tasks), total=len(rows), desc="Extracting"):
            index, filepath, status = await f
            df.at[index, 'content_file'] = filepath
            df.at[index, 'extract_status'] = status
        
        await browser.close()

    df.to_csv(OUTPUT_METADATA, index=False)
    print(f"\n✅ Extraction complete!")
    print(f"   Metadata saved to: {OUTPUT_METADATA}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())