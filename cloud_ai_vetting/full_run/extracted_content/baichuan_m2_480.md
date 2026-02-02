# Baichuan-M2
**URL:** https://huggingface.co/baichuan-inc/Baichuan-M2-32B
**Page Title:** baichuan-inc/Baichuan-M2-32B · Hugging Face
--------------------


## Baichuan-M2-32B

This repository contains the model presented in Baichuan-M2: Scaling Medical Capability with Large Verifier System .

## 🌟 Model Overview

Baichuan-M2-32B is Baichuan AI's medical-enhanced reasoning model, the second medical model released by Baichuan. Designed for real-world medical reasoning tasks, this model builds upon Qwen2.5-32B with an innovative Large Verifier System. Through domain-specific fine-tuning on real-world medical questions, it achieves breakthrough medical performance while maintaining strong general capabilities.
Model Features:
Baichuan-M2 incorporates three core technical innovations: First, through the Large Verifier System , it combines medical scenario characteristics to design a comprehensive medical verification framework, including patient simulators and multi-dimensional verification mechanisms; second, through medical domain adaptation enhancement via Mid-Training, it achieves lightweight and efficient medical domain adaptation while preserving general capabilities; finally, it employs a multi-stage reinforcement learning strategy, decomposing complex RL tasks into hierarchical training stages to progressively enhance the model's medical knowledge, reasoning, and patient interaction capabilities.
Core Highlights:
- 🏆 World's Leading Open-Source Medical Model : Outperforms all open-source models and many proprietary models on HealthBench, achieving medical capabilities closest to GPT-5
- 🧠 Doctor-Thinking Alignment : Trained on real clinical cases and patient simulators, with clinical diagnostic thinking and robust patient interaction capabilities
- ⚡ Efficient Deployment : Supports 4-bit quantization for single-RTX4090 deployment, with 58.5% higher token throughput in MTP version for single-user scenarios

## 📊 Performance Metrics

### HealthBench Scores

### General Performance

Note: AIME uses max_tokens=64k, others use 32k; temperature=0.6 for all tests.

## 🔧 Technical Features

📗 Technical Blog : Blog - Baichuan-M2
📑 Technical Report : Arxiv - Baichuan-M2

### Large Verifier System

- Patient Simulator : Virtual patient system based on real clinical cases
- Multi-Dimensional Verification : 8 dimensions including medical accuracy, response completeness, and follow-up awareness
- Dynamic Scoring : Real-time generation of adaptive evaluation criteria for complex clinical scenarios

### Medical Domain Adaptation

- Mid-Training : Medical knowledge injection while preserving general capabilities
- Reinforcement Learning : Multi-stage RL strategy optimization
- General-Specialized Balance : Carefully balanced medical, general, and mathematical composite training data

## ⚙️ Quick Start

For deployment, you can use sglang>=0.4.6.post1 or vllm>=0.9.0 or to create an OpenAI-compatible API endpoint:
- SGLang: python -m sglang.launch_server --model-path baichuan-inc/Baichuan-M2-32B --reasoning-parser qwen3
- vLLM: vllm serve baichuan-inc/Baichuan-M2-32B  --reasoning-parser qwen3

## MTP inference with SGLang

- Replace the qwen2.py file in the sglang installation directory with draft/qwen2.py.
- Launch sglang:

## ⚠️ Usage Notices

- Medical Disclaimer : For research and reference only; cannot replace professional medical diagnosis or treatment
- Intended Use Cases : Medical education, health consultation, clinical decision support
- Safe Use : Recommended under guidance of medical professionals

## 📄 License

Licensed under the Apache License 2.0 . Research and commercial use permitted.

## 🤝 Acknowledgements

- Base Model: Qwen2.5-32B
- Training Framework: verl
- Inference Engines: vLLM, SGLang
- Quantization: AutoRound, GPTQ
Thank you to the open-source community. We commit to continuous contribution and advancement of healthcare AI.

## 📞 Contact Us

- Resources: Baichuan AI Website
- Technical Support: GitHub
[LINK: GitHub](https://github.com/baichuan-inc)
Empowering Healthcare with AI, Making Health Accessible to All

## Model tree for baichuan-inc/Baichuan-M2-32B

Base model

## Spaces using baichuan-inc/Baichuan-M2-32B 2

## Collection including baichuan-inc/Baichuan-M2-32B

## Paper for baichuan-inc/Baichuan-M2-32B

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
baichuan-inc/Baichuan-M2-32B is supported by the following Inference Providers:

--------------------