import json
import google.generativeai as genai

# --- CONFIGURATION ---
# PASTE YOUR API KEY HERE
GEMINI_API_KEY = "AIzaSyCBLkXX2dBhaDx9EMciFO51_tAHCfNVC-4" 

MODEL_NAME = "gemini-2.5-flash"
OUTPUT_FILE = "augmented_search_phrases.txt"

# Your specific local AI seed list
SEED_PHRASES = [
    "local AI tools",
    "in browser ai",
    "browser executed ai",
    "client side ai",
    "client side inference",
    "local inference web",
    "local inference browser",
    "on device ai web",
    "browser native ai",
    "ai running locally in browser",
    "offline ai browser",
    "local ai web integration",
    "web integrated local ai",
    "browser based local inference",
    "local compute ai web",
    "browser ai runtime",
    "local ai runtime browser",
    "ai executed on device web",
    "on device web ai",
    "local compute API for In-browser inference",
    "run local AI in browser",
    "on device runtime for browsers",
    "run on-device ML inference",
    "run models in the browser"
]

def setup_gemini():
    """Configures the Gemini client using the hardcoded key."""
    if "YOUR_ACTUAL_API_KEY_HERE" in GEMINI_API_KEY:
        raise ValueError("❌ Please paste your real API key in the GEMINI_API_KEY variable at the top of the script.")
    
    genai.configure(api_key=GEMINI_API_KEY)
    print(f"✅ Gemini API configured using model: {MODEL_NAME}")

def generate_prompt(seed_list):
    """Constructs the prompt exactly as requested."""
    list_str = "\n".join([f"- {phrase}" for phrase in seed_list])
    
    return f"""
    You are a research assistant for a web measurement study. The goal is to discover all forms of local-based, web-integrable AI/ML services, platforms, libraries, and APIs. 
    We are looking for technologies that allow AI to run **Client-Side** (in the user's browser or device) rather than via server-side API calls.

    **Current Search Phrases:**
    {list_str}

    Your task is to suggest any other highly effective search queries to augment this list.
    """

def main():
    try:
        setup_gemini()
        
        print("⏳ Generating augmented search queries...")
        model = genai.GenerativeModel(MODEL_NAME)
        
        prompt = generate_prompt(SEED_PHRASES)
        
        # Enforce JSON output via config
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        
        # Parse response
        try:
            new_queries = json.loads(response.text)
            # Handle case where API returns a dict instead of a list
            if isinstance(new_queries, dict):
                for val in new_queries.values():
                    if isinstance(val, list):
                        new_queries = val
                        break
        except json.JSONDecodeError:
            print("❌ Failed to parse JSON response. Raw output:")
            print(response.text)
            return

        # Deduplicate
        unique_new_queries = [q for q in new_queries if q not in SEED_PHRASES]
        
        print(f"✅ Generated {len(unique_new_queries)} new unique queries.")
        
        # Save to file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            # Write original seeds
            for q in SEED_PHRASES:
                f.write(f"{q}\n")
            
            # Write new queries
            for q in unique_new_queries:
                f.write(f"{q}\n")
                
        print(f"💾 Saved combined list to: {OUTPUT_FILE}")
        
        # Preview
        print("\n--- Preview of new queries ---")
        for q in unique_new_queries[:10]:
            print(f"- {q}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()