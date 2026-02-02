# Devin.ai
**URL:** https://devin.ai
**Page Title:** Devin | The AI Software Engineer
--------------------


## How Nubank refactors millions of lines of code to improve engineering efficiency with Devin

## Overview

One of Nubank’s most critical, company-wide projects for 2023-2024 was a migration of their core ETL — an 8 year old, multi-million lines of code monolith — to sub-modules. To handle such a large refactor, their only option was a multi-year effort that distributed repetitive refactoring work across over one thousand of their engineers. With Devin, however, this changed: engineers were able to delegate Devin to handle their migrations and achieve a 12x efficiency improvement in terms of engineering hours saved, and over 20x cost savings. Among others, Data, Collections, and Risk business units verified and completed their migrations in weeks instead of months or years.

## The Problem

Nubank was born into the tradition of centralized ETL FinServ architectures. To date, the monolith architecture had worked well for Nubank — it enabled the developer autonomy and flexibility that carried them through their hypergrowth phases. After 8 years, however, Nubank’s sheer volume of customer growth, as well as geographic and product expansion beyond their original credit card business, led to an entangled, behemoth ETL with countless cross-dependencies and no clear path to continuing to scale.
For Nubankers, business critical data transformations started taking increasingly long to run, with chains of dependencies as deep as 70 and insufficient formal agreements on who was responsible for maintaining what. As the company continued to grow, it became clear that the ETL would be a primary bottleneck to scale.
Nubank concluded that there was an urgent need to split up their monolithic ETL repository, amassing over 6 million lines of code, into smaller, more flexible sub-modules.
Nubank’s code migration was filled with the monotonous, repetitive work that engineers dread. Moving each data class implementation from one architecture to another while tracing imports correctly, performing multiple delicate refactoring steps, and accounting for any number of edge cases was highly tedious, even to do just once or twice. At Nubank’s scale, however, the total migration scope involved more than 1,000 engineers moving ~100,000 data class implementations over an expected timeline of 18 months.
In a world where engineering resources are scarce, such large-scale migrations and modernizations become massively expensive, time-consuming projects that distract from any engineering team’s core mission: building better products for customers. Unfortunately, this is the reality for many of the world’s largest organizations.

## The Decision: an army of Devins to tackle subtasks in parallel

At project outset in 2023, Nubank had no choice but to rely on their engineers to perform code changes manually. Migrating one data class was a highly discretionary task, with multiple variations, edge cases, and ad hoc decision-making — far too complex to be scriptable, but high-volume enough to be a significant manual effort.
Within weeks of Devin’s launch, Nubank identified a clear opportunity to accelerate their refactor at a fraction of the engineering hours. Migration or large refactoring tasks are often fantastic projects for Devin: after investing a small, fixed cost to teach Devin how to approach sub-tasks, Devin can go and complete the migration autonomously. A human is kept in the loop just to manage the project and approve Devin’s changes.

## The Solution: Custom ETL Migration Devin

A task of this magnitude, with the vast number of variations that it had, was a ripe opportunity for fine-tuning. The Nubank team helped to collect examples of previous migrations their engineers had done manually, some of which were fed to Devin for fine-tuning. The rest were used to create a benchmark evaluation set. Against this evaluation set, we observed a doubling of Devin’s task completion scores after fine-tuning, as well as a 4x improvement in task speed. Roughly 40 minutes per sub-task dropped to 10, which made the whole migration start to look much cheaper and less time-consuming, allowing the company to devote more energy to new business and new value creation instead.
Devin contributed to its own speed improvements by building itself classical tools and scripts it would later use on the most common, mechanical components of the migration. For instance, detecting the country extension of a data class (either ‘br’, ‘co’, or ‘mx’) based on its file path was a few-step process for each sub-task. Devin’s script automatically turned this into a single step executable — improvements from which added up immensely across all tens of thousands of sub-tasks.
There is also a compounding advantage on Devin’s learning. In the first weeks, it was common to see outstanding errors to fix, or small things Devin wasn’t sure how to solve. But as Devin saw more examples and gained familiarity with the task, it started to avoid rabbit holes more often and find faster solutions to previously-seen errors and edge cases. Much like a human engineer, we observed obvious speed and reliability improvements with every day Devin worked on the migration.
“Devin provided an easy way to reduce the number of engineering hours for the migration, in a way that was more stable and less prone to human error. Rather than engineers having to work across several files and complete an entire migration task 100%, they could just review Devin’s changes, make minor adjustments, then merge their PR”
Jose Carlos Castro, Senior Product Manager

## Devin, the AI software engineer

Crush your backlog with your personal AI engineering team.
- 1 Ticket Integrate Slack, Teams, Linear, and Jira
- 2 Plan Quickly review Devin's proposal
- 3 Test Devin tests changes by itself
- 4 PR Review changes natively
- Ticket Integrate Slack, Teams, Linear, and Jira
- Plan Quickly review Devin's proposal
- Test Devin tests changes by itself
- PR Review changes natively

## Use cases

### Code Migration + Refactors

- Language migrations
- Version upgrades
- Codebase restructuring

### Data Engineering + Analysis

- Data warehouse migrations
- ETL development
- Data cleaning and preprocessing

### Bugs + Backlog Work

- Ticket resolution
- CI/CD
- First-draft PR creation for backlog tasks

### Code Migration + Refactors

- Language migrations
- Version upgrades
- Codebase restructuring

### Data Engineering + Analysis

- Data warehouse migrations
- ETL development
- Data cleaning and preprocessing

### Bugs + Backlog Work

- Ticket resolution
- CI/CD
- First-draft PR creation for backlog tasks

### Application development

- Frontend bugs and edge cases
- Unit and E2E testing
- Building SaaS integrations

### Bug & issue triage

- Automated on-call response
- Ticket resolution
- CI/CD autotriage

### And many others

- Technical debt
- Performance optimization
- Scraping
- New repo onboarding
- Maintaining documentation

## Learn & work together

Devin is built for collaboration and can learn to fit into your unique workflow.

### Devin learns your codebase & picks up tribal knowledge

### Code on the go

Write code using natural language instructions with Devin on mobile.

### Use Devin's editor, shell and browser

Take over and run commands, edit code, or use the browser for Devin at any time.

## Able to work with hundreds of tools Devin connects to your favorite MCP servers, from Asana to Zapier

Devin connects to your favorite MCP servers, from Asana to Zapier
Devin can independently create PRs, respond to PR comments, review PRs, etc.
Assign Devin tickets directly in Linear, or add the Devin tag.
Assign Devin tasks by tagging @Devin in Slack or Teams. Devin keeps you updated on progress in replies.
Tag @Devin directly in Linear tickets or add the Devin tag to delegate tasks to Devin.

## Build with Devin

### Build more with Devin

Devin Enterprise provides additional capabilities, security and control for your organization.

--------------------