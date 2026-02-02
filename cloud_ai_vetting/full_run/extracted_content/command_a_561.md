# Command A
**URL:** https://huggingface.co/CohereForAI/c4ai-command-a-03-2025
**Page Title:** CohereLabs/c4ai-command-a-03-2025 · Hugging Face
--------------------


## You need to agree to share your contact information to access this model

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
By submitting this form, you agree to the License Agreement and acknowledge that the information you provide will be collected, used, and shared in accordance with Cohere’s Privacy Policy . You’ll receive email updates about Cohere Labs and Cohere research, events, products and services. You can unsubscribe at any time.
Log in or Sign Up to review the conditions and access this model content.

## Model Card for Cohere Labs Command A

## Model Summary

Cohere Labs Command A is an open weights research release of a 111 billion parameter model optimized for demanding enterprises that require fast, secure, and high-quality AI. Compared to other leading proprietary and open-weights models Command A delivers maximum performance with minimum hardware costs, excelling on business-critical agentic and multilingual tasks while‬ being deployable on just two GPUs.
Developed by: Cohere and Cohere Labs
- Point of Contact: Cohere Labs
- License: CC-BY-NC , requires also adhering to Cohere Lab's Acceptable Use Policy
[LINK: Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)
- Model: c4ai-command-a-03-2025
- Model Size: 111 billion parameters
- Context length: 256K
For more details on how this model was developed, check out our Tech Report .
Note: The model supports a context length of 256K but it is configured in Hugging Face for 128K. This value can be updated in the configuration if needed.
Try Cohere Labs Command A
You can try out Cohere Labs Command A before downloading the weights in our hosted Hugging Face Space .
Usage
Please install transformers from the source repository that includes the necessary changes for this model.

## Model Details

Input : Models input text only.
Output : Models generate text only.
Model Architecture : This is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety. The model features three layers with sliding window attention (window size 4096) and RoPE for efficient local context modeling and relative positional encoding. A fourth layer uses global attention without positional embeddings, enabling unrestricted token interactions across the entire sequence.
Languages covered : The model has been trained on 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, Chinese, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
Context Length : Command A supports a context length of 256K.

### Chat Capabilities:

By default, Command A is configured as a conversational model. A preamble conditions the model on interactive behaviour, meaning it is expected to reply in a conversational fashion, provides introductory statements and follow-up questions, and uses Markdown as well as LaTeX where appropriate. This is desired for interactive experiences, such as chatbots, where the model engages in dialogue.
In other use cases, a non-interactive model behavior might be more desired (e.g. task-focused use cases like extracting information, summarizing text, translation, and categorization). Learn how system messages can be used to achieve such non-interactive behavior here .
[LINK: here](https://docs.cohere.com/docs/command-a-hf#obtaining-non-interactive-behavior)
Besides, Command A can be configured with two safety modes, which enable users to set guardrails that are both safe and suitable to their needs: contextual mode, or strict mode. Contextual mode is appropriate for wide-ranging interactions with fewer constraints on output, while maintaining core protections by rejecting harmful or illegal suggestions. Command A is configured to contextual mode by default. Strict mode aims to avoid all sensitive topics, such as violent or sexual acts and profanity. For more information, see the Command A prompt format docs .
[LINK: Command A prompt format docs](https://docs.cohere.com/docs/command-a-hf)

### RAG Capabilities:

Command A has been trained specifically for tasks like the final step of Retrieval Augmented Generation (RAG).
RAG with Command A is supported through chat templates in Transformers. The model takes a conversation as input (with an optional user-supplied system preamble), along with a list of document snippets.
[LINK: chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating#advanced-retrieval-augmented-generation)
You can then generate text from this input as normal.
Document snippets should be short chunks, rather than long documents, typically around 100-400 words per chunk, formatted as key-value pairs. The keys should be short descriptive strings, the values can be text or semi-structured.
You may find that simply including relevant documents directly in a user message works just as well, or better than using the documents parameter to render the special RAG template. The RAG template is generally a strong default and is ideal for users wanting citations. We encourage users to play with both, and to evaluate which mode works best for their specific use case.
Note that this was a very brief introduction to RAG - for more information, see the Command A prompt format docs and the Transformers RAG documentation .
[LINK: RAG documentation](https://huggingface.co/docs/transformers/main/chat_templating#advanced-retrieval-augmented-generation)
Optionally, one can ask the model to include grounding spans (citations) in its response to indicate the source of the information. The code is the same as before, except for this line.
The output looks like this: the model will associate pieces of texts (called "spans") with specific document snippets that support them (called "sources"). Command A uses a pair of tags "<co>" and "</co>" to indicate when a span can be grounded onto a list of sources. For example, "<co>span</co: 0:[0,1]>" means that "span" is supported by documents snippets 0 and 1 that were provided in the last message.

### Tool Use Capabilities:

Command A has been specifically trained with conversational tool use capabilities. This allows the model to interact with external tools like APIs, databases, or search engines.
Tool use with Command A is supported through chat templates in Transformers. We recommend providing tool descriptions using JSON schema.
[LINK: chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating#advanced-tool-use--function-calling)
You can then generate from this input as normal.
If the model generates a plan and tool calls, you should add them to the chat history like so:
and then call the tool and append the result, as a dictionary, with the tool role, like so:
After that, you can generate() again to let the model use the tool result in the chat.
Note that this was a very brief introduction to tool calling - for more information, see the Command A prompt format docs and the Transformers tool use documentation .
[LINK: the Command A prompt format docs](https://docs.cohere.com/docs/command-a-hf&sa=D&source=docs&ust=1741857329583678&usg=AOvVaw3sS-2eIfLzShS6c9VWXJWa)
[LINK: tool use documentation](https://huggingface.co/docs/transformers/main/chat_templating#advanced-tool-use--function-calling)
Optionally, one can ask the model to include grounding spans (citations) in its response to indicate the source of the information, by using enable_citations=True in tokenizer.apply_chat_template( ). The generation would look like this:
When citations are turned on, the model associates pieces of texts (called "spans") with those specific tool results that support them (called "sources"). Command A uses a pair of tags "<co>" and "</co>" to indicate when a span can be grounded onto a list of sources, listing them out in the closing tag. For example, "<co>span</co: 0:[1,2],1:[0]>" means that "span" is supported by result 1 and 2 from "tool_call_id=0" as well as result 0 from "tool_call_id=1". Sources from the same tool call are grouped together and listed as "{tool_call_id}:[{list of result indices}]", before they are joined together by ",".

### Code Capabilities:

Command A has meaningfully improved on code capabilities.  In addition to academic code benchmarks, we have evaluated it on enterprise-relevant scenarios, including SQL generation and code translation, where it outperforms other models of similar size. Try these out by requesting code snippets, code explanations, or code rewrites. For better performance, we also recommend using a low temperature (and even greedy decoding) for code-generation related instructions.

## Model Card Contact

For errors or additional questions about details in this model card, contact labs@cohere.com

## Terms of Use:

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant 111 billion parameter model to researchers all over the world. This model is governed by a CC-BY-NC , requires also adhering to Cohere Lab's Acceptable Use Policy
[LINK: Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)

## Try Chat:

You can try Command A chat in the playground here . You can also use it in our dedicated Hugging Face Space here .

## Citation:

## Model tree for CohereLabs/c4ai-command-a-03-2025

## Spaces using CohereLabs/c4ai-command-a-03-2025 8

## Collection including CohereLabs/c4ai-command-a-03-2025

## Paper for CohereLabs/c4ai-command-a-03-2025

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
CohereLabs/c4ai-command-a-03-2025 is supported by the following Inference Providers:

--------------------