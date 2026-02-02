# Internlm3-8b-instruct
**URL:** https://huggingface.co/internlm/internlm3-8b-instruct
**Page Title:** internlm/internlm3-8b-instruct · Hugging Face
--------------------


## InternLM

💻Github Repo • 🤗Demo • 🤔Reporting Issues • 📜Technical Report
[LINK: 💻Github Repo](https://github.com/InternLM/InternLM)
[LINK: 🤔Reporting Issues](https://github.com/InternLM/InternLM/issues/new)
👋 join us on Discord and WeChat
[LINK: WeChat](https://github.com/InternLM/InternLM/assets/25839884/a6aad896-7232-4220-ac84-9e070c2633ce)

## Introduction

InternLM3 has open-sourced an 8-billion parameter instruction model, InternLM3-8B-Instruct, designed for general-purpose usage and advanced reasoning. This model has the following characteristics:
- Enhanced performance at reduced cost : 
State-of-the-art performance on reasoning and knowledge-intensive tasks surpass models like Llama3.1-8B and Qwen2.5-7B. Remarkably, InternLM3 is trained on only 4 trillion high-quality tokens, saving more than 75% of the training cost compared to other LLMs of similar scale.
- Deep thinking capability :
InternLM3 supports both the deep thinking mode for solving complicated reasoning tasks via the long chain-of-thought and the normal response mode for fluent user interactions.

## InternLM3-8B-Instruct

### Performance Evaluation

We conducted a comprehensive evaluation of InternLM using the open-source evaluation tool OpenCompass . The evaluation covered five dimensions of capabilities: disciplinary competence, language competence, knowledge competence, inference competence, and comprehension competence. Here are some of the evaluation results, and you can visit the OpenCompass leaderboard for more evaluation results.
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
- Values marked in bold indicate the highest in open source models
- The evaluation results were obtained from OpenCompass (some data marked with *, which means evaluating with Thinking Mode), and evaluation configuration can be found in the configuration files provided by OpenCompass .
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
- The evaluation data may have numerical differences due to the version iteration of OpenCompass , so please refer to the latest evaluation results of OpenCompass .
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
Limitations: Although we have made efforts to ensure the safety of the model during the training process and to encourage the model to generate text that complies with ethical and legal requirements, the model may still produce unexpected outputs due to its size and probabilistic generation paradigm. For example, the generated responses may contain biases, discrimination, or other harmful content. Please do not propagate such content. We are not responsible for any consequences resulting from the dissemination of harmful information.

### Requirements

### Conversation Mode

To load the InternLM3 8B Instruct model using Transformers, use the following code:
LMDeploy is a toolkit for compressing, deploying, and serving LLM, developed by the MMRazor and MMDeploy teams.
You can run batch inference locally with the following python code:
Or you can launch an OpenAI compatible server with the following command:
Then you can send a chat request to the server:
Find more details in the LMDeploy documentation
[LINK: LMDeploy documentation](https://lmdeploy.readthedocs.io/en/latest/)
First install ollama,
inference code,
Refer to installation to install the latest code of vllm
[LINK: installation](https://docs.vllm.ai/en/latest/getting_started/installation/index.html)
inference code:

### Thinking Mode

LMDeploy is a toolkit for compressing, deploying, and serving LLM.
You can run batch inference locally with the following python code:
First install ollama,
inference code,
Refer to installation to install the latest code of vllm
[LINK: installation](https://docs.vllm.ai/en/latest/getting_started/installation/index.html)
inference code

## Open Source License

Code and model weights are licensed under Apache-2.0.

## Citation

### InternLM3-8B-Instruct

InternLM3，即书生·浦语大模型第3代，开源了80亿参数，面向通用使用与高阶推理的指令模型（InternLM3-8B-Instruct）。模型具备以下特点：
- 更低的代价取得更高的性能 :
在推理、知识类任务上取得同量级最优性能，超过Llama3.1-8B和Qwen2.5-7B。值得关注的是InternLM3只用了4万亿词元进行训练，对比同级别模型训练成本节省75%以上。
- 深度思考能力 :
InternLM3支持通过长思维链求解复杂推理任务的深度思考模式，同时还兼顾了用户体验更流畅的通用回复模式。
我们使用开源评测工具 OpenCompass 从学科综合能力、语言能力、知识能力、推理能力、理解能力五大能力维度对InternLM开展全面评测，部分评测结果如下表所示，欢迎访问 OpenCompass 榜单 获取更多的评测结果。
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
- 表中标粗的数值表示在对比的开源模型中的最高值。
- 以上评测结果基于 OpenCompass 获得(部分数据标注 * 代表使用深度思考模式进行评测)，具体测试细节可参见 OpenCompass 中提供的配置文件。
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
- 评测数据会因 OpenCompass 的版本迭代而存在数值差异，请以 OpenCompass 最新版的评测结果为主。
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
[LINK: OpenCompass](https://github.com/internLM/OpenCompass/)
局限性： 尽管在训练过程中我们非常注重模型的安全性，尽力促使模型输出符合伦理和法律要求的文本，但受限于模型大小以及概率生成范式，模型可能会产生各种不符合预期的输出，例如回复内容包含偏见、歧视等有害内容，请勿传播这些内容。由于传播不良信息导致的任何后果，本项目不承担责任。
通过以下的代码加载  InternLM3 8B Instruct 模型
LMDeploy 是涵盖了 LLM 任务的全套轻量化、部署和服务解决方案。
你可以使用以下 python 代码进行本地批量推理:
或者你可以使用以下命令启动兼容 OpenAI API 的服务:
然后你可以向服务端发起一个聊天请求:
更多信息请查看 LMDeploy 文档
[LINK: LMDeploy 文档](https://lmdeploy.readthedocs.io/en/latest/)
准备工作
推理代码
参考 文档 安装 vllm 最新代码
推理代码
LMDeploy is a toolkit for compressing, deploying, and serving LLM, developed by the MMRazor and MMDeploy teams.
You can run batch inference locally with the following python code:
准备工作
inference code,
参考 文档 安装 vllm 最新代码
推理代码

## 开源许可证

本仓库的代码和权重依照 Apache-2.0 协议开源。

## Model tree for internlm/internlm3-8b-instruct

## Spaces using internlm/internlm3-8b-instruct 12

## Collection including internlm/internlm3-8b-instruct

## Paper for internlm/internlm3-8b-instruct


--------------------