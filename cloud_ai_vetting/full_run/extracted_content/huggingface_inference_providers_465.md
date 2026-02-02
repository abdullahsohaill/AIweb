# HuggingFace Inference Providers
**URL:** https://huggingface.co/docs/inference-providers/en/index
**Page Title:** Inference Providers
--------------------

Inference Providers documentation
Inference Providers

## Inference Providers

[LINK: 496](https://github.com/huggingface/hub-docs)
and get access to the augmented documentation experience
to get started

## Inference Providers

Hugging Face’s Inference Providers give developers access to hundreds of machine learning models, powered by world-class inference providers. They are also integrated into our client SDKs (for JS and Python), making it easy to explore serverless inference of models on your favorite providers.

## Partners

Our platform integrates with leading AI infrastructure providers, giving you access to their specialized capabilities through a single, consistent API. Here’s what each partner supports:

## Why Choose Inference Providers?

When you build AI applications, it’s tough to manage multiple provider APIs, comparing model performance, and dealing with varying reliability. Inference Providers solves these challenges by offering:
Instant Access to Cutting-Edge Models : Go beyond mainstream providers to access thousands of specialized models across multiple AI tasks. Whether you need the latest language models, state-of-the-art image generators, or domain-specific embeddings, you’ll find them here.
Zero Vendor Lock-in : Unlike being tied to a single provider’s model catalog, you get access to models from Cerebras, Groq, Together AI, Replicate, and more — all through one consistent interface.
Production-Ready Performance : Built for enterprise workloads with the reliability your applications demand.
Here’s what you can build:
- Text Generation : Use Large language models with tool-calling capabilities for chatbots, content generation, and code assistance
- Image and Video Generation : Create custom images and videos, including support for LoRAs and style customization
- Search & Retrieval : State-of-the-art embeddings for semantic search, RAG systems, and recommendation engines
- Traditional ML Tasks : Ready-to-use models for classification, NER, summarization, and speech recognition
⚡ Get Started for Free : Inference Providers includes a generous free tier, with additional credits for PRO users and Enterprise Hub organizations .

## Key Features

- 🎯 All-in-One API : A single API for text generation, image generation, document embeddings, NER, summarization, image classification, and more.
- 🔀 Multi-Provider Support : Easily run models from top-tier providers like fal, Replicate, Sambanova, Together AI, and others.
- 🚀 Scalable & Reliable : Built for high availability and low-latency performance in production environments.
- 🔧 Developer-Friendly : Simple requests, fast responses, and a consistent developer experience across Python and JavaScript clients.
- 👷 Easy to integrate : Drop-in replacement for the OpenAI chat completions API.
- 💰 Cost-Effective : No extra markup on provider rates.

## Getting Started

Inference Providers works with your existing development workflow. Whether you prefer Python, JavaScript, or direct HTTP calls, we provide native SDKs and OpenAI-compatible APIs to get you up and running quickly.
We’ll walk through a practical example using openai/gpt-oss-120b , a state-of-the-art open-weights conversational model.

### Inference Playground

Before diving into integration, explore models interactively with our Inference Playground . Test different chat completion models with your prompts and compare responses to find the perfect fit for your use case.

### Authentication

You’ll need a Hugging Face token to authenticate your requests. Create one by visiting your token settings and generating a fine-grained token with Make calls to Inference Providers permissions.
For complete token management details, see our security tokens guide .
[LINK: security tokens guide](https://huggingface.co/docs/hub/en/security-tokens)

### Quick Start - LLM

Let’s start with the most common use case: conversational AI using large language models. This section demonstrates how to perform chat completions using DeepSeek V3, showcasing the different ways you can integrate Inference Providers into your applications.
Whether you prefer our native clients, want OpenAI compatibility, or need direct HTTP access, we’ll show you how to get up and running with just a few lines of code.
Here are three ways to integrate Inference Providers into your Python applications, from high-level convenience to low-level control:
For convenience, the huggingface_hub library provides an InferenceClient that automatically handles provider selection and request routing.
[LINK: InferenceClient](https://huggingface.co/docs/huggingface_hub/guides/inference)
In your terminal, install the Hugging Face Hub Python client and log in:
You can now use the client with a Python interpreter.
By default, our system automatically routes your request to the first available provider for the specified model, following your preference order in Inference Provider settings .
You can change the provider selection policy by appending :fastest (selects the provider with highest throughput) or :cheapest (selects the provider with lowest price per output token) to the model id (e.g., openai/gpt-oss-120b:fastest ).
You can also select the provider of your choice by appending the provider name to the model id (e.g. "openai/gpt-oss-120b:sambanova" ).
Integrate Inference Providers into your JavaScript applications with these flexible approaches:
Our JavaScript SDK provides a convenient interface with automatic provider selection and TypeScript support.
Install with NPM:
Then use the client with Javascript.
By default, our system automatically routes your request to the first available provider for the specified model, following your preference order in Inference Provider settings .
You can change the provider selection policy by appending :fastest (selects the provider with highest throughput) or :cheapest (selects the provider with lowest price per output token) to the model id (e.g., openai/gpt-oss-120b:fastest ).
You can also select the provider of your choice by appending the provider name to the model id (e.g. "openai/gpt-oss-120b:sambanova" ).
For testing, debugging, or integrating with any HTTP client, here’s the raw REST API format.
By default, our system automatically routes your request to the first available provider for the specified model, following your preference order in Inference Provider settings .
You can change the provider selection policy by appending :fastest (selects the provider with highest throughput) or :cheapest (selects the provider with lowest price per output token) to the model id (e.g., openai/gpt-oss-120b:fastest ).
You can also select the provider of your choice by appending the provider name to the model id (e.g. "openai/gpt-oss-120b:sambanova" ).

### Quick Start - Text-to-Image Generation

Let’s explore how to generate images from text prompts using Inference Providers. We’ll use black-forest-labs/FLUX.1-dev , a state-of-the-art diffusion model that produces highly detailed, photorealistic images.
Use the huggingface_hub library for the simplest image generation experience with automatic provider selection:
Use our JavaScript SDK for streamlined image generation with TypeScript support:

## Provider Selection

The Inference Providers API acts as a unified proxy layer that sits between your application and multiple AI providers. Understanding how provider selection works is crucial for optimizing performance, cost, and reliability in your applications.

### API as a Proxy Service

When using Inference Providers, your requests go through Hugging Face’s proxy infrastructure, which provides several key benefits:
- Unified Authentication & Billing : Use a single Hugging Face token for all providers
- Automatic Failover : When using automatic provider selection ( provider="auto" ), requests are automatically routed to alternative providers if the primary provider is flagged as unavailable by our validation system
- Consistent Interface through client libraries : When using our client libraries, the same request format works across different providers
Because the API acts as a proxy, the exact HTTP request may vary between providers as each provider has their own API requirements and response formats. When using our official client libraries (JavaScript or Python), these provider-specific differences are handled automatically whether you use provider="auto" or specify a particular provider.

### Client-Side Provider Selection (Inference Clients)

When using the Hugging Face inference clients (JavaScript or Python), you can explicitly specify a provider or let the system choose automatically. The client then formats the HTTP request to match the selected provider’s API requirements.
Provider Selection Policy:
- provider: "auto" (default): Selects the first available provider for the model, sorted by your preference order in Inference Provider settings .
- provider: "specific-provider" : Forces use of a specific provider (e.g., “together”, “replicate”, “fal-ai”, …).

### Alternative: OpenAI-Compatible Chat Completions Endpoint (Chat Only)

If you prefer to work with familiar OpenAI APIs or want to migrate existing chat completion code with minimal changes, we offer a drop-in compatible endpoint that handles all provider selection automatically on the server side.
By default, the selected provider is the first available provider for the selected model, sorted by your preference order in Inference Provider settings .
You can change that policy by adding a suffix to the model name:
- :fastest selects the fastest provider for the model (highest throughput in tokens per second)
- :cheapest selects the most cost-efficient provider for the model (lowest price per output tokens)
Note : This OpenAI-compatible endpoint is currently available for chat completion tasks only. For other tasks like text-to-image, embeddings, or speech processing, use the Hugging Face inference clients shown above.
This endpoint can also be requested through direct HTTP access, making it suitable for integration with various HTTP clients and applications that need to interact with the chat completion service directly.
Key Features:
- Server-Side Provider Selection : The server automatically chooses the best available provider
- Model Listing : GET /v1/models returns available models across all providers
- OpenAI SDK Compatibility : Works with existing OpenAI client libraries
- Chat Tasks Only : Limited to conversational workloads

### Choosing the Right Approach

Use Inference Clients when:
- You need support for all task types (text-to-image, speech, embeddings, etc.)
- You want explicit control over provider selection
- You’re building applications that use multiple AI tasks
Use OpenAI-Compatible Endpoint when:
- You’re only doing chat completions
- You want to migrate existing OpenAI-based code with minimal changes
- You prefer server-side provider management
Use Direct HTTP when:
- You’re implementing custom request logic
- You need fine-grained control over the request/response cycle
- You’re working in environments without available client libraries

## Next Steps

Now that you understand the basics, explore these resources to make the most of Inference Providers:
- Announcement Blog Post : Learn more about the launch of Inference Providers
- Pricing and Billing : Understand costs and billing of Inference Providers
- Hub Integration : Learn how Inference Providers are integrated with the Hugging Face Hub
- Register as a Provider : Requirements to join our partner network as a provider
- Hub API : Advanced API features and configuration
[LINK: Hub API](./hub-api)
- API Reference : Complete parameter documentation for all supported tasks
[LINK: Update on GitHub](https://github.com/huggingface/hub-docs/blob/main/docs/inference-providers/index.md)
[LINK: Pricing and Billing →](/docs/inference-providers/en/pricing)

--------------------