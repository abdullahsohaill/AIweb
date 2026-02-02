# Summarisation
**URL:** https://huggingface.co/tasks/summarization
**Page Title:** What is Summarization? - Hugging Face
--------------------


## Summarization

Summarization is the task of producing a shorter version of a document while preserving its important information. Some models can extract text from the original input, while other models can generate entirely new text.
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. It was the first structure to reach a height of 300 metres. Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. It was the first structure to reach a height of 300 metres.

## About Summarization

## Use Cases

### Research Paper Summarization 🧐

Research papers can be summarized to allow researchers to spend less time selecting which articles to read. There are several approaches you can take for a task like this:
- Use an existing extractive summarization model on the Hub to do inference.
- Pick an existing language model trained for academic papers. This model can then be trained in a process called fine-tuning so it can solve the summarization task.
- Use a sequence-to-sequence model like T5 for abstractive text summarization.

## Inference

You can use the 🤗 Transformers library summarization pipeline to infer with existing Summarization models. If no model name is provided the pipeline will be initialized with sshleifer/distilbart-cnn-12-6 .
You can use huggingface.js to infer summarization models on Hugging Face Hub.
[LINK: huggingface.js](https://github.com/huggingface/huggingface.js)

## Useful Resources

Would you like to learn more about the topic? Awesome! Here you can find some curated resources that you may find helpful!
- Course Chapter on Summarization
- Distributed Training: Train BART/T5 for Summarization using 🤗 Transformers and Amazon SageMaker

### Notebooks

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/notebooks/blob/master/examples/summarization.ipynb)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/notebooks/blob/master/examples/summarization-tf.ipynb)

### Scripts for training

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/transformers/tree/main/examples/pytorch/summarization)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/transformers/tree/main/examples/tensorflow/summarization)
- Flax
[LINK: Flax](https://github.com/huggingface/transformers/tree/main/examples/flax/summarization)

### Documentation

- Summarization task guide
[LINK: Summarization task guide](https://huggingface.co/docs/transformers/tasks/summarization)

## Compatible libraries

Note A strong summarization model trained on English news articles. Excels at generating factual summaries.
Note A summarization model trained on medical articles.
No example dataset is defined for this task.
Note Contribute by proposing a dataset for this task !
Note An application that can summarize long paragraphs.
Note A much needed summarization application for terms and conditions.
Note An application that summarizes long documents.
Note An application that can detect errors in abstractive summarization.

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
facebook/bart-large-cnn is supported by the following Inference Providers:

--------------------