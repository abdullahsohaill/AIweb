# Phi-3 Mini-128K-Instruct ONNX
**URL:** https://huggingface.co/microsoft/Phi-3-mini-128k-instruct-onnx
**Page Title:** microsoft/Phi-3-mini-128k-instruct-onnx · Hugging Face
--------------------


## Phi-3 Mini-128K-Instruct ONNX models

This repository hosts the optimized versions of Phi-3-mini-128k-instruct to accelerate inference with ONNX Runtime.
Phi-3 Mini is a lightweight, state-of-the-art open model built upon datasets used for Phi-2 - synthetic data and filtered websites - with a focus on very high-quality, reasoning dense data. The model belongs to the Phi-3 model family, and the mini version comes in two variants: 4K and 128K which is the context length (in tokens) it can support. The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
Optimized Phi-3 Mini models are published here in ONNX format to run with ONNX Runtime on CPU and GPU across devices, including server platforms, Windows, Linux and Mac desktops, and mobile CPUs, with the precision best suited to each of these targets.
DirectML support lets developers bring hardware acceleration to Windows devices at scale across AMD, Intel, and NVIDIA GPUs. Along with DirectML, ONNX Runtime provides cross platform support for Phi-3 Mini across a range of devices for CPU, GPU, and mobile.
To easily get started with Phi-3, you can use our newly introduced ONNX Runtime Generate() API. See here for instructions on how to run it.

## ONNX Models

Here are some of the optimized configurations we have added:
- ONNX model for int4 DML: ONNX model for AMD, Intel, and NVIDIA GPUs on Windows, quantized to int4 using AWQ .
- ONNX model for fp16 CUDA: ONNX model you can use to run for your NVIDIA GPUs.
- ONNX model for int4 CUDA: ONNX model for NVIDIA GPUs using int4 quantization via RTN.
- ONNX model for int4 CPU and Mobile: ONNX model for your CPU and Mobile, using int4 quantization via RTN. There are two versions uploaded to balance latency vs. accuracy.
  Acc=1 is targeted at improved accuracy, while Acc=4 is for improved perf. For mobile devices, we recommend using the model with acc-level-4.
More updates on AMD, and additional optimizations on CPU and Mobile will be added with the official ORT 1.18 release in early May. Stay tuned!

## Hardware Supported

The models are tested on:
- GPU SKU: RTX 4090 (DirectML)
- GPU SKU: 1 A100 80GB GPU, SKU: Standard_ND96amsr_A100_v4 (CUDA)
- CPU SKU: Standard F64s v2 (64 vcpus, 128 GiB memory)
- Mobile SKU: Samsung Galaxy S21
Minimum Configuration Required:
- Windows: DirectX 12-capable GPU and a minimum of 4GB of combined RAM
- CUDA: NVIDIA GPU with Compute Capability >= 7.0
[LINK: Compute Capability](https://developer.nvidia.com/cuda-gpus)

### Model Description

- Developed by: Microsoft
- Model type: ONNX
- Language(s) (NLP): Python, C, C++
- License: MIT
- Model Description: This is a conversion of the Phi-3 Mini-4K-Instruct model for ONNX Runtime inference.

## Additional Details

- ONNX Runtime Optimizations Blog Link
- Phi-3 Model Blog Link
- Phi-3 Model Card
- Phi-3 Technical Report

## How to Get Started with the Model

To make running of the Phi-3 models across a range of devices and platforms across various execution provider backends possible, we introduce a new API to wrap several aspects of generative AI inferencing. This API make it easy to drag and drop LLMs straight into your app. For running the early version of these models with ONNX Runtime, follow the steps here .
For example:

## Performance Metrics

Phi-3 Mini-128K-Instruct performs better in ONNX Runtime than PyTorch for all batch size, prompt length combinations. For FP16 CUDA, ORT performs up to 5X faster than PyTorch, while with INT4 CUDA it's up to 9X faster than PyTorch.
The table below shows the average throughput of the first 256 tokens generated (tps) for FP16 and INT4 precisions on CUDA as measured on 1 A100 80GB GPU, SKU: Standard_ND96amsr_A100_v4 .
Note: PyTorch compile and Llama.cpp currently do not support the Phi-3 Mini-128K-Instruct model.

### Package Versions

## Appendix

### Activation Aware Quantization

AWQ works by identifying the top 1% most salient weights that are most important for maintaining accuracy and quantizing the remaining 99% of weights. This leads to less accuracy loss from quantization compared to many other quantization techniques. For more on AWQ, see here .

## Model Card Contact

parinitarahi, kvaishnavi, natke

## Contributors

Kunal Vaishnavi, Sunghoon Choi, Yufeng Li, Akshay Sonawane, Sheetal Arun Kadam, Rui Ren, Edward Chen, Scott McKay, Ryan Hill, Emma Ning, Natalie Kershaw, Parinita Rahi, Patrice Vignola, Chai Chaoweeraprasit, Logan Iyer, Vicente Rivera, Jacques Van Rhyn

## Spaces using microsoft/Phi-3-mini-128k-instruct-onnx 3

## Collection including microsoft/Phi-3-mini-128k-instruct-onnx

## Paper for microsoft/Phi-3-mini-128k-instruct-onnx


--------------------