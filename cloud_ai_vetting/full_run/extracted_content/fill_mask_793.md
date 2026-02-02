# Fill-Mask
**URL:** https://huggingface.co/tasks/fill-mask
**Page Title:** What is Fill-Mask? - Hugging Face
--------------------


## Fill-Mask

Masked language modeling is the task of masking some of the words in a sentence and predicting which words should replace those masks. These models are useful when we want to get a statistical understanding of the language in which the model is trained in.
The <mask> barked at me

## About Fill-Mask

## Use Cases

### Domain Adaptation 👩‍⚕️

Masked language models do not require labelled data! They are trained by masking a couple of words in sentences and the model is expected to guess the masked word. This makes it very practical!
For example, masked language modeling is used to train large models for domain-specific problems. If you have to work on a domain-specific task, such as retrieving information from medical research papers, you can train a masked language model using those papers. 📄
The resulting model has a statistical understanding of the language used in medical research papers, and can be further trained in a process called fine-tuning to solve different tasks, such as Text Classification or Question Answering to build a medical research papers information extraction system. 👩‍⚕️ Pre-training on domain-specific data tends to yield better results (see this paper for an example).
If you don't have the data to train a masked language model, you can also use an existing domain-specific masked language model from the Hub and fine-tune it with your smaller task dataset. That's the magic of Open Source and sharing your work! 🎉

## Inference with Fill-Mask Pipeline

You can use the 🤗 Transformers library fill-mask pipeline to do inference with masked language models. If a model name is not provided, the pipeline will be initialized with distilroberta-base . You can provide masked text and it will return a list of possible mask values ​​ranked according to the score.

## Useful Resources

Would you like to learn more about the topic? Awesome! Here you can find some curated resources that can be helpful to you!
- Course Chapter on Fine-tuning a Masked Language Model
- Workshop on Pretraining Language Models and CodeParrot
- BERT 101: State Of The Art NLP Model Explained
- Nyströmformer: Approximating self-attention in linear time and memory via the Nyström method

### Notebooks

- Pre-training an MLM for JAX/Flax
[LINK: Pre-training an MLM for JAX/Flax](https://github.com/huggingface/notebooks/blob/master/examples/masked_language_modeling_flax.ipynb)
- Masked language modeling in TensorFlow
[LINK: Masked language modeling in TensorFlow](https://github.com/huggingface/notebooks/blob/master/examples/language_modeling-tf.ipynb)
- Masked language modeling in PyTorch
[LINK: Masked language modeling in PyTorch](https://github.com/huggingface/notebooks/blob/master/examples/language_modeling.ipynb)

### Scripts for training

- PyTorch
[LINK: PyTorch](https://github.com/huggingface/transformers/tree/main/examples/pytorch/language-modeling)
- Flax
[LINK: Flax](https://github.com/huggingface/transformers/tree/main/examples/flax/language-modeling)
- TensorFlow
[LINK: TensorFlow](https://github.com/huggingface/transformers/tree/main/examples/tensorflow/language-modeling)

### Documentation

- Masked language modeling task guide
[LINK: Masked language modeling task guide](https://huggingface.co/docs/transformers/tasks/masked_language_modeling)

## Compatible libraries

No example widget is defined for this task.
Note Contribute by proposing a widget for this task !
Note State-of-the-art masked language model.
Note A multilingual model trained on 100 languages.
No example dataset is defined for this task.
Note Contribute by proposing a dataset for this task !
No example Space is defined for this task.
Note Contribute by proposing a Space for this task !

--------------------