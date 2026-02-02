# MedGemma-27B-Text
**URL:** https://huggingface.co/litert-community/MedGemma-27B-IT
**Page Title:** litert-community/MedGemma-27B-IT · Hugging Face
--------------------


## Access MedGemma on Hugging Face

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
To access MedGemma on Hugging Face, you're required to review and agree to Health AI Developer Foundation's terms of use . To do this, please ensure you're logged in to Hugging Face and click below. Requests are processed immediately.
[LINK: Health AI Developer Foundation's terms of use](https://developers.google.com/health-ai-developer-foundations/terms)
Log in or Sign Up to review the conditions and access this model content.

## litert-community/MedGemma-27B-IT

This model provides a few variants of google/medgemma-27b-text-it that are ready for
deployment on Web using the MediaPipe LLM Inference API .
[LINK: MediaPipe LLM Inference API](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference)

### Web

- Build and run our sample web app .
[LINK: sample web app](https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/llm_inference/js/README.md)
To add the model to your web app, please follow the instructions in our documentation .
[LINK: documentation](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference/web_js)

## Performance

### Web

Note that all benchmark stats are from a MacBook Pro 2024 (Apple M4 Max chip) with 1280 KV cache size, 1024 tokens prefill, and 256 tokens decode, running in Chrome.
F16
int8
GPU
167 tk/s
8 tk/s
14.9 s
27.0 GB
1.5 GB
27.05 GB
F32
int8
GPU
97 tk/s
8 tk/s
15.0 s
28.0 GB
1.5 GB
27.05 GB
- Model size: measured by the size of the .tflite flatbuffer (serialization format for LiteRT models).
- int8: quantized model with int8 weights and float activations.
- GPU memory: measured by "GPU Process" memory for all of Chrome while running. Chrome was measured as using 340-350MB before any model loading took place.
- CPU memory: measured for the entire tab while running. Tab was measured as using 60-70MB before any model loading took place.
[LINK: How to track](https://huggingface.co/docs/hub/models-download-stats)

## Model tree for litert-community/MedGemma-27B-IT

Base model

## Spaces using litert-community/MedGemma-27B-IT 3

## Collections including litert-community/MedGemma-27B-IT


--------------------