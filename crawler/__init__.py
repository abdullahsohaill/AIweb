"""
AI Web Crawler — Package Initialization
========================================

A modular Playwright-based web crawler designed to detect, invoke, and
analyze AI services (chatbots, copilots, voice agents) on websites.

Modules:
    browser.py        — Browser launch, stealth, extension loading, CDP
    interaction.py    — Human-like mouse, scroll, clicks, consent fallback
    capture.py        — Frame content, network, CDP stack traces, storage,
                        dynamic frame re-capture, permission tracking
    ai_invocation.py  — 6-strategy AI detection, pre-chat forms, Shadow DOM,
                        MutationObserver, network AI confirmation, voice AI
    utils.py          — Config constants, logging, output helpers
    main.py           — Orchestrator (9-step pipeline), CLI entry point
"""
