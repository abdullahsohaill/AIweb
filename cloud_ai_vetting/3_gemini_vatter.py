import os
import csv
import json
import time
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path
from tqdm import tqdm

# --- CONFIGURATION ---
INPUT_FILE = "content_metadata.csv"
OUTPUT_FILE = "annotated_results.csv"
MODEL_NAME = "gemini-2.5-flash" 

GEMINI_API_KEY = "AIzaSyByFymWiabLlT3FHP-ruX8PatLZmVp63fQ" 

def setup_gemini():
    """Configures the Gemini client using the hardcoded key."""
    if "YOUR_ACTUAL_API_KEY_HERE" in GEMINI_API_KEY:
        raise ValueError("❌ Please paste your real API key in the GEMINI_API_KEY variable.")
    
    genai.configure(api_key=GEMINI_API_KEY)
    print(f"✅ Gemini API configured using model: {MODEL_NAME}")

def generate_prompt(tool_name, url, content):
    return f"""
    Act as a Technical Researcher. Your goal is to analyze the text provided below and determine if the tool "{tool_name}" ({url}) classifies as a **Web-Integrable Cloud AI Service**.

    A Web-Integrable Cloud AI Service is fundamentally defined by its ability to function as a building block for other software. Unlike standard consumer applications where a user logs in to perform a task manually, these services expose their AI capabilities—such as text generation, image processing, or data analysis—to external developers. This is typically achieved through public APIs, Software Development Kits (SDKs), or embeddable JavaScript widgets that allow the AI functionality to be triggered programmatically from a third-party website or application. Essentially, if a developer can write code to send data to this service and receive an AI-generated response back for use in their own product, it fits our definition. If the tool is a closed system designed solely for direct human interaction via its own dashboard, it does not.

    Based on the information below, evaluate whether this tool offers these integration capabilities. Return a JSON object with "is_integrable" set to 1 if it fits the description, or 0 if it does not, along with a "reasoning" field briefly explaining your decision.

    **Content:**
    {content[:20000]}
    """

def main():
    setup_gemini()
    model = genai.GenerativeModel(MODEL_NAME)
    
    # Load Input
    df = pd.read_csv(INPUT_FILE)
    
    # Check if output exists to resume
    if os.path.exists(OUTPUT_FILE):
        print("Resuming from existing output file...")
        results_df = pd.read_csv(OUTPUT_FILE)
    else:
        results_df = df.copy()
        results_df['gemini_decision'] = None
        results_df['gemini_reasoning'] = None
        results_df['Abdullah_Annotation'] = None 
        # Initialize file with headers
        results_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Starting classification...")

    # Iterate through rows
    for index, row in tqdm(results_df.iterrows(), total=len(results_df)):
        # Skip if already processed (check if decision is not NaN)
        if pd.notna(row['gemini_decision']):
            continue
            
        content_path = row['content_file']
        
        # --- FIX: ROBUST PATH CHECKING ---
        # 1. Check if path is NaN/None
        if pd.isna(content_path) or not str(content_path).strip():
            results_df.at[index, 'gemini_decision'] = 0
            results_df.at[index, 'gemini_reasoning'] = "Content extraction failed (No path)."
            continue

        # 2. Check if file exists on disk
        if not os.path.exists(str(content_path)):
            results_df.at[index, 'gemini_decision'] = 0
            results_df.at[index, 'gemini_reasoning'] = "Content file missing on disk."
            continue

        try:
            with open(str(content_path), 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ensure content isn't empty
            if not content.strip():
                 results_df.at[index, 'gemini_decision'] = 0
                 results_df.at[index, 'gemini_reasoning'] = "Extracted content was empty."
                 continue

            prompt = generate_prompt(row.get('Tool Name', row.get('tool_name')), row.get('Extracted URL', row.get('url')), content)
            
            response = model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            
            # Safe JSON parsing
            try:
                data = json.loads(response.text)
                decision = data.get('is_integrable', 0)
                reasoning = data.get('reasoning', 'No reasoning provided')
            except json.JSONDecodeError:
                decision = 0
                reasoning = "Error: Invalid JSON response from Gemini"
            
            # Update DataFrame in memory
            results_df.at[index, 'gemini_decision'] = decision
            results_df.at[index, 'gemini_reasoning'] = reasoning
            
            # Save IMMEDIATELY for fault tolerance
            results_df.to_csv(OUTPUT_FILE, index=False)
            
            time.sleep(1.0) # Rate limit pause

        except Exception as e:
            print(f"Error on row {index}: {e}")
            if "429" in str(e):
                print("🚨 API Quota Exceeded! Stopping. Run script again later to resume.")
                break

    print(f"✅ Vetting complete. Results in {OUTPUT_FILE}")

if __name__ == "__main__":
    main()