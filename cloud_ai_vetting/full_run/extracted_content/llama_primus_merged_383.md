# Llama-Primus-Merged
**URL:** https://huggingface.co/trendmicro-ailab/Llama-Primus-Merged
**Page Title:** trendmicro-ailab/Llama-Primus-Merged · Hugging Face
--------------------


## Primus: A Pioneering Collection of Open-Source Datasets for Cybersecurity LLM Training

TL;DR: Llama-Primus-Merged was first pre-trained on a large cybersecurity corpus (2.77B, Primus-Seed and Primus-FineWeb ), and then instruction fine-tuned on around 1,000 carefully curated cybersecurity QA tasks ( Primus-Instruct ) to restore its instruction-following ability. Finally, it was merged with Llama-3.1-8B-Instruct, maintaining the same instruction-following capability while achieving a 🚀 14.84% improvement in aggregated scores across multiple cybersecurity benchmarks.
🔥 For more details, please refer to the paper: [📄Paper] .

## Introduction

Large Language Models (LLMs) have demonstrated remarkable versatility in recent years, with promising applications in specialized domains such as finance, law, and biomedicine. However, in the domain of cybersecurity, we noticed a lack of open-source datasets specifically designed for LLM pre-training—even though much research has shown that LLMs acquire their knowledge during pre-training.  To fill this gap, we present a collection of datasets covering multiple stages of cybersecurity LLM training, including pre-training ( Primus-Seed and Primus-FineWeb ), instruction fine-tuning ( Primus-Instruct ), and reasoning data for distillation ( Primus-Reasoning ).  Based on these datasets and Llama-3.1-8B-Instruct, we developed Llama-Primus-Base , Llama-Primus-Merged , and Llama-Primus-Reasoning . This model card is Llama-Primus-Merged .
Note: No TrendMicro customer information is included.

## Benchmark Results

- Cybersecurity
- Function Calling
- Safety & Toxicity
- Multilingual
- General Chat Performance
- Long-Context
CTI-Bench(CVSS) is scored using Mean Absolute Deviation ( lower is better ), CTI-ATE uses F1 score, and the others use accuracy. The aggregate score ( Agg. ) is the sum of all benchmarks, with CTI-Bench(CVSS) negated.
References:
- CyberMetric : CyberMetric: A Benchmark Dataset based on Retrieval-Augmented...
- CTI-Bench : CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence
- SecEval : SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knowledge of Foundation Models
[LINK: SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knowledge of Foundation Models](https://xuanwuai.github.io/SecEval/)
Reference:
- BFCL (V2)

### Safety & Toxicity

References:
- Garak : Garak Repository
[LINK: Garak Repository](https://github.com/leondz/garak)
- XSTest : XSTest Repository
[LINK: XSTest Repository](https://github.com/paul-rottger/exaggerated-safety)

### Multilingual

References:
- English : MMLU Dataset
- German/French : MLMM Evaluation
[LINK: MLMM Evaluation](https://github.com/nlp-uoregon/mlmm-evaluation?tab=readme-ov-file)
- Japanese : Freedom Intelligence MMLU Japanese
Reference:
- MT Bench

### Long-Context

Reference:
- LongBench

## About Primus

Primus is Trend Micro's pioneering family of lightweight, state-of-the-art open cybersecurity language models and datasets. Developed through our cutting-edge research initiatives and advanced technology, these resources share the innovative foundation that powers our enterprise-class Trend Cybertron solution. As an industry leader in cybersecurity, Trend Micro is proud to contribute these powerful, efficiency-optimized models and datasets to the community, while maintaining the excellence and reliability that define our global security standards.

## License

This model is based on the MIT license, but you must also comply with the Llama 3.1 Community License Agreement.

## Model tree for trendmicro-ailab/Llama-Primus-Merged

Base model

## Datasets used to train trendmicro-ailab/Llama-Primus-Merged

## Space using trendmicro-ailab/Llama-Primus-Merged 1

## Collection including trendmicro-ailab/Llama-Primus-Merged

## Papers for trendmicro-ailab/Llama-Primus-Merged


--------------------