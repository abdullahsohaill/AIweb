# Create an API key for Gemini
**URL:** https://ai.google.dev/gemini-api/docs/quickstart
**Page Title:** Gemini API quickstart  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemini-api/docs/quickstart)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemini-api/docs/quickstart?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemini-api/docs/quickstart?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemini-api/docs/quickstart?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemini-api/docs/quickstart?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemini-api/docs/quickstart?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemini-api/docs/quickstart?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemini-api/docs/quickstart?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemini-api/docs/quickstart?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemini-api/docs/quickstart?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemini-api/docs/quickstart?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemini-api/docs/quickstart?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemini-api/docs/quickstart?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemini-api/docs/quickstart?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemini-api/docs/quickstart?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fquickstart&prompt=select_account)
- On this page
- Before you begin
- Install the Google GenAI SDK
- Make your first request
- What's next
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- Docs
[LINK: Docs](https://ai.google.dev/gemini-api/docs)

## Gemini API quickstart

- On this page
- Before you begin
- Install the Google GenAI SDK
- Make your first request
- What's next
This quickstart shows you how to install our libraries and make your first Gemini API request.
[LINK: libraries](/gemini-api/docs/libraries)

## Before you begin

Using the Gemini API requires an API key, you can create one for free to get started.
Create a Gemini API Key
[LINK: Create a Gemini API Key](https://aistudio.google.com/app/apikey)

## Install the Google Gen AI SDK

Using Python 3.9+ , install the google-genai package using the following pip command :
Using Node.js v18+ ,
install the Google Gen AI SDK for TypeScript and JavaScript using the following npm command :
[LINK: npm command](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
Install google.golang.org/genai in
your module directory using the go get command :
If you're using Maven, you can install google-genai by adding the
following to your dependencies:
[LINK: google-genai](https://github.com/googleapis/java-genai)
Install googleapis/go-genai in
your module directory using the dotnet add command
[LINK: googleapis/go-genai](https://googleapis.github.io/dotnet-genai/)
- To create a new Apps Script project, go to script.new .
- Click Untitled project .
- Rename the Apps Script project AI Studio and click Rename .
- Set your API key At the left, click Project Settings . Under Script Properties click Add script property . For Property , enter the key name: GEMINI_API_KEY . For Value , enter the value for the API key. Click Save script properties .
[LINK: API key](https://developers.google.com/apps-script/guides/properties#manage_script_properties_manually)
- At the left, click Project Settings .
- Under Script Properties click Add script property .
- For Property , enter the key name: GEMINI_API_KEY .
- For Value , enter the value for the API key.
- Click Save script properties .
- Replace the Code.gs file contents with the following code:

## Make your first request

Here is an example that uses the generateContent method
to send a request to the Gemini API using the Gemini 2.5 Flash model.
[LINK: generateContent](/api/generate-content#method:-models.generatecontent)
If you set your API key as the
environment variable GEMINI_API_KEY , it will be picked up automatically by the
client when using the Gemini API libraries .
Otherwise you will need to pass your API key as
an argument when initializing the client.
[LINK: set your API key](/gemini-api/docs/api-key#set-api-env-var)
[LINK: Gemini API libraries](/gemini-api/docs/libraries)
[LINK: pass your API key](/gemini-api/docs/api-key#provide-api-key-explicitly)
Note that all code samples in the Gemini API docs assume that you have set the
environment variable GEMINI_API_KEY .

## What's next

Now that you made your first API request, you might want to explore the
following guides that show Gemini in action:
- Text generation
[LINK: Text generation](/gemini-api/docs/text-generation)
- Image generation
[LINK: Image generation](/gemini-api/docs/image-generation)
- Image understanding
[LINK: Image understanding](/gemini-api/docs/image-understanding)
- Thinking
[LINK: Thinking](/gemini-api/docs/thinking)
- Function calling
[LINK: Function calling](/gemini-api/docs/function-calling)
- Long context
[LINK: Long context](/gemini-api/docs/long-context)
- Embeddings
[LINK: Embeddings](/gemini-api/docs/embeddings)
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2026-01-19 UTC.

--------------------