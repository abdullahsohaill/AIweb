# Zero-Shot Classification
**URL:** https://huggingface.co/tasks/zero-shot-classification
**Page Title:** What is Zero-Shot Classification? - Hugging Face
--------------------


## Zero-Shot Classification

Zero-shot text classification is a task in natural language processing where a model is trained on a set of labeled examples but is then able to classify new examples from previously unseen classes.
Dune is the best movie ever.
CINEMA, ART, MUSIC

## About Zero-Shot Classification

## About the Task

Zero Shot Classification is the task of predicting a class that wasn't seen by the model during training. This method, which leverages a pre-trained language model, can be thought of as an instance of transfer learning which generally refers to using a model trained for one task in a different application than what it was originally trained for. This is particularly useful for situations where the amount of labeled data is small.
In zero shot classification, we provide the model with a prompt and a sequence of text that describes what we want our model to do, in natural language. Zero-shot classification excludes any examples of the desired task being completed. This differs from single or few-shot classification, as these tasks include a single or a few examples of the selected task.
Zero, single and few-shot classification seem to be an emergent feature of large language models. This feature seems to come about around model sizes of +100M parameters. The effectiveness of a model at a zero, single or few-shot task seems to scale with model size, meaning that larger models (models with more trainable parameters or layers) generally do better at this task.
Here is an example of a zero-shot prompt for classifying the sentiment of a sequence of text:
One great example of this task with a nice off-the-shelf model is available at the widget of this page, where the user can input a sequence of text and candidate labels to the model. This is a word level example of zero shot classification, more elaborate and lengthy generations are available with larger models. Testing these models out and getting a feel for prompt engineering is the best way to learn how to use them.

## Inference

You can use the 🤗 Transformers library zero-shot-classification pipeline to infer with zero shot text classification models.

## Useful Resources

- Zero Shot Learning
[LINK: Zero Shot Learning](https://joeddav.github.io/blog/2020/05/29/ZSL.html)
- Hugging Face on Transfer Learning

## Compatible libraries

Note Powerful zero-shot text classification model.
Note Cutting-edge zero-shot multilingual text classification model.
Note Zero-shot text classification model that can be used for topic and sentiment classification.
Note A widely used dataset used to benchmark multiple variants of text classification.
Note The Multi-Genre Natural Language Inference (MultiNLI) corpus is a crowd-sourced collection of 433k sentence pairs annotated with textual entailment information.
Note FEVER is a publicly available dataset for fact extraction and verification against textual sources.
No example Space is defined for this task.
Note Contribute by proposing a Space for this task !
No example metric is defined for this task.
Note Contribute by proposing a metric for this task !

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
facebook/bart-large-mnli is supported by the following Inference Providers:

--------------------