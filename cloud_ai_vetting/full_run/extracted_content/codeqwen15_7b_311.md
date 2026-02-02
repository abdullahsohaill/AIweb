# CodeQwen1.5-7B
**URL:** https://huggingface.co/Qwen/CodeQwen1.5-7B
**Page Title:** Qwen/CodeQwen1.5-7B · Hugging Face
--------------------


## CodeQwen1.5-7B

## Introduction

CodeQwen1.5 is the Code-Specific version of Qwen1.5. It is a transformer-based decoder-only language model pretrained on a large amount of data of codes.
- Strong code generation capabilities and competitve performance across a series of benchmarks;
- Supporting long context understanding and generation with the context length of 64K tokens;
- Supporting 92 coding languages
- Excellent performance in text-to-SQL, bug fix, etc.
For more details, please refer to our blog post and GitHub repo .
[LINK: blog post](https://qwenlm.github.io/blog/codeqwen1.5/)
[LINK: GitHub repo](https://github.com/QwenLM/Qwen1.5)

## Model Details

CodeQwen1.5 is based on Qwen1.5, a language model series including decoder language models of different model sizes. It is trained on 3 trillion tokens of data of codes, and it includes group query attention (GQA) for efficient inference.

## Requirements

The code of Qwen1.5 has been in the latest Hugging face transformers and we advise you to install transformers>=4.37.0 , or you might encounter the following error:

## Usage

For the base language model, we do not advise you to use it for chat. You can use it for finetuning, and you can also use it for code infilling, code generation, etc., but please be careful about your stopping criteria.

## Citation

If you find our work helpful, feel free to give us a cite.

## Model tree for Qwen/CodeQwen1.5-7B

## Spaces using Qwen/CodeQwen1.5-7B 9

## Collection including Qwen/CodeQwen1.5-7B

## Paper for Qwen/CodeQwen1.5-7B


--------------------