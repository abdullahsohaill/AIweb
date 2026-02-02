# VIMA
**URL:** https://vimalabs.github.io
**Page Title:** VIMA | General Robot Manipulation with Multimodal Prompts
--------------------


## VIMA: General Robot Manipulation with Multimodal
                        Prompts

### ICML 2023

[LINK: Zichen "Charles" Zhang](https://zcczhang.github.io/)
[LINK: Code](https://github.com/vimalabs/VIMA)
[LINK: Models](https://github.com/vimalabs/VIMA#pretrained-models)
[LINK: Benchmark](https://github.com/vimalabs/VimaBench)

## Abstract

Prompt-based learning has emerged as a successful paradigm in natural language processing, where
                        a single general-purpose language model can be instructed to perform any task specified by input
                        prompts. Yet task specification in robotics comes in various forms, such as imitating one-shot
                        demonstrations, following language instructions, and reaching visual goals. They are often
                        considered different tasks and tackled by specialized models. We show that a wide spectrum of
                        robot manipulation tasks can be expressed with multimodal prompts , interleaving textual
                        and visual tokens. Accordingly, we develop a new simulation benchmark that consists of thousands
                        of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for
                        imitation learning, and a four-level evaluation protocol for systematic generalization. We
                        design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor
                        actions autoregressively. VIMA features a recipe that achieves strong model scalability and data
                        efficiency. It outperforms alternative designs in the hardest zero-shot generalization setting
                        by up to 2.9x task success rate given the same training data. With 10x less training data, VIMA
                        still performs 2.7x better than the best competing variant.

## VIMA: Visuomotor Attention Agent

## VIMA-Bench: Benchmark for Multimodal Robot Learning

### Simple Object Manipulation

### Visual Goal Reaching

### Novel Concept Grounding

### One-shot Video Imitation

### Visual Constraint Satisfaction

### Visual Reasoning

## Experiments

We answer three main questions during experiments:
- 1. What is the best recipe for building multi-task transformer-based robot agents with
                            multimodal prompts?
- 2. What are the scaling properties of our approach in
                            model capacity and data size?
- 3. How do different components, such as visual tokenizers, prompt conditioning, and prompt
                            encoding, affect robot performance?

### Evaluation Results

### Ablation Studies

## Conclusion

In this work, we introduce a novel multimodal prompting formulation that converts diverse
                        robot manipulation tasks into a uniform sequence modeling problem. We instantiate this
                        formulation in VIMA-Bench, a diverse benchmark with multimodal tasks and systematic evaluation
                        protocols for generalization. We propose VIMA, a conceptually simple transformer-based agent
                        capable of solving tasks such as visual goal reaching, one-shot video imitation, and novel
                        concept grounding with a single model. Through comprehensive experiments, we show that VIMA
                        exhibits strong model scalability and zero-shot generalization. Therefore, we recommend our
                        agent design as a solid starting point for future work.

## BibTeX


--------------------