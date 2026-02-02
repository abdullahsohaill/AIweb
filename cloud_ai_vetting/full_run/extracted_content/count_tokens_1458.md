# count tokens
**URL:** https://ai.google.dev/gemini-api/docs/tokens
**Page Title:** Understand and count tokens  |  Gemini API  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemini-api/docs/tokens)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemini-api/docs/tokens?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemini-api/docs/tokens?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemini-api/docs/tokens?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemini-api/docs/tokens?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemini-api/docs/tokens?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemini-api/docs/tokens?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemini-api/docs/tokens?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemini-api/docs/tokens?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemini-api/docs/tokens?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemini-api/docs/tokens?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemini-api/docs/tokens?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemini-api/docs/tokens?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemini-api/docs/tokens?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemini-api/docs/tokens?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Ftokens%3Flang%3Dpython&prompt=select_account)
- On this page
- About tokens
- Try out counting tokens in a Colab
- Context windows
- Count tokens Count text tokens Count multi-turn (chat) tokens Count multimodal tokens System instructions and tools
- Count text tokens
- Count multi-turn (chat) tokens
- Count multimodal tokens
- System instructions and tools
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- Docs
[LINK: Docs](https://ai.google.dev/gemini-api/docs)

## Understand and count tokens

- On this page
- About tokens
- Try out counting tokens in a Colab
- Context windows
- Count tokens Count text tokens Count multi-turn (chat) tokens Count multimodal tokens System instructions and tools
- Count text tokens
- Count multi-turn (chat) tokens
- Count multimodal tokens
- System instructions and tools
Gemini and other generative AI models process input and output at a granularity
called a token .
For Gemini models, a token is equivalent to about 4 characters.
100 tokens is equal to about 60-80 English words.

## About tokens

Tokens can be single characters like z or whole words like cat . Long words
are broken up into several tokens. The set of all tokens used by the model is
called the vocabulary, and the process of splitting text into tokens is called tokenization .
When billing is enabled, the cost of a call to the Gemini API is
determined in part by the number of input and output tokens, so knowing how to
count tokens can be helpful.

## Try out counting tokens in a Colab

You can try out counting tokens by using a Colab.
[LINK: View on ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens)
[LINK: Try a Colab notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb)
[LINK: View notebook on GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb)

## Context windows

The models available through the Gemini API have context windows that are
measured in tokens. The context window defines how much input you can provide
and how much output the model can generate. You can determine the size of the
context window by calling the getModels endpoint or
by looking in the models documentation .
[LINK: getModels endpoint](/api/rest/v1/models/get)
[LINK: models documentation](/gemini-api/docs/models/gemini)
In the following example, you can see that the gemini-2.0-flash model has an
input limit of about 1,000,000 tokens and an output limit of about 8,000 tokens,
which means a context window is 1,000,000 tokens.
[LINK: count_tokens.py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/count_tokens.py#L25-L31)

## Count tokens

All input to and output from the Gemini API is tokenized, including text, image
files, and other non-text modalities.
You can count tokens in the following ways:

### Count text tokens

[LINK: count_tokens.py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/count_tokens.py#L36-L54)

### Count multi-turn (chat) tokens

[LINK: count_tokens.py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/count_tokens.py#L59-L98)

### Count multimodal tokens

All input to the Gemini API is tokenized, including text, image files, and other
non-text modalities. Note the following high-level key points about tokenization
of multimodal input during processing by the Gemini API:
- With Gemini 2.0, image inputs with both dimensions <=384 pixels are counted as
258 tokens. Images larger in one or both dimensions are cropped and scaled as
needed into tiles of 768x768 pixels, each counted as 258 tokens. Prior to Gemini
2.0, images used a fixed 258 tokens.
With Gemini 2.0, image inputs with both dimensions <=384 pixels are counted as
258 tokens. Images larger in one or both dimensions are cropped and scaled as
needed into tiles of 768x768 pixels, each counted as 258 tokens. Prior to Gemini
2.0, images used a fixed 258 tokens.
- Video and audio files are converted to tokens at the following fixed rates:
video at 263 tokens per second and audio at 32 tokens per second.
Video and audio files are converted to tokens at the following fixed rates:
video at 263 tokens per second and audio at 32 tokens per second.
Gemini 3 Pro Preview introduces granular control over multimodal vision processing with the media_resolution parameter. The media_resolution parameter determines the maximum number of tokens allocated per input image or video frame. Higher resolutions improve the model's ability to
read fine text or identify small details, but increase token usage and latency.
For more details about the parameter and how it can impact token calculations,
see the media resolution guide.
[LINK: media resolution](/gemini-api/docs/media-resolution)
Example that uses an uploaded image from the File API:
[LINK: count_tokens.py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/count_tokens.py#L127-L144)
Example that provides the image as inline data:
[LINK: count_tokens.py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/count_tokens.py#L103-L122)
Audio and video are each converted to tokens at the following fixed rates:
- Video: 263 tokens per second
- Audio: 32 tokens per second
[LINK: count_tokens.py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/count_tokens.py#L149-L174)

### System instructions and tools

System instructions and tools also count towards the total token count for the
input.
If you use system instructions, the total_tokens count increases to
reflect the addition of system_instruction .
If you use function calling, the total_tokens count increases to reflect the
addition of tools .
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2025-12-18 UTC.

--------------------