# Magistral-Small-2509
**URL:** https://huggingface.co/mistralai/Magistral-Small-2509
**Page Title:** mistralai/Magistral-Small-2509 · Hugging Face
--------------------


## Magistral Small 1.2

Building upon Mistral Small 3.2 (2506) , with added reasoning capabilities , undergoing SFT from Magistral Medium traces and RL on top, it's a small, efficient reasoning model with 24B parameters.
Magistral Small can be deployed locally, fitting within a single RTX 4090 or a 32GB RAM MacBook once quantized.
Learn more about Magistral in our blog post .
The model was presented in the paper Magistral .

## Updates compared with Magistral Small 1.1

- Multimodality : The model now has a vision encoder and can take multimodal inputs, extending its reasoning capabilities to vision.
- Performance upgrade : Magistral Small 1.2 should give you significantly better performance than Magistral Small 1.1 as seen in the benchmark results .
- Better tone and persona : You should experience better LaTeX and Markdown formatting, and shorter answers on easy general prompts.
- Finite generation : The model is less likely to enter infinite generation loops.
- Special think tokens : [THINK] and [/THINK] special tokens encapsulate the reasoning content in a thinking chunk. This makes it easier to parse the reasoning trace and prevents confusion when the '[THINK]' token is given as a string in the prompt.
- Reasoning prompt : The reasoning prompt is given in the system prompt.

## Key Features

- Reasoning: Capable of long chains of reasoning traces before providing an answer.
- Multilingual: Supports dozens of languages, including English, French, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Nepali, Polish, Portuguese, Romanian, Russian, Serbian, Spanish, Turkish, Ukrainian, Vietnamese, Arabic, Bengali, Chinese, and Farsi.
- Vision : Vision capabilities enable the model to analyze images and reason based on visual content in addition to text.
- Apache 2.0 License: Open license allowing usage and modification for both commercial and non-commercial purposes.
- Context Window: A 128k context window. Performance might degrade past 40k but Magistral should still give good results. Hence we recommend to leave the maximum model length to 128k and only lower if you encounter low performance.

## Benchmark Results

## Sampling parameters

Please make sure to use:
- top_p : 0.95
- temperature : 0.7
- max_tokens : 131072

## Basic Chat Template

We highly recommend including the following system prompt for the best results, you can edit and customise it if needed for your specific use case.
The [THINK] and [/THINK] are special tokens that must be encoded as such.
Please make sure to use mistral-common as the source of truth . Find below examples from libraries supporting mistral-common .
[LINK: mistral-common](https://github.com/mistralai/mistral-common)
We invite you to choose, depending on your use case and requirements, between keeping reasoning traces during multi-turn interactions or keeping only the final assistant response.

## Usage

The model can be used with the following frameworks.

### Inference

- vllm (recommended) : See below
[LINK: vllm (recommended)](https://github.com/vllm-project/vllm)
- transformers : See below
[LINK: transformers](https://github.com/huggingface/transformers)
- llama.cpp : See https://huggingface.co/mistralai/Magistral-Small-2509-GGUF
[LINK: llama.cpp](https://github.com/ggml-org/llama.cpp)
- Unsloth GGUFs : See https://huggingface.co/unsloth/Magistral-Small-2509-GGUF
- Kaggle : See https://www.kaggle.com/models/mistral-ai/magistral-small-2509
- LM Studio : See https://lmstudio.ai/models/mistralai/magistral-small-2509

### Fine-tuning

- Axolotl : See https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/magistral
[LINK: https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/magistral](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/magistral)
- Unsloth : See https://docs.unsloth.ai/models/tutorials-how-to-fine-tune-and-run-llms/magistral-how-to-run-and-fine-tune
[LINK: https://docs.unsloth.ai/models/tutorials-how-to-fine-tune-and-run-llms/magistral-how-to-run-and-fine-tune](https://docs.unsloth.ai/models/tutorials-how-to-fine-tune-and-run-llms/magistral-how-to-run-and-fine-tune)

### vLLM (recommended)

We recommend using this model with the vLLM library to implement production-ready inference pipelines.
[LINK: vLLM library](https://github.com/vllm-project/vllm)
Installation
Make sure you install the latest vLLM code:
[LINK: vLLM](https://github.com/vllm-project/vllm/)
Doing so should automatically install mistral_common >= 1.8.5 .
[LINK: mistral_common >= 1.8.5](https://github.com/mistralai/mistral-common/releases/tag/v1.8.5)
To check:
You can also make use of a ready-to-go docker image or on the docker hub .
[LINK: docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile)
Serve model as follows:
Ping model as follows:

### Transformers

Make sure you install the latest Transformers version:
[LINK: Transformers](https://github.com/huggingface/transformers/)
This should also install mistral_common >= 1.8.5
[LINK: mistral_common >= 1.8.5](https://github.com/mistralai/mistral-common/releases/tag/v1.8.5)
To check:
Now you can use Transformers with Magistral:
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Magistral-Small-2509

Base model

## Spaces using mistralai/Magistral-Small-2509 3

## Paper for mistralai/Magistral-Small-2509


--------------------