# https://creatoreconomy.so/p/12-rules-to-vibe-code-without-frustration
**URL:** https://creatoreconomy.so/p/12-rules-to-vibe-code-without-frustration
**Page Title:** 12 Rules to Vibe Code Without Frustration - by Peter Yang
--------------------


## 12 Rules to Vibe Code Without Frustration

### My best tips after 50+ hours building apps with AI (without knowing how to code)

Dear subscribers,
Today, I want to share my 12 best rules for vibe coding.
I’ve spent 50+ hours building apps with AI (e.g., plane simulator , Star Wars run , zombie shooter ) and collected 200+ tips from my post below:
[LINK: plane simulator](https://petergyang.github.io/plane-simulator/)
[LINK: Star Wars run](https://petergyang.github.io/DeathStar/)
[LINK: zombie shooter](https://petergyang.github.io/ZombieSurvival/)
Vibe coding is magical, but it can also be incredibly frustrating. So let’s break down these 12 rules to help you build apps with AI without getting stuck:
P.S. If you don’t know what vibe coding means, check out my step-by-step guide to build a Star Wars game that complements this post.
This post is brought to you by… LTX Studio
LTX Studio is the best platform to create short films with AI.
I created this Mass Effect inspired short film in just 10 minutes using LTX Studio’s AI-assisted storyboards, consistent characters, epic music, and even SFX. I’m kind of blown away by how easy it is. Try creating your AI movie below.
Create Your AI Movie Now

## Planning

## 1. Start with vibe PMing

When starting a new project, ask AI to create a readme that includes:
- Requirements
Requirements
- Tech stack
Tech stack
- Milestones (up to 5)
Milestones (up to 5)
I call this "vibe PMing" because AI writes the spec with my feedback (I'm too lazy to write it myself 😅).
For example, I asked AI to write a readme for a plane simulator with five milestones that I could playtest. Milestone 1 was simply getting the 3D plane to appear on screen.
Pro tip: Many users claim that Grok is better at planning than Sonnet 3.7. Consider writing the readme using Grok and copying it to Cursor or another IDE.

## 2. Keep your tech stack simple

The simpler your tech stack, the less likely AI will break your app.
Everyone's vibe coding games because ThreeJS is a simple JavaScript library. Most of the time, you can build apps with client and local storage. There’s often no need for:
- Servers, databases, or complex tooling.
Servers, databases, or complex tooling.
- Even deploying your app to production (e.g., a URL).
Even deploying your app to production (e.g., a URL).
There’s no shame in building personal apps that can only be accessed via localhost.

## 3. Give AI the right rules & documentation

Giving AI the right context upfront helps you avoid frustration later. Three mini tips:
AI models have knowledge cutoffs that limit which libraries they know.
For example, Tailwind CSS upgraded to v4 in January 2025, but most AI models only know about v3 and will screw up the code.
Instead, ask AI which version it knows (e.g., "Which Tailwind version are you familiar with?") and start with that.
If you’re trying to get AI to hook up an API or install a framework, find the relevant documentation online and paste it into AI’s context.
For example, if you insist on using Tailwind v4, it’s best practice to paste Tailwind’s v4 documentation when you ask AI to set it up.
[LINK: Tailwind’s v4 documentation](https://tailwindcss.com/docs/installation/using-vite)
If you're using Cursor, you should create global and project-specific rules to control AI’s behavior. Here are a few global rules that I’ve added:
[LINK: global and project-specific rules](https://docs.cursor.com/context/rules-for-ai)
- Explain what you’ll do first and ask for my confirmation before coding.
Explain what you’ll do first and ask for my confirmation before coding.
- Do the simple thing first. Use modules instead of just a single file.
Do the simple thing first. Use modules instead of just a single file.
- Only make requested changes
Only make requested changes
- Do not write duplicate code - please look for existing solutions in the codebase.
Do not write duplicate code - please look for existing solutions in the codebase.
For project rules, I recommend this rules library by PatrickJS . For example, if you’re building with TailwindCSS, copy these rules into your project to avoid issues.
[LINK: rules library by PatrickJS](https://github.com/PatrickJS/awesome-cursorrules)
[LINK: rules](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/html-tailwind-css-javascript-cursorrules-prompt-fi/.cursorrules)
Pro tip: You can also get AI to index documentation directly in Cursor. Simply go to Cursor settings → Features → Docs and add the links.

## Coding

## 4. Ask AI NOT to code

“Tell me your plan first; don’t code.”
Ironically, this is probably my most common AI coding prompt.
Even if you don't know how to read code, it’s worth asking AI what it wants to do first. 9 out of 10 times, it'll suggest a complicated approach that you should then ask it to simplify. Here’s an example from building my plane game:

## 5. Ask AI for options and pick the simple one

“Give me a few options, starting with the simplest first. Don’t code.”
This is another common prompt that I use, especially for complex features.
For example, when adding enemy UFO AI to my plane game, I asked AI to give me some options, starting with the simplest. It listed a bunch of options, and I picked the 2nd simplest one:
Another powerful prompt is:
"Think as long as you need and ask me questions if you need more info."
This way, AI can ask you to clear up any uncertainties before coding.

## 6. Break tasks into small steps

In case it’s not obvious, simplicity is your best friend for vibe coding.
Models like Claude 3.7 tend to act like overconfident interns who do more than you ask and introduce unnecessary bugs. Try these approaches to keep things simple:
- Ask AI to “Keep it simple” in your prompt.
Ask AI to “Keep it simple” in your prompt.
- Ask AI to “Implement the simplest next step I can test.”
Ask AI to “Implement the simplest next step I can test.”
- Ask AI to change a specific file only.
Ask AI to change a specific file only.
I recommend starting a fresh chat for each feature to avoid bloating AI’s context window. You must give your AI new grad intern specific steps like a good manager.

## 7. Include images to give AI context

A picture is worth a thousand words to AI.
When you want AI to create a design or fix a bug, include a quick screenshot so that AI can see what you see.
For example, when creating the plane model for my game, including the screenshot below made it possible for AI to one-shot a similar plane model.

## Debugging

## 8. Test ruthlessly after every change

Despite all the tips above, you’ll inevitably hit situations where AI breaks your app.
Test your app in localhost after each update to catch problems early. Open your browser console (right-click and inspect or cmd-option-J on Mac) to check for errors.
If you're more advanced, you can also ask AI to write tests for you, but at minimum, you should personally verify that nothing is fundamentally broken after each change. Small, incremental testing prevents nightmare debugging sessions later.

## 9. Don't hesitate to revert

Cursor and Windsurf have a "Revert to checkpoint" button that restores past versions of your code. Use it liberally when AI:
- Makes changes that break your app
Makes changes that break your app
- Gets stuck in a doom loop trying to fix bugs
Gets stuck in a doom loop trying to fix bugs
- Starts changing all your files without reason
Starts changing all your files without reason
That last one is crucial. Your app might work, but AI's random changes could make future debugging 10x harder. Periodically, you should also ask AI:
“Look for duplicate code or redundancies and list them.”
Then ask AI to make the simple fixes to keep your code base clean.

## 10. Use Github for version control

This is obvious for engineers but vital for PMs and non-coders. GitHub is a remote repository of your project that lets you revert to working versions when things break.
To use GitHub:
- Create a GitHub account
Create a GitHub account
[LINK: GitHub account](https://github.com/)
- Set up a new repository for your project
Set up a new repository for your project
- Ask Cursor to "commit to Github" and share your repo link
Ask Cursor to "commit to Github" and share your repo link
You can also use Git commands manually, but step 3 works fine if you're lazy. The point is — Git provides an additional safety net when checkpoint reverting fails. I commit to Git whenever I complete a milestone from my readme spec.

## Vibing

## 11. Use your voice to feel the vibes

For the full vibe coding experience, install voice dictation software like Superwhisper . Then, just talk to AI instead of typing.
Imagine sitting at night in the dark, music playing softly as you dictate code instructions through your voice. It's arguably more fun than watching Netflix.

## 12. Ask AI to explain the code

Vibe coding is fun, but you should also use it to become more technical:
- For individual files, ask AI to “explain how this file works in simple terms.” or “Add comments that explain the code.”
For individual files, ask AI to “explain how this file works in simple terms.” or “Add comments that explain the code.”
- For entire code bases, use Repomix to create a single file with your entire codebase and then paste it into a large context AI model like Gemini with the prompt: “Can you explain how this app works? Give me an overview of the tech architecture.”
For entire code bases, use Repomix to create a single file with your entire codebase and then paste it into a large context AI model like Gemini with the prompt: “Can you explain how this app works? Give me an overview of the tech architecture.”
Focus on understanding how the code works instead of learning how to code.
Understanding the tech architecture and how things work is, in my opinion, more important than learning to code manually at this point. Learn from each project so you improve for the next one.

## Anyone can start vibe coding now

To recap, here are my 12 rules again:
Share this post with others and encourage your friends to start their vibe coding journey today. 🙂
even reading it , gives me vibes.
Amazing guidance!

### Ready for more?


--------------------