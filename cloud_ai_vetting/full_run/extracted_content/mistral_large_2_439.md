# Mistral Large 2
**URL:** https://huggingface.co/mistralai/Mistral-Large-Instruct-2411
**Page Title:** mistralai/Mistral-Large-Instruct-2411 · Hugging Face
--------------------


## Model Card for Mistral-Large-Instruct-2411

Mistral-Large-Instruct-2411 is an advanced dense Large Language Model (LLM) of 123B parameters with state-of-the-art reasoning, knowledge and coding capabilities extending Mistral-Large-Instruct-2407 with better Long Context, Function Calling and System Prompt.

## Key features

- Multi-lingual by design: Dozens of languages supported, including English, French, German, Spanish, Italian, Chinese, Japanese, Korean, Portuguese, Dutch and Polish.
- Proficient in coding: Trained on 80+ coding languages such as Python, Java, C, C++, Javacsript, and Bash. Also trained on more specific languages such as Swift and Fortran.
- Agent-centric: Best-in-class agentic capabilities with native function calling and JSON outputting.
- Advanced Reasoning: State-of-the-art mathematical and reasoning capabilities.
- Mistral Research License: Allows usage and modification for non-commercial usages.
- Large Context: A large 128k context window.
- Robust Context Adherence: Ensures strong adherence for RAG and large context applications.
- System Prompt: Maintains strong adherence and support for more reliable system prompts.

### System Prompt

We appreciate the feedback received from our community regarding our system prompt handling. In response, we have implemented stronger support for system prompts. To achieve optimal results, we recommend always including a system prompt that clearly outlines the bot's purpose, even if it is minimal.

### Basic Instruct Template (V7)

Be careful with subtle missing or trailing white spaces!
Please make sure to use mistral-common as the source of truth
[LINK: mistral-common](https://github.com/mistralai/mistral-common)

## Usage

The model can be used with the following frameworks
- vllm : See here
[LINK: vllm](https://github.com/vllm-project/vllm)

### vLLM

We recommend using this model with the vLLM library to implement production-ready inference pipelines.
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Installation
Make sure you install vLLM >= v0.6.4.post1 :
[LINK: vLLM >= v0.6.4.post1](https://github.com/vllm-project/vllm/releases/tag/v0.6.4.post1)
Also make sure you have mistral_common >= 1.5.0 installed:
[LINK: mistral_common >= 1.5.0](https://github.com/mistralai/mistral-common/releases/tag/v1.5.0)
You can also make use of a ready-to-go docker image or on the docker hub .
[LINK: docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile)

### Server

We recommand that you use Mistral-Large-Instruct-2411 in a server/client setting.
- Spin up a server:
Note: Running Mistral-Large-Instruct-2411 on GPU requires over 300 GB of GPU RAM.
- To ping the client you can use a simple Python snippet.

### Offline

### Improved Function Calling

Mistral-Large-2411 has much improved function calling capabilities that are fully supported 
using mistral_common >= 1.5.0 and vLLM >= v0.6.4.post1 .
[LINK: mistral_common >= 1.5.0](https://github.com/mistralai/mistral-common/releases/tag/v1.5.0)
[LINK: vLLM >= v0.6.4.post1](https://github.com/vllm-project/vllm/releases/tag/v0.6.4.post1)
Make sure to serve the model with the following flags in vLLM:

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Alok Kothari, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Augustin Garreau, Austin Birky, Bam4d, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Carole Rambaud, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Diogo Costa, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gaspard Blanchet, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Henri Roussez, Hichem Sattouf, Ian Mack, Jean-Malo Delignon, Jessica Chudnovsky, Justus Murke, Kartik Khandelwal, Lawrence Stewart, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Marjorie Janiewicz, Mickaël Seznec, Nicolas Schuhl, Niklas Muhs, Olivier de Garrigues, Patrick von Platen, Paul Jacob, Pauline Buche, Pavan Kumar Reddy, Perry Savas, Pierre Stock, Romain Sauvestre, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Wang, Théophile Gervet, Timothée Lacroix, Valera Nemychnikova, Wendy Shang, William El Sayed, William Marshall
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mistral-Large-Instruct-2411

## Spaces using mistralai/Mistral-Large-Instruct-2411 15


--------------------