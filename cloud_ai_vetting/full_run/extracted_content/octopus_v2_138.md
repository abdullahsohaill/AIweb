# Octopus V2
**URL:** https://huggingface.co/NexaAIDev/Octopus-v2
**Page Title:** NexaAI/Octopus-v2 · Hugging Face
--------------------


## Octopus V2: On-device language model for super agent

## Octopus V4 Release

We are excited to announce that Octopus v4 is now available! Octopus-V4-3B, an advanced open-source language model with 3 billion parameters, serves as the master node in Nexa AI's envisioned graph of language models. Tailored specifically for the MMLU benchmark topics, this model efficiently translates user queries into formats that specialized models can effectively process. It excels at directing these queries to the appropriate specialized model, ensuring precise and effective query handling.
check our papers and repos:
- paper
- Octopus V4 model page
- Octopus V4 quantized model page
- Octopus V4 github
[LINK: Octopus V4 github](https://github.com/NexaAI/octopus-v4)
Key Features of Octopus v4:
- 📱 Compact Size : Octopus-V4-3B is compact, enabling it to operate on smart devices efficiently and swiftly.
- 🐙 Accuracy : Octopus-V4-3B accurately maps user queries to the specialized model using a functional token design, enhancing its precision.
- 💪 Reformat Query : Octopus-V4-3B assists in converting natural human language into a more professional format, improving query description and resulting in more accurate responses.

## Octopus V3 Release

We are excited to announce that Octopus v3 is now available! check our technical report and Octopus V3 tweet !
Key Features of Octopus v3:
- Efficiency : Sub-billion parameters, making it less than half the size of its predecessor, Octopus v2.
- Multi-Modal Capabilities : Proceed both text and images inputs.
- Speed and Accuracy : Incorporate our patented functional token technology, achieving function calling accuracy on par with GPT-4V and GPT-4.
- Multilingual Support : Simultaneous support for English and Mandarin.
Check the Octopus V3 demo video for Android and iOS .

## Octopus V2 Release

After open-sourcing our model, we got many requests to compare our model with Apple's OpenELM and Microsoft's Phi-3 . Please see Evaluation section . From our benchmark dataset, Microsoft's Phi-3 achieves accuracy of 45.7% and the average inference latency is 10.2s. While Apple's OpenELM fails to generate function call, please see this screenshot . Our model, Octopus V2, achieves 99.5% accuracy and the average inference latency is 0.38s.
We are a very small team with many work. Please give us more time to prepare the code, and we will open source it. We hope Octopus v2 model will be helpful for you. Let's democratize AI agents for everyone. We've received many requests from car industry, health care, financial system etc. Octopus model is able to be applied to any function , and you can start to think about it now.
- Nexa AI Product - ArXiv - Video Demo

## Introduction

Octopus-V2-2B, an advanced open-source language model with 2 billion parameters, represents Nexa AI's research breakthrough in the application of large language models (LLMs) for function calling, specifically tailored for Android APIs. Unlike Retrieval-Augmented Generation (RAG) methods, which require detailed descriptions of potential function arguments—sometimes needing up to tens of thousands of input tokens—Octopus-V2-2B introduces a unique functional token strategy for both its training and inference stages. This approach not only allows it to achieve performance levels comparable to GPT-4 but also significantly enhances its inference speed beyond that of RAG-based methods, making it especially beneficial for edge computing devices.
📱 On-device Applications :  Octopus-V2-2B is engineered to operate seamlessly on Android devices, extending its utility across a wide range of applications, from Android system management to the orchestration of multiple devices.
🚀 Inference Speed : When benchmarked, Octopus-V2-2B demonstrates a remarkable inference speed, outperforming the combination of "Llama7B + RAG solution" by a factor of 36X on a single A100 GPU. Furthermore, compared to GPT-4-turbo (gpt-4-0125-preview), which relies on clusters A100/H100 GPUs, Octopus-V2-2B is 168% faster. This efficiency is attributed to our functional token design.
🐙 Accuracy : Octopus-V2-2B not only excels in speed but also in accuracy, surpassing the "Llama7B + RAG solution" in function call accuracy by 31%. It achieves a function call accuracy comparable to GPT-4 and RAG + GPT-3.5, with scores ranging between 98% and 100% across benchmark datasets.
💪 Function Calling Capabilities : Octopus-V2-2B is capable of generating individual, nested, and parallel function calls across a variety of complex scenarios.

## Example Use Cases

You can run the model on a GPU using the following code.

## Evaluation

The benchmark result can be viewed in this excel , which has been manually verified. Microsoft's Phi-3 model achieved an accuracy of 45.7%, with an average inference latency of 10.2 seconds. Meanwhile, Apple's OpenELM was unable to generate a function call, as shown in this screenshot . Additionally, OpenELM's score on the MMLU benchmark is quite low at 26.7, compared to Google's Gemma 2B, which scored 42.3.
Note : One can notice that the query includes all necessary parameters used for a function. It is expected that query includes all parameters during inference as well.

## Training Data

We wrote 20 Android API descriptions to used to train the models, see this file for details. The Android API implementations for our demos, and our training data will be published later. Below is one Android API description example

## License

This model was trained on commercially viable data. For use of our model, refer to the license information .

## References

We thank the Google Gemma team for their amazing models!

## Citation

## Contact

Please contact us to reach out for any issues and comments!

## Model tree for NexaAI/Octopus-v2

Base model

## Spaces using NexaAI/Octopus-v2 18

## Collection including NexaAI/Octopus-v2

## Papers for NexaAI/Octopus-v2


--------------------