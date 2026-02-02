# Ministral-8B-Instruct
**URL:** https://huggingface.co/mistralai/Ministral-8B-Instruct-2410
**Page Title:** mistralai/Ministral-8B-Instruct-2410 · Hugging Face
--------------------


## Model Card for Ministral-8B-Instruct-2410

We introduce two new state-of-the-art models for local intelligence, on-device computing, and at-the-edge use cases. We call them les Ministraux: Ministral 3B and Ministral 8B.
The Ministral-8B-Instruct-2410 Language Model is an instruct fine-tuned model significantly outperforming existing models of similar size, released under the Mistral Research License.
If you are interested in using Ministral-3B or Ministral-8B commercially, outperforming Mistral-7B, reach out to us .
For more details about les Ministraux please refer to our release blog post .

## Ministral 8B Key features

- Released under the Mistral Research License , reach out to us for a commercial license
- Trained with a 128k context window with interleaved sliding-window attention
- Trained on a large proportion of multilingual and code data
- Supports function calling
- Vocabulary size of 131k , using the V3-Tekken tokenizer

### Basic Instruct Template (V3-Tekken)

For more information about the tokenizer please refer to mistral-common
[LINK: mistral-common](https://github.com/mistralai/mistral-common)

## Ministral 8B Architecture

## Benchmarks

Knowledge & Commonsense
Code & Math
Multilingual

### Instruct Models

Chat/Arena (gpt-4o judge)
Code & Math
Function calling

## Usage Examples

### vLLM (recommended)

We recommend using this model with the vLLM library to implement production-ready inference pipelines.
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Currently vLLM is capped at 32k context size because interleaved attention kernels for paged attention are not yet implemented in vLLM.
Attention kernels for paged attention are being worked on and as soon as it is fully supported in vLLM, this model card will be updated.
To take advantage of the full 128k context size we recommend Mistral Inference
Installation
Make sure you install vLLM >= v0.6.4 :
Also make sure you have mistral_common >= 1.4.4 installed:
You can also make use of a ready-to-go docker image .
[LINK: docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile)
Offline
Server
You can also use Ministral-8B in a server/client setting.
- Spin up a server:
Note: Running Ministral-8B on a single GPU requires 24 GB of GPU RAM.
If you want to divide the GPU requirement over multiple devices, please add e.g. --tensor_parallel=2
- And ping the client:

### Mistral-inference

We recommend using mistral-inference to quickly try out / "vibe-check" the model.
[LINK: mistral-inference](https://github.com/mistralai/mistral-inference)
Install
Make sure to have mistral_inference >= 1.5.0 installed.
Download

### Chat

After installing mistral_inference , a mistral-chat CLI command should be available in your environment. You can chat with the model using

### Passkey detection

In this example the passkey message has over >100k tokens and mistral-inference
does not have a chunked pre-fill mechanism. Therefore you will need a lot of
GPU memory in order to run the below example (80 GB). For a more memory-efficient
solution we recommend using vLLM.

### Instruct following

### Function calling

## The Mistral AI Team

Albert Jiang, Alexandre Abou Chahine, Alexandre Sablayrolles, Alexis Tacnet, Alodie Boissonnet, Alok Kothari, Amélie Héliou, Andy Lo, Anna Peronnin, Antoine Meunier, Antoine Roux, Antonin Faure, Aritra Paul, Arthur Darcet, Arthur Mensch, Audrey Herblin-Stoop, Augustin Garreau, Austin Birky, Avinash Sooriyarachchi, Baptiste Rozière, Barry Conklin, Bastien Bouillon, Blanche Savary de Beauregard, Carole Rambaud, Caroline Feldman, Charles de Freminville, Charline Mauro, Chih-Kuan Yeh, Chris Bamford, Clement Auguy, Corentin Heintz, Cyriaque Dubois, Devendra Singh Chaplot, Diego Las Casas, Diogo Costa, Eléonore Arcelin, Emma Bou Hanna, Etienne Metzger, Fanny Olivier Autran, Francois Lesage, Garance Gourdel, Gaspard Blanchet, Gaspard Donada Vidal, Gianna Maria Lengyel, Guillaume Bour, Guillaume Lample, Gustave Denis, Harizo Rajaona, Himanshu Jaju, Ian Mack, Ian Mathew, Jean-Malo Delignon, Jeremy Facchetti, Jessica Chudnovsky, Joachim Studnia, Justus Murke, Kartik Khandelwal, Kenneth Chiu, Kevin Riera, Leonard Blier, Leonard Suslian, Leonardo Deschaseaux, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Sophia Yang, Margaret Jennings, Marie Pellat, Marie Torelli, Marjorie Janiewicz, Mathis Felardos, Maxime Darrin, Michael Hoff, Mickaël Seznec, Misha Jessel Kenyon, Nayef Derwiche, Nicolas Carmont Zaragoza, Nicolas Faurie, Nicolas Moreau, Nicolas Schuhl, Nikhil Raghuraman, Niklas Muhs, Olivier de Garrigues, Patricia Rozé, Patricia Wang, Patrick von Platen, Paul Jacob, Pauline Buche, Pavankumar Reddy Muddireddy, Perry Savas, Pierre Stock, Pravesh Agrawal, Renaud de Peretti, Romain Sauvestre, Romain Sinthe, Roman Soletskyi, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Soham Ghosh, Sylvain Regnier, Szymon Antoniak, Teven Le Scao, Theophile Gervet, Thibault Schueller, Thibaut Lavril, Thomas Wang, Timothée Lacroix, Valeriia Nemychnikova, Wendy Shang, William El Sayed, William Marshall
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Ministral-8B-Instruct-2410

## Spaces using mistralai/Ministral-8B-Instruct-2410 23


--------------------