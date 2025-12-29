#!/usr/bin/env python3
"""
query_subreddits.py

Usage:
  python query_subreddits.py saas llamaindex ollama localllama

Reads out/subreddits_metadata.json and prints a short numeric + textual summary
for each subreddit name passed on the command line (case-insensitive).
"""

import sys
import json
from pathlib import Path
from datetime import datetime

IN_PATH = Path("out/subreddits_metadata.json")

def normalize(name):
    if not name:
        return ""
    n = name.strip().lower()
    if n.startswith("r/"):
        n = n[2:]
    return n

def short_summary(item):
    subs = item.get("subscribers")
    active = item.get("active_user_count")
    avg_posts = item.get("avg_posts_per_day")
    recent_posts = item.get("recent_post_count")
    recent_comments = item.get("recent_comment_count")
    desc = (item.get("public_description") or "").strip()
    top_domains = item.get("top_external_domains") or []
    top_submitters = item.get("top_submitters") or []

    return {
        "subreddit": item.get("subreddit") or item.get("title"),
        "title": item.get("title"),
        "subscribers": subs,
        "active_user_count": active,
        "avg_posts_per_day": avg_posts,
        "recent_post_count": recent_posts,
        "recent_comment_count": recent_comments,
        "top_external_domains": top_domains[:5],
        "top_submitters_sample": top_submitters[:5],
        "description": desc[:300]  # cap length
    }

def main():
    if not IN_PATH.exists():
        print(f"Error: input file not found: {IN_PATH.resolve()}")
        return

    args = sys.argv[1:]
    if not args:
        print("Usage: python query_subreddits.py <subreddit1> <subreddit2> ...")
        return

    requested = [normalize(a) for a in args]

    with IN_PATH.open("r", encoding="utf8") as f:
        data = json.load(f)

    # index by normalized subreddit name and by title lowercased
    index = {}
    for it in data:
        name = normalize(it.get("subreddit") or "")
        if name:
            index[name] = it
        title = (it.get("title") or "").strip().lower()
        if title and title not in index:
            index[title] = it

    now = datetime.utcnow().isoformat() + "Z"
    print(f"\nQuery time: {now}")
    print(f"Loaded {len(data)} records from {IN_PATH}\n")

    for req in requested:
        it = index.get(req)
        if it is None:
            print(f"==> {req}  — NOT FOUND in {IN_PATH.name}")
            continue
        s = short_summary(it)
        print(f"==> r/{s['subreddit']}  (title: {s['title']})")
        print(f"    subscribers: {s['subscribers']:,}" if s['subscribers'] is not None else "    subscribers: N/A")
        print(f"    active_user_count: {s['active_user_count']}" if s['active_user_count'] is not None else "    active_user_count: N/A")
        print(f"    avg_posts_per_day: {s['avg_posts_per_day']}")
        print(f"    recent_post_count (sampled window): {s['recent_post_count']}")
        print(f"    recent_comment_count (sampled window): {s['recent_comment_count']}")
        print(f"    top_external_domains (sample): {s['top_external_domains']}")
        print(f"    top_submitters (sample): {s['top_submitters_sample']}")
        print(f"    description: {s['description']!r}")
        print()

if __name__ == "__main__":
    main()
