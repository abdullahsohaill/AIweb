# Project
**URL:** https://whaohan.github.io/bpt
**Page Title:** Scaling Mesh Generation via Compressive Tokenization
--------------------


## Scaling Mesh Generation via Compressive Tokenization

[LINK: Haohan Weng](https://whaohan.github.io/)
[LINK: Zibo Zhao](https://maikouuu.github.io/)
[LINK: Xianghui Yang](https://wi-sc.github.io/xianghui-yang/)
[LINK: Zeqiang Lai](https://zeqiang-lai.github.io/)
[LINK: Code](https://github.com/tencent-hunyuan/bpt)

### Point-cloud Conditioned Mesh Generation

### Image Conditioned Mesh Generation

## Abstract

We propose a compressive yet effective mesh representation, Blocked and Patchified Tokenization (BPT) , facilitating the generation of meshes exceeding 8k faces. 
                            BPT compresses mesh sequences by employing block-wise indexing and patch aggregation, reducing their length by approximately 75% compared to the original sequences. 
                            This compression milestone unlocks the potential to utilize mesh data with significantly more faces, thereby enhancing detail richness and improving generation robustness.
                            Empowered with the BPT, we have built a foundation mesh generative model training on scaled mesh data to support flexible control for point clouds and images. 
                            Our model demonstrates the capability to generate meshes with intricate details and accurate topology, achieving SoTA performance on mesh generation and reaching the level for direct product usage.

## Tokenization

The proposed Blocked and Patchified Tokenization (BPT). (a) We convert the coordinates from the Cartesian system to block-wise indexes. The coordinates are first separated equally into several blocks. Then vertices inside each block are located with 1-dim indexes. 
                            (b) The nearby faces are aggregated as patches to compress the mesh sequence. Each patch center is set as the vertex connected with the most unvisited faces. Subsequently, other vertices within the patch are included in the subsequence to create a complete patch.

## Scaling on Mesh Data

Scaling data for mesh generation with BPT. (a) Existing models can only handle meshes with at most 4k faces, which still lack intricate details. Empowered by BPT, our model can leverage meshes exceeding 8k faces, effectively extending the training scope for mesh generation.
                            (b) We train the same model on meshes with different maximum numbers of faces. As the number of mesh faces increases, the performance of mesh generation significantly improves, highlighting the value of high-poly training data. The generation performance is measured by the Hausdorff distance between the input point cloud and generated meshes (lower is better).

## BibTeX


--------------------