# Firecrawl MCP
**URL:** https://docs.firecrawl.dev/mcp
**Page Title:** 
--------------------

### (Raw Extraction Fallback)

{
  "server": {
    "name": "Firecrawl Docs",
    "version": "1.0.0",
    "transport": "http"
  },
  "capabilities": {
    "tools": {
      "SearchFirecrawlDocs": {
        "name": "SearchFirecrawlDocs",
        "description": "Search across the Firecrawl Docs knowledge base to find relevant information, code examples, API references, and guides. Use this tool when you need to answer questions about Firecrawl Docs, find specific documentation, understand how features work, or locate implementation details. The search returns contextual content with titles and direct links to the documentation pages.",
        "inputSchema": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "A query to search the content with."
            }
          },
          "required": [
            "query"
          ]
        },
        "operationId": "MintlifyDefaultSearch"
      }
    },
    "resources": [],
    "prompts": []
  }
}

--------------------