# Falcon3-10B-Instruct
**URL:** https://huggingface.co/tiiuae/Falcon3-10B-Instruct
**Page Title:** tiiuae/Falcon3-10B-Instruct · Hugging Face
--------------------


## Falcon3-10B-Instruct

Falcon3 family of Open Foundation Models is a set of pretrained and instruct LLMs ranging from 1B to 10B parameters.
This repository contains the Falcon3-10B-Instruct . It achieves state-of-the-art results (at the time of release) on reasoning, language understanding, instruction following, code and mathematics tasks.
Falcon3-10B-Instruct supports 4 languages (English, French, Spanish, Portuguese) and a context length of up to 32K.

## Model Details

- Architecture Transformer-based causal decoder-only architecture 40 decoder blocks Grouped Query Attention (GQA) for faster inference: 12 query heads and 4 key-value heads Wider head dimension: 256 High RoPE value to support long context understanding: 1000042 Uses SwiGLu and RMSNorm 32K context length 131K vocab size
- Transformer-based causal decoder-only architecture
- 40 decoder blocks
- Grouped Query Attention (GQA) for faster inference: 12 query heads and 4 key-value heads
- Wider head dimension: 256
- High RoPE value to support long context understanding: 1000042
- Uses SwiGLu and RMSNorm
- 32K context length
- 131K vocab size
- Depth up-scaled from Falcon3-7B-Base with 2 Teratokens of datasets comprising of web, code, STEM, high quality and mutlilingual data using 1024 H100 GPU chips
- Posttrained on 1.2 million samples of STEM, conversational, code, safety and function call data
- Supports EN, FR, ES, PT
- Developed by Technology Innovation Institute
- License: TII Falcon-LLM License 2.0
- Model Release Date: December 2024

## Getting started

## Benchmarks

We report the official HuggingFace leaderboard normalized evaluations Open LLM Leaderboard Evaluation Results in the following table.
Also, we report in the following table our internal pipeline benchmarks.
- We use lm-evaluation harness .
[LINK: lm-evaluation harness](https://github.com/EleutherAI/lm-evaluation-harness)
- We report raw scores obtained by applying chat template and fewshot_as_multiturn.
- We use same batch-size across all models.

## Useful links

- View our release blogpost .
- Feel free to join our discord server if you have any questions or to interact with our researchers and developers.

## Technical Report

Coming soon....

## Citation

If Falcon3 family were helpful in your work, feel free to give us a cite.

## Open LLM Leaderboard Evaluation Results

Detailed results can be found here

## Model tree for tiiuae/Falcon3-10B-Instruct

Base model

## Spaces using tiiuae/Falcon3-10B-Instruct 15

## Collection including tiiuae/Falcon3-10B-Instruct

## Evaluation results

- strict accuracy on IFEval (0-Shot) Open LLM Leaderboard 78.170
- normalized accuracy on BBH (3-Shot) Open LLM Leaderboard 44.820
- exact match on MATH Lvl 5 (4-Shot) Open LLM Leaderboard 25.910
- acc_norm on GPQA (0-shot) Open LLM Leaderboard 10.510
- acc_norm on MuSR (0-shot) Open LLM Leaderboard 13.610
- accuracy on MMLU-PRO (5-shot) test set Open LLM Leaderboard 38.100

--------------------