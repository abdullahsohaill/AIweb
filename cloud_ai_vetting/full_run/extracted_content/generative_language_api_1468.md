# Generative Language API
**URL:** https://ai.google.dev/api/rest
**Page Title:** Gemini API reference  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/api)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/api?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/api?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/api?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/api?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/api?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/api?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/api?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/api?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/api?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/api?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/api?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/api?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/api?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/api?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/api?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/api?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/api?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/api?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/api?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/api?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/api?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi&prompt=select_account)
- On this page
- Primary endpoints
- Authentication
- Content generation Request body structure Response body structure
- Request body structure
- Response body structure
- Request examples Text-only prompt Multimodal prompt (text and image) Multi-turn conversations (chat) Key takeaways
- Text-only prompt
- Multimodal prompt (text and image)
- Multi-turn conversations (chat)
- Key takeaways
- Response examples Text-only response
- Text-only response
- Live API (BidiGenerateContent) WebSockets API
[LINK: Live API (BidiGenerateContent) WebSockets API](#live-api)
- Specialized models
- Platform APIs
[LINK: Platform APIs](#platform-apis)
- What's next
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- API reference
[LINK: API reference](https://ai.google.dev/api)

## Gemini API reference

- On this page
- Primary endpoints
- Authentication
- Content generation Request body structure Response body structure
- Request body structure
- Response body structure
- Request examples Text-only prompt Multimodal prompt (text and image) Multi-turn conversations (chat) Key takeaways
- Text-only prompt
- Multimodal prompt (text and image)
- Multi-turn conversations (chat)
- Key takeaways
- Response examples Text-only response
- Text-only response
- Live API (BidiGenerateContent) WebSockets API
[LINK: Live API (BidiGenerateContent) WebSockets API](#live-api)
- Specialized models
- Platform APIs
[LINK: Platform APIs](#platform-apis)
- What's next
This API reference describes the standard, streaming, and real-time APIs you can
use to interact with the Gemini models. You can use the REST APIs in any
environment that supports HTTP requests. Refer to the Quickstart guide for how to
get started with your first API call. If you're looking for the references for
our language-specific libraries and SDKs, go to the link for that language in
the left navigation under SDK references .
[LINK: Quickstart guide](https://ai.google.dev/gemini-api/docs/quickstart)

## Primary endpoints

The Gemini API is organized around the following major endpoints:
- Standard content generation ( generateContent ): A standard REST endpoint that processes your request and returns the model's
full response in a single package. This is best for non-interactive tasks
where you can wait for the entire result.
[LINK: generateContent](/api/generate-content#method:-models.generatecontent)
- Streaming content generation ( streamGenerateContent ): Uses Server-Sent Events (SSE) to push chunks of the response to you as they
are generated. This provides a faster, more interactive experience for
applications like chatbots.
[LINK: streamGenerateContent](/api/generate-content#method:-models.streamGenerateContent)
- Live API ( BidiGenerateContent ): A stateful WebSocket-based
API for bi-directional streaming, designed for real-time conversational use
cases.
[LINK: BidiGenerateContent](/api/live#send-messages)
- Batch mode ( batchGenerateContent ): A standard REST
endpoint for submitting batches of generateContent requests.
[LINK: batchGenerateContent](/api/batch-mode)
- Embeddings ( embedContent ): A standard REST endpoint
that generates a text embedding vector from the input Content .
[LINK: embedContent](/api/embeddings)
- Gen Media APIs: Endpoints for generating media with our specialized
models such as Imagen for image generation ,
and Veo for video generation .
Gemini also has these capabilities built in which you can access using the generateContent API.
[LINK: Imagen for image generation](/api/models#method:-models.predict)
[LINK: Veo for video generation](/api/models#method:-models.predictlongrunning)
- Platform APIs: Utility endpoints that support core capabilities such as uploading files , and counting tokens .
[LINK: uploading files](/api/files)
[LINK: counting tokens](/api/tokens)

## Authentication

All requests to the Gemini API must include a x-goog-api-key header with your
API key. Create one with a few clicks in Google AI
Studio .
[LINK: Google AI
Studio](https://aistudio.google.com/app/apikey)
The following is an example request with the API key included in the header:
For instructions on how to pass your key to the API using Gemini SDKs,
see the Using Gemini API keys guide.
[LINK: Using Gemini API keys](/gemini-api/docs/api-key)

## Content generation

This is the central endpoint for sending prompts to the model. There are two
endpoints for generating content, the key difference is how you receive the
response:
- generateContent (REST) :
Receives a request and provides a
single response after the model has finished its entire generation.
[LINK: generateContent](/api/generate-content#method:-models.generatecontent)
- streamGenerateContent (SSE) : Receives the exact same
request, but the model streams back chunks of the response as they are
generated. This provides a better user experience for interactive
applications as it lets you display partial results immediately.
[LINK: streamGenerateContent](/api/generate-content#method:-models.streamgeneratecontent)

### Request body structure

The request body is a JSON object that is identical for both standard and streaming modes and is built from a few core
objects:
[LINK: request body](/api/generate-content#request-body)
- Content object: Represents a single turn in a
conversation.
[LINK: Content](/api/caching#Content)
- Part object: A piece of data within a Content turn
(like text or an image).
[LINK: Part](/api/caching#Part)
- inline_data ( Blob ): A container for raw media bytes
and their MIME type.
[LINK: Blob](/api/caching#Blob)
At the highest level, the request body contains a contents object, which is a
list of Content objects, each representing turns in conversation. In most
cases, for basic text generation, you will have a single Content object, but
if you'd like to maintain conversation history, you can use multiple Content objects.
The following shows a typical generateContent request body:

### Response body structure

The response body is similar for both
the streaming and standard modes except for the following:
[LINK: response body](/api/generate-content#response-body)
- Standard mode: The response body contains an instance of GenerateContentResponse .
[LINK: GenerateContentResponse](/api/generate-content#v1beta.GenerateContentResponse)
- Streaming mode: The response body contains a stream of GenerateContentResponse instances.
[LINK: GenerateContentResponse](/api/generate-content#v1beta.GenerateContentResponse)
At a high level, the response body contains a candidates object, which is a
list of Candidate objects. The Candidate object contains a Content object that has the generated response returned from the model.

## Request examples

The following examples show how these components come together for different
types of requests.

### Text-only prompt

A simple text prompt consists of a contents array with a single Content object. That object's parts array, in turn, contains a single Part object
with a text field.

### Multimodal prompt (text and image)

To provide both text and an image in a prompt, the parts array should contain
two Part objects: one for the text, and one for the image inline_data .

### Multi-turn conversations (chat)

To build a conversation with multiple turns, you define the contents array
with multiple Content objects. The API will use this entire history as context
for the next response. The role for each Content object should alternate
between user and model .

### Key takeaways

- Content is the envelope: It's the top-level container for a message turn,
whether it's from the user or the model.
- Part enables multimodality: Use multiple Part objects within a single Content object to combine different types of data (text, image, video URI, etc.).
- Choose your data method: For small, directly embedded media (like most images), use a Part with inline_data . For larger files or files you want to reuse across requests, use the
File API to upload the file and reference it with a file_data part.
- For small, directly embedded media (like most images), use a Part with inline_data .
- For larger files or files you want to reuse across requests, use the
File API to upload the file and reference it with a file_data part.
- Manage conversation history: For chat applications using the REST API, build
the contents array by appending Content objects for each turn,
alternating between "user" and "model" roles. If you're using an SDK,
refer to the SDK documentation for the recommended way to manage
conversation history.

## Response examples

The following examples show how these components come together for different
types of requests.

### Text-only response

A default text response consists of a candidates array with one or more content objects that contain the model's response.
The following is an example of a standard response:
The following is series of streaming responses. Each response contains a responseId that ties the full response together:

## Live API (BidiGenerateContent) WebSockets API

Live API offers a stateful WebSocket based API for bi-directional streaming to
enable real-time streaming use cases. You can review Live API guide and the Live API reference for more details.
[LINK: Live API guide](/gemini-api/docs/live)
[LINK: Live API reference](/api/live)

## Specialized models

In addition to the Gemini family of models, Gemini API offers endpoints for
specialized models such as Imagen , Lyria and embedding models. You can check out
these guides under the Models section.
[LINK: Imagen](/gemini-api/docs/imagen)
[LINK: Lyria](/gemini-api/docs/music-generation)
[LINK: embedding](/gemini-api/docs/embeddings)

## Platform APIs

The rest of the endpoints enable additional capabilities to use with the main
endpoints described so far. Check out topics Batch mode and File API in the Guides section to learn more.
[LINK: Batch mode](/gemini-api/docs/batch-mode)
[LINK: File API](/gemini-api/docs/files)

## What's next

If you're just getting started, check out the following guides, which will help
you understand the Gemini API programming model:
- Gemini API quickstart
[LINK: Gemini API quickstart](/gemini-api/docs/quickstart)
- Gemini model guide
[LINK: Gemini model guide](/gemini-api/docs/models/gemini)
You might also want to check out the capabilities guides, which introduce different
Gemini API features and provide code examples:
- Text generation
[LINK: Text generation](/gemini-api/docs/text-generation)
- Context caching
[LINK: Context caching](/gemini-api/docs/caching)
- Embeddings
[LINK: Embeddings](/gemini-api/docs/embeddings)
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2026-01-19 UTC.

--------------------