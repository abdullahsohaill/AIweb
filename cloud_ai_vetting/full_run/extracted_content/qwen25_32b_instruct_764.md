# Qwen2.5-32B-Instruct
**URL:** https://huggingface.co/Qwen/Qwen2.5-32B-Instruct
**Page Title:** Qwen/Qwen2.5-32B-Instruct · Hugging Face
--------------------


## Qwen2.5-32B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:
- Significantly more knowledge and has greatly improved capabilities in coding and mathematics , thanks to our specialized expert models in these domains.
- Significant improvements in instruction following , generating long texts (over 8K tokens), understanding structured data (e.g, tables), and generating structured outputs especially JSON. More resilient to the diversity of system prompts , enhancing role-play implementation and condition-setting for chatbots.
- Long-context Support up to 128K tokens and can generate up to 8K tokens.
- Multilingual support for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more.
This repo contains the instruction-tuned 32B Qwen2.5 model , which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 32.5B
- Number of Paramaters (Non-Embedding): 31.0B
- Number of Layers: 64
- Number of Attention Heads (GQA): 40 for Q and 8 for KV
- Context Length: Full 131,072 tokens and generation 8192 tokens Please refer to this section for detailed instructions on how to deploy Qwen2.5 for handling long texts.
- Please refer to this section for detailed instructions on how to deploy Qwen2.5 for handling long texts.
For more details, please refer to our blog , GitHub , and Documentation .
[LINK: blog](https://qwenlm.github.io/blog/qwen2.5/)
[LINK: GitHub](https://github.com/QwenLM/Qwen2.5)
[LINK: Documentation](https://qwen.readthedocs.io/en/latest/)

## Requirements

The code of Qwen2.5 has been in the latest Hugging face transformers and we advise you to use the latest version of transformers .
With transformers<4.37.0 , you will encounter the following error:

## Quickstart

Here provides a code snippet with apply_chat_template to show you how to load the tokenizer and model and how to generate contents.

### Processing Long Texts

The current config.json is set for context length up to 32,768 tokens.
To handle extensive inputs exceeding 32,768 tokens, we utilize YaRN , a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts.
For supported frameworks, you could add the following to config.json to enable YaRN:
For deployment, we recommend using vLLM. 
Please refer to our Documentation for usage if you are not familar with vLLM.
Presently, vLLM only supports static YARN, which means the scaling factor remains constant regardless of input length, potentially impacting performance on shorter texts . 
We advise adding the rope_scaling configuration only when processing long contexts is required.
[LINK: Documentation](https://qwen.readthedocs.io/en/latest/deployment/vllm.html)

## Evaluation & Performance

Detailed evaluation results are reported in this 📑 blog .
[LINK: 📑 blog](https://qwenlm.github.io/blog/qwen2.5/)
For requirements on GPU memory and the respective throughput, see results here .
[LINK: here](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html)

## Citation

If you find our work helpful, feel free to give us a cite.

## Model tree for Qwen/Qwen2.5-32B-Instruct

Base model

## Spaces using Qwen/Qwen2.5-32B-Instruct 100

## Collection including Qwen/Qwen2.5-32B-Instruct

## Papers for Qwen/Qwen2.5-32B-Instruct

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Qwen/Qwen2.5-32B-Instruct is supported by the following Inference Providers:

--------------------