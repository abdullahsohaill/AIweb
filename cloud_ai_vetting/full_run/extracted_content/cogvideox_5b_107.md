# CogVideoX-5B
**URL:** https://huggingface.co/THUDM/CogVideoX-5b
**Page Title:** zai-org/CogVideoX-5b · Hugging Face
--------------------


## CogVideoX-5B

📄 中文阅读 | 🤗 Huggingface Space | 🌐 Github | 📜 arxiv
[LINK: 🌐 Github](https://github.com/THUDM/CogVideo)
📍 Visit QingYing and API Platform to experience commercial video generation models.

## Demo Show

## Model Introduction

CogVideoX is an open-source version of the video generation model originating
from QingYing . The table below displays the list of video generation
models we currently offer, along with their foundational information.
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)
Data Explanation
- When testing using the diffusers library, all optimizations provided by the diffusers library were enabled. This
solution has not been tested for actual VRAM/memory usage on devices other than NVIDIA A100 / H100 . Generally,
this solution can be adapted to all devices with NVIDIA Ampere architecture and above. If the optimizations are
disabled, VRAM usage will increase significantly, with peak VRAM usage being about 3 times higher than the table
shows. However, speed will increase by 3-4 times. You can selectively disable some optimizations, including:
- When performing multi-GPU inference, the enable_model_cpu_offload() optimization needs to be disabled.
- Using INT8 models will reduce inference speed. This is to ensure that GPUs with lower VRAM can perform inference
normally while maintaining minimal video quality loss, though inference speed will decrease significantly.
- The 2B model is trained with FP16 precision, and the 5B model is trained with BF16 precision. We recommend using
the precision the model was trained with for inference.
- PytorchAO and Optimum-quanto can be
used to quantize the text encoder, Transformer, and VAE modules to reduce CogVideoX's memory requirements. This makes
it possible to run the model on a free T4 Colab or GPUs with smaller VRAM! It is also worth noting that TorchAO
quantization is fully compatible with torch.compile , which can significantly improve inference speed. FP8 precision must be used on devices with NVIDIA H100 or above, which requires installing
the torch , torchao , diffusers , and accelerate Python packages from source. CUDA 12.4 is recommended.
[LINK: PytorchAO](https://github.com/pytorch/ao)
[LINK: Optimum-quanto](https://github.com/huggingface/optimum-quanto/)
- The inference speed test also used the above VRAM optimization scheme. Without VRAM optimization, inference speed
increases by about 10%. Only the diffusers version of the model supports quantization.
- The model only supports English input; other languages can be translated into English during refinement by a large
model.
Note
- Using SAT for inference and fine-tuning of SAT version
models. Feel free to visit our GitHub for more information.
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)

## Quick Start 🤗

This model supports deployment using the huggingface diffusers library. You can deploy it by following these steps.
We recommend that you visit our GitHub and check out the relevant prompt
optimizations and conversions to get a better experience.
[LINK: GitHub](https://github.com/THUDM/CogVideo)
- Install the required dependencies
- Run the code

## Quantized Inference

PytorchAO and Optimum-quanto can be
used to quantize the Text Encoder, Transformer and VAE modules to lower the memory requirement of CogVideoX. This makes
it possible to run the model on free-tier T4 Colab or smaller VRAM GPUs as well! It is also worth noting that TorchAO
quantization is fully compatible with torch.compile , which allows for much faster inference speed.
[LINK: PytorchAO](https://github.com/pytorch/ao)
[LINK: Optimum-quanto](https://github.com/huggingface/optimum-quanto/)
Additionally, the models can be serialized and stored in a quantized datatype to save disk space when using PytorchAO.
Find examples and benchmarks at these links:
- torchao
[LINK: torchao](https://gist.github.com/a-r-r-o-w/4d9732d17412888c885480c6521a9897)
- quanto
[LINK: quanto](https://gist.github.com/a-r-r-o-w/31be62828b00a9292821b85c1017effa)

## Explore the Model

Welcome to our github , where you will find:
[LINK: github](https://github.com/THUDM/CogVideo)
- More detailed technical details and code explanation.
- Optimization and conversion of prompt words.
- Reasoning and fine-tuning of SAT version models, and even pre-release.
- Project update log dynamics, more interactive opportunities.
- CogVideoX toolchain to help you better use the model.
- INT8 model inference code support.

## Model License

This model is released under the CogVideoX LICENSE .

## Citation

## Model tree for zai-org/CogVideoX-5b

## Spaces using zai-org/CogVideoX-5b 100

## Collection including zai-org/CogVideoX-5b

## Paper for zai-org/CogVideoX-5b

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
zai-org/CogVideoX-5b is supported by the following Inference Providers:

--------------------