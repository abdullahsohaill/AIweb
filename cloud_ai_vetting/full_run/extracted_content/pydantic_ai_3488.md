# Pydantic AI
**URL:** https://ai.pydantic.dev
**Page Title:** Pydantic AI - Pydantic AI
--------------------


## Pydantic AI

GenAI Agent Framework, the Pydantic way
Pydantic AI is a Python agent framework designed to help you
  quickly, confidently, and painlessly build production grade applications and workflows with Generative AI.
FastAPI revolutionized web development by offering an innovative and ergonomic design, built on the foundation of Pydantic Validation and modern Python features like type hints.
[LINK: Pydantic Validation](https://docs.pydantic.dev)
Yet despite virtually every Python agent framework and LLM library using Pydantic Validation, when we began to use LLMs in Pydantic Logfire , we couldn't find anything that gave us the same feeling.
We built Pydantic AI with one simple aim: to bring that FastAPI feeling to GenAI app and agent development.

## Why use Pydantic AI

- Built by the Pydantic Team : Pydantic Validation is the validation layer of the OpenAI SDK, the Google ADK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor and many more. Why use the derivative when you can go straight to the source?
Built by the Pydantic Team : Pydantic Validation is the validation layer of the OpenAI SDK, the Google ADK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor and many more. Why use the derivative when you can go straight to the source?
[LINK: Pydantic Validation](https://docs.pydantic.dev/latest/)
- Model-agnostic :
Supports virtually every model and provider: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, and Perplexity; Azure AI Foundry, Amazon Bedrock, Google Vertex AI, Ollama, LiteLLM, Groq, OpenRouter, Together AI, Fireworks AI, Cerebras, Hugging Face, GitHub, Heroku, Vercel, Nebius, OVHcloud, Alibaba Cloud, SambaNova, and Outlines. If your favorite model or provider is not listed, you can easily implement a custom model .
Model-agnostic :
Supports virtually every model and provider: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, and Perplexity; Azure AI Foundry, Amazon Bedrock, Google Vertex AI, Ollama, LiteLLM, Groq, OpenRouter, Together AI, Fireworks AI, Cerebras, Hugging Face, GitHub, Heroku, Vercel, Nebius, OVHcloud, Alibaba Cloud, SambaNova, and Outlines. If your favorite model or provider is not listed, you can easily implement a custom model .
- Seamless Observability :
Tightly integrates with Pydantic Logfire , our general-purpose OpenTelemetry observability platform, for real-time debugging, evals-based performance monitoring, and behavior, tracing, and cost tracking. If you already have an observability platform that supports OTel, you can use that too .
Seamless Observability :
Tightly integrates with Pydantic Logfire , our general-purpose OpenTelemetry observability platform, for real-time debugging, evals-based performance monitoring, and behavior, tracing, and cost tracking. If you already have an observability platform that supports OTel, you can use that too .
- Fully Type-safe :
Designed to give your IDE or AI coding agent as much context as possible for auto-completion and type checking , moving entire classes of errors from runtime to write-time for a bit of that Rust "if it compiles, it works" feel.
Fully Type-safe :
Designed to give your IDE or AI coding agent as much context as possible for auto-completion and type checking , moving entire classes of errors from runtime to write-time for a bit of that Rust "if it compiles, it works" feel.
- Powerful Evals :
Enables you to systematically test and evaluate the performance and accuracy of the agentic systems you build, and monitor the performance over time in Pydantic Logfire.
Powerful Evals :
Enables you to systematically test and evaluate the performance and accuracy of the agentic systems you build, and monitor the performance over time in Pydantic Logfire.
- MCP, A2A, and UI :
Integrates the Model Context Protocol , Agent2Agent , and various UI event stream standards to give your agent access to external tools and data, let it interoperate with other agents, and build interactive applications with streaming event-based communication.
MCP, A2A, and UI :
Integrates the Model Context Protocol , Agent2Agent , and various UI event stream standards to give your agent access to external tools and data, let it interoperate with other agents, and build interactive applications with streaming event-based communication.
- Human-in-the-Loop Tool Approval :
Easily lets you flag that certain tool calls require approval before they can proceed, possibly depending on tool call arguments, conversation history, or user preferences.
Human-in-the-Loop Tool Approval :
Easily lets you flag that certain tool calls require approval before they can proceed, possibly depending on tool call arguments, conversation history, or user preferences.
- Durable Execution :
Enables you to build durable agents that can preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability.
Durable Execution :
Enables you to build durable agents that can preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability.
- Streamed Outputs :
Provides the ability to stream structured output continuously, with immediate validation, ensuring real time access to generated data.
Streamed Outputs :
Provides the ability to stream structured output continuously, with immediate validation, ensuring real time access to generated data.
- Graph Support :
Provides a powerful way to define graphs using type hints, for use in complex applications where standard control flow can degrade to spaghetti code.
Graph Support :
Provides a powerful way to define graphs using type hints, for use in complex applications where standard control flow can degrade to spaghetti code.
Realistically though, no list is going to be as convincing as giving it a try and seeing how it makes you feel!
Sign up for our newsletter, The Pydantic Stack , with updates & tutorials on Pydantic AI, Logfire, and Pydantic:

## Hello World Example

Here's a minimal example of Pydantic AI:
- We configure the agent to use Anthropic's Claude Sonnet 4.0 model, but you can also set the model when running the agent.
[LINK: Anthropic's Claude Sonnet 4.0](api/models/anthropic/)
- Register static instructions using a keyword argument to the agent.
- Run the agent synchronously, starting a conversation with the LLM.
(This example is complete, it can be run "as is", assuming you've installed the pydantic_ai package )
The exchange will be very short: Pydantic AI will send the instructions and the user prompt to the LLM, and the model will return a text response.
Not very interesting yet, but we can easily add tools , dynamic instructions , and structured outputs to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using Pydantic AI to build a support agent for a bank:
- This agent will act as first-tier support in a bank. Agents are generic in the type of dependencies they accept and the type of output they return. In this case, the support agent has type Agent [ SupportDependencies , SupportOutput ] .
- Here we configure the agent to use OpenAI's GPT-5 model , you can also set the model when running the agent.
[LINK: OpenAI's GPT-5 model](api/models/openai/)
- The SupportDependencies dataclass is used to pass data, connections, and logic into the model that will be needed when running instructions and tool functions. Pydantic AI's system of dependency injection provides a type-safe way to customise the behavior of your agents, and can be especially useful when running unit tests and evals.
- Static instructions can be registered with the instructions keyword argument to the agent.
[LINK: instructions keyword argument](api/agent/#pydantic_ai.agent.Agent.__init__)
- Dynamic instructions can be registered with the @agent.instructions decorator, and can make use of dependency injection. Dependencies are carried via the RunContext argument, which is parameterized with the deps_type from above. If the type annotation here is wrong, static type checkers will catch it.
[LINK: @agent.instructions](api/agent/#pydantic_ai.agent.Agent.instructions)
[LINK: RunContext](api/tools/#pydantic_ai.tools.RunContext)
- The @agent.tool decorator let you register functions which the LLM may call while responding to a user. Again, dependencies are carried via RunContext , any other arguments become the tool schema passed to the LLM. Pydantic is used to validate these arguments, and errors are passed back to the LLM so it can retry.
[LINK: RunContext](api/tools/#pydantic_ai.tools.RunContext)
- The docstring of a tool is also passed to the LLM as the description of the tool. Parameter descriptions are extracted from the docstring and added to the parameter schema sent to the LLM.
- Run the agent asynchronously, conducting a conversation with the LLM until a final response is reached. Even in this fairly simple case, the agent will exchange multiple messages with the LLM as tools are called to retrieve an output.
- The response from the agent will be guaranteed to be a SupportOutput . If validation fails reflection , the agent is prompted to try again.
- The output will be validated with Pydantic to guarantee it is a SupportOutput , since the agent is generic, it'll also be typed as a SupportOutput to aid with static type checking.
- In a real use case, you'd add more tools and longer instructions to the agent to extend the context it's equipped with and support it can provide.
- This is a simple sketch of a database connection, used to keep the example short and readable. In reality, you'd be connecting to an external database (e.g. PostgreSQL) to get information about customers.
- This Pydantic model is used to constrain the structured data returned by the agent. From this simple definition, Pydantic builds the JSON Schema that tells the LLM how to return the data, and performs validation to guarantee the data is correct at the end of the run.
[LINK: Pydantic](https://docs.pydantic.dev)
Complete bank_support.py example
The code included here is incomplete for the sake of brevity (the definition of DatabaseConn is missing); you can find the complete bank_support.py example here .

## Instrumentation with Pydantic Logfire

Even a simple agent with just a handful of tools can result in a lot of back-and-forth with the LLM, making it nearly impossible to be confident of what's going on just from reading the code.
To understand the flow of the above runs, we can watch the agent in action using Pydantic Logfire.
To do this, we need to set up Logfire , and add the following to our code:
- Configure the Logfire SDK, this will fail if project is not set up.
- This will instrument all Pydantic AI agents used from here on out. If you want to instrument only a specific agent, you can pass the instrument=True keyword argument to the agent.
[LINK: instrument=True keyword argument](api/agent/#pydantic_ai.agent.Agent.__init__)
- In our demo, DatabaseConn uses sqlite3 to connect to a PostgreSQL database, so logfire.instrument_sqlite3() is used to log the database queries.
[LINK: sqlite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3)
[LINK: logfire.instrument_sqlite3()](https://logfire.pydantic.dev/docs/integrations/databases/sqlite3/)
That's enough to get the following view of your agent in action:
Logfire instrumentation for the bank agent — View in Logfire
See Monitoring and Performance to learn more.

## llms.txt

The Pydantic AI documentation is available in the llms.txt format.
This format is defined in Markdown and suited for LLMs and AI coding assistants and agents.
Two formats are available:
- llms.txt : a file containing a brief description
  of the project, along with links to the different sections of the documentation. The structure
  of this file is described in details here .
- llms-full.txt : Similar to the llms.txt file,
  but every link content is included. Note that this file may be too large for some LLMs.
As of today, these files are not automatically leveraged by IDEs or coding agents, but they will use it if you provide a link or the full text.

## Next Steps

To try Pydantic AI for yourself, install it and follow the instructions in the examples .
Read the docs to learn more about building applications with Pydantic AI.
Read the API Reference to understand Pydantic AI's interface.
[LINK: API Reference](api/agent/)
Join :simple-slack: Slack or file an issue on GitHub if you have any questions.
[LINK: :simple-slack: Slack](https://logfire.pydantic.dev/docs/join-slack/)
[LINK: GitHub](https://github.com/pydantic/pydantic-ai/issues)

--------------------