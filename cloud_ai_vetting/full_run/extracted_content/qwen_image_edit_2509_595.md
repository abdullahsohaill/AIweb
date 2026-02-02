# Qwen-Image-Edit-2509
**URL:** https://huggingface.co/Qwen/Qwen-Image-Edit-2509
**Page Title:** Qwen/Qwen-Image-Edit-2509 · Hugging Face
--------------------

💜 Qwen Chat |   🤗 Hugging Face |   🤖 ModelScope |    📑 Tech Report |    📑 Blog 🖥️ Demo |   💬 WeChat (微信) |   🫨 Discord | Github
[LINK: Blog](https://qwenlm.github.io/blog/qwen-image-edit/)
[LINK: WeChat (微信)](https://github.com/QwenLM/Qwen-Image/blob/main/assets/wechat.png)
[LINK: Github](https://github.com/QwenLM/Qwen-Image)

## Introduction

This September, we are pleased to introduce Qwen-Image-Edit-2509, the monthly iteration of Qwen-Image-Edit. To experience the latest model, please visit Qwen Chat and select the "Image Editing" feature.
Compared with Qwen-Image-Edit released in August, the main improvements of Qwen-Image-Edit-2509 include:
- Multi-image Editing Support : For multi-image inputs, Qwen-Image-Edit-2509 builds upon the Qwen-Image-Edit architecture and is further trained via image concatenation to enable multi-image editing. It supports various combinations such as "person + person," "person + product," and "person + scene." Optimal performance is currently achieved with 1 to 3 input images.
- Enhanced Single-image Consistency : For single-image inputs, Qwen-Image-Edit-2509 significantly improves editing consistency, specifically in the following areas: Improved Person Editing Consistency : Better preservation of facial identity, supporting various portrait styles and pose transformations; Improved Product Editing Consistency : Better preservation of product identity, supporting product poster editing； Improved Text Editing Consistency : In addition to modifying text content, it also supports editing text fonts, colors, and materials；
- Improved Person Editing Consistency : Better preservation of facial identity, supporting various portrait styles and pose transformations;
- Improved Product Editing Consistency : Better preservation of product identity, supporting product poster editing；
- Improved Text Editing Consistency : In addition to modifying text content, it also supports editing text fonts, colors, and materials；
- Native Support for ControlNet : Including depth maps, edge maps, keypoint maps, and more.

## Quick Start

Install the latest version of diffusers
The following contains a code snippet illustrating how to use Qwen-Image-Edit-2509 :

## Showcase

The primary update in Qwen-Image-Edit-2509 is support for multi-image inputs.
Let’s first look at a "person + person" example:
Here is a "person + scene" example:
Below is a "person + object" example:
In fact, multi-image input also supports commonly used ControlNet keypoint maps—for example, changing a person’s pose:
Similarly, the following examples demonstrate results using three input images:
Another major update in Qwen-Image-Edit-2509 is enhanced consistency.
First, regarding person consistency, Qwen-Image-Edit-2509 shows significant improvement over Qwen-Image-Edit. Below are examples generating various portrait styles:
For instance, changing a person’s pose while maintaining excellent identity consistency:
Leveraging this improvement along with Qwen-Image’s unique text rendering capability, we find that Qwen-Image-Edit-2509 excels at creating meme images:
Of course, even with longer text, Qwen-Image-Edit-2509 can still render it while preserving the person’s identity:
Person consistency is also evident in old photo restoration. Below are two examples:
Naturally, besides real people, generating cartoon characters and cultural creations is also possible:
Second, Qwen-Image-Edit-2509 specifically enhances product consistency. We find that the model can naturally generate product posters from plain-background product images:
Or even simple logos:
Third, Qwen-Image-Edit-2509 specifically enhances text consistency and supports editing font type, font color, and font material:
Moreover, the ability for precise text editing has been significantly enhanced:
It is worth noting that text editing can often be seamlessly integrated with image editing—for example, in this poster editing case:
The final update in Qwen-Image-Edit-2509 is native support for commonly used ControlNet image conditions, such as keypoint control and sketches:

## License Agreement

Qwen-Image is licensed under Apache 2.0.

## Citation

We kindly encourage citation of our work if you find it useful.

## Model tree for Qwen/Qwen-Image-Edit-2509

## Spaces using Qwen/Qwen-Image-Edit-2509 100

## Collection including Qwen/Qwen-Image-Edit-2509

## Paper for Qwen/Qwen-Image-Edit-2509

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Qwen/Qwen-Image-Edit-2509 is supported by the following Inference Providers:

--------------------