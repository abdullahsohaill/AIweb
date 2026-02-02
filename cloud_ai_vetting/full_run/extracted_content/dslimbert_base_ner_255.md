# `dslim/bert-base-NER`
**URL:** https://huggingface.co/dslim/bert-base-NER
**Page Title:** dslim/bert-base-NER · Hugging Face
--------------------


## bert-base-NER

If my open source models have been useful to you, please consider supporting me in building small, useful AI models for everyone (and help me afford med school / help out my parents financially). Thanks!

## Model description

bert-base-NER is a fine-tuned BERT model that is ready to use for Named Entity Recognition and achieves state-of-the-art performance for the NER task. It has been trained to recognize four types of entities: location (LOC), organizations (ORG), person (PER) and Miscellaneous (MISC).
Specifically, this model is a bert-base-cased model that was fine-tuned on the English version of the standard CoNLL-2003 Named Entity Recognition dataset.
If you'd like to use a larger BERT-large model fine-tuned on the same dataset, a bert-large-NER version is also available.

### Available NER models

## Intended uses & limitations

You can use this model with Transformers pipeline for NER.
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. Furthermore, the model occassionally tags subword tokens as entities and post-processing of results may be necessary to handle those cases.

## Training data

This model was fine-tuned on English version of the standard CoNLL-2003 Named Entity Recognition dataset.
The training dataset distinguishes between the beginning and continuation of an entity so that if there are back-to-back entities of the same type, the model can output where the second entity begins. As in the dataset, each token will be classified as one of the following classes:

### CoNLL-2003 English Dataset Statistics

This dataset was derived from the Reuters corpus which consists of Reuters news stories. You can read more about how this dataset was created in the CoNLL-2003 paper.

## Training procedure

This model was trained on a single NVIDIA V100 GPU with recommended hyperparameters from the original BERT paper which trained & evaluated the model on CoNLL-2003 NER task.

## Eval results

The test metrics are a little lower than the official Google BERT results which encoded document context & experimented with CRF. More on replicating the original results here .
[LINK: here](https://github.com/google-research/bert/issues/223)

### BibTeX entry and citation info

## Model tree for dslim/bert-base-NER

## Dataset used to train dslim/bert-base-NER

## Spaces using dslim/bert-base-NER 100

## Paper for dslim/bert-base-NER

## Evaluation results

- Accuracy on conll2003 test set self-reported 0.912
- Precision on conll2003 test set self-reported 0.921
- Recall on conll2003 test set self-reported 0.931
- F1 on conll2003 test set self-reported 0.926
- loss on conll2003 test set self-reported 0.483

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
dslim/bert-base-NER is supported by the following Inference Providers:

--------------------