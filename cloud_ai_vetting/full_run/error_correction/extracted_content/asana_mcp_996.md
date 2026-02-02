# Asana MCP
**URL:** https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server
**Page Title:** Using Asana's MCP Server
--------------------


### Beta feature

By enabling this app integration, you acknowledge that you are using an experimental Model Context Protocol (MCP) server to connect Asana with external large language models (LLMs). As this is an experimental beta tool, it is provided on an "as is" basis. You may encounter bugs, errors, or unexpected results.

## Overview

Asana offers a Model Context Protocol (MCP) server, accessible via app integration, which allows AI assistants and other applications to access the Asana Work Graph from beyond the Asana platform. This server provides a way to interact with your Asana workspace through various AI platforms and tools that support MCP.
With this server, Asana customers can:
- Access Asana data from compatible AI applications
- Create and manage tasks and projects through natural language
- Generate reports and summaries based on Asana data
- Analyze project data and get AI-powered suggestions
Example requests users could make from outside Asana using the MCP:
- "Find all my incomplete tasks due this week"
- "Create a new task in the Marketing project assigned to me"
- "List all sections in the Product Launch project"
- "Show me the status of the Q2 Planning project"

## Requirements

- A compatible MCP client. There is a partial list of clients here!
[LINK: There is a partial list of clients here!](/docs/mcp-clients)
- The app named "Asana MCP" is not blocked via Asana app management . If you're not sure if the app is blocked, try to connect your MCP client to the server and go through the authorization flow. You'll either be able to authorize the app like normal or, if the app is currently blocked, be prompted to send a request for your admin to unblock the app for your domain.

## Available tools

Asana's MCP server includes 30+ tools for:
- Project tracking and status updates
- Task creation and management
- User information
- Getting updates on Goals
- Team organization
- Quick Asana object searching via typeahead

### Listing available tools

Once you’ve authenticated your client app, you can use the tools/list MCP command to view all of the Asana endpoints available through your connection. This ensures your client always has the most up-to-date list of supported tools.
This approach follows the Model Context Protocol best practices. Instead of documenting every tool statically, the protocol itself exposes a reliable way to discover them dynamically.

## Connecting to Asana's MCP Server

The Asana MCP server is available at: https://mcp.asana.com/sse
This server requires authentication with your Asana account. When connecting, you will be prompted to authorize the application to access your Asana data.

### Allowlist

Due to the implementation of an OAuth redirect URI allowlist, some third-party applications might require additional configuration or registration of their redirect URI with Asana Support before a successful connection can be established. If you’re a maintainer of an MCP client, see Integrating with Asana's MCP Server for details on how to register.
[LINK: Integrating with Asana's MCP Server](/docs/integrating-with-asanas-mcp-server)

## Using with Claude.ai

Note: Requires Claude Enterprise or Teams, and the connection must be set up by a Workspace Owner or Primary Owner in Claude before users will be able to connect

### For Claude.ai Admins

Only Workspace Owners and Primary Owners can set up MCP server connections in Claude.ai:
- Go to Settings in Claude.ai
- Navigate to the "Integrations" section
- Click "Add server"
- Enter "Asana" as the Name
- Enter https://mcp.asana.com/sse as the Server URL
- Click "Add server"
- Authenticate with your Asana account via OAuth
- Select which Asana tools to enable for your workspace
- Click "Save"

### For Claude.ai Users

After your admin has set up the integration:
- Navigate to claude.ai
- Click on the tools menu (next to the search icon)
- Select "Asana" from the list of available integrations
- If this is your first time using the integration, you'll be prompted to authenticate
- Once authenticated, you can start using Claude with Asana

### For Claude Code Users

- Install and configure Claude Code locally on your computer .
[LINK: Install and configure Claude Code locally on your computer](https://code.claude.com/docs/en/quickstart)
- Run the following command in the terminal (not Claude Code chat) to add Asana MCP to Claude Code:
- Authenticate to Asana if prompted.
- Open Claude Code chat in the terminal and start using Asana:

## Using with Cursor

- Go to your Cursor editor's settings ("Settings" > "Cursor Settings")
- "MCP" > "+ Add new global MCP server" OR "Tools & Integrations" > "New MCP Server"
- Add the following to your mcp.json : "asana" : { "command" : "npx" , "args" : [ "mcp-remote" , "https://mcp.asana.com/sse" ]
        }
- Save your mcp.json file. If this is your first time using the integration, you'll be prompted to authenticate NOTE: If you run into Internal Server Error you can delete your local ~/.mcp-auth directory rm -rf ~/.mcp-auth . WARNING: if you have other applications that might be using this directory ~/.mcp-auth you will need to re-auth ( EX: other applications that use mcp-remote )
- Once authenticated, you can start using Cursor with Asana

## Using with other supported MCP Clients

For MCP-compatible clients:
- Configure your client to connect to https://mcp.asana.com/sse
- Ensure your client supports OAuth authentication
- Set up the connection according to your client's documentation
- Authenticate with your Asana account when prompted
- Select which Asana tools to enable based on your needs

## Using with ChatGPT

We're excited about the potential for ChatGPT to connect with Asana's MCP server and actively exploring this integration! ChatGPT requires some additional tools we do not yet support, please check back soon for updates.

## Allowing / Blocking Asana's MCP Server

Customers in Asana's Enterprise+ tier may use Asana's App Management to allow or block the Asana MCP app. This action will apply to all MCP clients. Customers in other tiers may contact Asana Support to block the Asana MCP app. Super admins must make the support request.

## Troubleshooting

- If authentication fails, try logging out of your Asana account and logging back in. If that does not address the issue or you see a “Client not found” error, try removing the Asana MCP integration within your client and adding it back.
- Ensure your MCP client supports SSE-based servers (not Streamable HTTP)
- If you’re still not able to connect or are seeing an invalid_redirect_uri error, reach out to the maintainer of the app you’re using for help (see Integrating with Asana's MCP Server )
[LINK: Integrating with Asana's MCP Server](/docs/integrating-with-asanas-mcp-server)
- Check that your client can handle OAuth authentication flows
- Verify you have the necessary permissions in your Asana workspace

## Support

For additional help with Asana's MCP server, contact Asana Support .
Updated about 2 months ago

--------------------