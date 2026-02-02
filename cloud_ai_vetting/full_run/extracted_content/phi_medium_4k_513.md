# Phi-Medium 4k
**URL:** https://huggingface.co/microsoft/Phi-3-medium-4k-instruct
**Page Title:** microsoft/Phi-3-medium-4k-instruct · Hugging Face
--------------------

🎉 Phi-3.5 : [mini-instruct] ; [MoE-instruct] ; [vision-instruct]

## Model Summary

The Phi-3-Medium-4K-Instruct is a 14B parameters, lightweight, state-of-the-art open model trained with the Phi-3 datasets that includes both synthetic data and the filtered publicly available websites data with a focus on high-quality and reasoning dense properties.
The model belongs to the Phi-3 family with the Medium version in two variants 4K and 128K which is the context length (in tokens) that it can support.
The model has undergone a post-training process that incorporates both supervised fine-tuning and direct preference optimization for the instruction following and safety measures.
When assessed against benchmarks testing common sense, language understanding, math, code, long context and logical reasoning, Phi-3-Medium-4K-Instruct showcased a robust and state-of-the-art performance among models of the same-size and next-size-up.
Resources and Technical Documentation:
- Phi-3 Microsoft Blog
- Phi-3 Technical Report
- Phi-3 on Azure AI Studio
- Phi-3 Cookbook
[LINK: Phi-3 Cookbook](https://github.com/microsoft/Phi-3CookBook)

## Intended Uses

Primary use cases
The model is intended for broad commercial and research use in English. The model provides uses for general purpose AI systems and applications which require:
- Memory/compute constrained environments
- Latency bound scenarios
- Strong reasoning (especially code, math and logic)
Our model is designed to accelerate research on language and multimodal models, for use as a building block for generative AI powered features.
Use case considerations
Our models are not specifically designed or evaluated for all downstream purposes. Developers should consider common limitations of language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fariness before using within a specific downstream use case, particularly for high risk scenarios. Developers should be aware of and adhere to applicable laws or regulations (including privacy, trade compliance laws, etc.) that are relevant to their use case.
Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.

## How to Use

Phi-3-Medium-4K-Instruct has been integrated in the development version (4.40.2) of transformers . Until the official version is released through pip , ensure that you are doing one of the following:
- When loading the model, ensure that trust_remote_code=True is passed as an argument of the from_pretrained() function.
When loading the model, ensure that trust_remote_code=True is passed as an argument of the from_pretrained() function.
- Update your local transformers to the development version: pip uninstall -y transformers && pip install git+https://github.com/huggingface/transformers . The previous command is an alternative to cloning and installing from the source.
Update your local transformers to the development version: pip uninstall -y transformers && pip install git+https://github.com/huggingface/transformers . The previous command is an alternative to cloning and installing from the source.
The current transformers version can be verified with: pip list | grep transformers .
Phi-3-Medium-4K-Instruct is also available in Azure AI Studio .

### Tokenizer

Phi-3-Medium-4K-Instruct supports a vocabulary size of up to 32064 tokens. The tokenizer files already provide placeholder tokens that can be used for downstream fine-tuning, but they can also be extended up to the model's vocabulary size.

### Chat Format

Given the nature of the training data, the Phi-3-Medium-4K-Instruct model is best suited for prompts using the chat format as follows. 
You can provide the prompt as a question with a generic template as follow:
For example:
where the model generates the text after <|assistant|> . In case of few-shots prompt, the prompt can be formatted as the following:

### Sample inference code

This code snippets show how to get quickly started with running the model on a GPU:
Some applications/frameworks might not include a BOS token ( <s> ) at the start of the conversation. Please ensure that it is included since it provides more reliable results.

## Responsible AI Considerations

Like other language models, the Phi series models can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:
- Quality of Service: the Phi models are trained primarily on English text. Languages other than English will experience worse performance. English language varieties with less representation in the training data might experience worse performance than standard American English.
- Representation of Harms & Perpetuation of Stereotypes: These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.
- Inappropriate or Offensive Content: these models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.
- Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.
- Limited Scope for Code: Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.
Developers should apply responsible AI best practices and are responsible for ensuring that a specific use case complies with relevant laws and regulations (e.g. privacy, trade, etc.). Important areas for consideration include:
- Allocation: Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques.
- High-Risk Scenarios: Developers should assess suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.
- Misinformation: Models may produce inaccurate information. Developers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).
- Generation of Harmful Content: Developers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.
- Misuse: Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.

## Training

### Model

- Architecture: Phi-3-Medium-4K-Instruct has 14B parameters and is a dense decoder-only Transformer model. The model is fine-tuned with Supervised fine-tuning (SFT) and Direct Preference Optimization (DPO) to ensure alignment with human preferences and safety guidlines.
- Inputs: Text. It is best suited for prompts using chat format.
- Context length: 4K tokens
- GPUs: 512 H100-80G
- Training time: 42 days
- Training data: 4.8T tokens
- Outputs: Generated text in response to the input
- Dates: Our models were trained between February and April 2024
- Status: This is a static model trained on an offline dataset with cutoff date October 2023. Future versions of the tuned models may be released as we improve models.
- Release dates: The model weight is released on May 21, 2024.

### Datasets

Our training data includes a wide variety of sources, totaling 4.8 trillion tokens (including 10% multilingual), and is a combination of
- Publicly available documents filtered rigorously for quality, selected high-quality educational data, and code;
- Newly created synthetic, “textbook-like” data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world (science, daily activities, theory of mind, etc.);
- High quality chat format supervised data covering various topics to reflect human preferences on different aspects such as instruct-following, truthfulness, honesty and helpfulness.
We are focusing on the quality of data that could potentially improve the reasoning ability for the model, and we filter the publicly available documents to contain the correct level of knowledge. As an example, the result of a game in premier league in a particular day might be good training data for frontier models, but we need to remove such information to leave more model capacity for reasoning for the small size models. More details about data can be found in the Phi-3 Technical Report .

## Benchmarks

We report the results for Phi-3-Medium-4K-Instruct on standard open-source benchmarks measuring the model's reasoning ability (both common sense reasoning and logical reasoning). We compare to Mixtral-8x22b, Gemini-Pro, Command R+ 104B, Llama-3-70B-Instruct, GPT-3.5-Turbo-1106, and GPT-4-Turbo-1106(Chat).
All the reported numbers are produced with the exact same pipeline to ensure that the numbers are comparable. These numbers might differ from other published numbers due to slightly different choices in the evaluation.
As is now standard, we use few-shot prompts to evaluate the models, at temperature 0. 
The prompts and number of shots are part of a Microsoft internal tool to evaluate language models, and in particular we did no optimization to the pipeline for Phi-3.
More specifically, we do not change prompts, pick different few-shot examples, change prompt format, or do any other form of optimization for the model.
The number of k–shot examples is listed per-benchmark.
We take a closer look at different categories across 80 public benchmark datasets at the table below:

## Software

- PyTorch
[LINK: PyTorch](https://github.com/pytorch/pytorch)
- DeepSpeed
[LINK: DeepSpeed](https://github.com/microsoft/DeepSpeed)
- Transformers
[LINK: Transformers](https://github.com/huggingface/transformers)
- Flash-Attention
[LINK: Flash-Attention](https://github.com/HazyResearch/flash-attention)

## Hardware

Note that by default, the Phi-3-Medium model uses flash attention, which requires certain types of GPU hardware to run. We have tested on the following GPU types:
- NVIDIA A100
- NVIDIA A6000
- NVIDIA H100
If you want to run the model on:
- Optimized inference on GPU, CPU, and Mobile: use the ONNX models 4K

## Cross Platform Support

ONNX runtime ecosystem now supports Phi3 Medium models  across platforms and hardware. 
Optimized phi-3 models are also published here in ONNX format, to run with ONNX Runtime on CPU and GPU across devices, including server platforms, Windows, Linux and Mac desktops, and mobile CPUs, with the precision best suited to each of these targets. DirectML GPU acceleration is supported for Windows desktops GPUs (AMD, Intel, and NVIDIA). Along with DML, ONNX Runtime provides cross platform support for Phi3 Medium  across a range of devices CPU, GPU, and mobile. 
Here are some of the optimized configurations we have added:
- ONNX models for int4 DML: Quantized to int4 via AWQ
- ONNX model for fp16 CUDA
- ONNX model for int4 CUDA: Quantized to int4 via RTN
- ONNX model for int4 CPU and Mobile: Quantized to int4 via RTN

## License

The model is licensed under the MIT license .

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow Microsoft’s Trademark & Brand Guidelines . Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.

## Data Summary

https://huggingface.co/microsoft/Phi-3-medium-4k-instruct/blob/main/data_summary_card.md

## Model tree for microsoft/Phi-3-medium-4k-instruct

## Spaces using microsoft/Phi-3-medium-4k-instruct 42

## Collection including microsoft/Phi-3-medium-4k-instruct


--------------------