# CoDeF
**URL:** https://qiuyu96.github.io/CoDeF
**Page Title:** CoDeF
--------------------


## CoDeF: Content Deformation Fields for Temporally Consistent Video Processing

[LINK: Hao Ouyang](https://ken-ouyang.github.io/)
[LINK: Qiuyu Wang](https://github.com/qiuyu96)
[LINK: Yuxi Xiao](https://henry123-boy.github.io/)
[LINK: Juntao Zhang](https://github.com/JordanZh)
[LINK: Yujun Shen](https://shenyujun.github.io/)
[LINK: Code](https://github.com/qiuyu96/CoDeF)
[LINK: High-Res Video](https://ezioby.github.io/CoDeF_Demo/)

## Video Translation

## Consistent Video Translation with the learned canonical image and deformation. 
        Slide for comparison. For all the demos, the inputs are provided on the left.

## Abstract

We present the content deformation field (CoDeF) as a new type of video representation,
            which consists of a canonical content field aggregating the static contents in the entire video 
            and a temporal deformation field recording the transformations from the canonical image
            ( i.e. , rendered from the canonical content field) to each individual frame along the time axis.
            Given a target video, these two fields are jointly optimized to reconstruct it through a carefully tailored rendering pipeline.

            We advisedly introduce some regularizations into the optimization process, 
            urging the canonical content field to inherit semantics ( e.g. , the object shape) from the video.
With such a design, CoDeF naturally supports lifting image algorithms for video processing, 
            in the sense that one can apply an image algorithm to the canonical image 
            and effortlessly propagate the outcomes to the entire video with the aid of the temporal deformation field.

            We experimentally show that CoDeF is able to lift image-to-image translation to video-to-video translation 
            and lift keypoint detection to keypoint tracking without any training.

            More importantly, thanks to our lifting strategy that deploys the algorithms on only one image, 
            we achieve superior cross-frame consistency in processed videos compared to existing video-to-video translation approaches, 
            and even manage to track non-rigid objects like water and smog.

## Other Applications

## Point-based Tracking with the learned canonical image and deformation.

## Segmentation-based Tracking . The segmentation mask is acquired based on the learned canonical image and propagated to the sequence. Slide for better visualization.

## Video Super-resolution with the learned canonical image and deformation. 
        Slide for comparison.


--------------------