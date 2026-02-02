# create-llama
**URL:** https://blog.llamaindex.ai/create-llama-a-command-line-tool-to-generate-llamaindex-apps-8f7683021191
**Page Title:** create-llama, a command line tool to generate LlamaIndex apps
--------------------

Introducing create-llama , the easiest way to get started with LlamaIndex!
Update 2023–11–20: we now have a guide to deploying your create-llama apps !
Want to use the power of LlamaIndex to load, index and chat with your data using LLMs like GPT-4? It just got a lot easier! We’ve created a simple to use command-line tool that will generate a full-stack app just for you — just bring your own data! To get started, run:

## Ready to get started with LlamaCloud?

Explore our free and paid plans today.
- Learn more
The app will then ask you a series of questions about what kind of app you want. You’ll need to supply your own OpenAI API key (or you can customize it to use a different LLM), and make a few decisions.
[LINK: OpenAI API key](https://platform.openai.com/api-keys)

## How does it get my data?

The generated app has a data folder where you can put as many files as you want; the app will automatically index them at build time and after that you can quickly chat with them. If you’re using LlamaIndex.TS as the back-end (see below), you’ll be able to ingest PDF, text, CSV, Markdown, Word and HTML files. If you’re using the Python backend, you can read even more types, including audio and video files!

## Technical details

The front-end it generates is a Next.js application, with your choice of shadcn/ui or vanilla HTML and CSS for styling.
For the back-end, you have 3 options:
- Next.js : if you select this option, you’ll have a full stack Next.js application that you can deploy to a host like Vercel in just a few clicks. This uses LlamaIndex.TS , our TypeScript library.
- Express : if you want a more traditional Node.js application you can generate an Express backend. This also uses LlamaIndex.TS.
- Python FastAPI : if you select this option you’ll get a backend powered by the llama-index python package , which you can deploy to a service like Render or fly.io .
There are a couple of other questions you’ll be asked:
- Streaming or non-streaming: if you’re not sure, you’ll probably want a streaming backend.
- SimpleChatEngine or ContextChatEngine : the ContextChatEngine is the one that uses your data. If you just want to chat with GPT, you can use the SimpleChatEngine .

## Go forth and customize!

Once you’ve got your app up and running, you can customize it to your heart’s content! By default, for cost reasons, the app will use GPT-3.5-Turbo. If you’d like to use GPT-4 you can configure that by modifying the file app/api/chat/llamaindex-stream.ts (in the Next.js backend) or you can configure it to use a different LLM entirely! LlamaIndex has integrations with dozens of LLMs, both APIs and local.
Related articles

## Keep Reading

- Adding Native MCP to LlamaIndex Docs
Adding Native MCP to LlamaIndex Docs
[LINK: Adding Native MCP to LlamaIndex Docs](/blog/adding-native-mcp-to-llamaindex-docs)
- Beyond OCR: DeepSeek's New Vision Compression and How it Serves Document AI
Beyond OCR: DeepSeek's New Vision Compression and How it Serves Document AI
- SemTools: Are Coding Agents all you Need?
SemTools: Are Coding Agents all you Need?

## Start building your first document agent today

- Sign up for free
- Book a demo

--------------------