# OLMo-2-1124-13B-Instruct
**URL:** https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct
**Page Title:** allenai/OLMo-2-1124-13B-Instruct · Hugging Face
--------------------


## OLMo-2-1124-13B-Instruct

## NOTE: 1/3/2025 UPDATE:

Upon the initial release of OLMo-2 models, we realized the post-trained models did not share the pre-tokenization logic that the base models use. As a result, we have trained new post-trained models. The new models are available under the same names as the original models, but we have made the old models available with a postfix "-preview". See OLMo 2 Preview Post-trained Models for the colleciton of the legacy models.

## Release Documentation

OLMo 2 13B Instruct November 2024 is post-trained variant of the OLMo-2 13B November 2024 model, which has undergone supervised finetuning on an OLMo-specific variant of the [Tülu 3 dataset]( https://huggingface.co/datasets/allenai/tulu-3-sft-olmo-2-mixture and further DPO training on this dataset , and finally RLVR training using this data .
Tülu 3 is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval.
Check out the OLMo 2 paper or Tülu 3 paper for more details!
OLMo is a series of O pen L anguage Mo dels designed to enable the science of language models. 
These models are trained on the Dolma dataset. We are releasing all code, checkpoints, logs (coming soon), and associated training details. 
The core models released in this batch include the following:

## Model description

- Model type: A model trained on a mix of publicly available, synthetic and human-created datasets.
- Language(s) (NLP): Primarily English
- License: Apache 2.0
- Finetuned from model: allenai/OLMo-2-13B-1124-RLVR2

### Model Sources

- Project Page: https://allenai.org/olmo
- Repositories: Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo Evaluation code: https://github.com/allenai/olmes Further fine-tuning code: https://github.com/allenai/open-instruct
- Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo
[LINK: https://github.com/allenai/OLMo](https://github.com/allenai/OLMo)
- Evaluation code: https://github.com/allenai/olmes
[LINK: https://github.com/allenai/olmes](https://github.com/allenai/olmes)
- Further fine-tuning code: https://github.com/allenai/open-instruct
[LINK: https://github.com/allenai/open-instruct](https://github.com/allenai/open-instruct)
- Paper: https://arxiv.org/abs/2501.00656
- Demo: https://playground.allenai.org/

## Installation

OLMo 2 will be supported in the next version of Transformers, and you need to install it from the main branch using:

## Using the model

### Loading with HuggingFace

To load the model with HuggingFace, use the following snippet:

### Chat template

The chat template for our models is formatted as:
Or with new lines expanded:
It is embedded within the tokenizer as well, for tokenizer.apply_chat_template .

### System prompt

In Ai2 demos, we use this system prompt by default:
The model has not been trained with a specific system prompt in mind.

### Bias, Risks, and Limitations

The OLMo-2 models have limited safety training, but are not deployed automatically with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
See the Falcon 180B model card for an example of this.

## Performance

## License and use

OLMo 2 is licensed under the Apache 2.0 license.
OLMo 2 is intended for research and educational use.
For more information, please see our Responsible Use Guidelines .
This model has been fine-tuned using a dataset mix with outputs generated from third party models and are subject to additional terms: Gemma Terms of Use .

## Citation

## Model tree for allenai/OLMo-2-1124-13B-Instruct

Base model

## Dataset used to train allenai/OLMo-2-1124-13B-Instruct

## Spaces using allenai/OLMo-2-1124-13B-Instruct 10

## Collection including allenai/OLMo-2-1124-13B-Instruct

## Papers for allenai/OLMo-2-1124-13B-Instruct


--------------------