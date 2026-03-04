"""
CRAWLER_ARCHITECTURE.md — Complete Structure, Hierarchy & Workflow
==================================================================

HOW TO USE THIS FILE:
This document explains every file, every step, and how data flows through
the crawler. Read this FIRST before modifying any code.

LAST UPDATED: March 2026 (v0.2.0 — post-testing)
"""

# AI Web Crawler — Architecture Guide

## 1. Directory Structure

```
AI_Web/
├── crawler/                        # Main crawler package
│   ├── __init__.py                 # Package init + module docstrings
│   ├── utils.py                    # Config constants, logging, output helpers
│   ├── browser.py                  # Browser launch (two-tier), stealth, CDP
│   ├── interaction.py              # Human simulation, consent fallback
│   ├── capture.py                  # Frame/network/CDP/storage data capture
│   ├── ai_invocation.py            # AI detection (6-strategy), invocation, voice AI
│   ├── main.py                     # Orchestrator, CLI, 9-step pipeline
│   ├── requirements.txt            # Dependencies (playwright, playwright-stealth)
│   ├── test_sites.txt              # Test URLs for validation
│   ├── extensions/                 # Chrome extensions
│   │   ├── README.md               # Extension setup instructions
│   │   └── Consent-O-Matic/        # Built extension (from npm build)
│   │       ├── manifest.json       # Chrome MV3 manifest
│   │       ├── service.js          # Extension service worker
│   │       ├── content.js          # Content script
│   │       ├── GDPRConfig.js       # Consent config (all true)
│   │       └── ...
│   └── output/                     # Crawl results (auto-created)
│       ├── www.tawk.to.json        # One JSON per domain
│       ├── www.tidio.com.json
│       └── crawler.log             # Persistent log file
└── Consent-O-Matic/                # Cloned extension source
    ├── Extension/                  # Source files
    ├── webpack.config.js           # Build config
    └── package.json
```


## 2. Module Responsibilities

### A. `utils.py` — Configuration & Constants

**Purpose**: Single source of truth for ALL tuneable parameters.

| Constant | Value | Why |
|---|---|---|
| `PAGE_LOAD_TIMEOUT_MS` | 30,000ms | 30s prevents hanging on broken sites |
| `INTERACTION_TIMEOUT_MS` | 120,000ms | 2min for lazy-loaded AI widgets |
| `MAX_SCROLL_STEPS` | 120 | Prevents infinite-scroll hangs |
| `MAX_RESPONSE_BODY_SIZE` | 1MB | Captures API payloads, skips videos |
| `EXTENSION_PATH` | `extensions/Consent-O-Matic` | Consent extension location |

**Key objects**:
- `AI_TRIGGER_REGEX` — 1051-char regex matching 60+ AI/chatbot terms
- `CONSENT_POPUP_REGEX` — Fallback consent button keywords
- `PRECHAT_FORM_DATA` — Dummy Name/Email/Phone for pre-chat forms
- `AI_PROMPT_TEXTS` — Prompts to type into chatbots

**Key functions**:
- `setup_logger(name)` → Console + file logger
- `sanitize_domain(url)` → Safe filename from URL
- `save_crawl_data(data, domain)` → JSON output per domain
- `create_empty_crawl_result(url)` → Consistent output schema


### B. `browser.py` — Browser Launch & Stealth

**Purpose**: Launch Chromium with stealth, extensions, and permissions.

**Two-Tier Launch Strategy**:
```
Tier 1: launch_persistent_context()     ← Extensions work
         │ Requires socket directory     ← May fail on macOS
         ↓ Falls back to...
Tier 2: browser.launch() + new_context() ← Always works, no extensions
         │ Consent fallback compensates
         └─ interaction.py handles cookie banners
```

**Why persistent context?** Only way to load Chrome extensions in Playwright.
**Why fallback?** macOS blocks ProcessSingleton socket creation in some environments.

**Stealth measures**:
1. `playwright-stealth` patches (if installed): navigator.webdriver, plugins, etc.
2. `--disable-blink-features=AutomationControlled` (always active)
3. Fake media stream for voice AI testing

**Permissions auto-granted**: microphone, camera, geolocation, notifications

**CDP session**: Each page gets a Chrome DevTools Protocol session for stack trace capture.


### C. `interaction.py` — Human Behavior Simulation

**Purpose**: Make the crawler look like a real human.

**Action Sequence** (in `simulate_human_behavior()`):
1. **Initial pause** (1.5-3s) — human looks at page first
2. **Consent popup fallback** — dismiss banners Consent-O-Matic missed
3. **Random mouse movements** (2-4 elements) via Bezier curves
4. **Scroll down** (capped at 120 steps) — triggers lazy-loading
5. **Random clicks** (2-5) on non-navigational elements
6. **Second popup check** — some popups appear after scroll
7. **Final pause** (1-2s)

**Bezier Curves**:
```
Mouse moves from A→B along a curved path, not a straight line.
Control points are randomized so each movement is unique.
20-40 interpolation steps with 5-15ms micro-delays.
```

**Consent Popup Fallback** (`dismiss_consent_popups()`):
- Finds fixed/absolute elements with z-index > 100
- Looks for buttons matching accept/dismiss keywords
- Priority: "accept all" > "accept" > "agree" > "ok" > "close"
- Logs what was dismissed


### D. `capture.py` — Data Capture Engine

**Purpose**: Record everything the page does.

**Four capture layers**:

```
┌─ Layer 1: NETWORK CAPTURE ──────────────────────────┐
│  Playwright page.on('request'/'response')            │
│  → URL, method, headers, POST data, response body    │
│  → Response body capped at 1MB, text types only      │
└──────────────────────────────────────────────────────┘

┌─ Layer 2: CDP STACK TRACE CAPTURE ──────────────────┐
│  Chrome DevTools Protocol: Network.requestWillBeSent │
│  → Initiator type (script/parser/user/other)         │
│  → Full async call stack (function → script → line)  │
│  → Critical for tracing AI API calls to source JS    │
└──────────────────────────────────────────────────────┘

┌─ Layer 3: FRAME CONTENT ────────────────────────────┐
│  All frames: main page + iframes                     │
│  → HTML content, inner text, script URLs             │
│  → Dynamic re-capture: new frames after AI invoc.    │
│  → Marked with captured_phase for analysis           │
└──────────────────────────────────────────────────────┘

┌─ Layer 4: STORAGE ──────────────────────────────────┐
│  → Cookies (all domains)                             │
│  → localStorage entries                              │
│  → sessionStorage entries                            │
│  → Permission states (6 APIs)                        │
└──────────────────────────────────────────────────────┘
```

**Important**: Network/CDP capture is set up BEFORE navigation.
Frame/storage capture happens AFTER all interactions.


### E. `ai_invocation.py` — AI Detection & Triggering

**Purpose**: Find and interact with AI services on the page.

**6-Strategy GENERIC Detection Pipeline**:
*No provider-specific selectors are used. Discovery is purely heuristic.*

```
Strategy 1: FIXED-POSITION CORNER ELEMENTS
  ├── Detects position:fixed/sticky, z-index > 999
  ├── Checks bottom-right or bottom-left of viewport
  └── Confidence: HIGH if clickable, MEDIUM otherwise

Strategy 2: CROSS-ORIGIN IFRAMES
  ├── Detects ANY iframe from a different domain than host
  ├── Skips known ads/analytics domains (Google, Facebook, etc.)
  └── Confidence: MEDIUM

Strategy 3: ACCESSIBILITY (ARIA) TREE
  ├── Scans role="dialog", role="complementary", aria-live
  ├── Matches aria-labels/text against functional chat keywords
  └── Confidence: HIGH

Strategy 4: SHADOW DOM TRAVERSAL
  ├── Recursive traverseShadowRoots (up to 5 levels)
  ├── Checks shadow host id/class for functional chat keywords
  └── Confidence: HIGH

Strategy 5: GENERIC TEXT / ATTRIBUTES
  ├── Scans buttons, links, inputs for functional keywords
  ├── Keywords: "chat", "message", "help", "assistant" (no brand names)
  └── Confidence: MEDIUM

Strategy 6: INTERACTIVE WIDGET PATTERNS
  ├── Looks for floating <button> or <div> containing <img> or <svg>
  ├── Must be in bottom corners
  └── Confidence: MEDIUM
```

**Invocation Sequence**:
```
1. DETECT   → Run all 6 generic strategies, deduplicate by selector
2. MUTATE   → If nothing found, wait 5s for MutationObserver
3. SORT     → Order by confidence (high → low)
4. CLICK    → Click top elements, wait 2-4s each
5. PRE-CHAT → Dismiss modals, handle generic text forms + ARIA comboboxes
6. INPUT    → Find chat input across all frames + Shadow DOM
7. FILTER   → Skip search bars
8. TYPE     → Type prompt char-by-char (30-80ms delay)
9. SUBMIT   → Press Enter
10. WAIT    → 5-10s for AI response
```

**Network AI Confirmation** (`check_network_for_ai_activity()`):
Post-invocation verification that evaluates traffic payloads generically:
- **Conversational Payloads**: POST requests with ≥2 LLM markers (`"role"`, `"messages"`, `"content"`)
- **Streaming Responses**: SSE streams (`text/event-stream`)
- **WebSocket Connections**: WSS typically used for real-time voice/chat AI
- **Generic API Endpoints**: URL paths containing `/chat/completions`, `/generate`, etc.


### F. `main.py` — Orchestrator & CLI

**Purpose**: Tie everything together into a 9-step pipeline.

**9-Step Pipeline** (per site):

```
Step 1: CREATE PAGE        → browser.create_page()
         ├── New tab with stealth
         └── CDP session attached

Step 2: ATTACH CAPTURE     → capture.setup_network_capture()
         ├── capture.setup_cdp_capture()
         └── Listeners attached BEFORE navigation

Step 3: NAVIGATE           → page.goto(url)
         ├── wait_until="domcontentloaded" (30s timeout)
         └── Partial data saved even on timeout

Step 4: CONSENT WAIT       → asyncio.sleep(5)
         └── Gives Consent-O-Matic time to handle banners

Step 5: HUMAN BEHAVIOR     → interaction.simulate_human_behavior()
         ├── Mouse, scroll (max 120 steps), clicks
         └── Consent popup fallback

Step 6: AI INVOCATION      → ai_invocation.trigger_ai_components()
         ├── 6-strategy detection
         ├── Pre-chat form handling
         ├── Chat input + prompt typing
         └── ai_invocation.trigger_voice_ai()

Step 7: FRAME RE-CAPTURE   → capture.capture_frames_dynamic()
         └── Catches chatbot iframes injected during step 6

Step 8: NETWORK CONFIRM    → ai_invocation.check_network_for_ai_activity()
         └── Verifies AI via traffic analysis

Step 9: FINAL CAPTURE      → capture.run_full_capture()
         ├── All frames (main + iframes)
         ├── Storage (cookies, localStorage, sessionStorage)
         └── Permission states

SAVE → utils.save_crawl_data() → output/{domain}.json
```

**CLI**:
```bash
python -m crawler.main --url https://example.com           # Single site
python -m crawler.main --file sites.txt --max-sites 10     # Batch
python -m crawler.main --url https://example.com --headless # No GUI
python -m crawler.main --url https://example.com --verbose  # Debug logs
```


## 3. Data Flow Diagram

```
                    URL Input
                       │
                  ┌────▼────┐
                  │ main.py │
                  │ (Step 1)│
                  └────┬────┘
                       │
              ┌────────▼────────┐
              │   browser.py    │
              │ launch_browser()│────── Consent-O-Matic
              │  create_page()  │       (if available)
              └────────┬────────┘
                       │
           ┌───────────▼───────────┐
           │      capture.py       │
           │ setup_network_capture │
           │ setup_cdp_capture     │
           └───────────┬───────────┘
                       │ (listeners active)
              ┌────────▼────────┐
              │   page.goto()   │── Network/CDP recording ──►
              └────────┬────────┘
                       │
           ┌───────────▼───────────┐
           │   interaction.py      │
           │ simulate_human_behavior│
           │ dismiss_consent_popups │
           └───────────┬───────────┘
                       │
          ┌────────────▼────────────┐
          │    ai_invocation.py     │
          │ detect_ai_elements()    │
          │ handle_prechat_form()   │
          │ trigger_ai_components() │
          │ trigger_voice_ai()      │
          └────────────┬────────────┘
                       │
           ┌───────────▼───────────┐
           │     capture.py        │
           │ capture_frames_dynamic │
           │ run_full_capture       │
           │ capture_permission_state│
           └───────────┬───────────┘
                       │
              ┌────────▼────────┐
              │   utils.py      │
              │ save_crawl_data │
              └────────┬────────┘
                       │
              output/{domain}.json
```


## 4. Output JSON Schema

Each crawl produces a JSON file with this structure:

```json
{
  "url": "https://www.example.com",
  "status": "success",                    // or "error", "timeout"
  "http_status": 200,
  "error": null,
  "timing": {
    "start": "2026-03-01T12:00:00Z",
    "page_loaded": "...",
    "consent_handled": "...",
    "interaction_done": "...",
    "ai_invocation_done": "...",
    "capture_done": "...",
    "end": "..."
  },
  "frames": [
    {
      "index": 0,
      "url": "https://www.example.com",
      "is_main": true,
      "html": "<!DOCTYPE html>...",
      "inner_text": "...",
      "script_urls": ["https://cdn.../script.js"],
      "captured_phase": "initial"         // or "post_ai_invocation"
    }
  ],
  "network_requests": [
    {
      "url": "https://api.example.com/chat",
      "method": "POST",
      "headers": {},
      "post_data": "{\"messages\":[...]}",
      "resource_type": "fetch",
      "response": {
        "status": 200,
        "headers": {},
        "body": "..."
      }
    }
  ],
  "cdp_requests": [
    {
      "url": "https://api.example.com/chat",
      "method": "POST",
      "initiator": {
        "type": "script",
        "stack": {
          "callFrames": [
            {
              "functionName": "sendMessage",
              "url": "https://cdn.../chatbot.js",
              "lineNumber": 42
            }
          ]
        }
      }
    }
  ],
  "storage": {
    "cookies": [],
    "local_storage": {},
    "session_storage": {}
  },
  "ai_detection": {
    "elements_found": [
      {
        "type": "iframe",
        "selector": "iframe[src*='tawk.to']",
        "confidence": "high"
      }
    ],
    "interactions": [
      {"action": "type", "target": "textarea", "success": true}
    ],
    "triggered": true,
    "prechat_form_handled": false
  },
  "ai_network_confirmation": {
    "ai_confirmed": true,
    "ai_endpoints_hit": [],
    "conversational_payloads": [],
    "streaming_responses": []
  },
  "consent_handling": {
    "extension_handled": false,
    "fallback_used": true,
    "popups_dismissed": 1
  },
  "permissions_requested": [
    {"name": "microphone", "state": "granted"}
  ]
}
```


## 5. Test Results Summary (Robust Heuristic Mining)

The crawler is currently undergoing Phase 6 evaluation on 20 distinct major chatbot integrations. The goal is to maximize generic detection (avoiding provider-specific lists) through Shadow DOM piercing, interactive element identification, and generic pre-chat form completion logic.

| Site | Status | Notes |
|---|---|---|
| tawk.to | ⏳ Pending | |
| livechat.com | ⏳ Pending | |
| intercom.com | ⏳ Pending | |
| drift.com | ⏳ Pending | |
| zendesk.com | ⏳ Pending | |
| freshdesk.com | ⏳ Pending | |
| crisp.chat | ⏳ Pending | |
| tidio.com | ⏳ Pending | |
| kustomer.com | ⏳ Pending | |
| botpress.com | ⏳ Pending | |
| yellow.ai | ⏳ Pending | |
| ada.cx | ⏳ Pending | |
| verloop.io | ⏳ Pending | |
| kommunicate.io | ⏳ Pending | |
| smartsupp.com | ⏳ Pending | |
| user.com | ⏳ Pending | |
| genesys.com | ⏳ Pending | |
| qualified.com | ⏳ Pending | |
| landbot.io | ⏳ Pending | |
| helpshift.com | ⏳ Pending | |


## 6. Known Limitations & Future Work

1. **Headed mode** fails on macOS due to ProcessSingleton restriction. Workaround: headless mode with consent fallback.
2. **playwright-stealth** not installable in current venv — basic stealth flags used instead.
3. **Pre-chat form** typed into a registration form on tawk.to instead of a chat pre-chat form — needs tighter scoping to only fill forms inside chatbot containers.
4. **Shadow DOM detection** on intercom.com caught `media-control-bar` (video player) instead of the chatbot — false positive. Needs narrower shadow DOM keyword matching.
5. **Network AI confirmation** flagged tidio.com via `/messages` endpoint match — could be validated further by checking response content.

## 7. Running the Crawler

```bash
# Prerequisites
pip install playwright
python -m playwright install chromium

# Environment setup (macOS fix)
export TMPDIR=/tmp

# Single site
TMPDIR=/tmp python -m crawler.main --url https://www.tawk.to --headless --verbose

# Batch mode
TMPDIR=/tmp python -m crawler.main --file sites.txt --max-sites 10 --headless

# Output
ls crawler/output/*.json
cat crawler/output/www.tawk.to.json | python -m json.tool | head -50
```
