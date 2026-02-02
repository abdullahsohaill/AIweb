# The Pile
**URL:** https://pile.eleuther.ai
**Page Title:** The Pile
--------------------


## What is the Pile?

The Pile is a 825 GiB diverse, open
              source language modelling data set that consists of 22 smaller,
              high-quality datasets combined together.

## Download

The Pile is hosted by the Eye .
The format of the Pile is jsonlines data compressed using zstandard .
[LINK: zstandard](https://facebook.github.io/zstd/)
Have a model that uses or evaluates on the Pile? Let us know !

## Why is the Pile a good training set?

Recent work has shown that especially for large models, diversity
              in data sources improves general cross-domain knowledge of the
              model, as well as downstream generalization capability. In our
              evaluations, not only do models trained on the Pile show moderate
              improvements in traditional language modeling benchmarks, they
              also show significant improvements on Pile BPB.

## Why is the Pile a good benchmark?

To score well on Pile BPB (bits per byte), a model must be able to
              understand many disparate domains including books, github
              repositories, webpages, chat logs, and medical, physics, math,
              computer science, and philosophy papers. Pile BPB is a measure of
              world knowledge and reasoning ability in these domains, making it
              a robust benchmark of general, cross-domain text modeling ability
              for large language models.

## Citing

If you use the Pile or any of the components, please cite us!

## Leaderboard

* indicates potential test-set overlap. Zero-shot indicates that
              not all of the components of the Pile were present in the training
              data.
Jan 1.2021
GPT-3 (Zero-Shot)*
OpenAI
0.7177
Jan 1.2021
GPT-2 (Zero-Shot)*
OpenAI
1.2253
Evaluation code
[LINK: Evaluation code](https://github.com/EleutherAI/lm_perplexity)

--------------------