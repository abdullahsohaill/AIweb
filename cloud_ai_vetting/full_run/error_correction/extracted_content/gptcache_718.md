# GPTCache
**URL:** https://gptcache.readthedocs.io/en/latest
**Page Title:** GPTCache : A Library for Creating Semantic Cache for LLM Queries — GPTCache
--------------------

GPTCache
- .rst

## GPTCache : A Library for Creating Semantic Cache for LLM Queries

## Contents

## GPTCache : A Library for Creating Semantic Cache for LLM Queries #

Slash Your LLM API Costs by 10x 💰, Boost Speed by 100x ⚡
🎉 GPTCache has been fully integrated with 🦜️🔗 LangChain ! Here are detailed usage instructions .
[LINK: LangChain](https://github.com/hwchase17/langchain)
[LINK: usage instructions](https://python.langchain.com/docs/modules/model_io/models/llms/integrations/llm_caching#gptcache)
🐳 The GPTCache server docker image has been released, which means that any language will be able to use GPTCache!
[LINK: The GPTCache server docker image](https://github.com/zilliztech/GPTCache/blob/main/docs/usage.md#Use-GPTCache-server)
📔 This project is undergoing swift development, and as such, the API may be subject to change at any time. For the most up-to-date information, please refer to the latest documentation and release note .
[LINK: documentation](https://gptcache.readthedocs.io/en/latest/)
[LINK: release note](https://github.com/zilliztech/GPTCache/blob/main/docs/release_note.html)

## Quick Install #

pip install gptcache

## 🚀 What is GPTCache? #

ChatGPT and various large language models (LLMs) boast incredible versatility, enabling the development of a wide range of applications. However, as your application grows in popularity and encounters higher traffic levels, the expenses related to LLM API calls can become substantial. Additionally, LLM services might exhibit slow response times, especially when dealing with a significant number of requests.
To tackle this challenge, we have created GPTCache, a project dedicated to building a semantic cache for storing LLM responses.

## 😊 Quick Start #

Note :
- You can quickly try GPTCache and put it into a production environment without heavy development. However, please note that the repository is still under heavy development.
You can quickly try GPTCache and put it into a production environment without heavy development. However, please note that the repository is still under heavy development.
- By default, only a limited number of libraries are installed to support the basic cache functionalities. When you need to use additional features, the related libraries will be automatically installed .
By default, only a limited number of libraries are installed to support the basic cache functionalities. When you need to use additional features, the related libraries will be automatically installed .
- Make sure that the Python version is 3.8.1 or higher , check: python --version
Make sure that the Python version is 3.8.1 or higher , check: python --version
- If you encounter issues installing a library due to a low pip version, run: python -m pip install --upgrade pip .
If you encounter issues installing a library due to a low pip version, run: python -m pip install --upgrade pip .

### dev install #

### example usage #

These examples will help you understand how to use exact and similar matching with caching. You can also run the example on Colab . And more examples you can refer to the Bootcamp
[LINK: Bootcamp](https://gptcache.readthedocs.io/en/latest/bootcamp/openai/chat.html)
Before running the example, make sure the OPENAI_API_KEY environment variable is set by executing echo $OPENAI_API_KEY .
If it is not already set, it can be set by using export OPENAI_API_KEY=YOUR_API_KEY on Unix/Linux/MacOS systems or set OPENAI_API_KEY=YOUR_API_KEY on Windows systems.
It is important to note that this method is only effective temporarily, so if you want a permanent effect, you’ll need to modify the environment variable configuration file. For instance, on a Mac, you can modify the file located at /etc/profile .
OpenAI API original usage
OpenAI API + GPTCache, exact match cache
If you ask ChatGPT the exact same two questions, the answer to the second question will be obtained from the cache without requesting ChatGPT again.
OpenAI API + GPTCache, similar search cache
After obtaining an answer from ChatGPT in response to several similar questions, the answers to subsequent questions can be retrieved from the cache without the need to request ChatGPT again.
OpenAI API + GPTCache, use temperature
You can always pass a parameter of temperature while requesting the API service or model.
The range of temperature is [0, 2], default value is 0.0.
A higher temperature means a higher possibility of skipping cache search and requesting large model directly.
When temperature is 2, it will skip cache and send request to large model directly for sure. When temperature is 0, it will search cache before requesting large model service.
The default post_process_messages_func is temperature_softmax . In this case, refer to API reference to learn about how temperature affects output.
[LINK: API reference](https://gptcache.readthedocs.io/en/latest/references/processor.html#module-gptcache.processor.post)
To use GPTCache exclusively, only the following lines of code are required, and there is no need to modify any existing code.
More Docs：
- Usage, how to use GPTCache better
Usage, how to use GPTCache better
- Features, all features currently supported by the cache
Features, all features currently supported by the cache
- Examples, learn better custom caching
Examples, learn better custom caching

## 🎓 Bootcamp #

- GPTCache with LangChain QA Generation Question Answering SQL Chain BabyAGI User Guide
GPTCache with LangChain
- QA Generation
QA Generation
[LINK: QA Generation](https://gptcache.readthedocs.io/en/latest/bootcamp/langchain/qa_generation.html)
- Question Answering
Question Answering
[LINK: Question Answering](https://gptcache.readthedocs.io/en/latest/bootcamp/langchain/question_answering.html)
- SQL Chain
SQL Chain
[LINK: SQL Chain](https://gptcache.readthedocs.io/en/latest/bootcamp/langchain/sqlite.html)
- BabyAGI User Guide
BabyAGI User Guide
[LINK: BabyAGI User Guide](https://gptcache.readthedocs.io/en/latest/bootcamp/langchain/baby_agi.html)
- GPTCache with Llama_index WebPage QA
GPTCache with Llama_index
- WebPage QA
WebPage QA
[LINK: WebPage QA](https://gptcache.readthedocs.io/en/latest/bootcamp/llama_index/webpage_qa.html)
- GPTCache with OpenAI Chat completion Language Translation SQL Translate Twitter Classifier Multimodal: Image Generation Multimodal: Speech to Text
GPTCache with OpenAI
- Chat completion
Chat completion
[LINK: Chat completion](https://gptcache.readthedocs.io/en/latest/bootcamp/openai/chat.html)
- Language Translation
Language Translation
[LINK: Language Translation](https://gptcache.readthedocs.io/en/latest/bootcamp/openai/language_translate.html)
- SQL Translate
SQL Translate
[LINK: SQL Translate](https://gptcache.readthedocs.io/en/latest/bootcamp/openai/sql_translate.html)
- Twitter Classifier
Twitter Classifier
[LINK: Twitter Classifier](https://gptcache.readthedocs.io/en/latest/bootcamp/openai/tweet_classifier.html)
- Multimodal: Image Generation
Multimodal: Image Generation
[LINK: Multimodal: Image Generation](https://gptcache.readthedocs.io/en/latest/bootcamp/openai/image_generation.html)
- Multimodal: Speech to Text
Multimodal: Speech to Text
[LINK: Multimodal: Speech to Text](https://gptcache.readthedocs.io/en/latest/bootcamp/openai/speech_to_text.html)
- GPTCache with Replicate Visual Question Answering
GPTCache with Replicate
- Visual Question Answering
Visual Question Answering
[LINK: Visual Question Answering](https://gptcache.readthedocs.io/en/latest/bootcamp/replicate/visual_question_answering.html)
- GPTCache with Temperature Param OpenAI Chat OpenAI Image Creation
GPTCache with Temperature Param
- OpenAI Chat
OpenAI Chat
[LINK: OpenAI Chat](https://gptcache.readthedocs.io/en/latest/bootcamp/temperature/chat.html)
- OpenAI Image Creation
OpenAI Image Creation
[LINK: OpenAI Image Creation](https://gptcache.readthedocs.io/en/latest/bootcamp/temperature/create_image.html)

## 😎 What can this help with? #

GPTCache offers the following primary benefits:
- Decreased expenses : Most LLM services charge fees based on a combination of number of requests and token count . GPTCache effectively minimizes your expenses by caching query results, which in turn reduces the number of requests and tokens sent to the LLM service. As a result, you can enjoy a more cost-efficient experience when using the service.
Decreased expenses : Most LLM services charge fees based on a combination of number of requests and token count . GPTCache effectively minimizes your expenses by caching query results, which in turn reduces the number of requests and tokens sent to the LLM service. As a result, you can enjoy a more cost-efficient experience when using the service.
- Enhanced performance : LLMs employ generative AI algorithms to generate responses in real-time, a process that can sometimes be time-consuming. However, when a similar query is cached, the response time significantly improves, as the result is fetched directly from the cache, eliminating the need to interact with the LLM service. In most situations, GPTCache can also provide superior query throughput compared to standard LLM services.
Enhanced performance : LLMs employ generative AI algorithms to generate responses in real-time, a process that can sometimes be time-consuming. However, when a similar query is cached, the response time significantly improves, as the result is fetched directly from the cache, eliminating the need to interact with the LLM service. In most situations, GPTCache can also provide superior query throughput compared to standard LLM services.
- Adaptable development and testing environment : As a developer working on LLM applications, you’re aware that connecting to LLM APIs is generally necessary, and comprehensive testing of your application is crucial before moving it to a production environment. GPTCache provides an interface that mirrors LLM APIs and accommodates storage of both LLM-generated and mocked data. This feature enables you to effortlessly develop and test your application, eliminating the need to connect to the LLM service.
Adaptable development and testing environment : As a developer working on LLM applications, you’re aware that connecting to LLM APIs is generally necessary, and comprehensive testing of your application is crucial before moving it to a production environment. GPTCache provides an interface that mirrors LLM APIs and accommodates storage of both LLM-generated and mocked data. This feature enables you to effortlessly develop and test your application, eliminating the need to connect to the LLM service.
- Improved scalability and availability : LLM services frequently enforce rate limits , which are constraints that APIs place on the number of times a user or client can access the server within a given timeframe. Hitting a rate limit means that additional requests will be blocked until a certain period has elapsed, leading to a service outage. With GPTCache, you can easily scale to accommodate an increasing volume of of queries, ensuring consistent performance as your application’s user base expands.
Improved scalability and availability : LLM services frequently enforce rate limits , which are constraints that APIs place on the number of times a user or client can access the server within a given timeframe. Hitting a rate limit means that additional requests will be blocked until a certain period has elapsed, leading to a service outage. With GPTCache, you can easily scale to accommodate an increasing volume of of queries, ensuring consistent performance as your application’s user base expands.
[LINK: rate limits](https://platform.openai.com/docs/guides/rate-limits)

## 🤔 How does it work? #

Online services often exhibit data locality, with users frequently accessing popular or trending content. Cache systems take advantage of this behavior by storing commonly accessed data, which in turn reduces data retrieval time, improves response times, and eases the burden on backend servers. Traditional cache systems typically utilize an exact match between a new query and a cached query to determine if the requested content is available in the cache before fetching the data.
However, using an exact match approach for LLM caches is less effective due to the complexity and variability of LLM queries, resulting in a low cache hit rate. To address this issue, GPTCache adopt alternative strategies like semantic caching. Semantic caching identifies and stores similar or related queries, thereby increasing cache hit probability and enhancing overall caching efficiency.
GPTCache employs embedding algorithms to convert queries into embeddings and uses a vector store for similarity search on these embeddings. This process allows GPTCache to identify and retrieve similar or related queries from the cache storage, as illustrated in the Modules section .
[LINK: Modules section](https://github.com/zilliztech/GPTCache#-modules)
Featuring a modular design, GPTCache makes it easy for users to customize their own semantic cache. The system offers various implementations for each module, and users can even develop their own implementations to suit their specific needs.
In a semantic cache, you may encounter false positives during cache hits and false negatives during cache misses. GPTCache offers three metrics to gauge its performance, which are helpful for developers to optimize their caching systems:
- Hit Ratio : This metric quantifies the cache’s ability to fulfill content requests successfully, compared to the total number of requests it receives. A higher hit ratio indicates a more effective cache.
Hit Ratio : This metric quantifies the cache’s ability to fulfill content requests successfully, compared to the total number of requests it receives. A higher hit ratio indicates a more effective cache.
- Latency : This metric measures the time it takes for a query to be processed and the corresponding data to be retrieved from the cache. Lower latency signifies a more efficient and responsive caching system.
Latency : This metric measures the time it takes for a query to be processed and the corresponding data to be retrieved from the cache. Lower latency signifies a more efficient and responsive caching system.
- Recall : This metric represents the proportion of queries served by the cache out of the total number of queries that should have been served by the cache. Higher recall percentages indicate that the cache is effectively serving the appropriate content.
Recall : This metric represents the proportion of queries served by the cache out of the total number of queries that should have been served by the cache. Higher recall percentages indicate that the cache is effectively serving the appropriate content.
A sample benchmark is included for users to start with assessing the performance of their semantic cache.
[LINK: sample benchmark](https://github.com/zilliztech/gpt-cache/blob/main/examples/benchmark/benchmark_sqlite_faiss_onnx.py)

## 🤗 Modules #

- LLM Adapter :
The LLM Adapter is designed to integrate different LLM models by unifying their APIs and request protocols. GPTCache offers a standardized interface for this purpose, with current support for ChatGPT integration. [x] Support OpenAI ChatGPT API. [x] Support langchain . [x] Support minigpt4 . [x] Support Llamacpp . [x] Support dolly . [ ] Support other LLMs, such as Hugging Face Hub, Bard, Anthropic.
LLM Adapter :
The LLM Adapter is designed to integrate different LLM models by unifying their APIs and request protocols. GPTCache offers a standardized interface for this purpose, with current support for ChatGPT integration.
- [x] Support OpenAI ChatGPT API.
[x] Support OpenAI ChatGPT API.
- [x] Support langchain .
[x] Support langchain .
[LINK: langchain](https://github.com/hwchase17/langchain)
- [x] Support minigpt4 .
[x] Support minigpt4 .
[LINK: minigpt4](https://github.com/Vision-CAIR/MiniGPT-4.git)
- [x] Support Llamacpp .
[x] Support Llamacpp .
[LINK: Llamacpp](https://github.com/ggerganov/llama.cpp.git)
- [x] Support dolly .
[x] Support dolly .
[LINK: dolly](https://github.com/databrickslabs/dolly.git)
- [ ] Support other LLMs, such as Hugging Face Hub, Bard, Anthropic.
[ ] Support other LLMs, such as Hugging Face Hub, Bard, Anthropic.
- Multimodal Adapter (experimental) :
The Multimodal Adapter is designed to integrate different large multimodal models by unifying their APIs and request protocols. GPTCache offers a standardized interface for this purpose, with current support for integrations of image generation, audio transcription. [x] Support OpenAI Image Create API. [x] Support OpenAI Audio Transcribe API. [x] Support Replicate BLIP API. [x] Support Stability Inference API. [x] Support Hugging Face Stable Diffusion Pipeline (local inference). [ ] Support other multimodal services or self-hosted large multimodal models.
Multimodal Adapter (experimental) :
The Multimodal Adapter is designed to integrate different large multimodal models by unifying their APIs and request protocols. GPTCache offers a standardized interface for this purpose, with current support for integrations of image generation, audio transcription.
- [x] Support OpenAI Image Create API.
[x] Support OpenAI Image Create API.
- [x] Support OpenAI Audio Transcribe API.
[x] Support OpenAI Audio Transcribe API.
- [x] Support Replicate BLIP API.
[x] Support Replicate BLIP API.
- [x] Support Stability Inference API.
[x] Support Stability Inference API.
- [x] Support Hugging Face Stable Diffusion Pipeline (local inference).
[x] Support Hugging Face Stable Diffusion Pipeline (local inference).
- [ ] Support other multimodal services or self-hosted large multimodal models.
[ ] Support other multimodal services or self-hosted large multimodal models.
- Embedding Generator :
This module is created to extract embeddings from requests for similarity search. GPTCache offers a generic interface that supports multiple embedding APIs, and presents a range of solutions to choose from. [x] Disable embedding. This will turn GPTCache into a keyword-matching cache. [x] Support OpenAI embedding API. [x] Support ONNX with the GPTCache/paraphrase-albert-onnx model. [x] Support Hugging Face embedding with transformers, ViTModel, Data2VecAudio. [x] Support Cohere embedding API. [x] Support fastText embedding. [x] Support SentenceTransformers embedding. [x] Support Timm models for image embedding. [ ] Support other embedding APIs.
Embedding Generator :
This module is created to extract embeddings from requests for similarity search. GPTCache offers a generic interface that supports multiple embedding APIs, and presents a range of solutions to choose from.
- [x] Disable embedding. This will turn GPTCache into a keyword-matching cache.
[x] Disable embedding. This will turn GPTCache into a keyword-matching cache.
- [x] Support OpenAI embedding API.
[x] Support OpenAI embedding API.
- [x] Support ONNX with the GPTCache/paraphrase-albert-onnx model.
[x] Support ONNX with the GPTCache/paraphrase-albert-onnx model.
- [x] Support Hugging Face embedding with transformers, ViTModel, Data2VecAudio.
[x] Support Hugging Face embedding with transformers, ViTModel, Data2VecAudio.
- [x] Support Cohere embedding API.
[x] Support Cohere embedding API.
[LINK: Cohere](https://docs.cohere.ai/reference/embed)
- [x] Support fastText embedding.
[x] Support fastText embedding.
- [x] Support SentenceTransformers embedding.
[x] Support SentenceTransformers embedding.
- [x] Support Timm models for image embedding.
[x] Support Timm models for image embedding.
- [ ] Support other embedding APIs.
[ ] Support other embedding APIs.
- Cache Storage : Cache Storage is where the response from LLMs, such as ChatGPT, is stored. Cached responses are retrieved to assist in evaluating similarity and are returned to the requester if there is a good semantic match. At present, GPTCache supports SQLite and offers a universally accessible interface for extension of this module. [x] Support SQLite . [x] Support DuckDB . [x] Support PostgreSQL . [x] Support MySQL . [x] Support MariaDB . [x] Support SQL Server . [x] Support Oracle . [ ] Support MongoDB . [ ] Support Redis . [ ] Support Minio . [ ] Support HBase . [ ] Support ElasticSearch . [ ] Support other storages.
Cache Storage : Cache Storage is where the response from LLMs, such as ChatGPT, is stored. Cached responses are retrieved to assist in evaluating similarity and are returned to the requester if there is a good semantic match. At present, GPTCache supports SQLite and offers a universally accessible interface for extension of this module.
- [x] Support SQLite .
[x] Support SQLite .
[LINK: SQLite](https://sqlite.org/docs.html)
- [x] Support DuckDB .
[x] Support DuckDB .
- [x] Support PostgreSQL .
[x] Support PostgreSQL .
- [x] Support MySQL .
[x] Support MySQL .
- [x] Support MariaDB .
[x] Support MariaDB .
- [x] Support SQL Server .
[x] Support SQL Server .
- [x] Support Oracle .
[x] Support Oracle .
- [ ] Support MongoDB .
[ ] Support MongoDB .
- [ ] Support Redis .
[ ] Support Redis .
- [ ] Support Minio .
[ ] Support Minio .
- [ ] Support HBase .
[ ] Support HBase .
- [ ] Support ElasticSearch .
[ ] Support ElasticSearch .
- [ ] Support other storages.
[ ] Support other storages.
- Vector Store :
The Vector Store module helps find the K most similar requests from the input request’s extracted embedding. The results can help assess similarity. GPTCache provides a user-friendly interface that supports various vector stores, including Milvus, Zilliz Cloud, and FAISS. More options will be available in the future. [x] Support Milvus , an open-source vector database for production-ready AI/LLM applicaionts. [x] Support Zilliz Cloud , a fully-managed cloud vector database based on Milvus. [x] Support Milvus Lite , a lightweight version of Milvus that can be embedded into your Python application. [x] Support FAISS , a library for efficient similarity search and clustering of dense vectors. [x] Support Hnswlib , header-only C++/python library for fast approximate nearest neighbors. [x] Support PGVector , open-source vector similarity search for Postgres. [x] Support Chroma , the AI-native open-source embedding database. [x] Support DocArray , DocArray is a library for representing, sending and storing multi-modal data, perfect for Machine Learning applications. [ ] Support qdrant [ ] Support weaviate [ ] Support other vector databases.
Vector Store :
The Vector Store module helps find the K most similar requests from the input request’s extracted embedding. The results can help assess similarity. GPTCache provides a user-friendly interface that supports various vector stores, including Milvus, Zilliz Cloud, and FAISS. More options will be available in the future.
- [x] Support Milvus , an open-source vector database for production-ready AI/LLM applicaionts.
[x] Support Milvus , an open-source vector database for production-ready AI/LLM applicaionts.
- [x] Support Zilliz Cloud , a fully-managed cloud vector database based on Milvus.
[x] Support Zilliz Cloud , a fully-managed cloud vector database based on Milvus.
- [x] Support Milvus Lite , a lightweight version of Milvus that can be embedded into your Python application.
[x] Support Milvus Lite , a lightweight version of Milvus that can be embedded into your Python application.
[LINK: Milvus Lite](https://github.com/milvus-io/milvus-lite)
- [x] Support FAISS , a library for efficient similarity search and clustering of dense vectors.
[x] Support FAISS , a library for efficient similarity search and clustering of dense vectors.
- [x] Support Hnswlib , header-only C++/python library for fast approximate nearest neighbors.
[x] Support Hnswlib , header-only C++/python library for fast approximate nearest neighbors.
[LINK: Hnswlib](https://github.com/nmslib/hnswlib)
- [x] Support PGVector , open-source vector similarity search for Postgres.
[x] Support PGVector , open-source vector similarity search for Postgres.
[LINK: PGVector](https://github.com/pgvector/pgvector)
- [x] Support Chroma , the AI-native open-source embedding database.
[x] Support Chroma , the AI-native open-source embedding database.
[LINK: Chroma](https://github.com/chroma-core/chroma)
- [x] Support DocArray , DocArray is a library for representing, sending and storing multi-modal data, perfect for Machine Learning applications.
[x] Support DocArray , DocArray is a library for representing, sending and storing multi-modal data, perfect for Machine Learning applications.
[LINK: DocArray](https://github.com/docarray/docarray)
- [ ] Support qdrant
[ ] Support qdrant
- [ ] Support weaviate
[ ] Support weaviate
- [ ] Support other vector databases.
[ ] Support other vector databases.
- Cache Manager :
The Cache Manager is responsible for controlling the operation of both the Cache Storage and Vector Store . Eviction Policy :
Currently, GPTCache makes decisions about evictions based solely on the number of lines. This approach can result in inaccurate resource evaluation and may cause out-of-memory (OOM) errors. We are actively investigating and developing a more sophisticated strategy. [x] Support LRU eviction policy. [x] Support FIFO eviction policy. [ ] Support more complicated eviction policies.
Cache Manager :
The Cache Manager is responsible for controlling the operation of both the Cache Storage and Vector Store .
- Eviction Policy :
Currently, GPTCache makes decisions about evictions based solely on the number of lines. This approach can result in inaccurate resource evaluation and may cause out-of-memory (OOM) errors. We are actively investigating and developing a more sophisticated strategy. [x] Support LRU eviction policy. [x] Support FIFO eviction policy. [ ] Support more complicated eviction policies.
Eviction Policy :
Currently, GPTCache makes decisions about evictions based solely on the number of lines. This approach can result in inaccurate resource evaluation and may cause out-of-memory (OOM) errors. We are actively investigating and developing a more sophisticated strategy.
- [x] Support LRU eviction policy.
[x] Support LRU eviction policy.
- [x] Support FIFO eviction policy.
[x] Support FIFO eviction policy.
- [ ] Support more complicated eviction policies.
[ ] Support more complicated eviction policies.
- Similarity Evaluator :
This module collects data from both the Cache Storage and Vector Store , and uses various strategies to determine the similarity between the input request and the requests from the Vector Store . Based on this similarity, it determines whether a request matches the cache. GPTCache provides a standardized interface for integrating various strategies, along with a collection of implementations to use. The following similarity definitions are currently supported or will be supported in the future: [x] The distance we obtain from the Vector Store . [x] A model-based similarity determined using the GPTCache/albert-duplicate-onnx model from ONNX . [x] Exact matches between the input request and the requests obtained from the Vector Store . [x] Distance represented by applying linalg.norm from numpy to the embeddings. [ ] BM25 and other similarity measurements. [ ] Support other model serving framework such as PyTorch. Note :Not all combinations of different modules may be compatible with each other. For instance, if we disable the Embedding Extractor , the Vector Store may not function as intended. We are currently working on implementing a combination sanity check for GPTCache .
Similarity Evaluator :
This module collects data from both the Cache Storage and Vector Store , and uses various strategies to determine the similarity between the input request and the requests from the Vector Store . Based on this similarity, it determines whether a request matches the cache. GPTCache provides a standardized interface for integrating various strategies, along with a collection of implementations to use. The following similarity definitions are currently supported or will be supported in the future:
- [x] The distance we obtain from the Vector Store .
[x] The distance we obtain from the Vector Store .
- [x] A model-based similarity determined using the GPTCache/albert-duplicate-onnx model from ONNX .
[x] A model-based similarity determined using the GPTCache/albert-duplicate-onnx model from ONNX .
- [x] Exact matches between the input request and the requests obtained from the Vector Store .
[x] Exact matches between the input request and the requests obtained from the Vector Store .
- [x] Distance represented by applying linalg.norm from numpy to the embeddings.
[x] Distance represented by applying linalg.norm from numpy to the embeddings.
- [ ] BM25 and other similarity measurements.
[ ] BM25 and other similarity measurements.
- [ ] Support other model serving framework such as PyTorch.
[ ] Support other model serving framework such as PyTorch.
Note :Not all combinations of different modules may be compatible with each other. For instance, if we disable the Embedding Extractor , the Vector Store may not function as intended. We are currently working on implementing a combination sanity check for GPTCache .

## 😇 Roadmap #

Coming soon! Stay tuned!

## 😍 Contributing #

We are extremely open to contributions, be it through new features, enhanced infrastructure, or improved documentation.
For comprehensive instructions on how to contribute, please refer to our contribution guide .

--------------------