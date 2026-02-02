# Starcoder2-15b
**URL:** https://huggingface.co/bigcode/starcoder2-15b
**Page Title:** bigcode/starcoder2-15b · Hugging Face
--------------------


## StarCoder2

## Table of Contents

- Model Summary
- Use
- Limitations
- Training
- License
- Citation

## Model Summary

StarCoder2-15B model is a 15B parameter model trained on 600+ programming languages from The Stack v2 , with opt-out requests excluded. The model uses Grouped Query Attention , a context window of 16,384 tokens with a sliding window attention of 4,096 tokens ,  and was trained using the Fill-in-the-Middle objective on 4+ trillion tokens. The model was trained with NVIDIA NeMo™ Framework using the NVIDIA Eos Supercomputer built with NVIDIA DGX H100 systems.
- Project Website: bigcode-project.org
- Paper: Link
- Point of Contact: contact@bigcode-project.org
- Languages: 600+ Programming languages

## Use

### Intended use

The model was trained on GitHub code as well as additional selected data sources such as Arxiv and Wikipedia. As such it is not an instruction model and commands like "Write a function that computes the square root." do not work well.

### Generation

Here are some examples to get started with the model. You can find a script for fine-tuning in StarCoder2's GitHub repository .
[LINK: GitHub repository](https://github.com/bigcode-project/starcoder2)
First, make sure to install transformers from source:
- Using full precision
- Using torch.bfloat16
- Using 8-bit precision (int8)

### Attribution & Other Requirements

The pretraining dataset of the model was filtered for permissive licenses and code with no license only. Nevertheless, the model can generate source code verbatim from the dataset. The code's license might require attribution and/or other specific requirements that must be respected. We provide a search index that let's you search through the pretraining data to identify where generated code came from and apply the proper attribution to your code.

## Limitations

The model has been trained on source code from 600+ programming languages. The predominant language in source is English although other languages are also present. As such the model is capable to generate code snippets provided some context but the generated code is not guaranteed to work as intended. It can be inefficient, contain bugs or exploits. See the paper for an in-depth discussion of the model limitations.

## Training

## Model

- Architecture: Transformer decoder with grouped-query and sliding window attention and Fill-in-the-Middle objective
- Pretraining steps: 1 million
- Pretraining tokens: 4+ trillion
- Precision: bfloat16

## Hardware

- GPUs: 1024 x H100

## Software

- Framework: NeMo Framework
- Neural networks: PyTorch
[LINK: PyTorch](https://github.com/pytorch/pytorch)

## License

The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement here .

## Citation

## Model tree for bigcode/starcoder2-15b

## Dataset used to train bigcode/starcoder2-15b

## Spaces using bigcode/starcoder2-15b 87

## Collection including bigcode/starcoder2-15b

## Papers for bigcode/starcoder2-15b

## Evaluation results

- pass@1 on CruxEval-I self-reported 48.100
- pass@1 on DS-1000 self-reported 33.800
- accuracy on GSM8K (PAL) self-reported 65.100
- pass@1 on HumanEval+ self-reported 37.800
- pass@1 on HumanEval self-reported 46.300
- edit-smiliarity on RepoBench-v1.1 self-reported 74.080

--------------------