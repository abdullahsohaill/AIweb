#!/usr/bin/env python3
# count_shortlist.py
import json
from pathlib import Path
from collections import Counter

IN = Path("out/subreddits_annotated.json")
if not IN.exists():
    raise SystemExit(f"File not found: {IN.resolve()}")

data = json.loads(IN.read_text(encoding="utf8"))

# labels might be 1,0, or "skipped"
counts = Counter()
for it in data:
    lbl = it.get("label")
    counts[str(lbl)] += 1

total = len(data)
print(f"Total annotated items: {total}")
print(f"Relevant (1): {counts.get('1',0)}")
print(f"Irrelevant (0): {counts.get('0',0)}")
print(f"Skipped / other: {total - counts.get('1',0) - counts.get('0',0)}")
