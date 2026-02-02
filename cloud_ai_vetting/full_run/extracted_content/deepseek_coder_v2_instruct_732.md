# DeepSeek-Coder-V2-Instruct
**URL:** https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct
**Page Title:** deepseek-ai/DeepSeek-Coder-V2-Instruct · Hugging Face
--------------------

API Platform | How to Use | License |
[LINK: API Platform](#4-api-platform)
Paper Link 👁️
[LINK: Paper Link 👁️](https://github.com/deepseek-ai/DeepSeek-Coder-V2/blob/main/paper.pdf)

## DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence

## 1. Introduction

We present DeepSeek-Coder-V2, an open-source Mixture-of-Experts (MoE) code language model that achieves performance comparable to GPT4-Turbo in code-specific tasks. Specifically, DeepSeek-Coder-V2 is further pre-trained from an intermediate checkpoint of DeepSeek-V2 with additional 6 trillion tokens. Through this continued pre-training, DeepSeek-Coder-V2 substantially enhances the coding and mathematical reasoning capabilities of DeepSeek-V2, while maintaining comparable performance in general language tasks. Compared to DeepSeek-Coder-33B, DeepSeek-Coder-V2 demonstrates significant advancements in various aspects of code-related tasks, as well as reasoning and general capabilities. Additionally, DeepSeek-Coder-V2 expands its support for programming languages from 86 to 338, while extending the context length from 16K to 128K.
In standard benchmark evaluations, DeepSeek-Coder-V2 achieves superior performance compared to closed-source models such as GPT4-Turbo, Claude 3 Opus, and Gemini 1.5 Pro in coding and math benchmarks.  The list of supported programming languages can be found here .
[LINK: here](https://github.com/deepseek-ai/DeepSeek-Coder-V2/blob/main/supported_langs.txt)

## 2. Model Downloads

We release the DeepSeek-Coder-V2 with 16B and 236B parameters based on the DeepSeekMoE framework, which has actived parameters of only 2.4B and 21B , including base and instruct models, to the public.

## 3. Chat Website

You can chat with the DeepSeek-Coder-V2 on DeepSeek's official website: coder.deepseek.com

## 4. API Platform

We also provide OpenAI-Compatible API at DeepSeek Platform: platform.deepseek.com , and you can also pay-as-you-go at an unbeatable price.

## 5. How to run locally

Here, we provide some examples of how to use DeepSeek-Coder-V2-Lite model. If you want to utilize DeepSeek-Coder-V2 in BF16 format for inference, 80GB*8 GPUs are required.

### Inference with Huggingface's Transformers

You can directly employ Huggingface's Transformers for model inference.
[LINK: Huggingface's Transformers](https://github.com/huggingface/transformers)
The complete chat template can be found within tokenizer_config.json located in the huggingface model repository.
An example of chat template is as belows:
You can also add an optional system message:

### Inference with vLLM (recommended)

To utilize vLLM for model inference, please merge this Pull Request into your vLLM codebase: https://github.com/vllm-project/vllm/pull/4650 .
[LINK: vLLM](https://github.com/vllm-project/vllm)
[LINK: https://github.com/vllm-project/vllm/pull/4650](https://github.com/vllm-project/vllm/pull/4650)

## 6. License

This code repository is licensed under the MIT License . The use of DeepSeek-Coder-V2 Base/Instruct models is subject to the Model License . DeepSeek-Coder-V2 series (including Base and Instruct) supports commercial use.
[LINK: the MIT License](https://github.com/deepseek-ai/DeepSeek-Coder-V2/blob/main/LICENSE-CODE)
[LINK: the Model License](https://github.com/deepseek-ai/DeepSeek-Coder-V2/blob/main/LICENSE-MODEL)

## 7. Contact

If you have any questions, please raise an issue or contact us at service@deepseek.com .

## Model tree for deepseek-ai/DeepSeek-Coder-V2-Instruct

Base model

## Spaces using deepseek-ai/DeepSeek-Coder-V2-Instruct 62

## Collection including deepseek-ai/DeepSeek-Coder-V2-Instruct

## Paper for deepseek-ai/DeepSeek-Coder-V2-Instruct


--------------------