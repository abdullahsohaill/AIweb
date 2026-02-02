# DeepSeek-V3
**URL:** https://huggingface.co/deepseek-ai/DeepSeek-V3-0324
**Page Title:** deepseek-ai/DeepSeek-V3-0324 · Hugging Face
--------------------


## DeepSeek-V3-0324

## Features

DeepSeek-V3-0324 demonstrates notable improvements over its predecessor, DeepSeek-V3, in several key aspects.

### Reasoning Capabilities

- Significant improvements in benchmark performance: MMLU-Pro: 75.9 → 81.2 (+5.3) GPQA: 59.1 → 68.4 (+9.3) AIME: 39.6 → 59.4 (+19.8) LiveCodeBench: 39.2 → 49.2 (+10.0)
- MMLU-Pro: 75.9 → 81.2 (+5.3)
- GPQA: 59.1 → 68.4 (+9.3)
- AIME: 39.6 → 59.4 (+19.8)
- LiveCodeBench: 39.2 → 49.2 (+10.0)

### Front-End Web Development

- Improved the executability of the code
- More aesthetically pleasing web pages and game front-ends

### Chinese Writing Proficiency

- Enhanced style and content quality: Aligned with the R1 writing style Better quality in medium-to-long-form writing
Enhanced style and content quality:
- Aligned with the R1 writing style
- Better quality in medium-to-long-form writing
- Feature Enhancements Improved multi-turn interactive rewriting Optimized translation quality and letter writing
Feature Enhancements
- Improved multi-turn interactive rewriting
- Optimized translation quality and letter writing

### Chinese Search Capabilities

- Enhanced report analysis requests with more detailed outputs

### Function Calling Improvements

- Increased accuracy in Function Calling, fixing issues from previous V3 versions

## Usage Recommendations

### System Prompt

In the official DeepSeek web/app, we use the same system prompt with a specific date.
For example,

### Temperature

In our web and application environments, the temperature parameter $T_{model}$ is set to 0.3. Because many users use the default temperature 1.0 in API call, we have implemented an API temperature $T_{api}$ mapping mechanism that adjusts the input API temperature value of 1.0 to the most suitable model temperature setting of 0.3.
T m o d e l = T a p i × 0.3 ( 0 ≤ T a p i ≤ 1 ) T_{model} = T_{api} \times 0.3 \quad (0 \leq T_{api} \leq 1) T m o d e l ​ = T a p i ​ × 0.3 ( 0 ≤ T a p i ​ ≤ 1 )
T m o d e l = T a p i − 0.7 ( 1 < T a p i ≤ 2 ) T_{model} = T_{api} - 0.7 \quad (1 < T_{api} \leq 2) T m o d e l ​ = T a p i ​ − 0.7 ( 1 < T a p i ​ ≤ 2 )
Thus, if you call V3 via API, temperature 1.0 equals to the model temperature 0.3.

### Prompts for File Uploading and Web Search

For file uploading, please follow the template to create prompts, where {file_name}, {file_content} and {question} are arguments.
For Web Search, {search_results}, {cur_date}, and {question} are arguments.
For Chinese query, we use the prompt:
For English query, we use the prompt:

## How to Run Locally

The model structure of DeepSeek-V3-0324 is exactly the same as DeepSeek-V3. Please visit DeepSeek-V3 repo for more information about running this model locally.
[LINK: DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)
This model supports features such as function calling, JSON output, and FIM completion. For instructions on how to construct prompts to use these features, please refer to DeepSeek-V2.5 repo.
NOTE: Hugging Face's Transformers has not been directly supported yet.

## License

This repository and the model weights are licensed under the MIT License .

## Citation

## Contact

If you have any questions, please raise an issue or contact us at service@deepseek.com .

## Model tree for deepseek-ai/DeepSeek-V3-0324

## Spaces using deepseek-ai/DeepSeek-V3-0324 100

## Collection including deepseek-ai/DeepSeek-V3-0324

## Paper for deepseek-ai/DeepSeek-V3-0324

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
deepseek-ai/DeepSeek-V3-0324 is supported by the following Inference Providers:

--------------------