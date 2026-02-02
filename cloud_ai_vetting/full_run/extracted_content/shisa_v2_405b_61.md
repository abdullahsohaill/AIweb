# Shisa V2 405B
**URL:** https://huggingface.co/shisa-ai/shisa-v2-llama3.1-405b
**Page Title:** shisa-ai/shisa-v2-llama3.1-405b · Hugging Face
--------------------


## Shisa V2

Shisa V2 is a family of bilingual Japanese and English (JA/EN) general-purpose chat models trained by Shisa.AI . These models aim to excel in Japanese language tasks while retaining robust English capabilities.
Since our initial Shisa 7B releases, the baseline Japanese capabilities of open-weight language models have significantly improved. New models have more Japanese pre-training tokens, higher JA tokenizer efficiency , and better quality Japanese outputs overall. As such, for Shisa V2 we've eschewed both tokenizer extension and costly continued pre-training and have focused entirely on optimizing post-training. We've significantly expanded and refined the synthetic-data driven approach that was pioneered with our original Shisa 7B models, and have achieved substantial performance gains.
[LINK: JA tokenizer efficiency](https://github.com/shisa-ai/shisa-v2/blob/main/eval/tokenizer-efficiency/tokenizer-eval-ja.md)

## Shisa V2 405B

Llama 3.1 Shisa V2 405B 1 is a slightly special version of Shisa V2. Obviously, it is the largest, using Llama 3.1 405B Instruct as the base model and required >50x the compute for SFT+DPO compared to the 70B version. While it uses the same Japanese data mix as the other Shisa V2 models, it also has some contributed KO and ZH-TW language data mixed in as well.
Most notably, Shisa V2 405B not only outperforms Shisa V2 70B on our battery of evals, but also GPT-4 (0603) and GPT-4 Turbo (2024-04-09). Shisa V2 405B also goes toe-to-toe with GPT-4o (2024-11-20) and DeepSeek-V3 (0324) on Japanese MT-Bench. Based on the evaluation results, we believe that Shisa V2 405B is the highest performing LLM ever trained in Japan.

## Model Family Overview

Until now, the Shisa V2 family has comprised of models ranging from 7B to 70B parameters in size. We now add the 405B:
These Shisa V2 models were all trained using the same datasets and similar training recipes (with scaled learning rate based on model size). The 405B model has additional KO and ZH-TW data added to the SFT.
While most of our development and tuning was done on the Llama 3.1 8B model, we did some cross-validation during this process and we're pleased that our final recipe has shown robust scaling, improving Japanese language performance across all model sizes evaluated. We've prioritized releasing the highest-performing openly-licensed (Apache 2.0 and MIT) models in each class size.

## Performance

All Shisa V2 models demonstrate improved Japanese output quality compared to their respective base models:
NOTE: The scores below differ slightly from previously published scores in our Shisa V2 model cards as the LLM Judge used for these results is GPT 4.1 (2025-04-14). We use 4.1 because, similar to observations in previously published literature, we found that weaker models like GPT-4 or our LLM-as-a-Jury were not able to accurately evaluate the stronger Shisa V2 405B model (for example, in our JA MT-Bench testing, GPT-4 Turbo was not able to distinguish scoring between our 70B and 405B in most categories, while GPT 4.1 was).
Shisa V2 models perform well against other models in their respective class sizes. As there are not many other 405B models, we've included the strongest models we have tested for as references.
Our recently published shisa-v2-llama3.3-70b is also included in this chart as a point of comparison.

### Additional 405B Evals

The 405B model had a specific set of benchmark targets we aimed for, and we are please to report that we far exceeded them:
Again, these scores are based on GPT-4.1 (gpt-4.1-2025-04-14) as the judge, so they may not be directly comparable to other published benchmarks. For example, the JA MT-Bench score (excluding coding and math) using GPT-4 (0613) as evaluator scored 9.60 (vs 9.18 when scored by GPT 4.1).
The Shaberi testing suite we use for our evals actually delivers only a Turn 1 JA MT-Bench score (and uses a modified prompt that tries to emphasize additional score penalties for non-Japanese outputs), however for the more detailed JA MT-Bench testing of our 405B model we forked a more directly comparable ja-mt-bench-harness that is more faithful to the original JA MT-Bench, and runs Turn 1 and Turn 2 results.
[LINK: Shaberi testing suite](https://github.com/shisa-ai/shaberi)
[LINK: ja-mt-bench-harness](https://github.com/shisa-ai/ja-mt-bench-harness)
Interestingly, for strong LLMs, it appears that Turn 2 results now typically exceed Turn 1. Also, while average scores excluding coding and math were requested for reporting, we found, especially for the GPT 4.1 judging, that there was very little difference in the results between including vs/excluding them. The full results including raw output and scoring are available in our harness repository .
[LINK: harness repository](https://github.com/shisa-ai/ja-mt-bench-harness)
One of the other requested test results for the project was for llm-jp-eval . While we do use llm-jp-eval within our multieval as a datapoint, I've written in the past about my reservations about llm-jp-eval and the llm-jp-eval's README states:
[LINK: llm-jp-eval](https://github.com/llm-jp/llm-jp-eval)
[LINK: llm-jp-eval's README](https://github.com/llm-jp/llm-jp-eval/blob/dev/README_en.md)
It has become clear that models instruction-tuned using jaster can achieve very high llm-jp-eval evaluation scores, even if test data was not used for instruction tuning. Therefore, please note that obtaining a high evaluation score does not necessarily mean better performance than other LLMs.
All our llm-jp-eval testing is run with v1.4.1 with all defaults and detailed scoring is included for reference:

### Testing Notes

We developed a custom "multieval" harness to automate our model evaluations. Standard benchmarks we use include:
- ELYZA Tasks 100
- JA MT-Bench ( dataset )
[LINK: JA MT-Bench](https://github.com/Stability-AI/FastChat/tree/jp-stable/fastchat/llm_judge)
- Rakuda
- Tengu Bench
- llm-jp-eval (v1.4.1)
[LINK: llm-jp-eval](https://github.com/llm-jp/llm-jp-eval)
- MixEval
[LINK: MixEval](https://mixeval.github.io/)
- LiveBench (2024-11-25)
- IFEval ( Lighteval )
[LINK: Lighteval](https://github.com/huggingface/lighteval)
- EvalPlus
[LINK: EvalPlus](https://github.com/evalplus/evalplus)

### New Japanese Benchmarks

Over the course of model development, we also created several new evaluations to help us measure performance on important Japanese downstream tasks:
- shisa-jp-ifeval : Inspired by IFEval , but evaluating instruction-following abilities specific to Japanese grammar and linguistics (closed form)
- shisa-jp-rp-bench : Assessing performance on Japanese role-play and character/persona-based multi-turn conversations based on Aratako 's Japanese-RP-Bench (LLM judge)
[LINK: Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench)
- shisa-jp-tl-bench : Testing Japanese-English translation proficiency (LLM judge, BTL pairwise comparison with logistic transformation scoring)
We believe these benchmarks will be generally useful and plan to open-source them in the near future to support the Japanese LLM research community.

## Usage

All Shisa V2 models inherit the chat templates of their respective base models and have been tested and validated for proper inference with both vLLM and SGLang .
[LINK: chat templates](https://huggingface.co/docs/transformers/v4.37.1/chat_templating)
[LINK: vLLM](https://github.com/vllm-project/vllm)
[LINK: SGLang](https://github.com/sgl-project/sglang)
Running sampler sweeps, we found the models operate well across a variety of temperatures in most settings. For translation tasks specifically, we recommend a lower temperature (eg 0.2) to increase accuracy. For role-play and creative tasks, a higher temp (eg 1.0) seems to give good results. To prevent cross-lingual token leakage we recommend a top_p of 0.9 or min_p of 0.1.
No additional safety alignment has been done on these models, so they will largely inherit the base models' biases and safety profiles.

## Datasets

Our supervised fine-tuning (SFT) stage dataset consists of approximately 360K samples totaling roughly 420M Llama 3 tokens:
- shisa-ai/shisa-v2-sharegpt This is a filtered, regenerated and resampled version of the original Shisa V1 augmxnt/ultra-orca-boros-en-ja-v1 dataset This was the backbone of our Shisa V2 training and it proved to be an extremely robust dataset, out-performing all existing mixes/additions (Tulu, Olmo, Rewild, various Magpie sets, etc.) - if you need a JA/EN dataset, we believe this new version is among the best currently available
- This is a filtered, regenerated and resampled version of the original Shisa V1 augmxnt/ultra-orca-boros-en-ja-v1 dataset
- This was the backbone of our Shisa V2 training and it proved to be an extremely robust dataset, out-performing all existing mixes/additions (Tulu, Olmo, Rewild, various Magpie sets, etc.) - if you need a JA/EN dataset, we believe this new version is among the best currently available
- shisa-ai/rewild-set-deepseek-subset A filtered version of Rewild ( WildChat ) prompts translated into Japanese, with responses generated by DeepSeek-V3-0324
- A filtered version of Rewild ( WildChat ) prompts translated into Japanese, with responses generated by DeepSeek-V3-0324
- shisa-ai/magpie-ultra-set Japanese generations based on argilla/magpie-ultra-v1.0
- Japanese generations based on argilla/magpie-ultra-v1.0
- shisa-ai/magpie-advanced-questions-set Magpie -generated questions about advanced college-level topics across a variety of academic fields
- Magpie -generated questions about advanced college-level topics across a variety of academic fields
[LINK: Magpie](https://magpie-align.github.io/)
- shisa-ai/japan-magpie-set Magpie -generated questions about Japan's economy and history as well as cultural and business practices
- Magpie -generated questions about Japan's economy and history as well as cultural and business practices
[LINK: Magpie](https://magpie-align.github.io/)
- shisa-ai/shisa-v2-roleplaying-sft Synthetically-generated roleplaying data featuring a wide variety of characters, situations, and genres
- Synthetically-generated roleplaying data featuring a wide variety of characters, situations, and genres
- shisa-ai/translation_expanded_master_set_filtered A synthetic dataset involving a wide range of translation tasks, including essays, conversations, and fiction
- A synthetic dataset involving a wide range of translation tasks, including essays, conversations, and fiction
- shisa-ai/shisa-v2-instruction-following-sft An instruction following dataset based on prompts from ( Aratako/Magpie-Tanuki-8B-annotated-96k ) and a list of instruction-following constraints
- An instruction following dataset based on prompts from ( Aratako/Magpie-Tanuki-8B-annotated-96k ) and a list of instruction-following constraints
The 405B model contains two additional datasets provided by Ubitus K. K. :
- Korean (KO) dataset: 133M tokens (511K samples)
- Taiwanese Mandarin (ZH-TW) dataset: 3.7M tokens (23K samples)
Our final DPO mix is 113K samples totaling approximately 115M Llama 3 tokens:
- shisa-ai/deepseekv3-ultrafeedback-armorm-dpo This is a version of princeton-nlp/gemma2-ultrafeedback-armorm with chosen responses regenerated by DeepSeek-V3-0324 Surprisingly, we found that using this relatively small DPO alignment set in English-only outperformed both JA/EN DPO sets and also much larger sets like the Tulu 3 preference mixture
- This is a version of princeton-nlp/gemma2-ultrafeedback-armorm with chosen responses regenerated by DeepSeek-V3-0324
- Surprisingly, we found that using this relatively small DPO alignment set in English-only outperformed both JA/EN DPO sets and also much larger sets like the Tulu 3 preference mixture
- shisa-ai/shisa-v2-roleplaying-dpo A DPO variant of the roleplaying-sft set that uses an UltraFeedback -style rating system
- A DPO variant of the roleplaying-sft set that uses an UltraFeedback -style rating system
[LINK: UltraFeedback](https://github.com/OpenBMB/UltraFeedback)
- shisa-ai/translation-no-extra-text-dpo-dataset A DPO set that aims to reduce the tendency of models to output extraneous explanatory text for translations when not wanted
- A DPO set that aims to reduce the tendency of models to output extraneous explanatory text for translations when not wanted
- shisa-ai/shisa-v2-instruction-following-dpo A DPO variant of the instruction-following-sft set to further enhance instruction-following performance
- A DPO variant of the instruction-following-sft set to further enhance instruction-following performance
- shisa-ai/politeness-dpo-set A set to allow for greater controllability of speaking style for Japanese responses
- A set to allow for greater controllability of speaking style for Japanese responses

## Training

We trained over 200 models to empirically test a wide range of variables. Beyond hyper-parameter and data-mix testing, we also ran numerous tests on data ordering, multilingual-specific ordering, curriculum learning, multi-stage training, various forms of self-play, preference tuning, and some of the latest RL/verifiable reward techniques.
A full discussion of these learnings is out of scope here, but we will be updating the shisa-v2 wiki and the Shisa.AI website with forthcoming writeups.
[LINK: shisa-v2 wiki](https://github.com/shisa-ai/shisa-v2/wiki)
Most of our training was done on a small AWS Sagemaker-deployed 4-node H100 slurm cluster. Training was mostly done with Axolotl with DeepSpeed and Liger Kernels . The Phi 4 and Llama 3.3 70B versions of Shisa V2 were trained with OpenRLHF . Our training logs are publicly available on Weights and Biases .
[LINK: Axolotl](https://github.com/axolotl-ai-cloud/axolotl/)
[LINK: Liger Kernels](https://github.com/linkedin/Liger-Kernel)
[LINK: OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
Training Shisa V2 405B was significantly more involved compared to our smaller models. We trained with OpenRLHF on 32 H100 nodes. For SFT, 30 nodes (240 H100 GPUs) were used for training, with 2 nodes allocated for continuous evaluation of checkpoints. The DPO was trained on all 32 H100 nodes (256 H100 GPUs). Overall training time for the final 405B model was approximately 65,000+ H100 hours for the SFT and 4,000 H100 hours for the DPO. We will shre more details about the challenges faced during the 405B training in an upcoming technical report.

### Credits

The Shisa V2 models were developed by Leonard Lin and Adam Lensenmayer ( Shisa.AI ).
For Shisa V2 405B, additional multi-lingual datasets were provided by Ubitus K.K. .
Compute was provided by Ubitus K.K. and METI GENIAC .
Thanks to Meta Llama , Microsoft Research , Mistral AI , and Qwen Team for providing their models to the open source community, Unsloth for their llamafied conversion of Phi-4 , the Tulu team, whose detailed writeups and fast responses to our questions were very helpful, and Chanvichet Vong of the Axolotl team for his tireless work in the Axolotl Discord.
[LINK: Chanvichet Vong](https://github.com/NanoCode012)
We also extend our thanks to all open source AI developers and researchers - without their publicly shared research, tooling, and datasets, none of our work would be possible. We hope that our own contributions will further support the broader community.
A special thanks to Jon Durbin for his work on Shisa V1 and to chutes.ai for providing additional compute for inference hosting and evaluations of the 70B and 405B models.
For more details on our development and insights, please visit the Shisa V2 Github repository and the Shisa.AI website .
[LINK: Shisa V2 Github repository](https://github.com/shisa-ai/shisa-v2)
1: Per the Llama Community License Agreements, the official names of the Llama-based models are "Llama 3.1 shisa-v2-llama3.1-8b", "Llama 3.3 shisa-v2-llama3.3-70b", and "Llama 3.1 Shisa V2 405B"

## Model tree for shisa-ai/shisa-v2-llama3.1-405b

Base model

## Datasets used to train shisa-ai/shisa-v2-llama3.1-405b

## Collection including shisa-ai/shisa-v2-llama3.1-405b

## Paper for shisa-ai/shisa-v2-llama3.1-405b


--------------------