from bs4 import BeautifulSoup
import re
import json

def classify_with_heuristics(html_content, url):
    """Analyzes HTML content to determine if it's an AI service page."""
    
    # 1. Keyword Scoring
    score = 0
    text = BeautifulSoup(html_content, 'html.parser').get_text().lower()
    
    # High-value keywords
    high_value = ['api key', 'rest api', 'endpoint', 'sdk', 'inference', 'llm api', 'api reference']
    for keyword in high_value:
        if keyword in text:
            score += 15

    # Medium-value keywords
    medium_value = ['pricing', 'developer', 'docs', 'generative ai', 'machine learning', 'natural language processing', 'computer vision']
    for keyword in medium_value:
        if keyword in text:
            score += 5

    # 2. Structural Scoring
    soup = BeautifulSoup(html_content, 'html.parser')
    if soup.find('a', string=re.compile(r'API|Docs|Developers', re.IGNORECASE)):
        score += 20 # Strong signal if there's a dedicated developer section
    if soup.find('code') or soup.find('pre'):
        score += 10 # Code examples are a good sign
        
    # 3. Domain Scoring
    if 'api.' in url or 'dev.' in url:
        score += 25
        
    # 4. Final Decision & Extraction
    if score >= 40: # This threshold needs to be tuned
        service_name = soup.title.string if soup.title else url
        return {
            "is_ai_service": True,
            "service_name": service_name.strip(),
            "source_url": url,
            "confidence_score": min(score / 100.0, 1.0)
        }
    else:
        return {"is_ai_service": False}