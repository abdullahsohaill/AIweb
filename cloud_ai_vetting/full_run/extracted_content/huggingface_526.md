# Huggingface
**URL:** https://huggingface.co/datasets/intfloat/query2doc_msmarco
**Page Title:** intfloat/query2doc_msmarco · Datasets at Hugging Face
--------------------


### Dataset Summary

This dataset contains GPT-3.5 ( text-davinci-003 ) generations from MS-MARCO queries.
Query2doc: Query Expansion with Large Language Models Liang Wang, Nan Yang and Furu Wei

### Data Instances

An example looks as follows.

### Data Fields

- query_id : a string feature.
- query : a string feature.
- pseudo_doc : a string feature.

### Data Splits

### How to use this dataset

### Reproducing our results

We provide a python script repro_bm25.py to reproduce our results with BM25 retrieval.
First install some python dependency packages:
Then download and run the python code:
This script utilizes the pre-built Lucene index from Pyserini and might yield slightly different results compared to the paper.
[LINK: Pyserini](https://github.com/castorini/pyserini/blob/pyserini-0.15.0/docs/prebuilt-indexes.md)

### Citation Information

## Paper for intfloat/query2doc_msmarco


--------------------