"""
utils.py — Configuration, Logging, and Output Helpers
=====================================================

This module centralizes all configuration constants, sets up structured
logging, and provides helper functions for saving crawl data to disk.

WHY: Having a single source of truth for config (timeouts, paths, etc.)
makes the crawler easy to tune without touching business logic.
"""

import json
import logging
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path


# =============================================================================
# CONFIGURATION CONSTANTS
# =============================================================================

# --- Timeouts ---
# Page load timeout: 30s is aggressive but prevents hanging on slow sites.
# If a page doesn't load in 30s, it's likely broken or blocking us.
PAGE_LOAD_TIMEOUT_MS = 30_000  # 30 seconds, in milliseconds (Playwright uses ms)

# Interaction timeout: 2 minutes. After the page loads, we interact with it
# (click chatbots, type text, etc.). Some AI widgets take time to initialize
# (lazy-loaded iframes, WebSocket handshakes), so we give a generous window.
INTERACTION_TIMEOUT_MS = 120_000  # 2 minutes, in milliseconds

# --- Paths ---
# Extension path for Consent-O-Matic (handles cookie consent popups automatically).
# This extension must be downloaded, built (npm install && npm run build),
# and the Extension/ folder placed here.
# See: https://github.com/cavi-au/Consent-O-Matic
EXTENSION_PATH = os.path.join(os.path.dirname(__file__), "extensions", "Consent-O-Matic")

# Output directory for crawl results (JSON files, one per domain).
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

# --- Browser Settings ---
# Window dimensions — large enough to render most sites properly.
# We position the window off-center so it doesn't block the user's work.
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 900
WINDOW_X = 100  # pixels from left edge
WINDOW_Y = 100  # pixels from top edge

# --- Network Capture Limits ---
# Max response body size to store (in bytes). We don't want to store
# multi-megabyte video responses — just API payloads and HTML.
MAX_RESPONSE_BODY_SIZE = 1_000_000  # 1 MB

# --- Human Simulation ---
# These control how "human" the mouse/scroll behavior looks.
MOUSE_MOVE_STEPS_MIN = 20   # Minimum interpolation steps for Bezier curve
MOUSE_MOVE_STEPS_MAX = 40   # Maximum interpolation steps
SCROLL_INCREMENT_MIN = 200  # Minimum pixels per scroll step
SCROLL_INCREMENT_MAX = 500  # Maximum pixels per scroll step
PAUSE_MIN = 1.0             # Minimum pause between actions (seconds)
PAUSE_MAX = 3.0             # Maximum pause between actions (seconds)

# Maximum number of scroll steps before giving up.
# WHY: Infinite-scroll pages (e.g., Twitter/X, Reddit) will never reach
# scrollHeight. We cap at 120 scrolls (~24000-60000px) to prevent hanging.
MAX_SCROLL_STEPS = 120


# =============================================================================
# AI DETECTION — EXHAUSTIVE PATTERNS
# =============================================================================
# These patterns are compiled from multiple research sources:
# - Waheed et al. (2022): DOM/iframe scanning heuristics
# - Kaya et al. (2025): network-level chatbot interception
# - Hantke et al. (WebREC): DOM Mutation & lazy-loading detection
# - Manual analysis of Tranco Top 1K sites with chatbots

# Primary regex for finding AI-related UI elements.
# Covers: chatbots, copilots, virtual assistants, AI helpers, summarizers,
# voice agents, support widgets, and known provider names.


# Secondary regex specifically for cookie/consent/popup elements.
# WHY: If Consent-O-Matic misses a banner, we try to close it ourselves.
# This is a FALLBACK — Consent-O-Matic handles most cases, but custom
# banners, non-standard CMPs, and region-specific dialogs may slip through.
CONSENT_POPUP_REGEX = re.compile(
    r"(?i)\b("
    r"accept|accept[-_\s]?all|agree|allow|allow[-_\s]?all|"
    r"i[-_\s]?agree|i[-_\s]?accept|i[-_\s]?understand|"
    r"got[-_\s]?it|ok|okay|continue|proceed|"
    r"consent|cookie|gdpr|privacy|"
    r"dismiss|close|reject|deny|decline|"
    r"necessary[-_\s]?only|essential[-_\s]?only"
    r")\b",
    re.IGNORECASE,
)

# Regex for detecting permission/notification dialogs to auto-dismiss.
PERMISSION_DIALOG_REGEX = re.compile(
    r"(?i)\b("
    r"allow|block|deny|dismiss|close|cancel|not[-_\s]?now|"
    r"later|no[-_\s]?thanks|maybe[-_\s]?later|remind[-_\s]?later|"
    r"notifications|location|microphone|camera|push"
    r")\b",
    re.IGNORECASE,
)


# Pre-stored "meaningful" text inputs to type into AI chat fields.
# These are designed to trigger AI processing / LLM calls.
# WHY these specific prompts? They cover common chatbot capabilities:
# - Summarization (tests content extraction / RAG)
# - Product inquiry (tests FAQ / knowledge base)
# - General help (tests intent routing)
# - Privacy-relevant queries (tests data handling)
AI_PROMPT_TEXTS = [
    "Hello, can you help me summarize this page?",
    "What services does this website offer?",
    "Can you assist me with my question about this site?",
    "Tell me more about your products.",
    "I need help finding information on this page.",
    "What is your privacy policy regarding my data?",
    "How can I contact customer support?",
    "Can you explain the main features of this platform?",
]

# Pre-chat form dummy data — used when chatbots require Name/Email
# before allowing conversation (common with Intercom, Zendesk, Drift).
# WHY: Many chatbots show a "pre-chat survey" form. If we don't fill it,
# we never reach the actual AI conversation, missing the chatbot entirely.
PRECHAT_FORM_DATA = {
    "name": "Test User",
    "first_name": "Test",
    "last_name": "User",
    "email": "testcrawler@example.com",
    "phone": "+1234567890",
    "company": "Research Lab",
    "message": "I need help with your services.",
}

# User agent pool for rotation (if needed in the future).
# For now, Playwright's default user agent is fine since we use stealth mode.
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]


# =============================================================================
# LOGGING SETUP
# =============================================================================

def setup_logger(name: str = "crawler", level: int = logging.INFO) -> logging.Logger:
    """
    Create a structured logger with both console and file output.
    
    WHY: We need detailed logs for debugging (file) but concise output
    for monitoring (console). Each crawl site gets context via the logger name.
    
    Args:
        name: Logger name (typically the domain being crawled)
        level: Logging level (DEBUG for development, INFO for production)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if logger already exists
    if logger.handlers:
        return logger

    # Console handler — concise, INFO level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_fmt = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(name)s | %(message)s",
        datefmt="%H:%M:%S"
    )
    console_handler.setFormatter(console_fmt)
    logger.addHandler(console_handler)

    # File handler — verbose, DEBUG level, writes to output/crawler.log
    try:
        log_dir = Path(OUTPUT_DIR)
        log_dir.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_dir / "crawler.log", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_fmt = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s"
        )
        file_handler.setFormatter(file_fmt)
        logger.addHandler(file_handler)
    except (PermissionError, OSError):
        pass  # Fall back to console-only logging if output dir isn't writable

    return logger


# =============================================================================
# OUTPUT HELPERS
# =============================================================================

def sanitize_domain(url: str) -> str:
    """
    Convert a URL into a safe filename string.
    
    WHY: Domain names can contain characters invalid for filenames.
    We strip the protocol, replace special chars, and truncate.
    
    Examples:
        'https://www.example.com/path' → 'www.example.com'
        'http://sub.domain.co.uk:8080' → 'sub.domain.co.uk_8080'
    """
    # Remove protocol
    domain = re.sub(r'^https?://', '', url)
    # Remove path and query string
    domain = domain.split('/')[0]
    # Replace unsafe chars with underscores
    domain = re.sub(r'[^a-zA-Z0-9._-]', '_', domain)
    # Truncate to prevent filesystem issues
    return domain[:200]


def save_crawl_data(data: dict, domain: str) -> str:
    """
    Save crawl results to a structured JSON file.
    
    WHY: Each site gets its own JSON file so we can easily inspect,
    debug, or re-process individual results without parsing a massive log.
    
    Args:
        data: Dictionary containing all crawl data (frames, network, etc.)
        domain: Sanitized domain name (used as filename)
    
    Returns:
        Path to the saved JSON file
    """
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Add metadata to the output
    data["_metadata"] = {
        "crawl_timestamp": datetime.now(timezone.utc).isoformat(),
        "crawler_version": "0.2.0",
        "domain": domain,
    }

    filepath = output_dir / f"{domain}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)

    return str(filepath)


def create_empty_crawl_result(url: str) -> dict:
    """
    Create the skeleton structure for a crawl result.
    
    WHY: Having a consistent schema makes downstream analysis easier.
    Every field is initialized even if the crawl fails partway through.
    
    Returns:
        Dictionary with all expected fields initialized to empty defaults.
    """
    return {
        "url": url,
        "status": "pending",  # Will be set to "success", "error", or "timeout"
        "error": None,
        "timing": {
            "start": None,
            "page_loaded": None,
            "consent_handled": None,
            "interaction_done": None,
            "ai_invocation_done": None,
            "capture_done": None,
            "end": None,
        },
        "frames": [],              # List of frame data (main + iframes)
        "network_requests": [],    # Standard Playwright request/response data
        "cdp_requests": [],        # CDP-level data with stack traces / initiator info
        "storage": {
            "cookies": [],
            "local_storage": {},
            "session_storage": {},
        },
        "ai_detection": {
            "elements_found": [],   # AI-related elements detected in the DOM
            "interactions": [],     # Actions taken (clicks, typing)
            "triggered": False,     # Whether any AI component was successfully invoked
        },
        "consent_handling": {
            "extension_handled": False,  # Consent-O-Matic handled the banner
            "fallback_used": False,      # Our regex fallback was used
            "popups_dismissed": 0,       # Number of popups/banners we dismissed
        },
        "permissions_requested": [],  # Track what permissions the site asked for
    }


def timestamp() -> str:
    """Return current UTC timestamp as ISO string."""
    return datetime.now(timezone.utc).isoformat()
