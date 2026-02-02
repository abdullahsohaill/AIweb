# Token Classification
**URL:** https://huggingface.co/tasks/token-classification
**Page Title:** What is Token Classification? - Hugging Face
--------------------


## Token Classification

Token classification is a natural language understanding task in which a label is assigned to some tokens in a text. Some popular token classification subtasks are Named Entity Recognition (NER) and Part-of-Speech (PoS) tagging. NER models could be trained to identify specific entities in a text, such as dates, individuals and places; and PoS tagging would identify, for example, which words in a text are verbs, nouns, and punctuation marks.
My name is Omar and I live in Zürich.

## About Token Classification

## Use Cases

### Information Extraction from Invoices

You can extract entities of interest from invoices automatically using Named Entity Recognition (NER) models. Invoices can be read with Optical Character Recognition models and the output can be used to do inference with NER models. In this way, important information such as date, company name, and other named entities can be extracted.

## Task Variants

### Named Entity Recognition (NER)

NER is the task of recognizing named entities in a text. These entities can be the names of people, locations, or organizations. The task is formulated as labeling each token with a class for each named entity and a class named "0" for tokens that do not contain any entities. The input for this task is text and the output is the annotated text with named entities.
You can use the 🤗 Transformers library ner pipeline to infer with NER models.

### Part-of-Speech (PoS) Tagging

In PoS tagging, the model recognizes parts of speech, such as nouns, pronouns, adjectives, or verbs, in a given text. The task is formulated as labeling each word with a part of the speech.
You can use the 🤗 Transformers library token-classification pipeline with a POS tagging model of your choice. The model will return a json with PoS tags for each token.
This is not limited to transformers! You can also use other libraries such as Stanza, spaCy, and Flair to do inference! Here is an example using a canonical spaCy model.

## Useful Resources

Would you like to learn more about token classification? Great! Here you can find some curated resources that you may find helpful!
- Course Chapter on Token Classification
- Blog post: Welcome spaCy to the Hugging Face Hub

### Notebooks

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/notebooks/blob/master/examples/token_classification.ipynb)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/notebooks/blob/master/examples/token_classification-tf.ipynb)

### Scripts for training

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/transformers/tree/main/examples/pytorch/token-classification)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/transformers/tree/main/examples/tensorflow)
- Flax
[LINK: Flax](https://github.com/huggingface/transformers/tree/main/examples/flax/token-classification)

### Documentation

- Token classification task guide
[LINK: Token classification task guide](https://huggingface.co/docs/transformers/tasks/token_classification)

## Compatible libraries

Note A robust performance model to identify people, locations, organizations and names of miscellaneous entities.
Note A strong model to identify people, locations, organizations and names in multiple languages.
Note A token classification model specialized on medical entity recognition.
Note Flair models are typically the state of the art in named entity recognition tasks.
Note A widely used dataset useful to benchmark named entity recognition models.
Note A multilingual dataset of Wikipedia articles annotated for named entity recognition in over 150 different languages.
Note An application that can recognizes entities, extracts noun chunks and recognizes various linguistic features of each token.

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
FacebookAI/xlm-roberta-large-finetuned-conll03-english is supported by the following Inference Providers:

--------------------