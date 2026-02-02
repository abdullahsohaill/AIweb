# StarChat
**URL:** https://huggingface.co/HuggingFaceH4/starchat2-15b-v0.1
**Page Title:** HuggingFaceH4/starchat2-15b-v0.1 · Hugging Face
--------------------


## Model Card for StarChat2 15B

StarChat is a series of language models that are trained to act as helpful coding assistants. StarChat2 is the latest model in the series, and is a fine-tuned version of StarCoder2 that was trained with SFT and DPO on a mix of synthetic datasets.

## Model Details

### Model Description

- Model type: A 16B parameter GPT-like model fine-tuned on a mix of publicly available, synthetic datasets.
- Language(s) (NLP): Primarily English and 600+ programming languages.
- License: BigCode Open RAIL-M v1
- Finetuned from model: bigcode/starcoder2-15b

### Model Sources

- Repository: https://github.com/huggingface/alignment-handbook
[LINK: https://github.com/huggingface/alignment-handbook](https://github.com/huggingface/alignment-handbook)
- Demo: https://huggingface.co/spaces/HuggingFaceH4/starchat2-playground

## Performance

StarChat2 15B was trained to balance chat and programming capabilities. It achieves strong performance on chat benchmarks like MT Bench and IFEval , as well as the canonical HumanEval benchmark for Python code completion. The scores reported below were obtained using the LightEval evaluation suite (commit 988959cb905df4baa050f82b4d499d46e8b537f2 ) and each prompt has been formatted with the model's corresponding chat template to simulate real-world usage. This is why some scores may differ from those reported in technical reports or on the Open LLM Leaderboard.
[LINK: LightEval](https://github.com/huggingface/lighteval)

## Intended uses & limitations

The model was fine-tuned on a blend of chat, code, math, and reasoning datasets. As a result, the model can be used for chat and you can check out our demo to test its coding capabilities.
Here's how you can run the model using the pipeline() function from 🤗 Transformers:

## Bias, Risks, and Limitations

StarChat2 15B has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
Models trained primarily on code data will also have a more skewed demographic bias commensurate with the demographics of the GitHub community, for more on this see the StarCoder2 dataset
Since the base model was pretrained on a large corpus of code, it may produce code snippets that are syntactically valid but semantically incorrect. 
For example, it may produce code that does not compile or that produces incorrect results. It may also produce code that is vulnerable to security exploits. We have observed the model also has a tendency to produce false URLs which should be carefully inspected before clicking.
StarChat2 15B was fine-tuned from the base model StarCoder2 , please refer to its model card's Limitations Section for relevant information. 
In particular, the model was evaluated on some categories of gender biases, propensity for toxicity, and risk of suggesting code completions with known security flaws; these evaluations are reported in its technical report .

## Training details

This model is a fine-tuned version of starchat2-15b-sft-v0.1 on the HuggingFaceH4/ultrafeedback_binarized and the HuggingFaceH4/orca_dpo_pairs datasets. Check out the recipe in the Alignment Handbook for more details.
[LINK: Alignment Handbook](https://github.com/huggingface/alignment-handbook)
It achieves the following results on the evaluation set:
- Loss: 0.4347
- Rewards/chosen: -0.9461
- Rewards/rejected: -2.7745
- Rewards/accuracies: 0.7658
- Rewards/margins: 1.8284
- Logps/rejected: -322.1934
- Logps/chosen: -316.1898
- Logits/rejected: -2.3817
- Logits/chosen: -2.3005

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 2
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 2

### Training results

### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1

## Model tree for HuggingFaceH4/starchat2-15b-v0.1

Base model

## Datasets used to train HuggingFaceH4/starchat2-15b-v0.1

## Spaces using HuggingFaceH4/starchat2-15b-v0.1 72

## Collection including HuggingFaceH4/starchat2-15b-v0.1

## Papers for HuggingFaceH4/starchat2-15b-v0.1


--------------------