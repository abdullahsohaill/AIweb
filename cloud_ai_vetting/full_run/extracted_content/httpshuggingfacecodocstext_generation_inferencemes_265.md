# https://huggingface.co/docs/text-generation-inference/messages\_api
**URL:** https://huggingface.co/docs/text-generation-inference/messages_api
**Page Title:** Messages API
--------------------

text-generation-inference documentation
Messages API

## text-generation-inference

[LINK: 10,739](https://github.com/huggingface/text-generation-inference)
and get access to the augmented documentation experience
to get started

## Messages API

Text Generation Inference (TGI) now supports the Messages API, which is fully compatible with the OpenAI Chat Completion API. This feature is available starting from version 1.4.0. You can use OpenAI’s client libraries or third-party libraries expecting OpenAI schema to interact with TGI’s Messages API. Below are some examples of how to utilize this compatibility.
Note: The Messages API is supported from TGI version 1.4.0 and above. Ensure you are using a compatible version to access this feature.
- Making a Request
- Streaming
- Synchronous
- Hugging Face Inference Endpoints
- Cloud Providers Amazon SageMaker
- Amazon SageMaker

## Making a Request

You can make a request to TGI’s Messages API using curl . Here’s an example:

## Streaming

You can also use OpenAI’s Python client library to make a streaming request. Here’s how:

## Synchronous

If you prefer to make a synchronous request, you can do so like this:

## Hugging Face Inference Endpoints

The Messages API is integrated with Inference Endpoints .
Every endpoint that uses “Text Generation Inference” with an LLM, which has a chat template can now be used. Below is an example of how to use IE with TGI using OpenAI’s Python client library:
Note: Make sure to replace base_url with your endpoint URL and to include v1/ at the end of the URL. The api_key should be replaced with your Hugging Face API key.

## Cloud Providers

TGI can be deployed on various cloud providers for scalable and robust text generation. One such provider is Amazon SageMaker, which has recently added support for TGI. Here’s how you can deploy TGI on Amazon SageMaker:

## Amazon SageMaker

To enable the Messages API in Amazon SageMaker you need to set the environment variable MESSAGES_API_ENABLED=true .
This will modify the /invocations route to accept Messages dictonaries consisting out of role and content. See the example below on how to deploy Llama with the new Messages API.
[LINK: < > Update on GitHub](https://github.com/huggingface/text-generation-inference/blob/main/docs/source/messages_api.md)
[LINK: Text Generation Inference →](/docs/text-generation-inference/index)

--------------------