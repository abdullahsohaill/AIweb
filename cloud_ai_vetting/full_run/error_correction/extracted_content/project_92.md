# [project
**URL:** https://read-llm.github.io
**Page Title:** Efficient Multi-Agent LLM-based Planning: A Reinforced Approach
--------------------


## Efficient Multi-Agent LLM-based Planning: A Reinforced Approach

## Abstract

Grounding the reasoning ability of large language models (LLMs) on embodied agents is 
                  challenging due to the complexity of the physical world. Especially, LLM planning for
                  multi-agent collaboration requires communication of agents and credit assignment of 
                  total feedback. Thus existing methods relying on physical verification or self-reflection suffer from excessive querying of LLMs.
In this paper, we propose a novel framework for multi-agent collaboration that adopts Reinforced Advantage feedback (ReAd) for the self-refinement of plans. Specifically, 
                  we perform critic regression to learn a sequential advantage function from LLM-planned 
                  data, and then treat the LLM planner as an optimizer to generate actions that maximize 
                  the advantage function, which endows LLM with the foresight to discern whether the action 
                  contributes to accomplishing the final task.
We provide theoretical analysis by extending advantage-weighted regression in reinforcement 
                  learning to multi-agent systems. We adopt three multi-robot collaboration tasks with difficult 
                  variants in experiments. The results show that ReAd surpasses baselines in success rate, and
                  also significantly decreases the interaction steps of agents and query rounds of LLMs.

## Method

An overview of prompting and refinement. For each timestep t , the LLM planner is given the history which contains states, actions, 
                      and advantages, and prompted to generate a plan with the highest advantage. The pre-trained critic is used to evaluate the score of
                      the generated action S R e A d ( a t i ) . If S R e A d ( a t i ) < ϵ , the failed plan is used as a prompt, 
                      and the LLM planer is asked to refine the policy until the S R e A d ( a t i ) > ϵ . The (refined) action is used to interact 
                      with the environment, and the LLM planner is processed in the next step. In addition, we propose two different approaches called ReAd-S and ReAd-J . ReAd-S will require LLM to plan for each robot separately in a sequential decision 
                      manner, and ReAd-J will require LLM to generate planning results for all robots at once.

## Experiments Exhibition

We present Difficult Variants of RoCoBench (DV-RoCoBench) for embodied multi-robot collaboration, which is derived from RoCoBench.
                    Below we will show how ReAd-S , ReAd-J and RoCo work on the three most difficult tasks.
- Sweep Floor : There are some cubes on the table, and the two robots need to work together to sweep these cubes and dump them into the trash bin. Task Y3_G3 indicates that the current task only needs to sweep three yellow and three green cubes.
- Make Sandwich : There are some foods on the table, and the two robots must stack these foods in the exact order of the given recipe. Task recipe4 means the recipe length of the current task is 9, task recipe3 means the recipe length of the current task is 7.
- Sort Cubes : There are three cubes on the table, and the three robots need to work together to place these cubes in their corresponding target positions. Task sort5 indicates that there are two cubes in the current task whose distance from the target position is 3, and one cubes whose distance is 1.

## ReAd-S

## RoCo

## ReAct

## MindAgent

## Forced Coordination

Forced Coordination is a difficult task of Overcooked-AI . 
                    We will show the complete interaction between ReAd-J , MindAgent and Central Plan on this task.

### ReAd-J

### MindAgent

### Central Plan

## Experiments Using LLama-3.1-70B-Instruct

In addition, we use LLama-3.1-70B-Instruct to compare the performance of ReAd-J 、 ReAct 、 MindAgent 、 Reflexion and Central Planner .
                  Specifically, we set the temperature of the model to 0 and the top_p to 0.1, take the default values for the other parameters of the model.

### ReAd-J

## Robustness Experiments

In addition, we also designed robustness experiments to compare the robustness of ReAd-S and RoCo .
                  Specifically, we reset the state of the environment after a certain environment interaction, but do not clear the historical conversation information, 
                  in this setting we compare the performance of ReAd-S and RoCo when they complete the task. The setting of the example shown below is as follows: 
                  In task recipe3 , reset the environment state after fixing the second environment interaction .

### ReAd-S

### RoCo


--------------------