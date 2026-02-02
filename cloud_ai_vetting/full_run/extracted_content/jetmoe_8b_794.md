# JetMoE-8B
**URL:** https://huggingface.co/jetmoe/jetmoe-8b
**Page Title:** jetmoe/jetmoe-8b · Hugging Face
--------------------


## JetMoE: Reaching LLaMA2 Performance with 0.1M Dollars

## Key Messages

- JetMoE-8B is trained with less than $ 0.1 million 1 cost but outperforms LLaMA2-7B from Meta AI , who has multi-billion-dollar training resources. LLM training can be much cheaper than people previously thought .
JetMoE-8B is trained with less than $ 0.1 million 1 cost but outperforms LLaMA2-7B from Meta AI , who has multi-billion-dollar training resources. LLM training can be much cheaper than people previously thought .
- JetMoE-8B is fully open-sourced and academia-friendly because: It only uses public datasets for training, and the code is open-sourced. No proprietary resource is needed. It can be finetuned with very limited compute budget (e.g., consumer-grade GPU) that most labs can afford.
JetMoE-8B is fully open-sourced and academia-friendly because:
- It only uses public datasets for training, and the code is open-sourced. No proprietary resource is needed.
- It can be finetuned with very limited compute budget (e.g., consumer-grade GPU) that most labs can afford.
- JetMoE-8B only has 2.2B active parameters during inference, which drastically lowers the computational cost. Compared to a model with similar inference computation, like Gemma-2B, JetMoE-8B achieves constantly better performance.
JetMoE-8B only has 2.2B active parameters during inference, which drastically lowers the computational cost. Compared to a model with similar inference computation, like Gemma-2B, JetMoE-8B achieves constantly better performance.
1 We used a 96×H100 GPU cluster for 2 weeks, which cost ~$0.08 million.
Website: https://research.myshell.ai/jetmoe
HuggingFace: https://huggingface.co/jetmoe/jetmoe-8b
Online Demo on Lepton AI: https://www.lepton.ai/playground/chat?model=jetmoe-8b-chat
Technical Report: https://arxiv.org/pdf/2404.07413.pdf

## Authors

The project is contributed by Yikang Shen , Zhen Guo , Tianle Cai and Zengyi Qin . For technical inquiries, please contact Yikang Shen . For media and collaboration inquiries, please contact Zengyi Qin .
[LINK: Zhen Guo](https://zguo0525.github.io/)

## Collaboration

If you have great ideas but need more resources (GPU, data, funding, etc.) , welcome to contact MyShell.ai via Zengyi Qin . MyShell.ai is open to collaborations and are actively supporting high-quality open-source projects.

## Benchmarks

We use the same evaluation methodology as in the Open LLM leaderboard. For MBPP code benchmark, we use the same evaluation methodology as in the LLaMA2 and Deepseek-MoE paper. The results are shown below:
To our surprise, despite the lower training cost and computation, JetMoE-8B performs even better than LLaMA2-7B, LLaMA-13B, and DeepseekMoE-16B. Compared to a model with similar training and inference computation, like Gemma-2B, JetMoE-8B achieves better performance.

## Model Usage

To load the models, you need install this package :
[LINK: this package](https://github.com/myshell-ai/JetMoE)
Then you can load the model with the following code:

## Model Details

JetMoE-8B has 24 blocks. 
Each block has two MoE layers: Mixture of Attention heads (MoA) and Mixture of MLP Experts (MoE).
Each MoA and MoE layer has 8 expert, and 2 experts are activated for each input token.
It has 8 billion parameters in total and 2.2B active parameters. 
JetMoE-8B is trained on 1.25T tokens from publicly available datasets, with a learning rate of 5.0 x 10 -4 and a global batch-size of 4M tokens.

## Training Details

Our training recipe follows the MiniCPM 's two-phases training method. Phase 1 uses a constant learning rate with linear warmup and is trained on 1 trillion tokens from large-scale open-source pretraining datasets, including RefinedWeb, Pile, Github data, etc. Phase 2 uses exponential learning rate decay and is trained on 250 billion tokens from phase 1 datasets and extra high-quality open-source datasets.

## Technical Report

For more details, please refer to the JetMoE Technical Report .

## JetMoE Model Index

## Acknowledgement

We express our gratitude to Shengding Hu for his valuable advice on the Phase 2 data mixture. We also express our gratitude to Exabits for their assistance in setting up the GPU clusters, and to Lepton AI for their support in setting up the chat demo.
[LINK: Shengding Hu](https://shengdinghu.github.io/)

## Model tree for jetmoe/jetmoe-8b

## Paper for jetmoe/jetmoe-8b


--------------------