# Tiny StarCoder Py
**URL:** https://huggingface.co/bigcode/tiny_starcoder_py
**Page Title:** bigcode/tiny_starcoder_py · Hugging Face
--------------------


## TinyStarCoderPy

This is a 164M parameters model with the same architecture as StarCoder (8k context length, MQA & FIM). It was trained on the Python data from StarCoderData for ~6 epochs which amounts to 100B tokens.

## Use

### Intended use

The model was trained on GitHub code, to assist with some tasks like Assisted Generation . For pure code completion, we advise using our 15B models StarCoder or StarCoderBase .

### Generation

### Fill-in-the-middle

Fill-in-the-middle uses special tokens to identify the prefix/middle/suffix part of the input and output:

## Training

## Model

- Architecture: GPT-2 model with multi-query attention and Fill-in-the-Middle objective
- Pretraining steps: 50k
- Pretraining tokens: 100 billion
- Precision: bfloat16

## Hardware

- GPUs: 32 Tesla A100
- Training time: 18 hours

## Software

- Orchestration: Megatron-LM
[LINK: Megatron-LM](https://github.com/bigcode-project/Megatron-LM)
- Neural networks: PyTorch
[LINK: PyTorch](https://github.com/pytorch/pytorch)
- BP16 if applicable: apex
[LINK: apex](https://github.com/NVIDIA/apex)

## License

The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement here .

## Model tree for bigcode/tiny_starcoder_py

## Dataset used to train bigcode/tiny_starcoder_py

## Spaces using bigcode/tiny_starcoder_py 48

## Evaluation results

- pass@1 on HumanEval self-reported 7.84%

--------------------