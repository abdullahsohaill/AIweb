# [Link
**URL:** https://grail.cs.washington.edu/projects/dreampose
**Page Title:** DreamPose: Fashion Image-to-Video Synthesis via Stable Diffusion
--------------------


## DreamPose: Fashion Image-to-Video Synthesis via Stable Diffusion

[LINK: Johanna Karras](https://johannakarras.github.io/)
[LINK: Ting-Chun Wang](https://tcwang0509.github.io/)
[LINK: Code](https://github.com/johannakarras/DreamPose)

## DreamPose is a diffusion-based image-to-video synthesis model. Given an input image of a person and pose sequence, DreamPose synthesizes a photorealistic video of the input person following the pose sequence.

## Gallery

## Abstract

We present DreamPose, a diffusion-based method for generating animated fashion videos from still images. Given an image and a sequence of human body poses, our method synthesizes a video containing both human and fabric motion. To achieve this, we finetune a pretrained text-to-image model (Stable Diffusion) into a pose-and-image guided video synthesis model by using a novel encoder architecture and finetuning strategy aimed at producing temporally consistent frames that match the image details of the input image. Since DreamPose is fine-tuned from an initial Stable Diffusion checkpoint, it leverages a wealth of image pretraining knowledge, while also using the UBC Fashion dataset to maximize image quality for our particular task. Our results show that DreamPose achieves state-of-the-art results on fashion video synthesis. With potential applications in online retail, social media, animation, and virtual reality, our method introduces a novel way to showcase digital fashion.

## Architecture

a) We modify the original Stable Diffusion architecture in order to enable image and pose conditioning. First, we replace the CLIP text encoder with a dual CLIP-VAE image encoder. Then, we concatenate the target pose representation, consisting of {p i-1 , p i-1 , p i , p i+1 , p i+2 } where p i is the target pose, to the input noise. During training, we finetune the denoising UNet and our Adapter module on the full dataset and further perform subject-specific finetuning of the UNet, Adapter, and VAE Decoder on a single input image. b) We implement an adapter module to jointly model and reshape the concatenated pretrained CLIP and VAE embeddings for conditioning the UNet on the input frame.

## Two-Phase Training Scheme

DreamPose is finetuned in two phases. In phase 1, we finetune the model on the full dataset (UBC Fashion dataset). In phase 2, the model is further finetuned on one or more subject images.

## Comparison to State-of-the-Art

We compare DreamPose to state-of-the-art image animation methods: "Motion Representations for Articulated Animation" (Siarohin et al. 2021) and "Thin-Plate Spline Motion Model" (Zhao et al. 2022).

## Multiple Input Images

DreamPose achieves state-of-the-art results with only a single input image, but it can be finetuned with an arbitrary number of input images of the same subject. Increasing the number of input images increases the temporal consistency and realism of the output video.

## Pose Transfer

We showcase pose transfer results using DreamPose. Select an input image to animate it according the the pose sequence above.

## Ablation Studies

## We compare ablated versions of our method (middle) to our full model (right). Namely, we compare with only a CLIP image encoder, with only one target pose input, and without VAE decoder finetuning.

## Limitations

We suggest that future work tackle the current challenges that DreamPose faces: (1) inconsistencies in dress attributes, including sleeves, necklines, and length. (2) Flickering effect for complex patterns. (3) Pose misalignment.

## BibTeX

## Acknowledgments

This work was supported by the UW Reality Lab, Meta, Google, OPPO, and Amazon.

--------------------