"""
browser.py — Browser Launch, Stealth, and Extension Loading
============================================================

This module handles all browser-level configuration:
- Launching Chromium with TWO-TIER strategy:
  1. Persistent context (for extensions) — requires specific OS permissions
  2. Regular browser launch (fallback) — no extensions but always works
- Applying stealth measures to avoid bot detection
- Setting timeouts (30s page load, 2min interaction)
- Granting permissions for microphone/camera (needed to trigger voice/vision AI)

WHY TWO-TIER LAUNCH?
Extensions (like Consent-O-Matic) only work with `launch_persistent_context`.
However, on some macOS setups, Chromium can't create the ProcessSingleton
socket directory needed for persistent contexts. In that case, we fall back
to regular `browser.launch()` + `browser.new_context()` — everything works
EXCEPT extensions. The consent popup fallback in interaction.py compensates.
"""

import os
import logging
import random
import tempfile
import time
from pathlib import Path

from playwright.async_api import async_playwright, BrowserContext, Page

# playwright-stealth patches the browser to remove automation fingerprints
# (e.g., navigator.webdriver=true, missing plugins, etc.)
# This is optional — if not installed, we fall back to basic stealth flags.
try:
    from playwright_stealth import stealth_async
    HAS_STEALTH = True
except ImportError:
    HAS_STEALTH = False
    stealth_async = None  # Will use manual stealth flags instead

from .utils import (
    PAGE_LOAD_TIMEOUT_MS,
    INTERACTION_TIMEOUT_MS,
    EXTENSION_PATH,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_X,
    WINDOW_Y,
    setup_logger,
)

logger = setup_logger("crawler.browser")

# Module-level reference to the browser instance so close_browser() can clean up.
_browser_instance = None


def _get_chrome_args(with_extension: bool = False) -> list[str]:
    """Build Chrome launch arguments."""
    chrome_args = [
        # Window positioning — keep visible but out of the way
        f"--window-position={WINDOW_X},{WINDOW_Y}",
        f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}",
        # Fake media stream for voice AI (Vapi, Hume, etc.)
        "--use-fake-ui-for-media-stream",
        "--use-fake-device-for-media-stream",
        # Stealth + usability
        "--disable-crash-reporter",
        "--disable-blink-features=AutomationControlled",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-popup-blocking",
        "--disable-infobars",
        "--disable-quic",  # HTTP/3 causes net::ERR_QUIC_PROTOCOL_ERROR on certain sites like Wonderchat
    ]

    # Extension loading (only for persistent context mode)
    if with_extension:
        ext_path = os.path.abspath(EXTENSION_PATH)
        if os.path.isdir(ext_path):
            chrome_args.extend([
                f"--disable-extensions-except={ext_path}",
                f"--load-extension={ext_path}",
            ])
            logger.info(f"Loading extension: Consent-O-Matic from {ext_path}")
        else:
            logger.warning(
                f"Extension path not found: {ext_path}. "
                "Consent-O-Matic will NOT be loaded."
            )

    return chrome_args


async def launch_browser(
    playwright,
    headless: bool = False,
    load_extension: bool = True,
    user_data_dir: str = None,
    proxy: str = None,
) -> BrowserContext:
    """
    Launch a Chromium browser with stealth and extensions (if possible).
    
    TWO-TIER STRATEGY:
    1. Try launch_persistent_context (supports extensions)
    2. Fall back to browser.launch() + new_context() (no extensions, always works)
    
    On macOS, persistent context often fails due to ProcessSingleton socket
    directory permission issues. The fallback ensures the crawler always works,
    and the consent popup fallback in interaction.py compensates for the
    missing Consent-O-Matic extension.
    
    Args:
        playwright: Playwright instance (from async_playwright().start())
        headless: If True, run headless (extensions won't work). Default: False.
        load_extension: If True, attempt to load Consent-O-Matic.
        user_data_dir: Chrome user data directory. If None, uses a temp dir.
    
    Returns:
        BrowserContext ready for crawling.
    """
    global _browser_instance

    proxy_dict = {"server": proxy} if proxy else None

    # --- Tier 1: Try persistent context (with extensions) ---
    # HEADLESS MODE NOTE: Persistent contexts often fail headlessly on macOS.
    # We skip to Tier 2 if the user explicitly requests headless.
    if not headless and load_extension:
        try:
            if user_data_dir is None:
                user_data_dir = tempfile.mkdtemp(prefix="crawler_profile_")

            chrome_args = _get_chrome_args(with_extension=True)
            
            context = await playwright.chromium.launch_persistent_context(
                user_data_dir=user_data_dir,
                headless=False,
                args=chrome_args,
                proxy=proxy_dict,
                viewport={"width": WINDOW_WIDTH, "height": WINDOW_HEIGHT},
                permissions=["microphone", "camera", "geolocation", "notifications"],
                accept_downloads=True,
                locale="en-US",
                timezone_id="America/New_York",
                ignore_https_errors=True,
            )

            context.set_default_navigation_timeout(PAGE_LOAD_TIMEOUT_MS)
            context.set_default_timeout(INTERACTION_TIMEOUT_MS)

            logger.info(
                f"Browser launched (persistent context) | headed=True | "
                f"extensions=YES | profile={user_data_dir}"
            )
            return context

        except Exception as e:
            logger.warning(
                f"Persistent context failed: {e}. "
                "Falling back to regular launch (no extensions)."
            )

    # --- Tier 2: Fallback to regular browser.launch() ---
    # For HEADED mode: use channel='chrome' (system-installed Chrome).
    # WHY? Playwright's bundled Chromium is blocked by macOS ProcessSingleton
    # restrictions. The user's real Chrome app already has macOS permissions
    # (Full Disk Access, etc.) so it can create socket directories.
    # For HEADLESS mode: use bundled chromium (always works, no GUI needed).
    chrome_args = _get_chrome_args(with_extension=False)

    launch_kwargs = {
        "headless": headless,
        "args": chrome_args,
    }
    if proxy_dict:
        launch_kwargs["proxy"] = proxy_dict

    # Playwright's headless launch tries to create artifacts in /var/folders/
    # which fails due to macOS SIP. Force it to use our local tmp dir instead.
    launch_kwargs = {
        "headless": headless,
        "args": chrome_args,
    }
    if proxy_dict:
        launch_kwargs["proxy"] = proxy_dict

    browser = await playwright.chromium.launch(**launch_kwargs)
    _browser_instance = browser

    context = await browser.new_context(
        viewport={"width": WINDOW_WIDTH, "height": WINDOW_HEIGHT},
        permissions=["microphone", "camera", "geolocation", "notifications"],
        accept_downloads=True,
        locale="en-US",
        timezone_id="America/New_York",
        ignore_https_errors=True,
    )

    context.set_default_navigation_timeout(PAGE_LOAD_TIMEOUT_MS)
    context.set_default_timeout(INTERACTION_TIMEOUT_MS)

    if HAS_STEALTH and stealth_async:
        # Patch the first page that is automatically created by a persistent context
        if context.pages:
            await stealth_async(context.pages[0])

    logger.info(
        f"Browser launched (regular mode) | headed={not headless} | "
        f"channel={'chrome' if not headless else 'chromium'} | "
        f"extensions=NO (consent fallback active) | "
        f"page_timeout={PAGE_LOAD_TIMEOUT_MS}ms"
    )

    return context


async def create_page(context: BrowserContext) -> tuple[Page, object]:
    """
    Create a new page (tab) and attach a CDP session for advanced monitoring.
    
    WHY CDP?
    Standard Playwright events (page.on('request')) give us basic info.
    But we NEED the Chrome DevTools Protocol (CDP) to capture:
    - Stack traces: which JS function/script initiated each network request
    - Initiator info: was the request from a script, parser, or user action?
    This is CRITICAL for our research — we need to trace AI API calls back
    to the specific JavaScript code that triggered them.
    
    Args:
        context: The browser context from launch_browser()
    
    Returns:
        Tuple of (page, cdp_client) where cdp_client is a CDPSession
    """
    page = await context.new_page()

    # Apply stealth patches (if playwright-stealth is installed)
    if HAS_STEALTH:
        await stealth_async(page)
        logger.info("Applied playwright-stealth patches")
    else:
        logger.debug("playwright-stealth not installed — using basic stealth flags")

    # Create a CDP session for stack trace capture
    cdp_client = await context.new_cdp_session(page)
    logger.info("New page created with stealth and CDP session attached")

    return page, cdp_client


async def close_browser(context: BrowserContext) -> None:
    """
    Gracefully close the browser context (and browser if applicable).
    
    Args:
        context: The browser context to close
    """
    global _browser_instance
    try:
        await context.close()
        logger.info("Browser context closed")
    except Exception as e:
        logger.error(f"Error closing context: {e}")

    # If we used regular launch mode, also close the browser
    if _browser_instance:
        try:
            await _browser_instance.close()
            logger.info("Browser instance closed")
        except Exception as e:
            logger.error(f"Error closing browser: {e}")
        _browser_instance = None
