# mcpd official docs
**URL:** https://mozilla-ai.github.io/mcpd
**Page Title:** mcpd documentation
--------------------

[LINK: Skip to content](https://mozilla-ai.github.io/mcpd/#mcpd)

## mcpd ¶

Run your agents, not your infrastructure.
mcpd is a toolchain and runtime developed by Mozilla AI that simplifies the configuration, 
execution and integration of Model Context Protocol (MCP) servers with your agentic application.
It is intended to provide the same experience across local, development and production environments.
It removes the friction of cross-language server orchestration, secrets management, version pinning, and lifecycle control.

## Why mcpd ? ¶

Traditional agent frameworks often embed complex subprocess logic, brittle startup scripts, and ad-hoc 'desktop style' config.
mcpd replaces this with:
Zero-Config Tool Setup No cloning repos or installing language-specific dependencies. mcpd add and mcpd daemon handle everything.
Language-Agnostic Tooling Use MCP servers written in Python ( uvx ), JavaScript/TypeScript ( npx ) in your code via a HTTP REST API that supports routing to MCP Servers.
Declarative Tool Management Define version-pinned MCP servers and tools in .mcpd.toml . Reproducible, consistent, and CI-friendly.
Project config separated from runtime variables Exportable args and environment variables per server e.g. ~/.config/mcpd/secrets.dev.toml . 
Never commit dev specific vars to Git again.
Unified Dev Experience One command: mcpd daemon . Starts and manages all servers behind the scenes.
Intuitive SDK Integration The Python mcpd_sdk makes calling tools feel like native function calls; no HTTP, STDIO, or SSE boilerplate.
  Even easier for users of any-agent via .agent_tools() .
[LINK: any-agent](https://github.com/mozilla-ai/any-agent)
Seamless Local-to-Prod Transition The same .mcpd.toml and agent code work in dev, CI, and cloud environments without modification.

## Built for Dev & Infra ¶

[LINK: SDKs for Python](https://github.com/mozilla-ai/mcpd-sdk-python)

## Deploy Anywhere ¶

mcpd is runtime-flexible and infrastructure-agnostic:
- ⚙️ Works in any container or host with uv and npx
- ☁️ Multi-cloud ready (AWS, GCP, Azure, on-prem)
- ♻️ Low resource overhead via in-process server management

## 📦 Install ¶

### Homebrew ¶

Add the Mozilla.ai tap :
[LINK: Mozilla.ai tap](https://github.com/mozilla-ai/homebrew-tap)
Then install mcpd :
Or install directly from the cask in a single command:
Installation methods
Please see our Installation page for additional ways to install and run mcpd .
[LINK: Installation](https://mozilla-ai.github.io/mcpd/installation/)

## 📚 Explore the Docs ¶

Use the sidebar to explore:
- ✅ Requirements
[LINK: Requirements](https://mozilla-ai.github.io/mcpd/requirements/)
- ⚙️ Configuration
[LINK: Configuration](https://mozilla-ai.github.io/mcpd/configuration/)
- 🧭 CLI Reference
[LINK: CLI Reference](https://mozilla-ai.github.io/mcpd/commands/mcpd/)
- 🧵 Execution context and secrets
[LINK: Execution context and secrets](https://mozilla-ai.github.io/mcpd/execution-context/)
- 🛠️ Makefile and tooling
[LINK: Makefile and tooling](https://mozilla-ai.github.io/mcpd/makefile/)
- 📚 Tutorial
[LINK: Tutorial](https://mozilla-ai.github.io/mcpd/tutorial/)

## About Mozilla.ai ¶

This project is built and maintained by Mozilla.ai , a mission-driven organization reimagining AI for the public good.
Have ideas or feedback? Contributions welcome via GitHub .
[LINK: GitHub](https://github.com/mozilla-ai/mcpd)

--------------------