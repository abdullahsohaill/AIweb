# Open VSX Registry
**URL:** https://open-vsx.org/extension/Pipelex/pipelex
**Page Title:** Pipelex – Open VSX Registry
--------------------

Open VSX is growing! To support reliable access as usage increases, we've clarified our existing usage limits for community and organization users. Learn more here .
[LINK: here](https://github.com/EclipseFdn/open-vsx.org/wiki/rate-limiting)
[LINK: lchoquel](https://github.com/lchoquel)
[LINK: SEE LICENSE IN LICENSE.md](https://open-vsx.org/api/Pipelex/pipelex/0.2.1/file/LICENSE.md)
Pipelex Language (PLX) and TOML support

## Pipelex Extension

Rich language support for Pipelex Language (PLX) and TOML files
This extension provides comprehensive VS Code support for the Pipelex Language (PLX) , which is based on TOML syntax, along with full TOML language support. Built as a fork of the excellent Taplo language server, it tracks upstream closely while adding PLX-specific features like advanced syntax highlighting, semantic tokens, and intelligent language features for .plx files.
[LINK: Taplo](https://github.com/tamasfe/taplo)
About Pipelex:
Pipelex is an open-source language for building deterministic AI workflows. It enables agents and developers to transform natural language requirements into production-ready pipelines that process information reliably at scale. Unlike traditional workflow tools, Pipelex uses a declarative syntax that captures business logic directly, making pipelines readable by domain experts while remaining executable by any runtime. Write once, run anywhere, share with everyone.
[LINK: Pipelex](https://github.com/Pipelex/pipelex)

## 🚀 PLX Features

### 📝 Pipelex Language Support

- Rich syntax highlighting for PLX-specific constructs
- Concept definitions : [concept.Name] sections with specialized highlighting
- Pipe definitions : [pipe.name] sections for workflow steps
- Data injection : @variable syntax with smart highlighting
- Template variables : $variable support
- Jinja2 templates : {{ }} and {% %} blocks with keyword highlighting
- HTML templates : Basic HTML tag support within strings
- Semantic tokens for context-aware highlighting

### 🎨 PLX Syntax Highlighting

- 🔵 Concept sections - [concept.Name] in teal ( #4ECDC4 )
- 🔴 Pipe sections - [pipe.name] in red ( #FF6666 )
- 🟢 Data variables - @variable , $variable in green ( #98FB98 )
- 🟣 Template syntax - Jinja delimiters in pink ( #FF79C6 )
- 🟡 HTML elements - Tags and attributes in orange/yellow
- 🔷 Concept types - ConceptType references highlighted
- 🔶 Pipe types - PipeLLM , PipeSequence etc. highlighted

### Example PLX File

## 📦 Installation

- From extensions marketplace : Search for “Pipelex” in the Extensions view
- From Command Line : code --install-extension Pipelex.pipelex or cursor --install-extension Pipelex.pipelex
- Manual Installation : Download .vsix from releases
[LINK: releases](https://github.com/Pipelex/vscode-pipelex/releases)
“Pipelex” is a trademark of Evotis S.A.S.

## Original Taplo VS Code README (kept in sync)

Everything below is the original Taplo README, kept in sync with upstream for your reference.
A TOML language support extension backed by Taplo .
It is currently a preview extension , it might contain bugs, or might even crash. If you encounter any issues, please report them on github .
[LINK: on github](https://github.com/tamasfe/taplo/issues)
- Features TOML version 1.0.0 support Syntax highlighting Additional Syntax Colors Semantic highlighting Validation Folding Symbol tree and navigation Refactors Renaming Formatting Completion and Validation with JSON Schema Commands
- TOML version 1.0.0 support
- Syntax highlighting Additional Syntax Colors
- Additional Syntax Colors
- Semantic highlighting
- Validation
- Folding
- Symbol tree and navigation
- Refactors Renaming
- Renaming
- Formatting
- Completion and Validation with JSON Schema
- Commands
- Configuration File
- Special Thanks

## Features

## TOML version 1.0.0 support

This extension will try to support all the TOML versions in the future.

## Syntax highlighting

Syntax highlighting for TOML documents with TextMate grammar.

### Additional Syntax Colors

The extension defines custom scopes for array headers and arrays of tables.
In order to differentiate them from regular keys, you can set your own colors for them. Unfortunately this has to be done manually .
[LINK: has to be done manually](https://github.com/Microsoft/vscode/issues/32813)
You might also want to set a color for dates and times, as they don’t have have one in most themes.

## Semantic highlighting

Semantic key highlighting for inline tables and arrays can be enabled in the settings.
You need to set extended colors in order for this to have any practical effect.

## Validation

## Folding

Arrays, multi-line strings and top level tables and comments can be folded.

## Symbol tree and navigation

Works even for tables not in order.

## Refactors

### Renaming

## Formatting

The formatter is rather conservative by default, additional features can be enabled in the settings. If you’re missing a configuration option, feel free to open an issue about it!

## Completion and Validation with JSON Schema

There is support for completion, hover text, links and validation.
Schemas can be associated with document URIs with the evenBetterToml.schema.associations configuration.
You can provide your own schemas or use existing schemas from the JSON Schema Store . More details here .

## Commands

The extension provides commands for easy JSON<->TOML conversions.

## Configuration File

Taplo CLI’s configuration file is supported and automatically found in workspace roots, or can be manually set in the VS Code configuration.

## Special Thanks

- To @GalAster and @be5invis for letting me use their TextMate grammar.
[LINK: @GalAster](https://github.com/GalAster)
[LINK: @be5invis](https://github.com/be5invis)
- To every contributor.
- And to everyone else using this extension.
[LINK: Homepage](https://github.com/Pipelex/vscode-pipelex#readme)
[LINK: Repository](https://github.com/Pipelex/vscode-pipelex.git)
[LINK: Bugs](https://github.com/Pipelex/vscode-pipelex/issues)
[LINK: Download](https://open-vsx.org/api/Pipelex/pipelex/0.2.1/file/Pipelex.pipelex-0.2.1.vsix)
By clicking download, you accept this website's Terms of Use .
[LINK: Claim Ownership](https://github.com/EclipseFdn/open-vsx.org/issues/new?labels=namespace&title=Claiming%20namespace%20%60Pipelex%60&body=Briefly%20explain%20what%20makes%20you%20a%20legitimate%20owner%20of%20the%20namespace%20mentioned%20in%20the%20issue%20title.%0APlease%20ensure%20that%20you%20have%20logged%20in%20to%20https%3A%2F%2Fopen-vsx.org%20at%20least%20once%2C%20otherwise%20we%20cannot%20process%20your%20request.)

--------------------