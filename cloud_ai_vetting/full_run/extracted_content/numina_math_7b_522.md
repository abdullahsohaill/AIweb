# Numina Math 7B
**URL:** https://huggingface.co/AI-MO/NuminaMath-7B-TIR
**Page Title:** AI-MO/NuminaMath-7B-TIR · Hugging Face
--------------------


## Model Card for NuminaMath 7B TIR

NuminaMath is a series of language models that are trained to solve math problems using tool-integrated reasoning (TIR). NuminaMath 7B TIR won the first progress prize of the AI Math Olympiad (AIMO) , with a score of 29/50 on the public and private tests sets.
This model is a fine-tuned version of deepseek-ai/deepseek-math-7b-base with two stages of supervised fine-tuning:
- Stage 1: fine-tune the base model on a large, diverse dataset of natural language math problems and solutions, where each solution is templated with Chain of Thought (CoT) to facilitate reasoning.
- Stage 2: fine-tune the model from Stage 1 on a synthetic dataset of tool-integrated reasoning, where each math problem is decomposed into a sequence of rationales, Python programs, and their outputs. Here we followed Microsoft’s ToRA paper and prompted GPT-4 to produce solutions in the ToRA format with code execution feedback. Fine-tuning on this data produces a reasoning agent that can solve mathematical problems via a mix of natural language reasoning and use of the Python REPL to compute intermediate results.

## Model description

- Model type: A 7B parameter math LLM fine-tuned in two stages of supervised fine-tuning, first on a dataset with math problem-solution pairs and then on a synthetic dataset with examples of multi-step generations using tool-integrated reasoning.
- Language(s) (NLP): Primarily English
- License: Apache 2.0
- Finetuned from model: deepseek-ai/deepseek-math-7b-base

## Model performance

Table: Comparison of various 7B and 8B parameter language models on different math benchmarks. All scores except those for NuminaMath-7B-TIR are reported without tool-integrated reasoning.

### Model Sources

- Repository: Coming soon!
- Demo: https://huggingface.co/spaces/AI-MO/math-olympiad-solver

## Intended uses & limitations

Here's how you can run the model using the pipeline() function from 🤗 Transformers:
The above executes a single step of Python code - for more complex problems, you will want to run the logic for several steps to obtain the final solution.

## Bias, Risks, and Limitations

NuminaMath 7B TIR was created to solve problems in the narrow domain of competition-level mathematics. As a result, the model should not be used for general chat applications. With greedy decoding, we find the model is capable of solving problems at the level of AMC 12 , but often struggles generate a valid solution on harder problems at the AIME and Math Olympiad level. The model also struggles to solve geometry problems, likely due to it's limited capacity and lack of other modalities like vision.

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
- num_epochs: 4.0

### Framework versions

- Transformers 4.40.1
- Pytorch 2.3.1
- Datasets 2.18.0
- Tokenizers 0.19.1

## Citation

If you find NuminaMath 7B TIR is useful in your work, please cite it with:

## Model tree for AI-MO/NuminaMath-7B-TIR

Base model

## Spaces using AI-MO/NuminaMath-7B-TIR 17

## Collections including AI-MO/NuminaMath-7B-TIR

## Paper for AI-MO/NuminaMath-7B-TIR


--------------------