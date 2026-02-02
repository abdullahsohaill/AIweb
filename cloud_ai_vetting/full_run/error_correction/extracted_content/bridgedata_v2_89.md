# BridgeData V2
**URL:** https://rail-berkeley.github.io/bridgedata
**Page Title:** BridgeData V2
--------------------


## BridgeData V2: A Dataset for Robot Learning at Scale

[LINK: Code](https://github.com/rail-berkeley/bridge_data_v2)
BridgeData V2 is a large and diverse dataset of robotic manipulation behaviors designed to
            facilitate research in scalable robot learning. The dataset is compatible with open-vocabulary, multi-task
            learning methods conditioned on goal images or natural language instructions. Skills learned from the data
            generalize to novel objects and environments, as well as across institutions.

## Dataset Composition

To support broad generalization, we collected data for a wide range of tasks in many environments with
            variation in objects, camera pose, and workspace positioning. Each trajectory is labeled with a natural
            langauge instruction corresponding to the task the robot is performing.
- 60,096 trajectories 50,365 teleoperated demonstrations 9,731 rollouts from a scripted pick-and-place policy
- 50,365 teleoperated demonstrations
- 9,731 rollouts from a scripted pick-and-place policy
- 24 environments
- 13 skills

### Environments

The 24 environments in BridgeData V2 are grouped into 4 categories. The
                    majority of the data comes from 7 distinct toy kitchens, which include some combination of sinks,
                    stoves, and microwaves. The remaining environments come from diverse sources, including various
                    tabletops, standalone toy sinks, a toy laundry machine, and more.

### Skills

Below we show the various types of skills in BridgeData V2. The majority
                    of the data comes from foundational object manipulation tasks, such as pick-and-place, pushing,
                    and sweeping. Additional data comes from environment manipulation, which includes opening and
                    closing doors and drawers. The remaining data comes from more complex tasks, such as stacking
                    blocks, folding cloths, and sweeping granular media. Some segments of the data contain mixtures
                    of these categories.

### View a Random Trajectory

Use the "Sample" button to view a random trajectory from the dataset! We show the intial and final
            states of the trajectory, as well as the corresponding natural language annotation.

## Usage

The dataset can be downloaded here (stored as JPEGS). The
            teleopearated demonstration data and the data from the scripted pick-and-place policy are provided as
            separate zip files. We also provide both model training code and pre-trained weights for getting started
            with BridgeData V2:
- This repository provides code and
                instructions for training on the dataset and evaluating policies.
[LINK: This repository](https://github.com/rail-berkeley/bridge_data_v2)
- This
                    guide provides instructions for setting up the robot hardware.
[LINK: This
                    guide](https://docs.google.com/document/d/1si-6cTElTWTgflwcZRPfgHU7-UwfCUkEztkH3ge5CGc/edit?usp=sharing)
Above we show a breakdown of the entire dataset, including the autonomously collected data, by what camera
            views are included. "Over-the-shoulder" refers to the primary fixed camera, and "randomized" refers to the
            two alternative camera views that are randomized by the data collectors every 50 trajectories. "Depth",
            when present, is from the same perspective as the primary fixed camera. "Wrist" refers to the
            wide-angle wrist-mounted camera. More cameras were added to the hardware setup throughout data
            collection, so the majority of the data only includes the primary fixed camera view, and very little
            data currently includes all 4 views. However, now that the hardware is in place, more and more data will
            include all 4 views as the dataset continues to grow.

## Evaluations of Offline Learning Methods

We evaluated several state-of-the-art offline learning methods using the dataset. We first evaluated
            on tasks that are seen in the training data. Even though these tasks are seen in training, the methods
            must still generalize to novel object positions, distractor objects, and lighting. Next, we evaluated on
            tasks that require generalizing skills in the data to novel objects and environments. Below we show videos
            for some of the seen and unseen tasks evaluated in the paper. All videos are shown at 2x speed.

### Seen Goal-Conditioned Tasks

### Unseen Goal-Conditioned Tasks

### Seen Language-Conditioned Tasks

### Unseen Language-Conditioned Tasks

## System Setup

All the data was collected on a WidowX 250 6DOF robot arm. We collect demonstrations
            by teleoperating the robot with a VR controller. The control frequency is 5 Hz and the average
            trajectory length is 38 timesteps. For sensing, we use an RGBD camera that is fixed in an over-the-shoulder
            view, two RGB cameras with poses that are randomized during data collection, and RGB camera attached to the
            robot's wrist. The images are saved at a 640x480 resolution.

## Papers

- Bridge Data: Boosting Generalization of Robotic Skills with
                    Cross-Domain Datasets
- Pre-Training for Robots: Offline RL Enables Learning New
                    Tasks from a Handful of Trials
- Generalization with Lossy Affordances: Leveraging Broad
                    Offline Data for Learning Visuomotor Tasks
- BridgeData V2: A Dataset for Robot Learning at Scale

## Contributors

The following people contributed to the project.
Homer Walke , Kevin Black , Frederik Ebert , Aviral Kumar , Anikait Singh , Yanlai Yang , Patrick Yin , Gengchen Yan , Kuan Fang , Ashvin Nair , Tony Zhao , Quan Vuong , Chongyi Zheng , Philippe Hansen-Estruch , Andre He , Vivek Myers , Moo Jin Kim , Max Du , Karl Schmeckpeper , Bernadette Bucher , Georgios Georgakis , Kostas Daniilidis , Chelsea Finn , Sergey Levine
[LINK: Frederik Ebert](https://febert.github.io/)
[LINK: Aviral Kumar](https://aviralkumar2907.github.io/)
[LINK: Anikait Singh](https://asap7772.github.io/)
[LINK: Yanlai Yang](https://yanlai00.github.io/)
[LINK: Kuan Fang](http://kuanfang.github.io/)
[LINK: Tony Zhao](https://tonyzhaozh.github.io/)
[LINK: Quan Vuong](https://quanvuong.github.io/)
[LINK: Bernadette Bucher](https://bucherb.github.io/)
[LINK: Georgios Georgakis](https://ggeorgak11.github.io/)
We also thank Abraham Lee, Mia Galatis, Caroline Johnson, Christian Aviña, Samantha Huang, and Nicholas
            Lofrese for collecting data.
All data is provided under the Creative Commons
                Attribution 4.0 International License

--------------------