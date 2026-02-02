# Anthropic Model Comparison
**URL:** https://docs.anthropic.com/en/docs/about-claude/models
**Page Title:** Models overview - Claude API Docs
--------------------


## Choosing a model

If you're unsure which model to use, we recommend starting with Claude Sonnet 4.5 . It offers the best balance of intelligence, speed, and cost for most use cases, with exceptional performance in coding and agentic tasks.
All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available via the Anthropic API, AWS Bedrock, and Google Vertex AI.
Once you've picked a model, learn how to make your first API call .
[LINK: learn how to make your first API call](/docs/en/get-started)

### Latest models comparison

[LINK: Extended thinking](/docs/en/build-with-claude/extended-thinking)
[LINK: Priority Tier](/docs/en/api/service-tiers)
1 - Aliases automatically point to the most recent model snapshot. When we release new model snapshots, we migrate aliases to point to the newest version of a model, typically within a week of the new release. While aliases are useful for experimentation, we recommend using specific model versions (e.g., claude-sonnet-4-5-20250929 ) in production applications to ensure consistent behavior.
2 - See our pricing page for complete pricing information including batch API discounts, prompt caching rates, extended thinking costs, and vision processing fees.
[LINK: pricing page](/docs/en/about-claude/pricing)
3 - Claude Sonnet 4.5 supports a 1M token context window when using the context-1m-2025-08-07 beta header. Long context pricing applies to requests exceeding 200K tokens.
[LINK: 1M token context window](/docs/en/build-with-claude/context-windows#1m-token-context-window)
[LINK: Long context pricing](/docs/en/about-claude/pricing#long-context-pricing)
4 - Reliable knowledge cutoff indicates the date through which a model's knowledge is most extensive and reliable. Training data cutoff is the broader date range of training data used. For example, Claude Sonnet 4.5 was trained on publicly available information through July 2025, but its knowledge is most extensive and reliable through January 2025. For more information, see Anthropic's Transparency Hub .
[LINK: third-party platform pricing section](/docs/en/about-claude/pricing#third-party-platform-pricing)

## Prompt and output performance

Claude 4 models excel in:
- Performance : Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the Claude 4 blog post for more information.
Performance : Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the Claude 4 blog post for more information.
- Engaging responses : Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our prompt engineering guides for details. For specific Claude 4 prompting best practices, see our Claude 4 best practices guide .
Engaging responses : Claude models are ideal for applications that require rich, human-like interactions.
- If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our prompt engineering guides for details.
[LINK: prompt engineering guides](/docs/en/build-with-claude/prompt-engineering)
- For specific Claude 4 prompting best practices, see our Claude 4 best practices guide .
[LINK: Claude 4 best practices guide](/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices)
- Output quality : When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.
Output quality : When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.

## Migrating to Claude 4.5

If you're currently using Claude 3 models, we recommend migrating to Claude 4.5 to take advantage of improved intelligence and enhanced capabilities. For detailed migration instructions, see Migrating to Claude 4.5 .
[LINK: Migrating to Claude 4.5](/docs/en/about-claude/models/migrating-to-claude-4)

## Get started with Claude

If you're ready to start exploring what Claude can do for you, let's dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we've got you covered.
[LINK: Intro to Claude Explore Claude's capabilities and development flow.](/docs/en/intro)
Explore Claude's capabilities and development flow.
[LINK: Quickstart Learn how to make your first API call in minutes.](/docs/en/get-started)
Learn how to make your first API call in minutes.
Craft and test powerful prompts directly in your browser.
If you have any questions or need assistance, don't hesitate to reach out to our support team or consult the Discord community .
Was this page helpful?

--------------------