# CrewAI
**URL:** https://blog.replit.com/crew-ai
**Page Title:** Replit — Company Spotlight: CrewAI
--------------------

Blog
- Builder Spotlight

## Company Spotlight: CrewAI

Updated at:
Ornella Altunyan
Kevin Leffew

## AI agents are here to stay

Large Language Models (LLMs) are everywhere, doing various jobs, from chatting to parsing documents. Soon after LLMs took the world by storm, developers started creating more focused, goal-oriented LLM apps modeled after human reasoning and problem-solving, which became known as AI agents.
Here’s how one company is leveraging LangChain and Replit to solve complex tasks.

## AI agents with CrewAI

CrewAI is a library specifically designed to build and orchestrate groups of AI agents. It's made to be straightforward and modular, so integrating it into your projects is a breeze. Think of CrewAI like a set of building blocks - each piece is unique, but they're all designed to fit together smoothly. Built on top of LangChain , it's inherently compatible with many existing tools, including local open-source models through platforms like Ollama .
[LINK: CrewAI](https://github.com/joaomdmoura/crewai)
The AI agents can run natively on the cloud with Replit, making it even easier to get started with CrewAI. Check out the CrewAI templates on Replit to see the agents in action. Or, use them as a starting point for your own projects so you don't have to start from scratch. Here’s how it works.

## How CrewAI works

CrewAI has four main building blocks: Agents, Tasks, Tools, and Crews.
- Agents are your dedicated team members, each with their role, backstory, goal, and memory.
- Tasks are small and focused missions a given Agent should accomplish.
- Tools are the equipment our agents use to perform their tasks efficiently.
- Crews are where Agents, Tasks, and a Process meet. This is the container layer where the work happens.
CrewAI is built on LangChain, enabling developers to equip their agents with any of LangChain's existing tools and toolkits .
[LINK: tools](https://python.langchain.com/docs/integrations/tools)
[LINK: toolkits](https://python.langchain.com/docs/integrations/toolkits)
For example, you could use LangChain’s Gmail Toolkit to enable a crew of AI agents to sort through your inbox and help you write an email after they've done some research. AI agents built with CrewAI support a considerable spectrum of use cases, and the vision is to keep expanding on top of LangChain, allowing you to plug in other components.
[LINK: LangChain’s Gmail Toolkit](https://python.langchain.com/docs/integrations/toolkits/gmail)
Because CrewAI is built on top of LangChain, you can easily debug CrewAI agents with LangSmith . When you turn on LangSmith, it logs all agent runs. This means you can quickly inspect (1) what sequence of calls is being made, (2) what the input to the calls is, and (3) what the output of those calls is. Many of those calls are calls to LLMs - which are non-deterministic and can sometimes produce surprising results. Having this level of visibility into your CrewAI is helpful when trying to make them as performant as possible.
[LINK: LangSmith](https://docs.smith.langchain.com/)

## Try CrewAI

Try the following templates to build your own Crew and see it in action. They contain functional AI agents and crews, each with their own set of goals that you can fork, customize, and test yourself.
- Trip planning assistant
- Building a landing page from a one-line idea
- Individual stock analysis (Disclaimer: this is not investment advice)
Learn about the latest at CrewAI by following their founder , João Moura, on X/Twitter.
More
- Mon, Apr 1, 2024 Builder Profile: Pietro Schirano Pietro Schirano is the co-founder of EverArt. By pursuing his ideas on Replit, he’s been able to nurture a curiosity in AI into a startup with multiple apps and functions, run on Replit.

After starting his career in civil engineering, Pietro wanted to explore more creative endeavors. This journey would lead him to hold design lead roles across household names like OpenTable, Meta, Uber, and Brex, and eventually, to launch his own startup.

An avid social learner, Pietro picked up skills across marketing, business, and engineering in each of his jobs. One topic that particularly grabbed his attention was AI. After ChatGPT launched, Pietro says, “I had an epiphany that the world was never going to be the same.” Immediately, he started to test emerging AI tools, eventually sharing a prototype with his team at Brex that landed him a role as their AI team lead.

“Replit was the easiest A to B to get people experimenting with whatever product I wanted to test.”

## Builder Profile: Pietro Schirano

Pietro Schirano is the co-founder of EverArt. By pursuing his ideas on Replit, he’s been able to nurture a curiosity in AI into a startup with multiple apps and functions, run on Replit.

After starting his career in civil engineering, Pietro wanted to explore more creative endeavors. This journey would lead him to hold design lead roles across household names like OpenTable, Meta, Uber, and Brex, and eventually, to launch his own startup.

An avid social learner, Pietro picked up skills across marketing, business, and engineering in each of his jobs. One topic that particularly grabbed his attention was AI. After ChatGPT launched, Pietro says, “I had an epiphany that the world was never going to be the same.” Immediately, he started to test emerging AI tools, eventually sharing a prototype with his team at Brex that landed him a role as their AI team lead.

“Replit was the easiest A to B to get people experimenting with whatever product I wanted to test.”
- Mon, Apr 1, 2024 Builder Profile: Mason Kim As a Global DevOps Engineer at Zinus, Mason (Junkuk) Kim’s role is to build software to enable the marketing, business, and customer service teams to deliver their customers the highest quality support experience.

Often, the required turnaround time for these projects is extremely short, and Mason will need to have a solution ready within days or even hours. Even more, the teams he is supporting are based in numerous countries around the globe. The speed at which Mason’s team can build and deploy a working web service on Replit is the primary reason he chose the platform.

Zinus uses Shopify to host its e-commerce site, which they extend using an external front-end development platform. However, Mason’s team was recently tasked with switching off of their old front-end development platform and finding a new one. Their old platform caused excessively long response times to service requests from Zinus, which harmed their business. Mason had to redevelop the older web pages on the new platform in just a few weeks to ensure a smoother support process.

“At that moment, no other platform but Replit came to mind, and I had limited time to complete the development. In our situation, Replit was the best choice.”

## Builder Profile: Mason Kim

As a Global DevOps Engineer at Zinus, Mason (Junkuk) Kim’s role is to build software to enable the marketing, business, and customer service teams to deliver their customers the highest quality support experience.

Often, the required turnaround time for these projects is extremely short, and Mason will need to have a solution ready within days or even hours. Even more, the teams he is supporting are based in numerous countries around the globe. The speed at which Mason’s team can build and deploy a working web service on Replit is the primary reason he chose the platform.

Zinus uses Shopify to host its e-commerce site, which they extend using an external front-end development platform. However, Mason’s team was recently tasked with switching off of their old front-end development platform and finding a new one. Their old platform caused excessively long response times to service requests from Zinus, which harmed their business. Mason had to redevelop the older web pages on the new platform in just a few weeks to ensure a smoother support process.

“At that moment, no other platform but Replit came to mind, and I had limited time to complete the development. In our situation, Replit was the best choice.”
- Thu, Jan 11, 2024 Company Spotlight: Qdrant Vector Database With the rise of new generative AI development methods like retrieval-augmented generation (RAG), it can be difficult to demonstrate technical setup to developers and highlight the potential front-end products that can be created by these developer tools.

To speed up developer onboarding, Qdrant has developed several Replit templates. They simplify the initial steps for new developers, such as setting up the development environment and installing packages, making the onboarding process smoother and faster.

What is Qdrant?

Qdrant is a high-performance vector database used at companies like AlphaSense, Disney, Flipkart, HRS, HP, Bayer, Dailymotion, Deloitte, Microsoft, Mozilla, and others.

Qdrant exposes both HTTP and gRPC APIs so that you can integrate it with any programming language. They also have official Python, JS/TS, Rust, and Go SDKs, and various integrations with the most popular LLM frameworks, such as LangChain, LlamaIndex, and Deepset Haystack. Qdrant also has a  custom extension of the HNSW algorithm, enabling both rapid and precise Approximate Nearest Neighbor Search, which is essential for real-time applications.

## Company Spotlight: Qdrant Vector Database

With the rise of new generative AI development methods like retrieval-augmented generation (RAG), it can be difficult to demonstrate technical setup to developers and highlight the potential front-end products that can be created by these developer tools.

To speed up developer onboarding, Qdrant has developed several Replit templates. They simplify the initial steps for new developers, such as setting up the development environment and installing packages, making the onboarding process smoother and faster.

What is Qdrant?

Qdrant is a high-performance vector database used at companies like AlphaSense, Disney, Flipkart, HRS, HP, Bayer, Dailymotion, Deloitte, Microsoft, Mozilla, and others.

Qdrant exposes both HTTP and gRPC APIs so that you can integrate it with any programming language. They also have official Python, JS/TS, Rust, and Go SDKs, and various integrations with the most popular LLM frameworks, such as LangChain, LlamaIndex, and Deepset Haystack. Qdrant also has a  custom extension of the HNSW algorithm, enabling both rapid and precise Approximate Nearest Neighbor Search, which is essential for real-time applications.

--------------------