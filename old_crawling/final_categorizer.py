import google.generativeai as genai
import pandas as pd
import json

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

SYSTEM_PROMPT_CATEGORIZER = """
You are an expert AI market analyst. Based on the service name and its description, classify it into a primary use-case and a service type.

Respond ONLY with a single, minified JSON object with the following structure:
{
  "use_case_category": "One of [Text Generation, Image Generation, Speech-to-Text, Text-to-Speech, Computer Vision, Data Analytics, Code Generation, AI Agent, Other]",
  "service_type_category": "One of [Foundational Model API, Managed AI Platform, Specialized AI SaaS, API Aggregator, MLOps Platform]"
}
"""

def categorize_service(name, description):
    prompt = f"Service Name: {name}\nDescription: {description}"
    try:
        response = model.generate_content(SYSTEM_PROMPT_CATEGORIZER + "\n\n" + prompt)
        return json.loads(response.text.strip())
    except:
        return {"use_case_category": "Unknown", "service_type_category": "Unknown"}

if __name__ == "__main__":
    ranked_services_df = pd.read_csv('final_ranked_ai_services.csv')
    
    # You would need to get descriptions for each service, perhaps from the first LLM pass
    # or a quick scrape of the title/meta description.
    # For this example, we'll assume a 'description' column exists.
    
    categorization_results = ranked_services_df.apply(
        lambda row: categorize_service(row['service_name'], row.get('description', '')), 
        axis=1
    )
    
    final_df = pd.concat([ranked_services_df, pd.json_normalize(categorization_results)], axis=1)
    final_df.to_csv('FINAL_AI_ARTIFACT_REGISTRY.csv', index=False)