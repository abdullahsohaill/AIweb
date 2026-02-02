# TransPixar Adobe
**URL:** https://wileewang.github.io/TransPixar
**Page Title:** TransPixeler: Advancing Text-to-Video Generation with Transparency
--------------------


## TransPixeler: Advancing Text-to-Video Generation with Transparency

[LINK: Luozhou Wang](https://wileewang.github.io/)
[LINK: Yijun Li](https://yijunmaverick.github.io/)

## Zhifei Chen

[LINK: Zhifei Zhang](https://zzutk.github.io/)

## 1 HKUST(GZ)

## 2 HKUST

## 3 Adobe Research

## * Internship Project

## ** Project Lead

## † Corresponding Author

[LINK: Code](https://github.com/wileewang/TransPixeler)

## Abstract

Text-to-video generative models have made significant strides, enabling diverse applications in entertainment, advertising, and education. 
                However, generating RGBA video, which includes alpha channels for transparency, remains a challenge due to limited datasets and the difficulty of adapting existing models. 
                Alpha channels are crucial for visual effects (VFX), allowing transparent elements like smoke and reflections to blend seamlessly into scenes.
                We introduce TransPixeler , a method to extend pretrained video models for RGBA generation while retaining the original RGB capabilities. 
                TransPixar leverages a diffusion transformer (DiT) architecture, incorporating alpha-specific tokens and using LoRA-based fine-tuning to jointly generate RGB and alpha channels with high consistency. 
                By optimizing attention mechanisms, TransPixeler preserves the strengths of the original RGB model and achieves strong alignment between RGB and alpha channels despite limited training data.
                Our approach effectively generates diverse and consistent RGBA videos, advancing the possibilities for VFX and interactive content creation.

## Text-to-RGBA Video

(Results are generated using internal video model J)
A transparent glass of water with ice cubes gently swirling
An asteroid belt swirling chaotically through space.
A squirrel's bushy tail flicking quickly.
A cloud of dust erupting and dispersing like an explosion.

## Image-to-RGBA Video

Input Image
Generated Video

## Method Overview

We extend state-of-the-art DiT-like video generation models by introducing new tokens for alpha channel generation, reinitializing their positional embeddings, and adding a zero-initialized domain embedding to distinguish them from RGB tokens. 
                Using a LoRA-based fine-tuning scheme, we project alpha tokens into the qkv space while preserving RGB quality. 
                Our approach integrates text, RGB, and alpha tokens in a unified sequence with a grouped attention mechanism, retaining the original model’s performance while improving RGB-alpha alignment by keeping RGB-attend-to-Alpha attention and removing Text-attend-to-Alpha to mitigate risks from limited training data.

## BibTeX


--------------------