# Dapr Workflows
**URL:** https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview
**Page Title:** Workflow overview | Dapr Docs
--------------------


## Workflow overview

Dapr workflow makes it easy for developers to write business logic and integrations in a reliable way.
Since Dapr workflows are stateful, they support long-running and fault-tolerant applications, ideal for orchestrating microservices.
Dapr workflow works seamlessly with other Dapr building blocks, such as service invocation, pub/sub, state management, and bindings.
The durable, resilient Dapr Workflow capability:
- Offers a built-in workflow runtime for driving Dapr Workflow execution.
- Provides SDKs for authoring workflows in code, using any language.
- Provides HTTP and gRPC APIs for managing workflows (start, query, pause/resume, raise event, terminate, purge).
Some example scenarios that Dapr Workflow can perform are:
- Order processing involving orchestration between inventory management, payment systems, and shipping services.
- HR onboarding workflows coordinating tasks across multiple departments and participants.
- Orchestrating the roll-out of digital menu updates in a national restaurant chain.
- Image processing workflows involving API-based classification and storage.

## Features

### Workflows and activities

With Dapr Workflow, you can write activities and then orchestrate those activities in a workflow.
Workflow activities are:
- The basic unit of work in a workflow
- Used for calling other (Dapr) services, interacting with state stores, and pub/sub brokers.
- Used for calling external third party services.
Learn more about workflow activities.
[LINK: Learn more about workflow activities.](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#%23workflow-activities)

### Child workflows

In addition to activities, you can write workflows to schedule other workflows as child workflows.
A child workflow has its own instance ID, history, and status that is independent of the parent workflow that started it, except for the fact that terminating the parent workflow terminates all of the child workflows created by it.
Child workflow also supports automatic retry policies.
Learn more about child workflows.
[LINK: Learn more about child workflows.](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#child-workflows)

### Multi-application workflows

Multi-application workflows, enable you to orchestrate complex business processes that span across multiple applications. This allows a workflow to call activities or start child workflows in different applications, distributing the workflow execution while maintaining the security, reliability and durability guarantees of Dapr’s workflow engine.
Learn more about multi-application workflows.
[LINK: Learn more about multi-application workflows.](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-multi-app/)

### Timers and reminders

Same as Dapr actors, you can schedule reminder-like durable delays for any time range.
Learn more about workflow timers and reminders
[LINK: Learn more about workflow timers](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/#durable-timers)
[LINK: reminders](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-architecture/#reminder-usage-and-execution-guarantees)

### Workflow HTTP calls to manage a workflow

When you create an application with workflow code and run it with Dapr, you can call specific workflows that reside in the application.
Each individual workflow can be:
- Started or terminated through a POST request
- Triggered to deliver a named event through a POST request
- Paused and then resumed through a POST request
- Purged from your state store through a POST request
- Queried for workflow status through a GET request
Learn more about how manage a workflow using HTTP calls.
[LINK: Learn more about how manage a workflow using HTTP calls.](https://docs.dapr.io/reference/api/workflow_api/)

## Workflow patterns

Dapr Workflow simplifies complex, stateful coordination requirements in microservice architectures.
The following sections describe several application patterns that can benefit from Dapr Workflow.
Learn more about different types of workflow patterns
[LINK: different types of workflow patterns](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-patterns/)

## Workflow SDKs

The Dapr Workflow authoring SDKs are language-specific SDKs that contain types and functions to implement workflow logic.
The workflow logic lives in your application and is orchestrated by the Dapr Workflow engine running in the Dapr sidecar via a gRPC stream.

### Supported SDKs

You can use the following SDKs to author a workflow.
[LINK: dapr-ext-workflow](https://github.com/dapr/python-sdk/tree/master/ext/dapr-ext-workflow)
[LINK: DaprWorkflowClient](https://github.com/dapr/js-sdk/blob/main/src/workflow/client/DaprWorkflowClient.ts)
[LINK: io.dapr.workflows](https://dapr.github.io/java-sdk/io/dapr/workflows/package-summary.html)
[LINK: workflow](https://github.com/dapr/go-sdk/tree/main/client/workflow.go)

## Try out workflows

### Quickstarts and tutorials

Want to put workflows to the test? Walk through the following quickstart and tutorials to see workflows in action:
[LINK: Workflow quickstart](https://docs.dapr.io/getting-started/quickstarts/workflow-quickstart/)
[LINK: Workflow Python SDK example](https://github.com/dapr/python-sdk/tree/master/examples/demo_workflow)
[LINK: Workflow JavaScript SDK example](https://github.com/dapr/js-sdk/tree/main/examples/workflow)
[LINK: Workflow .NET SDK example](https://github.com/dapr/dotnet-sdk/tree/master/examples/Workflow)
[LINK: Workflow Java SDK example](https://github.com/dapr/java-sdk/tree/master/examples/src/main/java/io/dapr/examples/workflows)
[LINK: Workflow Go SDK example](https://github.com/dapr/go-sdk/tree/main/examples/workflow/README.md)

### Start using workflows directly in your app

Want to skip the quickstarts? Not a problem. You can try out the workflow building block directly in your application. After Dapr is installed , you can begin using workflows, starting with how to author a workflow .
[LINK: Dapr is installed](https://docs.dapr.io/getting-started/install-dapr-cli/)
[LINK: how to author a workflow](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-author-workflow/)

## Managing Workflows

Dapr provides comprehensive workflow management capabilities through both the HTTP API and the CLI.

### Workflow Lifecycle Operations

Start Workflows
Monitor Workflows
Control Workflows
Maintenance Operations
See How-To: Manage workflows for detailed instructions.
[LINK: How-To: Manage workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/howto-manage-workflow/)

## Limitations

- State stores: You can only use state stores which support workflows, as described here .
[LINK: described here](https://docs.dapr.io/reference/components-reference/supported-state-stores/)
- Azure Cosmos DB has payload and workflow complexity limitations .
[LINK: payload and workflow complexity limitations](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-azure-cosmosdb/#workflow-limitations)
- AWS DynamoDB has workflow complexity limitations .
[LINK: workflow complexity limitations](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-azure-cosmosdb/#workflow-limitations)

## Watch the demo

Watch this video for an overview on Dapr Workflow :

## Next steps

[LINK: Workflow features and concepts >>](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-features-concepts/)

## Related links

- Workflow API reference
[LINK: Workflow API reference](https://docs.dapr.io/reference/api/workflow_api/)
- Try out the full SDK examples: Python example JavaScript example .NET example Java example Go example
- Python example
[LINK: Python example](https://github.com/dapr/python-sdk/tree/master/examples/demo_workflow)
- JavaScript example
[LINK: JavaScript example](https://github.com/dapr/js-sdk/tree/main/examples/workflow)
- .NET example
[LINK: .NET example](https://github.com/dapr/dotnet-sdk/tree/master/examples/Workflow)
- Java example
[LINK: Java example](https://github.com/dapr/java-sdk/tree/master/examples/src/main/java/io/dapr/examples/workflows)
- Go example
[LINK: Go example](https://github.com/dapr/go-sdk/tree/main/examples/workflow/README.md)
[LINK: docs: document durable agent retry policy (#4982) (e60c52d)](https://github.com/dapr/docs/commit/e60c52d465190aa3ff35c81bb54289ae884704e9)

--------------------