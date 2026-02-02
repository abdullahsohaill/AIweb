# siliconflow
**URL:** https://docs.siliconflow.cn/api-reference/chat-completions/chat-completions
**Page Title:** 创建对话请求（OpenAI） - SiliconFlow
--------------------

[LINK: API手册](/cn/api-reference/chat-completions/chat-completions)
- POST 创建对话请求（OpenAI）
[LINK: POST 创建对话请求（OpenAI）](/cn/api-reference/chat-completions/chat-completions)
- POST 创建对话请求（Anthropic）
[LINK: POST 创建对话请求（Anthropic）](/cn/api-reference/chat-completions/messages)
- POST 创建嵌入请求
[LINK: POST 创建嵌入请求](/cn/api-reference/embeddings/create-embeddings)
- POST 创建重排序请求
[LINK: POST 创建重排序请求](/cn/api-reference/rerank/create-rerank)
- POST 创建图片生成请求
[LINK: POST 创建图片生成请求](/cn/api-reference/images/images-generations)
- POST 上传参考音频
[LINK: POST 上传参考音频](/cn/api-reference/audio/upload-voice)
- POST 创建文本转语音请求
[LINK: POST 创建文本转语音请求](/cn/api-reference/audio/create-speech)
- GET 参考音频列表获取
[LINK: GET 参考音频列表获取](/cn/api-reference/audio/voice-list)
- POST 删除参考音频
[LINK: POST 删除参考音频](/cn/api-reference/audio/delete-voice)
- POST 创建语音转文本请求
[LINK: POST 创建语音转文本请求](/cn/api-reference/audio/create-audio-transcriptions)
- POST 创建视频生成请求
[LINK: POST 创建视频生成请求](/cn/api-reference/videos/videos_submit)
- POST 获取视频生成链接请求
[LINK: POST 获取视频生成链接请求](/cn/api-reference/videos/get_videos_status)
- POST 上传文件
[LINK: POST 上传文件](/cn/api-reference/batch/upload-file)
- GET 获取文件列表
[LINK: GET 获取文件列表](/cn/api-reference/batch/get-file-list)
- POST 创建batch任务
[LINK: POST 创建batch任务](/cn/api-reference/batch/create-batch)
- GET 获取batch任务详情
[LINK: GET 获取batch任务详情](/cn/api-reference/batch/get-batch)
- GET 获取batch任务列表
[LINK: GET 获取batch任务列表](/cn/api-reference/batch/get-batch-list)
- POST 取消batch任务
[LINK: POST 取消batch任务](/cn/api-reference/batch/cancel-batch)
- GET 获取用户模型列表
[LINK: GET 获取用户模型列表](/cn/api-reference/models/get-model-list)
Use the following format for authentication: Bearer
- LLM
- VLM
Corresponding Model Name. We periodically update our models to enhance service quality. Changes may include model on/offlining or capability adjustments. We will strive to notify you via announcements or push messages. For a complete list of available models, please check the Models .
"Pro/zai-org/GLM-4.7"
A list of messages comprising the conversation so far.
Show child attributes
If set, tokens are returned as Server-Sent Events as they are made available. Stream terminates with data: [DONE]
false
The maximum number of tokens to generate. Ensure that input tokens + max_tokens do not exceed the model’s context window. As some services are still being updated, avoid setting max_tokens to the window’s upper bound; reserve ~10k tokens as buffer for input and system overhead. See Models( https://cloud.siliconflow.cn/models ) for details.
4096
Switches between thinking and non-thinking modes.  This field supports the following models:
false
Maximum number of tokens for chain-of-thought output. This field applies to all Reasoning models .
4096
Dynamic filtering threshold that adapts based on token probabilities.This field only applies to Qwen3.
0.05
Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.
null
Determines the degree of randomness in the response.
0.7
The top_p (nucleus) parameter is used to dynamically adjust the number of choices for each predicted token based on the cumulative probabilities.
0.7
0.5
Number of generations to return
An object specifying the format that the model must output.
Show child attributes
A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.
Show child attributes
The response from the model. The response header contains the x-siliconcloud-trace-id field, which serves as a unique identifier for tracing requests, facilitating log queries and issue troubleshooting.
Show child attributes
Show child attributes
[LINK: 创建对话请求（Anthropic）](/cn/api-reference/chat-completions/messages)

--------------------