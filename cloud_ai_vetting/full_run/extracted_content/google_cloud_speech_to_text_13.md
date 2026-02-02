# Google Cloud Speech to Text
**URL:** https://cloud.google.com/speech-to-text
**Page Title:** Speech-to-Text API: speech recognition and transcription | Google Cloud
--------------------

Try Gemini 3 , our best model for reasoning, coding, and multimodal understanding in Vertex AI

## Speech-to-Text

## Turn speech into text using Google AI

Convert audio into text transcriptions and integrate speech recognition into applications with easy-to-use APIs.
New customers also get up to $300 in free credits to try Speech-to-Text and other Google Cloud products.

### Product highlights

- Easily add Speech-to-Text to apps
Easily add Speech-to-Text to apps
- Transcribe audio files or real-time audio
Transcribe audio files or real-time audio
- Supports over 125 languages
Supports over 125 languages
- Use AI to caption videos
Use AI to caption videos
- How to use Speech-to-Text 02:26 mins
How to use Speech-to-Text
02:26 mins
Features

### Advanced speech AI

Speech-to-Text can utilize Chirp 3 , Google Cloud’s foundation model for speech trained on millions of hours of audio data and billions of text sentences. This contrasts with traditional speech recognition techniques that focus on large amounts of language-specific supervised data. These techniques give users improved recognition and transcription for more spoken languages and accents.
[LINK: Chirp 3](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)
[LINK: recognition and transcription](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)

### Support for 85+ languages and variants

Build for a global user base with extensive language support . Transcribe short, long, and even streaming audio data. Speech-to-Text also offers users more accurate and globe-spanning deployments for transcription with Chirp 3 , the next generation of universal speech models.
[LINK: extensive language support](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
[LINK: globe-spanning deployments for transcription with Chirp 3](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)
Chirp 3: Transcription was built using self-supervised training on millions of hours of audio and 28 billion sentences of text spanning 100+ languages.
[LINK: Transcribe short, long, or streaming audio View guide](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize)

### Streaming speech recognition

Receive real-time speech recognition results as the API processes the audio input streamed from your application’s microphone or sent from a prerecorded audio file (inline or through Cloud Storage).

### AI-powered speech recognition and transcription

Speech-to-Text uses model adaptation to improve the accuracy of frequently used words, expand the vocabulary available for transcription, and improve transcription from noisy audio. Model adaptation lets users customize Speech-to-Text to recognize specific words or phrases more frequently than other options that might otherwise be suggested. For example, you could bias Speech-to-Text towards transcribing "weather" over "whether."
[LINK: model adaptation](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3#improve_accuracy_with_model_adaptation)

### Out-of-the-box regulatory and security compliance

Speech-to-Text API v2 gives enterprise and business customers added security and regulatory requirements out of the box. Data residency enables the invocation of transcription models through a fully regionalized service that taps into Google Cloud regions like Singapore and Belgium. Logs for resource generation and transcription are made easily available in the Google Cloud console. And Speech-to-Text API v2 offers enterprise-grade encryption with customer-managed encryption keys for all resources as well as batch transcription.
[LINK: Data residency](https://docs.cloud.google.com/speech-to-text/docs/locations)
[LINK: customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek)

### Speech adaptation

Customize speech recognition to transcribe domain-specific terms and rare words by providing hints and boost your transcription accuracy of specific words or phrases. Automatically convert spoken numbers into addresses, years, currencies, and more using classes .
[LINK: boost](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model)
[LINK: classes](https://docs.cloud.google.com/speech-to-text/docs/class-tokens)

### Speech-to-Text On-Prem

Have full control over your infrastructure and protected speech data while leveraging Google’s speech recognition technology on-premises , right in your own private data centers. Contact sales to get started.
[LINK: on-premises](https://docs.cloud.google.com/speech-to-text/priv)

### Multichannel recognition

Speech-to-Text can recognize distinct channels in multichannel situations (for example, video conference) and annotate the transcripts to preserve the order.

### Noise robustness

Speech-to-Text can handle noisy audio from many environments without requiring additional noise cancellation.

### Domain-specific models

Choose from a selection of trained models for voice control and phone call and video transcription optimized for domain-specific quality requirements. For example, our enhanced phone call model is tuned for audio originated from telephony, such as phone calls recorded at an 8khz sampling rate.
[LINK: selection of trained models](https://docs.cloud.google.com/speech-to-text/docs/overview#select-model)

### Content filtering

Profanity filter helps you detect inappropriate or unprofessional content in your audio data and filter out profane words in text results.

### Transcription evaluation

Upload your own voice data and have it transcribed with no code. Evaluate quality by iterating on your configuration.

### Automatic punctuation (beta)

Speech-to-Text accurately punctuates transcriptions, such as by providing commas, question marks, and periods.

### Speaker diarization

Know who said what by receiving automatic predictions about which of the speakers in a conversation spoke each utterance.
Compare Speech-to-Text Chirp model in API and Vertex AI Studio
Chirp 3: Transcription in Vertex AI
A simple to use no code, web-based, graphical user interface.
Rapidly test audio files, quickly prototype, create audio transcription, upload audio or recordings directly into a web browser.
-Enhanced multilingual language detection and transcription
-Supports transcription in 85+ languages and variants
-Supports speaker diarization and model adaptation
-Automatic speech recognition, transcribing audio into text
-Multilingual language detection and transcription
Chirp 3: Transcription on Speech-to-Text V2 API
An API that is the next generation of Google's universal Speech-to-Text model, unifying data from multiple languages.
Building scalable, Enterprise-grade applications.
Easy transcription integration into existing software.
-Enhanced multilingual language detection and transcription
-Supports transcription in 85+ languages and variants
-Supports speaker diarization and model adaptation
-Automatic speech recognition, transcribing audio into text
-Multilingual language detection and transcription
Chirp 3: Transcription in Vertex AI
A simple to use no code, web-based, graphical user interface.
Rapidly test audio files, quickly prototype, create audio transcription, upload audio or recordings directly into a web browser.
-Enhanced multilingual language detection and transcription
-Supports transcription in 85+ languages and variants
-Supports speaker diarization and model adaptation
-Automatic speech recognition, transcribing audio into text
-Multilingual language detection and transcription
Chirp 3: Transcription on Speech-to-Text V2 API
An API that is the next generation of Google's universal Speech-to-Text model, unifying data from multiple languages.
Building scalable, Enterprise-grade applications.
Easy transcription integration into existing software.
-Enhanced multilingual language detection and transcription
-Supports transcription in 85+ languages and variants
-Supports speaker diarization and model adaptation
-Automatic speech recognition, transcribing audio into text
-Multilingual language detection and transcription
How It Works

### Speech-to-Text has three main methods to perform speech recognition: synchronous, asynchronous, and streaming. Each method returns text results based on if transcription is needed in post processing, periodically, or in real time. Simply put, you'll input audio data and then receive a text-based response.

Speech-to-Text has three main methods to perform speech recognition: synchronous, asynchronous, and streaming. Each method returns text results based on if transcription is needed in post processing, periodically, or in real time. Simply put, you'll input audio data and then receive a text-based response.
Demo

## Test out the Speech-to-Text API

Quickly create audio transcription from a file upload or directly speaking into a mic.
Common Uses

### Transcribe audio

## Create an audio transcription

Create an audio transcription
Learn how to use the Speech-to-Text API from within the Google Cloud console by creating an audio transcription in just a few steps. You can also transcribe streaming , short , and long audio.
[LINK: streaming](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize)
[LINK: short](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize)
[LINK: long](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize)
- Browse sample applications
[LINK: Browse sample applications](https://docs.cloud.google.com/speech-to-text/docs/samples)
Browse sample applications
- Speech-to-Text tutorials and guides
[LINK: Speech-to-Text tutorials and guides](https://docs.cloud.google.com/speech-to-text/docs/quickstarts/console-tutorials)
Speech-to-Text tutorials and guides
- Transcribe audio from a mic to text
[LINK: Transcribe audio from a mic to text](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize)
Transcribe audio from a mic to text

## Create an audio transcription

Create an audio transcription
Learn how to use the Speech-to-Text API from within the Google Cloud console by creating an audio transcription in just a few steps. You can also transcribe streaming , short , and long audio.
[LINK: streaming](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize)
[LINK: short](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize)
[LINK: long](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize)
- Browse sample applications
[LINK: Browse sample applications](https://docs.cloud.google.com/speech-to-text/docs/samples)
Browse sample applications
- Speech-to-Text tutorials and guides
[LINK: Speech-to-Text tutorials and guides](https://docs.cloud.google.com/speech-to-text/docs/quickstarts/console-tutorials)
Speech-to-Text tutorials and guides
- Transcribe audio from a mic to text
[LINK: Transcribe audio from a mic to text](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize)
Transcribe audio from a mic to text

### Caption videos using AI

## Create subtitles for videos using AI

Create subtitles for videos using AI
Transcribe your audio and video to include captions. Add subtitles to existing content or in real time to streaming content. Our Chirp 3: Transcription is ideal for indexing or subtitling video and/or multi-speaker content and uses similar machine learning technology as YouTube does for video captioning.
[LINK: Chirp 3: Transcription](https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model)
This tutorial shows you how to use the Google Cloud AI services Speech-to-Text API and Translation API to add subtitles to videos and to provide localized subtitles in other languages.
- Dub videos using AI
Dub videos using AI
- Transcribe audio from a video file using Speech-to-Text
[LINK: Transcribe audio from a video file using Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-audio-from-video-speech-to-text)
Transcribe audio from a video file using Speech-to-Text
- Transcribe audio from a streaming video
[LINK: Transcribe audio from a streaming video](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize)
Transcribe audio from a streaming video

## Create subtitles for videos using AI

Create subtitles for videos using AI
Transcribe your audio and video to include captions. Add subtitles to existing content or in real time to streaming content. Our Chirp 3: Transcription is ideal for indexing or subtitling video and/or multi-speaker content and uses similar machine learning technology as YouTube does for video captioning.
[LINK: Chirp 3: Transcription](https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model)
This tutorial shows you how to use the Google Cloud AI services Speech-to-Text API and Translation API to add subtitles to videos and to provide localized subtitles in other languages.
- Dub videos using AI
Dub videos using AI
- Transcribe audio from a video file using Speech-to-Text
[LINK: Transcribe audio from a video file using Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-audio-from-video-speech-to-text)
Transcribe audio from a video file using Speech-to-Text
- Transcribe audio from a streaming video
[LINK: Transcribe audio from a streaming video](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize)
Transcribe audio from a streaming video

### Add Speech-to-Text to apps

## How to add Speech-to-Text to apps

How to add Speech-to-Text to apps
Learn how you can quickly and easily enable Speech-to-Text for your application with Google Cloud. This video covers how to add AI to your application without extensive machine learning model experience. Using the pretrained Speech-to-Text API you'll quickly and easily enable AI for your application.
- Add voice control to apps
Add voice control to apps

## How to add Speech-to-Text to apps

How to add Speech-to-Text to apps
Learn how you can quickly and easily enable Speech-to-Text for your application with Google Cloud. This video covers how to add AI to your application without extensive machine learning model experience. Using the pretrained Speech-to-Text API you'll quickly and easily enable AI for your application.
- Add voice control to apps
Add voice control to apps

### Translate audio into text

## Language, speech, text, and translation with Google Cloud APIs

Language, speech, text, and translation with Google Cloud APIs
In this course, you'll use the Speech-to-Text API to transcribe an audio file into a text file, translate with the Google Cloud Translation API , and create synthetic speech with Natural Language AI .
- View supported languages
[LINK: View supported languages](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
View supported languages
[LINK: supported languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
- Learn more about Google Cloud Translation
Learn more about Google Cloud Translation

## Language, speech, text, and translation with Google Cloud APIs

Language, speech, text, and translation with Google Cloud APIs
In this course, you'll use the Speech-to-Text API to transcribe an audio file into a text file, translate with the Google Cloud Translation API , and create synthetic speech with Natural Language AI .
- View supported languages
[LINK: View supported languages](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
View supported languages
[LINK: supported languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
- Learn more about Google Cloud Translation
Learn more about Google Cloud Translation
Pricing
Speech-to-Text V2 API
V2 offers data residency for multi and single region deployments of Chirp 3. V2 does include audit logging and support for customer managed encryption keys.
$0.016
per min
View pricing details for Speech-to-Text.
How Speech-to-Text pricing works
Speech-to-Text pricing is based on the API version, channels, batch methods, and any additional Google Cloud service costs like storage.
Speech-to-Text V2 API
V2 offers data residency for multi and single region deployments of Chirp 3. V2 does include audit logging and support for customer managed encryption keys.
$0.016
per min
View pricing details for Speech-to-Text.

### Pricing calculator

### Custom quote

### Start your proof of concept

### New customers get up to $300 in free credits to try Speech-to-Text and other Google Cloud products

### Have a large project?

### Speech-to-Text On-Prem

### Speech-to-Text basics

### Speech-to-Text code samples


--------------------