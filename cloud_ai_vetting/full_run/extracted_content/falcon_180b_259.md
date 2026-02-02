# Falcon 180B
**URL:** https://huggingface.co/tiiuae/falcon-180B
**Page Title:** tiiuae/falcon-180B · Hugging Face
--------------------


## Acknowledge license to access the repository

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
You agree to the Falcon-180B TII license and acceptable use policy .
Log in or Sign Up to review the conditions and access this model content.

## 🚀 Falcon-180B

Falcon-180B is a 180B parameters causal decoder-only model built by TII and trained on 3,500B tokens of RefinedWeb enhanced with curated corpora. It is made available under the Falcon-180B TII License and Acceptable Use Policy .
Paper coming soon 😊
🤗 To get started with Falcon (inference, finetuning, quantization, etc.), we recommend reading this great blogpost from HF or this one from the release of the 40B!
Note that since the 180B is larger than what can easily be handled with transformers + acccelerate , we recommend using Text Generation Inference .
[LINK: Text Generation Inference](https://github.com/huggingface/text-generation-inference)
You will need at least 400GB of memory to swiftly run inference with Falcon-180B.

## Why use Falcon-180B?

- It is the best open-access model currently available, and one of the best model overall. Falcon-180B outperforms LLaMA-2 , StableLM , RedPajama , MPT , etc. See the OpenLLM Leaderboard .
[LINK: StableLM](https://github.com/Stability-AI/StableLM)
- It features an architecture optimized for inference , with multiquery ( Shazeer et al., 2019 ).
- It is made available under a permissive license allowing for commercial use .
- ⚠️ This is a raw, pretrained model, which should be further finetuned for most usecases. If you are looking for a version better suited to taking generic instructions in a chat format, we recommend taking a look at Falcon-180B-Chat .
💸 Looking for a smaller, less expensive model? Falcon-7B and Falcon-40B are Falcon-180B's little brothers!
💥 Falcon LLMs require PyTorch 2.0 for use with transformers !

## Model Card for Falcon-180B

## Model Details

### Model Description

- Developed by: https://www.tii.ae ;
- Model type: Causal decoder-only;
- Language(s) (NLP): English, German, Spanish, French (and limited capabilities in Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish);
- License: Falcon-180B TII License and Acceptable Use Policy .

### Model Source

- Paper: coming soon .

## Uses

See the acceptable use policy .

### Direct Use

Research on large language models; as a foundation for further specialization and finetuning for specific usecases (e.g., summarization, text generation, chatbot, etc.)

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful.

## Bias, Risks, and Limitations

Falcon-180B is trained mostly on English, German, Spanish, French, with limited capabilities also in in Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish. It will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Falcon-180B to consider finetuning it for the specific set of tasks of interest, and for guardrails and appropriate precautions to be taken for any production use.

## How to Get Started with the Model

To run inference with the model in full bfloat16 precision you need approximately 8xA100 80GB or equivalent.

## Training Details

### Training Data

Falcon-180B was trained on 3,500B tokens of RefinedWeb , a high-quality filtered and deduplicated web dataset which we enhanced with curated corpora. Significant components from our curated copora were inspired by The Pile ( Gao et al., 2020 ).
RefinedWeb-Europe is made of the following languages:
The data was tokenized with the Falcon tokenizer.

### Training Procedure

Falcon-180B was trained on up to 4,096 A100 40GB GPUs, using a 3D parallelism strategy (TP=8, PP=8, DP=64) combined with ZeRO.
Training started in early 2023.

## Evaluation

Paper coming soon.
See the OpenLLM Leaderboard for early results.

## Technical Specifications

### Model Architecture and Objective

Falcon-180B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).
The architecture is broadly adapted from the GPT-3 paper ( Brown et al., 2020 ), with the following differences:
- Positionnal embeddings: rotary ( Su et al., 2021 );
- Attention: multiquery ( Shazeer et al., 2019 ) and FlashAttention ( Dao et al., 2022 );
- Decoder-block: parallel attention/MLP with two layer norms.
For multiquery, we are using an internal variant which uses independent key and values per tensor parallel degree (so-called multigroup).

### Compute Infrastructure

Falcon-180B was trained on AWS SageMaker, on up to 4,096 A100 40GB GPUs in P4d instances.
Falcon-180B was trained a custom distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO and high-performance Triton kernels (FlashAttention, etc.)

## Citation

Paper coming soon 😊 (actually this time). In the meanwhile, you can use the following information to cite:
To learn more about the pretraining dataset, see the 📓 RefinedWeb paper .

## Contact

falconllm@tii.ae

## Model tree for tiiuae/falcon-180B

## Dataset used to train tiiuae/falcon-180B

## Spaces using tiiuae/falcon-180B 100

## Collection including tiiuae/falcon-180B

## Papers for tiiuae/falcon-180B


--------------------