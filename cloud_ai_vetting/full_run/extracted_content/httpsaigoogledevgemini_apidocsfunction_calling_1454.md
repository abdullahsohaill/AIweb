# https://ai.google.dev/gemini-api/docs/function-calling
**URL:** https://ai.google.dev/gemini-api/docs/function-calling
**Page Title:** Function calling with the Gemini API  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemini-api/docs/function-calling)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Ffunction-calling%3Fexample%3Dmeeting&prompt=select_account)
- On this page
- How function calling works Step 1: Define a function declaration Step 2: Call the model with function declarations Step 3: Execute set_light_values function code Step 4: Create user friendly response with function result and call the model again
- Step 1: Define a function declaration
- Step 2: Call the model with function declarations
- Step 3: Execute set_light_values function code
- Step 4: Create user friendly response with function result and call the model again
- Function declarations
- Function calling with thinking models Managing conversation history manually Inspecting thought signatures
- Managing conversation history manually
- Inspecting thought signatures
- Parallel function calling
- Compositional function calling
- Function calling modes
- Automatic function calling (Python only) Automatic function schema declaration
- Automatic function schema declaration
- Multi-tool use: Combine native tools with function calling
- Multimodal function responses
- Function calling with Structured output
- Model context protocol (MCP) Limitations with built-in MCP support
- Limitations with built-in MCP support
- Supported models
- Best practices
- Notes and limitations
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- Docs
[LINK: Docs](https://ai.google.dev/gemini-api/docs)

## Function calling with the Gemini API

- On this page
- How function calling works Step 1: Define a function declaration Step 2: Call the model with function declarations Step 3: Execute set_light_values function code Step 4: Create user friendly response with function result and call the model again
- Step 1: Define a function declaration
- Step 2: Call the model with function declarations
- Step 3: Execute set_light_values function code
- Step 4: Create user friendly response with function result and call the model again
- Function declarations
- Function calling with thinking models Managing conversation history manually Inspecting thought signatures
- Managing conversation history manually
- Inspecting thought signatures
- Parallel function calling
- Compositional function calling
- Function calling modes
- Automatic function calling (Python only) Automatic function schema declaration
- Automatic function schema declaration
- Multi-tool use: Combine native tools with function calling
- Multimodal function responses
- Function calling with Structured output
- Model context protocol (MCP) Limitations with built-in MCP support
- Limitations with built-in MCP support
- Supported models
- Best practices
- Notes and limitations
Function calling lets you connect models to external tools and APIs.
Instead of generating text responses, the model determines when to call specific
functions and provides the necessary parameters to execute real-world actions.
This allows the model to act as a bridge between natural language and real-world
actions and data. Function calling has 3 primary use cases:
- Augment Knowledge: Access information from external sources like
databases, APIs, and knowledge bases.
- Extend Capabilities: Use external tools to perform computations and
extend the limitations of the model, such as using a calculator or creating
charts.
- Take Actions: Interact with external systems using APIs, such as
scheduling appointments, creating invoices, sending emails, or controlling
smart home devices.

## How function calling works

Function calling involves a structured interaction between your application, the
model, and external functions. Here's a breakdown of the process:
- Define Function Declaration: Define the function declaration in your
application code. Function Declarations describe the function's name,
parameters, and purpose to the model.
- Call LLM with function declarations: Send user prompt along with the
function declaration(s) to the model. It analyzes the request and determines
if a function call would be helpful. If so, it responds with a structured
JSON object.
- Execute Function Code (Your Responsibility): The Model does not execute the function itself. It's your application's responsibility to
process the response and check for Function Call, if Yes : Extract the name and args of the function and execute the
corresponding function in your application. No: The model has provided a direct text response to the prompt
(this flow is less emphasized in the example but is a possible outcome).
- Yes : Extract the name and args of the function and execute the
corresponding function in your application.
- No: The model has provided a direct text response to the prompt
(this flow is less emphasized in the example but is a possible outcome).
- Create User friendly response: If a function was executed, capture the
result and send it back to the model in a subsequent turn of the
conversation. It will use the result to generate a final, user-friendly
response that incorporates the information from the function call.
This process can be repeated over multiple turns, allowing for complex
interactions and workflows. The model also supports calling multiple functions
in a single turn ( parallel function
calling ) and in
sequence ( compositional function
calling ).
[LINK: parallel function
calling](/gemini-api/docs/function-calling#parallel_function_calling)
[LINK: compositional function
calling](/gemini-api/docs/function-calling#compositional_function_calling)

### Step 1: Define a function declaration

Define a function and its declaration within your application code that allows
users to set light values and make an API request. This function could call
external services or APIs.

### Step 2: Call the model with function declarations

Once you have defined your function declarations, you can prompt the model to
use them. It analyzes the prompt and function declarations and decides whether
to respond directly or to call a function. If a function is called, the response
object will contain a function call suggestion.
The model then returns a functionCall object in an OpenAPI compatible
schema specifying how to call one or more of the declared functions in order to
respond to the user's question.

### Step 3: Execute set_light_values function code

Extract the function call details from the model's response, parse the arguments
, and execute the set_light_values function.

### Step 4: Create user friendly response with function result and call the model again

Finally, send the result of the function execution back to the model so it can
incorporate this information into its final response to the user.
This completes the function calling flow. The model successfully used the set_light_values function to perform the request action of the user.

## Function declarations

When you implement function calling in a prompt, you create a tools object,
which contains one or more function declarations . You define functions using
JSON, specifically with a select subset of the OpenAPI schema format. A
single function declaration can include the following parameters:
[LINK: select subset](https://ai.google.dev/api/caching#Schema)
[LINK: OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schemaw)
- name (string): A unique name for the function ( get_weather_forecast , send_email ). Use descriptive names without spaces or special characters
(use underscores or camelCase).
- description (string): A clear and detailed explanation of the function's
purpose and capabilities. This is crucial for the model to understand when
to use the function. Be specific and provide examples if helpful ("Finds
theaters based on location and optionally movie title which is currently
playing in theaters.").
- parameters (object): Defines the input parameters the function
expects. type (string): Specifies the overall data type, such as object . properties (object): Lists individual parameters, each with: type (string): The data type of the parameter, such as string , integer , boolean, array . description (string): A description of the parameter's purpose and
format. Provide examples and constraints ("The city and state,
e.g., 'San Francisco, CA' or a zip code e.g., '95616'."). enum (array, optional): If the parameter values are from a fixed
set, use "enum" to list the allowed values instead of just describing
them in the description. This improves accuracy ("enum":
["daylight", "cool", "warm"]). required (array): An array of strings listing the parameter names that
are mandatory for the function to operate.
- type (string): Specifies the overall data type, such as object .
- properties (object): Lists individual parameters, each with: type (string): The data type of the parameter, such as string , integer , boolean, array . description (string): A description of the parameter's purpose and
format. Provide examples and constraints ("The city and state,
e.g., 'San Francisco, CA' or a zip code e.g., '95616'."). enum (array, optional): If the parameter values are from a fixed
set, use "enum" to list the allowed values instead of just describing
them in the description. This improves accuracy ("enum":
["daylight", "cool", "warm"]).
- type (string): The data type of the parameter, such as string , integer , boolean, array .
- description (string): A description of the parameter's purpose and
format. Provide examples and constraints ("The city and state,
e.g., 'San Francisco, CA' or a zip code e.g., '95616'.").
- enum (array, optional): If the parameter values are from a fixed
set, use "enum" to list the allowed values instead of just describing
them in the description. This improves accuracy ("enum":
["daylight", "cool", "warm"]).
- required (array): An array of strings listing the parameter names that
are mandatory for the function to operate.
You can also construct FunctionDeclarations from Python functions directly using types.FunctionDeclaration.from_callable(client=client, callable=your_function) .

## Function calling with thinking models

Gemini 3 and 2.5 series models use an internal "thinking" process to reason through requests. This
significantly improves function calling performance,
allowing the model to better determine when to call a function and which
parameters to use. Because the Gemini API is stateless, models use thought signatures to maintain context
across multi-turn conversations.
[LINK: "thinking"](/gemini-api/docs/thinking)
[LINK: thought signatures](/gemini-api/docs/thought-signatures)
This section covers advanced management of thought signatures and is only
necessary if you're manually constructing API requests (e.g., via REST) or
manipulating conversation history.
If you're using the Google GenAI SDKs (our
official libraries), you don't need to manage this process . The SDKs
automatically handle the necessary steps, as shown in the earlier example .
[LINK: Google GenAI SDKs](/gemini-api/docs/libraries)
[LINK: example](/gemini-api/docs/function-calling#step-4)

### Managing conversation history manually

If you modify the conversation history manually, instead of sending the complete previous response you
must correctly handle the thought_signature included in the model's turn.
[LINK: complete previous response](/gemini-api/docs/function-calling#step-4)
Follow these rules to ensure the model's context is preserved:
- Always send the thought_signature back to the model inside its original Part .
[LINK: Part](/api#request-body-structure)
- Don't merge a Part containing a signature with one that does not. This
breaks the positional context of the thought.
- Don't combine two Parts that both contain signatures, as the signature
strings cannot be merged.
In Gemini 3, any Part of a model response
may contain a thought signature.
While we generally recommend returning signatures from all Part types,
passing back thought signatures is mandatory for function calling. Unless you
are manipulating conversation history manually, the Google GenAI SDK will
handle thought signatures automatically.
[LINK: Part](/api#request-body-structure)
If you are manipulating conversation history manually, refer to the Thoughts Signatures page for complete
guidance and details on handling thought signatures for Gemini 3.
[LINK: Thoughts Signatures](/gemini-api/docs/thought-signatures)

### Inspecting thought signatures

While not necessary for implementation, you can inspect the response to see the thought_signature for debugging or educational purposes.
Learn more about limitations and usage of thought signatures, and about thinking
models in general, on the Thinking page.
[LINK: Thinking](/gemini-api/docs/thinking#signatures)

## Parallel function calling

In addition to single turn function calling, you can also call multiple
functions at once. Parallel function calling lets you execute multiple functions
at once and is used when the functions are not dependent on each other. This is
useful in scenarios like gathering data from multiple independent sources, such
as retrieving customer details from different databases or checking inventory
levels across various warehouses or performing multiple actions such as
converting your apartment into a disco.
Configure the function calling mode to allow using all of the specified tools.
To learn more, you can read about configuring function calling .
[LINK: configuring function calling](/gemini-api/docs/function-calling#function_calling_modes)
Each of the printed results reflects a single function call that the model has
requested. To send the results back, include the responses in the same order as
they were requested.
The Python SDK supports automatic function calling ,
which automatically converts Python functions to declarations, handles the
function call execution and response cycle for you. Following is an example for
the disco use case.
[LINK: automatic function calling](/gemini-api/docs/function-calling#automatic_function_calling_python_only)

## Compositional function calling

Compositional or sequential function calling allows Gemini to chain multiple
function calls together to fulfill a complex request. For example, to answer
"Get the temperature in my current location", the Gemini API might first invoke
a get_current_location() function followed by a get_weather() function that
takes the location as a parameter.
The following example demonstrates how to implement compositional function
calling using the Python SDK and automatic function calling.
This example uses the automatic function calling feature of the google-genai Python SDK. The SDK automatically converts the Python
functions to the required schema, executes the function calls when requested
by the model, and sends the results back to the model to complete the task.
Expected Output
When you run the code, you will see the SDK orchestrating the function
calls. The model first calls get_weather_forecast , receives the
temperature, and then calls set_thermostat_temperature with the correct
value based on the logic in the prompt.
This example shows how to use JavaScript/TypeScript SDK to do comopositional
function calling using a manual execution loop.
Expected Output
When you run the code, you will see the SDK orchestrating the function
calls. The model first calls get_weather_forecast , receives the
temperature, and then calls set_thermostat_temperature with the correct
value based on the logic in the prompt.
Compositional function calling is a native Live
API feature. This means Live API
can handle the function calling similar to the Python SDK.
[LINK: Live
API](https://ai.google.dev/gemini-api/docs/live)

## Function calling modes

The Gemini API lets you control how the model uses the provided tools
(function declarations). Specifically, you can set the mode within
the. function_calling_config .
- AUTO (Default) : The model decides whether to generate a natural language
response or suggest a function call based on the prompt and context. This is the
most flexible mode and recommended for most scenarios.
- ANY : The model is constrained to always predict a function call and
guarantees function schema adherence. If allowed_function_names is not
specified, the model can choose from any of the provided function declarations.
If allowed_function_names is provided as a list, the model can only choose
from the functions in that list. Use this mode when you require a function
call response to every prompt (if applicable).
- NONE : The model is prohibited from making function calls. This is
equivalent to sending a request without any function declarations. Use this to
temporarily disable function calling without removing your tool definitions.
- VALIDATED (Preview): The model is constrained to predict either function
calls or natural language, and ensures function schema adherence. If allowed_function_names is not provided, the model picks from all of the
available function declarations. If allowed_function_names is provided, the
model picks from the set of allowed functions.
VALIDATED (Preview): The model is constrained to predict either function
calls or natural language, and ensures function schema adherence. If allowed_function_names is not provided, the model picks from all of the
available function declarations. If allowed_function_names is provided, the
model picks from the set of allowed functions.

## Automatic function calling (Python only)

When using the Python SDK, you can provide Python functions directly as tools.
The SDK converts these functions into declarations, manages the function call
execution, and handles the response cycle for you. Define your function with
type hints and a docstring. For optimal results, it is recommended to use Google-style docstrings. The SDK will then automatically:
[LINK: Google-style docstrings.](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
- Detect function call responses from the model.
- Call the corresponding Python function in your code.
- Send the function's response back to the model.
- Return the model's final text response.
The SDK currently does not parse argument descriptions into the property
description slots of the generated function declaration. Instead, it sends the
entire docstring as the top-level function description.
You can disable automatic function calling with:

### Automatic function schema declaration

The API is able to describe any of the following types. Pydantic types are
allowed, as long as the fields defined on them are also composed of allowed
types. Dict types (like dict[str: int] ) are not well supported here, don't
use them.
To see what the inferred schema looks like, you can convert it using from_callable :
[LINK: from_callable](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable)

## Multi-tool use: Combine native tools with function calling

You can enable multiple tools combining native tools with
function calling at the same time. Here's an example that enables two tools, Grounding with Google Search and code execution , in a request using the Live API .
[LINK: Grounding with Google Search](/gemini-api/docs/grounding)
[LINK: code execution](/gemini-api/docs/code-execution)
[LINK: Live API](/gemini-api/docs/live)
Python developers can try this out in the Live API Tool Use
notebook .
[LINK: Live API Tool Use
notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb)

## Multimodal function responses

For Gemini 3 series models, you can include multimodal content in
the function response parts that you send to the model. The model can process
this multimodal content in its next turn to produce a more informed response.
The following MIME types are supported for multimodal content in function
responses:
- Images : image/png , image/jpeg , image/webp
- Documents : application/pdf , text/plain
To include multimodal data in a function response, include it as one or more
parts nested within the functionResponse part. Each multimodal part must
contain inlineData . If you reference a multimodal part from
within the structured response field, it must contain a unique displayName .
You can also reference a multimodal part from within the structured response field of the functionResponse part by using the JSON reference format {"$ref": "<displayName>"} . The model substitutes the reference with the
multimodal content when processing the response. Each displayName can only be
referenced once in the structured response field.
The following example shows a message containing a functionResponse for a
function named get_image and a nested part containing image data with displayName: "instrument.jpg" . The functionResponse 's response field
references this image part:

## Function calling with Structured output

For Gemini 3 series models, you can use function calling with structured output . This lets the model predict function calls or outputs that adhere to a specific schema. As a result, you receive consistently formatted responses when the model doesn't generate function calls.
[LINK: structured output](/gemini-api/docs/structured-output)

## Model context protocol (MCP)

Model Context Protocol (MCP) is
an open standard for connecting AI applications with external tools and data.
MCP provides a common protocol for models to access context, such as functions
(tools), data sources (resources), or predefined prompts.
The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and
offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and
JavaScript client SDK can automatically execute the MCP tool and send the
response back to the model in a subsequent request, continuing this loop until
no more tool calls are made by the model.
[LINK: automatic tool calling](/gemini-api/docs/function-calling#automatic_function_calling_python_only)
Here, you can find an example of how to use a local MCP server with Gemini and mcp SDK.
Make sure the latest version of the mcp SDK is installed on
your platform of choice.
Make sure the latest version of the mcp SDK is installed on your platform
of choice.

### Limitations with built-in MCP support

Built-in MCP support is a experimental feature in our SDKs and has the following limitations:
[LINK: experimental](/gemini-api/docs/models#preview)
- Only tools are supported, not resources nor prompts
- It is available for the Python and JavaScript/TypeScript SDK.
- Breaking changes might occur in future releases.
Manual integration of MCP servers is always an option if these limit what you're
building.

## Supported models

This section lists models and their function calling capabilities. Experimental
models are not included. You can find a comprehensive capabilities overview on
the model overview page.
[LINK: model overview](https://ai.google.dev/gemini-api/docs/models)

## Best practices

- Function and Parameter Descriptions: Be extremely clear and specific in
your descriptions. The model relies on these to choose the correct function
and provide appropriate arguments.
- Naming: Use descriptive function names (without spaces, periods, or
dashes).
- Strong Typing: Use specific types (integer, string, enum) for parameters
to reduce errors. If a parameter has a limited set of valid values, use an
enum.
- Tool Selection: While the model can use an arbitrary number of tools,
providing too many can increase the risk of selecting an incorrect or
suboptimal tool. For best results, aim to provide only the relevant tools
for the context or task, ideally keeping the active set to a maximum of
10-20. Consider dynamic tool selection based on conversation context if you
have a large total number of tools.
- Prompt Engineering: Provide context: Tell the model its role (e.g., "You are a helpful
weather assistant."). Give instructions: Specify how and when to use functions (e.g., "Don't
guess dates; always use a future date for forecasts."). Encourage clarification: Instruct the model to ask clarifying questions
if needed. See Agentic workflows for further strategies on designing these prompts. Here is an example of a tested system instruction .
- Provide context: Tell the model its role (e.g., "You are a helpful
weather assistant.").
- Give instructions: Specify how and when to use functions (e.g., "Don't
guess dates; always use a future date for forecasts.").
- Encourage clarification: Instruct the model to ask clarifying questions
if needed.
- See Agentic workflows for further strategies on designing these prompts. Here is an example of a tested system instruction .
[LINK: Agentic workflows](/gemini-api/docs/prompting-strategies#agentic-workflows)
[LINK: system instruction](/gemini-api/docs/prompting-strategies#agentic-si-template)
- Temperature: Use a low temperature (e.g., 0) for more deterministic and
reliable function calls.
Temperature: Use a low temperature (e.g., 0) for more deterministic and
reliable function calls.
- Validation: If a function call has significant consequences (e.g.,
placing an order), validate the call with the user before executing it.
Validation: If a function call has significant consequences (e.g.,
placing an order), validate the call with the user before executing it.
- Check Finish Reason: Always check the finishReason in the model's response to handle cases where the model failed to generate a
valid function call.
Check Finish Reason: Always check the finishReason in the model's response to handle cases where the model failed to generate a
valid function call.
[LINK: finishReason](/api/generate-content#FinishReason)
- Error Handling : Implement robust error handling in your functions to
gracefully handle unexpected inputs or API failures. Return informative
error messages that the model can use to generate helpful responses to the
user.
Error Handling : Implement robust error handling in your functions to
gracefully handle unexpected inputs or API failures. Return informative
error messages that the model can use to generate helpful responses to the
user.
- Security: Be mindful of security when calling external APIs. Use
appropriate authentication and authorization mechanisms. Avoid exposing
sensitive data in function calls.
Security: Be mindful of security when calling external APIs. Use
appropriate authentication and authorization mechanisms. Avoid exposing
sensitive data in function calls.
- Token Limits: Function descriptions and parameters count towards your
input token limit. If you're hitting token limits, consider limiting the
number of functions or the length of the descriptions, break down complex
tasks into smaller, more focused function sets.
Token Limits: Function descriptions and parameters count towards your
input token limit. If you're hitting token limits, consider limiting the
number of functions or the length of the descriptions, break down complex
tasks into smaller, more focused function sets.

## Notes and limitations

- Only a subset of the OpenAPI
schema is supported.
[LINK: subset of the OpenAPI
schema](/api/caching#FunctionDeclaration)
- For ANY mode, the API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your function parameter and response schemas by shortening property names, reducing nesting, or limiting the number of function declarations.
- Supported parameter types in Python are limited.
- Automatic function calling is a Python SDK feature only.
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2026-01-23 UTC.

--------------------