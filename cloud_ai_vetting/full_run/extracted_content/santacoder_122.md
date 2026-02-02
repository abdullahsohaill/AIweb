# SantaCoder
**URL:** https://huggingface.co/bigcode/santacoder
**Page Title:** bigcode/santacoder · Hugging Face
--------------------


## SantaCoder

Play with the model on the SantaCoder Space Demo .

## Table of Contents

- Model Summary
- Use
- Limitations
- Training
- License
- Citation

## Model Summary

The SantaCoder models are a series of 1.1B parameter models trained on the Python, Java, and JavaScript subset of The Stack (v1.1) (which excluded opt-out requests). 
The main model uses Multi Query Attention , a context window of 2048 tokens, and was trained using near-deduplication and comment-to-code ratio as filtering criteria and using the Fill-in-the-Middle objective .
In addition there are several models that were trained on datasets with different filter parameters and with architecture and objective variations.
- Repository: bigcode/Megatron-LM
[LINK: bigcode/Megatron-LM](https://github.com/bigcode-project/Megatron-LM)
- Project Website: bigcode-project.org
- Paper: 🎅SantaCoder: Don't reach for the stars!🌟
- Point of Contact: contact@bigcode-project.org
- Languages: Python, Java, and JavaScript
The final model is the best performing model and was trained twice as long (236B tokens) as the others. This checkpoint is the default model and available on the main branch. All other checkpoints are on separate branches with according names.

## Use

## Intended use

The model was trained on GitHub code. As such it is not an instruction model and commands like "Write a function that computes the square root." do not work well.
You should phrase commands like they occur in source code such as comments (e.g. # the following function computes the sqrt ) or write a function signature and docstring and let the model complete the function body.
Feel free to share your generations in the Community tab!

## How to use

### Generation

### Fill-in-the-middle

Fill-in-the-middle uses special tokens to identify the prefix/middle/suffix part of the input and output:
Make sure to use <fim-prefix>, <fim-suffix>, <fim-middle> and not <fim_prefix>, <fim_suffix>, <fim_middle> as in StarCoder models.

### Load other checkpoints

We upload the checkpoint of each experiment to a separate branch as well as the intermediate checkpoints as commits on the branches. You can load them with the revision flag:

### Attribution & Other Requirements

The pretraining dataset of the model was filtered for permissive licenses only. Nevertheless, the model can generate source code verbatim from the dataset. The code's license might require attribution and/or other specific requirements that must be respected. We provide a search index that let's you search through the pretraining data to identify where generated code came from and apply the proper attribution to your code.

## Limitations

The model has been trained on source code in Python, Java, and JavaScript. The predominant language in source is English although other languages are also present. As such the model is capable to generate code snippets provided some context but the generated code is not guaranteed to work as intended. It can be inefficient, contain bugs or exploits.

## Training

## Model

- Architecture: GPT-2 model with multi-query attention and Fill-in-the-Middle objective
- Pretraining steps: 600K
- Pretraining tokens: 236 billion
- Precision: float16

## Hardware

- GPUs: 96 Tesla V100
- Training time: 6.2 days
- Total FLOPS: 2.1 x 10e21

## Software

- Orchestration: Megatron-LM
[LINK: Megatron-LM](https://github.com/bigcode-project/Megatron-LM)
- Neural networks: PyTorch
[LINK: PyTorch](https://github.com/pytorch/pytorch)
- FP16 if applicable: apex
[LINK: apex](https://github.com/NVIDIA/apex)

## License

The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement here .

## Citation

## Model tree for bigcode/santacoder

## Dataset used to train bigcode/santacoder

## Spaces using bigcode/santacoder 100

## Papers for bigcode/santacoder

## Evaluation results

- pass@1 on MultiPL HumanEval (Python) self-reported 0.180
- pass@10 on MultiPL HumanEval (Python) self-reported 0.290
- pass@100 on MultiPL HumanEval (Python) self-reported 0.490
- pass@1 on MultiPL MBPP (Python) self-reported 0.350
- pass@10 on MultiPL MBPP (Python) self-reported 0.580
- pass@100 on MultiPL MBPP (Python) self-reported 0.770
- pass@1 on MultiPL HumanEval (JavaScript) self-reported 0.160
- pass@10 on MultiPL HumanEval (JavaScript) self-reported 0.270
- pass@100 on MultiPL HumanEval (JavaScript) self-reported 0.470
- pass@1 on MultiPL MBPP (Javascript) self-reported 0.280
- pass@10 on MultiPL MBPP (Javascript) self-reported 0.510
- pass@100 on MultiPL MBPP (Javascript) self-reported 0.700
- pass@1 on MultiPL HumanEval (Java) self-reported 0.150
- pass@10 on MultiPL HumanEval (Java) self-reported 0.260
- pass@100 on MultiPL HumanEval (Java) self-reported 0.410
- pass@1 on MultiPL MBPP (Java) self-reported 0.280
- pass@10 on MultiPL MBPP (Java) self-reported 0.440
- pass@100 on MultiPL MBPP (Java) self-reported 0.590
- single_line on HumanEval FIM (Python) self-reported 0.440
- single_line on MultiPL HumanEval FIM (Java) self-reported 0.620

--------------------