# gpt-oss-120B-GGUF
**URL:** https://huggingface.co/unsloth/gpt-oss-120b-GGUF
**Page Title:** unsloth/gpt-oss-120b-GGUF · Hugging Face
--------------------

The F16 quant is gpt-oss in its original precision. All GGUFs have our fixes. Read our guide here.
[LINK: Read our guide here.](https://docs.unsloth.ai/basics/gpt-oss)
See our collection for all versions of gpt-oss including GGUF, 4-bit & 16-bit formats.
Learn to run gpt-oss correctly - Read our Guide .
[LINK: Read our Guide](https://docs.unsloth.ai/basics/gpt-oss)
See Unsloth Dynamic 2.0 GGUFs for our quantization benchmarks.
[LINK: Unsloth Dynamic 2.0 GGUFs](https://docs.unsloth.ai/basics/unsloth-dynamic-v2.0-gguf)

## ✨ Read our gpt-oss Guide here !

[LINK: here](https://docs.unsloth.ai/basics/gpt-oss)
- Read our Blog about gpt-oss support: unsloth.ai/blog/gpt-oss
- View the rest of our notebooks in our docs here .
[LINK: docs here](https://docs.unsloth.ai/get-started/unsloth-notebooks)
- Thank you to the llama.cpp team for their work on supporting this model. We wouldn't be able to release quants without them!
[LINK: llama.cpp](https://github.com/ggml-org/llama.cpp)

## gpt-oss-120b Details

Try gpt-oss · Guides · System card · OpenAI blog
Welcome to the gpt-oss series, OpenAI’s open-weight models designed for powerful reasoning, agentic tasks, and versatile developer use cases.
We’re releasing two flavors of the open models:
- gpt-oss-120b — for production, general purpose, high reasoning use cases that fits into a single H100 GPU (117B parameters with 5.1B active parameters)
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
- Native MXFP4 quantization: The models are trained with native MXFP4 precision for the MoE layer, making gpt-oss-120b run on a single H100 GPU and the gpt-oss-20b model run within 16GB of memory.

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
2-bit
3-bit
4-bit
5-bit
6-bit
8-bit
16-bit

## Model tree for unsloth/gpt-oss-120b-GGUF

Base model

## Collections including unsloth/gpt-oss-120b-GGUF


--------------------