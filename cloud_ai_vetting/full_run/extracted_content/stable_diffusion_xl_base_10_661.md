# Stable Diffusion XL base 1.0
**URL:** https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
**Page Title:** stabilityai/stable-diffusion-xl-base-1.0 · Hugging Face
--------------------


## SD-XL 1.0-base Model Card

## Model

SDXL consists of an ensemble of experts pipeline for latent diffusion: 
In a first step, the base model is used to generate (noisy) latents, 
which are then further processed with a refinement model (available here: https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/ ) specialized for the final denoising steps.
Note that the base model can be used as a standalone module.
Alternatively, we can use a two-stage pipeline as follows: 
First, the base model is used to generate latents of the desired output size. 
In the second step, we use a specialized high-resolution model and apply a technique called SDEdit ( https://arxiv.org/abs/2108.01073 , also known as "img2img") 
to the latents generated in the first step, using the same prompt. This technique is slightly slower than the first one, as it requires more function evaluations.
Source code is available at https://github.com/Stability-AI/generative-models .
[LINK: https://github.com/Stability-AI/generative-models](https://github.com/Stability-AI/generative-models)

### Model Description

- Developed by: Stability AI
- Model type: Diffusion-based text-to-image generative model
- License: CreativeML Open RAIL++-M License
- Model Description: This is a model that can be used to generate and modify images based on text prompts. It is a Latent Diffusion Model that uses two fixed, pretrained text encoders ( OpenCLIP-ViT/G and CLIP-ViT/L ).
[LINK: OpenCLIP-ViT/G](https://github.com/mlfoundations/open_clip)
[LINK: CLIP-ViT/L](https://github.com/openai/CLIP/tree/main)
- Resources for more information: Check out our GitHub Repository and the SDXL report on arXiv .
[LINK: GitHub Repository](https://github.com/Stability-AI/generative-models)

### Model Sources

For research purposes, we recommend our generative-models Github repository ( https://github.com/Stability-AI/generative-models ), which implements the most popular diffusion frameworks (both training and inference) and for which new functionalities like distillation will be added over time. Clipdrop provides free SDXL inference.
[LINK: https://github.com/Stability-AI/generative-models](https://github.com/Stability-AI/generative-models)
- Repository: https://github.com/Stability-AI/generative-models
[LINK: https://github.com/Stability-AI/generative-models](https://github.com/Stability-AI/generative-models)
- Demo: https://clipdrop.co/stable-diffusion

## Evaluation

The chart above evaluates user preference for SDXL (with and without refinement) over SDXL 0.9 and Stable Diffusion 1.5 and 2.1. 
The SDXL base model performs significantly better than the previous variants, and the model combined with the refinement module achieves the best overall performance.

### 🧨 Diffusers

Make sure to upgrade diffusers to >= 0.19.0:
In addition make sure to install transformers , safetensors , accelerate as well as the invisible watermark:
To just use the base model, you can run:
To use the whole base + refiner pipeline as an ensemble of experts you can run:
When using torch >= 2.0 , you can improve the inference speed by 20-30% with torch.compile. Simple wrap the unet with torch compile before running the pipeline:
If you are limited by GPU VRAM, you can enable cpu offloading by calling pipe.enable_model_cpu_offload instead of .to("cuda") :
For more information on how to use Stable Diffusion XL with diffusers , please have a look at the Stable Diffusion XL Docs .
[LINK: the Stable Diffusion XL Docs](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/stable_diffusion_xl)

### Optimum

Optimum provides a Stable Diffusion pipeline compatible with both OpenVINO and ONNX Runtime .
[LINK: Optimum](https://github.com/huggingface/optimum)
[LINK: OpenVINO](https://docs.openvino.ai/latest/index.html)
To install Optimum with the dependencies required for OpenVINO :
To load an OpenVINO model and run inference with OpenVINO Runtime, you need to replace StableDiffusionXLPipeline with Optimum OVStableDiffusionXLPipeline . In case you want to load a PyTorch model and convert it to the OpenVINO format on-the-fly, you can set export=True .
You can find more examples (such as static reshaping and model compilation) in optimum documentation .
[LINK: documentation](https://huggingface.co/docs/optimum/main/en/intel/inference#stable-diffusion-xl)
To install Optimum with the dependencies required for ONNX Runtime inference :
To load an ONNX model and run inference with ONNX Runtime, you need to replace StableDiffusionXLPipeline with Optimum ORTStableDiffusionXLPipeline . In case you want to load a PyTorch model and convert it to the ONNX format on-the-fly, you can set export=True .
You can find more examples in optimum documentation .
[LINK: documentation](https://huggingface.co/docs/optimum/main/en/onnxruntime/usage_guides/models#stable-diffusion-xl)

## Uses

### Direct Use

The model is intended for research purposes only. Possible research areas and tasks include
- Generation of artworks and use in design and other artistic processes.
- Applications in educational or creative tools.
- Research on generative models.
- Safe deployment of models which have the potential to generate harmful content.
- Probing and understanding the limitations and biases of generative models.
Excluded uses are described below.

### Out-of-Scope Use

The model was not trained to be factual or true representations of people or events, and therefore using the model to generate such content is out-of-scope for the abilities of this model.

## Limitations and Bias

### Limitations

- The model does not achieve perfect photorealism
- The model cannot render legible text
- The model struggles with more difficult tasks which involve compositionality, such as rendering an image corresponding to “A red cube on top of a blue sphere”
- Faces and people in general may not be generated properly.
- The autoencoding part of the model is lossy.

### Bias

While the capabilities of image generation models are impressive, they can also reinforce or exacerbate social biases.

## Model tree for stabilityai/stable-diffusion-xl-base-1.0

## Spaces using stabilityai/stable-diffusion-xl-base-1.0 100

## Collection including stabilityai/stable-diffusion-xl-base-1.0

## Papers for stabilityai/stable-diffusion-xl-base-1.0

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
stabilityai/stable-diffusion-xl-base-1.0 is supported by the following Inference Providers:

--------------------