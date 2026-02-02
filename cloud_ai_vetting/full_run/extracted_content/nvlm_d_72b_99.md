# NVLM-D-72B
**URL:** https://huggingface.co/nvidia/NVLM-D-72B
**Page Title:** nvidia/NVLM-D-72B · Hugging Face
--------------------


## Model Overview

## Description

This family of models performs vision-language and text-only tasks including optical character recognition, multimodal reasoning, localization, common sense reasoning, world knowledge utilization, and coding.
This model is ready for non-commercial use.

## License/Terms of Use

Governing Terms: Deed - Attribution-NonCommercial 4.0 International - Creative Commons .
Additional Information: LICENSE · Qwen/Qwen2-72B-Instruct at main for Qwen2-72B-Instruct and The MIT License – Open Source Initiative for InternViT-6B-448px-V1-2.

## Model Details

Today (September 17th, 2024), we introduce NVLM 1.0 , a family of frontier-class multimodal large language models (LLMs) that achieve state-of-the-art results on vision-language tasks, rivaling the leading proprietary models (e.g., GPT-4o) and open-access models (e.g., Llama 3-V 405B and InternVL 2). Remarkably, NVLM 1.0 shows improved text-only performance over its LLM backbone after multimodal training.
In this repo, we are open-sourcing NVLM-1.0-D-72B (decoder-only architecture), the decoder-only model weights and code for the community.

## Reference(s)

Paper Inference Code (HF) Training Code Website
[LINK: Training Code](https://github.com/NVIDIA/Megatron-LM/tree/NVLM-1.0/examples/multimodal/nvlm)

## Benchmark Results

We train our model with legacy Megatron-LM and adapt the codebase to Huggingface for model hosting, reproducibility, and inference.
We observe numerical differences between the Megatron and Huggingface codebases, which are within the expected range of variation. 
We provide the results from both the Huggingface codebase and the Megatron codebase for reproducibility and comparison with other models.
[LINK: Megatron-LM](https://github.com/NVIDIA/Megatron-LM/tree/main/megatron/legacy)
Results (as of September 17th, 2024) in the multimodal benchmarks are as follows:

### Vision-language Benchmarks

### Text-only Benchmarks

## Model Architectures

Network Architecture: Decoder-Only Transformer
Text-only LLM backbone: Qwen2-72B-Instruct
Vision encoder: InternViT-6B

### Robustness

The model trained on this dataset cannot regenerate its training data:
- The model has no image generation capability since its output is only text. Hence it cannot regenerate any image it would have seen during training.
The model has no image generation capability since its output is only text. Hence it cannot regenerate any image it would have seen during training.
- The model cannot regenerate training text data: during training, the model takes text and images as inputs, and the model output (text) is conditioned on both inputs. During inference, without training images as input, the models would not be able to reproduce any part of the training text data.
The model cannot regenerate training text data: during training, the model takes text and images as inputs, and the model output (text) is conditioned on both inputs. During inference, without training images as input, the models would not be able to reproduce any part of the training text data.

### Input

Input Type(s): Text, Image Input Format(s): String, Pillow Library-Supported Formats Input Dimensions: One-Dimensional (1D), Two Dimensional (2D) Other Properties Related to Input: Maximum Token Length = 128K Tokens
[LINK: Pillow Library-Supported Formats](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)

### Output

Output Type(s): Text Output Format: String Model Output: 1D Other Properties Related to Output: None

## How to use

When converting Megatron checkpoint to Huggingface, we adapt InternVL codebase to support model loading and multi-GPU inference in HF. 
We also use the tokenizer from Qwen2.5-72B-Instruct when adapting the tokenizer to Huggingface, as it contains extra special tokens for vision tasks, e.g., <|vision_pad|> . 
We train NVLM-1.0-D-72B based on the Qwen2-72B-Instruct text-only model and InternViT-6B-448px-V1-5 ViT model with our large-scale high-quality multimodal dataset. 
For training code, please refer to Megatron-Core .
[LINK: Megatron-Core](https://github.com/NVIDIA/Megatron-LM/tree/NVLM-1.0/examples/multimodal/nvlm)

### Prepare the environment

We provide a docker build file in the Dockerfile for reproduction.
The docker image is based on nvcr.io/nvidia/pytorch:23.09-py3 .
Note: We observe that different transformer versions / CUDA versions / docker versions can lead to slight benchmark number differences. We recommend using the Dockerfile above for precise reproduction.

### Model loading

### Multiple GPUs

The model can be loaded on multiple GPUs as follows:

### Inference

### Benchmark Evaluation

To test our NVLM-1.0 model on the benchmark datasets, you can use the following code:
Specifically,
- --config-path eval/full_eval.yaml file contains the evaluation configurations, including  the evaluation prompt, the evaluation dataset paths, and generation hyper-parameters.
- --result-save-path path/to/eval_results/ specifies the path to save the evaluation results.
- --zero-shot-eval-tasks specifies the tasks to evaluate on.

## Software Integration

Runtime Engine(s)
- PyTorch
Supported Hardware Microarchitecture Compatibility:
- NVIDIA Hopper
[Preferred/Supported] Operating System(s):
- Linux

## Inference

Engine: PyTorch Test Hardware:
- H100

## Model Version(s)

- v1.0-D (NVLM-D)

## Training, Testing, and Evaluation Datasets

### Pre-Training Dataset

Link
- See Table 4
Data Collection Method by dataset
- Hybrid: Automated, Human, Synthetic, Unknown
Labeling Method by dataset
- Hybrid: Automated, Human, Synthetic, Unknown
Properties
- Trained on image captions, image-text pairs, natural images, charts, documents, scene descriptions, and mathematical reasoning.

### Supervised Fine-Tuning Dataset

Link
- See Table 6
Data Collection Method by dataset
- Hybrid: Automated, Human, Synthetic, Unknown
Labeling Method by dataset
- Hybrid: Automated, Human, Synthetic, Unknown
Properties
- Trained on image captions; general knowledge; image-text pairs; natural images; charts; diagrams; documents; scene descriptions; science diagrams, lessons, textbook data, and question-answer pairs; visual instruction tuning; and mathematical reasoning.

### Evaluation Dataset

Link
- See Section 6.1, "Benchmark"
Data collection method by dataset
- Human
Labeling method by dataset
- Human
Properties
- Evaluated on general knowledge, visual answering, chart understanding, table, optical character recognition, and mathematical reasoning.

## Correspondence to

Wenliang Dai* ( wdai@nvidia.com ), Nayeon Lee* ( nayeonl@nvidia.com ), Boxin Wang* ( boxinw@nvidia.com ), Zhuolin Yang* ( zhuoliny@nvidia.com ), Wei Ping* ( wping@nvidia.com )
*Equal contribution

## Citation

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please report security vulnerabilities or NVIDIA AI Concerns here .

## Model tree for nvidia/NVLM-D-72B

## Spaces using nvidia/NVLM-D-72B 7

## Collection including nvidia/NVLM-D-72B

## Paper for nvidia/NVLM-D-72B


--------------------