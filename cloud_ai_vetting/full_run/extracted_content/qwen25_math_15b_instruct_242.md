# Qwen2.5-Math-1.5B-Instruct
**URL:** https://huggingface.co/Qwen/Qwen2.5-Math-1.5B-Instruct
**Page Title:** Qwen/Qwen2.5-Math-1.5B-Instruct · Hugging Face
--------------------


## Qwen2.5-Math-1.5B-Instruct

## Introduction

In August 2024, we released the first series of mathematical LLMs - Qwen2-Math - of our Qwen family. A month later, we have upgraded it and open-sourced Qwen2.5-Math series, including base models Qwen2.5-Math-1.5B/7B/72B , instruction-tuned models Qwen2.5-Math-1.5B/7B/72B-Instruct , and mathematical reward model Qwen2.5-Math-RM-72B .
[LINK: Qwen2-Math](https://qwenlm.github.io/blog/qwen2-math/)
Unlike Qwen2-Math series which only supports using Chain-of-Thught (CoT) to solve English math problems, Qwen2.5-Math series is expanded to support using both CoT and Tool-integrated Reasoning (TIR) to solve math problems in both Chinese and English. The Qwen2.5-Math series models have achieved significant performance improvements compared to the Qwen2-Math series models on the Chinese and English mathematics benchmarks with CoT.
While CoT plays a vital role in enhancing the reasoning capabilities of LLMs, it faces challenges in achieving computational accuracy and handling complex mathematical or algorithmic reasoning tasks, such as finding the roots of a quadratic equation or computing the eigenvalues of a matrix. TIR can further improve the model's proficiency in precise computation, symbolic manipulation, and algorithmic manipulation. Qwen2.5-Math-1.5B/7B/72B-Instruct achieve 79.7, 85.3, and 87.8 respectively on the MATH benchmark using TIR.

## Model Details

For more details, please refer to our blog post and GitHub repo .
[LINK: blog post](https://qwenlm.github.io/blog/qwen2.5-math/)
[LINK: GitHub repo](https://github.com/QwenLM/Qwen2.5-Math)

## Requirements

- transformers>=4.37.0 for Qwen2.5-Math models. The latest version is recommended.
For requirements on GPU memory and the respective throughput, see similar results of Qwen2 here .
[LINK: here](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html)

## Quick Start

Qwen2.5-Math-1.5B-Instruct is an instruction model for chatting;
Qwen2.5-Math-1.5B is a base model typically used for completion and few-shot inference, serving as a better starting point for fine-tuning.

### 🤗 Hugging Face Transformers

Qwen2.5-Math can be deployed and infered in the same way as Qwen2.5 . Here we show a code snippet to show you how to use the chat model with transformers :
[LINK: Qwen2.5](https://github.com/QwenLM/Qwen2.5)

## Citation

If you find our work helpful, feel free to give us a citation.

## Model tree for Qwen/Qwen2.5-Math-1.5B-Instruct

Base model

## Spaces using Qwen/Qwen2.5-Math-1.5B-Instruct 23

## Collection including Qwen/Qwen2.5-Math-1.5B-Instruct

## Paper for Qwen/Qwen2.5-Math-1.5B-Instruct

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Qwen/Qwen2.5-Math-1.5B-Instruct is supported by the following Inference Providers:

--------------------