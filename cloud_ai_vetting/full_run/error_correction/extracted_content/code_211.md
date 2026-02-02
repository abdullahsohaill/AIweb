# Code
**URL:** https://yanqval.github.io/PAE
**Page Title:** Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery for Foundation Model Internet Agents
--------------------


## Proposer-Agent-Evaluator (PAE) : Autonomous Skill Discovery for Foundation Model Internet Agents

[LINK: Yifei Zhou* 1](https://yifeizhou02.github.io/)
- Paper
- Code
[LINK: Code](https://github.com/amazon-science/PAE)

### Abstract

The vision of a broadly capable and goal-directed agent, such as an Internet-browsing agent in the digital world and a household humanoid in the physical world, has rapidly advanced, thanks to the generalization capability of foundation models. Such a generalist agent needs to have a large and diverse skill repertoire, such as finding directions between two travel locations and buying specific items from the Internet. If each skill needs to be specified manually through a fixed set of human-annotated instructions, the agent's skill repertoire will necessarily be limited due to the quantity and diversity of human-annotated instructions. In this work, we address this challenge by proposing Proposer-Agent-Evaluator (PAE), a complete working system that enables foundation model agents to autonomously discover and practice skills in the wild. At the heart of PAE is a context-aware task proposer that autonomously proposes tasks for the agent to practice with context information of the environment such as user demos or even just the name of the website itself for Internet-browsing agents. Then, the agent policy attempts those tasks with thoughts and actual grounded operations in the real world with resulting trajectories evaluated by an autonomous model-based success evaluator. The success evaluation serves as the reward signal for the agent to refine its policies through RL. We validate PAE on challenging vision-based web navigation, using both real-world and self-hosted websites from WebVoyager and WebArena. Our results show that PAE significantly improves the zero-shot generalization capability of VLM Internet agents (more than 30\% relative improvement) to both unseen tasks and websites. Our model also achieves an absolute advantage of over 10% (from 22.6% to 33.0%) comparing to other state-of-the-art open source VLM agents including Qwen2VL-72B. To the best of our knowledge, this work represents the first working system to apply autonomous task proposal with RL for agents that generalizes real-world human-annotated benchmarks with SOTA performances.

### Methodology

PAE is built with the awareness of the asymmetric capabilities of SOTA VLMs as task proposers/ evaluators and as agents. Our design 
		enables foundation model agents to autonomously discover and practice new skills by identifying the interesting tasks with a task proposer , 
		trying them with an agent policy , and performing an online RL loop based on the reward provided by an autonomous evaluator .
- Context-aware task proposer : in order to generate a diverse set of feasible tasks, we frame task proposing as a conditional auto-regressive generation based on the context information of the websites. Tasks are proposed prior to online RL training.
- Image-based outcome evaluator : to take full advantage of the asymmetric capability of SOTA VLMs as agents and as evaluators, we find it most robust for the autonomous evaluators to complete the easiest evaluation: evaluating the success of the final outcome based on the final three screenshots and the agents' final answers to provide only 0/1 response in the end.
- Chain-of-thought agent policy : to enable generalization to unseen evaluation tasks, we incorporate an additional reasoning step to outputs the agent's chain-of-thought before the actual web operation. This reasoning step is optimized with the RL algorithm just like the actual web operation. Our experiments are carried out using the simplest online RL algorithm: Filtered BC.

### Main Results on Webvoyager

We compare our generalist VLM web agent on the WebVoyager navigation benchmark on real-time commertial  websites. Task success rate is reported. We found PAE can effectively improve both the 7B and 34B model over their SFT checkpoints, resulting in 50% relative improvements in both cases. 
		Notably, our LLaVa-34B PAE (https://huggingface.co/yifeizhou/pae-llava-34b) has surpasses the prior best open-source Qwen2VL-72B by more than 10% (33.0% compared to 22.6%), establishing a new state-of-the-art for generalist VLM web agent.

### Main Results on WebArena Easy

To enhance reproducibility of our experiments, we also report the comparison results on another realistic sandboxed web navigation benchmark WebArena Easy, a simplified task set from WebArena.
		    Again, we observe a similar improvement of PAE compared to the SFT checkpoint, and surpassing the prior state-of-the-art Qwen2VL-72B despite 10x smaller in size.

### Comparison

We present two qualitative comparisons between the behavior of the SFT checkpoint and the checkpoint after PAE training. In both cases, we observe qualitative evidence of PAE teaching the agent a diverse repertoire to effectively complete unseen tasks.

### Failure Mode Analysis

To understand where the improvement of PAE comes from, we conducted a user study to analyze different error types across various models. Comparing the SFT checkpoint and the PAE checkpoint, we found that PAE can effectively both reduce visual hallucinations and enrich the skill repertoire with low-level web navigation skills, thereby reducing the low-level skill missing error.

### Citation

### Acknowledgements

We thank you and the other visitors for visiting our project page.

--------------------