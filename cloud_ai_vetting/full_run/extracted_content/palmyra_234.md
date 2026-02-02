# Palmyra
**URL:** https://huggingface.co/Writer/palmyra-base
**Page Title:** Writer/palmyra-base · Hugging Face
--------------------


## DEPRECATED MODEL NOTICE

Please note that this model is no longer maintained or supported by our team. We strongly advise against using it in production or for any critical applications.
Instead, we recommend using our latest and greatest models, which can be found at:
https://huggingface.co/collections/Writer/palmyra-writer-license-66476fa8156169f8720a2c89
==========================

## Palmyra Base 5B

| | |

## Model Description

Palmyra Base was primarily pre-trained with English text. Note that there is still a trace amount of non-English data present within the training corpus that was accessed through CommonCrawl. A causal language modeling (CLM) objective was utilized during the process of the model's pretraining. Similar to GPT-3, Palmyra Base is a member of the same family of models that only contain a decoder. As a result, it was pre-trained utilizing the objective of self-supervised causal language modeling. Palmyra Base uses the prompts and general experimental setup from GPT-3 in order to conduct its evaluation per GPT-3.

### Use case

Palmyra Base is extremely powerful while being extremely fast. This model excels at many nuanced tasks such as sentiment classification and summarization.

## Training data

Palmyra Base (5b) was trained on Writer’s custom dataset.

## Intended Use and Limitations

Palmyra Base learns an inner representation of the English language that can be used to extract features useful for downstream tasks. However, the model is best at what it was pre-trained for which is generating text from a prompt.

### How to use

This model can be easily loaded using the AutoModelForCausalLM functionality:

### Limitations and Biases

Palmyra Base’s core functionality is to take a string of text and predict the next token. While language models are widely used for other tasks, there are many unknowns in this work. When prompting Palmyra Base, keep in mind that the next statistically likely token is not always the token that produces the most "accurate" text. Never rely on Palmyra Base to produce factually correct results.
Palmyra Base was trained on Writer’s custom data. As with all language models, it is difficult to predict how Palmyra Base will respond to specific prompts, and offensive content may appear unexpectedly. We recommend that the outputs be curated or filtered by humans before they are released, both to censor undesirable content and to improve the quality of the results.

## Evaluation results

Evaluation of Palmyra-base model on the SuperGLUE benchmark

## Citation and Related Information

To cite this model:

## Model tree for Writer/palmyra-base

## Spaces using Writer/palmyra-base 33

## Collection including Writer/palmyra-base


--------------------