# Mellum-4b-base
**URL:** https://huggingface.co/JetBrains/Mellum-4b-base
**Page Title:** JetBrains/Mellum-4b-base · Hugging Face
--------------------


## Model Description

Mellum-4b-base is JetBrains' first open-source large language model (LLM) optimized for code-related tasks.
Trained on over 4 trillion tokens with a context window of 8192 tokens across multiple programming languages, Mellum-4b-base is tailored specifically for code completion. 
The model follows a LLaMA-style architecture with 4 billion parameters, making it efficient for both cloud inference (e.g., via vLLM) and local deployment (e.g., using llama.cpp or Ollama).
Mellum was trained using Automatic Mixed Precision (AMP) with bf16 precision. 
The uploaded version on Hugging Face retains the bf16 format for public use.
Designed for integration into professional developer tooling (e.g., intelligent code suggestions in IDEs), AI-powered coding assistants, and research on code understanding and generation, Mellum is also well-suited for educational applications and fine-tuning experiments.
This release includes a base model, and Python SFT models as well. 
Models for other languages will be released soon.
Keep in mind that base model is not fine-tuned for downstream tasks out-of-the-box, however, it is fully capable of supporting supervised fine-tuning (SFT) and reinforcement learning (RL) for adaptation to specific applications.

## Training Data

- Total Training Tokens: ~4.2 trillion tokens
- Corpus: The Stack, StarCoder Training Dataset, The Stack v2, CommitPack, English Wikipedia

## Training Details

- Context Window: 8,192 tokens
- Optimization: Standard language modeling objective.
- Hardware: Cluster of 256 x H200 NVIDIA GPUs with Infiniband
- Training Duration: ~20 days

## Benchmarks

In addition to the base model scores, we are providing scores for a Mellum fine-tuned for Python to provide model’s users with some estimation about potential capabilities.

## RepoBench 1.1

- Type: single-line
- Languages: Python and Java
- Metric: Exact Match (EM), %
Since Mellum has a maximum context window of 8k, we report here both the average performance across all evaluated context lengths (2k, 4k, 8k, 12k, and 16k) and the average over context lengths within its supported range (≤ 8k).

### Python Subset

### Java Subset

## Syntax-Aware Fill-in-the-Middle (SAFIM)

- Type: mix of multi-line and single-line
- Languages: multi-language
- Metric: pass@1, %

## HumanEval Infilling

- Type: single-line and multi-line
- Languages: Python
- Metric: pass@1, %
We continue to work on model improvements and will share the next iteration soon.

## Limitations

- Biases: May reflect biases present in public codebases. For example it will likely produce code which is similar in style to the open-source repositories.
- Security: Code suggestions should not be assumed to be secure or free of vulnerabilities.

## Sample Usage

Here are examples of how to run and sample from the model.

## Generic generaion

## Fill in the middle with additional files as context generation

## Citation

If you use this model, please cite:

## Contact

For questions, collaborations and requests reach us out via mellum@jetbrains.com

## Model tree for JetBrains/Mellum-4b-base

## Datasets used to train JetBrains/Mellum-4b-base

## Space using JetBrains/Mellum-4b-base 1

## Collection including JetBrains/Mellum-4b-base

## Evaluation results

- EM on RepoBench 1.1 (Python) self-reported 0.259
- EM ≤ 8k on RepoBench 1.1 (Python) self-reported 0.280
- EM on RepoBench 1.1 (Python, 2k) self-reported 0.282
- EM on RepoBench 1.1 (Python, 4k) self-reported 0.280
- EM on RepoBench 1.1 (Python, 8k) self-reported 0.278
- EM on RepoBench 1.1 (Python, 12k) self-reported 0.245
- EM on RepoBench 1.1 (Python, 16k) self-reported 0.211
- EM on RepoBench 1.1 (Java) self-reported 0.286
- EM ≤ 8k on RepoBench 1.1 (Java) self-reported 0.311
- EM on RepoBench 1.1 (Java, 2k) self-reported 0.320
- EM on RepoBench 1.1 (Java, 4k) self-reported 0.321
- EM on RepoBench 1.1 (Java, 8k) self-reported 0.291
- EM on RepoBench 1.1 (Java, 12k) self-reported 0.249
- EM on RepoBench 1.1 (Java, 16k) self-reported 0.247
- pass@1 on SAFIM self-reported 0.381
- pass@1 on SAFIM (Algorithmic) self-reported 0.253
- pass@1 on SAFIM (Control) self-reported 0.384
- pass@1 on SAFIM (API) self-reported 0.506
- pass@1 on HumanEval Infilling (Single-Line) self-reported 0.662
- pass@1 on HumanEval Infilling (Multi-Line) self-reported 0.385

--------------------