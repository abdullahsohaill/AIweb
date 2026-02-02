# Aria
**URL:** https://huggingface.co/rhymes-ai/Aria
**Page Title:** rhymes-ai/Aria · Hugging Face
--------------------


## Aria Model Card

[Dec 1, 2024] We have released the base models (with native multimodal pre-training) for Aria ( Aria-Base-8K and Aria-Base-64K ) for research purposes and continue training.

## Key features

- SoTA Multimodal Native Performance : Aria achieves strong performance on a wide range of multimodal, language, and coding tasks. It is superior in video and document understanding.
- Lightweight and Fast : Aria is a mixture-of-expert model with 3.9B activated parameters per token. It efficently encodes visual input of variable sizes and aspect ratios.
- Long Multimodal Context Window : Aria supports multimodal input of up to 64K tokens. It can caption a 256-frame video in 10 seconds.
🔗 Try Aria! · 📖 Blog · 📌 Paper · ⭐ GitHub · 🟣 Discord
[LINK: GitHub](https://github.com/rhymes-ai/Aria)

## Benchmark

## Quick Start

### Installation

### Inference

Aria has 25.3B total parameters, it can be loaded in one A100 (80GB) GPU with bfloat16 precision.
Here is a code snippet to show you how to use Aria.
From transformers>=v4.48, you can also pass image url or local path to the conversation history, and let the chat template handle the rest.
Chat template will load the image for you and return inputs in torch.Tensor which you can pass directly to model.generate() .
Here is how to rewrite the above example

### Advanced Inference and Fine-tuning

We provide a codebase for more advanced usage of Aria,
including vllm inference, cookbooks, and fine-tuning on custom datasets.
[LINK: codebase](https://github.com/rhymes-ai/Aria)

## Citation

If you find our work helpful, please consider citing.

## Model tree for rhymes-ai/Aria

Base model

## Spaces using rhymes-ai/Aria 8

## Paper for rhymes-ai/Aria


--------------------