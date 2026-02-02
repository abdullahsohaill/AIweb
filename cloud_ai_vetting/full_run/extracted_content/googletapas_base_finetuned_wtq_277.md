# `google/tapas-base-finetuned-wtq`
**URL:** https://huggingface.co/google/tapas-base-finetuned-wtq
**Page Title:** google/tapas-base-finetuned-wtq · Hugging Face
--------------------


## TAPAS base model fine-tuned on WikiTable Questions (WTQ)

This model has 2 versions which can be used. The default version corresponds to the tapas_wtq_wikisql_sqa_inter_masklm_base_reset checkpoint of the original Github repository .
This model was pre-trained on MLM and an additional step which the authors call intermediate pre-training, and then fine-tuned in a chain on SQA , WikiSQL and finally WTQ . It uses relative position embeddings (i.e. resetting the position index at every cell of the table).
[LINK: original Github repository](https://github.com/google-research/tapas)
[LINK: WikiSQL](https://github.com/salesforce/WikiSQL)
[LINK: WTQ](https://github.com/ppasupat/WikiTableQuestions)
The other (non-default) version which can be used is:
- no_reset , which corresponds to tapas_wtq_wikisql_sqa_inter_masklm_base (intermediate pre-training, absolute position embeddings).
Disclaimer: The team releasing TAPAS did not write a model card for this model so this model card has been written by
the Hugging Face team and contributors.

## Results

## Model description

TAPAS is a BERT-like transformers model pretrained on a large corpus of English data from Wikipedia in a self-supervised fashion. 
This means it was pretrained on the raw tables and associated texts only, with no humans labelling them in any way (which is why it
can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it
was pretrained with two objectives:
- Masked language modeling (MLM): taking a (flattened) table and associated context, the model randomly masks 15% of the words in 
the input, then runs the entire (partially masked) sequence through the model. The model then has to predict the masked words. 
This is different from traditional recurrent neural networks (RNNs) that usually see the words one after the other, 
or from autoregressive models like GPT which internally mask the future tokens. It allows the model to learn a bidirectional 
representation of a table and associated text.
- Intermediate pre-training: to encourage numerical reasoning on tables, the authors additionally pre-trained the model by creating 
a balanced dataset of millions of syntactically created training examples. Here, the model must predict (classify) whether a sentence 
is supported or refuted by the contents of a table. The training examples are created based on synthetic as well as counterfactual statements.
This way, the model learns an inner representation of the English language used in tables and associated texts, which can then be used 
to extract features useful for downstream tasks such as answering questions about a table, or determining whether a sentence is entailed
or refuted by the contents of a table. Fine-tuning is done by adding a cell selection head and aggregation head on top of the pre-trained model, and then jointly train these randomly initialized classification heads with the base model on SQa, WikiSQL and finally WTQ.

## Intended uses & limitations

You can use this model for answering questions related to a table.
For code examples, we refer to the documentation of TAPAS on the HuggingFace website.

## Training procedure

### Preprocessing

The texts are lowercased and tokenized using WordPiece and a vocabulary size of 30,000. The inputs of the model are
then of the form:
The authors did first convert the WTQ dataset into the format of SQA using automatic conversion scripts.

### Fine-tuning

The model was fine-tuned on 32 Cloud TPU v3 cores for 50,000 steps with maximum sequence length 512 and batch size of 512.
In this setup, fine-tuning takes around 10 hours. The optimizer used is Adam with a learning rate of 1.93581e-5, and a warmup 
ratio of 0.128960. An inductive bias is added such that the model only selects cells of the same column. This is reflected by the select_one_column parameter of TapasConfig . See the paper for more details (tables 11 and
12).

### BibTeX entry and citation info

## Model tree for google/tapas-base-finetuned-wtq

## Dataset used to train google/tapas-base-finetuned-wtq

## Spaces using google/tapas-base-finetuned-wtq 100

## Papers for google/tapas-base-finetuned-wtq

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
google/tapas-base-finetuned-wtq is supported by the following Inference Providers:

--------------------