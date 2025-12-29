# seed_generator.py (Final, Supercharged Version)
# Purpose: To programmatically generate a massive and diverse list of search queries
# for discovering both cloud and local AI services.

import random

def generate_queries():
    """
    Generates an exhaustive set of search queries using multiple strategies
    to ensure we find both popular services and the long-tail of niche providers.
    """
    all_queries = set()

    # --- Foundational Keyword Lists (Massively Expanded) ---
    categories_market = [
        "AI", "LLM", "Machine Learning", "Generative AI", "Computer Vision", "NLP", "Speech Recognition",
        "Text-to-Speech", "Voice Cloning", "Image Generation", "Video Generation", "Document Processing",
        "OCR", "API", "SDK", "Chatbot", "AI Agent", "RAG", "Vector Database", "Embedding Models",
        "Data Extraction", "AI Infrastructure", "Developer Platform", "Local AI", "On-device AI",
        "Web AI", "Cloud AI", "AI Service", "AI Tool", "AI Platform", "AI Middleware", "AI Workflow",
        "MLOps", "AI Model", "Foundation Model"
    ]

    technical_tasks = [
        "voice cloning", "image classification", "sentiment analysis", "document OCR", "text summarization",
        "object detection", "face recognition", "language translation", "real-time transcription",
        "named entity recognition", "speech-to-text", "text-to-speech", "code generation",
        "image editing API", "video analysis API", "audio intelligence", "model inference",
        "model deployment", "data annotation", "model monitoring", "in-browser inference", "semantic search",
        "recommendation engine", "fraud detection", "speaker diarization", "lip sync", "motion capture",
        "geospatial analysis", "document verification", "form processing"
    ]

    known_services = [
        "OpenAI", "Anthropic", "Hugging Face", "Midjourney", "Replicate", "AWS Bedrock", "Vertex AI",
        "Azure OpenAI", "Cohere", "Stability AI", "ElevenLabs", "AssemblyAI", "Groq", "Perplexity AI",
        "Together AI", "Anyscale", "Fireworks AI", "Mistral AI", "RunPod", "DeepInfra", "LangChain",
        "LlamaIndex", "TensorFlow.js", "ONNX Runtime", "Pinecone", "Weaviate", "Gradio", "Streamlit",
        "ChromaDB", "Modal", "Baseten", "OctoAI"
    ]
    
    platforms = [
        "github.com", "medium.com", "dev.to", "stackoverflow.com", "producthunt.com",
        "rapidapi.com", "huggingface.co", "techcrunch.com", "venturebeat.com", "npmjs.com",
        "towardsdatascience.com", "analyticsvidhya.com", "indiehackers.com"
    ]
    
    years = ["2022", "2023", "2024", "2025"]

    # --- Strategy A: "Market Analyst" ---
    templates_market = [
        "best {cat} APIs {year}", "top {cat} platforms {year}", "cloud {cat} providers", "{cat} as a service",
        "list of {cat} APIs", "AI API marketplace", "AI API comparison {year}", "list of generative AI tools",
        "AI SaaS platforms", "emerging {cat} APIs {year}", "new AI APIs {year}", "{cat} landscape {year}"
    ]
    for template in templates_market:
        for cat in categories_market:
            all_queries.add(template.format(cat=cat, year=random.choice(years)))

    # --- Strategy B: "Software Developer" ---
    templates_developer = [
        "REST API for {tech_task}", "javascript library for {tech_task}", "python SDK for {tech_task}",
        "how to integrate {feature} API", "API for {feature}", "golang SDK for {tech_task}", "embeddable {feature} widget"
    ]
    features = ["chatbot", "AI search", "AI writer", "video generation", "recommendation engine", "AI agent framework", "RAG pipeline"]
    for template in templates_developer:
        if "{tech_task}" in template:
            for task in technical_tasks: all_queries.add(template.format(tech_task=task))
        if "{feature}" in template:
            for feat in features: all_queries.add(template.format(feature=feat))

    # --- Strategy C: "Competitor Discovery" ---
    templates_competitor = ["alternatives to {service}", "{service} competitors API", "API like {service}"]
    for template in templates_competitor:
        for service in known_services: all_queries.add(template.format(service=service))

    # --- Strategy D: Systematic Platform Search (THE QUERY EXPLOSION) ---
    for platform in platforms:
        for cat in categories_market: all_queries.add(f"site:{platform} {cat}")
        for task in technical_tasks: all_queries.add(f"site:{platform} {task}")

    # --- Strategy E: "Business & Pricing Model" ---
    pricing_terms = ["token based pricing", "pay-per-call API", "API usage pricing", "API free tier", "self-hosted AI pricing"]
    for term in pricing_terms:
        all_queries.add(f"\"{term}\" generative ai")
        all_queries.add(f"\"{term}\" machine learning")
        
    # --- Strategy F: "Documentation & Learning" ---
    for service in known_services:
        all_queries.add(f"\"{service} API documentation\"")
    for task in technical_tasks:
        all_queries.add(f"how to use {task} API")

    # --- Strategy G: "Industry & Use-Case Specific" ---
    # This finds niche SaaS tools marketed to specific sectors.
    industries = ["healthcare", "finance", "legal", "real estate", "ecommerce", "education", "gaming", "logistics"]
    business_functions = ["customer support", "marketing", "sales", "HR", "content creation", "compliance"]
    for industry in industries:
        all_queries.add(f"AI platform for {industry}")
        all_queries.add(f"generative AI in {industry}")
    for func in business_functions:
        all_queries.add(f"AI tool for {func}")
        all_queries.add(f"automate {func} with AI")

    # --- Strategy H: "Integration & Tech Stack" ---
    # This finds services based on how they connect with other developer tools.
    tech_stack = ["React", "Next.js", "Vue", "Shopify", "Wordpress", "Salesforce", "Zapier", "Bubble.io"]
    for tech in tech_stack:
        all_queries.add(f"AI API for {tech}")
        all_queries.add(f"integrate AI into {tech} app")
    for service1 in ["LangChain", "LlamaIndex"]:
        for service2 in ["Pinecone", "Weaviate", "ChromaDB", "Replicate"]:
            all_queries.add(f"{service1} with {service2} integration")

    return list(all_queries)

if __name__ == "__main__":
    queries = generate_queries()
    with open('exhaustive_search_queries.txt', 'w', encoding='utf-8') as f:
        for query in queries:
            f.write(f"{query}\n")
    print(f"Generated {len(queries)} unique and exhaustive search queries into 'exhaustive_search_queries.txt'")