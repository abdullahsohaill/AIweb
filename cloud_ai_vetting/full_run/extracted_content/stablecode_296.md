# StableCode
**URL:** https://huggingface.co/stabilityai/stablecode-completion-alpha-3b-4k
**Page Title:** stabilityai/stablecode-completion-alpha-3b-4k · Hugging Face
--------------------


## StableCode-Completion-Alpha-3B-4K

## Model Description

StableCode-Completion-Alpha-3B-4K is a 3 billion parameter decoder-only code completion model pre-trained on diverse set of programming languages that topped the stackoverflow developer survey.

## Usage

The model is intended to do single/multiline code completion from a long context window upto 4k tokens.
Get started generating code with StableCode-Completion-Alpha-3B-4k by using the following code snippet:

## Model Details

- Developed by : Stability AI
- Model type : StableCode-Completion-Alpha-3B-4k models are auto-regressive language models based on the transformer decoder architecture.
- Language(s) : Code
- Library : GPT-NeoX
[LINK: GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
- License : Model checkpoints are licensed under the Apache 2.0 license.
- Contact : For questions and comments about the model, please email lm@stability.ai

### Model Architecture

- Decoder Layer : Parallel Attention and MLP residuals with a single input LayerNorm ( Wang & Komatsuzaki, 2021 )
[LINK: Wang & Komatsuzaki, 2021](https://github.com/kingoflolz/mesh-transformer-jax/tree/master)
- Position Embeddings : Rotary Position Embeddings ( Su et al., 2021 )
- Bias : LayerNorm bias terms only

## Training

StableCode-Completion-Alpha-3B-4k is pre-trained at a context length of 4096 for 300 billion tokens on the bigcode/starcoder-data .

### Training Dataset

The first pre-training stage relies on 300B tokens sourced from various top programming languages occuring in the stackoverflow developer survey present in the starcoder-data dataset.

### Training Procedure

The model is pre-trained on the dataset mixes mentioned above in mixed-precision BF16), optimized with AdamW, and trained using the StarCoder tokenizer with a vocabulary size of 49k.
- Software : We use a fork of gpt-neox ( EleutherAI, 2021 ) and train under 2D parallelism (Data and Tensor Parallel) with ZeRO-1 ( Rajbhandari et al., 2019 ) and rely on flash-attention as well as rotary embedding kernels from FlashAttention-2 ( Dao et al., 2023 )
[LINK: EleutherAI, 2021](https://github.com/EleutherAI/gpt-neox)

## Use and Limitations

### Intended Use

StableCode-Completion-Alpha-3B-4K independently generates new code completions, but we recommend that you use StableCode-Completion-Alpha-3B-4K together with the tool developed by BigCode and HuggingFace (huggingface/huggingface-vscode: Code completion VSCode extension for OSS models (github.com)) , to identify and, if necessary, attribute any outputs that match training code.
[LINK: (huggingface/huggingface-vscode: Code completion VSCode extension for OSS models (github.com))](https://github.com/huggingface/huggingface-vscode)

### Limitations and bias

This model is intended to be used responsibly. It is not intended to be used to create unlawful content of any kind, to further any unlawful activity, or to engage in activities with a high risk of physical or economic harm.

## How to cite

## Model tree for stabilityai/stablecode-completion-alpha-3b-4k

## Dataset used to train stabilityai/stablecode-completion-alpha-3b-4k

## Spaces using stabilityai/stablecode-completion-alpha-3b-4k 37

## Collection including stabilityai/stablecode-completion-alpha-3b-4k

## Papers for stabilityai/stablecode-completion-alpha-3b-4k

## Evaluation results

- pass@1 on HumanEval self-reported 0.177
- pass@10 on HumanEval self-reported 0.270

--------------------