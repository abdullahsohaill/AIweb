# Effective Agents patterns from Spring AI
**URL:** https://docs.spring.io/spring-ai/reference/api/effective-agents.html
**Page Title:** Building Effective Agents :: Spring AI Reference
--------------------


## Building Effective Agents

In a recent research publication, Building Effective Agents , Anthropic shared valuable insights about building effective Large Language Model (LLM) agents. What makes this research particularly interesting is its emphasis on simplicity and composability over complex frameworks. Let’s explore how these principles translate into practical implementations using Spring AI .
[LINK: Spring AI](https://docs.spring.io/spring-ai/reference/index.html)
While the pattern descriptions and diagrams are sourced from Anthropic’s original publication, we’ll focus on how to implement these patterns using Spring AI’s features for model portability and structured output. We recommend reading the original paper first.
The agentic-patterns directory in the spring-ai-examples repository contains all the code for the examples that follow.
[LINK: agentic-patterns](https://github.com/spring-projects/spring-ai-examples/tree/main/agentic-patterns)

## Agentic Systems

The research publication makes an important architectural distinction between two types of agentic systems:
- Workflows : Systems where LLMs and tools are orchestrated through predefined code paths (e.g., prescriptive systems)
Workflows : Systems where LLMs and tools are orchestrated through predefined code paths (e.g., prescriptive systems)
- Agents : Systems where LLMs dynamically direct their own processes and tool usage
Agents : Systems where LLMs dynamically direct their own processes and tool usage
The key insight is that while fully autonomous agents might seem appealing, workflows often provide better predictability and consistency for well-defined tasks. This aligns perfectly with enterprise requirements where reliability and maintainability are crucial.
Let’s examine how Spring AI implements these concepts through five fundamental patterns, each serving specific use cases:

### 1. Chain Workflow

[LINK: Chain Workflow](https://github.com/spring-projects/spring-ai-examples/tree/main/agentic-patterns/chain-workflow)
The Chain Workflow pattern exemplifies the principle of breaking down complex tasks into simpler, more manageable steps.
When to Use: - Tasks with clear sequential steps
- When you want to trade latency for higher accuracy
- When each step builds on the previous step’s output
Here’s a practical example from Spring AI’s implementation:
This implementation demonstrates several key principles:
- Each step has a focused responsibility
Each step has a focused responsibility
- Output from one step becomes input for the next
Output from one step becomes input for the next
- The chain is easily extensible and maintainable
The chain is easily extensible and maintainable

### 2. Parallelization Workflow

[LINK: Parallelization Workflow](https://github.com/spring-projects/spring-ai-examples/tree/main/agentic-patterns/parallelization-workflow)
LLMs can work simultaneously on tasks and have their outputs aggregated programmatically.
When to Use: - Processing large volumes of similar but independent items
- Tasks requiring multiple independent perspectives
- When processing time is critical and tasks are parallelizable

### 3. Routing Workflow

[LINK: Routing Workflow](https://github.com/spring-projects/spring-ai-examples/tree/main/agentic-patterns/routing-workflow)
The Routing pattern implements intelligent task distribution, enabling specialized handling for different types of input.
When to Use: - Complex tasks with distinct categories of input
- When different inputs require specialized processing
- When classification can be handled accurately

### 4. Orchestrator-Workers

[LINK: Orchestrator-Workers](https://github.com/spring-projects/spring-ai-examples/tree/main/agentic-patterns/orchestrator-workers)
When to Use: - Complex tasks where subtasks can’t be predicted upfront
- Tasks requiring different approaches or perspectives
- Situations needing adaptive problem-solving
Usage Example:

### 5. Evaluator-Optimizer

[LINK: Evaluator-Optimizer](https://github.com/spring-projects/spring-ai-examples/tree/main/agentic-patterns/evaluator-optimizer)
When to Use: - Clear evaluation criteria exist
- Iterative refinement provides measurable value
- Tasks benefit from multiple rounds of critique
Usage Example:

## Spring AI’s Implementation Advantages

Spring AI’s implementation of these patterns offers several benefits that align with Anthropic’s recommendations:

### Model Portability

[LINK: Model Portability](https://docs.spring.io/spring-ai/reference/api/chat/comparison.html)

### Structured Output

[LINK: Structured Output](https://docs.spring.io/spring-ai/reference/api/structured-output-converter.html)

### Consistent API

[LINK: Consistent API](https://docs.spring.io/spring-ai/reference/api/chatclient.html)
- Uniform interface across different LLM providers
Uniform interface across different LLM providers
- Built-in error handling and retries
Built-in error handling and retries
- Flexible prompt management
Flexible prompt management

## Best Practices and Recommendations

- Start Simple
Start Simple
- Begin with basic workflows before adding complexity
Begin with basic workflows before adding complexity
- Use the simplest pattern that meets your requirements
Use the simplest pattern that meets your requirements
- Add sophistication only when needed
Add sophistication only when needed
- Design for Reliability
Design for Reliability
- Implement clear error handling
Implement clear error handling
- Use type-safe responses where possible
Use type-safe responses where possible
- Build in validation at each step
Build in validation at each step
- Consider Trade-offs
Consider Trade-offs
- Balance latency vs. accuracy
Balance latency vs. accuracy
- Evaluate when to use parallel processing
Evaluate when to use parallel processing
- Choose between fixed workflows and dynamic agents
Choose between fixed workflows and dynamic agents

## Future Work

These guides will be updated to explore how to build more advanced Agents that combine these foundational patterns with sophisticated features:
Pattern Composition - Combining multiple patterns to create more powerful workflows
- Building hybrid systems that leverage the strengths of each pattern
- Creating flexible architectures that can adapt to changing requirements
Advanced Agent Memory Management - Implementing persistent memory across conversations
- Managing context windows efficiently
- Developing strategies for long-term knowledge retention
Tools and Model-Context Protocol (MCP) Integration - Leveraging external tools through standardized interfaces
- Implementing MCP for enhanced model interactions
- Building extensible agent architectures

## Conclusion

The combination of Anthropic’s research insights and Spring AI’s practical implementations provides a powerful framework for building effective LLM-based systems.
By following these patterns and principles, developers can create robust, maintainable, and effective AI applications that deliver real value while avoiding unnecessary complexity.
The key is to remember that sometimes the simplest solution is the most effective. Start with basic patterns, understand your use case thoroughly, and only add complexity when it demonstrably improves your system’s performance or capabilities.
- Spring AI 1.1.2 1.0.3 2.0.0-M2 2.0.0-SNAPSHOT 1.1.3-SNAPSHOT
- 1.1.2
- 1.0.3
- 2.0.0-M2
- 2.0.0-SNAPSHOT
- 1.1.3-SNAPSHOT
- Related Spring Documentation Spring Boot Spring Framework Spring Cloud Spring Cloud Build Spring Cloud Bus Spring Cloud Circuit Breaker Spring Cloud Commons Spring Cloud Config Spring Cloud Consul Spring Cloud Contract Spring Cloud Function Spring Cloud Gateway Spring Cloud Kubernetes Spring Cloud Netflix Spring Cloud OpenFeign Spring Cloud Stream Spring Cloud Task Spring Cloud Vault Spring Cloud Zookeeper Spring Data Spring Data Cassandra Spring Data Commons Spring Data Couchbase Spring Data Elasticsearch Spring Data JPA Spring Data KeyValue Spring Data LDAP Spring Data MongoDB Spring Data Neo4j Spring Data Redis Spring Data JDBC & R2DBC Spring Data REST Spring Integration Spring Batch Spring Security Spring Authorization Server Spring LDAP Spring Security Kerberos Spring Session Spring Vault Spring AI Spring AMQP Spring CLI Spring GraphQL Spring for Apache Kafka Spring Modulith Spring for Apache Pulsar Spring Shell
- Spring Boot
[LINK: Spring Boot](https://docs.spring.io/spring-boot/)
- Spring Framework
[LINK: Spring Framework](https://docs.spring.io/spring-framework/reference/)
- Spring Cloud Spring Cloud Build Spring Cloud Bus Spring Cloud Circuit Breaker Spring Cloud Commons Spring Cloud Config Spring Cloud Consul Spring Cloud Contract Spring Cloud Function Spring Cloud Gateway Spring Cloud Kubernetes Spring Cloud Netflix Spring Cloud OpenFeign Spring Cloud Stream Spring Cloud Task Spring Cloud Vault Spring Cloud Zookeeper
- Spring Cloud Build
[LINK: Spring Cloud Build](https://docs.spring.io/spring-cloud-build/reference/)
- Spring Cloud Bus
[LINK: Spring Cloud Bus](https://docs.spring.io/spring-cloud-bus/reference/)
- Spring Cloud Circuit Breaker
[LINK: Spring Cloud Circuit Breaker](https://docs.spring.io/spring-cloud-circuitbreaker/reference/)
- Spring Cloud Commons
[LINK: Spring Cloud Commons](https://docs.spring.io/spring-cloud-commons/reference/)
- Spring Cloud Config
[LINK: Spring Cloud Config](https://docs.spring.io/spring-cloud-config/reference/)
- Spring Cloud Consul
[LINK: Spring Cloud Consul](https://docs.spring.io/spring-cloud-consul/reference/)
- Spring Cloud Contract
[LINK: Spring Cloud Contract](https://docs.spring.io/spring-cloud-contract/reference/)
- Spring Cloud Function
[LINK: Spring Cloud Function](https://docs.spring.io/spring-cloud-function/reference/)
- Spring Cloud Gateway
[LINK: Spring Cloud Gateway](https://docs.spring.io/spring-cloud-gateway/reference/)
- Spring Cloud Kubernetes
[LINK: Spring Cloud Kubernetes](https://docs.spring.io/spring-cloud-kubernetes/reference/)
- Spring Cloud Netflix
[LINK: Spring Cloud Netflix](https://docs.spring.io/spring-cloud-netflix/reference/)
- Spring Cloud OpenFeign
[LINK: Spring Cloud OpenFeign](https://docs.spring.io/spring-cloud-openfeign/reference/)
- Spring Cloud Stream
[LINK: Spring Cloud Stream](https://docs.spring.io/spring-cloud-stream/reference/)
- Spring Cloud Task
[LINK: Spring Cloud Task](https://docs.spring.io/spring-cloud-task/reference/)
- Spring Cloud Vault
[LINK: Spring Cloud Vault](https://docs.spring.io/spring-cloud-vault/reference/)
- Spring Cloud Zookeeper
[LINK: Spring Cloud Zookeeper](https://docs.spring.io/spring-cloud-zookeeper/reference/)
- Spring Data Spring Data Cassandra Spring Data Commons Spring Data Couchbase Spring Data Elasticsearch Spring Data JPA Spring Data KeyValue Spring Data LDAP Spring Data MongoDB Spring Data Neo4j Spring Data Redis Spring Data JDBC & R2DBC Spring Data REST
- Spring Data Cassandra
[LINK: Spring Data Cassandra](https://docs.spring.io/spring-data/cassandra/reference/)
- Spring Data Commons
[LINK: Spring Data Commons](https://docs.spring.io/spring-data/commons/reference/)
- Spring Data Couchbase
[LINK: Spring Data Couchbase](https://docs.spring.io/spring-data/couchbase/reference/)
- Spring Data Elasticsearch
[LINK: Spring Data Elasticsearch](https://docs.spring.io/spring-data/elasticsearch/reference/)
- Spring Data JPA
[LINK: Spring Data JPA](https://docs.spring.io/spring-data/jpa/reference/)
- Spring Data KeyValue
[LINK: Spring Data KeyValue](https://docs.spring.io/spring-data/keyvalue/reference/)
- Spring Data LDAP
[LINK: Spring Data LDAP](https://docs.spring.io/spring-data/ldap/reference/)
- Spring Data MongoDB
[LINK: Spring Data MongoDB](https://docs.spring.io/spring-data/mongodb/reference/)
- Spring Data Neo4j
[LINK: Spring Data Neo4j](https://docs.spring.io/spring-data/neo4j/reference/)
- Spring Data Redis
[LINK: Spring Data Redis](https://docs.spring.io/spring-data/redis/reference/)
- Spring Data JDBC & R2DBC
[LINK: Spring Data JDBC & R2DBC](https://docs.spring.io/spring-data/relational/reference/)
- Spring Data REST
[LINK: Spring Data REST](https://docs.spring.io/spring-data/rest/reference/)
- Spring Integration
[LINK: Spring Integration](https://docs.spring.io/spring-integration/reference/)
- Spring Batch
[LINK: Spring Batch](https://docs.spring.io/spring-batch/reference/)
- Spring Security Spring Authorization Server Spring LDAP Spring Security Kerberos Spring Session Spring Vault
[LINK: Spring Security](https://docs.spring.io/spring-security/reference/)
- Spring Authorization Server
[LINK: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
- Spring LDAP
[LINK: Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
- Spring Security Kerberos
[LINK: Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
- Spring Session
[LINK: Spring Session](https://docs.spring.io/spring-session/reference/)
- Spring Vault
[LINK: Spring Vault](https://docs.spring.io/spring-vault/reference/)
- Spring AI
[LINK: Spring AI](https://docs.spring.io/spring-ai/reference/)
- Spring AMQP
[LINK: Spring AMQP](https://docs.spring.io/spring-amqp/reference/)
- Spring CLI
[LINK: Spring CLI](https://docs.spring.io/spring-cli/reference/)
- Spring GraphQL
[LINK: Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)
- Spring for Apache Kafka
[LINK: Spring for Apache Kafka](https://docs.spring.io/spring-kafka/reference/)
- Spring Modulith
[LINK: Spring Modulith](https://docs.spring.io/spring-modulith/reference/)
- Spring for Apache Pulsar
[LINK: Spring for Apache Pulsar](https://docs.spring.io/spring-pulsar/reference/)
- Spring Shell
[LINK: Spring Shell](https://docs.spring.io/spring-shell/reference/)

## Cookies

## Privacy Preference Center

## Privacy Preference Center

- Your Privacy

### Your Privacy

- Strictly Necessary Cookies

### Strictly Necessary Cookies

- Performance Cookies

### Performance Cookies

- Targeting Cookies

### Targeting Cookies

When you interact with Broadcom as set forth in the Privacy Policy through visiting any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Cookie Policy Privacy Policy
These cookies are necessary for the website to function and cannot be switched off in Broadcom’s systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
These cookies allow Broadcom to count visits and traffic sources so Broadcom can measure and improve the performance of its site. They help Broadcom to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies Broadcom will not know when you have visited our site and will not be able to monitor its performance.
These cookies may be set through Broadcom’s site by its advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List

- checkbox label label

--------------------