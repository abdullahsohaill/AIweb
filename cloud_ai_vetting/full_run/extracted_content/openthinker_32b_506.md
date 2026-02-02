# OpenThinker-32B
**URL:** https://huggingface.co/open-thoughts/OpenThinker-32B
**Page Title:** open-thoughts/OpenThinker-32B · Hugging Face
--------------------

We have released a paper for OpenThoughts! See our paper here .

## OpenThinker-32B

This model is a fine-tuned version of Qwen/Qwen2.5-32B-Instruct on the OpenThoughts-114k dataset.
The dataset is derived by distilling DeepSeek-R1 using the data pipeline available on github . 
More info about the dataset can be found on the dataset card at OpenThoughts-114k dataset .
[LINK: data pipeline available on github](https://github.com/open-thoughts/open-thoughts)
The numbers reported in the table below are evaluated with our open-source tool Evalchemy .
[LINK: Evalchemy](https://github.com/mlfoundations/Evalchemy)
We are fully open-source. Our model weights , datasets , data generation code , evaluation code , and training code are all publicly available.
[LINK: data generation code](https://github.com/open-thoughts/open-thoughts)
[LINK: evaluation code](https://github.com/mlfoundations/Evalchemy)
[LINK: training code](https://github.com/hiyouga/LLaMA-Factory)

## Intended uses & limitations

Apache 2.0 License

## Training procedure

We finetune Qwen2.5-32B-Instruct on OpenThoughts-114k for 
3 epochs with a 16k context length using LlamaFactory . 
Our full training configuration is provided in our repository . 
Training the 32B model on OpenThoughts-114k was done on AWS SageMaker with 8xH100 P5 nodes. On 4 nodes, this took around 90 hours. 
Meanwhile, for training on OpenThoughts-Unverified-173k , 
we used 96 nodes of 4xA100 (64 GB per GPU), training took 30 hours, spending 11,520 A100 hours on the Leonardo Supercomputer.
[LINK: LlamaFactory](https://github.com/hiyouga/LLaMA-Factory)
[LINK: full training configuration](https://github.com/open-thoughts/open-thoughts/blob/main/train/OpenThinker-32B.yaml)
[LINK: our repository](https://github.com/open-thoughts/open-thoughts/tree/main)

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 32
- gradient_accumulation_steps: 3
- total_train_batch_size: 96
- total_eval_batch_size: 256
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Framework versions

- Transformers 4.46.1
- Pytorch 2.3.0
- Datasets 3.1.0
- Tokenizers 0.20.3
More info can be found in our repository: https://github.com/open-thoughts/open-thoughts .
[LINK: https://github.com/open-thoughts/open-thoughts](https://github.com/open-thoughts/open-thoughts)

## Links

- 📝 OpenThoughts Paper
- 📊 Open Thoughts Launch Blog Post
- 📊 Open Thoughts Measuring Reasoning with Evalchmey Blog Post
- 📊 Open Thoughts OpenThinker-32B Post
- 💻 Open Thoughts GitHub Repository
[LINK: Open Thoughts GitHub Repository](https://github.com/open-thoughts/open-thoughts)
- 🧠 OpenThoughts-114k dataset
- 🧠 OpenThoughts-Unverified-173k dataset
- 🤖 OpenThinker-7B model
- 🤖 OpenThinker-7B-Unverfied model
- 🤖 OpenThinker-32B model - this model
- 🤖 OpenThinker-32B-Unverified model

## Citation

## Model tree for open-thoughts/OpenThinker-32B

Base model

## Dataset used to train open-thoughts/OpenThinker-32B

## Space using open-thoughts/OpenThinker-32B 1

## Collection including open-thoughts/OpenThinker-32B

## Paper for open-thoughts/OpenThinker-32B

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
open-thoughts/OpenThinker-32B is supported by the following Inference Providers:

--------------------