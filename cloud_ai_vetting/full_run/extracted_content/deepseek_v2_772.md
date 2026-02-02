# DeepSeek-V2
**URL:** https://huggingface.co/deepseek-ai/DeepSeek-V2-Chat
**Page Title:** deepseek-ai/DeepSeek-V2-Chat · Hugging Face
--------------------

Model Download | Evaluation Results | Model Architecture | API Platform | License | Citation
[LINK: API Platform](#6-api-platform)
Paper Link 👁️

## DeepSeek-V2:  A Strong, Economical, and Efficient Mixture-of-Experts Language Model

## 1. Introduction

Today, we’re introducing DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference. It comprises 236B total parameters, of which 21B are activated for each token. Compared with DeepSeek 67B, DeepSeek-V2 achieves stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times.

## 2. Model Downloads

Due to the constraints of HuggingFace, the open-source code currently experiences slower performance than our internal codebase when running on GPUs with Huggingface. To facilitate the efficient execution of our model, we offer a dedicated vllm solution that optimizes performance for running our model effectively.

## 3. Evaluation Results

### Base Model

Evaluation results on the Needle In A Haystack (NIAH) tests.  DeepSeek-V2 performs well across all context window lengths up to 128K .

### Chat Model

We evaluate our model on AlpacaEval 2.0 and MTBench, showing the competitive performance of DeepSeek-V2-Chat-RL on English conversation generation.
Alignbench ( https://arxiv.org/abs/2311.18743 )
We evaluate our model on LiveCodeBench (0901-0401), a benchmark designed for live coding challenges. As illustrated, DeepSeek-V2 demonstrates considerable proficiency in LiveCodeBench, achieving a Pass@1 score that surpasses several other sophisticated models. This performance highlights the model's effectiveness in tackling live coding tasks.

## 4. Model Architecture

DeepSeek-V2 adopts innovative architectures to guarantee economical training and efficient inference：
- For attention, we design MLA (Multi-head Latent Attention), which utilizes low-rank key-value union compression to eliminate the bottleneck of inference-time key-value cache, thus supporting efficient inference.
- For Feed-Forward Networks (FFNs), we adopt DeepSeekMoE architecture, a high-performance MoE architecture that enables training stronger models at lower costs.

## 5. Chat Website

You can chat with the DeepSeek-V2 on DeepSeek's official website: chat.deepseek.com

## 6. API Platform

We also provide OpenAI-Compatible API at DeepSeek Platform: platform.deepseek.com . Sign up for over millions of free tokens. And you can also pay-as-you-go at an unbeatable price.

## 7. How to run locally

To utilize DeepSeek-V2 in BF16 format for inference, 80GB*8 GPUs are required.

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

## 8. License

This code repository is licensed under the MIT License . The use of DeepSeek-V2 Base/Chat models is subject to the Model License . DeepSeek-V2 series (including Base and Chat) supports commercial use.

## 9. Citation

## 10. Contact

If you have any questions, please raise an issue or contact us at service@deepseek.com .

## Model tree for deepseek-ai/DeepSeek-V2-Chat

## Spaces using deepseek-ai/DeepSeek-V2-Chat 33

## Collection including deepseek-ai/DeepSeek-V2-Chat

## Papers for deepseek-ai/DeepSeek-V2-Chat


--------------------