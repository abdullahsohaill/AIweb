# Continue x MCP
**URL:** https://blog.continue.dev/model-context-protocol
**Page Title:** Model Context Protocol x Continue
--------------------

Launch background agents , iterate in terminal , and deploy workflows in CI/CD with Continue
[LINK: iterate in terminal](https://docs.continue.dev/cli/quick-start#tui-mode)
[LINK: deploy workflows in CI/CD](https://docs.continue.dev/cli/quick-start#headless-mode)
Last week, Anthropic introduced the Model Context Protocol (MCP), a new open protocol that "enables seamless integration between LLM applications and external data sources and tools". Also last week, Continue added support for MCP! Let’s explore why MCP is well-suited for Continue and how you can use it to improve your AI-assisted coding experience.
MCP breaks down into four primary concepts—Resources, Prompts, Tools, and Sampling. This framework maps smoothly onto Continue's existing features:
- Resources map to Context Providers in Continue
[LINK: Context Providers](https://docs.continue.dev/customize/context-providers?ref=blog.continue.dev)
- Prompts map to Slash Commands in Continue
[LINK: Slash Commands](https://docs.continue.dev/customize/slash-commands?ref=blog.continue.dev)
- Tools map to Tools in Continue
[LINK: Tools](https://docs.continue.dev/customize/tools?ref=blog.continue.dev)
- Sampling is currently unsupported
Open standards and developer-owned tools are crucial for shaping how AI assists development . MCP represents the kind of community-driven initiative that will help us build this future, giving developers the ability to build and share custom AI coding assistants.
Integrating MCP into Continue is just a quick config update. Start by setting up a local MCP server following the simple steps in their quickstart guide . Once set up, add the MCP Context Provider in your config.json as demonstrated in the snippet below:
~/.continue/config.json
In Continue, just type “@”, select “MCP” from the dropdown, and choose the resource for context.
Anthropic has created a collection of reference implementations in their MCP servers repository , which can be directly used with Continue.
[LINK: MCP servers repository](https://github.com/modelcontextprotocol/servers?ref=blog.continue.dev)
Here are some of the best examples we've seen:
- Google Drive : Access and search files within Google Drive
[LINK: Google Drive](https://github.com/modelcontextprotocol/servers/blob/main/src/gdrive?ref=blog.continue.dev)
- Sentry : Retrieve and analyze issues from Sentry.io
[LINK: Sentry](https://github.com/modelcontextprotocol/servers/blob/main/src/sentry?ref=blog.continue.dev)
- Puppeteer : Automate browser tasks and perform web scraping
[LINK: Puppeteer](https://github.com/modelcontextprotocol/servers/blob/main/src/puppeteer?ref=blog.continue.dev)
- Slack : Manage channels and messaging
[LINK: Slack](https://github.com/modelcontextprotocol/servers/blob/main/src/slack?ref=blog.continue.dev)
- Brave Search : Conduct web and local searches using Brave's Search API
[LINK: Brave Search](https://github.com/modelcontextprotocol/servers/blob/main/src/brave-search?ref=blog.continue.dev)
We're excited to see the developer community rally around open standards like MCP—it's an important step toward interoperable and powerful AI-assisted development tools. As we build further support for integration with MCP, we'd love to hear your thoughts and ideas. Join our Discord community to share your experience, suggest new features, or connect with other developers who are exploring the future of AI-assisted development.

## Sign up for more like this.


--------------------