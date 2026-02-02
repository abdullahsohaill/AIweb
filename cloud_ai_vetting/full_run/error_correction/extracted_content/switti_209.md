# Switti
**URL:** https://yandex-research.github.io/switti
**Page Title:** Switti
--------------------


## Switti: Designing Scale-Wise Transformers for Text-to-Image Synthesis

[LINK: Code](https://github.com/yandex-research/switti)

## Abstract

This work presents Switti, a scale-wise transformer for text-to-image generation.
            We start by adapting an existing next-scale prediction autoregressive (AR) architecture to T2I generation, investigating and mitigating training stability issues in the process.
            Next, we argue that scale-wise transformers do not require causality and propose a non-causal counterpart facilitating ∼21% faster sampling and lower memory usage while also achieving slightly better generation quality.
            Furthermore, we reveal that classifier-free guidance at high-resolution scales is often unnecessary and can even degrade performance. 
            By disabling guidance at these scales, we achieve an additional sampling acceleration of ∼32% and improve the generation of fine-grained details. 
            Extensive human preference studies and automated evaluations show that Switti outperforms existing T2I AR models and competes with state-of-the-art T2I diffusion models while being up to 7× faster.

## Human evaluation

## Switti vs competing AR and diffusion-based models.

## Inference performance evaluation

## Comparison of models' 1024×1024 image generation time.

## Automated Metrics

## Quantitative comparison of Switti to competing AR and diffusion-based models. The best model is highlighted in red , the second-best in blue , and the third-best in yellow according to the respective automated metric.

The best model is highlighted in red , the second-best in blue , and the third-best in yellow according to the respective automated metric.

## BibTeX


--------------------