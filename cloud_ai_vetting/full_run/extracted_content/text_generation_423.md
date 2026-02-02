# Text Generation
**URL:** https://huggingface.co/tasks/text-generation
**Page Title:** What is Text Generation? - Hugging Face
--------------------


## Text Generation

Generating text is the task of generating new text given another text. These models can, for example, fill in incomplete text or paraphrase.
Once upon a time,
Once upon a time, we knew that our ancestors were on the verge of extinction. The great explorers and poets of the Old World, from Alexander the Great to Chaucer, are dead and gone. A good many of our ancient explorers and poets have

## About Text Generation

This task covers guides on both text-generation and text-to-text generation models. Popular large language models that are used for chats or following instructions are also covered in this task. You can find the list of selected open-source large language models here , ranked by their performance scores.

## Use Cases

### Instruction Models

A model trained for text generation can be later adapted to follow instructions. You can try some of the most powerful instruction-tuned open-access models like Mixtral 8x7B, Cohere Command R+, and Meta Llama3 70B at Hugging Chat .

### Code Generation

A Text Generation model, also known as a causal language model, can be trained on code from scratch to help the programmers in their repetitive coding tasks. One of the most popular open-source models for code generation is StarCoder, which can generate code in 80+ languages. You can try it here .

### Stories Generation

A story generation model can receive an input like "Once upon a time" and proceed to create a story-like text based on those first words. You can try this application which contains a model trained on story generation, by MosaicML.
If your generative model training data is different than your use case, you can train a causal language model from scratch. Learn how to do it in the free transformers course !

## Task Variants

### Completion Generation Models

A popular variant of Text Generation models predicts the next word given a bunch of words. Word by word a longer text is formed that results in for example:
- Given an incomplete sentence, complete it.
- Continue a story given the first sentences.
- Provided a code description, generate the code.
The most popular models for this task are GPT-based models, Mistral or Llama series . These models are trained on data that has no labels, so you just need plain text to train your own model. You can train text generation models to generate a wide variety of documents, from code to stories.

### Text-to-Text Generation Models

These models are trained to learn the mapping between a pair of texts (e.g. translation from one language to another). The most popular variants of these models are NLLB , FLAN-T5 , and BART . Text-to-Text models are trained with multi-tasking capabilities, they can accomplish a wide range of tasks, including summarization, translation, and text classification.
[LINK: BART](https://huggingface.co/docs/transformers/model_doc/bart)

## Language Model Variants

When it comes to text generation, the underlying language model can come in several types:
- Base models: refers to plain language models like Mistral 7B and Meta Llama-3-70b . These models are good for fine-tuning and few-shot prompting.
Base models: refers to plain language models like Mistral 7B and Meta Llama-3-70b . These models are good for fine-tuning and few-shot prompting.
- Instruction-trained models: these models are trained in a multi-task manner to follow a broad range of instructions like "Write me a recipe for chocolate cake". Models like Qwen 2 7B , Yi 1.5 34B Chat , and Meta Llama 70B Instruct are examples of instruction-trained models. In general, instruction-trained models will produce better responses to instructions than base models.
Instruction-trained models: these models are trained in a multi-task manner to follow a broad range of instructions like "Write me a recipe for chocolate cake". Models like Qwen 2 7B , Yi 1.5 34B Chat , and Meta Llama 70B Instruct are examples of instruction-trained models. In general, instruction-trained models will produce better responses to instructions than base models.
- Human feedback models: these models extend base and instruction-trained models by incorporating human feedback that rates the quality of the generated text according to criteria like helpfulness, honesty, and harmlessness . The human feedback is then combined with an optimization technique like reinforcement learning to align the original model to be closer with human preferences. The overall methodology is often called Reinforcement Learning from Human Feedback , or RLHF for short. Zephyr ORPO 141B A35B is an open-source model aligned through human feedback.
Human feedback models: these models extend base and instruction-trained models by incorporating human feedback that rates the quality of the generated text according to criteria like helpfulness, honesty, and harmlessness . The human feedback is then combined with an optimization technique like reinforcement learning to align the original model to be closer with human preferences. The overall methodology is often called Reinforcement Learning from Human Feedback , or RLHF for short. Zephyr ORPO 141B A35B is an open-source model aligned through human feedback.

## Text Generation from Image and Text

There are language models that can input both text and image and output text, called vision language models. IDEFICS 2 and MiniCPM Llama3 V are good examples. They accept the same generation parameters as other language models. However, since they also take images as input, you have to use them with the image-to-text pipeline. You can find more information about this in the image-to-text task page .

## Inference

You can use the 🤗 Transformers library text-generation pipeline to do inference with Text Generation models. It takes an incomplete text and returns multiple outputs with which the text can be completed.
Text-to-Text generation models have a separate pipeline called text2text-generation . This pipeline takes an input containing the sentence including the task and returns the output of the accomplished task.
You can use huggingface.js to infer text classification models on Hugging Face Hub.
[LINK: huggingface.js](https://github.com/huggingface/huggingface.js)

## Text Generation Inference

Text Generation Inference (TGI) is an open-source toolkit for serving LLMs tackling challenges such as response time. TGI powers inference solutions like Inference Endpoints and Hugging Chat , as well as multiple community projects. You can use it to deploy any supported open-source large language model of your choice.
[LINK: Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference)

## ChatUI Spaces

Hugging Face Spaces includes templates to easily deploy your own instance of a specific application. ChatUI is an open-source interface that enables serving conversational interface for large language models and can be deployed with few clicks at Spaces. TGI powers these Spaces under the hood for faster inference. Thanks to the template, you can deploy your own instance based on a large language model with only a few clicks and customize it. Learn more about it here and create your large language model instance here .
[LINK: ChatUI](https://github.com/huggingface/chat-ui)
[LINK: here](https://huggingface.co/docs/hub/spaces-sdks-docker-chatui)

## Useful Resources

Would you like to learn more about the topic? Awesome! Here you can find some curated resources that you may find helpful!

### Tools within Hugging Face Ecosystem

- You can use PEFT to adapt large language models in efficient way.
[LINK: PEFT](https://github.com/huggingface/peft)
- ChatUI is the open-source interface to conversate with Large Language Models.
[LINK: ChatUI](https://github.com/huggingface/chat-ui)
- text-generation-inference
[LINK: text-generation-inference](https://github.com/huggingface/text-generation-inference)
- HuggingChat is a chat interface powered by Hugging Face to chat with powerful models like Meta Llama 3 70B, Mixtral 8x7B, etc.

### Documentation

- PEFT documentation
[LINK: PEFT documentation](https://huggingface.co/docs/peft/index)
- ChatUI Docker Spaces
[LINK: ChatUI Docker Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker-chatui)
- Causal language modeling task guide
[LINK: Causal language modeling task guide](https://huggingface.co/docs/transformers/tasks/language_modeling)
- Text generation strategies
[LINK: Text generation strategies](https://huggingface.co/docs/transformers/generation_strategies)
- Course chapter on training a causal language model from scratch

### Model Inference & Deployment

- Optimizing your LLM in production
- Open-Source Text Generation & LLM Ecosystem at Hugging Face
- Introducing RWKV - An RNN with the advantages of a transformer
- Llama 2 is at Hugging Face
- Guiding Text Generation with Constrained Beam Search in 🤗 Transformers
- Code generation with Hugging Face
- Assisted Generation: a new direction toward low-latency text generation
- How to generate text: using different decoding methods for language generation with Transformers
- Faster Text Generation with TensorFlow and XLA

### Model Fine-tuning/Training

- Non-engineers guide: Train a LLaMA 2 chatbot
- Training CodeParrot 🦜 from Scratch
- Creating a Coding Assistant with StarCoder

### Advanced Concepts Explained Simply

- Mixture of Experts Explained

### Advanced Fine-tuning/Training Recipes

- Fine-tuning Llama 2 70B using PyTorch FSDP
- The N Implementation Details of RLHF with PPO
- Preference Tuning LLMs with Direct Preference Optimization Methods
- Fine-tune Llama 2 with DPO

### Notebooks

- Training a CLM in Flax
[LINK: Training a CLM in Flax](https://github.com/huggingface/notebooks/blob/master/examples/causal_language_modeling_flax.ipynb)
- Training a CLM in TensorFlow
[LINK: Training a CLM in TensorFlow](https://github.com/huggingface/notebooks/blob/master/examples/language_modeling_from_scratch-tf.ipynb)
- Training a CLM in PyTorch
[LINK: Training a CLM in PyTorch](https://github.com/huggingface/notebooks/blob/master/examples/language_modeling_from_scratch.ipynb)

### Scripts for training

- Training a CLM in PyTorch
[LINK: Training a CLM in PyTorch](https://github.com/huggingface/transformers/tree/main/examples/pytorch/language-modeling)
- Training a CLM in TensorFlow
[LINK: Training a CLM in TensorFlow](https://github.com/huggingface/transformers/tree/main/examples/tensorflow/language-modeling)
- Text Generation in PyTorch
[LINK: Text Generation in PyTorch](https://github.com/huggingface/transformers/tree/main/examples/pytorch/text-generation)

## Compatible libraries

No example widget is defined for this task.
Note Contribute by proposing a widget for this task !
Note A text-generation model trained to follow instructions.
Note Powerful text generation model for coding.
Note Great text generation model with top-notch tool calling capabilities.
Note Powerful text generation model.
Note A powerful small model with reasoning capabilities.
Note Strong conversational model that supports very long instructions.
Note Text generation model used to write code.
Note Powerful reasoning based open large language model.
Note High quality multilingual data used to train text-generation models.
Note Truly open-source, curated and cleaned dialogue dataset.
Note A reasoning dataset.
Note A multilingual instruction dataset with preference ratings on responses.
Note A large synthetic dataset for alignment of text generation models.
Note A dataset made for training text generation models solving math questions.
Note An application that writes and executes code from text instructions and supports many models.
Note An application that builds websites from natural language prompts.
Note A leaderboard for comparing chain-of-thought performance of models.
Note An text generation based application based on a very powerful LLaMA2 model.
Note An text generation based application to converse with Zephyr model.
Note An chatbot to converse with a very powerful text generation model.

--------------------