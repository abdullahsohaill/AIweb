# Mistral Small 3
**URL:** https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501
**Page Title:** mistralai/Mistral-Small-24B-Instruct-2501 · Hugging Face
--------------------


## Model Card for Mistral-Small-24B-Instruct-2501

Mistral Small 3 ( 2501 ) sets a new benchmark in the "small" Large Language Models category below 70B, boasting 24B parameters and achieving state-of-the-art capabilities comparable to larger models! This model is an instruction-fine-tuned version of the base model: Mistral-Small-24B-Base-2501 .
Mistral Small can be deployed locally and is exceptionally "knowledge-dense", fitting in a single RTX 4090 or a 32GB RAM MacBook once quantized. Perfect for:
- Fast response conversational agents.
- Low latency function calling.
- Subject matter experts via fine-tuning.
- Local inference for hobbyists and organizations handling sensitive data.
For enterprises that need specialized capabilities (increased context, particular modalities, domain specific knowledge, etc.), we will be releasing commercial models beyond what Mistral AI contributes to the community.
This release demonstrates our commitment to open source, serving as a strong base model.
Learn more about Mistral Small in our blog post .
Model developper: Mistral AI Team

## Key Features

- Multilingual: Supports dozens of languages, including English, French, German, Spanish, Italian, Chinese, Japanese, Korean, Portuguese, Dutch, and Polish.
- Agent-Centric: Offers best-in-class agentic capabilities with native function calling and JSON outputting.
- Advanced Reasoning: State-of-the-art conversational and reasoning capabilities.
- Apache 2.0 License: Open license allowing usage and modification for both commercial and non-commercial purposes.
- Context Window: A 32k context window.
- System Prompt: Maintains strong adherence and support for system prompts.
- Tokenizer: Utilizes a Tekken tokenizer with a 131k vocabulary size.

## Benchmark results

### Human evaluated benchmarks

Note :
- We conducted side by side evaluations with an external third-party vendor, on a set of over 1k proprietary coding and generalist prompts.
- Evaluators were tasked with selecting their preferred model response from anonymized generations produced by Mistral Small 3 vs another model.
- We are aware that in some cases the benchmarks on human judgement starkly differ from publicly available benchmarks, but have taken extra caution in verifying a fair evaluation. We are confident that the above benchmarks are valid.

### Publicly accesible benchmarks

Reasoning & Knowledge
Math & Coding
Instruction following
Note :
- Performance accuracy on all benchmarks were obtained through the same internal evaluation pipeline - as such, numbers may vary slightly from previously reported performance
( Qwen2.5-32B-Instruct , Llama-3.3-70B-Instruct , Gemma-2-27B-IT ).
[LINK: Qwen2.5-32B-Instruct](https://qwenlm.github.io/blog/qwen2.5/)
- Judge based evals such as Wildbench, Arena hard and MTBench were based on gpt-4o-2024-05-13.

### Basic Instruct Template (V7-Tekken)

<system_prompt> , <user message> and <assistant response> are placeholders.
Please make sure to use mistral-common as the source of truth
[LINK: mistral-common](https://github.com/mistralai/mistral-common)

## Usage

The model can be used with the following frameworks;
- vllm : See here
[LINK: vllm](https://github.com/vllm-project/vllm)
- transformers : See here
[LINK: transformers](https://github.com/huggingface/transformers)

### vLLM

We recommend using this model with the vLLM library to implement production-ready inference pipelines.
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Note 1 : We recommond using a relatively low temperature, such as temperature=0.15 .
Note 2 : Make sure to add a system prompt to the model to best tailer it for your needs. If you want to use the model as a general assistant, we recommend the following 
system prompt:
Installation
Make sure you install vLLM >= 0.6.4 :
[LINK: vLLM >= 0.6.4](https://github.com/vllm-project/vllm/releases/tag/v0.6.4)
Also make sure you have mistral_common >= 1.5.2 installed:
[LINK: mistral_common >= 1.5.2](https://github.com/mistralai/mistral-common/releases/tag/v1.5.2)
You can also make use of a ready-to-go docker image or on the docker hub .
[LINK: docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile)
We recommand that you use Mistral-Small-24B-Instruct-2501 in a server/client setting.
- Spin up a server:
Note: Running Mistral-Small-24B-Instruct-2501 on GPU requires ~55 GB of GPU RAM in bf16 or fp16.
- To ping the client you can use a simple Python snippet.

### Function calling

Mistral-Small-24-Instruct-2501 is excellent at function / tool calling tasks via vLLM. E.g.:

### Transformers

If you want to use Hugging Face transformers to generate text, you can do something like this.

### Ollama

Ollama can run this model locally on MacOS, Windows and Linux.
[LINK: Ollama](https://github.com/ollama/ollama)
4-bit quantization (aliased to default):
8-bit quantization:
FP16:
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mistral-Small-24B-Instruct-2501

Base model

## Spaces using mistralai/Mistral-Small-24B-Instruct-2501 100


--------------------