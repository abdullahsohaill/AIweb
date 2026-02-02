# Docs
**URL:** https://automata.readthedocs.io/en/latest
**Page Title:** Automata: The Future is Self-Written — Automata documentation
--------------------

- Automata: The Future is Self-Written
- Edit on GitHub
[LINK: Edit on GitHub](https://github.com/emrgnt-cmplxty/Automata/blob/main/docs/index.rst)

## Automata: The Future is Self-Written 

Automata is an evolving, fully autonomous, self-programming Artificial Intelligence system. It utilizes Large Language Models like GPT-4 and a vector database to document, search, and write code, paving the path for the creation of AGI.
[LINK: Automata](https://github.com/emrgnt-cmplxty/Automata)
Getting Started
For those looking to embark on a journey with Automata, our quick-start guides are your first steps to understanding and implementing the project’s core features:
- For setup instructions, refer to our detailed setup guide
For setup instructions, refer to our detailed setup guide
- Learn how to create your own embeddings
Learn how to create your own embeddings
- Run your own agent
Run your own agent
Key Features
Automata comes with several core features, designed to promote a rich and interactive AI development experience. Each feature has associated examples and API documentation to ease your understanding and usage.
These features include, in order of complexity:
- `Embeddings`_ : Documentations on how to generate code embeddings for Automata Interpreter codebase.
`Embeddings`_ : Documentations on how to generate code embeddings for Automata Interpreter codebase.
- `Code and Documentation Generation`_ : Guides on comprehensive code and documentation generation forming the backbone of Automata’s self-programming ability.
`Code and Documentation Generation`_ : Guides on comprehensive code and documentation generation forming the backbone of Automata’s self-programming ability.
- Indexing : In-depth tutorials on creating and using SCIP indices for the Automata Search.
Indexing : In-depth tutorials on creating and using SCIP indices for the Automata Search.
- Execution : Detailed information about executing advanced coding tasks using downstream tooling.
Execution : Detailed information about executing advanced coding tasks using downstream tooling.
- Automata Agent : Complete guide on how to run an Automata agent, including trivial and non-trivial instruction execution.
Automata Agent : Complete guide on how to run an Automata agent, including trivial and non-trivial instruction execution.
Live Status
Stay Connected
Other
You can find a demo and a rough schematic diagram of the system on our GitHub page. For further information, including installation, usage and how to contribute, refer to the respective sections below.
[LINK: demo](https://github.com/emrgnt-cmplxty/Automata/assets/68796651/2e1ceb8c-ac93-432b-af42-c383ea7607d7)
Note
Please ensure you read our contribution guidelines and adhere to the code of conduct .
[LINK: contribution guidelines](https://github.com/emrgnt-cmplxty/Automata/blob/main/CONTRIBUTING.md)
[LINK: code of conduct](https://github.com/emrgnt-cmplxty/Automata/blob/main/CODE_OF_CONDUCT.md)
The following module documents are auto-generated via the run-doc-embedding pipeline. Please bear with us as the documentation is still a work in progress.
- Agent Guide OpenAIAutomataAgentConfigBuilder OpenAIAutomataAgent
- OpenAIAutomataAgentConfigBuilder
- OpenAIAutomataAgent
- Creating Your Own Embeddings Configure the pyright-scip repository Update the Code Embeddings Build and Embed the Docs
- Configure the pyright-scip repository
- Update the Code Embeddings
- Build and Embed the Docs
[LINK: Build and Embed the Docs](embedding_guide.html#build-and-embed-the-docs)
- Frequently Asked Questions
- Setup Create Local Environment Install the Project Setup Pre-commit Hooks Configure Environment Variables Detect Operating System Fetch Submodules Install and Initialize Git LFS
- Create Local Environment
- Install the Project
- Setup Pre-commit Hooks
- Configure Environment Variables
- Detect Operating System
- Fetch Submodules
- Install and Initialize Git LFS
- agent agent instances Agent Class AgentTaskInstructions AgentToolkitNames OpenAIAgentToolkitBuilder OpenAIAutomataAgent OpenAIAutomataAgentInstance UnknownToolError Agent Class AgentTaskInstructions AgentToolkitNames OpenAIAgentToolkitBuilder OpenAIAutomataAgent OpenAIAutomataAgentInstance UnknownToolError agent instances
- agent
- instances
- Agent Class
- AgentTaskInstructions
- AgentToolkitNames
- OpenAIAgentToolkitBuilder
- OpenAIAutomataAgent
- OpenAIAutomataAgentInstance
- UnknownToolError
- Agent Class
- AgentTaskInstructions
- AgentToolkitNames
- OpenAIAgentToolkitBuilder
- OpenAIAutomataAgent
- OpenAIAutomataAgentInstance
- UnknownToolError
- agent
- instances
- cli
- code_handling py py
- code_parsers py Directory DirectoryManager Directory DirectoryManager py
- Directory
- DirectoryManager
- Directory
- DirectoryManager
- code_writers py
- config base openai_agent AgentConfig AgentConfigBuilder OpenAIAutomataAgentConfig TemplateFormatter AgentConfig AgentConfigBuilder OpenAIAutomataAgentConfig TemplateFormatter base config_base openai_agent
- base
- openai_agent
- AgentConfig
- AgentConfigBuilder
- OpenAIAutomataAgentConfig
- TemplateFormatter
- AgentConfig
- AgentConfigBuilder
- OpenAIAutomataAgentConfig
- TemplateFormatter
- base
- config_base
- openai_agent
- context_providers SymbolProviderRegistry SymbolProviderSynchronizationContext SymbolProviderRegistry SymbolProviderSynchronizationContext
- SymbolProviderRegistry
- SymbolProviderSynchronizationContext
- SymbolProviderRegistry
- SymbolProviderSynchronizationContext
- core base base
- base
- base
- embedding EmbeddingBuilder EmbeddingHandler EmbeddingSimilarityCalculator EmbeddingBuilder EmbeddingHandler EmbeddingSimilarityCalculator
- EmbeddingBuilder
- EmbeddingHandler
- EmbeddingSimilarityCalculator
- EmbeddingBuilder
- EmbeddingHandler
- EmbeddingSimilarityCalculator
- eval Eval EvalResult agent tool
- Eval
- EvalResult
- agent
- tool
- experimental search code_parsers memory_store search symbol_embedding tools
- search
- code_parsers
- memory_store
- search
- symbol_embedding
- tools
- github_management GitHubClient RepositoryClient GitHubClient RepositoryClient
[LINK: github_management](github_management/index.html)
- GitHubClient
[LINK: GitHubClient](github_management/git_hub_client.html)
- RepositoryClient
[LINK: RepositoryClient](github_management/repository_client.html)
- GitHubClient
[LINK: GitHubClient](github_management/git_hub_client.html)
- RepositoryClient
[LINK: RepositoryClient](github_management/repository_client.html)
- llm foundation providers LLMChatCompletionProvider LLMConversation LLMConversationDatabaseProvider LLMChatCompletionProvider LLMConversation LLMConversationDatabaseProvider eval foundation llm_base providers
- foundation
- providers
- LLMChatCompletionProvider
- LLMConversation
- LLMConversationDatabaseProvider
- LLMChatCompletionProvider
- LLMConversation
- LLMConversationDatabaseProvider
- eval
- foundation
- llm_base
- providers
- memory_store AgentConversationDatabase SymbolCodeEmbeddingHandler AgentConversationDatabase OpenAIAutomataConversationDatabase SymbolCodeEmbeddingHandler
- AgentConversationDatabase
- SymbolCodeEmbeddingHandler
- AgentConversationDatabase
- OpenAIAutomataConversationDatabase
- SymbolCodeEmbeddingHandler
- navigation py automata.navigation.directory.Directory DirectoryManager File Node automata.navigation.directory.Directory DirectoryManager File Node py
- automata.navigation.directory.Directory
- DirectoryManager
- File
- Node
- automata.navigation.directory.Directory
- DirectoryManager
- File
- Node
- retrievers py py
- singletons DependencyFactory OpenAIAutomataAgentToolkitRegistry ParsingStrategy PyModuleLoader RepositoryClient DependencyFactory OpenAIAutomataAgentToolkitRegistry ParsingStrategy PyModuleLoader RepositoryClient
- DependencyFactory
- OpenAIAutomataAgentToolkitRegistry
- ParsingStrategy
- PyModuleLoader
- RepositoryClient
- DependencyFactory
- OpenAIAutomataAgentToolkitRegistry
- ParsingStrategy
- PyModuleLoader
- RepositoryClient
- symbol base graph GraphBuilder GraphProcessor ISymbolProvider Symbol SymbolDescriptor SymbolGraph SymbolReference GraphBuilder GraphProcessor ISymbolProvider Symbol SymbolDescriptor SymbolGraph SymbolReference base graph symbol_base
- base
- graph
- GraphBuilder
- GraphProcessor
- ISymbolProvider
- Symbol
- SymbolDescriptor
- SymbolGraph
- SymbolReference
- GraphBuilder
- GraphProcessor
- ISymbolProvider
- Symbol
- SymbolDescriptor
- SymbolGraph
- SymbolReference
- base
- graph
- symbol_base
- symbol_embedding ChromaSymbolEmbeddingVectorDatabase JSONSymbolEmbeddingVectorDatabase SymbolCodeEmbeddingBuilder SymbolDocEmbedding SymbolEmbedding SymbolEmbeddingHandler ChromaSymbolEmbeddingVectorDatabase JSONSymbolEmbeddingVectorDatabase SymbolCodeEmbeddingBuilder SymbolDocEmbedding SymbolEmbedding SymbolEmbeddingHandler
- ChromaSymbolEmbeddingVectorDatabase
- JSONSymbolEmbeddingVectorDatabase
- SymbolCodeEmbeddingBuilder
- SymbolDocEmbedding
- SymbolEmbedding
- SymbolEmbeddingHandler
- ChromaSymbolEmbeddingVectorDatabase
- JSONSymbolEmbeddingVectorDatabase
- SymbolCodeEmbeddingBuilder
- SymbolDocEmbedding
- SymbolEmbedding
- SymbolEmbeddingHandler
- tasks AutomataAgentTaskDatabase AutomataTask AutomataTaskEnvironment AutomataTaskExecutor AutomataTaskRegistry IAutomataTaskExecution Task TaskEnvironment AutomataAgentTaskDatabase AutomataTask AutomataTaskEnvironment AutomataTaskExecutor AutomataTaskRegistry IAutomataTaskExecution Task TaskEnvironment
- AutomataAgentTaskDatabase
- AutomataTask
- AutomataTaskEnvironment
- AutomataTaskExecutor
- AutomataTaskRegistry
- IAutomataTaskExecution
- Task
- TaskEnvironment
- AutomataAgentTaskDatabase
- AutomataTask
- AutomataTaskEnvironment
- AutomataTaskExecutor
- AutomataTaskRegistry
- IAutomataTaskExecution
- Task
- TaskEnvironment
- tests unit MockRepositoryClient MockRepositoryClient unit
- unit
- MockRepositoryClient
- MockRepositoryClient
- unit
- tools base builders AgentToolFactory AgentToolFactory base builders tool_base
- base
- builders
- AgentToolFactory
- AgentToolFactory
- base
- builders
- tool_base

--------------------