# Qwen2.5-VL-7B-Instruct
**URL:** https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
**Page Title:** Qwen/Qwen2.5-VL-7B-Instruct · Hugging Face
--------------------


## Qwen2.5-VL-7B-Instruct

## Introduction

In the past five months since Qwen2-VL’s release, numerous developers have built new models on the Qwen2-VL vision-language models, providing us with valuable feedback. During this period, we focused on building more useful vision-language models. Today, we are excited to introduce the latest addition to the Qwen family: Qwen2.5-VL.
- Understand things visually : Qwen2.5-VL is not only proficient in recognizing common objects such as flowers, birds, fish, and insects, but it is highly capable of analyzing texts, charts, icons, graphics, and layouts within images.
Understand things visually : Qwen2.5-VL is not only proficient in recognizing common objects such as flowers, birds, fish, and insects, but it is highly capable of analyzing texts, charts, icons, graphics, and layouts within images.
- Being agentic : Qwen2.5-VL directly plays as a visual agent that can reason and dynamically direct tools, which is capable of computer use and phone use.
Being agentic : Qwen2.5-VL directly plays as a visual agent that can reason and dynamically direct tools, which is capable of computer use and phone use.
- Understanding long videos and capturing events : Qwen2.5-VL can comprehend videos of over 1 hour, and this time it has a new ability of cpaturing event by pinpointing the relevant video segments.
Understanding long videos and capturing events : Qwen2.5-VL can comprehend videos of over 1 hour, and this time it has a new ability of cpaturing event by pinpointing the relevant video segments.
- Capable of visual localization in different formats : Qwen2.5-VL can accurately localize objects in an image by generating bounding boxes or points, and it can provide stable JSON outputs for coordinates and attributes.
Capable of visual localization in different formats : Qwen2.5-VL can accurately localize objects in an image by generating bounding boxes or points, and it can provide stable JSON outputs for coordinates and attributes.
- Generating structured outputs : for data like scans of invoices, forms, tables, etc. Qwen2.5-VL supports structured outputs of their contents, benefiting usages in finance, commerce, etc.
Generating structured outputs : for data like scans of invoices, forms, tables, etc. Qwen2.5-VL supports structured outputs of their contents, benefiting usages in finance, commerce, etc.
- Dynamic Resolution and Frame Rate Training for Video Understanding :
We extend dynamic resolution to the temporal dimension by adopting dynamic FPS sampling, enabling the model to comprehend videos at various sampling rates. Accordingly, we update mRoPE in the time dimension with IDs and absolute time alignment, enabling the model to learn temporal sequence and speed, and ultimately acquire the ability to pinpoint specific moments.
- Streamlined and Efficient Vision Encoder
We enhance both training and inference speeds by strategically implementing window attention into the ViT. The ViT architecture is further optimized with SwiGLU and RMSNorm, aligning it with the structure of the Qwen2.5 LLM.
We have three models with 3, 7 and 72 billion parameters. This repo contains the instruction-tuned 7B Qwen2.5-VL model. For more information, visit our Blog and GitHub .
[LINK: Blog](https://qwenlm.github.io/blog/qwen2.5-vl/)
[LINK: GitHub](https://github.com/QwenLM/Qwen2.5-VL)

## Evaluation

### Image benchmark

### Video Benchmarks

### Agent benchmark

## Requirements

The code of Qwen2.5-VL has been in the latest Hugging face transformers and we advise you to build from source with command:
or you might encounter the following error:

## Quickstart

Below, we provide simple examples to show how to use Qwen2.5-VL with 🤖 ModelScope and 🤗 Transformers.
The code of Qwen2.5-VL has been in the latest Hugging face transformers and we advise you to build from source with command:
or you might encounter the following error:
We offer a toolkit to help you handle various types of visual input more conveniently, as if you were using an API. This includes base64, URLs, and interleaved images and videos. You can install it using the following command:
If you are not using Linux, you might not be able to install decord from PyPI. In that case, you can use pip install qwen-vl-utils which will fall back to using torchvision for video processing. However, you can still install decord from source to get decord used when loading video.
[LINK: install decord from source](https://github.com/dmlc/decord?tab=readme-ov-file#install-from-source)

### Using 🤗  Transformers to Chat

Here we show a code snippet to show you how to use the chat model with transformers and qwen_vl_utils :
Video URL compatibility largely depends on the third-party library version. The details are in the table below. change the backend by FORCE_QWENVL_VIDEO_READER=torchvision or FORCE_QWENVL_VIDEO_READER=decord if you prefer not to use the default one.

### 🤖 ModelScope

We strongly advise users especially those in mainland China to use ModelScope. snapshot_download can help you solve issues concerning downloading checkpoints.

### More Usage Tips

For input images, we support local files, base64, and URLs. For videos, we currently only support local files.
The model supports a wide range of resolution inputs. By default, it uses the native resolution for input, but higher resolutions can enhance performance at the cost of more computation. Users can set the minimum and maximum number of pixels to achieve an optimal configuration for their needs, such as a token count range of 256-1280, to balance speed and memory usage.
Besides, We provide two methods for fine-grained control over the image size input to the model:
- Define min_pixels and max_pixels: Images will be resized to maintain their aspect ratio within the range of min_pixels and max_pixels.
Define min_pixels and max_pixels: Images will be resized to maintain their aspect ratio within the range of min_pixels and max_pixels.
- Specify exact dimensions: Directly set resized_height and resized_width . These values will be rounded to the nearest multiple of 28.
Specify exact dimensions: Directly set resized_height and resized_width . These values will be rounded to the nearest multiple of 28.

### Processing Long Texts

The current config.json is set for context length up to 32,768 tokens.
To handle extensive inputs exceeding 32,768 tokens, we utilize YaRN , a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts.
For supported frameworks, you could add the following to config.json to enable YaRN:
{
    ...,
    "type": "yarn",
    "mrope_section": [
        16,
        24,
        24
    ],
    "factor": 4,
    "original_max_position_embeddings": 32768
}
However, it should be noted that this method has a significant impact on the performance of temporal and spatial localization tasks, and is therefore not recommended for use.
At the same time, for long video inputs, since MRoPE itself is more economical with ids, the max_position_embeddings can be directly modified to a larger value, such as 64k.

## Citation

If you find our work helpful, feel free to give us a cite.

## Model tree for Qwen/Qwen2.5-VL-7B-Instruct

## Spaces using Qwen/Qwen2.5-VL-7B-Instruct 100

## Collection including Qwen/Qwen2.5-VL-7B-Instruct

## Papers for Qwen/Qwen2.5-VL-7B-Instruct

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Qwen/Qwen2.5-VL-7B-Instruct is supported by the following Inference Providers:

--------------------