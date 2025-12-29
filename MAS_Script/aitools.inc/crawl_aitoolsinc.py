import pandas as pd
import time
from playwright.sync_api import sync_playwright
import sys

# --- CONFIGURATION ---
OUTPUT_FILE = "aitoolsinc_complete.csv"
MAX_PAGES_PER_CATEGORY = 100
SAVE_INTERVAL = 5

CATEGORY_URLS = [
    "https://aitools.inc/categories/ai-image-generators",
    "https://aitools.inc/categories/ai-sales-tools",
    "https://aitools.inc/categories/ai-copywriting-tools",
    "https://aitools.inc/categories/ai-developer-tools",
    "https://aitools.inc/categories/ai-marketing-tools",
    "https://aitools.inc/categories/ai-business-tools",
    "https://aitools.inc/categories/ai-video-tools",
    "https://aitools.inc/categories/ai-art-tools",
    "https://aitools.inc/categories/ai-audio-tools",
    "https://aitools.inc/categories/ai-content-creation-tools",
    "https://aitools.inc/categories/ai-productivity-tools",
    "https://aitools.inc/categories/ai-writing-assistants",
    "https://aitools.inc/categories/ai-automation-tools",
    "https://aitools.inc/categories/ai-design-tools",
    "https://aitools.inc/categories/ai-content-generators",
    "https://aitools.inc/categories/ai-video-generators",
    "https://aitools.inc/categories/ai-research-tools",
    "https://aitools.inc/categories/ai-digital-marketing-tools",
    "https://aitools.inc/categories/ai-data-analytics-tools",
    "https://aitools.inc/categories/ai-chat-bots",
    "https://aitools.inc/categories/ai-personal-assistants",
    "https://aitools.inc/categories/ai-knowledge-management-tools",
    "https://aitools.inc/categories/ai-customer-support-tools",
    "https://aitools.inc/categories/ai-writing-generators",
    "https://aitools.inc/categories/ai-summarizers",
    "https://aitools.inc/categories/ai-art-generators",
    "https://aitools.inc/categories/ai-research-assistants",
    "https://aitools.inc/categories/ai-photo-editors",
    "https://aitools.inc/categories/ai-no-code-tools",
    "https://aitools.inc/categories/ai-seo-tools",
    "https://aitools.inc/categories/ai-video-editors",
    "https://aitools.inc/categories/ai-data-management-tools",
    "https://aitools.inc/categories/ai-text-to-image-tools",
    "https://aitools.inc/categories/ai-translators",
    "https://aitools.inc/categories/ai-animation-generators",
    "https://aitools.inc/categories/ai-text-generators",
    "https://aitools.inc/categories/ai-coding-assistants",
    "https://aitools.inc/categories/ai-agents",
    "https://aitools.inc/categories/ai-text-to-video-tools",
    "https://aitools.inc/categories/ai-background-removers",
    "https://aitools.inc/categories/ai-lead-generation-tools",
    "https://aitools.inc/categories/ai-text-to-speech-tools",
    "https://aitools.inc/categories/ai-voice-generators",
    "https://aitools.inc/categories/ai-data-visualization-tools",
    "https://aitools.inc/categories/ai-short-video-generators",
    "https://aitools.inc/categories/ai-avatar-generators",
    "https://aitools.inc/categories/ai-sales-assistants",
    "https://aitools.inc/categories/ai-photo-generators",
    "https://aitools.inc/categories/ai-code-generators",
    "https://aitools.inc/categories/ai-blog-post-generators",
    "https://aitools.inc/categories/ai-note-takers",
    "https://aitools.inc/categories/ai-subtitle-generators",
    "https://aitools.inc/categories/ai-graphic-design-tools",
    "https://aitools.inc/categories/ai-3d-model-generators",
    "https://aitools.inc/categories/ai-character-generators",
    "https://aitools.inc/categories/ai-tutors",
    "https://aitools.inc/categories/ai-voice-over-tools",
    "https://aitools.inc/categories/ai-website-builders",
    "https://aitools.inc/categories/ai-presentation-tools",
    "https://aitools.inc/categories/ai-teaching-tools",
    "https://aitools.inc/categories/ai-presentation-makers",
    "https://aitools.inc/categories/ai-video-clip-generators",
    "https://aitools.inc/categories/ai-image-upscalers",
    "https://aitools.inc/categories/ai-product-photo-tools",
    "https://aitools.inc/categories/ai-project-management-tools",
    "https://aitools.inc/categories/ai-meeting-note-takers",
    "https://aitools.inc/categories/ai-music-generators",
    "https://aitools.inc/categories/ai-security-software",
    "https://aitools.inc/categories/ai-job-search-tools",
    "https://aitools.inc/categories/ai-voice-agents",
    "https://aitools.inc/categories/ai-document-editors",
    "https://aitools.inc/categories/ai-prospecting-tools",
    "https://aitools.inc/categories/ai-document-summarizers",
    "https://aitools.inc/categories/personal-ais",
    "https://aitools.inc/categories/ai-slide-deck-generators",
    "https://aitools.inc/categories/ai-voice-cloning-tools",
    "https://aitools.inc/categories/ai-video-transcribers",
    "https://aitools.inc/categories/ai-governance-software",
    "https://aitools.inc/categories/ai-email-marketing-tools",
    "https://aitools.inc/categories/ai-writers",
    "https://aitools.inc/categories/ai-finance-tools",
    "https://aitools.inc/categories/ai-coaches",
    "https://aitools.inc/categories/ai-photo-retouching-tools",
    "https://aitools.inc/categories/ai-code-writers",
    "https://aitools.inc/categories/ai-scheduling-assistants",
    "https://aitools.inc/categories/ai-ad-generators",
    "https://aitools.inc/categories/ai-email-generators",
    "https://aitools.inc/categories/ai-document-processing-tools",
    "https://aitools.inc/categories/ai-search-engines",
    "https://aitools.inc/categories/ai-tiktok-video-generators",
    "https://aitools.inc/categories/ai-image-to-video-tools",
    "https://aitools.inc/categories/ai-face-swap-tools",
    "https://aitools.inc/categories/ai-quiz-generators",
    "https://aitools.inc/categories/chat-with-pdf-ai-tools",
    "https://aitools.inc/categories/ai-voice-to-text-tools",
    "https://aitools.inc/categories/ai-app-builders",
    "https://aitools.inc/categories/ai-portrait-generators",
    "https://aitools.inc/categories/ai-mental-health-tools",
    "https://aitools.inc/categories/ai-chart-generators",
    "https://aitools.inc/categories/ai-song-generators",
    "https://aitools.inc/categories/ai-talking-avatar-tools",
    "https://aitools.inc/categories/ai-cold-email-tools",
    "https://aitools.inc/categories/ai-email-writers",
    "https://aitools.inc/categories/ai-content-detectors",
    "https://aitools.inc/categories/ai-powerpoint-generators",
    "https://aitools.inc/categories/ai-plagiarism-checkers",
    "https://aitools.inc/categories/ai-paraphrasers",
    "https://aitools.inc/categories/ai-resume-builders",
    "https://aitools.inc/categories/ai-object-removers",
    "https://aitools.inc/categories/ai-interior-design-tools",
    "https://aitools.inc/categories/ai-prompt-engineering-tools",
    "https://aitools.inc/categories/ai-hiring-tools",
    "https://aitools.inc/categories/ai-fashion-tools",
    "https://aitools.inc/categories/ai-forecasting-tools",
    "https://aitools.inc/categories/ai-real-estate-tools",
    "https://aitools.inc/categories/ai-resume-checkers",
    "https://aitools.inc/categories/ai-audio-transcribers",
    "https://aitools.inc/categories/ai-podcast-tools",
    "https://aitools.inc/categories/ai-ad-creative-generators",
    "https://aitools.inc/categories/ai-keyword-tools",
    "https://aitools.inc/categories/ai-web-scraping-tools",
    "https://aitools.inc/categories/ai-video-summarizers",
    "https://aitools.inc/categories/ai-companions",
    "https://aitools.inc/categories/ai-recruiting-tools",
    "https://aitools.inc/categories/ai-story-generators",
    "https://aitools.inc/categories/ai-cover-letter-generators",
    "https://aitools.inc/categories/ai-dubbing-tools",
    "https://aitools.inc/categories/ai-virtual-staging-tools",
    "https://aitools.inc/categories/ai-video-enhancers",
    "https://aitools.inc/categories/ai-room-designers",
    "https://aitools.inc/categories/ai-games",
    "https://aitools.inc/categories/ai-sales-agents",
    "https://aitools.inc/categories/ai-language-learning-tools",
    "https://aitools.inc/categories/ai-drawing-generators",
    "https://aitools.inc/categories/ai-detectors",
    "https://aitools.inc/categories/ai-anime-art-generators",
    "https://aitools.inc/categories/ai-youtube-short-generators",
    "https://aitools.inc/categories/ai-image-to-text-tools",
    "https://aitools.inc/categories/llm-observability-tools",
    "https://aitools.inc/categories/ai-legal-tools",
    "https://aitools.inc/categories/ai-portrait-tools",
    "https://aitools.inc/categories/ai-image-to-3d-model-tools",
    "https://aitools.inc/categories/ai-math-solvers",
    "https://aitools.inc/categories/ai-flashcard-makers",
    "https://aitools.inc/categories/text-to-music-ai-tools",
    "https://aitools.inc/categories/ai-instagram-reel-generators",
    "https://aitools.inc/categories/ai-shopping-assistants",
    "https://aitools.inc/categories/ai-software-engineers",
    "https://aitools.inc/categories/ai-cartoon-generators",
    "https://aitools.inc/categories/ai-headshot-tools",
    "https://aitools.inc/categories/ai-report-generators",
    "https://aitools.inc/categories/ai-data-entry-tools",
    "https://aitools.inc/categories/ai-architecture-tools",
    "https://aitools.inc/categories/ai-essay-writers",
    "https://aitools.inc/categories/ai-pdf-summarizers",
    "https://aitools.inc/categories/ai-interview-coaches",
    "https://aitools.inc/categories/social-media-ai-assistants",
    "https://aitools.inc/categories/ai-fitness-tools",
    "https://aitools.inc/categories/ai-profile-picture-generators",
    "https://aitools.inc/categories/ai-video-translators",
    "https://aitools.inc/categories/ai-interview-tools",
    "https://aitools.inc/categories/ai-knowledge-base-tools",
    "https://aitools.inc/categories/ai-image-restoration-tools",
    "https://aitools.inc/categories/ai-diagram-generators",
    "https://aitools.inc/categories/ai-product-description-generators",
    "https://aitools.inc/categories/ai-wireframe-generators",
    "https://aitools.inc/categories/ai-personal-stylists",
    "https://aitools.inc/categories/ai-investing-tools",
    "https://aitools.inc/categories/ai-home-rendering-tools",
    "https://aitools.inc/categories/ai-youtube-video-summarizers",
    "https://aitools.inc/categories/ai-deepfake-tools",
    "https://aitools.inc/categories/ai-storyboard-generators",
    "https://aitools.inc/categories/ai-unblur-image-tools",
    "https://aitools.inc/categories/ai-logo-designers",
    "https://aitools.inc/categories/ai-infographic-generators",
    "https://aitools.inc/categories/ai-spreadsheet-tools",
    "https://aitools.inc/categories/ai-code-review-tools",
    "https://aitools.inc/categories/ai-outline-generators",
    "https://aitools.inc/categories/ai-thumbnail-makers",
    "https://aitools.inc/categories/ai-trip-planners",
    "https://aitools.inc/categories/ai-answer-generators",
    "https://aitools.inc/categories/ai-travel-planners",
    "https://aitools.inc/categories/llms",
    "https://aitools.inc/categories/ai-logo-generators",
    "https://aitools.inc/categories/ai-therapists",
    "https://aitools.inc/categories/ai-friends",
    "https://aitools.inc/categories/ai-meme-generators",
    "https://aitools.inc/categories/ai-image-description-generators",
    "https://aitools.inc/categories/ai-image-to-code-tools",
    "https://aitools.inc/categories/ai-mockup-generators",
    "https://aitools.inc/categories/ai-stock-image-generators",
    "https://aitools.inc/categories/ai-interview-prep-tools",
    "https://aitools.inc/categories/ai-contract-review-tools",
    "https://aitools.inc/categories/ai-pitch-deck-generators",
    "https://aitools.inc/categories/ai-pixel-art-generators",
    "https://aitools.inc/categories/ai-comic-generators",
    "https://aitools.inc/categories/ai-meal-planners",
    "https://aitools.inc/categories/ai-prompt-generators",
    "https://aitools.inc/categories/ai-social-media-post-generators",
    "https://aitools.inc/categories/ai-invoice-processing-tools",
    "https://aitools.inc/categories/ai-healthcare-tools",
    "https://aitools.inc/categories/ai-trainers",
    "https://aitools.inc/categories/ai-article-summarizers",
    "https://aitools.inc/categories/ai-script-generators",
    "https://aitools.inc/categories/ai-assessment-tools",
    "https://aitools.inc/categories/ai-essay-generators",
    "https://aitools.inc/categories/ai-landing-page-generators",
    "https://aitools.inc/categories/ai-legal-assistants",
    "https://aitools.inc/categories/prompt-to-video-ai-tools",
    "https://aitools.inc/categories/ai-sdrs",
    "https://aitools.inc/categories/chatgpt-detectors",
    "https://aitools.inc/categories/ai-cover-letter-tools",
    "https://aitools.inc/categories/ai-text-to-voice-tools",
    "https://aitools.inc/categories/ai-cad-design-tools",
    "https://aitools.inc/categories/ai-resource-management-tools",
    "https://aitools.inc/categories/ai-wallpaper-generators",
    "https://aitools.inc/categories/ai-lesson-plan-generators",
    "https://aitools.inc/categories/ai-dating-apps",
    "https://aitools.inc/categories/ai-sketch-to-image-tools",
    "https://aitools.inc/categories/ai-voice-actors",
    "https://aitools.inc/categories/ai-newsletter-generators",
    "https://aitools.inc/categories/ai-question-generators",
    "https://aitools.inc/categories/ai-concierges",
    "https://aitools.inc/categories/ai-stock-picking-tools",
    "https://aitools.inc/categories/ai-accounting-tools",
    "https://aitools.inc/categories/ai-legal-document-generators",
    "https://aitools.inc/categories/ai-girlfriends",
    "https://aitools.inc/categories/ai-lyric-generators",
    "https://aitools.inc/categories/ai-recipe-generators",
    "https://aitools.inc/categories/ai-voice-enhancers",
    "https://aitools.inc/categories/ai-business-plan-generators",
    "https://aitools.inc/categories/ai-tattoo-generators",
    "https://aitools.inc/categories/ai-workout-generators",
    "https://aitools.inc/categories/ai-bdrs",
    "https://aitools.inc/categories/ai-vector-databases",
    "https://aitools.inc/categories/ai-graph-generators",
    "https://aitools.inc/categories/ai-hairstyle-generators",
    "https://aitools.inc/categories/ai-coloring-book-generators",
    "https://aitools.inc/categories/ai-video-to-blog-tools",
    "https://aitools.inc/categories/ai-follow-up-email-tools",
    "https://aitools.inc/categories/ai-poster-generators",
    "https://aitools.inc/categories/ai-b-roll-generators",
    "https://aitools.inc/categories/rag-tools",
    "https://aitools.inc/categories/ai-sales-reps",
    "https://aitools.inc/categories/ai-mechanical-engineering-tools",
    "https://aitools.inc/categories/ai-checkers",
    "https://aitools.inc/categories/ai-voice-changers",
    "https://aitools.inc/categories/ugc-ai-tools",
    "https://aitools.inc/categories/ai-schedule-generators",
    "https://aitools.inc/categories/ai-excel-tools",
    "https://aitools.inc/categories/ai-essay-graders",
    "https://aitools.inc/categories/ai-book-summarizers",
    "https://aitools.inc/categories/ai-exterior-home-design-tools",
    "https://aitools.inc/categories/ai-job-description-generators",
    "https://aitools.inc/categories/ai-quality-assurance-tools",
    "https://aitools.inc/categories/ai-person-generators",
    "https://aitools.inc/categories/ai-sql-tools",
    "https://aitools.inc/categories/ai-texting-tools",
    "https://aitools.inc/categories/ai-youtube-title-generators",
    "https://aitools.inc/categories/ai-business-card-generators",
    "https://aitools.inc/categories/ai-stock-research-tools",
    "https://aitools.inc/categories/ai-astrology-apps",
    "https://aitools.inc/categories/ai-course-creators",
    "https://aitools.inc/categories/ai-proposal-generators",
    "https://aitools.inc/categories/ai-paper-writers",
    "https://aitools.inc/categories/ai-lawyers",
    "https://aitools.inc/categories/ai-invitation-generators",
    "https://aitools.inc/categories/ai-sports-betting-tools",
    "https://aitools.inc/categories/ai-rfp-software",
    "https://aitools.inc/categories/ai-gift-idea-generators",
    "https://aitools.inc/categories/ai-baby-name-generators",
    "https://aitools.inc/categories/ai-architecture-generators",
    "https://aitools.inc/categories/ai-audio-translators",
    "https://aitools.inc/categories/ai-doctors",
    "https://aitools.inc/categories/ai-browsers",
    "https://aitools.inc/categories/ai-therapy-notes",
    "https://aitools.inc/categories/ai-regex-generators",
    "https://aitools.inc/categories/ai-stock-trading-bots",
    "https://aitools.inc/categories/ai-handwriting-generators",
    "https://aitools.inc/categories/ai-instagram-caption-generators",
    "https://aitools.inc/categories/ai-floor-plan-generators",
    "https://aitools.inc/categories/ai-t-shirt-design-generators",
    "https://aitools.inc/categories/ai-instagram-post-generators",
    "https://aitools.inc/categories/ai-landscape-design-tools",
    "https://aitools.inc/categories/ai-movie-recommendation-tools",
    "https://aitools.inc/categories/ai-screenshot-tools",
    "https://aitools.inc/categories/ai-manga-generators",
    "https://aitools.inc/categories/ai-blueprint-generators",
    "https://aitools.inc/categories/ai-business-name-generators",
    "https://aitools.inc/categories/ai-twitter-post-generators",
    "https://aitools.inc/categories/ai-playlist-generators",
    "https://aitools.inc/categories/ai-backlink-tools",
    "https://aitools.inc/categories/ai-excel-formula-generators",
    "https://aitools.inc/categories/ai-human-generators",
    "https://aitools.inc/categories/ai-qr-code-generators",
    "https://aitools.inc/categories/ai-sticker-generators",
    "https://aitools.inc/categories/ai-map-generators",
    "https://aitools.inc/categories/ai-domain-name-generators",
    "https://aitools.inc/categories/ai-crypto-trading-bots",
    "https://aitools.inc/categories/ai-thank-you-note-generators",
    "https://aitools.inc/categories/ai-dating-profile-bio-generators",
    "https://aitools.inc/categories/ai-sentence-generators",
    "https://aitools.inc/categories/ai-review-generators",
    "https://aitools.inc/categories/ai-poem-generators",
    "https://aitools.inc/categories/ai-religious-tools",
    "https://aitools.inc/categories/ai-model-comparison-tools",
    "https://aitools.inc/categories/ai-passport-photo-generators",
    "https://aitools.inc/categories/ai-emoji-generators",
    "https://aitools.inc/categories/ai-youtube-banner-generators",
    "https://aitools.inc/categories/ai-stock-screeners"
]

def save_csv(data):
    if not data: return
    df = pd.DataFrame(data)
    cols = ["tool_name", "external_link", "description", "category_url", "internal_detail_url"]
    for c in cols:
        if c not in df.columns: df[c] = ""
    df = df[cols]
    df.to_csv(OUTPUT_FILE, index=False)

def resolve_link(browser, item):
    internal_url = item.get('internal_detail_url')
    if not internal_url: return item

    context = browser.new_context()
    page = context.new_page()
    final_url = ""
    
    try:
        # Block media
        page.route("**/*.{png,jpg,jpeg,svg,webp,gif,mp4,woff,woff2}", lambda route: route.abort())
        
        try:
            page.goto(internal_url, timeout=30000, wait_until="domcontentloaded")
        except:
            pass 

        # Find "Visit Website" button
        try:
            btn = page.locator("a:has-text('Visit Website')").first
            if btn.count() > 0:
                href = btn.get_attribute('href')
                # Follow redirect if needed
                if href and "/go/website" in href:
                    try:
                        page.goto(f"https://aitools.inc{href}", timeout=30000, wait_until="domcontentloaded")
                        final_url = page.url
                    except:
                        final_url = href
                else:
                    final_url = href
        except:
            pass

    except Exception:
        pass
    finally:
        page.close()
        context.close()
    
    # Cleanup
    if final_url:
        if "?ref=" in final_url: final_url = final_url.split("?")[0]
        item['external_link'] = final_url
    
    return item

def harvest_aitoolsinc():
    # SYNC PLAYWRIGHT
    with sync_playwright() as p:
        print("--- 🚀 Starting AITools.inc Crawler (Sync Mode) ---")
        
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context()
        page = context.new_page()

        global_tools = {}
        
        # PHASE 1: CATEGORIES
        print(f"--- 📂 Phase 1: Crawling Categories... ---")
        
        for cat_url in CATEGORY_URLS:
            cat_name = cat_url.strip('/').split('/')[-1]
            print(f"   👉 Category: {cat_name}")
            
            current_page = 1
            try:
                while current_page <= MAX_PAGES_PER_CATEGORY:
                    if current_page == 1:
                        url = cat_url
                    else:
                        url = f"{cat_url.rstrip('/')}/page/{current_page}/"
                    
                    try:
                        response = page.goto(url, timeout=6000000, wait_until="domcontentloaded")
                        if response.status == 404: break
                        
                        # Check for items
                        if page.locator('a[href^="/tools/"]').count() == 0:
                            break

                        # Extract
                        tools = page.evaluate("""() => {
                            const results = [];
                            const cards = document.querySelectorAll('div[class*="tool-card"]'); // Generic card selector
                            
                            // Fallback if card class varies: look for links
                            if (cards.length === 0) {
                                 const links = document.querySelectorAll('a[href^="/tools/"]');
                                 links.forEach(link => {
                                     try {
                                         const nameEl = link.querySelector('p, h3, span'); 
                                         const name = nameEl ? nameEl.innerText.trim() : "Unknown";
                                         results.push({
                                             tool_name: name,
                                             internal_detail_url: link.getAttribute('href')
                                         });
                                     } catch(e) {}
                                 });
                            }
                            return results;
                        }""")

                        new_count = 0
                        for t in tools:
                            full_url = f"https://aitools.inc{t['internal_detail_url']}"
                            if full_url not in global_tools:
                                global_tools[full_url] = {
                                    "tool_name": t['tool_name'],
                                    "description": "",
                                    "internal_detail_url": full_url,
                                    "category_url": cat_url,
                                    "external_link": ""
                                }
                                new_count += 1
                        
                        if new_count > 0:
                            save_csv(list(global_tools.values()))
                        else:
                            break

                        # Pagination
                        next_btn = page.locator('a:has-text("Next")')
                        if next_btn.count() > 0:
                            next_btn.click()
                            time.sleep(2)
                            current_page += 1
                        else:
                            break
                            
                    except Exception as e:
                        print(f"      ❌ Error: {e}")
                        break
            except:
                pass
            
        all_tools = list(global_tools.values())
        print(f"   ✨ Phase 1 Complete. Total: {len(all_tools)}")

        # PHASE 2: LINKS
        print(f"--- 🕵️‍♀️ Phase 2: Resolving Links (Sequential) ---")
        count = 0
        for item in all_tools:
            resolve_link(browser, item)
            count += 1
            if count % 20 == 0:
                print(f"      Processed {count}/{len(all_tools)}...", end="\r")
                save_csv(all_tools)
        
        save_csv(all_tools)
        print(f"\n🎉 DONE! Saved to {OUTPUT_FILE}")
        browser.close()

if __name__ == "__main__":
    harvest_aitoolsinc()