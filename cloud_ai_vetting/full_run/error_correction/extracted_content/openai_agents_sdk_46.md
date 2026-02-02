# OpenAI Agents SDK
**URL:** https://openai.github.io/openai-agents-python/mcp
**Page Title:** Model context protocol (MCP) - OpenAI Agents SDK
--------------------


## Model context protocol (MCP)

The Model context protocol (MCP) standardises how applications expose tools and
context to language models. From the official documentation:
MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI
applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP
provides a standardized way to connect AI models to different data sources and tools.
The Agents Python SDK understands multiple MCP transports. This lets you reuse existing MCP servers or build your own to expose
filesystem, HTTP, or connector backed tools to an agent.

## Choosing an MCP integration

Before wiring an MCP server into an agent decide where the tool calls should execute and which transports you can reach. The
matrix below summarises the options that the Python SDK supports.
The sections below walk through each option, how to configure it, and when to prefer one transport over another.

## 1. Hosted MCP server tools

Hosted tools push the entire tool round-trip into OpenAI's infrastructure. Instead of your code listing and calling tools, the HostedMCPTool forwards a server label (and optional connector metadata) to the Responses API. The
model lists the remote server's tools and invokes them without an extra callback to your Python process. Hosted tools currently
work with OpenAI models that support the Responses API's hosted MCP integration.

### Basic hosted MCP tool

Create a hosted tool by adding a HostedMCPTool to the agent's tools list. The tool_config dict mirrors the JSON you would send to the REST API:
The hosted server exposes its tools automatically; you do not add it to mcp_servers .

### Streaming hosted MCP results

Hosted tools support streaming results in exactly the same way as function tools. Pass stream=True to Runner.run_streamed to
consume incremental MCP output while the model is still working:

### Optional approval flows

If a server can perform sensitive operations you can require human or programmatic approval before each tool execution. Configure require_approval in the tool_config with either a single policy ( "always" , "never" ) or a dict mapping tool names to
policies. To make the decision inside Python, provide an on_approval_request callback.
The callback can be synchronous or asynchronous and is invoked whenever the model needs approval data to keep running.

### Connector-backed hosted servers

Hosted MCP also supports OpenAI connectors. Instead of specifying a server_url , supply a connector_id and an access token. The
Responses API handles authentication and the hosted server exposes the connector's tools.
Fully working hosted tool samples—including streaming, approvals, and connectors—live in examples/hosted_mcp .
[LINK: examples/hosted_mcp](https://github.com/openai/openai-agents-python/tree/main/examples/hosted_mcp)

## 2. Streamable HTTP MCP servers

When you want to manage the network connection yourself, use MCPServerStreamableHttp . Streamable HTTP servers are ideal when you control the
transport or want to run the server inside your own infrastructure while keeping latency low.
The constructor accepts additional options:
- client_session_timeout_seconds controls HTTP read timeouts.
- use_structured_content toggles whether tool_result.structured_content is preferred over textual output.
- max_retry_attempts and retry_backoff_seconds_base add automatic retries for list_tools() and call_tool() .
- tool_filter lets you expose only a subset of tools (see Tool filtering ).

## 3. HTTP with SSE MCP servers

Warning
The MCP project has deprecated the Server-Sent Events transport. Prefer Streamable HTTP or stdio for new integrations and keep SSE only for legacy servers.
If the MCP server implements the HTTP with SSE transport, instantiate MCPServerSse . Apart from the transport, the API is identical to the Streamable HTTP server.

## 4. stdio MCP servers

For MCP servers that run as local subprocesses, use MCPServerStdio . The SDK spawns the
process, keeps the pipes open, and closes them automatically when the context manager exits. This option is helpful for quick
proofs of concept or when the server only exposes a command line entry point.

## 5. MCP server manager

When you have multiple MCP servers, use MCPServerManager to connect them up front and expose the connected subset to your agents.
Key behaviors:
- active_servers includes only successfully connected servers when drop_failed_servers=True (the default).
- Failures are tracked in failed_servers and errors .
- Set strict=True to raise on the first connection failure.
- Call reconnect(failed_only=True) to retry failed servers, or reconnect(failed_only=False) to restart all servers.
- Use connect_timeout_seconds , cleanup_timeout_seconds , and connect_in_parallel to tune lifecycle behavior.

## Tool filtering

Each MCP server supports tool filters so that you can expose only the functions that your agent needs. Filtering can happen at
construction time or dynamically per run.

### Static tool filtering

Use create_static_tool_filter to configure simple allow/block lists:
When both allowed_tool_names and blocked_tool_names are supplied the SDK applies the allow-list first and then removes any
blocked tools from the remaining set.

### Dynamic tool filtering

For more elaborate logic pass a callable that receives a ToolFilterContext . The callable can be
synchronous or asynchronous and returns True when the tool should be exposed.
The filter context exposes the active run_context , the agent requesting the tools, and the server_name .

## Prompts

MCP servers can also provide prompts that dynamically generate agent instructions. Servers that support prompts expose two
methods:
- list_prompts() enumerates the available prompt templates.
- get_prompt(name, arguments) fetches a concrete prompt, optionally with parameters.

## Caching

Every agent run calls list_tools() on each MCP server. Remote servers can introduce noticeable latency, so all of the MCP
server classes expose a cache_tools_list option. Set it to True only if you are confident that the tool definitions do not
change frequently. To force a fresh list later, call invalidate_tools_cache() on the server instance.

## Tracing

Tracing automatically captures MCP activity, including:
- Calls to the MCP server to list tools.
- MCP-related information on tool calls.

## Further reading

- Model Context Protocol – the specification and design guides.
- examples/mcp – runnable stdio, SSE, and Streamable HTTP samples.
[LINK: examples/mcp](https://github.com/openai/openai-agents-python/tree/main/examples/mcp)
- examples/hosted_mcp – complete hosted MCP demonstrations including approvals and connectors.
[LINK: examples/hosted_mcp](https://github.com/openai/openai-agents-python/tree/main/examples/hosted_mcp)

--------------------