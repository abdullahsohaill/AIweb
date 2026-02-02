# Sentence Similarity
**URL:** https://huggingface.co/tasks/sentence-similarity
**Page Title:** What is Sentence Similarity? - Hugging Face
--------------------


## Sentence Similarity

Sentence Similarity is the task of determining how similar two texts are. Sentence similarity models convert input texts into vectors (embeddings) that capture semantic information and calculate how close (similar) they are between them. This task is particularly useful for information retrieval and clustering/grouping.
Machine learning is so easy.
Deep learning is so straightforward.
This is so difficult, like rocket science.
I can't believe how much I struggled with this.

## About Sentence Similarity

## Use Cases 🔍

### Information Retrieval

You can extract information from documents using Sentence Similarity models. The first step is to rank documents using Passage Ranking models. You can then get to the top ranked document and search it with Sentence Similarity models by selecting the sentence that has the most similarity to the input query.

## The Sentence Transformers library

The Sentence Transformers library is very powerful for calculating embeddings of sentences, paragraphs, and entire documents. An embedding is just a vector representation of a text and is useful for finding how similar two texts are.
You can find and use thousands of Sentence Transformers models from the Hub by directly using the library, playing with the widgets in the browser or using Inference Endpoints.

## Task Variants

### Passage Ranking

Passage Ranking is the task of ranking documents based on their relevance to a given query. The task is evaluated on Mean Reciprocal Rank. These models take one query and multiple documents and return ranked documents according to the relevancy to the query. 📄
You can infer with Passage Ranking models using Inference Endpoints . The Passage Ranking model inputs are a query for which we look for relevancy in the documents and the documents we want to search. The model will return scores according to the relevancy of these documents for the query.

### Semantic Textual Similarity

Semantic Textual Similarity is the task of evaluating how similar two texts are in terms of meaning. These models take a source sentence and a list of sentences in which we will look for similarities and will return a list of similarity scores. The benchmark dataset is the Semantic Textual Similarity Benchmark . The task is evaluated on Pearson’s Rank Correlation.
You can also infer with the models in the Hub using Sentence Transformer models.

## Useful Resources

Would you like to learn more about Sentence Transformers and Sentence Similarity? Awesome! Here you can find some curated resources that you may find helpful!
- Sentence Transformers Documentation
- Sentence Transformers in the Hub
- Building a Playlist Generator with Sentence Transformers
- Getting Started With Embeddings

## Compatible libraries

Note This model works well for sentences and paragraphs and can be used for clustering/grouping and semantic searches.
Note A multilingual robust sentence similarity model.
Note A robust sentence similarity model.
Note Bing queries with relevant passages from various web sources.
Note An application that leverages sentence similarity to answer questions from YouTube videos.
Note An application that retrieves relevant PubMed abstracts for a given online article which can be used as further references.
Note An application that leverages sentence similarity to summarize text.

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
sentence-transformers/all-MiniLM-L6-v2 is supported by the following Inference Providers:

--------------------