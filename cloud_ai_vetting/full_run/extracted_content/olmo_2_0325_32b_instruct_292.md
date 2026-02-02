# OLMo-2-0325-32B-Instruct
**URL:** https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct
**Page Title:** allenai/OLMo-2-0325-32B-Instruct · Hugging Face
--------------------

OLMo 2 32B Instruct March 2025 is post-trained variant of the OLMo-2 32B March 2025 model, which has undergone supervised finetuning on an OLMo-specific variant of the Tülu 3 dataset , further DPO training on this dataset , and final RLVR training on this dataset .
Tülu 3 is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval.
Check out the OLMo 2 paper or Tülu 3 paper for more details!
OLMo is a series of O pen L anguage Mo dels designed to enable the science of language models. 
These models are trained on the Dolma dataset. We are releasing all code, checkpoints, logs, and associated training details.

## Model description

- Model type: A model trained on a mix of publicly available, synthetic and human-created datasets.
- Language(s) (NLP): Primarily English
- License: Apache 2.0
- Finetuned from model: allenai/OLMo-2-0325-32B-DPO

### Model Sources

- Project Page: https://allenai.org/olmo
- Repositories: Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo-core Evaluation code: https://github.com/allenai/olmes Further fine-tuning code: https://github.com/allenai/open-instruct
- Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo-core
[LINK: https://github.com/allenai/OLMo-core](https://github.com/allenai/OLMo-core)
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

NOTE: This is different than previous OLMo 2 and Tülu 3 models due to a minor change in configuration. It does NOT have the bos token before the rest. Our other models have <|endoftext|> at the beginning of the chat template.
The chat template for our models is formatted as:
Or with new lines expanded:
It is embedded within the tokenizer as well, for tokenizer.apply_chat_template .

### System prompt

In Ai2 demos, we use this system prompt by default:
The model has not been trained with a specific system prompt in mind.

### Intermediate Checkpoints

To facilitate research on RL finetuning, we have released our intermediate checkpoints during the model's RLVR training.
The model weights are saved every 20 training steps, and can be accessible in the revisions of the HuggingFace repository.
For example, you can load with:

### Bias, Risks, and Limitations

The OLMo-2 models have limited safety training, but are not deployed automatically with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
See the Falcon 180B model card for an example of this.

## Performance

## Learning curves

Below is the training curves for allenai/OLMo-2-0325-32B-Instruct . The model was trained using 5 8xH100 nodes.
Below are the core eval scores over steps for allenai/OLMo-2-0325-32B-Instruct (note we took step 320 as the final checkpoint, corresponding to episode 573,440 ):
Below are the other eval scores over steps for allenai/OLMo-2-0325-32B-Instruct :

## Reproduction command

The command below is copied directly from the tracked training job:

## License and use

OLMo 2 is licensed under the Apache 2.0 license.
OLMo 2 is intended for research and educational use.
For more information, please see our Responsible Use Guidelines .
This model has been fine-tuned using a dataset mix with outputs generated from third party models and are subject to additional terms: Gemma Terms of Use .

## Citation

## Model tree for allenai/OLMo-2-0325-32B-Instruct

Base model

## Dataset used to train allenai/OLMo-2-0325-32B-Instruct

## Spaces using allenai/OLMo-2-0325-32B-Instruct 3

## Collection including allenai/OLMo-2-0325-32B-Instruct

## Papers for allenai/OLMo-2-0325-32B-Instruct


--------------------