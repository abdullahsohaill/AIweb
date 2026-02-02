# Zonos
**URL:** https://huggingface.co/Zyphra/Zonos-v0.1-hybrid
**Page Title:** Zyphra/Zonos-v0.1-hybrid · Hugging Face
--------------------


## Zonos-v0.1

Zonos-v0.1 is a leading open-weight text-to-speech model trained on more than 200k hours of varied multilingual speech, delivering expressiveness and quality on par with—or even surpassing—top TTS providers.
Our model enables highly natural speech generation from text prompts when given a speaker embedding or audio prefix, and can accurately perform speech cloning when given a reference clip spanning just a few seconds. The conditioning setup also allows for fine control over speaking rate, pitch variation, audio quality, and emotions such as happiness, fear, sadness, and anger. The model outputs speech natively at 44kHz.
Zonos follows a straightforward architecture: text normalization and phonemization via eSpeak, followed by DAC token prediction through a transformer or hybrid backbone. An overview of the architecture can be seen below.

## Usage

### Python

### Gradio interface (recommended)

This should produce a sample.wav file in your project root directory.
For repeated sampling we highly recommend using the gradio interface instead, as the minimal example needs to load the model every time it is run.

## Features

- Zero-shot TTS with voice cloning: Input desired text and a 10-30s speaker sample to generate high quality TTS output
- Audio prefix inputs: Add text plus an audio prefix for even richer speaker matching. Audio prefixes can be used to elicit behaviours such as whispering which can otherwise be challenging to replicate when cloning from speaker embeddings
- Multilingual support: Zonos-v0.1 supports English, Japanese, Chinese, French, and German
- Audio quality and emotion control: Zonos offers fine-grained control of many aspects of the generated audio. These include speaking rate, pitch, maximum frequency, audio quality, and various emotions such as happiness, anger, sadness, and fear.
- Fast: our model runs with a real-time factor of ~2x on an RTX 4090
- Gradio WebUI: Zonos comes packaged with an easy to use gradio interface to generate speech
- Simple installation and deployment: Zonos can be installed and deployed simply using the docker file packaged with our repository.

## Installation

At the moment this repository only supports Linux systems (preferably Ubuntu 22.04/24.04) with recent NVIDIA GPUs (3000-series or newer, 6GB+ VRAM).
See also Docker Installation
Zonos depends on the eSpeak library phonemization. You can install it on Ubuntu with the following command:
We highly recommend using a recent version of uv for installation. If you don't have uv installed, you can install it via pip: pip install -U uv .
For convenience we provide a minimal example to check that the installation works:

## Docker installation

## Citation

If you find this model useful in an academic context please cite as:

## Model tree for Zyphra/Zonos-v0.1-hybrid

## Spaces using Zyphra/Zonos-v0.1-hybrid 35

## Collection including Zyphra/Zonos-v0.1-hybrid


--------------------