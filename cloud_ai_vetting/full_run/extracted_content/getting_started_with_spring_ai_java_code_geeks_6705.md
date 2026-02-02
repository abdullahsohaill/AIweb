# Getting Started with Spring AI (Java Code Geeks)
**URL:** https://www.javacodegeeks.com/2024/09/getting-started-with-spring-ai.html
**Page Title:** Getting Started with Spring AI - Java Code Geeks
--------------------

Integrating artificial intelligence (AI) into applications is becoming necessary for businesses looking to stay ahead. The Spring Framework in the Java ecosystem brings AI capabilities to the forefront with Spring AI. Spring AI aims to make it easier to develop applications with built-in artificial intelligence features, without unnecessary complexity. It provides a set of core building blocks that simplify the creation of AI applications.
[LINK: artificial intelligence](https://www.javacodegeeks.com/2019/06/artificial-intelligence-tools-developers.html)
These building blocks are flexible, allowing us to switch between different components with minimal effort. For instance, Spring AI includes a ChatClient interface that can be implemented for various AI services, like OpenAI, making it easy to swap out one service for another with minimal code changes. This Spring AI tutorial is designed to guide developers through integrating AI and machine learning features into their Spring-based applications.

## 1. Core Concepts in Spring AI

In this section, we will delve into some essential concepts related to generative AI and how they are implemented in Spring AI.

### 1.1 ChatClient

The ChatClient is a core component that facilitates interaction with AI services. It handles sending prompts to an AI model like OpenAI’s GPT and retrieving the generated responses, allowing us to focus on implementing business logic rather than managing low-level API interactions. Spring Boot automatically configures ChatClient using the properties defined in our application.properties or application.yml file.

### 1.2 Prompt and PromptTemplate

In Spring AI, Prompt and PromptTemplate are tools designed to streamline the process of generating dynamic and structured prompts for AI models. They simplify the interaction with AI services, enabling us to create contextually relevant inputs for generating responses.
A Prompt represents the input that is sent to an AI model. It is essentially a string or set of instructions that guides the AI in generating a relevant and coherent response. In Spring AI, the Prompt class is used to encapsulate this input, making it easier to manage and manipulate.
PromptTemplate is a feature that allows us to define reusable and dynamic prompt templates. It helps in creating structured prompts by defining placeholders that can be replaced with actual values at runtime. This is useful for generating prompts based on varying inputs or contexts. Here is a simple example of a prompt template:
Explanation
- {adjective} : Describes the tone of the review, such as “ critical ,” or “ enthusiastic .”
- {genre} : Specifies the genre of the book, like “ mystery, ” “ science fiction ,” or “ romance .”
- {title} : The title of the book being reviewed.
Usage Example: For an enthusiastic review of a science fiction book titled “ Space Odyssey ,” the filled prompt would be: “Write an enthusiastic review of a science fiction book titled ‘ Space Odyssey ‘.”

### 1.3 What is ChatResponse in Spring AI?

In Spring AI, ChatResponse is a class that represents the output received from an AI model after sending a prompt. It is a data structure provided by Spring AI that contains the results returned by an AI model. It encapsulates the AI’s response, including the generated content and other relevant metadata.

## 2. Setting Up the API Key for Spring AI

To interact with external AI services like OpenAI using Spring AI, we need to set up an API key. This API key is essential for authenticating our application with the AI service provider, enabling us to send prompts and receive responses securely. Here is a guide to setting up an API key in our Spring Boot application.

### 2.1 Obtain the API Key

First, we must obtain an API key from our AI service provider. Here is how we can do it for OpenAI:
- Sign up or log in to your OpenAI account at https://platform.openai.com/ . You can create an account if you haven’t already. If you have a ChatGPT account, you can use the same credentials to log in.
- Navigate to the API section in your dashboard. Here, a link labelled Create new secret key opens a form to generate a secret key. When you click on Create a secret key , a secret key will be generated.
- Copy the API key to use in your Spring Boot application.

### 2.2 Store the API Key Securely

It is important to store the API key securely and avoid hardcoding it directly into the application’s source code. A common approach is to use environment variables. If using a Mac, we can set the API key as an environment variable on our system like this:

## 3. Adding OpenAI Dependency to Your Application

To start using Spring AI with OpenAI, we must add the spring-ai-openai-spring-boot-starter dependency to our Spring Boot project. We can use the Spring Initializr to generate the basic structure.
The above setup adds the following necessary dependencies for Sring AI to our pom.xml file:

## 4. A Simple Example: Basic AI Prompt

To understand how Spring AI works, let’s start with a simple example. In this example, we will create a Spring Boot REST controller that uses Spring AI to generate a motivational quote.
In this example, we’ve created a REST controller MotivationController with a single endpoint /motivate . When accessed, this endpoint sends a basic prompt to the AI model. The prompt in this case is "Give me a motivational quote to start my day" . The /motivate endpoint triggers the AI to generate a motivational quote.
The AI then generates a quote, and the controller returns both the prompt and the quote in a JSON format.  To test the application, you can open your web browser and navigate to http://localhost:8080/ai/motivate or you can use a tool like Postman to send a GET request to the same URL.
Using curl , we can send a GET request to the /ai/motivate endpoint.
When you run the above curl command, the application will process the request and return a JSON response. The JSON will contain the original prompt and the motivational quote generated by the AI.
An example output might look like this:

## 5. A More Advanced Example: Using Prompt Templates and Bean Parsing

Now let’s explore a more complex example that demonstrates the power of Spring AI by using prompt templates and parsing the response into a Java object.
In the above code example, the BeanOutputConverter class plays a crucial role in converting the textual response from an AI model into a structured Java object, specifically a MovieRecommendation object.
AI-generated text is often unstructured and may not easily map to a Java object. The BeanOutputConverter class is designed to handle the transformation of raw text into a Java object. In this case, it converts the response from the AI model (which is in text form) into a MovieRecommendation object.
The {format} in the prompt is a placeholder that the BeanOutputConverter replaces with a specific format. This format tells the AI how to structure its response so it matches the MovieRecommendation class. Including {format} in the prompt helps the AI generate output in a format like String, Map, List, XML, or JSON that the BeanOutputConverter can easily convert into a Java object.
Here is the MovieRecommendation class:
We can test the API by sending a GET request to the /ai/recommend/{genre} endpoint with the following curl command:
The AI might respond with a recommendation with an output that might look like this:

## 6. Conclusion

In this Spring AI tutorial, we explored how to leverage the power of Spring Boot and AI to create RESTful services. By integrating the ChatClient from the spring-ai-openai-spring-boot-starter , we demonstrated how to generate dynamic prompts and parse AI-generated responses into structured Java objects.

## 7. Download the Source Code

This was a tutorial on Spring AI.
We will contact you soon.

### Omozegie Aziegbe

- Facebook
- LinkedIn

### Related Articles

### Simple REST client in Java

### Spring Boot Error – Error creating a bean with name ‘dataSource’ defined in class path resource DataSourceAutoConfiguration

### How to fix Exception in thread “main” java.lang.NoClassDefFoundError: org/slf4j/LoggerFactory in Java

### Mockito: Cannot instantiate @InjectMocks field: the type is an interface

### Spring Boot Remove Embedded Tomcat Server, Enable Jetty Server

### What is SecurityContext and SecurityContextHolder in Spring Security?

### How to install Apache Web Server on EC2 Instance using User data script

### 100 Java Spring Interview Questions & Answers – The ULTIMATE List (PDF Download)

This site uses Akismet to reduce spam. Learn how your comment data is processed.
[LINK: WhatsApp](https://api.whatsapp.com/send?text=Getting%20Started%20with%20Spring%20AI%20https://www.javacodegeeks.com/getting-started-with-spring-ai.html)

--------------------