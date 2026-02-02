import os
import json
import time
import pandas as pd
from openai import OpenAI
from tqdm import tqdm
from dotenv import load_dotenv
from pathlib import Path

# --- CONFIGURATION ---
INPUT_FILE = "content_metadata.csv"
OUTPUT_FILE = "annotated_results.csv"

# Using the specific snapshot for research consistency
# Note: If this model is not yet available to your tier, switch to 'gpt-4o-2024-08-06'
MODEL_NAME = "gpt-5.1-2025-11-13" 

# --- SETUP CLIENT ---
def setup_client():
    """Configure OpenAI client from local .env"""
    current_dir = Path(__file__).parent
    env_path = current_dir / ".env"
    if not env_path.exists():
        env_path = current_dir.parent / ".env"
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY not found in .env")
    return OpenAI(api_key=api_key)

def generate_prompt(tool_name, url, content):
    """Refined research prompt with improved integration signals and reasoning-focused instructions."""
    return f"""
ROLE: You are a technical researcher who is expert at annotating whether an AI tool or service is web-integrable.

TASK: Your task is to determine whether the tool/service "{tool_name}" ({url}) should be classified as a Web-Integrable AI Service.

DEFINITION: A Web-Integrable AI Service is defined by how it is integrated by developers. The defining property is that a third-party website or application CAN integrate this service on their webpage or backend AND CAN programmatically send data to the service and receive AI-generated output in return. This is typically achieved through exposed public APIs, SDKs, developer libraries, or embeddable scripts or widgets intended for integration into third-party websites or applications.

KEY QUESTION YOU MUST ANSWER TO ANNOTATE:
Can a developer write code on their own website or web application that sends data to the referenced AI service and uses its AI-generated response?

IMPORTANT:
- Do NOT rely on marketing language or buzzwords alone. Reason through the provided content to identify concrete technical signals such as developer documentation, JavaScript snippets or embeddable code, API references, SDK installation instructions, authentication or API key flows, example requests, or clearly described integration mechanisms.
- The programmatic access must explicitly expose the service's core AI functionality to the external application. Otherwise, it does not qualify.
- In contrast to a standalone consumer-facing service or app, these tools are designed for direct human interaction rather than programmatic use by third-party scripts or API calls.
- If both a consumer-facing UI and developer-facing integration exist, classify the tool as web-integrable.

OUTPUT FORMAT:
Return ONLY a valid JSON object with exactly the structure below. Do not include Markdown code blocks or conversational text.

{{
    "is_integrable": 1 or 0, 
    "reasoning": "Briefly describe your reasoning by citing the specific technical evidence found or the lack thereof."
}}

CONTENT:
{content[:25000]}
"""

# --- MAIN PROCESS ---
def main():
    try:
        client = setup_client()
    except ValueError as e:
        print(e)
        return

    # Load input CSV
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file {INPUT_FILE} not found.")
        return
    df = pd.read_csv(INPUT_FILE)

    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Resume from existing output if available
    if os.path.exists(OUTPUT_FILE):
        print("Resuming from existing output file...")
        results_df = pd.read_csv(OUTPUT_FILE)
        results_df.columns = [c.strip().lower().replace(" ", "_") for c in results_df.columns]
    else:
        results_df = df.copy()
        for col in ['llm_decision', 'llm_reasoning', 'abdullah_annotation']:
            if col not in results_df.columns:
                results_df[col] = None
        results_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Starting classification using {MODEL_NAME}...")

    # Iterate rows
    for index, row in tqdm(results_df.iterrows(), total=len(results_df)):
        if pd.notna(row.get('llm_decision')) and row['llm_decision'] != "":
            continue  # skip processed rows

        content_path = row.get('content_file')
        if pd.isna(content_path) or not str(content_path).strip() or not os.path.exists(str(content_path)):
            results_df.at[index, 'llm_decision'] = 0
            results_df.at[index, 'llm_reasoning'] = "Content file missing or invalid."
            continue

        try:
            with open(str(content_path), 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            results_df.at[index, 'llm_decision'] = 0
            results_df.at[index, 'llm_reasoning'] = "Error reading content file."
            continue

        if not content.strip():
            results_df.at[index, 'llm_decision'] = 0
            results_df.at[index, 'llm_reasoning'] = "Content file was empty."
            continue

        prompt = generate_prompt(
            row.get('tool_name', 'Unknown Tool'),
            row.get('url', 'Unknown URL'),
            content
        )

        # --- API CALL WITH RETRIES ---
        for retry in range(5):
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": "You are a precise technical research assistant. You output valid JSON only."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.0,
                    timeout=120.0
                )

                raw_content = response.choices[0].message.content
                # Strip markdown fences if present
                clean_json = raw_content.replace('```json', '').replace('```', '').strip()
                
                try:
                    data = json.loads(clean_json)
                except json.JSONDecodeError:
                    print(f"⚠️ Row {index}: Failed to parse JSON. Using fallback.")
                    data = {"is_integrable": 0, "reasoning": f"Failed to parse LLM output: {raw_content[:200]}"}

                results_df.at[index, 'llm_decision'] = data.get('is_integrable', 0)
                results_df.at[index, 'llm_reasoning'] = data.get('reasoning', 'No reasoning provided')
                results_df.to_csv(OUTPUT_FILE, index=False)
                break  # success, exit retry loop

            except Exception as e:
                err_str = str(e).lower()
                if "rate_limit" in err_str:
                    sleep_time = 2 ** retry
                    print(f"🚨 Rate limit hit. Sleeping {sleep_time}s...")
                    time.sleep(sleep_time)
                elif "model_not_found" in err_str:
                    print(f"❌ Model '{MODEL_NAME}' not found. Please check API access or switch model.")
                    return
                elif "context_length_exceeded" in err_str:
                     # Handle context error by failing gracefully for this row
                    results_df.at[index, 'llm_decision'] = 0
                    results_df.at[index, 'llm_reasoning'] = "Error: Content exceeded context window."
                    results_df.to_csv(OUTPUT_FILE, index=False)
                    break
                else:
                    print(f"⚠️ Row {index}: Unexpected error: {e}")
                    time.sleep(5)  # small pause and retry

    print(f"✅ Annotation complete. Results saved in {OUTPUT_FILE}")

if __name__ == "__main__":
    main()