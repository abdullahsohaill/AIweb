# SmolVLM2-2.2B-Instruct
**URL:** https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct
**Page Title:** HuggingFaceTB/SmolVLM2-2.2B-Instruct · Hugging Face
--------------------


## SmolVLM2 2.2B

SmolVLM2-2.2B is a lightweight multimodal model designed to analyze video content. The model processes videos, images, and text inputs to generate text outputs - whether answering questions about media files, comparing visual content, or transcribing text from images. Despite its compact size, requiring only 5.2GB of GPU RAM for video inference, it delivers robust performance on complex multimodal tasks. This efficiency makes it particularly well-suited for on-device applications where computational resources may be limited.

## Model Summary

- Developed by: Hugging Face 🤗
- Model type: Multi-modal model (image/multi-image/video/text)
- Language(s) (NLP): English
- License: Apache 2.0
- Architecture: Based on Idefics3 (see technical summary)

## Resources

- Demo: Video Highlight Generator
- Blog: Blog post

## Uses

SmolVLM2 can be used for inference on multimodal (video / image / text) tasks where the input consists of text queries along with video or one or more images. Text and media files can be interleaved arbitrarily, enabling tasks like captioning, visual question answering, and storytelling based on visual content. The model does not support image or video generation.
To fine-tune SmolVLM2 on a specific task, you can follow the fine-tuning tutorial .
[LINK: the fine-tuning tutorial](https://github.com/huggingface/smollm/blob/main/vision/finetuning/Smol_VLM_FT.ipynb)

## Evaluation

### Vision Evaluation

### Video Evaluation

We evaluated the performance of the SmolVLM2 family on the following scientific benchmarks:

### How to get started

You can use transformers to load, infer and fine-tune SmolVLM. Make sure you have num2words, flash-attn and latest transformers installed.
You can load the model as follows.
You preprocess your inputs directly using chat templates and directly passing them
To use SmolVLM2 for video inference, make sure you have decord installed.
You can interleave multiple media with text using chat templates.

### Model optimizations

## Misuse and Out-of-scope Use

SmolVLM is not intended for high-stakes scenarios or critical decision-making processes that affect an individual's well-being or livelihood. The model may produce content that appears factual but may not be accurate. Misuse includes, but is not limited to:
- Prohibited Uses: Evaluating or scoring individuals (e.g., in employment, education, credit) Critical automated decision-making Generating unreliable factual content
- Evaluating or scoring individuals (e.g., in employment, education, credit)
- Critical automated decision-making
- Generating unreliable factual content
- Malicious Activities: Spam generation Disinformation campaigns Harassment or abuse Unauthorized surveillance
- Spam generation
- Disinformation campaigns
- Harassment or abuse
- Unauthorized surveillance

### License

SmolVLM2 is built upon the shape-optimized SigLIP as image encoder and SmolLM2 for text decoder part.
We release the SmolVLM2 checkpoints under the Apache 2.0 license.

## Citation information

You can cite us in the following way:

## Training Data

SmolVLM2 used 3.3M samples for training originally from ten different datasets: LlaVa Onevision , M4-Instruct , Mammoth , LlaVa Video 178K , FineVideo , VideoStar , VRipt , Vista-400K , MovieChat and ShareGPT4Video .
In the following plots we give a general overview of the samples across modalities and the source of those samples.

## Data Split per modality

## Granular dataset slices per modality

### Text Datasets

### Multi-image Datasets

### Image Datasets

### Video Datasets

## Model tree for HuggingFaceTB/SmolVLM2-2.2B-Instruct

Base model

## Datasets used to train HuggingFaceTB/SmolVLM2-2.2B-Instruct

## Spaces using HuggingFaceTB/SmolVLM2-2.2B-Instruct 35

## Collection including HuggingFaceTB/SmolVLM2-2.2B-Instruct

## Paper for HuggingFaceTB/SmolVLM2-2.2B-Instruct


--------------------