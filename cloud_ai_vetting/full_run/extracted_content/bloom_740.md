# BLOOM
**URL:** https://huggingface.co/bigscience/bloom
**Page Title:** bigscience/bloom · Hugging Face
--------------------

BigScience Large Open-science Open-access Multilingual Language Model Version 1.3 / 6 July 2022
Current Checkpoint: Training Iteration  95000
Link to paper: here
Total seen tokens: 366B

## Model Details

BLOOM is an autoregressive Large Language Model (LLM), trained to continue text from a prompt on vast amounts of text data using industrial-scale computational resources. As such, it is able to output coherent text in 46 languages and 13 programming languages that is hardly distinguishable from text written by humans. BLOOM can also be instructed to perform text tasks it hasn't been explicitly trained for, by casting them as text generation tasks.

## Basics

This section provides information about the model type, version, license, funders, release date, developers, and contact information. It is useful for anyone who wants to reference the model.
Developed by: BigScience ( website )
All collaborators are either volunteers or have an agreement with their employer. (Further breakdown of participants forthcoming.)
Model Type: Transformer-based Language Model
Checkpoints format: transformers (Megatron-DeepSpeed format available here )
Version: 1.0.0
Languages: Multiple; see training data
License: RAIL License v1.0 ( link / article and FAQ )
Release Date Estimate: Monday, 11.July.2022
Send Questions to: bigscience-contact@googlegroups.com
Cite as: BigScience, BigScience Language Open-science Open-access Multilingual (BLOOM) Language Model . International, May 2021-May 2022
Funded by:
- The French government.
The French government.
- Hugging Face ( website ).
Hugging Face ( website ).
- Organizations of contributors. (Further breakdown of organizations forthcoming.)
Organizations of contributors. (Further breakdown of organizations forthcoming.)

## Technical Specifications

This section includes details about the model objective and architecture, and the compute infrastructure. It is useful for people interested in model development.
Please see the BLOOM training README for full details on replicating training.
[LINK: the BLOOM training README](https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml#readme)

### Model Architecture and Objective

- Modified from Megatron-LM GPT2 (see paper , BLOOM Megatron code ):
Modified from Megatron-LM GPT2 (see paper , BLOOM Megatron code ):
[LINK: BLOOM Megatron code](https://github.com/bigscience-workshop/Megatron-DeepSpeed)
- Decoder-only architecture
Decoder-only architecture
- Layer normalization applied to word embeddings layer ( StableEmbedding ; see code , paper )
Layer normalization applied to word embeddings layer ( StableEmbedding ; see code , paper )
[LINK: code](https://github.com/facebookresearch/bitsandbytes)
- ALiBI positional encodings (see paper ), with GeLU activation functions
ALiBI positional encodings (see paper ), with GeLU activation functions
- 176,247,271,424 parameters: 3,596,615,680 embedding parameters 70 layers, 112 attention heads Hidden layers are 14336-dimensional Sequence length of 2048 tokens used (see BLOOM tokenizer , tokenizer description )
176,247,271,424 parameters:
- 3,596,615,680 embedding parameters
3,596,615,680 embedding parameters
- 70 layers, 112 attention heads
70 layers, 112 attention heads
- Hidden layers are 14336-dimensional
Hidden layers are 14336-dimensional
- Sequence length of 2048 tokens used (see BLOOM tokenizer , tokenizer description )
Sequence length of 2048 tokens used (see BLOOM tokenizer , tokenizer description )
Objective Function: Cross Entropy with mean reduction (see API documentation ).
[LINK: API documentation](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss)

### Compute infrastructure

Jean Zay Public Supercomputer, provided by the French government (see announcement ).
- 384 A100 80GB GPUs (48 nodes)
384 A100 80GB GPUs (48 nodes)
- Additional 32 A100 80GB GPUs (4 nodes) in reserve
Additional 32 A100 80GB GPUs (4 nodes) in reserve
- 8 GPUs per node Using NVLink 4 inter-gpu connects, 4 OmniPath links
8 GPUs per node Using NVLink 4 inter-gpu connects, 4 OmniPath links
- CPU: AMD
CPU: AMD
- CPU memory: 512GB per node
CPU memory: 512GB per node
- GPU memory: 640GB per node
GPU memory: 640GB per node
- Inter-node connect: Omni-Path Architecture (OPA)
Inter-node connect: Omni-Path Architecture (OPA)
- NCCL-communications network: a fully dedicated subnet
NCCL-communications network: a fully dedicated subnet
- Disc IO network: shared network with other types of nodes
Disc IO network: shared network with other types of nodes
- Megatron-DeepSpeed ( Github link )
Megatron-DeepSpeed ( Github link )
[LINK: Github link](https://github.com/bigscience-workshop/Megatron-DeepSpeed)
- DeepSpeed ( Github link )
DeepSpeed ( Github link )
[LINK: Github link](https://github.com/microsoft/DeepSpeed)
- PyTorch (pytorch-1.11 w/ CUDA-11.5; see Github link )
PyTorch (pytorch-1.11 w/ CUDA-11.5; see Github link )
[LINK: Github link](https://github.com/pytorch/pytorch)
- apex ( Github link )
apex ( Github link )
[LINK: Github link](https://github.com/NVIDIA/apex)

## Training

This section provides information about the training data, the speed and size of training elements, and the environmental impact of training. It is useful for people who want to learn more about the model inputs and training footprint.

## Training Data

This section provides a high-level overview of the training data. It is relevant for anyone who wants to know the basics of what the model is learning.
Details for each dataset are provided in individual Data Cards , and the sizes of each of their contributions to the aggregated training data are presented in an Interactive Corpus Map .
Training data includes:
- 46 natural languages
46 natural languages
- 13 programming languages
13 programming languages
- In 1.6TB of pre-processed text, converted into 350B unique tokens (see the tokenizer section for more.)
In 1.6TB of pre-processed text, converted into 350B unique tokens (see the tokenizer section for more.)

### Languages

The pie chart shows the distribution of languages in training data.
The following tables shows the further distribution of Niger-Congo & Indic languages and programming languages in the training data.
Distribution of Niger Congo and Indic languages.
Distribution of programming languages.

### Preprocessing

Tokenization: The BLOOM tokenizer ( link ), a learned subword tokenizer trained using:
- A byte-level Byte Pair Encoding (BPE) algorithm
A byte-level Byte Pair Encoding (BPE) algorithm
- A simple pre-tokenization rule, no normalization
A simple pre-tokenization rule, no normalization
- A vocabulary size of 250,680
A vocabulary size of 250,680
It was trained on a subset of a preliminary version of the corpus using alpha-weighting per language.

## Speeds, Sizes, Times

Training logs: Tensorboard link
- Dates: Started 11th March, 2022 11:42am PST Estimated end: 5th July, 2022
Dates:
- Started 11th March, 2022 11:42am PST
Started 11th March, 2022 11:42am PST
- Estimated end: 5th July, 2022
Estimated end: 5th July, 2022
- Checkpoint size: Bf16 weights: 329GB Full checkpoint with optimizer states: 2.3TB
Checkpoint size:
- Bf16 weights: 329GB
Bf16 weights: 329GB
- Full checkpoint with optimizer states: 2.3TB
Full checkpoint with optimizer states: 2.3TB
- Training throughput: About 150 TFLOP per GPU per second
Training throughput: About 150 TFLOP per GPU per second
- Number of epochs: 1
Number of epochs: 1
- Estimated cost of training: Equivalent of $2-5M in cloud computing (including preliminary experiments)
Estimated cost of training: Equivalent of $2-5M in cloud computing (including preliminary experiments)
- Server training location: Île-de-France, France
Server training location: Île-de-France, France

## Environmental Impact

The training supercomputer, Jean Zay ( website ), uses mostly nuclear energy. The heat generated by it is reused for heating campus housing.
Estimated carbon emissions: (Forthcoming.)
Estimated electricity usage: (Forthcoming.)

## Uses

This section addresses questions around how the model is intended to be used, discusses the foreseeable users of the model (including those affected by the model), and describes uses that are considered out of scope or misuse of the model. It is useful for anyone considering using the model or who is affected by the model.

## How to use

This model can be easily used and deployed using HuggingFace's ecosystem. This needs transformers and accelerate installed. The model can be downloaded as follows:

## Intended Use

This model is being created in order to enable public research on large language models (LLMs). LLMs are intended to be used for language generation or as a pretrained base model that can be further fine-tuned for specific tasks. Use cases below are not exhaustive.

### Direct Use

- Text generation
Text generation
- Exploring characteristics of language generated by a language model Examples: Cloze tests, counterfactuals, generations with reframings
Exploring characteristics of language generated by a language model
- Examples: Cloze tests, counterfactuals, generations with reframings

### Downstream Use

- Tasks that leverage language models include: Information Extraction, Question Answering, Summarization

### Misuse and Out-of-scope Use

This section addresses what users ought not do with the model.
See the BLOOM License , Attachment A, for detailed usage restrictions. The below list is non-exhaustive, but lists some easily foreseeable problematic use cases.
Using the model in high-stakes settings is out of scope for this model.  The model is not designed for critical decisions nor uses with any material consequences on an individual's livelihood or wellbeing. The model outputs content that appears factual but may not be correct.
Out-of-scope Uses Include:
- Usage in biomedical domains, political and legal domains, or finance domains
Usage in biomedical domains, political and legal domains, or finance domains
- Usage for evaluating or scoring individuals, such as for employment, education, or credit
Usage for evaluating or scoring individuals, such as for employment, education, or credit
- Applying the model for critical automatic decisions, generating factual content, creating reliable summaries, or generating predictions that must be correct
Applying the model for critical automatic decisions, generating factual content, creating reliable summaries, or generating predictions that must be correct
Intentionally using the model for harm, violating human rights , or other kinds of malicious activities, is a misuse of this model. This includes:
- Spam generation
Spam generation
- Disinformation and influence operations
Disinformation and influence operations
- Disparagement and defamation
Disparagement and defamation
- Harassment and abuse
Harassment and abuse
- Deception
Deception
- Unconsented impersonation and imitation
Unconsented impersonation and imitation
- Unconsented surveillance
Unconsented surveillance
- Generating content without attribution to the model, as specified in the RAIL License, Use Restrictions
Generating content without attribution to the model, as specified in the RAIL License, Use Restrictions

## Intended Users

### Direct Users

- General Public
General Public
- Researchers
Researchers
- Students
Students
- Educators
Educators
- Engineers/developers
Engineers/developers
- Non-commercial entities
Non-commercial entities
- Community advocates, including human and civil rights groups
Community advocates, including human and civil rights groups

### Indirect Users

- Users of derivatives created by Direct Users, such as those using software with an intended use
Users of derivatives created by Direct Users, such as those using software with an intended use
- Users of Derivatives of the Model, as described in the License
Users of Derivatives of the Model, as described in the License

### Others Affected (Parties Prenantes)

- People and groups referred to by the LLM
People and groups referred to by the LLM
- People and groups exposed to outputs of, or decisions based on, the LLM
People and groups exposed to outputs of, or decisions based on, the LLM
- People and groups whose original work is included in the LLM
People and groups whose original work is included in the LLM

## Risks and Limitations

This section identifies foreseeable harms and misunderstandings.
Model may:
- Overrepresent some viewpoints and underrepresent others
Overrepresent some viewpoints and underrepresent others
- Contain stereotypes
Contain stereotypes
- Contain personal information
Contain personal information
- Generate: Hateful, abusive, or violent language Discriminatory or prejudicial language Content that may not be appropriate for all settings, including sexual content
Generate:
- Hateful, abusive, or violent language
Hateful, abusive, or violent language
- Discriminatory or prejudicial language
Discriminatory or prejudicial language
- Content that may not be appropriate for all settings, including sexual content
Content that may not be appropriate for all settings, including sexual content
- Make errors, including producing incorrect information as if it were factual
Make errors, including producing incorrect information as if it were factual
- Generate irrelevant or repetitive outputs
Generate irrelevant or repetitive outputs
- Induce users into attributing human traits to it, such as sentience or consciousness
Induce users into attributing human traits to it, such as sentience or consciousness

## Evaluation

This section describes the evaluation protocols and provides the results.

## Metrics

This section describes the different ways performance is calculated and why.
Includes:
And multiple different metrics for specific tasks. (More evaluation metrics forthcoming upon completion of evaluation protocol.)

## Factors

This section lists some different aspects of BLOOM models. Its focus is on aspects that are likely to give rise to high variance in model behavior.
- Language, such as English or Yoruba
Language, such as English or Yoruba
- Domain, such as newswire or stories
Domain, such as newswire or stories
- Demographic characteristics, such as gender or nationality
Demographic characteristics, such as gender or nationality

## Results

Results are based on the Factors and Metrics .
Zero-shot evaluations:
WARNING: This section used to contain much more results, however they were not correct and we released without the approval of the evaluation working group. We are currently in the process of fixing the evaluations.
See this repository for JSON files: https://github.com/bigscience-workshop/evaluation-results
[LINK: https://github.com/bigscience-workshop/evaluation-results](https://github.com/bigscience-workshop/evaluation-results)
Train-time Evaluation:
Final checkpoint after 95K steps:
- Training Loss: 1.939
Training Loss: 1.939
- Validation Loss: 2.061
Validation Loss: 2.061
- Perplexity: 7.045
Perplexity: 7.045
For more see: https://huggingface.co/bigscience/tr11-176B-ml-logs

## Recommendations

This section provides information on warnings and potential mitigations.
- Indirect users should be made aware when the content they're working with is created by the LLM.
Indirect users should be made aware when the content they're working with is created by the LLM.
- Users should be aware of Risks and Limitations , and include an appropriate age disclaimer or blocking interface as necessary.
Users should be aware of Risks and Limitations , and include an appropriate age disclaimer or blocking interface as necessary.
- Models trained or finetuned downstream of BLOOM LM should include an updated Model Card.
Models trained or finetuned downstream of BLOOM LM should include an updated Model Card.
- Users of the model should provide mechanisms for those affected to provide feedback, such as an email address for comments.
Users of the model should provide mechanisms for those affected to provide feedback, such as an email address for comments.

## Glossary and Calculations

This section defines common terms and how metrics are calculated.
- Loss: A calculation of the difference between what the model has learned and what the data shows ("groundtruth"). The lower the loss, the better. The training process aims to minimize the loss.
Loss: A calculation of the difference between what the model has learned and what the data shows ("groundtruth"). The lower the loss, the better. The training process aims to minimize the loss.
- Perplexity: This is based on what the model estimates the probability of new data is. The lower the perplexity, the better.  If the model is 100% correct at predicting the next token it will see, then the perplexity is 1. Mathematically this is calculated using entropy.
Perplexity: This is based on what the model estimates the probability of new data is. The lower the perplexity, the better.  If the model is 100% correct at predicting the next token it will see, then the perplexity is 1. Mathematically this is calculated using entropy.
- High-stakes settings: Such as those identified as "high-risk AI systems" and "unacceptable risk AI systems" in the European Union's proposed Artificial Intelligence (AI) Act .
High-stakes settings: Such as those identified as "high-risk AI systems" and "unacceptable risk AI systems" in the European Union's proposed Artificial Intelligence (AI) Act .
- Critical decisions: Such as those defined in the United States' proposed Algorithmic Accountability Act .
Critical decisions: Such as those defined in the United States' proposed Algorithmic Accountability Act .
- Human rights: Includes those rights defined in the Universal Declaration of Human Rights .
Human rights: Includes those rights defined in the Universal Declaration of Human Rights .
- Personal Data and Personal Information: Personal data and information is defined in multiple data protection regulations, such as " personal data " in the European Union's General Data Protection Regulation ; and "personal information" in the Republic of South Africa's Protection of Personal Information Act , The People's Republic of China's Personal information protection law .
Personal Data and Personal Information: Personal data and information is defined in multiple data protection regulations, such as " personal data " in the European Union's General Data Protection Regulation ; and "personal information" in the Republic of South Africa's Protection of Personal Information Act , The People's Republic of China's Personal information protection law .
- Sensitive characteristics: This includes specifically protected categories in human rights (see UHDR, Article 2 ) and personal information regulation (see GDPR, Article 9; Protection of Personal Information Act, Chapter 1 )
Sensitive characteristics: This includes specifically protected categories in human rights (see UHDR, Article 2 ) and personal information regulation (see GDPR, Article 9; Protection of Personal Information Act, Chapter 1 )
- Deception: Doing something to intentionally mislead individuals to believe something that is false, such as by creating deadbots or chatbots on social media posing as real people, or generating text documents without making consumers aware that the text is machine generated.
Deception: Doing something to intentionally mislead individuals to believe something that is false, such as by creating deadbots or chatbots on social media posing as real people, or generating text documents without making consumers aware that the text is machine generated.

## More Information

This section provides links to writing on dataset creation, technical specifications, lessons learned, and initial results.

## Intermediate checkpoints

For academic (or any) usage, we published the intermediate checkpoints, corresponding to the model state at each 5000 steps. Please follow this link to get these checkpoints.

## Dataset Creation

Blog post detailing the design choices during the dataset creation: https://bigscience.huggingface.co/blog/building-a-tb-scale-multilingual-dataset-for-language-modeling

## Technical Specifications

Blog post summarizing how the architecture, size, shape, and pre-training duration where selected: https://bigscience.huggingface.co/blog/what-language-model-to-train-if-you-have-two-million-gpu-hours
More details on the architecture/optimizer: https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml
[LINK: https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml](https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml)
Blog post on the hardware/engineering side: https://bigscience.huggingface.co/blog/which-hardware-to-train-a-176b-parameters-model
Details on the distributed setup used for the training: https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml
[LINK: https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml](https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml)
Tensorboard updated during the training: https://huggingface.co/bigscience/tr11-176B-ml-logs/tensorboard#scalars&tagFilter=loss

## Lessons

Insights on how to approach training, negative results: https://github.com/bigscience-workshop/bigscience/blob/master/train/lessons-learned.md
[LINK: https://github.com/bigscience-workshop/bigscience/blob/master/train/lessons-learned.md](https://github.com/bigscience-workshop/bigscience/blob/master/train/lessons-learned.md)
Details on the obstacles overcome during the preparation on the engineering side (instabilities, optimization of training throughput, so many technical tricks and questions): https://github.com/bigscience-workshop/bigscience/blob/master/train/tr11-176B-ml/chronicles.md
[LINK: https://github.com/bigscience-workshop/bigscience/blob/master/train/tr11-176B-ml/chronicles.md](https://github.com/bigscience-workshop/bigscience/blob/master/train/tr11-176B-ml/chronicles.md)

## Initial Results

Initial prompting experiments using interim checkpoints: https://huggingface.co/spaces/bigscience/bloom-book

## Original checkpoints

The checkpoints in this repo correspond to the HuggingFace Transformers format. If you want to use our fork of Megatron-DeepSpeed that the model was trained with, you'd want to use this repo instead .
[LINK: Megatron-DeepSpeed](https://github.com/bigscience-workshop/Megatron-DeepSpeed)
Many intermediate checkpoints are available at https://huggingface.co/bigscience/bloom-intermediate/

## Model Card Authors

Ordered roughly chronologically and by amount of time spent on creating this model card.
Margaret Mitchell, Giada Pistilli, Yacine Jernite, Ezinwanne Ozoani, Marissa Gerchick, Nazneen Rajani, Sasha Luccioni, Irene Solaiman, Maraim Masoud, Somaieh Nikpoor, Carlos Muñoz Ferrandis, Stas Bekman, Christopher Akiki, Danish Contractor, David Lansky, Angelina McMillan-Major, Tristan Thrush, Suzana Ilić, Gérard Dupont, Shayne Longpre, Manan Dey, Stella Biderman, Douwe Kiela, Emi Baylor, Teven Le Scao, Aaron Gokaslan, Julien Launay, Niklas Muennighoff

## Model tree for bigscience/bloom

## Spaces using bigscience/bloom 100

## Papers for bigscience/bloom

## Evaluation results

- pass@1 on humaneval self-reported 0.155
- pass@10 on humaneval self-reported 0.328
- pass@100 on humaneval self-reported 0.572

--------------------