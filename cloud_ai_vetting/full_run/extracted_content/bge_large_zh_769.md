# bge-large-zh
**URL:** https://huggingface.co/BAAI/bge-large-zh
**Page Title:** BAAI/bge-large-zh · Hugging Face
--------------------

Recommend switching to newest BAAI/bge-large-zh-v1.5 , which has more reasonable similarity distribution and same method of usage.

## FlagEmbedding

Model List | FAQ | Usage | Evaluation | Train | Contact | Citation | License
More details please refer to our Github: FlagEmbedding .
[LINK: FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)
English | 中文
FlagEmbedding can map any text to a low-dimensional dense vector which can be used for tasks like retrieval, classification,  clustering, or semantic search.
And it also can be used in vector databases for LLMs.
************* 🌟 Updates 🌟 *************
- 10/12/2023: Release LLM-Embedder , a unified embedding model to support diverse retrieval augmentation needs for LLMs. Paper :fire:
- 09/15/2023: The technical report of BGE has been released
- 09/15/2023: The masive training data of BGE has been released
- 09/12/2023: New models: New reranker model : release cross-encoder models BAAI/bge-reranker-base and BAAI/bge-reranker-large , which are more powerful than embedding model. We recommend to use/fine-tune them to re-rank top-k documents returned by embedding models. update embedding model : release bge-*-v1.5 embedding model to alleviate the issue of the similarity distribution, and enhance its retrieval ability without instruction.
- New reranker model : release cross-encoder models BAAI/bge-reranker-base and BAAI/bge-reranker-large , which are more powerful than embedding model. We recommend to use/fine-tune them to re-rank top-k documents returned by embedding models.
- update embedding model : release bge-*-v1.5 embedding model to alleviate the issue of the similarity distribution, and enhance its retrieval ability without instruction.
- 09/07/2023: Update fine-tune code : Add script to mine hard negatives and support adding instruction during fine-tuning.
[LINK: fine-tune code](https://github.com/FlagOpen/FlagEmbedding/blob/master/FlagEmbedding/baai_general_embedding/README.md)
- 08/09/2023: BGE Models are integrated into Langchain , you can use it like this ; C-MTEB leaderboard is available .
- 08/05/2023: Release base-scale and small-scale models, best performance among the models of the same size 🤗
- 08/02/2023: Release bge-large-* (short for BAAI General Embedding) Models, rank 1st on MTEB and C-MTEB benchmark! :tada: :tada:
- 08/01/2023: We release the Chinese Massive Text Embedding Benchmark ( C-MTEB ), consisting of 31 test dataset.
[LINK: Chinese Massive Text Embedding Benchmark](https://github.com/FlagOpen/FlagEmbedding/blob/master/C_MTEB)

## Model List

bge is short for BAAI general embedding .
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/reranker)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/reranker)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: C-MTEB](https://github.com/FlagOpen/FlagEmbedding/tree/master/C_MTEB)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: Fine-tune](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[1]: If you need to search the relevant passages to a query, we suggest to add the instruction to the query; in other cases, no instruction is needed, just use the original query directly. In all cases, no instruction needs to be added to passages.
[2]: Different from embedding model, reranker uses question and document as input and directly output similarity instead of embedding. To balance the accuracy and time cost, cross-encoder is widely used to re-rank top-k documents retrieved by other simple models. 
For examples, use bge embedding model to retrieve top 100 relevant documents, and then use bge reranker to re-rank the top 100 document to get the final top-3 results.
All models have been uploaded to Huggingface Hub, and you can see them at https://huggingface.co/BAAI . 
If you cannot open the Huggingface Hub, you also can download the models at https://model.baai.ac.cn/models .

## Frequently asked questions

Following this example to prepare data and fine-tune your model. 
Some suggestions:
[LINK: example](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
- Mine hard negatives following this example , which can improve the retrieval performance.
[LINK: example](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune#hard-negatives)
- If you pre-train bge on your data, the pre-trained model cannot be directly used to calculate similarity, and it must be fine-tuned with contrastive learning before computing similarity.
- If the accuracy of the fine-tuned model is still not high, it is recommended to use/fine-tune the cross-encoder model (bge-reranker) to re-rank top-k results. Hard negatives also are needed to fine-tune reranker.
Suggest to use bge v1.5, which alleviates the issue of the similarity distribution.
Since we finetune the models by contrastive learning with a temperature of 0.01, 
the similarity distribution of the current BGE model is about in the interval [0.6, 1].
So a similarity score greater than 0.5 does not indicate that the two sentences are similar.
For downstream tasks, such as passage retrieval or semantic similarity, what matters is the relative order of the scores, not the absolute value. If you need to filter similar sentences based on a similarity threshold, 
please select an appropriate similarity threshold based on the similarity distribution on your data (such as 0.8, 0.85, or even 0.9).
For the bge-*-v1.5 , we improve its retrieval ability when not using instruction. 
No instruction only has a slight degradation in retrieval performance compared with using instruction. 
So you can generate embedding without instruction in all cases for convenience.
For a retrieval task that uses short queries to find long related documents, 
it is recommended to add instructions for these short queries. The best method to decide whether to add instructions for queries is choosing the setting that achieves better performance on your task. In all cases, the documents/passages do not need to add the instruction.

## Usage

### Usage for Embedding Model

Here are some examples for using bge models with FlagEmbedding , Sentence-Transformers , Langchain , or Huggingface Transformers .
If it doesn't work for you, you can see FlagEmbedding for more methods to install FlagEmbedding.
[LINK: FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding/blob/master/FlagEmbedding/baai_general_embedding/README.md)
For the value of the argument query_instruction_for_retrieval , see Model List .
[LINK: Model List](https://github.com/FlagOpen/FlagEmbedding/tree/master#model-list)
By default, FlagModel will use all available GPUs when encoding. Please set os.environ["CUDA_VISIBLE_DEVICES"] to select specific GPUs.
You also can set os.environ["CUDA_VISIBLE_DEVICES"]="" to make all GPUs unavailable.
You can also use the bge models with sentence-transformers :
For s2p(short query to long passage) retrieval task, 
each short query should start with an instruction (instructions see Model List ). 
But the instruction is not needed for passages.
[LINK: Model List](https://github.com/FlagOpen/FlagEmbedding/tree/master#model-list)
You can use bge in langchain like this:
With the transformers package, you can use the model like this: First, you pass your input through the transformer model, then you select the last hidden state of the first token (i.e., [CLS]) as the sentence embedding.

### Usage for Reranker

Different from embedding model, reranker uses question and document as input and directly output similarity instead of embedding. 
You can get a relevance score by inputting query and passage to the reranker. 
The reranker is optimized based cross-entropy loss, so the relevance score is not bounded to a specific range.
Get relevance scores (higher scores indicate more relevance):

## Evaluation

baai-general-embedding models achieve state-of-the-art performance on both MTEB and C-MTEB leaderboard! For more details and evaluation tools see our scripts .
[LINK: scripts](https://github.com/FlagOpen/FlagEmbedding/blob/master/C_MTEB/README.md)
- MTEB :
[LINK: text-embedding-ada-002](https://platform.openai.com/docs/guides/embeddings)
- C-MTEB : We create the benchmark C-MTEB for Chinese text embedding which consists of 31 datasets from 6 tasks. 
Please refer to C_MTEB for a detailed introduction.
[LINK: C_MTEB](https://github.com/FlagOpen/FlagEmbedding/blob/master/C_MTEB/README.md)
[LINK: text-embedding-ada-002(OpenAI)](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
- Reranking :
See C_MTEB for evaluation script.
[LINK: C_MTEB](https://github.com/FlagOpen/FlagEmbedding/blob/master/C_MTEB/)
* : T2RerankingZh2En and T2RerankingEn2Zh are cross-language retrieval tasks

## Train

### BAAI Embedding

We pre-train the models using retromae and train them on large-scale pairs data using contrastive learning. You can fine-tune the embedding model on your data following our examples . We also provide a pre-train example .
Note that the goal of pre-training is to reconstruct the text, and the pre-trained model cannot be used for similarity calculation directly, it needs to be fine-tuned.
More training details for bge see baai_general_embedding .
[LINK: retromae](https://github.com/staoxiao/RetroMAE)
[LINK: examples](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/finetune)
[LINK: pre-train example](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/pretrain)
[LINK: baai_general_embedding](https://github.com/FlagOpen/FlagEmbedding/blob/master/FlagEmbedding/baai_general_embedding/README.md)

### BGE Reranker

Cross-encoder will perform full-attention over the input pair, 
which is more accurate than embedding model (i.e., bi-encoder) but more time-consuming than embedding model.
Therefore, it can be used to re-rank the top-k documents returned by embedding model.
We train the cross-encoder on a multilingual pair data, 
The data format is the same as embedding model, so you can fine-tune it easily following our example . 
More details please refer to ./FlagEmbedding/reranker/README.md
[LINK: example](https://github.com/FlagOpen/FlagEmbedding/tree/master/examples/reranker)
[LINK: ./FlagEmbedding/reranker/README.md](https://github.com/FlagOpen/FlagEmbedding/tree/master/FlagEmbedding/reranker)

## Contact

If you have any question or suggestion related to this project, feel free to open an issue or pull request.
You also can email Shitao Xiao( stxiao@baai.ac.cn ) and Zheng Liu( liuzheng@baai.ac.cn ).

## Citation

If you find this repository useful, please consider giving a star :star: and citation

## License

FlagEmbedding is licensed under the MIT License . The released models can be used for commercial purposes free of charge.
[LINK: MIT License](https://github.com/FlagOpen/FlagEmbedding/blob/master/LICENSE)

## Model tree for BAAI/bge-large-zh

## Spaces using BAAI/bge-large-zh 5

## Collection including BAAI/bge-large-zh

## Papers for BAAI/bge-large-zh

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
BAAI/bge-large-zh is supported by the following Inference Providers:

--------------------