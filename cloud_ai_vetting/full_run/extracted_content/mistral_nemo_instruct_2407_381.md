# Mistral-Nemo-Instruct-2407
**URL:** https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407
**Page Title:** mistralai/Mistral-Nemo-Instruct-2407 · Hugging Face
--------------------


## Model Card for Mistral-Nemo-Instruct-2407

The Mistral-Nemo-Instruct-2407 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral-Nemo-Base-2407 . Trained jointly by Mistral AI and NVIDIA, it significantly outperforms existing models smaller or similar in size.
For more details about this model please refer to our release blog post .

## Key features

- Released under the Apache 2 License
- Pre-trained and instructed versions
- Trained with a 128k context window
- Trained on a large proportion of multilingual and code data
- Drop-in replacement of Mistral 7B

## Model Architecture

Mistral Nemo is a transformer model, with the following architecture choices:
- Layers: 40
- Dim: 5,120
- Head dim: 128
- Hidden dim: 14,336
- Activation Function: SwiGLU
- Number of heads: 32
- Number of kv-heads: 8 (GQA)
- Vocabulary size: 2**17 ~= 128k
- Rotary embeddings (theta = 1M)

## Metrics

### Main Benchmarks

### Multilingual Benchmarks (MMLU)

## Usage

The model can be used with three different frameworks
- mistral_inference : See here
[LINK: mistral_inference](https://github.com/mistralai/mistral-inference)
- transformers : See here
[LINK: transformers](https://github.com/huggingface/transformers)
- NeMo : See nvidia/Mistral-NeMo-12B-Instruct
[LINK: NeMo](https://github.com/NVIDIA/NeMo)

### Mistral Inference

It is recommended to use mistralai/Mistral-Nemo-Instruct-2407 with mistral-inference . For HF transformers code snippets, please keep scrolling.
[LINK: mistral-inference](https://github.com/mistralai/mistral-inference)
After installing mistral_inference , a mistral-chat CLI command should be available in your environment. You can chat with the model using
E.g. Try out something like:

### Transformers

NOTE: Until a new release has been made, you need to install transformers from source:
If you want to use Hugging Face transformers to generate text, you can do something like this.

## Function calling with transformers

To use this example, you'll need transformers version 4.42.0 or higher. Please see the function calling guide in the transformers docs for more information.
[LINK: function calling guide](https://huggingface.co/docs/transformers/main/chat_templating#advanced-tool-use--function-calling)
Note that, for reasons of space, this example does not show a complete cycle of calling a tool and adding the tool call and tool
results to the chat history so that the model can use them in its next generation. For a full tool calling example, please
see the function calling guide , 
and note that Mistral does use tool call IDs, so these must be included in your tool calls and tool results. They should be
exactly 9 alphanumeric characters.
[LINK: function calling guide](https://huggingface.co/docs/transformers/main/chat_templating#advanced-tool-use--function-calling)
Unlike previous Mistral models, Mistral Nemo requires smaller temperatures. We recommend to use a temperature of 0.3.

## Limitations

The Mistral Nemo Instruct model is a quick demonstration that the base model can be easily fine-tuned to achieve compelling performance. 
It does not have any moderation mechanisms. We're looking forward to engaging with the community on ways to
make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Alok Kothari, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Augustin Garreau, Austin Birky, Bam4d, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Carole Rambaud, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gaspard Blanchet, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Henri Roussez, Hichem Sattouf, Ian Mack, Jean-Malo Delignon, Jessica Chudnovsky, Justus Murke, Kartik Khandelwal, Lawrence Stewart, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Marjorie Janiewicz, Mickaël Seznec, Nicolas Schuhl, Niklas Muhs, Olivier de Garrigues, Patrick von Platen, Paul Jacob, Pauline Buche, Pavan Kumar Reddy, Perry Savas, Pierre Stock, Romain Sauvestre, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Wang, Théophile Gervet, Timothée Lacroix, Valera Nemychnikova, Wendy Shang, William El Sayed, William Marshall
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mistral-Nemo-Instruct-2407

Base model

## Spaces using mistralai/Mistral-Nemo-Instruct-2407 100


--------------------