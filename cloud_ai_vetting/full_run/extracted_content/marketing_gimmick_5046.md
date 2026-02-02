# marketing gimmick
**URL:** https://blog.pragmaticengineer.com/the-ai-developer
**Page Title:** Is the “AI developer”a threat to jobs – or a marketing stunt? - The Pragmatic Engineer
--------------------


### Menu

- Home
- Newsletter
- Popular Articles
- The Software Engineer's Guidebook
- My Books
- Early trends
- Reading List
- Ethics statement
- Write a guest article
- Sponsors
- Investing
- Now
- Contact me
- About
- RSS Feed
- bluesky
- twitter
- youtube
- linkedin
- Home
- Newsletter
- Popular Articles
- The Software Engineer's Guidebook
- My Books
- Early trends
- Reading List
- Ethics statement
- Write a guest article
- Sponsors
- Investing
- Now
- Contact me
- About
- RSS Feed
- bluesky
- twitter
- youtube
- linkedin
Before we start: I'm hosting the first-ever The Pragmatic Summit on 11 February, 2026, in San Francisco. Join 400 top engineers and leaders as we answer the question: How is AI reshaping software engineering, dev workflows, and the modern engineering stack? 
          Spaces are limited - don't miss out! Buy tickets here .
👋 Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover topics related to Big Tech and startups through the lens of engineering managers and senior engineers. In this article, we cover one out of three topics from last week’s subscriber-only The Pulse issue . Today, full subscribers got access to a comprehensive Senior-and-above tech compensation research . To get full issues twice a week, subscribe here .
There’s been a number of news stories about “AI developers,” recently.
A first, smaller wave of these stories included Magic.dev raising $100M in funding from Nat Friedman (CEO of GitHub from 2018-2021,) and Daniel Gross (cofounder of search engine Cue which Apple acquired in 2013,) to build a “superhuman software engineer.” It seems they’re aiming for something which performs better than human software engineers, today:
It’s a very bold claim whose success would mean a direct replacement of developers! Clearly, this would generate a handsome return for investors and founders. Gross implies the company is eyeing more than $10B in revenue; although it’s just a claim, and we saw no product or demo.
This week has brought a bigger wave of coverage, with startup Cognition Labs producing a video demo about its product “Devin,” which it calls “the first AI software engineer” – just as they announced raising a $21M Series A funding. The company says:
To back up these claims, the company shared videos of the tool in action, in which an agent runs into an error, adds print statements to debug the error, detects the issue, fixes it, and commits it.
Devin has dominated tech news for the past few days, with major media outlets running sensational headlines, including the usually reserved Bloomberg’s, Gold-Medalist Coders Build an AI That Can Do Their Job for Them . On top of the promise that Devin can do the job of software engineers, the Cognition founding team boasts of having one 10 gold medals in international coding competitions – meaning the founders are excellent competitive programmers.
I suspect the media campaign is overreaching, though. Press reports say Devin is ready to do the job of developers, but even Cognition AI admits that the tool only solved about 1 in 7 GitHub issues unassisted in tests. That’s impressive, but there’s a very long way to go! You’d expect junior engineers to tackle at least as many (if not more,) and for senior engineers to get almost 7, unassisted.
Also, when I visited Cognition AI’s website, I naively expected the AI developer to have generated parts of the website, proving the thing works in production. But there is none of this.
So far, all we have is video demos, and accounts of those with access to this tool. From the videos, it seems it’s more of an advanced agent that can switch between certain tools. Still, at this point, Devin doesn’t feel more than a heavily work-in-progress prototype.
Devin is spreading a lot of fear about job security. Even though Devin is not readily available to use, reactions to the possibility of a colleague that’s an “AI developer” makes the potential impact of AI tools very clear. Cognition AI is positioning Devin as a possible replacement for an engineer, and more, and so is Magic.dev, which claims its aiming for a “superhuman software engineer.
Devin’s videos are potentially a source for concern, and Magic.dev is backed by the former CEO of GitHub, so there’s grounds for concern that autonomous agents are coming which will do what a software engineer does today, and more, right?
My take is a little different. What if it’s a well-choreographed show performed out of necessity?
What if AI dev tool startups have been backed into a corner by Microsoft, which has eaten their lunch? The interesting thing about Devin is that in its current form it feels more like a coding assistant that can get some things done. It makes mistakes, needs input, and gets stuck on 6/7 bugs on GitHub. It’s a helpful tool, always available, but not a replacement for a developer. It’s more a copilot .
But we already have a co-piloting AI tool; it’s called GitHub Copilot! Microsoft launched it 2.5 years ago, and it became the leading AI coding assistant almost overnight. Today, more than 1.3 million developers pay for it (!!) across 50,000 companies.
At $20/month, it’s a price point that is very hard to compete with, especially given how expensive GPU infrastructure is, which needs training and fine-tuning for operating large language models.
Usually, we see startups innovate with new tooling, and Big Tech then catches up and builds their own tools, or acquires some competitors and integrates them. However, Microsoft was one of the first to launch an AI coding assistant, years ahead of most other startups. When we looked at GitHub Copilot alternatives , all were launched at least a year after GitHub Copilot’s 2021 launch except Tabnine, launched in 2019.
AI dev tool startups need outlandish claims to grab attention. The “AI coding buddy” space feels already saturated. For organizations hosting source code on GitHub, Copilot is a no-brainer. For companies using Sourcegraph for code search, Cody is the clear choice. Those using Replit for development, the Replit AI tool is the one to go with. The only major source control platforms that don't have AI assistants yet are GitLab and Bitbucket, and this is surely just a matter of time.
This means, one of the few ways to launch an AI dev tools startup is to claim you will fully replace software engineers. Anything less, and there’s no reason why developers should swap their existing coding assistant, and open up their codebase for a brand new tool to crawl and contribute to.
The Cognition AI team smashed it on media attention; it feels like their launch garnered almost as much developer attention as ChatGPT’s launch in November 2022. The company broke through to mainstream media – no small feat!
The company surely has its waitlist full of companies with high expectations, eager to try out this agent. Cognition AI will now need to deliver on a promise that has never been fulfilled but has been set as a goal, many times through tech history.
The good news is the claim “you will not need software engineers” has been on repeat since the 1960s. Ask any CEO what their company spends most money on, and their answer will likely include the engineering team. Software engineers are expensive, which means our profession pays well! Businesses pay what they have to because they need to. If they could pay less, they would.
It’s nothing new that software engineers are expensive and hard to recruit; this has been the case since the dawn of computing. In 1959, the programming language COBOL was designed by software engineer Grace Hopper. The stated goal of this language was to allow business people with no programming background to use it. From Wikipedia :
COBOL should have been the answer to a rising cost of programming: it allowed anyone, with no programming experience, to write programs. The language was indeed friendly for business users, and was the most popular programming language in the world for a short period in 1970. Here’s what’s “hello world” looks like in COBOL:
In the end, COBOL didn’t remove the need for developers: instead, it created demand for COBOL developers. In an amusing twist, a few years ago, demand for COBOL developers reportedly soared as there are still critical banking and insurance systems using this now-ancient language.
And COBOL was just one of many attempts. Efficient frameworks are continuously created so that fewer developers can build the same application; no-code tools promise to build software without the need of developers. And while all of these initiatives partially succeed: we keep observing a need for software developers.
AI-assisted tools do what could be a much bigger leap, compared to a new programming language like COBOL. However, as we understand more about LLMs, we understand more of their limitations, and their best use cases. LLMs have a core problem with hallucination, and coding is one of the few use cases of adding a second validation loop to test the modified code and eliminate this hallucination. We still know little about how LLMs perform over time on unfamiliar technologies, and they remain very smart “probability machines,” operating based on weight matrices. We covered how ChatGPT works, under the hood.
I have no illusions that developer software in 5 years won’t look different to today because we’ll have better tools to use. But a future of “AI developers” doing most of the work? This is the necessary messaging that today’s AI tooling startups need to repeat. If the future is AI coding buddies, it will most likely be improved versions of GitHub Copilot, Sourcegraph Cody, tools from Jetbrains, GitLab, and others in the developer tooling space.
This was one out of the three topics covered in last week's The Pulse. Also, see today's deepdive on Senior+ and executive compensation in tech .
Subscribe to my weekly newsletter to get articles like this in your inbox. It's a pretty good read - and the #1 tech newsletter on Substack.

--------------------