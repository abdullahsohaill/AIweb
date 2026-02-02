# The Ultimate Guide to AI Agents for PMs
**URL:** https://www.productcompass.pm/p/ai-agents
**Page Title:** Introduction to AI Agents for PMs - by Paweł Huryn
--------------------


## The Product Compass

## Introduction to AI Agents for PMs

### What is an AI agent? How to build an AI agent? Multi-agent systems, AI agent frameworks, recommend tolls, resources, and more.

Hey, welcome to the premium edition of The Product Compass newsletter.
Every week, I share actionable tips, templates, resources, and insights for AI PMs.
Consider subscribing or upgrading your account for the full experience:
Updated: 11/2/2025
AI agents are the most valuable skill in AI and product right now.
This is an extended edition of several posts I recently published on social media with more new tools and resources.
In this issue, we cover:
- What is an AI Agent
What is an AI Agent
- How to Build an AI Agent
How to Build an AI Agent
- 🔒 What Are Multi-Agent Systems (With Agent Types and Architectures)
🔒 What Are Multi-Agent Systems (With Agent Types and Architectures)
- 🔒Workflows, Agentic Workflows, and Agentic AI
🔒Workflows, Agentic Workflows, and Agentic AI
- 🔒 AI Agent Frameworks: Comparison and Recommendation
🔒 AI Agent Frameworks: Comparison and Recommendation
- 🔒 Recommended AI Agent Tools and Resources
🔒 Recommended AI Agent Tools and Resources

## 1. What is an AI Agent

Anthropic offered the best definition:
"Agents (...) are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."
An AI agent is like an LLM on steroids. It can:
- Autonomy : Pursue its goals autonomously.
Autonomy : Pursue its goals autonomously.
- Reasoning : Plan tasks, take action, analyze the results, and adjust.
Reasoning : Plan tasks, take action, analyze the results, and adjust.
- Tools : Use tools (e.g., a function, MCP server, API, data retrieval, or code editor).
Tools : Use tools (e.g., a function, MCP server, API, data retrieval, or code editor).
- Memory : Remember its previous actions, or even learn from past interactions.
Memory : Remember its previous actions, or even learn from past interactions.
Some AI agents can also collaborate or delegate work to other AI agents or humans.
An example implementation of an AI agent with n8n with short-term memory, built-in tools (Google Sheets, Gmail) and Atlassian MCP server:

## 2. How to Build an AI Agent

Building the first AI agent might take just 30-60 minutes.
Share
Here’s how:

### Step 1: Define a System Prompt

It defines the goals, logic, and expectations.
I suggest you start with 14 Prompting Techniques Every PM Should Know .
Other guides:
- GPT-5 Prompting Guide - unique insights, especially for coding agents
GPT-5 Prompting Guide - unique insights, especially for coding agents
- GPT-4.1 Prompting Guide - focuses on agentic capabilities
GPT-4.1 Prompting Guide - focuses on agentic capabilities
- Anthropic Prompt Engineering - my go to resource
Anthropic Prompt Engineering - my go to resource
[LINK: Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- (Optional) Prompt Engineering by Google
(Optional) Prompt Engineering by Google
- (Optional, super valuable) System Prompt Analysis for Claude 4
(Optional, super valuable) System Prompt Analysis for Claude 4

### Step 2: Select an LLM

Unless the framework handles iterating (e.g., n8n), start with a reasoning model (e.g., GPT-5-mini).

### Step 3: Connect Tools

What might your AI agent need to achieve its goals? Consider simple tools, like a calculator, custom functions, integrations, data sources, and MCP servers.

### Step 4: Connect Memory

The agent must track its progress and learn. Most platforms support:
- Short-term memory (variables, last interactions)
Short-term memory (variables, last interactions)
- Long-term memory (vector, SQL, graph)
Long-term memory (vector, SQL, graph)
- Scratchpad (e.g., n8n Think tool)
Scratchpad (e.g., n8n Think tool)

### Step 5: Orchestrate the Logic

Whether a single agent or multiple agents working together, you must:
- Map/code repeatable logic (flow) that doesn't belong to specific agents
Map/code repeatable logic (flow) that doesn't belong to specific agents
- Orchestrate communication between AI agents (static or dynamic)
Orchestrate communication between AI agents (static or dynamic)
You might also like the AI Agent Architectures With n8n Examples .

### Step 6: Add User Interface

If your AI agent is user-facing, you can easily add logic using tools like Lovable, Bolt, or Google Firebase. No coding.
For more information, see:
- Best Practices: How to Create SaaS Without Coding
Best Practices: How to Create SaaS Without Coding
- A Complete Course: How to Build a Full-Stack App with Lovable (No-Coding)
A Complete Course: How to Build a Full-Stack App with Lovable (No-Coding)
- Advanced: No-Code B2C SaaS Template With Stripe Payments
Advanced: No-Code B2C SaaS Template With Stripe Payments

### Step 7: Evaluate the AI Agent

Rather than relying on standard metrics (hallucinations, helpfulness), perform error analysis and let metrics naturally emerge.
Some evaluators can serve as guardrails, executed at inference time. Most are code-based evals.
Our guides:
- Mastering AI Evals: A Complete Guide for PMs
Mastering AI Evals: A Complete Guide for PMs
- AI Evals: How to Find The Right AI Product Metrics
AI Evals: How to Find The Right AI Product Metrics
- A PM’s Guide to Evaluating AI Agents
A PM’s Guide to Evaluating AI Agents
If your system involves RAG, evaluate retrieval and generation separately. Jason Liu’s There Are Only 6 RAG Evals provides a framework that maps well to this separation.

### Bottom Line: Start Building. Stop Theorizing.

You can start with those step-by-step guides (<60 min):
- How to Build a RAG Chatbot, No Coding
How to Build a RAG Chatbot, No Coding
- J.A.R.V.I.S. for PMs: Automate Anything with n8n and MCP
J.A.R.V.I.S. for PMs: Automate Anything with n8n and MCP
- How to Build Anthropic Multi-Agent Research System
How to Build Anthropic Multi-Agent Research System

## 3. What Are Multi-Agent Systems (With Agent Types and Architectures)

## Keep reading with a 7-day free trial

Subscribe to The Product Compass to keep reading this post and get 7 days of free access to the full post archives.

--------------------