# Fuyu-8B
**URL:** https://huggingface.co/adept/fuyu-8b
**Page Title:** adept/fuyu-8b · Hugging Face
--------------------


## Fuyu-8B Model Card

We’re releasing Fuyu-8B, a small version of the multimodal model that powers our product. The model is available on HuggingFace. We think Fuyu-8B is exciting because:
- It has a much simpler architecture and training procedure than other multi-modal models, which makes it easier to understand, scale, and deploy.
- It’s designed from the ground up for digital agents, so it can support arbitrary image resolutions, answer questions about graphs and diagrams, answer UI-based questions, and do fine-grained localization on screen images.
- It’s fast - we can get responses for large images in less than 100 milliseconds.
- Despite being optimized for our use-case, it performs well at standard image understanding benchmarks such as visual question-answering and natural-image-captioning.
Please note that the model we have released is a base model. We expect you to need to finetune the model for specific use cases like verbose captioning or multimodal chat. In our experience, the model responds well to few-shotting and fine-tuning for a variety of use-cases.

## Model

Fuyu-8B is a multi-modal text and image transformer trained by Adept AI .
Architecturally, Fuyu is a vanilla decoder-only transformer - there is no image encoder. 
Image patches are instead linearly projected into the first layer of the transformer, bypassing the embedding lookup. 
We simply treat the transformer decoder like an image transformer (albeit with no pooling and causal attention).
See the below diagram for more details.
This simplification allows us to support arbitrary image resolutions. 
To accomplish this, we treat the sequence of image tokens like the sequence of text tokens. 
We remove image-specific position embeddings and feed in as many image tokens as necessary in raster-scan order. 
To tell the model when a line has broken, we simply use a special image-newline character. 
The model can use its existing position embeddings to reason about different image sizes, and we can use images of arbitrary size at training time, removing the need for separate high and low-resolution training stages.

### Model Description

- Developed by: Adept-AI
- Model type: Decoder-only multi-modal transformer model
- License: CC-BY-NC
- Model Description: This is a multi-modal model that can consume images and text and produce text.
- Resources for more information: Check out our blog post .

## Evaluation

Though not the focus of this model, we did evaluate it on standard image understanding benchmarks:

## How to Use

You can load the model and perform inference as follows:
N.B.: The token |SPEAKER| is a placeholder token for image patch embeddings, so it will show up in the model context (e.g., in the portion of generation_output representing the model context). |NEWLINE| is the "image newline" token, denoting new rows in the raster scan order input of the image patches. \x04 is the "beginning of answer" token.
Fuyu can also perform some question answering on natural images and charts/diagrams (thought fine-tuning may be required for good performance):
For best performance, it's recommended to end questions with \n , as shown above!

## Uses

### Direct Use

The model is intended for research purposes only. Because this is a raw model release, we have not added further finetuning, postprocessing or sampling strategies to control for undesirable outputs. You should expect to have to fine-tune the model for your use-case.
Possible research areas and tasks include
- Applications in computer control or digital agents.
- Research on multi-modal models generally.
Excluded uses are described below.

### Out-of-Scope Use

The model was not trained to be factual or true representations of people or events, and therefore using the model to generate such content is out-of-scope for the abilities of this model.

## Limitations and Bias

### Limitations

- Faces and people in general may not be generated properly.

### Bias

While the capabilities of these models are impressive, they can also reinforce or exacerbate social biases.

## Model tree for adept/fuyu-8b

## Spaces using adept/fuyu-8b 56


--------------------