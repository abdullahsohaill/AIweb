# xLAM-8x22b-r
**URL:** https://huggingface.co/Salesforce/xLAM-8x22b-r
**Page Title:** Salesforce/xLAM-8x22b-r · Hugging Face
--------------------

[Homepage] | [Paper] | [Github] | [Discord] | [Blog] | [Community Demo]
[LINK: [Github]](https://github.com/SalesforceAIResearch/xLAM)
Welcome to the xLAM model family! Large Action Models (LAMs) are advanced large language models designed to enhance decision-making and translate user intentions into executable actions that interact with the world. LAMs autonomously plan and execute tasks to achieve specific goals, serving as the brains of AI agents. They have the potential to automate workflow processes across various domains, making them invaluable for a wide range of applications. The model release is exclusively for research purposes. A new and enhanced version of xLAM will soon be available exclusively to customers on our Platform.
Trained with ActionStudio: A Lightweight Framework for Data and Training of Action Models .

## Table of Contents

- Model Series
- Repository Overview
- Benchmark Results
- Usage Basic Usage with Huggingface
- Basic Usage with Huggingface
- License
- Citation

## Model Series

We provide a series of xLAMs in different sizes to cater to various applications, including those optimized for function-calling and general agent applications:
For our Function-calling series (more details are included at here ), we also provide their quantized GGUF files for efficient deployment and execution. GGUF is a file format designed to efficiently store and load large language models, making GGUF ideal for running AI models on local devices with limited resources, enabling offline functionality and enhanced privacy.
[LINK: GGUF](https://huggingface.co/docs/hub/en/gguf)
For more details, check our GitHub and paper .
[LINK: GitHub](https://github.com/SalesforceAIResearch/xLAM)

## Check Latest Examples on Interaction with xLAM

Here is the latest examples and tokenizer on interacting with xLAM models.

## Repository Overview

This repository is about the general tool use series. For more specialized function calling models, please take a look into our fc series here .
The instructions will guide you through the setup, usage, and integration of our model series with HuggingFace.

### Framework Versions

- Transformers 4.41.0
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1

## Usage

### Basic Usage with Huggingface

To use the model from Huggingface, please first install the transformers library:
Please note that, our model works best with our provided prompt format. 
It allows us to extract JSON output that is similar to the function-calling mode of ChatGPT .
[LINK: function-calling mode of ChatGPT](https://platform.openai.com/docs/guides/function-calling)
We use the following example to illustrate how to use our model for 1) single-turn use case, and 2) multi-turn use case
Then you should be able to see the following output string in JSON format:
We also support multi-turn interaction with our model series. Here is the example of next round of interaction from the above example:
This would be the corresponding output:
We highly recommend to use our provided prompt format and helper functions to yield the best function-calling performance of our model.
Prompt:
Output:

## Benchmark Results

Note: Bold and Underline results denote the best result and the second best result for Success Rate, respectively.

### Berkeley Function-Calling Leaderboard (BFCL)

Table 1: Performance comparison on BFCL-v2 leaderboard (cutoff date 09/03/2024). The rank is based on the overall accuracy, which is a weighted average of different evaluation categories. "FC" stands for function-calling mode in contrast to using a customized "prompt" to extract the function calls.

### Webshop and ToolQuery

Table 2: Testing results on Webshop and ToolQuery. Bold and Underline results denote the best result and the second best result for Success Rate, respectively.

### Unified ToolQuery

Table 3: Testing results on ToolQuery-Unified. Bold and Underline results denote the best result and the second best result for Success Rate, respectively. Values in brackets indicate corresponding performance on ToolQuery

### ToolBench

Table 4: Pass Rate on ToolBench on three distinct scenarios. Bold and Underline results denote the best result and the second best result for each setting, respectively. The results for xLAM-8x22b-r are unavailable due to the ToolBench server being down between 07/28/2024 and our evaluation cutoff date 09/03/2024.

## License

The model is distributed under the CC-BY-NC-4.0 license.

## Ethical Considerations

This release is for research purposes only in support of an academic paper. Our models, datasets, and code are not specifically designed or evaluated for all downstream purposes. We strongly recommend users evaluate and address potential concerns related to accuracy, safety, and fairness before deploying this model. We encourage users to consider the common limitations of AI, comply with applicable laws, and leverage best practices when selecting use cases, particularly for high-risk scenarios where errors or misuse could significantly impact people’s lives, rights, or safety. For further guidance on use cases, refer to our AUP and AI AUP.

## Citation

If you find this repo helpful, please consider to cite our papers:

## Model tree for Salesforce/xLAM-8x22b-r

## Dataset used to train Salesforce/xLAM-8x22b-r

## Spaces using Salesforce/xLAM-8x22b-r 3

## Collection including Salesforce/xLAM-8x22b-r

## Papers for Salesforce/xLAM-8x22b-r


--------------------