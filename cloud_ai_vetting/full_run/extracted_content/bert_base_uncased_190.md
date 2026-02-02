# bert-base-uncased
**URL:** https://huggingface.co/bert-base-uncased
**Page Title:** google-bert/bert-base-uncased · Hugging Face
--------------------


## BERT base model (uncased)

Pretrained model on English language using a masked language modeling (MLM) objective. It was introduced in this paper and first released in this repository . This model is uncased: it does not make a difference
between english and English.
[LINK: this repository](https://github.com/google-research/bert)
Disclaimer: The team releasing BERT did not write a model card for this model so this model card has been written by
the Hugging Face team.

## Model description

BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. This means it
was pretrained on the raw texts only, with no humans labeling them in any way (which is why it can use lots of
publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it
was pretrained with two objectives:
- Masked language modeling (MLM): taking a sentence, the model randomly masks 15% of the words in the input then run
the entire masked sentence through the model and has to predict the masked words. This is different from traditional
recurrent neural networks (RNNs) that usually see the words one after the other, or from autoregressive models like
GPT which internally masks the future tokens. It allows the model to learn a bidirectional representation of the
sentence.
- Next sentence prediction (NSP): the models concatenates two masked sentences as inputs during pretraining. Sometimes
they correspond to sentences that were next to each other in the original text, sometimes not. The model then has to
predict if the two sentences were following each other or not.
This way, the model learns an inner representation of the English language that can then be used to extract features
useful for downstream tasks: if you have a dataset of labeled sentences, for instance, you can train a standard
classifier using the features produced by the BERT model as inputs.

## Model variations

BERT has originally been released in base and large variations, for cased and uncased input text. The uncased models also strips out an accent markers. Chinese and multilingual uncased and cased versions followed shortly after. Modified preprocessing with whole word masking has replaced subpiece masking in a following work, with the release of two models. Other 24 smaller models are released afterward.
The detailed release history can be found on the google-research/bert readme on github.
[LINK: google-research/bert readme](https://github.com/google-research/bert/blob/master/README.md)

## Intended uses & limitations

You can use the raw model for either masked language modeling or next sentence prediction, but it's mostly intended to
be fine-tuned on a downstream task. See the model hub to look for
fine-tuned versions of a task that interests you.
Note that this model is primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked)
to make decisions, such as sequence classification, token classification or question answering. For tasks such as text
generation you should look at model like GPT2.

### How to use

You can use this model directly with a pipeline for masked language modeling:
Here is how to use this model to get the features of a given text in PyTorch:
and in TensorFlow:

### Limitations and bias

Even if the training data used for this model could be characterized as fairly neutral, this model can have biased
predictions:
This bias will also affect all fine-tuned versions of this model.

## Training data

The BERT model was pretrained on BookCorpus , a dataset consisting of 11,038
unpublished books and English Wikipedia (excluding lists, tables and
headers).

## Training procedure

### Preprocessing

The texts are lowercased and tokenized using WordPiece and a vocabulary size of 30,000. The inputs of the model are
then of the form:
With probability 0.5, sentence A and sentence B correspond to two consecutive sentences in the original corpus, and in
the other cases, it's another random sentence in the corpus. Note that what is considered a sentence here is a
consecutive span of text usually longer than a single sentence. The only constrain is that the result with the two
"sentences" has a combined length of less than 512 tokens.
The details of the masking procedure for each sentence are the following:
- 15% of the tokens are masked.
- In 80% of the cases, the masked tokens are replaced by [MASK] .
- In 10% of the cases, the masked tokens are replaced by a random token (different) from the one they replace.
- In the 10% remaining cases, the masked tokens are left as is.

### Pretraining

The model was trained on 4 cloud TPUs in Pod configuration (16 TPU chips total) for one million steps with a batch size
of 256. The sequence length was limited to 128 tokens for 90% of the steps and 512 for the remaining 10%. The optimizer
used is Adam with a learning rate of 1e-4, β 1 = 0.9 \beta_{1} = 0.9 β 1 ​ = 0.9 and β 2 = 0.999 \beta_{2} = 0.999 β 2 ​ = 0.999 , a weight decay of 0.01,
learning rate warmup for 10,000 steps and linear decay of the learning rate after.

## Evaluation results

When fine-tuned on downstream tasks, this model achieves the following results:
Glue test results:

### BibTeX entry and citation info

## Model tree for google-bert/bert-base-uncased

## Datasets used to train google-bert/bert-base-uncased

## Spaces using google-bert/bert-base-uncased 100

## Paper for google-bert/bert-base-uncased

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
google-bert/bert-base-uncased is supported by the following Inference Providers:

--------------------