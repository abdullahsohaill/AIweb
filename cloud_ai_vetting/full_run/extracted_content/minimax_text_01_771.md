# MiniMax-Text-01
**URL:** https://huggingface.co/MiniMaxAI/MiniMax-Text-01
**Page Title:** MiniMaxAI/MiniMax-Text-01 · Hugging Face
--------------------

[LINK: WeChat](https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg)

## MiniMax-Text-01

## 1. Introduction

MiniMax-Text-01 is a powerful language model with 456 billion total parameters, of which 45.9 billion are activated per token. To better unlock the long context capabilities of the model, MiniMax-Text-01 adopts a hybrid architecture that combines Lightning Attention, Softmax Attention and Mixture-of-Experts (MoE). Leveraging advanced parallel strategies and innovative compute-communication overlap methods—such as Linear Attention Sequence Parallelism Plus (LASP+), varlen ring attention, Expert Tensor Parallel (ETP), etc., MiniMax-Text-01's training context length is extended to 1 million tokens, and it can handle a context of up to 4 million tokens during the inference. On various academic benchmarks, MiniMax-Text-01 also demonstrates the performance of a top-tier model.

## 2. Model Architecture

The architecture of MiniMax-Text-01 is briefly described as follows:
- Total Parameters: 456B
- Activated Parameters per Token: 45.9B
- Number Layers: 80
- Hybrid Attention: a softmax attention is positioned after every 7 lightning attention. Number of attention heads: 64 Attention head dimension: 128
- Number of attention heads: 64
- Attention head dimension: 128
- Mixture of Experts: Number of experts: 32 Expert hidden dimension: 9216 Top-2 routing strategy
- Number of experts: 32
- Expert hidden dimension: 9216
- Top-2 routing strategy
- Positional Encoding: Rotary Position Embedding (RoPE) applied to half of the attention head dimension with a base frequency of 10,000,000
- Hidden Size: 6144
- Vocab Size: 200,064

## 3. Evaluation

### Core Academic Benchmarks

* Evaluated following a 0-shot CoT setting.

### Long Benchmarks

## 4. Quickstart

Here we provide a simple example of loading the tokenizer and model to generate content.

## 5. Deployment Guide

For production deployment, we recommend using vLLM to serve MiniMax-Text-01. vLLM provides excellent performance for serving large language models with the following features:
[LINK: vLLM](https://docs.vllm.ai/en/latest/)
🔥 Outstanding service throughput performance ⚡ Efficient and intelligent memory management 📦 Powerful batch request processing capability ⚙️ Deeply optimized underlying performance
For detailed deployment instructions, please refer to our vLLM Deployment Guide .
[LINK: vLLM Deployment Guide](https://github.com/MiniMax-AI/MiniMax-01/blob/main/docs/vllm_deployment_guide.md)

## 6. Function Calling

MiniMax-Text-01 supports Function Calling capability, enabling the model to intelligently identify when external functions need to be called and output parameters in structured JSON format. With Function Calling, you can:
- Let the model recognize implicit function call needs in user requests
- Receive structured parameter outputs for seamless application integration
- Support various complex parameter types, including nested objects and arrays
Function Calling supports standard OpenAI-compatible format definitions and integrates seamlessly with the Transformers library. For detailed usage instructions, please refer to our Function Call Guide or Chinese Guide .

## 7. Citation

## 8. Chatbot & API

For general use and evaluation, we provide a Chatbot with online search capabilities and the online API for developers. For general use and evaluation, we provide the MiniMax MCP Server with video generation, image generation, speech synthesis, and voice cloning for developers.
[LINK: MiniMax MCP Server](https://github.com/MiniMax-AI/MiniMax-MCP)

## 9. Contact Us

Contact us at model@minimax.io .

## Model tree for MiniMaxAI/MiniMax-Text-01

## Spaces using MiniMaxAI/MiniMax-Text-01 14

## Collection including MiniMaxAI/MiniMax-Text-01

## Paper for MiniMaxAI/MiniMax-Text-01


--------------------