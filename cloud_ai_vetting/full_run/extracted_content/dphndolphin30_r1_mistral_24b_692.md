# dphn/Dolphin3.0-R1-Mistral-24B
**URL:** https://huggingface.co/dphn/Dolphin3.0-R1-Mistral-24B
**Page Title:** dphn/Dolphin3.0-R1-Mistral-24B · Hugging Face
--------------------


## Dolphin 3.0 R1 Mistral 24B 🐬

Part of the Dolphin 3.0 Collection
Curated and trained by Eric Hartford , Ben Gitter , BlouseJury and Cognitive Computations
Discord: https://discord.gg/cognitivecomputations

## Sponsors

Our appreciation for the generous sponsors of Dolphin 3.0:
- Dria https://x.com/driaforall - Inference Sponsor
- Chutes https://x.com/rayon_labs - Compute Sponsor
- Crusoe Cloud - Compute Sponsor
- Andreessen Horowitz - provided the grant that originally launched Dolphin

## What is Dolphin?

Dolphin 3.0 R1 is the next generation of the Dolphin series of instruct-tuned models.  Designed to be the ultimate general purpose local model, enabling coding, math, agentic, function calling, and general use cases.
The R1 version has been trained for 3 epochs to reason using 800k reasoning traces from the Dolphin-R1 dataset.
Dolphin aims to be a general purpose reasoning instruct model, similar to the models behind ChatGPT, Claude, Gemini.  But these models present problems for businesses seeking to include AI in their products.
- They maintain control of the system prompt, deprecating and changing things as they wish, often causing software to break.
- They maintain control of the model versions, sometimes changing things silently, or deprecating older models that your business relies on.
- They maintain control of the alignment, and in particular the alignment is one-size-fits all, not tailored to the application.
- They can see all your queries and they can potentially use that data in ways you wouldn't want.
Dolphin, in contrast, is steerable and gives control to the system owner. You set the system prompt.  You decide the alignment.  You have control of your data.  Dolphin does not impose its ethics or guidelines on you.  You are the one who decides the guidelines.
Dolphin belongs to YOU, it is your tool, an extension of your will.
Just as you are personally responsible for what you do with a knife, gun, fire, car, or the internet, you are the creator and originator of any content you generate with Dolphin.
https://erichartford.com/uncensored-models

## Recommended Temperature

Experimentally we note that Mistral-24B based models require a low temperature.  We have seen much better results in the range of 0.05 to 0.1.
With Dolphin2.0-R1 a too-high temperature can result in behaviors like second guessing and talking itself out of correct answers.

## Quants

https://huggingface.co/bartowski/cognitivecomputations_Dolphin3.0-R1-Mistral-24B-GGUF

## Run Dolphin in Ollama (13 GB)

## Chat Template

We use ChatML for the chat template.

## System Prompt

In Dolphin, the system prompt is what you use to set the tone and alignment of the responses.  You can set a character, a mood, rules for its behavior, and it will try its best to follow them.
Make sure to set the system prompt in order to set the tone and guidelines for the responses - Otherwise, it will act in a default way that might not be what you want.
Example use of system prompt:
Here is a recommended reasoning system prompt:
You are Dolphin, a lovable yet intelligent AI assistant created by Eric Hartford and his open source AI research collective, Cognitive Computations.
Your primary directive is to provide well-reasoned, structured, correct, unbiased, and detailed responses.
You value freedom, enabling the user, and complying with the user's requests.
Formatting Requirements:
- The <think></think> section is your scratch space for your internal thought process - it is not shared with the user.
- If the answer requires minimal thought, the <think></think> block may be left empty.
- Keep your thoughts concise, don't overthink. The user is waiting for your answer.
- If you notice yourself engaging in circular reasoning or repetition, immediately terminate your thinking with a </think> and proceed to address the user.
- You may say </think> when you like (which will end your thinking process) - but do not ever say <think>.
Response Guidelines:
- Detailed and Structured: Use markdown, json, mermaid, latex math notation, etc. when appropriate.
- Scientific and Logical Approach: Your explanations should reflect the depth and precision of the greatest scientific minds.
- Concise yet Complete: Ensure responses are informative, yet to the point without unnecessary elaboration.
- Maintain a professional yet friendly and lovable, intelligent, and analytical tone in all interactions.

## Sample Outputs

TBD

## How to use

There are many ways to use a huggingface model including:
- ollama
- LM Studio
- Huggingface Transformers library
- vllm
- sglang
- tgi

## Evals

TBD

## Appreciation

Respect and thanks to the creators of the open source datasets that were used:
- OpenCoder-LLM (opc-sft-stage1, opc-sft-stage2)
- microsoft (orca-agentinstruct-1M-v1, orca-math-word-problems-200k)
- NousResearch (hermes-function-calling-v1)
- AI-MO (NuminaMath-CoT, NuminaMath-TIR)
- allenai (tulu-3-sft-mixture)
- HuggingFaceTB (smoltalk)
- m-a-p (CodeFeedback-Filtered-Instruction, Code-Feedback)
Special thanks to
- Meta, Qwen, and OpenCoder, who wrote papers and published models that were instrumental in creating Dolphin 3.0.
- RLHFlow for the excellent reward model used to filter the datasets
- Deepseek, for the ridiculously fast Deepseek-V3 that we used to augment the data.

## Model tree for dphn/Dolphin3.0-R1-Mistral-24B

Base model

## Datasets used to train dphn/Dolphin3.0-R1-Mistral-24B

## Spaces using dphn/Dolphin3.0-R1-Mistral-24B 15


--------------------