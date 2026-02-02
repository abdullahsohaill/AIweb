# BYOM help center guide
**URL:** https://support.brave.app/hc/en-us/articles/34070140231821-How-do-I-use-the-Bring-Your-Own-Model-BYOM-with-Brave-Leo
**Page Title:** How do I use the Bring Your Own Model (BYOM) with Brave Leo? – Brave Help Center
--------------------


### Articles in this section

- How do I use Brave Leo?
- How do I use Skills in Brave Leo?
- How do I use AI Browsing in Brave?
- How to Use Multi Tab Context with Brave Leo
- How do I use Brave Leo [Android]?
- What are the differences between Leo's AI Models?
- How do I use the Bring Your Own Model (BYOM) with Brave Leo?
- How do I add my ChatGPT account to Brave Leo?
- How do I use Leo customization and memory features?
- How do I use Chat History in Brave Leo?
Brave Leo's Bring Your Own Model (BYOM) feature allows you to connect your own AI models to Leo, whether they're running locally on your device or hosted remotely. This gives you more control over your AI interactions while maintaining Brave's commitment to privacy.

### What is BYOM?

BYOM is an optional way to use Leo that lets you:
- Run local AI models directly on your device, keeping your data private
- Connect to your own remote model endpoints
- Use third-party APIs like OpenAI's ChatGPT
- Maintain end-to-end control of your AI interactions

### Requirements

In order to use BYOM, you will need:
- Brave Browser version 1.69 or higher
- Desktop platform (Windows, macOS, or Linux)
- For local models: A compatible serving framework (e.g., Ollama)
- For remote models: Valid API credentials for your chosen service

### Hardware Requirements for Local Models

- Minimum 8GB RAM
- Storage space depending on chosen model size (ranging from 829MB to 40GB)
- Sufficient processing power for model inference

### Model Selection

When running models locally, consider using models that match your hardware capabilities and use cases. For example, the LLama 3.2 models are optimized for multilingual dialogue and summarization tasks.
- Smaller variants ideal for resource-constrained devices: 3B variant (2.0GB) Outperforms similar-sized models on instruction following, summarization, and tool use Good for general-purpose tasks 1B variant Efficient for edge devices Suitable for personal information management and rewriting tasks
- 3B variant (2.0GB) Outperforms similar-sized models on instruction following, summarization, and tool use Good for general-purpose tasks
- Outperforms similar-sized models on instruction following, summarization, and tool use
- Good for general-purpose tasks
- 1B variant Efficient for edge devices Suitable for personal information management and rewriting tasks
- Efficient for edge devices
- Suitable for personal information management and rewriting tasks
- Officially supports 8 languages: English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai
- Trained on additional languages beyond the officially supported ones
View the full list of supported models on Ollama's model list .

### Setting Up BYOM

- First, set up a local model serving framework. For example, to use Ollama: Visit https://ollama.com/download Download and install Ollama for your platform Open terminal and pull your desired model (e.g., ollama pull deepseek-r1 )
- Visit https://ollama.com/download
- Download and install Ollama for your platform
- Open terminal and pull your desired model (e.g., ollama pull deepseek-r1 )
- Configure Leo to use your local model: Open Brave Settings Navigate to Leo settings Scroll to Bring your own model section Click Add new model Fill in the required fields: Label : Name that will appear in the model selection menu Model request name : The model identifier (e.g., "deepseek-r1") Server endpoint : Your local endpoint (for Ollama, use http://localhost:11434/v1/chat/completions ) API Key : Leave blank if not required by your framework
- Open Brave Settings
- Navigate to Leo settings
- Scroll to Bring your own model section
- Click Add new model
- Fill in the required fields: Label : Name that will appear in the model selection menu Model request name : The model identifier (e.g., "deepseek-r1") Server endpoint : Your local endpoint (for Ollama, use http://localhost:11434/v1/chat/completions ) API Key : Leave blank if not required by your framework
- Label : Name that will appear in the model selection menu
- Model request name : The model identifier (e.g., "deepseek-r1")
- Server endpoint : Your local endpoint (for Ollama, use http://localhost:11434/v1/chat/completions )
- API Key : Leave blank if not required by your framework

### Using Remote Models

To connect Leo to remote models or third-party APIs (like OpenAI's ChatGPT):
- Get your API credentials from your chosen provider
- In Brave, Settings > Leo > Bring your own model : Click Add new model Fill in the details: Label : Your chosen name for the model Model request name : The model identifier (e.g., "gpt-4" for OpenAI) Server endpoint : The API endpoint (e.g., https://api.openai.com/v1/chat/completions for OpenAI) API Key : Your authentication credentials
- Click Add new model
- Fill in the details: Label : Your chosen name for the model Model request name : The model identifier (e.g., "gpt-4" for OpenAI) Server endpoint : The API endpoint (e.g., https://api.openai.com/v1/chat/completions for OpenAI) API Key : Your authentication credentials
- Label : Your chosen name for the model
- Model request name : The model identifier (e.g., "gpt-4" for OpenAI)
- Server endpoint : The API endpoint (e.g., https://api.openai.com/v1/chat/completions for OpenAI)
- API Key : Your authentication credentials

### Using Your Model

Once configured:
- Open Leo in the browser
- Click the model selection menu
- Choose your custom model from the list
- Start chatting with your configured model

### Privacy and Security

Enabling alternative models using the BYOM feature gives you greater control over your experience and how your conversations are handled, but the privacy protections will vary. Brave Leo’s default settings ensure your data isn't stored, tracked, or used for training, and you can use the service without creating an account (See our Privacy Policy for more). Local and remote third party models will have different privacy characteristics.
- All processing happens directly on your device
- Conversations, webpages, and prompts never leave your machine
- Complete data privacy for sensitive information
When using BYOM with third-party services like OpenAI or other remote endpoints:
- Your data will be subject to the third party's privacy policies and data practices
- Brave's privacy protections (like the reverse proxy and data retention policies) do not apply
- The third party may: Store your conversations and inputs Use your data for model training Share or analyze your data according to their terms Have different data retention periods Process your data in various jurisdictions
- Store your conversations and inputs
- Use your data for model training
- Share or analyze your data according to their terms
- Have different data retention periods
- Process your data in various jurisdictions
Technical Implementation:
- Direct connection between your device and the model endpoint
- Requests bypass Brave's servers entirely
- Brave has no access to or visibility into the traffic
- API credentials are stored securely in your browser
- End-to-end control over your data and model interactions
💡 Important : Before using a third-party model, review their privacy policy and data handling practices. Do not submit sensitive personal information, health data, financial details, or other confidential information unless you are comfortable with how the third party handles such data. Before using a third-party model, review their privacy policy and data handling practices. Do not submit sensitive personal information, health data, financial details, or other confidential information unless you are comfortable with how the third party handles such data.

### Related articles

- What are the differences between Leo's AI Models?
- How do I use Brave Leo?
- How do I use Chat History in Brave Leo?
- How does Leo get current information?
- How do I fix file download errors?

--------------------