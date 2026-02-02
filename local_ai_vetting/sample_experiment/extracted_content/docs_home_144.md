# Docs Home →
**URL:** https://cnm13ryan.github.io/inspect_agents
**Page Title:** inspect_agents
--------------------


## inspect_agents

Inspect‑AI–native, CLI‑first agents with typed state, tools, and rich traces. Ship agents in minutes, not days.

## Quickstart (Offline, 60 seconds)

Works with zero API keys and no local model server. New here? Follow these three steps, then see the docs Home.
Start Here
- uv sync
- uv run python env_templates/configure.py
- python scripts/quickstart_toy.py → prints Completion: DONE
Next: Examples — Start Here →
Docs Home →
[LINK: Docs Home →](https://cnm13ryan.github.io/inspect_agents)

## Why Inspect Agents?

Setting up practical LLM agents is slow: you fight glue code, logging, state, and tool orchestration. Inspect Agents removes the overhead with an Inspect-AI-native, CLI-first workflow: one command to run; typed state (todos/files); built-in tools; transcripts and traces by default. Ship in minutes, not days.

## Key Features

- ✅ CLI-first : One command to run an agent or eval with Inspect
- ✅ Inspect-native tools : Todos + virtual filesystem (store or sandbox)
- ✅ Optional standard tools : Think, web_search, bash/python, web_browser, text_editor (policy: bash_session is internal‑only; used by the FS sandbox and not exposed)
- ✅ Typed state : Simple, explicit models backed by Inspect Store
- ✅ Sub-agents : Choose “handoff” (iterative control-flow) or “tool” (single-shot)
- ✅ Traces & transcripts : Rich logs and JSONL artifacts out of the box
- ✅ Safe by default : Approvals, quarantine filters, and sandbox file operations
- ✅ Works offline : Guaranteed “toy” example to validate setup in seconds

## Table of Contents

- Installation
- Usage (CLI and Python)
- Logs & Inspect View
- Examples
- Documentation
- Project Status
- Contributing
- Support

## Installation

### Prerequisites

- Python : 3.11 or later (tested on 3.12)
- OS : macOS or Linux

### Using uv (Recommended)

### Using pip/venv

### Configure Environment Variables

Use the interactive configurator to generate .env files with sensible defaults:
This writes a .env at the repo root and examples/inspect/.env . You can also point runners to the file with --env-file or by exporting INSPECT_ENV_FILE=path/to/.env .

## Usage

### Scaffold a new agent

Generate a minimal agent module (and optional smoke test) in seconds.
Notes
- Safe by default: refuses to overwrite existing files unless --force (or interactive confirmation in a TTY).
- The template uses build_iterative_agent(code_only=True) so it runs without exec/search/browser tools.
- Files are created under src/<package>/ and tests/<package>/ ; missing __init__.py files are added automatically.

### CLI (Inspect)

Basic evaluation with built-in tools:
Provider quick switch (pick one):
With optional tools:
Policy note: Enabling INSPECT_ENABLE_EXEC=1 exposes only single‑shot bash() and python() tools. The stateful bash_session tool is never surfaced by this repo’s standard_tools() ; it is reserved for internal filesystem‑sandbox operations (e.g., sed , ls , wc -c ).
For prompts with special characters, use single quotes:

## Viewing Logs (Inspect View)

Start the Inspect log viewer to explore evaluation logs in your browser:
See docs: docs/cli/inspect_view.md
[LINK: docs/cli/inspect_view.md](/inspect_agents/docs/cli/inspect_view.html)

### Provider Examples

## Advanced Usage

### Sub-agents Configuration

Define sub-agents in YAML and load programmatically. You can also set root-level runtime limits:

## Architecture

Fallback: docs/diagrams/architecture_overview.png

## Documentation

- Getting Started : docs/getting-started/inspect_agents_quickstart.md
- Tools Reference : docs/tools/README.md
- Sub-agent Patterns : docs/guides/subagents.md
- Sandboxing Profiles (AISI-aligned) : docs/guides/sandbox_profiles.md
- Examples : examples/inspect/
- Open Questions : docs/design/open-questions.md
- Testing Guides (repo) : tests/README.md

### Docs (MkDocs)

Preview the documentation site locally with MkDocs.
Using uv (recommended):
Using pip/venv:
Then open http://127.0.0.1:8000. Sources live under docs/ and the site is configured via mkdocs.yml .

## Project Status

- Version : 0.0.4 (repo) / see PyPI badge for latest
- Status : Beta
- Python : 3.11+ (tested on 3.12)
- Roadmap : Milestones Projects
[LINK: Milestones](https://github.com/cnm13ryan/inspect_agents/milestones)
[LINK: Projects](https://github.com/cnm13ryan/inspect_agents/projects)

### Coming Soon

- CI workflows (tests, lint, coverage) and release automation
- Expanded examples for web_browser and sandboxed exec
- Additional sub-agent templates (researcher, coder, editor)

## Contributing

See CONTRIBUTING.md for guidelines.

### Quick Setup for Contributors

## Support

- Questions : GitHub Discussions
[LINK: GitHub Discussions](https://github.com/cnm13ryan/inspect_agents/discussions)
- Bugs & Features : Open an Issue with repro steps
[LINK: Issue](https://github.com/cnm13ryan/inspect_agents/issues)

## License & Acknowledgments

- Licensed under MIT
- Thanks to the Inspect-AI project and ecosystem
- Inspired by CLI-first DX from projects like Bun and Supabase
[LINK: Improve this page](https://github.com/cnm13ryan/inspect_agents/edit/inspect-ai-rewrite/README.md)

--------------------