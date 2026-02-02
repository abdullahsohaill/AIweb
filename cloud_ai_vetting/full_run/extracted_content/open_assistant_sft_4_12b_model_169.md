# Open-Assistant SFT-4 12B Model
**URL:** https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5
**Page Title:** OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5 · Hugging Face
--------------------


## Open-Assistant SFT-4 12B Model

This is the 4th iteration English supervised-fine-tuning (SFT) model of 
the Open-Assistant project. 
It is based on a Pythia 12B that was fine-tuned on human demonstrations 
of assistant conversations collected through the https://open-assistant.io/ human feedback web 
app before March 25, 2023.
[LINK: Open-Assistant](https://github.com/LAION-AI/Open-Assistant)

## Model Details

- Developed by: Open-Assistant Contributors
- Model type: Transformer-based Language Model
- Language: English
- Finetuned from: EleutherAI / pythia-12b-deduped
- Code: Open-Assistant/model/model_training
[LINK: Open-Assistant/model/model_training](https://github.com/LAION-AI/Open-Assistant/tree/main/model/model_training)
- Demo: Continuations for 250 random prompts
[LINK: Continuations for 250 random prompts](https://open-assistant.github.io/oasst-model-eval/?f=https%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Foasst-sft%2F2023-04-03_andreaskoepf_oasst-sft-4-pythia-12b-epoch-3_5_sampling_noprefix_lottery.json%0Ahttps%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Fchat-gpt%2F2023-04-11_gpt-3.5-turbo_lottery.json)
- License: Apache 2.0
- Contact: Open-Assistant Discord

## Prompting

Two special tokens are used to mark the beginning of user and assistant turns: <|prompter|> and <|assistant|> . Each turn ends with a <|endoftext|> token.
Input prompt example:
The input ends with the <|assistant|> token to signal that the model should 
start generating the assistant reply.

## Dev Details

- wandb: https://wandb.ai/open-assistant/supervised-finetuning/runs/770a0t41
- base model: andreaskoepf/pythia-12b-pre-2000
- checkpoint: 4000 steps
command: deepspeed trainer_sft.py --configs defaults reference-data reference-pythia-12b --cache_dir /home/ubuntu/data_cache --output_dir .saved/oasst-sft-3-pythia-12b-reference_2kpre --num_train_epochs 8 --residual_dropout 0.2 --deepspeed --use_flash_attention true --model_name andreaskoepf/pythia-12b-pre-2000
data:
pythia:
zero config:

## Model tree for OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5

## Spaces using OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5 100


--------------------