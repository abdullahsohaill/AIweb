# LMEval
**URL:** https://opensource.googleblog.com/2025/05/announcing-lmeval-an-open-ource-framework-cross-model-evaluation.html
**Page Title:** Announcing LMEval: An Open Source Framework for Cross-Model Evaluation | Google Open Source Blog
--------------------


## Google Open Source Blog

The latest news from Google on open source releases, major projects, events, and outreach programs for early career developers.

### Announcing LMEval: An Open Source Framework for Cross-Model Evaluation

## Announcing LMEval: An Open Source Framework for Cross-Model Evaluation

## Simplifying Cross-Provider Model Benchmarking

At InCyber Forum Europe in April, we open sourced LMEval , a large model evaluation framework, to help others accurately and efficiently compare how models from various providers perform across benchmark datasets. This announcement coincided with a joint talk with Giskard about our collaboration to increase trust in model safety and security. Giskard uses LMeval to run the Phare benchmark that independently evaluates popular models' security and safety .
[LINK: LMEval](https://github.com/google/lmeval)

## Rapid Changes in the Landscape of Large Models

New Large Language Models (LLMs) are released constantly, often promising improvements and new features. To keep up with this fast-paced lifecycle, developers, researchers, and organizations must quickly and reliably evaluate if those newer models are better suited for their specific applications. So far, rapid model evaluation has proven difficult, as it requires tools that allow scalable, accurate, easy-to-use, cross-provider benchmarking.

## Introducing LMEval: Simplifying Cross-Provider Model Benchmarking

To address this challenge, we are excited to introduce LMEval ( L arge M odel Eval uator), an open source framework that Google developed to streamline the evaluation of LLMs across diverse benchmark datasets and model providers. LMEval is designed from the ground up to be accurate, multimodal, and easy-to-use. Its key features include:
- Multi-Provider Compatibility : Evaluating models shouldn't require wrestling with different APIs for each provider. LMEval leverages the LiteLLM framework to offer out-of-the-box compatibility with major model providers including Google, OpenAI, Anthropic, Ollama, and Hugging Face. You can define your benchmark once and run it consistently across various models with minimal code changes.
- Incremental & Efficient Evaluation: Re-running an entire benchmark suite every time a new model or version is released is slow, inefficient and costly. LMEval's intelligent evaluation engine plans and executes evaluations incrementally. It runs only the necessary evaluations for new models, prompts, or questions, saving significant time and compute resources. Its multi-threaded engine further accelerates this process.
- Multimodal & Multi-Metric Support : Modern foundation models go beyond text. LMEval is designed for multimodal evaluation, supporting benchmarks that include text, images and code. Adding new modalities is straightforward. Furthermore, it supports various scoring metrics to support a wide range of benchmark formats from boolean questions, to multi-choices, to free form generation. Additionally, LMEval provides support for safety/punting detection.
- Scalable & Secure Storage : To store benchmark results in a secure and efficient manner, LMEval utilizes a self-encrypting SQLite database. This approach protects benchmark data and results from inadvertent crawling/indexing while they stay easily accessible through LMEval.

## Getting Started with LMEval

Creating and running evaluations with LMEval is designed to be intuitive. Here's a simplified example demonstrating how to evaluate two Gemini model versions on a benchmark:
The LMEval GitHub repository includes example notebooks to help you get started.
[LINK: LMEval GitHub repository](https://github.com/google/lmeval)

## Visualizing Results with LMEvalboard

Understanding benchmark results requires more than just summary statistics. To help with this, LMEval includes LMEvalboard, a companion dashboard tool that offers an interactive visualization of how models stack up against each other. LMEvalboard provides valuable insights into model strengths and weaknesses, complementing traditional raw evaluation data.
LMEvalboard allows you to:
- View Overall Performance : Quickly compare all models' accuracy across the entire benchmark.
- Analyze a Single Model : Dive deep into a specific model's performance characteristics across different categories using radar charts and drill down on specific examples of failures
- Perform Head-to-Head Comparisons: Directly compare two models, visualizing their performance differences across categories and examine specific questions where they disagree.

## Try LMEval Today!

We invite you to explore LMEval, use it for your own evaluations, and contribute to its development by heading to the LMEval GitHub repository: https://github.com/google/lmeval
[LINK: LMEval GitHub repository: https://github.com/google/lmeval](https://github.com/google/lmeval)

## Acknowledgements

LMEval would not have been possible without the help of many people, including: Luca Invernizzi, Lenin Simicich, Marianna Tishchenko, Amanda Walker, and many other Googlers.

--------------------