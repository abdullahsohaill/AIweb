# `deepset/roberta-base-squad2`
**URL:** https://huggingface.co/deepset/roberta-base-squad2
**Page Title:** deepset/roberta-base-squad2 · Hugging Face
--------------------


## roberta-base for Extractive QA

This is the roberta-base model, fine-tuned using the SQuAD2.0 dataset. It's been trained on question-answer pairs, including unanswerable questions, for the task of Extractive Question Answering. 
We have also released a distilled version of this model called deepset/tinyroberta-squad2 . It has a comparable prediction quality and runs at twice the speed of deepset/roberta-base-squad2 .

## Overview

Language model: roberta-base Language: English Downstream-task: Extractive QA Training data: SQuAD 2.0 Eval data: SQuAD 2.0 Code: See an example extractive QA pipeline built with Haystack Infrastructure : 4x Tesla v100

## Hyperparameters

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

Branden Chan: branden.chan@deepset.ai Timo Möller: timo.moeller@deepset.ai Malte Pietsch: malte.pietsch@deepset.ai Tanay Soni: tanay.soni@deepset.ai

## About us

deepset is the company behind the production-ready open-source AI framework Haystack .
Some of our other work:
- Distilled roberta-base-squad2 (aka "tinyroberta-squad2")
- German BERT , GermanQuAD and GermanDPR , German embedding model
- deepset Cloud
- deepset Studio

## Get in touch and join the Haystack community

For more info on Haystack, visit our GitHub repo and Documentation .
[LINK: GitHub](https://github.com/deepset-ai/haystack)
[LINK: Documentation](https://docs.haystack.deepset.ai)
We also have a Discord community open to everyone!
Twitter | LinkedIn | Discord | GitHub Discussions | Website | YouTube
[LINK: GitHub Discussions](https://github.com/deepset-ai/haystack/discussions)
By the way: we're hiring!

## Model tree for deepset/roberta-base-squad2

Base model

## Dataset used to train deepset/roberta-base-squad2

## Spaces using deepset/roberta-base-squad2 100

## Evaluation results

- Exact Match on squad_v2 validation set verified 79.931
- F1 on squad_v2 validation set verified 82.950
- total on squad_v2 validation set verified 11869.000
- Exact Match on squad validation set self-reported 85.289
- F1 on squad validation set self-reported 91.841
- Exact Match on adversarial_qa validation set self-reported 29.500
- F1 on adversarial_qa validation set self-reported 40.367
- Exact Match on squad_adversarial validation set self-reported 78.567
- F1 on squad_adversarial validation set self-reported 84.469
- Exact Match on squadshifts amazon test set self-reported 69.924
- F1 on squadshifts amazon test set self-reported 83.284
- Exact Match on squadshifts new_wiki test set self-reported 81.204
- F1 on squadshifts new_wiki test set self-reported 90.595
- Exact Match on squadshifts nyt test set self-reported 82.931
- F1 on squadshifts nyt test set self-reported 90.756
- Exact Match on squadshifts reddit test set self-reported 71.550
- F1 on squadshifts reddit test set self-reported 82.939

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
deepset/roberta-base-squad2 is supported by the following Inference Providers:

--------------------