# OpenHermes-13B
**URL:** https://huggingface.co/teknium/OpenHermes-13B
**Page Title:** teknium/OpenHermes-13B · Hugging Face
--------------------


## OpenHermes-13B

## Model description

OpenHermes 13B is the first fine tune of the Hermes dataset that has a fully open source dataset!
OpenHermes was trained on 242,000 entries of primarily GPT-4 generated data, from open datasets across the AI landscape, including:
- GPTeacher - General Instruct, Roleplay v1, Roleplay v2, and Code Instruct Datasets, by Teknium
- WizardLM (v1, evol_instruct 70k), by WizardLM Team/nlpxucan
- Airoboros GPT-4 (v1.0), by JonDurbin
- Camel-AI's domain expert datasets, by the Camel-AI Team
- CodeAlpaca, by Sahil2801
- GPT4-LLM and Unnatural Instructions, by Microsoft
Filtering included removal of OpenAI refusals, disclaimers, and "As an AI" type examples and more
The base dataset mix the model was trained on is identical to Nous-Hermes', minus the Nous-Instruct and PDACTL datasets which were private datasets.
The WANDB Project is public and can be examined at this link: https://wandb.ai/teknium1/openhermes/runs/openhermes-v2-fullft-13b
Huge thank you to main_horse for compute access and a16z for sponsoring my work, and all the dataset creators and other people who's work has contributed to this project!

## Example Outputs

## Benchmark Information

## Benchmark Results

GPT-4All Benchmark Set
AGI-Eval
BigBench Reasoning Test
This is a slight improvement on GPT4ALL Suite and BigBench Suite, with a degredation in AGIEval compared to the original hermes.
Average Score Comparison between Nous-Hermes Llama-2 and OpenHermes Llama-2:

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 300
- num_epochs: 3

## Model tree for teknium/OpenHermes-13B

Base model

## Dataset used to train teknium/OpenHermes-13B

## Collection including teknium/OpenHermes-13B


--------------------