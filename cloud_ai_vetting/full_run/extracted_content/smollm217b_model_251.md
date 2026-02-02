# SmolLM2–1.7B model
**URL:** https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B
**Page Title:** HuggingFaceTB/SmolLM2-1.7B · Hugging Face
--------------------


## SmolLM2

## Table of Contents

- Model Summary
- Evaluation
- Limitations
- Training
- License
- Citation

## Model Summary

SmolLM2 is a family of compact language models available in three size: 135M, 360M, and 1.7B parameters. They are capable of solving a wide range of tasks while being lightweight enough to run on-device. More details in our paper: https://arxiv.org/abs/2502.02737v1
The 1.7B variant demonstrates significant advances over its predecessor SmolLM1-1.7B, particularly in instruction following, knowledge, reasoning, and mathematics. It was trained on 11 trillion tokens using a diverse dataset combination: FineWeb-Edu, DCLM, The Stack, along with new mathematics and coding datasets that we curated and will release soon. We developed the instruct version through supervised fine-tuning (SFT) using a combination of public datasets and our own curated datasets. We then applied Direct Preference Optimization (DPO) using UltraFeedback .
The instruct model additionally supports tasks such as text rewriting, summarization and function calling thanks to datasets developed by Argilla such as Synth-APIGen-v0.1 .
You can find the SFT dataset here: https://huggingface.co/datasets/HuggingFaceTB/smoltalk and finetuning code in the alignement handbook .
[LINK: Synth-APIGen-v0.1](https://huggingface.co/datasets/argilla/Synth-APIGen-v0.1)
[LINK: alignement handbook](https://github.com/huggingface/alignment-handbook/tree/main/recipes/smollm2)
For more details refer to: https://github.com/huggingface/smollm . You will find pre-training, post-training, evaluation and local inference code.
[LINK: https://github.com/huggingface/smollm](https://github.com/huggingface/smollm)

### How to use

- Using full precision
- Using torch.bfloat16

## Evaluation

In this section, we report the evaluation results of SmolLM2. All evaluations are zero-shot unless stated otherwise, and we use lighteval to run them.
[LINK: lighteval](https://github.com/huggingface/lighteval)

## Base Pre-Trained Model

## Instruction Model

## Limitations

SmolLM2 models primarily understand and generate content in English. They can produce text on a variety of topics, but the generated content may not always be factually accurate, logically consistent, or free from biases present in the training data. These models should be used as assistive tools rather than definitive sources of information. Users should always verify important information and critically evaluate any generated content.

## Training

### Model

- Architecture: Transformer decoder
- Pretraining tokens: 11T
- Precision: bfloat16

### Hardware

- GPUs: 256 H100

### Software

- Training Framework: nanotron
[LINK: nanotron](https://github.com/huggingface/nanotron/tree/main)

## License

Apache 2.0

## Citation

## Model tree for HuggingFaceTB/SmolLM2-1.7B

## Spaces using HuggingFaceTB/SmolLM2-1.7B 20

## Collection including HuggingFaceTB/SmolLM2-1.7B

## Paper for HuggingFaceTB/SmolLM2-1.7B


--------------------