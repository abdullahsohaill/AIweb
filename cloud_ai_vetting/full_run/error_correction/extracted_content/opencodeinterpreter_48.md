# OpenCodeInterpreter
**URL:** https://opencodeinterpreter.github.io
**Page Title:** OpenCodeInterpreter
--------------------


## OpenCodeInterpreter

## Integrating Code Generation with Execution and Refinement

[LINK: Jie Fu 4](https://bigaidream.github.io/)
[LINK: Wenhu Chen 1 , 2](https://wenhuchen.github.io/)
[LINK: Xiang Yue* † , 1 , 5](https://xiangyue9607.github.io/)
[LINK: Code](https://github.com/OpenCodeInterpreter/OpenCodeInterpreter)
[LINK: 🏆 EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html)
Overview of the OpenCodeInterpreter and its pass@1 accuracy on the HumanEval. With appropriate feedback, OpenCodeInterpreter-DS-33B achieves performance comparable to that of the GPT-4 Code Interpreter.

## 🔔News

🏆[2024-03-13]: Our 33B model has claimed the top spot on the BigCode leaderboard !
💡[2024-03-01]: We have open-sourced OpenCodeInterpreter-SC2 series Model (based on StarCoder2 base)!
🛠️[2024-02-29]: Our official online demo is deployed on HuggingFace Spaces! Take a look at Demo Page !
🛠️[2024-02-28]: We have open-sourced the Demo Local Deployment Code with a Setup Guide.
[LINK: Demo Local Deployment Code](https://github.com/OpenCodeInterpreter/OpenCodeInterpreter/tree/main/demo)
✨[2024-02-26]: We have open-sourced the OpenCodeInterpreter-DS-1.3b Model.
📘[2024-02-26]: We have open-sourced the CodeFeedback-Filtered-Instruction Dataset.
🚀[2024-02-23]: We have open-sourced the datasets used in our project named Code-Feedback .
🔥[2024-02-19]: We have open-sourced all models  in the OpenCodeInterpreter series ! We welcome everyone to try out our models and look forward to your participation! 😆

## Introduction

The introduction of large language models has significantly advanced code generation. However, open-source models often lack the execution capabilities and iterative refinement of advanced systems like the GPT-4 Code Interpreter. To address this, we introduce OpenCodeInterpreter, a family of open-source code systems designed for generating, executing, and iteratively refining code. Supported by Code-Feedback, a dataset featuring 68K multi-turn interactions, OpenCodeInterpreter integrates execution and human feedback for dynamic code refinement. Our comprehensive evaluation of OpenCodeInterpreter across key benchmarks such as HumanEval, MBPP, and their enhanced versions from EvalPlus reveals its exceptional performance. Notably, OpenCodeInterpreter-33B achieves an accuracy of 83.2 (76.4) on the average (and plus versions) of HumanEval and MBPP, closely rivaling GPT-4's 84.2 (76.2) and further elevates to 91.6 (84.6) with synthesized human feedback from GPT-4. OpenCodeInterpreter brings the gap between open-source code generation models and proprietary systems like GPT-4 Code Interpreter.

## OpenCodeInterpreter

## Overview

Code generation has long been a cornerstone challenge in computer science, evolving significantly over the years from its initial reliance on symbolic methods to the recent revolutionary impact of large language models (LLMs). These LLMs, pre-trained on vast code corpora, have dramatically advanced the field by generating code that closely aligns with user intents, thereby offering substantial support for software development. As these models continue to evolve, they have become integral tools in automating and enhancing the coding process, exemplified by innovations such as GitHub Copilot.
To further enhance the capabilities of pre-trained code models, instruction-tuning methods have been introduced. Among these, OpenCodeInterpreter stands out as a pioneering approach, leveraging a unique dataset named Code-Feedback. This dataset comprises 68K multi-turn interactions that include both user instructions and compiler feedback, enabling the model to not only generate but also refine code based on execution outputs and human guidance. Such advancements allow OpenCodeInterpreter to produce solutions that are not only technically sound but also closely aligned with user expectations, setting a new standard in code generation.
OpenCodeInterpreter's innovative integration of execution and human feedback marks a significant leap forward in the domain. By harnessing compiler diagnostics to correct errors and incorporating human insights for code refinement, OpenCodeInterpreter achieves an unparalleled balance of accuracy and user alignment. Its performance on widely recognized benchmarks, including HumanEval and MBPP, demonstrates its superior ability to iteratively refine code, achieving results that narrow the performance gap with proprietary systems like GPT-4's Code Interpreter. OpenCodeInterpreter thus heralds a new era in code generation, offering open-source systems that rival the sophistication and efficacy of their proprietary counterparts.

## Code-Feedback

In the development of Code-Feedback, we meticulously crafted our dataset, known as Code-Feedback, to train the OpenCodeInterpreter, with a focus on specific criteria that ensure the dataset's effectiveness and relevance to real-world coding challenges. Code-Feedback is distinguished by its inclusion of diverse and challenging queries derived from actual coding tasks. This diversity is crucial, as it ensures that the dataset covers a broad spectrum of problems, providing both variety and complexity. Moreover, the dataset adopts a multi-turn dialogue structure, enhancing its utility by incorporating execution feedback, such as outputs and diagnostics from compilers, alongside human feedback, which includes additional guidance or instructions from users. This structure is pivotal in simulating real-world coding scenarios where iterative feedback and adjustments are common.
The creation of Code-Feedback involved a comprehensive approach, employing five distinct methods to gather and curate data. This multifaceted approach was designed to fulfill the dataset's three key criteria: the incorporation of diverse real-world queries, a structured multi-turn dialogue format, and the interleaving of text and code responses to offer a comprehensive solution to coding queries. The sources of our queries were twofold, comprising a variety of open-source datasets and coding challenges from platforms like LeetCode. This combination ensures a rich and varied dataset that accurately reflects the nature of coding tasks encountered by developers. In subsequent sections, we delve into the specific methods employed in constructing the dataset, illustrating our commitment to creating a robust and effective tool for coding instruction and feedback.
Summary of our proposed dataset OpenCodeInterpreter construction and comparison with existing code instruction tuning datasets. M.T: Multi Turn, E.F: Execute Feedback, H.F: Human Feedback.

## Main Results

This section outlines the experimental framework for evaluating the performance of OpenCodeInterpreter and its comparison with leading models in both single-turn and multi-turn code generation settings. The study leverages data from the EvalPlus leaderboard, examining OpenCodeInterpreter's performance against benchmarks such as GPT-3.5/4-Turbo, CodeLlama-Python, WizardCoder, Deepseek-Coder, and CodeT5+ across various scales on the HumanEval and MBPP benchmarks and their advanced versions. For multi-turn code generation, the focus shifts to assessing OpenCodeInterpreter's capability in iterative refinement through a two-round limit, considering execution feedback and human feedback scenarios. The experimental setup aims to highlight OpenCodeInterpreter's adaptability and proficiency in code generation, underscored by its achievements in setting new standards in software development tools through iterative feedback and refinement.
`CL': based on CodeLlama; `DS': based on DeepseekCoder. 
                Baseline results are copied from the EvalPlus Leaderboard or replicated by running the official checkpoints.

## Example

## BibTeX


--------------------