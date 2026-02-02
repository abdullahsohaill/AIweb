# S-NeRF
**URL:** https://ziyang-xie.github.io/s-nerf
**Page Title:** S-NeRF
--------------------


## S-NeRF : Neural Radiance Fields for Street Views

[LINK: Junge Zhang 1*](https://andy-zd.github.io/)
[LINK: Li Zhang 1†](https://lzrobots.github.io)
- Paper
- Demo
- Code (Pre-released)
[LINK: Code (Pre-released)](https://github.com/fudan-zvg/S-NeRF)

### Abstract

Neural Radiance Fields (NeRFs) aim to synthesize novel views of objects and scenes, given the object-centric camera views with large overlaps. However, we conjugate that this paradigm does not fit the nature of the street views that are collected by many self-driving cars from the large-scale unbounded scenes. Also, the onboard cameras perceive scenes without much overlapping. Thus, existing NeRFs often produce blurs, "floaters" and other artifacts on  street-view synthesis. In this paper, we propose a new street-view NeRF (S-NeRF) that considers novel view synthesis of both the large-scale background scenes and the foreground moving vehicles jointly. Specifically, we improve the scene parameterization function and the camera poses for learning better neural representations from street views. We also use the the noisy and sparse LiDAR points to boost the training and learn a robust geometry and reprojection based confidence to address the depth outliers.   Moreover, we extend our S-NeRF for reconstructing moving vehicles that is impracticable for conventional NeRFs. Thorough experiments on the large-scale driving datasets (e.g., nuScenes and Waymo) demonstrate that our method beats the state-of-the-art rivals by reducing 7～40% of the mean-squared error in the street-view synthesis and a 45% PSNR gain for the moving vehicles rendering.

### Video demo

### Model Overview

### Foreground Camera Transformation

### Semantic Label Generation

### Bibtex

The website template was borrowed from Michaël Gharbi .

--------------------