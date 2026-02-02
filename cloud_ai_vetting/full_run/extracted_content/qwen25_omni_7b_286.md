# Qwen2.5-Omni-7B
**URL:** https://huggingface.co/Qwen/Qwen2.5-Omni-7B
**Page Title:** Qwen/Qwen2.5-Omni-7B · Hugging Face
--------------------


## Qwen2.5-Omni

## Overview

### Introduction

Qwen2.5-Omni is an end-to-end multimodal model designed to perceive diverse modalities, including text, images, audio, and video, while simultaneously generating text and natural speech responses in a streaming manner.

### Key Features

- Omni and Novel Architecture : We propose Thinker-Talker architecture, an end-to-end multimodal model designed to perceive diverse modalities, including text, images, audio, and video, while simultaneously generating text and natural speech responses in a streaming manner. We propose a novel position embedding, named TMRoPE (Time-aligned Multimodal RoPE), to synchronize the timestamps of video inputs with audio.
Omni and Novel Architecture : We propose Thinker-Talker architecture, an end-to-end multimodal model designed to perceive diverse modalities, including text, images, audio, and video, while simultaneously generating text and natural speech responses in a streaming manner. We propose a novel position embedding, named TMRoPE (Time-aligned Multimodal RoPE), to synchronize the timestamps of video inputs with audio.
- Real-Time Voice and Video Chat : Architecture designed for fully real-time interactions, supporting chunked input and immediate output.
Real-Time Voice and Video Chat : Architecture designed for fully real-time interactions, supporting chunked input and immediate output.
- Natural and Robust Speech Generation : Surpassing many existing streaming and non-streaming alternatives, demonstrating superior robustness and naturalness in speech generation.
Natural and Robust Speech Generation : Surpassing many existing streaming and non-streaming alternatives, demonstrating superior robustness and naturalness in speech generation.
- Strong Performance Across Modalities : Exhibiting exceptional performance across all modalities when benchmarked against similarly sized single-modality models. Qwen2.5-Omni outperforms the similarly sized Qwen2-Audio in audio capabilities and achieves comparable performance to Qwen2.5-VL-7B.
Strong Performance Across Modalities : Exhibiting exceptional performance across all modalities when benchmarked against similarly sized single-modality models. Qwen2.5-Omni outperforms the similarly sized Qwen2-Audio in audio capabilities and achieves comparable performance to Qwen2.5-VL-7B.
- Excellent End-to-End Speech Instruction Following : Qwen2.5-Omni shows performance in end-to-end speech instruction following that rivals its effectiveness with text inputs, evidenced by benchmarks such as MMLU and GSM8K.
Excellent End-to-End Speech Instruction Following : Qwen2.5-Omni shows performance in end-to-end speech instruction following that rivals its effectiveness with text inputs, evidenced by benchmarks such as MMLU and GSM8K.

### Model Architecture

### Performance

We conducted a comprehensive evaluation of Qwen2.5-Omni, which demonstrates strong performance across all modalities when compared to similarly sized single-modality models and closed-source models like Qwen2.5-VL-7B, Qwen2-Audio, and Gemini-1.5-pro. In tasks requiring the integration of multiple modalities, such as OmniBench, Qwen2.5-Omni achieves state-of-the-art performance. Furthermore, in single-modality tasks, it excels in areas including speech recognition (Common Voice), translation (CoVoST2), audio understanding (MMAU), image reasoning (MMMU, MMStar), video understanding (MVBench), and speech generation (Seed-tts-eval and subjective naturalness).

## Quickstart

Below, we provide simple examples to show how to use Qwen2.5-Omni with 🤗 Transformers. The codes of Qwen2.5-Omni has been in the latest Hugging face transformers and we advise you to build from source with command:
or you might encounter the following error:
We offer a toolkit to help you handle various types of audio and visual input more conveniently, as if you were using an API. This includes base64, URLs, and interleaved audio, images and videos. You can install it using the following command and make sure your system has ffmpeg installed:
If you are not using Linux, you might not be able to install decord from PyPI. In that case, you can use pip install qwen-omni-utils -U which will fall back to using torchvision for video processing. However, you can still install decord from source to get decord used when loading video.
[LINK: install decord from source](https://github.com/dmlc/decord?tab=readme-ov-file#install-from-source)

### 🤗  Transformers Usage

Here we show a code snippet to show you how to use the chat model with transformers and qwen_omni_utils :
Note: The table above presents the theoretical minimum memory requirements for inference with transformers and BF16 is test with attn_implementation="flash_attention_2" ; however, in practice, the actual memory usage is typically at least 1.2 times higher. For more information, see the linked resource here .
[LINK: here](https://huggingface.co/docs/accelerate/main/en/usage_guides/model_size_estimator)
Video URL compatibility largely depends on the third-party library version. The details are in the table below. Change the backend by FORCE_QWENVL_VIDEO_READER=torchvision or FORCE_QWENVL_VIDEO_READER=decord if you prefer not to use the default one.
The model can batch inputs composed of mixed samples of various types such as text, images, audio and videos as input when return_audio=False is set. Here is an example.

### Usage Tips

If users need audio output, the system prompt must be set as "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech.", otherwise the audio output may not work as expected.
In the process of multimodal interaction, the videos provided by users are often accompanied by audio (such as questions about the content in the video, or sounds generated by certain events in the video). This information is conducive to the model providing a better interactive experience. So we provide the following options for users to decide whether to use audio in video.
It is worth noting that during a multi-round conversation, the use_audio_in_video parameter in these places must be set to the same, otherwise unexpected results will occur.
The model supports both text and audio outputs, if users do not need audio outputs, they can call model.disable_talker() after init the model. This option will save about ~2GB of GPU memory but the return_audio option for generate function will only allow to be set at False .
In order to obtain a flexible experience, we recommend that users can decide whether to return audio when generate function is called. If return_audio is set to False , the model will only return text outputs to get text responses faster.
Qwen2.5-Omni supports the ability to change the voice of the output audio. The "Qwen/Qwen2.5-Omni-7B" checkpoint support two voice types as follow:
Users can use the speaker parameter of generate function to specify the voice type. By default, if speaker is not specified, the default voice type is Chelsie .
First, make sure to install the latest version of Flash Attention 2:
Also, you should have hardware that is compatible with FlashAttention 2. Read more about it in the official documentation of the flash attention repository . FlashAttention-2 can only be used when a model is loaded in torch.float16 or torch.bfloat16 .
[LINK: flash attention repository](https://github.com/Dao-AILab/flash-attention)
To load and run a model using FlashAttention-2, add attn_implementation="flash_attention_2" when loading the model:

## Citation

If you find our paper and code useful in your research, please consider giving a star :star: and citation :pencil: :)
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for Qwen/Qwen2.5-Omni-7B

## Spaces using Qwen/Qwen2.5-Omni-7B 55

## Collection including Qwen/Qwen2.5-Omni-7B

## Paper for Qwen/Qwen2.5-Omni-7B


--------------------