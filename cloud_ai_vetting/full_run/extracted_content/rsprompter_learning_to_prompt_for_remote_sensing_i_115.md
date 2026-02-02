# RSPrompter: Learning to Prompt for Remote Sensing Instance Segmentation based on Visual Foundation Model
**URL:** https://huggingface.co/papers/2306.16269
**Page Title:** Paper page - RSPrompter: Learning to Prompt for Remote Sensing Instance Segmentation based on Visual Foundation Model
--------------------


## RSPrompter: Learning to Prompt for Remote Sensing Instance Segmentation
  based on Visual Foundation Model

## Abstract

RSPrompter enhances SAM's instance segmentation for remote sensing by learning prompts, improving semantic segmentation accuracy and applicability.
Leveraging vast training data (SA-1B), the foundation Segment Anything Model ( SAM ) proposed by Meta AI Research exhibits remarkable generalization and
zero-shot capabilities. Nonetheless, as a category-agnostic instance
segmentation method, SAM heavily depends on prior manual guidance involving
points, boxes, and coarse-grained masks. Additionally, its performance on remote sensing image segmentation tasks has yet to be fully explored and
demonstrated. In this paper, we consider designing an automated instance
segmentation approach for remote sensing images based on the SAM foundation
model, incorporating semantic category information . Inspired by prompt
learning, we propose a method to learn the generation of appropriate prompts
for SAM input. This enables SAM to produce semantically discernible
segmentation results for remote sensing images, which we refer to as
RSPrompter. We also suggest several ongoing derivatives for instance
segmentation tasks, based on recent developments in the SAM community, and
compare their performance with RSPrompter. Extensive experimental results on
the WHU building , NWPU VHR-10 , and SSDD datasets validate the efficacy of our
proposed method. Our code is accessible at
https://kyanchen.github.io/RSPrompter.
[LINK: GitHub 649 auto](https://github.com/KyanChen/RSPrompter)

### Community

· Sign up or log in to comment

## Models citing this paper 0

No model linking this paper

## Datasets citing this paper 0

No dataset linking this paper

### Spaces citing this paper 2

## Collections including this paper 0

No Collection including this paper

--------------------