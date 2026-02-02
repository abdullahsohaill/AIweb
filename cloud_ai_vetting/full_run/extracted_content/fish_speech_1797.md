# Fish Speech
**URL:** https://speech.fish.audio
**Page Title:** OpenAudio
--------------------


## OpenAudio (formerly Fish-Speech)

License Notice
This codebase is released under Apache License and all model weights are released under CC-BY-NC-SA-4.0 License . Please refer to CODE LICENSE and MODEL LICENSE for more details.
[LINK: CODE LICENSE](https://github.com/fishaudio/fish-speech/blob/main/LICENSE)
Legal Disclaimer
We do not hold any responsibility for any illegal usage of the codebase. Please refer to your local laws about DMCA and other related laws.

## Introduction

We are excited to announce that we have rebranded to OpenAudio - introducing a brand new series of advanced Text-to-Speech models that builds upon the foundation of Fish-Speech with significant improvements and new capabilities.
Openaudio-S1-mini : Blog ; Video ; Hugging Face ;
Fish-Speech v1.5 : Video ; Hugging Face ;

## Highlights

### Excellent TTS quality

We use Seed TTS Eval Metrics to evaluate the model performance, and the results show that OpenAudio S1 achieves 0.008 WER and 0.004 CER on English text, which is significantly better than previous models. (English, auto eval, based on OpenAI gpt-4o-transcribe, speaker distance using Revai/pyannote-wespeaker-voxceleb-resnet34-LM)

### Best Model in TTS-Arena2

OpenAudio S1 has achieved the #1 ranking on TTS-Arena2 , the benchmark for text-to-speech evaluation:

### Speech Control

OpenAudio S1 supports a variety of emotional, tone, and special markers to enhance speech synthesis:
- Basic emotions : (angry) (sad) (excited) (surprised) (satisfied) (delighted) (scared) (worried) (upset) (nervous) (frustrated) (depressed) (empathetic) (embarrassed) (disgusted) (moved) (proud) (relaxed) (grateful) (confident) (interested) (curious) (confused) (joyful)
Basic emotions :
- Advanced emotions : (disdainful) (unhappy) (anxious) (hysterical) (indifferent) (impatient) (guilty) (scornful) (panicked) (furious) (reluctant) (keen) (disapproving) (negative) (denying) (astonished) (serious) (sarcastic) (conciliative) (comforting) (sincere) (sneering) (hesitating) (yielding) (painful) (awkward) (amused)
Advanced emotions :
(Support for English, Chinese and Japanese now, and more languages is coming soon!)
- Tone markers : (in a hurry tone) (shouting) (screaming) (whispering) (soft tone)
Tone markers :
- Special audio effects : (laughing) (chuckling) (sobbing) (crying loudly) (sighing) (panting) (groaning) (crowd laughing) (background laughter) (audience laughing)
Special audio effects :
You can also use Ha,ha,ha to control, there's many other cases waiting to be explored by yourself.

### Two Type of Models

We offer two model variants to suit different needs:
- OpenAudio S1 (4B parameters) : Our full-featured flagship model available on fish.audio , delivering the highest quality speech synthesis with all advanced features.
OpenAudio S1 (4B parameters) : Our full-featured flagship model available on fish.audio , delivering the highest quality speech synthesis with all advanced features.
- OpenAudio S1-mini (0.5B parameters) : A distilled version with core capabilities, available on Hugging Face Space , optimized for faster inference while maintaining excellent quality.
OpenAudio S1-mini (0.5B parameters) : A distilled version with core capabilities, available on Hugging Face Space , optimized for faster inference while maintaining excellent quality.
Both S1 and S1-mini incorporate online Reinforcement Learning from Human Feedback (RLHF).

## Features

- Zero-shot & Few-shot TTS: Input a 10 to 30-second vocal sample to generate high-quality TTS output. For detailed guidelines, see Voice Cloning Best Practices .
Zero-shot & Few-shot TTS: Input a 10 to 30-second vocal sample to generate high-quality TTS output. For detailed guidelines, see Voice Cloning Best Practices .
[LINK: Voice Cloning Best Practices](https://docs.fish.audio/text-to-speech/voice-clone-best-practices)
- Multilingual & Cross-lingual Support: Simply copy and paste multilingual text into the input box—no need to worry about the language. Currently supports English, Japanese, Korean, Chinese, French, German, Arabic, and Spanish.
Multilingual & Cross-lingual Support: Simply copy and paste multilingual text into the input box—no need to worry about the language. Currently supports English, Japanese, Korean, Chinese, French, German, Arabic, and Spanish.
- No Phoneme Dependency: The model has strong generalization capabilities and does not rely on phonemes for TTS. It can handle text in any language script.
No Phoneme Dependency: The model has strong generalization capabilities and does not rely on phonemes for TTS. It can handle text in any language script.
- Highly Accurate: Achieves a low CER (Character Error Rate) of around 0.4% and WER (Word Error Rate) of around 0.8% for Seed-TTS Eval.
Highly Accurate: Achieves a low CER (Character Error Rate) of around 0.4% and WER (Word Error Rate) of around 0.8% for Seed-TTS Eval.
- Fast: Accelerated by torch compile, the real-time factor is approximately 1:7 on an Nvidia RTX 4090 GPU.
Fast: Accelerated by torch compile, the real-time factor is approximately 1:7 on an Nvidia RTX 4090 GPU.
- WebUI Inference: Features an easy-to-use, Gradio-based web UI compatible with Chrome, Firefox, Edge, and other browsers.
WebUI Inference: Features an easy-to-use, Gradio-based web UI compatible with Chrome, Firefox, Edge, and other browsers.
- GUI Inference: Offers a PyQt6 graphical interface that works seamlessly with the API server. Supports Linux, Windows, and macOS. See GUI .
GUI Inference: Offers a PyQt6 graphical interface that works seamlessly with the API server. Supports Linux, Windows, and macOS. See GUI .
[LINK: See GUI](https://github.com/AnyaCoder/fish-speech-gui)
- Deploy-Friendly: Easily set up an inference server with native support for Linux, Windows (MacOS comming soon), minimizing speed loss.
Deploy-Friendly: Easily set up an inference server with native support for Linux, Windows (MacOS comming soon), minimizing speed loss.

## Media & Demos

### Social Media

### Interactive Demos

### Video Showcases

## Documentation

### Quick Start

- Build Environment - Set up your development environment
- Inference Guide - Run the model and generate speech

## Community & Support

- Discord: Join our Discord community
- Website: Visit OpenAudio.com for latest updates
- Try Online: Fish Audio Playground

--------------------