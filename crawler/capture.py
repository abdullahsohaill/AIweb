"""
capture.py — Advanced Data Capture: Frames, Network, CDP Stack Traces
======================================================================

This is the MOST CRITICAL module in the crawler. It captures:

1. FRAME CONTENT (Main page + all iframes)
   - HTML source, inner text, frame URL, parent-child relationships
   - WHY: Chatbots often live inside iframes (Intercom, Drift, Tawk.to).
     If we only scrape the main frame, we miss them entirely.

2. NETWORK REQUESTS/RESPONSES
   - URL, method, headers, POST payload, response body
   - WHY: AI services communicate via HTTP APIs. Capturing the full
     request/response lets us see what data is sent to AI endpoints
     (user inputs, page content, PII, etc.)

3. CDP (Chrome DevTools Protocol) STACK TRACES
   - For each network request: which JS function, in which script file,
     at which line number, initiated the request
   - WHY: This is the KEY to our research. Standard Playwright logging
     tells us WHAT was sent, but not WHO sent it. The CDP initiator
     tells us exactly which script (e.g., intercom-widget.js:452)
     triggered an API call. This lets us trace AI API calls back to
     their source code and understand the integration architecture.

4. LOCAL STORAGE / COOKIES
   - WHY: AI services may store session data, user preferences, or
     tracking identifiers in local storage or cookies.
"""

import asyncio
import json
import logging
from typing import Any

from playwright.async_api import Page, Request, Response

from .utils import (
    MAX_RESPONSE_BODY_SIZE,
    setup_logger,
)

logger = setup_logger("crawler.capture")


# =============================================================================
# DATA CONTAINERS
# =============================================================================

class CaptureSession:
    """
    Holds all captured data for a single page visit.
    
    WHY a class instead of global lists?
    Each crawl visit creates its own CaptureSession, preventing data
    from mixing between sites. The session accumulates data as events
    fire (network requests, CDP events) and is collected at the end.
    """

    def __init__(self):
        # Network requests captured via Playwright's event system
        self.network_requests: list[dict] = []
        
        # CDP-level request data with initiator/stack trace information
        self.cdp_requests: list[dict] = []
        
        # Frame content (HTML, text) for main frame + all iframes
        self.frames: list[dict] = []
        
        # Storage data (cookies, localStorage)
        self.storage: dict = {"cookies": [], "local_storage": {}}

    def to_dict(self) -> dict:
        """Convert all captured data to a serializable dictionary."""
        return {
            "network_requests": self.network_requests,
            "cdp_requests": self.cdp_requests,
            "frames": self.frames,
            "storage": self.storage,
        }


# =============================================================================
# NETWORK MONITORING (Standard Playwright Events)
# =============================================================================

def setup_network_capture(page: Page, session: CaptureSession) -> None:
    """
    Set up Playwright event listeners to capture ALL network requests/responses.
    
    WHY BOTH request AND response handlers?
    - The request handler fires BEFORE the request is sent (captures intent)
    - The response handler fires AFTER we get a response (captures result)
    We match them by URL to build a complete picture of each API call.
    
    This captures the WHAT (what data was sent, what came back).
    For the WHO (which script initiated it), we need CDP (see below).
    
    Args:
        page: Playwright page instance
        session: CaptureSession to accumulate data into
    """

    async def on_request(request: Request) -> None:
        """
        Fired for every outgoing network request (XHR, fetch, script, etc.).
        We capture the request details for later analysis.
        """
        try:
            # Extract POST data (this is where AI prompts, user inputs, etc. live)
            post_data = None
            try:
                post_data = request.post_data
            except Exception:
                pass  # Some requests don't have post data

            request_data = {
                "url": request.url,
                "method": request.method,
                "headers": dict(request.headers) if request.headers else {},
                "post_data": post_data,
                "resource_type": request.resource_type,  # xhr, fetch, script, image, etc.
                "frame_url": request.frame.url if request.frame else None,
                "is_navigation": request.is_navigation_request(),
                # Response will be filled in by on_response
                "response": None,
            }

            session.network_requests.append(request_data)

        except Exception as e:
            logger.debug(f"Error capturing request: {e}")

    async def on_response(response: Response) -> None:
        """
        Fired for every response received. We match it to the corresponding
        request and store the response body (with size limits).
        
        WHY SIZE LIMITS?
        AI API responses are typically small JSON payloads (< 100KB).
        But pages also load images, videos, and other large assets.
        We cap the response body capture to avoid memory issues.
        """
        try:
            # Find the matching request in our list
            request_url = response.url
            matching = [r for r in session.network_requests if r["url"] == request_url and r["response"] is None]

            if not matching:
                return

            # Capture response body (with size limit)
            body = None
            try:
                # Only capture body for text-based responses (JSON, HTML, JS)
                # Skip binary content (images, videos, fonts)
                content_type = response.headers.get("content-type", "")
                is_text = any(t in content_type for t in [
                    "json", "text", "javascript", "xml", "html", "css"
                ])
                
                if is_text:
                    body_bytes = await response.body()
                    if len(body_bytes) <= MAX_RESPONSE_BODY_SIZE:
                        body = body_bytes.decode("utf-8", errors="replace")
                    else:
                        body = f"[TRUNCATED: {len(body_bytes)} bytes, limit={MAX_RESPONSE_BODY_SIZE}]"
            except Exception:
                body = "[ERROR: Could not read response body]"

            # Attach response data to the matching request
            matching[-1]["response"] = {
                "status": response.status,
                "status_text": response.status_text,
                "headers": dict(response.headers) if response.headers else {},
                "body": body,
            }

        except Exception as e:
            logger.debug(f"Error capturing response: {e}")

    # Register the event listeners on the page
    page.on("request", on_request)
    page.on("response", on_response)

    logger.info("Network capture listeners attached")


# =============================================================================
# CDP STACK TRACE CAPTURE (The Critical Part)
# =============================================================================

async def setup_cdp_capture(page: Page, cdp_client, session: CaptureSession) -> None:
    """
    Use Chrome DevTools Protocol to capture WHO initiated each network request.
    
    WHY CDP?
    Standard Playwright network events tell us:
    - WHAT URL was requested
    - WHAT data was sent/received
    
    But they DON'T tell us:
    - WHICH JavaScript file made the request
    - WHICH function in that file
    - WHICH line number
    
    The CDP `Network.requestWillBeSent` event includes an `initiator` field
    that contains the full call stack. This is EXACTLY what Chrome DevTools
    shows in the "Initiator" column of the Network tab.
    
    For our research, this is critical because:
    - We can trace "POST api.openai.com/v1/chat/completions" back to
      "chatbot-widget.js:line 452, function sendMessage()"
    - This reveals the integration architecture of AI services
    - We can identify first-party vs third-party AI integrations
    
    Args:
        page: Playwright page instance
        cdp_client: CDP session from browser.create_page()
        session: CaptureSession to accumulate data into
    """
    # Enable the Network domain — this makes CDP emit network events
    # Without this, we won't receive any Network.* events
    await cdp_client.send("Network.enable")

    # Enable the Debugger domain — this allows stack traces to include
    # resolved script URLs and line numbers (instead of just script IDs)
    await cdp_client.send("Debugger.enable")

    logger.info("CDP Network + Debugger domains enabled")

    def on_request_will_be_sent(params: dict) -> None:
        """
        CDP event handler for Network.requestWillBeSent.
        
        This fires BEFORE every network request. The `params` dict includes:
        - requestId: Unique ID for this request
        - request: {url, method, headers, postData}
        - initiator: THE GOLD — contains type and call stack
        - type: Document, XHR, Fetch, Script, etc.
        
        The `initiator` field structure:
        {
            "type": "script" | "parser" | "other",
            "url": "https://...",  // URL of the initiating script
            "stack": {
                "callFrames": [
                    {
                        "functionName": "sendMessage",
                        "scriptId": "42",
                        "url": "https://cdn.chatbot.com/widget.js",
                        "lineNumber": 451,
                        "columnNumber": 12
                    },
                    ...  // Full call stack (most recent first)
                ]
            }
        }
        """
        try:
            request_info = params.get("request", {})
            initiator = params.get("initiator", {})

            # Extract stack trace frames (if available)
            stack_frames = []
            stack = initiator.get("stack")
            if stack:
                for frame in stack.get("callFrames", []):
                    stack_frames.append({
                        "function_name": frame.get("functionName", ""),
                        "script_url": frame.get("url", ""),
                        "line_number": frame.get("lineNumber", -1),
                        "column_number": frame.get("columnNumber", -1),
                    })

                # CDP events can have parent stacks (async call chains).
                # These show the FULL async trace, e.g.:
                # setTimeout -> fetch callback -> API call
                parent = stack.get("parent")
                while parent:
                    for frame in parent.get("callFrames", []):
                        stack_frames.append({
                            "function_name": frame.get("functionName", ""),
                            "script_url": frame.get("url", ""),
                            "line_number": frame.get("lineNumber", -1),
                            "column_number": frame.get("columnNumber", -1),
                            "is_async": True,  # Mark as async parent frame
                        })
                    parent = parent.get("parent")

            cdp_entry = {
                "request_id": params.get("requestId"),
                "url": request_info.get("url", ""),
                "method": request_info.get("method", ""),
                "resource_type": params.get("type", ""),
                "post_data": request_info.get("postData"),
                "headers": dict(request_info.get("headers", {})),
                # The initiator — this is what makes CDP capture special
                "initiator": {
                    "type": initiator.get("type", "unknown"),
                    "url": initiator.get("url", ""),
                    "stack_trace": stack_frames,
                },
                "frame_id": params.get("frameId", ""),
                "timestamp": params.get("timestamp"),
                # Redirect info (if this request is a redirect)
                "redirect_url": params.get("redirectResponse", {}).get("url") if params.get("redirectResponse") else None,
            }

            session.cdp_requests.append(cdp_entry)

        except Exception as e:
            logger.debug(f"Error in CDP request handler: {e}")

    # Register the CDP event listener
    cdp_client.on("Network.requestWillBeSent", on_request_will_be_sent)

    logger.info("CDP stack trace capture attached")


# =============================================================================
# FRAME CONTENT CAPTURE
# =============================================================================

async def capture_all_frames(page: Page, session: CaptureSession) -> None:
    """
    Capture content from the main frame AND all iframes.
    
    WHY ITERATE FRAMES?
    Chatbots almost ALWAYS live inside iframes:
    - Intercom: creates an iframe for the chat widget
    - Drift: injects an iframe with the conversation UI
    - Tawk.to: loads the entire chat in an embedded iframe
    - Custom bots: often hosted on a different domain in an iframe
    
    If we only capture `page.content()`, we miss ALL of this.
    We must iterate through `page.frames` to get every frame's content.
    
    IMPORTANT: Frames can be detached (removed from DOM) at any time,
    especially dynamic ones. We wrap each capture in try/except to handle this.
    
    Args:
        page: Playwright page instance
        session: CaptureSession to store frame data
    """
    logger.info(f"Capturing frames | total_frames={len(page.frames)}")

    for i, frame in enumerate(page.frames):
        frame_data = {
            "index": i,
            "url": frame.url,
            "name": frame.name,
            "is_main": frame == page.main_frame,
            "parent_url": frame.parent_frame.url if frame.parent_frame else None,
            "html": None,
            "inner_text": None,
            "is_detached": False,
        }

        try:
            # Capture the full HTML source of this frame.
            # This includes injected scripts, dynamically added elements, etc.
            frame_data["html"] = await frame.content()

        except Exception as e:
            # Frame may have been detached (removed from DOM) or navigated away
            frame_data["html"] = f"[ERROR: {e}]"
            frame_data["is_detached"] = True
            logger.debug(f"Frame {i} HTML capture failed (likely detached): {e}")

        try:
            # Capture the visible text content (what a human would see).
            # This is useful for keyword analysis and sentiment detection.
            frame_data["inner_text"] = await frame.inner_text("body")

        except Exception as e:
            frame_data["inner_text"] = f"[ERROR: {e}]"
            logger.debug(f"Frame {i} text capture failed: {e}")

        # --- Capture JavaScript file URLs loaded in this frame ---
        try:
            scripts = await frame.evaluate("""
                () => {
                    const scripts = document.querySelectorAll('script[src]');
                    return Array.from(scripts).map(s => s.src);
                }
            """)
            frame_data["script_urls"] = scripts
        except Exception as e:
            frame_data["script_urls"] = []
            logger.debug(f"Frame {i} script URL capture failed: {e}")

        session.frames.append(frame_data)

    logger.info(f"Captured {len(session.frames)} frames")


# =============================================================================
# STORAGE CAPTURE (Cookies + Local Storage)
# =============================================================================

async def capture_storage(page: Page, session: CaptureSession) -> None:
    """
    Capture cookies and localStorage for the current page.
    
    WHY?
    AI services often store:
    - Session tokens (to maintain chat state across page loads)
    - User identifiers (for analytics/tracking)
    - Conversation history (some chatbots persist chats in localStorage)
    - Configuration (widget settings, A/B test flags)
    
    This data is relevant for privacy analysis — we want to know
    what AI services are storing on the user's machine.
    
    Args:
        page: Playwright page instance
        session: CaptureSession to store data
    """
    # --- Cookies ---
    try:
        cookies = await page.context.cookies()
        session.storage["cookies"] = [
            {
                "name": c.get("name"),
                "value": c.get("value"),
                "domain": c.get("domain"),
                "path": c.get("path"),
                "expires": c.get("expires"),
                "httpOnly": c.get("httpOnly"),
                "secure": c.get("secure"),
                "sameSite": c.get("sameSite"),
            }
            for c in cookies
        ]
        logger.info(f"Captured {len(cookies)} cookies")
    except Exception as e:
        logger.warning(f"Cookie capture failed: {e}")

    # --- Local Storage ---
    try:
        local_storage = await page.evaluate("""
            () => {
                const data = {};
                for (let i = 0; i < localStorage.length; i++) {
                    const key = localStorage.key(i);
                    try {
                        data[key] = localStorage.getItem(key);
                    } catch (e) {
                        data[key] = '[ERROR: ' + e.message + ']';
                    }
                }
                return data;
            }
        """)
        session.storage["local_storage"] = local_storage
        logger.info(f"Captured {len(local_storage)} localStorage entries")
    except Exception as e:
        logger.warning(f"localStorage capture failed: {e}")

    # --- Session Storage ---
    try:
        session_storage = await page.evaluate("""
            () => {
                const data = {};
                for (let i = 0; i < sessionStorage.length; i++) {
                    const key = sessionStorage.key(i);
                    try {
                        data[key] = sessionStorage.getItem(key);
                    } catch (e) {
                        data[key] = '[ERROR: ' + e.message + ']';
                    }
                }
                return data;
            }
        """)
        session.storage["session_storage"] = session_storage
        logger.info(f"Captured {len(session_storage)} sessionStorage entries")
    except Exception as e:
        logger.warning(f"sessionStorage capture failed: {e}")


# =============================================================================
# DYNAMIC FRAME RE-CAPTURE (Post-AI Invocation)
# =============================================================================

async def capture_frames_dynamic(page: Page, session: CaptureSession) -> int:
    """
    Re-capture frames that were injected AFTER the initial frame capture.
    
    WHY: During AI invocation (clicking chatbot buttons, typing prompts),
    new iframes are often injected dynamically:
    - Intercom injects a conversation iframe after clicking the launcher
    - Drift loads its chat iframe only when the widget opens
    - Custom chatbots may create new iframes for the conversation view
    
    If we only capture frames once (before AI invocation), we miss all
    the chatbot iframe content. This function captures any NEW frames
    that appeared since the last capture.
    
    Args:
        page: Playwright page instance
        session: CaptureSession to append new frames to
    
    Returns:
        Number of new frames captured
    """
    # Track which frame URLs we already captured
    existing_urls = {f["url"] for f in session.frames}
    new_count = 0

    for i, frame in enumerate(page.frames):
        if frame.url in existing_urls:
            continue  # Already captured

        frame_data = {
            "index": len(session.frames),
            "url": frame.url,
            "name": frame.name,
            "is_main": frame == page.main_frame,
            "parent_url": frame.parent_frame.url if frame.parent_frame else None,
            "html": None,
            "inner_text": None,
            "is_detached": False,
            "captured_phase": "post_ai_invocation",  # Mark as late capture
        }

        try:
            frame_data["html"] = await frame.content()
        except Exception as e:
            frame_data["html"] = f"[ERROR: {e}]"
            frame_data["is_detached"] = True

        try:
            frame_data["inner_text"] = await frame.inner_text("body")
        except Exception as e:
            frame_data["inner_text"] = f"[ERROR: {e}]"

        try:
            scripts = await frame.evaluate("""
                () => {
                    const scripts = document.querySelectorAll('script[src]');
                    return Array.from(scripts).map(s => s.src);
                }
            """)
            frame_data["script_urls"] = scripts
        except Exception:
            frame_data["script_urls"] = []

        session.frames.append(frame_data)
        new_count += 1

    if new_count > 0:
        logger.info(f"Dynamic re-capture found {new_count} new frames (post-AI invocation)")

    return new_count


# =============================================================================
# PERMISSION REQUEST TRACKING
# =============================================================================

async def capture_permission_state(page: Page) -> list[dict]:
    """
    Check what permissions the site has requested or been granted.
    
    WHY: AI services often request permissions (microphone, camera, geolocation,
    notifications) that reveal their capabilities and privacy implications.
    We auto-grant all permissions during crawling, but we want to RECORD
    which ones were requested — this is valuable for privacy analysis.
    
    Args:
        page: Playwright page instance
    
    Returns:
        List of permission states [{name, state}]
    """
    try:
        permissions = await page.evaluate("""
            async () => {
                const permissionNames = [
                    'geolocation', 'notifications', 'camera', 'microphone',
                    'clipboard-read', 'clipboard-write'
                ];
                const results = [];
                
                for (const name of permissionNames) {
                    try {
                        const status = await navigator.permissions.query({ name: name });
                        results.push({
                            name: name,
                            state: status.state,  // 'granted', 'denied', 'prompt'
                        });
                    } catch (e) {
                        results.push({
                            name: name,
                            state: 'unsupported',
                        });
                    }
                }
                
                return results;
            }
        """)
        logger.info(f"Captured {len(permissions)} permission states")
        return permissions
    except Exception as e:
        logger.debug(f"Permission state capture failed: {e}")
        return []


# =============================================================================
# CONVENIENCE: FULL CAPTURE PIPELINE
# =============================================================================

async def run_full_capture(page: Page, cdp_client, session: CaptureSession) -> None:
    """
    Run the complete capture pipeline: frames + storage + permissions.
    
    Network and CDP captures are already running via event listeners
    (set up during page creation). This function captures the "snapshot"
    data that we collect at a specific point in time.
    
    Call this AFTER human simulation and AI invocation are done,
    so we capture the final state of the page (including any
    AI chat widgets that were opened, conversations that happened, etc.)
    
    Args:
        page: Playwright page instance
        cdp_client: CDP session (for future expansion)
        session: CaptureSession to accumulate data into
    """
    logger.info("Running full capture pipeline")

    # Capture all frame content (main + iframes)
    await capture_all_frames(page, session)

    # Capture storage (cookies, localStorage, sessionStorage)
    await capture_storage(page, session)

    # Give a moment for any final network requests to complete
    # (some AI widgets send analytics pings when the page state changes)
    await asyncio.sleep(2)

    logger.info(
        f"Capture complete | "
        f"frames={len(session.frames)} | "
        f"network_requests={len(session.network_requests)} | "
        f"cdp_requests={len(session.cdp_requests)} | "
        f"cookies={len(session.storage.get('cookies', []))}"  
    )
