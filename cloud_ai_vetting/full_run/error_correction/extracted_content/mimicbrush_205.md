# MimicBrush
**URL:** https://xavierchen34.github.io/MimicBrush-Page
**Page Title:** MimicBrush
--------------------


## MimicBrush: Zero-shot Image Editing with Reference Imitation

[LINK: Xi Chen](https://xavierchen34.github.io/)
[LINK: Mengting Chen](https://mengtingchen.github.io/)
[LINK: Shilong Zhang](https://jshilong.github.io/)
[LINK: Yujun Shen](https://shenyujun.github.io/)
[LINK: Hengshuang Zhao](https://hszhao.github.io/)
[LINK: Code](https://github.com/ali-vilab/MimicBrush)
Diverse editing results produced by MimicBrush, where users only need to specify the
              to-edit regions in the source image (i.e., white masks) and provide an in-the-wild reference image
              illustrating how the regions are expected after editing. Our model automatically captures the semantic
              correspondence between them, and accomplishes the editing in one execution.

## Video Introduction

## Local Region Editing

## Texture Transfer

## Post-processing Refinement

## Abstract

Image editing serves as a practical yet challenging task considering the diverse
            demands from users, where one of the hardest parts is to precisely describe how
            the edited image should look like. In this work, we present a new form of editing,
            termed imitative editing, to help users exercise their creativity more conveniently.
            Concretely, to edit an image region of interest, users are free to directly draw
            inspiration from some in-the-wild references (e.g., some relative pictures come
            across online), without having to cope with the fit between the reference and the
            source. Such a design requires the system to automatically figure out what to
            expect from the reference to perform the editing. For this purpose, we propose a
            generative training framework, dubbed MimicBrush, which randomly selects two
            frames froma video clip, masks some regions of one frame, and learns to recover the
            masked regions using the information from the other frame. That way, our model,
            developed from a diffusion prior, is able to capture the semantic correspondence
            between separate images in a self-supervised manner. We experimentally show the
            effectiveness of our method under various test cases as well as its superiority over
            existing alternatives. We also construct a benchmark to facilitate further research.

## Overall Pipeline

The training process of MimicBrush. First, we randomly sample two frames from a video
            sequence as the reference and source image. The source image are then masked and exerted with
            data augmentation. Afterward, we feed the noisy image latent, mask, background latent, and depth
            latent of the source image into the imitative U-Net. The reference image is also augmented and sent
            to the reference U-Net. The dual U-Nets are trained to recover the masked area of source image. The
            attention keys and values of reference U-Net are concatenated with the imitative U-Net to assist the
            synthesis of the masked regions.

## BibTeX


--------------------