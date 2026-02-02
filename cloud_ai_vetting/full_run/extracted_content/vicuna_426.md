# Vicuna
**URL:** https://huggingface.co/lmsys/vicuna-13b-delta-v1.1
**Page Title:** lmsys/vicuna-13b-delta-v1.1 · Hugging Face
--------------------

NOTE: New version available Please check out a newer version of the weights here .
[LINK: here](https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md)
NOTE: This "delta model" cannot be used directly. Users have to apply it on top of the original LLaMA weights to get actual Vicuna weights. See instructions .
[LINK: instructions](https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md#how-to-apply-delta-weights-for-weights-v11-and-v0)

## Vicuna Model Card

## Model Details

Vicuna is a chat assistant trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT.
- Developed by: LMSYS
- Model type: An auto-regressive language model based on the transformer architecture.
- License: Non-commercial license
- Finetuned from model: LLaMA .

### Model Sources

- Repository: https://github.com/lm-sys/FastChat
[LINK: https://github.com/lm-sys/FastChat](https://github.com/lm-sys/FastChat)
- Blog: https://lmsys.org/blog/2023-03-30-vicuna/
- Paper: https://arxiv.org/abs/2306.05685
- Demo: https://chat.lmsys.org/

## Uses

The primary use of Vicuna is research on large language models and chatbots.
The primary intended users of the model are researchers and hobbyists in natural language processing, machine learning, and artificial intelligence.

## How to Get Started with the Model

Command line interface: https://github.com/lm-sys/FastChat#vicuna-weights . APIs (OpenAI API, Huggingface API): https://github.com/lm-sys/FastChat/tree/main#api .
[LINK: https://github.com/lm-sys/FastChat#vicuna-weights](https://github.com/lm-sys/FastChat#vicuna-weights)
[LINK: https://github.com/lm-sys/FastChat/tree/main#api](https://github.com/lm-sys/FastChat/tree/main#api)

## Training Details

Vicuna v1.1 is fine-tuned from LLaMA with supervised instruction fine-tuning.
The training data is around 70K conversations collected from ShareGPT.com.
See more details in the "Training Details of Vicuna Models" section in the appendix of this paper .

## Evaluation

Vicuna is evaluated with standard benchmarks, human preference, and LLM-as-a-judge. See more details in this paper and leaderboard .

## Difference between different versions of Vicuna

See vicuna_weights_version.md
[LINK: vicuna_weights_version.md](https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md)

## Spaces using lmsys/vicuna-13b-delta-v1.1 57

## Papers for lmsys/vicuna-13b-delta-v1.1


--------------------