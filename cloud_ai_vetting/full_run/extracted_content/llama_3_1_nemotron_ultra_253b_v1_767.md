# Llama-3_1-Nemotron-Ultra-253B-v1
**URL:** https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1
**Page Title:** nvidia/Llama-3_1-Nemotron-Ultra-253B-v1 · Hugging Face
--------------------


## Llama-3.1-Nemotron-Ultra-253B-v1

## Model Overview

Llama-3.1-Nemotron-Ultra-253B-v1 is a large language model (LLM) which is a derivative of Meta Llama-3.1-405B-Instruct (AKA the reference model ). It is a reasoning model that is post trained for reasoning, human chat preferences, and tasks, such as RAG and tool calling. The model supports a context length of 128K tokens. This model fits on a single 8xH100 node for inference.
Llama-3.1-Nemotron-Ultra-253B-v1 is a model which offers a great tradeoff between model accuracy and efficiency. Efficiency (throughput) directly translates to savings. Using a novel Neural Architecture Search (NAS) approach, we greatly reduce the model’s memory footprint, enabling larger workloads, as well as reducing the number of GPUs required to run the model in a data center environment. This NAS approach enables the selection of a desired point in the accuracy-efficiency tradeoff. Furthermore, by using a novel method to vertically compress the model (see details here ), it also offers a significant improvement in latency.
The model underwent a multi-phase post-training process to enhance both its reasoning and non-reasoning capabilities. This includes a supervised fine-tuning stage for Math, Code, Reasoning, Chat, and Tool Calling as well as multiple reinforcement learning (RL) stages using Group Relative Policy Optimization (GRPO) algorithms for reasoning, chat, and instruction-following.
This model is ready for commercial use.
For more details on how the model was trained, please see our technical report and blog .
[LINK: blog](https://developer.nvidia.com/blog/build-enterprise-ai-agents-with-advanced-open-nvidia-llama-nemotron-reasoning-models/)
This model is part of the Llama Nemotron Collection. You can find the other model(s) in this family here:
- Llama-3.1-Nemotron-Nano-8B-v1
- Llama-3.3-Nemotron-Super-49B-v1

## Feature Voting

We want to hear from you! Share your ideas, vote on what matters, and help shape the future of Nemotron .

## License/Terms of Use

GOVERNING TERMS: Your use of this model is governed by the NVIDIA Open Model License. Additional Information: Llama 3.1 Community License Agreement . Built with Llama.
Model Developer: NVIDIA
Model Dates: Trained between November 2024 and April 2025
Data Freshness: The pretraining data has a cutoff of 2023 per Llama-3.1-405B-Instruct

### Use Case:

Developers designing AI Agent systems, chatbots, RAG systems, and other AI-powered applications. Also suitable for typical instruction-following tasks.

### Release Date:

2025-04-07

## References

- [2505.00949] Llama-Nemotron: Efficient Reasoning Models
- [2502.00203] Reward-aware Preference Optimization: A Unified Mathematical Framework for Model Alignment
- [2411.19146]Puzzle: Distillation-Based NAS for Inference-Optimized LLMs
- [2503.18908]FFN Fusion: Rethinking Sequential Computation in Large Language Models

## Model Architecture

Architecture Type: Dense decoder-only Transformer model Network Architecture: Llama-3.1-405B-Instruct, customized through Neural Architecture Search (NAS)
**This model was developed based on Llama-3.1-405B-Instruct ** This model has 253B model parameters.
The model is a derivative of Llama 3.1-405B-Instruct, using Neural Architecture Search (NAS). The NAS algorithm results in non-standard and non-repetitive blocks. This includes the following:
- Skip attention: In some blocks, the attention is skipped entirely, or replaced with a single linear layer.
- Variable FFN: The expansion/compression ratio in the FFN layer is different between blocks.
- FFN Fusion: When several consecutive attention layers are skipped, which can result in a sequence of multiple FFNs, that sequence of FFNs are fused into a smaller number of wider FFN layers.
For each block of the reference model, we create multiple variants providing different tradeoffs of quality vs. computational complexity, discussed in more depth below. We then search over the blocks to create a model which meets the required throughput and memory while minimizing the quality degradation. To recover performance, the model initially undergoes knowledge distillation (KD) for 65 billion tokens. This is followed by a continual pretraining (CPT) phase for 88 billion tokens.

## Intended use

Llama-3.1-Nemotron-Ultra-253B-v1 is a general purpose reasoning and chat model intended to be used in English and coding languages. Other non-English languages (German, French, Italian, Portuguese, Hindi, Spanish, and Thai) are also supported.

## Input

- Input Type: Text
- Input Format: String
- Input Parameters: One-Dimensional (1D)
- Other Properties Related to Input: Context length up to 131,072 tokens

## Output

- Output Type: Text
- Output Format: String
- Output Parameters: One-Dimensional (1D)
- Other Properties Related to Output: Context length up to 131,072 tokens

## Software Integration

- Runtime Engine: Transformers
- Recommended Hardware Microarchitecture Compatibility: NVIDIA Hopper NVIDIA Ampere
- NVIDIA Hopper
- NVIDIA Ampere
- Preferred Operating System(s): Linux

## Model Version

1.0 (4/7/2025)

## Quick Start and Usage Recommendations:

- Reasoning mode (ON/OFF) is controlled via the system prompt, which must be set as shown in the example below. All instructions should be contained within the user prompt
- We recommend setting temperature to `0.6`, and Top P to `0.95` for Reasoning ON mode
- We recommend using greedy decoding (temperature 0) for Reasoning OFF mode
- We do not recommend to add additional system prompts besides the control prompt, all instructions should be put into user query
- We have provided a list of prompts to use for evaluation for each benchmark where a specific template is required
- The model will include <think></think> if no reasoning was necessary in Reasoning ON model, this is expected behaviour
You can try this model out through the preview API, using this link: Llama-3_1-Nemotron-Ultra-253B-v1 .

### Use It with Transformers

See the snippet below for usage with Hugging Face Transformers library. Reasoning mode (ON/OFF) is controlled via system prompt. Please see the example below
[LINK: Hugging Face Transformers](https://huggingface.co/docs/transformers/main/en/index)
We recommend using the transformers package with version 4.48.3. Example of reasoning on:
Example of reasoning off:

### Use It with vLLM

An example on how to serve with vLLM:

## Inference:

Engine:
- Transformers
Test Hardware:
- BF16: 8x NVIDIA H100-80GB 4x NVIDIA B100
- 8x NVIDIA H100-80GB
- 4x NVIDIA B100
- FP 8 4x NVIDIA H100-80GB
- 4x NVIDIA H100-80GB

## Training and Evaluation Datasets

## Training Datasets

A large variety of training data was used for the knowledge distillation phase before post-training pipeline, 3 of which included: FineWeb, Buzz-V1.2, and Dolma.
The data for the multi-stage post-training phases is a compilation of SFT and RL data that supports improvements of math, code, general reasoning, and instruction following capabilities of the original Llama instruct model.
Prompts have been sourced from either public and open corpus or synthetically generated. Responses were synthetically generated by a variety of models, with some prompts containing responses for both reasoning on and off modes, to train the model to distinguish between two modes. This model was improved with Qwen.
We have released our Llama-Nemotron-Post-Training-Dataset to promote openness and transparency in model development and improvement.
Data Collection for Training Datasets:
- Hybrid: Automated, Human, Synthetic
Data Labeling for Training Datasets:
- Hybrid: Automated, Human, Synthetic

## Evaluation Datasets

We used the datasets listed in the next section to evaluate Llama-3.1-Nemotron-Ultra-253B-v1.
Data Collection for Evaluation Datasets:
- Hybrid: Human/Synthetic
Data Labeling for Evaluation Datasets:
- Hybrid: Human/Synthetic/Automatic

## Evaluation Results

These results contain both Reasoning On, and Reasoning Off. We recommend using temperature=`0.6`, top_p=`0.95` for Reasoning On mode, and greedy decoding for Reasoning Off mode. All evaluations are done with 32k sequence length. We run the benchmarks up to 16 times and average the scores to be more accurate.
NOTE: Where applicable, a Prompt Template will be provided. While completing benchmarks, please ensure that you are parsing for the correct output format as per the provided prompt in order to reproduce the benchmarks seen below.

### GPQA

User Prompt Template:

### AIME25

User Prompt Template:

### BFCL V2 Live

User Prompt Template:

### LiveCodeBench (20240801-20250201)

User Prompt Template (without starter code):
User Prompt Template (with starter code):

### IFEval

### MATH500

User Prompt Template:

### JudgeBench

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability , Bias , Safety & Security , and Privacy Subcards.
Please report security vulnerabilities or NVIDIA AI Concerns here .

## Citation

## Model tree for nvidia/Llama-3_1-Nemotron-Ultra-253B-v1

## Spaces using nvidia/Llama-3_1-Nemotron-Ultra-253B-v1 12

## Collection including nvidia/Llama-3_1-Nemotron-Ultra-253B-v1

## Papers for nvidia/Llama-3_1-Nemotron-Ultra-253B-v1


--------------------