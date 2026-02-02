# OmniObject3D
**URL:** https://omniobject3d.github.io
**Page Title:** OmniObject3D: Large-Vocabulary 3D Object Dataset for Realistic Perception, Reconstruction and Generation
--------------------


## OmniObject3D

## OmniObject3D: Large-Vocabulary 3D Object Dataset for Realistic  Perception, Reconstruction and Generation

## CVPR 2023 (Award Candidate)

Tong Wu 1,2 , Jiarui Zhang 1,3 , Xiao Fu 1 , Yuxin Wang 1,4 , Jiawei Ren 5 , Liang Pan 5 , Wayne Wu 1 , Lei Yang 1,3 , Jiaqi Wang 1 , Chen Qian 1 , Dahua Lin 1,2 ✉, Ziwei Liu 5 ✉
[LINK: Tong Wu](https://wutong16.github.io/)
[LINK: Xiao Fu](https://fuxiao0719.github.io/)
[LINK: Jiawei Ren](https://jiawei-ren.github.io/)
[LINK: Wayne Wu](https://wywu.github.io/)
[LINK: Jiaqi Wang](https://myownskyw7.github.io/)
[LINK: Ziwei Liu](https://liuziwei7.github.io/)

## 1 Shanghai Artificial Intelligence Laboratory, 2 The Chinese University of Hong Kong, 3 SenseTime Research, 4 Hong Kong University of Science and Technology, 5 S-Lab, Nanyang Technological University

[LINK: Code](https://github.com/omniobject3d/OmniObject3D/tree/main)
[LINK: Challenge](https://omniobject3d.github.io/challenge.html)

## Abstract

We propose OmniObject3D, a large vocabulary 3D object dataset with massive high-quality real-scanned 3D objects to facilitate the development of 3D perception, reconstruction, and generation in the real world.
OmniObject3D has several appealing properties: 1) Large Vocabulary: It comprises 6,000 scanned objects in 190 daily categories, sharing common classes with popular 2D datasets (e.g., ImageNet and LVIS), benefiting the pursuit of generalizable 3D representations. 2) Rich Annotations: Each 3D object is captured with both 2D and 3D sensors, providing textured meshes , point clouds , multi-view rendered images , and multiple real-captured videos . 3) Realistic Scans: The professional scanners support high-quality object scans with precise shapes and realistic appearances.
With the vast exploration space offered by OmniObject3D, we carefully set up four evaluation tracks: a) robust 3D perception , b) novel-view synthesis , c) neural surface reconstruction , and d) 3D object generation .
[LINK: Toys4K](https://github.com/rehg-lab/lowshot-shapebias)
[LINK: ScanObjectNN](https://hkust-vgd.github.io/scanobjectnn/)
[LINK: AKB-48](https://liuliu66.github.io/articulationobjects/)
Table 1. A comparison between OmniObject3D and other commonly-used 3D object datasets. It is the largest among all the real-world scanned object datasets.
Figure 1. Semantic distribution of our dataset.

## Robust 3D Perception

OmniObject3D boosts robustness analysis of point cloud classification by disentangling the two critical out-of-distribution (OOD) challenges introduced in the paper, i.e., OOD styles and OOD corruptions.
Figure 2. Analysis on robustness to OOD styles and OOD corruptions.

## Novel View Synthesis

We study several representative methods on OmniObject3D for novel view synthesis (NVS) in two settings: 1) training on a single scene with densely captured images and 2) learning priors across scenes from the dataset to explore the generalization ability of NeRF-style models. We show examples of single-scene NVS by Mip-NeRF .
We show examples of cross-scene NVS by pixelNeRF , MVSNeRF , and IBRNet given 3 views (ft denotes fine-tuned with 13 views).
[LINK: MVSNeRF](https://apchenstu.github.io/mvsnerf/)
[LINK: IBRNet](https://ibrnet.github.io/)

## Neural Surface Reconstruction

Precise surface reconstruction from multi-view images enables a broad range of applications. We include representative methods for dense-view and sparse-view surface reconstruction, respectively. We show examples of dense-view surface reconstruction by NeuS . More results on the sparse-view setting can be found in the paper.
[LINK: NeuS](https://lingjie0206.github.io/papers/NeuS/)

## 3D Object Generation

State-of-the-art generative models can directly generate textured 3D meshes. We train We train GET3D on OmniObject3D and show examples of the generated shapes.
[LINK: GET3D](https://nv-tlabs.github.io/GET3D/)
Some concurrent works also focus on building large-scale 3D object datasets:
- Objaverse is a massive dataset with 800K+ annotated 3D objects collected from Sketchfab .
- ScanNeRF provides an effective pipeline for scanning real objects in quantity and effortlessly for evaluating Neural Rendering frameworks.
[LINK: ScanNeRF](https://eyecan-ai.github.io/scannerf/)

--------------------