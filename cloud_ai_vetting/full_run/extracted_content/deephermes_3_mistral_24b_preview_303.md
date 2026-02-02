# DeepHermes-3-Mistral-24B-Preview
**URL:** https://huggingface.co/NousResearch/DeepHermes-3-Mistral-24B-Preview
**Page Title:** NousResearch/DeepHermes-3-Mistral-24B-Preview · Hugging Face
--------------------


## DeepHermes 3 - Mistral 24B Preview

## Model Description

DeepHermes 3 Preview is the latest version of our flagship Hermes series of LLMs by Nous Research, and one of the first models in the world to unify Reasoning (long chains of thought that improve answer accuracy) and normal LLM response modes into one model. We have also improved LLM annotation, judgement, and function calling.
DeepHermes 3 Preview is a hybrid reasoning model, and one of the first LLM models to unify both "intuitive", traditional mode responses and long chain of thought reasoning responses into a single model, toggled by a system prompt.
Hermes 3, the predecessor of DeepHermes 3, is a generalist language model with many improvements over Hermes 2, including advanced agentic capabilities, much better roleplaying, reasoning, multi-turn conversation, long context coherence, and improvements across the board.
The ethos of the Hermes series of models is focused on aligning LLMs to the user, with powerful steering capabilities and control given to the end user.
This is a preview Hermes with early reasoning capabilities, distilled from R1 across a variety of tasks that benefit from reasoning and objectivity. Some quirks may be discovered! Please let us know any interesting findings or issues you discover!

## Note: To toggle REASONING ON, you must use the following system prompt:

## Nous API

This model is also available on our new API product - Check out the API and sign up for the waitlist here: https://portal.nousresearch.com/

## Benchmarks:

Comparisons between Reasoning mode ON and OFF:
Benchmarks of Non-Reasoning mode on Traditional Benchmarks against Mistral-Small-24B-Instruct:

## Example Outputs:

## Prompt Format

DeepHermes 3 now uses Llama-Chat format as the prompt format, opening up a more unified, structured system for engaging the LLM in multi-turn chat dialogue.
System prompts allow steerability and interesting new ways to interact with an LLM, guiding rules, roles, and stylistic choices of the model.

## Deep Thinking Mode - Deep Hermes Preview can activate long chain of thought with a system prompt.

For an example of using deep reasoning mode with HuggingFace Transformers:
Please note, for difficult problems DeepHermes can think using as many as 13,000 tokens. You may need to increase max_new_tokens to be much larger than 2500 for difficult problems.

## Standard "Intuitive" Response Mode

Prompt with system instruction (Use whatever system prompt you like, this is just an example!):

## VLLM Inference

You can also run this model with vLLM, by running the following in your terminal after pip install vllm
vllm serve NousResearch/DeepHermes-3-Mistral-24B-Preview
You may then use the model over API using the OpenAI library just like you would call OpenAI's API.

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
Given the {schema} that you provide, it should follow the format of that json to create its response, all you have to do is give a typical user prompt, and it will respond in JSON.

## Inference Code for Function Calling:

All code for utilizing, parsing, and building function calling templates is available on our github: https://github.com/NousResearch/Hermes-Function-Calling
[LINK: https://github.com/NousResearch/Hermes-Function-Calling](https://github.com/NousResearch/Hermes-Function-Calling)

## Quantized Versions:

GGUF Quants: https://huggingface.co/NousResearch/DeepHermes-3-Mistral-24B-Preview-GGUF

## How to cite:

## Model tree for NousResearch/DeepHermes-3-Mistral-24B-Preview

Base model

## Spaces using NousResearch/DeepHermes-3-Mistral-24B-Preview 100

## Collection including NousResearch/DeepHermes-3-Mistral-24B-Preview


--------------------