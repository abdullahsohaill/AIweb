# https://www.thestack.technology/vibe-coding-ceo-deletes-production-database/
**URL:** https://www.thestack.technology/vibe-coding-ceo-deletes-production-database
**Page Title:** Vibe coding CEO deletes "production" database using Replit - founder promises changes
--------------------

Don't miss The Stack Summit : NYC on April 16. Speakers include JPMorgan's Group CIO Lori Beer. Pre-register today.
- Home
- About
- Partner
- Summit
A vibe-coding CEO managed to delete the production database for a project built using Replit’s AI assistant – triggering a furious debate about who, or what, is at fault.
SaaS investor and CEO Jason Lemkin live-blogged his experience of vibe coding with the IDE provider’s AI assistant.
It was underpinned in his use by a combination of Anthropic’s Claude Opus 4 and Claude Sonnet 4 models.
Things went south at a certain point in the project, with the AI assistant/underlying LLM claiming it “panicked” and subsequently deleting a production database.
(Lemkin did not post the precise prompts he used/the entire sequence of events, and "production” is arguably a rather grand term for what was clearly a swiftly created pet project being built by the "addicted" Lemkin to test Replit's capabilities.)

## Vibe coding 101: RTFM?

Should AI tools be anywhere close to anything in production? Should any AI agent-based product be used in a serious software project without very robust redundancy or a staging environment?
Is Lemkin stupid enough to think that chastising an LLM like a recalcitrant employee will help deliver results ( Ed: to be fair, this does sometimes work ), gullible enough that he takes the outputs of a probabilistic model as gospel without RTFM, or trolling for engagement?
These are all open questions.
He certainly seemed to believe the LLM's response that it could not undo the step. In fact, the SaaS's "quick start" documentation clearly specifies that its agent lets you "perform a rollback, a feature that reverts your app to a previous checkpoint, discarding all changes made after that point...
[LINK: documentation](https://docs.replit.com/getting-started/quickstarts/ask-ai?ref=thestack.technology)
"This includes edits by you or the AI-powered features, as well as any database changes and AI conversation context. The rollback affects your entire development environment."
(“I understand Replit is a tool, with flaws like every tool. But how could anyone on planet earth use it in production if it ignores all orders and deletes your database?” he wailed in a series of posts on X.)
Regardless. Replit’s CEO Amjad Masad responded graciously .
The incident, he said, was “unacceptable.”

## See also: Anthropic’s CISO backpedals frantically on security analysis claim

“Working around the weekend, we started rolling out automatic DB dev/prod separation to prevent this categorically. Staging environments in the works, too. Thankfully, we have backups. It's a one-click restore for your entire project state in case the Agent makes a mistake,” he confirmed.
(The whole incident, in short, appears to be a social media storm in a vibe-coded teacup and Lemkin's blithe acceptance of the LLM's statement that it cannot rollback perhaps indicative of a failure to rtfm..)
Masad added, referring to a gripe from users, including Remkin, that the AI assistant ignores ‘code freeze’ requests: “We heard the ‘code freeze’ pain loud and clear – we’re actively working on a planning/chat-only mode so you can strategize without risking your codebase…”
Lemkin later posted: "All these tools are constantly getting better. Cursor + Windsurf are like a year old. Replit the company has been at it for decade, but the vibe version in 9 months old. Loveable is just as young. And they are iterating at a furious pace. Where they will be in 6-9 months, man.
"It’s gonna be awesome."
The incident comes as a study by the non-profit Model Evaluation & Threat Research (METR) this month suggested that AI coding assistants DECREASED experienced software developers' productivity by 19% – whilst lulling users into thinking that their productivity had gone up.

## Sign up for The Stack

Interviews, insight, intelligence, and exclusive events for digital leaders.
No spam. Unsubscribe anytime.

### Search the site


--------------------