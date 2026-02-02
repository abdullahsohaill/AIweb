# Dolphin3.0-Qwen2.5-1.5B
**URL:** https://huggingface.co/cognitivecomputations/Dolphin3.0-Qwen2.5-1.5B
**Page Title:** dphn/Dolphin3.0-Qwen2.5-1.5B · Hugging Face
--------------------


## Dolphin 3.0 Qwen 2.5 1.5B 🐬

Part of the Dolphin 3.0 Collection
Curated and trained by Eric Hartford , Ben Gitter , BlouseJury and Cognitive Computations
Discord: https://discord.gg/cognitivecomputations

## Sponsors

Our appreciation for the generous sponsors of Dolphin 3.0:
- Crusoe Cloud - provided 16x L40s for training and evals
- Akash - provided on-demand 8x H100 for training
- Lazarus - provided 16x H100 for training
- Cerebras - provided excellent and fast inference services for data labeling
- Andreessen Horowitz - provided a grant that make Dolphin 1.0 possible and enabled me to bootstrap my homelab

## What is Dolphin?

Dolphin 3.0 is the next generation of the Dolphin series of instruct-tuned models.  Designed to be the ultimate general purpose local model, enabling coding, math, agentic, function calling, and general use cases.
Dolphin aims to be a general purpose model, similar to the models behind ChatGPT, Claude, Gemini.  But these models present problems for businesses seeking to include AI in their products.
- They maintain control of the system prompt, deprecating and changing things as they wish, often causing software to break.
- They maintain control of the model versions, sometimes changing things silently, or deprecating older models that your business relies on.
- They maintain control of the alignment, and in particular the alignment is one-size-fits all, not tailored to the application.
- They can see all your queries and they can potentially use that data in ways you wouldn't want.
Dolphin, in contrast, is steerable and gives control to the system owner. You set the system prompt.  You decide the alignment.  You have control of your data.  Dolphin does not impose its ethics or guidelines on you.  You are the one who decides the guidelines.
Dolphin belongs to YOU, it is your tool, an extension of your will.
Just as you are personally responsible for what you do with a knife, gun, fire, car, or the internet, you are the creator and originator of any content you generate with Dolphin.
https://erichartford.com/uncensored-models

## Chat Template

We use ChatML for the chat template.

## System Prompt

In Dolphin, the system prompt is what you use to set the tone and alignment of the responses.  You can set a character, a mood, rules for its behavior, and it will try its best to follow them.
Make sure to set the system prompt in order to set the tone and guidelines for the responses - Otherwise, it will act in a default way that might not be what you want.
Example use of system prompt:

## Sample Outputs

TBD

## How to use

There are many ways to use a huggingface model including:
- ollama
- LM Studio
- Huggingface Transformers library
- vllm
- sglang
- tgi

## Evals

TBD

## Appreciation

Respect and thanks to the creators of the open source datasets that were used:
- OpenCoder-LLM (opc-sft-stage1, opc-sft-stage2)
- microsoft (orca-agentinstruct-1M-v1, orca-math-word-problems-200k)
- NousResearch (hermes-function-calling-v1)
- AI-MO (NuminaMath-CoT, NuminaMath-TIR)
- allenai (tulu-3-sft-mixture)
- HuggingFaceTB (smoltalk)
- m-a-p (CodeFeedback-Filtered-Instruction, Code-Feedback)
Special thanks to
- Meta, Qwen, and OpenCoder, who wrote papers and published models that were instrumental in creating Dolphin 3.0.
- RLHFlow for the excellent reward model used to filter the datasets
- Deepseek, for the ridiculously fast Deepseek-V3 that we used to augment the data.
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for dphn/Dolphin3.0-Qwen2.5-1.5B

Base model

## Datasets used to train dphn/Dolphin3.0-Qwen2.5-1.5B

## Space using dphn/Dolphin3.0-Qwen2.5-1.5B 1


--------------------