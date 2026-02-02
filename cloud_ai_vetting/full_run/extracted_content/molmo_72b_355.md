# Molmo-72B
**URL:** https://huggingface.co/allenai/Molmo-72B-0924
**Page Title:** allenai/Molmo-72B-0924 · Hugging Face
--------------------


## Molmo 72B

Molmo is a family of open vision-language models developed by the Allen Institute for AI. Molmo models are trained on PixMo, a dataset of 1 million, highly-curated image-text pairs. It has state-of-the-art performance among multimodal models with a similar size while being fully open-source. You can find all models in the Molmo family here . Learn more about the Molmo family in our announcement blog post or the paper .
Molmo 72B is based on Qwen2-72B and uses OpenAI CLIP as vision backbone. 
Molmo-72B achieves the highest academic benchmark score and ranks second on human evaluation, just slightly behind GPT-4o.
This checkpoint is a preview of the Molmo release. All artifacts used in creating Molmo (PixMo dataset, training code, evaluations, intermediate checkpoints) will be made available at a later date, furthering our commitment to open-source AI development and reproducibility.
Sign up here to be the first to know when artifacts are released.
[LINK: Sign up here](https://docs.google.com/forms/d/e/1FAIpQLSdML1MhNNBDsCHpgWG65Oydg2SjZzVasyqlP08nBrWjZp_c7A/viewform)
Quick links:
- 💬 Demo
- 📂 All Models
- 📃 Paper
- 🎥 Blog with Videos

## Quick Start

To run Molmo, first install dependencies:
Then, follow these steps:
To make inference more efficient, run with autocast:
We did most of our evaluation in this setting (autocast on, but float32 weights)
To even further reduce the memory requirements, the model can be run with bfloat16 weights:
Note that we have observed that this can change the output of the model compared to running with float32 weights.

## vLLM

Molmo is supported in vLLM, however please use version <=0.7.2 until a prepreprocessing bug is fixed.
[LINK: prepreprocessing bug](https://github.com/vllm-project/vllm/issues/26451)

## Evaluations

Benchmarks: AI2D test, ChartQA test, VQA v2.0 test, DocQA test, InfographicVQA test, TextVQA val, RealWorldQA, MMMU val, MathVista testmini, CountBenchQA, Flickr Count (we collected this new dataset that is significantly harder than CountBenchQA).

## FAQs

### I'm getting an error a broadcast error when processing images!

Your image might not be in RGB format. You can convert it using the following code snippet:

### Molmo doesn't work great with transparent images!

We received reports that Molmo models might struggle with transparent images. 
For the time being, we recommend adding a white or dark background to your images before passing them to the model. The code snippet below shows how to do this using the Python Imaging Library (PIL):

## License and Use

This model is licensed under Apache 2.0. It is intended for research and educational use.
For more information, please see our Responsible Use Guidelines .
The base model used is Qwen2-72B, whose license (the Tongyi Qianwen license) you can find here .

## Model tree for allenai/Molmo-72B-0924

Base model

## Spaces using allenai/Molmo-72B-0924 4

## Collection including allenai/Molmo-72B-0924

## Paper for allenai/Molmo-72B-0924


--------------------