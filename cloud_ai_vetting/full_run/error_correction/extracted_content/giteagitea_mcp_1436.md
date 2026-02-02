# gitea/gitea-mcp
**URL:** https://gitea.com/gitea/gitea-mcp
**Page Title:** gitea/gitea-mcp: Interactive with Gitea instances with MCP - gitea-mcp - Gitea: Git with a cup of tea
--------------------


## Gitea MCP Server

繁體中文 | 简体中文
Gitea MCP Server is an integration plugin designed to connect Gitea with Model Context Protocol (MCP) systems. This allows for seamless command execution and repository management through an MCP-compatible chat interface.

## Table of Contents

- Gitea MCP Server Table of Contents What is Gitea? What is MCP? 🚧 Installation Usage with VS Code 📥 Download the official binary release 🔧 Build from Source 📁 Add to PATH 🚀 Usage ✅ Available Tools 🐛 Debugging 🛠 Troubleshooting
- Table of Contents
- What is Gitea?
- What is MCP?
- 🚧 Installation Usage with VS Code 📥 Download the official binary release 🔧 Build from Source 📁 Add to PATH
- Usage with VS Code
- 📥 Download the official binary release
- 🔧 Build from Source
- 📁 Add to PATH
- 🚀 Usage
- ✅ Available Tools
- 🐛 Debugging
- 🛠 Troubleshooting

## What is Gitea?

Gitea is a community-managed lightweight code hosting solution written in Go. It is published under the MIT license. Gitea provides Git hosting including a repository viewer, issue tracking, pull requests, and more.

## What is MCP?

Model Context Protocol (MCP) is a protocol that allows for the integration of various tools and systems through a chat interface. It enables seamless command execution and management of repositories, users, and other resources.

## 🚧 Installation

### Usage with VS Code

For quick installation, use one of the one-click install buttons at the top of this README.
For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing Ctrl + Shift + P and typing Preferences: Open User Settings (JSON) .
Optionally, you can add it to a file called .vscode/mcp.json in your workspace. This will allow you to share the configuration with others.
Note that the mcp key is not needed in the .vscode/mcp.json file.

### 📥 Download the official binary release

You can download the official release from official Gitea MCP binary releases .

### 🔧 Build from Source

You can download the source code by cloning the repository using Git:
Before building, make sure you have the following installed:
- make
- Golang (Go 1.24 or later recommended)
Then run:

### 📁 Add to PATH

After installing, copy the binary gitea-mcp to a directory included in your system's PATH. For example:

## 🚀 Usage

This example is for Cursor, you can also use plugins in VSCode.
To configure the MCP server for Gitea, add the following to your MCP configuration file:
- stdio mode
- http mode
Default log path : $HOME/.gitea-mcp/gitea-mcp.log
Note
You can provide your Gitea host and access token either as command-line arguments or environment variables.
Command-line arguments have the highest priority
Once everything is set up, try typing the following in your MCP-compatible chatbox:

## ✅ Available Tools

The Gitea MCP Server supports the following tools:

## 🐛 Debugging

To enable debug mode, add the -d flag when running the Gitea MCP Server with http mode:

## 🛠 Troubleshooting

If you encounter any issues, here are some common troubleshooting steps:
- Check your PATH : Ensure that the gitea-mcp binary is in a directory included in your system's PATH.
- Verify dependencies : Make sure you have all the required dependencies installed, such as make and Golang .
- Review configuration : Double-check your MCP configuration file for any errors or missing information.
- Consult logs : Check the logs for any error messages or warnings that can provide more information about the issue.
Enjoy exploring and managing your Gitea repositories via chat!

--------------------