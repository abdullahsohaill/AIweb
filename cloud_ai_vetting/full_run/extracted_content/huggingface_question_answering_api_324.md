# Huggingface Question Answering API
**URL:** https://huggingface.co/deepset/tinyroberta-squad2
**Page Title:** deepset/tinyroberta-squad2 · Hugging Face
--------------------


## tinyroberta for Extractive QA

This is the distilled version of the deepset/roberta-base-squad2 model. This model has a comparable prediction quality and runs at twice the speed of the base model.

## Overview

Language model: tinyroberta-squad2 Language: English Downstream-task: Extractive QA Training data: SQuAD 2.0 Eval data: SQuAD 2.0 Code: See an example extractive QA pipeline built with Haystack Infrastructure : 4x Tesla v100

## Hyperparameters

## Distillation

This model was distilled using the TinyBERT approach described in this paper and implemented in haystack .
Firstly, we have performed intermediate layer distillation with roberta-base as the teacher which resulted in deepset/tinyroberta-6l-768d .
Secondly, we have performed task-specific distillation with deepset/roberta-base-squad2 as the teacher for further intermediate layer distillation on an augmented version of SQuADv2 and then with deepset/roberta-large-squad2 as the teacher for prediction layer distillation.
[LINK: haystack](https://github.com/deepset-ai/haystack)

## Usage

### In Haystack

Haystack is an AI orchestration framework to build customizable, production-ready LLM applications. You can use this model in Haystack to do extractive question answering on documents. 
To load and run the model with Haystack :
[LINK: Haystack](https://github.com/deepset-ai/haystack/)
For a complete example with an extractive question answering pipeline that scales over many documents, check out the corresponding Haystack tutorial .

### In Transformers

## Performance

Evaluated on the SQuAD 2.0 dev set with the official eval script .

## Authors

Branden Chan: branden.chan@deepset.ai Timo Möller: timo.moeller@deepset.ai Malte Pietsch: malte.pietsch@deepset.ai Tanay Soni: tanay.soni@deepset.ai Michel Bartels: michel.bartels@deepset.ai

## About us

deepset is the company behind the production-ready open-source AI framework Haystack .
Some of our other work:
- Distilled roberta-base-squad2 (aka "tinyroberta-squad2")
- German BERT , GermanQuAD and GermanDPR , German embedding model
- deepset Cloud , deepset Studio

## Get in touch and join the Haystack community

For more info on Haystack, visit our GitHub repo and Documentation .
[LINK: GitHub](https://github.com/deepset-ai/haystack)
[LINK: Documentation](https://docs.haystack.deepset.ai)
We also have a Discord community open to everyone!
Twitter | LinkedIn | Discord | GitHub Discussions | Website | YouTube
[LINK: GitHub Discussions](https://github.com/deepset-ai/haystack/discussions)
By the way: we're hiring!

## Model tree for deepset/tinyroberta-squad2

## Dataset used to train deepset/tinyroberta-squad2

## Spaces using deepset/tinyroberta-squad2 47

## Paper for deepset/tinyroberta-squad2

## Evaluation results

- Exact Match on squad_v2 validation set verified 78.863
- F1 on squad_v2 validation set verified 82.035
- Exact Match on squad validation set self-reported 83.860
- F1 on squad validation set self-reported 90.752
- Exact Match on adversarial_qa validation set self-reported 25.967
- F1 on adversarial_qa validation set self-reported 37.006
- Exact Match on squad_adversarial validation set self-reported 76.329
- F1 on squad_adversarial validation set self-reported 83.292
- Exact Match on squadshifts amazon test set self-reported 63.915
- F1 on squadshifts amazon test set self-reported 78.395
- Exact Match on squadshifts new_wiki test set self-reported 80.297
- F1 on squadshifts new_wiki test set self-reported 89.808
- Exact Match on squadshifts nyt test set self-reported 80.149
- F1 on squadshifts nyt test set self-reported 88.321
- Exact Match on squadshifts reddit test set self-reported 66.959
- F1 on squadshifts reddit test set self-reported 79.300

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
deepset/tinyroberta-squad2 is supported by the following Inference Providers:

--------------------