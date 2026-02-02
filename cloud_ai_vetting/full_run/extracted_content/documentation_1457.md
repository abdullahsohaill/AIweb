# documentation
**URL:** https://ai.google.dev/api/rest/v1/models/embedContent
**Page Title:** Embeddings  |  Gemini API  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/api/embeddings#v1beta.models.embedContent)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/api/embeddings?hl=de#v1beta.models.embedContent)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/api/embeddings?hl=es-419#v1beta.models.embedContent)
- Français
[LINK: Français](https://ai.google.dev/api/embeddings?hl=fr#v1beta.models.embedContent)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/api/embeddings?hl=id#v1beta.models.embedContent)
- Italiano
[LINK: Italiano](https://ai.google.dev/api/embeddings?hl=it#v1beta.models.embedContent)
- Polski
[LINK: Polski](https://ai.google.dev/api/embeddings?hl=pl#v1beta.models.embedContent)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/api/embeddings?hl=pt-br#v1beta.models.embedContent)
- Shqip
[LINK: Shqip](https://ai.google.dev/api/embeddings?hl=sq#v1beta.models.embedContent)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/api/embeddings?hl=vi#v1beta.models.embedContent)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/api/embeddings?hl=tr#v1beta.models.embedContent)
- Русский
[LINK: Русский](https://ai.google.dev/api/embeddings?hl=ru#v1beta.models.embedContent)
- עברית
[LINK: עברית](https://ai.google.dev/api/embeddings?hl=he#v1beta.models.embedContent)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/api/embeddings?hl=ar#v1beta.models.embedContent)
- فارسی
[LINK: فارسی](https://ai.google.dev/api/embeddings?hl=fa#v1beta.models.embedContent)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/api/embeddings?hl=hi#v1beta.models.embedContent)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/api/embeddings?hl=bn#v1beta.models.embedContent)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/api/embeddings?hl=th#v1beta.models.embedContent)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/api/embeddings?hl=zh-cn#v1beta.models.embedContent)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/api/embeddings?hl=zh-tw#v1beta.models.embedContent)
- 日本語
[LINK: 日本語](https://ai.google.dev/api/embeddings?hl=ja#v1beta.models.embedContent)
- 한국어
[LINK: 한국어](https://ai.google.dev/api/embeddings?hl=ko#v1beta.models.embedContent)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi%2Fembeddings%23v1beta.models.embedContent&prompt=select_account)
- On this page
- Method: models.embedContent Endpoint Path parameters Request body Example request Response body
- Endpoint
- Path parameters
- Request body
- Example request
- Response body
- Method: models.batchEmbedContents Endpoint Path parameters Request body Example request Response body
- Endpoint
- Path parameters
- Request body
- Example request
- Response body
- Method: models.asyncBatchEmbedContent Endpoint Path parameters Request body Response body
- Endpoint
- Path parameters
- Request body
- Response body
- EmbedContentResponse
- ContentEmbedding
- TaskType
- EmbedContentBatch
- InputEmbedContentConfig
- InlinedEmbedContentRequests
- InlinedEmbedContentRequest
- EmbedContentBatchOutput
- InlinedEmbedContentResponses
- InlinedEmbedContentResponse
- EmbedContentBatchStats
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- API reference
[LINK: API reference](https://ai.google.dev/api)

## Embeddings

- On this page
- Method: models.embedContent Endpoint Path parameters Request body Example request Response body
- Endpoint
- Path parameters
- Request body
- Example request
- Response body
- Method: models.batchEmbedContents Endpoint Path parameters Request body Example request Response body
- Endpoint
- Path parameters
- Request body
- Example request
- Response body
- Method: models.asyncBatchEmbedContent Endpoint Path parameters Request body Response body
- Endpoint
- Path parameters
- Request body
- Response body
- EmbedContentResponse
- ContentEmbedding
- TaskType
- EmbedContentBatch
- InputEmbedContentConfig
- InlinedEmbedContentRequests
- InlinedEmbedContentRequest
- EmbedContentBatchOutput
- InlinedEmbedContentResponses
- InlinedEmbedContentResponse
- EmbedContentBatchStats
Embeddings are a numerical representation of text input that open up a number of unique use cases, such as clustering, similarity measurement and information retrieval. For an introduction, check out the Embeddings guide .
[LINK: Embeddings guide](https://ai.google.dev/gemini-api/docs/embeddings)
Unlike generative AI models that create new content, the Gemini Embedding model is only intended to transform the format of your input data into a numerical representation. While Google is responsible for providing an embedding model that transforms the format of your input data to the numerical-format requested, users retain full responsibility for the data they input and the resulting embeddings. By using the Gemini Embedding model you confirm that you have the necessary rights to any content that you upload. Do not generate content that infringes on others' intellectual property or privacy rights. Your use of this service is subject to our Prohibited Use Policy and Google's Terms of Service .
[LINK: Google's Terms of Service](https://ai.google.dev/gemini-api/terms)

## Method: models. embed Content

- Endpoint
- Path parameters
- Request body JSON representation
- JSON representation
- Response body
- Authorization scopes
- Example request Basic
- Basic
Generates a text embedding vector from the input Content using the specified Gemini Embedding model .
[LINK: Gemini Embedding model](https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding)

### Endpoint

### Path parameters

Required. The model's resource name. This serves as an ID for the Model to use.
This name should match a model name returned by the models.list method.
Format: models/{model} It takes the form models/{model} .

### Request body

The request body contains data with the following structure:
[LINK: Content](/api/caching#Content)
Required. The content to embed. Only the parts.text fields will be counted.
[LINK: TaskType](/api/embeddings#v1beta.TaskType)
Optional. Optional task type for which the embeddings will be used. Not supported on earlier models ( models/embedding-001 ).
Optional. An optional title for the text. Only applicable when TaskType is RETRIEVAL_DOCUMENT .
Note: Specifying a title for RETRIEVAL_DOCUMENT provides better quality embeddings for retrieval.
Optional. Optional reduced dimension for the output embedding. If set, excessive values in the output embedding are truncated from the end. Supported by newer models since 2024 only. You cannot set this value if using the earlier model ( models/embedding-001 ).

### Example request

[LINK: embed . py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/embed.py#L22-L32)
[LINK: embed . js](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/javascript/embed.js#L22-L31)
[LINK: embed . go](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/go/embed.go#L15-L41)
[LINK: embed.sh](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/rest/embed.sh#L4-L12)

### Response body

If successful, the response body contains an instance of EmbedContentResponse .
[LINK: EmbedContentResponse](/api/embeddings#v1beta.EmbedContentResponse)

## Method: models. batch Embed Contents

- Endpoint
- Path parameters
- Request body JSON representation
- JSON representation
- Response body JSON representation
- JSON representation
- Authorization scopes
- Example request Basic
- Basic
Generates multiple embedding vectors from the input Content which consists of a batch of strings represented as EmbedContentRequest objects.

### Endpoint

### Path parameters

Required. The model's resource name. This serves as an ID for the Model to use.
This name should match a model name returned by the models.list method.
Format: models/{model} It takes the form models/{model} .

### Request body

The request body contains data with the following structure:
[LINK: EmbedContentRequest](/api/batch-api#EmbedContentRequest)
Required. Embed requests for the batch. The model in each of these requests must match the model specified BatchEmbedContentsRequest.model .

### Example request

[LINK: embed . py](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/python/embed.py#L37-L51)
[LINK: embed . js](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/javascript/embed.js#L38-L51)
[LINK: embed . go](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/go/embed.go#L48-L75)
[LINK: embed.sh](https://github.com/google-gemini/api-examples/blob/856e8a0f566a2810625cecabba6e2ab1fe97e496/rest/embed.sh#L16-L34)

### Response body

The response to a BatchEmbedContentsRequest .
If successful, the response body contains data with the following structure:
[LINK: ContentEmbedding](/api/embeddings#v1beta.ContentEmbedding)
Output only. The embeddings for each request, in the same order as provided in the batch request.
[LINK: ContentEmbedding](/api/embeddings#v1beta.ContentEmbedding)

## Method: models. async Batch Embed Content

- Endpoint
- Path parameters
- Request body JSON representation JSON representation JSON representation JSON representation
- JSON representation JSON representation JSON representation JSON representation
- JSON representation
- JSON representation
- JSON representation
- Response body
- Authorization scopes
Enqueues a batch of models.embedContent requests for batch processing. We have a models.batchEmbedContents handler in GenerativeService , but it was synchronized. So we name this one to be Async to avoid confusion.

### Endpoint

### Path parameters

Required. The name of the Model to use for generating the completion.
Format: models/{model} . It takes the form models/{model} .

### Request body

The request body contains data with the following structure:
Output only. Identifier. Resource name of the batch.
Format: batches/{batchId} .
Required. The user-defined name of this batch.
[LINK: InputEmbedContentConfig](/api/embeddings#InputEmbedContentConfig)
Required. Input configuration of the instances on which batch processing are performed.
[LINK: EmbedContentBatchOutput](/api/embeddings#EmbedContentBatchOutput)
Output only. The output of the batch request.
Output only. The time at which the batch was created.
Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z" , "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30" .
Output only. The time at which the batch processing completed.
Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z" , "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30" .
Output only. The time at which the batch was last updated.
Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z" , "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30" .
[LINK: EmbedContentBatchStats](/api/embeddings#EmbedContentBatchStats)
Output only. Stats about the batch.
[LINK: BatchState](/api/batch-api#v1beta.BatchState)
Output only. The state of the batch.
[LINK: int64](https://developers.google.com/discovery/v1/type-format)
Optional. The priority of the batch. Batches with a higher priority value will be processed before batches with a lower priority value. Negative values are allowed. Default is 0.

### Response body

If successful, the response body contains an instance of Operation .
[LINK: Operation](/api/batch-api#Operation)

## Embed Content Response

- JSON representation
The response to an EmbedContentRequest .
[LINK: ContentEmbedding](/api/embeddings#v1beta.ContentEmbedding)
Output only. The embedding generated from the input content.
[LINK: ContentEmbedding](/api/embeddings#v1beta.ContentEmbedding)

## Content Embedding

- JSON representation
A list of floats representing an embedding.
The embedding values.

## Task Type

Type of task for which the embedding will be used.

## Embed Content Batch

- JSON representation
- InputEmbedContentConfig JSON representation
- JSON representation
- InlinedEmbedContentRequests JSON representation
- JSON representation
- InlinedEmbedContentRequest JSON representation
- JSON representation
- EmbedContentBatchOutput JSON representation
- JSON representation
- InlinedEmbedContentResponses JSON representation
- JSON representation
- InlinedEmbedContentResponse JSON representation
- JSON representation
- EmbedContentBatchStats JSON representation
- JSON representation
A resource representing a batch of EmbedContent requests.
Required. The name of the Model to use for generating the completion.
Format: models/{model} .
Output only. Identifier. Resource name of the batch.
Format: batches/{batchId} .
Required. The user-defined name of this batch.
[LINK: InputEmbedContentConfig](/api/embeddings#InputEmbedContentConfig)
Required. Input configuration of the instances on which batch processing are performed.
[LINK: EmbedContentBatchOutput](/api/embeddings#EmbedContentBatchOutput)
Output only. The output of the batch request.
Output only. The time at which the batch was created.
Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z" , "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30" .
Output only. The time at which the batch processing completed.
Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z" , "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30" .
Output only. The time at which the batch was last updated.
Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: "2014-10-02T15:01:23Z" , "2014-10-02T15:01:23.045123456Z" or "2014-10-02T15:01:23+05:30" .
[LINK: EmbedContentBatchStats](/api/embeddings#EmbedContentBatchStats)
Output only. Stats about the batch.
[LINK: BatchState](/api/batch-api#v1beta.BatchState)
Output only. The state of the batch.
[LINK: int64](https://developers.google.com/discovery/v1/type-format)
Optional. The priority of the batch. Batches with a higher priority value will be processed before batches with a lower priority value. Negative values are allowed. Default is 0.
[LINK: InputEmbedContentConfig](/api/embeddings#InputEmbedContentConfig)
[LINK: EmbedContentBatchOutput](/api/embeddings#EmbedContentBatchOutput)
[LINK: EmbedContentBatchStats](/api/embeddings#EmbedContentBatchStats)
[LINK: BatchState](/api/batch-api#v1beta.BatchState)

## Input Embed Content Config

Configures the input to the batch request.
The name of the File containing the input requests.
[LINK: InlinedEmbedContentRequests](/api/embeddings#InlinedEmbedContentRequests)
The requests to be processed in the batch.
[LINK: InlinedEmbedContentRequests](/api/embeddings#InlinedEmbedContentRequests)

## Inlined Embed Content Requests

The requests to be processed in the batch if provided as part of the batch creation request.
[LINK: InlinedEmbedContentRequest](/api/embeddings#InlinedEmbedContentRequest)
Required. The requests to be processed in the batch.
[LINK: InlinedEmbedContentRequest](/api/embeddings#InlinedEmbedContentRequest)

## Inlined Embed Content Request

The request to be processed in the batch.
[LINK: EmbedContentRequest](/api/batch-api#EmbedContentRequest)
Required. The request to be processed in the batch.
Optional. The metadata to be associated with the request.
[LINK: EmbedContentRequest](/api/batch-api#EmbedContentRequest)

## Embed Content Batch Output

The output of a batch request. This is returned in the AsyncBatchEmbedContentResponse or the EmbedContentBatch.output field.
Output only. The file ID of the file containing the responses. The file will be a JSONL file with a single response per line. The responses will be EmbedContentResponse messages formatted as JSON. The responses will be written in the same order as the input requests.
[LINK: InlinedEmbedContentResponses](/api/embeddings#InlinedEmbedContentResponses)
Output only. The responses to the requests in the batch. Returned when the batch was built using inlined requests. The responses will be in the same order as the input requests.
[LINK: InlinedEmbedContentResponses](/api/embeddings#InlinedEmbedContentResponses)

## Inlined Embed Content Responses

The responses to the requests in the batch.
[LINK: InlinedEmbedContentResponse](/api/embeddings#InlinedEmbedContentResponse)
Output only. The responses to the requests in the batch.
[LINK: InlinedEmbedContentResponse](/api/embeddings#InlinedEmbedContentResponse)

## Inlined Embed Content Response

The response to a single request in the batch.
Output only. The metadata associated with the request.
[LINK: Status](/api/files#v1beta.Status)
Output only. The error encountered while processing the request.
[LINK: EmbedContentResponse](/api/embeddings#v1beta.EmbedContentResponse)
Output only. The response to the request.
[LINK: Status](/api/files#v1beta.Status)
[LINK: EmbedContentResponse](/api/embeddings#v1beta.EmbedContentResponse)

## Embed Content Batch Stats

Stats about the batch.
[LINK: int64](https://developers.google.com/discovery/v1/type-format)
Output only. The number of requests in the batch.
[LINK: int64](https://developers.google.com/discovery/v1/type-format)
Output only. The number of requests that were successfully processed.
[LINK: int64](https://developers.google.com/discovery/v1/type-format)
Output only. The number of requests that failed to be processed.
[LINK: int64](https://developers.google.com/discovery/v1/type-format)
Output only. The number of requests that are still pending processing.
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2025-10-30 UTC.

--------------------