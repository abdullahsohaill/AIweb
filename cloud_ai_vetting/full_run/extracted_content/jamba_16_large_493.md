# Jamba 1.6 Large
**URL:** https://huggingface.co/ai21labs/AI21-Jamba-Large-1.6
**Page Title:** ai21labs/AI21-Jamba-Large-1.6 · Hugging Face
--------------------


## You need to agree to share your contact information to access this model

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
Log in or Sign Up to review the conditions and access this model content.

## Model Information

The AI21 Jamba 1.6 family of models is state-of-the-art, hybrid SSM-Transformer instruction following foundation models. The Jamba models are the most powerful & efficient long-context models on the market, which deliver up to 2.5X faster inference than leading models of comparable sizes.
The models demonstrate superior long context handling, speed, and quality. They mark the first time a non-Transformer model has been successfully scaled to the quality and strength of the market's leading models.
Jamba Mini 1.6 (12B active/52B total) and Jamba Large 1.6 (94B active/398B total) are also optimized for business use cases and capabilities such as function calling, structured output (JSON), and grounded generation.
The models are released under the Jamba Open Model License , a permissive license allowing full research use and commercial use under the license terms. If you need to license the model for your needs, talk to us .
For more details of this model, see the white paper and the release blog post .

## Model Details

- Developed by: AI21
- Model type: Joint Attention and Mamba (Jamba)
- License: Jamba Open Model License
- Context length: 256K
- Knowledge cutoff date: March 5, 2024
- Supported languages: English, Spanish, French, Portuguese, Italian, Dutch, German, Arabic and Hebrew

## Results on common benchmarks

LongBench and Arena Hard scores are from official leaderboards for applicable models. Examples that couldn't fit models' context windows were scored accordingly. Due to a 32K context limit in its vLLM deployment, Mistral Large was evaluated through its official API.

## Usage

### Prerequisites

You have to have the model on a CUDA device.

### Run the model with vLLM

The recommended way to perform efficient inference with Jamba Large 1.6 is using vLLM . First, make sure to install vLLM (version 0.6.5 or higher is required)
[LINK: vLLM](https://docs.vllm.ai/en/latest/)
Jamba Large 1.6 is too large to be loaded in full (FP32) or half (FP16/BF16) precision on a single node of 8 80GB GPUs. Therefore, quantization is required. We've developed an innovative and efficient quantization technique, ExpertsInt8 , designed for MoE models deployed in vLLM, including Jamba models. Using it, you'll be able to deploy Jamba Large 1.6 on a single node of 8 80GB GPUs.
With ExpertsInt8 quantization and the default vLLM configuration, you'll be able to perform inference on prompts up to 220K tokens long on 8 80GB GPUs:
Note: Versions 4.44.0 and 4.44.1 of transformers have a bug that restricts the ability to run the Jamba architecture. Make sure you're not using these versions.
Note: If you're having trouble installing mamba-ssm and causal-conv1d for the optimized Mamba kernels, you can run Jamba Large 1.6 without them, at the cost of extra latency. In order to do that, add the kwarg use_mamba_kernels=False when loading the model via AutoModelForCausalLM.from_pretained() .
If you don't have access to a GPU, you can also load and run Jamba Large 1.6 on a CPU. Note this will result in poor inference performance.

## Documentation

For comprehensive guides and advanced usage:
- Tokenization Guide - Using ai21-tokenizer
[LINK: Tokenization Guide](https://docs.ai21.com/docs/tokenization)
- Quantization Guide - ExpertsInt8, bitsandbytes
[LINK: Quantization Guide](https://docs.ai21.com/docs/quantization)
- Fine-tuning Guide - LoRA, qLoRA and full fine-tuning
[LINK: Fine-tuning Guide](https://docs.ai21.com/docs/fine-tuning)
For complete documentation and deployment guides, visit our official documentation .
[LINK: official documentation](https://docs.ai21.com/docs)

## Model tree for ai21labs/AI21-Jamba-Large-1.6

## Collection including ai21labs/AI21-Jamba-Large-1.6


--------------------