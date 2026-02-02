# Nemotron-4-340B
**URL:** https://huggingface.co/nvidia/Nemotron-4-340B-Instruct
**Page Title:** nvidia/Nemotron-4-340B-Instruct · Hugging Face
--------------------


## Nemotron-4-340B-Instruct

### Model Overview

Nemotron-4-340B-Instruct is a large language model (LLM) that can be used as part of a synthetic data generation pipeline to create training data that helps researchers and developers build their own LLMs. It is a fine-tuned version of the Nemotron-4-340B-Base model, optimized for English-based single and multi-turn chat use-cases. It supports a context length of 4,096 tokens.
Try this model on build.nvidia.com now.
The base model was pre-trained on a corpus of 9 trillion tokens consisting of a diverse assortment of English based texts, 50+ natural languages, and 40+ coding languages. Subsequently the Nemotron-4-340B-Instruct model went through additional alignment steps including:
- Supervised Fine-tuning (SFT)
- Direct Preference Optimization (DPO)
- Reward-aware Preference Optimization (RPO) ( Additional in-house alignment technique )
Throughout the alignment process, we relied on only approximately 20K human-annotated data while our data generation pipeline synthesized over 98% of the data used for supervised fine-tuning and preference fine-tuning (DPO & RPO). We provide comprehensive details about our synthetic data generation pipeline in the technical report .
This results in a model that is aligned for human chat preferences, improvements in mathematical reasoning, coding and instruction-following, and is capable of generating high quality synthetic data for a variety of use cases.
Under the NVIDIA Open Model License, NVIDIA confirms:
- Models are commercially usable.
- You are free to create and distribute Derivative Models.
- NVIDIA does not claim ownership to any outputs generated using the Models or Derivative Models.

### License:

NVIDIA Open Model License
[LINK: NVIDIA Open Model License](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)

### Intended use

Nemotron-4-340B-Instruct is a chat model intended for use for the English language.
Nemotron-4-340B-Instruct is designed for Synthetic Data Generation to enable developers and enterprises for building and customizing their own large language models and LLM applications.
The instruct model itself can be further customized using the NeMo Framework suite of customization tools including Parameter-Efficient Fine-Tuning (P-tuning, Adapters, LoRA, and more), and Model Alignment (SFT, SteerLM, RLHF, and more) using NeMo-Aligner . Refer to the documentation for examples.
[LINK: NeMo Framework](https://docs.nvidia.com/nemo-framework/index.html)
[LINK: NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner)
[LINK: documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/nemotron/index.html)
Model Developer: NVIDIA
Model Dates: Nemotron-4-340B-Instruct was trained between December 2023 and May 2024.
Data Freshness: The pretraining data has a cutoff of June 2023.

### Required Hardware

BF16 Inference:
- 8x H200 (1x H200 node)
- 16x H100 (2x H100 nodes)
- 16x A100 80GB (2x A100 80GB nodes)

### Model Architecture:

Nemotron-4-340B-Instruct is standard decoder-only Transformer, trained with a sequence length of 4096 tokens, uses Grouped-Query Attention (GQA), and Rotary Position Embeddings (RoPE).
Architecture Type: Transformer Decoder (auto-regressive language model)
Network Architecture: Nemotron-4

### Prompt Format

Note: For Nemotron-4-340B-Instruct we recommend keeping the system prompt empty.
An example of a formattable prompt template is available in the following section.

### Usage

Deployment and inference with Nemotron-4-340B-Instruct can be done in three steps using NeMo Framework:
Create a Python script to interact with the deployed model.
Create a Bash script to start the inference server
Schedule a Slurm job to distribute the model across 2 nodes and associate them with the inference server.
- Define the Python script call_server.py
- Given this Python script, create a Bash script which spins up the inference server within the NeMo container ( docker pull nvcr.io/nvidia/nemo:24.05 ) and calls the Python script call_server.py . The Bash script nemo_inference.sh is as follows,
- Launch nemo_inference.sh with a Slurm script defined like below, which starts a 2-node job for model inference.

### Evaluation Results

Evaluated using MT-Bench judging by GPT-4-0125-Preview as described in Appendix H in the HelpSteer2 Dataset Paper
Evaluated using the Instruction Following Eval (IFEval) introduced in Instruction-Following Evaluation for Large Language Models.
Evaluated using the Multi-task Language Understanding benchmarks as introduced in Measuring Massive Multitask Language Understanding.
Evaluated using the Grade School Math 8K (GSM8K) benchmark as introduced in Training Verifiers to Solve Math Word Problems.
Evaluated using the HumanEval benchmark as introduced in Evaluating Large Language Models Trained on Code.
Evaluated using the MBPP Dataset as introduced in the Program Synthesis with Large Language Models.
Evaluated using the Arena-Hard Pipeline from the LMSys Org.
Evaluated using the AlpacaEval 2.0 LC (Length Controlled) as introduced in the paper: Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators
Evaluated using the CantTalkAboutThis Dataset as introduced in the CantTalkAboutThis: Aligning Language Models to Stay on Topic in Dialogues.

### Adversarial Testing and Red Teaming Efforts

The Nemotron-4 340B-Instruct model underwent safety evaluation including adversarial testing via three distinct methods:
- Garak , is an automated LLM vulnerability scanner that probes for common weaknesses, including prompt injection and data leakage.
[LINK: Garak](https://docs.garak.ai/garak)
- AEGIS, is a content safety evaluation dataset and LLM based content safety classifier model, that adheres to a broad taxonomy of 13 categories of critical risks in human-LLM interactions.
- Human Content Red Teaming leveraging human interaction and evaluation of the models' responses.

### Limitations

The model was trained on data that contains toxic language, unsafe content, and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.

### Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards here .  Please report security vulnerabilities or NVIDIA AI Concerns here .
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for nvidia/Nemotron-4-340B-Instruct

## Spaces using nvidia/Nemotron-4-340B-Instruct 23

## Collection including nvidia/Nemotron-4-340B-Instruct

## Paper for nvidia/Nemotron-4-340B-Instruct


--------------------