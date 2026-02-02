# Baichuan-7B
**URL:** https://huggingface.co/baichuan-inc/baichuan-7B
**Page Title:** baichuan-inc/Baichuan-7B · Hugging Face
--------------------


## Baichuan-7B

Baichuan-7B是由百川智能开发的一个开源的大规模预训练模型。基于Transformer结构，在大约1.2万亿tokens上训练的70亿参数模型，支持中英双语，上下文窗口长度为4096。在标准的中文和英文权威benchmark（C-EVAL/MMLU）上均取得同尺寸最好的效果。
如果希望使用Baichuan-7B（如进行推理、Finetune等），我们推荐使用配套代码库 Baichuan-7B 。
[LINK: Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)
Baichuan-7B is an open-source large-scale pre-trained model developed by Baichuan Intelligent Technology. Based on the Transformer architecture, it is a model with 7 billion parameters trained on approximately 1.2 trillion tokens. It supports both Chinese and English, with a context window length of 4096. It achieves the best performance of its size on standard Chinese and English authoritative benchmarks (C-EVAL/MMLU).
If you wish to use Baichuan-7B (for inference, finetuning, etc.), we recommend using the accompanying code library Baichuan-7B .
[LINK: Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)

## Why use Baichuan-7B

- 在同尺寸模型中Baichuan-7B达到了目前SOTA的水平，参考下面MMLU指标
在同尺寸模型中Baichuan-7B达到了目前SOTA的水平，参考下面MMLU指标
- Baichuan-7B使用自有的中英文双语语料进行训练，在中文上进行优化，在C-Eval达到SOTA水平
Baichuan-7B使用自有的中英文双语语料进行训练，在中文上进行优化，在C-Eval达到SOTA水平
- 不同于LLaMA完全禁止商业使用，Baichuan-7B使用更宽松的开源协议，允许用于商业目的
不同于LLaMA完全禁止商业使用，Baichuan-7B使用更宽松的开源协议，允许用于商业目的
- Among models of the same size, Baichuan-7B has achieved the current state-of-the-art (SOTA) level, as evidenced by the following MMLU metrics.
Among models of the same size, Baichuan-7B has achieved the current state-of-the-art (SOTA) level, as evidenced by the following MMLU metrics.
- Baichuan-7B is trained on proprietary bilingual Chinese-English corpora, optimized for Chinese, and achieves SOTA performance on C-Eval.
Baichuan-7B is trained on proprietary bilingual Chinese-English corpora, optimized for Chinese, and achieves SOTA performance on C-Eval.
- Unlike LLaMA, which completely prohibits commercial use, Baichuan-7B employs a more lenient open-source license, allowing for commercial purposes.
Unlike LLaMA, which completely prohibits commercial use, Baichuan-7B employs a more lenient open-source license, allowing for commercial purposes.

## How to Get Started with the Model

如下是一个使用Baichuan-7B进行1-shot推理的任务，根据作品给出作者名，正确输出为"夜雨寄北->李商隐"
The following is a task of performing 1-shot inference using Baichuan-7B, where the author's name is given based on the work, with the correct output being "One Hundred Years of Solitude->Gabriel Garcia Marquez"

## Model Details

### Model Description

- Developed by: 百川智能(Baichuan Intelligent Technology)
- Email : opensource@baichuan-inc.com
- Language(s) (NLP): Chinese/English
- License: Baichuan-7B License

### Model Sources

整体模型基于标准的Transformer结构，我们采用了和LLaMA一样的模型设计
- Position Embedding ：采用rotary-embedding，是现阶段被大多数模型采用的位置编码方案，具有很好的外推性。
- Feedforward Layer ：采用SwiGLU，Feedforward变化为(8/3)倍的隐含层大小，即11008。
- Layer Normalization : 基于 RMSNorm 的Pre-Normalization。
具体参数和见下表
The overall model is based on the standard Transformer structure, and we have adopted the same model design as LLaMA:
- Position Embedding: We use rotary-embedding, which is the position encoding scheme adopted by most models at this stage, and it has excellent extrapolation capabilities.
- Feedforward Layer: We use SwiGLU. The feedforward changes to (8/3) times the size of the hidden layer, that is, 11008.
- Layer Normalization: Pre-Normalization based on RMSNorm .
The specific parameters are as follows:

## Uses

### Downstream Use

我们同时开源出了和本模型配套的训练代码，允许进行高效的Finetune用于下游任务，具体参见 Baichuan-7B 。
[LINK: Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)
We have also open-sourced the training code that accompanies this model, allowing for efficient finetuning for downstream tasks. For more details, please refer to Baichuan-7B .
[LINK: Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)

### Out-of-Scope Use

在没有充分评估风险和采取缓解措施的情况下投入生产使用；任何可能被视为不负责任或有害的使用案例。
Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful.

## Bias, Risks, and Limitations

Baichuan-7B可能会产生事实上不正确的输出，不应依赖它产生事实上准确的信息。Baichuan-7B是在各种公共数据集上进行训练的。尽管我们已经做出了巨大的努力来清洗预训练数据，但这个模型可能会生成淫秽、偏见或其他冒犯性的输出。
Baichuan-7B can produce factually incorrect output, and should not be relied on to produce factually accurate information. Baichuan-7B was trained on various public datasets. While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

## Training Details

训练具体设置参见 Baichuan-7B 。
[LINK: Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)
For specific training settings, please refer to Baichuan-7B .
[LINK: Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)

## Evaluation

### 中文评测

CEval数据集 是一个全面的中文基础模型评测数据集，涵盖了52个学科和四个难度的级别。我们使用该数据集的dev集作为few-shot的来源，在test集上进行了5-shot测试。
Gaokao 是一个以中国高考题作为评测大语言模型能力的数据集，用以评估模型的语言能力和逻辑推理能力。
我们只保留了其中的单项选择题，并对所有模型进行统一5-shot测试。
[LINK: Gaokao](https://github.com/ExpressAI/AI-Gaokao)
以下是测试的结果。
AGIEval 旨在评估模型的认知和解决问题相关的任务中的一般能力。
我们只保留了其中的四选一单项选择题，随机划分后对所有模型进行了统一5-shot测试。
[LINK: AGIEval](https://github.com/microsoft/AGIEval)
* 其中Aquila模型来源于 智源官方网站 ，仅做参考

### English Leaderboard

In addition to Chinese, we also tested the model's performance in English.
MMLU is an English evaluation dataset that includes 57 multiple-choice tasks, covering elementary mathematics, American history, computer science, law, etc. The difficulty ranges from high school level to expert level, making it a mainstream LLM evaluation dataset.
We adopted the open-source evaluation scheme, and the final 5-shot results are as follows:
[LINK: open-source](/baichuan-inc/Baichuan-7B/blob/main/(https://github.com/hendrycks/test))
The superscript in the Model column indicates the source of the results.

## Our Group

## Model tree for baichuan-inc/Baichuan-7B

## Spaces using baichuan-inc/Baichuan-7B 62

## Papers for baichuan-inc/Baichuan-7B


--------------------