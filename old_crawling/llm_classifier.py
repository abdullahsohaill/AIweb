# llm_classifier.py
import google.generativeai as genai
import os
import pandas as pd
import json

# Configure with your API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

SYSTEM_PROMPT = """
You are an expert research assistant for a web measurement study. Your task is to analyze the raw HTML content of a webpage and determine if it describes a cloud-based AI service that can be integrated into other web applications via an API.

A "Cloud AI Service" is defined as a service hosted by a third party that provides AI functionality (like text generation, image analysis, speech-to-text, etc.) through a network API call (REST, GraphQL, WebSocket).

Analyze the provided HTML content and respond ONLY with a single, minified JSON object with the following structure:
{
  "is_ai_service": boolean,
  "service_name": "Name of the service if applicable, otherwise null",
  "category": "One of [Foundational Model API, Managed AI Platform, Specialized AI SaaS, API Aggregator, MLOps Platform, Other], or null",
  "description": "A concise, one-sentence description of the service, or null",
  "confidence_score": float (from 0.0 to 1.0, your confidence that this is a true AI service)
}

Base your decision on keywords like 'API', 'SDK', 'developer', 'inference', 'machine learning', 'LLM', 'endpoint', 'API key', 'REST API', pricing pages with token/usage models, and code examples. If the page is just a blog post *about* AI, a news article, or a general company homepage without clear developer/API information, set "is_ai_service" to false.
"""

def classify_html(html_content):
    try:
        response = model.generate_content(SYSTEM_PROMPT + "\n\nHTML CONTENT:\n" + html_content)
        # Add post-processing here to clean and parse the JSON from the response text
        return json.loads(response.text.strip())
    except Exception as e:
        print(f"LLM classification failed: {e}")
        return None

if __name__ == "__main__":
    html_files_dir = 'crawled_html/'
    classified_results = []
    
    for filename in os.listdir(html_files_dir):
        if filename.endswith('.html'):
            with open(os.path.join(html_files_dir, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                result = classify_html(content)
                if result and result['is_ai_service']:
                    # Add the original source URL back for traceability
                    result['source_url'] = filename.replace('_', '/') # A trick to store URL in filename
                    classified_results.append(result)

    df = pd.DataFrame(classified_results)
    df.to_csv('classified_ai_services.csv', index=False)