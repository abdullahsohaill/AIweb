import asyncio
import pandas as pd
import os
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys

# --- CONFIGURATION ---
INPUT_FILE = "sampled_50.csv" 
OUTPUT_METADATA = "full_content_metadata.csv"
CONTENT_DIR = "extracted_content"
MAX_CONCURRENT_TABS = 8

if not os.path.exists(CONTENT_DIR):
    os.makedirs(CONTENT_DIR)

def sanitize_filename(name):
    clean = re.sub(r'[^\w\s-]', '', str(name)).strip().lower()
    return re.sub(r'[-\s]+', '_', clean)[:50]

def clean_text_content(soup):
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
        else: output.append(text)
    return "\n".join(output)

async def process_url(context, row, semaphore):
    url = row.get('extracted_url') or row.get('url')
    tool_name = row.get('tool_name') or row.get('Tool Name')
    
    if not url: return row.name, None, "No URL"

    # Resume check
    filename = f"{sanitize_filename(tool_name)}_{row.name}.md"
    filepath = os.path.join(CONTENT_DIR, filename)
    if os.path.exists(filepath):
         return row.name, filepath, "Skipped (Exists)"

    async with semaphore:
        page = await context.new_page()
        try:
            # Block heavy media
            await page.route("**/*.{mp4,webm,avi,mkv,flv,mov}", lambda route: route.abort())
            
            try:
                await page.goto(url, timeout=45000, wait_until="networkidle") 
            except:
                try: await page.wait_for_load_state("domcontentloaded", timeout=10000)
                except: pass

            # --- FLUTTER DETECTION ---
            # We explicitly check for the Flutter engine tag
            is_flutter = False
            try:
                if await page.locator("flt-glass-pane").count() > 0:
                    is_flutter = True
                    # Flutter needs extra time to hydrate the semantics tree
                    await asyncio.sleep(5) 
            except: pass

            final_text = ""
            title = ""
            try:
                title = await page.title()
            except:
                title = "No Title"

            # --- STRATEGY A: FLUTTER / CANVAS (Priority if detected) ---
            if is_flutter:
                # print(f"   ℹ️  Flutter detected for {tool_name}. Using AX Tree.")
                try:
                    # interesting_only=False ensures we get everything, as Flutter semantics can be messy
                    snapshot = await page.accessibility.snapshot(interesting_only=False)
                    
                    def extract_ax_text(node):
                        text = []
                        # Flutter puts the visible text in 'name' or 'value'
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
                        # Remove duplicates while preserving order (common in Flutter ax trees)
                        seen = set()
                        deduped_lines = [x for x in ax_lines if not (x in seen or seen.add(x))]
                        
                        final_text = f"### (Flutter/Canvas Extraction)\n\n" + "\n".join(deduped_lines)
                except Exception as e:
                    final_text = "" # Fallback to standard if AX fails

            # --- STRATEGY B: STANDARD HTML (If not Flutter or AX failed) ---
            if not final_text:
                html_content = await page.content()
                soup = BeautifulSoup(html_content, 'html.parser')
                final_text = clean_text_content(soup)

            # --- STRATEGY C: RAW BODY FALLBACK (Last Resort) ---
            # If standard extraction was weak (< 200 chars), try raw body text
            if len(final_text) < 200:
                raw_body = await page.inner_text("body")
                # Only overwrite if raw body actually has more info
                if len(raw_body) > len(final_text):
                    final_text = f"### (Raw Extraction Fallback)\n\n{raw_body}"

            # Final validation
            if len(final_text) < 50: 
                return row.name, None, "Empty Content"

            final_text = re.sub(r'\n{3,}', '\n\n', final_text)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {tool_name}\n**URL:** {url}\n**Page Title:** {title}\n" + "-"*20 + "\n\n" + final_text + "\n\n" + "-"*20)

            return row.name, filepath, "Success"
        except Exception as e:
            return row.name, None, "Error"
        finally:
            await page.close()

async def main():
    print(f"--- 🚀 LOCAL AI FULL EXTRACTOR (Hybrid + Flutter) ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file not found: {INPUT_FILE}")
        return

    df = pd.read_csv(INPUT_FILE)
    df['content_file'] = None
    
    if os.path.exists(OUTPUT_METADATA):
        print("   Found existing metadata. Resuming...")
        try:
            existing_df = pd.read_csv(OUTPUT_METADATA)
            df.update(existing_df)
        except: pass

    rows = [row for _, row in df.iterrows()]

    async with async_playwright() as p:
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
                df.to_csv(OUTPUT_METADATA, index=False)
        
        await browser.close()

    df.to_csv(OUTPUT_METADATA, index=False)
    print(f"\n✅ Full Extraction complete! Metadata saved.")

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())