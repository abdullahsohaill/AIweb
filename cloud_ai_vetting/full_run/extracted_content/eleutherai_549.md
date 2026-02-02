# EleutherAI
**URL:** https://huggingface.co/EleutherAI/gpt-neox-20b
**Page Title:** EleutherAI/gpt-neox-20b · Hugging Face
--------------------

GPT-NeoX-20B is a 20 billion parameter autoregressive language model trained 
on the Pile using the GPT-NeoX 
library . Its architecture intentionally 
resembles that of GPT-3, and is almost identical to that of GPT-J-
6B . Its training dataset contains 
a multitude of English-language texts, reflecting the general-purpose nature 
of this model. See the accompanying paper for details about model architecture (including how it differs from GPT-3), 
training procedure, and additional evaluations.
[LINK: GPT-NeoX 
library](https://github.com/EleutherAI/gpt-neox)

### Model details

- Developed by: EleutherAI
- Model type: Transformer-based Language Model
- Language: English
- Learn more: GPT-NeoX-20B: An Open-Source Autoregressive Language 
Model . For details about the training dataset, 
see the Pile paper , and its data
sheet .
- License: Apache 2.0
- Contact: to ask questions about this model, join the EleutherAI 
Discord , and post them in #release-discussion . 
Please read the existing GPT-NeoX-20B documentation before asking about the model 
on Discord. For general correspondence: contact@eleuther.
ai .

### Uses and limitations

GPT-NeoX-20B was developed primarily for research purposes. It learns an inner 
representation of the English language that can be used to extract features 
useful for downstream tasks.
In addition to scientific uses, you may also further fine-tune and adapt 
GPT-NeoX-20B for deployment, as long as your use is in accordance with the 
Apache 2.0 license. This model works with the Transformers 
Library . If you decide to use 
pre-trained GPT-NeoX-20B as a basis for your fine-tuned model, please note that 
you need to conduct your own risk and bias assessment.
[LINK: Transformers 
Library](https://huggingface.co/docs/transformers/index)
GPT-NeoX-20B is not intended for deployment as-is. It is not a product 
and cannot be used for human-facing interactions without supervision.
GPT-NeoX-20B has not been fine-tuned for downstream tasks for which language 
models are commonly deployed, such as writing genre prose, or commercial 
chatbots. This means GPT-NeoX-20B will likely not respond to a given prompt 
the way products such as ChatGPT do. This is because, unlike GPT-NeoX-20B, 
ChatGPT was fine-tuned using methods such as Reinforcement Learning from Human 
Feedback (RLHF) to better “understand” human instructions and dialogue.
This model is English-language only, and thus cannot be used for translation
or generating text in other languages.
The core functionality of GPT-NeoX-20B is to take a string of text and predict 
the next token. Remember that the statistically most likely next token need 
not result in the most “accurate” text. Never rely on GPT-NeoX-20B to produce 
factually accurate output.
This model was trained on the Pile , a dataset 
known to contain profanity and texts that are lewd or otherwise offensive. 
See Section 6 of the Pile paper for a 
discussion of documented biases with regards to gender, religion, and race. 
GPT-NeoX-20B may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.
We recommend curating the outputs of this model before presenting it to a human 
reader. Please inform your audience that you are using artificially generated 
text.
If you simply want to try out some prompts, check out this 
 playground .
GPT-NeoX-20B can be loaded using the AutoModelForCausalLM functionality:

### Training

The Pile is a 825GiB general-purpose dataset in English. It was created by 
EleutherAI specifically for training large language models. It contains texts 
from 22 diverse sources, roughly broken down into five categories: academic 
writing (e.g. arXiv), internet (e.g. CommonCrawl), prose (e.g. Project 
Gutenberg), dialogue (e.g. YouTube subtitles), and miscellaneous (e.g. GitHub, 
Enron Emails). See the Pile paper for 
a breakdown of all data sources, methodology, and a discussion of ethical 
implications. Consult the datasheet for 
more detailed documentation about the Pile and its component datasets. The 
Pile can be downloaded from the official website , 
or from a community mirror .
The Pile was not deduplicated before being used to train GPT-NeoX-20B.
GPT-NeoX-20B was trained with a batch size of approximately 3.15M tokens 
(1538 sequences of 2048 tokens each), for a total of 150,000 steps. Tensor 
parallelism and pipeline parallelism were used to distribute the model across 
GPUs. Additional details about the training procedure are in Section 3 of 
the accompanying paper .

### Evaluations

This is a heavily abridged version of the evaluation results. Appendix D of the GPT-NeoX-20B paper compares more model 
sizes, and contains additional evaluations, including on: zero and five-shot 
natural language tasks, zero and five-shot Basic Arithmetic and MATH, 
and zero-shot Hendrycks tasks.

### BibTeX

To cite the GPT-NeoX-20B paper:

## Open LLM Leaderboard Evaluation Results

Detailed results can be found here

## Model tree for EleutherAI/gpt-neox-20b

## Dataset used to train EleutherAI/gpt-neox-20b

## Spaces using EleutherAI/gpt-neox-20b 100

## Papers for EleutherAI/gpt-neox-20b


--------------------