# Arch-Router-1.5B
**URL:** https://huggingface.co/katanemo/Arch-Router-1.5B
**Page Title:** katanemo/Arch-Router-1.5B · Hugging Face
--------------------


## katanemo/Arch-Router-1.5B

## Overview

With the rapid proliferation of large language models (LLMs) -- each optimized for different strengths, style, or latency/cost profile -- routing has become an essential technique to operationalize the use of different models. However, existing LLM routing approaches are limited in two key ways: they evaluate performance using benchmarks that often fail to capture human preferences driven by subjective evaluation criteria, and they typically select from a limited pool of models.
We introduce a preference-aligned routing framework that guides model selection by matching queries to user-defined domains (e.g., travel) or action types (e.g., image editing) -- offering a practical mechanism to encode preferences in routing decisions. Specifically, we introduce Arch-Router, a compact 1.5B model that learns to map queries to domain-action preferences for model routing decisions. Experiments on conversational datasets demonstrate that our approach achieves state-of-the-art (SOTA) results in matching queries with human preferences, outperforming top proprietary models.
This model is described in the paper: https://arxiv.org/abs/2506.16655 , and powers Arch the models-native proxy server for agents.
[LINK: Arch](https://github.com/katanemo/arch)

### How It Works

To support effective routing, Arch-Router introduces two key concepts:
- Domain – the high-level thematic category or subject matter of a request (e.g., legal, healthcare, programming).
- Action – the specific type of operation the user wants performed (e.g., summarization, code generation, booking appointment, translation).
Both domain and action configs are associated with preferred models or model variants. At inference time, Arch-Router analyzes the incoming prompt to infer its domain and action using semantic similarity, task indicators, and contextual cues. It then applies the user-defined routing preferences to select the model best suited to handle the request.

### Key Features

- Structured Preference Routing : Aligns prompt request with model strengths using explicit domain–action mappings.
- Transparent and Controllable : Makes routing decisions transparent and configurable, empowering users to customize system behavior.
- Flexible and Adaptive : Supports evolving user needs, model updates, and new domains/actions without retraining the router.
- Production-Ready Performance : Optimized for low-latency, high-throughput applications in multi-model environments.

## Requirements

The code of Arch-Router-1.5B has been in the Hugging Face transformers library and we advise you to install latest version:

## How to use

We use the following example to illustrate how to use our model to perform routing tasks. Please note that, our model works best with our provided prompt format.

### Quickstart

Then you should be able to see the following output string in JSON format:
To better understand how to create the route descriptions, please take a look at our Katanemo API .
[LINK: Katanemo API](https://docs.archgw.com/guides/llm_router.html)

## License

Katanemo Arch-Router model is distributed under the Katanemo license .
GitHub: https://github.com/katanemo/arch
[LINK: https://github.com/katanemo/arch](https://github.com/katanemo/arch)

## Model tree for katanemo/Arch-Router-1.5B

Base model

## Spaces using katanemo/Arch-Router-1.5B 4

## Collection including katanemo/Arch-Router-1.5B

## Paper for katanemo/Arch-Router-1.5B

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
katanemo/Arch-Router-1.5B is supported by the following Inference Providers:

--------------------