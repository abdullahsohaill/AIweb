# Llama-3.1-Nemotron-70B-Instruct
**URL:** https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF
**Page Title:** nvidia/Llama-3.1-Nemotron-70B-Instruct-HF · Hugging Face
--------------------


## Model Overview

## Description:

Llama-3.1-Nemotron-70B-Instruct is a large language model customized by NVIDIA to improve the helpfulness of LLM generated responses to user queries.
This model reaches Arena Hard of 85.0, AlpacaEval 2 LC of 57.6 and GPT-4-Turbo MT-Bench of 8.98, which are known to be predictive of LMSys Chatbot Arena Elo
[LINK: Arena Hard](https://github.com/lmarena/arena-hard-auto)
[LINK: AlpacaEval 2 LC](https://tatsu-lab.github.io/alpaca_eval/)
[LINK: GPT-4-Turbo MT-Bench](https://github.com/lm-sys/FastChat/pull/3158)
As of 1 Oct 2024, this model is #1 on all three automatic alignment benchmarks (verified tab for AlpacaEval 2 LC), edging out strong frontier models such as GPT-4o and Claude 3.5 Sonnet.
As of Oct 24th, 2024 the model has Elo Score of 1267(+-7), rank 9 and style controlled rank of 26 on ChatBot Arena leaderboard .
This model was trained using RLHF (specifically, REINFORCE), Llama-3.1-Nemotron-70B-Reward and HelpSteer2-Preference prompts on a Llama-3.1-70B-Instruct model as the initial policy.
Llama-3.1-Nemotron-70B-Instruct-HF has been converted from Llama-3.1-Nemotron-70B-Instruct to support it in the HuggingFace Transformers codebase. Please note that evaluation results might be slightly different from the Llama-3.1-Nemotron-70B-Instruct as evaluated in NeMo-Aligner, which the evaluation results below are based on.
Try hosted inference for free at build.nvidia.com - it comes with an OpenAI-compatible API interface.
See details on our paper at https://arxiv.org/abs/2410.01257 - as a preview, this model can correctly the question How many r in strawberry? without specialized prompting or additional reasoning tokens:
Note: This model is a demonstration of our techniques for improving helpfulness in general-domain instruction following. It has not been tuned for performance in specialized domains such as math.

## License

Your use of this model is governed by the NVIDIA Open Model License .
Additional Information: Llama 3.1 Community License Agreement . Built with Llama.
[LINK: NVIDIA Open Model License](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)

## Evaluation Metrics

As of 1 Oct 2024, Llama-3.1-Nemotron-70B-Instruct performs best on Arena Hard, AlpacaEval 2 LC (verified tab) and MT Bench (GPT-4-Turbo)

## Usage:

You can use the model using HuggingFace Transformers library with 2 or more 80GB GPUs (NVIDIA Ampere or newer) with at least 150GB of free disk space to accomodate the download.
This code has been tested on Transformers v4.44.0, torch v2.4.0 and 2 A100 80GB GPUs, but any setup that supports meta-llama/Llama-3.1-70B-Instruct should support this model as well. If you run into problems, you can consider doing pip install -U transformers .

## References(s):

- NeMo Aligner
- HelpSteer2-Preference
- HelpSteer2
- Introducing Llama 3.1: Our most capable models to date
- Meta's Llama 3.1 Webpage
[LINK: Meta's Llama 3.1 Webpage](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1)
- Meta's Llama 3.1 Model Card
[LINK: Meta's Llama 3.1 Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md)

## Model Architecture:

Architecture Type: Transformer Network Architecture: Llama 3.1

## Input:

Input Type(s): Text Input Format: String Input Parameters: One Dimensional (1D) Other Properties Related to Input: Max of 128k tokens

## Output:

Output Type(s): Text Output Format: String Output Parameters: One Dimensional (1D) Other Properties Related to Output: Max of 4k tokens

## Software Integration:

Supported Hardware Microarchitecture Compatibility:
- NVIDIA Ampere
- NVIDIA Hopper
- NVIDIA Turing Supported Operating System(s): Linux

## Model Version:

v1.0

## Training & Evaluation:

## Alignment methodology

- REINFORCE implemented in NeMo Aligner

## Datasets:

Data Collection Method by dataset
- [Hybrid: Human, Synthetic]
Labeling Method by dataset
- [Human]
Link:
- HelpSteer2
Properties (Quantity, Dataset Descriptions, Sensor(s)):
- 21, 362 prompt-responses built to make more models more aligned with human preference - specifically more helpful, factually-correct, coherent, and customizable based on complexity and verbosity.
- 20, 324 prompt-responses used for training and 1, 038 used for validation.

## Inference:

Engine: Triton Test Hardware: H100, A100 80GB, A100 40GB
[LINK: Triton](https://developer.nvidia.com/triton-inference-server)

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns here .
Please report security vulnerabilities or NVIDIA AI Concerns here .

## Citation

If you find this model useful, please cite the following works

## Model tree for nvidia/Llama-3.1-Nemotron-70B-Instruct-HF

Base model

## Dataset used to train nvidia/Llama-3.1-Nemotron-70B-Instruct-HF

## Spaces using nvidia/Llama-3.1-Nemotron-70B-Instruct-HF 69

## Collection including nvidia/Llama-3.1-Nemotron-70B-Instruct-HF

## Papers for nvidia/Llama-3.1-Nemotron-70B-Instruct-HF

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
nvidia/Llama-3.1-Nemotron-70B-Instruct-HF is supported by the following Inference Providers:

--------------------