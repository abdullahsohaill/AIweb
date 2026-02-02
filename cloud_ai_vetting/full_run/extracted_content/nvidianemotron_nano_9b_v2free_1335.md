# nvidia/nemotron-nano-9b-v2:free
**URL:** https://openrouter.ai/nvidia/nemotron-nano-9b-v2:free
**Page Title:** Nemotron Nano 9B V2 (free) - API, Providers, Stats | OpenRouter
--------------------

[LINK: Send traces to your favorite observability platforms with Broadcast (now GA).](/docs/guides/features/broadcast)

## NVIDIA: Nemotron Nano 9B V2 (free)

### nvidia / nemotron-nano-9b-v2:free

NVIDIA-Nemotron-Nano-9B-v2 is a large language model (LLM) trained from scratch by NVIDIA, and designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and tasks by first generating a reasoning trace and then concluding with a final response.
The model's reasoning capabilities can be controlled via a system prompt. If the user prefers the model to provide its final answer without intermediate reasoning traces, it can be configured to do so.

## Providers for Nemotron Nano 9B V2 (free)

### OpenRouter routes requests to the best providers that are able to handle your prompt size and parameters, with fallbacks to maximize uptime .

[LINK: routes requests](/docs/provider-routing)

## Performance for Nemotron Nano 9B V2 (free)

### Compare different providers across OpenRouter

### Throughput

### Latency

### E2E Latency

## Apps using Nemotron Nano 9B V2 (free)

### Top public apps this month

[LINK: Chronos Gold Pipeline](/apps?url=https%3A%2F%2Fgithub.com%2Fchronos-harvester)

## Recent activity on Nemotron Nano 9B V2 (free)

### Total usage per day on OpenRouter

Prompt tokens measure input size. Reasoning tokens show internal thinking before a response. Completion tokens reflect total output length.

## Uptime stats for Nemotron Nano 9B V2 (free)

### Uptime stats for Nemotron Nano 9B V2 (free) on the only provider

When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access uptime data programmatically through the Endpoints API
[LINK: Endpoints API](/docs/api/api-reference/endpoints/list-endpoints)
Learn more about our load balancing and customization options.
[LINK: Learn more](/docs/provider-routing)

## Sample code and API for Nemotron Nano 9B V2 (free)

### OpenRouter normalizes requests and responses across providers for you.

OpenRouter provides an OpenAI-compatible completion API to 300+ models & providers that you can call directly, or using the OpenAI SDK. Additionally, some third-party SDKs are available.
In the examples below, the OpenRouter-specific headers are optional. Setting them allows your app to appear on the OpenRouter leaderboards.
[LINK: OpenRouter-specific headers](/docs/requests#request-headers)

## Using third-party SDKs

For information about using third-party SDKs and frameworks with OpenRouter, please see our frameworks documentation .
[LINK: frameworks documentation](/docs/guides/community/frameworks-and-integrations-overview)
See the Request docs for all possible fields, and Parameters for explanations of specific sampling parameters.
[LINK: Request docs](/docs/api-reference/overview)
[LINK: Parameters](/docs/api-reference/parameters)

## More models from Nvidia

NVIDIA Nemotron 3 Nano 30B A3B is a small language MoE model with highest compute efficiency and accuracy for developers to build specialized agentic AI systems.
The model is fully open with open-weights, datasets and recipes so developers can easily
customize, optimize, and deploy the model on their infrastructure for maximum privacy and
security.
Note: For the free endpoint, all prompts and output are logged to improve the provider's model and its product and services. Please do not upload any personal, confidential, or otherwise sensitive information. This is a trial use only. Do not use for production or business-critical systems.
NVIDIA Nemotron 3 Nano 30B A3B is a small language MoE model with highest compute efficiency and accuracy for developers to build specialized agentic AI systems.
The model is fully open with open-weights, datasets and recipes so developers can easily
customize, optimize, and deploy the model on their infrastructure for maximum privacy and
security.
Note: For the free endpoint, all prompts and output are logged to improve the provider's model and its product and services. Please do not upload any personal, confidential, or otherwise sensitive information. This is a trial use only. Do not use for production or business-critical systems.
NVIDIA Nemotron Nano 2 VL is a 12-billion-parameter open multimodal reasoning model designed for video understanding and document intelligence. It introduces a hybrid Transformer-Mamba architecture, combining transformer-level accuracy with Mamba’s memory-efficient sequence modeling for significantly higher throughput and lower latency.
The model supports inputs of text and multi-image documents, producing natural-language outputs. It is trained on high-quality NVIDIA-curated synthetic datasets optimized for optical-character recognition, chart reasoning, and multimodal comprehension.
Nemotron Nano 2 VL achieves leading results on OCRBench v2 and scores ≈ 74 average across MMMU, MathVista, AI2D, OCRBench, OCR-Reasoning, ChartQA, DocVQA, and Video-MME—surpassing prior open VL baselines. With Efficient Video Sampling (EVS), it handles long-form videos while reducing inference cost.
Open-weights, training data, and fine-tuning recipes are released under a permissive NVIDIA open license, with deployment supported across NeMo, NIM, and major inference runtimes.
NVIDIA Nemotron Nano 2 VL is a 12-billion-parameter open multimodal reasoning model designed for video understanding and document intelligence. It introduces a hybrid Transformer-Mamba architecture, combining transformer-level accuracy with Mamba’s memory-efficient sequence modeling for significantly higher throughput and lower latency.
The model supports inputs of text and multi-image documents, producing natural-language outputs. It is trained on high-quality NVIDIA-curated synthetic datasets optimized for optical-character recognition, chart reasoning, and multimodal comprehension.
Nemotron Nano 2 VL achieves leading results on OCRBench v2 and scores ≈ 74 average across MMMU, MathVista, AI2D, OCRBench, OCR-Reasoning, ChartQA, DocVQA, and Video-MME—surpassing prior open VL baselines. With Efficient Video Sampling (EVS), it handles long-form videos while reducing inference cost.
Open-weights, training data, and fine-tuning recipes are released under a permissive NVIDIA open license, with deployment supported across NeMo, NIM, and major inference runtimes.
Llama-3.3-Nemotron-Super-49B-v1.5 is a 49B-parameter, English-centric reasoning/chat model derived from Meta’s Llama-3.3-70B-Instruct with a 128K context. It’s post-trained for agentic workflows (RAG, tool calling) via SFT across math, code, science, and multi-turn chat, followed by multiple RL stages; Reward-aware Preference Optimization (RPO) for alignment, RL with Verifiable Rewards (RLVR) for step-wise reasoning, and iterative DPO to refine tool-use behavior. A distillation-driven Neural Architecture Search (“Puzzle”) replaces some attention blocks and varies FFN widths to shrink memory footprint and improve throughput, enabling single-GPU (H100/H200) deployment while preserving instruction following and CoT quality.
In internal evaluations (NeMo-Skills, up to 16 runs, temp = 0.6, top_p = 0.95), the model reports strong reasoning/coding results, e.g., MATH500 pass@1 = 97.4, AIME-2024 = 87.5, AIME-2025 = 82.71, GPQA = 71.97, LiveCodeBench (24.10–25.02) = 73.58, and MMLU-Pro (CoT) = 79.53. The model targets practical inference efficiency (high tokens/s, reduced VRAM) with Transformers/vLLM support and explicit “reasoning on/off” modes (chat-first defaults, greedy recommended when disabled). Suitable for building agents, assistants, and long-context retrieval systems where balanced accuracy-to-cost and reliable tool use matter.
NVIDIA-Nemotron-Nano-9B-v2 is a large language model (LLM) trained from scratch by NVIDIA, and designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and tasks by first generating a reasoning trace and then concluding with a final response.
The model's reasoning capabilities can be controlled via a system prompt. If the user prefers the model to provide its final answer without intermediate reasoning traces, it can be configured to do so.
NVIDIA-Nemotron-Nano-9B-v2 is a large language model (LLM) trained from scratch by NVIDIA, and designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and tasks by first generating a reasoning trace and then concluding with a final response.
The model's reasoning capabilities can be controlled via a system prompt. If the user prefers the model to provide its final answer without intermediate reasoning traces, it can be configured to do so.
Llama-3.1-Nemotron-Nano-8B-v1 is a compact large language model (LLM) derived from Meta's Llama-3.1-8B-Instruct, specifically optimized for reasoning tasks, conversational interactions, retrieval-augmented generation (RAG), and tool-calling applications. It balances accuracy and efficiency, fitting comfortably onto a single consumer-grade RTX GPU for local deployment. The model supports extended context lengths of up to 128K tokens.
Note: you must include detailed thinking on in the system prompt to enable reasoning. Please see Usage Recommendations for more.
Llama-3.3-Nemotron-Super-49B-v1 is a large language model (LLM) optimized for advanced reasoning, conversational interactions, retrieval-augmented generation (RAG), and tool-calling tasks. Derived from Meta's Llama-3.3-70B-Instruct, it employs a Neural Architecture Search (NAS) approach, significantly enhancing efficiency and reducing memory requirements. This allows the model to support a context length of up to 128K tokens and fit efficiently on single high-performance GPUs, such as NVIDIA H200.
Note: you must include detailed thinking on in the system prompt to enable reasoning. Please see Usage Recommendations for more.
Llama-3.1-Nemotron-Ultra-253B-v1 is a large language model (LLM) optimized for advanced reasoning, human-interactive chat, retrieval-augmented generation (RAG), and tool-calling tasks. Derived from Meta’s Llama-3.1-405B-Instruct, it has been significantly customized using Neural Architecture Search (NAS), resulting in enhanced efficiency, reduced memory usage, and improved inference latency. The model supports a context length of up to 128K tokens and can operate efficiently on an 8x NVIDIA H100 node.
Note: you must include detailed thinking on in the system prompt to enable reasoning. Please see Usage Recommendations for more.
NVIDIA's Llama 3.1 Nemotron 70B is a language model designed for generating precise and useful responses. Leveraging Llama 3.1 70B architecture and Reinforcement Learning from Human Feedback (RLHF), it excels in automatic alignment benchmarks. This model is tailored for applications requiring high accuracy in helpfulness and response generation, suitable for diverse user queries across multiple domains.
Usage of this model is subject to Meta's Acceptable Use Policy .
Nemotron-4-340B-Instruct is an English-language chat model optimized for synthetic data generation. This large language model (LLM) is a fine-tuned version of Nemotron-4-340B-Base, designed for single and multi-turn chat use-cases with a 4,096 token context length.
The base model was pre-trained on 9 trillion tokens from diverse English texts, 50+ natural languages, and 40+ coding languages. The instruct model underwent additional alignment steps:
The alignment process used approximately 20K human-annotated samples, while 98% of the data for fine-tuning was synthetically generated. Detailed information about the synthetic data generation pipeline is available in the technical report .

--------------------