# OpenELM
**URL:** https://huggingface.co/apple/OpenELM
**Page Title:** apple/OpenELM · Hugging Face
--------------------


## OpenELM: An Efficient Language Model Family with Open Training and Inference Framework

Sachin Mehta, Mohammad Hossein Sekhavat, Qingqing Cao, Maxwell Horton, Yanzi Jin, Chenfan Sun, Iman Mirzadeh, Mahyar Najibi, Dmitry Belenko, Peter Zatloukal, Mohammad Rastegari
We introduce OpenELM , a family of Open E fficient L anguage M odels. OpenELM uses a layer-wise scaling strategy to efficiently allocate parameters within each layer of the transformer model, leading to enhanced accuracy. We pretrained OpenELM models using the CoreNet library. We release both pretrained and instruction tuned models with 270M, 450M, 1.1B and 3B parameters.
[LINK: CoreNet](https://github.com/apple/corenet)
Our pre-training dataset contains RefinedWeb, deduplicated PILE, a subset of RedPajama, and a subset of Dolma v1.6, totaling approximately 1.8 trillion tokens. Please check license agreements and terms of these datasets before using them.
See the list below for the details of each model:
- OpenELM-270M
- OpenELM-450M
- OpenELM-1_1B
- OpenELM-3B
- OpenELM-270M-Instruct
- OpenELM-450M-Instruct
- OpenELM-1_1B-Instruct
- OpenELM-3B-Instruct

## Usage

We have provided an example function to generate output from OpenELM models loaded via HuggingFace Hub in generate_openelm.py .
[LINK: HuggingFace Hub](https://huggingface.co/docs/hub/)
You can try the model by running the following command:
Please refer to this link to obtain your hugging face access token.
[LINK: this link](https://huggingface.co/docs/hub/security-tokens)
Additional arguments to the hugging face generate function can be passed via generate_kwargs . As an example, to speedup the inference, you can try lookup token speculative generation by passing the prompt_lookup_num_tokens argument as follows:
[LINK: lookup token speculative generation](https://huggingface.co/docs/transformers/generation_strategies)
Alternatively, try model-wise speculative generation with an assistive model by passing a smaller model through the assistant_model argument, for example:

## Main Results

### Zero-Shot

### LLM360

### OpenLLM Leaderboard

See the technical report for more results and comparison.

## Evaluation

### Setup

Install the following dependencies:

### Evaluate OpenELM

## Bias, Risks, and Limitations

The release of OpenELM models aims to empower and enrich the open research community by providing access to state-of-the-art language models. Trained on publicly available datasets, these models are made available without any safety guarantees. Consequently, there exists the possibility of these models producing outputs that are inaccurate, harmful, biased, or objectionable in response to user prompts. Thus, it is imperative for users and developers to undertake thorough safety testing and implement appropriate filtering mechanisms tailored to their specific requirements.

## Citation

If you find our work useful, please cite:
[LINK: How to track](https://huggingface.co/docs/hub/models-download-stats)
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for apple/OpenELM

## Spaces using apple/OpenELM 4

## Paper for apple/OpenELM


--------------------