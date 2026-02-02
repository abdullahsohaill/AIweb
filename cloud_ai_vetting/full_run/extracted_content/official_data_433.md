# official data
**URL:** https://huggingface.co/THUDM/CogVideoX1.5-5B
**Page Title:** zai-org/CogVideoX1.5-5B · Hugging Face
--------------------


## CogVideoX1.5-5B

📄 中文阅读 | 🤗 Huggingface Space | 🌐 Github | 📜 arxiv
[LINK: 🌐 Github](https://github.com/THUDM/CogVideo)
📍 Visit QingYing and API Platform to experience larger-scale commercial video generation models.

## Model Introduction

CogVideoX is an open-source video generation model similar to QingYing . The table below displays the list of video generation models we currently offer, along with their foundational information.
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)
[LINK: SAT](https://github.com/THUDM/SwissArmyTransformer)
Data Explanation
- Testing with the diffusers library enabled all optimizations included in the library. This scheme has not been
tested on non-NVIDIA A100/H100 devices. It should generally work with all NVIDIA Ampere architecture or higher
devices. Disabling optimizations can triple VRAM usage but increase speed by 3-4 times. You can selectively disable
certain optimizations, including:
- In multi-GPU inference, enable_sequential_cpu_offload() optimization needs to be disabled.
- Using an INT8 model reduces inference speed, meeting the requirements of lower VRAM GPUs while retaining minimal video
quality degradation, at the cost of significant speed reduction.
- PytorchAO and Optimum-quanto can be
used to quantize the text encoder, Transformer, and VAE modules, reducing CogVideoX’s memory requirements, making it
feasible to run the model on smaller VRAM GPUs. TorchAO quantization is fully compatible with torch.compile ,
significantly improving inference speed. FP8 precision is required for NVIDIA H100 and above, which requires source
installation of torch , torchao , diffusers , and accelerate . Using CUDA 12.4 is recommended.
[LINK: PytorchAO](https://github.com/pytorch/ao)
[LINK: Optimum-quanto](https://github.com/huggingface/optimum-quanto/)
- Inference speed testing also used the above VRAM optimizations, and without optimizations, speed increases by about
10%. Only diffusers versions of models support quantization.
- Models support English input only; other languages should be translated into English during prompt crafting with a
larger model.
Note
- Use SAT for inference and fine-tuning SAT version models. Check our
GitHub for more details.
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

## Spaces using zai-org/CogVideoX1.5-5B 2

## Collection including zai-org/CogVideoX1.5-5B

## Paper for zai-org/CogVideoX1.5-5B


--------------------