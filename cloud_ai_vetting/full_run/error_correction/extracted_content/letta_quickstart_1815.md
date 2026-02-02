# Letta Quickstart
**URL:** https://docs.letta.com/quickstart
**Page Title:** Developer quickstart | Letta Docs
--------------------


## Developer quickstart

Quick start guide to creating your first Letta agent and sending messages.
This guide will show you how to create a Letta agent with the Letta APIs or SDKs (Python/Typescript). To create agents with a low-code UI, see our ADE quickstart .

## Why Letta?

Unlike traditional LLM APIs where you manually manage conversation history and state, Letta agents maintain their own persistent memory. You only send new messages. The agent remembers everything from past conversations without you storing or retrieving anything. This enables agents that truly learn and evolve over time.

## 1. Prerequisites

Create an API key :
[LINK: Create an API key](https://app.letta.com/api-keys)
Set your API key as an environment variable:
- TypeScript
- Python

## 2. Install the Letta SDK

- TypeScript
- Python

## 3. Create an agent

Agents in Letta have two key components:
- Memory blocks : Persistent context that’s always visible to the agent (like a persona and information about the user)
- Tools : Actions the agent can take (like searching the web or running code)
- TypeScript
- Python
- curl

## 4. Message your agent

Once the agent is created, we can send the agent a message using its id field:
- TypeScript
- Python
- curl
The response contains the agent’s full response to the message, which includes reasoning steps (chain-of-thought), tool calls, tool responses, and assistant (agent) messages:
Notice how the agent retrieved information from its memory blocks without you having to send the context. This is the key difference from traditional LLM APIs where you’d need to include the full conversation history with every request.
You can read more about the response format from the message route here .

## 5. View your agent in the ADE

Another way to interact with Letta agents is via the Agent Development Environment (or ADE for short). The ADE is a UI on top of the Letta API that allows you to quickly build, prototype, and observe your agents.
If we navigate to our agent in the ADE, we should see our agent’s state in full detail, as well as the message that we sent to it:
Read our ADE setup guide →

## Next steps

Congratulations! 🎉 You just created and messaged your first stateful agent with Letta using the API and SDKs. See the following resources for next steps for building more complex agents with Letta:
- Create and attach custom tools to your agent
- Customize agentic memory management
- Version and distribute your agent with agent templates
- View the full API and SDK reference
[LINK: API and SDK reference](/api-reference/overview)

### Hi, I'm Ezra.

I help developers build with Letta. Ask me about agents, memory, tools, or deployment.

--------------------