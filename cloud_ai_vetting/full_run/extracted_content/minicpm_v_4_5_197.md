# MiniCPM-V-4_5
**URL:** https://huggingface.co/openbmb/MiniCPM-V-4_5
**Page Title:** openbmb/MiniCPM-V-4_5 · Hugging Face
--------------------


## A GPT-4o Level MLLM for Single Image, Multi Image and High-FPS Video Understanding on Your Phone

GitHub | CookBook | Technical Report | Demo
[LINK: GitHub](https://github.com/OpenBMB/MiniCPM-o)
[LINK: CookBook](https://github.com/OpenSQZ/MiniCPM-V-CookBook)

## MiniCPM-V 4.5

MiniCPM-V 4.5 is the latest and most capable model in the MiniCPM-V series. The model is built on Qwen3-8B and SigLIP2-400M with a total of 8B parameters. It exhibits a significant performance improvement over previous MiniCPM-V and MiniCPM-o models, and introduces new useful features. Notable features of MiniCPM-V 4.5 include:
- 🔥 State-of-the-art Vision-Language Capability. MiniCPM-V 4.5 achieves an average score of 77.0 on OpenCompass, a comprehensive evaluation of 8 popular benchmarks. With only 8B parameters, it surpasses widely used proprietary models like GPT-4o-latest, Gemini-2.0 Pro, and strong open-source models like Qwen2.5-VL 72B for vision-language capabilities, making it the most performant MLLM under 30B parameters.
🔥 State-of-the-art Vision-Language Capability. MiniCPM-V 4.5 achieves an average score of 77.0 on OpenCompass, a comprehensive evaluation of 8 popular benchmarks. With only 8B parameters, it surpasses widely used proprietary models like GPT-4o-latest, Gemini-2.0 Pro, and strong open-source models like Qwen2.5-VL 72B for vision-language capabilities, making it the most performant MLLM under 30B parameters.
- 🎬 Efficient High-FPS and Long Video Understanding. Powered by a new unified 3D-Resampler over images and videos, MiniCPM-V 4.5 can now achieve 96x compression rate for video tokens, where 6 448x448 video frames can be jointly compressed into 64 video tokens (normally 1,536 tokens for most MLLMs). This means that the model can perceive significantly more video frames without increasing the LLM inference cost. This brings state-of-the-art high-FPS (up to 10FPS) video understanding and long video understanding capabilities on Video-MME, LVBench, MLVU, MotionBench, FavorBench, etc., efficiently.
🎬 Efficient High-FPS and Long Video Understanding. Powered by a new unified 3D-Resampler over images and videos, MiniCPM-V 4.5 can now achieve 96x compression rate for video tokens, where 6 448x448 video frames can be jointly compressed into 64 video tokens (normally 1,536 tokens for most MLLMs). This means that the model can perceive significantly more video frames without increasing the LLM inference cost. This brings state-of-the-art high-FPS (up to 10FPS) video understanding and long video understanding capabilities on Video-MME, LVBench, MLVU, MotionBench, FavorBench, etc., efficiently.
- ⚙️ Controllable Hybrid Fast/Deep Thinking. MiniCPM-V 4.5 supports both fast thinking for efficient frequent usage with competitive performance, and deep thinking for more complex problem solving. To cover efficiency and performance trade-offs in different user scenarios, this fast/deep thinking mode can be switched in a highly controlled fashion.
⚙️ Controllable Hybrid Fast/Deep Thinking. MiniCPM-V 4.5 supports both fast thinking for efficient frequent usage with competitive performance, and deep thinking for more complex problem solving. To cover efficiency and performance trade-offs in different user scenarios, this fast/deep thinking mode can be switched in a highly controlled fashion.
- 💪 Strong OCR, Document Parsing and Others. Based on LLaVA-UHD architecture, MiniCPM-V 4.5 can process high-resolution images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344), using 4x less visual tokens than most MLLMs. The model achieves leading performance on OCRBench, surpassing proprietary models such as GPT-4o-latest and Gemini 2.5 . It also achieves state-of-the-art performance for PDF document parsing capability on OmniDocBench among general MLLMs. Based on the latest RLAIF-V and VisCPM techniques, it features trustworthy behaviors , outperforming GPT-4o-latest on MMHal-Bench, and supports multilingual capabilities in more than 30 languages.
💪 Strong OCR, Document Parsing and Others. Based on LLaVA-UHD architecture, MiniCPM-V 4.5 can process high-resolution images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344), using 4x less visual tokens than most MLLMs. The model achieves leading performance on OCRBench, surpassing proprietary models such as GPT-4o-latest and Gemini 2.5 . It also achieves state-of-the-art performance for PDF document parsing capability on OmniDocBench among general MLLMs. Based on the latest RLAIF-V and VisCPM techniques, it features trustworthy behaviors , outperforming GPT-4o-latest on MMHal-Bench, and supports multilingual capabilities in more than 30 languages.
[LINK: RLAIF-V](https://github.com/RLHF-V/RLAIF-V/)
[LINK: VisCPM](https://github.com/OpenBMB/VisCPM)
- 💫 Easy Usage. MiniCPM-V 4.5 can be easily used in various ways: (1) llama.cpp and ollama support for efficient CPU inference on local devices, (2) int4 , GGUF and AWQ format quantized models in 16 sizes, (3) SGLang and vLLM support for high-throughput and memory-efficient inference, (4) fine-tuning on new domains and tasks with Transformers and LLaMA-Factory , (5) quick local WebUI demo , (6) optimized local iOS app on iPhone and iPad, and (7) online web demo on server . See our Cookbook for full usages!
💫 Easy Usage. MiniCPM-V 4.5 can be easily used in various ways: (1) llama.cpp and ollama support for efficient CPU inference on local devices, (2) int4 , GGUF and AWQ format quantized models in 16 sizes, (3) SGLang and vLLM support for high-throughput and memory-efficient inference, (4) fine-tuning on new domains and tasks with Transformers and LLaMA-Factory , (5) quick local WebUI demo , (6) optimized local iOS app on iPhone and iPad, and (7) online web demo on server . See our Cookbook for full usages!
[LINK: llama.cpp](https://github.com/tc-mb/llama.cpp/blob/Support-MiniCPM-V-4.5/docs/multimodal/minicpmv4.5.md)
[LINK: ollama](https://github.com/tc-mb/ollama/tree/MIniCPM-V)
[LINK: AWQ](https://github.com/tc-mb/AutoAWQ)
[LINK: SGLang](https://github.com/tc-mb/sglang/tree/main)
[LINK: Transformers](https://github.com/tc-mb/transformers/tree/main)
[LINK: LLaMA-Factory](/openbmb/MiniCPM-V-4_5/blob/main/./docs/llamafactory_train_and_infer.md)
[LINK: local iOS app](https://github.com/tc-mb/MiniCPM-o-demo-iOS)
[LINK: Cookbook](https://github.com/OpenSQZ/MiniCPM-V-CookBook)

### Key Techniques

- Architechture: Unified 3D-Resampler for High-density Video Compression. MiniCPM-V 4.5 introduces a 3D-Resampler that overcomes the performance-efficiency trade-off in video understanding. By grouping and jointly compressing up to 6 consecutive video frames into just 64 tokens (the same token count used for a single image in MiniCPM-V series), MiniCPM-V 4.5 achieves a 96× compression rate for video tokens. This allows the model to process more video frames without additional LLM computational cost, enabling high-FPS video and long video understanding. The architecture supports unified encoding for images, multi-image inputs, and videos, ensuring seamless capability and knowledge transfer.
Architechture: Unified 3D-Resampler for High-density Video Compression. MiniCPM-V 4.5 introduces a 3D-Resampler that overcomes the performance-efficiency trade-off in video understanding. By grouping and jointly compressing up to 6 consecutive video frames into just 64 tokens (the same token count used for a single image in MiniCPM-V series), MiniCPM-V 4.5 achieves a 96× compression rate for video tokens. This allows the model to process more video frames without additional LLM computational cost, enabling high-FPS video and long video understanding. The architecture supports unified encoding for images, multi-image inputs, and videos, ensuring seamless capability and knowledge transfer.
- Pre-training: Unified Learning for OCR and Knowledge from Documents. Existing MLLMs learn OCR capability and knowledge from documents in isolated training approaches. We observe that the essential difference between these two training approaches is the visibility of the text in images. By dynamically corrupting text regions in documents with varying noise levels and asking the model to reconstruct the text, the model learns to adaptively and properly switch between accurate text recognition (when text is visible) and multimodal context-based knowledge reasoning (when text is heavily obscured). This eliminates reliance on error-prone document parsers in knowledge learning from documents, and prevents hallucinations from over-augmented OCR data, resulting in top-tier OCR and multimodal knowledge performance with minimal engineering overhead.
Pre-training: Unified Learning for OCR and Knowledge from Documents. Existing MLLMs learn OCR capability and knowledge from documents in isolated training approaches. We observe that the essential difference between these two training approaches is the visibility of the text in images. By dynamically corrupting text regions in documents with varying noise levels and asking the model to reconstruct the text, the model learns to adaptively and properly switch between accurate text recognition (when text is visible) and multimodal context-based knowledge reasoning (when text is heavily obscured). This eliminates reliance on error-prone document parsers in knowledge learning from documents, and prevents hallucinations from over-augmented OCR data, resulting in top-tier OCR and multimodal knowledge performance with minimal engineering overhead.
- Post-training: Hybrid Fast/Deep Thinking with Multimodal RL. MiniCPM-V 4.5 offers a balanced reasoning experience through two switchable modes: fast thinking for efficient daily use and deep thinking for complex tasks. Using a new hybrid reinforcement learning method, the model jointly optimizes both modes, significantly enhancing fast-mode performance without compromising deep-mode capability. Incorporated with RLPR and RLAIF-V , it generalizes robust reasoning skills from broad multimodal data while effectively reducing hallucinations.
Post-training: Hybrid Fast/Deep Thinking with Multimodal RL. MiniCPM-V 4.5 offers a balanced reasoning experience through two switchable modes: fast thinking for efficient daily use and deep thinking for complex tasks. Using a new hybrid reinforcement learning method, the model jointly optimizes both modes, significantly enhancing fast-mode performance without compromising deep-mode capability. Incorporated with RLPR and RLAIF-V , it generalizes robust reasoning skills from broad multimodal data while effectively reducing hallucinations.
[LINK: RLPR](https://github.com/OpenBMB/RLPR)
[LINK: RLAIF-V](https://github.com/RLHF-V/RLAIF-V)

### Evaluation

### Inference Efficiency

OpenCompass
Video-MME
Both Video-MME and OpenCompass were evaluated using 8×A100 GPUs for inference. The reported inference time of Video-MME includes full model-side computation, and excludes the external cost of video frame extraction (dependent on specific frame extraction tools) for fair comparison.

### Examples

We deploy MiniCPM-V 4.5 on iPad M4 with iOS demo . The demo video is the raw screen recording without editing.
[LINK: iOS demo](https://github.com/tc-mb/MiniCPM-o-demo-iOS)

## Framework Support Matrix

[LINK: Llama.cpp Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/deployment/llama.cpp/minicpm-v4_5_llamacpp.md)
[LINK: #15575](https://github.com/ggml-org/llama.cpp/pull/15575)
[LINK: b6282](https://github.com/ggml-org/llama.cpp/releases/tag/b6282)
[LINK: Ollama Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/deployment/ollama/minicpm-v4_5_ollama.md)
[LINK: #12078](https://github.com/ollama/ollama/pull/12078)
[LINK: vLLM Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/deployment/vllm/minicpm-v4_5_vllm.md)
[LINK: #23586](https://github.com/vllm-project/vllm/pull/23586)
[LINK: v0.10.2](https://github.com/vllm-project/vllm/releases/tag/v0.10.2)
[LINK: SGLang Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/deployment/sglang/MiniCPM-v4_5_sglang.md)
[LINK: #9610](https://github.com/sgl-project/sglang/pull/9610)
[LINK: LLaMA-Factory Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/finetune/finetune_llamafactory.md)
[LINK: #9022](https://github.com/hiyouga/LLaMA-Factory/pull/9022)
[LINK: GGUF Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/quantization/gguf/minicpm-v4_5_gguf_quantize.md)
[LINK: BNB Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/quantization/bnb/minicpm-v4_5_bnb_quantize.md)
[LINK: AWQ Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/quantization/awq/minicpm-v4_5_awq_quantize.md)
[LINK: Gradio Demo Doc](https://github.com/OpenSQZ/MiniCPM-V-CookBook/blob/main/demo/web_demo/gradio/README.md)
Note: If you'd like us to prioritize support for another open-source framework, please let us know via this short form .
[LINK: short form](https://docs.google.com/forms/d/e/1FAIpQLSdyTUrOPBgWqPexs3ORrg47ZcZ1r4vFQaA4ve2iA7L9sMfMWw/viewform)

## Usage

If you wish to enable thinking mode, provide the argument enable_thinking=True to the chat function.
You will get the following output:

## License

- The MiniCPM-o/V model weights and code are open-sourced under the Apache-2.0 license.
[LINK: Apache-2.0](https://github.com/OpenBMB/MiniCPM-V/blob/main/LICENSE)
- To help us better understand and support our users, we would deeply appreciate it if you could consider optionally filling out a brief registration "questionnaire" .
- As an LMM, MiniCPM-V 4.5 generates contents by learning a large amount of multimodal corpora, but it cannot comprehend, express personal opinions or make value judgement. Anything generated by MiniCPM-V 4.5 does not represent the views and positions of the model developers
- We will not be liable for any problems arising from the use of the MinCPM-V models, including but not limited to data security issues, risk of public opinion, or any risks and problems arising from the misdirection, misuse, dissemination or misuse of the model.

## Key Techniques and Other Multimodal Projects

👏 Welcome to explore key techniques of MiniCPM-V 4.5 and other multimodal projects of our team:
VisCPM | RLPR | RLHF-V | LLaVA-UHD | RLAIF-V
[LINK: VisCPM](https://github.com/OpenBMB/VisCPM/tree/main)
[LINK: RLPR](https://github.com/OpenBMB/RLPR)
[LINK: RLHF-V](https://github.com/RLHF-V/RLHF-V)
[LINK: LLaVA-UHD](https://github.com/thunlp/LLaVA-UHD)
[LINK: RLAIF-V](https://github.com/RLHF-V/RLAIF-V)

## Citation

If you find our work helpful, please consider citing our papers 📝 and liking this project ❤️！

## Model tree for openbmb/MiniCPM-V-4_5

## Dataset used to train openbmb/MiniCPM-V-4_5

## Spaces using openbmb/MiniCPM-V-4_5 16

## Collection including openbmb/MiniCPM-V-4_5

## Papers for openbmb/MiniCPM-V-4_5


--------------------