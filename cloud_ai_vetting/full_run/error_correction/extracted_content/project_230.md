# [Project
**URL:** https://zhoues.github.io/RoboRefer
**Page Title:** RoboRefer | Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics
--------------------


## RoboRefer: Towards Spatial Referring with Reasoning
                            in Vision-Language Models for Robotics

### NeurIPS 2025

[LINK: Enshen Zhou](https://zhoues.github.io/)
[LINK: Jingkun An](https://anjingkun.github.io/)
[LINK: Cheng Chi](https://chicheng123.github.io/)
[LINK: Yi Han](https://github.com/hany01rye)
[LINK: Shanyu Rong](https://rainfallsdown.github.io/)
[LINK: Chi Zhang](https://github.com/AibohDij)
[LINK: Lu Sheng](https://lucassheng.github.io/)
[LINK: Code](https://github.com/Zhoues/RoboRefer)

## Highlights

Highlights
- RoboRefer is the first 3D-aware VLM for multi-step spatial referring with explicit
                                reasoning.
- RoboRefer first acquires precise spatial
                                    understanding via SFT, and further exhibits generalized strong reasoning via RFT.
- To support SFT and RFT training, we introduce RefSpatial, a large-scale dataset of 20M QA pairs (2x prior) ,
                                covering 31 spatial relations ( vs. 15
                                    prior) and containing complex reasoning
                                    processes (up to 5 steps) .
- SFT-trained RoboRefer achieves SOTA
                                    spatial understanding , and RFT-trained RoboRefer exhibits generalizable spatial referring under novel spatial relation combinations.

## Motivation

Spatial referring in complex 3D environments
                            demands not only precise single-step spatial understanding but also multi-step spatial reasoning to resolve intricate references step-by-step, thereby enabling efficient control of diverse
                            robots (e.g. UR5 arm, G1 Humanoid) across tasks (e.g., manipulation, navigation).
Spatial Referring for Location via RoboRefer
Spatial Referring for Placement via RoboRefer

## Real-world Demos

These demos shows that RoboRefer can handle challenging long-horizon tasks
                    requiring complex multi-step spatial referring in cluttered and dynamic environments by integrating various control policies diverse robots (e.g., UR5, G1 humanoid).
System Stability
This video demonstrates the model's referential ability in color recognition and its stability in continuous operation.
Real-time Scene Adaptation
This video demonstrate the model's rapid scene adaptation ability and its capability to judge object proximity, recognize orientation, and determine distance.
Real-time Voice Interruption Adjustment
This video demonstrates the model's capabilities in object spatial relationship recognition, multi-step reasoning, rapid interactive reasoning, and real-time interruption adjustment.
Part-level Orientation-related Referring
This video demonstrates the model's capabilities in object spatial height recognition and part-level orientation-related region identification.
Functionality-oriented Referring
This video demonstrating the model's capabilities in object spatial height recognition and illuminated area identification.
Multi-step Spatial Referring with Reasoning
This video demonstrates the model's object spatial relationship recognition and multi-step spaital referring with reasoning capability.
Structured Arrangement
This video demonstrates the model's ability to understand spatial relationships and pattern reasoning between objects.
System Stability
This video demonstrates the model's referential ability in color recognition and its stability in continuous operation.

## Abstract

Spatial referring is a fundamental capability of embodied robots
                            to interact with the 3D physical world. However, even with the powerful pretrained
                            vision language models (VLMs), recent approaches are still not qualified to
                            accurately understand the complex 3D scenes and dynamically reason about the
                            instruction-indicated locations for interaction. To this end, we propose RoboRefer,
                            a 3D-aware VLM that can first achieve precise spatial understanding by integrating
                            a disentangled but dedicated depth encoder via supervised fine-tuning (SFT).
                            Moreover, RoboRefer advances generalized multi-step spatial reasoning via
                            reinforcement fine-tuning (RFT), with metric-sensitive process reward functions
                            tailored for spatial referring tasks. To support SFT and RFT training,
                            we introduce RefSpatial, a large-scale dataset of 20M QA pairs (2x prior),
                            covering 31 spatial relations (vs. 15 prior) and supporting complex
                            reasoning processes (up to 5 steps). In addition, we introduce RefSpatial-Bench,
                            a challenging benchmark filling the gap in evaluating spatial referring with
                            multi-step reasoning. Experiments show that SFT-trained RoboRefer achieves
                            state-of-the-art spatial understanding, with an average success rate of 89.6%.
                            RFT-trained RoboRefer further outperforms all other baselines by a large margin,
                            even surpassing Gemini-2.5-Pro by 12.4% in average accuracy on RefSpatial-Bench.
                            Notably, RoboRefer can be integrated with various control policies to execute
                            long-horizon, dynamic tasks across diverse robots (e,g., UR5, G1 humanoid)
                            in cluttered real-world scenes.

## Method Overview

Overview of RoboRefer . RoboRefer can perform single-step precise spatial
                            understanding
                            from RGB(D) inputs with spatially constrained instructions
                            ( enabled by the SFT stage introducing depth
                                    modality ),
                            and multi-step spatial referring with explicit reasoning
                            ( powered by the RFT stage and
                                    leveraging spatial understanding within each step learned in SFT ).

## Dataset Overview

RefSpatial is a comprehensive dataset including 2.5M data samples from 2D/3D/Simulated sources,
                            with 31 spatial relations.
                            RefSpatial's key features are: (1) Fine-Grained
                                    Annotations, (2) Multi-Dimensionality, (3) High Quality, (4) Large Scale,
                                    (5) Rich Diversity, (6) Easy Scalability .

## Open6DOR V2 Benchmark Demos in LIBERO

These demos shows that RoboRefer can be integrated into the system as a useful tool
                            for spatial referring to predict location and placement with spatial relations , which
                        is crucial for robots both in simulator and real-world scenes.
Task: Place the tissue box to the left of the
                                        wineglass
                                        on the table
Task: Place the wineglass to the right of the
                                        hard drive
                                        on the table.
Task: Place the cup in front of the spatula
                                        on the
                                        table.
Task: Place the cup behind the skillet on the
                                        table
Task: Place the skillet between the hard
                                        drive and the
                                        box on the table.
Task: Place the shoe at the center of all the
                                        objects on
                                        the table.

## Visualization of RefSpatial Dataset

we show more visualization of RefSpatial Dataset, which has 31
                            different spatial relations to enhance spatial understanding in SFT stage and advance multi-step spatial referring with reasoning in RFT
                        stage.

## RoboRefer's Prediction Visualization for Cluttered Tabletops.

we show more visualization of RoboRefer's prediction on a cluttered tabletop to demonstrate the strong generalizability on unseen
                        scenarios, tasks with novel spatial relation combinations, and objects .

## BibTeX


--------------------