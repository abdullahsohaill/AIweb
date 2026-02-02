# Pixtral-12B
**URL:** https://huggingface.co/mistralai/Pixtral-12B-2409
**Page Title:** mistralai/Pixtral-12B-2409 · Hugging Face
--------------------


## Model Card for Pixtral-12B-2409

The Pixtral-12B-2409 is a Multimodal Model of 12B parameters plus a 400M parameter vision encoder.
For more details about this model please refer to our release blog post .
Feel free to try it here

## Key features

- Natively multimodal, trained with interleaved image and text data
- 12B parameter Multimodal Decoder + 400M parameter Vision Encoder
- Supports variable image sizes
- Leading performance in its weight class on multimodal tasks
- Maintains state-of-the-art performance on text-only benchmarks
- Sequence length: 128k
- License: Apache 2.0

## Benchmarks

The performance of Pixtral-12B-2409 compared to multimodal models. All models were re-evaluated and benchmarked through the same evaluation pipeline.

### Multimodal Benchmarks

### Instruction Following

### Text Benchmarks

### Comparison with Closed Source and Larger Models

## Usage Examples

### vLLM (recommended)

We recommend using Pixtral with the vLLM library to implement production-ready inference pipelines with Pixtral.
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Installation
Make sure you install vLLM >= v0.6.2 :
Also make sure you have mistral_common >= 1.4.4 installed:
You can also make use of a ready-to-go docker image .
Simple Example
Advanced Example
You can also pass multiple images per message and/or pass multi-turn conversations
You can find more examples and tests directly in vLLM.
- Examples
[LINK: Examples](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_pixtral.py)
- Tests
[LINK: Tests](https://github.com/vllm-project/vllm/blob/main/tests/models/test_pixtral.py)
Server
You can also use pixtral in a server/client setting.
- Spin up a server:
- And ping the client:

### Mistral-inference

We recommend using mistral-inference to quickly try out / "vibe-check" Pixtral.
[LINK: mistral-inference](https://github.com/mistralai/mistral-inference)
Install
Make sure to have mistral_inference >= 1.4.1 installed.
Download
Chat
After installing mistral_inference , a mistral-chat CLI command should be available in your environment. 
You can pass text and images or image urls to the model in instruction-following mode as follows:
E.g. Try out something like:
Python
You can also run the model in a Python shell as follows.

## Limitations

The Pixtral model does not have any moderation mechanisms. We're looking forward to engaging with the community on ways to
make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Alok Kothari, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Augustin Garreau, Austin Birky, Bam4d, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Carole Rambaud, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Diogo Costa, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gaspard Blanchet, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Henri Roussez, Hichem Sattouf, Ian Mack, Jean-Malo Delignon, Jessica Chudnovsky, Justus Murke, Kartik Khandelwal, Lawrence Stewart, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Marjorie Janiewicz, Mickaël Seznec, Nicolas Schuhl, Niklas Muhs, Olivier de Garrigues, Patrick von Platen, Paul Jacob, Pauline Buche, Pavan Kumar Reddy, Perry Savas, Pierre Stock, Romain Sauvestre, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Wang, Théophile Gervet, Timothée Lacroix, Valera Nemychnikova, Wendy Shang, William El Sayed, William Marshall
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Pixtral-12B-2409

Base model

## Spaces using mistralai/Pixtral-12B-2409 36


--------------------