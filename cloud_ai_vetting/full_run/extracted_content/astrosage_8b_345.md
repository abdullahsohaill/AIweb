# AstroSage-8B
**URL:** https://huggingface.co/AstroMLab/AstroSage-8B
**Page Title:** AstroMLab/AstroSage-8B · Hugging Face
--------------------


## AstroSage-Llama-3.1-8B

https://arxiv.org/abs/2411.09012
AstroSage-Llama-3.1-8B is a domain-specialized natural-language AI assistant tailored for research in astronomy, astrophysics, and cosmology. Trained on the complete collection of astronomy-related arXiv papers from 2007-2024 along with millions of synthetically-generated question-answer pairs and other astronomical literature, AstroSage-Llama-3.1-8B demonstrates excellent proficiency on a wide range of questions. This achievement demonstrates the potential of domain specialization in AI, suggesting that focused training can yield capabilities exceeding those of much larger, general-purpose models.

## Model Details

- Base Architecture : Meta-Llama-3.1-8B
- Base Model : Meta-Llama-3.1-8B
- Parameters : 8 billion
- Training Focus : Astronomy, Astrophysics, Cosmology, and Astronomical Instrumentation
- License : Llama 3.1 Community License
- Development Process : Continued Pre-training (CPT) on astronomical literature Supervised Fine-tuning (SFT) on QA pairs and instruction sets Model merging with Meta-Llama-3.1-8B-Instruct (75% CPT+SFT / 25% Meta-Instruct)
- Continued Pre-training (CPT) on astronomical literature
- Supervised Fine-tuning (SFT) on QA pairs and instruction sets
- Model merging with Meta-Llama-3.1-8B-Instruct (75% CPT+SFT / 25% Meta-Instruct)

## Using the model

## Model Improvements and Performance

AstroSage-Llama-3.1-8B shows remarkable performance improvements:
The model demonstrates:
- Outperformance of all 8B parameter models
- Comparable performance to GPT-4o (80.4%)
- ~1000x more cost-effective than proprietary models
- 7 percentage-point improvement over base Llama-3.1-8b model

## Training Data

- Continued Pre-training : ~250,000 arXiv preprints (2007-2024) from astro-ph and gr-qc Astronomy-related Wikipedia articles Selected astronomy textbooks Total: 3.3 billion tokens, 19.9 GB plaintext
Continued Pre-training :
- ~250,000 arXiv preprints (2007-2024) from astro-ph and gr-qc
- Astronomy-related Wikipedia articles
- Selected astronomy textbooks
- Total: 3.3 billion tokens, 19.9 GB plaintext
- Supervised Fine-tuning : 8.8 million curated QA pairs Filtered Infinity-Instruct-7M dataset Paper summaries and metadata Total: 2.0 billion tokens, 9.8 GB plaintext
Supervised Fine-tuning :
- 8.8 million curated QA pairs
- Filtered Infinity-Instruct-7M dataset
- Paper summaries and metadata
- Total: 2.0 billion tokens, 9.8 GB plaintext

## Intended Use

- Curiosity-driven question answering
- Brainstorming new ideas
- Astronomical research assistance
- Educational support in astronomy
- Literature review and summarization
- Scientific explanation of concepts

## Limitations

- Training data cutoff: January 2024
- As with all LLMs, hallucinations are possible
- Limited by 8B parameter size for complex reasoning
- Paper metadata not perfectly memorized
- Performance primarily validated on multiple-choice questions
- Primarily trained for use in English

## Technical Specifications

- Architecture: Based on Meta-Llama 3.1
- Training Infrastructure: ORNL OLCF Frontier
- Hosting: Hugging Face Hub (AstroMLab/AstroSage-8B)

## Ethical Considerations

While this model is designed for scientific use:
- Should not be used as sole source for critical research decisions
- Output should be verified against primary sources
- May reflect biases present in astronomical literature

## Citation and Contact

- Corresponding author: Tijmen de Haan (tijmen dot dehaan at gmail dot com)
- AstroMLab: astromachinelearninglab at gmail dot com
- Please cite the AstroMLab 3 paper when referencing this model:

## Model tree for AstroMLab/AstroSage-8B

Base model

## Space using AstroMLab/AstroSage-8B 1

## Paper for AstroMLab/AstroSage-8B

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
AstroMLab/AstroSage-8B is supported by the following Inference Providers:

--------------------