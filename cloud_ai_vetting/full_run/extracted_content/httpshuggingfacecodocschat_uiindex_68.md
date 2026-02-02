# https://huggingface.co/docs/chat-ui/index
**URL:** https://huggingface.co/docs/chat-ui/index
**Page Title:** Chat UI
--------------------

Chat UI documentation
Chat UI

## Chat UI

[LINK: 10,452](https://github.com/huggingface/chat-ui)
and get access to the augmented documentation experience
to get started

## Chat UI

Open source chat interface with support for tools, multimodal inputs, and intelligent routing across models. The app uses MongoDB and SvelteKit behind the scenes. Try the live version called HuggingChat on hf.co/chat or setup your own instance .
Chat UI connects to any OpenAI-compatible API endpoint, making it work with:
- Hugging Face Inference Providers
[LINK: Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers)
- Ollama
- llama.cpp
[LINK: llama.cpp](https://github.com/ggerganov/llama.cpp)
- OpenRouter
- Any other OpenAI-compatible service
MCP Tools : Function calling via Model Context Protocol (MCP) servers
LLM Router : Intelligent routing to select the best model for each request
Multimodal : Image uploads on models that support vision
OpenID : Optional user authentication via OpenID Connect

## Quickstart

Step 1 - Create .env.local :
You can use any OpenAI-compatible endpoint:
Step 2 - Install and run:
That’s it! Chat UI will automatically discover available models from your endpoint.
MongoDB is optional for development. When MONGODB_URL is not set, Chat UI uses an embedded database that persists to ./db .
For production deployments, see the installation guides .
[LINK: Update on GitHub](https://github.com/huggingface/chat-ui/blob/main/docs/source/index.md)
[LINK: Local →](/docs/chat-ui/installation/local)

--------------------