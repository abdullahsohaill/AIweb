# [link]
**URL:** https://rgbd.cs.princeton.edu
**Page Title:** SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite
--------------------


## SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite

## Abstract

Although RGB-D sensors have enabled major breakthroughs
for several vision tasks, such as 3D reconstruction,
we haven not achieved a similar performance jump for
high-level scene understanding. Perhaps one of the main
reasons for this is the lack of a benchmark of reasonable
size with 3D annotations for training and 3D metrics for
evaluation. In this paper, we present an RGB-D benchmark
suite for the goal of advancing the state-of-the-art in all major
scene understanding tasks. Our dataset is captured by
four different sensors and contains 10,000 RGB-D images,
at a similar scale as PASCAL VOC. The whole dataset is
densely annotated and includes 146,617 2D polygons and
58,657 3D bounding boxes with accurate object orientations,
as well as a 3D room layout and category for scenes.
This dataset enables us to train data-hungry algorithms for
scene-understanding tasks, evaluate them using direct and
meaningful 3D metrics, avoid overfitting to a small testing
set, and study cross-sensor bias.

## News

## Paper

- S. Song, S. Lichtenberg, and J. Xiao. SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite Proceedings of 28th IEEE Conference on Computer Vision and Pattern Recognition ( CVPR2015 ) Oral Presentation

## Video (Download raw video here )

## Data and Annotation

- SUNRGBD V1 :
This file contains the 10335 RGBD images of SUNRGBD V1.
[1] N. Silberman, D. Hoiem, P. Kohli, R. Fergus. Indoor
segmentation and support inference from rgbd images. In
ECCV, 2012.
[2] A. Janoch, S. Karayev, Y. Jia, J. T. Barron, M. Fritz,
K. Saenko, and T. Darrell. A category-level 3-d object
dataset: Putting the kinect to work. In ICCV Workshop on
Consumer Depth Cameras for Computer Vision, 2011.
[3] J. Xiao, A. Owens, and A. Torralba. SUN3D: A database
of big spaces reconstructed using SfM and object labels. In
ICCV, 2013
- SUNRGBDtoolbox :
This file contains annotation and Matlab code to load and visualize the data. Here is the README.txt

## Updates

- SUNRGBDMeta2DBB_v2.mat : Updated 2D bounding box.
- SUNRGBDMeta3DBB_v2.mat : Updated 3D bounding box.

## Evaluation

- detection.zip (15.1 MB)
- holisticScene.zip (269 KB)
- roomlayout.zip (274 KB) (contains code for "Manhattan Box" and "Convex Hull" methods.)

## Feature

- deep_features.mat (230.1 MB) : Places-CNN [4] features on depth and color images.

## Presentation

- Oral Presentation Slides
- Poster

## Other Materials

- supp.pdf : This file contains more results and detials about our annotation tool.

## Acknowledgement

This work is supported by gift funds from Intel Corporation.
We thank Thomas Funkhouser, Jitendra Malik, Alexi A. Efros and Szymon Rusinkiewicz for valuable discussion.
We also thank Linguang Zhang, Fisher Yu, Yinda Zhang, Luna Song, Pingmei Xu and Guoxuan Zhang for capturing and labeling.

## Reference

[4] B. Zhou, A. Lapedriza, J. Xiao, A. Torralba, and A. Oliva
Learning Deep Features for Scene Recognition using Places Database
Advances in Neural Information Processing Systems 27 (NIPS2014)

--------------------