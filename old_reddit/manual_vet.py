#!/usr/bin/env python3
"""
manual_vet.py

Interactive terminal tool to manually label subreddits as relevant (1) or not (0).

Usage:
    python manual_vet.py

Inputs:
    out/subreddits_metadata.json  (crawler output)

Outputs (written as you label):
    out/subreddits_annotated.json
    out/subreddits_annotated.csv

Controls during the interactive session:
    1 -> mark Relevant
    0 -> mark Irrelevant
    s -> skip this item for now (saved as 'skipped')
    b -> go back one item (undo last saved decision)
    q -> quit (saves progress; you can resume later)

Notes:
 - The script filters to subreddits with subscribers >= 100000 by default.
 - Change MIN_SUBSCRIBERS at top if you want a different cutoff.
"""

import json
import csv
from pathlib import Path
from datetime import datetime

IN_PATH = Path("out/subreddits_metadata.json")
OUT_JSON = Path("out/subreddits_annotated.json")
OUT_CSV = Path("out/subreddits_annotated.csv")
MIN_SUBSCRIBERS = 100_000  # change if desired

def load_data():
    if not IN_PATH.exists():
        raise SystemExit(f"Input file not found: {IN_PATH.resolve()}")
    items = json.loads(IN_PATH.read_text(encoding="utf8"))
    # filter to numeric subs >= MIN_SUBSCRIBERS
    filtered = []
    for it in items:
        subs = it.get("subscribers")
        try:
            if subs is not None and int(subs) >= MIN_SUBSCRIBERS:
                filtered.append(it)
        except Exception:
            # skip items with non-numeric subscribers
            continue
    # sort by subscribers descending
    filtered.sort(key=lambda x: (x.get("subscribers") or 0), reverse=True)
    return filtered

def load_progress():
    if OUT_JSON.exists():
        annotated = json.loads(OUT_JSON.read_text(encoding="utf8"))
        # convert to dict by subreddit for quick lookup
        return {item["subreddit"]: item for item in annotated}
    return {}

def save_progress(annotated_dict):
    # annotated_dict: map subreddit -> annotated_item
    items = list(annotated_dict.values())
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf8")
    # also write CSV for easy viewing
    with OUT_CSV.open("w", encoding="utf8", newline="") as f:
        w = csv.writer(f)
        header = ["subreddit", "title", "subscribers", "avg_posts_per_day",
                  "recent_post_count", "recent_comment_count", "label", "label_time", "public_description"]
        w.writerow(header)
        for it in items:
            meta = it.get("metadata", {})
            row = [
                it.get("subreddit"),
                meta.get("title"),
                meta.get("subscribers"),
                meta.get("avg_posts_per_day"),
                meta.get("recent_post_count"),
                meta.get("recent_comment_count"),
                it.get("label"),
                it.get("label_time"),
                meta.get("public_description", "")[:300].replace("\n", " ")
            ]
            w.writerow(row)

def short_print(item):
    s = item.get("subreddit") or ""
    title = item.get("title") or ""
    subs = item.get("subscribers")
    avg_posts = item.get("avg_posts_per_day")
    recent_posts = item.get("recent_post_count")
    recent_comments = item.get("recent_comment_count")
    desc = (item.get("public_description") or "").strip()
    top_domains = item.get("top_external_domains") or []
    print("\n" + "="*80)
    print(f"r/{s} — {title}")
    print(f"subscribers: {subs:,}" if subs else "subscribers: N/A")
    print(f"avg_posts_per_day: {avg_posts}")
    print(f"recent_post_count (sampled): {recent_posts}")
    print(f"recent_comment_count (sampled): {recent_comments}")
    print("top_external_domains (sample):", top_domains[:6])
    print("\nDescription:")
    if desc:
        print(desc)
    else:
        print("[no description]")
    print("="*80)

def main():
    print("Loading data...")
    items = load_data()
    n = len(items)
    if n == 0:
        print(f"No subreddits with >= {MIN_SUBSCRIBERS} subscribers found in {IN_PATH}")
        return
    print(f"Loaded {n} subreddits with >= {MIN_SUBSCRIBERS} subscribers.")

    progress = load_progress()  # map subreddit->annotated item
    order = [it["subreddit"] for it in items]
    # find starting position: first unlabelled index
    idx = 0
    for i, name in enumerate(order):
        if name not in progress:
            idx = i
            break
        idx = i + 1  # if all labelled, idx becomes n

    history = []  # stack of subreddits in order labeled (for 'b' back)

    while idx < n:
        sub_name = order[idx]
        item = next((it for it in items if it["subreddit"] == sub_name), None)
        if item is None:
            idx += 1
            continue

        short_print(item)
        # if already labelled (shouldn't happen if we pick idx correctly) skip
        if sub_name in progress:
            print(f"[already labelled: {progress[sub_name]['label']}]")
            idx += 1
            continue

        # prompt
        print("\nLabel this subreddit: (type 1 = Relevant, 0 = Irrelevant, s = skip, b = back, q = quit/save)")
        ans = input("Your input: ").strip().lower()

        if ans == "1" or ans == "0":
            label = int(ans)
            annotated_item = {
                "subreddit": sub_name,
                "label": label,
                "label_time": datetime.utcnow().isoformat() + "Z",
                "metadata": {
                    "title": item.get("title"),
                    "subscribers": item.get("subscribers"),
                    "avg_posts_per_day": item.get("avg_posts_per_day"),
                    "recent_post_count": item.get("recent_post_count"),
                    "recent_comment_count": item.get("recent_comment_count"),
                    "public_description": item.get("public_description"),
                    "top_external_domains": item.get("top_external_domains")
                }
            }
            progress[sub_name] = annotated_item
            history.append(sub_name)
            # save after each label (resumable)
            save_progress(progress)
            print(f"Saved label {label} for r/{sub_name}. Progress: {len(progress)}/{n}")
            idx += 1
            continue

        if ans == "s":
            # mark as skipped (allows revisit later)
            annotated_item = {
                "subreddit": sub_name,
                "label": "skipped",
                "label_time": datetime.utcnow().isoformat() + "Z",
                "metadata": {
                    "title": item.get("title"),
                    "subscribers": item.get("subscribers"),
                    "avg_posts_per_day": item.get("avg_posts_per_day"),
                    "recent_post_count": item.get("recent_post_count"),
                    "recent_comment_count": item.get("recent_comment_count"),
                    "public_description": item.get("public_description"),
                    "top_external_domains": item.get("top_external_domains")
                }
            }
            progress[sub_name] = annotated_item
            history.append(sub_name)
            save_progress(progress)
            print(f"Skipped r/{sub_name}. Progress: {len(progress)}/{n}")
            idx += 1
            continue

        if ans == "b":
            # back one: remove last label if exists
            if not history:
                print("Nothing to go back to.")
                continue
            last = history.pop()
            if last in progress:
                del progress[last]
                save_progress(progress)
                print(f"Removed label for r/{last}. You will revisit it next.")
                # set idx to the index of last so loop re-visits it
                idx = order.index(last)
                continue
            else:
                print("Last labelled item not found in progress. Continuing.")
                continue

        if ans == "q":
            print("Quitting and saving progress...")
            save_progress(progress)
            print(f"Saved {len(progress)} labels. You can resume by running this script again.")
            return

        # invalid input
        print("Unrecognized input. Use 1, 0, s, b, or q.")

    # finished loop
    print("\nAll items iterated. Finalizing save...")
    save_progress(progress)
    print(f"Done. Total labelled/skipped: {len(progress)}/{n}")
    print(f"Annotated files: {OUT_JSON.resolve()}, {OUT_CSV.resolve()}")

if __name__ == "__main__":
    main()
