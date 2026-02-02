# MiniCPM-o-2_6
**URL:** https://huggingface.co/openbmb/MiniCPM-o-2_6
**Page Title:** openbmb/MiniCPM-o-2_6 · Hugging Face
--------------------


## A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming on Your Phone

GitHub | Online Demo | Technical Blog | Join Us
[LINK: GitHub](https://github.com/OpenBMB/MiniCPM-o)

### News

- [2025.06.20] ⭐️⭐️⭐️ Our official ollama repository is released. Try our latest models with one click ！
[2025.06.20] ⭐️⭐️⭐️ Our official ollama repository is released. Try our latest models with one click ！
- [2025.03.01] 🚀🚀🚀 RLAIF-V, which is the alignment technique of MiniCPM-o, is accepted by CVPR 2025！The code , dataset , paper are open-sourced!
[2025.03.01] 🚀🚀🚀 RLAIF-V, which is the alignment technique of MiniCPM-o, is accepted by CVPR 2025！The code , dataset , paper are open-sourced!
[LINK: code](https://github.com/RLHF-V/RLAIF-V)
- [2025.01.24] 📢📢📢 MiniCPM-o 2.6 technical report is released! See Here .
[2025.01.24] 📢📢📢 MiniCPM-o 2.6 technical report is released! See Here .
- [2025.01.19] ⭐️⭐️⭐️ MiniCPM-o tops GitHub Trending and reaches top-2 on Hugging Face Trending!
[2025.01.19] ⭐️⭐️⭐️ MiniCPM-o tops GitHub Trending and reaches top-2 on Hugging Face Trending!

## MiniCPM-o 2.6

MiniCPM-o 2.6 is the latest and most capable model in the MiniCPM-o series. The model is built in an end-to-end fashion based on SigLip-400M, Whisper-medium-300M, ChatTTS-200M, and Qwen2.5-7B with a total of 8B parameters. It exhibits a significant performance improvement over MiniCPM-V 2.6, and introduces new features for real-time speech conversation and multimodal live streaming. Notable features of MiniCPM-o 2.6 include:
- 🔥 Leading Visual Capability. MiniCPM-o 2.6 achieves an average score of 70.2 on OpenCompass, a comprehensive evaluation over 8 popular benchmarks. With only 8B parameters, it surpasses widely used proprietary models like GPT-4o-202405, Gemini 1.5 Pro, and Claude 3.5 Sonnet for single image understanding. It also outperforms GPT-4V and Claude 3.5 Sonnet in mutli-image and video understanding, and shows promising in-context learning capability.
🔥 Leading Visual Capability. MiniCPM-o 2.6 achieves an average score of 70.2 on OpenCompass, a comprehensive evaluation over 8 popular benchmarks. With only 8B parameters, it surpasses widely used proprietary models like GPT-4o-202405, Gemini 1.5 Pro, and Claude 3.5 Sonnet for single image understanding. It also outperforms GPT-4V and Claude 3.5 Sonnet in mutli-image and video understanding, and shows promising in-context learning capability.
- 🎙 State-of-the-art Speech Capability. MiniCPM-o 2.6 supports bilingual real-time speech conversation with configurable voices in English and Chinese. It outperforms GPT-4o-realtime on audio understanding tasks such as ASR and STT translation, and shows state-of-the-art performance on speech conversation in both semantic and acoustic evaluations in the open-source community . It also allows for fun features such as emotion/speed/style control, end-to-end voice cloning, role play, etc.
🎙 State-of-the-art Speech Capability. MiniCPM-o 2.6 supports bilingual real-time speech conversation with configurable voices in English and Chinese. It outperforms GPT-4o-realtime on audio understanding tasks such as ASR and STT translation, and shows state-of-the-art performance on speech conversation in both semantic and acoustic evaluations in the open-source community . It also allows for fun features such as emotion/speed/style control, end-to-end voice cloning, role play, etc.
- 🎬 Strong Multimodal Live Streaming Capability. As a new feature, MiniCPM-o 2.6 can accept continous video and audio streams independent of user queries, and support real-time speech interaction . It outperforms GPT-4o-202408 and Claude 3.5 Sonnet and shows state-of-art performance in open-source community on StreamingBench , a comprehensive benchmark for real-time video understanding, omni-source (video & audio) understanding, and multimodal contextual understanding.
🎬 Strong Multimodal Live Streaming Capability. As a new feature, MiniCPM-o 2.6 can accept continous video and audio streams independent of user queries, and support real-time speech interaction . It outperforms GPT-4o-202408 and Claude 3.5 Sonnet and shows state-of-art performance in open-source community on StreamingBench , a comprehensive benchmark for real-time video understanding, omni-source (video & audio) understanding, and multimodal contextual understanding.
- 💪 Strong OCR Capability and Others. Advancing popular visual capabilites from MiniCPM-V series, MiniCPM-o 2.6 can process images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344). It achieves state-of-the-art performance on OCRBench for models under 25B, surpassing proprietary models such as GPT-4o-202405 .
Based on the the latest RLAIF-V and VisCPM techniques, it features trustworthy behaviors , outperforming GPT-4o and Claude 3.5 Sonnet on MMHal-Bench, and supports multilingual capabilities on more than 30 languages.
💪 Strong OCR Capability and Others. Advancing popular visual capabilites from MiniCPM-V series, MiniCPM-o 2.6 can process images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344). It achieves state-of-the-art performance on OCRBench for models under 25B, surpassing proprietary models such as GPT-4o-202405 .
Based on the the latest RLAIF-V and VisCPM techniques, it features trustworthy behaviors , outperforming GPT-4o and Claude 3.5 Sonnet on MMHal-Bench, and supports multilingual capabilities on more than 30 languages.
[LINK: RLAIF-V](https://github.com/RLHF-V/RLAIF-V/)
[LINK: VisCPM](https://github.com/OpenBMB/VisCPM)
- 🚀 Superior Efficiency. In addition to its friendly size, MiniCPM-o 2.6 also shows state-of-the-art token density (i.e., number of pixels encoded into each visual token). It produces only 640 tokens when processing a 1.8M pixel image, which is 75% fewer than most models . This directly improves the inference speed, first-token latency, memory usage, and power consumption. As a result, MiniCPM-o 2.6 can efficiently support multimodal live streaming on end-side devices such as iPad.
🚀 Superior Efficiency. In addition to its friendly size, MiniCPM-o 2.6 also shows state-of-the-art token density (i.e., number of pixels encoded into each visual token). It produces only 640 tokens when processing a 1.8M pixel image, which is 75% fewer than most models . This directly improves the inference speed, first-token latency, memory usage, and power consumption. As a result, MiniCPM-o 2.6 can efficiently support multimodal live streaming on end-side devices such as iPad.
- 💫 Easy Usage. MiniCPM-o 2.6 can be easily used in various ways: (1) llama.cpp support for efficient CPU inference on local devices, (2) int4 and GGUF format quantized models in 16 sizes, (3) vLLM support for high-throughput and memory-efficient inference, (4) fine-tuning on new domains and tasks with LLaMA-Factory , (5) quick local WebUI demo setup with Gradio , and (6) online web demo on server .
💫 Easy Usage. MiniCPM-o 2.6 can be easily used in various ways: (1) llama.cpp support for efficient CPU inference on local devices, (2) int4 and GGUF format quantized models in 16 sizes, (3) vLLM support for high-throughput and memory-efficient inference, (4) fine-tuning on new domains and tasks with LLaMA-Factory , (5) quick local WebUI demo setup with Gradio , and (6) online web demo on server .
[LINK: llama.cpp](https://github.com/OpenBMB/llama.cpp/blob/minicpm-omni/examples/llava/README-minicpmo2.6.md)
[LINK: LLaMA-Factory](/openbmb/MiniCPM-o-2_6/blob/main/./docs/llamafactory_train.md)
Model Architecture.
- End-to-end Omni-modal Architecture. Different modality encoder/decoders are connected and trained in an end-to-end fashion to fully exploit rich multimodal knowledge.
- Omni-modal Live Streaming Mechanism. (1) We change the offline modality encoder/decoders into online ones for streaminig inputs/outputs. (2) We devise a time-division multiplexing (TDM) mechanism for omni-modality streaminig processing in the LLM backbone. It divides parallel omni-modality streams into sequential info within small periodic time slices.
- Configurable Speech Modeling Design. We devise a multimodal system prompt, including traditional text system prompt, and a new audio system prompt to determine the assistant voice . This enables flexible voice configurations in inference time, and also facilitates end-to-end voice cloning and description-based voice creation.

### Evaluation

Image Understanding:
+ Token Density: number of pixels encoded into each visual token at maximum resolution, i.e., # pixels at maximum resolution / # visual tokens.
Note: For proprietary models, we calculate token density based on the image encoding charging strategy defined in the official API documentation, which provides an upper-bound estimation.
Multi-image and Video Understanding:
Audio Understanding:
Speech Generation:
[LINK: UltraEval-Audio](https://github.com/OpenBMB/UltraEval-Audio)
End-to-end Voice Cloning
Multimodal Live Streaming: results on StreamingBench

### Examples

We deploy MiniCPM-o 2.6 on end devices. The demo video is the raw-speed recording on an iPad Pro and a Web demo.

## Online Demo

Click here to try the online demo of MiniCPM-o 2.6 .

## Usage

Inference using Huggingface transformers on NVIDIA GPUs. Please ensure that transformers==4.44.2 is installed, as other versions may have compatibility issues. We are investigating this issue. Requirements tested on python 3.10：

### Model initialization

If you are using an older version of PyTorch, you might encounter this issue "weight_norm_fwd_first_dim_kernel" not implemented for 'BFloat16' , Please convert the TTS to float32 type.

### Omni mode

We provide two inference modes: chat and streaming

### Speech and Audio Mode

Model initialization
Mimick task reflects a model's end-to-end speech modeling capability. The model takes audio input, and outputs an ASR transcription and subsequently reconstructs the original audio with high similarity. The higher the similarity between the reconstructed audio and the original audio, the stronger the model's foundational capability in end-to-end speech modeling.
A general usage scenario of MiniCPM-o-2.6 is role-playing a specific character based on the audio prompt. It will mimic the voice of the character to some extent and act like the character in text, including language style. In this mode, MiniCPM-o-2.6 sounds more natural and human-like . Self-defined audio prompts can be used to customize the voice of the character in an end-to-end manner.
An enhanced feature of MiniCPM-o-2.6 is to act as an AI assistant, but only with limited choice of voices. In this mode, MiniCPM-o-2.6 is less human-like and more like a voice assistant . In this mode, the model is more instruction-following. For demo, you are suggested to use assistant_female_voice , assistant_male_voice , and assistant_default_female_voice . Other voices may work but not as stable as the default voices.
Please note that, assistant_female_voice and assistant_male_voice are more stable but sounds like robots, while assistant_default_female_voice is more human-alike but not stable, its voice often changes in multiple turns. We suggest you to try stable voices assistant_female_voice and assistant_male_voice .
MiniCPM-o-2.6 can also do Instruction-to-Speech, aka Voice Creation . You can describe a voice in detail, and the model will generate a voice that matches the description. For more Instruction-to-Speech sample instructions, you can refer to https://voxinstruct.github.io/VoxInstruct/ .
[LINK: https://voxinstruct.github.io/VoxInstruct/](https://voxinstruct.github.io/VoxInstruct/)
MiniCPM-o-2.6 can also do zero-shot text-to-speech, aka Voice Cloning . With this mode, model will act like a TTS model.
MiniCPM-o-2.6 can also be used to address various audio understanding tasks, such as ASR, speaker analysis, general audio captioning, and sound scene tagging.
For audio-to-text tasks, you can use the following prompts:
- ASR with ZH(same as AST en2zh): 请仔细听这段音频片段，并将其内容逐字记录。
- ASR with EN(same as AST zh2en): Please listen to the audio snippet carefully and transcribe the content.
- Speaker Analysis: Based on the speaker's content, speculate on their gender, condition, age range, and health status.
- General Audio Caption: Summarize the main content of the audio.
- General Sound Scene Tagging: Utilize one keyword to convey the audio's content or the associated scene.

### Vision-Only mode

MiniCPM-o-2_6 has the same inference methods as MiniCPM-V-2_6
Please look at GitHub for more detail about usage.
[LINK: GitHub](https://github.com/OpenBMB/MiniCPM-o)

## Inference with llama.cpp

MiniCPM-o 2.6 (vision-only mode) can run with llama.cpp. See our fork of llama.cpp and readme for more detail.
[LINK: llama.cpp](https://github.com/OpenBMB/llama.cpp/tree/minicpm-omni)
[LINK: readme](https://github.com/OpenBMB/llama.cpp/blob/minicpm-omni/examples/llava/README-minicpmo2.6.md)

## Int4 quantized version

Download the int4 quantized version for lower GPU memory (7GB) usage: MiniCPM-o-2_6-int4 .

## License

- The MiniCPM-o/V model weights and code are open-sourced under the Apache-2.0 license.
[LINK: Apache-2.0](https://github.com/OpenBMB/MiniCPM-V/blob/main/LICENSE)
- To help us better understand and support our users, we would deeply appreciate it if you could consider optionally filling out a brief registration "questionnaire" .
- As an LMM, MiniCPM-o 2.6 generates contents by learning a large mount of multimodal corpora, but it cannot comprehend, express personal opinions or make value judgement. Anything generated by MiniCPM-o 2.6 does not represent the views and positions of the model developers
- We will not be liable for any problems arising from the use of the MinCPM-V models, including but not limited to data security issues, risk of public opinion, or any risks and problems arising from the misdirection, misuse, dissemination or misuse of the model.

## Key Techniques and Other Multimodal Projects

👏 Welcome to explore key techniques of MiniCPM-o 2.6 and other multimodal projects of our team:
VisCPM | RLHF-V | LLaVA-UHD | RLAIF-V
[LINK: VisCPM](https://github.com/OpenBMB/VisCPM/tree/main)
[LINK: RLHF-V](https://github.com/RLHF-V/RLHF-V)
[LINK: LLaVA-UHD](https://github.com/thunlp/LLaVA-UHD)
[LINK: RLAIF-V](https://github.com/RLHF-V/RLAIF-V)

## Citation

If you find our work helpful, please consider citing our papers 📝 and liking this project ❤️！
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for openbmb/MiniCPM-o-2_6

## Dataset used to train openbmb/MiniCPM-o-2_6

## Spaces using openbmb/MiniCPM-o-2_6 10

## Collections including openbmb/MiniCPM-o-2_6

## Papers for openbmb/MiniCPM-o-2_6


--------------------