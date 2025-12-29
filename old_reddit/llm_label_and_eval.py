#!/usr/bin/env python3
# llm_label_and_eval.py
import os
import json
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from tqdm import tqdm

# ML metrics
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, cohen_kappa_score, confusion_matrix

# load env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise SystemExit("Set GEMINI_API_KEY in environment or .env")

# google-genai client
from google import genai
client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_ID = "gemini-2.0-flash"   # change if needed

IN = Path("out/subreddits_annotated.json")
OUT = Path("out/subreddits_llm_labels.json")

# PROMPT: strict one-digit output only
PROMPT_PREFIX = """
You are assisting an academic study identifying Reddit communities where people discuss AI technologies, tools, frameworks, platforms, or services.

Task: Decide if the subreddit described below is RELEVANT (1) or IRRELEVANT (0) to that focus.

Respond with exactly one character: "1" (Relevant) or "0" (Irrelevant). Return nothing else — no explanation or whitespace.

Relevance (1): subreddit discusses AI tools, services, frameworks, APIs, platforms, or applied AI technologies (models, LLMs, MLOps, deployments, SDKs, SaaS).
Irrelevance (0): no explicit focus on AI tools/services.

Now classify the following subreddit description. Output only the digit (1/0) and nothing else.
"""

SLEEP = 2
MAX_RETRIES = 8

def build_prompt(name, desc):
    # keep JSON-like input small
    return PROMPT_PREFIX + "\nInput: " + json.dumps({"name": name, "description": (desc or "")}, ensure_ascii=False) + "\nOutput:"

def safe_extract_digit(text):
    if not text:
        return None
    # find first 0 or 1 character
    for ch in text.strip():
        if ch in ("0","1"):
            return int(ch)
    # attempt to find digit anywhere
    for ch in text:
        if ch in ("0","1"):
            return int(ch)
    return None

def call_gemini(prompt):
    # uses models.generate_content API via google-genai
    resp = client.models.generate_content(model=MODEL_ID, contents=prompt)
    # resp.text is usually present; fallback to candidates
    text = getattr(resp, "text", None)
    if text is None:
        try:
            text = resp.candidates[0].content[0].text
        except Exception:
            text = str(resp)
    return text

def main():
    if not IN.exists():
        raise SystemExit(f"Input not found: {IN.resolve()}")

    data = json.loads(IN.read_text(encoding="utf8"))
    outputs = []
    to_eval_human = []
    to_eval_llm = []

    for it in tqdm(data, desc="LLM labeling"):
        name = it.get("subreddit") or it.get("metadata", {}).get("title") or ""
        desc = (it.get("metadata", {}) or it).get("public_description") or it.get("metadata", {}).get("public_description") or ""
        human_label = it.get("label")
        # skip ones that were skipped in manual vet
        if human_label not in (0,1):
            # still include in outputs but mark human None
            human_label = None

        prompt = build_prompt(name, desc)
        raw = None
        llm_label = None
        error = None
        for attempt in range(1, MAX_RETRIES+1):
            try:
                raw = call_gemini(prompt)
                llm_label = safe_extract_digit(raw)
                if llm_label is None:
                    raise RuntimeError("no digit found")
                break
            except Exception as e:
                error = f"attempt {attempt} failed: {e}"
                time.sleep(1.5 * attempt)
        time.sleep(SLEEP)

        out_item = {
            "subreddit": name,
            "description": desc,
            "human_label": human_label,
            "llm_label": llm_label,
            "raw_response": raw,
            "error": error,
            "time": datetime.utcnow().isoformat() + "Z"
        }
        outputs.append(out_item)

        if human_label in (0,1) and llm_label in (0,1):
            to_eval_human.append(human_label)
            to_eval_llm.append(llm_label)

    # save LLM outputs
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(outputs, indent=2, ensure_ascii=False), encoding="utf8")
    print(f"Saved LLM outputs to {OUT.resolve()}")

    # compute metrics if we have comparisons
    if len(to_eval_human) == 0:
        print("No comparable human labels found (maybe all were 'skipped'). Nothing to evaluate.")
        return

    y_true = to_eval_human
    y_pred = to_eval_llm

    acc = accuracy_score(y_true, y_pred)
    prec, rec, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="binary", pos_label=1)
    kappa = cohen_kappa_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)

    print("\n=== EVALUATION ===")
    print(f"Number compared: {len(y_true)}")
    print("Confusion matrix (rows=true 0/1, cols=pred 0/1):")
    print(cm)
    print(f"Accuracy: {acc:.3f}")
    print(f"Precision (pos=1): {prec:.3f}")
    print(f"Recall (pos=1):    {rec:.3f}")
    print(f"F1 (pos=1):        {f1:.3f}")
    print(f"Cohen's Kappa:     {kappa:.3f}")

if __name__ == "__main__":
    main()
