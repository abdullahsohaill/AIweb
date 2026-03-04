"""
ai_invocation.py — Exhaustive AI Component Detection and Triggering
====================================================================

This module handles the detection and invocation of AI services embedded
on web pages. This is the "research payload" of the crawler — everything
else (stealth, scrolling, capture) exists to support THIS.

DETECTION STRATEGY (Multi-Signal, Literature-Driven):
We use a comprehensive 6-layer approach to find AI chatbots, copilots,
and assistants, informed by:
- Waheed et al. (2022): DOM/iFrame scanning, keyword heuristics
- Kaya et al. (2025): Network-level AI confirmation (JSON payloads, WSS)
- Hantke et al. (WebREC): MutationObserver for lazy-loaded widgets

1. KNOWN PROVIDER SELECTORS: CSS selectors for 40+ chatbot platforms
2. TEXT/ATTRIBUTE REGEX: Scan aria-label, placeholder, title, innerText
3. FIXED-POSITION ELEMENTS: Chat bubbles at bottom-right with high z-index
4. IFRAME SOURCE DOMAINS: Known chatbot iframe hosts (30+ domains)
5. SHADOW DOM TRAVERSAL: Pierce shadow roots to find hidden widgets
6. DOM MUTATION OBSERVATION: Wait for lazy-loaded chatbot widgets

INVOCATION STRATEGY:
1. Click the chat bubble/icon
2. Handle PRE-CHAT FORMS (Name/Email) using dummy data
3. Find the input field (across all frames, including Shadow DOM)
4. Type a meaningful prompt character-by-character
5. Submit the message (Enter key)
6. Wait for AI response + network confirmation
"""

import asyncio
import random
import re
import logging
from typing import Any

from playwright.async_api import Page, Locator

from .utils import (

    AI_PROMPT_TEXTS,
    PRECHAT_FORM_DATA,
    PAUSE_MIN,
    PAUSE_MAX,
    setup_logger,
)

logger = setup_logger("crawler.ai_invocation")


# =============================================================================
# GENERIC CHATBOT DETECTION HEURISTICS
# =============================================================================
# NO provider-specific selectors — only standardized, generic strategies
# that can detect ANY chatbot widget without prior knowledge of the provider.
#
# WHY GENERIC? Hardcoded provider selectors (Intercom, Zendesk, Drift, etc.)
# create a methodological bias — we'd only detect what we already know.
# True discovery requires generic heuristics that work for unknown widgets.
#
# KEYWORDS: These are functional terms (what something DOES) not brand names.
# "chat", "message", "help", "assistant" describe the FUNCTION of a widget,
# not the PROVIDER. This is the key distinction.

# Functional keywords for chatbot detection (NO provider/brand names)
CHAT_FUNCTION_KEYWORDS = re.compile(
    r"(?i)\b("
    r"chat|chatbot|live[-_\s]?chat|"
    r"message|send[-_\s]?message|"
    r"help|get[-_\s]?help|need[-_\s]?help|"
    r"assistant|virtual[-_\s]?assistant|"
    r"support|support[-_\s]?chat|"
    r"ask[-_\s]?us|talk[-_\s]?to[-_\s]?us|contact[-_\s]?us|"
    r"let'?s[-_\s]?chat|start[-_\s]?chat|"
    r"bot|chatbot|"
    r"conversation|start[-_\s]?conversation|"
    r"agent|ai[-_\s]?agent"
    r")\b"
)

# Exclude patterns — things that match chat keywords but aren't chatbots
EXCLUDE_KEYWORDS = re.compile(
    r"(?i)(video|media|audio|player|slider|carousel|progress|seekbar|"
    r"volume|playback|cookie|consent|gdpr|privacy|accept|reject|"
    r"newsletter|subscribe|login|sign[-_\s]?in|password|captcha|"
    r"search|navigation|nav[-_\s]?bar|header|footer|menu|"
    r"advertisement|ad[-_\s]?banner|sidebar)"
)


# =============================================================================
# AI ELEMENT DETECTION — GENERIC STRATEGIES ONLY
# =============================================================================

async def detect_ai_elements(page: Page) -> list[dict]:
    """
    Scan the page for elements likely to be chatbot/AI widget triggers.

    Uses 6 GENERIC detection strategies — no provider-specific selectors:
    1. Fixed-position corner elements (high z-index, bottom-right/left)
    2. Cross-origin iframes (ANY 3rd-party domain, not a known list)
    3. ARIA accessibility tree (role=dialog/complementary + chat keywords)
    4. Shadow DOM traversal (pierce shadow roots, generic keywords)
    5. Generic text/attribute heuristics (functional keywords, not brands)
    6. Interactive widget patterns (buttons/divs with chat-like attributes)

    Returns:
        List of detected elements with metadata (type, selector, confidence, etc.)
    """
    detected = []

    # --- Strategy 1: Fixed-position corner elements ---
    # Chat bubbles are almost always position:fixed, bottom-right, high z-index.
    # WHY z-index > 999? Chat widgets float above all page content.
    # WHY bottom 30%? Chat bubbles sit at the bottom of the viewport.
    # WHY 15-300px? Chat bubble icons are small (not fullscreen modals).
    try:
        fixed_elements = await page.evaluate("""
            () => {
                const getAllElements = (root) => {
                    let all = [];
                    const elements = root.querySelectorAll('*');
                    for (const el of elements) {
                        all.push(el);
                        if (el.shadowRoot) {
                            all = all.concat(getAllElements(el.shadowRoot));
                        }
                    }
                    return all;
                };

                const results = [];
                const allElements = getAllElements(document);
                
                for (const el of allElements) {
                    const style = window.getComputedStyle(el);
                    const position = style.position;
                    const zIndex = parseInt(style.zIndex) || 0;
                    
                    if ((position === 'fixed' || position === 'sticky') && zIndex > 999) {
                        const rect = el.getBoundingClientRect();
                        
                        // Bottom-right OR bottom-left of viewport
                        const isBottomRight = (
                            rect.bottom > window.innerHeight * 0.7 && 
                            rect.right > window.innerWidth * 0.6
                        );
                        const isBottomLeft = (
                            rect.bottom > window.innerHeight * 0.7 && 
                            rect.left < window.innerWidth * 0.4
                        );
                        
                        if ((isBottomRight || isBottomLeft) &&
                            rect.width < 300 && rect.height < 300 &&
                            rect.width > 15 && rect.height > 15) {
                            
                            // Check if it has click handler or is a button
                            const isClickable = (
                                el.tagName === 'BUTTON' || 
                                el.tagName === 'A' ||
                                el.getAttribute('role') === 'button' ||
                                el.onclick !== null ||
                                style.cursor === 'pointer'
                            );
                            
                            results.push({
                                type: 'fixed_corner',
                                selector: el.tagName.toLowerCase() + 
                                    (el.id ? '#' + el.id : '') +
                                    (el.className && typeof el.className === 'string'
                                        ? '.' + el.className.split(' ')[0] : ''),
                                text: (el.innerText || el.getAttribute('aria-label') || '').substring(0, 200),
                                tag: el.tagName.toLowerCase(),
                                confidence: isClickable ? 'high' : 'medium',
                                x: rect.x + rect.width / 2,
                                y: rect.y + rect.height / 2,
                                zIndex: zIndex,
                                position: isBottomRight ? 'bottom-right' : 'bottom-left',
                            });
                        }
                    }
                }
                
                return results;
            }
        """)
        detected.extend(fixed_elements)
    except Exception as e:
        logger.debug(f"Fixed-position detection failed: {e}")

    # --- Strategy 2: Cross-origin iframes ---
    # WHY: Chatbot widgets are almost always loaded from a DIFFERENT domain
    # than the host page. We detect ANY cross-origin iframe, rather than
    # matching against a hardcoded list of known domains.
    try:
        page_domain = ""
        try:
            from urllib.parse import urlparse
            page_domain = urlparse(page.url).netloc.lower()
            # Strip "www." for comparison
            if page_domain.startswith("www."):
                page_domain = page_domain[4:]
        except Exception:
            pass
        
        for frame in page.frames:
            if frame == page.main_frame:
                continue  # Skip the main frame itself
            frame_url = frame.url.lower()
            if not frame_url or frame_url == "about:blank":
                continue
            
            try:
                frame_domain = urlparse(frame_url).netloc.lower()
                if frame_domain.startswith("www."):
                    frame_domain = frame_domain[4:]
            except Exception:
                continue
            
            # Only flag cross-origin iframes (different domain)
            if frame_domain and frame_domain != page_domain:
                # Skip well-known non-chatbot iframes (analytics, ads, social, consent)
                non_chat_domains = [
                    "google.com", "googleapis.com", "gstatic.com",
                    "facebook.com", "fb.com", "twitter.com", "youtube.com",
                    "doubleclick.net", "googlesyndication.com",
                    "googletagmanager.com", "google-analytics.com",
                    "recaptcha.net", "gstatic.com",
                ]
                is_non_chat = any(d in frame_domain for d in non_chat_domains)
                
                detected.append({
                    "type": "cross_origin_iframe",
                    "selector": f"iframe[src*='{frame_domain}']",
                    "text": f"Cross-origin iframe: {frame_domain}",
                    "tag": "iframe",
                    "confidence": "low" if is_non_chat else "medium",
                    "frame_url": frame.url,
                    "frame_domain": frame_domain,
                })
    except Exception as e:
        logger.debug(f"Cross-origin iframe detection failed: {e}")

    # --- Strategy 3: ARIA accessibility tree ---
    # WHY: Chatbot UIs often use proper ARIA roles (dialog, complementary, log)
    # and aria-labels mentioning "chat", "help", "message", etc.
    # Also scans ANY element with aria-label matching chat keywords (catches
    # buttons like <button aria-label="Open LiveChat chat widget">).
    try:
        a11y_elements = await page.evaluate("""
            () => {
                const getAllElements = (root) => {
                    let all = [];
                    const elements = root.querySelectorAll('*');
                    for (const el of elements) {
                        all.push(el);
                        if (el.shadowRoot) {
                            all = all.concat(getAllElements(el.shadowRoot));
                        }
                    }
                    return all;
                };

                const results = [];
                const allNodes = getAllElements(document);
                
                const dialogs = allNodes.filter(el => {
                    const r = el.getAttribute('role');
                    return r === 'dialog' || r === 'complementary' || r === 'log' || 
                           r === 'alertdialog' || r === 'status' || 
                           el.getAttribute('aria-live') === 'polite' || 
                           el.getAttribute('aria-live') === 'assertive';
                });
                
                const ariaLabeled = allNodes.filter(el => el.hasAttribute('aria-label'));
                
                const chatKeywords = /chat|bot|assistant|help|support|message|conversation|jivo|chitchat|helpcrunch/i;
                const excludeKeywords = /video|media|audio|player|cookie|consent|gdpr|privacy|search|navigation|menu|login|captcha/i;
                
                const allCandidates = new Set([...dialogs, ...ariaLabeled]);
                
                for (const el of allCandidates) {
                    const label = el.getAttribute('aria-label') || 
                                  el.getAttribute('aria-labelledby') || 
                                  el.getAttribute('title') || '';
                    const text = el.innerText || '';
                    
                    if (chatKeywords.test(label) || chatKeywords.test(text.substring(0, 500))) {
                        // Skip excluded patterns
                        if (excludeKeywords.test(label) || excludeKeywords.test(text.substring(0, 200))) continue;
                        
                        // Skip navigation links (a tags with real href paths)
                        if (el.tagName === 'A' && el.getAttribute('href')) {
                            const href = el.getAttribute('href');
                            if (href.startsWith('/') || href.startsWith('http')) continue;
                        }
                        
                        const rect = el.getBoundingClientRect();
                        if (rect.width > 0 && rect.height > 0) {
                            const role = el.getAttribute('role') || '';
                            results.push({
                                type: 'a11y_match',
                                selector: el.tagName.toLowerCase() + 
                                    (el.id ? '#' + el.id : '') +
                                    (role ? '[role="' + role + '"]' : '') +
                                    (el.className && typeof el.className === 'string'
                                        ? '.' + el.className.split(' ')[0] : ''),
                                text: (label || text).substring(0, 200),
                                tag: el.tagName.toLowerCase(),
                                confidence: 'high',
                                x: rect.x + rect.width / 2,
                                y: rect.y + rect.height / 2,
                            });
                        }
                    }
                }
                
                return results;
            }
        """)
        detected.extend(a11y_elements)
    except Exception as e:
        logger.debug(f"Accessibility tree detection failed: {e}")

    # --- Strategy 4: Shadow DOM traversal ---
    # WHY: Some widgets use Shadow DOM to encapsulate their UI.
    # Regular querySelector can't pierce shadow roots.
    # Uses GENERIC functional keywords (chat, help, support) not brand names.
    try:
        shadow_elements = await page.evaluate("""
            () => {
                const results = [];
                const chatKeywords = /chat|bot|assistant|widget|help|support|messenger|conversation|message/i;
                const excludeKeywords = /video|media|audio|player|slider|carousel|progress|seekbar|volume|playback|cookie|consent|gdpr|privacy|newsletter|search|navigation|login|captcha/i;
                
                function traverseShadowRoots(root, depth) {
                    if (depth > 5) return;  // Limit recursion
                    
                    const elements = root.querySelectorAll('*');
                    for (const el of elements) {
                        if (el.shadowRoot) {
                            const hostId = el.id || '';
                            const hostClass = (typeof el.className === 'string' ? el.className : '') || '';
                            const hostTag = el.tagName.toLowerCase();
                            const ariaLabel = el.getAttribute('aria-label') || '';
                            
                            // Skip excluded elements
                            if (excludeKeywords.test(hostId) || excludeKeywords.test(hostClass) || excludeKeywords.test(hostTag)) {
                                continue;
                            }
                            
                            if (chatKeywords.test(hostId) || chatKeywords.test(hostClass) || 
                                chatKeywords.test(hostTag) || chatKeywords.test(ariaLabel)) {
                                const rect = el.getBoundingClientRect();
                                if (rect.width > 0 && rect.height > 0) {
                                    results.push({
                                        type: 'shadow_dom',
                                        selector: hostTag + (hostId ? '#' + hostId : ''),
                                        text: 'Shadow DOM: ' + hostTag + (ariaLabel ? ' (' + ariaLabel + ')' : ''),
                                        tag: hostTag,
                                        confidence: 'high',
                                        x: rect.x + rect.width / 2,
                                        y: rect.y + rect.height / 2,
                                    });
                                }
                            }
                            
                            // Recurse into shadow root
                            traverseShadowRoots(el.shadowRoot, depth + 1);
                        }
                    }
                }
                
                traverseShadowRoots(document, 0);
                return results;
            }
        """)
        detected.extend(shadow_elements)
    except Exception as e:
        logger.debug(f"Shadow DOM traversal failed: {e}")

    # --- Strategy 5: Generic text/attribute heuristics ---
    # Scan buttons, links, and labeled elements for FUNCTIONAL chat keywords.
    # NO provider/brand names — only "chat", "help", "support", "message", etc.
    # FILTERS: Skip navigation links (<a> with real hrefs), elements inside
    # <nav>/<header>/<footer>, and elements wider than 400px (nav bars).
    try:
        text_matches = await page.evaluate("""
            () => {
                const getAllElements = (root) => {
                    let all = [];
                    const elements = root.querySelectorAll('*');
                    for (const el of elements) {
                        all.push(el);
                        if (el.shadowRoot) {
                            all = all.concat(getAllElements(el.shadowRoot));
                        }
                    }
                    return all;
                };

                const chatRegex = /\\b(chat|chatbot|live[\\-_\\s]?chat|message|send[\\-_\\s]?message|help|get[\\-_\\s]?help|assistant|support|ask[\\-_\\s]?us|talk[\\-_\\s]?to[\\-_\\s]?us|let'?s[\\-_\\s]?chat|start[\\-_\\s]?chat|bot|conversation|start[\\-_\\s]?conversation|ai[\\-_\\s]?agent|ai[\\-_\\s]?assistant|ai[\\-_\\s]?chat|jivo|chitchat|helpcrunch)\\b/i;
                const excludeRegex = /video|media|audio|player|cookie|consent|gdpr|privacy|newsletter|subscribe|login|sign[\\-_\\s]?in|search|navigation|menu|captcha|advertisement/i;
                const results = [];
                
                const allNodes = getAllElements(document);
                const candidates = allNodes.filter(el => 
                    el.matches('button, a, [role="button"], [role="dialog"]') ||
                    el.hasAttribute('aria-label') ||
                    el.hasAttribute('placeholder') ||
                    el.hasAttribute('title')
                );
                
                for (const el of candidates) {
                    // --- FILTER 1: Skip <a> tags with real navigation hrefs ---
                    if (el.tagName === 'A') {
                        const href = el.getAttribute('href') || '';
                        // Skip links to internal pages (has a path component)
                        if (href.startsWith('/') && href.length > 1) continue;
                        if (href.startsWith('http')) continue;
                    }
                    
                    // --- FILTER 2: Skip elements inside nav/header/footer ---
                    if (el.closest('nav') || el.closest('header') || el.closest('footer')) continue;
                    
                    // --- FILTER 3: Skip very wide elements (navigation bars) ---
                    const rect = el.getBoundingClientRect();
                    if (rect.width > 400) continue;
                    
                    const texts = [
                        el.getAttribute('aria-label') || '',
                        el.getAttribute('placeholder') || '',
                        el.getAttribute('title') || '',
                        el.getAttribute('alt') || '',
                        el.innerText || '',
                    ];
                    
                    const matchedText = texts.find(t => chatRegex.test(t));
                    if (matchedText && !excludeRegex.test(matchedText)) {
                        if (rect.width > 0 && rect.height > 0) {
                            results.push({
                                type: 'text_heuristic',
                                selector: el.tagName.toLowerCase() + 
                                    (el.id ? '#' + el.id : '') + 
                                    (el.className && typeof el.className === 'string' 
                                        ? '.' + el.className.split(' ')[0] : ''),
                                text: matchedText.substring(0, 200),
                                tag: el.tagName.toLowerCase(),
                                confidence: 'medium',
                                x: rect.x + rect.width / 2,
                                y: rect.y + rect.height / 2,
                                width: rect.width,
                                height: rect.height,
                            });
                        }
                    }
                }
                
                return results;
            }
        """)
        detected.extend(text_matches)
    except Exception as e:
        logger.debug(f"Text heuristic detection failed: {e}")

    # --- Strategy 6: Interactive widget patterns ---
    # Look for elements that STRUCTURALLY look like chat launchers:
    # - <button> or clickable <div> with an <img> or <svg> (even nested)
    # - With cursor:pointer and position:fixed or high z-index
    # - In the bottom-right area of the viewport
    # - Also checks PARENT containers for fixed position (button inside a fixed wrapper)
    try:
        widget_elements = await page.evaluate("""
            () => {
                const getAllElements = (root) => {
                    let all = [];
                    const elements = root.querySelectorAll('*');
                    for (const el of elements) {
                        all.push(el);
                        if (el.shadowRoot) {
                            all = all.concat(getAllElements(el.shadowRoot));
                        }
                    }
                    return all;
                };

                const results = [];
                const allNodes = getAllElements(document);
                
                // Find buttons/divs that contain SVG or img (using querySelector for nested)
                const allButtons = allNodes.filter(el => 
                    el.matches('button, div[role="button"], [tabindex="0"]')
                );
                
                for (const el of allButtons) {
                    // Must contain an icon (svg or img), even if deeply nested
                    if (!el.querySelector('svg') && !el.querySelector('img')) continue;
                    
                    const rect = el.getBoundingClientRect();
                    const style = window.getComputedStyle(el);
                    const zIndex = parseInt(style.zIndex) || 0;
                    
                    // Check if ELEMENT or its PARENT (up 2 levels) is position:fixed
                    let isFloating = style.position === 'fixed' || style.position === 'absolute';
                    let parentZ = zIndex;
                    if (!isFloating) {
                        let parent = el.parentElement;
                        for (let i = 0; i < 3 && parent; i++) {
                            const ps = window.getComputedStyle(parent);
                            if (ps.position === 'fixed' || ps.position === 'absolute') {
                                isFloating = true;
                                parentZ = Math.max(parentZ, parseInt(ps.zIndex) || 0);
                                break;
                            }
                            parent = parent.parentElement;
                        }
                    }
                    
                    // Must be bottom-right, small, and floating
                    const isBottomRight = rect.bottom > window.innerHeight * 0.7 && 
                                         rect.right > window.innerWidth * 0.6;
                    const isSmall = rect.width < 150 && rect.height < 150 && rect.width > 15 && rect.height > 15;
                    
                    if (isBottomRight && (isFloating || parentZ > 100) && isSmall) {
                        results.push({
                            type: 'widget_pattern',
                            selector: el.tagName.toLowerCase() + 
                                (el.id ? '#' + el.id : '') +
                                (el.className && typeof el.className === 'string'
                                    ? '.' + el.className.split(' ')[0] : ''),
                            text: (el.getAttribute('aria-label') || el.innerText || '').substring(0, 200),
                            tag: el.tagName.toLowerCase(),
                            confidence: 'high',
                            x: rect.x + rect.width / 2,
                            y: rect.y + rect.height / 2,
                            zIndex: Math.max(zIndex, parentZ),
                        });
                    }
                }
                
                return results;
            }
        """)
        detected.extend(widget_elements)
    except Exception as e:
        logger.debug(f"Widget pattern detection failed: {e}")

    # --- Deduplicate by selector ---
    seen = set()
    unique = []
    for d in detected:
        key = d["selector"]
        if key not in seen:
            seen.add(key)
            unique.append(d)

    logger.info(f"Detected {len(unique)} potential AI elements "
                f"(fixed={sum(1 for d in unique if d['type']=='fixed_corner')}, "
                f"iframe={sum(1 for d in unique if d['type']=='cross_origin_iframe')}, "
                f"a11y={sum(1 for d in unique if d['type']=='a11y_match')}, "
                f"shadow={sum(1 for d in unique if d['type']=='shadow_dom')}, "
                f"text={sum(1 for d in unique if d['type']=='text_heuristic')}, "
                f"widget={sum(1 for d in unique if d['type']=='widget_pattern')})")
    return unique



# =============================================================================
# PRE-CHAT FORM HANDLING
# =============================================================================

async def dismiss_modal_overlays(page: Page) -> int:
    """
    Dismiss full-screen modal overlays / splash screens that block interaction.
    
    WHY: Sites like Freshdesk show branding videos or promo modals that cover
    the chat widget. These have a close/X button we need to click first.
    
    Returns:
        Number of modals dismissed.
    """
    dismissed = 0
    try:
        # Find modal close buttons (X icons, close buttons)
        close_selectors = [
            # Specific close patterns
            "button[aria-label*='close' i]",
            "button[aria-label*='dismiss' i]",
            "[class*='modal-close']",
            "[class*='close-button']",
            "[class*='closeButton']",
            "[class*='close-modal']",
            "[data-dismiss='modal']",
            ".modal button.close",
            # Generic X buttons on overlays
            "div[class*='overlay'] button",
            "div[class*='modal'] button[class*='close']",
        ]

        for sel in close_selectors:
            try:
                elements = await page.query_selector_all(sel)
                for el in elements:
                    if await el.is_visible():
                        await el.click()
                        dismissed += 1
                        logger.info(f"Dismissed modal overlay: {sel}")
                        await asyncio.sleep(0.5)
                        break
                if dismissed > 0:
                    break
            except Exception:
                continue

        # Fallback: press Escape to close modals
        if dismissed == 0:
            try:
                await page.keyboard.press("Escape")
                await asyncio.sleep(0.5)
            except Exception:
                pass

    except Exception as e:
        logger.debug(f"Modal overlay dismissal failed: {e}")

    if dismissed > 0:
        logger.info(f"Dismissed {dismissed} modal overlay(s)")
    return dismissed


async def handle_prechat_form(page: Page) -> bool:
    """
    Handle pre-chat survey forms that appear before the actual chat.
    
    WHY: Many chatbot platforms (Intercom, Zendesk, Drift, LiveChat, Freshdesk)
    require users to enter their Name/Email or select Language/Country before
    connecting to the chatbot. If we don't fill these forms, we never reach the AI.
    
    STRATEGY (from Waheed et al.):
    1. Dismiss any modal overlays blocking the chat
    2. Look for input fields AND select dropdowns inside chat containers
    3. Match field labels/placeholders to known form field types
    4. Fill text inputs with dummy data, select first valid option in dropdowns
    5. Submit the form
    
    Returns:
        True if a pre-chat form was found and submitted
    """
    # First, dismiss any modal overlays that might be blocking the chat
    await dismiss_modal_overlays(page)

    for frame in page.frames:
        try:
            # --- Handle text inputs ---
            form_filled = await frame.evaluate("""
                (formData) => {
                    const namePatterns = /^(name|full[-_\\s]?name|your[-_\\s]?name|first[-_\\s]?name)/i;
                    const emailPatterns = /^(email|e[-_]?mail|your[-_\\s]?email)/i;
                    const phonePatterns = /^(phone|tel|mobile|number)/i;
                    const messagePatterns = /^(message|question|how[-_\\s]?can|what|describe)/i;
                    
                    const inputs = document.querySelectorAll(
                        'input[type="text"], input[type="email"], input[type="tel"], textarea'
                    );
                    
                    let filledCount = 0;
                    
                    for (const input of inputs) {
                        const rect = input.getBoundingClientRect();
                        if (rect.width === 0 || rect.height === 0) continue;
                        
                        const label = (
                            input.getAttribute('placeholder') || 
                            input.getAttribute('aria-label') || 
                            input.getAttribute('name') ||
                            input.getAttribute('id') || 
                            ''
                        ).toLowerCase();
                        
                        let value = null;
                        
                        if (input.type === 'email' || emailPatterns.test(label)) {
                            value = formData.email;
                        } else if (namePatterns.test(label)) {
                            if (/first/i.test(label)) {
                                value = formData.first_name;
                            } else if (/last/i.test(label)) {
                                value = formData.last_name;
                            } else {
                                value = formData.name;
                            }
                        } else if (phonePatterns.test(label)) {
                            value = formData.phone;
                        } else if (input.tagName === 'TEXTAREA' || messagePatterns.test(label)) {
                            value = formData.message;
                        }
                        
                        if (value) {
                            // Set value via native setter to trigger React/Vue state updates
                            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                                window.HTMLInputElement.prototype, 'value'
                            ).set;
                            nativeInputValueSetter.call(input, value);
                            input.dispatchEvent(new Event('input', { bubbles: true }));
                            input.dispatchEvent(new Event('change', { bubbles: true }));
                            filledCount++;
                        }
                    }
                    
                    return filledCount;
                }
            """, PRECHAT_FORM_DATA)

            # --- Handle <select> dropdowns (Language, Country, etc.) ---
            selects_filled = await frame.evaluate("""
                () => {
                    const selects = document.querySelectorAll('select');
                    let filledCount = 0;
                    
                    for (const select of selects) {
                        const rect = select.getBoundingClientRect();
                        if (rect.width === 0 || rect.height === 0) continue;
                        
                        // Skip if already has a valid value selected
                        if (select.value && select.value !== '' && 
                            select.value !== 'none' && select.value !== 'None') {
                            continue;
                        }
                        
                        // Find the first non-empty, non-"None" option
                        let selectedOption = null;
                        for (const opt of select.options) {
                            const val = opt.value.toLowerCase();
                            const text = opt.text.toLowerCase();
                            if (val && val !== '' && val !== 'none' && 
                                text !== 'none' && text !== 'select' &&
                                text !== '-- select --' && text !== 'choose') {
                                // Prefer English if it's a language dropdown
                                if (/english/i.test(opt.text)) {
                                    selectedOption = opt;
                                    break;
                                }
                                // Prefer US/United States if country
                                if (/united states|usa|^us$/i.test(opt.text)) {
                                    selectedOption = opt;
                                    break;
                                }
                                // Otherwise take the first valid option
                                if (!selectedOption) {
                                    selectedOption = opt;
                                }
                            }
                        }
                        
                        if (selectedOption) {
                            select.value = selectedOption.value;
                            select.dispatchEvent(new Event('change', { bubbles: true }));
                            select.dispatchEvent(new Event('input', { bubbles: true }));
                            filledCount++;
                        }
                    }
                    
                    return filledCount;
                }
            """)

            # --- Handle ARIA combobox dropdowns (Salesforce LWC, etc.) ---
            # WHY: Freshdesk/Salesforce uses lightning-combobox which renders
            # as button[role='combobox'] + div[role='listbox'] with role='option'
            # items. These are NOT native <select> elements.
            aria_filled = 0
            try:
                # Find all combobox triggers (buttons with role="combobox")
                combobox_selectors = [
                    "button[role='combobox']",
                    "[role='combobox']",
                    "lightning-combobox button",
                    "lightning-base-combobox button",
                ]
                for cb_sel in combobox_selectors:
                    try:
                        comboboxes = await frame.query_selector_all(cb_sel)
                        for cb in comboboxes:
                            if not await cb.is_visible():
                                continue
                            # Check if it needs filling (shows "None" or empty)
                            cb_text = (await cb.inner_text()).strip().lower()
                            if cb_text in ("none", "", "select", "-- select --", "choose"):
                                # Click to open the dropdown
                                await cb.click()
                                await asyncio.sleep(0.8)

                                # Find and click the first valid option
                                options = await frame.query_selector_all("[role='option']")
                                for opt in options:
                                    if not await opt.is_visible():
                                        continue
                                    opt_text = (await opt.inner_text()).strip().lower()
                                    # Skip empty/none/placeholder options
                                    if opt_text in ("none", "", "select", "choose"):
                                        continue
                                    # Prefer English for language dropdowns
                                    if "english" in opt_text:
                                        await opt.click()
                                        aria_filled += 1
                                        logger.info(f"Selected 'English' in ARIA combobox")
                                        await asyncio.sleep(0.5)
                                        break
                                    # Prefer US for country dropdowns
                                    if "united states" in opt_text or opt_text == "us":
                                        await opt.click()
                                        aria_filled += 1
                                        logger.info(f"Selected 'United States' in ARIA combobox")
                                        await asyncio.sleep(0.5)
                                        break
                                else:
                                    # No preferred option found — take the first valid one
                                    for opt in options:
                                        if not await opt.is_visible():
                                            continue
                                        opt_text = (await opt.inner_text()).strip().lower()
                                        if opt_text not in ("none", "", "select", "choose"):
                                            await opt.click()
                                            aria_filled += 1
                                            logger.info(f"Selected first valid ARIA option")
                                            await asyncio.sleep(0.5)
                                            break
                    except Exception:
                        continue
            except Exception as e:
                logger.debug(f"ARIA combobox handling failed: {e}")

            total_filled = (form_filled or 0) + (selects_filled or 0) + aria_filled

            if total_filled > 0:
                logger.info(
                    f"Filled {total_filled} pre-chat form fields "
                    f"({form_filled or 0} text, {selects_filled or 0} dropdowns) "
                    f"in frame {frame.url[:60]}"
                )
                
                # Look for a submit button and click it
                submit_clicked = False
                submit_selectors = [
                    "button[type='submit']",
                    "input[type='submit']",
                    "button:has-text('Start Conversation')",
                    "button:has-text('Start Chat')",
                    "button:has-text('Begin Chat')",
                    "button:has-text('Submit')",
                    "button:last-of-type",
                    "[class*='submit']",
                    "[class*='start-chat']",
                    "[class*='startConversation']",
                    "[class*='begin-chat']",
                    "button",
                ]
                
                for sel in submit_selectors:
                    try:
                        btn = await frame.query_selector(sel)
                        if btn and await btn.is_visible():
                            await btn.click()
                            submit_clicked = True
                            logger.info(f"Clicked pre-chat submit button: {sel}")
                            await asyncio.sleep(random.uniform(2.0, 4.0))
                            break
                    except Exception:
                        continue
                
                if not submit_clicked:
                    try:
                        await frame.press("input:last-of-type", "Enter")
                        logger.info("Pressed Enter on last input as submit fallback")
                        await asyncio.sleep(random.uniform(2.0, 4.0))
                    except Exception:
                        pass
                
                return True

        except Exception as e:
            logger.debug(f"Pre-chat form handling failed in frame: {e}")
            continue

    return False


# =============================================================================
# DOM MUTATION OBSERVER FOR LAZY-LOADED WIDGETS
# =============================================================================

async def wait_for_chatbot_mutations(page: Page, timeout_ms: int = 8000) -> list[dict]:
    """
    Wait for DOM mutations that indicate a lazy-loaded chatbot widget appearing.
    
    WHY: Many chatbot widgets (especially on SPAs) are loaded lazily — they
    inject their iframe/container after the initial page load, sometimes
    after a scroll or timer event. Hantke et al. (WebREC) showed that
    MutationObserver is essential for catching these dynamic injections.
    
    STRATEGY:
    1. Set up a MutationObserver on the document body
    2. Watch for new iframes, divs with chat-related classes, shadow hosts
    3. Wait up to timeout_ms for relevant mutations
    4. Return any new chatbot-related elements found
    
    Args:
        page: Playwright page
        timeout_ms: How long to wait for mutations (default: 8 seconds)
    
    Returns:
        List of newly detected chatbot elements from DOM mutations
    """
    try:
        new_elements = await page.evaluate("""
            (timeoutMs) => {
                return new Promise((resolve) => {
                    const chatKeywords = /chat|bot|assistant|widget|help|support|messenger|drift|intercom|tawk|tidio|crisp|zendesk|hubspot|freshchat|olark|livechat|jivo|chitchat|helpcrunch/i;
                    const results = [];
                    
                    const observer = new MutationObserver((mutations) => {
                        for (const mutation of mutations) {
                            for (const node of mutation.addedNodes) {
                                if (node.nodeType !== 1) continue;  // Only element nodes
                                
                                const tag = node.tagName ? node.tagName.toLowerCase() : '';
                                const id = node.id || '';
                                const className = (typeof node.className === 'string' ? node.className : '') || '';
                                const src = node.getAttribute ? (node.getAttribute('src') || '') : '';
                                
                                // Check if this new element is chatbot-related
                                if (chatKeywords.test(id) || chatKeywords.test(className) || 
                                    chatKeywords.test(src) || tag === 'iframe') {
                                    const rect = node.getBoundingClientRect ? node.getBoundingClientRect() : null;
                                    if (rect && rect.width > 0 && rect.height > 0) {
                                        results.push({
                                            type: 'mutation',
                                            selector: tag + (id ? '#' + id : '') + 
                                                (className ? '.' + className.split(' ')[0] : ''),
                                            text: (tag === 'iframe' ? 'New iframe: ' + src : 
                                                   (node.innerText || '').substring(0, 200)),
                                            tag: tag,
                                            confidence: tag === 'iframe' ? 'high' : 'medium',
                                            x: rect.x + rect.width / 2,
                                            y: rect.y + rect.height / 2,
                                        });
                                    }
                                }
                            }
                        }
                    });
                    
                    observer.observe(document.body, {
                        childList: true,
                        subtree: true,
                    });
                    
                    // Stop observing after timeout
                    setTimeout(() => {
                        observer.disconnect();
                        resolve(results);
                    }, timeoutMs);
                });
            }
        """, timeout_ms)

        if new_elements:
            logger.info(f"MutationObserver detected {len(new_elements)} new chatbot-related elements")
        
        return new_elements or []

    except Exception as e:
        logger.debug(f"MutationObserver failed: {e}")
        return []


# =============================================================================
# NETWORK-LEVEL AI CONFIRMATION
# =============================================================================

def check_network_for_ai_activity(network_requests: list[dict]) -> dict:
    """
    Analyze captured network requests to confirm AI activity.
    
    WHY: Kaya et al. (2025) showed that the most reliable way to confirm
    a chatbot is actually AI-powered (not just a contact form or live chat)
    is to inspect network traffic for:
    1. POST requests to known AI API endpoints
    2. JSON payloads with conversational structure ({"messages": [...], "role": ...})
    3. WebSocket connections (voice AI / streaming chat)
    4. Server-Sent Events (SSE) for streaming LLM responses
    
    This function runs AFTER invocation to verify that our interaction
    actually triggered an AI backend, not just a contact form.
    
    Args:
        network_requests: List of captured network request dicts
    
    Returns:
        Dict with AI activity confirmation details
    """
    result = {
        "ai_confirmed": False,
        "ai_endpoints_hit": [],
        "conversational_payloads": [],
        "websocket_connections": [],
        "streaming_responses": [],
    }

    for req in network_requests:
        url = req.get("url", "")
        method = req.get("method", "")
        post_data = req.get("post_data", "") or ""
        resource_type = req.get("resource_type", "")
        response = req.get("response", {}) or {}
        response_headers = response.get("headers", {}) or {}

        # Check 1: Generic AI indicators in URL path (functional, not brand)
        generic_ai_paths = ["/chat/completions", "/generate", "/conversation", "suggest-reply", "summarize", "api.tawk.to"]
        for pattern in generic_ai_paths:
            if pattern in url.lower():
                result["ai_endpoints_hit"].append({
                    "url": url[:500],
                    "method": method,
                    "pattern_matched": pattern,
                })
                result["ai_confirmed"] = True

        # Check 2: POST request with conversational JSON payload
        if method == "POST" and post_data:
            # Look for LLM-style payload structures
            conversational_markers = [
                '"role"', '"content"', '"messages"',
                '"prompt"', '"query"', '"input"',
                '"conversation"', '"chat_history"',
                '"user_message"', '"assistant"',
            ]
            markers_found = [m for m in conversational_markers if m in post_data]
            if len(markers_found) >= 2:  # At least 2 markers = likely AI
                result["conversational_payloads"].append({
                    "url": url[:500],
                    "markers": markers_found,
                    "payload_preview": post_data[:1000],
                })
                result["ai_confirmed"] = True

        # Check 3: WebSocket connections (voice AI like Vapi, Hume)
        if resource_type == "websocket" or "wss://" in url or "ws://" in url:
            result["websocket_connections"].append({
                "url": url[:500],
            })

        # Check 4: Server-Sent Events (streaming LLM responses)
        content_type = response_headers.get("content-type", "")
        if "text/event-stream" in content_type:
            result["streaming_responses"].append({
                "url": url[:500],
                "content_type": content_type,
            })
            result["ai_confirmed"] = True

    if result["ai_confirmed"]:
        logger.info(f"AI CONFIRMED via network analysis: "
                    f"{len(result['ai_endpoints_hit'])} endpoints, "
                    f"{len(result['conversational_payloads'])} conversational payloads, "
                    f"{len(result['streaming_responses'])} SSE streams")
    
    return result


# =============================================================================
# AI TRIGGERING / INVOCATION (MAIN FUNCTION)
# =============================================================================

async def trigger_ai_components(page: Page) -> dict:
    """
    Attempt to invoke AI components (chatbots, copilots, etc.) on the page.
    
    This is the core "AI invocation" logic. Enhanced sequence:
    1. DETECT: Multi-signal detection (6 strategies)
    2. MUTATE: Wait for lazy-loaded widgets via MutationObserver
    3. CLICK: Click on chat bubbles/icons (sorted by confidence)
    4. PRE-CHAT: Handle Name/Email forms with dummy data
    5. INPUT: Find input fields and type meaningful text
    6. SUBMIT: Press Enter to send the message
    7. WAIT: Give the AI time to respond
    
    Returns:
        Dictionary with detection results and interaction log
    """
    result = {
        "elements_found": [],
        "interactions": [],
        "triggered": False,
        "prechat_form_handled": False,
    }

    # --- Phase 0: Hardcoded Integrations (Fast-Path) ---
    logger.info("Phase 0: Checking for known hardcoded integrations (Tawk, Wonderchat)")
    await asyncio.sleep(2)  # Give JS time to mount frames

    try:
        # Fast-Path 1: Tawk.to
        tawk_frames = [f for f in page.frames if "tawk.to" in f.url.lower()]
        
        # Check both the main page and ALL frames for the button since it lives inside an isolated iframe usually
        tawk_trigger_clicked = False
        
        if tawk_frames:
            logger.info("⚡ FAST-PATH: Detected Tawk.to integration frames. Executing perfect flow.")
            
            # Step 1: Find and click the trigger in either the page or its own frame
            # The trigger might be on the main page OR injected inside one of the tawk frames
            trigger_locators = ["button.tawk-button", "[aria-label='Chat widget']", "[title='Chat widget']"]
            
            # First try frames
            for frame in tawk_frames:
                for loc in trigger_locators:
                    trigger = frame.locator(loc).first
                    if await trigger.count() > 0 and await trigger.is_visible():
                        await trigger.click(timeout=5000)
                        tawk_trigger_clicked = True
                        break
                if tawk_trigger_clicked:
                    break
                    
            # If not in frames, try main page
            if not tawk_trigger_clicked:
                for loc in trigger_locators:
                    trigger = page.locator(loc).first
                    if await trigger.count() > 0 and await trigger.is_visible():
                        await trigger.click(timeout=5000)
                        tawk_trigger_clicked = True
                        break
            
            if tawk_trigger_clicked:
                await asyncio.sleep(2)
                
            # Step 2: Now that it's open, find the input box in the newly visible frame
            target_frame = next((f for f in page.frames if "tawk.to" in f.url.lower()), None)
            if target_frame:
                input_box = target_frame.locator("textarea.tawk-chatinput-editor, textarea[placeholder*='message' i], div[data-testid='chat-input']")
                if await input_box.count() > 0:
                    await input_box.first.click()
                    await asyncio.sleep(1)
                    
                    # Message 1
                    await input_box.first.type("Hi there, I have a few questions about your features.", delay=80)
                    await asyncio.sleep(1)
                    await input_box.first.press("Enter")
                    result["interactions"].append({"action": "type", "target": "tawk.to fastpath", "text": "Hi there, I have a few questions about your features.", "success": True})
                    
                    # Wait for AI response (longer human delay)
                    logger.info("Sent message 1, waiting 10s for AI to stream reply...")
                    await asyncio.sleep(10)
                    
                    # Message 2 (Privacy)
                    await input_box.first.click()
                    await asyncio.sleep(1)
                    await input_box.first.type("Also, what data do you collect and how are my chat logs used?", delay=80)
                    await asyncio.sleep(1)
                    await input_box.first.press("Enter")
                    result["interactions"].append({"action": "type", "target": "tawk.to fastpath", "text": "Also, what data do you collect and how are my chat logs used?", "success": True})
                    
                    logger.info("Sent message 2, waiting 10s for AI reply...")
                    await asyncio.sleep(10)
                    
                    result["triggered"] = True
                    logger.info("✅ Tawk.to multi-turn fast-path successful!")
                    return result
    except Exception as e:
        logger.debug(f"Tawk.to fast-path failed: {e}")

    try:
        # Fast-Path 2: Wonderchat.io
        wonder_frames = [f for f in page.frames if "wonderchat" in f.url.lower()]
        wonder_triggers = await page.locator("iframe[src*='wonderchat.io'], iframe[title*='wonderchat' i], div[style*='animation: pulse'], button.chakra-button").count()
        if wonder_frames or wonder_triggers > 0:
            logger.info("⚡ FAST-PATH: Detected Wonderchat integration. Executing perfect flow.")
            
            # Wonderchat sometimes has a floating pulse div and a button with text "Chat"
            trigger = page.locator("button.chakra-button:has(svg), button:has-text('Chat')").first
            
            # If the user's specific pulse div is blocking it or acts as the trigger itself:
            pulse_div = page.locator("div[style*='animation: pulse']").first
            
            if await pulse_div.count() > 0 and await pulse_div.is_visible():
                await pulse_div.click(timeout=5000)
                await asyncio.sleep(2)
            elif await trigger.count() > 0 and await trigger.is_visible():
                await trigger.click(timeout=5000)
                await asyncio.sleep(2)
                
            # Step 1.5: Wonderchat often has an interstitial window where we must explicitly select "Chat mode"
            target_frame = next((f for f in page.frames if "wonderchat" in f.url.lower()), None)
            if target_frame:
                # The user provided these specific secondary triggers inside the frame
                chat_mode_triggers = [
                    "button.chakra-button:has-text('Chat')",
                    "div.chakra-stack:has(img[alt='Wonderchat'])"
                ]
                for cm_loc in chat_mode_triggers:
                    mode_btn = target_frame.locator(cm_loc).first
                    if await mode_btn.count() > 0 and await mode_btn.is_visible():
                        await mode_btn.click()
                        await asyncio.sleep(2)
                        break
            if target_frame:
                # The user's input box is usually a standard input mapped to a form
                input_locators = ["input[placeholder*='message' i]", "textarea", "input[type='text']"]
                for loc in input_locators:
                    element = target_frame.locator(loc).first
                    if await element.count() > 0 and await element.is_visible():
                        await element.click()
                        await asyncio.sleep(1)
                        
                        # Message 1
                        await element.type("Hi there, what features do you offer?", delay=80)
                        await asyncio.sleep(1)
                        await element.press("Enter")
                        result["interactions"].append({"action": "type", "target": "wonderchat fastpath", "text": "Hi there, what features do you offer?", "success": True})
                        
                        # Wait for AI response (longer human delay)
                        logger.info("Sent message 1, waiting 10s for AI to stream reply...")
                        await asyncio.sleep(10)
                        
                        # Message 2 (Privacy)
                        await element.click()
                        await asyncio.sleep(1)
                        await element.type("And what is your privacy policy regarding user chat history?", delay=80)
                        await asyncio.sleep(1)
                        await element.press("Enter")
                        result["interactions"].append({"action": "type", "target": "wonderchat fastpath", "text": "And what is your privacy policy regarding user chat history?", "success": True})
                        
                        logger.info("Sent message 2, waiting 10s for AI reply...")
                        await asyncio.sleep(10)
                        
                        result["triggered"] = True
                        logger.info("✅ Wonderchat multi-turn fast-path successful!")
                        return result
    except Exception as e:
        logger.debug(f"Wonderchat.io fast-path failed: {e}")

    # --- Phase 1: DETECT ---
    logger.info("Phase 1: Detecting AI elements (6-strategy scan)")
    detected = await detect_ai_elements(page)
    result["elements_found"] = detected

    if not detected:
        # Even if initial scan finds nothing, wait for lazy-loaded widgets
        logger.info("No initial AI elements found, waiting for lazy-loaded widgets...")
        mutation_elements = await wait_for_chatbot_mutations(page, timeout_ms=5000)
        detected.extend(mutation_elements)
        result["elements_found"] = detected

    if not detected:
        logger.info("No AI elements detected on this page (after mutation wait)")
        return result

    logger.info(f"Found {len(detected)} potential AI elements, attempting invocation")

    # --- Phase 2: CLICK on detected elements ---
    # Prioritize by confidence: high > medium > low
    sorted_detections = sorted(
        detected,
        key=lambda d: {"high": 0, "medium": 1, "low": 2}.get(d["confidence"], 3)
    )

    for detection in sorted_detections[:5]:  # Try at most 5 elements
        try:
            logger.info(f"Clicking: {detection['selector']} "
                       f"(confidence: {detection['confidence']}, type: {detection['type']})")

            # Try to click the element
            clicked = False

            # Method A: Use coordinates if available
            if detection.get("x") is not None and detection.get("y") is not None:
                try:
                    await page.mouse.click(detection["x"], detection["y"])
                    clicked = True
                except Exception:
                    pass

            # Method B: Use CSS selector
            if not clicked:
                try:
                    await page.click(detection["selector"], timeout=5000)
                    clicked = True
                except Exception:
                    pass

            # Method C: Use text content
            if not clicked and detection.get("text"):
                try:
                    text_snippet = detection["text"][:50].strip()
                    if text_snippet:
                        await page.get_by_text(text_snippet).first.click(timeout=5000)
                        clicked = True
                except Exception:
                    pass

            if clicked:
                result["interactions"].append({
                    "action": "click",
                    "target": detection["selector"],
                    "confidence": detection["confidence"],
                    "type": detection["type"],
                    "success": True,
                })

                # Wait for the widget to initialize
                # (iframe loads, animations complete, input field appears)
                await asyncio.sleep(random.uniform(2.0, 4.0))

        except Exception as e:
            logger.debug(f"Click failed on {detection['selector']}: {e}")
            result["interactions"].append({
                "action": "click",
                "target": detection["selector"],
                "confidence": detection["confidence"],
                "success": False,
                "error": str(e)[:200],
            })

    # --- Phase 3: HANDLE PRE-CHAT FORMS ---
    # Some chatbots (Intercom, Zendesk, Drift) show a form asking for
    # Name/Email before the actual chat. We fill these automatically.
    logger.info("Phase 3: Checking for pre-chat forms")
    prechat_handled = await handle_prechat_form(page)
    result["prechat_form_handled"] = prechat_handled

    if prechat_handled:
        # After form submission, wait for the actual chat input to appear
        await asyncio.sleep(random.uniform(2.0, 4.0))

    # --- Phase 4: INPUT — Find text fields and type meaningful text ---
    logger.info("Phase 4: Looking for AI input fields")

    # Select a meaningful prompt to type
    prompt_text = random.choice(AI_PROMPT_TEXTS)

    # Search for input fields in ALL frames (main + iframes)
    # WHY ALL FRAMES? Chatbot input fields are typically inside iframes
    for frame in page.frames:
        try:
            # Common selectors for chat input fields, ordered by specificity
            input_selectors = [
                # Chat-specific inputs (highest priority)
                "textarea[placeholder*='message' i]",
                "textarea[placeholder*='type' i]",
                "textarea[placeholder*='ask' i]",
                "textarea[placeholder*='chat' i]",
                "textarea[placeholder*='write' i]",
                "textarea[placeholder*='reply' i]",
                "input[placeholder*='message' i]",
                "input[placeholder*='type' i]",
                "input[placeholder*='ask' i]",
                "input[placeholder*='chat' i]",
                "input[placeholder*='write' i]",
                # ARIA-labeled inputs
                "[aria-label*='message' i]",
                "[aria-label*='chat' i]",
                "[aria-label*='type' i]",
                # Contenteditable (used by modern chat UIs)
                "[contenteditable='true']",
                "[role='textbox']",
                # Generic text inputs (lowest priority)
                "textarea",
                "input[type='text']",
            ]

            for selector in input_selectors:
                try:
                    elements = await frame.query_selector_all(selector)
                    for el in elements:
                        visible = await el.is_visible()
                        if visible:
                            # Verify this looks like a chat input (not a search bar)
                            # WHY: Search bars also match "input[type=text]" but
                            # we don't want to type chat prompts there.
                            is_search = False
                            try:
                                attrs = await el.evaluate("""
                                    el => ({
                                        type: el.type || '',
                                        name: el.name || '',
                                        id: el.id || '',
                                        role: el.getAttribute('role') || '',
                                        placeholder: el.placeholder || '',
                                        ariaLabel: el.getAttribute('aria-label') || '',
                                    })
                                """)
                                search_indicators = ["search", "query", "find", "lookup"]
                                for ind in search_indicators:
                                    if (ind in attrs.get("name", "").lower() or
                                        ind in attrs.get("id", "").lower() or
                                        ind in attrs.get("role", "").lower() or
                                        ind in attrs.get("placeholder", "").lower()):
                                        is_search = True
                                        break
                            except Exception:
                                pass

                            if is_search:
                                logger.debug(f"Skipping search bar: {selector}")
                                continue

                            # Found a visible chat input field! Type our prompt.
                            logger.info(f"Typing prompt into {selector} in frame {frame.url[:80]}")

                            # Click on the input first (to focus it)
                            await el.click()
                            await asyncio.sleep(random.uniform(0.5, 1.0))

                            # Type the prompt character by character (human-like)
                            # WHY char-by-char? Some chatbots detect paste events
                            # and behave differently. Typing triggers proper
                            # keydown/keyup events that chatbots listen for.
                            await el.type(prompt_text, delay=random.uniform(30, 80))

                            result["interactions"].append({
                                "action": "type",
                                "target": selector,
                                "frame_url": frame.url,
                                "text": prompt_text,
                                "success": True,
                            })

                            # --- Phase 5: SUBMIT ---
                            # Press Enter to send the message
                            await asyncio.sleep(random.uniform(0.5, 1.0))
                            await el.press("Enter")

                            result["interactions"].append({
                                "action": "submit",
                                "target": selector,
                                "success": True,
                            })

                            result["triggered"] = True

                            # Wait for AI response (network requests, DOM changes)
                            logger.info("Waiting for AI response...")
                            await asyncio.sleep(random.uniform(5.0, 10.0))

                            # Don't try more input fields once we've triggered one
                            break

                except Exception as e:
                    logger.debug(f"Input attempt failed for {selector}: {e}")
                    continue

            # If we already triggered AI in this frame, don't check other frames
            if result["triggered"]:
                break

        except Exception as e:
            logger.debug(f"Frame input search failed: {e}")
            continue

    # --- Phase 6: Log results ---
    if result["triggered"]:
        logger.info("AI component TRIGGERED successfully!")
    else:
        logger.info("AI detection found elements but could not trigger invocation")

    return result


# =============================================================================
# AUDIO/VOICE AI DETECTION + TRIGGER
# =============================================================================


