# [page]
**URL:** https://pku-epic.github.io/Open6DOR
**Page Title:** Open6DOR
--------------------


## Open6DOR: Benchmarking Open-instruction 6-DoF Object Rearrangement and A VLM-based Approach

[LINK: Yufei Ding](https://selina2023.github.io/)
[LINK: Haoran Geng](https://geng-haoran.github.io/)
[LINK: Chaoyi Xu](https://github.com/co1one)
[LINK: Jiazhao Zhang](https://jzhzhang.github.io/)
[LINK: Qiyu Dai](https://daiqy.github.io/)
[LINK: He Wang](https://hughw19.github.io/)
1 School of Electrical Engineering and Computer Science, Peking University 2 Galbot 3 Beijing Academy of Artificial Intelligence 4 CFCS, School of Computer Science, Peking University
* equal contributions † corresponding author
Paper
Code
[LINK: Code](https://github.com/Selina2023/Open6DOR)
Benchmark & Dataset
Open6DOR Benchmark and Real-world Experiments. We introduce a challenging and comprehensive benchmark for open-instruction
6-DoF object rearrangement tasks, termed Open6DOR. Following this, we propose a zero-shot and robust method, Open6DORGPT,
which proves effective in demanding simulation environments and real-world scenarios.

## Video

## Abstract

The integration of large-scale Vision-Language Models (VLMs) with embodied AI can greatly enhance the
              generalizability and the capacity to follow open instructions for robots. However, existing studies on object rearrangement are
              not up to full consideration of the 6-DoF requirements, let alone establishing a comprehensive benchmark. In this paper, we
              propel the pioneer construction of the benchmark and approach for table-top Open-instruction 6-DoF Object Rearrangement
              ( Open6DOR ). Specifically, we collect a synthetic dataset of 200+ objects and carefully design 2400+ Open6DOR tasks.
              These tasks are divided into the Position-track, Rotation-track, and 6-DoF-track for evaluating different embodied agents in
              predicting the positions and rotations of target objects. Besides, we also propose a VLM-based approach for Open6DOR, named Open6DOR-GPT , which empowers GPT-4V with 3Dawareness
              and simulation-assistance and exploits its strengths in generalizability and instruction-following for this task. We
              compare the existing embodied agents with our Open6DORGPT on the proposed Open6DOR benchmark and find that
              Open6DOR-GPT achieves the state-of-the-art performance. We further show the impressive performance of Open6DORGPT
              in diverse real-world experiments. Our constructed benchmark and method will be released upon paper acceptance.

## Methods

### Full pipeline

Method Overview. Open6DOR-GPT takes the RGB-D image and instruction as input and outputs the corresponding robot motion
                  trajectory. Firstly, the preprocessing module extracts the object names and masks. Then, two modules simultaneously predict the position
                  and rotation of the target object in a decoupled way. Finally, the planning module generates a trajectory for execution.

### Rotation pipeline

Simulation-assisted Rotation Module. Firstly, a textured mesh is reconstructed from the single-view image of the target object.
Then, we employ large-scale sampling to obtain multiple rotation samples. This sample set is then narrowed down through a simulationassisted
filtering process to derive several stable pose categories. Finally, we generate rendered images of the pose candidates, from which
GPT-4V selects the optimal goal rotation.

## Results

## Contact

If you have any questions, please feel free to contact us:
- Yufei Ding : selina Prevent spamming @ Prevent spamming stu.pku.edu.cn
- Haoran Geng : ghr Prevent spamming @ Prevent spamming stu.pku.edu.cn
- He Wang : hewang Prevent spamming @ Prevent spamming pku.edu.cn

--------------------