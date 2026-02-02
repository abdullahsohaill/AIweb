# Replit Code V1.5 3B
**URL:** https://huggingface.co/replit/replit-code-v1_5-3b
**Page Title:** replit/replit-code-v1_5-3b · Hugging Face
--------------------


## Replit Code V-1.5 3B

Developed by: Replit, Inc.

## Model Description

Replit Code v1.5 is a 3.3B parameter Causal Language Model focused on Code Completion .
The model is trained in bfloat16 on 1T tokens of code (~200B tokens  over 5 epochs, including linear cooldown) for 30 programming languages from a subset of permissively licensed code from Bigcode's Stack Dedup dataset , a filtered natural language sample from Markdown and reStructuredText subsets from the same Stack Dedup dataset, and a dev-oriented sample from RedPajama's StackExchange dataset sourced from the Stack Exchange Data Dump by Stack Exchange Inc .
[LINK: RedPajama's StackExchange dataset](https://github.com/togethercomputer/RedPajama-Data)
The 30 programming languages are:
The context size of the model is 4096 tokens. We use the GPTNeoX tokenizer with a custom trained and optimized vocabulary of 32768 tokens. This custom vocabulary led to single-digit % points on compression while maintaining or improving coverage on our training corpus.
The model has been trained on the MosaicML platform on 128  H100-80GB GPUs using their LLM Foundry and Composer training library built on top of PyTorch.
[LINK: LLM Foundry](https://github.com/mosaicml/llm-foundry)
[LINK: Composer](https://github.com/mosaicml/composer)

## Dependencies

You will need to install the latest versions of the following dependencies:

## How to Use

### Generation

You can generate code using the transformers library as follows:
Experiment with different decoding methods and parameters to get the best results for your use case.

### Using Triton Implementation of Flash Attention

Experiment with different decoding methods and parameters to get the best results for your use case. We recommend experimenting with temperature and reptition_penalty for optimal performance on your use case!

## Intended Use

Replit intends this model be used by anyone as a foundational model for application-specific fine-tuning without strict limitations on commercial use.
The model is trained specifically for code completion tasks.

## Limitations

The pre-training dataset may have contained offensive or inappropriate content even after applying data cleansing and toxicity and profanity filters, and such content may be reflected in model generated text. We recommend that users exercise reasonable caution when using in production systems. Do not use for any applications that may cause harm or distress to individuals or groups.

## Model tree for replit/replit-code-v1_5-3b

## Datasets used to train replit/replit-code-v1_5-3b

## Spaces using replit/replit-code-v1_5-3b 4


--------------------