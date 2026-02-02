# Llama-3.1-8B-Lexi-Uncensored-V2
**URL:** https://huggingface.co/Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2
**Page Title:** Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2 · Hugging Face
--------------------


## VERSION 2 Update Notes:

- More compliant
- Smarter
- For best response, use this system prompt (feel free to expand upon it as you wish):
Think step by step with a logical reasoning and intellectual sense before you provide any response.
- For more uncensored and compliant response, you can expand the system message differently, or simply enter a dot "." as system message.
For more uncensored and compliant response, you can expand the system message differently, or simply enter a dot "." as system message.
- IMPORTANT: Upon further investigation, the Q4 seems to have refusal issues sometimes. 
There seems to be some of the fine-tune loss happening due to the quantization. I will look into it for V3. 
Until then, I suggest you run F16 or Q8 if possible.
IMPORTANT: Upon further investigation, the Q4 seems to have refusal issues sometimes. 
There seems to be some of the fine-tune loss happening due to the quantization. I will look into it for V3. 
Until then, I suggest you run F16 or Q8 if possible.

## GENERAL INFO:

This model is based on Llama-3.1-8b-Instruct, and is governed by META LLAMA 3.1 COMMUNITY LICENSE AGREEMENT
[LINK: META LLAMA 3.1 COMMUNITY LICENSE AGREEMENT](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE)
Lexi is uncensored, which makes the model compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones.
You are responsible for any content you create using this model. Please use it responsibly.
Lexi is licensed according to Meta's Llama license. I grant permission for any use, including commercial, that falls within accordance with Meta's Llama-3.1 license.

## IMPORTANT:

Use the same template as the official Llama 3.1 8B instruct.
System tokens must be present during inference, even if you set an empty system message. If you are unsure, just add a short system message as you wish.

## FEEDBACK:

If you find any issues or have suggestions for improvements, feel free to leave a review and I will look into it for upcoming improvements and next version.

## Open LLM Leaderboard Evaluation Results

Detailed results can be found here

## Model tree for Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2

## Spaces using Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2 37

## Evaluation results

- strict accuracy on IFEval (0-Shot) Open LLM Leaderboard 77.920
- normalized accuracy on BBH (3-Shot) Open LLM Leaderboard 29.690
- exact match on MATH Lvl 5 (4-Shot) Open LLM Leaderboard 16.920
- acc_norm on GPQA (0-shot) Open LLM Leaderboard 4.360
- acc_norm on MuSR (0-shot) Open LLM Leaderboard 7.770
- accuracy on MMLU-PRO (5-shot) test set Open LLM Leaderboard 30.900

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2 is supported by the following Inference Providers:

--------------------