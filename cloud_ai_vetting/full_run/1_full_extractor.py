import asyncio
import pandas as pd
import os
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys

# --- CONFIGURATION ---
INPUT_FILE = "../../services_collection/final_tools_1M_vetting/final_tools_1M_corrected.csv"
OUTPUT_METADATA = "full_content_metadata.csv"
CONTENT_DIR = "extracted_content"
MAX_CONCURRENT_TABS = 1  # Concurrency for bulk processing

if not os.path.exists(CONTENT_DIR):
    os.makedirs(CONTENT_DIR)

def sanitize_filename(name):
    """Creates a safe filename from a tool name."""
    clean = re.sub(r'[^\w\s-]', '', str(name)).strip().lower()
    return re.sub(r'[-\s]+', '_', clean)[:50]

def clean_text_content(soup):
    """Extracts semantic text: Headers, Paragraphs, Lists, and Links."""
    for tag in soup(['script', 'style', 'noscript', 'iframe', 'svg', 'header', 'footer', 'nav', 'aside', 'form', 'button']):
        tag.decompose()

    output = []
    for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'li', 'a']):
        text = element.get_text(" ", strip=True)
        if not text or len(text) < 3: continue
        
        if element.name in ['h1', 'h2']: output.append(f"\n## {text}\n")
        elif element.name == 'h3': output.append(f"\n### {text}\n")
        elif element.name == 'li': output.append(f"- {text}")
        elif element.name == 'a':
            href = element.get('href')
            if href and any(x in href.lower() for x in ['api', 'docs', 'developer', 'github']):
                output.append(f"[LINK: {text}]({href})")
        else:
            output.append(text)
    return "\n".join(output)

async def process_url(context, row, semaphore):
    url = row.get('Extracted URL') or row.get('url')
    tool_name = row.get('Tool Name') or row.get('tool_name')
    
    if not url: return row.name, None, "No URL"

    # Resume check: Skip if the file already exists
    filename = f"{sanitize_filename(tool_name)}_{row.name}.md"
    filepath = os.path.join(CONTENT_DIR, filename)
    if os.path.exists(filepath):
         return row.name, filepath, "Skipped (Exists)"

    async with semaphore:
        page = await context.new_page()
        try:
            # Block video/audio to save bandwidth
            await page.route("**/*.{mp4,webm,avi,mkv,flv,mov,mp3,wav,ogg}", lambda route: route.abort())
            
            try:
                await page.goto(url, timeout=450000, wait_until="networkidle") 
            except:
                try: await page.wait_for_load_state("domcontentloaded", timeout=100000)
                except: pass

            # Detect Flutter/Canvas engine
            is_flutter = False
            try:
                if await page.locator("flt-glass-pane").count() > 0:
                    is_flutter = True
                    await asyncio.sleep(4) # Wait for canvas to paint
            except: pass

            final_text = ""
            title = "No Title"
            try: title = await page.title()
            except: pass

            # --- STRATEGY A: FLUTTER / CANVAS (Priority if detected) ---
            if is_flutter:
                try:
                    snapshot = await page.accessibility.snapshot(interesting_only=False)
                    def extract_ax_text(node):
                        text = []
                        if 'name' in node and node['name'] and len(node['name']) > 1:
                            text.append(node['name'])
                        if 'value' in node and node['value'] and len(node['value']) > 1:
                            text.append(str(node['value']))
                        if 'children' in node:
                            for child in node['children']:
                                text.extend(extract_ax_text(child))
                        return text
                    
                    if snapshot:
                        ax_lines = extract_ax_text(snapshot)
                        seen = set()
                        deduped_lines = [x for x in ax_lines if not (x in seen or seen.add(x))]
                        final_text = f"### (Flutter/Canvas Extraction)\n\n" + "\n".join(deduped_lines)
                except: final_text = ""

            # --- STRATEGY B: STANDARD HTML ---
            if not final_text:
                html_content = await page.content()
                soup = BeautifulSoup(html_content, 'html.parser')
                final_text = clean_text_content(soup)

            # --- STRATEGY C: RAW BODY TEXT ---
            if len(final_text) < 200:
                raw_body = await page.inner_text("body")
                if len(raw_body) > len(final_text):
                    final_text = f"### (Raw Extraction Fallback)\n\n{raw_body}"

            if len(final_text) < 50: return row.name, None, "Empty Content"

            final_text = re.sub(r'\n{3,}', '\n\n', final_text)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {tool_name}\n**URL:** {url}\n**Page Title:** {title}\n" + "-"*20 + "\n\n" + final_text + "\n\n" + "-"*20)

            return row.name, filepath, "Success"
        except Exception as e:
            return row.name, None, "Error"
        finally:
            await page.close()

async def main():
    print(f"--- 🚀 FULL SCALE CLOUD AI EXTRACTOR (Hybrid + Canvas + Resume) ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file not found: {INPUT_FILE}")
        return

    df = pd.read_csv(INPUT_FILE)
    df['content_file'] = None
    
    # Load existing metadata to resume progress
    if os.path.exists(OUTPUT_METADATA):
        print("   Found existing metadata. Resuming...")
        try:
            existing_df = pd.read_csv(OUTPUT_METADATA)
            df.update(existing_df)
        except: pass

    rows = [row for _, row in df.iterrows()]

    async with async_playwright() as p:
        # HEADLESS=FALSE is crucial for rendering all app types and passing bot checks
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [process_url(context, row, semaphore) for row in rows]
        
        counter = 0
        for f in tqdm(asyncio.as_completed(tasks), total=len(rows)):
            index, filepath, status = await f
            df.at[index, 'content_file'] = filepath
            
            counter += 1
            if counter % 50 == 0:
                df.to_csv(OUTPUT_METADATA, index=False) # Save progress every 50 items
        
        await browser.close()

    df.to_csv(OUTPUT_METADATA, index=False)
    print(f"\n✅ Full Extraction complete! Metadata saved to {OUTPUT_METADATA}")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())