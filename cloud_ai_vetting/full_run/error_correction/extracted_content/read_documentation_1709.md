# Read Documentation
**URL:** https://docs.runware.ai/en/utilities/image-to-text
**Page Title:** Caption API | Runware Docs
--------------------

[LINK: _docs](/docs/getting-started/introduction)

## Introduction

Image to text, also known as image captioning , allows you to obtain descriptive text prompts based on uploaded or previously generated images. This powerful feature allows advanced vision-language models to analyze visual content and generate accurate, detailed descriptions.

### Core capabilities

- General captioning : Generate comprehensive descriptions of any image content.
- Content analysis : Detect objects, scenes, activities, and composition details.
- Age detection : Specialized models for age estimation and demographic analysis.
Image captioning is instrumental for creating textual descriptions that can be used to generate similar images, provide accessibility descriptions, or gain detailed insights into visual content.
Different models excel at different types of analysis. LLaVA models provide rich, detailed descriptions, while CLIP offers semantic understanding, and specialized detectors focus on specific attributes like age estimation.

## Request

Our API always accepts an array of objects as input, where each object represents a specific task to be performed . The structure varies depending on the model and analysis type used.
The following examples demonstrate different captioning workflows using various models.

### taskType

[LINK: taskType](https://runware.ai/docs/tools/caption#request-tasktype)
The type of task to be performed. For this task, the value should be caption .

### taskUUID

[LINK: taskUUID](https://runware.ai/docs/tools/caption#request-taskuuid)
When a task is sent to the API you must include a random UUID v4 string using the taskUUID parameter. This string is used to match the async responses to their corresponding tasks.
If you send multiple tasks at the same time, the taskUUID will help you match the responses to the correct tasks.
The taskUUID must be unique for each task you send to the API.

### webhookURL

[LINK: webhookURL](https://runware.ai/docs/tools/caption#request-webhookurl)
Specifies a webhook URL where JSON responses will be sent via HTTP POST when generation tasks complete. For batch requests with multiple results, each completed item triggers a separate webhook call as it becomes available.
Webhooks can be secured using standard authentication methods supported by your endpoint, such as tokens in query parameters or API keys.
The webhook POST body contains the JSON response for the completed task according to your request configuration.

### deliveryMethod

[LINK: deliveryMethod](https://runware.ai/docs/tools/caption#request-deliverymethod)
Determines how the API delivers task results. Choose between immediate synchronous delivery or polling-based asynchronous delivery depending on your task requirements.
Sync mode ( "sync" ) :
Returns complete results directly in the API response when processing completes within the timeout window. For long-running tasks like video generation or model uploads, the request will timeout before completion, though the task continues processing in the background and results remain accessible through the dashboard.
Async mode ( "async" ) :
Returns an immediate acknowledgment with the task UUID, requiring you to poll for results using getResponse once processing completes. This approach prevents timeout issues and allows your application to handle other operations while waiting.
[LINK: getResponse](/docs/utilities/task-responses)
Polling workflow (async) :
- Submit request with deliveryMethod: "async" .
- Receive immediate response with the task UUID.
- Poll for completion using getResponse task.
- Retrieve final results when status shows "success" .
When to use each mode :
- Sync : Fast image generation, simple processing tasks.
- Async : Video generation, model uploads, or any task that usually takes more than 60 seconds.
Async mode is required for computationally intensive operations to avoid timeout errors.

### includeCost

[LINK: includeCost](https://runware.ai/docs/tools/caption#request-includecost)
If set to true , the cost to perform the task will be included in the response object.

### inputs

[LINK: inputs](https://runware.ai/docs/tools/caption#request-inputs)
Configuration object containing the input image for caption generation.
Object properties :
- image (string, required for image captioning models): Source of the image that will be analyzed.
The image can be specified in one of the following formats:
- An UUID v4 string of a previously uploaded image or a generated image.
- A data URI string representing the image. The data URI must be in the format data:<mediaType>;base64, followed by the base64-encoded image. For example: data:image/png;base64,iVBORw0KGgo... .
- A base64 encoded image without the data URI prefix. For example: iVBORw0KGgo... .
- A URL pointing to the image. The image must be accessible publicly.
Supported formats are: PNG, JPG and WEBP.
- video (string, required for video transcription models): Source of the video used to extract speech audio for transcription.
The video can be specified in one of the following formats:
- An UUID v4 string of a previously uploaded video or a generated video.
- A data URI string representing the video. The data URI must be in the format data:<mediaType>;base64, followed by the base64-encoded video. For example: data:video/mp4;base64,iVBORw0KGgo... .
- A base64 encoded video without the data URI prefix. For example: iVBORw0KGgo... .
- A URL pointing to the video. The video must be accessible publicly.
Supported video formats: MP4, WEBM.

### model

[LINK: model](https://runware.ai/docs/tools/caption#request-model)
We make use of the AIR system to identify background removal models. This identifier is a unique string that represents a specific model.
[LINK: AIR system](/docs/image-inference/models#air-system)
Specialized models return specific parameters in the structuredData object instead of the text field.

### prompt

[LINK: prompt](https://runware.ai/docs/tools/caption#request-prompt)
Provides specific instructions or questions to guide the image analysis. When specified, the model will focus on answering your question or following your instructions. If no prompt is provided, the model will automatically describe the image in detail, including objects, scenes, composition, style, and other visual elements.
Examples :
- "Describe the artistic style and color palette used in this image."
- "What emotions or mood does this image convey?"
- "List all the objects visible in this image."
- "Analyze the lighting and composition techniques."

## Response

Results will be delivered in the format below.

### taskType

[LINK: taskType](https://runware.ai/docs/tools/caption#response-tasktype)
The type of task to be performed. For this task, the value should be caption .

### taskUUID

[LINK: taskUUID](https://runware.ai/docs/tools/caption#response-taskuuid)
The API will return the taskUUID you sent in the request. This way you can match the responses to the correct request tasks.

### text

[LINK: text](https://runware.ai/docs/tools/caption#response-text)
The resulting text or prompt from interrogating the image.

### structuredData

[LINK: structuredData](https://runware.ai/docs/tools/caption#response-structureddata)
Contains structured, machine-readable data returned by specialized models instead of free-form text descriptions. This field is used when models perform specific analytical tasks that benefit from formatted output rather than natural language responses.
When structuredData is present, the standard text field will be omitted from the response, as the structured format provides the analysis result. The exact structure and properties depend on the specific model and analysis type being performed.
Always check for the presence of structuredData before falling back to the text field. Parse the structure according to the specific model's documented format.
Return age group classifications with confidence scores.

### cost

[LINK: cost](https://runware.ai/docs/tools/caption#response-cost)
if includeCost is set to true , the response will include a cost field for each task object. This field indicates the cost of the request in USD.

--------------------