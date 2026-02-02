# SDXL-Lightning
**URL:** https://huggingface.co/ByteDance/SDXL-Lightning
**Page Title:** ByteDance/SDXL-Lightning · Hugging Face
--------------------


## SDXL-Lightning

SDXL-Lightning is a lightning-fast text-to-image generation model. It can generate high-quality 1024px images in a few steps. For more information, please refer to our research paper: SDXL-Lightning: Progressive Adversarial Diffusion Distillation . We open-source the model as part of the research.
Our models are distilled from stabilityai/stable-diffusion-xl-base-1.0 . This repository contains checkpoints for 1-step, 2-step, 4-step, and 8-step distilled models. The generation quality of our 2-step, 4-step, and 8-step model is amazing. Our 1-step model is more experimental.
We provide both full UNet and LoRA checkpoints. The full UNet models have the best quality while the LoRA models can be applied to other base models.

## Demos

- Generate with all configurations, best quality: Demo

## Checkpoints

- sdxl_lightning_Nstep.safetensors : All-in-one checkpoint, for ComfyUI.
- sdxl_lightning_Nstep_unet.safetensors : UNet checkpoint only, for Diffusers.
- sdxl_lightning_Nstep_lora.safetensors : LoRA checkpoint, for Diffusers and ComfyUI.

## Diffusers Usage

Please always use the correct checkpoint for the corresponding inference steps.

### 2-Step, 4-Step, 8-Step UNet

### 2-Step, 4-Step, 8-Step LoRA

Use LoRA only if you are using non-SDXL base models. Otherwise use our UNet checkpoint for better quality.

### 1-Step UNet

The 1-step model is only experimental and the quality is much less stable. Consider using the 2-step model for much better quality.
The 1-step model uses "sample" prediction instead of "epsilon" prediction! The scheduler needs to be configured correctly.

## ComfyUI Usage

Please always use the correct checkpoint for the corresponding inference steps.
Please use Euler sampler with sgm_uniform scheduler.

### 2-Step, 4-Step, 8-Step Full

- Download the full checkpoint ( sdxl_lightning_Nstep.safetensors ) to /ComfyUI/models/checkpoints .
- Download our ComfyUI full workflow .

### 2-Step, 4-Step, 8-Step LoRA

Use LoRA only if you are using non-SDXL base models. Otherwise use our full checkpoint for better quality.
- Prepare your own base model.
- Download the LoRA checkpoint ( sdxl_lightning_Nstep_lora.safetensors ) to /ComfyUI/models/loras
- Download our ComfyUI LoRA workflow .

### 1-Step

The 1-step model is only experimental and the quality is much less stable. Consider using the 2-step model for much better quality.
- Update your ComfyUI to the latest version.
- Download the full checkpoint ( sdxl_lightning_1step_x0.safetensors ) to /ComfyUI/models/checkpoints .
- Download our ComfyUI full 1-step workflow .

## Cite Our Work

## Model tree for ByteDance/SDXL-Lightning

## Spaces using ByteDance/SDXL-Lightning 100

## Paper for ByteDance/SDXL-Lightning

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
ByteDance/SDXL-Lightning is supported by the following Inference Providers:

--------------------