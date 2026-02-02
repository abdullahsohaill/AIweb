# Codestral-22B-v0.1
**URL:** https://huggingface.co/mistralai/Codestral-22B-v0.1
**Page Title:** mistralai/Codestral-22B-v0.1 · Hugging Face
--------------------


## Model Card for Codestral-22B-v0.1

## Encode and Decode with mistral_common

## Inference with mistral_inference

## Inference with hugging face transformers

PRs to correct the transformers tokenizer so that it gives 1-to-1 the same results as the mistral_common reference implementation are very welcome!
Codestral-22B-v0.1 is trained on a diverse dataset of 80+ programming languages, including the most popular ones, such as Python, Java, C, C++, JavaScript, and Bash (more details in the Blogpost ). The model can be queried:
- As instruct, for instance to answer any questions about a code snippet (write documentation, explain, factorize) or to generate code following specific indications
- As Fill in the Middle (FIM), to predict the middle tokens between a prefix and a suffix (very useful for software development add-ons like in VS Code)

## Installation

It is recommended to use mistralai/Codestral-22B-v0.1 with mistral-inference .
[LINK: mistral-inference](https://github.com/mistralai/mistral-inference)

## Download

### Chat

After installing mistral_inference , a mistral-chat CLI command should be available in your environment.
Will generate an answer to "Write me a function that computes fibonacci in Rust" and should give something along the following lines:

### Fill-in-the-middle (FIM)

After installing mistral_inference and running pip install --upgrade mistral_common to make sure to have mistral_common>=1.2 installed:
Should give something along the following lines:

## Usage with transformers library

This model is also compatible with transformers library, first run pip install -U transformers then use the snippet below to quickly get started:
By default, transformers will load the model in full precision. Therefore you might be interested to further reduce down the memory requirements to run the model through the optimizations we offer in HF ecosystem.

## Limitations

The Codestral-22B-v0.1 does not have any moderation mechanisms. We're looking forward to engaging with the community on ways to
make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.

## License

Codestral-22B-v0.1 is released under the MNLP-0.1 license.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Bam4d, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Henri Roussez, Jean-Malo Delignon, Jia Li, Justus Murke, Kartik Khandelwal, Lawrence Stewart, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Marjorie Janiewicz, Mickael Seznec, Nicolas Schuhl, Patrick von Platen, Romain Sauvestre, Pierre Stock, Sandeep Subramanian, Saurabh Garg, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibaut Lavril, Thibault Schueller, Timothée Lacroix, Théophile Gervet, Thomas Wang, Valera Nemychnikova, Wendy Shang, William El Sayed, William Marshall
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Codestral-22B-v0.1

## Spaces using mistralai/Codestral-22B-v0.1 33


--------------------