# Mamba
**URL:** https://huggingface.co/state-spaces/mamba-130m-hf
**Page Title:** state-spaces/mamba-130m-hf · Hugging Face
--------------------


## Mamba

This repository contains the transfromers compatible mamba-2.8b . The checkpoints are untouched, but the full config.json and tokenizer are pushed to this repo.

## Usage

You need to install transformers from main until transformers=4.39.0 is released.
We also recommend you to install both causal_conv_1d and mamba-ssm using:
If any of these two is not installed, the "eager" implementation will be used. Otherwise the more optimised cuda kernels will be used.

## Generation

You can use the classic generate API:

## PEFT finetuning example

In order to finetune using the peft library, we recommend keeping the model in float32!

## Model tree for state-spaces/mamba-130m-hf

## Spaces using state-spaces/mamba-130m-hf 10

## Collection including state-spaces/mamba-130m-hf


--------------------