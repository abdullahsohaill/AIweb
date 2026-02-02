# Granite-20b-code-instruct-8k
**URL:** https://huggingface.co/ibm-granite/granite-20b-code-instruct-8k
**Page Title:** ibm-granite/granite-20b-code-instruct-8k · Hugging Face
--------------------


## Granite-20B-Code-Instruct-8K

## Model Summary

Granite-20B-Code-Instruct-8K is a 20B parameter model fine tuned from Granite-20B-Code-Base-8K on a combination of permissively licensed instruction data to enhance instruction following capabilities including logical reasoning and problem-solving skills.
- Developers: IBM Research
- GitHub Repository: ibm-granite/granite-code-models
[LINK: ibm-granite/granite-code-models](https://github.com/ibm-granite/granite-code-models)
- Paper: Granite Code Models: A Family of Open Foundation Models for Code Intelligence
- Release Date : May 6th, 2024
- License: Apache 2.0 .

## Usage

### Intended use

The model is designed to respond to coding related instructions and can be used to build coding assistants.

### Generation

This is a simple example of how to use Granite-20B-Code-Instruct-8K model.

## Training Data

Granite Code Instruct models are trained on the following types of data.
- Code Commits Datasets: we sourced code commits data from the CommitPackFT dataset, a filtered version of the full CommitPack dataset. From CommitPackFT dataset, we only consider data for 92 programming languages. Our inclusion criteria boils down to selecting programming languages common across CommitPackFT and the 116 languages that we considered to pretrain the code-base model ( Granite-20B-Code-Base ).
- Math Datasets: We consider two high-quality math datasets, MathInstruct and MetaMathQA . Due to license issues, we filtered out GSM8K-RFT and Camel-Math from MathInstruct dataset.
- Code Instruction Datasets: We use Glaive-Code-Assistant-v3 , Glaive-Function-Calling-v2 , NL2SQL11 and a small collection of synthetic API calling datasets.
- Language Instruction Datasets: We include high-quality datasets such as HelpSteer and an open license-filtered version of Platypus . We also include a collection of hardcoded prompts to ensure our model generates correct outputs given inquiries about its name or developers.

## Infrastructure

We train the Granite Code models using two of IBM's super computing clusters, namely Vela and Blue Vela, both outfitted with NVIDIA A100 and H100 GPUs respectively. These clusters provide a scalable and efficient infrastructure for training our models over thousands of GPUs.

## Ethical Considerations and Limitations

Granite code instruct models are primarily finetuned using instruction-response pairs across a specific set of programming languages. Thus, their performance may be limited with out-of-domain programming languages. In this situation, it is beneficial providing few-shot examples to steer the model's output. Moreover, developers should perform safety testing and target-specific tuning before deploying these models on critical applications. The model also inherits ethical considerations and limitations from its base model. For more information, please refer to Granite-20B-Code-Base-8K model card.

## Model tree for ibm-granite/granite-20b-code-instruct-8k

Base model

## Datasets used to train ibm-granite/granite-20b-code-instruct-8k

## Collection including ibm-granite/granite-20b-code-instruct-8k

## Paper for ibm-granite/granite-20b-code-instruct-8k

## Evaluation results

- pass@1 on HumanEvalSynthesis(Python) self-reported 60.400
- pass@1 on HumanEvalSynthesis(JavaScript) self-reported 53.700
- pass@1 on HumanEvalSynthesis(Java) self-reported 58.500
- pass@1 on HumanEvalSynthesis(Go) self-reported 42.100
- pass@1 on HumanEvalSynthesis(C++) self-reported 45.700
- pass@1 on HumanEvalSynthesis(Rust) self-reported 42.700
- pass@1 on HumanEvalExplain(Python) self-reported 44.500
- pass@1 on HumanEvalExplain(JavaScript) self-reported 42.700
- pass@1 on HumanEvalExplain(Java) self-reported 49.400
- pass@1 on HumanEvalExplain(Go) self-reported 32.300
- pass@1 on HumanEvalExplain(C++) self-reported 42.100
- pass@1 on HumanEvalExplain(Rust) self-reported 18.300
- pass@1 on HumanEvalFix(Python) self-reported 43.900
- pass@1 on HumanEvalFix(JavaScript) self-reported 43.900
- pass@1 on HumanEvalFix(Java) self-reported 45.700
- pass@1 on HumanEvalFix(Go) self-reported 41.500
- pass@1 on HumanEvalFix(C++) self-reported 41.500
- pass@1 on HumanEvalFix(Rust) self-reported 29.900

--------------------