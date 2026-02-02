# Llama-3.1-Nemotron-Nano-8B-v1
**URL:** https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1
**Page Title:** nvidia/Llama-3.1-Nemotron-Nano-8B-v1 · Hugging Face
--------------------


## Llama-3.1-Nemotron-Nano-8B-v1

## Model Overview

Llama-3.1-Nemotron-Nano-8B-v1 is a large language model (LLM) which is a derivative of Meta Llama-3.1-8B-Instruct (AKA the reference model). It is a reasoning model that is post trained for reasoning, human chat preferences, and tasks, such as RAG and tool calling.
Llama-3.1-Nemotron-Nano-8B-v1 is a model which offers a great tradeoff between model accuracy and efficiency. It is created from Llama 3.1 8B Instruct and offers improvements in model accuracy. The model fits on a single RTX GPU and can be used locally. The model supports a context length of 128K.
This model underwent a multi-phase post-training process to enhance both its reasoning and non-reasoning capabilities. This includes a supervised fine-tuning stage for Math, Code, Reasoning, and Tool Calling as well as multiple reinforcement learning (RL) stages using REINFORCE (RLOO) and Online Reward-aware Preference Optimization (RPO) algorithms for both chat and instruction-following. The final model checkpoint is obtained after merging the final SFT and Online RPO checkpoints. Improved using Qwen.
This model is part of the Llama Nemotron Collection. You can find the other model(s) in this family here: Llama-3.3-Nemotron-Super-49B-v1
This model is ready for commercial use.

## Feature Voting

We want to hear from you! Share your ideas, vote on what matters, and help shape the future of Nemotron .

## License/Terms of Use

GOVERNING TERMS: Your use of this model is governed by the NVIDIA Open Model License . Additional Information: Llama 3.1 Community License Agreement . Built with Llama.
Model Developer: NVIDIA
Model Dates: Trained between August 2024 and March 2025
Data Freshness: The pretraining data has a cutoff of 2023 per Meta Llama 3.1 8B

## Use Case:

Developers designing AI Agent systems, chatbots, RAG systems, and other AI-powered applications. Also suitable for typical instruction-following tasks. Balance of model accuracy and compute efficiency (the model fits on a single RTX GPU and can be used locally).

## Release Date:

3/18/2025

## References

- [2505.00949] Llama-Nemotron: Efficient Reasoning Models
- [2502.00203] Reward-aware Preference Optimization: A Unified Mathematical Framework for Model Alignment

## Model Architecture

Architecture Type: Dense decoder-only Transformer model
Network Architecture: Llama 3.1 8B Instruct

## Intended use

Llama-3.1-Nemotron-Nano-8B-v1 is a general purpose reasoning and chat model intended to be used in English and coding languages. Other non-English languages (German, French, Italian, Portuguese, Hindi, Spanish, and Thai) are also supported.

## Input:

- Input Type: Text
- Input Format: String
- Input Parameters: One-Dimensional (1D)
- Other Properties Related to Input: Context length up to 131,072 tokens

## Output:

- Output Type: Text
- Output Format: String
- Output Parameters: One-Dimensional (1D)
- Other Properties Related to Output: Context length up to 131,072 tokens

## Model Version:

1.0 (3/18/2025)

## Software Integration

- Runtime Engine: NeMo 24.12
- Recommended Hardware Microarchitecture Compatibility: NVIDIA Hopper NVIDIA Ampere
- NVIDIA Hopper
- NVIDIA Ampere

## Quick Start and Usage Recommendations:

- Reasoning mode (ON/OFF) is controlled via the system prompt, which must be set as shown in the example below. All instructions should be contained within the user prompt
- We recommend setting temperature to 0.6 , and Top P to 0.95 for Reasoning ON mode
- We recommend using greedy decoding for Reasoning OFF mode
- We have provided a list of prompts to use for evaluation for each benchmark where a specific template is required
- The model will include <think></think> if no reasoning was necessary in Reasoning ON model, this is expected behaviour
You can try this model out through the preview API, using this link: Llama-3.1-Nemotron-Nano-8B-v1 .
See the snippet below for usage with Hugging Face Transformers library. Reasoning mode (ON/OFF) is controlled via system prompt. Please see the example below.
Our code requires the transformers package version to be 4.44.2 or higher.

### Example of “Reasoning On:”

### Example of “Reasoning Off:”

For some prompts, even though thinking is disabled, the model emergently prefers to think before responding. But if desired, the users can prevent it by pre-filling the assistant response.

## Inference:

Engine: Transformers Test Hardware:
- BF16: 1x RTX 50 Series GPUs 1x RTX 40 Series GPUs 1x RTX 30 Series GPUs 1x H100-80GB GPU 1x A100-80GB GPU Jetson AGX Thor
- 1x RTX 50 Series GPUs
- 1x RTX 40 Series GPUs
- 1x RTX 30 Series GPUs
- 1x H100-80GB GPU
- 1x A100-80GB GPU
- Jetson AGX Thor
Preferred/Supported] Operating System(s): Linux

## Training Datasets

A large variety of training data was used for the post-training pipeline, including manually annotated data and synthetic data.
The data for the multi-stage post-training phases for improvements in Code, Math, and Reasoning is a compilation of SFT and RL data that supports improvements of math, code, general reasoning, and instruction following capabilities of the original Llama instruct model.
Prompts have been sourced from either public and open corpus or synthetically generated. Responses were synthetically generated by a variety of models, with some prompts containing responses for both Reasoning On and Off modes, to train the model to distinguish between two modes.
Data Collection for Training Datasets:
- Hybrid: Automated, Human, Synthetic
Data Labeling for Training Datasets:
- N/A

## Evaluation Datasets

We used the datasets listed below to evaluate Llama-3.1-Nemotron-Nano-8B-v1.
Data Collection for Evaluation Datasets: Hybrid: Human/Synthetic
Data Labeling for Evaluation Datasets: Hybrid: Human/Synthetic/Automatic

## Evaluation Results

These results contain both “Reasoning On”, and “Reasoning Off”. We recommend using temperature= 0.6 , top_p= 0.95 for “Reasoning On” mode, and greedy decoding for “Reasoning Off” mode. All evaluations are done with 32k sequence length. We run the benchmarks up to 16 times and average the scores to be more accurate.
NOTE: Where applicable, a Prompt Template will be provided. While completing benchmarks, please ensure that you are parsing for the correct output format as per the provided prompt in order to reproduce the benchmarks seen below.

### MT-Bench

### MATH500

User Prompt Template:

### AIME25

User Prompt Template:

### GPQA-D

User Prompt Template:

### IFEval Average

### BFCL v2 Live

User Prompt Template:

### MBPP 0-shot

User Prompt Template:

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability , Bias , Safety & Security , and Privacy Subcards.
Please report security vulnerabilities or NVIDIA AI Concerns here .

## Citation

## Model tree for nvidia/Llama-3.1-Nemotron-Nano-8B-v1

## Spaces using nvidia/Llama-3.1-Nemotron-Nano-8B-v1 9

## Collection including nvidia/Llama-3.1-Nemotron-Nano-8B-v1

## Papers for nvidia/Llama-3.1-Nemotron-Nano-8B-v1

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
nvidia/Llama-3.1-Nemotron-Nano-8B-v1 is supported by the following Inference Providers:

--------------------