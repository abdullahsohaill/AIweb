# CogVideoX-5B-I2V
**URL:** https://huggingface.co/THUDM/CogVideoX-5b-I2V
**Page Title:** zai-org/CogVideoX-5b-I2V · Hugging Face
--------------------


## CogVideoX-5B-I2V

📄 Read in English | 🤗 Huggingface Space | 🌐 Github | 📜 arxiv
[LINK: 🌐 Github](https://github.com/THUDM/CogVideo)
📍 Visit Qingying and API Platform for the commercial version of the video generation model

## Model Introduction

CogVideoX is an open-source video generation model originating
from Qingying . The table below presents information related to the video
generation models we offer in this version.
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)
Data Explanation
- While testing using the diffusers library, all optimizations included in the diffusers library were enabled. This
scheme has not been tested for actual memory usage on devices outside of NVIDIA A100 / H100 architectures.
Generally, this scheme can be adapted to all NVIDIA Ampere architecture and above devices. If optimizations are
disabled, memory consumption will multiply, with peak memory usage being about 3 times the value in the table.
However, speed will increase by about 3-4 times. You can selectively disable some optimizations, including:
- For multi-GPU inference, the enable_sequential_cpu_offload() optimization needs to be disabled.
- Using INT8 models will slow down inference, which is done to accommodate lower-memory GPUs while maintaining minimal
video quality loss, though inference speed will significantly decrease.
- The CogVideoX-2B model was trained in FP16 precision, and all CogVideoX-5B models were trained in BF16 precision.
We recommend using the precision in which the model was trained for inference.
- PytorchAO and Optimum-quanto can be
used to quantize the text encoder, transformer, and VAE modules to reduce the memory requirements of CogVideoX. This
allows the model to run on free T4 Colabs or GPUs with smaller memory! Also, note that TorchAO quantization is fully
compatible with torch.compile , which can significantly improve inference speed. FP8 precision must be used on
devices with NVIDIA H100 and above, requiring source installation of torch , torchao , diffusers , and accelerate Python packages. CUDA 12.4 is recommended.
[LINK: PytorchAO](https://github.com/pytorch/ao)
[LINK: Optimum-quanto](https://github.com/huggingface/optimum-quanto/)
- The inference speed tests also used the above memory optimization scheme. Without memory optimization, inference speed
increases by about 10%. Only the diffusers version of the model supports quantization.
- The model only supports English input; other languages can be translated into English for use via large model
refinement.
- The memory usage of model fine-tuning is tested in an 8 * H100 environment, and the program automatically
uses Zero 2 optimization. If a specific number of GPUs is marked in the table, that number or more GPUs must be used
for fine-tuning.
Reminders
- Use SAT for inference and fine-tuning SAT version models. Feel free
to visit our GitHub for more details.
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)

## Getting Started Quickly 🤗

This model supports deployment using the Hugging Face diffusers library. You can follow the steps below to get started.
We recommend that you visit our GitHub to check out prompt optimization and
conversion to get a better experience.
[LINK: GitHub](https://github.com/THUDM/CogVideo)
- Install the required dependencies
- Run the code

## Quantized Inference

PytorchAO and Optimum-quanto can be
used to quantize the text encoder, transformer, and VAE modules to reduce CogVideoX's memory requirements. This allows
the model to run on free T4 Colab or GPUs with lower VRAM! Also, note that TorchAO quantization is fully compatible
with torch.compile , which can significantly accelerate inference.
[LINK: PytorchAO](https://github.com/pytorch/ao)
[LINK: Optimum-quanto](https://github.com/huggingface/optimum-quanto/)
Additionally, these models can be serialized and stored using PytorchAO in quantized data types to save disk space. You
can find examples and benchmarks at the following links:
- torchao
[LINK: torchao](https://gist.github.com/a-r-r-o-w/4d9732d17412888c885480c6521a9897)
- quanto
[LINK: quanto](https://gist.github.com/a-r-r-o-w/31be62828b00a9292821b85c1017effa)

## Further Exploration

Feel free to enter our GitHub , where you'll find:
[LINK: GitHub](https://github.com/THUDM/CogVideo)
- More detailed technical explanations and code.
- Optimized prompt examples and conversions.
- Detailed code for model inference and fine-tuning.
- Project update logs and more interactive opportunities.
- CogVideoX toolchain to help you better use the model.
- INT8 model inference code.

## Model License

This model is released under the CogVideoX LICENSE .

## Citation

## Model tree for zai-org/CogVideoX-5b-I2V

## Spaces using zai-org/CogVideoX-5b-I2V 77

## Collection including zai-org/CogVideoX-5b-I2V

## Paper for zai-org/CogVideoX-5b-I2V


--------------------