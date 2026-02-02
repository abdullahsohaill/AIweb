# Egnyte MCP
**URL:** https://developers.egnyte.com/docs/Remote_MCP_Server
**Page Title:** API Documentation - Remote MCP Server | Egnyte for Developers
--------------------


## API Documentation - Remote MCP Server

## Egnyte Remote MCP Server LIMITED AVAILABILITY

Securely integrate Claude, ChatGPT, and any OAuth-compatible MCP client with your Egnyte content

## Overview

The Egnyte Remote MCP Server is a fully-managed Model Context Protocol (MCP) server that enables secure integration between your Egnyte content and popular AI tools. This service provides a standardized way for AI assistants to access and interact with your Egnyte data while maintaining enterprise-grade security through OAuth authentication.

## Getting Started

### Prerequisites

- An active Egnyte account on either Gen 4: Essential, Elite, and Ultimate plans OR Gen 3: Platform Enterprise or Enterprise Lite, with the Co-Pilot add-on
- An MCP-compatible AI client that supports OAuth authentication (Claude, ChatGPT, etc.)
- Your Egnyte domain name and credentials for authentication

### Configuration Steps

The Egnyte MCP Server can be connected to any AI client that supports the Model Context Protocol with OAuth authentication. The general setup process is:
- Configure your AI client with the Egnyte MCP Server URL: https://mcp-server.egnyte.com/mcp
- Initiate the connection from your AI client. You will be redirected to the Egnyte authentication page.
- Enter your Egnyte domain and authenticate with your Egnyte credentials
- Grant the necessary permissions for the integration
- Begin interacting with your Egnyte content through your AI assistant
See the client-specific instructions below for detailed setup guides for popular AI platforms.

## Authentication

The Egnyte Remote MCP Server uses OAuth 2.0 for secure authentication. When connecting your AI client:
- The client will redirect you to Egnyte's OAuth authorization page
- Enter your Egnyte domain and authenticate with your Egnyte credentials
- Review and approve the requested permissions
- The client will receive an access token for API calls
Access tokens are managed automatically by the MCP server and refreshed as needed to maintain your session.

## Connecting Egnyte MCP to Popular AI Clients

### ChatGPT

Egnyte is available as an app in ChatGPT, enabling secure access to your Egnyte files for natural language searches, summaries, and insights while respecting your organization's permissions.
Key Benefits:
- Search and retrieve permitted files using natural language queries
- Generate summaries, analyses, or drafts grounded in your Egnyte content
- Maintain security as ChatGPT enforces Egnyte permissions and compliance
Setup Steps:
- Navigate to ChatGPT Settings and select Apps
- Find and enable the Egnyte app for your workspace
- Authenticate with your Egnyte credentials when prompted
- Start interacting with your Egnyte content directly in ChatGPT prompts
For more information, see the ChatGPT Apps documentation .

### Claude

Egnyte is available as a connector in Claude, allowing you to seamlessly access your Egnyte content directly within your Claude conversations.
For Claude Pro or Team Users:
On the Desktop App or Web Version:
- Go to Settings → Connectors
- Find Egnyte in the available connectors list, or add as a custom connector with URL: https://mcp-server.egnyte.com/mcp
- Click "Add" and "Connect"
- You will be redirected to the authentication page
- Enter your Egnyte domain and authenticate with your Egnyte credentials
- All Egnyte tools should appear in Claude
For detailed instructions, see the official Claude + Egnyte documentation .

### Claude Code

Claude Code is a command line tool for agentic coding that allows developers to delegate coding tasks to Claude directly from their terminal. It also supports MCP servers for enhanced functionality.
To add the Egnyte MCP server to Claude Code, run:
For more information about Claude Code and MCP integration, see the official Claude Code MCP documentation .
[LINK: official Claude Code MCP documentation](https://docs.claude.com/en/docs/claude-code/mcp)

### Other MCP-Compatible Clients

Any AI client that supports the Model Context Protocol with OAuth 2.0 authentication can connect to the Egnyte MCP Server. Configure your client with the server URL https://mcp-server.egnyte.com/mcp and follow the standard OAuth authentication flow.

## Available Tools

The Egnyte Remote MCP Server provides a comprehensive set of tools for interacting with your Egnyte content. These tools are organized by functionality:

### Search and Discovery Tools

### AI-Powered Tools

### File System Operations

### Project Management Tools

### Workflow Management Tools

### Collaboration Tools

## Data Privacy and Security

When using the Egnyte Remote MCP Server, data security and privacy are maintained through the following measures:

### Data Access and Responsibilities

- Customer Responsibilities: Customers maintain control over which AI clients are granted access to their Egnyte content and must ensure compliance with their organization's data governance policies.
- AI Client Responsibilities: AI clients must adhere to their own privacy policies and data handling practices when processing Egnyte content.
- Egnyte Responsibilities: Egnyte ensures secure OAuth authentication, respects existing permissions, and does not store or cache any content accessed through the MCP server.

## Additional Information

[LINK: Egnyte Developer Portal](https://developers.egnyte.com/docs/read/Best_Practices#Rate-Limiting)
[LINK: Helpdesk article](https://helpdesk.egnyte.com/hc/en-us/articles/17683455594125-Public-API-Usage-Restrictions-by-Plan)

--------------------