# Mistral 7B model
**URL:** https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
**Page Title:** mistralai/Mistral-7B-Instruct-v0.2 · Hugging Face
--------------------


## Model Card for Mistral-7B-Instruct-v0.2

## Encode and Decode with mistral_common

## Inference with mistral_inference

## Inference with hugging face transformers

PRs to correct the transformers tokenizer so that it gives 1-to-1 the same results as the mistral_common reference implementation are very welcome!
The Mistral-7B-Instruct-v0.2 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral-7B-v0.2.
Mistral-7B-v0.2 has the following changes compared to Mistral-7B-v0.1
- 32k context window (vs 8k context in v0.1)
- Rope-theta = 1e6
- No Sliding-Window Attention
For full details of this model please read our paper and release blog post .

## Instruction format

In order to leverage instruction fine-tuning, your prompt should be surrounded by [INST] and [/INST] tokens. The very first instruction should begin with a begin of sentence id. The next instructions should not. The assistant generation will be ended by the end-of-sentence token id.
E.g.
This format is available as a chat template via the apply_chat_template() method:
[LINK: chat template](https://huggingface.co/docs/transformers/main/chat_templating)

## Troubleshooting

- If you see the following error:
Installing transformers from source should solve the issue
pip install git+ https://github.com/huggingface/transformers
[LINK: https://github.com/huggingface/transformers](https://github.com/huggingface/transformers)
This should not be required after transformers-v4.33.4.

## Limitations

The Mistral 7B Instruct model is a quick demonstration that the base model can be easily fine-tuned to achieve compelling performance. 
It does not have any moderation mechanisms. We're looking forward to engaging with the community on ways to
make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Louis Ternon, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed.

## Model tree for mistralai/Mistral-7B-Instruct-v0.2

## Spaces using mistralai/Mistral-7B-Instruct-v0.2 100

## Paper for mistralai/Mistral-7B-Instruct-v0.2

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
mistralai/Mistral-7B-Instruct-v0.2 is supported by the following Inference Providers:

--------------------