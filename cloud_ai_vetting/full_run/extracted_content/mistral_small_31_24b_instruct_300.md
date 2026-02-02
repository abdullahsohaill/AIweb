# Mistral-Small-3.1-24B-Instruct
**URL:** https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503
**Page Title:** mistralai/Mistral-Small-3.1-24B-Instruct-2503 · Hugging Face
--------------------


## Model Card for Mistral-Small-3.1-24B-Instruct-2503

Building upon Mistral Small 3 (2501), Mistral Small 3.1 (2503) adds state-of-the-art vision understanding and enhances long context capabilities up to 128k tokens without compromising text performance. 
With 24 billion parameters, this model achieves top-tier capabilities in both text and vision tasks. This model is an instruction-finetuned version of: Mistral-Small-3.1-24B-Base-2503 .
Mistral Small 3.1 can be deployed locally and is exceptionally "knowledge-dense," fitting within a single RTX 4090 or a 32GB RAM MacBook once quantized.
It is ideal for:
- Fast-response conversational agents.
- Low-latency function calling.
- Subject matter experts via fine-tuning.
- Local inference for hobbyists and organizations handling sensitive data.
- Programming and math reasoning.
- Long document understanding.
- Visual understanding.
For enterprises requiring specialized capabilities (increased context, specific modalities, domain-specific knowledge, etc.), we will release commercial models beyond what Mistral AI contributes to the community.
Learn more about Mistral Small 3.1 in our blog post .

## Key Features

- Vision: Vision capabilities enable the model to analyze images and provide insights based on visual content in addition to text.
- Multilingual: Supports dozens of languages, including English, French, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Nepali, Polish, Portuguese, Romanian, Russian, Serbian, Spanish, Swedish, Turkish, Ukrainian, Vietnamese, Arabic, Bengali, Chinese, Farsi.
- Agent-Centric: Offers best-in-class agentic capabilities with native function calling and JSON outputting.
- Advanced Reasoning: State-of-the-art conversational and reasoning capabilities.
- Apache 2.0 License: Open license allowing usage and modification for both commercial and non-commercial purposes.
- Context Window: A 128k context window.
- System Prompt: Maintains strong adherence and support for system prompts.
- Tokenizer: Utilizes a Tekken tokenizer with a 131k vocabulary size.

## Benchmark Results

When available, we report numbers previously published by other model providers, otherwise we re-evaluate them using our own evaluation harness.

### Pretrain Evals

### Instruction Evals

### Multilingual Evals

### Long Context Evals

## Basic Instruct Template (V7-Tekken)

<system_prompt> , <user message> and <assistant response> are placeholders.
Please make sure to use mistral-common as the source of truth
[LINK: mistral-common](https://github.com/mistralai/mistral-common)

## Usage

The model can be used with the following frameworks;
- vllm (recommended) : See here
[LINK: vllm (recommended)](https://github.com/vllm-project/vllm)
Note 1 : We recommend using a relatively low temperature, such as temperature=0.15 .
Note 2 : Make sure to add a system prompt to the model to best tailer it for your needs. If you want to use the model as a general assistant, we recommend the following 
system prompt:

### vLLM (recommended)

We recommend using this model with the vLLM library to implement production-ready inference pipelines.
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Installation
Make sure you install vLLM >= 0.8.1 :
[LINK: vLLM >= 0.8.1](https://github.com/vllm-project/vllm/releases/tag/v0.8.1)
Doing so should automatically install mistral_common >= 1.5.4 .
[LINK: mistral_common >= 1.5.4](https://github.com/mistralai/mistral-common/releases/tag/v1.5.4)
To check:
You can also make use of a ready-to-go docker image or on the docker hub .
[LINK: docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile)
We recommand that you use Mistral-Small-3.1-24B-Instruct-2503 in a server/client setting.
- Spin up a server:
Note: Running Mistral-Small-3.1-24B-Instruct-2503 on GPU requires ~55 GB of GPU RAM in bf16 or fp16.
- To ping the client you can use a simple Python snippet.

### Function calling

Mistral-Small-3.1-24-Instruct-2503 is excellent at function / tool calling tasks via vLLM. E.g.:

### Transformers (untested)

Transformers-compatible model weights are also uploaded (thanks a lot @cyrilvallez). 
However the transformers implementation was not throughly tested , but only on "vibe-checks".
Hence, we can only ensure 100% correct behavior when using the original weight format with vllm (see above).
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mistral-Small-3.1-24B-Instruct-2503

Base model

## Spaces using mistralai/Mistral-Small-3.1-24B-Instruct-2503 83


--------------------