# CodeParrot
**URL:** https://huggingface.co/codeparrot/codeparrot
**Page Title:** codeparrot/codeparrot · Hugging Face
--------------------


## CodeParrot 🦜

CodeParrot 🦜 is a GPT-2 model (1.5B parameters) trained to generate Python code. After the initial training and release of v1.0 we trained the model some more and released v1.1 (see below for details).

## Usage

You can load the CodeParrot model and tokenizer directly in transformers :
or with a pipeline :

## Training

The model was trained on the cleaned CodeParrot 🦜 dataset in two steps. After the initial training (v1.0) the model was trained for another 30k steps resulting in v1.1 and you find the settings in the following table:
The training was executed on 16 x A100 (40GB) GPUs. This setting amounts to roughly 26 + 15 billion tokens.

## Performance

We evaluated the model on OpenAI's HumanEval benchmark which consists of programming challenges:
The pass@k metric tells the probability that at least one out of k generations passes the tests.

## Resources

- Dataset: full , train , valid
- Code: repository
[LINK: repository](https://github.com/huggingface/transformers/tree/master/examples/research_projects/codeparrot)
- Spaces: generation , highlighting

## Model tree for codeparrot/codeparrot

## Dataset used to train codeparrot/codeparrot

## Spaces using codeparrot/codeparrot 18

## Evaluation results

- pass@1 on HumanEval self-reported 3.990
- pass@10 on HumanEval self-reported 8.690
- pass@100 on HumanEval self-reported 17.880

--------------------