# Qwen2-VL-7B-Instruct
**URL:** https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct
**Page Title:** Qwen/Qwen2-VL-7B-Instruct · Hugging Face
--------------------


## Qwen2-VL-7B-Instruct

## Introduction

We're excited to unveil Qwen2-VL , the latest iteration of our Qwen-VL model, representing nearly a year of innovation.

### What’s New in Qwen2-VL?

- SoTA understanding of images of various resolution & ratio : Qwen2-VL achieves state-of-the-art performance on visual understanding benchmarks, including MathVista, DocVQA, RealWorldQA, MTVQA, etc.
SoTA understanding of images of various resolution & ratio : Qwen2-VL achieves state-of-the-art performance on visual understanding benchmarks, including MathVista, DocVQA, RealWorldQA, MTVQA, etc.
- Understanding videos of 20min+ : Qwen2-VL can understand videos over 20 minutes for high-quality video-based question answering, dialog, content creation, etc.
Understanding videos of 20min+ : Qwen2-VL can understand videos over 20 minutes for high-quality video-based question answering, dialog, content creation, etc.
- Agent that can operate your mobiles, robots, etc. : with the abilities of complex reasoning and decision making, Qwen2-VL can be integrated with devices like mobile phones, robots, etc., for automatic operation based on visual environment and text instructions.
Agent that can operate your mobiles, robots, etc. : with the abilities of complex reasoning and decision making, Qwen2-VL can be integrated with devices like mobile phones, robots, etc., for automatic operation based on visual environment and text instructions.
- Multilingual Support : to serve global users, besides English and Chinese, Qwen2-VL now supports the understanding of texts in different languages inside images, including most European languages, Japanese, Korean, Arabic, Vietnamese, etc.
Multilingual Support : to serve global users, besides English and Chinese, Qwen2-VL now supports the understanding of texts in different languages inside images, including most European languages, Japanese, Korean, Arabic, Vietnamese, etc.
- Naive Dynamic Resolution : Unlike before, Qwen2-VL can handle arbitrary image resolutions, mapping them into a dynamic number of visual tokens, offering a more human-like visual processing experience.
- Multimodal Rotary Position Embedding (M-ROPE) : Decomposes positional embedding into parts to capture 1D textual, 2D visual, and 3D video positional information, enhancing its multimodal processing capabilities.
We have three models with 2, 7 and 72 billion parameters. This repo contains the instruction-tuned 7B Qwen2-VL model. For more information, visit our Blog and GitHub .
[LINK: Blog](https://qwenlm.github.io/blog/qwen2-vl/)
[LINK: GitHub](https://github.com/QwenLM/Qwen2-VL)

## Evaluation

### Image Benchmarks

### Video Benchmarks

## Requirements

The code of Qwen2-VL has been in the latest Hugging face transformers and we advise you to build from source with command pip install git+https://github.com/huggingface/transformers , or you might encounter the following error:

## Quickstart

We offer a toolkit to help you handle various types of visual input more conveniently. This includes base64, URLs, and interleaved images and videos. You can install it using the following command:
Here we show a code snippet to show you how to use the chat model with transformers and qwen_vl_utils :

### More Usage Tips

For input images, we support local files, base64, and URLs. For videos, we currently only support local files.
The model supports a wide range of resolution inputs. By default, it uses the native resolution for input, but higher resolutions can enhance performance at the cost of more computation. Users can set the minimum and maximum number of pixels to achieve an optimal configuration for their needs, such as a token count range of 256-1280, to balance speed and memory usage.
Besides, We provide two methods for fine-grained control over the image size input to the model:
- Define min_pixels and max_pixels: Images will be resized to maintain their aspect ratio within the range of min_pixels and max_pixels.
Define min_pixels and max_pixels: Images will be resized to maintain their aspect ratio within the range of min_pixels and max_pixels.
- Specify exact dimensions: Directly set resized_height and resized_width . These values will be rounded to the nearest multiple of 28.
Specify exact dimensions: Directly set resized_height and resized_width . These values will be rounded to the nearest multiple of 28.

## Limitations

While Qwen2-VL are applicable to a wide range of visual tasks, it is equally important to understand its limitations. Here are some known restrictions:
- Lack of Audio Support: The current model does not comprehend audio information within videos.
- Data timeliness: Our image dataset is updated until June 2023 , and information subsequent to this date may not be covered.
- Constraints in Individuals and Intellectual Property (IP): The model's capacity to recognize specific individuals or IPs is limited, potentially failing to comprehensively cover all well-known personalities or brands.
- Limited Capacity for Complex Instruction: When faced with intricate multi-step instructions, the model's understanding and execution capabilities require enhancement.
- Insufficient Counting Accuracy: Particularly in complex scenes, the accuracy of object counting is not high, necessitating further improvements.
- Weak Spatial Reasoning Skills: Especially in 3D spaces, the model's inference of object positional relationships is inadequate, making it difficult to precisely judge the relative positions of objects.
These limitations serve as ongoing directions for model optimization and improvement, and we are committed to continually enhancing the model's performance and scope of application.

## Citation

If you find our work helpful, feel free to give us a cite.

## Model tree for Qwen/Qwen2-VL-7B-Instruct

Base model

## Spaces using Qwen/Qwen2-VL-7B-Instruct 100

## Collection including Qwen/Qwen2-VL-7B-Instruct

## Papers for Qwen/Qwen2-VL-7B-Instruct

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Qwen/Qwen2-VL-7B-Instruct is supported by the following Inference Providers:

--------------------