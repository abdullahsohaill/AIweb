# `facebook/bart-large-mnli`
**URL:** https://huggingface.co/facebook/bart-large-mnli
**Page Title:** facebook/bart-large-mnli · Hugging Face
--------------------


## bart-large-mnli

This is the checkpoint for bart-large after being trained on the MultiNLI (MNLI) dataset.
Additional information about this model:
- The bart-large model page
- BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
- BART fairseq implementation
[LINK: BART fairseq implementation](https://github.com/pytorch/fairseq/tree/master/fairseq/models/bart)

## NLI-based Zero Shot Text Classification

Yin et al. proposed a method for using pre-trained NLI models as a ready-made zero-shot sequence classifiers. The method works by posing the sequence to be classified as the NLI premise and to construct a hypothesis from each candidate label. For example, if we want to evaluate whether a sequence belongs to the class "politics", we could construct a hypothesis of This text is about politics. . The probabilities for entailment and contradiction are then converted to label probabilities.
This method is surprisingly effective in many cases, particularly when used with larger pre-trained models like BART and Roberta. See this blog post for a more expansive introduction to this and other zero shot methods, and see the code snippets below for examples of using this model for zero-shot classification both with Hugging Face's built-in pipeline and with native Transformers/PyTorch code.
[LINK: this blog post](https://joeddav.github.io/blog/2020/05/29/ZSL.html)
The model can be loaded with the zero-shot-classification pipeline like so:
You can then use this pipeline to classify sequences into any of the class names you specify.
If more than one candidate label can be correct, pass multi_label=True to calculate each class independently:

## Model tree for facebook/bart-large-mnli

## Dataset used to train facebook/bart-large-mnli

## Spaces using facebook/bart-large-mnli 100

## Papers for facebook/bart-large-mnli

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
facebook/bart-large-mnli is supported by the following Inference Providers:

--------------------