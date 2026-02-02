import os
import json
import sys
import pandas as pd
from openai import OpenAI
from tqdm import tqdm
from dotenv import load_dotenv
from pathlib import Path
import asyncio

# --- CONFIGURATION ---
INPUT_FILE = "annotated_results.csv"
MODEL_NAME = "gpt-5.1-2025-11-13" 

# --- SETUP CLIENT ---
def setup_client():
    current_dir = Path(__file__).parent
    env_path = current_dir / ".env"
    if not env_path.exists(): env_path = current_dir.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key: raise ValueError("❌ OPENAI_API_KEY not found in .env")
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

async def get_new_decision(client, row):
    content_path = row.get('content_file')
    if pd.isna(content_path) or not os.path.exists(str(content_path)):
        return {"is_integrable": 0, "reasoning": "Content file missing."}

    with open(str(content_path), 'r', encoding='utf-8') as f:
        content = f.read()

    prompt = generate_prompt(row.get('tool_name'), row.get('url'), content)

    try:
        response = await asyncio.to_thread(
            client.chat.completions.create,
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a precise technical research assistant. You output valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        raw_content = response.choices[0].message.content
        return json.loads(raw_content)
    except Exception as e:
        return {"is_integrable": -1, "reasoning": f"API Error: {e}"} # Use -1 for error

async def main():
    try:
        client = setup_client()
    except ValueError as e:
        print(e)
        return

    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file {INPUT_FILE} not found.")
        return
        
    results_df = pd.read_csv(INPUT_FILE)
    results_df.columns = [c.strip().lower().replace(" ", "_") for c in results_df.columns]
    
    results_df['abdullah_annotation'] = pd.to_numeric(results_df['abdullah_annotation'], errors='coerce')
    results_df['llm_decision'] = pd.to_numeric(results_df['llm_decision'], errors='coerce')
    
    disagreements = results_df[
        (pd.notna(results_df['abdullah_annotation'])) &
        (pd.notna(results_df['llm_decision'])) &
        (results_df['abdullah_annotation'] != results_df['llm_decision'])
    ].copy()

    if disagreements.empty:
        print("✅ No disagreements found.")
        return

    print(f"--- 🕵️‍♀️ AUDITING {len(disagreements)} DISAGREEMENTS ---")
    
    tasks = [get_new_decision(client, row) for _, row in disagreements.iterrows()]
    new_decisions = await asyncio.gather(*tasks)
    
    disagreements['new_llm_decision'] = [d.get('is_integrable', -1) for d in new_decisions]
    
    # --- FINAL REPORT ---
    print("\n\n--- AUDIT REPORT ---")
    
    align_count = 0
    for index, row in disagreements.iterrows():
        your_vote = int(row['abdullah_annotation'])
        old_llm_vote = int(row['llm_decision'])
        new_llm_vote = int(row['new_llm_decision'])

        status = "✅ ALIGNED" if your_vote == new_llm_vote else "❌ STILL DISAGREES"
        if your_vote == new_llm_vote:
            align_count += 1
            
        print(f"\n--- {row.get('tool_name')} ---")
        print(f"Status: {status}")
        print(f"  - Your Annotation:      {your_vote}")
        print(f"  - OLD LLM Decision:     {old_llm_vote}")
        print(f"  - NEW LLM Decision:     {new_llm_vote}")
    
    print("\n--- SUMMARY ---")
    print(f"Total Disagreements Audited: {len(disagreements)}")
    print(f"Aligned with your Vetting:   {align_count} / {len(disagreements)} ({align_count/len(disagreements):.1%})")

if __name__ == "__main__":
    # To run async functions in a script
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())