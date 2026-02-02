# ToolMaker
**URL:** https://huggingface.co/papers/2502.11705
**Page Title:** Paper page - LLM Agents Making Agent Tools
--------------------


## LLM Agents Making Agent Tools

## Abstract

ToolMaker autonomously converts scientific code repositories into tools for large language models by managing dependencies and self-correcting errors, demonstrating improved performance over existing agents.
Tool use has turned large language models ( LLMs ) into powerful agents that
can perform complex multi-step tasks by dynamically utilising external software
components. However, these tools must be implemented in advance by human
developers, hindering the applicability of LLM agents in domains which demand
large numbers of highly specialised tools, like in life sciences and medicine.
Motivated by the growing trend of scientific studies accompanied by public code
repositories, we propose ToolMaker , a novel agentic framework that autonomously
transforms papers with code into LLM-compatible tools. Given a short task
description and a repository URL, ToolMaker autonomously installs required
dependencies and generates code to perform the task, using a closed-loop self-correction mechanism to iteratively diagnose and rectify errors. To
evaluate our approach, we introduce a benchmark comprising 15 diverse and
complex computational tasks spanning both medical and non-medical domains with
over 100 unit tests to objectively assess tool correctness and robustness. ToolMaker correctly implements 80% of the tasks, substantially outperforming
current state-of-the-art software engineering agents . ToolMaker therefore is a
step towards fully autonomous agent-based scientific workflows .
[LINK: GitHub 66 auto](https://github.com/katherlab/toolmaker)

### Community

@ librarian-bot
@ countkc shared how to call librarian-bot below :)
@ librarian-bot recommend
This is an automated message from the Librarian Bot . I found the following papers similar to this paper.
The following papers were recommended by the Semantic Scholar API
- Aviary: training language agents on challenging scientific tasks (2024)
- AutoAgent: A Fully-Automated and Zero-Code Framework for LLM Agents (2025)
- Autonomous Deep Agent (2025)
- OctoTools: An Agentic Framework with Extensible Tools for Complex Reasoning (2025)
- Defining and Detecting the Defects of the Large Language Model-based Autonomous Agents (2024)
- CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation (2025)
- Leveraging Dual Process Theory in Language Agent Framework for Real-time Simultaneous Human-AI Collaboration (2025)
Please give a thumbs up to this comment if you found it helpful!
If you want recommendations for any Paper on Hugging Face checkout this Space
You can directly ask Librarian Bot for paper recommendations by tagging it in a comment: @ librarian-bot recommend
· Sign up or log in to comment

## Models citing this paper 0

No model linking this paper

## Datasets citing this paper 0

No dataset linking this paper

### Spaces citing this paper 0

No Space linking this paper

## Collections including this paper 0

No Collection including this paper

--------------------