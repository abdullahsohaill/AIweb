# **StableLM Zephyr**
**URL:** https://huggingface.co/stabilityai/stablelm-2-zephyr-1_6b
**Page Title:** stabilityai/stablelm-2-zephyr-1_6b · Hugging Face
--------------------


## StableLM 2 Zephyr 1.6B

## Model Description

Stable LM 2 Zephyr 1.6B is a 1.6 billion parameter instruction tuned language model inspired by HugginFaceH4's Zephyr 7B training pipeline. The model is trained on a mix of publicly available datasets and synthetic datasets, utilizing Direct Preference Optimization (DPO) .

## Usage

StableLM 2 Zephyr 1.6B uses the following instruction format:
This format is also available through the tokenizer's apply_chat_template method:

## Model Details

- Developed by : Stability AI
- Model type : StableLM 2 Zephyr 1.6B model is an auto-regressive language model based on the transformer decoder architecture.
- Language(s) : English
- Paper : Stable LM 2 1.6B Technical Report
- Library : Alignment Handbook
[LINK: Alignment Handbook](https://github.com/huggingface/alignment-handbook.git)
- Finetuned from model : https://huggingface.co/stabilityai/stablelm-2-1_6b
- License : StabilityAI Non-Commercial Research Community License . If you want to use this model for your commercial products or purposes, please contact us here to learn more.
- Contact : For questions and comments about the model, please email lm@stability.ai

### Training Dataset

The dataset is comprised of a mixture of open datasets large-scale datasets available on the HuggingFace Hub :
- SFT Datasets
- HuggingFaceH4/ultrachat_200k
- meta-math/MetaMathQA
- WizardLM/WizardLM_evol_instruct_V2_196k
- Open-Orca/SlimOrca
- openchat/openchat_sharegpt4_dataset
- LDJnr/Capybara
- hkust-nlp/deita-10k-v0
- Preference Datasets:
- allenai/ultrafeedback_binarized_cleaned
- Intel/orca_dpo_pairs

## Performance

### MT-Bench

### OpenLLM Leaderboard

### Training Infrastructure

- Hardware : StableLM 2 Zephyr 1.6B was trained on the Stability AI cluster across 8 nodes with 8 A100 80GBs GPUs for each nodes.
- Code Base : We use our internal script for SFT steps and used HuggingFace Alignment Handbook script for DPO training.
[LINK: HuggingFace Alignment Handbook script](https://github.com/huggingface/alignment-handbook)

## Use and Limitations

### Intended Use

The model is intended to be used in chat-like applications. Developers must evaluate the model for safety performance in their specific use case. Read more about safety and limitations below.

### Limitations and Bias

​
This model is not trained against adversarial inputs. We strongly recommend pairing this model with an input and output classifier to prevent harmful responses.
Through our internal red teaming, we discovered that while the model will not output harmful information if not prompted to do so, it will hallucinate many facts. It is also willing to output potentially harmful outputs or misinformation when the user requests it.
Using this model will require guardrails around your inputs and outputs to ensure that any outputs returned are not misinformation or harmful.
Additionally, as each use case is unique, we recommend running your own suite of tests to ensure proper performance of this model.
Finally, do not use the models if they are unsuitable for your application, or for any applications that may cause deliberate or unintentional harm to others.

## How to Cite

## Model tree for stabilityai/stablelm-2-zephyr-1_6b

## Datasets used to train stabilityai/stablelm-2-zephyr-1_6b

## Spaces using stabilityai/stablelm-2-zephyr-1_6b 35

## Paper for stabilityai/stablelm-2-zephyr-1_6b


--------------------