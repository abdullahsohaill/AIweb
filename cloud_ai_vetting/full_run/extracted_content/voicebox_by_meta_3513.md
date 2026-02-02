# Voicebox by Meta
**URL:** https://voicebox.metademolab.com
**Page Title:** Home | VoiceBox
--------------------

- Denoising
- Editing
- Zero-Shot TTS
- Cross-Lingual Zero-Shot TTS
- Sampling
- Efficiency
- SpeechFlow
- Blog
- Paper
- Denoising
- Editing
- Zero-Shot TTS
- Cross-Lingual Zero-Shot TTS
- Sampling
- Efficiency
- SpeechFlow
- Blog
- Paper

## Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale

## Model Overview

Voicebox is a non-autoregressive flow-matching model trained to infill
speech given audio context and text. We train an English-only Voicebox
on 60K hours of data and a multilingual version on 50K hours of data
covering six languages (English, French, German, Spanish, Polish, and
Portuguese).

## Application Overview

Voicebox can tasks not explicitly trained on through in-context
learning. It is more flexible than auto-regressive models because it
can condition on not only past but also future context. We show that
Voicebox can be used for monolingual and cross-lingual zero-shot
text-to-speech synthesis, style conversion, transient noise removal,
content editing, and diverse sample generation.

## Demos

In this website we included a series of Voicebox examples, covering editing, sampling and style transfer with cross lingual features. Take a look.

### Transient noise removal

Getting interrupted by doorbell or dog barking while recording speech?
Now there is no need to re-record the speech anymore. Voicebox can be
used like a magic eraser to remove transient noise by re-generating
noise corrupted speech.
Text : in zero weather in mid-winter when the earth is frozen to a great depth below the surface when in driving over the unpaved country roads they give forth a hard metallic road

### Content editing

Voicebox can also help correct misspoken words without having the
speaker to re-record the audio.
Original text: will find himself completely at a loss on occasions of common and constant recurrence speculative ability is one thing and practical ability is another
Edited text: will find himself completely at a loss on rare and unpredictable circumstances speculative ability is one thing and practical ability is another

### Zero-shot text-to-speech synthesis

Through in-context learning, Voicebox can synthesize speech with any
audio style by taking as input a reference audio of the desired style
and the text to synthesize. It produces speech that sounds coherent to
the reference in every aspects, including voice, background noise, and
speaking style.
Target Text : Voicebox is the swiss army knife of text to speech acing multiple languages, changing voice styles, and dishing out custom samples.

### Cross-lingual style transfer

Beyond using an English audio prompt to generate English speech,
Voicebox can also transfer style across languages. For example, one can
generate English with a French prompt, which would enable everyone to speak any
language in their own voice one day! In addition, Voicebox can also preserve
the original temporal alignment between text and speech, which can be used for
converting dubbed speech to the original speaker’s voice.
We see by this example that admirable as is the progress accomplished in certain regions of physics there still exist many over neglected regions which remain in painful darkness

### Diverse speech generation

Last but not least, Voicebox can create unique and expressive audio
styles by sampling without conditioning on any audio.
Text : His conduct and presence of mind in this emergence appeared conspicuous

## Ethics Statement

As with other powerful new AI innovations, we recognize this technology brings the potential for misuse and unintended harm. In our paper, we detail how we built a highly effective classifier that can distinguish between authentic speech and audio generated with Voicebox to mitigate these possible future risks. There are many exciting use cases for generative speech models, but because of the risks of misuse, we are not making the Voicebox model or code publicly available at this time. While we believe it is important to be open with the AI community and to share our research to advance the state of the art in AI, it’s also necessary to strike the right balance between openness with responsibility.

--------------------