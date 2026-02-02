# What is Papers with Code?
**URL:** https://paperswithcode.com
**Page Title:** Trending Papers - Hugging Face
--------------------

Get trending papers in your email inbox once a day!
Get trending papers in your email inbox!

## Trending Papers

## by AK and the research community

### Agent Lightning: Train ANY AI Agents with Reinforcement Learning

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.
- 8 authors
[LINK: GitHub 11.3k](https://github.com/microsoft/agent-lightning)

### Agent Lightning: Train ANY AI Agents with Reinforcement Learning

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.
- 8 authors
[LINK: GitHub 11.3k](https://github.com/microsoft/agent-lightning)

### HeartMuLa: A Family of Open Sourced Music Foundation Models

A suite of open-source music foundation models is introduced, featuring components for audio-text alignment, lyric recognition, music coding, and large language model-based song generation with controllable attributes and scalable parameterization.
- 28 authors
[LINK: GitHub 1.32k](https://github.com/HeartMuLa/heartlib)

### HeartMuLa: A Family of Open Sourced Music Foundation Models

A suite of open-source music foundation models is introduced, featuring components for audio-text alignment, lyric recognition, music coding, and large language model-based song generation with controllable attributes and scalable parameterization.
- 28 authors
[LINK: GitHub 1.32k](https://github.com/HeartMuLa/heartlib)

### MemOS: A Memory OS for AI System

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.
- 39 authors
[LINK: GitHub 4.51k](https://github.com/MemTensor/MemOS)

### MemOS: A Memory OS for AI System

MemOS, a memory operating system for Large Language Models, addresses memory management challenges by unifying plaintext, activation-based, and parameter-level memories, enabling efficient storage, retrieval, and continual learning.
- 39 authors
[LINK: GitHub 4.51k](https://github.com/MemTensor/MemOS)

### ShapeR: Robust Conditional 3D Shape Generation from Casual Captures

ShapeR generates high-fidelity 3D shapes from casual image sequences using visual-inertial SLAM, 3D detection, and vision-language models with rectified flow transformer conditioning.
[LINK: GitHub 476](https://github.com/facebookresearch/ShapeR)

### ShapeR: Robust Conditional 3D Shape Generation from Casual Captures

ShapeR generates high-fidelity 3D shapes from casual image sequences using visual-inertial SLAM, 3D detection, and vision-language models with rectified flow transformer conditioning.
[LINK: GitHub 476](https://github.com/facebookresearch/ShapeR)

### Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models

Conditional memory via Engram module enhances Transformer models by enabling efficient knowledge lookup and improving reasoning capabilities through optimized sparsity allocation.
[LINK: GitHub 3.16k](https://github.com/deepseek-ai/Engram)

### Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models

Conditional memory via Engram module enhances Transformer models by enabling efficient knowledge lookup and improving reasoning capabilities through optimized sparsity allocation.
[LINK: GitHub 3.16k](https://github.com/deepseek-ai/Engram)

### SimpleMem: Efficient Lifelong Memory for LLM Agents

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.
- 8 authors
[LINK: GitHub 1.77k](https://github.com/aiming-lab/SimpleMem)

### SimpleMem: Efficient Lifelong Memory for LLM Agents

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.
- 8 authors
[LINK: GitHub 1.77k](https://github.com/aiming-lab/SimpleMem)

### Continuous Audio Language Models

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io
- 5 authors
[LINK: GitHub 2.14k](https://github.com/kyutai-labs/pocket-tts)

### Continuous Audio Language Models

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io
- 5 authors
[LINK: GitHub 2.14k](https://github.com/kyutai-labs/pocket-tts)

### dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model

A unified Vision-Language Model, dots.ocr, achieves state-of-the-art performance on document layout parsing by jointly learning layout detection, text recognition, and relational understanding, validated on OmniDocBench and XDocParse benchmarks.
[LINK: GitHub 7.02k](https://github.com/rednote-hilab/dots.ocr)

### dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model

A unified Vision-Language Model, dots.ocr, achieves state-of-the-art performance on document layout parsing by jointly learning layout detection, text recognition, and relational understanding, validated on OmniDocBench and XDocParse benchmarks.
[LINK: GitHub 7.02k](https://github.com/rednote-hilab/dots.ocr)

### SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.
[LINK: GitHub 50.8k](https://github.com/docling-project/docling)

### SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.
[LINK: GitHub 50.8k](https://github.com/docling-project/docling)

### EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.
- 11 authors
[LINK: GitHub 1.88k](https://github.com/EverMind-AI/EverMemOS)

### EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.
- 11 authors
[LINK: GitHub 1.88k](https://github.com/EverMind-AI/EverMemOS)

### MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.
- 54 authors
[LINK: GitHub 5.59k](https://github.com/MiroMindAI/MiroThinker)

### MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.
- 54 authors
[LINK: GitHub 5.59k](https://github.com/MiroMindAI/MiroThinker)

### PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.
[LINK: GitHub 68.6k](https://github.com/PaddlePaddle/PaddleOCR)

### PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.
[LINK: GitHub 68.6k](https://github.com/PaddlePaddle/PaddleOCR)

### Efficient Memory Management for Large Language Model Serving with
  PagedAttention

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.
- 9 authors
[LINK: GitHub 68.1k](https://github.com/vllm-project/vllm)

### Efficient Memory Management for Large Language Model Serving with
  PagedAttention

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.
- 9 authors
[LINK: GitHub 68.1k](https://github.com/vllm-project/vllm)

### LTX-2: Efficient Joint Audio-Visual Foundation Model

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.
- 29 authors
[LINK: GitHub 2.96k](https://github.com/Lightricks/LTX-2)

### LTX-2: Efficient Joint Audio-Visual Foundation Model

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.
- 29 authors
[LINK: GitHub 2.96k](https://github.com/Lightricks/LTX-2)

### Agent READMEs: An Empirical Study of Context Files for Agentic Coding

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.
- 11 authors
[LINK: GitHub 15.8k](https://github.com/openai/agents.md)

### Agent READMEs: An Empirical Study of Context Files for Agentic Coding

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.
- 11 authors
[LINK: GitHub 15.8k](https://github.com/openai/agents.md)

### LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.
- 5 authors
[LINK: GitHub 66.3k](https://github.com/hiyouga/LLaMA-Factory)

### LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.
- 5 authors
[LINK: GitHub 66.3k](https://github.com/hiyouga/LLaMA-Factory)

### MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.
- 61 authors
[LINK: GitHub 52.6k](https://github.com/opendatalab/MinerU)

### MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.
- 61 authors
[LINK: GitHub 52.6k](https://github.com/opendatalab/MinerU)

### MinerU: An Open-Source Solution for Precise Document Content Extraction

MinerU is an open-source tool that enhances document content extraction using fine-tuned models and pre/postprocessing rules across diverse document types.
- 18 authors
[LINK: GitHub 52.6k](https://github.com/opendatalab/mineru)

### MinerU: An Open-Source Solution for Precise Document Content Extraction

MinerU is an open-source tool that enhances document content extraction using fine-tuned models and pre/postprocessing rules across diverse document types.
- 18 authors
[LINK: GitHub 52.6k](https://github.com/opendatalab/mineru)

### VibeVoice Technical Report

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.
[LINK: GitHub 20.6k](https://github.com/microsoft/VibeVoice)

### VibeVoice Technical Report

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.
[LINK: GitHub 20.6k](https://github.com/microsoft/VibeVoice)

### Recursive Language Models

We study allowing large language models (LLMs) to process arbitrarily long prompts through the lens of inference-time scaling. We propose Recursive Language Models (RLMs), a general inference strategy that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt. We find that RLMs successfully handle inputs up to two orders of magnitude beyond model context windows and, even for shorter prompts, dramatically outperform the quality of base LLMs and common long-context scaffolds across four diverse long-context tasks, while having comparable (or cheaper) cost per query.
[LINK: GitHub 1.57k](https://github.com/alexzhang13/rlm/tree/main)

### Recursive Language Models

We study allowing large language models (LLMs) to process arbitrarily long prompts through the lens of inference-time scaling. We propose Recursive Language Models (RLMs), a general inference strategy that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt. We find that RLMs successfully handle inputs up to two orders of magnitude beyond model context windows and, even for shorter prompts, dramatically outperform the quality of base LLMs and common long-context scaffolds across four diverse long-context tasks, while having comparable (or cheaper) cost per query.
[LINK: GitHub 1.57k](https://github.com/alexzhang13/rlm/tree/main)

### OmniTransfer: All-in-one Framework for Spatio-temporal Video Transfer

OmniTransfer presents a unified framework for spatio-temporal video transfer that enhances appearance consistency and temporal control through multi-view information and multimodal semantic guidance.
[LINK: GitHub 84](https://github.com/PangzeCheung/OmniTransfer)

### OmniTransfer: All-in-one Framework for Spatio-temporal Video Transfer

OmniTransfer presents a unified framework for spatio-temporal video transfer that enhances appearance consistency and temporal control through multi-view information and multimodal semantic guidance.
[LINK: GitHub 84](https://github.com/PangzeCheung/OmniTransfer)

### Advances and Frontiers of LLM-based Issue Resolution in Software Engineering: A Comprehensive Survey

Large language models face significant challenges in software issue resolution, prompting the development of autonomous coding agents through various training-free and training-based methodologies.
[LINK: GitHub 43](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution)

### Advances and Frontiers of LLM-based Issue Resolution in Software Engineering: A Comprehensive Survey

Large language models face significant challenges in software issue resolution, prompting the development of autonomous coding agents through various training-free and training-based methodologies.
[LINK: GitHub 43](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution)

### InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents

InfiAgent is a framework that maintains bounded reasoning context for long-horizon tasks by externalizing persistent state into a file-centric abstraction, enabling stable performance without task-specific fine-tuning.
- 5 authors
[LINK: GitHub 641](https://github.com/ChenglinPoly/infiAgent)

### InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents

InfiAgent is a framework that maintains bounded reasoning context for long-horizon tasks by externalizing persistent state into a file-centric abstraction, enabling stable performance without task-specific fine-tuning.
- 5 authors
[LINK: GitHub 641](https://github.com/ChenglinPoly/infiAgent)

### AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.
- 23 authors
[LINK: GitHub 15.8k](https://github.com/agentscope-ai/agentscope)

### AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.
- 23 authors
[LINK: GitHub 15.8k](https://github.com/agentscope-ai/agentscope)

### Very Large-Scale Multi-Agent Simulation in AgentScope

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.
- 8 authors
[LINK: GitHub 15.8k](https://github.com/modelscope/agentscope)

### Very Large-Scale Multi-Agent Simulation in AgentScope

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.
- 8 authors
[LINK: GitHub 15.8k](https://github.com/modelscope/agentscope)

### HunyuanVideo 1.5 Technical Report

HunyuanVideo 1.5 is a lightweight video generation model with state-of-the-art visual quality and motion coherence, using a DiT architecture with SSTA and an efficient video super-resolution network.
- 81 authors
[LINK: GitHub 3.63k](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)

### HunyuanVideo 1.5 Technical Report

HunyuanVideo 1.5 is a lightweight video generation model with state-of-the-art visual quality and motion coherence, using a DiT architecture with SSTA and an efficient video super-resolution network.
- 81 authors
[LINK: GitHub 3.63k](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)

### OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.
- 24 authors
[LINK: GitHub 66.9k](https://github.com/opendevin/opendevin)

### OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.
- 24 authors
[LINK: GitHub 66.9k](https://github.com/opendevin/opendevin)

### Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.
- 5 authors
[LINK: GitHub 45.8k](https://github.com/mem0ai/mem0)

### Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.
- 5 authors
[LINK: GitHub 45.8k](https://github.com/mem0ai/mem0)

### TradingAgents: Multi-Agents LLM Financial Trading Framework

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.
- 4 authors
[LINK: GitHub 28.3k](https://github.com/tauricresearch/tradingagents)

### TradingAgents: Multi-Agents LLM Financial Trading Framework

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.
- 4 authors
[LINK: GitHub 28.3k](https://github.com/tauricresearch/tradingagents)

### Multi-Agent Software Development through Cross-Team Collaboration

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.
- 8 authors
[LINK: GitHub 28.9k](https://github.com/OpenBMB/ChatDev)

### Multi-Agent Software Development through Cross-Team Collaboration

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.
- 8 authors
[LINK: GitHub 28.9k](https://github.com/OpenBMB/ChatDev)

### Scaling Large-Language-Model-based Multi-Agent Collaboration

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.
- 10 authors
[LINK: GitHub 29k](https://github.com/OpenBMB/ChatDev/tree/macnet)

### Scaling Large-Language-Model-based Multi-Agent Collaboration

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.
- 10 authors
[LINK: GitHub 29k](https://github.com/OpenBMB/ChatDev/tree/macnet)

### Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization

Being-H0.5 is a Vision-Language-Action model that enables robust cross-embodiment generalization through human-centric learning and a Mixture-of-Transformers architecture with specialized embodiment handling.
[LINK: GitHub 283](https://github.com/BeingBeyond/Being-H)

### Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization

Being-H0.5 is a Vision-Language-Action model that enables robust cross-embodiment generalization through human-centric learning and a Mixture-of-Transformers architecture with specialized embodiment handling.
[LINK: GitHub 283](https://github.com/BeingBeyond/Being-H)

### Single-stream Policy Optimization

Single-stream Policy Optimization (SPO) improves policy-gradient training for Large Language Models by eliminating group-based issues and providing a stable, low-variance learning signal, leading to better performance and efficiency.
[LINK: GitHub 18.6k](https://github.com/volcengine/verl)

### Single-stream Policy Optimization

Single-stream Policy Optimization (SPO) improves policy-gradient training for Large Language Models by eliminating group-based issues and providing a stable, low-variance learning signal, leading to better performance and efficiency.
[LINK: GitHub 18.6k](https://github.com/volcengine/verl)

### Self-Supervised Prompt Optimization

A self-supervised framework optimizes prompts for both closed and open-ended tasks by evaluating LLM outputs without external references, reducing costs and required data.
- 9 authors
[LINK: GitHub 63.3k](https://github.com/geekan/metagpt)

### Self-Supervised Prompt Optimization

A self-supervised framework optimizes prompts for both closed and open-ended tasks by evaluating LLM outputs without external references, reducing costs and required data.
- 9 authors
[LINK: GitHub 63.3k](https://github.com/geekan/metagpt)

### FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable
  Reasoning

Flawed-Aware Policy Optimization (FAPO) enhances reinforcement learning with verifiable rewards by penalizing flawed-positive rollouts, improving reasoning capability and training stability in large language models.
- 6 authors
[LINK: GitHub 18.6k](https://github.com/volcengine/verl/tree/main/recipe/fapo)

### FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable
  Reasoning

Flawed-Aware Policy Optimization (FAPO) enhances reinforcement learning with verifiable rewards by penalizing flawed-positive rollouts, improving reasoning capability and training stability in large language models.
- 6 authors
[LINK: GitHub 18.6k](https://github.com/volcengine/verl/tree/main/recipe/fapo)

### Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.
[LINK: GitHub 9.24k](https://github.com/Tongyi-MAI/Z-Image/tree/main)

### Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.
[LINK: GitHub 9.24k](https://github.com/Tongyi-MAI/Z-Image/tree/main)

### Toward Efficient Agents: Memory, Tool learning, and Planning

Efficiency in agentic systems is examined across memory, tool learning, and planning components, analyzing trade-offs between effectiveness and computational costs through various optimization strategies and benchmarks.
[LINK: GitHub 38](https://github.com/yxf203/Awesome-Efficient-Agents)

### Toward Efficient Agents: Memory, Tool learning, and Planning

Efficiency in agentic systems is examined across memory, tool learning, and planning components, analyzing trade-offs between effectiveness and computational costs through various optimization strategies and benchmarks.
[LINK: GitHub 38](https://github.com/yxf203/Awesome-Efficient-Agents)

### Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.
[LINK: GitHub 9.23k](https://github.com/Tongyi-MAI/Z-Image)

### Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.
[LINK: GitHub 9.23k](https://github.com/Tongyi-MAI/Z-Image)

### Action100M: A Large-scale Video Action Dataset

Action100M is a large-scale video action dataset constructed from internet instructional videos using automated pipelines with V-JEPA embeddings and GPT-based reasoning for structured annotations.
[LINK: GitHub 317](https://github.com/facebookresearch/Action100M)

### Action100M: A Large-scale Video Action Dataset

Action100M is a large-scale video action dataset constructed from internet instructional videos using automated pipelines with V-JEPA embeddings and GPT-based reasoning for structured annotations.
[LINK: GitHub 317](https://github.com/facebookresearch/Action100M)

### UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation

UltraRAG is a comprehensive RAG toolkit that automates knowledge adaptation across the entire workflow while providing a user-friendly interface for non-coding deployment.
- 15 authors
[LINK: GitHub 2.55k](https://github.com/OpenBMB/UltraRAG)

### UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation

UltraRAG is a comprehensive RAG toolkit that automates knowledge adaptation across the entire workflow while providing a user-friendly interface for non-coding deployment.
- 15 authors
[LINK: GitHub 2.55k](https://github.com/OpenBMB/UltraRAG)

### Zep: A Temporal Knowledge Graph Architecture for Agent Memory

Zep, a memory layer service, outperforms MemGPT in the DMR benchmark and LongMemEval by excelling in dynamic knowledge integration and temporal reasoning, critical for enterprise use cases.
- 5 authors
[LINK: GitHub 22.2k](https://github.com/getzep/graphiti)

### Zep: A Temporal Knowledge Graph Architecture for Agent Memory

Zep, a memory layer service, outperforms MemGPT in the DMR benchmark and LongMemEval by excelling in dynamic knowledge integration and temporal reasoning, critical for enterprise use cases.
- 5 authors
[LINK: GitHub 22.2k](https://github.com/getzep/graphiti)

### GigaBrain-0: A World Model-Powered Vision-Language-Action Model

GigaBrain-0, a VLA foundation model, uses world model-generated data to enhance cross-task generalization and policy robustness, improving real-world performance on complex manipulation tasks.
[LINK: GitHub 1.85k](https://github.com/open-gigaai/giga-brain-0)

### GigaBrain-0: A World Model-Powered Vision-Language-Action Model

GigaBrain-0, a VLA foundation model, uses world model-generated data to enhance cross-task generalization and policy robustness, improving real-world performance on complex manipulation tasks.
[LINK: GitHub 1.85k](https://github.com/open-gigaai/giga-brain-0)

### OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation

A novel GPT-based model, OmniFlatten, enables real-time natural full-duplex spoken dialogue through a multi-stage post-training technique that integrates speech and text without altering the original model's architecture.
- 9 authors
[LINK: GitHub 52.2k](https://github.com/karpathy/nanogpt)

### OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation

A novel GPT-based model, OmniFlatten, enables real-time natural full-duplex spoken dialogue through a multi-stage post-training technique that integrates speech and text without altering the original model's architecture.
- 9 authors
[LINK: GitHub 52.2k](https://github.com/karpathy/nanogpt)

### IndexTTS: An Industrial-Level Controllable and Efficient Zero-Shot
  Text-To-Speech System

IndexTTS, an enhanced text-to-speech system combining XTTS and Tortoise models, offers improved naturalness, enhanced voice cloning, and controllable usage through hybrid character-pinyin modeling and optimized vector quantization.
- 5 authors
[LINK: GitHub 18.1k](https://github.com/index-tts/index-tts)

### IndexTTS: An Industrial-Level Controllable and Efficient Zero-Shot
  Text-To-Speech System

IndexTTS, an enhanced text-to-speech system combining XTTS and Tortoise models, offers improved naturalness, enhanced voice cloning, and controllable usage through hybrid character-pinyin modeling and optimized vector quantization.
- 5 authors
[LINK: GitHub 18.1k](https://github.com/index-tts/index-tts)

### LightRAG: Simple and Fast Retrieval-Augmented Generation

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.
- 5 authors
[LINK: GitHub 27.5k](https://github.com/hkuds/lightrag)

### LightRAG: Simple and Fast Retrieval-Augmented Generation

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.
- 5 authors
[LINK: GitHub 27.5k](https://github.com/hkuds/lightrag)

### MediaPipe: A Framework for Building Perception Pipelines

MediaPipe framework facilitates the development of perception applications by providing tools for combining components, prototyping, and measuring performance across platforms.
- 14 authors
[LINK: GitHub 33.4k](https://github.com/google-ai-edge/mediapipe)

### MediaPipe: A Framework for Building Perception Pipelines

MediaPipe framework facilitates the development of perception applications by providing tools for combining components, prototyping, and measuring performance across platforms.
- 14 authors
[LINK: GitHub 33.4k](https://github.com/google-ai-edge/mediapipe)

### FunAudioLLM: Voice Understanding and Generation Foundation Models for
  Natural Interaction Between Humans and LLMs

FunAudioLLM enhances voice interactions by integrating SenseVoice for multilingual speech recognition, emotion detection, and audio event detection with CosyVoice for natural speech generation across languages, timbres, and styles.
- 1 authors
[LINK: GitHub 19.2k](https://github.com/funaudiollm/cosyvoice)

### FunAudioLLM: Voice Understanding and Generation Foundation Models for
  Natural Interaction Between Humans and LLMs

FunAudioLLM enhances voice interactions by integrating SenseVoice for multilingual speech recognition, emotion detection, and audio event detection with CosyVoice for natural speech generation across languages, timbres, and styles.
- 1 authors
[LINK: GitHub 19.2k](https://github.com/funaudiollm/cosyvoice)

### DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI

DataFlow is an LLM-driven data preparation framework that enhances data quality and reproducibility for various tasks, improving LLM performance with automatically generated pipelines.
[LINK: GitHub 2.58k](https://github.com/OpenDCAI/DataFlow)

### DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI

DataFlow is an LLM-driven data preparation framework that enhances data quality and reproducibility for various tasks, improving LLM performance with automatically generated pipelines.
[LINK: GitHub 2.58k](https://github.com/OpenDCAI/DataFlow)

### SkyReels-V2: Infinite-length Film Generative Model

SkyReels-V2 combines multi-modal language models, reinforcement learning, and diffusion forcing to address challenges in video generation, enabling high-quality, long-form synthesis with realistic motion and duration.
- 25 authors
[LINK: GitHub 5.88k](https://github.com/skyworkai/skyreels-v2)

### SkyReels-V2: Infinite-length Film Generative Model

SkyReels-V2 combines multi-modal language models, reinforcement learning, and diffusion forcing to address challenges in video generation, enabling high-quality, long-form synthesis with realistic motion and duration.
- 25 authors
[LINK: GitHub 5.88k](https://github.com/skyworkai/skyreels-v2)

### Multi-module GRPO: Composing Policy Gradients and Prompt Optimization
  for Language Model Programs

mmGRPO, a multi-module extension of GRPO, enhances accuracy in modular AI systems by optimizing LM calls and prompts across various tasks.
- 13 authors
[LINK: GitHub 31.7k](https://github.com/stanfordnlp/dspy)

### Multi-module GRPO: Composing Policy Gradients and Prompt Optimization
  for Language Model Programs

mmGRPO, a multi-module extension of GRPO, enhances accuracy in modular AI systems by optimizing LM calls and prompts across various tasks.
- 13 authors
[LINK: GitHub 31.7k](https://github.com/stanfordnlp/dspy)

--------------------