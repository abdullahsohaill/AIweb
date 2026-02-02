# Qwen2.5-Coder-7B-Instruct
**URL:** https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct
**Page Title:** Qwen/Qwen2.5-Coder-7B-Instruct · Hugging Face
--------------------


## Qwen2.5-Coder-7B-Instruct

## Introduction

Qwen2.5-Coder is the latest series of Code-Specific Qwen large language models (formerly known as CodeQwen). As of now, Qwen2.5-Coder has covered six mainstream model sizes, 0.5, 1.5, 3, 7, 14, 32 billion parameters, to meet the needs of different developers. Qwen2.5-Coder brings the following improvements upon CodeQwen1.5:
- Significantly improvements in code generation , code reasoning and code fixing . Base on the strong Qwen2.5, we scale up the training tokens into 5.5 trillion including source code, text-code grounding, Synthetic data, etc. Qwen2.5-Coder-32B has become the current state-of-the-art open-source codeLLM, with its coding abilities matching those of GPT-4o.
- A more comprehensive foundation for real-world applications such as Code Agents . Not only enhancing coding capabilities but also maintaining its strengths in mathematics and general competencies.
- Long-context Support up to 128K tokens.
This repo contains the instruction-tuned 7B Qwen2.5-Coder model , which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 7.61B
- Number of Paramaters (Non-Embedding): 6.53B
- Number of Layers: 28
- Number of Attention Heads (GQA): 28 for Q and 4 for KV
- Context Length: Full 131,072 tokens Please refer to this section for detailed instructions on how to deploy Qwen2.5 for handling long texts.
- Please refer to this section for detailed instructions on how to deploy Qwen2.5 for handling long texts.
For more details, please refer to our blog , GitHub , Documentation , Arxiv .
[LINK: blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
[LINK: GitHub](https://github.com/QwenLM/Qwen2.5-Coder)
[LINK: Documentation](https://qwen.readthedocs.io/en/latest/)

## Requirements

The code of Qwen2.5-Coder has been in the latest Hugging face transformers and we advise you to use the latest version of transformers .
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
[LINK: 📑 blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
For requirements on GPU memory and the respective throughput, see results here .
[LINK: here](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html)

## Citation

If you find our work helpful, feel free to give us a cite.

## Model tree for Qwen/Qwen2.5-Coder-7B-Instruct

Base model

## Spaces using Qwen/Qwen2.5-Coder-7B-Instruct 100

## Collection including Qwen/Qwen2.5-Coder-7B-Instruct

## Papers for Qwen/Qwen2.5-Coder-7B-Instruct

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Qwen/Qwen2.5-Coder-7B-Instruct is supported by the following Inference Providers:

--------------------