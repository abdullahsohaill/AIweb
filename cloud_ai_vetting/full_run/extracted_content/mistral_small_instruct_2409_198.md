# Mistral-Small-Instruct-2409
**URL:** https://huggingface.co/mistralai/Mistral-Small-Instruct-2409
**Page Title:** mistralai/Mistral-Small-Instruct-2409 · Hugging Face
--------------------


## Model Card for Mistral-Small-Instruct-2409

Mistral-Small-Instruct-2409 is an instruct fine-tuned version with the following characteristics:
- 22B parameters
- Vocabulary to 32768
- Supports function calling
- 32k sequence length

## Usage Examples

### vLLM (recommended)

We recommend using this model with the vLLM library to implement production-ready inference pipelines.
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Installation
Make sure you install vLLM >= v0.6.1.post1 :
Also make sure you have mistral_common >= 1.4.1 installed:
You can also make use of a ready-to-go docker image .
Offline
Server
You can also use Mistral Small in a server/client setting.
- Spin up a server:
Note: Running Mistral-Small on a single GPU requires at least 44 GB of GPU RAM.
If you want to divide the GPU requirement over multiple devices, please add e.g. --tensor_parallel=2
- And ping the client:

### Mistral-inference

We recommend using mistral-inference to quickly try out / "vibe-check" the model.
[LINK: mistral-inference](https://github.com/mistralai/mistral-inference)
Install
Make sure to have mistral_inference >= 1.4.1 installed.
Download

### Chat

After installing mistral_inference , a mistral-chat CLI command should be available in your environment. You can chat with the model using

### Instruct following

### Function calling

### Usage in Hugging Face Transformers

You can also use Hugging Face transformers library to run inference using various chat templates, or fine-tune the model.
Example for inference:
And you should obtain

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Alok Kothari, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Augustin Garreau, Austin Birky, Bam4d, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Carole Rambaud, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Diogo Costa, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gaspard Blanchet, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Henri Roussez, Hichem Sattouf, Ian Mack, Jean-Malo Delignon, Jessica Chudnovsky, Justus Murke, Kartik Khandelwal, Lawrence Stewart, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Marjorie Janiewicz, Mickaël Seznec, Nicolas Schuhl, Niklas Muhs, Olivier de Garrigues, Patrick von Platen, Paul Jacob, Pauline Buche, Pavan Kumar Reddy, Perry Savas, Pierre Stock, Romain Sauvestre, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Wang, Théophile Gervet, Timothée Lacroix, Valera Nemychnikova, Wendy Shang, William El Sayed, William Marshall
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mistral-Small-Instruct-2409

## Spaces using mistralai/Mistral-Small-Instruct-2409 17


--------------------