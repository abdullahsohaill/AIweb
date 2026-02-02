# Florence-2
**URL:** https://huggingface.co/microsoft/Florence-2-large
**Page Title:** microsoft/Florence-2-large · Hugging Face
--------------------


## Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks

## Model Summary

This is a continued pretrained version of Florence-2-large model with 4k context length, only 0.1B samples are used for continue pretraining, thus it might not be trained well. In addition, OCR task has been updated with line separator ('\n'). COCO OD AP 39.8
This Hub repository contains a HuggingFace's transformers implementation of Florence-2 model from Microsoft.
Florence-2 is an advanced vision foundation model that uses a prompt-based approach to handle a wide range of vision and vision-language tasks.  Florence-2 can interpret simple text prompts to perform tasks like captioning, object detection, and segmentation. It leverages our FLD-5B dataset, containing 5.4 billion annotations across 126 million images, to master multi-task learning. The model's sequence-to-sequence architecture enables it to excel in both zero-shot and fine-tuned settings, proving to be a competitive vision foundation model.
Resources and Technical Documentation:
- Florence-2 technical report .
- Jupyter Notebook for inference and visualization of Florence-2-large

## How to Get Started with the Model

Use the code below to get started with the model. All models are trained with float16.

## Tasks

This model is capable of performing different tasks through changing the prompts.
First, let's define a function to run a prompt.
Here are the tasks Florence-2 could perform:

### Caption

### Detailed Caption

### More Detailed Caption

### Caption to Phrase Grounding

caption to phrase grounding task requires additional text input, i.e. caption.
Caption to phrase grounding results format: 
{'<CAPTION_TO_PHRASE_GROUNDING>': {'bboxes': [[x1, y1, x2, y2], ...], 'labels': ['', '', ...]}}

### Object Detection

OD results format: 
{'<OD>': {'bboxes': [[x1, y1, x2, y2], ...], 
'labels': ['label1', 'label2', ...]} }

### Dense Region Caption

Dense region caption results format: 
{'<DENSE_REGION_CAPTION>' : {'bboxes': [[x1, y1, x2, y2], ...], 
'labels': ['label1', 'label2', ...]} }

### Region proposal

Dense region caption results format: 
{'<REGION_PROPOSAL>': {'bboxes': [[x1, y1, x2, y2], ...], 
'labels': ['', '', ...]}}

### OCR

### OCR with Region

OCR with region output format:
{'<OCR_WITH_REGION>': {'quad_boxes': [[x1, y1, x2, y2, x3, y3, x4, y4], ...], 'labels': ['text1', ...]}}

### Output confidence score with Object Detection

for More detailed examples, please refer to notebook

## Benchmarks

## Florence-2 Zero-shot performance

The following table presents the zero-shot performance of generalist vision foundation models on image captioning and object detection evaluation tasks. These models have not been exposed to the training data of the evaluation tasks during their training phase.
The following table continues the comparison with performance on other vision-language evaluation tasks.

## Florence-2 finetuned performance

We finetune Florence-2 models with a collection of downstream tasks, resulting two generalist models Florence-2-base-ft and Florence-2-large-ft that can conduct a wide range of downstream tasks.
The table below compares the performance of specialist and generalist models on various captioning and Visual Question Answering (VQA) tasks. Specialist models are fine-tuned specifically for each task, whereas generalist models are fine-tuned in a task-agnostic manner across all tasks. The symbol "▲" indicates the usage of external OCR as input.

## BibTex and citation info

[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for microsoft/Florence-2-large

## Spaces using microsoft/Florence-2-large 100

## Collection including microsoft/Florence-2-large

## Paper for microsoft/Florence-2-large


--------------------