# Command R-35B
**URL:** https://huggingface.co/CohereForAI/c4ai-command-r-v01
**Page Title:** CohereLabs/c4ai-command-r-v01 · Hugging Face
--------------------


## You need to agree to share your contact information to access this model

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
By submitting this form, you agree to the License Agreement and acknowledge that the information you provide will be collected, used, and shared in accordance with Cohere’s Privacy Policy . You’ll receive email updates about Cohere Labs and Cohere research, events, products and services. You can unsubscribe at any time.
Log in or Sign Up to review the conditions and access this model content.

## Model Card for Cohere Labs Command-R

🚨 This model is non-quantized version of Cohere Labs Command-R. You can find the quantized version of Cohere Labs Command-R using bitsandbytes here .

## Model Summary

Cohere Labs Command-R is a research release of a 35 billion parameter highly performant generative model. Command-R is a large language model with open weights optimized for a variety of use cases including reasoning, summarization, and question answering. Command-R has the capability for multilingual generation evaluated in 10 languages and highly performant RAG capabilities.
Developed by: Cohere and Cohere Labs
- Point of Contact: Cohere Labs
- License: CC-BY-NC , requires also adhering to Cohere Lab's Acceptable Use Policy
[LINK: Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)
- Model: c4ai-command-r-v01
- Model Size: 35 billion parameters
- Context length: 128K
Try Cohere Labs Command R
If you want to try Command R before downloading the weights, the model is hosted in a hugging face space here .
Usage
Please use transformers version 4.39.1 or higher
Quantized model through bitsandbytes, 8-bit precision
Quantized model through bitsandbytes, 4-bit precision
You can find a quantized version of this model to 4-bit precision here .

## Model Details

Input : Models input text only.
Output : Models generate text only.
Model Architecture : This is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.
Languages covered : The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic.
Pre-training data additionally included the following 13 languages: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian.
Context length : Command-R supports a context length of 128K.

### Grounded Generation and RAG Capabilities:

Command-R has been specifically trained with grounded generation capabilities. This means that it can generate responses based on a list of supplied document snippets, and it will include grounding spans (citations) in its response indicating the source of the information.
This can be used to enable behaviors such as grounded summarization and the final step of Retrieval Augmented Generation (RAG).This behavior has been trained into the model via a mixture of supervised fine-tuning and preference fine-tuning, using a specific prompt template.
Deviating from this prompt template may reduce performance, but we encourage experimentation.
Command-R’s grounded generation behavior takes a conversation as input (with an optional user-supplied system preamble, indicating task, context and desired output style), along with a list of retrieved document snippets.
The document snippets should be chunks, rather than long documents, typically around  100-400 words per chunk. Document snippets consist of key-value pairs. The keys should be short descriptive strings, the values can be text or semi-structured.
By default, Command-R will generate grounded responses by first predicting which documents are relevant, then predicting which ones it will cite, then generating an answer. 
Finally, it will then insert grounding spans into the answer. See below for an example. This is referred to as accurate grounded generation.
The model is trained with a number of other answering modes, which can be selected by prompt changes . A fast citation mode is supported in the tokenizer, which will directly generate an answer with grounding spans in it, without first writing the answer out in full. This sacrifices some grounding accuracy in favor of generating fewer tokens.
Comprehensive documentation for working with command-R's grounded generation prompt template can be found here .
[LINK: here](https://docs.cohere.com/docs/prompting-command-r)
The code snippet below shows a minimal working example on how to render a prompt.

### Single-Step Tool Use Capabilities ("Function Calling"):

Single-step tool use (or “Function Calling”) allows Command R to interact with external tools like APIs, databases, or search engines. Single-step tool use is made of two model inferences:
- Tool Selection: The model decides which tools to call and with what parameters. It’s then up to the developer to execute these tool calls and obtain tool results.
- Response Generation: The model generates the final response given the tool results.
You can learn more about single step tool use in our documentation .
[LINK: documentation](https://docs.cohere.com/docs/tool-use)
Command R has been specifically trained with single-step tool use (or “Function Calling”) capabilities. These have been trained into the model via a mixture of supervised fine-tuning and preference fine-tuning, using a specific prompt template. Deviating from this prompt template may reduce performance. This is why we recommend using the prompt template described below.
Command R’s single-step tool use functionality takes a conversation as input (with an optional user-system preamble), along with a list of available tools. The model will then generate a json-formatted list of actions to execute on a subset of those tools. Command R may use one of its supplied tools more than once.
The model has been trained to recognise a special directly_answer tool, which it uses to indicate that it doesn’t want to use any of its other tools. The ability to abstain from calling a specific tool can be useful in a range of situations, such as greeting a user, or asking clarifying questions. We recommend including the directly_answer tool, but it can be removed or renamed if required.
Comprehensive documentation for working with Command R's single-step tool use prompt template can be found here and here .
[LINK: here](https://docs.cohere.com/docs/prompting-command-r#single-step-tool-use-with-command-rr-function-calling)
[LINK: here](https://docs.cohere.com/docs/prompting-command-r#single-step-tool-use-with-command-rr-function-calling-1)
You can render the single-step tool use prompt template by using the function apply_tool_use_template() . The code snippet below shows a minimal working example on how to render this prompt.
Command R also supports Hugging Face's tool use API to render the same prompt.
[LINK: tool use API](https://huggingface.co/docs/transformers/main/en/chat_templating#advanced-tool-use--function-calling)

### Multi-Step Tool Use Capabilities ("Agents"):

Multi-step tool use is suited for building agents that can plan and execute a sequence of actions using multiple tools. Unlike single-step tool use, the model can perform several inference cycles, iterating through Action → Observation → Reflection until it decides on a final response. For more details, refer to our documentation on multi-step tool use .
[LINK: documentation on multi-step tool use](https://docs.cohere.com/docs/multi-step-tool-use)
Command R has been specifically trained with multi-step tool use (or “Agents”) capabilities. These have been trained into the model via a mixture of supervised fine-tuning and preference fine-tuning, using a specific prompt template. Deviating from this prompt template may reduce performance. This is why we recommend using the prompt template described below.
The prompt template is not yet available in the HuggingFace tokenizer. However, comprehensive documentation for working with Command R's multi-step tool use prompt template can be found here and here .
[LINK: here](https://docs.cohere.com/docs/prompting-command-r#multi-step-tool-use-with-command-rr-agents)
[LINK: here](https://docs.cohere.com/docs/prompting-command-r#multihop-tool-use-with-command-rr-agents)

### Code Capabilities:

Command-R has been optimized to interact with your code, by requesting code snippets, code explanations, or code rewrites. It might not perform well out-of-the-box for pure code completion. For better performance, we also recommend using a low temperature (and even greedy decoding) for code-generation related instructions.

### Model Card Contact

For errors or additional questions about details in this model card, contact labs@cohere.com

### Terms of Use:

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant 35 billion parameter model to researchers all over the world. This model is governed by a CC-BY-NC License with an acceptable use addendum, and also requires adhering to Cohere Lab's Acceptable Use Policy .
[LINK: Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)

### Try Chat:

You can try Command-R chat in the playground here .

## Model tree for CohereLabs/c4ai-command-r-v01

## Spaces using CohereLabs/c4ai-command-r-v01 57


--------------------