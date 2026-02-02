# Development Productivity, Not Developer Productivity
**URL:** https://redmonk.com/rstephens/2025/09/25/development-productivity
**Page Title:** Development Productivity, Not Developer Productivity – Alt + E S V
--------------------

Skip to Content
Imagine a snake that just ate a mouse.
A snake can unhinge its jaw and swallow its prey whole in seconds, but it takes the snake’s body quite a long time to digest the mouse. In the meantime there’s an unmistakable mouse-shaped lump slowly making its way through the snake’s body.
The state of the AI market in 2025 is dominated by code generation tools. There are other solutions around the periphery, but to date, code gen is the AI use case that has traction and widespread adoption.
Tools that help developers write code faster can be great!
But what if we’ve inadvertently created a lump-in-the-snake scenario? (Arguably in some cases we’ve Antoine de Saint-Exupéry -ied the situation and created a boa constrictor that swallowed an elephant.)
At the industry level, we’ve collectively swallowed the mouse with widespread AI code generation adoption. But each enterprise has their own snake as individual development teams moving faster while the rest of the SDLC still digests at the same old speed.
As an industry we’ve embraced the creation of code using AI assistance; we’ve swallowed a mouse. However, the rest of the SDLC has not kept up. We’ve created a glut of code, but the constraints on the rest of the system remain largely unchanged. We do not have a scalable repeatable way to metaphorically digest this influx of code.
Code assistance, in some ways, was the simplest problem to tackle first as opposed to other aspects of the SDLC. Developers tend to embrace change more than ops people. There was a large corpus of data available to train the models, which meant there was a clear and marketable use case to target towards developers.  Furthermore, the target area of tools to tackle is relatively constrained. The number of possible permutations of tools used together in the full tech stack is massive, but tackling the IDE (and even more specifically, building solutions for either VS Code or a fork of VS Code) is relatively confined as a target.
Developers may be moving faster than ever with these tools. Part of the appeal of AI coding tools is how easy they make vibe coding . The fast, exploratory, write-now-polish-later style of development can make individual developers feel wildly productive. But while vibe coding can feed the snake at record speed, the rate of digestion has not commensurately changed.
Security and Operations tooling is on its way, though adoption is harder to discern because the market is so fractured. Many enterprises have started using some of the AI capabilities being built into SecOps tools. But by and large this AI functionality is less mature and the tools collectively have less traction in market than AI coding assistants.
The 2024 DORA Report has some counterintuitive findings about individuals reported productivity using AI compared to systemic metrics. Here’s my summary of the findings:
Roughly 75% of people report using AI as part of their jobs and report that AI makes them more productive.
And yet, in this same survey we get these findings:
- if AI adoption increases by 25%, time spent doing valuable work is estimated to decrease 2.6%
- if AI adoption increases by 25%, estimated throughput delivery is expected to decrease by 1.5%
- if AI adoption increases by 25%, estimated delivery stability is expected to decrease by 7.2%
Rachel Stephens, DORA Report 2024 – A Look at Throughput and Stability
In my analysis about why, I hypothesized:
But I think thus far a lot of the industry metrics around AI have been focused on individuals rather than holistic systems. I think what the DORA report is showing is that a x% code acceptance rate might be a great way to see how developers benefit from AI, but an individual developer or even a team of developers going faster does not necessarily make the system move faster. Our systems interact in complex ways.
Or in other words, eating more and more mice does not make the snake digest its food any faster.
Developer productivity measures that do not consider the holistic system are meaningless. This has always been the case; the DORA metrics have addressed this (starting before AI tools were in use) by using global measures of throughput and stability.
Amazon recently published a blog post about calculating their ‘cost to serve software’ metric in a post Quantifying the Impact of Developer Experience: Amazon’s 15.9% Breakthrough .
[LINK: Quantifying the Impact of Developer Experience: Amazon’s 15.9% Breakthrough](https://aws.amazon.com/blogs/enterprise-strategy/business-value-of-developer-experience-improvements-amazons-15-9-breakthrough/)
No matter what metric you use, it’s worth remembering to take “time saved” marketing with many grains of salt. A tool that markets itself as saving an individual developer an hour doesn’t necessarily save the company an hour if the overall system throughput or stability doesn’t change.
AI tools have made it easier than ever to feed the snake. But until the rest of the system learns to digest as quickly as it swallows, speed gains stay stuck in the middle.
And just one more time, I am very sorry to everyone averse to snakes, mice, and digestion-related metaphors.
Disclaimer: AWS and Google (DORA) are RedMonk clients.

## No Comments

### Leave a Reply Cancel reply

### About

I’m Rachel Stephens, Research Director with RedMonk. I focus on helping clients understand and contextualize technology adoption trends, particularly from the lens of the practitioner. I cover a broad range of developer and infrastructure products, with a particular focus on developer tools.
Before joining RedMonk, I worked as a database administrator and financial analyst. I am located in Colorado.
- Bluesky
- Mastodon
- Twitter
- LinkedIn
- GitHub
[LINK: GitHub](https://github.com/gitcub)
- RSS Feed

### Subscribe via Email

### Recent Posts

- DORA 2025: Measuring Software Delivery After AI
- Progressive Delivery
- Development Productivity, Not Developer Productivity
- MongoDB AMP
- An Evolution of Agent Demos that Impressed Me

### Categories

### Archives

### Recent Comments

- Trevor Mitchell on Heroku in 2025
- 16 Cute and Cuddly Animals You’ll Fall in Love With, Just Like Koalas – Animals Realm on You Otter Know
- Alex Williams on IANAL: agent edition
- Rob Hirschfeld on Under New Management: Impressions from VMware Explore 2024
- RobBob on AI Headshots vs. My Senior Pictures

--------------------