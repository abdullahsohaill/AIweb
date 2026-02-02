# https://huggingface.co/dog-god/texture-synthesis-sdxl-lora
**URL:** https://huggingface.co/dog-god/texture-synthesis-sdxl-lora
**Page Title:** dog-god/texture-synthesis-sdxl-lora · Hugging Face
--------------------


## Material Synthesis With SDXL

NOTE: The Inference API uses the 3D model by default, so if you want to generate 2D textures you may want to clone to a space or run the model yourself.

## Model description

This is a SDXL LoRA specifically designed for generating material textures, as well as images of 3D objects with the textures already applied to them.
It's recommended to use controlnet for maximum consistency between images.
The model is already in a standard safetensors format, and can be readily used in A1111, ComfyUI, or any other model inference API of your choosing.
This model is part of the "Material synthesis with diffusion models" project by Artemiy Zhukov.

## Trigger words

To represent different texture types, the model uses a two-token system for the type of texture.
heighmap - height texture
colormap - albedo texture
roughmap - roughness texture
normalmap - normal texture
specmap - specular texture
ambmap - ambient occlusion texture
metalmap - metallic texture
Here are some examples of the 3D model in action (although you may want to use the base if you just want top-down textures)

## Model tree for dog-god/texture-synthesis-sdxl-lora

Base model

## Spaces using dog-god/texture-synthesis-sdxl-lora 3

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
dog-god/texture-synthesis-sdxl-lora is supported by the following Inference Providers:

--------------------