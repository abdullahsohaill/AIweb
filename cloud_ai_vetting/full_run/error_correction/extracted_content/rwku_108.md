# **RWKU**
**URL:** https://rwku-bench.github.io
**Page Title:** RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models
--------------------


## RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models

[LINK: Pengfei Cao](https://cpf-nlpr.github.io/)
[LINK: Code](https://github.com/jinzhuoran/RWKU)

## Summary

Large language models (LLMs) inevitably memorize sensitive, copyrighted, and harmful knowledge from the training corpus; therefore, it is crucial to erase this knowledge from the models.
Machine unlearning is a promising solution for efficiently removing specific knowledge by post hoc modifying models. In this paper, we propose a R eal- W orld K nowledge U nlearning benchmark ( RWKU ) for LLM unlearning.
RWKU is designed based on the following three key factors: (1) For the task setting , we consider a more practical and challenging unlearning setting, where neither the forget corpus nor the retain corpus is accessible.
(2) For the knowledge source , we choose 200 real-world famous people as the unlearning targets and show that such popular knowledge is widely present in various LLMs.
(3) For the evaluation framework , we design the forget set and the retain set to evaluate the model’s capabilities across various real-world applications.
Regarding the forget set, we provide four membership inference attack (MIA) methods and nine kinds of adversarial attack probes to rigorously test unlearning efficacy. Regarding the retain set, we assess locality and utility in terms of neighbor perturbation , general ability , reasoning ability , truthfulness , factuality , and fluency .
We conduct extensive experiments across two unlearning scenarios, two models and six baseline methods and obtain some meaningful findings.

## Evaluation Framework

## Benchmark Comparison

We provide a detailed comparison between existing unlearning benchmarks and RWKU.

## Data Collection and Construction

## Knowledge Source

A general unlearning benchmark should be applicable to various mainstream open-source LLMs.
This means ensuring that the knowledge to be forgotten is widely present in these models.
Therefore, we choose famous people as the unlearning targets, requiring the unlearning method to erase factual knowledge about the targets from the model without affecting the neighbor knowledge.

## Probe Construction

To construct the forget probes, we first use GPT-4 to generate an excess of query-answer pairs related to the unlearning targets.
Specifically, we collect relevant passages about each unlearning target from their Wikipedia pages and then prompt GPT-4 to generate query-answer pairs related to the targets based on these passages.

### Memorization Quantification

To further validate our collected unlearning targets, we quantify the memorization of various LLMs regarding knowledge from different sources. Higher EM and lower NLL indicate better memorization performance.
            We choose four different knowledge sources.

### Experimental Results

Results of our main experiment on LLaMA3-Instruct (8B) .
Results of our main experiment on Phi-3 Mini-4K-Instruct (3.8B) .

## Trade Off

We show the trade-off between unlearning efficacy,
locality and model utility in Figure below. (where trainable methods sample different training epochs and RepE samples different intervention weights).
A good unlearning method should be a straight line down from the top right to the bottom right.

## Adversarial Attack Types

Figure below illustrates the effectiveness of different types of adversarial attacks in inducing target knowledge from the model after forgetting.
We can observe that prefix injection, affirmative suffix, multiple choice and reverse query attacks effectively elicit unlearned knowledge from the model.
Because RT is fine-tuned on refusal data, it achieves the best unlearning efficiency under adversarial attacks.
NPO also demonstrates the potential to resist adversarial attacks.

## Batch-sample Unlearning

We also explore a particularly challenging unlearning scenario, involving the forgetting of multiple targets simultaneously.
As illustrated in Figures below, we conducted batch-unlearning experiments with target sizes of 10, 20, 30, 40, and 50.

## Partial-layer Unlearning

We conduct an interesting experiment to verify that updating the parameters in which layers can achieve more effective unlearning.

## BibTeX


--------------------