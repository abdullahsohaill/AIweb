# Improving Language Plasticity via Pretraining with Active Forgetting
**URL:** https://huggingface.co/papers/2307.01163
**Page Title:** Paper page - Improving Language Plasticity via Pretraining with Active Forgetting
--------------------


## Improving Language Plasticity via Pretraining with Active Forgetting

## Abstract

Active forgetting mechanism during pretraining improves pretrained language models' adaptation to new, especially distant languages with limited data.
Pretrained language models ( PLMs ) are today the primary model for natural
language processing. Despite their impressive downstream performance, it can be
difficult to apply PLMs to new languages, a barrier to making their
capabilities universally accessible. While prior work has shown it possible to
address this issue by learning a new embedding layer for the new language,
doing so is both data and compute inefficient. We propose to use an active
forgetting mechanism during pretraining, as a simple way of creating PLMs that
can quickly adapt to new languages. Concretely, by resetting the embedding
layer every K updates during pretraining, we encourage the PLM to improve its
ability of learning new embeddings within a limited number of updates, similar
to a meta-learning effect. Experiments with RoBERTa show that models pretrained
with our forgetting mechanism not only demonstrate faster convergence during language adaptation but also outperform standard ones in a low-data regime ,
particularly for languages that are distant from English.

### Community

· Sign up or log in to comment

## Models citing this paper 0

No model linking this paper

## Datasets citing this paper 0

No dataset linking this paper

### Spaces citing this paper 0

No Space linking this paper

## Collections including this paper 1


--------------------