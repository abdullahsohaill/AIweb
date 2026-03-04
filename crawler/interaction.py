"""
interaction.py — Human-Like Behavior Simulation + Consent Fallback
===================================================================

This module makes the crawler behave like a real human to avoid bot detection.
Bot detection systems (Cloudflare, Akamai, PerimeterX, etc.) look for:
- Perfectly straight mouse movements (humans move in curves)
- Instant scrolling (humans scroll gradually)
- No pauses (humans read and think)
- No random clicks (humans explore pages)

Our approach:
1. Bezier curves for mouse movement (non-linear, natural paths)
2. Gradual scrolling with random pauses (simulating reading)
3. Random clicks on non-navigational elements
4. Random delays between all actions
5. Consent/popup fallback dismissal (when Consent-O-Matic misses banners)

WHY BEZIER CURVES?
Real human mouse movements follow curved paths, not straight lines.
A cubic Bezier curve with randomized control points produces natural-looking
trajectories. We interpolate 20-40 points along the curve and move the mouse
to each one with small delays, creating smooth, human-like motion.
"""

import asyncio
import math
import random
import logging

from playwright.async_api import Page

from .utils import (
    MOUSE_MOVE_STEPS_MIN,
    MOUSE_MOVE_STEPS_MAX,
    SCROLL_INCREMENT_MIN,
    SCROLL_INCREMENT_MAX,
    PAUSE_MIN,
    PAUSE_MAX,
    MAX_SCROLL_STEPS,
    CONSENT_POPUP_REGEX,
    PERMISSION_DIALOG_REGEX,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    setup_logger,
)

logger = setup_logger("crawler.interaction")


# =============================================================================
# BEZIER CURVE MATH
# =============================================================================

def _bezier_point(t: float, p0: tuple, p1: tuple, p2: tuple, p3: tuple) -> tuple:
    """
    Calculate a point on a cubic Bezier curve at parameter t.
    
    WHY CUBIC BEZIER?
    A cubic Bezier curve is defined by 4 control points:
    - p0: start point (current mouse position)
    - p1: first control point (random offset — creates the curve shape)
    - p2: second control point (random offset — adds more curvature)
    - p3: end point (target element position)
    
    The curve naturally produces the kind of smooth, arcing motion
    that humans make when moving a mouse. Straight-line interpolation
    is a dead giveaway for bots.
    
    Args:
        t: Parameter from 0.0 (start) to 1.0 (end)
        p0-p3: Control points as (x, y) tuples
    
    Returns:
        (x, y) point on the curve at parameter t
    """
    # Cubic Bezier formula: B(t) = (1-t)^3*P0 + 3*(1-t)^2*t*P1 + 3*(1-t)*t^2*P2 + t^3*P3
    x = (
        (1 - t) ** 3 * p0[0]
        + 3 * (1 - t) ** 2 * t * p1[0]
        + 3 * (1 - t) * t ** 2 * p2[0]
        + t ** 3 * p3[0]
    )
    y = (
        (1 - t) ** 3 * p0[1]
        + 3 * (1 - t) ** 2 * t * p1[1]
        + 3 * (1 - t) * t ** 2 * p2[1]
        + t ** 3 * p3[1]
    )
    return (x, y)


def _generate_bezier_path(
    start: tuple, end: tuple, steps: int = None
) -> list[tuple]:
    """
    Generate a sequence of points along a Bezier curve from start to end.
    
    Control points are placed randomly to create natural-looking curves.
    The randomness in control point placement means each mouse movement
    follows a unique path — no two movements look the same.
    
    Args:
        start: (x, y) starting position
        end: (x, y) ending position
        steps: Number of interpolation points (more = smoother but slower)
    
    Returns:
        List of (x, y) tuples representing the mouse path
    """
    if steps is None:
        steps = random.randint(MOUSE_MOVE_STEPS_MIN, MOUSE_MOVE_STEPS_MAX)

    # Calculate the distance between start and end to scale control points.
    # Larger distances get wider curves; short distances get subtle curves.
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)

    # Control points are offset perpendicular to the line between start and end.
    # The offset magnitude is proportional to the distance (30-70% of distance).
    offset_scale = distance * random.uniform(0.3, 0.7)

    # Randomize control point positions for natural variation
    p1 = (
        start[0] + dx * random.uniform(0.2, 0.4) + random.uniform(-offset_scale, offset_scale) * 0.5,
        start[1] + dy * random.uniform(0.2, 0.4) + random.uniform(-offset_scale, offset_scale) * 0.5,
    )
    p2 = (
        start[0] + dx * random.uniform(0.6, 0.8) + random.uniform(-offset_scale, offset_scale) * 0.5,
        start[1] + dy * random.uniform(0.6, 0.8) + random.uniform(-offset_scale, offset_scale) * 0.5,
    )

    # Interpolate points along the Bezier curve
    path = []
    for i in range(steps + 1):
        t = i / steps
        point = _bezier_point(t, start, p1, p2, end)
        path.append(point)

    return path


# =============================================================================
# ELEMENT SELECTION
# =============================================================================

async def _get_random_visible_element(page: Page) -> dict | None:
    """
    Pick a random visible, non-navigational element on the page.
    
    WHY NON-NAVIGATIONAL?
    We want to click on harmless elements (paragraphs, headings, divs)
    to simulate casual browsing. Clicking links (<a>) or buttons would
    navigate away from the page or trigger unwanted actions.
    
    Returns:
        Dict with {x, y, tag} of the element, or None if no suitable elements.
    """
    try:
        # Use JavaScript to find all visible elements that are NOT links/buttons/forms.
        # We filter by visibility (offsetWidth > 0) and exclude interactive elements.
        elements = await page.evaluate("""
            () => {
                // Tags we want to AVOID clicking (would navigate or submit forms)
                const excludeTags = new Set([
                    'A', 'BUTTON', 'INPUT', 'SELECT', 'TEXTAREA', 'FORM',
                    'NAV', 'HEADER', 'FOOTER', 'IFRAME', 'VIDEO', 'AUDIO',
                    'SCRIPT', 'STYLE', 'LINK', 'META', 'SVG', 'CANVAS'
                ]);
                
                // Tags we DO want to interact with (safe, non-navigational)
                const includeTags = new Set([
                    'P', 'DIV', 'SPAN', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
                    'LI', 'TD', 'TH', 'SECTION', 'ARTICLE', 'MAIN'
                ]);
                
                const candidates = [];
                const allElements = document.querySelectorAll('*');
                
                for (const el of allElements) {
                    // Must be a safe tag
                    if (!includeTags.has(el.tagName)) continue;
                    
                    // Must be visible (has dimensions and is in viewport)
                    const rect = el.getBoundingClientRect();
                    if (rect.width === 0 || rect.height === 0) continue;
                    if (rect.top < 0 || rect.left < 0) continue;
                    if (rect.top > window.innerHeight || rect.left > window.innerWidth) continue;
                    
                    // USER REQUEST: DO NOT CLICK ON ANYTHING THAT MIGHT HAVE A HYPERLINK
                    // If an element or ANY of its descendants is an <a> tag, forms, or has an href, ABORT
                    if (el.hasAttribute('href') || el.closest('a') !== null || el.querySelector('a') !== null) continue;
                    
                    // Must have some text content (not empty divs)
                    if (el.innerText && el.innerText.trim().length > 0) {
                        candidates.push({
                            x: rect.x + rect.width / 2,
                            y: rect.y + rect.height / 2,
                            tag: el.tagName.toLowerCase()
                        });
                    }
                }
                
                return candidates;
            }
        """)

        if not elements:
            return None

        return random.choice(elements)

    except Exception as e:
        logger.debug(f"Could not get random element: {e}")
        return None


# =============================================================================
# HUMAN-LIKE MOUSE MOVEMENT
# =============================================================================

async def _move_mouse_human(page: Page, target_x: float, target_y: float) -> None:
    """
    Move the mouse to (target_x, target_y) along a Bezier curve.
    
    WHY NOT page.mouse.move()?
    Playwright's built-in mouse.move() goes in a straight line at constant speed.
    Bot detection systems flag this as non-human. Our Bezier approach creates
    curved, variable-speed paths that look natural.
    
    Args:
        page: Playwright page instance
        target_x: Target X coordinate
        target_y: Target Y coordinate
    """
    # Get current mouse position (default to center if unknown)
    try:
        current = await page.evaluate("() => ({x: window._mouseX || 0, y: window._mouseY || 0})")
        start_x, start_y = current.get("x", 0), current.get("y", 0)
    except Exception:
        start_x, start_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2

    # Generate the Bezier path
    path = _generate_bezier_path(
        start=(start_x, start_y),
        end=(target_x, target_y)
    )

    # Move along each point in the path with tiny delays.
    # The delays vary slightly to simulate human motor imprecision.
    for point in path:
        await page.mouse.move(point[0], point[1])
        # Micro-delay between movements (5-15ms) for realistic speed
        await asyncio.sleep(random.uniform(0.005, 0.015))

    # Track current position for next movement
    try:
        await page.evaluate(f"() => {{ window._mouseX = {target_x}; window._mouseY = {target_y}; }}")
    except Exception:
        pass


# =============================================================================
# HUMAN-LIKE SCROLLING (WITH SCROLL LIMIT)
# =============================================================================

async def _scroll_page_human(page: Page) -> None:
    """
    Scroll down to the bottom of the page and back up, simulating reading.
    
    WHY SCROLL?
    1. Many AI widgets are lazy-loaded and only appear after scrolling.
    2. Bot detectors check if the user interacts with the full page.
    3. Chatbot triggers sometimes fire on scroll events.
    
    WHY SCROLL LIMIT?
    Infinite-scroll pages (Reddit, Twitter/X, news feeds) will never reach
    scrollHeight — the page keeps growing. We cap at MAX_SCROLL_STEPS
    (default: 120 steps, ~24000-60000px of content) to prevent hanging.
    
    The scroll uses random increments and pauses to look natural.
    A real human doesn't scroll at constant speed — they pause to read,
    scroll fast past images, and slow down at text-heavy sections.
    """
    try:
        # Get the total scrollable height of the page
        scroll_height = await page.evaluate("() => document.body.scrollHeight")
        viewport_height = await page.evaluate("() => window.innerHeight")
        current_scroll = 0
        scroll_count = 0

        logger.debug(f"Scrolling page | total_height={scroll_height}px | max_steps={MAX_SCROLL_STEPS}")

        # --- Phase 1: Scroll DOWN ---
        while current_scroll < scroll_height - viewport_height:
            # SCROLL LIMIT: Prevent infinite-scroll pages from hanging the crawler
            if scroll_count >= MAX_SCROLL_STEPS:
                logger.info(f"Scroll limit reached ({MAX_SCROLL_STEPS} steps, scrolled {current_scroll}px)")
                break

            # Random scroll increment (simulates varying reading speed)
            increment = random.randint(SCROLL_INCREMENT_MIN, SCROLL_INCREMENT_MAX)
            current_scroll = min(current_scroll + increment, scroll_height - viewport_height)

            await page.evaluate(f"window.scrollTo(0, {current_scroll})")
            scroll_count += 1

            # Random pause between scrolls (simulates reading)
            await asyncio.sleep(random.uniform(0.3, 1.5))

            # Re-check scroll height — infinite-scroll pages increase it dynamically
            # WHY: On sites like Reddit, scrollHeight grows as you scroll.
            # We re-measure to detect this and enforce the scroll limit.
            new_scroll_height = await page.evaluate("() => document.body.scrollHeight")
            if new_scroll_height > scroll_height:
                logger.debug(f"Page height increased: {scroll_height} → {new_scroll_height}px (infinite scroll detected)")
                scroll_height = new_scroll_height

        logger.debug(f"Finished scrolling down | steps={scroll_count} | distance={current_scroll}px")

        # --- Phase 2: Scroll BACK UP ---
        # Scroll back up faster (humans often do this quicker)
        up_count = 0
        while current_scroll > 0:
            if up_count >= MAX_SCROLL_STEPS // 2:  # Up-scroll also capped
                current_scroll = 0
                await page.evaluate("window.scrollTo(0, 0)")
                break

            increment = random.randint(SCROLL_INCREMENT_MIN * 2, SCROLL_INCREMENT_MAX * 2)
            current_scroll = max(current_scroll - increment, 0)

            await page.evaluate(f"window.scrollTo(0, {current_scroll})")
            up_count += 1

            # Shorter pauses going up (humans scroll up faster)
            await asyncio.sleep(random.uniform(0.1, 0.5))

        logger.debug("Scrolled back to top")

    except Exception as e:
        logger.warning(f"Scroll simulation error: {e}")


# =============================================================================
# RANDOM CLICKS
# =============================================================================

async def _random_clicks(page: Page, num_clicks: int = 3) -> None:
    """
    Click on random non-navigational elements.
    
    WHY?
    1. Real users click around the page, even on non-interactive elements.
    2. Some chatbot widgets detect user engagement via click events.
    3. Bot detectors measure click patterns (zero clicks = suspicious).
    
    Args:
        page: Playwright page instance
        num_clicks: How many random clicks to perform
    """
    for i in range(num_clicks):
        element = await _get_random_visible_element(page)
        if element:
            # Move mouse to the element via Bezier curve, then click
            await _move_mouse_human(page, element["x"], element["y"])
            try:
                await page.mouse.click(element["x"], element["y"])
                logger.debug(f"Random click #{i+1} on <{element['tag']}> at ({element['x']:.0f}, {element['y']:.0f})")
            except Exception as e:
                logger.debug(f"Click failed: {e}")

        # Pause between clicks
        await asyncio.sleep(random.uniform(PAUSE_MIN, PAUSE_MAX))


# =============================================================================
# CONSENT/POPUP FALLBACK DISMISSAL
# =============================================================================

async def dismiss_consent_popups(page: Page) -> dict:
    """
    Try to dismiss any remaining cookie banners, consent popups, or 
    notification dialogs that Consent-O-Matic didn't handle.
    
    WHY A FALLBACK?
    Consent-O-Matic handles ~90% of cookie consent banners, but it misses:
    - Custom/homegrown consent implementations
    - Non-standard CMPs (Consent Management Platforms)
    - Region-specific dialogs (e.g., CCPA-style "Do Not Sell" banners)
    - Newsletter popups, notification permission dialogs
    - Age verification gates
    
    STRATEGY:
    1. Look for high-z-index overlays (modals/banners sit on top of content)
    2. Find buttons/links inside them that match accept/dismiss patterns
    3. Click the most likely "accept" or "dismiss" button
    4. Record what we dismissed for the crawl output
    
    Args:
        page: Playwright page instance
    
    Returns:
        Dict with dismissal results (popups_found, popups_dismissed, details)
    """
    result = {
        "popups_found": 0,
        "popups_dismissed": 0,
        "details": [],
    }

    try:
        # Find overlay/modal elements that might be consent banners
        popups = await page.evaluate("""
            () => {
                const results = [];
                const allElements = document.querySelectorAll('*');
                
                for (const el of allElements) {
                    const style = window.getComputedStyle(el);
                    const zIndex = parseInt(style.zIndex) || 0;
                    const position = style.position;
                    const rect = el.getBoundingClientRect();
                    
                    // Look for high-z-index fixed/absolute elements (overlays)
                    if ((position === 'fixed' || position === 'absolute') && 
                        zIndex > 100 && 
                        rect.width > 200 && rect.height > 50 &&
                        rect.width < window.innerWidth * 1.1) {
                        
                        // Look for buttons inside this overlay
                        const buttons = el.querySelectorAll('button, a, [role="button"], input[type="submit"]');
                        const buttonData = [];
                        
                        for (const btn of buttons) {
                            const btnRect = btn.getBoundingClientRect();
                            if (btnRect.width > 0 && btnRect.height > 0) {
                                buttonData.push({
                                    text: (btn.innerText || btn.value || btn.getAttribute('aria-label') || '').trim().substring(0, 100),
                                    tag: btn.tagName.toLowerCase(),
                                    x: btnRect.x + btnRect.width / 2,
                                    y: btnRect.y + btnRect.height / 2,
                                    id: btn.id || '',
                                    className: (btn.className || '').toString().substring(0, 100),
                                });
                            }
                        }
                        
                        if (buttonData.length > 0) {
                            results.push({
                                tag: el.tagName.toLowerCase(),
                                id: el.id || '',
                                className: (el.className || '').toString().substring(0, 100),
                                zIndex: zIndex,
                                width: rect.width,
                                height: rect.height,
                                buttons: buttonData,
                            });
                        }
                    }
                }
                
                return results;
            }
        """)

        result["popups_found"] = len(popups)

        # For each popup, try to find and click the "accept" or "dismiss" button
        for popup in popups:
            # Sort buttons: prefer "accept all" > "accept" > "agree" > "ok" > "close"
            accept_keywords = ["accept all", "accept", "allow all", "allow", "agree", 
                             "i agree", "got it", "ok", "okay", "continue", "proceed",
                             "i understand", "acknowledge"]
            dismiss_keywords = ["close", "dismiss", "x", "×", "✕", "✖"]
            
            best_button = None
            best_priority = 999

            for btn in popup["buttons"]:
                btn_text = btn["text"].lower().strip()
                
                # Check accept keywords (higher priority = click first)
                for i, keyword in enumerate(accept_keywords):
                    if keyword in btn_text:
                        if i < best_priority:
                            best_priority = i
                            best_button = btn
                        break
                
                # Check dismiss keywords (lower priority than accept)
                if best_button is None:
                    for keyword in dismiss_keywords:
                        if keyword == btn_text or btn_text == "":
                            best_button = btn
                            break

            if best_button:
                try:
                    await page.mouse.click(best_button["x"], best_button["y"])
                    result["popups_dismissed"] += 1
                    result["details"].append({
                        "popup_id": popup.get("id", ""),
                        "button_text": best_button["text"],
                        "action": "clicked",
                    })
                    logger.info(f"Dismissed popup: clicked '{best_button['text']}' in #{popup.get('id', 'unknown')}")
                    await asyncio.sleep(random.uniform(0.5, 1.5))
                except Exception as e:
                    logger.debug(f"Failed to click popup button: {e}")

    except Exception as e:
        logger.debug(f"Consent popup fallback failed: {e}")

    if result["popups_dismissed"] > 0:
        logger.info(f"Dismissed {result['popups_dismissed']}/{result['popups_found']} popups via fallback")
    
    return result


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

async def simulate_human_behavior(page: Page) -> dict:
    """
    Run the full human behavior simulation on a page.
    
    This is the main function called by the crawler after the page loads.
    It performs a sequence of human-like actions to:
    1. Avoid bot detection
    2. Trigger lazy-loaded content (including AI widgets)
    3. Generate realistic interaction patterns
    4. Dismiss any remaining cookie/consent popups
    
    The sequence:
    1. Initial pause (human would look at the page first)
    2. Dismiss any consent popups Consent-O-Matic missed
    3. Random mouse movements to various elements
    4. Scroll down to bottom (triggers lazy-loading, capped at MAX_SCROLL_STEPS)
    5. Random clicks on page content
    6. Scroll back to top
    7. Final pause
    
    Args:
        page: Playwright page instance (already navigated to a URL)
    
    Returns:
        Dict with interaction results including consent dismissal info
    """
    logger.info("Starting human behavior simulation")
    
    interaction_result = {
        "consent_fallback": {},
        "scroll_completed": False,
        "clicks_performed": 0,
    }

    try:
        # Step 1: Initial pause — a real human looks at the page before acting
        initial_pause = random.uniform(1.5, 3.0)
        logger.debug(f"Initial pause: {initial_pause:.1f}s")
        await asyncio.sleep(initial_pause)

        # Step 2: Try to dismiss consent popups that Consent-O-Matic missed
        # WHY HERE? We do this early so popups don't block the rest of our interaction.
        logger.debug("Checking for remaining consent popups")
        consent_result = await dismiss_consent_popups(page)
        interaction_result["consent_fallback"] = consent_result

        # Step 3: Move mouse to a few random elements (establishes mouse presence)
        logger.debug("Performing random mouse movements")
        for _ in range(random.randint(2, 4)):
            element = await _get_random_visible_element(page)
            if element:
                await _move_mouse_human(page, element["x"], element["y"])
                await asyncio.sleep(random.uniform(0.5, 1.5))

        # Step 4: Scroll down to the bottom and back up
        # Note: This is now capped at MAX_SCROLL_STEPS to prevent infinite-scroll hangs
        logger.debug("Starting scroll simulation")
        await _scroll_page_human(page)
        interaction_result["scroll_completed"] = True

        # Step 5: Random clicks on non-navigational elements
        num_clicks = random.randint(2, 5)
        logger.debug(f"Performing {num_clicks} random clicks")
        await _random_clicks(page, num_clicks=num_clicks)
        interaction_result["clicks_performed"] = num_clicks

        # Step 6: Second consent popup check (some popups appear after scrolling)
        consent_result_2 = await dismiss_consent_popups(page)
        if consent_result_2["popups_dismissed"] > 0:
            interaction_result["consent_fallback"]["popups_dismissed"] += consent_result_2["popups_dismissed"]
            interaction_result["consent_fallback"]["details"].extend(consent_result_2["details"])

        # Step 7: Final pause — human would review the page one more time
        final_pause = random.uniform(1.0, 2.0)
        logger.debug(f"Final pause: {final_pause:.1f}s")
        await asyncio.sleep(final_pause)

        logger.info("Human behavior simulation complete")

    except Exception as e:
        logger.error(f"Human behavior simulation failed: {e}")
        # Don't re-raise — the crawl should continue even if simulation fails

    return interaction_result
