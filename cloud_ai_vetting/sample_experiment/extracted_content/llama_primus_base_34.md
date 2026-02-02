# Llama-Primus-Base
**URL:** https://huggingface.co/trendmicro-ailab/Llama-Primus-Base
**Page Title:** trendmicro-ailab/Llama-Primus-Base · Hugging Face
--------------------


## Primus: A Pioneering Collection of Open-Source Datasets for Cybersecurity LLM Training

TL;DR: Llama-Primus-Base is a foundation model based on Llama-3.1-8B-Instruct, continually pre-trained on Primus-Seed (0.2B) and Primus-FineWeb (2.57B). Primus-Seed is a high-quality, manually curated cybersecurity text dataset, while Primus-FineWeb consists of cybersecurity texts filtered from FineWeb, a refined version of Common Crawl. By pretraining on such a large-scale cybersecurity corpus, it achieves a 🚀 15.88% improvement in aggregated scores across multiple cybersecurity benchmarks, demonstrating the effectiveness of cybersecurity-specific pretraining.
🔥 For more details, please refer to the paper: [📄Paper] .

## Introduction

Large Language Models (LLMs) have demonstrated remarkable versatility in recent years, with promising applications in specialized domains such as finance, law, and biomedicine. However, in the domain of cybersecurity, we noticed a lack of open-source datasets specifically designed for LLM pre-training—even though much research has shown that LLMs acquire their knowledge during pre-training.  To fill this gap, we present a collection of datasets covering multiple stages of cybersecurity LLM training, including pre-training ( Primus-Seed and Primus-FineWeb ), instruction fine-tuning ( Primus-Instruct ), and reasoning data for distillation ( Primus-Reasoning ).  Based on these datasets and Llama-3.1-8B-Instruct, we developed Llama-Primus-Base , Llama-Primus-Merged , and Llama-Primus-Reasoning . This model card is Llama-Primus-Base .
Note: No TrendMicro customer information is included.

## Cybersecurity Benchmark Results

CTI-Bench (CVSS) is scored using Mean Absolute Deviation ( lower is better ), CTI-ATE uses F1 score, and the others use accuracy. The aggregate score ( Agg. ) is the sum of all benchmarks, with CTI-Bench (CVSS) negated.
References:
- CyberMetric : CyberMetric: A Benchmark Dataset based on Retrieval-Augmented...
- CtiBench : CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence
- SecEval : SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knowledge of Foundation Models
[LINK: SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knowledge of Foundation Models](https://xuanwuai.github.io/SecEval/)

## About Primus

Primus is Trend Micro's pioneering family of lightweight, state-of-the-art open cybersecurity language models and datasets. Developed through our cutting-edge research initiatives and advanced technology, these resources share the innovative foundation that powers our enterprise-class Trend Cybertron solution. As an industry leader in cybersecurity, Trend Micro is proud to contribute these powerful, efficiency-optimized models and datasets to the community, while maintaining the excellence and reliability that define our global security standards.

## License

This model is based on the MIT license, but you must also comply with the Llama 3.1 Community License Agreement.

## Model tree for trendmicro-ailab/Llama-Primus-Base

Base model

## Datasets used to train trendmicro-ailab/Llama-Primus-Base

## Collection including trendmicro-ailab/Llama-Primus-Base

## Papers for trendmicro-ailab/Llama-Primus-Base


--------------------