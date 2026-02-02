# Mixtral 8x22B
**URL:** https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1
**Page Title:** mistralai/Mixtral-8x22B-Instruct-v0.1 · Hugging Face
--------------------


## Model Card for Mixtral-8x22B-Instruct-v0.1

## Encode and Decode with mistral_common

## Inference with mistral_inference

## Preparing inputs with Hugging Face transformers

## Inference with hugging face transformers

PRs to correct the transformers tokenizer so that it gives 1-to-1 the same results as the mistral_common reference implementation are very welcome!
The Mixtral-8x22B-Instruct-v0.1 Large Language Model (LLM) is an instruct fine-tuned version of the Mixtral-8x22B-v0.1 .

## Function calling example

## Function calling with transformers

To use this example, you'll need transformers version 4.42.0 or higher. Please see the function calling guide in the transformers docs for more information.
[LINK: function calling guide](https://huggingface.co/docs/transformers/main/chat_templating#advanced-tool-use--function-calling)
Note that, for reasons of space, this example does not show a complete cycle of calling a tool and adding the tool call and tool
results to the chat history so that the model can use them in its next generation. For a full tool calling example, please
see the function calling guide , 
and note that Mixtral does use tool call IDs, so these must be included in your tool calls and tool results. They should be
exactly 9 alphanumeric characters.
[LINK: function calling guide](https://huggingface.co/docs/transformers/main/chat_templating#advanced-tool-use--function-calling)

## Instruct tokenizer

The HuggingFace tokenizer included in this release should match our own. To compare: pip install mistral-common

## Function calling and special tokens

This tokenizer includes more special tokens, related to function calling :
- [TOOL_CALLS]
- [AVAILABLE_TOOLS]
- [/AVAILABLE_TOOLS]
- [TOOL_RESULTS]
- [/TOOL_RESULTS]
If you want to use this model with function calling, please be sure to apply it similarly to what is done in our SentencePieceTokenizerV3 .
[LINK: SentencePieceTokenizerV3](https://github.com/mistralai/mistral-common/blob/main/src/mistral_common/tokens/tokenizers/sentencepiece.py#L299)

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Antoine Roux,
Arthur Mensch, Audrey Herblin-Stoop, Baptiste Bout, Baudouin de Monicault,
Blanche Savary, Bam4d, Caroline Feldman, Devendra Singh Chaplot,
Diego de las Casas, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger,
Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona,
Jean-Malo Delignon, Jia Li, Justus Murke, Louis Martin, Louis Ternon,
Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat,
Marie Torelli, Marie-Anne Lachaux, Nicolas Schuhl, Patrick von Platen,
Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao,
Thibaut Lavril, Timothée Lacroix, Théophile Gervet, Thomas Wang,
Valera Nemychnikova, William El Sayed, William Marshall
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mixtral-8x22B-Instruct-v0.1

Base model

## Spaces using mistralai/Mixtral-8x22B-Instruct-v0.1 100


--------------------