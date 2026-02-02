# [Source
**URL:** https://we-math.github.io
**Page Title:** We-Math
--------------------


## We-Math

## Does Your Large Multimodal Model Achieve Human-like Mathematical Reasoning?

[LINK: Code](https://github.com/We-Math/We-Math)
Overview diagram and the statistics of We-Math .
            The left and right side shows the first two layers of We-Math 's categories and information of different samples and terminal nodes.

## Introduction

Inspired by human-like mathematical reasoning, we introduce We-Math , 
             the first benchmark specifically designed to explore the problem-solving principles beyond the end-to-end performance.
We meticulously collect and categorize 6.5K visual math problems, 
            spanning 67 hierarchical knowledge concepts and 5 layers of knowledge granularity. 
            We firstly decompose composite problems into sub-problems according to the required knowledge concepts and introduce a novel four-dimensional metric, 
            namely Insufficient Knowledge (IK) , Inadequate Generalization (IG) , Complete Mastery (CM) , and Rote Memorization (RM) to hierarchically assess inherent issues in LMMs' reasoning process.
With We-Math , we conduct a thorough evaluation of existing LMMs
            in visual mathematical reasoning and reveal a negative correlation between solving
            step and problem-specific performance. We confirm the IK issue of LMMs can
            be effectively improved via knowledge augmentation strategy. More notably, the
            primary challenge of GPT-4o has significantly transitioned from IK to IG , establishing 
            it as the first LMM advancing towards the knowledge generalization stage.
            In contrast, other LMMs exhibit a marked inclination towards Rote Memorization they correctly solve composite problems involving multiple knowledge concepts,
            yet fail in answering sub-problems.
We anticipate that We-Math will open new
            pathways for advancements in visual mathematical reasoning for LMMs.
Overview of LMMs' performances on We-Math . Figures from left to right illustrates the
            (1) accuracy of different LMMs on various problem-solving steps, (2) the performance in different
            visual mathematics categories and (3) the result in knowledge based reasoning evaluation.

## We-Math Benchmark

## Overview

Different from existing benchmarks, We-Math is constructed around textbook knowledge units, 
            decomposing composite problem solutions into sub-problems based on the knowledge concepts. (1) Hierarchical Knowledge Structure. Strictly adheres to the knowledge presented in mathematics textbooks, 
            featuring a rigorous hierarchical and multi-category architecture. It
            ensures the independence of knowledge concepts within the same level, while establishing logical
            relationships among concepts at different hierarchical levels. (2) Knowledge based Reasoning Evaluation. To explore how LMMs solve
            problems. Drawing upon that humans tackle problems incrementally by leveraging fundamental
            knowledge concepts, we break down complex mathematical problems into more manageable sub105
            problems. Furthermore, we employ diverse measurement dimensions for meticulous evaluations. (3) Knowledge Concept Augmentation. To alleviate the inherent issues during the problem-solving
            process, we heuristically introduce descriptions for 67 knowledge concepts from Wikipedia and 
            textbooks, thereby providing essential knowledge support for the reasoning processes of LMMs.
The pipeline of knowledge-based data decomposition (an example of a two-step problem in We-Math ).
The pipeline of knowledge-based data decomposition (an example of a three-step problem in We-Math ).
The pipeline of knowledge-based data decomposition (an example of a two-step problem in We-Math ).
The pipeline of knowledge-based data decomposition (an example of a three-step problem in We-Math ).
The pipeline of knowledge-based data decomposition (an example of a two-step problem in We-Math ).
The pipeline of knowledge-based data decomposition (an example of a three-step problem in We-Math ).
The pipeline of knowledge-based data decomposition (an example of a two-step problem in We-Math ).

## Metric for Reasoning Evaluation

Based on the decomposed multi-step problems, we further reveal the inherent issues of LMMs in problem-solving process. 
            We feed both the M one-step sub-problems and the original problem into LMMs, 
            and classifying the responses into four categories 1. Insufficient Knowledge (IK) : Part of one-step problems contain errors, and the multi-step problem
            is wrong. It is reasonable because model's insufficient grasp of single knowledge concept may lead
            to errors in multi-step problem. 2. Inadequate Generalization (IG) : One-Step problems are all correct, but the multi-step problem is
            incorrect. This is also considered reasonable. While LMMs are capable of understanding individual
            knowledge concepts, they may struggle to generalize that knowledge to solve composite problems. 3. Complete Mastery (CM) : One-Step problems are all correct, and multi-step problem is also
            answered correctly. This result demonstrates that the model's results are both reliable and accurate. 4. Rote Memorization (RM) : One-Step problems contain errors, but the multi-step problem is
            answered correctly, which contradicts human logical thinking. If a model can solve composite
            multi-step problems but fails to answer the one-step problems needed in the process, it raises doubts
            about the model's reliability.
Diagram illustrating strict metric in three-step problem.
Diagram illustrating loose metric in three-step problem.
An example of the four-dimensional metrics for evaluating a two-step problem, using both loose and strict settings.
Diagram illustrating strict metric in three-step problem.
Diagram illustrating loose metric in three-step problem.
An example of the four-dimensional metrics for evaluating a two-step problem, using both loose and strict settings.
Diagram illustrating strict metric in three-step problem.
Diagram illustrating loose metric in three-step problem.
An example of the four-dimensional metrics for evaluating a two-step problem, using both loose and strict settings.

## Experiment Results

## Leaderboard on We-Math (testmini)

Accuracy scores on the testmini subset (1,740 examples) of We-Math .
More results can be found on the OpenCompass !
              We recommend using VLMEvalKit for evaluation, and adopting the Strict Score as the reported metric.
[LINK: VLMEvalKit](https://github.com/open-compass/VLMEvalKit/tree/main)
[LINK: Link](https://github.com/ByteDance-Seed/Seed1.5-VL)
[LINK: Link](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
[LINK: Link](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
🚨 To submit your results to the leaderboard, please send to this email with your result json files.

## Results on Existing Foundation Models

The performance of different LMMs on four-dimensional metrics under loose metric.
The Leaderboard of different LMMs under the strict and loose metric (average score %). 
                  ~ represents an approximate estimate of the total parameters nums in LMMs.
The visualization of different LMMs' performances on each category.
The performance of different LMMs on four-dimensional metrics under strict metric.
The performance of different LMMs on four-dimensional metrics under loose metric.
The Leaderboard of different LMMs under the strict and loose metric (average score %). 
                  ~ represents an approximate estimate of the total parameters nums in LMMs.
The visualization of different LMMs' performances on each category.
The performance of different LMMs on four-dimensional metrics under strict metric.
The performance of different LMMs on four-dimensional metrics under loose metric.
The Leaderboard of different LMMs under the strict and loose metric (average score %). 
                  ~ represents an approximate estimate of the total parameters nums in LMMs.
The visualization of different LMMs' performances on each category.

## Knowledge Card

The description of the knowledge concept "Understanding of Plane Figures".
The description of the knowledge concept "Understanding of Solid Figures".
The description of the knowledge concept "Angles and Length".
The description of the knowledge concept "Correspondence of Coordinates and Positions".
The description of the knowledge concept "Basic Transformations of Figures".
The description of the knowledge concept "Cutting and Combining of Figures".
The description of the knowledge concepts "Direction" and "Position".
The description of the knowledge concept "Route Map".
The description of the knowledge concept "Understanding and Conversion of Units".
The description of the knowledge concept "Calculation of Solid Figures".
The description of the knowledge concept "Calculation of Plane Figures".
The description of the knowledge concept "Understanding of Plane Figures".
The description of the knowledge concept "Understanding of Solid Figures".
The description of the knowledge concept "Angles and Length".
The description of the knowledge concept "Correspondence of Coordinates and Positions".
The description of the knowledge concept "Basic Transformations of Figures".
The description of the knowledge concept "Cutting and Combining of Figures".
The description of the knowledge concepts "Direction" and "Position".
The description of the knowledge concept "Route Map".
The description of the knowledge concept "Understanding and Conversion of Units".
The description of the knowledge concept "Calculation of Solid Figures".
The description of the knowledge concept "Calculation of Plane Figures".
The description of the knowledge concept "Understanding of Plane Figures".
The description of the knowledge concept "Understanding of Solid Figures".
The description of the knowledge concept "Angles and Length".

## BibTeX


--------------------