# LTX-Video
**URL:** https://huggingface.co/Lightricks/LTX-Video
**Page Title:** Lightricks/LTX-Video · Hugging Face
--------------------


## LTX-Video Model Card

This model card focuses on the model associated with the LTX-Video model, codebase available here .
[LINK: here](https://github.com/Lightricks/LTX-Video)
LTX-Video is the first DiT-based video generation model capable of generating high-quality videos in real-time. It produces 30 FPS videos at a 1216×704 resolution faster than they can be watched. Trained on a large-scale dataset of diverse videos, the model generates high-resolution videos with realistic and varied content.

### Image-to-video examples

## Models & Workflows

[LINK: ltxv-13b-0.9.8-dev.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-13b-0.9.8-dev.yaml)
[LINK: ltxv-13b-i2v-base.json](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/ltxv-13b-i2v-base.json)
[LINK: ltxv-13b-i2v-mixed-multiscale.json](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/ltxv-13b-i2v-mixed-multiscale.json)
[LINK: ltxv-13b-0.9.8-distilled.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-13b-0.9.8-dev.yaml)
[LINK: ltxv-13b-dist-i2v-base.json](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/13b-distilled/ltxv-13b-dist-i2v-base.json)
[LINK: ltxv-2b-0.9.8-distilled.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.8-dev.yaml)
[LINK: ltxv-13b-0.9.8-dev-fp8.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-13b-0.9.8-dev-fp8.yaml)
[LINK: ltxv-13b-i2v-base-fp8.json](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/ltxv-13b-i2v-base-fp8.json)
[LINK: ltxv-13b-0.9.8-distilled-fp8.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-13b-0.9.8-distilled-fp8.yaml)
[LINK: ltxv-13b-dist-i2v-base-fp8.json](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/13b-distilled/ltxv-13b-dist-i2v-base-fp8.json)
[LINK: ltxv-2b-0.9.8-distilled-fp8.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.8-distilled-fp8.yaml)
[LINK: ltxv-2b-0.9.6-dev.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-dev.yaml)
[LINK: ltxvideo-i2v.json](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/low_level/ltxvideo-i2v.json)
[LINK: ltxv-2b-0.9.6-distilled.yaml](https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-distilled.yaml)
[LINK: ltxvideo-i2v-distilled.json](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/low_level/ltxvideo-i2v-distilled.json)

## Model Details

- Developed by: Lightricks
- Model type: Diffusion-based image-to-video generation model
- Language(s): English

## Usage

### Direct use

You can use the model for purposes under the license:
- 2B version 0.9: license
- 2B version 0.9.1 license
- 2B version 0.9.5 license
- 2B version 0.9.6-dev license
- 2B version 0.9.6-distilled license
- 13B version 0.9.7-dev license
- 13B version 0.9.7-dev-fp8 license
- 13B version 0.9.7-distilled license
- 13B version 0.9.7-distilled-fp8 license
- 13B version 0.9.7-distilled-lora128 license
- 13B version 0.9.7-ICLoRA Depth license
- 13B version 0.9.7-ICLoRA Pose license
- 13B version 0.9.7-ICLoRA Canny license
- Temporal upscaler version 0.9.7 license
- Spatial upscaler version 0.9.7 license
- 13B version 0.9.8-dev license
- 13B version 0.9.8-dev-fp8 license
- 13B version 0.9.8-distilled license
- 13B version 0.9.8-distilled-fp8 license
- 2B version 0.9.8-distilled license
- 2B version 0.9.8-distilled-fp8 license
- 13B version 0.9.8-ICLoRA detailer license
- Temporal upscaler version 0.9.8 license
- Spatial upscaler version 0.9.8 license

### General tips:

- The model works on resolutions that are divisible by 32 and number of frames that are divisible by 8 + 1 (e.g. 257). In case the resolution or number of frames are not divisible by 32 or 8 + 1, the input will be padded with -1 and then cropped to the desired resolution and number of frames.
- The model works best on resolutions under 720 x 1280 and number of frames below 257.
- Prompts should be in English. The more elaborate the better. Good prompt looks like The turquoise waves crash against the dark, jagged rocks of the shore, sending white foam spraying into the air. The scene is dominated by the stark contrast between the bright blue water and the dark, almost black rocks. The water is a clear, turquoise color, and the waves are capped with white foam. The rocks are dark and jagged, and they are covered in patches of green moss. The shore is lined with lush green vegetation, including trees and bushes. In the background, there are rolling hills covered in dense forest. The sky is cloudy, and the light is dim.

### Online demo

The model is accessible right away via the following links:
- LTX-Studio image-to-video (13B-mix)
- LTX-Studio image-to-video (13B distilled)
- Fal.ai image-to-video (13B full)
- Fal.ai image-to-video (13B distilled)
- Replicate image-to-video

### ComfyUI

To use our model with ComfyUI, please follow the instructions at a dedicated ComfyUI repo .
[LINK: ComfyUI repo](https://github.com/Lightricks/ComfyUI-LTXVideo/)

### Run locally

The codebase was tested with Python 3.10.5, CUDA version 12.2, and supports PyTorch >= 2.1.2.
To use our model, please follow the inference code in inference.py :
[LINK: inference.py](https://github.com/Lightricks/LTX-Video/blob/main/inference.py)
You can now generate a video conditioned on a set of images and/or short video segments.
Simply provide a list of paths to the images or video segments you want to condition on, along with their target frame numbers in the generated video. You can also specify the conditioning strength for each item (default: 1.0).

### Diffusers 🧨

LTX Video is compatible with the Diffusers Python library for image-to-video generation.
[LINK: Diffusers Python library](https://huggingface.co/docs/diffusers/main/en/index)
Make sure you install diffusers before trying out the examples below.
Now, you can run the examples below (note that the upsampling stage is optional but reccomeneded):

### For image-to-video:

### For video-to-video:

To learn more, check out the official documentation .
[LINK: official documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx_video)
Diffusers also supports directly loading from the original LTX checkpoints using the from_single_file() method. Check out this section to learn more.
[LINK: this section](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx_video#loading-single-files)

## Limitations

- This model is not intended or able to provide factual information.
- As a statistical model this checkpoint might amplify existing societal biases.
- The model may fail to generate videos that matches the prompts perfectly.
- Prompt following is heavily influenced by the prompting-style.

## Model tree for Lightricks/LTX-Video

## Spaces using Lightricks/LTX-Video 100

## Collection including Lightricks/LTX-Video

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Lightricks/LTX-Video is supported by the following Inference Providers:

--------------------