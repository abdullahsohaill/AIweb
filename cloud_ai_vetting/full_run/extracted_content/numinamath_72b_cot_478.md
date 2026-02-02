# NuminaMath-72B-CoT
**URL:** https://huggingface.co/AI-MO/NuminaMath-72B-CoT
**Page Title:** AI-MO/NuminaMath-72B-CoT · Hugging Face
--------------------


## Model Card for NuminaMath 72B CoT

NuminaMath is a series of language models that are trained with two stages of supervised fine-tuning to solve math problems using chain of thought (CoT) and tool-integrated reasoning (TIR):
- Stage 1: fine-tune the base model on a large, diverse dataset of natural language math problems and solutions, where each solution is templated with Chain of Thought (CoT) to facilitate reasoning.
- Stage 2: fine-tune the model from Stage 1 on a synthetic dataset of tool-integrated reasoning, where each math problem is decomposed into a sequence of rationales, Python programs, and their outputs.
NuminaMath 72B CoT is the model from Stage 1 and was fine-tuned on AI-MO/NuminaMath-CoT , a large-scale dataset of 860k+ math competition problem-solution pairs.

## Model description

- Model type: A 72B parameter math LLM fine-tuned on a dataset with 860k+ math problem-solution pairs.
- Language(s) (NLP): Primarily English
- License: Tongyi Qianwen
- Finetuned from model: Qwen/Qwen2-72B

### Model Sources

- Repository: https://github.com/project-numina/aimo-progress-prize
[LINK: https://github.com/project-numina/aimo-progress-prize](https://github.com/project-numina/aimo-progress-prize)

## Intended uses & limitations

Here's how you can run the model using the pipeline() function from 🤗 Transformers:

## Bias, Risks, and Limitations

NuminaMath 72B CoT was created to solve problems in the narrow domain of competition-level mathematics. As a result, the model should not be used for general chat applications. With greedy decoding, we find the model is capable of solving problems at the level of AMC 12 , but often struggles generate a valid solution on harder problems at the AIME and Math Olympiad level. The model also struggles to solve geometry problems, likely due to it's limited capacity and lack of other modalities like vision.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 32
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Framework versions

- Transformers 4.42.3
- Pytorch 2.3.0+cu121
- Datasets 2.18.0
- Tokenizers 0.19.1

## Citation

If you find NuminaMath 72B CoT is useful in your work, please cite it with:

## Model tree for AI-MO/NuminaMath-72B-CoT

Base model

## Dataset used to train AI-MO/NuminaMath-72B-CoT

## Space using AI-MO/NuminaMath-72B-CoT 1

## Collection including AI-MO/NuminaMath-72B-CoT


--------------------