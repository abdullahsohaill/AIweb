# Pyramid-flow
**URL:** https://huggingface.co/rain1011/pyramid-flow-sd3
**Page Title:** rain1011/pyramid-flow-sd3 · Hugging Face
--------------------


## ⚡️Pyramid Flow SD3⚡️

[Paper] [Project Page ✨] [Code 🚀] [miniFLUX Model ⚡️] [ demo 🤗 ]
[LINK: [Project Page ✨]](https://pyramid-flow.github.io)
[LINK: [Code 🚀]](https://github.com/jy0205/Pyramid-Flow)
This is the model repository for Pyramid Flow, a training-efficient Autoregressive Video Generation method based on Flow Matching . By training only on open-source datasets, it generates high-quality 10-second videos at 768p resolution and 24 FPS, and naturally supports image-to-video generation.

## News

- 2024.10.29 ⚡️⚡️⚡️ We release training code and new model checkpoints with FLUX structure trained from scratch. We have switched the model structure from SD3 to a mini FLUX to fix human structure issues, please try our 1024p image checkpoint and 384p video checkpoint. We will release 768p video checkpoint in a few days.
2024.10.29 ⚡️⚡️⚡️ We release training code and new model checkpoints with FLUX structure trained from scratch.
[LINK: training code](https://github.com/jy0205/Pyramid-Flow?tab=readme-ov-file#training)
We have switched the model structure from SD3 to a mini FLUX to fix human structure issues, please try our 1024p image checkpoint and 384p video checkpoint. We will release 768p video checkpoint in a few days.
- 2024.10.11 🤗🤗🤗 Hugging Face demo is available. Thanks @multimodalart for the commit!
2024.10.11 🤗🤗🤗 Hugging Face demo is available. Thanks @multimodalart for the commit!
- 2024.10.10 🚀🚀🚀 We release the technical report , project page and model checkpoint of Pyramid Flow.
2024.10.10 🚀🚀🚀 We release the technical report , project page and model checkpoint of Pyramid Flow.
[LINK: project page](https://pyramid-flow.github.io)

## Installation

We recommend setting up the environment with conda. The codebase currently uses Python 3.8.10 and PyTorch 2.1.2, and we are actively working to support a wider range of versions.
Then, download the model from Huggingface (there are two variants: miniFLUX or SD3 ). The miniFLUX models support 1024p image and 384p video generation, and the SD3-based models support 768p and 384p video generation. The 384p checkpoint generates 5-second video at 24FPS, while the 768p checkpoint generates up to 10-second video at 24FPS.

## Usage

For inference, we provide Gradio demo, single-GPU, multi-GPU, and Apple Silicon inference code, as well as VRAM-efficient features such as CPU offloading. Please check our code repository for usage.
[LINK: code repository](https://github.com/jy0205/Pyramid-Flow?tab=readme-ov-file#inference)
Below is a simplified two-step usage procedure. First, load the downloaded model:
Then, you can try text-to-video generation on your own prompts:
As an autoregressive model, our model also supports (text conditioned) image-to-video generation:

## Usage tips

- The guidance_scale parameter controls the visual quality. We suggest using a guidance within [7, 9] for the 768p checkpoint during text-to-video generation, and 7 for the 384p checkpoint.
- The video_guidance_scale parameter controls the motion. A larger value increases the dynamic degree and mitigates the autoregressive generation degradation, while a smaller value stabilizes the video.
- For 10-second video generation, we recommend using a guidance scale of 7 and a video guidance scale of 5.

## Gallery

The following video examples are generated at 5s, 768p, 24fps. For more results, please visit our project page .
[LINK: project page](https://pyramid-flow.github.io)

## Acknowledgement

We are grateful for the following awesome projects when implementing Pyramid Flow:
- SD3 Medium and Flux 1.0 : State-of-the-art image generation models based on flow matching.
- Diffusion Forcing and GameNGen : Next-token prediction meets full-sequence diffusion.
[LINK: GameNGen](https://gamengen.github.io)
- WebVid-10M , OpenVid-1M and Open-Sora Plan : Large-scale datasets for text-to-video generation.
[LINK: WebVid-10M](https://github.com/m-bain/webvid)
[LINK: OpenVid-1M](https://github.com/NJU-PCALab/OpenVid-1M)
[LINK: Open-Sora Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan)
- CogVideoX : An open-source text-to-video generation model that shares many training details.
[LINK: CogVideoX](https://github.com/THUDM/CogVideo)
- Video-LLaMA2 : An open-source video LLM for our video recaptioning.
[LINK: Video-LLaMA2](https://github.com/DAMO-NLP-SG/VideoLLaMA2)

## Citation

Consider giving this repository a star and cite Pyramid Flow in your publications if it helps your research.

## Model tree for rain1011/pyramid-flow-sd3

Base model

## Spaces using rain1011/pyramid-flow-sd3 41

## Paper for rain1011/pyramid-flow-sd3


--------------------