# Phi-3.5-vision-instruct
**URL:** https://huggingface.co/microsoft/Phi-3.5-vision-instruct
**Page Title:** microsoft/Phi-3.5-vision-instruct · Hugging Face
--------------------


## Model Summary

Phi-3.5-vision is a lightweight, state-of-the-art open multimodal model built upon datasets which include - synthetic data and filtered publicly available websites - with a focus on very high-quality, reasoning dense data both on text and vision. The model belongs to the Phi-3 model family, and the multimodal version comes with 128K context length (in tokens) it can support. The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.
🏡 Phi-3 Portal 📰 Phi-3 Microsoft Blog 📖 Phi-3 Technical Report 👩‍🍳 Phi-3 Cookbook 🖥️ Try It
[LINK: Phi-3 Cookbook](https://github.com/microsoft/Phi-3CookBook)
Phi-3.5 : [mini-instruct] ; [MoE-instruct] ; [vision-instruct]

## Intended Uses

### Primary Use Cases

The model is intended for broad commercial and research use in English. The model provides uses for general purpose AI systems and applications with visual and text input capabilities which require:
- Memory/compute constrained environments
- Latency bound scenarios
- General image understanding
- Optical character recognition
- Chart and table understanding
- Multiple image comparison
- Multi-image or video clip summarization
Our model is designed to accelerate research on language and multimodal models, for use as a building block for generative AI powered features.

### Use Case Considerations

Our models are not specifically designed or evaluated for all downstream purposes. Developers should consider common limitations of language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fariness before using within a specific downstream use case, particularly for high risk scenarios. Developers should be aware of and adhere to applicable laws or regulations (including privacy, trade compliance laws, etc.) that are relevant to their use case.
Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.

## Release Notes

In this release, the model enables multi-frame image understanding and reasoning which is based on valuable customer feedback. The hero example multi-frame capabilities include detailed image comparison, multi-image summarization/storytelling and video summarization, which have broad applications in Office scenarios. We also observed performance improvement on most single image benchmarks, e.g., boost MMMU performance from 40.2 to 43.0, MMBench performance from 80.5 to 81.9, document understanding benchmark TextVQA from 70.9 to 72.0. We believe most use cases will benefit from this release, but we encourage users to test the new model in their AI applications. We appreciate the enthusiastic adoption of the Phi-3 model family and continue to welcome all the feedback from the community.
Below are the comparison results on existing multi-image benchmarks. On average, our model outperforms competitor models on the same size and competitive with much bigger models on multi-frame capabilities and video summarization.
BLINK : a benchmark with 14 visual tasks that humans can solve very quickly but are still hard for current multimodal LLMs.
Video-MME : comprehensively assess the capabilities of MLLMs in processing video data, covering a wide range of visual domains, temporal durations, and data modalities.

## Usage

### Requirements

The current transformers version can be verified with: pip list | grep transformers .
Examples of required packages:
Phi-3.5-vision-Instruct is also available in Azure AI Studio .

### Input Formats

Given the nature of the training data, the Phi-3.5-vision model is best suited for prompts using the chat format as follows:
Single image:
Multi-turn conversations:
For multi-image usage, add multiple image placeholders in the front of the prompts. <|image_{}|> index should start from 1. One example of prompt is shown as follows:

### Loading the model locally

After obtaining the Phi-3.5-vision-instruct model checkpoints, users can use this sample code for inference.
Notes:
- to achieve best performances we suggest to set num_crops=4 for multi-frame and num_crops=16 for single-frame.
- to turn off flash_attention users can set _ attn_implementation='eager'

## Responsible AI Considerations

Like other models, the Phi family of models can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:
- Quality of Service: The Phi models are trained primarily on English text. Languages other than English will experience worse performance. English language varieties with less representation in the training data might experience worse performance than standard American English.
- Representation of Harms & Perpetuation of Stereotypes: These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.
- Inappropriate or Offensive Content: These models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.
- Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.
- Limited Scope for Code: Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.
Developers should apply responsible AI best practices and are responsible for ensuring that a specific use case complies with relevant laws and regulations (e.g. privacy, trade, etc.). Important areas for consideration include:
- Allocation: Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques.
- High-Risk Scenarios: Developers should assess suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.
- Misinformation: Models may produce inaccurate information. Developers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).
- Generation of Harmful Content: Developers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.
- Misuse: Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.
- Identification of individuals: models with vision capabilities may have the potential to uniquely identify individuals in images. Safety post-training steers the model to refuse such requests, but developers should consider and implement, as appropriate, additional mitigations or user consent flows as required in their respective jurisdiction, (e.g., building measures to blur faces in image inputs before processing).

## Training

### Models

Architecture: Phi-3.5-vision has 4.2B parameters and contains image encoder, connector, projector, and Phi-3 Mini language model. Inputs: Text and Image. It’s best suited for prompts using the chat format. Context length: 128K tokens GPUs: 256 A100-80G Training time: 6 days Training data: 500B tokens (vision tokens + text tokens) Outputs: Generated text in response to the input Dates: Trained between July and August 2024 Status: This is a static model trained on an offline text dataset with cutoff date March 15, 2024. Future versions of the tuned models may be released as we improve models. Release date: August 2024

### Data Overview

Our training data includes a wide variety of sources, and is a combination of
- publicly available documents filtered rigorously for quality, selected high-quality educational data and code;
- selected high-quality image-text interleave data;
- newly created synthetic, “textbook-like” data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world (science, daily activities, theory of mind, etc.), newly created image data, e.g., chart/table/diagram/slides, newly created multi-image and video data, e.g., short video clips/pair of two similar images;
- high quality chat format supervised data covering various topics to reflect human preferences on different aspects such as instruct-following, truthfulness, honesty and helpfulness.
The data collection process involved sourcing information from publicly available documents, with a meticulous approach to filtering out undesirable documents and images. To safeguard privacy, we carefully filtered various image and text data sources to remove or scrub any potentially personal data from the training data. More details about data can be found in the Phi-3 Technical Report .

### How to finetune?

We recommend user to take a look at the Phi-3 CookBook finetuning recipe for Vision
[LINK: Phi-3 CookBook finetuning recipe for Vision](https://github.com/microsoft/Phi-3CookBook/blob/main/md/04.Fine-tuning/FineTuning_Vision.md)

## Benchmarks

To understand the capabilities, we compare Phi-3.5-vision with a set of models over a variety of zero-shot benchmarks using our internal benchmark platform. At the high-level overview of the model quality on representative benchmarks:

## Safety Evaluation and Red-Teaming

Approach The Phi-3 family of models has adopted a robust safety post-training approach. This approach leverages a variety of both open-source and in-house generated datasets. 
The overall technique employed to do the safety alignment is a combination of SFT (Supervised Fine-Tuning) and RLHF (Reinforcement Learning from Human Feedback) approaches
by utilizing human-labeled and synthetic English-language datasets, including publicly available datasets focusing on helpfulness and harmlessness as well as various 
questions and answers targeted to multiple safety categories.
Safety Evaluation We leveraged various evaluation techniques including red teaming, adversarial conversation simulations, and safety evaluation benchmark datasets to evaluate Phi-3.5 
models' propensity to produce undesirable outputs across multiple risk categories. Several approaches were used to compensate for the limitations of one approach alone. 
Please refer to the technical report for more details of our safety alignment.

## Software

- PyTorch
[LINK: PyTorch](https://github.com/pytorch/pytorch)
- Transformers
[LINK: Transformers](https://github.com/huggingface/transformers)
- Flash-Attention
[LINK: Flash-Attention](https://github.com/HazyResearch/flash-attention)

## Hardware

Note that by default, the Phi-3.5-Mini-Instruct model uses flash attention, which requires certain types of GPU hardware to run. We have tested on the following GPU types:
- NVIDIA A100
- NVIDIA A6000
- NVIDIA H100

## License

The model is licensed under the MIT license .

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow Microsoft’s Trademark & Brand Guidelines . Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.

## Data Summary

https://huggingface.co/microsoft/Phi-3.5-vision-instruct/blob/main/data_summary_card.md

## Model tree for microsoft/Phi-3.5-vision-instruct

## Spaces using microsoft/Phi-3.5-vision-instruct 100

## Collection including microsoft/Phi-3.5-vision-instruct

## Paper for microsoft/Phi-3.5-vision-instruct


--------------------