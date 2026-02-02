# [Project page
**URL:** https://worv-ai.github.io/d2e
**Page Title:** D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI
--------------------


## D2E: Scaling Vision-Action Pretraining on Desktop Data
                            for Transfer to Embodied AI

[LINK: Jaeyoon Jung](https://lastdefiance20.github.io/)
[LINK: Haebin Seong](https://hbseong97.github.io/)
[LINK: Youngjae Yu](https://yj-yu.github.io/home/)
[LINK: Code](https://github.com/worv-ai/D2E)
Overview of D2E (Desktop to Embodied AI) framework. (1) The OWA Toolkit captures 335.6 hours of rich
                    desktop demonstrations across 31 games with 152× compression. (2) The Generalist-IDM uses nextevent
                    prediction with temporal offset (NEP-τ) to achieve OOD generalization, enabling pseudolabeling of
                    1K+ hours of YouTube gameplay. (3) Vision-Action Pretraining transfers desktoppretrained
                    representations to embodied AI, achieving 96.6% success on LIBERO manipulation and
                    83.3% on CANVAS navigation benchmarks which demonstrates desktop-to-robotics transfer.

## Pseudo-Label result on YouTube dataset

Brotato
CSGO2
Stardew Valley
Minecraft
Slime Rancher
Raft
Barony
Dinkum
Generalist-IDM uses a single model to label actions on video-only
                        data, across 2D/3D games and visual navigation/UI interactions without separate processing. Remarkably, in Counter-Strike videos where spectator mode begins around 10 seconds,
                        it can distinguish between active gameplay and spectator mode by recognizing subtle UI elements,
                        avoiding action predictions during spectator phases.

## Abstract

Large language models leverage internet-scale text data, yet embodied AI remains constrained
                            by the prohibitive costs of physical trajectory collection. Desktop
                            environments---particularly gaming---offer a compelling alternative: they provide rich
                            sensorimotor interactions at scale while maintaining the structured observation-action
                            coupling essential for embodied learning. We present D2E (Desktop to Embodied AI), a
                            framework that demonstrates desktop interactions can serve as an effective pretraining
                            substrate for robotics embodied AI tasks. Unlike prior work that remained domain-specific
                            (e.g., VPT for Minecraft) or kept data proprietary (e.g., SIMA), D2E establishes a complete
                            pipeline from scalable desktop data collection to verified transfer in embodied domains. Our
                            framework comprises three components: (1) the OWA Toolkit that unifies diverse desktop
                            interactions into a standardized format with 152× compression, (2) the Generalist-IDM that
                            achieves strong zero-shot generalization across unseen games through timestamp-based event
                            prediction, enabling internet-scale pseudo-labeling, and (3) VAPT that transfers
                            desktop-pretrained representations to physical manipulation and navigation. Using 1.3K+
                            hours of data (259 hours of human demonstrations, and 1K+ hours of pseudo-labeled gameplay),
                            we achieve a total of 96.6% success rate on LIBERO manipulation and 83.3% on CANVAS
                            navigation benchmarks. This validates that sensorimotor primitives in digital interactions
                            exhibit sufficient invariance to transfer meaningfully to physical embodied tasks,
                            establishing desktop pretraining as a practical paradigm for robotics. We will make all our
                            work public, including the OWA toolkit, datasets of human-collected and pseudo-labeled, and
                            VAPT-trained models.

## Generalist Inverse Dynamics Model (G-IDM)

The Generalist Inverse Dynamics Model (G-IDM) learns to predict actions from observation
                            transitions across diverse desktop environments.
                            This enables zero-shot generalization to unseen games and provides a foundation for
                            pseudo-labeling large-scale gameplay data.
Ground Truth
IDM
G-IDM
Ground Truth
IDM
G-IDM

## Out-of-Distribution Generalization

G-IDM demonstrates strong out-of-distribution generalization capabilities, successfully
                            transferring learned sensorimotor patterns
                            from desktop gaming environments to completely unseen game domains and interaction
                            modalities.
Ground Truth
IDM (Fine Tune)
G-IDM (Zero Shot)
G-IDM (Few Shot)
G-IDM (Fine Tune)
In Battlefield 6, for G-IDM (Zero Shot) we can observe that scale of mouse movement is
                            different with GT,
                            but we can observe that scale of movement remain nearly same for G-IDM (Few Shot).
                            This improvement occurs because providing context examples helps the model calibrate the
                            appropriate movement scale.
Ground Truth
IDM (Fine Tune)
G-IDM (Zero Shot)
G-IDM (Few Shot)
G-IDM (Fine Tune)

## Desktop-to-Embodied Transfer

To validate the effectiveness of desktop pretraining for embodied AI, we evaluate our
                            approach on two challenging downstream tasks: LIBERO manipulation and CANVAS navigation . These
                            benchmarks represent diverse embodied scenarios
                            requiring different sensorimotor skills - precise object manipulation and spatial navigation
                            respectively.
                            Our Vision-Action Pretraining (VAPT) framework transfers desktop-pretrained representations
                            to these physical domains,
                            demonstrating that sensorimotor patterns learned from gaming environments can generalize to
                            real-world robotic tasks.

## LIBERO Manipulation Results

D2E achieves impressive results on LIBERO manipulation benchmarks, demonstrating that
                            desktop-pretrained models
                            can effectively transfer to physical robotic manipulation tasks with a 96.6% success rate.
Baseline (42%)
+ VAPT w/o pseudo (98%)
+ VAPT w/ pseudo (100%)
Baseline (36%)
+ VAPT w/o pseudo (88%)
+ VAPT w/ pseudo (90%)
Baseline (10%)
+ VAPT w/o pseudo (88%)
+ VAPT w/ pseudo (46%)

## CANVAS Navigation Results

The framework also excels in navigation tasks, achieving 83.3% success rate
                            on CANVAS navigation benchmarks,
                            validating the transferability of desktop sensorimotor patterns to embodied navigation
                            scenarios.
Baseline (fail)
+ VAPT w/ pseudo (success)
Baseline (fail)
+ VAPT w/ pseudo (success)

## BibTeX

[LINK: general-navigation-models](https://github.com/general-navigation-models/general-navigation-models.github.io)
[LINK: Nerfies](https://nerfies.github.io)

--------------------