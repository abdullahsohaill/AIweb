# Janus-1.3B
**URL:** https://huggingface.co/deepseek-ai/Janus-1.3B
**Page Title:** deepseek-ai/Janus-1.3B · Hugging Face
--------------------


## 0. Update

2024.10.20 : We have uploaded the correct tokenizer_config.json . The previous file was missing the pad_token , which caused poor visual generation results.

## 1. Introduction

Janus is a novel autoregressive framework that unifies multimodal understanding and generation. 
It addresses the limitations of previous approaches by decoupling visual encoding into separate pathways, while still utilizing a single, unified transformer architecture for processing. The decoupling not only alleviates the conflict between the visual encoder’s roles in understanding and generation, but also enhances the framework’s flexibility. 
Janus surpasses previous unified model and matches or exceeds the performance of task-specific models. 
The simplicity, high flexibility, and effectiveness of Janus make it a strong candidate for next-generation unified multimodal models.
Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation
Github Repository
[LINK: Github Repository](https://github.com/deepseek-ai/Janus)

### 2. Model Summary

Janus is a unified understanding and generation MLLM, which decouples visual encoding for multimodal understanding and generation. 
Janus is constructed based on the DeepSeek-LLM-1.3b-base which is trained on an approximate corpus of 500B text tokens.
For multimodal understanding, it uses the SigLIP-L as the vision encoder, which supports 384 x 384 image input. For image generation, Janus uses the tokenizer from here with a downsample rate of 16.
[LINK: here](https://github.com/FoundationVision/LlamaGen)

## 3. Quick Start

Please refer to Github Repository
[LINK: Github Repository](https://github.com/deepseek-ai/Janus)

## 4. License

This code repository is licensed under the MIT License . The use of Janus models is subject to DeepSeek Model License .
[LINK: the MIT License](https://github.com/deepseek-ai/DeepSeek-LLM/blob/HEAD/LICENSE-CODE)
[LINK: DeepSeek Model License](https://github.com/deepseek-ai/DeepSeek-LLM/blob/HEAD/LICENSE-MODEL)

## 5. Citation

## 6. Contact

If you have any questions, please raise an issue or contact us at service@deepseek.com .
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for deepseek-ai/Janus-1.3B

## Spaces using deepseek-ai/Janus-1.3B 19

## Collection including deepseek-ai/Janus-1.3B

## Paper for deepseek-ai/Janus-1.3B


--------------------