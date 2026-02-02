# gitee
**URL:** https://gitee.com/moyangzhan/langchain4j-aideepin
**Page Title:** langchain4j-aideepin: 基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)
--------------------


## moyangzhan / langchain4j-aideepin

[LINK: docs](/moyangzhan/langchain4j-aideepin/tree/main/docs)
- Getting Started
- System Composition and Documentation
- Demo URL
- Features
- Integrated Platform Features
- Tech Stack
- How to Deploy
- Initialization Build and Run
- Initialization
- Build and Run
- Screenshots
- Recommended Projects

## Getting Started

LangChain4j-AIDeepin is an AI-based productivity enhancement tool.
It can be used to assist enterprises/teams in technical research and development, product design, HR/finance/IT information consulting, system/product consulting, customer service support, etc.
🌟 If this project is helpful to you, please give it a star 🌟

## System Composition and Documentation

中文文档 | English
AIDEEPIN
|__ Server (langchain4j-aideepin)
|__ User Web (langchain4j-aideepin-web)
|__ Admin Web (langchain4j-aideepin-admin)
👉 Detailed Documentation
[LINK: Detailed Documentation](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fmoyangzhan%2Flangchain4j-aideepin%2Fwiki)
Backend source repository: github or gitee
[LINK: github](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fmoyangzhan%2Flangchain4j-aideepin)
Frontend projects:
- User Web: langchain4j-aideepin-web github gitee
- github
[LINK: github](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fmoyangzhan%2Flangchain4j-aideepin-web)
- gitee
- Admin Web: langchain4j-aideepin-admin github gitee
- github
[LINK: github](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fmoyangzhan%2Flangchain4j-aideepin-admin)
- gitee

## Demo URL

http://www.aideepin.com

## Features

- Multi-conversation (multi-role)
- Image generation (text-to-image, image editing, image-to-image)
- Knowledge base based on large models (RAG) Vector search Graph search
- Vector search
- Graph search
- Network search based on large models (RAG)
- AI workflow
- MCP service marketplace
- ASR & TTS Text question - Text response Text question - Voice response Voice question - Text response Voice question - Voice response
- Text question - Text response
- Text question - Voice response
- Voice question - Text response
- Voice question - Voice response
- Long-term memory
- Storage Local Storage OSS (Alibaba Cloud)
- Local Storage
- OSS (Alibaba Cloud)

## Integrated Platform Features

## Tech Stack

This repository is for the backend service
Tech stack:
- jdk17
- springboot3.0.5
- langchain4j(Java version of LangChain)
[LINK: langchain4j(Java version of LangChain)](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Flangchain4j%2Flangchain4j)
- langgraph4j
[LINK: langgraph4j](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fbsorrentino%2Flanggraph4j)
- Postgresql pgvector extension: https://github.com/pgvector/pgvector Apache AGE extension: https://github.com/apache/age
- pgvector extension: https://github.com/pgvector/pgvector
[LINK: https://github.com/pgvector/pgvector](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fpgvector%2Fpgvector)
- Apache AGE extension: https://github.com/apache/age
[LINK: https://github.com/apache/age](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fapache%2Fage)
- neo4j
Frontend tech stack:
- vue3
- vite
- typescript
- pnpm
- pinia
- naiveui

## How to Deploy

### Initialization

a. Initialize the database
- Create the database aideepin
Create the database aideepin
- Execute docs/create.sql
Execute docs/create.sql
- Enable and configure the model platform (also referred to as model provider in some projects) or use the admin web to configure on the interface Configure model platforms -- DeepSeek
update adi_model_platform set api_key = 'my_deepseek_secret_key' where name = 'deepseek';

-- OpenAI
update adi_model_platform set api_key = 'my_openai_secret_key' where name = 'openai';

-- Dashscope
update adi_model_platform set api_key = 'my_dashcope_api_key' where name = 'dashscope';

--siliconflow
update adi_model_platform set api_key = 'my_siliconflow_api_key' where name = 'siliconflow_setting';

-- Qianfan API key and secret key
update adi_model_platform set api_key = 'my_qianfan_api_key',secret_key='my_qianfan_secret_key' where name = 'qianfan';

-- Ollama configuration
update adi_model_platform set base_url = 'my_ollama_base_url' where name = 'ollama'; Enable model platform models or add new models -- Enable model
update adi_ai_model set is_enable = true where name = 'deepseek-chat';
update adi_ai_model set is_enable = true where name = 'gpt-3.5-turbo';
update adi_ai_model set is_enable = true where name = 'dall-e-2';
update adi_ai_model set is_enable = true where name = 'qwen-turbo';
update adi_ai_model set is_enable = true where name = 'THUDM/GLM-Z1-9B-0414';
update adi_ai_model set is_enable = true where name = 'ernie_speed';
update adi_ai_model set is_enable = true where name = 'tinydolphin';

-- Add new model
INSERT INTO adi_ai_model (name, type, platform, is_enable) VALUES ('vicuna', 'text', 'ollama', true);
Enable and configure the model platform (also referred to as model provider in some projects) or use the admin web to configure on the interface
[LINK: admin web](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fmoyangzhan%2Flangchain4j-aideepin-admin)
- Configure model platforms -- DeepSeek
update adi_model_platform set api_key = 'my_deepseek_secret_key' where name = 'deepseek';

-- OpenAI
update adi_model_platform set api_key = 'my_openai_secret_key' where name = 'openai';

-- Dashscope
update adi_model_platform set api_key = 'my_dashcope_api_key' where name = 'dashscope';

--siliconflow
update adi_model_platform set api_key = 'my_siliconflow_api_key' where name = 'siliconflow_setting';

-- Qianfan API key and secret key
update adi_model_platform set api_key = 'my_qianfan_api_key',secret_key='my_qianfan_secret_key' where name = 'qianfan';

-- Ollama configuration
update adi_model_platform set base_url = 'my_ollama_base_url' where name = 'ollama';
- Enable model platform models or add new models -- Enable model
update adi_ai_model set is_enable = true where name = 'deepseek-chat';
update adi_ai_model set is_enable = true where name = 'gpt-3.5-turbo';
update adi_ai_model set is_enable = true where name = 'dall-e-2';
update adi_ai_model set is_enable = true where name = 'qwen-turbo';
update adi_ai_model set is_enable = true where name = 'THUDM/GLM-Z1-9B-0414';
update adi_ai_model set is_enable = true where name = 'ernie_speed';
update adi_ai_model set is_enable = true where name = 'tinydolphin';

-- Add new model
INSERT INTO adi_ai_model (name, type, platform, is_enable) VALUES ('vicuna', 'text', 'ollama', true);
- Fill in the search engine configuration Google configuration update adi_sys_config set value = '{"url":"https://www.googleapis.com/customsearch/v1","key":"my key from cloud.google.com","cx":"my cx from programmablesearchengine.google.com"}' where name = 'google_setting';
Fill in the search engine configuration
- Google configuration update adi_sys_config set value = '{"url":"https://www.googleapis.com/customsearch/v1","key":"my key from cloud.google.com","cx":"my cx from programmablesearchengine.google.com"}' where name = 'google_setting';
b. Modify the configuration file
- postgresql: application-[dev|prod].xml in spring.datasource
- redis: application-[dev|prod].xml in spring.data.redis
- mail: application.xml in spring.mail

### Build and Run

- Enter the project cd langchain4j-aideepin
Enter the project
- Package: mvn clean package -Dmaven.test.skip=true
Package:
- Run Start with jar: cd adi-bootstrap/target
nohup java -jar -Xms768m -Xmx1024m -XX:+HeapDumpOnOutOfMemoryError adi-bootstrap-0.0.1-SNAPSHOT.jar --spring.profiles.active=[dev|prod] dev/null 2>&1 & Start with docker cd adi-bootstrap
docker build . -t aideepin:0.0.1
docker run -d \
  --name=aideepin \
  -e APP_PROFILE=[dev|prod] \
  -v="/data/aideepin/logs:/data/logs" \
  aideepin:0.0.1
Run
- Start with jar:
- Start with docker

## Screenshots

AI Chat:
AI Drawing:
Knowledge Base:
Vectorization:
Knowledge Graph:
Workflow：

## Recommended Projects

Mango Desk
[LINK: Mango Desk](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fmoyangzhan%2Fmango-desk)
Mango Desk is a local-first desktop app for searching your local documents with natural language.
It helps you find information based on what you remember, not file names or folder structures.
此处可能存在不合适展示的内容，页面不予展示。您可通过相关编辑功能自查并修改。
如您确认内容无涉及 不当用语 / 纯广告导流 / 暴力 / 低俗色情 / 侵权 / 盗版 / 虚假 / 无价值内容或违法国家有关法律法规的内容，可点击提交进行申诉，我们将尽快为您处理。

### Search


--------------------