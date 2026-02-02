# MiniCPM-V-2_6
**URL:** https://huggingface.co/openbmb/MiniCPM-V-2_6
**Page Title:** openbmb/MiniCPM-V-2_6 · Hugging Face
--------------------


## You need to agree to share your contact information to access this model

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
Log in or Sign Up to review the conditions and access this model content.

## A GPT-4V Level MLLM for Single Image, Multi Image and Video on Your Phone

GitHub | Demo
[LINK: GitHub](https://github.com/OpenBMB/MiniCPM-V)

## News

- [2025.01.14] 🔥🔥 We open source MiniCPM-o 2.6 , with significant performance improvement over MiniCPM-V 2.6 , and support real-time speech-to-speech conversation and multimodal live streaming. Try it now.

## MiniCPM-V 2.6

MiniCPM-V 2.6 is the latest and most capable model in the MiniCPM-V series. The model is built on SigLip-400M and Qwen2-7B with a total of 8B parameters. It exhibits a significant performance improvement over MiniCPM-Llama3-V 2.5, and introduces new features for multi-image and video understanding. Notable features of MiniCPM-V 2.6 include:
- 🔥 Leading Performance. MiniCPM-V 2.6 achieves an average score of 65.2 on the latest version of OpenCompass, a comprehensive evaluation over 8 popular benchmarks. With only 8B parameters, it surpasses widely used proprietary models like GPT-4o mini, GPT-4V, Gemini 1.5 Pro, and Claude 3.5 Sonnet for single image understanding.
🔥 Leading Performance. MiniCPM-V 2.6 achieves an average score of 65.2 on the latest version of OpenCompass, a comprehensive evaluation over 8 popular benchmarks. With only 8B parameters, it surpasses widely used proprietary models like GPT-4o mini, GPT-4V, Gemini 1.5 Pro, and Claude 3.5 Sonnet for single image understanding.
- 🖼️ Multi Image Understanding and In-context Learning. MiniCPM-V 2.6 can also perform conversation and reasoning over multiple images . It achieves state-of-the-art performance on popular multi-image benchmarks such as Mantis-Eval, BLINK, Mathverse mv and Sciverse mv, and also shows promising in-context learning capability.
🖼️ Multi Image Understanding and In-context Learning. MiniCPM-V 2.6 can also perform conversation and reasoning over multiple images . It achieves state-of-the-art performance on popular multi-image benchmarks such as Mantis-Eval, BLINK, Mathverse mv and Sciverse mv, and also shows promising in-context learning capability.
- 🎬 Video Understanding. MiniCPM-V 2.6 can also accept video inputs , performing conversation and providing dense captions for spatial-temporal information. It outperforms GPT-4V, Claude 3.5 Sonnet and LLaVA-NeXT-Video-34B on Video-MME with/without subtitles.
🎬 Video Understanding. MiniCPM-V 2.6 can also accept video inputs , performing conversation and providing dense captions for spatial-temporal information. It outperforms GPT-4V, Claude 3.5 Sonnet and LLaVA-NeXT-Video-34B on Video-MME with/without subtitles.
- 💪 Strong OCR Capability and Others. MiniCPM-V 2.6 can process images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344). It achieves state-of-the-art performance on OCRBench, surpassing proprietary models such as GPT-4o, GPT-4V, and Gemini 1.5 Pro .
Based on the the latest RLAIF-V and VisCPM techniques, it features trustworthy behaviors , with significantly lower hallucination rates than GPT-4o and GPT-4V on Object HalBench, and supports multilingual capabilities on English, Chinese, German, French, Italian, Korean, etc.
💪 Strong OCR Capability and Others. MiniCPM-V 2.6 can process images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344). It achieves state-of-the-art performance on OCRBench, surpassing proprietary models such as GPT-4o, GPT-4V, and Gemini 1.5 Pro .
Based on the the latest RLAIF-V and VisCPM techniques, it features trustworthy behaviors , with significantly lower hallucination rates than GPT-4o and GPT-4V on Object HalBench, and supports multilingual capabilities on English, Chinese, German, French, Italian, Korean, etc.
[LINK: RLAIF-V](https://github.com/RLHF-V/RLAIF-V/)
[LINK: VisCPM](https://github.com/OpenBMB/VisCPM)
- 🚀 Superior Efficiency. In addition to its friendly size, MiniCPM-V 2.6 also shows state-of-the-art token density (i.e., number of pixels encoded into each visual token). It produces only 640 tokens when processing a 1.8M pixel image, which is 75% fewer than most models . This directly improves the inference speed, first-token latency, memory usage, and power consumption. As a result, MiniCPM-V 2.6 can efficiently support real-time video understanding on end-side devices such as iPad.
🚀 Superior Efficiency. In addition to its friendly size, MiniCPM-V 2.6 also shows state-of-the-art token density (i.e., number of pixels encoded into each visual token). It produces only 640 tokens when processing a 1.8M pixel image, which is 75% fewer than most models . This directly improves the inference speed, first-token latency, memory usage, and power consumption. As a result, MiniCPM-V 2.6 can efficiently support real-time video understanding on end-side devices such as iPad.
- 💫 Easy Usage. MiniCPM-V 2.6 can be easily used in various ways: (1) llama.cpp and ollama support for efficient CPU inference on local devices, (2) int4 and GGUF format quantized models in 16 sizes, (3) vLLM support for high-throughput and memory-efficient inference, (4) fine-tuning on new domains and tasks, (5) quick local WebUI demo setup with Gradio and (6) online web demo .
💫 Easy Usage. MiniCPM-V 2.6 can be easily used in various ways: (1) llama.cpp and ollama support for efficient CPU inference on local devices, (2) int4 and GGUF format quantized models in 16 sizes, (3) vLLM support for high-throughput and memory-efficient inference, (4) fine-tuning on new domains and tasks, (5) quick local WebUI demo setup with Gradio and (6) online web demo .
[LINK: llama.cpp](https://github.com/OpenBMB/llama.cpp/blob/minicpmv-main/examples/llava/README-minicpmv2.6.md)
[LINK: ollama](https://github.com/OpenBMB/ollama/tree/minicpm-v2.6)
[LINK: vLLM](https://github.com/OpenBMB/MiniCPM-V/tree/main?tab=readme-ov-file#inference-with-vllm)
[LINK: Gradio](https://github.com/OpenBMB/MiniCPM-V/tree/main?tab=readme-ov-file#chat-with-our-demo-on-gradio)

### Evaluation

* We evaluate this benchmark using chain-of-thought prompting.
+ Token Density: number of pixels encoded into each visual token at maximum resolution, i.e., # pixels at maximum resolution / # visual tokens.
Note: For proprietary models, we calculate token density based on the image encoding charging strategy defined in the official API documentation, which provides an upper-bound estimation.
+ We evaluate the pretraining ckpt without SFT.

### Examples

We deploy MiniCPM-V 2.6 on end devices. The demo video is the raw screen recording on a iPad Pro without edition.

## Demo

Click here to try the Demo of MiniCPM-V 2.6 .

## Usage

Inference using Huggingface transformers on NVIDIA GPUs. Requirements tested on python 3.10：

### Chat with multiple images

### In-context few-shot learning

### Chat with video

Please look at GitHub for more detail about usage.
[LINK: GitHub](https://github.com/OpenBMB/MiniCPM-V)

## Inference with llama.cpp

MiniCPM-V 2.6 can run with llama.cpp. See our fork of llama.cpp for more detail.
[LINK: llama.cpp](https://github.com/OpenBMB/llama.cpp/tree/minicpm-v2.5/examples/minicpmv)

## Int4 quantized version

Download the int4 quantized version for lower GPU memory (7GB) usage: MiniCPM-V-2_6-int4 .

## License

- The code in this repo is released under the Apache-2.0 License.
[LINK: Apache-2.0](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE)
- The usage of MiniCPM-V series model weights must strictly follow MiniCPM Model License.md .
[LINK: MiniCPM Model License.md](https://github.com/OpenBMB/MiniCPM/blob/main/MiniCPM%20Model%20License.md)
- The models and weights of MiniCPM are completely free for academic research. After filling out a "questionnaire" for registration, MiniCPM-V 2.6 weights are also available for free commercial use.
- As an LMM, MiniCPM-V 2.6 generates contents by learning a large mount of multimodal corpora, but it cannot comprehend, express personal opinions or make value judgement. Anything generated by MiniCPM-V 2.6 does not represent the views and positions of the model developers
- We will not be liable for any problems arising from the use of the MinCPM-V models, including but not limited to data security issues, risk of public opinion, or any risks and problems arising from the misdirection, misuse, dissemination or misuse of the model.

## Key Techniques and Other Multimodal Projects

👏 Welcome to explore key techniques of MiniCPM-V 2.6 and other multimodal projects of our team:
VisCPM | RLHF-V | LLaVA-UHD | RLAIF-V
[LINK: VisCPM](https://github.com/OpenBMB/VisCPM/tree/main)
[LINK: RLHF-V](https://github.com/RLHF-V/RLHF-V)
[LINK: LLaVA-UHD](https://github.com/thunlp/LLaVA-UHD)
[LINK: RLAIF-V](https://github.com/RLHF-V/RLAIF-V)

## Citation

If you find our work helpful, please consider citing our papers 📝 and liking this project ❤️！

## Model tree for openbmb/MiniCPM-V-2_6

## Dataset used to train openbmb/MiniCPM-V-2_6

## Spaces using openbmb/MiniCPM-V-2_6 29

## Collections including openbmb/MiniCPM-V-2_6

## Paper for openbmb/MiniCPM-V-2_6


--------------------