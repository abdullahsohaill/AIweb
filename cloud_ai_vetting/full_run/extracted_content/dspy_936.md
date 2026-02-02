# DSPy
**URL:** https://dspy-docs.vercel.app
**Page Title:** DSPy
--------------------


## Programming —not prompting— LMs ¶

DSPy is a declarative framework for building modular AI software. It allows you to iterate fast on structured code , rather than brittle strings, and offers algorithms that compile AI programs into effective prompts and weights for your language models, whether you're building simple classifiers, sophisticated RAG pipelines, or Agent loops.
Instead of wrangling prompts or training jobs, DSPy (Declarative Self-improving Python) enables you to build AI software from natural-language modules and to generically compose them with different models, inference strategies, or learning algorithms. This makes AI software more reliable, maintainable, and portable across models and strategies.
tl;dr Think of DSPy as a higher-level language for AI programming ( lecture ), like the shift from assembly to C or pointer arithmetic to SQL. Meet the community, seek help, or start contributing via GitHub and Discord .
[LINK: GitHub](https://github.com/stanfordnlp/dspy)
Getting Started I: Install DSPy and set up your LM
You can authenticate by setting the OPENAI_API_KEY env variable or passing api_key below.
You can authenticate by setting the ANTHROPIC_API_KEY env variable or passing api_key below.
If you're on the Databricks platform, authentication is automatic via their SDK. If not, you can set the env variables DATABRICKS_API_KEY and DATABRICKS_API_BASE , or pass api_key and api_base below.
You can authenticate by setting the GEMINI_API_KEY env variable or passing api_key below.
First, install Ollama and launch its server with your LM.
[LINK: Ollama](https://github.com/ollama/ollama)
Then, connect to it from your DSPy code.
First, install SGLang and launch its server with your LM.
[LINK: SGLang](https://docs.sglang.ai/get_started/install.html)
If you don't have access from Meta to download meta-llama/Llama-3.1-8B-Instruct , use Qwen/Qwen2.5-7B-Instruct for example.
Next, connect to your local LM from your DSPy code as an OpenAI -compatible endpoint.
In DSPy, you can use any of the dozens of LLM providers supported by LiteLLM . Simply follow their instructions for which {PROVIDER}_API_KEY to set and how to write pass the {provider_name}/{model_name} to the constructor.
[LINK: LLM providers supported by LiteLLM](https://docs.litellm.ai/docs/providers)
Some examples:
- anyscale/mistralai/Mistral-7B-Instruct-v0.1 , with ANYSCALE_API_KEY
- together_ai/togethercomputer/llama-2-70b-chat , with TOGETHERAI_API_KEY
- sagemaker/<your-endpoint-name> , with AWS_ACCESS_KEY_ID , AWS_SECRET_ACCESS_KEY , and AWS_REGION_NAME
- azure/<your_deployment_name> , with AZURE_API_KEY , AZURE_API_BASE , AZURE_API_VERSION , and the optional AZURE_AD_TOKEN and AZURE_API_TYPE
If your provider offers an OpenAI-compatible endpoint, just add an openai/ prefix to your full model name.
Idiomatic DSPy involves using modules , which we define in the rest of this page. However, it's still easy to call the lm you configured above directly. This gives you a unified API and lets you benefit from utilities like automatic caching.

## 1) Modules help you describe AI behavior as code , not strings. ¶

To build reliable AI systems, you must iterate fast. But maintaining prompts makes that hard: it forces you to tinker with strings or data every time you change your LM, metrics, or pipeline . Having built over a dozen best-in-class compound LM systems since 2020, we learned this the hard way—and so built DSPy to decouple AI system design from messy incidental choices about specific LMs or prompting strategies.
DSPy shifts your focus from tinkering with prompt strings to programming with structured and declarative natural-language modules . For every AI component in your system, you specify input/output behavior as a signature and select a module to assign a strategy for invoking your LM. DSPy expands your signatures into prompts and parses your typed outputs, so you can compose different modules together into ergonomic, portable, and optimizable AI systems.
Getting Started II: Build DSPy modules for various tasks
Try the examples below after configuring your lm above. Adjust the fields to explore what tasks your LM can do well out of the box. Each tab below sets up a DSPy module, like dspy.Predict , dspy.ChainOfThought , or dspy.ReAct , with a task-specific signature . For example, question -> answer: float tells the module to take a question and to produce a float answer.
Possible Output:
Possible Output:
Possible Output:
Possible Output:
Possible Output:
Possible Output:
A 1500-word article on the topic, e.g.
Note that DSPy makes it straightforward to optimize multi-stage modules like this. As long as you can evaluate the final output of the system, every DSPy optimizer can tune all of the intermediate modules.
Standard prompts conflate interface ("what should the LM do?") with implementation ("how do we tell it to do that?"). DSPy isolates the former as signatures so we can infer the latter or learn it from data — in the context of a bigger program.
Even before you start using optimizers, DSPy's modules allow you to script effective LM systems as ergonomic, portable code . Across many tasks and LMs, we maintain signature test suites that assess the reliability of the built-in DSPy adapters. Adapters are the components that map signatures to prompts prior to optimization. If you find a task where a simple prompt consistently outperforms idiomatic DSPy for your LM, consider that a bug and file an issue . We'll use this to improve the built-in adapters.
[LINK: file an issue](https://github.com/stanfordnlp/dspy/issues)

## 2) Optimizers tune the prompts and weights of your AI modules. ¶

DSPy provides you with the tools to compile high-level code with natural language annotations into the low-level computations, prompts, or weight updates that align your LM with your program's structure and metrics. If you change your code or your metrics, you can simply re-compile accordingly.
Given a few tens or hundreds of representative inputs of your task and a metric that can measure the quality of your system's outputs, you can use a DSPy optimizer. Different optimizers in DSPy work by synthesizing good few-shot examples for every module, like dspy.BootstrapRS , 1 proposing and intelligently exploring better natural-language instructions for every prompt, like dspy.GEPA 2 , dspy.MIPROv2 , 3 and building datasets for your modules and using them to finetune the LM weights in your system, like dspy.BootstrapFinetune . 4 For detailed tutorials on running dspy.GEPA , please take a look at dspy.GEPA tutorials .
Getting Started III: Optimizing the LM prompts or weights in DSPy programs
A typical simple optimization run costs on the order of $2 USD and takes around 20 minutes, but be careful when running optimizers with very large LMs or very large datasets.
Optimization can cost as little as a few cents or up to tens of dollars, depending on your LM, dataset, and configuration.
Examples below rely on HuggingFace/datasets, you can install it by the command below.
This is a minimal but fully runnable example of setting up a dspy.ReAct agent that answers questions via
search from Wikipedia and then optimizing it using dspy.MIPROv2 in the cheap light mode on 500
question-answer pairs sampled from the HotPotQA dataset.
An informal run like this raises ReAct's score from 24% to 51%, by teaching gpt-4o-mini more about the specifics of the task.
Given a retrieval index to search , your favorite dspy.LM , and a small trainset of questions and ground-truth responses, the following code snippet can optimize your RAG system with long outputs against the built-in SemanticF1 metric, which is implemented as a DSPy module.
For a complete RAG example that you can run, start this tutorial . It improves the quality of a RAG system over a subset of StackExchange communities by 10% relative gain.
Possible Output (from the last line):
An informal run similar to this on DSPy 2.5.29 raises GPT-4o-mini's score 66% to 87%.
Take the dspy.MIPROv2 optimizer as an example. First, MIPRO starts with the bootstrapping stage . It takes your program, which may be unoptimized at this point, and runs it many times across different inputs to collect traces of input/output behavior for each one of your modules. It filters these traces to keep only those that appear in trajectories scored highly by your metric. Second, MIPRO enters its grounded proposal stage . It previews your DSPy program's code, your data, and traces from running your program, and uses them to draft many potential instructions for every prompt in your program. Third, MIPRO launches the discrete search stage . It samples mini-batches from your training set, proposes a combination of instructions and traces to use for constructing every prompt in the pipeline, and evaluates the candidate program on the mini-batch. Using the resulting score, MIPRO updates a surrogate model that helps the proposals get better over time.
One thing that makes DSPy optimizers so powerful is that they can be composed. You can run dspy.MIPROv2 and use the produced program as an input to dspy.MIPROv2 again or, say, to dspy.BootstrapFinetune to get better results. This is partly the essence of dspy.BetterTogether . Alternatively, you can run the optimizer and then extract the top-5 candidate programs and build a dspy.Ensemble of them. This allows you to scale inference-time compute (e.g., ensembles) as well as DSPy's unique pre-inference time compute (i.e., optimization budget) in highly systematic ways.

## 3) DSPy's Ecosystem advances open-source AI research. ¶

Compared to monolithic LMs, DSPy's modular paradigm enables a large community to improve the compositional architectures, inference-time strategies, and optimizers for LM programs in an open, distributed way. This gives DSPy users more control, helps them iterate much faster, and allows their programs to get better over time by applying the latest optimizers or modules.
The DSPy research effort started at Stanford NLP in Feb 2022, building on what we had learned from developing early compound LM systems like ColBERT-QA , Baleen , and Hindsight . The first version was released as DSP in Dec 2022 and evolved by Oct 2023 into DSPy . Thanks to 250 contributors , DSPy has introduced tens of thousands of people to building and optimizing modular LM programs.
[LINK: 250 contributors](https://github.com/stanfordnlp/dspy/graphs/contributors)
Since then, DSPy's community has produced a large body of work on optimizers, like MIPROv2 , BetterTogether , and LeReT , on program architectures, like STORM , IReRa , and DSPy Assertions , and on successful applications to new problems, like PAPILLON , PATH , WangLab@MEDIQA , UMD's Prompting Case Study , and Haize's Red-Teaming Program , in addition to many open-source projects, production applications, and other use cases .

--------------------