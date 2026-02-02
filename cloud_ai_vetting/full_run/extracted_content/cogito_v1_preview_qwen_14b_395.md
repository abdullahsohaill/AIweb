# Cogito-v1-preview-qwen-14B
**URL:** https://huggingface.co/deepcogito/cogito-v1-preview-qwen-14B
**Page Title:** deepcogito/cogito-v1-preview-qwen-14B · Hugging Face
--------------------


## Cogito v1 preview - 14B

Blog Post
The Cogito LLMs are instruction tuned generative models (text in/text out). All models are released under an open license for commercial use.
- Cogito models are hybrid reasoning models. Each model can answer directly (standard LLM), or self-reflect before answering (like reasoning models).
- The LLMs are trained using Iterated Distillation and Amplification (IDA) - an scalable and efficient alignment strategy for superintelligence using iterative self-improvement.
- The models have been optimized for coding, STEM, instruction following and general helpfulness, and have significantly higher multilingual, coding and tool calling capabilities than size equivalent counterparts. In both standard and reasoning modes, Cogito v1-preview models outperform their size equivalent counterparts on common industry benchmarks.
- In both standard and reasoning modes, Cogito v1-preview models outperform their size equivalent counterparts on common industry benchmarks.
- Each model is trained in over 30 languages and supports a context length of 128k.

## Evaluations

We compare our models against the state of the art size equivalent models in direct mode as well as the reasoning mode. For the direct mode, we compare against Llama / Qwen instruct counterparts. For reasoning, we use Deepseek's R1 distilled counterparts / Qwen's QwQ model.
Livebench Global Average:
For detailed evaluations, please refer to the Blog Post .

## Usage

Here is a snippet below for usage with Transformers:

## Implementing extended thinking

- By default, the model will answer in the standard mode.
- To enable thinking, you can do any one of the two methods: Add a specific system prompt, or Set enable_thinking=True while applying the chat template.
- Add a specific system prompt, or
- Set enable_thinking=True while applying the chat template.

### Method 1 - Add a specific system prompt.

To enable thinking, simply use this in the system prompt system_instruction = 'Enable deep thinking subroutine.'
If you already have a system_instruction, then use system_instruction = 'Enable deep thinking subroutine.' + '\n\n' + system_instruction .
Here is an example -
Similarly, if you have a system prompt, you can append the DEEP_THINKING_INSTRUCTION to the beginning in this way -

### Method 2 - Set enable_thinking=True in the tokenizer

If you are using Huggingface tokenizers, then you can simply use add the argument enable_thinking=True to the tokenization (this option is added to the chat template).
Here is an example -

## Tool Calling

Cogito models support tool calling (single, parallel, multiple and parallel_multiple) both in standard and extended thinking mode.
Here is a snippet -
This will result in the output -
You can then generate text from this input as normal. If the model generates a tool call, you should add it to the chat like so:
and then call the tool and append the result, with the tool role, like so:
After that, you can generate() again to let the model use the tool result in the chat:
This should result in the string -

## License

This repository and the model weights are licensed under the Apache 2.0 License Agreement.

## Contact

If you would like to reach out to our team, send an email to contact@deepcogito.com .

## Model tree for deepcogito/cogito-v1-preview-qwen-14B

Base model

## Collection including deepcogito/cogito-v1-preview-qwen-14B


--------------------