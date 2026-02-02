# Jan-nano-128k
**URL:** https://huggingface.co/Menlo/Jan-nano-128k
**Page Title:** Menlo/Jan-nano-128k · Hugging Face
--------------------


## Jan-Nano-128k: Empowering deeper research through extended context understanding.

Note: Jan-Nano is a non-thinking model.
Authors: Alan Dao , Bach Vu Dinh

## Overview

Jan-Nano-128k represents a significant advancement in compact language models for research applications. Building upon the success of Jan-Nano , this enhanced version features a native 128k context window that enables deeper, more comprehensive research capabilities without the performance degradation typically associated with context extension methods.
Key Improvements:
- 🔍 Research Deeper : Extended context allows for processing entire research papers, lengthy documents, and complex multi-turn conversations
- ⚡ Native 128k Window : Built from the ground up to handle long contexts efficiently, maintaining performance across the full context range
- 📈 Enhanced Performance : Unlike traditional context extension methods, Jan-Nano-128k shows improved performance with longer contexts
This model maintains full compatibility with Model Context Protocol (MCP) servers while dramatically expanding the scope of research tasks it can handle in a single session.

## Evaluation

Jan-Nano-128k has been rigorously evaluated on the SimpleQA benchmark using our MCP-based methodology, demonstrating superior performance compared to its predecessor:

## Why Jan-Nano-128k?

Traditional approaches to extending context length, such as YaRN (Yet another RoPE extensioN), often result in performance degradation as context length increases. Jan-Nano-128k breaks this paradigm:
This fundamental difference makes Jan-Nano-128k ideal for research applications requiring deep document analysis, multi-document synthesis, and complex reasoning over large information sets.

## 🖥️ How to Run Locally

Jan desktop will eventually support this model (WIP). Otherwise you can check the deployment options below that we have tested.
For additional tutorials and community guidance, visit our Discussion Forums .

### Deployment

Deploy using VLLM:
Or llama-server from llama.cpp :
Note: The chat template is included in the tokenizer. For troubleshooting, download the Non-think chat template .
[LINK: Non-think chat template](https://qwen.readthedocs.io/en/latest/_downloads/c101120b5bebcc2f12ec504fc93a965e/qwen3_nonthinking.jinja)

### Recommended Sampling Parameters

## FAQ:

- I have Jinja template issue with LMStudio, how can i fix? Here

## 🤝 Community & Support

- Discussions : HuggingFace Community
- Issues : GitHub Repository
[LINK: GitHub Repository](https://github.com/menloresearch/jan/issues)
- Documentation : Official Docs
[LINK: Official Docs](https://menloresearch.github.io/deep-research/)

## 📄 Citation

Jan-Nano-128k: Empowering deeper research through extended context understanding.

## Model tree for Menlo/Jan-nano-128k

Base model

## Collection including Menlo/Jan-nano-128k

## Paper for Menlo/Jan-nano-128k


--------------------