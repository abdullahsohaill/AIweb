# InternVL2-26B
**URL:** https://huggingface.co/OpenGVLab/InternVL2-26B
**Page Title:** OpenGVLab/InternVL2-26B · Hugging Face
--------------------


## InternVL2-26B

[📂 GitHub] [📜 InternVL 1.0] [📜 InternVL 1.5] [📜 Mini-InternVL] [📜 InternVL 2.5]
[LINK: [📂 GitHub]](https://github.com/OpenGVLab/InternVL)
[🆕 Blog] [🗨️ Chat Demo] [🤗 HF Demo] [🚀 Quick Start] [📖 Documents]
[LINK: [🆕 Blog]](https://internvl.github.io/blog/)
[LINK: [📖 Documents]](https://internvl.readthedocs.io/en/latest/)

## Introduction

We are excited to announce the release of InternVL 2.0, the latest addition to the InternVL series of multimodal large language models. InternVL 2.0 features a variety of instruction-tuned models , ranging from 1 billion to 108 billion parameters. This repository contains the instruction-tuned InternVL2-26B model.
Compared to the state-of-the-art open-source multimodal large language models, InternVL 2.0 surpasses most open-source models. It demonstrates competitive performance on par with proprietary commercial models across various capabilities, including document and chart comprehension, infographics QA, scene text understanding and OCR tasks, scientific and mathematical problem solving, as well as cultural understanding and integrated multimodal capabilities.
InternVL 2.0 is trained with an 8k context window and utilizes training data consisting of long texts, multiple images, and videos, significantly improving its ability to handle these types of inputs compared to InternVL 1.5. For more details, please refer to our blog and GitHub .
[LINK: blog](https://internvl.github.io/blog/2024-07-02-InternVL-2.0/)
[LINK: GitHub](https://github.com/OpenGVLab/InternVL)

## Model Details

InternVL 2.0 is a multimodal large language model series, featuring models of various sizes. For each size, we release instruction-tuned models optimized for multimodal tasks. InternVL2-26B consists of InternViT-6B-448px-V1-5 , an MLP projector, and internlm2-chat-20b .

## Performance

### Image Benchmarks

- For more details and evaluation reproduction, please refer to our Evaluation Guide .
For more details and evaluation reproduction, please refer to our Evaluation Guide .
[LINK: Evaluation Guide](https://internvl.readthedocs.io/en/latest/internvl2.0/evaluation.html)
- We simultaneously use InternVL and VLMEvalKit repositories for model evaluation. Specifically, the results reported for DocVQA, ChartQA, InfoVQA, TextVQA, MME, AI2D, MMBench, CCBench, MMVet (GPT-4-0613), and SEED-Image were tested using the InternVL repository. MMMU, OCRBench, RealWorldQA, HallBench, MMVet (GPT-4-Turbo), and MathVista were evaluated using the VLMEvalKit.
We simultaneously use InternVL and VLMEvalKit repositories for model evaluation. Specifically, the results reported for DocVQA, ChartQA, InfoVQA, TextVQA, MME, AI2D, MMBench, CCBench, MMVet (GPT-4-0613), and SEED-Image were tested using the InternVL repository. MMMU, OCRBench, RealWorldQA, HallBench, MMVet (GPT-4-Turbo), and MathVista were evaluated using the VLMEvalKit.
[LINK: InternVL](https://github.com/OpenGVLab/InternVL)
[LINK: VLMEvalKit](https://github.com/open-compass/VLMEvalKit)

### Video Benchmarks

- We evaluate our models on MVBench and Video-MME by extracting 16 frames from each video, and each frame was resized to a 448x448 image.

### Grounding Benchmarks

- We use the following prompt to evaluate InternVL's grounding ability: Please provide the bounding box coordinates of the region this sentence describes: <ref>{}</ref>
Limitations: Although we have made efforts to ensure the safety of the model during the training process and to encourage the model to generate text that complies with ethical and legal requirements, the model may still produce unexpected outputs due to its size and probabilistic generation paradigm. For example, the generated responses may contain biases, discrimination, or other harmful content. Please do not propagate such content. We are not responsible for any consequences resulting from the dissemination of harmful information.

## Quick Start

We provide an example code to run InternVL2-26B using transformers .
Please use transformers>=4.37.2 to ensure the model works normally.

### Model Loading

The reason for writing the code this way is to avoid errors that occur during multi-GPU inference due to tensors not being on the same device. By ensuring that the first and last layers of the large language model (LLM) are on the same device, we prevent such errors.

### Inference with Transformers

Besides this method, you can also use the following code to get streamed output.

## Finetune

Many repositories now support fine-tuning of the InternVL series models, including InternVL , SWIFT , XTurner , and others. Please refer to their documentation for more details on fine-tuning.
[LINK: InternVL](https://github.com/OpenGVLab/InternVL)
[LINK: SWIFT](https://github.com/modelscope/ms-swift)
[LINK: XTurner](https://github.com/InternLM/xtuner)

## Deployment

### LMDeploy

LMDeploy is a toolkit for compressing, deploying, and serving LLMs & VLMs.
LMDeploy abstracts the complex inference process of multi-modal Vision-Language Models (VLM) into an easy-to-use pipeline, similar to the Large Language Model (LLM) inference pipeline.
If ImportError occurs while executing this case, please install the required dependency packages as prompted.
When dealing with multiple images, you can put them all in one list. Keep in mind that multiple images will lead to a higher number of input tokens, and as a result, the size of the context window typically needs to be increased.
Warning: Due to the scarcity of multi-image conversation data, the performance on multi-image tasks may be unstable, and it may require multiple attempts to achieve satisfactory results.
Conducting inference with batch prompts is quite straightforward; just place them within a list structure:
There are two ways to do the multi-turn conversations with the pipeline. One is to construct messages according to the format of OpenAI and use above introduced method, the other is to use the pipeline.chat interface.
LMDeploy's api_server enables models to be easily packed into services with a single command. The provided RESTful APIs are compatible with OpenAI's interfaces. Below are an example of service startup:
To use the OpenAI-style interface, you need to install OpenAI:
Then, use the code below to make the API call:

## License

This project is released under the MIT License. This project uses the pre-trained internlm2-chat-20b as a component, which is licensed under the Apache License 2.0.

## Citation

If you find this project useful in your research, please consider citing:

## Model tree for OpenGVLab/InternVL2-26B

## Space using OpenGVLab/InternVL2-26B 1

## Collection including OpenGVLab/InternVL2-26B

## Papers for OpenGVLab/InternVL2-26B


--------------------