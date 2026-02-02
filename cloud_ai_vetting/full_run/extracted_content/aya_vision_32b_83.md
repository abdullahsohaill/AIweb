# Aya-vision-32b
**URL:** https://huggingface.co/CohereForAI/aya-vision-32b
**Page Title:** CohereLabs/aya-vision-32b · Hugging Face
--------------------


## You need to agree to share your contact information to access this model

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
By submitting this form, you agree to the License Agreement and acknowledge that the information you provide will be collected, used, and shared in accordance with Cohere’s Privacy Policy . You’ll receive email updates about Cohere Labs and Cohere research, events, products and services. You can unsubscribe at any time.
Log in or Sign Up to review the conditions and access this model content.

## Model Card for Aya Vision 32B

Cohere Labs Aya Vision 32B is an open weights research release of a 32-billion parameter model with advanced capabilities optimized for a variety of vision-language use cases, including OCR, captioning, visual reasoning, summarization, question answering, code, and more. 
It is a multilingual model trained to excel in 23 languages in vision and language.
This model card corresponds to the 32-billion version of the Aya Vision model. We also released an 8-billion version which you can find here .
- Developed by: Cohere Labs
- Point of Contact: Cohere Labs
- License: CC-BY-NC , requires also adhering to Cohere Lab's Acceptable Use Policy
[LINK: Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)
- Model: Cohere Labs-aya-vision-32b
- Model Size: 32 billion parameters
- Context length: 16K

## Try it: Aya Vision in Action

Before downloading the weights, you can try Aya Vision 32B chat in the Cohere playground or our dedicated Hugging Face Space for interactive exploration.

## Example Notebook

You can check out the following notebook to understand how to use Aya Vision for different use cases.
[LINK: notebook](https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/aya_vision_intro.ipynb)

## How to Use Aya Vision

Please install transformers from the source repository that includes the necessary changes for this model:
You can also use the model directly using transformers pipeline abstraction:

## Model Details

Input: Model accepts input text and images.
Output: Model generates text.
Model Architecture: This is a vision-language model that uses a state-of-the-art multilingual language model, Aya Expanse 32B , which is trained with Aya Expanse recipe, paired with SigLIP2-patch14-384 vision encoder through a multimodal adapter for vision-language understanding.
Image Processing: We use 169 visual tokens to encode an image tile with a resolution of 364x364 pixels . Input images of arbitrary sizes are mapped to the nearest supported resolution based on the aspect ratio. Aya Vision uses up to 12 input tiles and a thumbnail (resized to 364x364)  (2197 image tokens).
Languages covered: The model has been trained on 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, Chinese (Simplified and Traditional), Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
Context length : Aya Vision 32B supports a context length of 16K.
For more details about how the model was trained, check out our blogpost .

## Evaluation

We evaluated Aya Vision 32B against Llama-3.2 90B Vision , Molmo 72B , Qwen2.5-VL 72B using Aya Vision Benchmark and m-WildVision . 
Win-rates were determined using claude-3-7-sonnet-20250219 as a judge, based on the superior judge performance compared to other models.
We also evaluated Aya Vision 32B’s performance for text-only input against the same models using m-ArenaHard , a challenging open-ended generation evaluation, measured using win-rates using gpt-4o-2024-11-20 as a judge.

### Model Card Contact

For errors or additional questions about details in this model card, contact labs@cohere.com

### Terms of Use

We hope that the release of this model will make community-based research efforts more accessible by releasing the weights of a highly performant 32 billion parameter Vision-Language Model to researchers all over the world.
This model is governed by a CC-BY-NC , requires also adhering to Cohere Lab's Acceptable Use Policy
[LINK: Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)

## Model tree for CohereLabs/aya-vision-32b

## Spaces using CohereLabs/aya-vision-32b 5

## Collection including CohereLabs/aya-vision-32b

## Paper for CohereLabs/aya-vision-32b

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
CohereLabs/aya-vision-32b is supported by the following Inference Providers:

--------------------