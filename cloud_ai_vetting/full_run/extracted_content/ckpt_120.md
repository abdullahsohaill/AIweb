# ckpt
**URL:** https://huggingface.co/t5-11b
**Page Title:** google-t5/t5-11b · Hugging Face
--------------------


## Model Card for T5 11B

## Table of Contents

- Model Details
- Uses
- Bias, Risks, and Limitations
- Training Details
- Evaluation
- Environmental Impact
- Citation
- Model Card Authors
- How To Get Started With the Model

## Model Details

## Model Description

The developers of the Text-To-Text Transfer Transformer (T5) write :
With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the input and output are always text strings, in contrast to BERT-style models that can only output either a class label or a span of the input. Our text-to-text framework allows us to use the same model, loss function, and hyperparameters on any NLP task.
T5-11B is the checkpoint with 11 billion parameters.
- Developed by: Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu. See associated paper and GitHub repo
[LINK: GitHub repo](https://github.com/google-research/text-to-text-transfer-transformer#released-model-checkpoints)
- Model type: Language model
- Language(s) (NLP): English, French, Romanian, German
- License: Apache 2.0
- Related Models: All T5 Checkpoints
- Resources for more information: Research paper Google's T5 Blog Post GitHub Repo Hugging Face T5 Docs
- Research paper
- Google's T5 Blog Post
- GitHub Repo
[LINK: GitHub Repo](https://github.com/google-research/text-to-text-transfer-transformer)
- Hugging Face T5 Docs
[LINK: Hugging Face T5 Docs](https://huggingface.co/docs/transformers/model_doc/t5)

## Uses

## Direct Use and Downstream Use

The developers write in a blog post that the model:
Our text-to-text framework allows us to use the same model, loss function, and hyperparameters on any NLP task, including machine translation, document summarization, question answering, and classification tasks (e.g., sentiment analysis). We can even apply T5 to regression tasks by training it to predict the string representation of a number instead of the number itself.
See the blog post and research paper for further details.

## Out-of-Scope Use

More information needed.

## Bias, Risks, and Limitations

More information needed.

## Recommendations

More information needed.

## Training Details

## Training Data

The model is pre-trained on the Colossal Clean Crawled Corpus (C4) , which was developed and released in the context of the same research paper as T5.
The model was pre-trained on a on a multi-task mixture of unsupervised (1.) and supervised tasks (2.) .
Thereby, the following datasets were being used for (1.) and (2.):
- Datasets used for Unsupervised denoising objective :
- Wiki-DPR
- Datasets used for Supervised text-to-text language modeling objective
- Sentence acceptability judgment CoLA Warstadt et al., 2018
- CoLA Warstadt et al., 2018
- Sentiment analysis SST-2 Socher et al., 2013
- SST-2 Socher et al., 2013
- Paraphrasing/sentence similarity MRPC Dolan and Brockett, 2005 STS-B Ceret al., 2017 QQP Iyer et al., 2017
- MRPC Dolan and Brockett, 2005
- STS-B Ceret al., 2017
- QQP Iyer et al., 2017
- Natural language inference MNLI Williams et al., 2017 QNLI Rajpurkar et al.,2016 RTE Dagan et al., 2005 CB De Marneff et al., 2019
- MNLI Williams et al., 2017
- QNLI Rajpurkar et al.,2016
- RTE Dagan et al., 2005
- CB De Marneff et al., 2019
- Sentence completion COPA Roemmele et al., 2011
- COPA Roemmele et al., 2011
- Word sense disambiguation WIC Pilehvar and Camacho-Collados, 2018
- WIC Pilehvar and Camacho-Collados, 2018
- Question answering MultiRC Khashabi et al., 2018 ReCoRD Zhang et al., 2018 BoolQ Clark et al., 2019
- MultiRC Khashabi et al., 2018
- ReCoRD Zhang et al., 2018
- BoolQ Clark et al., 2019

## Training Procedure

In their abstract , the model developers write:
In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts every language problem into a text-to-text format. Our systematic study compares pre-training objectives, architectures, unlabeled datasets, transfer approaches, and other factors on dozens of language understanding tasks.
The framework introduced, the T5 framework, involves a training procedure that brings together the approaches studied in the paper. See the research paper for further details.

## Evaluation

## Testing Data, Factors & Metrics

The developers evaluated the model on 24 tasks, see the research paper for full details.

## Results

For full results for T5-11B, see the research paper , Table 14.

## Environmental Impact

Carbon emissions can be estimated using the Machine Learning Impact calculator presented in Lacoste et al. (2019) .
[LINK: Machine Learning Impact calculator](https://mlco2.github.io/impact#compute)
- Hardware Type: Google Cloud TPU Pods
- Hours used: More information needed
- Cloud Provider: GCP
- Compute Region: More information needed
- Carbon Emitted: More information needed

## Citation

BibTeX:
APA:
- Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., ... & Liu, P. J. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. J. Mach. Learn. Res., 21(140), 1-67.

## Model Card Authors

This model card was written by the team at Hugging Face.

## How to Get Started with the Model

## Disclaimer

Before transformers v3.5.0 , due do its immense size, t5-11b required some special treatment. 
If you're using transformers <= v3.4.0 , t5-11b should be loaded with flag use_cdn set to False as follows:
Secondly, a single GPU will most likely not have enough memory to even load the model into memory as the weights alone amount to over 40 GB.
- Model parallelism has to be used here to overcome this problem as is explained in this PR .
- DeepSpeed's ZeRO-Offload is another approach as explained in this post .
[LINK: post](https://github.com/huggingface/transformers/issues/9996)
See the Hugging Face T5 docs and a Colab Notebook created by the model developers for more context.
[LINK: Hugging Face T5](https://huggingface.co/docs/transformers/model_doc/t5#transformers.T5Model)
[LINK: Colab Notebook](https://colab.research.google.com/github/google-research/text-to-text-transfer-transformer/blob/main/notebooks/t5-trivia.ipynb)

## Model tree for google-t5/t5-11b

## Dataset used to train google-t5/t5-11b

## Spaces using google-t5/t5-11b 100

## Papers for google-t5/t5-11b


--------------------