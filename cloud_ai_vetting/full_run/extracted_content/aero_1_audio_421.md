# Aero-1-Audio
**URL:** https://huggingface.co/lmms-lab/Aero-1-Audio
**Page Title:** lmms-lab/Aero-1-Audio · Hugging Face
--------------------


## Aero-1-Audio

Aero-1-Audio is a compact audio model adept at various audio tasks, including speech recognition, audio understanding, and following audio instructions.
- Built upon the Qwen-2.5-1.5B language model, Aero delivers strong performance across multiple audio benchmarks while remaining parameter-efficient, even compared with larger advanced models like Whisper and Qwen-2-Audio and Phi-4-Multimodal, or commercial services like ElevenLabs/Scribe.
Built upon the Qwen-2.5-1.5B language model, Aero delivers strong performance across multiple audio benchmarks while remaining parameter-efficient, even compared with larger advanced models like Whisper and Qwen-2-Audio and Phi-4-Multimodal, or commercial services like ElevenLabs/Scribe.
- Aero is trained within one day on 16 H100 GPUs using just 50k hours of audio data. Our insight suggests that audio model training could be sample efficient with high quality and filtered data.
Aero is trained within one day on 16 H100 GPUs using just 50k hours of audio data. Our insight suggests that audio model training could be sample efficient with high quality and filtered data.
- Aero can accurately perform ASR and audio understanding on continuous audio inputs up to 15 minutes in length, which we find the scenario is still a challenge for other models.
Aero can accurately perform ASR and audio understanding on continuous audio inputs up to 15 minutes in length, which we find the scenario is still a challenge for other models.
- Developed by: [LMMs-Lab]
- Model type: [LLM + Audio Encoder]
- Language(s) (NLP): [English]
- License: [MIT]

## How to Get Started with the Model

Use the code below to get started with the model.
You are encouraged to install transformers by using
as this is the transformers version we are using when building this model.

### Simple Demo

### Batch Inference

The model supports batch inference with transformers. An example demo is like this:

## Training Details

### Training Data

We present the contributions of our data mixture here. Our SFT data mixture includes over 20 publicly available datasets, and comparisons with other models highlight the data's lightweight nature.
*The hours of some training datasets are estimated and may not be fully accurate One of the key strengths of our training recipe lies in the quality and quantity of our data. Our training dataset consists of approximately 5 billion tokens, corresponding to around 50,000 hours of audio. Compared to models such as Qwen-Omni and Phi-4, our dataset is over 100 times smaller, yet our model achieves competitive performance. All data is sourced from publicly available open-source datasets, highlighting the sample efficiency of our training approach. A detailed breakdown of our data distribution is provided below, along with comparisons to other models.

## Model tree for lmms-lab/Aero-1-Audio

Base model

## Space using lmms-lab/Aero-1-Audio 1

## Collection including lmms-lab/Aero-1-Audio


--------------------