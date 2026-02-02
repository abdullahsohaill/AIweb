# google/siglip2-so400m-patch16-naflex
**URL:** https://huggingface.co/google/siglip2-so400m-patch16-naflex
**Page Title:** google/siglip2-so400m-patch16-naflex · Hugging Face
--------------------


## SigLIP 2 So400m

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques
into a unified recipe, for improved semantic understanding, localization, and dense features.

## Intended uses

You can use the raw model for tasks like zero-shot image classification and
image-text retrieval, or as a vision encoder for VLMs (and other vision tasks).
Here is how to use this model to perform zero-shot image classification:
You can encode an image using the Vision Tower like so:
For more code examples, we refer to the siglip2 documentation .

## Training procedure

SigLIP 2 adds some clever training objectives on top of SigLIP:
- Decoder loss
- Global-local and masked prediction loss
- Aspect ratio and resolution adaptibility

### Training data

SigLIP 2 is pre-trained on the WebLI dataset (Chen et al., 2023) .

### Compute

The model was trained on up to 2048 TPU-v5e chips.

## Evaluation results

Evaluation of SigLIP 2 is shown below (taken from the paper).

### BibTeX entry and citation info

## Model tree for google/siglip2-so400m-patch16-naflex

## Spaces using google/siglip2-so400m-patch16-naflex 2

## Collection including google/siglip2-so400m-patch16-naflex

## Papers for google/siglip2-so400m-patch16-naflex


--------------------