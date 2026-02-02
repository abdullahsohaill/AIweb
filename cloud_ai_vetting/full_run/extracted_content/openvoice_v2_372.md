# OpenVoice V2
**URL:** https://huggingface.co/myshell-ai/OpenVoiceV2
**Page Title:** myshell-ai/OpenVoiceV2 · Hugging Face
--------------------


## OpenVoice V2

In April 2024, we release OpenVoice V2, which includes all features in V1 and has:
- Better Audio Quality. OpenVoice V2 adopts a different training strategy that delivers better audio quality.
Better Audio Quality. OpenVoice V2 adopts a different training strategy that delivers better audio quality.
- Native Multi-lingual Support. English, Spanish, French, Chinese, Japanese and Korean are natively supported in OpenVoice V2.
Native Multi-lingual Support. English, Spanish, French, Chinese, Japanese and Korean are natively supported in OpenVoice V2.
- Free Commercial Use. Starting from April 2024, both V2 and V1 are released under MIT License. Free for commercial use.
Free Commercial Use. Starting from April 2024, both V2 and V1 are released under MIT License. Free for commercial use.

### Features

- Accurate Tone Color Cloning. OpenVoice can accurately clone the reference tone color and generate speech in multiple languages and accents.
- Flexible Voice Style Control. OpenVoice enables granular control over voice styles, such as emotion and accent, as well as other style parameters including rhythm, pauses, and intonation.
- Zero-shot Cross-lingual Voice Cloning. Neither of the language of the generated speech nor the language of the reference speech needs to be presented in the massive-speaker multi-lingual training dataset.

### How to Use

Please see usage for detailed instructions.
[LINK: usage](https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md)

## Usage

## Table of Content

- Quick Use : directly use OpenVoice without installation.
- Linux Install : for researchers and developers only. V1 V2
- Install on Other Platforms : unofficial installation guide contributed by the community

## Quick Use

The input speech audio of OpenVoice can be in Any Language . OpenVoice can clone the voice in that speech audio, and use the voice to speak in multiple languages. For quick use, we recommend you to try the already deployed services:
- British English
- American English
- Indian English
- Australian English
- Spanish
- French
- Chinese
- Japanese
- Korean

## Linux Install

This section is only for developers and researchers who are familiar with Linux, Python and PyTorch. Clone this repo, and run
No matter if you are using V1 or V2, the above installation is the same.

### OpenVoice V1

Download the checkpoint from here and extract it to the checkpoints folder.
1. Flexible Voice Style Control. Please see demo_part1.ipynb for an example usage of how OpenVoice enables flexible style control over the cloned voice.
[LINK: demo_part1.ipynb](https://github.com/myshell-ai/OpenVoice/blob/main/demo_part1.ipynb)
2. Cross-Lingual Voice Cloning. Please see demo_part2.ipynb for an example for languages seen or unseen in the MSML training set.
[LINK: demo_part2.ipynb](https://github.com/myshell-ai/OpenVoice/blob/main/demo_part2.ipynb)
3. Gradio Demo. . We provide a minimalist local gradio demo here. We strongly suggest the users to look into demo_part1.ipynb , demo_part2.ipynb and the QnA if they run into issues with the gradio demo. Launch a local gradio demo with python -m openvoice_app --share .

### OpenVoice V2

Download the checkpoint from here and extract it to the checkpoints_v2 folder.
Install MeloTTS :
[LINK: MeloTTS](https://github.com/myshell-ai/MeloTTS)
Demo Usage. Please see demo_part3.ipynb for example usage of OpenVoice V2. Now it natively supports English, Spanish, French, Chinese, Japanese and Korean.
[LINK: demo_part3.ipynb](https://github.com/myshell-ai/OpenVoice/blob/main/demo_part3.ipynb)

## Install on Other Platforms

This section provides the unofficial installation guides by open-source contributors in the community:
- Windows Guide by @Alienpups You are welcome to contribute if you have a better installation guide. We will list you here.
- Guide by @Alienpups
[LINK: Guide](https://github.com/Alienpups/OpenVoice/blob/main/docs/USAGE_WINDOWS.md)
[LINK: @Alienpups](https://github.com/Alienpups)
- You are welcome to contribute if you have a better installation guide. We will list you here.
- Docker Guide by @StevenJSCF You are welcome to contribute if you have a better installation guide. We will list you here.
- Guide by @StevenJSCF
[LINK: Guide](https://github.com/StevenJSCF/OpenVoice/blob/update-docs/docs/DF_USAGE.md)
[LINK: @StevenJSCF](https://github.com/StevenJSCF)
- You are welcome to contribute if you have a better installation guide. We will list you here.

### Links

- Github
[LINK: Github](https://github.com/myshell-ai/OpenVoice)
- HFDemo
- Discord
[LINK: How to track](https://huggingface.co/docs/hub/models-download-stats)

## Model tree for myshell-ai/OpenVoiceV2

## Spaces using myshell-ai/OpenVoiceV2 26


--------------------