# **ICLR 2023**] [[**Project page**
**URL:** https://prior.allenai.org/projects/action-adaptive-policy
**Page Title:** Perceptual Reasoning and Interaction Research - Moving Forward by Moving Backward: Embedding Action Impact over Action Semantics
--------------------


## Moving Forward by Moving Backward: Embedding Action Impact over Action Semantics

## Action Adaptive Policy

A common assumption when training embodied agents is that the impact of taking an action is stable; for instance, executing the “move ahead” action will always move the agent forward by a fixed distance, perhaps with some small amount of actuator-induced noise. This assumption is limiting; an agent may encounter settings that dramatically alter the impact of actions: a move ahead action on a wet floor may send the agent twice as far as it expects and using the same action with a broken wheel might transform the expected translation into a rotation. Instead of relying that the impact of an action stably reflects its pre-defined semantic meaning, we propose to model the impact of actions on-the-fly using latent embeddings. By combining these latent action embeddings with a novel, transformer-based, policy head, we design an Action Adaptive Policy (AAP). We evaluate our AAP on two challenging visual navigation tasks in the AI2-THOR and Habitat environments and show that our AAP is highly performant even when faced, at inference-time with missing actions and, previously unseen, perturbed action space. Moreover, we observe significant improvement in robustness against these actions when evaluating in real-world scenarios.

## Video

## Code

- Source Code
[LINK: Source Code](https://github.com/KuoHaoZeng/AAP)

## Paper

### Moving Forward by Moving Backward: Embedding Action Impact over Action Semantics

- PDF View PDF
- Github View on Github
[LINK: Github](https://github.com/KuoHaoZeng/AAP)

--------------------