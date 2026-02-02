# AskUI/PTA-1
**URL:** https://huggingface.co/AskUI/PTA-1
**Page Title:** AskUI/PTA-1 · Hugging Face
--------------------


## PTA-1: Controlling Computers with Small Models

PTA (Prompt-to-Automation) is a vision language model for computer & phone automation, based on Florence-2. 
With only 270M parameters it outperforms much larger models in GUI text and element localization.
This enables low-latency computer automation with local execution.
▶️ Try the demo at: AskUI/PTA-1
Model Input: Screenshot + description_of_target_element
Model Output: BoundingBox for Target Element

## How to Get Started with the Model

Use the code below to get started with the model.
Requirements: torch, timm, einops, Pillow, transformers

## Evaluation

Note: This is a first version of our evaluation, based on 999 samples (333 samples from each dataset). 
We are still running all models on the full test sets, and we are seeing ±5% deviations for a subset of the models we have already evaluated.
* Models is known to be trained on the train split of that dataset.
The high benchmark scores for our model are partially due to data bias. 
Therefore, we expect users of the model to fine-tune it according to the data distributions of their use case.
Click success rate is calculated as the number of clicks inside the target bounding box relative to all clicks. 
If a model predicts a target bounding box instead of a click coordinate, its center is used as its click prediction.
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for AskUI/PTA-1

Base model

## Space using AskUI/PTA-1 1

## Collection including AskUI/PTA-1


--------------------