# Falcon Mamba 7B
**URL:** https://huggingface.co/tiiuae/falcon-mamba-7b-instruct
**Page Title:** tiiuae/falcon-mamba-7b-instruct · Hugging Face
--------------------

Model card for FalconMamba Instruct model

## Table of Contents

- TL;DR
- Model Details
- Usage
- Training Details
- Evaluation

## TL;DR

## Model Details

## Model Description

- Developed by: https://www.tii.ae
- Model type: Causal decoder-only
- Architecture: Mamba
- Language(s) (NLP): Mainly English
- License: TII Falcon-Mamba License 2.0
Check out the blogpost for more details!

## Usage

Find below some example scripts on how to use the model in transformers (Make sure to have the latest transformers, or the one built from source):

## Using the Pytorch model

### Running the model on a CPU

### Running the model on a GPU

### Running the model on a GPU using torch.compile

### Running the model on a GPU using different precisions

## Training Details

## Training Data

Falcon-Mamba has been trained with ~ 5,500 GT mainly coming from Refined-Web , a large volume web-only dataset filtered and deduplicated.
Similar to the others Falcon suite models, Falcon-Mamba has been trained leveraging a multi-stage training strategy to increase the context-length from 2,048 to 8,192. 
Moreover, inspired by the concept of Curriculum Learning, we carefully selected data mixtures throughout the training stages, considering both data diversity and complexity. 
Note that at inference the context-length is not relevant as the Mamba architecture has no limit on long range dependency.
At the last training stage, small portion of high-quality curated data was used to further enhance performance.
Overall, the data sources included RefinedWeb-English, high quality technical data, code data and math data extracted from public sources.
In particular, we used samples coming from Fineweb-edu during our last training stage.
The data was tokenized with the Falcon- 7B / 11B tokenizer.
After pre-training, the model has been further fine-tuned on instruction data.

## Training Procedure

Falcon-Mamba-7B was trained on 256 H100 80GB GPUs for the majority of the training, using a 3D parallelism strategy (TP=1, PP=1, DP=256) combined with ZeRO.

### Training Hyperparameters

The model was trained AdamW optimizer, WSD (warmup-stable-decay) learning rate schedule, and a batch size rampup from b m i n = 128 b_{\mathrm{min}}=128 b min ​ = 128 to b m a x = 2048 b_{\mathrm{max}}=2048 b max ​ = 2048 during first 50 GT of training. 
In the stable phase we used maximal learning rate η m a x = 6.4 × 10 − 4 \eta_{\mathrm{max}}=6.4 \times 10^{-4} η max ​ = 6.4 × 1 0 − 4 , and decayed it to the minimal value η m i n = η m a x 256 \eta_{\mathrm{min}}=\frac{\eta_{\mathrm{max}}}{256} η min ​ = 256 η max ​ ​ with exponential schedule over 500 GT. 
Also, we applied BatchScaling during the rampup — rescaling learning rate η \eta η so that the Adam noise temperature T n o i s e ≡ η b T_{\mathrm{noise}}\equiv\frac{\eta}{\sqrt{b}} T noise ​ ≡ b ​ η ​ is kept constant.

### Speeds, Sizes, Times

The model training took roughly two months.

## Evaluation

## Benchmarks

We evaluate our model on all benchmarks of the new leaderboard's version using the lm-evaluation-harness package, and then normalize the evaluation results with HuggingFace score normalization.
Also, we evaluate our model on the benchmarks of the first leaderboard using lighteval .
Mostly, we took evaluation results from both leaderboards. For the models marked by star we evaluated the tasks internally, while for the models marked by two stars the results were taken from paper or model card.

## Throughput

This model can achieve comparable throughput and performance compared to other transformer based models that use optimized kernels such as Flash Attention 2. Make sure to install the optimized Mamba kernels with the following commands:
Refer to our FalconMamba blogpost for more details about performance evaluation.

## Technical Specifications

## Model Architecture and Objective

Falcon-Mamba-7B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).
The model is based on the Mamba architecture ( Gu et al., 2023 ).

## Compute Infrastructure

### Hardware

Falcon-Mamba-7B was trained on AWS SageMaker, using on average 256 H100 80GB GPUs in 32 p5 instances.

### Software

Falcon-Mamba-7B was trained on an internal distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO, high-performance Triton kernels.

## Citation

You can use the following bibtex citation:

## Model tree for tiiuae/falcon-mamba-7b-instruct

Base model

## Datasets used to train tiiuae/falcon-mamba-7b-instruct

## Spaces using tiiuae/falcon-mamba-7b-instruct 5

## Collection including tiiuae/falcon-mamba-7b-instruct

## Papers for tiiuae/falcon-mamba-7b-instruct


--------------------