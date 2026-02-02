# DeepCoder-14B-Preview
**URL:** https://huggingface.co/agentica-org/DeepCoder-14B-Preview
**Page Title:** agentica-org/DeepCoder-14B-Preview · Hugging Face
--------------------


## DeepCoder Overview

DeepCoder-14B-Preview is a code reasoning LLM fine-tuned from DeepSeek-R1-Distilled-Qwen-14B using distributed reinforcement learning (RL) to scale up to long context lengths. The model achieves 60.6% Pass@1 accuracy on LiveCodeBench v5 (8/1/24-2/1/25), representing a 8% improvement over the base model (53%) and achieving similar performance to OpenAI's o3-mini with just 14B parameters.

## Data

Our training dataset consists of approximately 24K unique problem-tests pairs compiled from:
- Taco-Verified
- PrimeIntellect SYNTHETIC-1
- LiveCodeBench v5 (5/1/23-7/31/24)

## Training Recipe

Our training recipe relies on an improved version of GRPO (GRPO+) and iterative context lengthening, introduced in DeepScaleR.

### GRPO+

We enhance the original GRPO algorithm with insights from DAPO to enable more stable training:
- Offline Difficulty Filtering: DAPO employs online dynamic sampling, discarding both entirely correct and entirely incorrect samples on the fly. While this helps maintain a more stable effective batch size, it introduces significant runtime overhead due to rejection sampling. Instead, we perform offline difficulty filtering on a subset of coding problems to ensure the training dataset remains within a suitable difficulty range.
- No Entropy Loss: We observed that including an entropy loss term often led to instability, with entropy growing exponentially and ultimately collapsing training. To mitigate this, we eliminate the entropy loss entirely.
- No KL Loss: Eliminating KL loss prevents the LLM from staying within trust region of the original SFT model. This removal also obviates the need to compute log probabilities for the reference policy, thereby accelerating training.
- Overlong Filtering (from DAPO): To preserve long-context reasoning, we mask the loss for truncated sequences. This technique enables DeepCoder to generalize to 64K-context inference despite being trained with a 32K context.
- Clip High (from DAPO): By increasing the upper bound in GRPO/PPO’s surrogate loss, we encourage more exploration and more stable entropy.

### Iterative Context Lengthening

Our original Deepscaler-1.5B-Preview scaled long context training from 8K→16K→24K, achieving 33→38→43% on AIME respectively. Similarly, Deepcoder-14B-Preview is trained on 16K→32K, achieving 54→58% on LiveCodeBench (v5). DeepCoder-14B-Preview successfully generalizes to longer contexts when evaluated at 64K context, reaching 60.6%.
DeepCoder generalizes better to long contexts than the base distilled model, due to DAPO's overlong filtering. However, it's longer responses are often truncated when the max length is capped at 16K, which can lower its scores.
A more detailed description of the training recipe can be found in our blog post .

## Evaluation

We evaluate Deepcoder-14B-Preview on various coding benchmarks, including LiveCodeBench (LCBv5), Codeforces, and HumanEval+.

## Serving DeepCoder

Our model can be served using popular high-performance inference systems:
- vLLM
- Hugging Face Text Generation Inference (TGI)
- SGLang
- TensorRT-LLM
All these systems support the OpenAI Chat Completions API format.

### Usage Recommendations

Our usage recommendations are similar to those of R1 and R1 Distill series:
- Avoid adding a system prompt; all instructions should be contained within the user prompt.
- temperature = 0.6
- top_p = 0.95
- This model performs best with max_tokens set to at least 64000

## License

This project is released under the MIT License, reflecting our commitment to open and accessible AI development.
We believe in democratizing AI technology by making our work freely available for anyone to use, modify, and build upon.
This permissive license ensures that researchers, developers, and enthusiasts worldwide can leverage and extend our work without restrictions, fostering innovation and collaboration in the AI community.

## Acknowledgement

- Our training experiments are powered by our heavily modified fork of Verl , an open-source post-training library.
[LINK: Verl](https://github.com/agentica-project/verl)
- Our model is trained on top of DeepSeek-R1-Distill-Qwen-14B .
- Our work is done as part of Berkeley Sky Computing Lab and Berkeley AI Research .

## Citation

## Model tree for agentica-org/DeepCoder-14B-Preview

Base model

## Datasets used to train agentica-org/DeepCoder-14B-Preview

## Spaces using agentica-org/DeepCoder-14B-Preview 34

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
agentica-org/DeepCoder-14B-Preview is supported by the following Inference Providers:

--------------------