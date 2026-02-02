# HunyuanImage-2.1
**URL:** https://huggingface.co/tencent/HunyuanImage-2.1
**Page Title:** tencent/HunyuanImage-2.1 · Hugging Face
--------------------

中文阅读

## HunyuanImage-2.1: An Efficient Diffusion Model for High-Resolution (2K) Text-to-Image Generation​

👋 Join our WeChat
[LINK: WeChat](https://github.com/Tencent-Hunyuan/HunyuanImage-2.1/blob/main/assets/WECHAT.md)
This repo contains PyTorch model definitions, pretrained weights and inference/sampling code for our HunyuanImage-2.1. You can find more visualizations on our project page .

## 🔥🔥🔥 Latest Updates

- September 12, 2025: 🚀 Released FP8 quantized models! Making it possible to generate 2K images with only 24GB GPU memory!
- September 8, 2025: 🚀 Released inference code and model weights for HunyuanImage-2.1.

## 🎥 Demo

## Contents

- HunyuanImage-2.1: An Efficient Diffusion Model for High-Resolution (2K) Text-to-Image Generation​ 🔥🔥🔥 Latest Updates 🎥 Demo Contents Abstract HunyuanImage-2.1 Overall Pipeline Training Data and Caption Text-to-Image Model Architecture Reinforcement Learning from Human Feedback Rewriting Model Model distillation 🎉 HunyuanImage-2.1 Key Features Prompt Enhanced Demo 📈 Comparisons SSAE Evaluation GSB Evaluation 📜 System Requirements 🛠️ Dependencies and Installation 🧱 Download Pretrained Models 🔑 Usage 🔗 BibTeX Acknowledgements Github Star History
- 🔥🔥🔥 Latest Updates
- 🎥 Demo
- Contents
- Abstract
- HunyuanImage-2.1 Overall Pipeline Training Data and Caption Text-to-Image Model Architecture Reinforcement Learning from Human Feedback Rewriting Model Model distillation
- Training Data and Caption
- Text-to-Image Model Architecture
- Reinforcement Learning from Human Feedback
- Rewriting Model
- Model distillation
- 🎉 HunyuanImage-2.1 Key Features
- Prompt Enhanced Demo
- 📈 Comparisons SSAE Evaluation GSB Evaluation
- SSAE Evaluation
- GSB Evaluation
- 📜 System Requirements
- 🛠️ Dependencies and Installation
- 🧱 Download Pretrained Models
- 🔑 Usage
- 🔗 BibTeX
- Acknowledgements
- Github Star History
[LINK: Github Star History](#github-star-history)

## Abstract

We present HunyuanImage-2.1, a highly efficient text-to-image model that is capable of generating 2K (2048 × 2048) resolution images. Leveraging an extensive dataset and structured captions involving multiple expert models, we significantly enhance text-image alignment capabilities. The model employs a highly expressive VAE with a (32 × 32) spatial compression ratio, substantially reducing computational costs.
Our architecture consists of two stages:
- ​Base text-to-image Model:​​ The first stage is a text-to-image model that utilizes two text encoders: a multimodal large language model (MLLM) to improve image-text alignment, and a multi-language, character-aware encoder to enhance text rendering across various languages. This stage features a single- and dual-stream diffusion transformer with 17 billion parameters. To optimize aesthetics and structural coherence, we apply reinforcement learning from human feedback (RLHF).
- Refiner Model: The second stage introduces a refiner model that further enhances image quality and clarity, while minimizing artifacts.
Additionally, we developed the PromptEnhancer module to further boost model performance, and employed meanflow distillation for efficient inference. HunyuanImage-2.1 demonstrates robust semantic alignment and cross-scenario generalization, leading to improved consistency between text and image, enhanced control of scene details, character poses, and expressions, and the ability to generate multiple objects with distinct descriptions.

## HunyuanImage-2.1 Overall Pipeline

### Training Data and Caption

Structured captions provide hierarchical semantic information at short, medium, long, and extra-long levels, significantly enhancing the model’s responsiveness to complex semantics. Innovatively, an OCR agent and IP RAG are introduced to address the shortcomings of general VLM captioners in dense text and world knowledge descriptions, while a bidirectional verification strategy ensures caption accuracy.

### Text-to-Image Model Architecture

Core Components:
- High-Compression VAE with REPA Training Acceleration: A VAE with a 32× compression rate drastically reduces the number of input tokens for the DiT model. By aligning its feature space with DINOv2 features, we facilitate the training of high-compression VAEs. As a result, our model generates 2K images with the same token length (and thus similar inference time) as other models require for 1K images, achieving superior inference efficiency. Multi-bucket, multi-resolution REPA loss aligns DiT features with a high-dimensional semantic feature space, accelerating model convergence.
- A VAE with a 32× compression rate drastically reduces the number of input tokens for the DiT model. By aligning its feature space with DINOv2 features, we facilitate the training of high-compression VAEs. As a result, our model generates 2K images with the same token length (and thus similar inference time) as other models require for 1K images, achieving superior inference efficiency.
- Multi-bucket, multi-resolution REPA loss aligns DiT features with a high-dimensional semantic feature space, accelerating model convergence.
- Dual Text Encoder: A vision-language multimodal encoder is employed to better understand scene descriptions, character actions, and detailed requirements. A multilingual ByT5 text encoder is introduced to specialize in text generation and multilingual expression.
- A vision-language multimodal encoder is employed to better understand scene descriptions, character actions, and detailed requirements.
- A multilingual ByT5 text encoder is introduced to specialize in text generation and multilingual expression.
- Network: A single- and dual-stream diffusion transformer with 17 billion parameters.

### Reinforcement Learning from Human Feedback

Two-Stage Post-Training with Reinforcement Learning: Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) are applied sequentially in two post-training stages. We introduce a Reward Distribution Alignment algorithm, which innovatively incorporates high-quality images as selected samples to ensure stable and improved reinforcement learning outcomes.

### Rewriting Model

- The first systematic industrial-level rewriting model. SFT training structurally rewrites user text instructions to enrich visual expression, while GRPO training employs a fine-grained semantic AlignEvaluator reward model to substantially improve the semantics of images generated from rewritten text. The AlignEvaluator covers 6 major categories and 24 fine-grained assessment points. PromptEnhancer supports both Chinese and English rewriting and demonstrates general applicability in enhancing semantics for both open-source and proprietary text-to-image models.

### Model distillation

We propose a novel distillation method based on meanflow that addresses the key challenges of instability and inefficiency inherent in standard meanflow training. This approach enables high-quality image generation with only a few sampling steps. To our knowledge, this is the first successful application of meanflow to an industrial-scale model.

## 🎉 HunyuanImage-2.1 Key Features

- High-Quality Generation : Efficiently produces ultra-high-definition (2K) images with cinematic composition.
- Multilingual Support : Provides native support for both Chinese and English prompts.
- Advanced Architecture : Built on a multi-modal, single- and dual-stream combined DiT (Diffusion Transformer) backbone.
- Glyph-Aware Processing : Utilizes ByT5's text rendering capabilities for improved text generation accuracy.
- Flexible Aspect Ratios : Supports a variety of image aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3).
- Prompt Enhancement : Automatically rewrites prompts to improve descriptive accuracy and visual quality.

## Prompt Enhanced Demo

To improve the quality and detail of generated images, we use a prompt rewriting model. This model automatically enhances user-provided text prompts by adding detailed and descriptive information.

## 📈 Comparisons

### SSAE Evaluation

SSAE (Structured Semantic Alignment Evaluation) is an intelligent evaluation metric for image-text alignment based on advanced multimodal large language models (MLLMs). We extracted 3500 key points across 12 categories, then used multimodal large language models to automatically evaluate and score by comparing the generated images with these key points based on the visual content of the images. Mean Image Accuracy represents the image-wise average score across all key points, while Global Accuracy directly calculates the average score across all key points.
From the SSAE evaluation results, our model has currently achieved the optimal performance among open-source models in terms of semantic alignment, and is very close to the performance of closed-source commercial models (GPT-Image).

### GSB Evaluation

We adopted the GSB evaluation method commonly used to assess the relative performance between two models from an overall image perception perspective. In total, we utilized 1000 text prompts, generating an equal number of image samples for all compared models in a single run. For a fair comparison, we conducted inference only once for each prompt, avoiding any cherry-picking of results. When comparing with the baseline methods, we maintained the default settings for all selected models. The evaluation was performed by more than 100 professional evaluators.
From the results, HunyuanImage 2.1 achieved a relative win rate of -1.36% against Seedream3.0 (closed-source) and 2.89% outperforming Qwen-Image (open-source). The GSB evaluation results demonstrate that HunyuanImage 2.1, as an open-source model, has reached a level of image generation quality comparable to closed-source commercial models (Seedream3.0), while showing certain advantages in comparison with similar open-source models (Qwen-Image). This fully validates the technical advancement and practical value of HunyuanImage 2.1 in text-to-image generation tasks.

## 📜 System Requirements

Hardware and OS Requirements:
- NVIDIA GPU with CUDA support. Minimum requrement for now: 24 GB GPU memory for 2048x2048 image generation. Note: The memory requirements above are measured with model CPU offloading and FP8 quantization enabled. If your GPU has sufficient memory, you may disable offloading for improved inference speed.
NVIDIA GPU with CUDA support.
Minimum requrement for now: 24 GB GPU memory for 2048x2048 image generation.
Note: The memory requirements above are measured with model CPU offloading and FP8 quantization enabled. If your GPU has sufficient memory, you may disable offloading for improved inference speed.
- Supported operating system: Linux.
Supported operating system: Linux.

## 🛠️ Dependencies and Installation

- Clone the repository:
- Install dependencies:

## 🧱 Download Pretrained Models

The details of download pretrained models are shown here .

## 🔑 Usage

HunyuanImage-2.1 only supports 2K image generation (e.g. 2048x2048 for 1:1 images, 2560x1536 for 16:9 images, etc.).
Generating images with 1K resolution will result in artifacts.
Additionally, we recommend using the full generation pipeline for better quality (i.e. enabling prompt enhancement and refinment).

## 🔗 BibTeX

If you find this project useful for your research and applications, please cite as:

## Acknowledgements

We would like to thank the following open-source projects and communities for their contributions to open research and exploration: Qwen , FLUX , diffusers and HuggingFace .
[LINK: FLUX](https://github.com/black-forest-labs/flux)
[LINK: diffusers](https://github.com/huggingface/diffusers)

## Github Star History

## Model tree for tencent/HunyuanImage-2.1

## Spaces using tencent/HunyuanImage-2.1 19

## Collection including tencent/HunyuanImage-2.1

## Paper for tencent/HunyuanImage-2.1

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
tencent/HunyuanImage-2.1 is supported by the following Inference Providers:

--------------------