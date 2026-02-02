# MiniMax-VL-01
**URL:** https://huggingface.co/MiniMaxAI/MiniMax-VL-01
**Page Title:** MiniMaxAI/MiniMax-VL-01 · Hugging Face
--------------------

[LINK: WeChat](https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg)

## MiniMax-VL-01

## 1. Introduction

We are delighted to introduce our MiniMax-VL-01 model. It adopts the "ViT-MLP-LLM" framework, which is a commonly used technique in the field of multimodal large language models. The model is initialized and trained with three key parts: a 303-million-parameter Vision Transformer (ViT) for visual encoding, a randomly initialized two-layer MLP projector for image adaptation, and the MiniMax-Text-01 as the base LLM.
MiniMax-VL-01 has a notable dynamic resolution feature. Input images are resized per a pre-set grid, with resolutions from 336×336 to 2016×2016, keeping a 336×336 thumbnail. The resized images are split into non-overlapping patches of the same size. These patches and the thumbnail are encoded separately and then combined for a full image representation.
The training data for MiniMax-VL-01 consists of caption, description, and instruction data. The Vision Transformer (ViT) is trained on 694 million image-caption pairs from scratch. Across four distinct stages of the training pipeline, a total of 512 billion tokens are processed, leveraging this vast amount of data to endow the model with strong capabilities.
Finally, MiniMax-VL-01 has reached top-level performance on multimodal leaderboards, demonstrating its edge and dependability in complex multimodal tasks.

## 2. Evaluation

* Evaluated following a 0-shot CoT setting.

## 3. Quickstart

Here we provide a simple example of loading the tokenizer and model to generate content.

## 4. Deployment Guide

For production deployment, we recommend using vLLM to serve MiniMax-VL-01. vLLM provides excellent performance for serving large language models with the following features:
🔥 Outstanding service throughput performance ⚡ Efficient and intelligent memory management 📦 Powerful batch request processing capability ⚙️ Deeply optimized underlying performance For detailed deployment instructions, please refer to our vLLM Deployment Guide .
[LINK: vLLM](https://docs.vllm.ai/en/latest/)
[LINK: vLLM Deployment Guide](https://github.com/MiniMax-AI/MiniMax-01/blob/main/docs/vllm_deployment_guide.md)

## 5. Function Calling

MiniMax-VL-01 supports Function Calling capability, enabling the model to intelligently identify when external functions need to be called and output parameters in structured JSON format. With Function Calling, you can:
- Let the model recognize implicit function call needs in user requests
- Receive structured parameter outputs for seamless application integration
- Support various complex parameter types, including nested objects and arrays
Function Calling supports standard OpenAI-compatible format definitions and integrates seamlessly with the Transformers library. For detailed usage instructions, please refer to our Function Call Guide or Chinese Guide .

## 6. Citation

## 7. Chatbot & API

For general use and evaluation, we provide a Chatbot with online search capabilities and the online API for developers. For general use and evaluation, we provide the MiniMax MCP Server with video generation, image generation, speech synthesis, and voice cloning for developers.
[LINK: MiniMax MCP Server](https://github.com/MiniMax-AI/MiniMax-MCP)

## 8. Contact Us

Contact us at model@minimax.io .

## Spaces using MiniMaxAI/MiniMax-VL-01 11

## Collection including MiniMaxAI/MiniMax-VL-01

## Paper for MiniMaxAI/MiniMax-VL-01


--------------------