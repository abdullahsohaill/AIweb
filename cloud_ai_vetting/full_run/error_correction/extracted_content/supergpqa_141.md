# SuperGPQA
**URL:** https://supergpqa.github.io
**Page Title:** super gpqa
--------------------


## SuperGPQA: Scaling LLM Evaluation across 285 Graduate Disciplines

## M-A-P

## ByteDance.Inc

## 2077AI

[LINK: Code](https://github.com/SuperGPQA/SuperGPQA)

## Introduction

We introduce SuperGPQA, a comprehensive benchmark designed to evaluate the knowledge and reasoning abilities of Large Language Models (LLMs) across 285 graduate-level disciplines . SuperGPQA features at least 50 questions per discipline , covering a broad spectrum of graduate-level topics, and is designed to be a challenging frontier for LLM evaluation. SuperGPQA pushes the boundaries beyond common knowledge domains and reveals key insights into LLM performance, such as the importance of reasoning abilities, the benefits of instruction tuning, and the correlation between model power and balanced performance across varying difficulty levels. Top performing LLMs currently achieve scores around 60 on SuperGPQA, highlighting the benchmark's difficulty and its potential to drive future advancements in LLM research.

## Overview

SuperGPQA is a rigorous benchmark designed to evaluate Large Language Model (LLM) capabilities. Surpassing benchmarks like GPQA and MMLU-Pro in comprehensiveness, depth, and difficulty, SuperGPQA addresses the limitations of existing benchmarks that focus on common fields and neglect diverse, real-world professional disciplines. Covering specialized, rarely tested domains, SuperGPQA poses a significant challenge for state-of-the-art LLMs ( top models score ~60% ).
Comprehensiveness & Discrimination : SuperGPQA contains 26,529 questions across 13 disciplines, 72 fields, and 285 graduate-level disciplines, with at least 50 questions per discipline. This ensures accessibility and relevance to diverse real-world professional scenarios, including long-tail expertise often overlooked by other benchmarks. While STEM-heavy (77.2% of questions), this distribution results from rigorous curation. SuperGPQA effectively discriminates LLM performance across all domains, even with smaller non-STEM samples.
Difficulty : SuperGPQA exhibits varying difficulty levels across disciplines, with STEM fields showing a balanced distribution, non-STEM disciplines featuring more easy and medium questions, and 42.33% requiring calculations, aligning with its design rationale to use difficulty levels as diagnostic tools for dissecting complementary capabilities in modern LLMs.
Sentence Length : SuperGPQA features varied question lengths across disciplines, averaging 58.42 tokens, with extremes like Literature questions reaching 869 tokens and Engineering questions averaging 67.26 tokens. Notably, answer options are consistently sized across disciplines, averaging 12.86 tokens, a design choice that supports error option curation.
Semantic Visualization : t-SNE visualization shows discipline-specific clusters and cross-disciplinary overlaps. This highlights semantic relationships, capturing both domain-specific knowledge and cross-disciplinary connections.

## Statistics

SuperGPQA is a new, comprehensive benchmark designed to push the limits of Large Language Model (LLM) capabilities. Significantly larger and more detailed than existing benchmarks, EncycloBench contains 26,529 questions across 13 disciplines, 72 fields, and 285 subfields. The following table details the distribution of questions across the various disciplines included in SuperGPQA:

## Experiment Results

We evaluate 8 reasoning models, 41 chat models and 26 base models on SuperGPQA, which includes closed-source models, open-source models, and fully open-source models.

## BibTeX


--------------------