# tests](./tests/test_retrieve.py) and [documentation
**URL:** https://wi2trier.github.io/cbrkit
**Page Title:** cbrkit API documentation
--------------------


## cbrkit

🌟 GitHub Project 🌟
[LINK: 🌟 GitHub Project 🌟](https://github.com/wi2trier/cbrkit)
CBRkit is a customizable and modular toolkit for Case-Based Reasoning (CBR) in Python.
It provides a set of tools for loading cases and queries, defining similarity measures, and retrieving cases based on a query.
The toolkit is designed to be flexible and extensible, allowing you to define custom similarity measures or use built-in ones.
Retrieval pipelines are declared by composing these metrics, and the toolkit provides utility functions for applying them on a casebase.
Additionally, it offers ready-to-use API and CLI interfaces for easy integration into your projects.
The library is fully typed, enabling autocompletion and type checking in modern IDEs like VSCode and PyCharm.
To get started, we provide a demo project which contains a casebase and a predefined retriever.
Further examples can be found in our tests and documentation .
The following modules are part of CBRkit:
[LINK: demo project](https://github.com/wi2trier/cbrkit-demo)
[LINK: documentation](https://wi2trier.github.io/cbrkit/)
- cbrkit.loaders and cbrkit.dumpers : Functions for loading and exporting cases and queries.
- cbrkit.sim : Similarity functions for common data types and some utility functions such as cache , combine , transpose , etc. cbrkit.sim.strings : String similarity measures (Levenshtein, Jaro, semantic, etc.). cbrkit.sim.numbers : Numeric similarity measures (linear, exponential, threshold). cbrkit.sim.collections : Similarity measures for collections and sequences (Jaccard, DTW, Smith-Waterman). cbrkit.sim.embed : Embedding-based similarity functions with caching support. cbrkit.sim.graphs : Graph similarity algorithms including GED, A*, VF2, and more. cbrkit.sim.taxonomy : Taxonomy-based similarity functions. cbrkit.sim.generic : Generic similarity functions (equality, tables, static). cbrkit.sim.attribute_value : Similarity for attribute-value based data. cbrkit.sim.pooling : Functions for aggregating multiple similarity values. cbrkit.sim.aggregator : Combines multiple local measures into global scores.
- cbrkit.sim.strings : String similarity measures (Levenshtein, Jaro, semantic, etc.).
- cbrkit.sim.numbers : Numeric similarity measures (linear, exponential, threshold).
- cbrkit.sim.collections : Similarity measures for collections and sequences (Jaccard, DTW, Smith-Waterman).
- cbrkit.sim.embed : Embedding-based similarity functions with caching support.
- cbrkit.sim.graphs : Graph similarity algorithms including GED, A*, VF2, and more.
- cbrkit.sim.taxonomy : Taxonomy-based similarity functions.
- cbrkit.sim.generic : Generic similarity functions (equality, tables, static).
- cbrkit.sim.attribute_value : Similarity for attribute-value based data.
- cbrkit.sim.pooling : Functions for aggregating multiple similarity values.
- cbrkit.sim.aggregator : Combines multiple local measures into global scores.
- cbrkit.retrieval : Functions for defining and applying retrieval pipelines, includes BM25 retrieval, rerankers, etc.
- cbrkit.adapt : Adaptation generator functions for adapting cases based on a query.
- cbrkit.reuse : Functions for defining and applying reuse pipelines.
- cbrkit.eval : Evaluation metrics for retrieval results including precision, recall, and custom metrics.
- cbrkit.model : Data models for graphs and results.
- cbrkit.cycle : CBR cycle implementation.
- cbrkit.typing : Generic type definitions for defining custom functions.
- cbrkit.synthesis : Functions for working on a casebase with LLMs to create new insights, e.g., in a RAG context.

## Installation

The library is available on PyPI , so you can install it with pip :
It comes with several optional dependencies for certain tasks like NLP which can be installed with:
where EXTRA_NAME is one of the following:
- all : All optional dependencies
- api : REST API Server
- cli : Command Line Interface (CLI)
- eval : Evaluation tools for common metrics like precision and recall
- graphs : Graph libraries like networkx and rustworkx
- llm : Large Language Models (LLM) APIs like Ollama and OpenAI
- nlp : Standalone NLP tools levenshtein , nltk , openai , and spacy
- timeseries : Time series similarity measures like dtw and smith_waterman
- transformers : Advanced NLP tools based on pytorch and transformers
Alternatively, you can also clone this git repository and install CBRKit and its dependencies via uv: uv sync --all-extras

## Loading Cases

The first step is to load cases and queries.
We provide predefined functions for the following formats:
- csv
- json
- toml
- xml
- yaml
- py (object inside of a python file).
Loading one of those formats can be done via the file function:
Additionally, CBRkit also integrates with polars and pandas for loading data frames.
The following example shows how to load cases and queries from a CSV file using polars :

## Defining Queries

CBRkit expects the type of the queries to match the type of the cases.
You may define a single query directly in Python as a dict:
If you have a collection of queries, you can load them using the same loader functions as for the cases.
In case your query collection only contains a single entry, you can use the singleton function to extract it.

## Similarity Measures and Aggregation

The next step is to define similarity measures for the cases and queries.
It is possible to define custom measures, use built-in ones, or combine both.

### Custom Similarity Measures

In CBRkit, a similarity measure is defined as a function that compares two arguments (a case and a query) and returns a similarity score: sim = f(x, y) .
It also supports pipeline-based similarity measures that are popular in NLP where a list of tuples is passed to the similarity measure: sims = f([(x1, y1), (x2, y2), ...]) .
This generic approach allows you to define custom similarity measures for your specific use case.
For instance, the following function, which can be used to compare a string attribute of a case and a query, not only checks for strict equality, but also for partial matches (e.g., x = "blue" and y = "light blue" ):
Please note: CBRkit inspects the signature of custom similarity functions to perform some checks.
You need to make sure that the two parameters are named x and y , otherwise CBRkit will throw an error.

### Built-in Similarity Measures

CBRkit contains a comprehensive selection of built-in similarity measures for various data types in the module cbrkit.sim .
They are provided through generator functions that allow you to customize the behavior of the built-in measures.
Please note: Calling these functions returns a similarity function itself that has the signature sim = f(x, y) .
An overview of all available similarity measures can be found in the module documentation .
[LINK: module documentation](https://wi2trier.github.io/cbrkit/cbrkit/sim.html)

### Graph Similarity

CBRkit provides extensive support for graph similarity through various algorithms:
Available graph algorithms include:
- astar : A* search for optimal graph edit distance
- vf2 : VF2 algorithm for (sub)graph isomorphism
- lap : Linear assignment problem solver
- greedy : Fast greedy matching
- brute_force : Exhaustive search for small graphs
- dfs : Depth-first search based matching

### Global Similarity and Aggregation

When dealing with cases that are not represented through elementary data types like strings, we need to aggregate individual measures to obtain a global similarity score.
We provide a predefined aggregator that transforms a list of similarities into a single score.
It can be used with custom and/or built-in measures.
For the common use case of attribute-value based data, CBRkit provides a predefined global similarity measure that can be used as follows:
The attribute_value function lets you define measures for each attribute of the cases/queries as well as the aggregation function.
It also allows to use custom measures like the color_similarity function defined above.
Please note: The custom measure is not executed (i.e., there are no parenthesis at the end), but instead passed as a reference to the attribute_value function.
You may even nest similarity functions to create measures for object-oriented cases:

## Retrieval

The final step is to retrieve cases based on the loaded queries.
The cbrkit.retrieval module provides utility functions for this purpose.
You first build a retrieval pipeline by specifying a global similarity function and optionally a limit for the number of retrieved cases.
This retriever can then be applied on a casebase to retrieve cases for a given query.
Our result has the following attributes:
- similarities : A dictionary containing the similarity scores for each case.
- ranking A list of case indices sorted by their similarity score.
- casebase The casebase containing only the retrieved cases (useful for downstream tasks).
An example using the provided cars-1k dataset can be found under examples/cars_retriever.py .
[LINK: examples/cars_retriever.py](https://github.com/wi2trier/cbrkit/blob/main/examples/cars_retriever.py)
In some cases, it is useful to combine multiple retrieval pipelines, for example when applying the MAC/FAC pattern where a cheap pre-filter is applied to the whole casebase before a more expensive similarity measure is applied on the remaining cases.
To use this pattern, first create the corresponding retrievers using the builder:
Then apply all of them sequentially by passing them as a list or tuple to the apply_query function:
The result has the following two attributes:
- final_step : Result of the last retriever in the list.
- steps : A list of results for each retriever in the list.
Both final_step and each entry in steps have the same attributes as discussed previously.
The returned result also has these entries which are an alias for the corresponding entries in final_step (i.e., result.ranking == result.final_step.ranking ).

## Adaptation Functions

Case adaptation is a crucial step in the CBR cycle that allows us to modify retrieved cases to better suit the current query.
CBRkit offers both built-in adaptation functions for common scenarios and the flexibility to define custom adaptation logic.
Please note: cbrkit.adapt contains the built-in adaption functions. To apply these (or custom adaption functions) to your actual casebase, please refer to Reuse .

### Custom Adaptation Functions

In CBRkit, an adaptation function is defined as a function that takes two arguments (a case and a query) and returns an adapted case: adapted = f(case, query) .
For more complex scenarios, CBRkit also supports two additional types of adaptation functions:
- Map functions that operate on the entire casebase: adapted = f(casebase, query)
- Reduce functions that select and adapt a single case: key, adapted = f(casebase, query)
This generic approach allows you to define custom adaptation functions for your specific use case.
For instance, the following function replaces a case value with the query value if they differ:
Please note: CBRkit inspects the signature of custom adaptation functions to determine their type.
Make sure that the parameters are named either case and query for pair functions, or casebase and query for map/reduce functions.

### Built-in Adaptation Functions

CBRkit contains adaptation functions for common data types like strings and numbers in the module cbrkit.adapt .
They are provided through generator functions that allow you to customize the behavior of the built-in functions.
For example, a number aggregator can be obtained as follows:
Please note: Calling the function cbrkit.adapt.numbers.aggregate returns an adaptation function that takes a collection of values and returns an adapted value.
For the common use case of attribute-value based data, CBRkit provides a predefined global adapter that can be used as follows:
The attribute_value function lets you define adaptation functions for each attribute of the cases.
You may even nest adaptation functions to handle object-oriented cases.
An overview of all available adaptation functions can be found in the module documentation .
[LINK: module documentation](https://wi2trier.github.io/cbrkit/cbrkit/adapt.html)

## Reuse

The reuse phase applies adaptation functions to retrieved cases. The cbrkit.reuse module provides utility functions for this purpose. You first build a reuse pipeline by specifying a global adaptation function:
This reuser can then be applied to the retrieval result to adapt cases based on a query:
Our result has the following attributes:
- adaptations : A dictionary containing the adapted values for each case.
- ranking : A list of case indices matching the retrieval result.
- casebase : The casebase containing only the adapted cases.
Multiple reuse pipelines can be combined by passing them as a list or tuple:
The result structure follows the same pattern as the retrieval results with final_step and steps attributes.

## Advanced Retrieval

### BM25 Retrieval

CBRkit includes a BM25 retriever for text-based retrieval:

### Combining Multiple Retrievers

The combine function allows merging results from multiple retrievers:

### Distributed Processing

For large-scale retrieval, use the distribute wrapper:

## Evaluation

CBRkit provides evaluation tools through the cbrkit.eval module for assessing the quality of retrieval results.
The basic evaluation function cbrkit.eval.compute expects the following arguments:
- qrels : Ground truth relevance scores for query-case pairs. A higher value means a higher relevance.
- run : Retrieval similarity scores for query-case pairs.
- metrics : A list of metrics to compute.
You can evaluate retrieval results directly with the functions cbrkit.eval.retrieval and cbrkit.eval.retrieval_step .

### Custom Metrics

Users can provide custom metric functions that implement the signature defined in the cbrkit.typing.EvalMetricFunc protocol:
You can then pass your custom metric function to the compute function:

### Built-in Metrics

The module also supports standard Information Retrieval metrics through ranx like precision , recall , and f1 .
A complete list is available in the ranx documentation .
Additionally, CBRkit provides two custom metrics not available in ranx:
[LINK: ranx documentation](https://amenra.github.io/ranx/metrics/)
- correctness : Measures how well the ranking preserves the relevance ordering (-1 to 1).
- completeness : Measures what fraction of relevance pairs are preserved (0 to 1).
All of them can be computed at different cutoff points by appending @k , e.g., precision@5 .
We also offer a function to automatically generate a list of metrics for different cutoff points:

## Synthesis

In the context of CBRkit, synthesis refers to creating new insights from the cases which were retrieved in a previous retrieval step, for example in a RAG context. CBRkit builds a synthesizer using the function cbrkit.synthesis.build with a provider and a prompt . A synthesizer maps a Result (obtained in the retrieval step) to an LLM output (can be a string or structurized). An example can be found in examples/cars_rag.py .
[LINK: examples/cars_rag.py](https://github.com/wi2trier/cbrkit/blob/main/examples/cars_rag.py)
The following providers are currently supported if a valid API key is stored the respective environment variable:
- Anthropic ( ANTHROPIC_API_KEY )
- Cohere ( CO_API_KEY )
- Google ( GOOGLE_API_KEY )
- Ollama
- OpenAI ( OPENAI_API_KEY )
The respective provider class in cbrkit.synthesis.providers has to be initialized with the model name and a response type (either str or a Pydantic model for structured output). Further model options like temperature , seed , max_tokens , etc. can also be specified here.
[LINK: Pydantic model](https://docs.pydantic.dev/latest/concepts/models/)
A prompt produces an LLM input based on the specified instructions , an optional encoder (which maps a case or query to a string) and optional metadata . For a list of the currently included prompts, please refer to the module documentation
[LINK: module documentation](https://wi2trier.github.io/cbrkit/cbrkit/synthesis/prompts.html)
If the casebase is small enough, that it fits inside the LLM's context window, you can use CBRKit's synthesis as follows:

### Working with large casebases

Because the built-in default and document_aware prompt functions include the entire casebase as context, the LLM input can be quite long when working with a large casebase.
Because of this, in this case, we recommend transposing the cases (e.g., truncate every case to a fixed length) and/or apply chunking.
CBRKit's transpose prompt allows to transpose cases and queries before they are passed to the main prompt function. This allows shortening entries like so:
Instead of using cbrkit.synthesis.apply_result , CBRKit also provides the cbrkit.synthesis.chunks function to process the synthesis in batches. The partial results can then be aggregated using a pooling prompt.
The complete version of this example can be found under examples/cars_rag_large.py .

## Logging

CBRkit integrates with the logging module to provide a unified logging interface.
By default, logging is not configured, you can activate by placing the following code in your project's __init__.py file:

## REST API and CLI

In order to use the built-in API and CLI, you need to define a retriever/reuser in a Python module using the function cbrkit.retrieval.build and/or cbrkit.reuse.build .
For example, the file ./retriever_module.py could contain the following code:
Our custom retriever can then be specified for the API/CLI using standard Python module syntax: retriever_module:custom_retriever .

### CLI

When installing with the cli extra, CBRkit provides a command line interface:
Please visit the documentation for more information on how to use the CLI.
[LINK: documentation](https://wi2trier.github.io/cbrkit/cbrkit/cli.html)

### API

When installing with the api extra, CBRkit provides a REST API server:
After starting the server, you can access the API documentation at http://localhost:8080/docs .

--------------------