# DeepSeek-V3.2-Exp
**URL:** https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp
**Page Title:** deepseek-ai/DeepSeek-V3.2-Exp · Hugging Face
--------------------


## DeepSeek-V3.2-Exp

## Introduction

We are excited to announce the official release of DeepSeek-V3.2-Exp, an experimental version of our model. As an intermediate step toward our next-generation architecture, V3.2-Exp builds upon V3.1-Terminus by introducing DeepSeek Sparse Attention—a sparse attention mechanism designed to explore and validate optimizations for training and inference efficiency in long-context scenarios.
This experimental release represents our ongoing research into more efficient transformer architectures, particularly focusing on improving computational efficiency when processing extended text sequences.
- DeepSeek Sparse Attention (DSA) achieves fine-grained sparse attention for the first time, delivering substantial improvements in long-context training and inference efficiency while maintaining virtually identical model output quality.
DeepSeek Sparse Attention (DSA) achieves fine-grained sparse attention for the first time, delivering substantial improvements in long-context training and inference efficiency while maintaining virtually identical model output quality.
- To rigorously evaluate the impact of introducing sparse attention, we deliberately aligned the training configurations of DeepSeek-V3.2-Exp with V3.1-Terminus. Across public benchmarks in various domains, DeepSeek-V3.2-Exp demonstrates performance on par with V3.1-Terminus.
To rigorously evaluate the impact of introducing sparse attention, we deliberately aligned the training configurations of DeepSeek-V3.2-Exp with V3.1-Terminus. Across public benchmarks in various domains, DeepSeek-V3.2-Exp demonstrates performance on par with V3.1-Terminus.

## Update

- 2025.11.17: We have identified that previous versions of the inference demo code contained an implementation discrepancy in Rotary Position Embedding (RoPE) within the indexer module, potentially leading to degraded model performance. Specifically, the input tensor to RoPE in the indexer module requires a non-interleaved layout, whereas RoPE in the MLA module expects an interleaved layout. This issue has now been resolved. Please refer to the updated version of the inference demo code and take note of this implementation detail.

## How to Run Locally

### HuggingFace

We provide an updated inference demo code in the inference folder to help the community quickly get started with our model and understand its architectural details.
First convert huggingface model weights to the the format required by our inference demo. Set MP to match your available GPU count:
Launch the interactive chat interface and start exploring DeepSeek's capabilities:

### SGLang

### vLLM

vLLM provides day-0 support of DeepSeek-V3.2-Exp. See the recipes for up-to-date details.
[LINK: recipes](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2-Exp.html)

## Open-Source Kernels

For TileLang kernels with better readability and research-purpose design , please refer to TileLang .
[LINK: TileLang](https://github.com/tile-ai/tilelang/tree/main/examples/deepseek_v32)
For high-performance CUDA kernels , indexer logit kernels (including paged versions) are available in DeepGEMM . Sparse attention kernels are released in FlashMLA .
[LINK: DeepGEMM](https://github.com/deepseek-ai/DeepGEMM/pull/200)
[LINK: FlashMLA](https://github.com/deepseek-ai/FlashMLA/pull/98)

## License

This repository and the model weights are licensed under the MIT License .

## Citation

## Contact

If you have any questions, please raise an issue or contact us at service@deepseek.com .

## Model tree for deepseek-ai/DeepSeek-V3.2-Exp

Base model

## Spaces using deepseek-ai/DeepSeek-V3.2-Exp 100

## Collection including deepseek-ai/DeepSeek-V3.2-Exp

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
deepseek-ai/DeepSeek-V3.2-Exp is supported by the following Inference Providers:

--------------------