# DeepSeek-V2.5
**URL:** https://huggingface.co/deepseek-ai/DeepSeek-V2.5
**Page Title:** deepseek-ai/DeepSeek-V2.5 · Hugging Face
--------------------

Paper Link 👁️

## DeepSeek-V2.5

## 1. Introduction

DeepSeek-V2.5 is an upgraded version that combines DeepSeek-V2-Chat and DeepSeek-Coder-V2-Instruct. The new model integrates the general and coding abilities of the two previous versions.
For model details, please visit DeepSeek-V2 page for more information.
[LINK: DeepSeek-V2 page](https://github.com/deepseek-ai/DeepSeek-V2)
DeepSeek-V2.5 better aligns with human preferences and has been optimized in various aspects, including writing and instruction following:

## 2. How to run locally

To utilize DeepSeek-V2.5 in BF16 format for inference, 80GB*8 GPUs are required.

### Inference with Huggingface's Transformers

You can directly employ Huggingface's Transformers for model inference.
[LINK: Huggingface's Transformers](https://github.com/huggingface/transformers)
The complete chat template can be found within tokenizer_config.json located in the huggingface model repository.
Note: The chat template has been updated compared to the previous DeepSeek-V2-Chat version.
An example of chat template is as belows:
You can also add an optional system message:

### Inference with vLLM (recommended)

To utilize vLLM for model inference, please merge this Pull Request into your vLLM codebase: https://github.com/vllm-project/vllm/pull/4650 .
[LINK: vLLM](https://github.com/vllm-project/vllm)
[LINK: https://github.com/vllm-project/vllm/pull/4650](https://github.com/vllm-project/vllm/pull/4650)

### Function calling

Function calling allows the model to call external tools to enhance its capabilities.
Here is an example:

### JSON output

You can use JSON Output Mode to ensure the model generates a valid JSON object. To active this mode, a special instruction should be appended to your system prompt.

### FIM completion

In FIM (Fill In the Middle) completion, you can provide a prefix and an optional suffix, and the model will complete the content in between.

## 3. License

This code repository is licensed under the MIT License. The use of DeepSeek-V2 Base/Chat models is subject to the Model License . DeepSeek-V2 series (including Base and Chat) supports commercial use.

## 4. Citation

## 5. Contact

If you have any questions, please raise an issue or contact us at service@deepseek.com .

## Model tree for deepseek-ai/DeepSeek-V2.5

## Spaces using deepseek-ai/DeepSeek-V2.5 51

## Collections including deepseek-ai/DeepSeek-V2.5

## Paper for deepseek-ai/DeepSeek-V2.5


--------------------