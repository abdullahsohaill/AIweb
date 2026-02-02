# `sentence-transformers/all-MiniLM-L6-v2`
**URL:** https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
**Page Title:** sentence-transformers/all-MiniLM-L6-v2 · Hugging Face
--------------------


## all-MiniLM-L6-v2

This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.

## Usage (Sentence-Transformers)

Using this model becomes easy when you have sentence-transformers installed:
Then you can use the model like this:

## Usage (HuggingFace Transformers)

Without sentence-transformers , you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

## Background

The project aims to train sentence embedding models on very large sentence level datasets using a self-supervised 
contrastive learning objective. We used the pretrained nreimers/MiniLM-L6-H384-uncased model and fine-tuned in on a 
1B sentence pairs dataset. We use a contrastive learning objective: given a sentence from the pair, the model should predict which out of a set of randomly sampled other sentences, was actually paired with it in our dataset.
We developed this model during the Community week using JAX/Flax for NLP & CV , 
organized by Hugging Face. We developed this model as part of the project: Train the Best Sentence Embedding Model Ever with 1B Training Pairs . We benefited from efficient hardware infrastructure to run the project: 7 TPUs v3-8, as well as intervention from Googles Flax, JAX, and Cloud team member about efficient deep learning frameworks.

## Intended uses

Our model is intended to be used as a sentence and short paragraph encoder. Given an input text, it outputs a vector which captures 
the semantic information. The sentence vector may be used for information retrieval, clustering or sentence similarity tasks.
By default, input text longer than 256 word pieces is truncated.

## Training procedure

### Pre-training

We use the pretrained nreimers/MiniLM-L6-H384-uncased model. Please refer to the model card for more detailed information about the pre-training procedure.

### Fine-tuning

We fine-tune the model using a contrastive objective. Formally, we compute the cosine similarity from each possible sentence pairs from the batch.
We then apply the cross entropy loss by comparing with true pairs.
We trained our model on a TPU v3-8. We train the model during 100k steps using a batch size of 1024 (128 per TPU core).
We use a learning rate warm up of 500. The sequence length was limited to 128 tokens. We used the AdamW optimizer with
a 2e-5 learning rate. The full training script is accessible in this current repository: train_script.py .
We use the concatenation from multiple datasets to fine-tune our model. The total number of sentence pairs is above 1 billion sentences.
We sampled each dataset given a weighted probability which configuration is detailed in the data_config.json file.
[LINK: Reddit comments (2015-2018)](https://github.com/PolyAI-LDN/conversational-datasets/tree/master/reddit)
[LINK: S2ORC](https://github.com/allenai/s2orc)
[LINK: WikiAnswers](https://github.com/afader/oqa#wikianswers-corpus)
[LINK: PAQ](https://github.com/facebookresearch/PAQ)
[LINK: S2ORC](https://github.com/allenai/s2orc)
[LINK: S2ORC](https://github.com/allenai/s2orc)
[LINK: MS MARCO](https://microsoft.github.io/msmarco/)
[LINK: GOOAQ: Open Question Answering with Diverse Answer Types](https://github.com/allenai/gooaq)
[LINK: SPECTER](https://github.com/allenai/specter)
[LINK: Sentence Compression](https://github.com/google-research-datasets/sentence-compression)
[LINK: Wikihow](https://github.com/pvl/wikihow_pairs_dataset)
[LINK: Altlex](https://github.com/chridey/altlex/)
[LINK: SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/)

## Model tree for sentence-transformers/all-MiniLM-L6-v2

## Datasets used to train sentence-transformers/all-MiniLM-L6-v2

## Spaces using sentence-transformers/all-MiniLM-L6-v2 100

## Papers for sentence-transformers/all-MiniLM-L6-v2

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
sentence-transformers/all-MiniLM-L6-v2 is supported by the following Inference Providers:

--------------------