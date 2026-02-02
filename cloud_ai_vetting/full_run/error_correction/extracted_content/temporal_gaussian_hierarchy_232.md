# Temporal Gaussian Hierarchy
**URL:** https://zju3dv.github.io/longvolcap
**Page Title:** Long Volumetric Video
--------------------


## Representing Long Volumetric Video with Temporal Gaussian Hierarchy

[LINK: Yinghao Xu 2 *](https://justimyhxu.github.io/)
1 Zhejiang University 2 Stanford University 3 HKUST * Equal Contribution x Corresponding Author
Paper
arXiv
YouTube
Bilibili
Renderer
[LINK: Renderer](https://github.com/dendenxu/fast-gaussian-rasterization)
Framework
[LINK: Framework](https://github.com/zju3dv/EasyVolcap)
SelfCap Dataset

### Overview Video

### Abstract

This paper aims to address the challenge of reconstructing long volumetric videos from multi-view RGB videos. Recent dynamic view synthesis methods leverage powerful 4D representations, like feature grids or point cloud sequences, to achieve high-quality rendering results. However, they are typically limited to short (1~2s) video clips and often suffer from large memory footprints when dealing with longer videos. To solve this issue, we propose a novel 4D representation, named Temporal Gaussian Hierarchy, to compactly model long volumetric videos. Our key observation is that there are generally various degrees of temporal redundancy in dynamic scenes, which consist of areas changing at different speeds. Extensive experimental results demonstrate the superiority of our method over alternative methods in terms of training cost, rendering speed, and storage usage. To our knowledge, this work is the first approach capable of efficiently handling minutes of volumetric video data while maintaining state-of-the-art rendering quality.

### Method

Given a long multi-view video sequence, our method can generate a compact volumetric video with minimal training
            and memory usage while maintaining real-time rendering with state-of-the-art quality.
- (a) We propose a hierarchical structure where each level consists of
              multiple temporal segments. Each segment stores a set of 4D Gaussians [Yang et al. 2023b] to parametrize scenes. As shown at the bottom, the 4D Gaussians
              in different segments represent different granularities of motions, efficiently and effectively modeling video dynamics.
- (b) The appearance model leverages
              gradient thresholding to obtain sparse Spherical Harmonics coefficients, resulting in very compact storage while still maintaining view-dependent effects well.

### Real-Time Demos

[LINK: DNA-Rendering](https://dna-rendering.github.io/)
[LINK: Sports](https://zju3dv.github.com/longvolcap/)
[LINK: MobileStage](https://github.com/zju3dv/4K4D?tab=readme-ov-file#mobile-stage-dataset)
[LINK: Neural3DV](https://github.com/facebookresearch/Neural_3D_Video)
[LINK: ENeRF-Outdoor](https://github.com/zju3dv/ENeRF/blob/master/docs/enerf_outdoor.md)

### Real-Time VR Demos

### Baseline Comparisons

[LINK: 4K4D](https://zju3dv.github.io/4k4d/)
[LINK: K-Planes](https://sarafridov.github.io/K-Planes/)
[LINK: ENeRF](https://zju3dv.github.io/enerf/)

### Citation

### Business Inquiries


--------------------