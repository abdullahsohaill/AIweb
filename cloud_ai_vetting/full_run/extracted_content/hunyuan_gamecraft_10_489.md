# Hunyuan-GameCraft-1.0
**URL:** https://huggingface.co/tencent/Hunyuan-GameCraft-1.0
**Page Title:** tencent/Hunyuan-GameCraft-1.0 · Hugging Face
--------------------


## Hunyuan-GameCraft 🎮

Hunyuan-GameCraft: High-dynamic Interactive Game Video Generation with Hybrid History Condition

## 🔥🔥🔥 News!!

- Aug  14, 2025: 👋 We release the inference code and model weights of Hunyuan-GameCraft. Download .

## 📑 Open-source Plan

- Hunyuan-GameCraft Inference Checkpoints Gradio & Huggingface Demo
- Inference
- Checkpoints
- Gradio & Huggingface Demo

## Contents

- Hunyuan-GameCraft 🌅 🔥🔥🔥 News!! 📑 Open-source Plan Contents Abstract Overall Architecture 📜 Requirements 🛠️ Dependencies and Installation Installation Guide for Linux 🧱 Download Pretrained Models 🚀 Parallel Inference on Multiple GPUs 🔑 Single-gpu Inference Run with very low VRAM Run a Gradio Server 🔗 BibTeX Acknowledgements
- 🔥🔥🔥 News!!
- 📑 Open-source Plan
- Contents
- Abstract
- Overall Architecture
- 📜 Requirements
- 🛠️ Dependencies and Installation Installation Guide for Linux
- Installation Guide for Linux
- 🧱 Download Pretrained Models
- 🚀 Parallel Inference on Multiple GPUs
- 🔑 Single-gpu Inference Run with very low VRAM
- Run with very low VRAM
- Run a Gradio Server
- 🔗 BibTeX
- Acknowledgements

## Abstract

Recent advances in diffusion-based and controllable video generation have enabled high-quality and temporally coherent video synthesis, laying the groundwork for immersive interactive gaming experiences. However, current methods face limitations in dynamics , physically realistic , long-term consistency , and efficiency , which limit the ability to create various gameplay videos. To address these gaps, we introduce Hunyuan-GameCraft, a novel framework for high-dynamic interactive video generation in game environments. To achieve fine-grained action control, we unify standard keyboard and mouse inputs into a shared camera representation space , facilitating smooth interpolation between various camera and movement operations. Then we propose a hybrid history-conditioned training strategy that extends video sequences autoregressively while preserving game scene information. Additionally, to enhance inference efficiency and playability, we achieve model distillation to reduce computational overhead while maintaining consistency across long temporal sequences, making it suitable for real-time deployment in complex interactive environments. The model is trained on a large-scale dataset comprising over one million gameplay recordings across over 100 AAA games, ensuring broad coverage and diversity, then fine-tuned on a carefully annotated synthetic dataset to enhance precision and control. The curated game scene data significantly improves the visual fidelity, realism and action controllability. Extensive experiments demonstrate that Hunyuan-GameCraft significantly outperforms existing models, advancing the realism and playability of interactive game video generation.

## Overall Architecture

Given a reference image and the corresponding prompt, the keyboard or mouse signal, we transform these options to the continuous camera space. Then we design a light-weight action encoder to encode the input camera trajectory. The action and image features are added after patchify. For long video extension, we design a variable mask indicator, where 1 and 0 indicate history frames and predicted frames, respectively.

## 📜 Requirements

- An NVIDIA GPU with CUDA support is required. The model is tested on a machine with 8GPUs. Minimum : The minimum GPU memory required is 24GB but very slow. Recommended : We recommend using a GPU with 80GB of memory for better generation quality.
- The model is tested on a machine with 8GPUs.
- Minimum : The minimum GPU memory required is 24GB but very slow.
- Recommended : We recommend using a GPU with 80GB of memory for better generation quality.
- Tested operating system: Linux

## 🛠️ Dependencies and Installation

Begin by cloning the repository:

### Installation Guide for Linux

We recommend CUDA versions 12.4 for the manual installation.
Conda's installation instructions are available here .
[LINK: here](https://docs.anaconda.com/free/miniconda/index.html)
Additionally, you can also use HunyuanVideo Docker image. Use the following command to pull and run the docker image.

## 🚀 Parallel Inference on Multiple GPUs

For example, to generate a video using 8 GPUs, you can use the following command, where --action-list w s d a simulate keyboard manipulation signals to help you generate a video of the corresponding content. --action-speed-list 0.2 0.2 0.2 0.2 represents the displacement distance and can be replaced with any value between 0 and 3, the length of action-speed-list must be the same as action-list :
Additionally, we support FP8 optimization and SageAttn . To enable FP8, simply add the --use-fp8 to your command. 
And install SageAttention with:
[LINK: SageAttn](https://github.com/thu-ml/SageAttention)
We also provide accelerated model, you can use the following command:

## 🔑 Single-gpu with Low-VRAM Inference

For example, to generate a video with 1 GPU with Low-VRAM (over 24GB), you can use the following command:

## 🔗 BibTeX

If you find Hunyuan-GameCraft useful for your research and applications, please cite using this BibTeX:

## Acknowledgements

We would like to thank the contributors to the HunyuanVideo , HunyuanVideo-Avatar , SD3 , FLUX , Llama , LLaVA , Xtuner , diffusers and HuggingFace repositories, for their open research and exploration.
[LINK: HunyuanVideo](https://github.com/Tencent/HunyuanVideo)
[LINK: HunyuanVideo-Avatar](https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar)
[LINK: FLUX](https://github.com/black-forest-labs/flux)
[LINK: Llama](https://github.com/meta-llama/llama)
[LINK: LLaVA](https://github.com/haotian-liu/LLaVA)
[LINK: Xtuner](https://github.com/InternLM/xtuner)
[LINK: diffusers](https://github.com/huggingface/diffusers)

## Spaces using tencent/Hunyuan-GameCraft-1.0 3

## Paper for tencent/Hunyuan-GameCraft-1.0


--------------------