# dedupe_subreddits.py
import csv
from pathlib import Path

INPUT = "raw_subreddits.csv"    # your raw file
OUTPUT = "subreddits_clean.csv"  # cleaned output

def normalize_name(s: str) -> str:
    if not s:
        return ""
    s = s.strip()
    # remove leading 'r/' or '/r/' if present
    if s.lower().startswith("/r/"):
        s = s[3:]
    elif s.lower().startswith("r/"):
        s = s[2:]
    # remove stray non-alphanumeric chars at ends
    s = s.strip()
    # subreddit names can include underscores, numbers, hyphens
    # but remove spaces
    s = s.replace(" ", "")
    # lower-case to canonicalize
    return s.lower()

def read_input(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} not found.")
    names = []
    with path.open("r", encoding="utf8") as f:
        # try read as CSV if comma present, else plain lines
        first = f.readline()
        f.seek(0)
        f_lines = [line.strip() for line in f if line.strip()]
        # try to parse header vs plain list
    return f_lines

def dedupe_and_write(input_file=INPUT, output_file=OUTPUT):
    rows = read_input(input_file)
    seen = set()
    cleaned = []
    for row in rows:
        # if CSV with header, split by comma and try first field
        if "," in row:
            # pick first non-empty column
            parts = [c.strip() for c in row.split(",") if c.strip()]
            token = parts[0] if parts else row
        else:
            token = row
        norm = normalize_name(token)
        if not norm:
            continue
        if norm not in seen:
            seen.add(norm)
            cleaned.append(norm)
    # write CSV with header
    with open(output_file, "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["subreddit"])
        for s in cleaned:
            writer.writerow([s])
    print(f"Wrote {len(cleaned)} unique subreddits to {output_file}")

if __name__ == "__main__":
    dedupe_and_write()
