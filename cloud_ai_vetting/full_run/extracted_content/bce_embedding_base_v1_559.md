# bce-embedding-base_v1
**URL:** https://huggingface.co/maidalun1020/bce-embedding-base_v1
**Page Title:** maidalun1020/bce-embedding-base_v1 · Hugging Face
--------------------


## BCEmbedding: Bilingual and Crosslingual Embedding for RAG

最新、最详细的bce-embedding-base_v1相关信息，请移步（The latest "Updates" should be checked in）：
GitHub
[LINK: GitHub](https://github.com/netease-youdao/BCEmbedding)

## 主要特点(Key Features)：

- 中英双语，以及中英跨语种能力(Bilingual and Crosslingual capability in English and Chinese)；
- RAG优化，适配更多真实业务场景(RAG adaptation for more domains, including Education, Law, Finance, Medical, Literature, FAQ, Textbook, Wikipedia, etc.)；
- 方便集成进langchain和llamaindex(Easy integrations for langchain and llamaindex in BCEmbedding )。
[LINK: BCEmbedding](https://github.com/netease-youdao/BCEmbedding)
- EmbeddingModel 不需要“精心设计”instruction，尽可能召回有用片段。 (No need for "instruction")
- 最佳实践（Best practice） ：embedding召回top50-100片段，reranker对这50-100片段精排，最后取top5-10片段。（1. Get top 50-100 passages with bce-embedding-base_v1 for " recall "；    2. Rerank passages with bce-reranker-base_v1 and get top 5-10 for " precision " finally. ）

## News:

- BCEmbedding 技术博客（ Technical Blog ）: 为RAG而生-BCEmbedding技术报告
- Related link for RerankerModel : bce-reranker-base_v1

## Third-party Examples:

- RAG applications: QAnything , ragflow , HuixiangDou , ChatPDF .
[LINK: QAnything](https://github.com/netease-youdao/qanything)
[LINK: ragflow](https://github.com/infiniflow/ragflow)
[LINK: HuixiangDou](https://github.com/InternLM/HuixiangDou)
[LINK: ChatPDF](https://github.com/shibing624/ChatPDF)
- Efficient inference framework: ChatLLM.cpp , Xinference , mindnlp (Huawei GPU, 华为GPU) .
[LINK: ChatLLM.cpp](https://github.com/foldl/chatllm.cpp)
[LINK: Xinference](https://github.com/xorbitsai/inference)
[LINK: mindnlp (Huawei GPU, 华为GPU)](https://github.com/mindspore-lab/mindnlp/tree/master/llm/inference/bce)
- 🌐 Bilingual and Crosslingual Superiority
- 💡 Key Features
- 🚀 Latest Updates
- 🍎 Model List
- 📖 Manual Installation Quick Start ( transformers , sentence-transformers ) Integrations for RAG Frameworks ( langchain , llama_index )
- Installation
- Quick Start ( transformers , sentence-transformers )
- Integrations for RAG Frameworks ( langchain , llama_index )
- ⚙️ Evaluation Evaluate Semantic Representation by MTEB Evaluate RAG by LlamaIndex
- Evaluate Semantic Representation by MTEB
- Evaluate RAG by LlamaIndex
- 📈 Leaderboard Semantic Representation Evaluations in MTEB RAG Evaluations in LlamaIndex
- Semantic Representation Evaluations in MTEB
- RAG Evaluations in LlamaIndex
- 🛠 Youdao's BCEmbedding API
[LINK: 🛠 Youdao's BCEmbedding API](#-youdaos-bcembedding-api)
- 🧲 WeChat Group
- ✏️ Citation
- 🔐 License
- 🔗 Related Links
B ilingual and C rosslingual Embedding ( BCEmbedding ), developed by NetEase Youdao, encompasses EmbeddingModel and RerankerModel . The EmbeddingModel specializes in generating semantic vectors, playing a crucial role in semantic search and question-answering, and the RerankerModel excels at refining search results and ranking tasks.
BCEmbedding serves as the cornerstone of Youdao's Retrieval Augmented Generation (RAG) implmentation, notably QAnything [ github ], an open-source implementation widely integrated in various Youdao products like Youdao Speed Reading and Youdao Translation .
[LINK: github](https://github.com/netease-youdao/qanything)
Distinguished for its bilingual and crosslingual proficiency, BCEmbedding excels in bridging Chinese and English linguistic gaps, which achieves
- A high performence on Semantic Representation Evaluations in MTEB ;
A high performence on Semantic Representation Evaluations in MTEB ;
- A new benchmark in the realm of RAG Evaluations in LlamaIndex . BCEmbedding 是由网易有道开发的双语和跨语种语义表征算法模型库，其中包含 EmbeddingModel 和 RerankerModel 两类基础模型。 EmbeddingModel 专门用于生成语义向量，在语义搜索和问答中起着关键作用，而 RerankerModel 擅长优化语义搜索结果和语义相关顺序精排。 BCEmbedding 作为有道的检索增强生成式应用（RAG）的基石，特别是在 QAnything [ github ]中发挥着重要作用。QAnything作为一个网易有道开源项目，在有道许多产品中有很好的应用实践，比如 有道速读 和 有道翻译 BCEmbedding 以其出色的双语和跨语种能力而著称，在语义检索中消除中英语言之间的差异，从而实现： 强大的双语和跨语种语义表征能力【 基于MTEB的语义表征评测指标 】。 基于LlamaIndex的RAG评测，表现SOTA【 基于LlamaIndex的RAG评测指标 】。
A new benchmark in the realm of RAG Evaluations in LlamaIndex .
BCEmbedding 是由网易有道开发的双语和跨语种语义表征算法模型库，其中包含 EmbeddingModel 和 RerankerModel 两类基础模型。 EmbeddingModel 专门用于生成语义向量，在语义搜索和问答中起着关键作用，而 RerankerModel 擅长优化语义搜索结果和语义相关顺序精排。
BCEmbedding 作为有道的检索增强生成式应用（RAG）的基石，特别是在 QAnything [ github ]中发挥着重要作用。QAnything作为一个网易有道开源项目，在有道许多产品中有很好的应用实践，比如 有道速读 和 有道翻译
[LINK: github](https://github.com/netease-youdao/qanything)
BCEmbedding 以其出色的双语和跨语种能力而著称，在语义检索中消除中英语言之间的差异，从而实现：
- 强大的双语和跨语种语义表征能力【 基于MTEB的语义表征评测指标 】。
- 基于LlamaIndex的RAG评测，表现SOTA【 基于LlamaIndex的RAG评测指标 】。

## 🌐 Bilingual and Crosslingual Superiority

Existing embedding models often encounter performance challenges in bilingual and crosslingual scenarios, particularly in Chinese, English and their crosslingual tasks. BCEmbedding , leveraging the strength of Youdao's translation engine, excels in delivering superior performance across monolingual, bilingual, and crosslingual settings.
EmbeddingModel supports Chinese (ch) and English (en) (more languages support will come soon), while RerankerModel supports Chinese (ch), English (en), Japanese (ja) and Korean (ko) .
现有的单个语义表征模型在双语和跨语种场景中常常表现不佳，特别是在中文、英文及其跨语种任务中。 BCEmbedding 充分利用有道翻译引擎的优势，实现只需一个模型就可以在单语、双语和跨语种场景中表现出卓越的性能。
EmbeddingModel 支持 中文和英文 （之后会支持更多语种）； RerankerModel 支持 中文，英文，日文和韩文 。

## 💡 Key Features

- Bilingual and Crosslingual Proficiency : Powered by Youdao's translation engine, excelling in Chinese, English and their crosslingual retrieval task, with upcoming support for additional languages.
Bilingual and Crosslingual Proficiency : Powered by Youdao's translation engine, excelling in Chinese, English and their crosslingual retrieval task, with upcoming support for additional languages.
- RAG-Optimized : Tailored for diverse RAG tasks including translation, summarization, and question answering , ensuring accurate query understanding . See RAG Evaluations in LlamaIndex .
RAG-Optimized : Tailored for diverse RAG tasks including translation, summarization, and question answering , ensuring accurate query understanding . See RAG Evaluations in LlamaIndex .
- Efficient and Precise Retrieval : Dual-encoder for efficient retrieval of EmbeddingModel in first stage, and cross-encoder of RerankerModel for enhanced precision and deeper semantic analysis in second stage.
Efficient and Precise Retrieval : Dual-encoder for efficient retrieval of EmbeddingModel in first stage, and cross-encoder of RerankerModel for enhanced precision and deeper semantic analysis in second stage.
- Broad Domain Adaptability : Trained on diverse datasets for superior performance across various fields.
Broad Domain Adaptability : Trained on diverse datasets for superior performance across various fields.
- User-Friendly Design : Instruction-free, versatile use for multiple tasks without specifying query instruction for each task.
User-Friendly Design : Instruction-free, versatile use for multiple tasks without specifying query instruction for each task.
- Meaningful Reranking Scores : RerankerModel provides relevant scores to improve result quality and optimize large language model performance.
Meaningful Reranking Scores : RerankerModel provides relevant scores to improve result quality and optimize large language model performance.
- Proven in Production : Successfully implemented and validated in Youdao's products. 双语和跨语种能力 ：基于有道翻译引擎的强大能力，我们的 BCEmbedding 具备强大的中英双语和跨语种语义表征能力。 RAG适配 ：面向RAG做了针对性优化，可以适配大多数相关任务，比如 翻译，摘要，问答 等。此外，针对 问题理解 （query understanding）也做了针对优化，详见 基于LlamaIndex的RAG评测指标 。 高效且精确的语义检索 ： EmbeddingModel 采用双编码器，可以在第一阶段实现高效的语义检索。 RerankerModel 采用交叉编码器，可以在第二阶段实现更高精度的语义顺序精排。 更好的领域泛化性 ：为了在更多场景实现更好的效果，我们收集了多种多样的领域数据。 用户友好 ：语义检索时不需要特殊指令前缀。也就是，你不需要为各种任务绞尽脑汁设计指令前缀。 有意义的重排序分数 ： RerankerModel 可以提供有意义的语义相关性分数（不仅仅是排序），可以用于过滤无意义文本片段，提高大模型生成效果。 产品化检验 ： BCEmbedding 已经被有道众多真实产品检验。
Proven in Production : Successfully implemented and validated in Youdao's products.
- 双语和跨语种能力 ：基于有道翻译引擎的强大能力，我们的 BCEmbedding 具备强大的中英双语和跨语种语义表征能力。
双语和跨语种能力 ：基于有道翻译引擎的强大能力，我们的 BCEmbedding 具备强大的中英双语和跨语种语义表征能力。
- RAG适配 ：面向RAG做了针对性优化，可以适配大多数相关任务，比如 翻译，摘要，问答 等。此外，针对 问题理解 （query understanding）也做了针对优化，详见 基于LlamaIndex的RAG评测指标 。
RAG适配 ：面向RAG做了针对性优化，可以适配大多数相关任务，比如 翻译，摘要，问答 等。此外，针对 问题理解 （query understanding）也做了针对优化，详见 基于LlamaIndex的RAG评测指标 。
- 高效且精确的语义检索 ： EmbeddingModel 采用双编码器，可以在第一阶段实现高效的语义检索。 RerankerModel 采用交叉编码器，可以在第二阶段实现更高精度的语义顺序精排。
高效且精确的语义检索 ： EmbeddingModel 采用双编码器，可以在第一阶段实现高效的语义检索。 RerankerModel 采用交叉编码器，可以在第二阶段实现更高精度的语义顺序精排。
- 更好的领域泛化性 ：为了在更多场景实现更好的效果，我们收集了多种多样的领域数据。
更好的领域泛化性 ：为了在更多场景实现更好的效果，我们收集了多种多样的领域数据。
- 用户友好 ：语义检索时不需要特殊指令前缀。也就是，你不需要为各种任务绞尽脑汁设计指令前缀。
用户友好 ：语义检索时不需要特殊指令前缀。也就是，你不需要为各种任务绞尽脑汁设计指令前缀。
- 有意义的重排序分数 ： RerankerModel 可以提供有意义的语义相关性分数（不仅仅是排序），可以用于过滤无意义文本片段，提高大模型生成效果。
有意义的重排序分数 ： RerankerModel 可以提供有意义的语义相关性分数（不仅仅是排序），可以用于过滤无意义文本片段，提高大模型生成效果。
- 产品化检验 ： BCEmbedding 已经被有道众多真实产品检验。
产品化检验 ： BCEmbedding 已经被有道众多真实产品检验。

## 🚀 Latest Updates

- 2024-01-03 : Model Releases - bce-embedding-base_v1 and bce-reranker-base_v1 are available.
2024-01-03 : Model Releases - bce-embedding-base_v1 and bce-reranker-base_v1 are available.
- 2024-01-03 : Eval Datasets [ CrosslingualMultiDomainsDataset ] - Evaluate the performence of RAG, using LlamaIndex .
2024-01-03 : Eval Datasets [ CrosslingualMultiDomainsDataset ] - Evaluate the performence of RAG, using LlamaIndex .
[LINK: LlamaIndex](https://github.com/run-llama/llama_index)
- 2024-01-03 : Eval Datasets [ Details ] - Evaluate the performence of crosslingual semantic representation, using MTEB . 2024-01-03 : 模型发布 - bce-embedding-base_v1 和 bce-reranker-base_v1 已发布. 2024-01-03 : RAG评测数据 [ CrosslingualMultiDomainsDataset ] - 基于 LlamaIndex 的RAG评测数据已发布。 2024-01-03 : 跨语种语义表征评测数据 [ 详情 ] - 基于 MTEB 的跨语种评测数据已发布.
2024-01-03 : Eval Datasets [ Details ] - Evaluate the performence of crosslingual semantic representation, using MTEB .
[LINK: Details](https://github.com/netease-youdao/BCEmbedding/blob/master/BCEmbedding/evaluation/c_mteb/Retrieval.py)
[LINK: MTEB](https://github.com/embeddings-benchmark/mteb)
- 2024-01-03 : 模型发布 - bce-embedding-base_v1 和 bce-reranker-base_v1 已发布.
- 2024-01-03 : RAG评测数据 [ CrosslingualMultiDomainsDataset ] - 基于 LlamaIndex 的RAG评测数据已发布。
[LINK: LlamaIndex](https://github.com/run-llama/llama_index)
- 2024-01-03 : 跨语种语义表征评测数据 [ 详情 ] - 基于 MTEB 的跨语种评测数据已发布.
[LINK: MTEB](https://github.com/embeddings-benchmark/mteb)

## 🍎 Model List

## 📖 Manual

### Installation

First, create a conda environment and activate it.
Then install BCEmbedding for minimal installation:
Or install from source:

### Quick Start

Use EmbeddingModel , and cls pooler is default.
Use RerankerModel to calculate relevant scores and rerank:
NOTE:
- In RerankerModel.rerank method, we provide an advanced preproccess that we use in production for making sentence_pairs , when "passages" are very long.
For EmbeddingModel :
For RerankerModel :
For EmbeddingModel :
For RerankerModel :

### Integrations for RAG Frameworks

## ⚙️ Evaluation

### Evaluate Semantic Representation by MTEB

We provide evaluateion tools for embedding and reranker models, based on MTEB and C_MTEB .
[LINK: MTEB](https://github.com/embeddings-benchmark/mteb)
[LINK: C_MTEB](https://github.com/FlagOpen/FlagEmbedding/tree/master/C_MTEB)
我们基于 MTEB 和 C_MTEB ，提供 embedding 和 reranker 模型的语义表征评测工具。
[LINK: MTEB](https://github.com/embeddings-benchmark/mteb)
[LINK: C_MTEB](https://github.com/FlagOpen/FlagEmbedding/tree/master/C_MTEB)
Just run following cmd to evaluate your_embedding_model (e.g. maidalun1020/bce-embedding-base_v1 ) in bilingual and crosslingual settings (e.g. ["en", "zh", "en-zh", "zh-en"] ).
运行下面命令评测 your_embedding_model （比如， maidalun1020/bce-embedding-base_v1 ）。评测任务将会在 双语和跨语种 （比如， ["en", "zh", "en-zh", "zh-en"] ）模式下评测：
The total evaluation tasks contain 114 datastes of "Retrieval", "STS", "PairClassification", "Classification", "Reranking" and "Clustering" .
评测包含 "Retrieval"， "STS"， "PairClassification"， "Classification"， "Reranking"和"Clustering" 这六大类任务的 114个数据集 。
NOTE:
- All models are evaluated in their recommended pooling method ( pooler ) . mean pooler: "jina-embeddings-v2-base-en", "m3e-base", "m3e-large", "e5-large-v2", "multilingual-e5-base", "multilingual-e5-large" and "gte-large". cls pooler: Other models.
- mean pooler: "jina-embeddings-v2-base-en", "m3e-base", "m3e-large", "e5-large-v2", "multilingual-e5-base", "multilingual-e5-large" and "gte-large".
- cls pooler: Other models.
- "jina-embeddings-v2-base-en" model should be loaded with trust_remote_code .
注意：
- 所有模型的评测采用各自推荐的 pooler 。"jina-embeddings-v2-base-en", "m3e-base", "m3e-large", "e5-large-v2", "multilingual-e5-base", "multilingual-e5-large"和"gte-large"的 pooler 采用 mean ，其他模型的 pooler 采用 cls .
- "jina-embeddings-v2-base-en"模型在载入时需要 trust_remote_code 。
Run following cmd to evaluate your_reranker_model (e.g. "maidalun1020/bce-reranker-base_v1") in bilingual and crosslingual settings (e.g. ["en", "zh", "en-zh", "zh-en"] ).
运行下面命令评测 your_reranker_model （比如， maidalun1020/bce-reranker-base_v1 ）。评测任务将会在 双语种和跨语种 （比如， ["en", "zh", "en-zh", "zh-en"] ）模式下评测：
The evaluation tasks contain 12 datastes of "Reranking" .
评测包含 "Reranking" 任务的 12个数据集 。
We proveide a one-click script to sumarize evaluation results of embedding and reranker models as Embedding Models Evaluation Summary and Reranker Models Evaluation Summary .
[LINK: Embedding Models Evaluation Summary](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/embedding_eval_summary.md)
[LINK: Reranker Models Evaluation Summary](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/reranker_eval_summary.md)
我们提供了 embedding 和 reranker 模型的指标可视化一键脚本，输出一个markdown文件，详见 Embedding模型指标汇总 和 Reranker模型指标汇总 。
[LINK: Embedding模型指标汇总](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/embedding_eval_summary.md)
[LINK: Reranker模型指标汇总](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/reranker_eval_summary.md)

### Evaluate RAG by LlamaIndex

LlamaIndex is a famous data framework for LLM-based applications, particularly in RAG. Recently, the LlamaIndex Blog has evaluated the popular embedding and reranker models in RAG pipeline and attract great attention. Now, we follow its pipeline to evaluate our BCEmbedding .
[LINK: LlamaIndex](https://github.com/run-llama/llama_index)
LlamaIndex 是一个著名的大模型应用的开源工具，在RAG中很受欢迎。最近， LlamaIndex博客 对市面上常用的embedding和reranker模型进行RAG流程的评测，吸引广泛关注。下面我们按照该评测流程验证 BCEmbedding 在RAG中的效果。
[LINK: LlamaIndex](https://github.com/run-llama/llama_index)
First, install LlamaIndex:
- Hit Rate: Hit rate calculates the fraction of queries where the correct answer is found within the top-k retrieved documents. In simpler terms, it's about how often our system gets it right within the top few guesses. The larger, the better.
Hit Rate:
Hit rate calculates the fraction of queries where the correct answer is found within the top-k retrieved documents. In simpler terms, it's about how often our system gets it right within the top few guesses. The larger, the better.
- Mean Reciprocal Rank (MRR): For each query, MRR evaluates the system's accuracy by looking at the rank of the highest-placed relevant document. Specifically, it's the average of the reciprocals of these ranks across all the queries. So, if the first relevant document is the top result, the reciprocal rank is 1; if it's second, the reciprocal rank is 1/2, and so on. The larger, the better. 命中率（Hit Rate） 命中率计算的是在检索的前k个文档中找到正确答案的查询所占的比例。简单来说，它反映了我们的系统在前几次猜测中答对的频率。 该指标越大越好。 平均倒数排名（Mean Reciprocal Rank，MRR） 对于每个查询，MRR通过查看最高排名的相关文档的排名来评估系统的准确性。具体来说，它是在所有查询中这些排名的倒数的平均值。因此，如果第一个相关文档是排名最靠前的结果，倒数排名就是1；如果是第二个，倒数排名就是1/2，依此类推。 该指标越大越好。
Mean Reciprocal Rank (MRR):
For each query, MRR evaluates the system's accuracy by looking at the rank of the highest-placed relevant document. Specifically, it's the average of the reciprocals of these ranks across all the queries. So, if the first relevant document is the top result, the reciprocal rank is 1; if it's second, the reciprocal rank is 1/2, and so on. The larger, the better.
- 命中率（Hit Rate） 命中率计算的是在检索的前k个文档中找到正确答案的查询所占的比例。简单来说，它反映了我们的系统在前几次猜测中答对的频率。 该指标越大越好。
命中率（Hit Rate）
命中率计算的是在检索的前k个文档中找到正确答案的查询所占的比例。简单来说，它反映了我们的系统在前几次猜测中答对的频率。 该指标越大越好。
- 平均倒数排名（Mean Reciprocal Rank，MRR） 对于每个查询，MRR通过查看最高排名的相关文档的排名来评估系统的准确性。具体来说，它是在所有查询中这些排名的倒数的平均值。因此，如果第一个相关文档是排名最靠前的结果，倒数排名就是1；如果是第二个，倒数排名就是1/2，依此类推。 该指标越大越好。
平均倒数排名（Mean Reciprocal Rank，MRR）
对于每个查询，MRR通过查看最高排名的相关文档的排名来评估系统的准确性。具体来说，它是在所有查询中这些排名的倒数的平均值。因此，如果第一个相关文档是排名最靠前的结果，倒数排名就是1；如果是第二个，倒数排名就是1/2，依此类推。 该指标越大越好。
In order to compare our BCEmbedding with other embedding and reranker models fairly, we provide a one-click script to reproduce results of the LlamaIndex Blog, including our BCEmbedding :
为了公平起见，运行下面脚本，复现LlamaIndex博客的结果，将 BCEmbedding 与其他embedding和reranker模型进行对比分析：
Then, sumarize the evaluation results by:
Results Reproduced from the LlamaIndex Blog can be checked in Reproduced Summary of RAG Evaluation , with some obvious conclusions :
[LINK: Reproduced Summary of RAG Evaluation](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/rag_eval_reproduced_summary.md)
- In WithoutReranker setting, our bce-embedding-base_v1 outperforms all the other embedding models.
In WithoutReranker setting, our bce-embedding-base_v1 outperforms all the other embedding models.
- With fixing the embedding model, our bce-reranker-base_v1 achieves the best performence.
With fixing the embedding model, our bce-reranker-base_v1 achieves the best performence.
- The combination of bce-embedding-base_v1 and bce-reranker-base_v1 is SOTA. 输出的指标汇总详见 *** LlamaIndex RAG评测结果复现 ***。从该复现结果中，可以看出： 在 WithoutReranker 设置下（ 竖排对比 ）， bce-embedding-base_v1 比其他embedding模型效果都要好。 在固定embedding模型设置下，对比不同reranker效果（ 横排对比 ）， bce-reranker-base_v1 比其他reranker模型效果都要好。 bce-embedding-base_v1 和 bce-reranker-base_v1 组合，表现SOTA。
The combination of bce-embedding-base_v1 and bce-reranker-base_v1 is SOTA.
输出的指标汇总详见 *** LlamaIndex RAG评测结果复现 ***。从该复现结果中，可以看出：
[LINK: LlamaIndex RAG评测结果复现](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/rag_eval_reproduced_summary.md)
- 在 WithoutReranker 设置下（ 竖排对比 ）， bce-embedding-base_v1 比其他embedding模型效果都要好。
- 在固定embedding模型设置下，对比不同reranker效果（ 横排对比 ）， bce-reranker-base_v1 比其他reranker模型效果都要好。
- bce-embedding-base_v1 和 bce-reranker-base_v1 组合，表现SOTA。
The evaluation of LlamaIndex Blog is monolingual, small amount of data, and specific domain (just including "llama2" paper). In order to evaluate the broad domain adaptability, bilingual and crosslingual capability , we follow the blog to build a multiple domains evaluation dataset (includding "Computer Science", "Physics", "Biology", "Economics", "Math", and "Quantitative Finance"), named CrosslingualMultiDomainsDataset , by OpenAI gpt-4-1106-preview for high quality .
在上述的 LlamaIndex博客 的评测数据只用了“llama2”这一篇文章，该评测是 单语种，小数据量，特定领域 的。为了兼容更真实更广的用户使用场景，评测算法模型的 领域泛化性，双语和跨语种能力 ，我们按照该博客的方法构建了一个多领域（计算机科学，物理学，生物学，经济学，数学，量化金融等）的双语种、跨语种评测数据， CrosslingualMultiDomainsDataset 。 为了保证构建数据的高质量，我们采用OpenAI的 gpt-4-1106-preview 。
First, run following cmd to evaluate the most popular and powerful embedding and reranker models:
Then, run the following script to sumarize the evaluation results:
The summary of multiple domains evaluations can be seen in Multiple Domains Scenarios .

## 📈 Leaderboard

### Semantic Representation Evaluations in MTEB

NOTE:
- Our bce-embedding-base_v1 outperforms other opensource embedding models with comparable model size.
Our bce-embedding-base_v1 outperforms other opensource embedding models with comparable model size.
- 114 datastes of "Retrieval", "STS", "PairClassification", "Classification", "Reranking" and "Clustering" in ["en", "zh", "en-zh", "zh-en"] setting.
114 datastes of "Retrieval", "STS", "PairClassification", "Classification", "Reranking" and "Clustering" in ["en", "zh", "en-zh", "zh-en"] setting.
- The crosslingual evaluation datasets we released belong to Retrieval task.
The crosslingual evaluation datasets we released belong to Retrieval task.
[LINK: crosslingual evaluation datasets](https://github.com/netease-youdao/BCEmbedding/blob/master/BCEmbedding/evaluation/c_mteb/Retrieval.py)
- More evaluation details please check Embedding Models Evaluation Summary . 要点： 对比其他开源的相同规模的embedding模型， bce-embedding-base_v1 表现最好，效果比最好的large模型稍差。 评测包含 "Retrieval"， "STS"， "PairClassification"， "Classification"， "Reranking"和"Clustering" 这六大类任务的共 114个数据集 。 我们开源的 跨语种语义表征评测数据 属于 Retrieval 任务。 更详细的评测结果详见 Embedding模型指标汇总 。
More evaluation details please check Embedding Models Evaluation Summary .
[LINK: Embedding Models Evaluation Summary](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/embedding_eval_summary.md)
要点：
- 对比其他开源的相同规模的embedding模型， bce-embedding-base_v1 表现最好，效果比最好的large模型稍差。
- 评测包含 "Retrieval"， "STS"， "PairClassification"， "Classification"， "Reranking"和"Clustering" 这六大类任务的共 114个数据集 。
- 我们开源的 跨语种语义表征评测数据 属于 Retrieval 任务。
[LINK: 跨语种语义表征评测数据](https://github.com/netease-youdao/BCEmbedding/blob/master/BCEmbedding/evaluation/c_mteb/Retrieval.py)
- 更详细的评测结果详见 Embedding模型指标汇总 。
[LINK: Embedding模型指标汇总](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/embedding_eval_summary.md)
NOTE:
- Our bce-reranker-base_v1 outperforms other opensource reranker models.
Our bce-reranker-base_v1 outperforms other opensource reranker models.
- 12 datastes of "Reranking" in ["en", "zh", "en-zh", "zh-en"] setting.
12 datastes of "Reranking" in ["en", "zh", "en-zh", "zh-en"] setting.
- More evaluation details please check Reranker Models Evaluation Summary . 要点： bce-reranker-base_v1 优于其他开源reranker模型。 评测包含 "Reranking" 任务的 12个数据集 。 更详细的评测结果详见 Reranker模型指标汇总
More evaluation details please check Reranker Models Evaluation Summary .
[LINK: Reranker Models Evaluation Summary](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/reranker_eval_summary.md)
要点：
- bce-reranker-base_v1 优于其他开源reranker模型。
- 评测包含 "Reranking" 任务的 12个数据集 。
- 更详细的评测结果详见 Reranker模型指标汇总
[LINK: Reranker模型指标汇总](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/EvaluationSummary/reranker_eval_summary.md)

### RAG Evaluations in LlamaIndex

NOTE:
- Evaluated in ["en", "zh", "en-zh", "zh-en"] setting .
Evaluated in ["en", "zh", "en-zh", "zh-en"] setting .
- In WithoutReranker setting, our bce-embedding-base_v1 outperforms all the other embedding models.
In WithoutReranker setting, our bce-embedding-base_v1 outperforms all the other embedding models.
- With fixing the embedding model, our bce-reranker-base_v1 achieves the best performence.
With fixing the embedding model, our bce-reranker-base_v1 achieves the best performence.
- The combination of bce-embedding-base_v1 and bce-reranker-base_v1 is SOTA . 要点： 评测是在 ["en", "zh", "en-zh", "zh-en"] 设置下。 在 WithoutReranker 设置下（ 竖排对比 ）， bce-embedding-base_v1 优于其他Embedding模型，包括开源和闭源。 在固定Embedding模型设置下，对比不同reranker效果（ 横排对比 ）， bce-reranker-base_v1 比其他reranker模型效果都要好，包括开源和闭源。 bce-embedding-base_v1 和 bce-reranker-base_v1 组合，表现SOTA。
The combination of bce-embedding-base_v1 and bce-reranker-base_v1 is SOTA .
要点：
- 评测是在 ["en", "zh", "en-zh", "zh-en"] 设置下。
- 在 WithoutReranker 设置下（ 竖排对比 ）， bce-embedding-base_v1 优于其他Embedding模型，包括开源和闭源。
- 在固定Embedding模型设置下，对比不同reranker效果（ 横排对比 ）， bce-reranker-base_v1 比其他reranker模型效果都要好，包括开源和闭源。
- bce-embedding-base_v1 和 bce-reranker-base_v1 组合，表现SOTA。

## 🛠 Youdao's BCEmbedding API

For users who prefer a hassle-free experience without the need to download and configure the model on their own systems, BCEmbedding is readily accessible through Youdao's API. This option offers a streamlined and efficient way to integrate BCEmbedding into your projects, bypassing the complexities of manual setup and maintenance. Detailed instructions and comprehensive API documentation are available at Youdao BCEmbedding API . Here, you'll find all the necessary guidance to easily implement BCEmbedding across a variety of use cases, ensuring a smooth and effective integration for optimal results.
[LINK: Youdao BCEmbedding API](https://ai.youdao.com/DOCSIRMA/html/aigc/api/embedding/index.html)
对于那些更喜欢直接调用api的用户，有道提供方便的 BCEmbedding 调用api。该方式是一种简化和高效的方式，将 BCEmbedding 集成到您的项目中，避开了手动设置和系统维护的复杂性。更详细的api调用接口说明详见 有道BCEmbedding API 。
[LINK: 有道BCEmbedding API](https://ai.youdao.com/DOCSIRMA/html/aigc/api/embedding/index.html)

## 🧲 WeChat Group

Welcome to scan the QR code below and join the WeChat group.
欢迎大家扫码加入官方微信交流群。

## ✏️ Citation

If you use BCEmbedding in your research or project, please feel free to cite and star it:
如果在您的研究或任何项目中使用本工作，烦请按照下方进行引用，并打个小星星～

## 🔐 License

BCEmbedding is licensed under Apache 2.0 License
[LINK: Apache 2.0 License](https://github.com/netease-youdao/BCEmbedding/blob/master/LICENSE)

## 🔗 Related Links

Netease Youdao - QAnything
[LINK: Netease Youdao - QAnything](https://github.com/netease-youdao/qanything)
FlagEmbedding
[LINK: FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)
MTEB
[LINK: MTEB](https://github.com/embeddings-benchmark/mteb)
C_MTEB
[LINK: C_MTEB](https://github.com/FlagOpen/FlagEmbedding/tree/master/C_MTEB)
LLama Index | LlamaIndex Blog
[LINK: LLama Index](https://github.com/run-llama/llama_index)

## Model tree for maidalun1020/bce-embedding-base_v1

## Spaces using maidalun1020/bce-embedding-base_v1 18

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
maidalun1020/bce-embedding-base_v1 is supported by the following Inference Providers:

--------------------