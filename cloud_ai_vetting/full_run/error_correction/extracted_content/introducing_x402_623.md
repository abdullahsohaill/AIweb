# Introducing x402
**URL:** https://www.coinbase.com/developer-platform/discover/launches/x402
**Page Title:** Introducing x402: a new standard for internet-native payments | Coinbase
--------------------

- Developer Platform
[LINK: Developer Platform](/developer-platform)
- Discover
[LINK: Discover](/developer-platform/discover)
- Launches
[LINK: Launches](/developer-platform/discover/launches)

## Introducing x402: a new standard for internet-native payments

May 6, 2025
By: Erik Reppel, Nemil Dalal, Dan Kim
TL;DR: Coinbase is launching x402, a payment protocol that enables instant stablecoin payments directly over HTTP. It allows APIs, apps, and AI agents to transact seamlessly, unlocking a faster, automated internet economy.
The internet economy has always struggled with payments.
Traditional payment rails—credit cards, bank transfers, subscriptions—were built for a pre-internet world. They’re slow, expensive, geographically limited, and riddled with manual steps. As digital interactions have scaled, payments have lagged behind: fragmented, sluggish, and hard to program.
There is a need for a more modern approach—one that supports autonomous AI agents, the rise of stablecoins and generally enables instant, frictionless payments native to the internet itself. Recently, Citi called this era the “ChatGPT moment” for payments, and a16z labeled it the “WhatsApp moment,” for stablecoins, reflecting a growing consensus: the world is ready for payment rails as seamless and global as the web itself.
At Coinbase, we're addressing exactly this challenge by introducing x402 : an open standard that leverages the original HTTP "402 Payment Required" status code to embed stablecoin payments directly into web interactions. This protocol draws inspiration from Balaji and team's work on crypto micropayments with http://21.co many years ago. At the time, you could only achieve micropayments with Bitcoin payment channels, which required expensive setup/teardown. But with modern L2s like Base, onchain fees have dropped to 1 cent, so many of the applications they prototyped are becoming possible.
[LINK: work](https://medium.com/@earndotcom/how-to-use-21-to-create-and-host-a-machine-payable-api-on-heroku-or-aws-31245850386d])
x402 lets developers and AI agents pay for APIs, services, and software directly with stablecoins over HTTP.  With just a few lines of code, x402 offers built-in authentication, automatic settlement, and seamless integration into existing web infrastructure. It makes monetization instant and automatic, allowing businesses and agents to transact value as easily as they exchange data.
Erik Reppel, Head of Engineering at Coinbase Developer Platform and co-author of the x402 whitepaper , captures the vision behind this initiative:
“We built x402 because the internet has always needed a native way to send and receive payments—and stablecoins finally make that possible. Just like HTTPS secured the web, x402 could define the next era of the internet; one where value moves as freely and instantly as information. We’re laying the groundwork for an economy run not just by people, but by software—autonomous, intelligent, and always on.”
x402 is launching alongside leading collaborators including AWS, Anthropic, Circle and NEAR , who share our belief in an open, programmable internet economy.
Gagan Mac, VP Product Management at Circle—the issuer of USDC —sees x402 as a powerful new standard for making stablecoin payments a first-class citizen of the web:
“ USDC is built for fast, borderless, and programmable payments, and the x402 protocol elegantly simplifies real-time monetization by removing friction around registrations, authentication, and complex signatures. Together, they unlock exciting new use cases like micropayments for AI agents and apps."
And Illia Polosukhin, co-founder of NEAR and co-author of "Attention Is All You Need"—the paper introducing the architecture behind GPT—sees x402 as a natural fit for building seamless agent-driven experiences:
“Our vision merges x402’s frictionless payments with NEAR intents, allowing users to confidently buy anything through their AI agent, while agent developers collect revenue through cross-chain settlements that make blockchain complexity invisible.”
Together with these partners, we’re not just introducing a new payment standard—we're building a foundational infrastructure for a digital economy that's fast, programmable, and truly internet-native, powering experiences designed equally for humans and autonomous machines.

## Why x402 Matters

Traditional payment methods aren't just outdated—they actively hinder the internet economy.
Legacy payment systems like credit cards and bank transfers weren’t built for today’s fast, global, and automated internet. They’re slow, expensive, and riddled with geographical and authentication barriers. Even crypto solutions often require complex wallets or blockchain-specific tools, adding friction instead of removing it.
x402 solves this by resurrecting the HTTP 402 "Payment Required" status code, a dormant feature of the web designed for seamless payment requests within standard HTTP interactions. Now, clients—whether humans, scripts, or AI agents—can respond to payment prompts instantly using widely-used stablecoins (like USDC ), making transactions as effortless as loading a webpage.
Specifically, x402 enables:
- Servers to instantly issue standardized 402 Payment Required responses for premium digital resources.
Servers to instantly issue standardized 402 Payment Required responses for premium digital resources.
- Embedded, automatic payment instructions directly within standard HTTP responses.
Embedded, automatic payment instructions directly within standard HTTP responses.
- Seamless integration into existing HTTP infrastructure, eliminating the need for special wallet interfaces, layers, or separate authentication mechanisms.
Seamless integration into existing HTTP infrastructure, eliminating the need for special wallet interfaces, layers, or separate authentication mechanisms.
The practical impact is clear: payments become instant, seamless, and embedded directly into the internet—unlocking new business models, frictionless global transactions, and fully autonomous software interactions.

## How x402 Works

x402 follows a straightforward flow:
- Client (AI agent or app) requests access to an x402-enabled HTTP server with a resource that it needs (e.g. GET /api).
Client (AI agent or app) requests access to an x402-enabled HTTP server with a resource that it needs (e.g. GET /api).
- Server replies with a 402 Payment Required status, including payment details (e.g., price, acceptable tokens).
Server replies with a 402 Payment Required status, including payment details (e.g., price, acceptable tokens).
- Client sends a signed payment payload using a supported token (like USDC ) through a standard HTTP header.
Client sends a signed payment payload using a supported token (like USDC ) through a standard HTTP header.
- Client retries the request, now including the X-PAYMENT header with the encoded payment payload.
Client retries the request, now including the X-PAYMENT header with the encoded payment payload.
- Payment facilitator (like the Coinbase x402 Facilitator service) verifies and settles the payment onchain, and fulfills the request.
Payment facilitator (like the Coinbase x402 Facilitator service) verifies and settles the payment onchain, and fulfills the request.
[LINK: Coinbase x402 Facilitator](https://docs.cdp.coinbase.com/x402/docs/welcome)
- Server returns the requested data to the client, including an X-PAYMENT-RESPONSE header confirming success of the transaction.
Server returns the requested data to the client, including an X-PAYMENT-RESPONSE header confirming success of the transaction.
Because it extends native HTTP behavior, x402 can work with nearly any client - browsers, SDKs, AI agents, mobile apps - without additional requests, changing a website’s client/server flow or extensive UI integrations.

## What Developers Can Build

With managed solutions like the Coinbase x402 Facilitator service, developers can effortlessly integrate stablecoin payments directly into their services—using just a few lines of code. This eliminates the complexity, overhead, and friction traditionally associated with payment integrations, allowing creators and businesses to unlock entirely new revenue streams and user experiences.
[LINK: Coinbase x402 Facilitator](https://docs.cdp.coinbase.com/x402/docs/welcome)
For example:
- Paid APIs: Monetize each API call instantly with frictionless micropayments, removing the barriers and complexity of subscription-based models.
Paid APIs: Monetize each API call instantly with frictionless micropayments, removing the barriers and complexity of subscription-based models.
- Software Unlocks: Provide seamless, on-demand access to premium features and content, without subscriptions or complicated paywalls.
Software Unlocks: Provide seamless, on-demand access to premium features and content, without subscriptions or complicated paywalls.
- Metered Services: Dynamically charge users based on actual resource usage, enabling scalable, pay-as-you-go experiences without the hassle of pre-payment or billing cycles.
Metered Services: Dynamically charge users based on actual resource usage, enabling scalable, pay-as-you-go experiences without the hassle of pre-payment or billing cycles.
Imagine creators getting automatically compensated per minute viewed, news sites instantly monetizing individual articles, or AI agents autonomously buying cloud resources in real-time. By embedding payments directly within HTTP, x402 makes previously impractical microtransactions effortless—transforming everyday digital interactions for humans, automated scripts, and autonomous agents alike, bridging today's web seamlessly to tomorrow's decentralized digital economy.

## What AI Agents Can Unlock

AI agents today can think, reason, and act—but their ability to transact remains dependent on manual, human-driven methods like credit cards, prepaid API keys, or subscription models. x402 fundamentally changes this, granting AI systems the power to autonomously transact in real-time, unlocking a new wave of intelligent, independent software agents.
With x402, agents gain instant economic autonomy, enabling scenarios such as:
- Autonomous Cloud Compute: AI agents can provision compute resources and pay per inference in real-time, eliminating human-managed credits or manual provisioning processes.
Autonomous Cloud Compute: AI agents can provision compute resources and pay per inference in real-time, eliminating human-managed credits or manual provisioning processes.
- Market Intelligence: AI systems autonomously access specialized data sources, seamlessly paying per request to obtain crucial market or product insights without manual intervention.
Market Intelligence: AI systems autonomously access specialized data sources, seamlessly paying per request to obtain crucial market or product insights without manual intervention.
- Prediction Markets: Automated betting agents can independently purchase real-time sports statistics and market data, placing informed bets without human involvement.
Prediction Markets: Automated betting agents can independently purchase real-time sports statistics and market data, placing informed bets without human involvement.
- Consumer and Supply Chain Automation: AI inventory managers dynamically request and pay for real-time price quotes, supply chain data, and logistics, instantly adapting to market changes autonomously.
Consumer and Supply Chain Automation: AI inventory managers dynamically request and pay for real-time price quotes, supply chain data, and logistics, instantly adapting to market changes autonomously.
- AI-driven Creative Tools: Intelligent content creation systems autonomously access premium media libraries, design tools, and specialized software, instantly paying for resources to produce high-quality content independently.
AI-driven Creative Tools: Intelligent content creation systems autonomously access premium media libraries, design tools, and specialized software, instantly paying for resources to produce high-quality content independently.
Instead of static tools that require constant human setup, x402 transforms AI into truly dynamic agents—capable of autonomously discovering, acquiring, and leveraging new capabilities on-demand. When an agent encounters a paywall or premium resource, it simply attaches a signed stablecoin payment, seamlessly resumes the interaction, and continues toward its goal.
This isn’t mere automation—it's economic autonomy for software. It represents the foundation of a new generation of intelligent agents that independently transact, adapt, and evolve.

## Who’s Building With x402

Our early partners illustrate the transformative possibilities when payments become seamlessly embedded in HTTP, unlocking entirely new business models and enabling genuinely autonomous software interactions:

### Autonomous Infrastructure

- Hyperbolic : AI agents autonomously pay per GPU inference, enabling scalable workloads without manual management.
Hyperbolic : AI agents autonomously pay per GPU inference, enabling scalable workloads without manual management.
- OpenMind : Robots autonomously procure compute and data, transforming physical agents into economic actors on-chain.
OpenMind : Robots autonomously procure compute and data, transforming physical agents into economic actors on-chain.
- PLVR : AI agents autonomously buy event tickets, creating frictionless, instant fan engagement.
PLVR : AI agents autonomously buy event tickets, creating frictionless, instant fan engagement.

### Agent Interactions

- Anthropic (MCP Protocol) : AI models dynamically discover, retrieve, and autonomously pay for context and tools, showcasing truly independent agent interactions powered by x402.
Anthropic (MCP Protocol) : AI models dynamically discover, retrieve, and autonomously pay for context and tools, showcasing truly independent agent interactions powered by x402.
- Apexti Toolbelt : Empowers developers and agents to tap—or dynamically spin up—over 1,500 Web3 APIs through x402-enabled MCP servers, monetizing each API call seamlessly within a single prompt.
Apexti Toolbelt : Empowers developers and agents to tap—or dynamically spin up—over 1,500 Web3 APIs through x402-enabled MCP servers, monetizing each API call seamlessly within a single prompt.
- NEAR AI : Simplifies blockchain integration for AI applications, enabling autonomous economic interactions without complexity. “Our vision merges x402’s frictionless payments with NEAR intents, allowing users to confidently buy anything through their AI agent, while agent developers collect revenue through cross-chain settlements that make blockchain complexity invisible.” – Illia Polosukhin, co-founder of NEAR.ai and a key inventor of the transformer architecture underlying GPT.
NEAR AI : Simplifies blockchain integration for AI applications, enabling autonomous economic interactions without complexity.
- “Our vision merges x402’s frictionless payments with NEAR intents, allowing users to confidently buy anything through their AI agent, while agent developers collect revenue through cross-chain settlements that make blockchain complexity invisible.” – Illia Polosukhin, co-founder of NEAR.ai and a key inventor of the transformer architecture underlying GPT.
“Our vision merges x402’s frictionless payments with NEAR intents, allowing users to confidently buy anything through their AI agent, while agent developers collect revenue through cross-chain settlements that make blockchain complexity invisible.” – Illia Polosukhin, co-founder of NEAR.ai and a key inventor of the transformer architecture underlying GPT.

### Social & Messaging

- XMTP : Messaging platforms become economic hubs—agents and users seamlessly pay to join private groups, unlock exclusive content, or monetize their expertise directly within chats.
XMTP : Messaging platforms become economic hubs—agents and users seamlessly pay to join private groups, unlock exclusive content, or monetize their expertise directly within chats.
- Neynar : AI agents seamlessly query Farcaster’s social graph and profiles, powering innovative social applications and creative content generation. “x402 turns Neynar’s Farcaster APIs into a pure on-demand utility—agents can pull exactly the data they need, settle in USDC on the same HTTP 402 round-trip, and skip API keys or pre-paid tiers entirely. It’s a huge unlock for real-time, context-rich social apps.” – Rish Mukherji, founder of Neynar
Neynar : AI agents seamlessly query Farcaster’s social graph and profiles, powering innovative social applications and creative content generation.
- “x402 turns Neynar’s Farcaster APIs into a pure on-demand utility—agents can pull exactly the data they need, settle in USDC on the same HTTP 402 round-trip, and skip API keys or pre-paid tiers entirely. It’s a huge unlock for real-time, context-rich social apps.” – Rish Mukherji, founder of Neynar
“x402 turns Neynar’s Farcaster APIs into a pure on-demand utility—agents can pull exactly the data they need, settle in USDC on the same HTTP 402 round-trip, and skip API keys or pre-paid tiers entirely. It’s a huge unlock for real-time, context-rich social apps.” – Rish Mukherji, founder of Neynar

### Real-time Data

- Chainlink : Built a demo using the x402 protocol that requires USDC payment to enable user interaction with a contract on Base Sepolia to mint a random NFT using Chainlink VRF.
Chainlink : Built a demo using the x402 protocol that requires USDC payment to enable user interaction with a contract on Base Sepolia to mint a random NFT using Chainlink VRF.
- Boosty Labs : Shows how AI agents can autonomously buy real-time insights (via X API and Grok 3 inference) instantly—no API keys or human intervention required.
Boosty Labs : Shows how AI agents can autonomously buy real-time insights (via X API and Grok 3 inference) instantly—no API keys or human intervention required.
- Zyte.com : Agents dynamically purchase structured web data, such as market insights and product listings, via micropayments.
Zyte.com : Agents dynamically purchase structured web data, such as market insights and product listings, via micropayments.

### Easy Integrations

- BuffetPay : Smart x402 payments with built-in guardrails and multi-wallet control, streamlining secure, programmable payments.
BuffetPay : Smart x402 payments with built-in guardrails and multi-wallet control, streamlining secure, programmable payments.
- Cal.com : Embeds automated scheduling and paid human interactions directly into workflows, accessible by both agents and users alike.
Cal.com : Embeds automated scheduling and paid human interactions directly into workflows, accessible by both agents and users alike.
- Cred Protocol : Provides decentralized credit scoring infrastructure, allowing AI agents to autonomously assess on-chain creditworthiness in real-time.
Cred Protocol : Provides decentralized credit scoring infrastructure, allowing AI agents to autonomously assess on-chain creditworthiness in real-time.
- Fewsats : Built a lightweight proxy enabling rapid adoption and testing of x402 without modifying existing application infrastructure.
Fewsats : Built a lightweight proxy enabling rapid adoption and testing of x402 without modifying existing application infrastructure.
These pioneering examples illustrate how x402 transforms the web into a programmable economic platform, empowering a new generation of intelligent agents and dynamic services to transact, adapt, and evolve independently.
x402 is open and available now for developers, teams, and innovators to explore and integrate into their applications. Check out x402.org for complete documentation, working demos, the official whitepaper, and GitHub resources.
We're excited to see what you'll build—and to shape the future of payments and programmable internet commerce together.

## Download the App

Information provided on this Site is for general educational purposes only and is not intended to constitute investment or other advice on financial products. Such information is not, and should not be read as, an offer or recommendation to buy or sell or a solicitation of an offer or recommendation to buy or sell any particular digital asset or to use any particular investment strategy. Coinbase and its affiliates (collectively “Coinbase”) makes no representations as to the accuracy, completeness, timeliness, suitability, or validity of any information on this Site and will not be liable for any errors, omissions, or delays in this information or any losses, injuries, or damages arising from its display or use. Unless otherwise noted, all images are the property of Coinbase. Coinbase  is not registered or licensed with the U.S. Securities and Exchange Commission or the U.S. Commodity Futures Trading Commission. Links provided to third-party sites are for informational purposes. Such sites are not under the control of Coinbase, and Coinbase is not responsible for the accuracy of the content on such third-party sites.

## Cookie consent manager

### Manage cookie preferences

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. These also include cookies we may rely on for fraud prevention. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work.
These cookies enable us to remember choices you have made in the past in order to provide enhanced functionality and personalisation (e.g. what language you prefer). If you do not allow these cookies then some or all of these services may not function properly.
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant ads on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

### Cookie List

- checkbox label label

--------------------