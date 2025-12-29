#!/usr/bin/env python3
"""
resolve_discrepancies.py

Interactive resolver for disagreements between human labels and LLM labels.

Inputs:
  - out/subreddits_annotated.json   (from manual_vet.py)
  - out/subreddits_llm_labels.json  (from llm_label_and_eval.py)

Outputs (saved as you go):
  - out/subreddits_resolved.json    (full records with final_label)
  - out/subreddits_resolved.csv     (tabular with human/llm/final)
  - out/subreddits_final_relevant.csv (only final_label==1, first column prefixed with r/)

Usage:
  python resolve_discrepancies.py
"""
import json
import csv
from pathlib import Path
from datetime import datetime

IN_HUMAN = Path("out/subreddits_annotated.json")
IN_LLM = Path("out/subreddits_llm_labels.json")
OUT_RESOLVED_JSON = Path("out/subreddits_resolved.json")
OUT_RESOLVED_CSV = Path("out/subreddits_resolved.csv")
OUT_FINAL_CSV = Path("out/subreddits_final_relevant.csv")

def load_json(p):
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf8"))

def index_by_subreddit(list_of_objs, key_names=("subreddit", "subreddit")):
    idx = {}
    for obj in list_of_objs:
        # support different structures
        name = None
        for k in ("subreddit", "name"):
            if k in obj and obj[k]:
                name = obj[k]
                break
        # fallback: metadata.title
        if not name:
            meta = obj.get("metadata") or {}
            name = meta.get("title") or meta.get("subreddit")
        if not name:
            continue
        idx[str(name).lower()] = obj
    return idx

def safe_int(x):
    try:
        if x is None: return None
        return int(x)
    except Exception:
        return None

def save_resolved(resolved_map):
    items = list(resolved_map.values())
    OUT_RESOLVED_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_RESOLVED_JSON.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf8")

    # write CSV
    with OUT_RESOLVED_CSV.open("w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        header = ["subreddit","title","human_label","llm_label","final_label","human_description","llm_raw_response","subscribers","avg_posts_per_day","saved_at"]
        writer.writerow(header)
        for it in items:
            meta = it.get("metadata") or {}
            writer.writerow([
                it.get("subreddit"),
                meta.get("title") or "",
                it.get("human_label"),
                it.get("llm_label"),
                it.get("final_label"),
                (meta.get("public_description") or "")[:400].replace("\n"," "),
                (it.get("llm_raw_response") or "")[:500].replace("\n"," "),
                meta.get("subscribers") or "",
                meta.get("avg_posts_per_day") or "",
                it.get("final_time") or ""
            ])
    # write final relevant CSV with r/ prefix
    relevant = [it for it in items if it.get("final_label") == 1]
    with OUT_FINAL_CSV.open("w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["subreddit_prefixed","subreddit","title","subscribers","avg_posts_per_day"])
        for it in relevant:
            name = it.get("subreddit")
            title = (it.get("metadata") or {}).get("title") or ""
            subs = (it.get("metadata") or {}).get("subscribers") or ""
            avg_p = (it.get("metadata") or {}).get("avg_posts_per_day") or ""
            writer.writerow([f"r/{name}", name, title, subs, avg_p])

def main():
    human = load_json(IN_HUMAN)
    if human is None:
        raise SystemExit(f"Human annotations not found: {IN_HUMAN}")

    llm = load_json(IN_LLM)
    if llm is None:
        raise SystemExit(f"LLM outputs not found: {IN_LLM} - run LLM labeling first")

    human_idx = index_by_subreddit(human)
    llm_idx = index_by_subreddit(llm)

    # build master set of subreddits present in either file
    all_keys = set(human_idx.keys()) | set(llm_idx.keys())

    # prepare resolved map (load previous if exists)
    resolved_map = {}
    if OUT_RESOLVED_JSON.exists():
        try:
            prev = load_json(OUT_RESOLVED_JSON)
            for it in prev:
                resolved_map[str(it.get("subreddit","")).lower()] = it
            print(f"Loaded {len(resolved_map)} previously resolved items (resume mode).")
        except Exception:
            print("Failed to load previous resolved json; starting fresh.")

    # initialize entries: auto-fill agreed items
    for key in sorted(all_keys):
        if key in resolved_map:
            continue
        h = human_idx.get(key)
        l = llm_idx.get(key)
        human_label = safe_int(h.get("label") if h else None)
        llm_label = safe_int(l.get("llm_label") if l else l.get("llm_label") if l else None)
        # If llm file uses 'llm_label' or 'llm_label' as int; support both field names
        if l and llm_label is None:
            # try 'label' field in llm outputs (some scripts name it differently)
            llm_label = safe_int(l.get("label"))
        # Build base entry
        entry = {
            "subreddit": (h.get("subreddit") if h else (l.get("subreddit") if l else key)),
            "metadata": {
                "title": (h.get("metadata",{}).get("title") if h else l.get("description", "")[:80]) if (h or l) else "",
                "public_description": (h.get("metadata",{}).get("public_description") if h else (l.get("description") if l else "")),
                "subscribers": (h.get("metadata",{}).get("subscribers") if h else None),
                "avg_posts_per_day": (h.get("metadata",{}).get("avg_posts_per_day") if h else None),
            },
            "human_label": human_label,
            "llm_label": llm_label,
            "llm_raw_response": (l.get("raw_response") if l else None),
            "final_label": None,
            "final_time": None
        }
        # If both present and agree, auto-resolve
        if human_label in (0,1) and llm_label in (0,1) and human_label == llm_label:
            entry["final_label"] = human_label
            entry["final_time"] = datetime.utcnow().isoformat() + "Z"
        # if human present but llm missing, set final to human (trusted)
        elif human_label in (0,1) and llm_label is None:
            entry["final_label"] = human_label
            entry["final_time"] = datetime.utcnow().isoformat() + "Z"
        # if llm present but human missing, set final to llm (or choose to mark skipped) — choose llm to minimize manual work
        elif llm_label in (0,1) and human_label is None:
            entry["final_label"] = llm_label
            entry["final_time"] = datetime.utcnow().isoformat() + "Z"
        # else leave final_label None for interactive resolution (disagree or missing)
        resolved_map[key] = entry

    # build list of keys needing manual resolution: where human_label and llm_label both in {0,1} and differ
    need_keys = [k for k, v in resolved_map.items() if (v["human_label"] in (0,1) and v["llm_label"] in (0,1) and v["human_label"] != v["llm_label"] and v["final_label"] is None)]
    need_keys.sort(key=lambda k: (resolved_map[k].get("metadata",{}).get("subscribers") or 0), reverse=True)

    print(f"Total subreddits in dataset: {len(all_keys)}")
    print(f"Total already auto-resolved: {sum(1 for v in resolved_map.values() if v['final_label'] is not None)}")
    print(f"Total needing manual resolution (human != llm): {len(need_keys)}")
    print("You can quit at any time (press q) and resume later. Decisions are saved after each choice.\n")

    # interactive loop
    idx = 0
    while idx < len(need_keys):
        key = need_keys[idx]
        it = resolved_map[key]
        print("="*80)
        print(f"Item {idx+1}/{len(need_keys)} — subreddit: r/{it['subreddit']}")
        print(f"subs: {it['metadata'].get('subscribers')}, avg_posts/day: {it['metadata'].get('avg_posts_per_day')}")
        print(f"Human label: {it.get('human_label')}, LLM label: {it.get('llm_label')}")
        print("\nDescription (human):")
        print((it['metadata'].get('public_description') or "[none]")[:800])
        print("\nLLM raw response (truncated):")
        print((it.get("llm_raw_response") or "[none]")[:800])
        print("\nOptions: (h) accept human, (l) accept llm, (1) set final=1, (0) set final=0, (s) skip (leave unresolved), (b) back, (q) quit & save")
        ans = input("Your choice: ").strip().lower()
        if ans == "h":
            it["final_label"] = it.get("human_label")
            it["final_time"] = datetime.utcnow().isoformat() + "Z"
            print(f"Accepted human label {it['final_label']}")
            save_resolved(resolved_map)
            idx += 1
            continue
        if ans == "l":
            it["final_label"] = it.get("llm_label")
            it["final_time"] = datetime.utcnow().isoformat() + "Z"
            print(f"Accepted LLM label {it['final_label']}")
            save_resolved(resolved_map)
            idx += 1
            continue
        if ans == "1":
            it["final_label"] = 1
            it["final_time"] = datetime.utcnow().isoformat() + "Z"
            print("Set final_label = 1")
            save_resolved(resolved_map)
            idx += 1
            continue
        if ans == "0":
            it["final_label"] = 0
            it["final_time"] = datetime.utcnow().isoformat() + "Z"
            print("Set final_label = 0")
            save_resolved(resolved_map)
            idx += 1
            continue
        if ans == "s":
            print("Skipping for now (left unresolved).")
            idx += 1
            continue
        if ans == "b":
            if idx > 0:
                idx -= 1
            else:
                print("Already at first item.")
            continue
        if ans == "q":
            print("Saving progress and quitting...")
            save_resolved(resolved_map)
            print(f"Saved {len(resolved_map)} resolved entries to {OUT_RESOLVED_JSON} and CSV.")
            return
        print("Unrecognized input. Try again.")

    # finished: ensure everything has final_label (for any remaining None, default to human if present else llm else 0)
    for k, it in resolved_map.items():
        if it.get("final_label") is None:
            if it.get("human_label") in (0,1):
                it["final_label"] = it["human_label"]
            elif it.get("llm_label") in (0,1):
                it["final_label"] = it["llm_label"]
            else:
                it["final_label"] = 0
            it["final_time"] = datetime.utcnow().isoformat() + "Z"

    save_resolved(resolved_map)
    print("\nAll discrepancies processed (or auto-defaulted).")
    print(f"Saved resolved JSON: {OUT_RESOLVED_JSON.resolve()}")
    print(f"Saved resolved CSV:  {OUT_RESOLVED_CSV.resolve()}")
    print(f"Saved final relevant list CSV: {OUT_FINAL_CSV.resolve()}")
    # summary counts
    total = len(resolved_map)
    final_1 = sum(1 for v in resolved_map.values() if v.get("final_label")==1)
    final_0 = total - final_1
    print(f"\nFinal tally: total={total}, relevant (final_label==1)={final_1}, not relevant={final_0}")

if __name__ == "__main__":
    main()
