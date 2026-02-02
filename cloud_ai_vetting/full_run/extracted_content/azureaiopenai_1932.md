# Azure.AI.OpenAI
**URL:** https://www.nuget.org/packages/Azure.AI.OpenAI
**Page Title:** NuGet Gallery | Azure.AI.OpenAI 2.1.0
--------------------


## Azure. AI. OpenAI 2.1.0

[LINK: Prefix Reserved](https://docs.microsoft.com/nuget/nuget-org/id-prefix-reservation)
- .NET CLI
- PMC
- PackageReference
- CPM
- Paket CLI
- Script & Interactive
- File-based Apps
- Cake
[LINK: Install-Package](https://docs.microsoft.com/nuget/reference/ps-reference/ps-ref-install-package)
[LINK: PackageReference](https://docs.microsoft.com/nuget/consume-packages/package-references-in-project-files)
[LINK: maintainers](https://fsprojects.github.io/Paket/contact.html)
- README
- Frameworks
- Dependencies
- Used By
- Versions
- Release Notes

## Azure OpenAI client library for .NET

The Azure OpenAI client library for .NET is a companion to the official OpenAI client library for .NET . The Azure OpenAI library configures a client for use with Azure OpenAI and provides additional strongly typed extension support for request and response models specific to Azure OpenAI scenarios.
[LINK: OpenAI client library for .NET](https://github.com/openai/openai-dotnet)
Azure OpenAI is a managed service that allows developers to deploy, tune, and generate content from OpenAI models on Azure resources.
Source code | Package (NuGet) | API reference documentation | Product documentation | Samples
[LINK: Source code](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/src)
[LINK: Samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/tests/Samples)

### Getting started

To use an Azure OpenAI resource, you must have:
- An Azure subscription
- Azure OpenAI access
These prerequisites allow you to create an Azure OpenAI resource and get both a connection URL and API keys. For more information, see Quickstart: Get started generating text using Azure OpenAI Service .
Install the client library for .NET with NuGet :
The Azure.AI.OpenAI package builds on the official OpenAI package , which is included as a dependency.
To interact with Azure OpenAI or OpenAI, create an instance of AzureOpenAIClient with one of the following approaches:
[LINK: AzureOpenAIClient](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/src/Custom/AzureOpenAIClient.cs)
- Create client with a Microsoft Entra credential (Recommended)
- Create client with an API key
[LINK: Create client with an API key](#create-client-with-an-api-key)
A secure, keyless authentication approach is to use Microsoft Entra ID (formerly Azure Active Directory) via the Azure Identity library . To use the library:
[LINK: Azure Identity library](https://learn.microsoft.com/dotnet/api/overview/azure/identity-readme?view=azure-dotnet)
- Install the Azure.Identity package : dotnet add package Azure.Identity
Install the Azure.Identity package :
- Use the desired credential type from the library. For example, DefaultAzureCredential :
Use the desired credential type from the library. For example, DefaultAzureCredential :
[LINK: DefaultAzureCredential](https://learn.microsoft.com/dotnet/api/azure.identity.defaultazurecredential?view=azure-dotnet)
If your Microsoft Entra credentials are issued by an entity other than Azure Public Cloud, you can set the Audience property on OpenAIClientOptions to modify the token authorization scope used for requests.
For example, the following will configure the client to authenticate tokens via Azure Government Cloud, using https://cognitiveservices.azure.us/.default as the authorization scope:
For a custom or non-enumerated value, the authorization scope can be provided directly as the value for Audience :
While not as secure as Microsoft Entra-based authentication , it's possible to authenticate using a client subscription key:

### Key concepts

See OpenAI's Assistants API overview .
[LINK: OpenAI's Assistants API overview](https://platform.openai.com/docs/assistants/overview)
See OpenAI Capabilities: Speech to text .
[LINK: OpenAI Capabilities: Speech to text](https://platform.openai.com/docs/guides/speech-to-text/speech-to-text)
See OpenAI's Batch API guide .
[LINK: OpenAI's Batch API guide](https://platform.openai.com/docs/guides/batch)
Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is
designed to make multi-turn conversations easy, it's also useful for single-turn tasks without any conversation.
See OpenAI Capabilities: Chat completion .
[LINK: OpenAI Capabilities: Chat completion](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)
See OpenAI Capabilities: Image generation .
[LINK: OpenAI Capabilities: Image generation](https://platform.openai.com/docs/guides/images/introduction)
See OpenAI's Files API reference .
[LINK: OpenAI's Files API reference](https://platform.openai.com/docs/api-reference/files)
See OpenAI Capabilities: Embeddings .
[LINK: OpenAI Capabilities: Embeddings](https://platform.openai.com/docs/guides/embeddings/embeddings)
We guarantee that all client instance methods are thread-safe and independent of each other ( guideline ). This ensures that the recommendation of reusing client instances is always safe, even across threads.
[LINK: guideline](https://azure.github.io/azure-sdk/dotnet_introduction.html#dotnet-service-methods-thread-safety)
Client options | Accessing the response | Long-running operations | Handling failures | Diagnostics | Mocking | Client lifetime
[LINK: Client options](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/README.md#configuring-service-clients-using-clientoptions)
[LINK: Accessing the response](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/README.md#accessing-http-response-details-using-responset)
[LINK: Long-running operations](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/README.md#consuming-long-running-operations-using-operationt)
[LINK: Handling failures](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/README.md#reporting-errors-requestfailedexception)
[LINK: Diagnostics](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/core/Azure.Core/samples/Diagnostics.md)

### Examples

You can familiarize yourself with different APIs using Samples from OpenAI's .NET library or Azure.AI.OpenAI-specific samples . Most OpenAI capabilities are available on both Azure OpenAI and OpenAI using the same scenario clients and methods, so not all scenarios are redundantly covered here.
[LINK: Samples from OpenAI's .NET library](https://github.com/openai/openai-dotnet/tree/main/examples)
[LINK: Azure.AI.OpenAI-specific samples](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/openai/Azure.AI.OpenAI/tests/Samples)
Streaming chat completions use the CompleteChatStreaming and CompleteChatStreamingAsync method, which return a ResultCollection<StreamingChatCompletionUpdate> or AsyncCollectionResult<StreamingChatCompletionUpdate> instead of a ClientResult<ChatCompletion> . These result collections can be iterated over using foreach or await foreach , with each update arriving as new data is available from the streamed response.
Tools extend chat completions by allowing an assistant to invoke defined functions and other capabilities in the
process of fulfilling a chat completions request. To use chat tools, start by defining a function tool. Here, we root the tools in local methods for clarity and convenience:
With the tool defined, include that new definition in the options for a chat completions request:
When the assistant decides that one or more tools should be used, the response message includes one or more "tool
calls" that must all be resolved via "tool messages" on the subsequent request. This resolution of tool calls into
new request messages can be thought of as a sort of "callback" for chat completions.
To provide tool call resolutions to the assistant to allow the request to continue, provide all prior historical
context -- including the original system and user messages, the response from the assistant that included the tool
calls, and the tool messages that resolved each of those tools -- when making a subsequent request.
When using tool calls with streaming responses, accumulate tool call details much like you'd accumulate the other
portions of streamed choices, in this case using the accumulated StreamingToolCallUpdate data to instantiate new
tool call messages for assistant message history. Note that the model will ignore ChoiceCount when providing tools
and that all streamed responses should map to a single, common choice index in the range of [0..(ChoiceCount - 1)] .
The use your own data feature is unique to Azure OpenAI and won't work with a client configured to use the non-Azure service.
See the Azure OpenAI using your own data quickstart for conceptual background and detailed setup instructions.
NOTE: The concurrent use of Chat Functions and Azure Chat Extensions on a single request isn't yet supported. Supplying both will result in the Chat Functions information being ignored and the operation behaving as if only the Azure Chat Extensions were provided. To address this limitation, consider separating the evaluation of Chat Functions and Azure Chat Extensions across multiple requests in your solution design.
Assistants provide a stateful, service-persisted conversational
model that can be enriched with a larger array of tools than Chat Completions.
[LINK: Assistants](https://platform.openai.com/docs/assistants/overview)
Creating an AssistantClient is similar to other scenario clients. An important difference is that Assistants features
are marked as [Experimental] to reflect the API's beta status, and thus you'll need to suppress the corresponding
warning to instantiate a client. This can be done in the .csproj file via the <NoWarn> element or, as below, in
the code itself with a #pragma directive.
With a client, you can then create Assistants, Threads, and new Messages on a thread in preparation to start a run. As is the case for other shared API surfaces, you should use an Azure OpenAI model deployment name wherever a model name is requested.
You can then start a run and stream updates as they arrive using the Streaming method variants, handling the updates
you're interested in using the enumerated kind of event it is and/or one of the several derived types for the streaming
update class, as shown here for content:
Remember that things like Assistants, Threads, and Vector Stores are persistent resources. You can save their IDs to
reuse them later or, as demonstrated below, delete them when no longer desired.

### Next steps

### Troubleshooting

When you interact with Azure OpenAI using the .NET SDK, errors returned by the service correspond to the same HTTP status codes returned for REST API requests.
For example, if you try to create a client using an endpoint that doesn't match your Azure OpenAI Resource endpoint, a 404 error is returned, indicating Resource Not Found .

### Contributing

See the OpenAI CONTRIBUTING.md for details on building, testing, and contributing to this library.
[LINK: OpenAI CONTRIBUTING.md](https://github.com/Azure/azure-sdk-for-net/blob/main/CONTRIBUTING.md)
This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit cla.microsoft.com .
When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.
This project has adopted the Microsoft Open Source Code of Conduct . For more information, see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.
[LINK: Target Frameworks](https://docs.microsoft.com/dotnet/standard/frameworks)
[LINK: .NET Standard](https://docs.microsoft.com/dotnet/standard/net-standard)
- .NETStandard 2.0 Azure.Core (>= 1.44.1) OpenAI (>= 2.1.0)
- Azure.Core (>= 1.44.1)
- OpenAI (>= 2.1.0)

### NuGet packages (121)

Showing the top 5 NuGet packages that depend on Azure.AI.OpenAI:
Package Description
Semantic Kernel connectors for Azure OpenAI. Contains clients for chat completion, embedding and DALL-E text to image.
ASP.NET Core based CMS
Defines a concrete Agent based on the OpenAI Assistant API.
A client for Azure OpenAI that integrates with Aspire, including logging and telemetry.

### GitHub repositories (50)

Showing the top 20 popular GitHub repositories that depend on Azure.AI.OpenAI:
[LINK: microsoft/PowerToys](https://github.com/microsoft/PowerToys)
[LINK: microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)
[LINK: dotnet/aspire](https://github.com/dotnet/aspire)
[LINK: sourcegit-scm/sourcegit](https://github.com/sourcegit-scm/sourcegit)
[LINK: dotnet/maui-samples](https://github.com/dotnet/maui-samples)
[LINK: Azure-Samples/cognitive-services-speech-sdk](https://github.com/Azure-Samples/cognitive-services-speech-sdk)
[LINK: dotnet/extensions](https://github.com/dotnet/extensions)
[LINK: SciSharp/BotSharp](https://github.com/SciSharp/BotSharp)
[LINK: microsoft/Generative-AI-for-beginners-dotnet](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
[LINK: OfficeDev/Microsoft-Teams-Samples](https://github.com/OfficeDev/Microsoft-Teams-Samples)
[LINK: Azure-Samples/Cognitive-Speech-TTS](https://github.com/Azure-Samples/Cognitive-Speech-TTS)
[LINK: CodeMazeBlog/CodeMazeGuides](https://github.com/CodeMazeBlog/CodeMazeGuides)
[LINK: dotnet/ai-samples](https://github.com/dotnet/ai-samples)
[LINK: Azure-Samples/azure-search-openai-demo-csharp](https://github.com/Azure-Samples/azure-search-openai-demo-csharp)
[LINK: microsoft/psi](https://github.com/microsoft/psi)
[LINK: PowerShell/AIShell](https://github.com/PowerShell/AIShell)
[LINK: dotnet/smartcomponents](https://github.com/dotnet/smartcomponents)
[LINK: Avanade/Liquid-Application-Framework](https://github.com/Avanade/Liquid-Application-Framework)
[LINK: VedAstro/VedAstro](https://github.com/VedAstro/VedAstro)
[LINK: DevExpress/Blazor](https://github.com/DevExpress/Blazor)
https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.OpenAI_2.1.0/sdk/openai/Azure.AI.OpenAI/CHANGELOG.md
[LINK: https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.OpenAI_2.1.0/sdk/openai/Azure.AI.OpenAI/CHANGELOG.md](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.OpenAI_2.1.0/sdk/openai/Azure.AI.OpenAI/CHANGELOG.md)

--------------------