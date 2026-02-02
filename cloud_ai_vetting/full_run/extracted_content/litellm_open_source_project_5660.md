# LiteLLM Open source project
**URL:** https://docs.litellm.ai
**Page Title:** LiteLLM - Getting Started | liteLLM
--------------------

https://github.com/BerriAI/litellm
[LINK: https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)

## Call 100+ LLMs using the OpenAI Input/Output Format ​

- Translate inputs to provider's completion , embedding , and image_generation endpoints
- Consistent output , text responses will always be available at ['choices'][0]['message']['content']
[LINK: Consistent output](https://docs.litellm.ai/docs/completion/output)
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - Router
[LINK: Router](https://docs.litellm.ai/docs/routing)
- Track spend & set budgets per project LiteLLM Proxy Server
[LINK: LiteLLM Proxy Server](https://docs.litellm.ai/docs/simple_proxy)

## How to use LiteLLM ​

You can use litellm through either:
- LiteLLM Proxy Server - Server (LLM Gateway) to call 100+ LLMs, load balance, cost tracking across projects
- LiteLLM python SDK - Python Client to call 100+ LLMs, load balance, cost tracking

### When to use LiteLLM Proxy Server (LLM Gateway) ​

Use LiteLLM Proxy Server if you want a central service (LLM Gateway) to access multiple LLMs
Typically used by Gen AI Enablement /  ML PLatform Teams
- LiteLLM Proxy gives you a unified interface to access multiple LLMs (100+ LLMs)
- Track LLM Usage and setup guardrails
- Customize Logging, Guardrails, Caching per project

### When to use LiteLLM Python SDK ​

Use LiteLLM Python SDK if you want to use LiteLLM in your python code
Typically used by developers building llm projects
- LiteLLM SDK gives you a unified interface to access multiple LLMs (100+ LLMs)
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - Router
[LINK: Router](https://docs.litellm.ai/docs/routing)

## LiteLLM Python SDK ​

### Basic usage ​

- OpenAI
- Anthropic
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI

### Responses API ​

Use litellm.responses() for advanced models that support reasoning content like GPT-5, o3, etc.
- OpenAI
- Anthropic (Claude)
- VertexAI
- Azure OpenAI

### Streaming ​

Set stream=True in the completion args.
- OpenAI
- Anthropic
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI

### Exception handling ​

LiteLLM maps exceptions across all supported providers to the OpenAI exceptions. All our exceptions inherit from OpenAI's exception types, so any error-handling you have for that, should work out of the box with LiteLLM.

### Logging Observability - Log LLM Input/Output ( Docs ) ​

[LINK: Docs](https://docs.litellm.ai/docs/observability/callbacks)
LiteLLM exposes pre defined callbacks to send data to MLflow, Lunary, Langfuse, Helicone, Promptlayer, Traceloop, Slack

### Track Costs, Usage, Latency for streaming ​

Use a callback function for this - more info on custom callbacks: https://docs.litellm.ai/docs/observability/custom_callback
[LINK: https://docs.litellm.ai/docs/observability/custom_callback](https://docs.litellm.ai/docs/observability/custom_callback)

## LiteLLM Proxy Server (LLM Gateway) ​

Track spend across multiple projects/people
The proxy provides:
- Hooks for auth
[LINK: Hooks for auth](https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth)
- Hooks for logging
[LINK: Hooks for logging](https://docs.litellm.ai/docs/proxy/logging#step-1---create-your-custom-litellm-callback-class)
- Cost tracking
[LINK: Cost tracking](https://docs.litellm.ai/docs/proxy/virtual_keys#tracking-spend)
- Rate Limiting
[LINK: Rate Limiting](https://docs.litellm.ai/docs/proxy/users#set-rate-limits)

### 📖 Proxy Endpoints - Swagger Docs ​

[LINK: Swagger Docs](https://litellm-api.up.railway.app/)
Go here for a complete tutorial with keys + rate limits - here

### Quick Start Proxy - CLI ​

- pip package
- Docker container

### Step 1. CREATE config.yaml ​

Example litellm_config.yaml

### Step 2. RUN Docker Image ​

- Chat Completions
- Responses API

## More details ​

- exception mapping
[LINK: exception mapping](/docs/exception_mapping)
- E2E Tutorial for LiteLLM Proxy Server
[LINK: E2E Tutorial for LiteLLM Proxy Server](/docs/proxy/docker_quick_start)
- proxy virtual keys & spend management
[LINK: proxy virtual keys & spend management](/docs/proxy/virtual_keys)
- Call 100+ LLMs using the OpenAI Input/Output Format
- How to use LiteLLM When to use LiteLLM Proxy Server (LLM Gateway) When to use LiteLLM Python SDK
- When to use LiteLLM Proxy Server (LLM Gateway)
- When to use LiteLLM Python SDK
- LiteLLM Python SDK Basic usage Responses API Streaming Exception handling Logging Observability - Log LLM Input/Output (Docs) Track Costs, Usage, Latency for streaming
- Basic usage
- Responses API
[LINK: Responses API](#responses-api)
- Streaming
- Exception handling
- Logging Observability - Log LLM Input/Output (Docs)
[LINK: Logging Observability - Log LLM Input/Output (Docs)](#logging-observability---log-llm-inputoutput-docs)
- Track Costs, Usage, Latency for streaming
- LiteLLM Proxy Server (LLM Gateway) 📖 Proxy Endpoints - Swagger Docs Quick Start Proxy - CLI Step 1. CREATE config.yaml Step 2. RUN Docker Image
- 📖 Proxy Endpoints - Swagger Docs
[LINK: 📖 Proxy Endpoints - Swagger Docs](#-proxy-endpoints---swagger-docs)
- Quick Start Proxy - CLI
- Step 1. CREATE config.yaml
- Step 2. RUN Docker Image
- More details

--------------------