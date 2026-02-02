# Mercado Libre
**URL:** https://mcp.mercadolibre.com
**Page Title:** Developers
--------------------

Usamos cookies para mejorar tu experiencia en Mercado Libre. Consultar más en nuestro Centro de Privacidad.
Documentation  Mercado Libre
Documentation

## 1. MCP Server from Mercado Libre

The Model Context Protocol (MCP) is an open protocol that standardizes the connection of artificial intelligence models with different data sources and tools. In this context, the MCP Server from Mercado Libre offers utilities so that developers can easily interact with Mercado Libre’s APIs and resources using natural language, simplifying tasks and product integrations.

## 2. Prerequisites

Before starting, make sure you have the following environment:

## 3. Installation and configuration

## 3.1 Cursor

To connect to our MCP from Mercado Libre, you must first connect with the client that best fits your integration. Check the step-by-step according to the client type.
In Cursor, you can click the button below or follow the steps manually.
[LINK: information](https://developers.mercadolibre.com.ar/en_us/authorization-and-token-recommendations)
To connect to the MCP server of Mercado Libre from Cursor manually, follow these steps:
This will open a tab where you can view and configure the available MCP servers. In the configuration, be sure to include the following JSON block to connect to the Mercado Libre MCP server
JSON:
[LINK: information](https://developers.mercadolibre.com.ar/en_us/authorization-and-token-recommendations)

## 3.2 Windsurf

To connect to Mercado Libre's MCP server from Windsurf, follow these steps:
JSON:

## 3.3 Other IDEs

Open the IDE settings and look for the JSON file related to MCP servers. Then, fill the “Authorization” fields with your Access Token.
JSON:

## 4. MCP Server connection

- Establish the remote connection from your preferred client (e.g. Cursor).
- Make sure the MCP server is available and correctly configured in your client.
- If it doesn't appear, check the configuration and reload the MCP servers list.

## 5. Available tools

The MCP Server from Mercado Libre offers tools to make integration and information queries easier.

## search_documentation

Enables searching for specific terms or key concepts across all the technical documentation for Mercado Libre developers.
- query : Keywords to search for within the documentation (Required)
- language : Language of the documentation to consult (e.g., en_us, es_ar, pt_br) (Required)
- siteId : Country ID to filter results (e.g., MLA, MLB, MLM, etc) (Optional)
- limit : Maximum number of results to return (Optional)
- offset : Number of results to skip (Optional)

## get_documentation_page

Retrieves the full content of a specific documentation page, useful for accessing detailed specifications or use cases.
- path : Path of the page to retrieve (Required)
- language : Language of the documentation to consult (e.g., en_us, es_ar, pt_br) (Required)
- siteId : Country ID to filter results (e.g., MLA, MLB, MLM, etc) (Optional)

## 6. Use cases

MCP Server ensures that common developer activities are optimized easily and quickly. Below, find some use cases to implement in your integration.

## 6.1 Search documentation from your IDE

The tools are not used directly by the user or developer, but by the Agent IDE. For example:
The tool allows the Agentic IDE to search for keywords throughout the official Mercado Libre documentation and retrieve the most relevant endpoints or routes for the consulted context.
Then, with the get_documentation_page tool, the Agentic IDE accesses the complete content of the routes identified in the previous step, allowing it to obtain specific information and concrete use cases directly from the documentation.
This way, the IDE automates querying and browsing documentation, making it easier for the developer to receive contextualized and precise answers without having to search manually.

## 6.2 Generate integration code

In addition to consulting documentation, MCP tools are used by the Agentic IDE to generate code and assist in product integration in your projects.
For example, you can ask the assistant to review the documentation of the product you want to integrate and identify the steps required to complete the integration. MCP Server provides the relevant context (including code samples and technical documentation) that the Agentic IDE uses to suggest or even directly apply the necessary changes in your project.
In this way, the IDE automates querying, analysis, and implementation of integrations, making the developer's work easier and speeding up the development process.
You can request recommendations to implement specific integrations, for example:

## 7. Errors and solutions

## 7.1 Invalid or missing token

If when trying to connect, the application remains in "Loading Tools" state indefinitely or fails to connect to the server, there may be a problem with the authentication token.
Possible causes:
- No authentication token was provided in the request.
- The provided token has expired or is incorrect.
- The token format is invalid (e.g., missing or incorrectly copied characters).
- The token does not have the necessary permissions to access the requested resource.
Suggested solutions:
- Check that the token is present in the request header (in Authorization: Bearer <Access_Token>).
- Make sure the token has not expired. If so, request a new one.
- Copy the full token, with no additional spaces or missing characters.
- 1. MCP Server from Mercado Libre
- 2. Prerequisites
- 3. Installation and configuration
- 3.1 Cursor
- 3.2 Windsurf
- 3.3 Other IDEs
- 4. MCP Server connection
- 5. Available tools
- search_documentation
- get_documentation_page
- 6. Use cases
- 6.1 Search documentation from your IDE
- 6.2 Generate integration code
- 7. Errors and solutions
- 7.1 Invalid or missing token

--------------------