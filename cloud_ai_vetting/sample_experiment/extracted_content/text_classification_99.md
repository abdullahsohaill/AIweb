# Text Classification
**URL:** https://huggingface.co/tasks/text-classification
**Page Title:** What is Text Classification? - Hugging Face
--------------------


## Text Classification

Text Classification is the task of assigning a label or class to a given text. Some use cases are sentiment analysis, natural language inference, and assessing grammatical correctness.
I love Hugging Face!

## About Text Classification

## Use Cases

### Sentiment Analysis on Customer Reviews

You can track the sentiments of your customers from the product reviews using sentiment analysis models. This can help understand churn and retention by grouping reviews by sentiment, to later analyze the text and make strategic decisions based on this knowledge.

## Task Variants

### Natural Language Inference (NLI)

In NLI the model determines the relationship between two given texts. Concretely, the model takes a premise and a hypothesis and returns a class that can either be:
- entailment , which means the hypothesis is true.
- contraction , which means the hypothesis is false.
- neutral , which means there's no relation between the hypothesis and the premise.
The benchmark dataset for this task is GLUE (General Language Understanding Evaluation). NLI models have different variants, such as Multi-Genre NLI, Question NLI and Winograd NLI.

### Multi-Genre NLI (MNLI)

MNLI is used for general NLI. Here are som examples:
You can use the 🤗 Transformers library text-classification pipeline to infer with NLI models.

### Question Natural Language Inference (QNLI)

QNLI is the task of determining if the answer to a certain question can be found in a given document. If the answer can be found the label is “entailment”. If the answer cannot be found the label is “not entailment".
You can use the 🤗 Transformers library text-classification pipeline to infer with QNLI models. The model returns the label and the confidence.

### Sentiment Analysis

In Sentiment Analysis, the classes can be polarities like positive, negative, neutral, or sentiments such as happiness or anger.
You can use the 🤗 Transformers library with the sentiment-analysis pipeline to infer with Sentiment Analysis models. The model returns the label with the score.

### Quora Question Pairs

Quora Question Pairs models assess whether two provided questions are paraphrases of each other. The model takes two questions and returns a binary value, with 0 being mapped to “not paraphrase” and 1 to “paraphrase". The benchmark dataset is Quora Question Pairs inside the GLUE benchmark . The dataset consists of question pairs and their labels.
You can use the 🤗 Transformers library text-classification pipeline to infer with QQPI models.
You can use huggingface.js to infer text classification models on Hugging Face Hub.
[LINK: huggingface.js](https://github.com/huggingface/huggingface.js)

### Grammatical Correctness

Linguistic Acceptability is the task of assessing the grammatical acceptability of a sentence. The classes in this task are “acceptable” and “unacceptable”. The benchmark dataset used for this task is Corpus of Linguistic Acceptability (CoLA) . The dataset consists of texts and their labels.

## Useful Resources

Would you like to learn more about the topic? Awesome! Here you can find some curated resources that you may find helpful!
- SetFitABSA: Few-Shot Aspect Based Sentiment Analysis using SetFit
- Course Chapter on Fine-tuning a Text Classification Model
- Getting Started with Sentiment Analysis using Python
- Sentiment Analysis on Encrypted Data with Homomorphic Encryption
- Leveraging Hugging Face for complex text classification use cases

### Notebooks

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/notebooks/blob/master/examples/text_classification.ipynb)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/notebooks/blob/master/examples/text_classification-tf.ipynb)
- Flax
[LINK: Flax](https://github.com/huggingface/notebooks/blob/master/examples/text_classification_flax.ipynb)

### Scripts for training

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/transformers/tree/main/examples/pytorch/text-classification)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/transformers/tree/main/examples/tensorflow/text-classification)
- Flax
[LINK: Flax](https://github.com/huggingface/transformers/tree/main/examples/flax/text-classification)

### Documentation

- Text classification task guide
[LINK: Text classification task guide](https://huggingface.co/docs/transformers/tasks/sequence_classification)

## Compatible libraries

Note A robust model trained for sentiment analysis.
Note A sentiment analysis model specialized in financial sentiment.
Note A sentiment analysis model specialized in analyzing tweets.
Note A model that can classify languages.
Note A model that can classify text generation attacks.
Note A widely used dataset used to benchmark multiple variants of text classification.
Note A text classification dataset used to benchmark natural language inference models
Note An application that can classify financial sentiment.
Note A dashboard that contains various text classification tasks.
Note An application that analyzes user reviews in healthcare.

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
distilbert/distilbert-base-uncased-finetuned-sst-2-english is supported by the following Inference Providers:

--------------------