# Mixtral 8x7B
**URL:** https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
**Page Title:** mistralai/Mixtral-8x7B-Instruct-v0.1 · Hugging Face
--------------------


## Model Card for Mixtral-8x7B

### Tokenization with mistral-common

## Inference with mistral_inference

## Inference with hugging face transformers

PRs to correct the transformers tokenizer so that it gives 1-to-1 the same results as the mistral-common reference implementation are very welcome!
The Mixtral-8x7B Large Language Model (LLM) is a pretrained generative Sparse Mixture of Experts. The Mixtral-8x7B outperforms Llama 2 70B on most benchmarks we tested.
For full details of this model please read our release blog post .

## Warning

This repo contains weights that are compatible with vLLM serving of the model as well as Hugging Face transformers library. It is based on the original Mixtral torrent release , but the file format and parameter names are different. Please note that model cannot (yet) be instantiated with HF.
[LINK: vLLM](https://github.com/vllm-project/vllm)
[LINK: transformers](https://github.com/huggingface/transformers)

## Instruction format

This format must be strictly respected, otherwise the model will generate sub-optimal outputs.
The template used to build a prompt for the Instruct model is defined as follows:
Note that <s> and </s> are special tokens for beginning of string (BOS) and end of string (EOS) while [INST] and [/INST] are regular strings.
As reference, here is the pseudo-code used to tokenize instructions during fine-tuning:
In the pseudo-code above, note that the tokenize method should not add a BOS or EOS token automatically, but should add a prefix space.
In the Transformers library, one can use chat templates which make sure the right format is applied.
[LINK: chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating)

## Run the model

By default, transformers will load the model in full precision. Therefore you might be interested to further reduce down the memory requirements to run the model through the optimizations we offer in HF ecosystem:

### In half-precision

Note float16 precision only works on GPU devices

### Lower precision using (8-bit & 4-bit) using bitsandbytes

### Load the model with Flash Attention 2

## Limitations

The Mixtral-8x7B Instruct model is a quick demonstration that the base model can be easily fine-tuned to achieve compelling performance. 
It does not have any moderation mechanisms. We're looking forward to engaging with the community on ways to
make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Louis Ternon, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed.
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mixtral-8x7B-Instruct-v0.1

Base model

## Spaces using mistralai/Mixtral-8x7B-Instruct-v0.1 100


--------------------