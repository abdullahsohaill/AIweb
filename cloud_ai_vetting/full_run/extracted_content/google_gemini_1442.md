# google gemini
**URL:** https://ai.google.dev/gemini-api/docs/text-generation
**Page Title:** Text generation  |  Gemini API  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemini-api/docs/text-generation)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemini-api/docs/text-generation?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemini-api/docs/text-generation?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemini-api/docs/text-generation?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemini-api/docs/text-generation?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemini-api/docs/text-generation?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemini-api/docs/text-generation?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemini-api/docs/text-generation?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemini-api/docs/text-generation?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Ftext-generation&prompt=select_account)
- On this page
- Thinking with Gemini
- System instructions and other configurations
- Multimodal inputs
- Streaming responses
- Multi-turn conversations (chat)
- Prompting tips
- What's next
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- Docs
[LINK: Docs](https://ai.google.dev/gemini-api/docs)

## Text generation

- On this page
- Thinking with Gemini
- System instructions and other configurations
- Multimodal inputs
- Streaming responses
- Multi-turn conversations (chat)
- Prompting tips
- What's next
The Gemini API can generate text output from text, images, video, and audio
inputs.
Here's a basic example:

## Thinking with Gemini

Gemini models often have "thinking" enabled by default
which allows the model to reason before responding to a request.
[LINK: "thinking"](/gemini-api/docs/thinking)
Each model supports different thinking configurations which gives you control
over cost, latency, and intelligence. For more details, see the thinking guide .
[LINK: thinking guide](/gemini-api/docs/thinking#set-budget)

## System instructions and other configurations

You can guide the behavior of Gemini models with system instructions. To do so,
pass a GenerateContentConfig object.
[LINK: GenerateContentConfig](/api/generate-content#v1beta.GenerationConfig)
The GenerateContentConfig object also lets you override default generation parameters, such as temperature .
[LINK: GenerateContentConfig](/api/generate-content#v1beta.GenerationConfig)
[LINK: temperature](/api/generate-content#v1beta.GenerationConfig)
Refer to the GenerateContentConfig in our API reference for a complete list of configurable parameters and their
descriptions.
[LINK: GenerateContentConfig](/api/generate-content#v1beta.GenerationConfig)

## Multimodal inputs

The Gemini API supports multimodal inputs, allowing you to combine text with
media files. The following example demonstrates providing an image:
For alternative methods of providing images and more advanced image processing,
see our image understanding guide .
The API also supports document , video , and audio inputs and understanding.
[LINK: image understanding guide](/gemini-api/docs/image-understanding)
[LINK: document](/gemini-api/docs/document-processing)
[LINK: video](/gemini-api/docs/video-understanding)
[LINK: audio](/gemini-api/docs/audio)

## Streaming responses

By default, the model returns a response only after the entire generation 
process is complete.
For more fluid interactions, use streaming to receive GenerateContentResponse instances incrementally
as they're generated.
[LINK: GenerateContentResponse](/api/generate-content#v1beta.GenerateContentResponse)

## Multi-turn conversations (chat)

Our SDKs provide functionality to collect multiple rounds of prompts and
responses into a chat, giving you an easy way to keep track of the conversation
history.
Streaming can also be used for multi-turn conversations.

## Prompting tips

Consult our prompt engineering guide for
suggestions on getting the most out of Gemini.
[LINK: prompt engineering guide](/gemini/docs/prompting-strategies)

## What's next

- Try Gemini in Google AI Studio .
- Experiment with structured outputs for
JSON-like responses.
[LINK: structured outputs](/gemini-api/docs/structured-output)
- Explore Gemini's image , video , audio and document understanding capabilities.
[LINK: image](/gemini-api/docs/image-understanding)
[LINK: video](/gemini-api/docs/video-understanding)
[LINK: audio](/gemini-api/docs/audio)
[LINK: document](/gemini-api/docs/document-processing)
- Learn about multimodal file prompting strategies .
[LINK: file prompting strategies](/gemini-api/docs/files#prompt-guide)
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2026-01-16 UTC.

--------------------