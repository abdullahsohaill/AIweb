# **ECCV 2024**] [[**Project page**
**URL:** https://twoongg.github.io/projects/realfred
**Page Title:** ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environment
--------------------


## ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments

## ECCV 2024

[LINK: Taewoong Kim](https://twoongg.github.io)
[LINK: Cheolhong Min](https://mch0916.github.io)
[LINK: Byeonghwi Kim](https://bhkim94.github.io)
[LINK: Wonje Jeung](https://cryinginitial.github.io/)
[LINK: Jonghyun Choi](https://ppolon.github.io)
* Equal Contribution. † Corresponding author.
[LINK: Code](https://github.com/snumprlab/realfred)

## Proposed ReALFRED bechmark

## Abstract

Simulated virtual environments have been widely used to learn robotic agents that perform daily household tasks. These environments encourage research progress by far, but often provide limited object interactability, visual appearance different from real-world environments, or relatively smaller environment sizes. This prevents the learned models in the virtual scenes from being readily deployable. To bridge the gap between these learning environments and deploying (i.e., real) environments, we propose the ReALFRED benchmark that employs real-world scenes, objects, and room layouts to learn agents to complete household tasks by understanding free-form language instructions and interacting with objects in large, multi-room and 3D-captured scenes. Specifically, we extend the ALFRED benchmark with updates for larger environmental spaces with smaller visual domain gaps. With ReALFRED, we analyze previously crafted methods for the ALFRED benchmark and observe that they consistently yield lower performance in all metrics, encouraging the community to develop methods in more realistic environments. Our code and data are publicly available.

## Video

## The ReALFRED Benchmark

To develop agents capable of performing household tasks, substantial progress
        has been achieved in various domains, including navigation, rearrangement, and manipulation tasks. In particular, Shridhar et al. recently introduced
        the ALFRED benchmark that requires agents to complete long-horizon household tasks by jointly understanding egocentric visual observations and natural
        language instructions in household environments.
However, the spatial size of these environments is somewhat restricted to a
        single room compared to the size of previously proposed 3D-captured environments consisting of multiple rooms, which could potentially restrict the
        deployability of agents to larger environments. Furthermore, the environments
        used in the ALFRED benchmark are built with synthetic CAD assets and
        therefore could potentially yield visual aesthetics different from those obtained
        from real-world environments, which could eventually cause performance
        degradation due to visual domain gaps.
To address these issues, we extend the ALFRED benchmark and propose
        a challenging benchmark, named the ReALFRED benchmark, which requires
        agents to perform household tasks in large indoor environments captured in 3D
        with object interaction. For training and evaluation, we follow the same protocol
        as ALFRED to collect expert demonstrations in the captured large environments.

## Visualization

## Data Explorer

## Results

We follow the same evaluation protocol of the ALFRED benchmark.
          The primary metric is Success Rate (SR) which measures the percentage of
          completed tasks. Goal-Condition Success Rate (GC) measures the percentage
          of achieved goal conditions. Finally, we also measure the penalized SR and GC
          by the length of the trajectory path ( i.e. , PLWSR and PLWGC) which indicate
          how efficiently an agent completes tasks.
For more details, please check out the paper.

## BibTeX


--------------------