# Plugin Reference
**URL:** https://docs.claude.com/en/docs/claude-code/plugins-reference
**Page Title:** Plugins reference - Claude Code Docs
--------------------

[LINK: Claude Code Docs home page](/docs)
[LINK: Getting started](/docs/en/overview)
[LINK: Build with Claude Code](/docs/en/sub-agents)
[LINK: Deployment](/docs/en/third-party-integrations)
[LINK: Administration](/docs/en/setup)
[LINK: Configuration](/docs/en/settings)
[LINK: Reference](/docs/en/cli-reference)
[LINK: Resources](/docs/en/legal-and-compliance)
- CLI reference
[LINK: CLI reference](/docs/en/cli-reference)
- Interactive mode
[LINK: Interactive mode](/docs/en/interactive-mode)
- Checkpointing
[LINK: Checkpointing](/docs/en/checkpointing)
- Hooks reference
[LINK: Hooks reference](/docs/en/hooks)
- Plugins reference
[LINK: Plugins reference](/docs/en/plugins-reference)
- Plugin components reference
- Skills
- Agents
- Hooks
- MCP servers
- LSP servers
- Plugin installation scopes
- Plugin manifest schema
- Complete schema
- Required fields
- Metadata fields
- Component path fields
- Path behavior rules
- Environment variables
- Plugin caching and file resolution
- How plugin caching works
- Path traversal limitations
- Working with external dependencies
- Plugin directory structure
- Standard plugin layout
- File locations reference
- CLI commands reference
- plugin install
- plugin uninstall
- plugin enable
- plugin disable
- plugin update
- Debugging and development tools
- Debugging commands
- Common issues
- Example error messages
- Hook troubleshooting
- MCP server troubleshooting
- Directory structure mistakes
- Distribution and versioning reference
- Version management
- See also
[LINK: Discover and install plugins](/docs/en/discover-plugins)
[LINK: Plugins](/docs/en/plugins)
[LINK: Plugin marketplaces](/docs/en/plugin-marketplaces)

## ​ Plugin components reference

### ​ Skills

- Skills and commands are automatically discovered when the plugin is installed
- Claude can invoke them automatically based on task context
- Skills can include supporting files alongside SKILL.md
[LINK: Skills](/docs/en/skills)

### ​ Agents

- Agents appear in the /agents interface
- Claude can invoke agents automatically based on task context
- Agents can be invoked manually by users
- Plugin agents work alongside built-in Claude agents

### ​ Hooks

- PreToolUse : Before Claude uses any tool
- PostToolUse : After Claude successfully uses any tool
- PostToolUseFailure : After Claude tool execution fails
- PermissionRequest : When a permission dialog is shown
- UserPromptSubmit : When user submits a prompt
- Notification : When Claude Code sends notifications
- Stop : When Claude attempts to stop
- SubagentStart : When a subagent is started
- SubagentStop : When a subagent attempts to stop
- SessionStart : At the beginning of sessions
- SessionEnd : At the end of sessions
- PreCompact : Before conversation history is compacted
- command : Execute shell commands or scripts
- prompt : Evaluate a prompt with an LLM (uses $ARGUMENTS placeholder for context)
- agent : Run an agentic verifier with tools for complex verification tasks

### ​ MCP servers

- Plugin MCP servers start automatically when the plugin is enabled
- Servers appear as standard MCP tools in Claude’s toolkit
- Server capabilities integrate seamlessly with Claude’s existing tools
- Plugin servers can be configured independently of user MCP servers

### ​ LSP servers

[LINK: Language Server Protocol](https://microsoft.github.io/language-server-protocol/)
- Instant diagnostics : Claude sees errors and warnings immediately after each edit
- Code navigation : go to definition, find references, and hover information
- Language awareness : type information and documentation for code symbols
[LINK: See rust-analyzer installation](https://rust-analyzer.github.io/manual.html#installation)

## ​ Plugin installation scopes

[LINK: Install plugins](/docs/en/discover-plugins#install-plugins)
[LINK: Configuration scopes](/docs/en/settings#configuration-scopes)

## ​ Plugin manifest schema

### ​ Complete schema

### ​ Required fields

### ​ Metadata fields

### ​ Component path fields

[LINK: Language Server Protocol](https://microsoft.github.io/language-server-protocol/)

### ​ Path behavior rules

- If commands/ exists, it’s loaded in addition to custom command paths
- All paths must be relative to plugin root and start with ./
- Commands from custom paths use the same naming and namespacing rules
- Multiple paths can be specified as arrays for flexibility

### ​ Environment variables

## ​ Plugin caching and file resolution

### ​ How plugin caching works

- For marketplace plugins with relative paths : The path specified in the source field is copied recursively. For example, if your marketplace entry specifies "source": "./plugins/my-plugin" , the entire ./plugins directory is copied.
- For plugins with .claude-plugin/plugin.json : The implicit root directory (the directory containing .claude-plugin/plugin.json ) is copied recursively.

### ​ Path traversal limitations

### ​ Working with external dependencies

## ​ Plugin directory structure

### ​ Standard plugin layout

### ​ File locations reference

## ​ CLI commands reference

### ​ plugin install

- <plugin> : Plugin name or plugin-name@marketplace-name for a specific marketplace

### ​ plugin uninstall

- <plugin> : Plugin name or plugin-name@marketplace-name

### ​ plugin enable

- <plugin> : Plugin name or plugin-name@marketplace-name

### ​ plugin disable

- <plugin> : Plugin name or plugin-name@marketplace-name

### ​ plugin update

- <plugin> : Plugin name or plugin-name@marketplace-name

## ​ Debugging and development tools

### ​ Debugging commands

- Which plugins are being loaded
- Any errors in plugin manifests
- Command, agent, and hook registration
- MCP server initialization

### ​ Common issues

### ​ Example error messages

- Invalid JSON syntax: Unexpected token } in JSON at position 142 : check for missing commas, extra commas, or unquoted strings
- Plugin has an invalid manifest file at .claude-plugin/plugin.json. Validation errors: name: Required : a required field is missing
- Plugin has a corrupt manifest file at .claude-plugin/plugin.json. JSON parse error: ... : JSON syntax error
- Warning: No commands found in plugin my-plugin custom directory: ./cmds. Expected .md files or SKILL.md in subdirectories. : command path exists but contains no valid command files
- Plugin directory not found at path: ./plugins/my-plugin. Check that the marketplace entry has the correct path. : the source path in marketplace.json points to a non-existent directory
- Plugin my-plugin has conflicting manifests: both plugin.json and marketplace entry specify components. : remove duplicate component definitions or set strict: true in marketplace entry

### ​ Hook troubleshooting

- Check the script is executable: chmod +x ./scripts/your-script.sh
- Verify the shebang line: First line should be #!/bin/bash or #!/usr/bin/env bash
- Check the path uses ${CLAUDE_PLUGIN_ROOT} : "command": "${CLAUDE_PLUGIN_ROOT}/scripts/your-script.sh"
- Test the script manually: ./scripts/your-script.sh
- Verify the event name is correct (case-sensitive): PostToolUse , not postToolUse
- Check the matcher pattern matches your tools: "matcher": "Write|Edit" for file operations
- Confirm the hook type is valid: command , prompt , or agent

### ​ MCP server troubleshooting

- Check the command exists and is executable
- Verify all paths use ${CLAUDE_PLUGIN_ROOT} variable
- Check the MCP server logs: claude --debug shows initialization errors
- Test the server manually outside of Claude Code
- Ensure the server is properly configured in .mcp.json or plugin.json
- Verify the server implements the MCP protocol correctly
- Check for connection timeouts in debug output

### ​ Directory structure mistakes

- Run claude --debug and look for “loading plugin” messages
- Check that each component directory is listed in the debug output
- Verify file permissions allow reading the plugin files

## ​ Distribution and versioning reference

### ​ Version management

- MAJOR : Breaking changes (incompatible API changes)
- MINOR : New features (backward-compatible additions)
- PATCH : Bug fixes (backward-compatible fixes)
- Start at 1.0.0 for your first stable release
- Update the version in plugin.json before distributing changes
- Document changes in a CHANGELOG.md file
- Use pre-release versions like 2.0.0-beta.1 for testing

## ​ See also

- Plugins - Tutorials and practical usage
[LINK: Plugins](/docs/en/plugins)
- Plugin marketplaces - Creating and managing marketplaces
[LINK: Plugin marketplaces](/docs/en/plugin-marketplaces)
- Skills - Skill development details
[LINK: Skills](/docs/en/skills)
- Subagents - Agent configuration and capabilities
[LINK: Subagents](/docs/en/sub-agents)
- Hooks - Event handling and automation
[LINK: Hooks](/docs/en/hooks)
- MCP - External tool integration
[LINK: MCP](/docs/en/mcp)
- Settings - Configuration options for plugins
[LINK: Settings](/docs/en/settings)
Was this page helpful?
[LINK: Hooks reference](/docs/en/hooks)

--------------------