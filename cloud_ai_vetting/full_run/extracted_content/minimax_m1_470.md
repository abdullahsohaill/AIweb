# MiniMax-M1
**URL:** https://huggingface.co/MiniMaxAI/MiniMax-M1-40k
**Page Title:** MiniMaxAI/MiniMax-M1-40k · Hugging Face
--------------------


## MiniMax-M1

## 1. Model Overview

We introduce MiniMax-M1, the world's first open-weight, large-scale hybrid-attention reasoning model.
MiniMax-M1 is powered by a hybrid Mixture-of-Experts (MoE) architecture combined with a lightning
attention mechanism. The model is developed based on our previous MiniMax-Text-01 model , 
which contains a total of 456 billion parameters with 45.9 billion parameters activated
per token. Consistent with MiniMax-Text-01, the M1 model natively supports a context length of 1
million tokens, 8x the context size of DeepSeek R1. Furthermore, the lightning attention mechanism
in MiniMax-M1 enables efficient scaling of test-time compute – For example, compared to DeepSeek
R1, M1 consumes 25% of the FLOPs at a generation length of 100K tokens. These properties make M1
particularly suitable for complex tasks that require processing long inputs and thinking extensively.
MiniMax-M1 is trained using large-scale reinforcement learning (RL) on diverse problems ranging from
traditional mathematical reasoning to sandbox-based, real-world software engineering environments.
We develop an efficient RL scaling framework for M1 highlighting two perspectives: (1) We propose
CISPO, a novel algorithm that clips importance sampling weights instead of token updates, which
outperforms other competitive RL variants; (2) Our hybrid-attention design naturally enhances the
efficiency of RL, where we address unique challenges when scaling RL with the hybrid architecture. We
train two versions of MiniMax-M1 models with 40K and 80K thinking budgets respectively. Experiments
on standard benchmarks show that our models outperform other strong open-weight models such as
the original DeepSeek-R1 and Qwen3-235B, particularly on complex software engineering, tool using,
and long context tasks. With efficient scaling of test-time compute, MiniMax-M1 serves as a strong
foundation for next-generation language model agents to reason and tackle real-world challenges.
Benchmark performance comparison of leading commercial and open-weight models across competition-level mathematics, coding, software engineering, agentic tool use, and long-context understanding tasks. We use the MiniMax-M1-80k model here for MiniMax-M1.

## 2. Evaluation

Performance of MiniMax-M1 on core benchmarks.
* conducted on the text-only HLE subset.
Our models are evaluated with temperature=1.0 , top_p=0.95 .

### SWE-bench methodology

We report results derived from the Agentless scaffold. Departing from the original pipeline, our methodology employs a two-stage localization process (without any embedding-based retrieval mechanisms): initial coarse-grained file localization followed by fine-grained localization to specific files and code elements. The values for our models are calculated on the subset of n=486 verified tasks which work on our infrastructure. The excluded 14 test cases that were incompatible with our internal infrastructure are: "astropy__astropy-7606" , "astropy__astropy-8707" , "astropy__astropy-8872" , "django__django-10097" , "matplotlib__matplotlib-20488" , "psf__requests-2317" , "psf__requests-2931" , "psf__requests-5414" , "pylint-dev__pylint-6528" , "pylint-dev__pylint-7277" , "sphinx-doc__sphinx-10435" , "sphinx-doc__sphinx-7985" , "sphinx-doc__sphinx-8269" , "sphinx-doc__sphinx-8475"

### TAU-bench methodology

We evaluate TAU-Bench with GPT-4.1 as user model and without any custom tools. The maximum number of interaction steps is 40. 
Our general system prompt is:

## 3. Recommendations for Minimax-M1 Model Usage

To achieve the best results with the Minimax-M1 model, we suggest focusing on two key points: Inference Parameters and the System Prompt.

### 3.1. Inference Parameters

- Temperature: 1.0
- Top_p: 0.95
This setting is optimal for encouraging creativity and diversity in the model's responses. It allows the model to explore a wider range of linguistic possibilities, preventing outputs that are too rigid or repetitive, while still maintaining strong logical coherence.

### 3.2. System Prompt

Tailoring your system prompt to the specific task is crucial for guiding the model effectively. Below are suggested settings for different scenarios.
For common tasks like summarization, translation, Q&A, or creative writing:
For complex tasks like generating code for web pages:
When dealing with problems that require calculation or logical deduction:

## 4. Deployment Guide

Download the model from HuggingFace repository:
- MiniMax-M1-40k
- MiniMax-M1-80k
For production deployment, we recommend using vLLM to serve MiniMax-M1. vLLM provides excellent performance for serving large language models with the following features:
[LINK: vLLM](https://docs.vllm.ai/en/latest/)
- 🔥 Outstanding service throughout performance
- ⚡ Efficient and intelligent memory management
- 📦 Powerful batch request processing capability
- ⚙️ Deeply optimized underlying performance
For detailed vLLM deployment instructions, please refer to our vLLM Deployment Guide .
Alternatively, you can also deploy using Transformers directly. For detailed Transformers deployment instructions, you can see our MiniMax-M1 Transformers Deployment Guide .
[LINK: vLLM Deployment Guide](/MiniMaxAI/MiniMax-M1-40k/blob/main/./docs/vllm_deployment_guide.md)
[LINK: MiniMax-M1 Transformers Deployment Guide](/MiniMaxAI/MiniMax-M1-40k/blob/main/./docs/transformers_deployment_guide.md)

## 5. Function Calling

The MiniMax-M1 model supports function calling capabilities, enabling the model to identify when external functions need to be called and output function call parameters in a structured format. MiniMax-M1 Function Call Guide provides detailed instructions on how to use the function calling feature of MiniMax-M1.
[LINK: MiniMax-M1 Function Call Guide](/MiniMaxAI/MiniMax-M1-40k/blob/main/./docs/function_call_guide.md)

## 6. Chatbot & API

For general use and evaluation, we provide a Chatbot with online search capabilities and the online API for developers. For general use and evaluation, we provide the MiniMax MCP Server with video generation, image generation, speech synthesis, and voice cloning for developers.
[LINK: MiniMax MCP Server](https://github.com/MiniMax-AI/MiniMax-MCP)

## 7. Citation

## 8. Contact Us

Contact us at model@minimax.io .

## Spaces using MiniMaxAI/MiniMax-M1-40k 3

## Collection including MiniMaxAI/MiniMax-M1-40k

## Paper for MiniMaxAI/MiniMax-M1-40k


--------------------