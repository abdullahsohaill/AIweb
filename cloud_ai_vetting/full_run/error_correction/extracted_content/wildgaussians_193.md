# WildGaussians
**URL:** https://wild-gaussians.github.io
**Page Title:** WildGaussians: 3D Gaussian Splatting in the Wild
--------------------

[LINK: Jonas Kulhanek](https://jkulhanek.github.io/)
[LINK: Songyou Peng](https://pengsongyou.github.io/)
[LINK: Torsten Sattler](https://tsattler.github.io/)
[LINK: Code](https://github.com/jkulhanek/wild-gaussians/)
WildGaussians boost 3DGS for in-the-wild scenes with appearance and dynamic changes

## Abstract

We introduce WildGaussians, a novel approach to handle occlusions and appearance changes with 3DGS. By leveraging robust DINO features and integrating an appearance modeling module within 3DGS, our method achieves state-of-the-art results. We demonstrate that WildGaussians matches the real-time rendering speed of 3DGS while surpassing both 3DGS and NeRF baselines in handling in-the-wild data, all within a simple architectural framework.

## Appearance modeling

In order to enable training on images with varying appearance (images captured at different time of the day), we extend 3DGS with appearance modeling module which achieves the same inference speed as 3DGS.
      In these visualizations, we interpolate between different training image embeddings to demonstrate how each method handles appearance changes.
      Note, we report FPS computed on NVIDIA 4090 at FullHD resolution (1920x1080).

## Appearance interpolation

We show that our approach is able to smoothly interpolate between different appearances of the same scene.

## Removing occluders

When there are occluders in the scene, the Gaussian splatting will not be able to represent the scene correctly leading to excessive ammounts of floaters . Our approach can remove these occluders by using DINO-based uncertainty predictor.
      Note, we report FPS computed on NVIDIA 4090 at FullHD resolution (1920x1080).

## Depth prediction

For reference, we show the depth prediction rendered by rasterizing the Gaussians' centers.

## Concurrent works

There are several concurrent works that also aim to extend 3DGS to handle in-the-wild data:
- Wild-GS: Real-Time Novel View Synthesis from Unconstrained Photo Collections
- Gaussian in the Wild: 3D Gaussian Splatting for Unconstrained Image Collections
- SpotlessSplats: Ignoring Distractors in 3D Gaussian Splatting
- SWAG: Splatting in the Wild images with Appearance-conditioned Gaussians
- WE-GS: An In-the-wild Efficient 3D Gaussian Representation for Unconstrained Photo Collections

## Acknowledgements

We would like to thank Weining Ren for his help with the NeRF On-the-go dataset and code and Tobias Fischer and Xi Wang for fruitful discussions.
        This work was supported by the Czech Science Foundation (GAČR) EXPRO (grant no. 23-07973X)
        and by the Ministry of Education, Youth and Sports of the Czech Republic through the e-INFRA CZ (ID:90254).
        The renderer is built on 3DGS, Mip-Splatting. Please follow the license of 3DGS and Mip-Splatting. 
        We thank all the authors for their great work and repos. Finally, we would also like to thank 
        Dor Verbin for the video comparison tool used in this website.

## Citation


--------------------