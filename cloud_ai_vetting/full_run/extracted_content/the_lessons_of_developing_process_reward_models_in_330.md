# The Lessons of Developing Process Reward Models in Mathematical Reasoning
**URL:** https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B
**Page Title:** Qwen/Qwen2.5-Math-PRM-72B · Hugging Face
--------------------


## Qwen2.5-Math-PRM-72B

## Introduction

In addition to the mathematical Outcome Reward Model (ORM) Qwen2.5-Math-RM-72B, we release the Process Reward Model (PRM), namely Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B. PRMs emerge as a promising approach for process supervision in mathematical reasoning of Large Language Models (LLMs), aiming to identify and mitigate intermediate errors in the reasoning processes. Our trained PRMs exhibit both impressive performance in the Best-of-N (BoN) evaluation and stronger error identification performance in ProcessBench .

## Model Details

For more details, please refer to our paper .

## Requirements

- transformers>=4.40.0 for Qwen2.5-Math models. The latest version is recommended.
For requirements on GPU memory and the respective throughput, see similar results of Qwen2 here .
[LINK: here](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html)

## Quick Start

Qwen2.5-Math-PRM-72B is a process reward model typically used for offering feedback on the quality of reasoning and intermediate steps rather than generation.

### Prerequisites

- Step Separation: We recommend using double line breaks ("\n\n") to separate individual steps within the solution if using responses from Qwen2.5-Math-Instruct.
- Reward Computation: After each step, we insert a special token " <extra_0> ". For reward calculation, we extract the probability score of this token being classified as positive, resulting in a reward value between 0 and 1.

### 🤗 Hugging Face Transformers

Here we show a code snippet to show you how to use the Qwen2.5-Math-PRM-72B with transformers :

## Citation

If you find our work helpful, feel free to give us a citation.

## Model tree for Qwen/Qwen2.5-Math-PRM-72B

Base model

## Space using Qwen/Qwen2.5-Math-PRM-72B 1

## Collection including Qwen/Qwen2.5-Math-PRM-72B

## Papers for Qwen/Qwen2.5-Math-PRM-72B


--------------------