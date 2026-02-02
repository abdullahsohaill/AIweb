# Jan-nano
**URL:** https://huggingface.co/Menlo/Jan-nano
**Page Title:** Menlo/Jan-nano · Hugging Face
--------------------


## Jan-Nano: An Agentic Model

Note: Jan-Nano is a non-thinking model.
Authors: Alan Dao , Bach Vu Dinh

## Overview

Jan-Nano is a compact 4-billion parameter language model specifically designed and trained for deep research tasks. This model has been optimized to work seamlessly with Model Context Protocol (MCP) servers, enabling efficient integration with various research tools and data sources.

## Evaluation

Jan-Nano has been evaluated on the SimpleQA benchmark using our MCP-based benchmark methodology, demonstrating strong performance for its model size:
The evaluation was conducted using our MCP-based benchmark approach, which assesses the model's performance on SimpleQA tasks while leveraging its native MCP server integration capabilities. This methodology better reflects Jan-Nano's real-world performance as a tool-augmented research model, validating both its factual accuracy and its effectiveness in MCP-enabled environments.

## How to Run Locally

Jan-Nano is currently supported by Jan, an open-source ChatGPT alternative that runs entirely on your computer. Jan provides a user-friendly interface for running local AI models with full privacy and control.
For non-jan app or tutorials there are guidance inside community section, please check those out! Discussion

### VLLM

Here is an example command you can use to run vllm with Jan-nano
Chat-template is already included in tokenizer so chat-template is optional, but in case it has issue you can download the template here Non-think chat template
[LINK: Non-think chat template](https://qwen.readthedocs.io/en/latest/_downloads/c101120b5bebcc2f12ec504fc93a965e/qwen3_nonthinking.jinja)

### Recommended Sampling Parameters

- Temperature: 0.7
- Top-p: 0.8
- Top-k: 20
- Min-p: 0

## 📄 Citation

### Documentation

Setup, Usage & FAQ
[LINK: Setup, Usage & FAQ](https://menloresearch.github.io/deep-research/)

## Model tree for Menlo/Jan-nano

Base model

## Spaces using Menlo/Jan-nano 2

## Collection including Menlo/Jan-nano

## Paper for Menlo/Jan-nano

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Menlo/Jan-nano is supported by the following Inference Providers:

--------------------