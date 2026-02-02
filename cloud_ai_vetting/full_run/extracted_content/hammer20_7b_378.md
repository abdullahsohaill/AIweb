# Hammer2.0-7b
**URL:** https://huggingface.co/MadeAgents/Hammer2.0-7b
**Page Title:** MadeAgents/Hammer2.0-7b · Hugging Face
--------------------


## Introduction

We're excited to release lightweight Hammer 2.0 models ( 0.5B , 1.5B , 3B ,  and 7B ) with strong function calling capability, which empower developers to build personalized, on-device agentic applications.

## Model Details

Hammer2.0 finetuned based on Qwen 2.5 series and Qwen 2.5 coder series using function masking techniques. It's trained using the APIGen Function Calling Datasets containing 60,000 samples, supplemented by xlam-irrelevance-7.5k we generated. Hammer2.0 has achieved exceptional performances across numerous function calling benchmarks. For more details, please refer to Hammer: Robust Function-Calling for On-Device Language Models via Function Masking and Hammer GitHub repository .
[LINK: Hammer GitHub repository](https://github.com/MadeAgents/Hammer)

## Evaluation

The evaluation results of Hammer 2.0 models on the Berkeley Function-Calling Leaderboard (BFCL-v3) are presented in the following table:
Our Hammer 2.0 series consistently achieves corresponding best performance at comparable scales. The 7B model outperforms most function calling enchanced models, and the 1.5B model also achieves unexpected performance.
In addition, we evaluated the Hammer 2.0 models on other academic benchmarks to further demonstrate the generalization ability of our models.
Hammer 2.0 models showcase highly stable performance, suggesting the robustness of Hammer 2.0 series. In contrast, the baseline approaches display varying levels of effectiveness.

## Requiements

The code of Hammer 2.0 models have been in the latest Hugging face transformers and we advise you to install transformers>=4.37.0 .

## How to Use

This is a simple example of how to use our model.
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for MadeAgents/Hammer2.0-7b

Base model

## Datasets used to train MadeAgents/Hammer2.0-7b

## Collection including MadeAgents/Hammer2.0-7b

## Paper for MadeAgents/Hammer2.0-7b


--------------------