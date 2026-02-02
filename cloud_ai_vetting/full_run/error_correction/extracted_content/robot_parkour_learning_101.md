# Robot Parkour Learning
**URL:** https://robot-parkour.github.io
**Page Title:** Robot Parkour Learning
--------------------


## Robot Parkour Learning

[LINK: Ziwen Zhuang](https://ziwenzhuang.github.io/)
[LINK: Zipeng Fu](https://zipengfu.github.io/)
[LINK: Hang Zhao](https://hangzhaomit.github.io/)
[LINK: Code](https://github.com/ZiwenZhuang/parkour)

## Abstract

Parkour is a grand challenge for legged locomotion that requires robots to overcome various obstacles rapidly in complex environments. Existing methods can generate either diverse but blind locomotion skills or vision-based but specialized skills by using reference animal data or complex rewards. However, autonomous parkour requires robots to learn generalizable skills that are both vision-based and diverse to perceive and react to various scenarios. In this work, we propose a system for learning a single end-to-end vision-based parkour policy of diverse parkour skills using a simple reward without any reference motion data. We develop a reinforcement learning method inspired by direct collocation to generate parkour skills, including climbing over high obstacles, leaping over large gaps, crawling beneath low barriers, squeezing through thin slits, and running. We distill these skills into a single vision-based parkour policy and transfer it to a quadrupedal robot using its egocentric depth camera. We demonstrate that our system can empower two different low-cost robots to autonomously select and execute appropriate parkour skills to traverse challenging real-world environments.

## Climb

## Leap

## Crawl

## Tilt

## Emergent Re-trying Behaviors

Our parkour policy allows the robot to attempt overcoming an obstacle multiple times if it initially fails. The robot learns to push against the obstacle, ensuring adequate run-up space for subsequent attempts.

## Method

## Stage 1: RL Pre-training with Soft Dynamics Constraints

In the RL pre-training stage, we allow robots to penetrate obstacles using an automatic curriculum that enforces soft dynamics constraints. This encourages robots to gradually learn to overcome these obstacles while minimizing penetrations.

## Stage 2: RL Fine-tuning with Hard Dynamics Constraints

In the RL fine-tuning stage, we enforce all dynamics constraints and fine-tune the behaviors learned in the pre-training stage with realistic dynamics.

## Stage 3: Learning a Vision-Based Parkour Policy via Distillation

After each individual parkour skill is learned, we use DAgger to distill them into a single vision-based parkour policy that can be deployed to a legged robot using only onboard perception and computation power.

## Failure Cases

The robot fails to climb very high obstacles of 0.8m, three times the robot height.
The robot fails to leap on a low-friction platform. The rear legs slip during leaping leading to not much forward momentum for the robot to reach the other side.
The robot fails to climb a high and soft obstacle.

## BibTeX


--------------------