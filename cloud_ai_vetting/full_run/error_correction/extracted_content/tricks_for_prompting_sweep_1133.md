# Tricks for prompting Sweep
**URL:** https://sweep-ai.notion.site/Tricks-for-prompting-Sweep-3124d090f42e42a6a53618eaa88cdbf1
**Page Title:** Tricks for prompting Sweep
--------------------

### (Raw Extraction Fallback)

Skip to content
Tricks for prompting Sweep
 Tricks for prompting Sweep
 Use Sweep Chat: Instead of using vanilla Sweep, you can use Sweep Chat to plan out the changes by chatting with Sweep, while interactively controlling which files Sweep should be looking at.
 Be specific: Don’t just put “fix typos” or “fix the first error”. Sweep will get confused and probably crash. Put a real issue that you would like solved in your codebase. Oftentimes, this is the lack of tests, especially unit tests. 
 Use GitHub Actions! We highly recommend linters, as well as Netlify/Vercel preview builds. Not only can Sweep auto-correct based on linter and build errors, but it also helps with iteration cycles by providing previews of static sites using Netlify (which we use)
 Mention important files: To ensure that Sweep scans a file, mention the file path or name (src/main.py or main.py) in your ticket. Sweep searches for relevant files at runtime, but specifying the file helps avoid missing important details.
 Reply to Sweep: If Sweep's plan isn't accurate, reply to the same ticket and provide instructions on what changes should be made instead.
 Comment on PRs: If Sweep creates a pull request with a few lines missing small changes, leave a review comment in the file where the change should be made.
 Limitations of Sweep
 Sweep, just like a regular junior developer will likely not get complex issues right first try. Try to keep the tickets to the following sizes. If you break it you’ll likely have to tweak it a lot with PR and code comments.
150 lines of code changes
3 files modified
Files with 60k characters
This equates to about 10k tokens, which having in the context and the generation could break the 32k context window
 Sweep is GPT-4 powered so will not have access to the latest docs and API specs. In the future, it will be able to search for these but for now you can just copy paste the relevant bits into the ticket.
 Similarly, Sweep’s research capabilities are limited. Bug fixes work only when you have a good idea of the cause of the bug but not before that. Sweep will later have access to terminals and debugging tools but for now it’s only great at tasks where the changes are obvious like adding menu items or moving a function to a different file. 
If you find something else that’s really helpful, feel free to ping Kevin and Will on Discord.

--------------------