# Voxtral-Small-24B-2507
**URL:** https://huggingface.co/mistralai/Voxtral-Small-24B-2507
**Page Title:** mistralai/Voxtral-Small-24B-2507 · Hugging Face
--------------------


## Voxtral Small 1.0 (24B) - 2507

Voxtral Small is an enhancement of Mistral Small 3 , incorporating state-of-the-art audio input capabilities while retaining best-in-class text performance. It excels at speech transcription, translation and audio understanding.
Learn more about Voxtral in our blog post here and our research paper .

## Key Features

Voxtral builds upon Mistral Small 3 with powerful audio understanding capabilities.
- Dedicated transcription mode : Voxtral can operate in a pure speech transcription mode to maximize performance. By default, Voxtral automatically predicts the source audio language and transcribes the text accordingly
- Long-form context : With a 32k token context length, Voxtral handles audios up to 30 minutes for transcription, or 40 minutes for understanding
- Built-in Q&A and summarization : Supports asking questions directly through audio. Analyze audio and generate structured summaries without the need for separate ASR and language models
- Natively multilingual : Automatic language detection and state-of-the-art performance in the world’s most widely used languages (English, Spanish, French, Portuguese, Hindi, German, Dutch, Italian)
- Function-calling straight from voice : Enables direct triggering of backend functions, workflows, or API calls based on spoken user intents
- Highly capable at text : Retains the text understanding capabilities of its language model backbone, Mistral Small 3.1

## Benchmark Results

### Audio

Average word error rate (WER) over the FLEURS, Mozilla Common Voice and Multilingual LibriSpeech benchmarks:

### Text

## Usage

The model can be used with the following frameworks;
- vllm (recommended) : See here
[LINK: vllm (recommended)](https://github.com/vllm-project/vllm)
- Transformers 🤗 : See here
[LINK: Transformers 🤗](https://github.com/huggingface/transformers)
Notes :
- temperature=0.2 and top_p=0.95 for chat completion ( e.g. Audio Understanding ) and temperature=0.0 for transcription
- Multiple audios per message and multiple user turns with audio are supported
- Function calling is supported
- System prompts are not yet supported

### vLLM (recommended)

We recommend using this model with vLLM .
[LINK: vLLM](https://github.com/vllm-project/vllm)
Make sure to install vllm >= 0.10.0 , we recommend using uv
Doing so should automatically install mistral_common >= 1.8.1 .
[LINK: mistral_common >= 1.8.1](https://github.com/mistralai/mistral-common/releases/tag/v1.8.1)
To check:
You can test that your vLLM setup works as expected by cloning the vLLM repo:
and then running:
We recommend that you use Voxtral-Small-24B-2507 in a server/client setting.
- Spin up a server:
Note: Running Voxtral-Small-24B-2507 on GPU requires ~55 GB of GPU RAM in bf16 or fp16.
- To ping the client you can use a simple Python snippet. See the following examples.

### Audio Instruct

Leverage the audio capabilities of Voxtral-Small-24B-2507 to chat.
Make sure that your client has mistral-common with audio installed:
Voxtral-Small-24B-2507 has powerful transcription capabilities!
Make sure that your client has mistral-common with audio installed:
Voxtral has some experimental function calling support. You can try as shown below.
Make sure that your client has mistral-common with audio installed:

### Transformers 🤗

Starting with transformers >= 4.54.0 and above, you can run Voxtral natively!
Install Transformers:
Make sure to have mistral-common >= 1.8.1 installed with audio dependencies:
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for mistralai/Voxtral-Small-24B-2507

Base model

## Spaces using mistralai/Voxtral-Small-24B-2507 10

## Paper for mistralai/Voxtral-Small-24B-2507


--------------------