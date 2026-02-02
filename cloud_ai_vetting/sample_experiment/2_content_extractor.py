import asyncio
import pandas as pd
import os
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
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
        else:
            output.append(text)
    return "\n".join(output)

async def process_url(context, row, semaphore):
    # Adjust column names for Cloud AI CSV structure
    url = row.get('Extracted URL') or row.get('url')
    tool_name = row.get('Tool Name') or row.get('tool_name')
    
    if not url: return row.name, None, "No URL"

    async with semaphore:
        page = await context.new_page()
        try:
            # Only block heavy video, allow JS/CSS for rendering apps
            await page.route("**/*.{mp4,webm,avi,mkv,flv,mov}", lambda route: route.abort())
            
            try:
                await page.goto(url, timeout=45000, wait_until="networkidle") 
            except:
                try: await page.wait_for_load_state("domcontentloaded", timeout=10000)
                except: pass

            # Wait for dynamic apps to hydrate
            await asyncio.sleep(3)

            html_content = await page.content()
            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.title.string.strip() if soup.title else "No Title"

            # --- STRATEGY 1: SEMANTIC HTML ---
            final_text = clean_text_content(soup)

            # --- STRATEGY 2: RAW BODY TEXT ---
            if len(final_text) < 200:
                raw_body = await page.inner_text("body")
                final_text = f"### (Raw Extraction Fallback)\n\n{raw_body}"

            # --- STRATEGY 3: ACCESSIBILITY TREE (For Flutter/Canvas/React) ---
            if len(final_text) < 100:
                # print(f"   ℹ️  Canvas/Flutter app detected for {tool_name}, using accessibility tree.")
                try:
                    snapshot = await page.accessibility.snapshot()
                    
                    def extract_ax_text(node):
                        text = []
                        if 'name' in node and node['name']:
                            text.append(node['name'])
                        if 'children' in node:
                            for child in node['children']:
                                text.extend(extract_ax_text(child))
                        return text
                    
                    ax_lines = extract_ax_text(snapshot)
                    final_text = f"### (Accessibility Tree Fallback)\n\n" + "\n".join(ax_lines)
                except: pass

            if len(final_text) < 50: return row.name, None, "Empty Content"

            final_text = re.sub(r'\n{3,}', '\n\n', final_text)

            filename = f"{sanitize_filename(tool_name)}_{row.name}.md"
            filepath = os.path.join(CONTENT_DIR, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {tool_name}\n**URL:** {url}\n**Page Title:** {title}\n" + "-"*20 + "\n\n" + final_text + "\n\n" + "-"*20)

            return row.name, filepath, "Success"

        except Exception as e:
            return row.name, None, f"Error: {str(e)[:50]}"
        finally:
            await page.close()

async def main():
    print(f"--- 📄 CLOUD AI SAMPLE EXTRACTOR (Hybrid + Canvas) ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file {INPUT_FILE} not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    df['content_file'] = None
    df['extract_status'] = "Pending"
    
    rows = [row for _, row in df.iterrows()]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_TABS)
        
        tasks = [process_url(context, row, semaphore) for row in rows]
        
        for f in tqdm(asyncio.as_completed(tasks), total=len(rows)):
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