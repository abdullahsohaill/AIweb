# Get Started
**URL:** https://docs.browser-use.com/supported-models
**Page Title:** Supported Models - Browser Use
--------------------

- Introduction
- Human Quickstart
- LLM Quickstart
- Supported Models
- Going to Production
- Get Help
- Browser Use example
- Pricing
- Google Gemini example
- OpenAI example
- Anthropic example
- Azure OpenAI example
- Using the Responses API (for GPT-5.1 Codex models)
[LINK: Using the Responses API (for GPT-5.1 Codex models)](#using-the-responses-api-for-gpt-5-1-codex-models)
- AWS Bedrock example
- General AWS Bedrock (supports all providers)
- Anthropic Claude via AWS Bedrock (convenience class)
- AWS Authentication
- Groq example
- Oracle Cloud Infrastructure (OCI) example
- Ollama
- Langchain
- Qwen example
- ModelScope example
- Vercel AI Gateway example
- Other models (DeepSeek, Novita, X…)

### ​ Browser Use example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/browser_use_llm.py)
[LINK: Browser Use Cloud](https://cloud.browser-use.com/new-api-key)

### ​ Google Gemini example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/gemini.py)

### ​ OpenAI example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/gpt-4.1.py)

### ​ Anthropic example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/claude-4-sonnet.py)

### ​ Azure OpenAI example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/azure_openai.py)
- gpt-5.1-codex , gpt-5.1-codex-mini , gpt-5.1-codex-max
- gpt-5-codex , codex-mini-latest
- computer-use-preview
- 'auto' (default): Automatically uses Responses API for models that require it
- True : Force use of the Responses API
- False : Force use of the Chat Completions API

### ​ AWS Bedrock example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/aws.py)
- Environment variables ( AWS_ACCESS_KEY_ID , AWS_SECRET_ACCESS_KEY , AWS_DEFAULT_REGION )
- AWS profiles and credential files
- IAM roles (when running on EC2)
- Session tokens for temporary credentials
- AWS SSO authentication ( aws_sso_auth=True )

## ​ Groq example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/llama4-groq.py)

## ​ Oracle Cloud Infrastructure (OCI) example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/oci_models.py)
- Set up OCI configuration file at ~/.oci/config
- Have access to OCI Generative AI models in your tenancy
- Install the OCI Python SDK: uv add oci or pip install oci
- API_KEY : Uses API key authentication (default)
- INSTANCE_PRINCIPAL : Uses instance principal authentication
- RESOURCE_PRINCIPAL : Uses resource principal authentication

## ​ Ollama

- Install Ollama: https://github.com/ollama/ollama
[LINK: https://github.com/ollama/ollama](https://github.com/ollama/ollama)
- Run ollama serve to start the server
- In a new terminal, install the model you want to use: ollama pull llama3.1:8b (this has 4.9GB)

## ​ Langchain

[LINK: Example](https://github.com/browser-use/browser-use/blob/main/examples/models/langchain)

## ​ Qwen example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/qwen.py)

## ​ ModelScope example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/modelscope_example.py)

### ​ Vercel AI Gateway example

[LINK: example](https://github.com/browser-use/browser-use/blob/main/examples/models/vercel_ai_gateway.py)

## ​ Other models (DeepSeek, Novita, X…)

- DeepSeek
[LINK: DeepSeek](https://github.com/browser-use/browser-use/blob/main/examples/models/deepseek-chat.py)
- Novita
[LINK: Novita](https://github.com/browser-use/browser-use/blob/main/examples/models/novita.py)
- OpenRouter
[LINK: OpenRouter](https://github.com/browser-use/browser-use/blob/main/examples/models/openrouter.py)
Was this page helpful?

--------------------