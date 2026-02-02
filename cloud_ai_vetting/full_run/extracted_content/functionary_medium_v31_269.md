# Functionary-medium-v3.1
**URL:** https://huggingface.co/meetkai/functionary-medium-v3.1
**Page Title:** meetkai/functionary-medium-v3.1 · Hugging Face
--------------------


## Model Card for functionary-medium-v3.1

This model was based on meta-llama/Meta-Llama-3.1-70B-Instruct , using Meta's original prompt template as described in: User-defined Custom tool calling
[LINK: User-defined Custom tool calling](https://llama.meta.com/docs/model-cards-and-prompt-formats/llama3_1/#user-defined-custom-tool-calling)
https://github.com/MeetKai/functionary
[LINK: https://github.com/MeetKai/functionary](https://github.com/MeetKai/functionary)
Functionary is a language model that can interpret and execute functions/plugins.
The model determines when to execute functions, whether in parallel or serially, and can understand their outputs. It only triggers functions as needed. Function definitions are given as JSON Schema Objects, similar to OpenAI GPT function calls.

## Key Features

- Intelligent parallel tool use
- Able to analyze functions/tools outputs and provide relevant responses grounded in the outputs
- Able to decide when to not use tools/call functions and provide normal chat response
- Truly one of the best open-source alternative to GPT-4
- Support code interpreter

## How to Get Started

We provide custom code for parsing raw model responses into a JSON object containing role, content and tool_calls fields. This enables the users to read the function-calling output of the model easily.

## Prompt Template

We convert function definitions to a similar text to TypeScript definitions. Then we inject these definitions as system prompts. After that, we inject the default system prompt. Then we start the conversation messages.
This formatting is also available via our vLLM server which we process the functions into Typescript definitions encapsulated in a system message using a pre-defined Transformers Jinja chat template. This means that the lists of messages can be formatted for you with the apply_chat_template() method within our server:
will yield:
A more detailed example is provided here .
[LINK: here](https://github.com/MeetKai/functionary/blob/main/tests/prompt_test_v3-llama3.1.txt)

## Run the model

We encourage users to run our models using our OpenAI-compatible vLLM server here .
[LINK: here](https://github.com/MeetKai/functionary)

## The MeetKai Team

[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for meetkai/functionary-medium-v3.1

## Collection including meetkai/functionary-medium-v3.1


--------------------