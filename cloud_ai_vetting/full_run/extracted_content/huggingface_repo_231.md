# Huggingface Repo
**URL:** https://huggingface.co/fancyfeast/llama-joycaption-alpha-two-hf-llava
**Page Title:** fancyfeast/llama-joycaption-alpha-two-hf-llava · Hugging Face
--------------------


## Model Card for Llama JoyCaption Alpha Two

Github
[LINK: Github](https://github.com/fpgaminer/joycaption)
JoyCaption is an image captioning Visual Language Model (VLM) being built from the ground up as a free, open, and uncensored model for the community to use in training Diffusion models.
Key Features:
- Free and Open : It will be released for free, open weights, no restrictions, and just like bigASP , will come with training scripts and lots of juicy details on how it gets built.
- Uncensored : Equal coverage of SFW and NSFW concepts. No "cylindrical shaped object with a white substance coming out on it" here.
- Diversity : All are welcome here. Do you like digital art? Photoreal? Anime? Furry? JoyCaption is for everyone. Pains are being taken to ensure broad coverage of image styles, content, ethnicity, gender, orientation, etc.
- Minimal Filtering : JoyCaption is trained on large swathes of images so that it can understand almost all aspects of our world. almost. Illegal content will never be tolerated in JoyCaption's training.

## Motivation

Automated descriptive captions enable the training and finetuning of diffusion models on a wider range of images, since trainers are no longer required to either find images with already associated text or write the descriptions themselves. They also improve the quality of generations produced by Text-to-Image models trained on them (ref: DALL-E 3 paper). But to-date, the community has been stuck with ChatGPT, which is expensive and heavily censored; or alternative models, like CogVLM, which are weaker than ChatGPT and have abysmal performance outside of the SFW domain.
I'm building JoyCaption to help fill this gap by performing near or on-par with GPT4o in captioning images, while being free, unrestricted, and open.

## How to Get Started with the Model

Please see the Github for more details.
[LINK: Github](https://github.com/fpgaminer/joycaption)
Example usage:

## vLLM

vLLM provides the highest performance inference for JoyCaption, and an OpenAI compatible API so JoyCaption can be used like any other VLMs.  Example usage:
VLMs are a bit finicky on vLLM, and vLLM is memory hungry, so you may have to adjust settings for your particular environment, such as forcing eager mode, adjusting max-model-len, adjusting gpu_memory_utilization, etc.
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for fancyfeast/llama-joycaption-alpha-two-hf-llava

Base model

## Spaces using fancyfeast/llama-joycaption-alpha-two-hf-llava 2


--------------------