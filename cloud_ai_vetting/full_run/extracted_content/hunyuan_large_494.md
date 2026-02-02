# Hunyuan-Large
**URL:** https://huggingface.co/tencent/Tencent-Hunyuan-Large
**Page Title:** tencent/Tencent-Hunyuan-Large · Hugging Face
--------------------

GITHUB |    🖥️ official website ｜  🕖 HunyuanAPI ｜  🐳 Gitee
[LINK: GITHUB](https://github.com/Tencent/Tencent-Hunyuan-Large)
Technical Report ｜ Demo ｜ Tencent Cloud TI

### Model Introduction

With the rapid development of artificial intelligence technology, large language models (LLMs) have made significant progress in fields such as natural language processing, computer vision, and scientific tasks. However, as the scale of these models increases, optimizing resource consumption while maintaining high performance has become a key challenge. To address this challenge, we have explored Mixture of Experts (MoE) models. The currently unveiled Hunyuan-Large (Hunyuan-MoE-A52B) model is the largest open-source Transformer-based MoE model in the industry, featuring a total of 389 billion parameters and 52 billion active parameters. This is currently the largest open-source Transformer-based MoE model in the industry, featuring a total of 389 billion parameters and 52 billion active parameters.
By open-sourcing the Hunyuan-Large model and revealing related technical details, we hope to inspire more researchers with innovative ideas and collectively advance the progress and application of AI technology. We welcome you to join our open-source community to explore and optimize future AI models together!

### Introduction to Model Technical Advantages

- High-Quality Synthetic Data : By enhancing training with synthetic data, Hunyuan-Large can learn richer representations, handle long-context inputs, and generalize better to unseen data.
High-Quality Synthetic Data : By enhancing training with synthetic data, Hunyuan-Large can learn richer representations, handle long-context inputs, and generalize better to unseen data.
- KV Cache Compression : Utilizes Grouped Query Attention (GQA) and Cross-Layer Attention (CLA) strategies to significantly reduce memory usage and computational overhead of KV caches, improving inference throughput.
KV Cache Compression : Utilizes Grouped Query Attention (GQA) and Cross-Layer Attention (CLA) strategies to significantly reduce memory usage and computational overhead of KV caches, improving inference throughput.
- Expert-Specific Learning Rate Scaling : Sets different learning rates for different experts to ensure each sub-model effectively learns from the data and contributes to overall performance.
Expert-Specific Learning Rate Scaling : Sets different learning rates for different experts to ensure each sub-model effectively learns from the data and contributes to overall performance.
- Long-Context Processing Capability : The pre-trained model supports text sequences up to 256K, and the Instruct model supports up to 128K, significantly enhancing the ability to handle long-context tasks.
Long-Context Processing Capability : The pre-trained model supports text sequences up to 256K, and the Instruct model supports up to 128K, significantly enhancing the ability to handle long-context tasks.
- Extensive Benchmarking : Conducts extensive experiments across various languages and tasks to validate the practical effectiveness and safety of Hunyuan-Large.
Extensive Benchmarking : Conducts extensive experiments across various languages and tasks to validate the practical effectiveness and safety of Hunyuan-Large.

## Benchmark Evaluation

Hunyuan-Large pre-trained model achieves the best overall performance compared to both Dense and MoE based 
competitors having similar activated parameter sizes.  For aggregated benchmarks such as MMLU, MMLU-Pro, and CMMLU, 
Hunyuan-Large consistently achieves the best performance, confirming its comprehensive abilities on aggregated tasks.
Hunyuan-Large also shows superior performance in commonsense understanding and reasoning, and classical NLP tasks 
such as QA and reading comprehension tasks (e.g., CommonsenseQA, PIQA and TriviaQA). For the mathematics capability, Hunyuan-Large outperforms all baselines in math datasets of GSM8K and MATH, 
and also gains the best results on CMATH in Chinese.We also observe that Hunyuan-Large achieves the overall 
best performance in all Chinese tasks (e.g., CMMLU, C-Eval).
Hunyuan-Large-Instruct achieves consistent improvements on most types of tasks compared to LLMs having similar 
activated parameters, indicating the effectiveness of our post-training.    Delving into the model performance 
in different categories of benchmarks, we find that our instruct model achieves the best performance on MMLU and MATH dataset. Notably, on the MMLU dataset, our model demonstrates a significant improvement, outperforming the LLama3.1-405B model by 2.6%. This enhancement is not just marginal but indicative of the Hunyuan-Large-Instruct’s superior understanding and reasoning 
capabilities across a wide array of language understanding tasks. The model’s prowess is further underscored in its performance 
on the MATH dataset, where it surpasses the LLama3.1-405B by a notable margin of 3.6%. Remarkably, this leap in accuracy is achieved with only 52 billion activated parameters, underscoring the efficiency of our model.

## Quick Start

You can quickly get started by referring to the content in the Quick Start Guide .
[LINK: Quick Start Guide](https://github.com/Tencent/Tencent-Hunyuan-Large/tree/main/examples)

## Inference and Deployment

HunyuanLLM uses TRT-LLM and vLLM for deployment. We are open sourcing the vLLM deployment (see Reasoning with vLLM), and the TRT-LLM deployment (see Reasoning with TRT-LLM) will be available in the near future.
Learn More at Tencent-Hunyuan-Large .
[LINK: Tencent-Hunyuan-Large](https://github.com/Tencent/Tencent-Hunyuan-Large)

### Citation

If you find our work helpful, feel free to give us a cite.

## Model tree for tencent/Tencent-Hunyuan-Large

## Spaces using tencent/Tencent-Hunyuan-Large 28

## Paper for tencent/Tencent-Hunyuan-Large


--------------------