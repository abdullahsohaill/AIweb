# DeepSeek R1
**URL:** https://openrouter.ai/deepseek/deepseek-r1:free
**Page Title:** R1 - API, Providers, Stats | OpenRouter
--------------------

[LINK: Send traces to your favorite observability platforms with Broadcast (now GA).](/docs/guides/features/broadcast)

## DeepSeek: R1

### deepseek / deepseek-r1

DeepSeek R1 is here: Performance on par with OpenAI o1 , but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass.
Fully open-source model & technical report .
[LINK: technical report](https://api-docs.deepseek.com/news/news250120)
MIT licensed: Distill & commercialize freely!

## Recent activity on R1

### Total usage per day on OpenRouter

Prompt tokens measure input size. Reasoning tokens show internal thinking before a response. Completion tokens reflect total output length.

## More models from DeepSeek

DeepSeek-V3.2-Speciale is a high-compute variant of DeepSeek-V3.2 optimized for maximum reasoning and agentic performance. It builds on DeepSeek Sparse Attention (DSA) for efficient long-context processing, then scales post-training reinforcement learning to push capability beyond the base model. Reported evaluations place Speciale ahead of GPT-5 on difficult reasoning workloads, with proficiency comparable to Gemini-3.0-Pro, while retaining strong coding and tool-use reliability. Like V3.2, it benefits from a large-scale agentic task synthesis pipeline that improves compliance and generalization in interactive environments.
DeepSeek-V3.2 is a large language model designed to harmonize high computational efficiency with strong reasoning and agentic tool-use performance. It introduces DeepSeek Sparse Attention (DSA), a fine-grained sparse attention mechanism that reduces training and inference cost while preserving quality in long-context scenarios. A scalable reinforcement learning post-training framework further improves reasoning, with reported performance in the GPT-5 class, and the model has demonstrated gold-medal results on the 2025 IMO and IOI. V3.2 also uses a large-scale agentic task synthesis pipeline to better integrate reasoning into tool-use settings, boosting compliance and generalization in interactive environments.
Users can control the reasoning behaviour with the reasoning enabled boolean. Learn more in our docs
DeepSeek-V3.2-Exp is an experimental large language model released by DeepSeek as an intermediate step between V3.1 and future architectures. It introduces DeepSeek Sparse Attention (DSA), a fine-grained sparse attention mechanism designed to improve training and inference efficiency in long-context scenarios while maintaining output quality. Users can control the reasoning behaviour with the reasoning enabled boolean. Learn more in our docs
The model was trained under conditions aligned with V3.1-Terminus to enable direct comparison. Benchmarking shows performance roughly on par with V3.1 across reasoning, coding, and agentic tool-use tasks, with minor tradeoffs and gains depending on the domain. This release focuses on validating architectural optimizations for extended context lengths rather than advancing raw task accuracy, making it primarily a research-oriented model for exploring efficient transformer designs.
DeepSeek-V3.1 Terminus is an update to DeepSeek V3.1 that maintains the model's original capabilities while addressing issues reported by users, including language consistency and agent capabilities, further optimizing the model's performance in coding and search agents. It is a large hybrid reasoning model (671B parameters, 37B active) that supports both thinking and non-thinking modes. It extends the DeepSeek-V3 base with a two-phase long-context training process, reaching up to 128K tokens, and uses FP8 microscaling for efficient inference. Users can control the reasoning behaviour with the reasoning enabled boolean. Learn more in our docs
The model improves tool use, code generation, and reasoning efficiency, achieving performance comparable to DeepSeek-R1 on difficult benchmarks while responding more quickly. It supports structured tool calling, code agents, and search agents, making it suitable for research, coding, and agentic workflows.
DeepSeek-V3.1 Terminus is an update to DeepSeek V3.1 that maintains the model's original capabilities while addressing issues reported by users, including language consistency and agent capabilities, further optimizing the model's performance in coding and search agents. It is a large hybrid reasoning model (671B parameters, 37B active) that supports both thinking and non-thinking modes. It extends the DeepSeek-V3 base with a two-phase long-context training process, reaching up to 128K tokens, and uses FP8 microscaling for efficient inference. Users can control the reasoning behaviour with the reasoning enabled boolean. Learn more in our docs
The model improves tool use, code generation, and reasoning efficiency, achieving performance comparable to DeepSeek-R1 on difficult benchmarks while responding more quickly. It supports structured tool calling, code agents, and search agents, making it suitable for research, coding, and agentic workflows.
DeepSeek-V3.1 is a large hybrid reasoning model (671B parameters, 37B active) that supports both thinking and non-thinking modes via prompt templates. It extends the DeepSeek-V3 base with a two-phase long-context training process, reaching up to 128K tokens, and uses FP8 microscaling for efficient inference. Users can control the reasoning behaviour with the reasoning enabled boolean. Learn more in our docs
The model improves tool use, code generation, and reasoning efficiency, achieving performance comparable to DeepSeek-R1 on difficult benchmarks while responding more quickly. It supports structured tool calling, code agents, and search agents, making it suitable for research, coding, and agentic workflows.
It succeeds the DeepSeek V3-0324 model and performs well on a variety of tasks.
This is a base model, trained only for raw next-token prediction. Unlike instruct/chat models, it has not been fine-tuned to follow user instructions. Prompts need to be written more like training text or examples rather than simple requests (e.g., “Translate the following sentence…” instead of just “Translate this”).
DeepSeek-V3.1 Base is a 671B parameter open Mixture-of-Experts (MoE) language model with 37B active parameters per forward pass and a context length of 128K tokens. Trained on 14.8T tokens using FP8 mixed precision, it achieves high training efficiency and stability, with strong performance across language, reasoning, math, and coding tasks.
DeepSeek-R1-Distill-Qwen-7B is a 7 billion parameter dense language model distilled from DeepSeek-R1, leveraging reinforcement learning-enhanced reasoning data generated by DeepSeek's larger models. The distillation process transfers advanced reasoning, math, and code capabilities into a smaller, more efficient model architecture based on Qwen2.5-Math-7B. This model demonstrates strong performance across mathematical benchmarks (92.8% pass@1 on MATH-500), coding tasks (Codeforces rating 1189), and general reasoning (49.1% pass@1 on GPQA Diamond), achieving competitive accuracy relative to larger models while maintaining smaller inference costs.
DeepSeek-R1-0528 is a lightly upgraded release of DeepSeek R1 that taps more compute and smarter post-training tricks, pushing its reasoning and inference to the brink of flagship models like O3 and Gemini 2.5 Pro.
It now tops math, programming, and logic leaderboards, showcasing a step-change in depth-of-thought.
The distilled variant, DeepSeek-R1-0528-Qwen3-8B, transfers this chain-of-thought into an 8 B-parameter form, beating standard Qwen3 8B by +10 pp and tying the 235 B “thinking” giant on AIME 2024.
May 28th update to the original DeepSeek R1 Performance on par with OpenAI o1 , but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass.
Fully open-source model.
May 28th update to the original DeepSeek R1 Performance on par with OpenAI o1 , but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass.
Fully open-source model.
DeepSeek Prover V2 is a 671B parameter model, speculated to be geared towards logic and mathematics. Likely an upgrade from DeepSeek-Prover-V1.5 Not much is known about the model yet, as DeepSeek released it on Hugging Face without an announcement or description.
Note that this is a base model mostly meant for testing, you need to provide detailed prompts for the model to return useful responses.
DeepSeek-V3 Base is a 671B parameter open Mixture-of-Experts (MoE) language model with 37B active parameters per forward pass and a context length of 128K tokens. Trained on 14.8T tokens using FP8 mixed precision, it achieves high training efficiency and stability, with strong performance across language, reasoning, math, and coding tasks.
DeepSeek-V3 Base is the pre-trained model behind DeepSeek V3
DeepSeek V3, a 685B-parameter, mixture-of-experts model, is the latest iteration of the flagship chat model family from the DeepSeek team.
It succeeds the DeepSeek V3 model and performs really well on a variety of tasks.
DeepSeek-R1-Zero is a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step. It's 671B parameters in size, with 37B active in an inference pass.
It demonstrates remarkable performance on reasoning. With RL, DeepSeek-R1-Zero naturally emerged with numerous powerful and interesting reasoning behaviors.
DeepSeek-R1-Zero encounters challenges such as endless repetition, poor readability, and language mixing. See DeepSeek R1 for the SFT model.
DeepSeek R1 Distill Llama 8B is a distilled large language model based on Llama-3.1-8B-Instruct , using outputs from DeepSeek R1 . The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:
The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.
Hugging Face:
DeepSeek R1 Distill Qwen 1.5B is a distilled large language model based on Qwen 2.5 Math 1.5B , using outputs from DeepSeek R1 . It's a very small and efficient model which outperforms GPT 4o 0513 on Math Benchmarks.
Other benchmark results include:
The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.
DeepSeek R1 Distill Qwen 32B is a distilled large language model based on Qwen 2.5 32B , using outputs from DeepSeek R1 . It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.\n\nOther benchmark results include:\n\n- AIME 2024 pass@1: 72.6\n- MATH-500 pass@1: 94.3\n- CodeForces Rating: 1691\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.
DeepSeek R1 Distill Qwen 14B is a distilled large language model based on Qwen 2.5 14B , using outputs from DeepSeek R1 . It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.
Other benchmark results include:
The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.
DeepSeek R1 Distill Llama 70B is a distilled large language model based on Llama-3.3-70B-Instruct , using outputs from DeepSeek R1 . The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:
The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.
DeepSeek R1 is here: Performance on par with OpenAI o1 , but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass.
Fully open-source model & technical report .
MIT licensed: Distill & commercialize freely!
DeepSeek-V2.5 is an upgraded version that combines DeepSeek-V2-Chat and DeepSeek-Coder-V2-Instruct. The new model integrates the general and coding abilities of the two previous versions. For model details, please visit DeepSeek-V2 page for more information.

--------------------