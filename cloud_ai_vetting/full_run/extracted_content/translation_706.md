# Translation
**URL:** https://huggingface.co/tasks/translation
**Page Title:** What is Translation? - Hugging Face
--------------------


## Translation

Translation is the task of converting text from one language to another.
My name is Omar and I live in Zürich.
Mein Name ist Omar und ich wohne in Zürich.

## About Translation

## Use Cases

You can find over a thousand Translation models on the Hub, but sometimes you might not find a model for the language pair you are interested in. When this happen, you can use a pretrained multilingual Translation model like mBART and further train it on your own data in a process called fine-tuning.

### Multilingual conversational agents

Translation models can be used to build conversational agents across different languages. This can be done in two ways.
- Translate the dataset to a new language. You can translate a dataset of intents (inputs) and responses to the target language. You can then train a new intent classification model with this new dataset. This allows you to proofread responses in the target language and have better control of the chatbot's outputs.
- Translate the input and output of the agent. You can use a Translation model in user inputs so that the chatbot can process it. You can then translate the output of the chatbot into the language of the user. This approach might be less reliable as the chatbot will generate responses that were not defined before.

## Inference

You can use the 🤗 Transformers library with the translation_xx_to_yy pattern where xx is the source language code and yy is the target language code. The default model for the pipeline is t5-base which under the hood adds a task prefix indicating the task itself, e.g. “translate: English to French”.
If you’d like to use a specific model checkpoint that is from one specific language to another, you can also directly use the translation pipeline.
You can use huggingface.js to infer translation models on Hugging Face Hub.
[LINK: huggingface.js](https://github.com/huggingface/huggingface.js)

## Useful Resources

Would you like to learn more about Translation? Great! Here you can find some curated resources that you may find helpful!
- Course Chapter on Translation

### Notebooks

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/notebooks/blob/master/examples/translation.ipynb)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/notebooks/blob/master/examples/translation-tf.ipynb)

### Scripts for training

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/transformers/tree/main/examples/pytorch/translation)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/transformers/tree/main/examples/tensorflow/translation)

### Documentation

- Translation task guide
[LINK: Translation task guide](https://huggingface.co/docs/transformers/tasks/translation)

## Compatible libraries

Note Very powerful model that can translate many languages between each other, especially low-resource languages.
Note A general-purpose Transformer that can be used to translate from English to German, French, or Romanian.
Note A dataset of copyright-free books translated into 16 different languages.
Note An example of translation between programming languages. This dataset consists of functions in Java and C#.
Note An application that can translate between 100 languages.
Note An application that can translate between many languages.

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
facebook/mbart-large-50-many-to-many-mmt is supported by the following Inference Providers:

--------------------