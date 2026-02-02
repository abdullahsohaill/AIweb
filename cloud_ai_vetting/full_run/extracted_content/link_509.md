# 🔗 Link
**URL:** https://huggingface.co/learn/cookbook/en/agents
**Page Title:** Build an agent with tool-calling superpowers 🦸 using smolagents - Hugging Face Open-Source AI Cookbook
--------------------

Open-Source AI Cookbook documentation
Build an agent with tool-calling superpowers 🦸 using smolagents

## Open-Source AI Cookbook

[LINK: 2,582](https://github.com/huggingface/cookbook)
and get access to the augmented documentation experience
to get started

## Build an agent with tool-calling superpowers 🦸 using smolagents

Authored by: Aymeric Roucher
This notebook demonstrates how you can use smolagents to build awesome agents !
[LINK: smolagents](https://huggingface.co/docs/smolagents/index)
What are agents ? Agents are systems that are powered by an LLM and enable the LLM (with careful prompting and output parsing) to use specific tools to solve problems.
These tools are basically functions that the LLM couldn’t perform well by itself: for instance for a text-generation LLM like Llama-3-70B , this could be an image generation tool, a web search tool, a calculator…
What is smolagents ? It’s an library that provides building blocks to build your own agents! Learn more about it in the documentation .
[LINK: documentation](https://huggingface.co/docs/smolagents/index)
Let’s see how to use it, and which use cases it can solve.
Run the line below to install required dependencies:
Let’s login in order to call the HF Inference API:

## 1. 🏞️ Multimodal + 🌐 Web-browsing assistant

For this use case, we want to show an agent that browses the web and is able to generate images.
To build it, we simply need to have two tools ready: image generation and web search.
- For image generation, we load a tool from the Hub that uses the HF Inference API (Serverless) to generate images using Stable Diffusion.
- For the web search, we use a built-in tool.

## 2. 📚💬 RAG with Iterative query refinement & Source selection

Quick definition: Retrieval-Augmented-Generation (RAG) is “using an LLM to answer a user query, but basing the answer on information retrieved from a knowledge base”.
This method has many advantages over using a vanilla or fine-tuned LLM: to name a few, it allows to ground the answer on true facts and reduce confabulations, it allows to provide the LLM with domain-specific knowledge, and it allows fine-grained control of access to information from the knowledge base.
- Now let’s say we want to perform RAG, but with the additional constraint that some parameters must be dynamically generated. For example, depending on the user query we could want to restrict the search to specific subsets of the knowledge base, or we could want to adjust the number of documents retrieved. The difficulty is: how to dynamically adjust these parameters based on the user query?
Now let’s say we want to perform RAG, but with the additional constraint that some parameters must be dynamically generated. For example, depending on the user query we could want to restrict the search to specific subsets of the knowledge base, or we could want to adjust the number of documents retrieved. The difficulty is: how to dynamically adjust these parameters based on the user query?
- A frequent failure case of RAG is when the retrieval based on the user query does not return any relevant supporting documents. Is there a way to iterate by re-calling the retriever with a modified query in case the previous results were not relevant?
A frequent failure case of RAG is when the retrieval based on the user query does not return any relevant supporting documents. Is there a way to iterate by re-calling the retriever with a modified query in case the previous results were not relevant?
🔧 Well, we can solve the points above in a simple way: we will give our agent control over the retriever’s parameters!
➡️ Let’s show how to do this. We first load a knowledge base on which we want to perform RAG: this dataset is a compilation of the documentation pages for many huggingface packages, stored as markdown.
Now we prepare the knowledge base by processing the dataset and storing it into a vector database to be used by the retriever. We are going to use LangChain, since it features excellent utilities for vector databases:
Now that we have the database ready, let’s build a RAG system that answers user queries based on it!
We want our system to select only from the most relevant sources of information, depending on the query.
Our documentation pages come from the following sources:
👉 Now let’s build a RetrieverTool that our agent can leverage to retrieve information from the knowledge base.
Since we need to add a vectordb as an attribute of the tool, we cannot simply use the simple tool constructor with a @tool decorator: so we will follow the advanced setup highlighted in the advanced agents documentation .
[LINK: simple tool constructor](https://huggingface.co/docs/transformers/main/en/agents#create-a-new-tool)
[LINK: advanced agents documentation](https://huggingface.co/docs/transformers/main/en/agents_advanced#directly-define-a-tool-by-subclassing-tool-and-share-it-to-the-hub)

### Optional: Share your Retriever tool to Hub

To share your tool to the Hub, first copy-paste the code in the RetrieverTool definition cell to a new file named for instance retriever.py .
When the tool is loaded from a separate file, you can then push it to the Hub using the code below (make sure to login with a write access token)

### Run the agent!

What happened here? First, the agent launched the retriever with specific sources in mind ( ['transformers', 'blog'] ).
But this retrieval did not yield enough results ⇒ no problem! The agent could iterate on previous results, so it just re-ran its retrieval with less restrictive search parameters.
Thus the research was successful!
Note that using an LLM agent that calls a retriever as a tool and can dynamically modify the query and other retrieval parameters is a more general formulation of RAG , which also covers many RAG improvement techniques like iterative query refinement.

## 3. 💻 Debug Python code

Since the CodeAgent has a built-in Python code interpreter, we can use it to debug our faulty Python script!
As you can see, the agent tried the given code, gets an error, analyses the error, corrects the code and returns it after veryfing that it works!
And the final code is the corrected code:

## ➡️ Conclusion

The use cases above should give you a glimpse into the possibilities of our Agents framework!
For more advanced usage, read the documentation .
[LINK: documentation](https://huggingface.co/docs/smolagents/index)
All feedback is welcome, it will help us improve the framework! 🚀
[LINK: Update on GitHub](https://github.com/huggingface/cookbook/blob/main/notebooks/en/agents.md)

--------------------