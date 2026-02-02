# Code
**URL:** https://niujinshuchong.github.io/mip-splatting
**Page Title:** Mip-Splatting
--------------------


## Mip-Splatting

## Alias-free 3D Gaussian Splatting

## CVPR 2024 (Oral, Best Student Paper)

[LINK: Zehao Yu](https://niujinshuchong.github.io/)
[LINK: Anpei Chen](https://apchenstu.github.io/)
[LINK: Binbin Huang](https://github.com/hbb1)
[LINK: Torsten Sattler](https://tsattler.github.io/)
[LINK: Code](https://github.com/autonomousvision/mip-splatting)
[LINK: Viewer](https://niujinshuchong.github.io/mip-splatting-demo/)

## TL;DR: We introduce a 3D smoothing filter and a 2D Mip filter for 3D Gaussian Splatting (3DGS), eliminating multiple artifacts and achieving alias-free renderings.

## Abstract

Recently, 3D Gaussian Splatting (3DGS) has demonstrated impressive novel view synthesis results, reaching high fidelity and efficiency. 
            However, strong artifacts can be observed when changing the sampling rate, e.g., by changing focal length or camera distance. 
            We find that the source for this phenomenon can be attributed to the lack of 3D frequency constraints and the usage of a 2D dilation filter. 
            To address this problem, we introduce a 3D smoothing filter which constrains the size of the 3D Gaussian primitives based on the maximal sampling frequency induced by the input views, eliminating high frequency artifacts when zooming in. 
            Moreover, replacing 2D dilation with a 2D Mip filter, which simulates a 2D box filter, effectively mitigates aliasing and dilation issues.
            Our comprehensive evaluation, including scenarios such as training on single-scale images and testing on multiple scales, validates the effectiveness of our approach.

## Motivation

3D Gaussian Splatting renders images by representing 3D Objects as Gaussians which are projected onto the image plane followed by 2D Dilation in screen space as shown in (a). 
            The method's intrinsic shrinkage bias leads to degenerate 3D Gaussians exceed the sampling limit as illustrated by the δ function in (b) while rendering similarly to 2D due to the dilation operation. 
            However, when changing the sampling rate (via the focal length or camera distance), we observe strong dilation effects (c) and high frequency artifacts (d).

## Video

## Results

### Comparison wtih 3DGS

3DGS produces dilation and erosion artifacts due to the use of dilation. 
            It produces erosion effects when zooming in or moving the camera closer. 
            This is because the dilated 2D Gaussians become smaller in screen space, rendering object structures thinner than they actually appear.
            Conversely, screen space dilation produces dilation artifacts when zooming out or moving away from the scene. 
            In this case, dilated 2D Gaussian become bigger in screen space, rendering object structures thicker than they actually appear.
            In contrast, our method is free of such artifacts by introducing a 3D smoothing filter and a 2D Mip filter.

### Comparison wtih 3DGS + EWA

Replacing the 2D dilation of 3DGS with an EWA (elliptical weighted average) filter, denoted as 3DGS + EWA, reduces the dilation and erosion artifacts.
            However, it produces high-frequency artifacts when zooming in, while our method is free of such artifacts, as shown in the following comparisons.
Here, we show more comparisons with 3DGS + EWA. Both models are trained with downsampled images with factor 8 and render at higher-resolution. 
            GT (Training resolution) is the image we used for training but bilinearly upsampled to higher-resolution for reference and GT (8x resolution) is the real GT image we used for evaluation.
- bicycle
- bonsai
- counter
- flowers
- garden
- kitchen
- stump
- treehill
3DGS+EWA
Mip-Splatting (ours)
GT (Training resolution)
GT (8x resolution)

### Effectiveness of 2D Mip Filter

Our 2D Mip filter simulates a 2D box filter in physical imaging process. It approximates exactly 1 pixel in screen space, thus effectively reducing aliasing artifacts.
            As shown in the following video, removing the 2D Mip filter results in aliasing artifacts when zooming out.

### Effectiveness of 3D Smoothing Filter

The 3D smoothing filter constrains the size of the 3D Gaussian primitives based on the maximal sampling frequency induced by the training views, eliminating high frequency artifacts when zooming in. 
            In the following comparisons, we train the models with downsampled images and render high resolution images to simulate zoom-in effects. Excluding the 3D smoothing filter results in high-frequency artifacts. 
            Note that both models are trained with downsampled images with factor 8 and render at higher-resolution. 
            GT (Training resolution) is the image we used for training but bilinearly upsampled to higher-resolution for reference and GT (8x resolution) is the real GT image we used for evaluation.
- bicycle 1
- bicycle 2
- bicycle 3
- garden 1
- garden 2
- treehill
Ours w/o 3D filter
Mip-Splatting (ours)
GT (Training resolution)
GT (8x resolution)

### Real-Time Interactive Viewer

Click the image to use the real-time interactive viewer. Please open the viewer with Chrome or Firefox. For more results, please check our online viewer .
[LINK: online viewer](https://niujinshuchong.github.io/mip-splatting-demo/)

## BibTeX

## Acknowledgements

### References

- 3D Gaussian Splatting for Real-Time Radiance Field Rendering
- EWA Splatting

--------------------