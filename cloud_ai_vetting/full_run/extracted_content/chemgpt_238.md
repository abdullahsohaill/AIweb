# ChemGPT
**URL:** https://huggingface.co/ncfrey/ChemGPT-1.2B
**Page Title:** ncfrey/ChemGPT-1.2B · Hugging Face
--------------------


## ChemGPT 1.2B

ChemGPT is based on the GPT-Neo model and was introduced in the paper Neural Scaling of Deep Chemical Models .

## Model description

ChemGPT is a transformers model for generative molecular modeling, which was pretrained on the PubChem10M dataset.

## Intended uses & limitations

### How to use

You can use this model directly from the 🤗/transformers library.

### Limitations and bias

This model was trained on a subset of molecules from PubChem. You can use this model to generate molecules, but it is mostly intended to be used for investigations of the effects of pre-training and fine-tuning on downstream datasets.

## Training data

PubChem10M, a dataset of SMILES strings from PubChem, available via DeepChem .

## Training procedure

### Preprocessing

SMILES strings were converted to SELFIES using version 1.0.4 of the SELFIES library.

### Pretraining

See code in the LitMatter repository .
[LINK: LitMatter repository](https://github.com/ncfrey/litmatter/blob/main/lit_models/lit_chemgpt.py)

### BibTeX entry and citation info

## Space using ncfrey/ChemGPT-1.2B 1


--------------------