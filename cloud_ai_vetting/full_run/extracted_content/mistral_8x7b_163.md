# Mistral 8x7b
**URL:** https://huggingface.co/mistralai/Mixtral-8x7B-v0.1
**Page Title:** mistralai/Mixtral-8x7B-v0.1 · Hugging Face
--------------------


## Model Card for Mixtral-8x7B

The Mixtral-8x7B Large Language Model (LLM) is a pretrained generative Sparse Mixture of Experts. The Mistral-8x7B outperforms Llama 2 70B on most benchmarks we tested.
For full details of this model please read our release blog post .

## Warning

This repo contains weights that are compatible with vLLM serving of the model as well as Hugging Face transformers library. It is based on the original Mixtral torrent release , but the file format and parameter names are different. Please note that model cannot (yet) be instantiated with HF.
[LINK: vLLM](https://github.com/vllm-project/vllm)
[LINK: transformers](https://github.com/huggingface/transformers)

## Run the model

By default, transformers will load the model in full precision. Therefore you might be interested to further reduce down the memory requirements to run the model through the optimizations we offer in HF ecosystem:

### In half-precision

Note float16 precision only works on GPU devices

### Lower precision using (8-bit & 4-bit) using bitsandbytes

### Load the model with Flash Attention 2

## Notice

Mixtral-8x7B is a pretrained base model and therefore does not have any moderation mechanisms.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Louis Ternon, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed.
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mixtral-8x7B-v0.1

## Spaces using mistralai/Mixtral-8x7B-v0.1 100


--------------------