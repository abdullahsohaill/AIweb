# uses ONNXand OpenVINO
**URL:** https://www.sbert.net
**Page Title:** SentenceTransformers Documentation — Sentence Transformers documentation
--------------------

- SentenceTransformers Documentation
- Edit on GitHub
[LINK: Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/index.rst)
Note
Sentence Transformers v5.2 recently released, introducing multi-processing for CrossEncoder, multilingual NanoBEIR evaluators, similarity score outputs in mine_hard_negatives , Transformers v5 support, and more. Read the v5.2 Release Notes for more information.
[LINK: mine_hard_negatives](docs/package_reference/util.html#sentence_transformers.util.mine_hard_negatives)
[LINK: v5.2 Release Notes](https://github.com/huggingface/sentence-transformers/releases/tag/v5.2.0)
Attention
Sentence Transformers is transitioning from UKP Lab to 🤗 Hugging Face . This formalizes the existing maintenance structure, as Hugging Face has been maintaining the project for the past two years. The project’s development roadmap, support, and commitment to the community remain unchanged. Read the full announcement for more details!

## SentenceTransformers Documentation 

Sentence Transformers (a.k.a. SBERT) is the go-to Python module for accessing, using, and training state-of-the-art embedding and reranker models.
It can be used to compute embeddings using Sentence Transformer models ( quickstart ), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) models ( quickstart ), or to generate sparse embeddings using Sparse Encoder models ( quickstart ). This unlocks a wide range of applications, including semantic search , semantic textual similarity , and paraphrase mining .
[LINK: quickstart](docs/quickstart.html#sentence-transformer)
[LINK: quickstart](docs/quickstart.html#cross-encoder)
[LINK: quickstart](docs/quickstart.html#sparse-encoder)
[LINK: semantic textual similarity](docs/sentence_transformer/usage/semantic_textual_similarity.html)
A wide selection of over 10,000 pre-trained Sentence Transformers models are available for immediate use on 🤗 Hugging Face, including many of the state-of-the-art models from the Massive Text Embeddings Benchmark (MTEB) leaderboard . Additionally, it is easy to train or finetune your own embedding models , reranker models , or sparse encoder models using Sentence Transformers, enabling you to create custom models for your specific use cases.
[LINK: embedding models](docs/sentence_transformer/training_overview.html)
[LINK: reranker models](docs/cross_encoder/training_overview.html)
[LINK: sparse encoder models](docs/sparse_encoder/training_overview.html)
Sentence Transformers was created by UKP Lab and is being maintained by 🤗 Hugging Face . Don’t hesitate to open an issue on the Sentence Transformers repository if something is broken or if you have further questions.
[LINK: Sentence Transformers repository](https://github.com/huggingface/sentence-transformers)

## Usage 

See also
See the Quickstart for more quick information on how to use Sentence Transformers.
[LINK: Quickstart](docs/quickstart.html)
Working with Sentence Transformer models is straightforward:

## What Next? 

Consider reading one of the following sections to answer the related questions:
- Embedding Models: How to use Sentence Transformer models? Sentence Transformers > Usage What Sentence Transformer models can I use? Sentence Transformers > Pretrained Models How do I make Sentence Transformer models faster ? Sentence Transformers > Usage > Speeding up Inference How do I train/finetune a Sentence Transformer model? Sentence Transformers > Training Overview
- How to use Sentence Transformer models? Sentence Transformers > Usage
How to use Sentence Transformer models? Sentence Transformers > Usage
[LINK: Sentence Transformers > Usage](docs/sentence_transformer/usage/usage.html)
- What Sentence Transformer models can I use? Sentence Transformers > Pretrained Models
What Sentence Transformer models can I use? Sentence Transformers > Pretrained Models
[LINK: Sentence Transformers > Pretrained Models](docs/sentence_transformer/pretrained_models.html)
- How do I make Sentence Transformer models faster ? Sentence Transformers > Usage > Speeding up Inference
How do I make Sentence Transformer models faster ? Sentence Transformers > Usage > Speeding up Inference
[LINK: Sentence Transformers > Usage > Speeding up Inference](docs/sentence_transformer/usage/efficiency.html)
- How do I train/finetune a Sentence Transformer model? Sentence Transformers > Training Overview
How do I train/finetune a Sentence Transformer model? Sentence Transformers > Training Overview
[LINK: Sentence Transformers > Training Overview](docs/sentence_transformer/training_overview.html)
- Reranker Models: How to use Cross Encoder models? Cross Encoder > Usage What Cross Encoder models can I use? Cross Encoder > Pretrained Models How do I make Cross Encoder models faster ? Cross Encoder > Usage > Speeding up Inference How do I train/finetune a Cross Encoder model? Cross Encoder > Training Overview
- How to use Cross Encoder models? Cross Encoder > Usage
How to use Cross Encoder models? Cross Encoder > Usage
[LINK: Cross Encoder > Usage](docs/cross_encoder/usage/usage.html)
- What Cross Encoder models can I use? Cross Encoder > Pretrained Models
What Cross Encoder models can I use? Cross Encoder > Pretrained Models
[LINK: Cross Encoder > Pretrained Models](docs/cross_encoder/pretrained_models.html)
- How do I make Cross Encoder models faster ? Cross Encoder > Usage > Speeding up Inference
How do I make Cross Encoder models faster ? Cross Encoder > Usage > Speeding up Inference
[LINK: Cross Encoder > Usage > Speeding up Inference](docs/cross_encoder/usage/efficiency.html)
- How do I train/finetune a Cross Encoder model? Cross Encoder > Training Overview
How do I train/finetune a Cross Encoder model? Cross Encoder > Training Overview
[LINK: Cross Encoder > Training Overview](docs/cross_encoder/training_overview.html)
- Sparse Encoder Models: How to use Sparse Encoder models? Sparse Encoder > Usage What Sparse Encoder models can I use? Sparse Encoder > Pretrained Models How do I make Sparse Encoder models faster ? Sparse Encoder > Usage > Speeding up Inference How do I train/finetune a Sparse Encoder model? Sparse Encoder > Training Overview How do I integrate Sparse Encoder models with search engines? Sparse Encoder > Vector Database Integration
- How to use Sparse Encoder models? Sparse Encoder > Usage
How to use Sparse Encoder models? Sparse Encoder > Usage
[LINK: Sparse Encoder > Usage](docs/sparse_encoder/usage/usage.html)
- What Sparse Encoder models can I use? Sparse Encoder > Pretrained Models
What Sparse Encoder models can I use? Sparse Encoder > Pretrained Models
[LINK: Sparse Encoder > Pretrained Models](docs/sparse_encoder/pretrained_models.html)
- How do I make Sparse Encoder models faster ? Sparse Encoder > Usage > Speeding up Inference
How do I make Sparse Encoder models faster ? Sparse Encoder > Usage > Speeding up Inference
[LINK: Sparse Encoder > Usage > Speeding up Inference](docs/sparse_encoder/usage/efficiency.html)
- How do I train/finetune a Sparse Encoder model? Sparse Encoder > Training Overview
How do I train/finetune a Sparse Encoder model? Sparse Encoder > Training Overview
[LINK: Sparse Encoder > Training Overview](docs/sparse_encoder/training_overview.html)
- How do I integrate Sparse Encoder models with search engines? Sparse Encoder > Vector Database Integration
How do I integrate Sparse Encoder models with search engines? Sparse Encoder > Vector Database Integration

## Citing 

If you find this repository helpful, feel free to cite our publication Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks :
If you use one of the multilingual models, feel free to cite our publication Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation :
If you use the code for data augmentation , feel free to cite our publication Augmented SBERT: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks :
[LINK: data augmentation](https://github.com/huggingface/sentence-transformers/tree/main/examples/sentence_transformer/training/data_augmentation)

--------------------