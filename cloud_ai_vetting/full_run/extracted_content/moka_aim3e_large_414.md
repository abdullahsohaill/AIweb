# moka-ai/m3e-large
**URL:** https://huggingface.co/moka-ai/m3e-large
**Page Title:** moka-ai/m3e-large · Hugging Face
--------------------


## M3E Models

m3e-small | m3e-base | m3e-large
M3E 是 Moka Massive Mixed Embedding 的缩写
- Moka，此模型由 MokaAI 训练，开源和评测，训练脚本使用 uniem ，评测 BenchMark 使用 MTEB-zh
[LINK: uniem](https://github.com/wangyuxinwhy/uniem/blob/main/scripts/train_m3e.py)
[LINK: MTEB-zh](https://github.com/wangyuxinwhy/uniem/tree/main/mteb-zh)
- Massive，此模型通过 千万级 (2200w+) 的中文句对数据集进行训练
- Mixed，此模型支持中英双语的同质文本相似度计算，异质文本检索等功能，未来还会支持代码检索
- Embedding，此模型是文本嵌入模型，可以将自然语言转换成稠密的向量

## 更新说明

- 2023.06.14，添加了三个中文开源文本嵌入模型到评测中，包括 UER, ErLangShen, DMetaSoul
- 2023.06.08，添加检索任务的评测结果，在 T2Ranking 1W 中文数据集上，m3e-base 在 ndcg@10 上达到了 0.8004，超过了 openai-ada-002 的 0.7786
- 2023.06.07，添加文本分类任务的评测结果，在 6 种文本分类数据集上，m3e-base 在 accuracy 上达到了 0.6157，超过了 openai-ada-002 的 0.5956

## 模型对比

说明：
- s2s, 即 sentence to sentence ，代表了同质文本之间的嵌入能力，适用任务：文本相似度，重复问题检测，文本分类等
- s2p, 即 sentence to passage ，代表了异质文本之间的嵌入能力，适用任务：文本检索，GPT 记忆模块等
- s2c, 即 sentence to code ，代表了自然语言和程序语言之间的嵌入能力，适用任务：代码检索
- 兼容性，代表了模型在开源社区中各种项目被支持的程度，由于 m3e 和 text2vec 都可以直接通过 sentence-transformers 直接使用，所以和 openai 在社区的支持度上相当
- ACC & ndcg@10，详情见下方的评测
Tips:
- 使用场景主要是中文，少量英文的情况，建议使用 m3e 系列的模型
- 多语言使用场景，并且不介意数据隐私的话，我建议使用 openai text-embedding-ada-002
- 代码检索场景，推荐使用 openai text-embedding-ada-002
- 文本检索场景，请使用具备文本检索能力的模型，只在 S2S 上训练的文本嵌入模型，没有办法完成文本检索任务

## 使用方式

您需要先安装 sentence-transformers
安装完成后，您可以使用以下代码来使用 M3E Models
M3E 系列的所有模型在设计的时候就考虑到完全兼容 sentence-transformers ，所以你可以通过 替换名称字符串 的方式在所有支持 sentence-transformers 的项目中 无缝 使用 M3E Models，比如 chroma , guidance , semantic-kernel 。
[LINK: chroma](https://docs.trychroma.com/getting-started)
[LINK: guidance](https://github.com/microsoft/guidance)
[LINK: semantic-kernel](https://github.com/microsoft/semantic-kernel)

## 训练方案

M3E 使用 in-batch 负采样的对比学习的方式在句对数据集进行训练，为了保证 in-batch 负采样的效果，我们使用 A100 80G 来最大化 batch-size，并在共计 2200W+ 的句对数据集上训练了 1 epoch。训练脚本使用 uniem ，您可以在这里查看具体细节。
[LINK: uniem](https://github.com/wangyuxinwhy/uniem/blob/main/scripts/train_m3e.py)
- 中文训练集，M3E 在大规模句对数据集上的训练，包含中文百科，金融，医疗，法律，新闻，学术等多个领域共计 2200W 句对样本，数据集详见 M3E 数据集
- 英文训练集，M3E 使用 MEDI 145W 英文三元组数据集进行训练，数据集详见 MEDI 数据集 ，此数据集由 instructor team 提供
[LINK: instructor team](https://github.com/HKUNLP/instructor-embedding)
- 指令数据集，M3E 使用了 300W + 的指令微调数据集，这使得 M3E 对文本编码的时候可以遵从指令，这部分的工作主要被启发于 instructor-embedding
[LINK: instructor-embedding](https://github.com/HKUNLP/instructor-embedding)
- 基础模型，M3E 使用 hfl 实验室的 Roberta 系列模型进行训练，目前提供  small、base和large三个版本，大家则需选用
- ALL IN ONE，M3E 旨在提供一个 ALL IN ONE 的文本嵌入模型，不仅支持同质句子相似度判断，还支持异质文本检索，你只需要一个模型就可以覆盖全部的应用场景，未来还会支持代码检索
- 评测模型， text2vec , m3e-base, m3e-small, openai text-embedding-ada-002, DMetaSoul , UER , ErLangShen
[LINK: text2vec](https://github.com/shibing624/text2vec)
- 评测脚本，具体参考 [MTEB-zh] ( https://github.com/wangyuxinwhy/uniem/blob/main/mteb-zh )
[LINK: https://github.com/wangyuxinwhy/uniem/blob/main/mteb-zh](https://github.com/wangyuxinwhy/uniem/blob/main/mteb-zh)

### 文本分类

- 数据集选择，选择开源在 HuggingFace 上的 6 种文本分类数据集，包括新闻、电商评论、股票评论、长文本等
- 评测方式，使用 MTEB 的方式进行评测，报告 Accuracy。

### 检索排序

- 数据集选择，使用 T2Ranking 数据集，由于 T2Ranking 的数据集太大，openai 评测起来的时间成本和 api 费用有些高，所以我们只选择了 T2Ranking 中的前 10000 篇文章
[LINK: T2Ranking](https://github.com/THUIR/T2Ranking/tree/main)
- 评测方式，使用 MTEB 的方式进行评测，报告 map@1, map@10, mrr@1, mrr@10, ndcg@1, ndcg@10
- 注意！从实验结果和训练方式来看，除了 M3E 模型和 openai 模型外，其余模型都没有做检索任务的训练，所以结果仅供参考。
- 数据集选择，使用 T2Ranking，刨除 openai-ada-002 模型后，我们对剩余的三个模型，进行 T2Ranking 10W 和 T2Ranking 50W 的评测。（T2Ranking 评测太耗内存了... 128G 都不行）
- 评测方式，使用 MTEB 的方式进行评测，报告 ndcg@10
说明：
- 检索排序对于 text2vec 并不公平，因为 text2vec 在训练的时候没有使用过检索相关的数据集，所以没有办法很好的完成检索任务也是正常的。

## M3E数据集

如果您想要使用这些数据集，你可以在 uniem process_zh_datasets 中找到加载 huggingface 数据集的脚本，非 huggingface 数据集需要您根据下方提供的链接自行下载和处理。
[LINK: uniem process_zh_datasets](https://github.com/wangyuxinwhy/uniem/blob/main/scripts/process_zh_datasets.py)
[LINK: https://github.com/ymcui/cmrc2018/blob/master/README_CN.md](https://github.com/ymcui/cmrc2018/blob/master/README_CN.md)
[LINK: https://github.com/brightmart/nlp_chinese_corpus](https://github.com/brightmart/nlp_chinese_corpus)
[LINK: https://github.com/brightmart/nlp_chinese_corpus](https://github.com/brightmart/nlp_chinese_corpus)
[LINK: https://github.com/brightmart/nlp_chinese_corpus](https://github.com/brightmart/nlp_chinese_corpus)
[LINK: https://github.com/CLUEbenchmark/SimCLUE](https://github.com/CLUEbenchmark/SimCLUE)
[LINK: https://github.com/pluto-junzeng/ChineseSquad](https://github.com/pluto-junzeng/ChineseSquad)

## 计划表

- 完成 MTEB 中文评测 BenchMark, MTEB-zh
[LINK: MTEB-zh](https://github.com/wangyuxinwhy/uniem/tree/main/mteb-zh)
- 完成 Large 模型的训练和开源
- 完成支持代码检索的模型
- 对 M3E 数据集进行清洗，保留高质量的部分，组成 m3e-hq，并在 huggingface 上开源
- 在 m3e-hq 的数据集上补充 hard negative 的样本及相似度分数，组成 m3e-hq-with-score，并在 huggingface 上开源
- 在 m3e-hq-with-score 上通过 cosent loss loss 进行训练并开源模型，CoSent 原理参考这篇 博客
[LINK: cosent loss](https://github.com/wangyuxinwhy/uniem/blob/main/uniem/criteria.py#LL24C39-L24C39)
- 开源商用版本的 M3E models
感谢开源社区提供的中文语料，感谢所有在此工作中提供帮助的人们，希望中文社区越来越好，共勉！

## License

M3E models 使用的数据集中包括大量非商用的数据集，所以 M3E models 也是非商用的，仅供研究使用。不过我们已经在 M3E 数据集上标识了商用和非商用的数据集，您可以根据自己的需求自行训练。

## Citation

Please cite this model using the following format:
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Spaces using moka-ai/m3e-large 13


--------------------