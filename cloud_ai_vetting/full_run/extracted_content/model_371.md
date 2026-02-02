# Model
**URL:** https://huggingface.co/Kwaipilot/SRPO-Qwen-32B
**Page Title:** Kwaipilot/SRPO-Qwen-32B · Hugging Face
--------------------


## SRPO: A Cross-Domain Implementation of Large-Scale Reinforcement Learning on LLM

## Overview

We introduce SRPO (two-Staged history-Resampling Policy Optimization) , a novel RL framework designed to systematically address large-scale multi-domain reasoning challenges. SRPO successfully surpasses the performance of DeepSeek-R1-Zero-32B on both the AIME24 and LiveCodeBench benchmarks while using only about 1/10 of the training steps.
Building upon Group Relative Policy Optimization (GRPO), SRPO introduces two key methodological innovations:
- A two-stage cross-domain training paradigm designed to balance the development of mathematical reasoning and coding proficiency
- History Resampling (HR) , a technique to address ineffective samples and enhance training efficiency
Our approach demonstrates that with proper training methodology, the same base model (Qwen2.5-32B) can achieve superior performance across diverse domains without requiring extensive training resources.

## Main Results

Figure: SRPO achieves superior results with only 10% of DeepSeek's training steps. The values shown are pass@1 scores, averaged over 32 samples per question.

## Training Approach

### Two-Stage Training Paradigm

To address the intrinsic response-length conflict between math and code, SRPO employs a two-stage training approach:
- Stage 1 (Eliciting Reasoning Abilities) : Initial training focuses solely on challenging mathematical data to encourage extended Chain-of-Thought (CoT) capabilities, including reflective thinking and step-by-step decomposition.
Stage 1 (Eliciting Reasoning Abilities) : Initial training focuses solely on challenging mathematical data to encourage extended Chain-of-Thought (CoT) capabilities, including reflective thinking and step-by-step decomposition.
- Stage 2 (Skill Integration) : Once the reasoning foundation is established, coding data is introduced to develop programming proficiency while maintaining the reasoning capabilities from Stage 1.
Stage 2 (Skill Integration) : Once the reasoning foundation is established, coding data is introduced to develop programming proficiency while maintaining the reasoning capabilities from Stage 1.

### History Resampling (HR)

SRPO introduces History Resampling to address ineffective samples that provide minimal gradient signals:
- Filter Out "Too Easy" : Samples where all rollouts get the correct answer are excluded as they provide no informative contrastive signals
- Retain "Informative" : Samples that yield either mixed outcomes or exclusively incorrect outcomes are retained to ensure effective gradient signals
This approach significantly improves computational efficiency and enhances the growth of response length during training.

## Emerging Thinking Behaviors

During RL training, SRPO models gradually develop self-reflection, correction, and backtracking capabilities analogous to human cognitive processes:
Figure: Occurrence of various reasoning patterns during training.
An interesting observed phenomenon is the model's spontaneous use of code to verify mathematical solutions, demonstrating cross-domain skill integration and advanced problem-solving strategies.

## Inference

## Using with vLLM

## Citation

[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for Kwaipilot/SRPO-Qwen-32B

Base model

## Paper for Kwaipilot/SRPO-Qwen-32B


--------------------