# SAPIEN
**URL:** https://sapien.ucsd.edu
**Page Title:** SAPIEN
--------------------


## SAPIEN

## ManiSkill3 Benchmark Release

[LINK: SAPIEN Open-Source Manipulation Skill (ManiSkill) Benchmark](https://github.com/haosulab/ManiSkill)
- GPU parallelized visual data collection system for RGBD + Segmentation data at 20k FPS
- Example robots including quadruped, mobile manipulators, and single-arm robots
- Example tasks covering table-top, locomotion, and dextrous manipulation.
- Flexible unified task building API for GPU

## News

- 05/02/2024, SAPIEN 3 and ManiSkill 3 beta releases are available.
[LINK: SAPIEN 3](https://github.com/haosulab/SAPIEN/tree/3.0.0b1)
[LINK: ManiSkill 3](https://github.com/haosulab/ManiSkill)
- 02/10/2023, ManiSkill 2 , Colab tutorials , pip package and the associated challenge fully released with significant improvements on speed and quality.
[LINK: ManiSkill 2](https://maniskill2.github.io/)
[LINK: Colab tutorials](https://colab.research.google.com/github/haosulab/ManiSkill2/blob/main/examples/tutorials/1_quickstart.ipynb)
- 02/10/2023, SAPIEN 2.2 released with GPU-accelerated physics-grounded depth sensor and upgraded ray tracer .
[LINK: GPU-accelerated physics-grounded depth sensor](https://sapien.ucsd.edu/docs/2.2/tutorial/rendering/depth_sensor.html)
[LINK: ray tracer](https://sapien.ucsd.edu/docs/2.2/tutorial/rendering/raytracing_renderer.html)

## Features & Contents

### SAPIEN Simulator

SAPIEN simulator provides physical simulation for robots, rigidbody, and articulated objects. It powers reinforcement learning and robotics with its pure Python interface. It also provides multiple rendering modalities, including depth map, normal map, optical flow, active light, and ray tracing.

### PartNet-Mobility Dataset

PartNet-Mobility dataset is a collection of 2K articulated objects with motion annotations and rendernig material. The dataset powers research for generalizable computer vision and manipulation. The dataset is a continuation of ShapeNet and PartNet.

### Motion Planning Library

We recommend using mplib for motion planning with SAPIEN. mplib is a lightweight Python package that includes common functionalities for motion planning, including path planning, inverse kinematics, and collision avoidance.

## Quick Start

### Installation

### Source code

[LINK: https://github.com/haosulab/SAPIEN](https://github.com/haosulab/SAPIEN)
[LINK: https://github.com/haosulab/mplib](https://github.com/haosulab/mplib)

### Reinforcement Learning?

[LINK: tutorial](https://sapien-sim.github.io/docs/user_guide/rl/gym.html)

### 2D/3D Vision?

[LINK: tutorial](https://sapien-sim.github.io/docs/user_guide/rendering/camera.html)

### Robotics?

[LINK: robotics tutorial](https://sapien-sim.github.io/docs/user_guide/robotics/basic_robot.html)
[LINK: motion planning tutorial](https://motion-planning-lib.readthedocs.io/latest/index.html)

## Publication & Citation

SAPIEN is publised at CVPR 2020, the paper is available here . If you use SAPIEN and its assets, please cite the following works.

--------------------