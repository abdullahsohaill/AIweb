# Spring AI Documentation
**URL:** https://spring.io/projects/spring-ai
**Page Title:** Spring AI
--------------------


## Spring AI 1.1.2

- Overview
- Learn
- Support
Spring AI is an application framework for AI engineering.
Its goal is to apply to the AI domain Spring ecosystem design principles such as portability and modular design and promote using POJOs as the building blocks of an application to the AI domain.
At its core, Spring AI addresses the fundamental challenge of AI integration: Connecting your enterprise Data and APIs with the AI Models .

## Features

Spring AI provides the following features:
- Support for all major AI Model providers such as Anthropic, OpenAI, Microsoft, Amazon, Google, and Ollama. Supported model types include: Chat Completion Embedding Text to Image Audio Transcription Text to Speech Moderation
[LINK: AI Model providers](https://docs.spring.io/spring-ai/reference/api/index.html)
- Chat Completion
[LINK: Chat Completion](https://docs.spring.io/spring-ai/reference/api/chatmodel.html)
- Embedding
[LINK: Embedding](https://docs.spring.io/spring-ai/reference/api/embeddings.html)
- Text to Image
[LINK: Text to Image](https://docs.spring.io/spring-ai/reference/api/imageclient.html)
- Audio Transcription
[LINK: Audio Transcription](https://docs.spring.io/spring-ai/reference/api/audio/transcriptions.html)
- Text to Speech
[LINK: Text to Speech](https://docs.spring.io/spring-ai/reference/api/audio/speech.html)
- Moderation
[LINK: Moderation](https://docs.spring.io/spring-ai/reference/api/index.html#api/moderation)
- Portable API support across AI providers for both synchronous and streaming API options are supported. Access to model-specific features is also available.
[LINK: model-specific features](https://docs.spring.io/spring-ai/reference/api/chatmodel.html#_chat_options)
- Structured Outputs - Mapping of AI Model output to POJOs.
[LINK: Structured Outputs](https://docs.spring.io/spring-ai/reference/api/structured-output-converter.html)
- Support for all major Vector Database providers such as Apache Cassandra, Azure Vector Search, Chroma, Milvus, MongoDB Atlas, Neo4j, Oracle, PostgreSQL/PGVector, PineCone, Qdrant, Redis, and Weaviate .
[LINK: Vector Database providers](https://docs.spring.io/spring-ai/reference/api/vectordbs.html)
- Portable API across Vector Store providers, including a novel SQL-like metadata filter API .
[LINK: metadata filter API](https://docs.spring.io/spring-ai/reference/api/vectordbs.html#metadata-filters)
- Tools/Function Calling - permits the model to request the execution of client-side tools and functions, thereby accessing necessary real-time information as required.
[LINK: Tools/Function Calling](https://docs.spring.io/spring-ai/reference/api/functions.html)
- Observability - Provides insights into AI-related operations.
[LINK: Observability](https://docs.spring.io/spring-ai/reference/observability/index.html)
- Document injection ETL framework for Data Engineering.
[LINK: ETL framework](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html)
- AI Model Evaluation - Utilities to help evaluate generated content and protect against hallucinated response.
[LINK: AI Model Evaluation](https://docs.spring.io/spring-ai/reference/api/testing.html)
- ChatClient API - Fluent API for communicating with AI Chat Models, idiomatically similar to the WebClient and RestClient APIs.
[LINK: ChatClient API](https://docs.spring.io/spring-ai/reference/api/chatclient.html)
- Advisors API - Encapsulates recurring Generative AI patterns, transforms data sent to and from Language Models (LLMs), and provides portability across various models and use cases.
[LINK: Advisors API](https://docs.spring.io/spring-ai/reference/api/advisors.html)
- Support for Chat Conversation Memory and Retrieval Augmented Generation (RAG) .
[LINK: Chat Conversation Memory](https://docs.spring.io/spring-ai/reference/api/chatclient.html#_chat_memory)
[LINK: Retrieval Augmented Generation (RAG)](https://docs.spring.io/spring-ai/reference/api/chatclient.html#_retrieval_augmented_generation)
- Spring Boot Auto Configuration and Starters for all AI Models and Vector Stores - use the start.spring.io to select the Model or Vector-store of choice.
This feature set lets you implement common use cases such as " Q&A over your documentation " or " Chat with your documentation. "

## Documentation

Extensive reference documentation , sample applications, and workshop/course material.
[LINK: reference documentation](https://docs.spring.io/spring-ai/reference/index.html)

## Getting Started

You can get started in a few simple steps:
- Create a Spring Boot Web application with a Spring AI OpenAI boot starter dependency. This Spring Initializr link can help you bootstrap the application.
( With start.spring.io you can select any AI Models or Vector Stores that you want to use in your new applications ).
Create a Spring Boot Web application with a Spring AI OpenAI boot starter dependency. This Spring Initializr link can help you bootstrap the application.
( With start.spring.io you can select any AI Models or Vector Stores that you want to use in your new applications ).
- Add your OpenAI key to the application.properties : spring.ai.openai.api-key= < YOUR OPENAI KEY >
Add your OpenAI key to the application.properties :
- Add the following snippet to your SpringAiDemoApplication class: @Bean public CommandLineRunner runner (ChatClient.Builder builder) { return args -> {
        ChatClient chatClient = builder.build();
        String response = chatClient.prompt( "Tell me a joke" ).call().content();							
        System.out.println(response);
    };
}
Add the following snippet to your SpringAiDemoApplication class:
- Run the application: ./mvnw spring-boot:run
Run the application:
Want to get started in another way?  View the Getting Started section in the reference documentation.
[LINK: Getting Started section](https://docs.spring.io/spring-ai/reference/getting-started.html)

## Quickstart Your Project

Bootstrap your application with Spring Initializr .

## Get ahead

VMware offers training and certification to turbo-charge your progress.

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

## Upcoming events

Check out all the upcoming events in the Spring community.

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