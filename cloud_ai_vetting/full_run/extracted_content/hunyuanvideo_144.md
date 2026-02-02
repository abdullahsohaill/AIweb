# HunyuanVideo
**URL:** https://huggingface.co/tencent/HunyuanVideo
**Page Title:** tencent/HunyuanVideo · Hugging Face
--------------------


## HunyuanVideo: A Systematic Framework For Large Video Generation Model Training

This repo contains PyTorch model definitions, pre-trained weights and inference/sampling code for our paper exploring HunyuanVideo. You can find more visualizations on our project page .
HunyuanVideo: A Systematic Framework For Large Video Generation Model Training

## News!!

- Jan 13, 2025: 📈 We release the Penguin Video Benchmark .
[LINK: Penguin Video Benchmark](https://github.com/Tencent/HunyuanVideo/blob/main/assets/PenguinVideoBenchmark.csv)
- Dec 18, 2024: 🏃‍♂️ We release the FP8 model weights of HunyuanVideo to save more GPU memory.
- Dec 17, 2024: 🤗 HunyuanVideo has been integrated into Diffusers .
[LINK: Diffusers](https://huggingface.co/docs/diffusers/main/api/pipelines/hunyuan_video)
- Dec 7, 2024: 🚀 We release the parallel inference code for HunyuanVideo powered by xDiT .
[LINK: xDiT](https://github.com/xdit-project/xDiT)
- Dec 3, 2024: 👋 We release the inference code and model weights of HunyuanVideo. Download .
[LINK: Download](https://github.com/Tencent/HunyuanVideo/blob/main/ckpts/README.md)

## Open-source Plan

- HunyuanVideo (Text-to-Video Model) Inference Checkpoints Multi-gpus Sequence Parallel inference (Faster inference speed on more gpus) Web Demo (Gradio) Diffusers FP8 Quantified weight Penguin Video Benchmark ComfyUI
- Inference
- Checkpoints
- Multi-gpus Sequence Parallel inference (Faster inference speed on more gpus)
- Web Demo (Gradio)
- Diffusers
- FP8 Quantified weight
- Penguin Video Benchmark
- ComfyUI
- HunyuanVideo (Image-to-Video Model) Inference Checkpoints
[LINK: HunyuanVideo (Image-to-Video Model)](https://github.com/Tencent/HunyuanVideo-I2V)
- Inference
- Checkpoints

## Contents

- HunyuanVideo: A Systematic Framework For Large Video Generation Model News!! Open-source Plan Contents Abstract HunyuanVideo Overall Architecture HunyuanVideo Key Features Unified Image and Video Generative Architecture MLLM Text Encoder 3D VAE Prompt Rewrite Comparisons Requirements Dependencies and Installation Installation Guide for Linux Download Pretrained Models Single-gpu Inference Using Command Line Run a Gradio Server More Configurations Parallel Inference on Multiple GPUs by xDiT Using Command Line FP8 Inference Using Command Line BibTeX Acknowledgements
- News!!
- Open-source Plan
- Contents
- Abstract
- HunyuanVideo Overall Architecture
- HunyuanVideo Key Features Unified Image and Video Generative Architecture MLLM Text Encoder 3D VAE Prompt Rewrite
- Unified Image and Video Generative Architecture
- MLLM Text Encoder
- 3D VAE
- Prompt Rewrite
- Comparisons
- Requirements
- Dependencies and Installation Installation Guide for Linux
- Installation Guide for Linux
- Download Pretrained Models
- Single-gpu Inference Using Command Line Run a Gradio Server More Configurations
- Using Command Line
- Run a Gradio Server
- More Configurations
- Parallel Inference on Multiple GPUs by xDiT Using Command Line
- Using Command Line
- FP8 Inference Using Command Line
- Using Command Line
- BibTeX
- Acknowledgements

## Abstract

We present HunyuanVideo, a novel open-source video foundation model that exhibits performance in video generation that is comparable to, if not superior to, leading closed-source models. In order to train HunyuanVideo model, we adopt several key technologies for model learning, including data curation, image-video joint model training, and an efficient infrastructure designed to facilitate large-scale model training and inference. Additionally, through an effective strategy for scaling model architecture and dataset, we successfully trained a video generative model with over 13 billion parameters, making it the largest among all open-source models.
We conducted extensive experiments and implemented a series of targeted designs to ensure high visual quality, motion diversity, text-video alignment, and generation stability. According to professional human evaluation results, HunyuanVideo outperforms previous state-of-the-art models, including Runway Gen-3, Luma 1.6, and 3 top-performing Chinese video generative models. By releasing the code and weights of the foundation model and its applications, we aim to bridge the gap between closed-source and open-source video foundation models. This initiative will empower everyone in the community to experiment with their ideas, fostering a more dynamic and vibrant video generation ecosystem.

## HunyuanVideo Overall Architecture

HunyuanVideo is trained on a spatial-temporally
compressed latent space, which is compressed through a Causal 3D VAE. Text prompts are encoded
using a large language model, and used as the conditions. Taking Gaussian noise and the conditions as
input, our generative model produces an output latent, which is then decoded to images or videos through
the 3D VAE decoder.

## HunyuanVideo Key Features

### Unified Image and Video Generative Architecture

HunyuanVideo introduces the Transformer design and employs a Full Attention mechanism for unified image and video generation. 
Specifically, we use a "Dual-stream to Single-stream" hybrid model design for video generation. In the dual-stream phase, video and text
tokens are processed independently through multiple Transformer blocks, enabling each modality to learn its own appropriate modulation mechanisms without interference. In the single-stream phase, we concatenate the video and text
tokens and feed them into subsequent Transformer blocks for effective multimodal information fusion.
This design captures complex interactions between visual and semantic information, enhancing
overall model performance.

### MLLM Text Encoder

Some previous text-to-video models typically use pre-trained CLIP and T5-XXL as text encoders where CLIP uses Transformer Encoder and T5 uses an Encoder-Decoder structure. In contrast, we utilize a pre-trained Multimodal Large Language Model (MLLM) with a Decoder-Only structure as our text encoder, which has the following advantages: (i) Compared with T5, MLLM after visual instruction finetuning has better image-text alignment in the feature space, which alleviates the difficulty of the instruction following in diffusion models; (ii)
Compared with CLIP, MLLM has demonstrated superior ability in image detail description
and complex reasoning; (iii) MLLM can play as a zero-shot learner by following system instructions prepended to user prompts, helping text features pay more attention to key information. In addition, MLLM is based on causal attention while T5-XXL utilizes bidirectional attention that produces better text guidance for diffusion models. Therefore, we introduce an extra bidirectional token refiner to enhance text features.

### 3D VAE

HunyuanVideo trains a 3D VAE with CausalConv3D to compress pixel-space videos and images into a compact latent space. We set the compression ratios of video length, space, and channel to 4, 8, and 16 respectively. This can significantly reduce the number of tokens for the subsequent diffusion transformer model, allowing us to train videos at the original resolution and frame rate.

### Prompt Rewrite

To address the variability in linguistic style and length of user-provided prompts, we fine-tune the Hunyuan-Large model as our prompt rewrite model to adapt the original user prompt to model-preferred prompt.
[LINK: Hunyuan-Large model](https://github.com/Tencent/Tencent-Hunyuan-Large)
We provide two rewrite modes: Normal mode and Master mode, which can be called using different prompts. The prompts are shown here . The Normal mode is designed to enhance the video generation model's comprehension of user intent, facilitating a more accurate interpretation of the instructions provided. The Master mode enhances the description of aspects such as composition, lighting, and camera movement, which leans towards generating videos with a higher visual quality. However, this emphasis may occasionally result in the loss of some semantic details.
The Prompt Rewrite Model can be directly deployed and inferred using the Hunyuan-Large original code . We release the weights of the Prompt Rewrite Model here .
[LINK: Hunyuan-Large original code](https://github.com/Tencent/Tencent-Hunyuan-Large)

## Comparisons

To evaluate the performance of HunyuanVideo, we selected five strong baselines from closed-source video generation models. In total, we utilized 1,533 text prompts, generating an equal number of video samples with HunyuanVideo in a single run. For a fair comparison, we conducted inference only once, avoiding any cherry-picking of results. When comparing with the baseline methods, we maintained the default settings for all selected models, ensuring consistent video resolution. Videos were assessed based on three criteria: Text Alignment, Motion Quality, and Visual Quality. More than 60 professional evaluators performed the evaluation. Notably, HunyuanVideo demonstrated the best overall performance, particularly excelling in motion quality. Please note that the evaluation is based on Hunyuan Video's high-quality version. This is different from the currently released fast version.

## Requirements

The following table shows the requirements for running HunyuanVideo model (batch size = 1) to generate videos:
- An NVIDIA GPU with CUDA support is required. The model is tested on a single 80G GPU. Minimum : The minimum GPU memory required is 60GB for 720px1280px129f and 45G for 544px960px129f. Recommended : We recommend using a GPU with 80GB of memory for better generation quality.
- The model is tested on a single 80G GPU.
- Minimum : The minimum GPU memory required is 60GB for 720px1280px129f and 45G for 544px960px129f.
- Recommended : We recommend using a GPU with 80GB of memory for better generation quality.
- Tested operating system: Linux

## Dependencies and Installation

Begin by cloning the repository:

### Installation Guide for Linux

We recommend CUDA versions 12.4 or 11.8 for the manual installation.
Conda's installation instructions are available here .
[LINK: here](https://docs.anaconda.com/free/miniconda/index.html)
In case of running into float point exception(core dump) on the specific GPU type, you may try the following solutions:
Additionally, HunyuanVideo also provides a pre-built Docker image. Use the following command to pull and run the docker image.

## Download Pretrained Models

The details of download pretrained models are shown here .

## Single-gpu Inference

We list the height/width/frame settings we support in the following table.

### Using Command Line

### Run a Gradio Server

### More Configurations

We list some more useful configurations for easy usage:

## Parallel Inference on Multiple GPUs by xDiT

xDiT is a Scalable Inference Engine for Diffusion Transformers (DiTs) on multi-GPU Clusters.
It has successfully provided low-latency parallel inference solutions for a variety of DiTs models, including mochi-1, CogVideoX, Flux.1, SD3, etc. This repo adopted the Unified Sequence Parallelism (USP) APIs for parallel inference of the HunyuanVideo model.
[LINK: xDiT](https://github.com/xdit-project/xDiT)

### Using Command Line

For example, to generate a video with 8 GPUs, you can use the following command:
You can change the --ulysses-degree and --ring-degree to control the parallel configurations for the best performance. The valid parallel configurations are shown in the following table.

## FP8 Inference

Using HunyuanVideo with FP8 quantized weights, which saves about 10GB of GPU memory. You can download the weights and weight scales from Huggingface.

### Using Command Line

Here, you must explicitly specify the FP8 weight path. For example, to generate a video with fp8 weights, you can use the following command:

## BibTeX

If you find HunyuanVideo useful for your research and applications, please cite using this BibTeX:

## Acknowledgements

We would like to thank the contributors to the SD3 , FLUX , Llama , LLaVA , Xtuner , diffusers and HuggingFace repositories, for their open research and exploration.
Additionally, we also thank the Tencent Hunyuan Multimodal team for their help with the text encoder.
[LINK: FLUX](https://github.com/black-forest-labs/flux)
[LINK: Llama](https://github.com/meta-llama/llama)
[LINK: LLaVA](https://github.com/haotian-liu/LLaVA)
[LINK: Xtuner](https://github.com/InternLM/xtuner)
[LINK: diffusers](https://github.com/huggingface/diffusers)

## Model tree for tencent/HunyuanVideo

## Spaces using tencent/HunyuanVideo 100

## Collection including tencent/HunyuanVideo

## Papers for tencent/HunyuanVideo

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
tencent/HunyuanVideo is supported by the following Inference Providers:

--------------------