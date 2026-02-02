# Devstral-Small-2507
**URL:** https://huggingface.co/mistralai/Devstral-Small-2507
**Page Title:** mistralai/Devstral-Small-2507 · Hugging Face
--------------------


## Devstral Small 1.1

Devstral is an agentic LLM for software engineering tasks built under a collaboration between Mistral AI and All Hands AI 🙌. Devstral excels at using tools to explore codebases, editing multiple files and power software engineering agents. The model achieves remarkable performance on SWE-bench which positions it as the #1 open source model on this benchmark .
It is finetuned from Mistral-Small-3.1 , therefore it has a long context window of up to 128k tokens. As a coding agent, Devstral is text-only and before fine-tuning from Mistral-Small-3.1 the vision encoder was removed.
For enterprises requiring specialized capabilities (increased context, domain-specific knowledge, etc.), we will release commercial models beyond what Mistral AI contributes to the community.
Learn more about Devstral in our blog post .
Updates compared to Devstral Small 1.0 :
- Improved performance, please refer to the benchmark results .
- Devstral Small 1.1 is still great when paired with OpenHands. This new version also generalizes better to other prompts and coding environments.
- Supports Mistral's function calling format .
[LINK: Mistral's function calling format](https://mistralai.github.io/mistral-common/usage/tools/)

## Key Features:

- Agentic coding : Devstral is designed to excel at agentic coding tasks, making it a great choice for software engineering agents.
- lightweight : with its compact size of just 24 billion parameters, Devstral is light enough to run on a single RTX 4090 or a Mac with 32GB RAM, making it an appropriate model for local deployment and on-device use.
- Apache 2.0 License : Open license allowing usage and modification for both commercial and non-commercial purposes.
- Context Window : A 128k context window.
- Tokenizer : Utilizes a Tekken tokenizer with a 131k vocabulary size.

## Benchmark Results

### SWE-Bench

Devstral Small 1.1 achieves a score of 53.6% on SWE-Bench Verified, outperforming Devstral Small 1.0 by +6,8% and the second best state of the art model by +11.4%.
When evaluated under the same test scaffold (OpenHands, provided by All Hands AI 🙌), Devstral exceeds far larger models such as Deepseek-V3-0324 and Qwen3 232B-A22B.

## Usage

We recommend to use Devstral with the OpenHands scaffold.
You can use it either through our API or by running locally.
[LINK: OpenHands](https://github.com/All-Hands-AI/OpenHands/tree/main)

### API

Follow these instructions to create a Mistral account and get an API key.
[LINK: instructions](https://docs.mistral.ai/getting-started/quickstart/#account-setup)
Then run these commands to start the OpenHands docker container.

### Local inference

The model can also be deployed with the following libraries:
- vllm (recommended) : See here
[LINK: vllm (recommended)](https://github.com/vllm-project/vllm)
- mistral-inference : See here
[LINK: mistral-inference](https://github.com/mistralai/mistral-inference)
- transformers : See here
[LINK: transformers](https://github.com/huggingface/transformers)
- LMStudio : See here
- llama.cpp : See here
[LINK: llama.cpp](https://github.com/ggml-org/llama.cpp)
- ollama : See here
[LINK: ollama](https://github.com/ollama/ollama)
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Installation
Make sure you install vLLM >= 0.9.1 :
[LINK: vLLM >= 0.9.1](https://github.com/vllm-project/vllm/releases/tag/v0.9.1)
Also make sure to have installed mistral_common >= 1.7.0 .
[LINK: mistral_common >= 1.7.0](https://github.com/mistralai/mistral-common/releases/tag/v1.7.0)
To check:
You can also make use of a ready-to-go docker image or on the docker hub .
[LINK: docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile)
Launch server
We recommand that you use Devstral in a server/client setting.
- Spin up a server:
- To ping the client you can use a simple Python snippet.
Installation
Make sure to have mistral_inference >= 1.6.0 installed.
Download
Chat
You can run the model using the following command:
You can then prompt it with anything you'd like.
[LINK: installed](https://github.com/mistralai/mistral-common)
Then load our tokenizer along with the model and generate:
- LM Studio GGUF repository (recommended): https://huggingface.co/lmstudio-community/Devstral-Small-2507-GGUF
- our GGUF repository: https://huggingface.co/mistralai/Devstral-Small-2507_gguf
You can serve the model locally with LMStudio .
- Download LM Studio and install it
- Install lms cli ~/.lmstudio/bin/lms bootstrap
- In a bash terminal, run lms import Devstral-Small-2507-Q4_K_M.gguf in the directory where you've downloaded the model checkpoint (e.g. Devstral-Small-2507_gguf )
- Open the LM Studio application, click the terminal icon to get into the developer tab. Click select a model to load and select Devstral Small 2507 . Toggle the status button to start the model, in setting toggle Serve on Local Network to be on.
- On the right tab, you will see an API identifier which should be devstral-small-2507 and an api address under API Usage. Keep note of this address, this is used for OpenHands or Cline.
Then run Devstral using the llama.cpp server.

### OpenHands (recommended)

Make sure you launched an OpenAI-compatible server such as vLLM or Ollama as described above. Then, you can use OpenHands to interact with Devstral Small 1.1 .
In the case of the tutorial we spineed up a vLLM server running the command:
The server address should be in the following format: http://<your-server-url>:8000/v1
You can follow installation of OpenHands here .
[LINK: here](https://docs.all-hands.dev/modules/usage/installation)
The easiest way to launch OpenHands is to use the Docker image:
Then, you can access the OpenHands UI at http://localhost:3000 .
When accessing the OpenHands UI, you will be prompted to connect to a server. You can use the advanced mode to connect to the server you launched earlier.
Fill the following fields:
- Custom Model : openai/mistralai/Devstral-Small-2507
- Base URL : http://<your-server-url>:8000/v1
- API Key : token (or any other token you used to launch the server if any)

### Cline

Make sure you launched an OpenAI-compatible server such as vLLM or Ollama as described above. Then, you can use OpenHands to interact with Devstral Small 1.1 .
In the case of the tutorial we spineed up a vLLM server running the command:
The server address should be in the following format: http://<your-server-url>:8000/v1
You can follow installation of Cline here . Then you can configure the server address in the settings.
[LINK: here](https://docs.cline.bot/getting-started/installing-cline)

### Examples

We can start the OpenHands scaffold and link it to a repo to analyze test coverage and identify badly covered files.
Here we start with our public mistral-common repo.
After the repo is mounted in the workspace, we give the following instruction
The agent will first browse the code base to check test configuration and structure.
Then it sets up the testing dependencies and launches the coverage test:
Finally, the agent writes necessary code to visualize the coverage, export the results and save the plots to a png.
At the end of the run, the following plots are produced:
and the model is able to explain the results:
First initialize Cline inside VSCode and connect it to the server you launched earlier.
We give the following instruction to builde the video game:
The agent will first create the game:
Then it will explain how to launch the game:
Finally, the game is ready to be played:
Don't hesitate to iterate or give more information to Devstral to improve the game!
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Devstral-Small-2507

Base model

## Spaces using mistralai/Devstral-Small-2507 10


--------------------