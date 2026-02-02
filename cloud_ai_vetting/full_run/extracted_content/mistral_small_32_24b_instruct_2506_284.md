# Mistral-Small-3.2-24B-Instruct-2506
**URL:** https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506
**Page Title:** mistralai/Mistral-Small-3.2-24B-Instruct-2506 · Hugging Face
--------------------


## Mistral-Small-3.2-24B-Instruct-2506

Mistral-Small-3.2-24B-Instruct-2506 is a minor update of Mistral-Small-3.1-24B-Instruct-2503 .
Small-3.2 improves in the following categories:
- Instruction following : Small-3.2 is better at following precise instructions
- Repetition errors : Small-3.2 produces less infinite generations or repetitive answers
- Function calling : Small-3.2's function calling template is more robust (see here and examples )
[LINK: here](https://github.com/mistralai/mistral-common/blob/535b4d0a0fc94674ea17db6cf8dc2079b81cbcfa/src/mistral_common/tokens/tokenizers/instruct.py#L778)
In all other categories Small-3.2 should match or slightly improve compared to Mistral-Small-3.1-24B-Instruct-2503 .

## Key Features

- same as Mistral-Small-3.1-24B-Instruct-2503

## Benchmark Results

We compare Mistral-Small-3.2-24B to Mistral-Small-3.1-24B-Instruct-2503 .
For more comparison against other models of similar size, please check Mistral-Small-3.1's Benchmarks'

### Text

Small 3.2 reduces infinite generations by 2x on challenging, long and repetitive prompts.

### Vision

## Usage

The model can be used with the following frameworks;
- vllm (recommended) : See here
[LINK: vllm (recommended)](https://github.com/vllm-project/vllm)
- transformers : See here
[LINK: transformers](https://github.com/huggingface/transformers)
Note 1 : We recommend using a relatively low temperature, such as temperature=0.15 .
Note 2 : Make sure to add a system prompt to the model to best tailor it to your needs. If you want to use the model as a general assistant, we recommend to use the one provided in the SYSTEM_PROMPT.txt file.

### vLLM (recommended)

We recommend using this model with vLLM .
[LINK: vLLM](https://github.com/vllm-project/vllm)
Make sure to install vLLM >= 0.9.1 :
[LINK: vLLM >= 0.9.1](https://github.com/vllm-project/vllm/releases/tag/v0.9.1)
Doing so should automatically install mistral_common >= 1.6.2 .
[LINK: mistral_common >= 1.6.2](https://github.com/mistralai/mistral-common/releases/tag/v1.6.2)
To check:
You can also make use of a ready-to-go docker image or on the docker hub .
[LINK: docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile)
We recommend that you use Mistral-Small-3.2-24B-Instruct-2506 in a server/client setting.
- Spin up a server:
Note: Running Mistral-Small-3.2-24B-Instruct-2506 on GPU requires ~55 GB of GPU RAM in bf16 or fp16.
- To ping the client you can use a simple Python snippet. See the following examples.
Leverage the vision capabilities of Mistral-Small-3.2-24B-Instruct-2506 to make the best choice given a scenario, go catch them all !
Mistral-Small-3.2-24B-Instruct-2506 is excellent at function / tool calling tasks via vLLM. E.g.:
Mistral-Small-3.2-24B-Instruct-2506 will follow your instructions down to the last letter !

### Transformers

You can also use Mistral-Small-3.2-24B-Instruct-2506 with Transformers !
To make the best use of our model with Transformers make sure to have installed mistral-common >= 1.6.2 to use our tokenizer.
[LINK: installed](https://github.com/mistralai/mistral-common)
Then load our tokenizer along with the model and generate:
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Mistral-Small-3.2-24B-Instruct-2506

Base model

## Spaces using mistralai/Mistral-Small-3.2-24B-Instruct-2506 14


--------------------