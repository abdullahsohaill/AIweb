# **WikiText-103**
**URL:** https://huggingface.co/datasets/Salesforce/wikitext
**Page Title:** Salesforce/wikitext · Datasets at Hugging Face
--------------------


## Dataset Card for "wikitext"

### Dataset Summary

The WikiText language modeling dataset is a collection of over 100 million tokens extracted from the set of verified
 Good and Featured articles on Wikipedia. The dataset is available under the Creative Commons Attribution-ShareAlike License.
Compared to the preprocessed version of Penn Treebank (PTB), WikiText-2 is over 2 times larger and WikiText-103 is over
110 times larger. The WikiText dataset also features a far larger vocabulary and retains the original case, punctuation
and numbers - all of which are removed in PTB. As it is composed of full articles, the dataset is well suited for models
that can take advantage of long term dependencies.
Each subset comes in two different variants:
- Raw (for character level work) contain the raw tokens, before the addition of the  (unknown) tokens.
- Non-raw (for word level work) contain only the tokens in their vocabulary (wiki.train.tokens, wiki.valid.tokens, and wiki.test.tokens).
The out-of-vocabulary tokens have been replaced with the the  token.

### Supported Tasks and Leaderboards

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

- Size of downloaded dataset files: 191.98 MB
- Size of the generated dataset: 549.42 MB
- Total amount of disk used: 741.41 MB
An example of 'validation' looks as follows.
- Size of downloaded dataset files: 190.23 MB
- Size of the generated dataset: 548.05 MB
- Total amount of disk used: 738.27 MB
An example of 'train' looks as follows.
- Size of downloaded dataset files: 4.72 MB
- Size of the generated dataset: 13.54 MB
- Total amount of disk used: 18.26 MB
An example of 'train' looks as follows.
- Size of downloaded dataset files: 4.48 MB
- Size of the generated dataset: 13.34 MB
- Total amount of disk used: 17.82 MB
An example of 'train' looks as follows.

### Data Fields

The data fields are the same among all splits.
- text : a string feature.
- text : a string feature.
- text : a string feature.
- text : a string feature.

### Data Splits

## Dataset Creation

### Curation Rationale

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

More Information Needed
[LINK: More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

The dataset is available under the Creative Commons Attribution-ShareAlike License (CC BY-SA 4.0) .

### Citation Information

### Contributions

Thanks to @thomwolf , @lewtun , @patrickvonplaten , @mariamabarham for adding this dataset.
[LINK: @thomwolf](https://github.com/thomwolf)
[LINK: @lewtun](https://github.com/lewtun)
[LINK: @patrickvonplaten](https://github.com/patrickvonplaten)
[LINK: @mariamabarham](https://github.com/mariamabarham)

## Models trained or fine-tuned on Salesforce/wikitext

## Spaces using Salesforce/wikitext 24

## Paper for Salesforce/wikitext


--------------------