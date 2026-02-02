# Gemma-3n
documentation
**URL:** https://ai.google.dev/gemma/docs/gemma-3n
**Page Title:** Gemma 3n model overview  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemma/docs/gemma-3n)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemma/docs/gemma-3n?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemma/docs/gemma-3n?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemma/docs/gemma-3n?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemma/docs/gemma-3n?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemma/docs/gemma-3n?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemma/docs/gemma-3n?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemma/docs/gemma-3n?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemma/docs/gemma-3n?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemma/docs/gemma-3n?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemma/docs/gemma-3n?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemma/docs/gemma-3n?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemma/docs/gemma-3n?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemma/docs/gemma-3n?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemma/docs/gemma-3n?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemma/docs/gemma-3n?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemma/docs/gemma-3n?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemma/docs/gemma-3n?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemma/docs/gemma-3n?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemma/docs/gemma-3n?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemma/docs/gemma-3n?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemma/docs/gemma-3n?hl=ko)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemma%2Fdocs%2Fgemma-3n&prompt=select_account)
- On this page
- Model parameters and effective parameters
- PLE caching
- MatFormer architecture
- Conditional parameter loading
[LINK: Learn more](/gemma/docs/functiongemma)
- Home
- Gemma
- Models
- Docs
[LINK: Docs](https://ai.google.dev/gemma/docs)

## Gemma 3n model overview

- On this page
- Model parameters and effective parameters
- PLE caching
- MatFormer architecture
- Conditional parameter loading
Gemma 3n is a generative AI model optimized for use in everyday devices, such as
phones, laptops, and tablets. This model includes innovations in
parameter-efficient processing, including Per-Layer Embedding (PLE) parameter
caching and a MatFormer model architecture that provides the flexibility to
reduce compute and memory requirements. These models feature audio input
handling, as well as text and visual data.
Gemma 3n includes the following key features:
- Audio input : Process sound data for speech recognition, translation,
and audio data analysis. Learn more
[LINK: Learn more](/gemma/docs/core/huggingface_inference#audio)
- Visual and text input : Multimodal capabilities let you handle vision,
sound, and text to help you understand and analyze the world around you. Learn more
[LINK: Learn more](/gemma/docs/core/huggingface_inference#vision)
- Vision encoder: High-performance MobileNet-V5 encoder substantially
improves speed and accuracy of processing visual data. Learn more
[LINK: Learn more](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/#mobilenet-v5:-new-state-of-the-art-vision-encoder)
- PLE caching : Per-Layer Embedding (PLE) parameters contained in these
models can be cached to fast, local storage to reduce model memory run
costs. Learn more
- MatFormer architecture: Matryoshka Transformer architecture allows
for selective activation of the models parameters per request to reduce
compute cost and response times. Learn more
- Conditional parameter loading: Bypass loading of vision and audio
parameters in the model to reduce the total number of loaded parameters and
save memory resources. Learn more
- Wide language support : Wide linguistic capabilities, trained in over
140 languages.
- 32K token context : Substantial input context for analyzing data and
handling processing tasks.
Get it on Kaggle Get it on Hugging Face
As with other Gemma models, Gemma 3n is provided with open weights and
licensed for responsible commercial use , allowing you to tune
and deploy it in your own projects and applications.

## Model parameters and effective parameters

Gemma 3n models are listed with parameter counts, such as E2B and E4B , that are lower than the total number of parameters contained in the
models. The E prefix indicates these models can operate with a reduced set
of Effective parameters. This reduced parameter operation can be achieved using
the flexible parameter technology built into Gemma 3n models to help them run
efficiently on lower resource devices.
The parameters in Gemma 3n models are divided into 4 main groups: text, visual,
audio, and per-layer embedding (PLE) parameters. With standard execution of the
E2B model, over 5 billion parameters are loaded when executing the model.
However, using parameter skipping and PLE caching techniques, this model can be
operated with an effective memory load of just under 2 billion (1.91B)
parameters, as illustrated in Figure 1.
Figure 1. Gemma 3n E2B model parameters running in standard execution
versus an effectively lower parameter load using PLE caching and parameter
skipping techniques.
Using these parameter offloading and selective activation techniques, you can
run the model with a very lean set of parameters or activate additional
parameters to handle other data types such as visual and audio. These features
enable you to ramp up model functionality or ramp down capabilities based on
device capabilities or task requirements. The following sections explain more
about the parameter efficient techniques available in Gemma 3n models.

## PLE caching

Gemma 3n models include Per-Layer Embedding (PLE) parameters that are used
during model execution to create data that enhances the performance of each
model layer. The PLE data can be generated separately, outside the operating
memory of the model, cached to fast storage, and then added to the model
inference process as each layer runs. This approach allows PLE parameters to be
kept out of the model memory space, reducing resource consumption while still
improving model response quality.

## MatFormer architecture

Gemma 3n models use a Matryoshka Transformer or MatFormer model architecture
that contains nested, smaller models within a single, larger model. The nested
sub-models can be used for inferences without activating the parameters of the
enclosing models when responding to requests. This ability to run just the
smaller, core models within a MatFormer model can reduce compute cost, and
response time, and energy footprint for the model. In the case of Gemma 3n, the
E4B model contains the parameters of the E2B model. This architecture also
lets you select parameters and assemble models in intermediate sizes
between 2B and 4B. For more details on this approach, see the MatFormer research paper .
Try using MatFormer techniques to reduce the size of a Gemma 3n model with the MatFormer Lab guide.

## Conditional parameter loading

Similar to PLE parameters, you can skip loading of some parameters into memory,
such as audio or visual parameters, in the Gemma 3n model to reduce memory load.
These parameters can be dynamically loaded at runtime if the device has the
required resources. Overall, parameter skipping can further reduce the required
operating memory for a Gemma 3n model, enabling execution on a wider range of
devices and allowing developers to increase resource efficiency for less
demanding tasks.
Ready to start building? Get started with Gemma models!
[LINK: Get started](/gemma/docs/get_started)
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2025-11-01 UTC.

--------------------