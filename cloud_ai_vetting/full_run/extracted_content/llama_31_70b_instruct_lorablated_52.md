# Llama-3.1-70B-Instruct-lorablated
**URL:** https://huggingface.co/mlabonne/Llama-3.1-70B-Instruct-lorablated
**Page Title:** mlabonne/Llama-3.1-70B-Instruct-lorablated · Hugging Face
--------------------


## 🦙 Llama-3.1-70B-Instruct-lorablated

This is an uncensored version of Llama 3.1 70B Instruct created with abliteration (see this article to know more about it) using @grimjim 's recipe.
More precisely, this is a LoRA-abliterated (lorablated) model:
- Extraction : We extract a LoRA adapter by comparing two models: a censored Llama 3 and an abliterated Llama 3
- Merge : We merge this new LoRA adapter using task arithmetic to a censored Llama 3.1 to abliterate it.
I adapted this recipe to Llama 3.1 70B using failspy/Meta-Llama-3-70B-Instruct-abliterated-v3.5 and optimized the LoRA rank.
The model is fully uncensored in my tests and maintains a high level of quality. A more rigorous evaluation is still needed to measure the impact of this process on benchmarks.
Special thanks to @grimjim for this technique (see his 8B model ) and @FailSpy for his 70B abliterated model . Please follow them if you're interested in abliterated models.
In addition, thanks to brev.dev for providing me with compute!

## 🔍 Applications

General-purpose, role-play (see feedback from McUH ). Use the Llama 3 chat template.

## ⚡️ Quantization

- GGUF : https://huggingface.co/mlabonne/Llama-3.1-70B-Instruct-lorablated-GGUF
- Bartowski : https://huggingface.co/bartowski/Llama-3.1-70B-Instruct-lorablated-GGUF (with IQ quants)

## 🧩 Configuration

This model was merged using the task arithmetic merge method using ./meta-llama/Meta-Llama-3.1-70B-Instruct + Llama-3-70B-Instruct-abliterated-LORA as a base.
The following YAML configuration was used to produce this model:
You can reproduce this model using the following commands:

## Model tree for mlabonne/Llama-3.1-70B-Instruct-lorablated

Base model

## Space using mlabonne/Llama-3.1-70B-Instruct-lorablated 1

## Collection including mlabonne/Llama-3.1-70B-Instruct-lorablated

## Paper for mlabonne/Llama-3.1-70B-Instruct-lorablated


--------------------