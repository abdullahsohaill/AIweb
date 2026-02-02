# GPT-OSS-120B
**URL:** https://huggingface.co/openai/gpt-oss-120b
**Page Title:** openai/gpt-oss-120b · Hugging Face
--------------------

Try gpt-oss · Guides · Model card · OpenAI blog
Welcome to the gpt-oss series, OpenAI’s open-weight models designed for powerful reasoning, agentic tasks, and versatile developer use cases.
We’re releasing two flavors of these open models:
- gpt-oss-120b — for production, general purpose, high reasoning use cases that fit into a single 80GB GPU (like NVIDIA H100 or AMD MI300X) (117B parameters with 5.1B active parameters)
- gpt-oss-20b — for lower latency, and local or specialized use cases (21B parameters with 3.6B active parameters)
Both models were trained on our harmony response format and should only be used with the harmony format as it will not work correctly otherwise.
[LINK: harmony response format](https://github.com/openai/harmony)
This model card is dedicated to the larger gpt-oss-120b model. Check out gpt-oss-20b for the smaller model.

## Highlights

- Permissive Apache 2.0 license: Build freely without copyleft restrictions or patent risk—ideal for experimentation, customization, and commercial deployment.
- Configurable reasoning effort: Easily adjust the reasoning effort (low, medium, high) based on your specific use case and latency needs.
- Full chain-of-thought: Gain complete access to the model’s reasoning process, facilitating easier debugging and increased trust in outputs. It’s not intended to be shown to end users.
- Fine-tunable: Fully customize models to your specific use case through parameter fine-tuning.
- Agentic capabilities: Use the models’ native capabilities for function calling, web browsing , Python code execution , and Structured Outputs.
[LINK: web browsing](https://github.com/openai/gpt-oss/tree/main?tab=readme-ov-file#browser)
[LINK: Python code execution](https://github.com/openai/gpt-oss/tree/main?tab=readme-ov-file#python)
- MXFP4 quantization: The models were post-trained with MXFP4 quantization of the MoE weights, making gpt-oss-120b run on a single 80GB GPU (like NVIDIA H100 or AMD MI300X) and the gpt-oss-20b model run within 16GB of memory. All evals were performed with the same MXFP4 quantization.

## Inference examples

## Transformers

You can use gpt-oss-120b and gpt-oss-20b with Transformers. If you use the Transformers chat template, it will automatically apply the harmony response format . If you use model.generate directly, you need to apply the harmony format manually using the chat template or use our openai-harmony package.
[LINK: harmony response format](https://github.com/openai/harmony)
[LINK: openai-harmony](https://github.com/openai/harmony)
To get started, install the necessary dependencies to setup your environment:
Once, setup you can proceed to run the model by running the snippet below:
Alternatively, you can run the model via Transformers Serve to spin up a OpenAI-compatible webserver:
[LINK: Transformers Serve](https://huggingface.co/docs/transformers/main/serving)
Learn more about how to use gpt-oss with Transformers.

## vLLM

vLLM recommends using uv for Python dependency management. You can use vLLM to spin up an OpenAI-compatible webserver. The following command will automatically download the model and start the server.
Learn more about how to use gpt-oss with vLLM.

## PyTorch / Triton

To learn about how to use this model with PyTorch and Triton, check out our reference implementations in the gpt-oss repository .
[LINK: reference implementations in the gpt-oss repository](https://github.com/openai/gpt-oss?tab=readme-ov-file#reference-pytorch-implementation)

## Ollama

If you are trying to run gpt-oss on consumer hardware, you can use Ollama by running the following commands after installing Ollama .
Learn more about how to use gpt-oss with Ollama.
If you are using LM Studio you can use the following commands to download.
Check out our awesome list for a broader collection of gpt-oss resources and inference partners.
[LINK: awesome list](https://github.com/openai/gpt-oss/blob/main/awesome-gpt-oss.md)

## Download the model

You can download the model weights from the Hugging Face Hub directly from Hugging Face CLI:

## Reasoning levels

You can adjust the reasoning level that suits your task across three levels:
- Low: Fast responses for general dialogue.
- Medium: Balanced speed and detail.
- High: Deep and detailed analysis.
The reasoning level can be set in the system prompts, e.g., "Reasoning: high".

## Tool use

The gpt-oss models are excellent for:
- Web browsing (using built-in browsing tools)
- Function calling with defined schemas
- Agentic operations like browser tasks

## Fine-tuning

Both gpt-oss models can be fine-tuned for a variety of specialized use cases.
This larger model gpt-oss-120b can be fine-tuned on a single H100 node, whereas the smaller gpt-oss-20b can even be fine-tuned on consumer hardware.

## Citation

## Model tree for openai/gpt-oss-120b

## Spaces using openai/gpt-oss-120b 100

## Collection including openai/gpt-oss-120b

## Paper for openai/gpt-oss-120b

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
openai/gpt-oss-120b is supported by the following Inference Providers:

--------------------