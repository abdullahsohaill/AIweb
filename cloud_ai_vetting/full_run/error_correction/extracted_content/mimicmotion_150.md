# MimicMotion
**URL:** https://tencent.github.io/MimicMotion
**Page Title:** MimicMotion
--------------------


## MimicMotion : High-Quality Human Motion Video Generation with Confidence-aware Pose Guidance

[LINK: Code](https://github.com/tencent/MimicMotion)

## Showcases: Dancing&Talking

Hover over to view the input reference images. Cases generated with face swapping and frame interpolation post-processing.

## Comparisons with baseline methods

## Abstract

In recent years, generative artificial intelligence has achieved significant advancements in the field of image generation, spawning a variety of applications. However, video generation still faces considerable challenges in various aspects such as controllability, video length, and richness of details, which hinder the application and popularization of this technology. In this work, we propose a controllable video generation framework, dubbed MimicMotion, which can generate high-quality videos of arbitrary length with any motion guidance. Comparing with previous methods, our approach has several highlights. Firstly, with confidence-aware pose guidance, temporal smoothness can be achieved so model robustness can be enhanced with large-scale training data. Secondly, regional loss amplification based on pose confidence significantly eases the distortion of image significantly. Lastly, for generating long smooth videos, a progressive latent fusion strategy is proposed. By this means, videos of arbitrary length can be generated with acceptable resource consumption. With extensive experiments and user studies, MimicMotion demonstrates significant improvements over previous approaches in multiple aspects.

## Method

MimicMotion integrates an image-to-video diffusion model with novel confidence-aware pose guidance.
The model's trainable components consist of a spatiotemporal U-Net and a PoseNet for introducing pose sequence as the condition.
Key features of confidence-aware pose guidance include:
1) The pose sequence is accompanied by keypoint confidence scores, enabling the model to adaptively adjust the influence of pose guidance based on the score.
2) The regions with high confidence are given greater weight in the loss function, amplifying their impact in training.

## Model structure based on the pre-trained SVD.

### Confidence-aware pose guiding

We utilize brightness on the pose guidance frame to represent the confidence level of pose estimation.

## Illustration of confidence-aware pose guiding.

### Region-specific hands refiner

We implement a masking strategy that generate masks based on a confidence threshold.
          We unmask areas where confidence scores surpass a predefined threshold, thereby identifying reliable regions.
          When computing the loss of the video diffusion model, the loss values corresponding to the unmasked regions are amplified by a certain scale so they can be take more effect on the model training than other masked regions.

### Gradually latent fusion for temporal smoothness

We propose a progressive approach for generating long video with temporal smoothness.
          During each denoising step, video segments are firstly denoised separately with the trained model, conditioning on the same reference image and the corresponding sub-sequence of poses. Within each denoising step, the overlapped frames, marked within dashed boxes in the figure, are progressively fused according to their frame positions.

## Overlapped diffusion for generating any-length videos.

## Comparison to state-of-the-art methods

### Quantitative evaluation

Our method achieves better hand generation quality, and more accurately adheres to the reference pose. Note that our method is not trained on TikTokDataset .

## Qualitative comparison to the state-of-the-art methods on the test set of TikTokDataset .

We visualize the 106th frame from seq 338 of TikTokDataset and the pixel-wise difference between consecutive frames. MagicPose exhibits abrupt transitions, while Moore and MuseV show instability in texture and text. In contrast, our method demonstrates stable inter-frame differences and better temporal smoothness.

## Comparison of temporal smoothness with state-of-the-art methods.

### Quantitative evaluation

### User study

## Preference of MimicMotion (ours) over baseline methods on the test split of TikTokDataset . Users prefer MimicMotion over other methods.

## Ablation Study

### Confidence-aware pose guiding

This design enhances generation robustness to false guiding signals (Pose 1&2) and provides visibility hints to tackle pose ambiguity (Pose 3).

## Confidence-aware pose guiding.

### Hand region enhancement

Under identical reference image and pose guidance, training with hand enhancement consistently reduces hand distortion and enhances visual appeal.

## Hand region enhancement

### Progressive latent fusion

Progressive latent fusion enables smooth transitions and avoids abrupt changes across video segment
          boundaries, thereby enhancing overall visual temporal coherence for long video generation.

## BibTeX


--------------------