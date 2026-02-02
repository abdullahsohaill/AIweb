# Falcon-40B on Hugging Face
**URL:** https://huggingface.co/tiiuae/falcon-40b
**Page Title:** tiiuae/falcon-40b · Hugging Face
--------------------


## 🚀 Falcon-40B

Falcon-40B is a 40B parameters causal decoder-only model built by TII and trained on 1,000B tokens of RefinedWeb enhanced with curated corpora. It is made available under the Apache 2.0 license.
Paper coming soon 😊.
🤗 To get started with Falcon (inference, finetuning, quantization, etc.), we recommend reading this great blogpost fron HF !

## Why use Falcon-40B?

- It is the best open-source model currently available. Falcon-40B outperforms LLaMA , StableLM , RedPajama , MPT , etc. See the OpenLLM Leaderboard .
[LINK: LLaMA](https://github.com/facebookresearch/llama)
[LINK: StableLM](https://github.com/Stability-AI/StableLM)
- It features an architecture optimized for inference , with FlashAttention ( Dao et al., 2022 ) and multiquery ( Shazeer et al., 2019 ).
- It is made available under a permissive Apache 2.0 license allowing for commercial use , without any royalties or restrictions.
- ⚠️ This is a raw, pretrained model, which should be further finetuned for most usecases. If you are looking for a version better suited to taking generic instructions in a chat format, we recommend taking a look at Falcon-40B-Instruct .
💸 Looking for a smaller, less expensive model? Falcon-7B is Falcon-40B's little brother!
💥 Falcon LLMs require PyTorch 2.0 for use with transformers !
For fast inference with Falcon, check-out Text Generation Inference ! Read more in this blogpost .
[LINK: Text Generation Inference](https://github.com/huggingface/text-generation-inference)
You will need at least 85-100GB of memory to swiftly run inference with Falcon-40B.

## Model Card for Falcon-40B

## Model Details

### Model Description

- Developed by: https://www.tii.ae ;
- Model type: Causal decoder-only;
- Language(s) (NLP): English, German, Spanish, French (and limited capabilities in Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish);
- License: Apache 2.0 license.

### Model Source

- Paper: coming soon .

## Uses

### Direct Use

Research on large language models; as a foundation for further specialization and finetuning for specific usecases (e.g., summarization, text generation, chatbot, etc.)

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful.

## Bias, Risks, and Limitations

Falcon-40B is trained mostly on English, German, Spanish, French, with limited capabilities also in in Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish. It will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Falcon-40B to consider finetuning it for the specific set of tasks of interest, and for guardrails and appropriate precautions to be taken for any production use.

## How to Get Started with the Model

## Training Details

### Training Data

Falcon-40B was trained on 1,000B tokens of RefinedWeb , a high-quality filtered and deduplicated web dataset which we enhanced with curated corpora. Significant components from our curated copora were inspired by The Pile ( Gao et al., 2020 ).
RefinedWeb-Europe is made of the following languages:
The data was tokenized with the Falcon- 7B / 40B tokenizer.

### Training Procedure

Falcon-40B was trained on 384 A100 40GB GPUs, using a 3D parallelism strategy (TP=8, PP=4, DP=12) combined with ZeRO.
Training started in December 2022 and took two months.

## Evaluation

Paper coming soon.
See the OpenLLM Leaderboard for early results.

## Technical Specifications

### Model Architecture and Objective

Falcon-40B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).
The architecture is broadly adapted from the GPT-3 paper ( Brown et al., 2020 ), with the following differences:
- Positionnal embeddings: rotary ( Su et al., 2021 );
- Attention: multiquery ( Shazeer et al., 2019 ) and FlashAttention ( Dao et al., 2022 );
- Decoder-block: parallel attention/MLP with a two layer norms.
For multiquery, we are using an internal variant which uses independent key and values per tensor parallel degree.

### Compute Infrastructure

Falcon-40B was trained on AWS SageMaker, on 384 A100 40GB GPUs in P4d instances.
Falcon-40B was trained a custom distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO and high-performance Triton kernels (FlashAttention, etc.)

## Citation

Paper coming soon 😊. In the meanwhile, you can use the following information to cite:
To learn more about the pretraining dataset, see the 📓 RefinedWeb paper .

## License

Falcon-40B is made available under the Apache 2.0 license.

## Contact

falconllm@tii.ae

## Model tree for tiiuae/falcon-40b

## Dataset used to train tiiuae/falcon-40b

## Spaces using tiiuae/falcon-40b 100

## Collection including tiiuae/falcon-40b

## Papers for tiiuae/falcon-40b


--------------------