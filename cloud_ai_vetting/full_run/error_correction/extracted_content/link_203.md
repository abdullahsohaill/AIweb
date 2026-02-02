# [link]
**URL:** https://x-humanoid-robomind.github.io
**Page Title:** RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation
--------------------


## RoboMIND: Benchmark on Multi-embodiment
              Intelligence Normative Data for Robot Manipulation

(hover to display full author list)
2 State Key Laboratory of Multimedia Information Processing, School of Computer Science, Peking University,
[LINK: Github](https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io)

## We introduce RoboMIND , a benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation, comprising 107k real-world demonstration trajectories across 4 embodiments, 479 diverse tasks and 96 distinct object classes.

## Abstract

Developing robust and general-purpose manipulation policies is a key goal in robotics. To achieve effective
              generalization, it is essential to construct comprehensive datasets
              that encompass a large number of demonstration trajectories
              and diverse tasks. While existing works have focused on assembling various
              individual robot datasets, there is still a lack of a unified data collection standard and insufficient high-quality data across diverse
              tasks, scenarios, and robot types. In this paper, we introduce
              RoboMIND (Multi-embodiment Intelligence Normative Data for
              Robot Manipulation), a dataset containing 107k demonstration
              trajectories across 479 diverse tasks involving 96 object classes.
              RoboMIND is collected through human teleoperation and encompasses comprehensive robotic-related information, including
              multi-view observations, proprioceptive robot state information,
              and linguistic task descriptions. To ensure data consistency and
              reliability for imitation learning, RoboMIND is built on a unified
              data collection platform and a standardized protocol, covering
              four distinct robotic embodiments: the Franka Emika Panda,
              the UR5e, the AgileX dual-arm robot, and a humanoid robot
              with dual dexterous hands. Our dataset also includes 5k real-
              world failure demonstrations, each accompanied by detailed
              causes, enabling failure reflection and correction during policy
              learning. Additionally, we created a digital twin environment
              in the Isaac Sim simulator, replicating the real-world tasks
              and assets, which facilitates the low-cost collection of additional
              training data and enables efficient evaluation. To demonstrate
              the quality and diversity of our dataset, we conducted extensive
              experiments using various imitation learning methods for single-task settings and state-of-the-art Vision-Language-Action (VLA)
              models for multi-task scenarios. By leveraging RoboMIND, the
              VLA models achieved high manipulation success rates and
              demonstrated strong generalization capabilities. To the best of
              our knowledge, RoboMIND is the largest multi-embodiment
              teleoperation dataset collected on a unified platform, providing
              large-scale and high-quality robotic training data.

## Hardware Setup

Here are some examples of the hardware setup for data collection, which is also the hardware setup we used to establish our real-world experiments. For the Franka Emika Panda robots, we use cameras positioned at the top, left, and right viewpoints to record the visual information of the task trajectories. For the AgileX/Tien Kung robots, we use their built-in cameras to record visual information. For UR robots, we use an external top camera. All demonstrations are collected using high-quality human teleoperation and stored on a unified intelligence platform.

## RoboMIND Data Analysis

Dataset Overview . (a) the total trajectory numbers categorized by different types of robots, (b) average trajectory lengths (frames) categorized by different types of robots, (c) trajectory ratio of different task categories (Artic. M.: Articulated Manipulations; Coord. M.: Coordination Manipulations; Basic M.: Basic Manipulations; Obj. Int.: Multiple Object Interactions; Precision M.: Precision Manipulations; Scene U.: Scene Understanding), and (d) trajectory ratio of different scenarios.
Distribution of objects in RoboMIND, categorized as domestic, industrial, kitchen, office, and retail.
Left : Skill number distribution histogram across tasks for each embodiment. We observe that over 70% of the Franka tasks involve only a single skill, while over 75% of the Tien Kung and AgileX tasks involve two or more skills, indicating that these dual-arm tasks are mostly long-horizon tasks. Right : We visualize the AX-PutCarrot task with the AgileX robot, which involves three different skills.
Language Description Annotation . We provide refined linguistic annotations for 10,000 successful robot motion trajectories. The video of the robotic arm placing the apple in the drawer is divided into six segments using Gemini. The language descriptions provided for each segment were initially generated by Gemini and subsequently refined through manual revision.
Visualization of failed data collection cases . We present two examples of failure from Franka and AgileX. In the FR-PlacePlateInPlateRack task (second row), the Franka arm fails to align with the slot, causing the plate to slip due to operator interference. In the AX-PutCarrot task (fourth row), the AgileX gripper unexpectedly opens, dropping the carrot. These failure cases were filtered out during quality inspection to maintain dataset quality.

## Experiments

We conduct comprehensive experiments employing four popular imitation learning methods, including ACT, Diffusion Policy,
        BAKU, RDT-1B, Crossformer and OpenVLA on selected RoboMIND tasks to assess their performance and limitations.

### Success Examples of ACT on Single Tasks

FR-PlacePearBowl
FR-SideCloseDrawer
FR-PlaceBluePink
HR-OpenTrashBin
HR-CloseTrashBin
HR-OpenDrawerLowerCabinet
AX-AppleYellowPlate
AX-CarrotGreenPlate
AX-UnpackBowl
UR-CloseTopWhiteDrawer
UR-PickRoundBread
AX-PackPlate

### Success Examples of RDT-1B Finetuned on Multi-task Setting

AX-AppleBluePlate
AX-PackBowl
AX-TakePotato

### Success Examples of OpenVLA Finetuned on Multi-task Setting

FR-OpenCapLid
FR-PickStrawberryInBowl
FR-SlideCloseDrawer
For more details on data analysis and experiment results, please refer to our paper . For technical questions or any other inquiries, please file a bug at the github repo .
[LINK: the github repo](https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io)

## BibTeX


--------------------