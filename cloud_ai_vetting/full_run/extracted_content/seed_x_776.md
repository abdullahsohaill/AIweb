# Seed-X
**URL:** https://huggingface.co/ByteDance-Seed/Seed-X-PPO-7B
**Page Title:** ByteDance-Seed/Seed-X-PPO-7B · Hugging Face
--------------------


## Seed-X-PPO-7B

## Introduction

We are excited to introduce Seed-X , a powerful series of open-source multilingual translation language models, including an instruction model, a reinforcement learning model, and a reward model. It pushes the boundaries of translation capabilities within 7 billion parameters.
We develop Seed-X as an accessible, off-the-shelf tool to support the community in advancing translation research and applications:
- Exceptional translation capabilities : Seed-X exhibits state-of-the-art translation capabilities, on par with or outperforming ultra-large models like Gemini-2.5, Claude-3.5, and GPT-4, as validated by human evaluations and automatic metrics.
- Deployment and inference-friendly : With a compact 7B parameter count and mistral architecture, Seed-X offers outstanding translation performance in a lightweight and efficient package, ideal for deployment and inference.
- Broad domain coverage : Seed-X excels on a highly challenging translation test set spanning diverse domains, including the internet, science and technology, office dialogues, e-commerce, biomedicine, finance, law, literature, and entertainment.
This repo contains the Seed-X-PPO model, with the following features:
- Type: Causal language models
- Training Stage: Pretraining & Post-training
- Support: Multilingual translation among 28 languages
（We recommend using Seed-X-PPO model, as its translation performance is superior to Seed-X-Instruct.）

## Model Downloads

## Quickstart

📮 Notice
- The language tags at the end of the prompt is necessary , which are used in PPO training. For example, when the target language is German, <de> needs to be added. You can refer to the above table for language abbreviations.
- This model is specialized in multilingual translation , which is unexpected to support other tasks.
- We don't have any chat template , thus you don't have to perform tokenizer.apply_chat_template . Please avoid prompting the model in a multi-round conversation format.
- We recommend against using unofficial quantized versions for local deployment. We will soon release an official quantized model and develop a demo on Hugging Face Space.
Here is a simple example demonstrating how to load the model and perform translation using vllm
Recommended: vllm==0.8.0, transformers==4.51.3

## Evaluation

We evaluated Seed-X on a diverse set of translation benchmarks, including FLORES-200, WMT-25, and a publicly released challenge set accompanied by human evaluations. For detailed benchmark results and analysis, please refer to our Technical Report .
[LINK: challenge set](https://github.com/ByteDance-Seed/Seed-X-7B/tree/main/challenge_set)

## License

This project is licensed under OpenMDW. See the LICENSE file for details.
[LINK: LICENSE](https://github.com/ByteDance-Seed/Seed-X-7B/blob/main/LICENSE.openmdw)

## Citation

If you find Seed-X useful for your research and applications, feel free to give us a star ⭐ or cite us using:

## Model tree for ByteDance-Seed/Seed-X-PPO-7B

## Datasets used to train ByteDance-Seed/Seed-X-PPO-7B

## Spaces using ByteDance-Seed/Seed-X-PPO-7B 3

## Collection including ByteDance-Seed/Seed-X-PPO-7B

## Paper for ByteDance-Seed/Seed-X-PPO-7B


--------------------