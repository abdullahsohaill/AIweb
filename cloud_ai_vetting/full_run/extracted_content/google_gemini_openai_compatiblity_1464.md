# Google Gemini OpenAI Compatiblity
**URL:** https://ai.google.dev/gemini-api/docs/openai
**Page Title:** OpenAI compatibility  |  Gemini API  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemini-api/docs/openai)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemini-api/docs/openai?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemini-api/docs/openai?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemini-api/docs/openai?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemini-api/docs/openai?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemini-api/docs/openai?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemini-api/docs/openai?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemini-api/docs/openai?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemini-api/docs/openai?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemini-api/docs/openai?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemini-api/docs/openai?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemini-api/docs/openai?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemini-api/docs/openai?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemini-api/docs/openai?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemini-api/docs/openai?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemini-api/docs/openai?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemini-api/docs/openai?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemini-api/docs/openai?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemini-api/docs/openai?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fopenai&prompt=select_account)
- On this page
- Thinking
- Streaming
- Function calling
- Image understanding
- Generate an image
- Audio understanding
- Structured output
- Embeddings
- Batch API
- extra_body cached_content
- cached_content
- List models
- Retrieve a model
- Current limitations
- What's next
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- Docs
[LINK: Docs](https://ai.google.dev/gemini-api/docs)

## Open AI compatibility

- On this page
- Thinking
- Streaming
- Function calling
- Image understanding
- Generate an image
- Audio understanding
- Structured output
- Embeddings
- Batch API
- extra_body cached_content
- cached_content
- List models
- Retrieve a model
- Current limitations
- What's next
Gemini models are accessible using the OpenAI libraries (Python and TypeScript /
Javascript) along with the REST API, by updating three lines of code
and using your Gemini API key . If you
aren't already using the OpenAI libraries, we recommend that you call the Gemini API directly .
[LINK: Gemini API key](https://aistudio.google.com/apikey)
[LINK: Gemini API directly](https://ai.google.dev/gemini-api/docs/quickstart)
What changed? Just three lines!
- api_key="GEMINI_API_KEY" : Replace " GEMINI_API_KEY " with your actual Gemini
API key, which you can get in Google AI Studio .
api_key="GEMINI_API_KEY" : Replace " GEMINI_API_KEY " with your actual Gemini
API key, which you can get in Google AI Studio .
- base_url="https://generativelanguage.googleapis.com/v1beta/openai/" : This
tells the OpenAI library to send requests to the Gemini API endpoint instead of
the default URL.
base_url="https://generativelanguage.googleapis.com/v1beta/openai/" : This
tells the OpenAI library to send requests to the Gemini API endpoint instead of
the default URL.
- model="gemini-3-flash-preview" : Choose a compatible Gemini model
model="gemini-3-flash-preview" : Choose a compatible Gemini model

## Thinking

Gemini models are trained to think through complex problems, leading
to significantly improved reasoning. The Gemini API comes with thinking
parameters which give fine grain
control over how much the model will think.
[LINK: thinking
parameters](/gemini-api/docs/thinking)
Different Gemini models have different reasoning configurations, you can see how
they map to OpenAI's reasoning efforts as follows:
If no reasoning_effort is specified, Gemini uses the model's
default level or budget .
[LINK: level](/gemini-api/docs/thinking#levels)
[LINK: budget](/gemini-api/docs/thinking#set-budget)
If you want to disable thinking, you can set reasoning_effort to "none" for
2.5 models. Reasoning cannot be turned off for Gemini 2.5 Pro or 3 models.
Gemini thinking models also produce thought summaries .
You can use the extra_body field to include Gemini fields
in your request.
[LINK: thought summaries](/gemini-api/docs/thinking#summaries)
Note that reasoning_effort and thinking_level / thinking_budget overlap
functionality, so they can't be used at the same time.
Gemini 3 supports OpenAI compatibility for thought signatures in chat completion
APIs. You can find the full example on the thought signatures page.
[LINK: thought signatures](/gemini-api/docs/thought-signatures#openai)

## Streaming

The Gemini API supports streaming responses .
[LINK: streaming responses](/gemini-api/docs/text-generation?lang=python#generate-a-text-stream)

## Function calling

Function calling makes it easier for you to get structured data outputs from
generative models and is supported in the Gemini API .
[LINK: supported in the Gemini API](/gemini-api/docs/function-calling/tutorial)

## Image understanding

Gemini models are natively multimodal and provide best in class performance on many common vision tasks .
[LINK: many common vision tasks](/gemini-api/docs/vision)

## Generate an image

Generate an image:

## Audio understanding

Analyze audio input:

## Structured output

Gemini models can output JSON objects in any structure you define .
[LINK: structure you define](/gemini-api/docs/structured-output)

## Embeddings

Text embeddings measure the relatedness of text strings and can be generated
using the Gemini API .
[LINK: Gemini API](/gemini-api/docs/embeddings)

## Batch API

You can create batch jobs , submit them, and check
their status using the OpenAI library.
[LINK: batch jobs](/gemini-api/docs/batch-mode)
You'll need to prepare the JSONL file in OpenAI input format. For example:
OpenAI compatibility for Batch supports creating a batch,
monitoring job status, and viewing batch results.
Compatibility for upload and download is currently not supported. Instead, the
following example uses the genai client for uploading and downloading files , the same as when using the Gemini Batch API .
[LINK: files](/gemini-api/docs/files)
[LINK: Batch API](/gemini-api/docs/batch-mode#input-file)
The OpenAI SDK also supports generating embeddings with the Batch API . To do so, switch out the create method's endpoint field for an embeddings endpoint, as well as the url and model keys in the JSONL file:
[LINK: generating embeddings with the Batch API](/gemini-api/docs/batch-api#batch-embeddings)
See the Batch embedding generation section of the OpenAI compatibility cookbook for a complete example.
[LINK: Batch embedding generation](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)

## extra_body

There are several features supported by Gemini that are not available in OpenAI
models but can be enabled using the extra_body field.
extra_body features

### cached_content

Here's an example of using extra_body to set cached_content :

## List models

Get a list of available Gemini models:

## Retrieve a model

Retrieve a Gemini model:

## Current limitations

Support for the OpenAI libraries is still in beta while we extend feature support.
If you have questions about supported parameters, upcoming features, or run into
any issues getting started with Gemini, join our Developer Forum .
[LINK: Developer Forum](https://discuss.ai.google.dev/c/gemini-api/4)

## What's next

Try our OpenAI Compatibility Colab to work through more detailed
examples.
[LINK: OpenAI Compatibility Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2026-01-22 UTC.

--------------------