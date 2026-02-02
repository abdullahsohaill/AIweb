# Hermes-3-Llama-3.1-8B
**URL:** https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B
**Page Title:** NousResearch/Hermes-3-Llama-3.1-8B · Hugging Face
--------------------


## Hermes 3 - Llama-3.1 8B

## Model Description

Hermes 3 is the latest version of our flagship Hermes series of LLMs by Nous Research.
For more details on new capabilities, training results, and more, see the Hermes 3 Technical Report .
Hermes 3 is a generalist language model with many improvements over Hermes 2, including advanced agentic capabilities, much better roleplaying, reasoning, multi-turn conversation, long context coherence, and improvements across the board.
The ethos of the Hermes series of models is focused on aligning LLMs to the user, with powerful steering capabilities and control given to the end user.
The Hermes 3 series builds and expands on the Hermes 2 set of capabilities, including more powerful and reliable function calling and structured output capabilities, generalist assistant capabilities, and improved code generation skills.

## Benchmarks

Hermes 3 is competitive, if not superior, to Llama-3.1 Instruct models at general capabilities, with varying strengths and weaknesses attributable between the two.
Full benchmark comparisons below:

## Prompt Format

Hermes 3 uses ChatML as the prompt format, opening up a much more structured system for engaging the LLM in multi-turn chat dialogue.
System prompts allow steerability and interesting new ways to interact with an LLM, guiding rules, roles, and stylistic choices of the model.
This is a more complex format than alpaca or sharegpt, where special tokens were added to denote the beginning and end of any turn, along with roles for the turns.
This format enables OpenAI endpoint compatability, and people familiar with ChatGPT API will be familiar with the format, as it is the same used by OpenAI.
Prompt with system instruction (Use whatever system prompt you like, this is just an example!):
This prompt is available as a chat template , which means you can format messages using the tokenizer.apply_chat_template() method:
[LINK: chat template](https://huggingface.co/docs/transformers/main/chat_templating)
When tokenizing messages for generation, set add_generation_prompt=True when calling apply_chat_template() . This will append <|im_start|>assistant\n to your prompt, to ensure
that the model continues with an assistant response.
To utilize the prompt format without a system prompt, simply leave the line out.

## Prompt Format for Function Calling

Our model was trained on specific system prompts and structures for Function Calling.
You should use the system role with this message, followed by a function signature json as this example shows here.
To complete the function call, create a user prompt that follows the above system prompt, like so:
The model will then generate a tool call, which your inference code must parse, and plug into a function (see example inference code here: https://github.com/NousResearch/Hermes-Function-Calling ):
[LINK: https://github.com/NousResearch/Hermes-Function-Calling](https://github.com/NousResearch/Hermes-Function-Calling)
Once you parse the tool call, call the api and get the returned values for the call, and pass it back in as a new role, tool like so:
The assistant will then read in that data from the function's response, and generate a natural language response:

## Prompt Format for JSON Mode / Structured Outputs

Our model was also trained on a specific system prompt for Structured Outputs, which should respond with only a json object response, in a specific json schema.
Your schema can be made from a pydantic object using our codebase, with the standalone script jsonmode.py available here: https://github.com/NousResearch/Hermes-Function-Calling/tree/main
[LINK: https://github.com/NousResearch/Hermes-Function-Calling/tree/main](https://github.com/NousResearch/Hermes-Function-Calling/tree/main)
Given the {schema} that you provide, it should follow the format of that json to create it's response, all you have to do is give a typical user prompt, and it will respond in JSON.

## Inference

Here is example code using HuggingFace Transformers to inference the model
You can also run this model with vLLM, by running the following in your terminal after pip install vllm
vllm serve NousResearch/Hermes-3-Llama-3.1-8B

## Inference Code for Function Calling:

All code for utilizing, parsing, and building function calling templates is available on our github: https://github.com/NousResearch/Hermes-Function-Calling
[LINK: https://github.com/NousResearch/Hermes-Function-Calling](https://github.com/NousResearch/Hermes-Function-Calling)

## Quantized Versions:

GGUF Quants: https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF

## How to cite:

## Open LLM Leaderboard Evaluation Results

Detailed results can be found here

## Model tree for NousResearch/Hermes-3-Llama-3.1-8B

Base model

## Spaces using NousResearch/Hermes-3-Llama-3.1-8B 75

## Collection including NousResearch/Hermes-3-Llama-3.1-8B

## Paper for NousResearch/Hermes-3-Llama-3.1-8B

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
NousResearch/Hermes-3-Llama-3.1-8B is supported by the following Inference Providers:

--------------------