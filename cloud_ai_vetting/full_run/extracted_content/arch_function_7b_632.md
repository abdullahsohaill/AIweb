# Arch-Function-7B
**URL:** https://huggingface.co/katanemo/Arch-Function-7B
**Page Title:** katanemo/Arch-Function-7B · Hugging Face
--------------------


## katanemo/Arch-Function-7B

## Overview

The Katanemo Arch-Function collection of large language models (LLMs) is a collection state-of-the-art (SOTA) LLMs specifically designed for function calling tasks. The models are designed to understand complex function signatures, identify required parameters, and produce accurate function call outputs based on natural language prompts. Achieving performance on par with GPT-4, these models set a new benchmark in the domain of function-oriented tasks, making them suitable for scenarios where automated API interaction and function execution is crucial.
In summary, the Katanemo Arch-Function collection demonstrates:
- State-of-the-art performance in function calling
- Accurate parameter identification and suggestion , even in ambiguous or incomplete inputs
- High generalization across multiple function calling use cases, from API interactions to automated backend tasks.
- Optimized low-latency, high-throughput performance, making it suitable for real-time, production environments.
Arch-Function is the core LLM used in then open source Arch Gateway to seamlessly integrate user prompts with developers APIs
[LINK: Arch Gateway](https://github.com/katanemo/arch)

## Key Features

## Training Details

Katanemo Arch-Function collection is built on top of the Qwen 2.5 . A blog with technical details leading to our models will be published soon.

## Performance Benchmarks

We evaluate Katanemo Arch-Function series on the Berkeley Function-Calling Leaderboard (BFCL) . We compare with commonly-used models and the results (as of Oct 21st, 2024) are shwon below. For each model family, we select the one with the highest rank.

## Requirements

The code of Arch-Function-7B has been in the Hugging Face transformers library and we advise you to install latest version:

## How to use

We use the following example to illustrate how to use our model to perform function calling tasks. Please note that, our model works best with our provided prompt format. It allows us to extract JSON output that is similar to the function-calling mode of ChatGPT .
[LINK: function-calling mode of ChatGPT](https://platform.openai.com/docs/guides/function-calling)

### Single Turn Example

Then you should be able to see the following output string in JSON format:

### Multi Turn Example

Upon getting results from functions, you can add it to the messages list as a user message and pass it to the model to get responses for users.
Then you should be able to see the following output:

## License

Katanemo Arch-Function collection is distributed under the Katanemo license .

## Model tree for katanemo/Arch-Function-7B

Base model

## Collection including katanemo/Arch-Function-7B


--------------------