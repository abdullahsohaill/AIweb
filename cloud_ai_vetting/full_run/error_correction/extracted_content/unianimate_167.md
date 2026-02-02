# UniAnimate
**URL:** https://unianimate.github.io
**Page Title:** UniAnimate
--------------------


## UniAnimate: Taming Unified Video Diffusion Models for Consistent Human Image Animation

[LINK: Code](https://github.com/ali-vilab/UniAnimate)

## Abstract

Recent diffusion-based human image animation techniques have demonstrated impressive success in synthesizing videos that faithfully follow a given reference identity and a sequence of desired movement poses. Despite this, there are still two limitations: i) an extra reference model is required to align the identity image with the main video branch, which significantly increases the optimization burden and model parameters; ii) the generated video is usually short in time (e.g., 24 frames), hampering practical applications. To address these shortcomings, we present a UniAnimate framework to enable efficient and long-term human video generation. First, to reduce the optimization difficulty and ensure temporal coherence, we map the reference image along with the posture guidance and noise video into a common feature space by incorporating a unified video diffusion model. Second, we propose a unified noise input that supports random noised input as well as first frame conditioned input, which enhances the ability to generate long-term video. Finally, to further efficiently handle long sequences, we explore an alternative temporal modeling architecture based on state space model to replace the original computation-consuming temporal Transformer. Extensive experimental results indicate that UniAnimate achieves superior synthesis results over existing state-of-the-art counterparts in both quantitative and qualitative evaluations. Notably, UniAnimate can even generate highly consistent one-minute videos by iteratively employing the first frame conditioning strategy. Code and models will be publicly available.

## Overall Framework of UniAnimate

## The overall architecture of the proposed UniAnimate. Firstly, we utilize the CLIP encoder and VAE encoder to extract latent features of the given reference image. To facilitate the learning of the human body structure in the reference image, we also incorporate the representation of the reference pose into the final reference guidance. Subsequently, we employ a pose encoder to encode the target driven pose sequence and concatenate it with the noised input along the channel dimension. The noised input is derived from the first frame conditioned video or a noised video. Then, the concatenated noised input is stacked with the reference guidance along the temporal dimension and fed into the unified video diffusion model to remove noise. The temporal module in the unified video diffusion model can be the temporal Transformer or temporal Mamba. Finally, a VAE decoder is adopted to map the generated latent video to the pixel space.

## Overview: Summary of the Generated Videos

### (The generated one-minute example is displayed at the end of the demo video)

## Animating Synthesized Model Characters

## Animating Real Model Characters

## Animating Clay Style Characters

## Internationaly Renowned Figure: Elon Musk

## Animating Other Cross-Domain Characters

## Internationaly Renowned Figure: Yann LeCun

## Reference


--------------------