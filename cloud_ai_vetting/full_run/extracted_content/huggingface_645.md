# [huggingface
**URL:** https://huggingface.co/bosonai/Higgs-Llama-3-70B
**Page Title:** bosonai/Higgs-Llama-3-70B · Hugging Face
--------------------


## Higgs-Llama-3-70B

Higgs-Llama-3-70B is post-trained from meta-llama/Meta-Llama-3-70B , specially tuned for role-playing while being competitive in general-domain instruction-following and reasoning.
We perform supervised fine-tuning with our in-house instruction-following and chat datasets. Afterwards, we construct preference pairs with a semi-automated pipeline that relies on both human-labelers and our private LLMs.
We conduct iterative preference optimization to align the model. During alignment, we adopted a special strategy to align the model’s behavior with the system message.
Compared with other instruct models, Higgs models follow their roles more closely.
See our release blog .

## Evaluation

All benchmarks lead to eventual overfitting, including those for LLMs. Training on data, particularly beneficial for benchmarks typically does not improve (or even worsen) role-playing performance. We worked to exclude benchmark data, including their training examples, from our fine-tuning data.
We highlight our results on two new and challenging benchmarks: MMLU-Pro and Arena-Hard . MMLU-Pro extends the popular MMLU benchmark. We believe that it suffers from less overfitting by other released models as well, as it was released only recently (it was released after our models finished training).
[LINK: Arena-Hard](https://github.com/lm-sys/arena-hard-auto)

### MMLU-Pro

### Arena-Hard

## Overall Results

In the following, we compare our model's performance with gpt-4o and Llama-3-70B-Instruct on MMLU-Pro , Arena-Hard , AlpacaEval 2.0 LC , MMLU, GPQA and DROP. For MMLU, GPQA and DROP, we adopt openai/simple-evals for evaluation. For the other benchmarks, we evaluate via the official implementation.
[LINK: MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro)
[LINK: Arena-Hard](https://github.com/lm-sys/arena-hard-auto/tree/main)
[LINK: AlpacaEval 2.0 LC](https://github.com/tatsu-lab/alpaca_eval)
[LINK: openai/simple-evals](https://github.com/openai/simple-evals)
*For Llama-3-70B-Instruct, the MMLU-Pro number is copied from the MMLU-Pro leaderboard ; the Arena-Hard numbers are copied from the leaderboard updated on 5/21 while we run gpt-4o ourselves; and the MMLU/GPQA/DROP are copied from simple-evals .
[LINK: leaderboard updated on 5/21](https://github.com/lm-sys/arena-hard-auto/tree/main?tab=readme-ov-file#full-leaderboard-updated-0521)
[LINK: simple-evals](https://github.com/openai/simple-evals)

## How to use

We use the same prompting format as in Meta-Llama-3-70B-Instruct.

### Use with transformers

See the snippet below for usage with Transformers:

## License

Our license is based on Meta's LLama 3 Community License.

## Model tree for bosonai/Higgs-Llama-3-70B

Base model

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
bosonai/Higgs-Llama-3-70B is supported by the following Inference Providers:

--------------------