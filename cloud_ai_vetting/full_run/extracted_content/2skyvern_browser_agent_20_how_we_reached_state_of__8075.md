# 2.Skyvern Browser Agent 2.0: How We Reached State of the Art in EvalsSkyvern Blog
**URL:** https://blog.skyvern.com/skyvern-2-0-state-of-the-art-web-navigation-with-85-8-on-webvoyager-eval
**Page Title:** Skyvern Browser Agent 2.0: How We Reached State of the Art in Evals
--------------------

We're building Skyvern: an open source no-code browser agent builder. Our customers have used Skyvern to build agents that can automatically apply to jobs, log in and fetch invoices, and automatically purchase items from hundreds of different websites.
We just released Skyvern 2.0, which can take a single prompt such as "Navigate to Amazon.com and add an iPhone 16, a phone case, and a screen protector to cart", load Amazon.com and carry out the instruction on your behalf.
Skyvern 2.0, scores state of the art 85.85% on WebVoyager Eval. View the full results here: https://eval.skyvern.com
This is best-in-class performance of all WebAgents, giving advanced closed-source web agents like Google Mariner a run for its money

### TL;DR

- Real World Tests: We ran all of the tests in Skyvern Cloud to get a better representation of autonomous browser operations (ie they didn’t run in any local machines)
- Open Sourced Results: We published the entire evaluation run so you can see exactly Skyvern's thought process and actions for each case. Check it out here: https://eval.skyvern.com/
- See it in action . Try Skyvern Cloud or run Skyvern Open Source locally on your computer to see it in action!
[LINK: Skyvern Open Source](https://github.com/Skyvern-AI/Skyvern?ref=skyvern.com)

## Agent Architecture expansion

Achieving this SOTA result required expanding Skyvern’s original architecture from a single actor prompt to a planner-actor-validator agent loop.

### Skyvern 1.0 - Starting with simple prompts

Skyvern 1.0 involved a single prompt operating in a loop both making decisions and taking actions on a website.
This approach was a good starting point, but scored ~45% on the WebVoyager benchmark. It was really well suited to simple single-objective goals, and could handle complex objectives if the website provided enough feedback to the client.
To illustrate this...
✅ If you asked Skyvern to "Go to Amazon.com and add an iPhone 16 to cart", it would execute it flawlessly every time.
❌ If you asked Skyvern to "Go to Amazon.com and add an iPhone 16, a screen protector, and a case to cart", it would add an iPhone 16 to cart, and use visual feedback to determine what to do next. You would sometimes end up with 3 iPhone 16s in the cart, or 1 iPhone 16 and 2 screen protectors.

### Improvement #1 - Adding a planning phase

To solve this problem, we added a “Planner” phase which could decompose very complex objectives down into smaller achievable goals
- This allowed Skyvern to have a working memory of things it had completed and things that were still waiting to be finished
- This allows Skyvern to work with long complex prompts without increasing the hallucation rate
This approach worked really well! Suddenly, Skyvern was able to consistently carry out complex objectives, and we saw our WebVoyager Eval jump to ~68.7%
But.. we still had some issues. Sometimes, Skyvern would carry out operations thinking they had succeeded, but they had actually failed
⚠️ For example, If you asked Skyvern to "Go to Amazon.com and add an iPhone 16 to cart, a screen protector, and a case to cart"... in a small percentage of cases, Skyvern would attempt to click the "add to cart" button.. but the product didn't actually get added to cart!
In this case, the Task runner would report back that it was successful, and the planner would assume it worked and moved on.

### Improvement #2 - Adding in a Validation phase

We added a “Validator” phase which confirmed whether or not the original goals the “Planner” generates are successfully completed or not.
- This acts as a supervisor function to confirm that the Task executor is achieving its objectives as expected, and report any errors / tweaks back to the Planner so it can make adjustments in real-time as needed
This was the final change needed to boost the WebVoyager accuracy to 85.85%. Now.. if a given action failed, Skyvern had the tools to identify that the desired outcome hadn't been achieved, and could generate new goals to move back to the desired state!

## Test Setup

All tests were run in Skyvern Cloud with an async cloud browser and used a combination of GPT-4o and GPT-4o-mini as the primary decision-making LLMs. The goal of this test is to assert real-world quality — the quality represented by this benchmark is the same as what you would experience with Skyvern ’s browsers running asynchronously.
In addition to the above, we’ve made a few minor tweaks to the dataset to bring it up to date:
- We’ve removed 8 tasks from the dataset because the results are no longer valid. For example, one of the tasks asked to go to apple.com and check when the Apple Vision Pro will be released — in 2025 it’s already been released and forgotten
- Many of the flight / hotel booking tasks referenced old dates. We updated both the prompt and the answer to more modern dates for this evaluation
🔍 For the curious :
The full results can be seen here: https://eval.skyvern.com
The full dataset can be seen here: https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets ,
[LINK: https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets](https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets?ref=skyvern.com)
The full list of modifications can be seen here: https://github.com/Skyvern-AI/skyvern/pull/1576/commits/60dc48f4cf3b113ff1850e5267a197c84254edf1
[LINK: https://github.com/Skyvern-AI/skyvern/pull/1576/commits/60dc48f4cf3b113ff1850e5267a197c84254edf1](https://github.com/Skyvern-AI/skyvern/pull/1576/commits/60dc48f4cf3b113ff1850e5267a197c84254edf1?ref=skyvern.com)

## Test Results

We’re doing something out of the ordinary. In addition to the results, we’re making our entire benchmark run public. You can go to https://eval.skyvern.com and see each entry in the WebVoyager dataset, see what actions Skyvern took and why it took them.
We believe this isn’t aligned with our open source mission, and have decided to publish the entire eval results to the public.
📊 All individual run results can be seen here: https://eval.skyvern.com
🔍 The entire Eval dataset can be seen here: https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets
[LINK: https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets](https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets?ref=skyvern.com)

## Limitations of the WebVoyager benchmark

The WebVoyager benchmark is a comprehensive benchmark testing a variety of prompts on 15 different websites. While this acts as a good first step in testing Web agents, this only captures 15 hand-picked websites of the millions of active websites on the internet.
We think there is tremendous opportunity here to better evaluate web agents against one-another with a more comprehensive benchmark similar to SWE-Bench.

## What’s on the horizon

Browser automation is still a nascent space with tons of room for improvement. While we’ve achieved a major milestone in agent performance, a few important issues are next to be solved:
- Can we improve Skyvern’s reasoning to operate efficiently in situations with more uncertainty? Examples include vague prompts, ambiguous or highly complex websites / tools, websites with extremely poor UX (legacy portals)
- Can we give Skyvern access to more tools so it can effectively log into websites, do purchases, and behave more like a human?
- Can we have Skyvern better memorize things it has already done in the past so it can do them again at a lower price point?

## References

- Google Mariner Report
- Claude Computer Use Report
[LINK: Claude Computer Use Report](https://docs.anthropic.com/en/docs/build-with-claude/computer-use?ref=skyvern.com)
- WebVoyager Report
- WILBUR Report
- AgentE Report
- HCompany Report

## Sign up for more like this.


--------------------