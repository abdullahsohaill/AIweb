# Realtime API
**URL:** https://platform.minimaxi.com/document/Realtime
**Page Title:** 文档中心 - MiniMax 开放平台
--------------------

### (Raw Extraction Fallback)

文档中心
账户管理
订阅 Coding Plan
登录
Realtime API
构建低延迟、多模态体验，使用实时 API。
实时 API 使您能够构建低延迟、多模态的对话体验。它目前支持文本和音频作为输入和输出。Realtime API 是一种基于事件的有状态 API，通过 WebSocket 进行通信。WebSocket 连接需要以下参数：
URL：wss://api.minimax.chat/ws/v1/realtime
Query Parameters: ?model=abab6.5s-chat
Headers: Authorization: Bearer YOUR_API_KEY
下面是一个使用 Node.js 中的 ws 库建立套接字连接、发送消息和接收响应的简单示例。
请求示例
import WebSocket from "ws";

const url = "wss://api.minimax.chat/ws/v1/realtime?model=abab6.5s-chat";
const ws = new WebSocket(url, {
    headers: {
        "Authorization": "Bearer Your_API_Key" 
    },
});

ws.on("open", function open() {
    console.log("Connected to server.");
    ws.send(JSON.stringify({
        type: "response.create",
        response: {
            modalities: ["text"],
            instructions: "Please assist the user.",
        }
    }));
});

ws.on("message", function incoming(message) {
    console.log(JSON.parse(message.toString()));
});
集成指南
1.
支持的音频格式，目前，Realtime API 支持的音频格式：PCM、16bits、24kHz、 单声道。音频必须是 base64 编码的音频帧块。
2.
发送事件，要将事件发送到 API，您必须发送包含事件负载数据的 JSON 字符串。在发送前确保您已连接到 API。
Send a user mesage
javascript
// Make sure we are connected
ws.on('open', () => {
  // Send an event
  const event = {
    type: 'conversation.item.create',
    item: {
      type: 'message',
      role: 'user',
      content: [
        {
          type: 'input_text',
          text: 'Hello!'
        }
      ]
    }
  };
  ws.send(JSON.stringify(event));
});
3.
接收事件，要接收事件，请侦听 WebSocket 消息事件，并将结果解析为 JSON。
receive events
javascript
ws.on('message', data => {
  try {
    const event = JSON.parse(data);
    console.log(event);
  } catch (e) {
    console.error(e);
  }
});
4.
常见的使用示例，以下是 API 功能的一些常见示例，供您开始使用。这些示例假定您已经实例化 WebSocket。
Send user text
Send user audio
Stream user audio
send user text
javascript
const event = {
  type: 'conversation.item.create',
  item: {
    type: 'message',
    role: 'user',
    content: [
      {
        type: 'input_text',
        text: 'Hello!'
      }
    ]
  }
};
ws.send(JSON.stringify(event));
ws.send(JSON.stringify({type: 'response.create'}));
Client events
session.update
发送此事件以更新会话的默认配置。客户端可以随时发送此事件来更新 session 配置，任何字段都可能随时更新，除了 “voice” 之外。服务器将使用 session.updated 事件进行响应，该事件显示完整的有效配置。只有存在的字段才会被更新，因此清除像 “instructions” 这样的字段的正确方法是传递一个空字符串。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为 "session.update"
sessionobject
错误信息
隐藏参数
modalitiesstring
模型可以使用的模态集。要禁用音频，请将其设置为 [“text”]。
instructionsstring
默认系统指令（即 system message）附加到 model 调用之前。此字段允许客户端指导模型获得所需的响应。该模型可以被指导回答内容和格式（例如，“要非常简洁”、“行为友好”、“这里有好回应的例子”）和音频行为（例如，“快声说”、“在你的声音中注入情感”、“经常大笑”）。不能保证模型会遵循这些说明，但它们会为模型提供有关所需行为的指导。
voicestring
可参考t2a的voiceid进行接入
input_audio_formatstring
输入音频的格式。选项包括 pcm16。
output_audio_formatstring
输出音频的格式。选项包括 pcm16。
max_response_output_tokensstring
单个 Assistant 响应的最大输出令牌数，支持 (0,245760]
session.update
{
    "event_id": "event_123",
    "type": "session.update",
    "session": {
        "modalities": ["text", "audio"],
        "instructions": "Your knowledge cutoff is 2023-10. You are a helpful assistant.",
        "voice": "female-yujie",
        "input_audio_format": "pcm16",
        "output_audio_format": "pcm16",
        "temperature": 0.8,
        "max_response_output_tokens": "500"
    }
}

input_audio_buffer.append
发送此事件以将音频字节追加到输入音频缓冲区。音频缓冲区是您可以写入并在以后提交的临时存储，目前必须手动提交音频缓冲区。客户端可以选择在每个事件中放置多少音频，最高可达 15 MiB。与创建的其他客户端事件不同，服务器不会向此事件发送确认响应。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"input_audio_buffer.append"
audioobject
Base64 编码的音频字节。这必须采用会话配置中 input_audio_format 字段指定的格式。
input_audio_buffer.append
{
    "event_id": "event_456",
    "type": "input_audio_buffer.append",
    "audio": "Base64EncodedAudioData"
}

input_audio_buffer.commit
发送此事件以提交用户输入音频缓冲区，这将在对话中创建新的用户消息项。如果输入音频缓冲区为空，则此事件将产生错误。提交输入音频缓冲区将触发输入音频转录（如果在会话配置中启用），但不会从模型创建响应。服务器将使用 input_audio_buffer.committed 事件进行响应。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"input_audio_buffer.commit"
input_audio_buffer.commit
{
    "event_id": "event_789",
    "type": "input_audio_buffer.commit"
}
input_audio_buffer.clear
发送此事件以清除缓冲区中的音频字节。服务器将使用 input_audio_buffer.cleared 事件进行响应。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"input_audio_buffer.clear"
input_audio_buffer.clear
{
    "event_id": "event_012",
    "type": "input_audio_buffer.clear"
}

conversation.item.create
将新 Item 添加到 Conversation 的上下文中，包括消息、函数调用和函数调用响应。此事件既可用于填充对话的 “历史记录” ，也可用于在中途添加新项目，但当前限制是它无法填充 Assistant 音频消息。如果成功，服务器将使用 conversation.item.created 事件进行响应，否则将发送错误事件。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"conversation.item.create"
previous_item_idstring
前一项的 ID，新项将在其后插入。如果未设置，则新项目将附加到对话的末尾。如果设置，则允许在对话中插入项目。如果找不到 ID，将返回错误，并且不会添加该项目。
itemstring
要添加到对话中的项。
隐藏参数
idstring
项目的唯一 ID，可以由客户端生成以帮助管理服务器端上下文，但不是必需的，因为如果未提供，服务器将生成一个。
typestring
项目的类型
statusstring
项目的状态 （completed， incomplete）。这些对会话没有影响，但会接受这些值以与 conversation.item.created 事件保持一致。
rolestring
消息发送者的角色（用户、助手、系统），仅适用于消息项。
contentstring
消息的内容，适用于消息项。system仅支持input_text内容、User 支持input_text 和 input_audio 内容的消息项、assistant助手支持text内容的消息项。
隐藏参数
typestring
内容类型:input_text、input_audio、text
textstring
文本内容，用于 input_text 和 text 内容类型。
audiostring
Base64 编码的音频字节，用于 input_audio 内容类型。
transcriptstring
音频的转录文本，用于 input_audio 内容类型。
conversation.item.create
{
    "event_id": "event_345",
    "type": "conversation.item.create",
    "previous_item_id": null,
    "item": {
        "id": "msg_001",
        "type": "message",
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": "Hello, how are you?"
            }
        ]
    }
}

conversation.item.delete
当您想从对话历史记录中删除任何项目时，发送此事件。服务器将使用 conversation.item.deleted 事件进行响应，除非该项目在对话历史记录中不存在，在这种情况下，服务器将响应错误。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"conversation.item.delete"
item_idstring
要删除的项目的 ID。
conversation.item.delete
{
    "event_id": "event_901",
    "type": "conversation.item.delete",
    "item_id": "msg_003"
}

response.create
此事件指示服务器创建 Response，这意味着触发模型推理。Response 包含一个 Item。这些项目将附加到对话历史记录中。服务器将使用 response.created 事件、Items 和 content created 事件以及最后的 response.done 事件进行响应，以指示响应已完成。response.create 事件包括推理配置（如 instructions）和 temperature。这些字段将仅覆盖此 Response 的 Session 配置。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"response.create"
responseobject
要添加到对话中的项。
隐藏参数
idstring
响应的唯一 ID。
objectstring
对象类型必须为:realtime.response
statusstring
响应的最终状态 （completed， cancelled， failed， incomplete）。
status_detailsobject
有关状态的其他详细信息。
隐藏参数
typestring
导致响应失败的错误类型，与状态字段（已取消、不完整、失败）相对应。
reasonstring
响应未完成的原因。
errorobject
导致响应失败的错误的说明，在状态为 failed 时填充。
隐藏参数
typestring
错误的类型。
codestring
错误代码（如果有）
outputarray
响应生成的输出项列表。
usagearray
Response 的使用情况统计信息，这将对应于账单。
隐藏参数
total_tokensinteger
响应中的令牌总数，包括输入和输出文本token。
input_tokensinteger
响应中使用的输入token的数量，包括文本token。
output_tokensinteger
响应中发送的输出token的数量，包括文本token。
total_asr_timeinteger
asr识别语音的时长
total_audio_charactersinteger
语音生成对应的字符数
response.create
{
    "event_id": "event_234",
    "type": "response.create",
    "response": {
        "modalities": ["text", "audio"],
        "instructions": "Please assist the user.",
        "voice": "male-qn-qingse",
        "output_audio_format": "pcm16",
        "temperature": 0.7,
        "max_response_output_tokens": 150
    }
}

Server events
error
发生错误时返回，这可能是客户端问题或服务器问题。大多数错误都是可恢复的，并且会话将保持打开状态，我们建议实现者默认监控和记录错误消息。
event_idstring
服务器事件的唯一 ID。
typestring
事件类型必须为"error"
errorsobject
错误的详细信息。
隐藏参数
typestring
错误类型（例如，“invalid_request_error”、“server_error”）。
codestring
错误代码（如果有）。
messagestring
人类可读的错误消息。
paramstring
与错误相关的参数（如果有）。
event_idstring
导致错误的 client 事件的 event_id（如果适用）。
error
{
    "event_id": "event_890",
    "type": "error",
    "error": {
        "type": "invalid_request_error",
        "code": "invalid_event",
        "message": "The 'type' field is missing.",
        "param": null,
        "event_id": "event_567"
    }
}
session.created
创建 Session 时返回。当新连接建立为第一个服务器事件时自动发出。此事件将包含默认的 Session 配置。
event_idstring
服务端的 ID。
typestring
事件类型必须为 “session.created
sessionobject
错误信息
隐藏参数
modalitiesstring
模型可以使用的模态集。要禁用音频，请将其设置为 [“text”]。
instructionsstring
默认系统指令（即 system message）附加到 model 调用之前。此字段允许客户端指导模型获得所需的响应。该模型可以被指导回答内容和格式（例如，“要非常简洁”、“行为友好”、“这里有好回应的例子”）和音频行为（例如，“快声说”、“在你的声音中注入情感”、“经常大笑”）。不能保证模型会遵循这些说明，但它们会为模型提供有关所需行为的指导。
voicestring
可参考t2a的voiceid进行接入
input_audio_formatstring
输入音频的格式。选项包括 pcm16。
output_audio_formatstring
输出音频的格式。选项包括 pcm16。
max_response_output_tokensstring
单个 Assistant 响应的最大输出令牌数，支持 (0,245760]
session.updated
{
    "event_id": "event_5678",
    "type": "session.updated",
    "session": {
        "id": "sess_001",
        "object": "realtime.session",
        "model": "abab6.5s-chat",
        "modalities": ["text"],
        "instructions": "New instructions",
        "voice": "male-qn-qingse",
        "input_audio_format": "pcm16",
        "output_audio_format": "pcm16",
        "temperature": 0.7,
        "max_response_output_tokens": 200
    }
}

session.updated
除非出现错误，否则在使用 session.update 事件更新会话时返回。
event_idstring
服务端的 ID。
typestring
事件类型必须为 “session.updated
sessionobject
错误信息
隐藏参数
modalitiesstring
模型可以使用的模态集。要禁用音频，请将其设置为 [“text”]。
instructionsstring
默认系统指令（即 system message）附加到 model 调用之前。此字段允许客户端指导模型获得所需的响应。该模型可以被指导回答内容和格式（例如，“要非常简洁”、“行为友好”、“这里有好回应的例子”）和音频行为（例如，“快声说”、“在你的声音中注入情感”、“经常大笑”）。不能保证模型会遵循这些说明，但它们会为模型提供有关所需行为的指导。
voicestring
可参考t2a的voiceid进行接入
input_audio_formatstring
输入音频的格式。选项包括 pcm16。
output_audio_formatstring
输出音频的格式。选项包括 pcm16。
max_response_output_tokensstring
单个 Assistant 响应的最大输出令牌数，支持 (0,245760]
session.updated
{
    "event_id": "event_5678",
    "type": "session.updated",
    "session": {
        "id": "sess_001",
        "object": "realtime.session",
        "model": "abab6.5s-chat",
        "modalities": ["text"],
        "instructions": "New instructions",
        "voice": "alloy",
        "input_audio_format": "pcm16",
        "output_audio_format": "pcm16",
        "temperature": 0.7,
        "max_response_output_tokens": 200
    }
}

conversation.created
创建对话时返回。在会话创建后立即发出。
event_idstring
服务端ID。
typestring
事件类型必须为"conversation.created"
conversationobject
要添加到对话中的项。
隐藏参数
idstring
会话的唯一 ID。
objectstring
对象类型必须为 “realtime.conversation”。
conversation.created
{
    "event_id": "event_9101",
    "type": "conversation.created",
    "conversation": {
        "id": "conv_001",
        "object": "realtime.conversation"
    }
}

conversation.item.created
创建对话项时返回。有几种情况会产生此事件：
1.服务器正在生成一个 Response，如果成功，将生成一个或两个 Item，其类型为 message；
2.输入音频缓冲区已由客户端提交。服务器将获取 input audio buffer 的内容，并将其添加到新的用户消息 Item 中；
3.客户端已发送 conversation.item.create 事件以向 Conversation 添加新 Item。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"conversation.item.create"
previous_item_idstring
前一项的 ID，新项将在其后插入。如果未设置，则新项目将附加到对话的末尾。如果设置，则允许在对话中插入项目。如果找不到 ID，将返回错误，并且不会添加该项目。
itemstring
要添加到对话中的项。
隐藏参数
idstring
项目的唯一 ID，可以由客户端生成以帮助管理服务器端上下文，但不是必需的，因为如果未提供，服务器将生成一个。
typestring
项目的类型
statusstring
项目的状态 （completed， incomplete）。这些对会话没有影响，但会接受这些值以与 conversation.item.created 事件保持一致。
rolestring
消息发送者的角色（用户、助手、系统），仅适用于消息项。
contentstring
消息的内容，适用于消息项。system仅支持input_text内容、User 支持input_text 和 input_audio 内容的消息项、assistant助手支持text内容的消息项。
隐藏参数
typestring
内容类型:input_text、input_audio、text
textstring
文本内容，用于 input_text 和 text 内容类型。
audiostring
Base64 编码的音频字节，用于 input_audio 内容类型。
transcriptstring
音频的转录文本，用于 input_audio 内容类型。
conversation.item.created
{
    "event_id": "event_1920",
    "type": "conversation.item.created",
    "previous_item_id": "msg_002",
    "item": {
        "id": "msg_003",
        "object": "realtime.item",
        "type": "message",
        "status": "completed",
        "role": "user",
        "content": [
            {
                "type": "input_audio",
                "transcript": "hello how are you",
                "audio": "base64encodedaudio=="
            }
        ]
    }
}

conversation.item.deleted
当客户端使用 conversation.item.delete 事件删除对话中的项目时返回。此事件用于将服务器对 conversation history 的理解与 Client 端的视图同步。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"conversation.item.delete"
item_idstring
要删除的项目的 ID。
conversation.item.deleted
{
    "event_id": "event_2728",
    "type": "conversation.item.deleted",
    "item_id": "msg_005"
}

input_audio_buffer.committed
当客户端提交输入音频缓冲区时返回。item_id 属性是将创建的用户消息项的 ID，因此 conversation.item.created 事件也将发送到客户端。
event_idstring
用于标识此事件的可选客户端生成的 ID。
typestring
事件类型必须为"input_audio_buffer.committed"
previous_item_idstring
前一项的 ID，新项将在其后插入。
item_idstring
将创建的用户消息项的 ID。
input_audio_buffer.committed
{
    "event_id": "event_1121",
    "type": "input_audio_buffer.committed",
    "previous_item_id": "msg_001",
    "item_id": "msg_002"
}

input_audio_buffer.cleared
当客户端使用 input_audio_buffer.clear 事件清除输入音频缓冲区时返回。
event_idstring
服务器事件的唯一 ID。
typestring
事件类型必须为"input_audio_buffer.cleared"
input_audio_buffer.cleared
{
    "event_id": "event_1314",
    "type": "input_audio_buffer.cleared"
}

response.created
创建新 Response 时返回。响应创建的第一个事件，其中响应的初始状态为 in_progress。
event_idstring
服务端 ID。
typestring
事件类型必须为"response.created"
responseobject
要添加到对话中的项。
隐藏参数
idstring
响应的唯一 ID。
objectstring
对象类型必须为:realtime.response
statusstring
响应的最终状态 （completed， cancelled， failed， incomplete）。
status_detailsobject
有关状态的其他详细信息。
隐藏参数
typestring
导致响应失败的错误类型，与状态字段（已取消、不完整、失败）相对应。
reasonstring
响应未完成的原因。
errorobject
导致响应失败的错误的说明，在状态为 failed 时填充。
隐藏参数
typestring
错误的类型。
codestring
错误代码（如果有）
outputarray
响应生成的输出项列表。
usagearray
Response 的使用情况统计信息，这将对应于账单。
隐藏参数
total_tokensinteger
响应中的令牌总数，包括输入和输出文本token。
input_tokensinteger
响应中使用的输入token的数量，包括文本token。
output_tokensinteger
响应中发送的输出token的数量，包括文本token。
total_asr_timeinteger
asr识别语音的时长
total_audio_charactersinteger
语音生成对应的字符数
response.created
{
    "event_id": "event_3132",
    "type": "response.done",
    "response": {
        "id": "resp_001",
        "object": "realtime.response",
        "status": "completed",
        "status_details": null,
        "output": [
            {
                "id": "msg_006",
                "object": "realtime.item",
                "type": "message",
                "status": "completed",
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Sure, how can I assist you today?"
                    }
                ]
            }
        ],
        "usage": {
            "total_tokens":275,
            "total_asr_time":256,
            "total_audio_characters":256,
            "input_tokens":127,
            "output_tokens":148,
        }
    }
}

response.done
当 Response 完成流式处理时返回。始终发出，无论最终状态如何。response.done 事件中包含的 Response 对象将包括 Response 中的所有输出 Item，但会省略原始音频数据。
event_idstring
服务端的 ID。
typestring
事件类型必须为"response.done"
responseobject
要添加到对话中的项。
隐藏参数
idstring
响应的唯一 ID。
objectstring
对象类型必须为:realtime.response
statusstring
响应的最终状态 （completed， cancelled， failed， incomplete）。
status_detailsobject
有关状态的其他详细信息。
隐藏参数
typestring
导致响应失败的错误类型，与状态字段（已取消、不完整、失败）相对应。
reasonstring
响应未完成的原因。
errorobject
导致响应失败的错误的说明，在状态为 failed 时填充。
隐藏参数
typestring
错误的类型。
codestring
错误代码（如果有）
outputarray
响应生成的输出项列表。
usagearray
Response 的使用情况统计信息，这将对应于账单。
隐藏参数
total_tokensinteger
响应中的令牌总数，包括输入和输出文本token。
input_tokensinteger
响应中使用的输入token的数量，包括文本token。
output_tokensinteger
响应中发送的输出token的数量，包括文本token。
total_asr_timeinteger
asr识别语音的时长
total_audio_charactersinteger
语音生成对应的字符数
response.done
{
    "event_id": "event_3132",
    "type": "response.done",
    "response": {
        "id": "resp_001",
        "object": "realtime.response",
        "status": "completed",
        "status_details": null,
        "output": [
            {
                "id": "msg_006",
                "object": "realtime.item",
                "type": "message",
                "status": "completed",
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Sure, how can I assist you today?"
                    }
                ]
            }
        ],
        "usage": {
            "total_tokens":275,
            "input_tokens":127,
            "output_tokens":148,
            "total_tokens":275,
            "total_asr_time":256,
            "total_audio_characters":256
        }
    }
}

response.output_item.added
在生成 Response 期间创建新 Item 时返回。
event_idstring
服务端ID。
typestring
事件类型必须为"response.output_item.added"
response_idstring
项目所属的 Response 的 ID。
output_indexstring
响应中输出项的索引。
itemstring
要添加到对话中的项。
隐藏参数
idstring
项目的唯一 ID，可以由客户端生成以帮助管理服务器端上下文，但不是必需的，因为如果未提供，服务器将生成一个。
typestring
项目的类型
statusstring
项目的状态 （completed， incomplete）。这些对会话没有影响，但会接受这些值以与 conversation.item.created 事件保持一致。
rolestring
消息发送者的角色（用户、助手、系统），仅适用于消息项。
contentstring
消息的内容，适用于消息项。system仅支持input_text内容、User 支持input_text 和 input_audio 内容的消息项、assistant助手支持text内容的消息项。
隐藏参数
typestring
内容类型:input_text、input_audio、text
textstring
文本内容，用于 input_text 和 text 内容类型。
audiostring
Base64 编码的音频字节，用于 input_audio 内容类型。
transcriptstring
音频的转录文本，用于 input_audio 内容类型。
response.output_item.added
{
    "event_id": "event_3334",
    "type": "response.output_item.added",
    "response_id": "resp_001",
    "output_index": 0,
    "item": {
        "id": "msg_007",
        "object": "realtime.item",
        "type": "message",
        "status": "in_progress",
        "role": "assistant",
        "content": []
    }
}
response.output_item.done
event_idstring
服务端ID。
typestring
事件类型必须为"response.output_item.done"
response_idstring
项目所属的 Response 的 ID。
output_indexstring
响应中输出项的索引。
itemstring
要添加到对话中的项。
隐藏参数
idstring
项目的唯一 ID，可以由客户端生成以帮助管理服务器端上下文，但不是必需的，因为如果未提供，服务器将生成一个。
typestring
项目的类型
statusstring
项目的状态 （completed， incomplete）。这些对会话没有影响，但会接受这些值以与 conversation.item.created 事件保持一致。
rolestring
消息发送者的角色（用户、助手、系统），仅适用于消息项。
contentstring
消息的内容，适用于消息项。system仅支持input_text内容、User 支持input_text 和 input_audio 内容的消息项、assistant助手支持text内容的消息项。
隐藏参数
typestring
内容类型:input_text、input_audio、text
textstring
文本内容，用于 input_text 和 text 内容类型。
audiostring
Base64 编码的音频字节，用于 input_audio 内容类型。
transcriptstring
音频的转录文本，用于 input_audio 内容类型。
response.output_item.done
{
    "event_id": "event_3536",
    "type": "response.output_item.done",
    "response_id": "resp_001",
    "output_index": 0,
    "item": {
        "id": "msg_007",
        "object": "realtime.item",
        "type": "message",
        "status": "completed",
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Sure, I can help with that."
            }
        ]
    }
}
response.text.delta
当 “text” 内容部分的 text 值更新时返回。
event_idstring
服务端ID。
typestring
事件类型必须为"response.text.delta"
response_idstring
响应的 ID。
item_idstring
项目的 ID。
output_indexstring
响应中输出项的索引。
content_indexstring
内容部分在项的 content 数组中的索引。
deltastring
文本增量。
response.text.delta
{
    "event_id": "event_4142",
    "type": "response.text.delta",
    "response_id": "resp_001",
    "item_id": "msg_007",
    "output_index": 0,
    "content_index": 0,
    "delta": "Sure, I can h"
}

response.text.done
当 “text” 内容部分的 text 值完成流式处理时返回。当 Response 中断、不完整或取消时也会发出。
event_idstring
服务端ID。
typestring
事件类型必须为"response.text.done"
response_idstring
响应的 ID。
item_idstring
项目的 ID。
output_indexstring
响应中输出项的索引。
content_indexstring
内容部分在项的 content 数组中的索引。
deltastring
最终的文本内容。
response.text.done
{
    "event_id": "event_4344",
    "type": "response.text.done",
    "response_id": "resp_001",
    "item_id": "msg_007",
    "output_index": 0,
    "content_index": 0,
    "text": "Sure, I can help with that."
}
response.audio_transcript.delta
更新模型生成的音频输出转录时返回。
event_idstring
服务端ID。
typestring
事件类型必须为"response.audio_transcript.delta"
response_idstring
响应的 ID。
item_idstring
项目的 ID。
output_indexstring
响应中输出项的索引。
content_indexstring
内容部分在项的 content 数组中的索引。
deltastring
转录增量。
response.audio_transcript.delta
{
    "event_id": "event_4546",
    "type": "response.audio_transcript.delta",
    "response_id": "resp_001",
    "item_id": "msg_008",
    "output_index": 0,
    "content_index": 0,
    "delta": "Hello, how can I a"
}

response.audio_transcript.done
当模型生成的音频输出转录完成流式处理时返回。当 Response 中断、不完整或取消时也会发出。
event_idstring
服务端ID。
typestring
事件类型必须为"response.audio_transcript.done"
response_idstring
响应的 ID。
item_idstring
项目的 ID。
output_indexstring
响应中输出项的索引。
content_indexstring
内容部分在项的 content 数组中的索引。
deltastring
音频的最终转录。
response.audio_transcript.done
{
    "event_id": "event_4748",
    "type": "response.audio_transcript.done",
    "response_id": "resp_001",
    "item_id": "msg_008",
    "output_index": 0,
    "content_index": 0,
    "transcript": "Hello, how can I assist you today?"
}

response.audio.delta
更新模型生成的音频时返回。
event_idstring
服务端ID。
typestring
事件类型必须为"response.audio.delta"
response_idstring
响应的 ID。
item_idstring
项目的 ID。
output_indexstring
响应中输出项的索引。
content_indexstring
内容部分在项的 content 数组中的索引。
deltastring
Base64 编码的音频数据增量。
response.audio.delta
{
    "event_id": "event_4950",
    "type": "response.audio.delta",
    "response_id": "resp_001",
    "item_id": "msg_008",
    "output_index": 0,
    "content_index": 0,
    "delta": "Base64EncodedAudioDelta"
}

response.audio.done
在模型生成的音频完成时返回。当 Response 中断、不完整或取消时也会发出。
event_idstring
服务端ID。
typestring
事件类型必须为"response.audio.done"
response_idstring
响应的 ID。
item_idstring
项目的 ID。
output_indexstring
响应中输出项的索引。
content_indexstring
内容部分在项的 content 数组中的索引。
response.audio.done
{
    "event_id": "event_5152",
    "type": "response.audio.done",
    "response_id": "resp_001",
    "item_id": "msg_008",
    "output_index": 0,
    "content_index": 0
}

本文是否对您有帮助
是
否
上一页
ChatCompletion Pro
下一页
Finetune
On this page
集成指南
Client events
Server events
© 2026 MiniMax

--------------------