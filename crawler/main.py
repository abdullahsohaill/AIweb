"""
main.py — Crawler Orchestrator Entry Point
============================================

This is the main entry point for the AI web crawler. It ties together
all the modules into a coherent pipeline:

    1. Launch browser (stealth, extensions, permissions)
    2. Navigate to target URL
    3. Wait for Consent-O-Matic to handle cookies
    4. Set up network + CDP capture listeners
    5. Simulate human behavior (mouse, scroll, clicks, popup dismissal)
    6. Detect and trigger AI components (chatbots, voice AI)
    7. Re-capture frames to catch dynamically injected chatbot iframes
    8. Run network-level AI confirmation
    9. Capture all frames, storage, permissions, and final page state
    10. Save structured JSON output
    11. Cleanup

USAGE:
    # Crawl a single URL:
    python -m crawler.main --url https://example.com

    # Crawl from a file (one URL per line):
    python -m crawler.main --file sites.txt

    # Crawl with custom output directory:
    python -m crawler.main --url https://example.com --output ./results/

    # Run in headless mode (NOTE: extensions won't work):
    python -m crawler.main --url https://example.com --headless
"""

import argparse
import asyncio
import json
import logging
import sys
import time
from pathlib import Path

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

from .browser import launch_browser, create_page, close_browser
from .interaction import simulate_human_behavior
from .capture import (
    CaptureSession, 
    setup_network_capture, 
    setup_cdp_capture, 
    run_full_capture,
    capture_frames_dynamic,
    capture_permission_state,
)
from .ai_invocation import trigger_ai_components, check_network_for_ai_activity
from .utils import (
    PAGE_LOAD_TIMEOUT_MS,
    INTERACTION_TIMEOUT_MS,
    OUTPUT_DIR,
    setup_logger,
    sanitize_domain,
    save_crawl_data,
    create_empty_crawl_result,
    timestamp,
)

logger = setup_logger("crawler.main")


# =============================================================================
# SINGLE SITE CRAWL PIPELINE
# =============================================================================

async def crawl_site(
    context,
    url: str,
    output_dir: str = None,
) -> dict:
    """
    Execute the full crawl pipeline for a single website.
    
    This is the core function that orchestrates all modules for one URL.
    It follows a strict sequence designed to:
    1. Set up monitoring BEFORE any navigation (to capture everything)
    2. Let the page stabilize before interacting
    3. Simulate human behavior to avoid detection and trigger lazy-loading
    4. Invoke AI components after the page is settled
    5. RE-CAPTURE frames after AI invocation (catches new chatbot iframes)
    6. Run network-level AI confirmation
    7. Capture the FINAL state of everything
    
    WHY THIS ORDER?
    - Network/CDP capture must be set up FIRST so we don't miss requests
    - Human behavior happens before AI invocation because some sites
      require "engagement" before showing chatbot widgets
    - Frame re-capture after AI invocation catches dynamically injected
      chatbot iframes (Intercom, Drift, etc.)
    - Network AI confirmation happens LAST because it analyzes the
      network requests accumulated during the entire crawl
    - Final capture happens LAST to get the complete state including
      any AI conversations that happened
    
    Args:
        context: Browser context from launch_browser()
        url: URL to crawl
        output_dir: Override output directory (optional)
    
    Returns:
        Dictionary with full crawl results
    """
    domain = sanitize_domain(url)
    crawl_data = create_empty_crawl_result(url)
    crawl_data["timing"]["start"] = timestamp()

    logger.info(f"{'=' * 60}")
    logger.info(f"CRAWLING: {url}")
    logger.info(f"{'=' * 60}")

    page = None
    cdp_client = None
    capture_session = CaptureSession()

    try:
        # --- Step 1: Create page with stealth and CDP ---
        logger.info("[1/9] Creating page with stealth + CDP")
        page, cdp_client = await create_page(context)

        # --- Step 2: Set up capture BEFORE navigation ---
        # WHY BEFORE? We want to capture the very first requests the page makes
        # (initial HTML, CSS, JS, and any pre-load API calls). If we set up
        # capture after navigation, we'd miss these early requests.
        logger.info("[2/9] Setting up network + CDP capture")
        setup_network_capture(page, capture_session)
        await setup_cdp_capture(page, cdp_client, capture_session)

        # --- Step 3: Navigate to the URL ---
        logger.info(f"[3/9] Navigating to {url}")
        try:
            response = await page.goto(
                url,
                wait_until="domcontentloaded",  # Don't wait for ALL resources
                timeout=PAGE_LOAD_TIMEOUT_MS,
            )

            if response:
                crawl_data["http_status"] = response.status
                logger.info(f"Page loaded | status={response.status}")
            else:
                crawl_data["http_status"] = None
                logger.warning("Navigation returned no response")

        except PlaywrightTimeout:
            # Page took too long to load. This is common for slow/broken sites.
            # We continue the crawl anyway — partial data is still valuable.
            logger.warning(f"Page load TIMEOUT after {PAGE_LOAD_TIMEOUT_MS}ms (continuing anyway)")
            crawl_data["http_status"] = "timeout"

        crawl_data["timing"]["page_loaded"] = timestamp()

        # --- Step 4: Wait for Consent-O-Matic ---
        # The extension needs a moment to detect and click cookie banners.
        # WHY 5 SECONDS? Cookie banners typically appear within 2-3s of page load.
        # The extension then needs ~1-2s to find and click the accept button.
        logger.info("[4/9] Waiting for Consent-O-Matic (5s)")
        await asyncio.sleep(5)
        crawl_data["timing"]["consent_handled"] = timestamp()

        # --- Step 5: Simulate human behavior ---
        # This serves THREE purposes:
        # 1. Anti-detection: Look like a real user (avoid CAPTCHAs, blocks)
        # 2. Trigger lazy-loading: Scroll reveals hidden content, chatbot widgets
        # 3. Dismiss popups: Fallback consent/notification handling
        logger.info("[5/9] Simulating human behavior")
        interaction_result = await simulate_human_behavior(page)
        crawl_data["timing"]["interaction_done"] = timestamp()
        
        # Record consent fallback results
        if interaction_result.get("consent_fallback"):
            fallback = interaction_result["consent_fallback"]
            crawl_data["consent_handling"]["fallback_used"] = fallback.get("popups_dismissed", 0) > 0
            crawl_data["consent_handling"]["popups_dismissed"] = fallback.get("popups_dismissed", 0)

        # --- Step 6: Detect and trigger AI components ---
        # This is the research-critical step. We look for chatbots, copilots,
        # AI widgets, etc., and try to interact with them.
        logger.info("[6/9] Detecting and triggering AI components")
        ai_result = await trigger_ai_components(page)
        crawl_data["ai_detection"] = ai_result


        crawl_data["timing"]["ai_invocation_done"] = timestamp()

        # --- Step 7: Re-capture frames after AI invocation ---
        # WHY? Chatbot iframes are often injected DURING AI invocation.
        # If we only captured frames before, we miss the chatbot content.
        logger.info("[7/9] Re-capturing frames (post-AI invocation)")
        new_frames = await capture_frames_dynamic(page, capture_session)
        
        # --- Step 8: Network-level AI confirmation ---
        # WHY? Clicking a chat button doesn't prove it's AI-powered.
        # We verify by checking if network requests hit known AI endpoints
        # or contain conversational JSON (Kaya et al., 2025).
        logger.info("[8/9] Running network-level AI confirmation")
        network_confirmation = check_network_for_ai_activity(
            [r for r in capture_session.network_requests]
        )
        crawl_data["ai_network_confirmation"] = network_confirmation

        # --- Step 9: Final capture ---
        # Capture everything: all frames (main + iframes), storage, and
        # any remaining network data. This includes chatbot iframe content
        # that may have been loaded during AI invocation.
        logger.info("[9/9] Running final capture")
        await run_full_capture(page, cdp_client, capture_session)

        # Capture permission states for privacy analysis
        permissions = await capture_permission_state(page)
        crawl_data["permissions_requested"] = permissions

        # Merge capture session data into crawl result
        capture_data = capture_session.to_dict()
        crawl_data["frames"] = capture_data["frames"]
        crawl_data["network_requests"] = capture_data["network_requests"]
        crawl_data["cdp_requests"] = capture_data["cdp_requests"]
        crawl_data["storage"] = capture_data["storage"]

        crawl_data["timing"]["capture_done"] = timestamp()
        crawl_data["status"] = "success"

        logger.info(
            f"Crawl COMPLETE | "
            f"frames={len(crawl_data['frames'])} | "
            f"requests={len(crawl_data['network_requests'])} | "
            f"cdp_requests={len(crawl_data['cdp_requests'])} | "
            f"ai_triggered={ai_result.get('triggered', False)} | "
            f"ai_confirmed={network_confirmation.get('ai_confirmed', False)} | "
            f"new_frames_post_ai={new_frames}"
        )

    except Exception as e:
        # Catch-all for unexpected errors. We still save whatever data
        # we managed to collect before the error.
        crawl_data["status"] = "error"
        crawl_data["error"] = str(e)
        logger.error(f"Crawl FAILED: {e}", exc_info=True)

    finally:
        crawl_data["timing"]["end"] = timestamp()

        # Close the page (but keep the browser context for the next site)
        if page:
            try:
                await page.close()
            except Exception:
                pass

    # --- Save output ---
    out_dir = output_dir or OUTPUT_DIR
    filepath = save_crawl_data(crawl_data, domain)
    logger.info(f"Results saved to: {filepath}")

    return crawl_data


# =============================================================================
# BATCH CRAWL (Multiple Sites)
# =============================================================================

async def crawl_sites(
    urls: list[str],
    headless: bool = False,
    output_dir: str = None,
    proxy: str = None,
) -> list[dict]:
    """
    Crawl multiple sites sequentially.
    
    WHY SEQUENTIAL (not parallel)?
    1. Extensions only work with one browser context at a time
    2. Bot detection is triggered by multiple concurrent sessions
    3. It's easier to debug and maintain
    4. For research, we need reliable data over speed
    
    Args:
        urls: List of URLs to crawl
        headless: If True, run without GUI (extensions won't work!)
        output_dir: Override output directory
    
    Returns:
        List of crawl result dictionaries
    """
    results = []

    async with async_playwright() as playwright:
        # Launch browser once, reuse for all sites
        context = await launch_browser(playwright, headless=headless, proxy=proxy)

        try:
            for i, url in enumerate(urls):
                logger.info(f"\n{'#' * 60}")
                logger.info(f"Site {i + 1}/{len(urls)}: {url}")
                logger.info(f"{'#' * 60}")

                try:
                    result = await crawl_site(context, url, output_dir)
                    results.append(result)
                except Exception as e:
                    logger.error(f"Fatal error crawling {url}: {e}")
                    results.append({
                        "url": url,
                        "status": "fatal_error",
                        "error": str(e),
                    })

                # Brief pause between sites to avoid rate limiting
                if i < len(urls) - 1:
                    pause = 3
                    logger.info(f"Pausing {pause}s before next site...")
                    await asyncio.sleep(pause)

        finally:
            await close_browser(context)

    return results


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Examples:
        python -m crawler.main --url https://example.com
        python -m crawler.main --file tranco_top1000.txt
        python -m crawler.main --url https://example.com --headless --output ./results/
    """
    parser = argparse.ArgumentParser(
        description="AI Web Crawler — Detect and analyze AI services on websites",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m crawler.main --url https://example.com
  python -m crawler.main --file sites.txt
  python -m crawler.main --url https://example.com --output ./results/
        """,
    )

    # URL source (one of these is required)
    url_group = parser.add_mutually_exclusive_group(required=True)
    url_group.add_argument(
        "--url",
        type=str,
        help="Single URL to crawl",
    )
    url_group.add_argument(
        "--file",
        type=str,
        help="Path to a text file with one URL per line",
    )

    # Options
    parser.add_argument(
        "--headless",
        action="store_true",
        default=False,
        help="Run in headless mode (NOTE: extensions will NOT work)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help=f"Output directory for JSON results (default: {OUTPUT_DIR})",
    )
    parser.add_argument(
        "--max-sites",
        type=int,
        default=None,
        help="Maximum number of sites to crawl (useful for testing)",
    )
    parser.add_argument(
        "--proxy",
        type=str,
        help="Proxy server URL (e.g., http://user:pass@ip:port) to route traffic through.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose (DEBUG) logging",
    )

    return parser.parse_args()


def load_urls_from_file(filepath: str) -> list[str]:
    """
    Load URLs from a text file (one URL per line).
    Skips empty lines and comments (lines starting with #).
    
    Args:
        filepath: Path to the URL list file
    
    Returns:
        List of URLs
    """
    urls = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                # Add https:// if no protocol specified
                if not line.startswith(("http://", "https://")):
                    line = f"https://{line}"
                urls.append(line)
    return urls


async def async_main():
    """Async entry point — parses args and runs the crawl."""
    args = parse_args()

    # Set up logging level
    if args.verbose:
        logging.getLogger("crawler").setLevel(logging.DEBUG)

    # Determine URLs to crawl
    if args.url:
        urls = [args.url]
    else:
        urls = load_urls_from_file(args.file)
        logger.info(f"Loaded {len(urls)} URLs from {args.file}")

    # Apply max-sites limit
    if args.max_sites:
        urls = urls[:args.max_sites]
        logger.info(f"Limited to {len(urls)} sites (--max-sites)")

    # Run the crawl
    logger.info(f"Starting crawl of {len(urls)} site(s)")
    start_time = time.time()

    results = await crawl_sites(
        urls=urls,
        headless=args.headless,
        output_dir=args.output,
        proxy=args.proxy,
    )

    elapsed = time.time() - start_time
    success_count = sum(1 for r in results if r.get("status") == "success")
    ai_triggered = sum(1 for r in results if r.get("ai_detection", {}).get("triggered"))
    ai_confirmed = sum(1 for r in results if r.get("ai_network_confirmation", {}).get("ai_confirmed"))

    logger.info(f"\n{'=' * 60}")
    logger.info(f"CRAWL COMPLETE")
    logger.info(f"{'=' * 60}")
    logger.info(f"Total sites:        {len(urls)}")
    logger.info(f"Successful:         {success_count}")
    logger.info(f"Failed:             {len(urls) - success_count}")
    logger.info(f"AI triggered:       {ai_triggered}")
    logger.info(f"AI confirmed (net): {ai_confirmed}")
    logger.info(f"Time elapsed:       {elapsed:.1f}s")
    logger.info(f"Output dir:         {args.output or OUTPUT_DIR}")


def main():
    """Synchronous entry point (wraps async_main)."""
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
