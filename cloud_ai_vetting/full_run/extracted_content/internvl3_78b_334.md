# InternVL3-78B
**URL:** https://huggingface.co/OpenGVLab/InternVL3-78B
**Page Title:** OpenGVLab/InternVL3-78B · Hugging Face
--------------------


## InternVL3-78B

[📂 GitHub] [📜 InternVL 1.0] [📜 InternVL 1.5] [📜 InternVL 2.5] [📜 InternVL2.5-MPO] [📜 InternVL3]
[LINK: [📂 GitHub]](https://github.com/OpenGVLab/InternVL)
[🆕 Blog] [🗨️ Chat Demo] [🤗 HF Demo] [🚀 Quick Start] [📖 Documents]
[LINK: [🆕 Blog]](https://internvl.github.io/blog/)
[LINK: [📖 Documents]](https://internvl.readthedocs.io/en/latest/)

## Introduction

We introduce InternVL3, an advanced multimodal large language model (MLLM) series that demonstrates superior overall performance.
Compared to InternVL 2.5, InternVL3 exhibits superior multimodal perception and reasoning capabilities, while further extending its multimodal capabilities to encompass tool usage, GUI agents, industrial image analysis, 3D vision perception, and more.
Additionally, we compare InternVL3 with  Qwen2.5 Chat models, whose corresponding pre-trained base models are employed as the initialization of the langauge component in InternVL3. Benefitting from Native Multimodal Pre-Training, the InternVL3 series achieves even better overall text performance than the Qwen2.5 series.

## InternVL3 Family

In the following table, we provide an overview of the InternVL3 series.

## Model Architecture

As shown in the following figure, InternVL3 retains the same model architecture as InternVL 2.5 and its predecessors, InternVL 1.5 and 2.0, following the "ViT-MLP-LLM" paradigm. In this new version, we integrate a newly incrementally pre-trained InternViT with various pre-trained LLMs, including InternLM 3 and Qwen 2.5, using a randomly initialized MLP projector.
[LINK: InternVL3](https://internvl.github.io/blog/2025-04-11-InternVL-3/)
[LINK: InternVL 2.5](https://internvl.github.io/blog/2024-12-05-InternVL-2.5/)
As in the previous version, we applied a pixel unshuffle operation, reducing the number of visual tokens to one-quarter of the original. Besides, we adopted a similar dynamic resolution strategy as InternVL 1.5, dividing images into tiles of 448×448 pixels. The key difference, starting from InternVL 2.0, is that we additionally introduced support for multi-image and video data.
Notably, in InternVL3, we integrate the Variable Visual Position Encoding (V2PE) , which utilizes smaller, more flexible position increments for visual tokens. Benefiting from V2PE, InternVL3 exhibits better long context understanding capabilities compared to its predecessors.

## Training Strategy

### Native Multimodal Pre-Training

We propose a Native Multimodal Pre-Training approach that consolidates language and vision learning into a single pre-training stage.
In contrast to standard paradigms that first train a language-only model and subsequently adapt it to handle additional modalities, our method interleaves multimodal data (e.g., image-text, video-text, or image-text interleaved sequences) with large-scale textual corpora. This unified training scheme allows the model to learn both linguistic and multimodal representations simultaneously, ultimately enhancing its capability to handle vision-language tasks without the need for separate alignment or bridging modules.
Please see our paper for more details.

### Supervised Fine-Tuning

In this phase, the techniques of random JPEG compression, square loss re-weighting, and multimodal data packing proposed in InternVL2.5 are also employed in the InternVL3 series.
The main advancement of the SFT phase in InternVL3 compared to InternVL2.5 lies in the use of higher-quality and more diverse training data.
Specifically, we further extend  training samples for tool use, 3D scene understanding, GUI operations, long context tasks, video understanding, scientific diagrams, creative writing, and multimodal reasoning.

### Mixed Preference Optimization

During Pre-training and SFT, the model is trained to predict the next token conditioned on previous ground-truth tokens.
However, during inference, the model predicts each token based on its own prior outputs. 
This discrepancy between ground-truth tokens and model-predicted tokens introduces a distribution shift, which can impair the model’s Chain-of-Thought (CoT) reasoning capabilities.
To mitigate this issue, we employ MPO , which introduces additional supervision from both positive and negative samples to align the model response distribution with the ground-truth distribution, thereby improving reasoning performance.
Specifically, the training objective of MPO is a combination of
preference loss L p \mathcal{L}_{\text{p}} L p ​ ,
quality loss L q \mathcal{L}_{\text{q}} L q ​ ,
and generation loss L g \mathcal{L}_{\text{g}} L g ​ ,
which can be formulated as follows:
L = w p ⋅ L p + w q ⋅ L q + w g ⋅ L g , \mathcal{L}=w_{p}\cdot\mathcal{L}_{\text{p}} + w_{q}\cdot\mathcal{L}_{\text{q}} + w_{g}\cdot\mathcal{L}_{\text{g}}, L = w p ​ ⋅ L p ​ + w q ​ ⋅ L q ​ + w g ​ ⋅ L g ​ ,
where w ∗ w_{*} w ∗ ​ represents the weight assigned to each loss component. Please see our paper for more details about MPO.

### Test-Time Scaling

Test-Time Scaling has been shown to be an effective method to enhance the reasoning abilities of LLMs and MLLMs.
In this work, we use the Best-of-N evaluation strategy and employ VisualPRM-8B as the critic model to select the best response for reasoning and mathematics evaluation.

## Evaluation on Multimodal Capability

### Multimodal Reasoning and Mathematics

### OCR, Chart, and Document Understanding

### Multi-Image & Real-World Comprehension

### Comprehensive Multimodal & Hallucination Evaluation

### Visual Grounding

### Multimodal Multilingual Understanding

### Video Understanding

### GUI Grounding

### Spatial Reasoning

## Evaluation on Language Capability

We compare InternVL3 with  Qwen2.5 Chat models, whose corresponding pre-trained base models are employed as the initialization of the langauge component in InternVL3.
Benefitting from Native Multimodal Pre-Training, the InternVL3 series achieves even better overall text performance than the Qwen2.5 series.
Please note that the evaluation scores of Qwen2.5 series  may differ from those officially reported, as we have adopted the prompt versions provided in the table across all datasets for OpenCompass evaluation.

## Ablation Study

### Native Multimodal Pre-Training

We conduct experiments on the InternVL2-8B model while keeping its architecture, initialization parameters, and training data entirely unchanged. Traditionally, InternVL2-8B employs a training pipeline that begins with an MLP warmup phase for feature alignment followed by an Instruction Tuning stage. In our experiments, we substitute the conventional MLP warmup phase with a native multimodal pre-training process. This modification isolates the contribution of native multimodal pre-training to the overall multimodal capability of the model.
The evaluation results in the Figure below shows that the model with native multimodal pre-training exhibits performance on most benchmarks that is comparable to the fully multi-stage-trained InternVL2-8B baseline. Furthermore, when followed by instruction tuning on higher-quality data, the model demonstrates further performance gains across evaluated multimodal tasks. These findings underscore the efficiency of native multimodal pre-training in imparting powerful multimodal capabilities to MLLMs.

### Mixed Preference Optimization

As shown in the table below, models fine-tuned with MPO demonstrate superior reasoning performance across seven multimodal reasoning benchmarks compared to their counterparts without MPO. Specifically, InternVL3-78B and InternVL3-38B outperform their counterparts by 4.1 and 4.5 points, respectively. Notably, the training data used for MPO is a subset of that used for SFT, indicating that the performance improvements primarily stem from the training algorithm rather than the training data.

### Variable Visual Position Encoding

As reported in the table below, the introduction of V2PE leads to significant performance gains across most evaluation metrics. In addition, our ablation studies—by varying the positional increment δ \delta δ —reveal that even for tasks primarily involving conventional contexts, relatively small δ \delta δ values can achieve optimal performance. These findings provide important insights for future efforts aimed at refining position encoding strategies for visual tokens in MLLMs.

## Quick Start

We provide an example code to run InternVL3-78B using transformers .
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
Conducting inference with batch prompts is quite straightforward; just place them within a list structure:
There are two ways to do the multi-turn conversations with the pipeline. One is to construct messages according to the format of OpenAI and use above introduced method, the other is to use the pipeline.chat interface.
LMDeploy's api_server enables models to be easily packed into services with a single command. The provided RESTful APIs are compatible with OpenAI's interfaces. Below are an example of service startup:
To use the OpenAI-style interface, you need to install OpenAI:
Then, use the code below to make the API call:

## License

This project is released under the MIT License. This project uses the pre-trained Qwen2.5 as a component, which is licensed under the Qwen License.

## Citation

If you find this project useful in your research, please consider citing:

## Model tree for OpenGVLab/InternVL3-78B

Base model

## Dataset used to train OpenGVLab/InternVL3-78B

## Spaces using OpenGVLab/InternVL3-78B 2

## Collection including OpenGVLab/InternVL3-78B

## Papers for OpenGVLab/InternVL3-78B


--------------------