# reddit_crawler_metadata.py
"""
Crawl subreddit metadata + recent activity + top external domains.

Requirements:
  pip install praw python-dotenv tqdm requests

Usage:
  - Create .env with REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
  - Ensure subreddits_clean.csv exists with header: subreddit
  - python reddit_crawler_metadata.py
"""

import os
import json
import time
import csv
from datetime import datetime, timedelta
from collections import Counter
from pathlib import Path

import praw
import requests
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "reddit-crawler/0.1 by yourusername")

# PARAMETERS (tune as needed)
POSTS_TO_FETCH = 200         # how many latest submissions to pull per subreddit
RECENT_DAYS = 30             # window to count "recent" posts (use 7, 30 etc.)
SLEEP_BETWEEN_SUBS = 0.6     # politeness backoff
OUTPUT_DIR = Path("out")
OUTPUT_DIR.mkdir(exist_ok=True)

INPUT_CSV = "subreddits_clean.csv"

def make_reddit():
    if not (REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET):
        raise ValueError("Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET in environment (.env).")
    return praw.Reddit(client_id=REDDIT_CLIENT_ID,
                       client_secret=REDDIT_CLIENT_SECRET,
                       user_agent=REDDIT_USER_AGENT,
                       check_for_async=False)

def read_subreddits(csv_path=INPUT_CSV):
    subs = []
    p = Path(csv_path)
    if not p.exists():
        raise FileNotFoundError(f"{csv_path} missing")
    with p.open("r", encoding="utf8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            name = r.get("subreddit") or r.get("Subreddit") or ""
            name = name.strip()
            if name:
                subs.append(name)
    return subs

def domain_from_url(url):
    try:
        n = requests.utils.urlparse(url).netloc.lower()
        if n.startswith("www."):
            n = n[4:]
        return n
    except Exception:
        return None

def extract_links_from_text(text):
    if not text:
        return []
    parts = text.split()
    links = []
    for p in parts:
        if p.startswith("http://") or p.startswith("https://"):
            links.append(p.strip().rstrip(")"))
    return links

def analyze_subreddit(reddit, name):
    out = {
        "subreddit": name,
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "title": None,
        "subscribers": None,
        "active_user_count": None,
        "public_description": None,
        "created_utc": None,
        "moderators": [],
        "recent_post_count": 0,
        "recent_comment_count": 0,
        "sampled_posts": 0,
        "avg_posts_per_day": None,
        "top_external_domains": [],
        "top_submitters": []
    }
    try:
        sr = reddit.subreddit(name)
        # basic metadata
        out["title"] = getattr(sr, "title", None)
        out["subscribers"] = getattr(sr, "subscribers", None)
        out["active_user_count"] = getattr(sr, "active_user_count", None)
        out["public_description"] = getattr(sr, "public_description", "") or ""
        out["created_utc"] = getattr(sr, "created_utc", None)

        # moderators (may raise if restricted; handle)
        try:
            out["moderators"] = [m.name for m in sr.moderator()]
        except Exception:
            out["moderators"] = []

        # iterate newest submissions
        cutoff_ts = (datetime.utcnow() - timedelta(days=RECENT_DAYS)).timestamp()
        external_domains = Counter()
        submitters = Counter()
        recent_posts = 0
        recent_comments = 0
        sampled = 0

        for submission in sr.new(limit=POSTS_TO_FETCH):
            sampled += 1
            # count recent posts
            if getattr(submission, "created_utc", 0) >= cutoff_ts:
                recent_posts += 1
            # count comments (only top-level count to approximate)
            try:
                recent_comments += getattr(submission, "num_comments", 0) or 0
            except Exception:
                pass
            # submitter
            try:
                if submission.author:
                    submitters[submission.author.name] += 1
            except Exception:
                pass
            # extract domain from url and body links
            try:
                url = submission.url or ""
                if url and "reddit.com" not in url:
                    dom = domain_from_url(url)
                    if dom:
                        external_domains[dom] += 1
                # also parse body for links
                links = extract_links_from_text(submission.selftext or "")
                for link in links:
                    dom = domain_from_url(link)
                    if dom:
                        external_domains[dom] += 1
            except Exception:
                pass

        out["recent_post_count"] = recent_posts
        out["recent_comment_count"] = recent_comments
        out["sampled_posts"] = sampled
        # average posts per day estimate over RECENT_DAYS
        out["avg_posts_per_day"] = (recent_posts / RECENT_DAYS) if RECENT_DAYS > 0 else None
        out["top_external_domains"] = external_domains.most_common(10)
        out["top_submitters"] = submitters.most_common(10)

    except Exception as e:
        out["error"] = str(e)
    return out

def crawl_all():
    reddit = make_reddit()
    subs = read_subreddits()
    results = []
    for name in tqdm(subs, desc="Crawling subs"):
        try:
            res = analyze_subreddit(reddit, name)
        except Exception as e:
            res = {"subreddit": name, "error": str(e)}
        results.append(res)
        time.sleep(SLEEP_BETWEEN_SUBS)
    # write outputs
    out_json = OUTPUT_DIR / "subreddits_metadata.json"
    out_csv = OUTPUT_DIR / "subreddits_metadata.csv"
    with out_json.open("w", encoding="utf8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    # Flatten CSV: serialize lists
    keys = set()
    for r in results:
        keys.update(r.keys())
    keys = list(keys)
    with out_csv.open("w", encoding="utf8", newline="") as f:
        import csv as _csv
        writer = _csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in results:
            row = {}
            for k in keys:
                v = r.get(k)
                if isinstance(v, (list, dict)):
                    row[k] = json.dumps(v, ensure_ascii=False)
                else:
                    row[k] = v
            writer.writerow(row)
    print("Saved:", out_json, out_csv)
    return results

if __name__ == "__main__":
    crawl_all()
