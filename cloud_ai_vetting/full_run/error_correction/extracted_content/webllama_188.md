# WebLlama
**URL:** https://webllama.github.io
**Page Title:** 🖥️WebLlama🦙
--------------------


## 🖥️ WebLlama🦙

[LINK: 💻 GitHub](https://github.com/McGill-NLP/webllama)
[LINK: 🏠 Homepage](https://webllama.github.io)
🎉Announcement🎉 We are thrilled to release Llama-3-8B-Web , the most capable agent built with 🦙 Llama 3 and finetuned for web navigation with dialogue. You can download the agent from the 🤗 Huggingface Model Hub .
[LINK: WebLINX](https://mcgill-nlp.github.io/weblinx/)

## About the project

[LINK: WebLINX](https://mcgill-nlp.github.io/weblinx/)

## Modeling

Our first agent is a finetuned Meta-Llama-3-8B-Instruct model, which was recently released by Meta GenAI team. We have finetuned this model on the WebLINX dataset, which contains over 100K instances of web navigation and dialogue, each collected and verified by expert annotators. We use a 24K curated subset for training the data. The model is available on the 🤗 Hugging Face Model Hub as McGill-NLP/Llama-3-8B-Web . The training and evaluation data is available on Huggingface Hub as McGill-NLP/WebLINX .
[LINK: WebLINX](https://mcgill-nlp.github.io/weblinx/)
It surpasses GPT-4V (zero-shot * ) by over 18% on the WebLINX benchmark , achieving an overall score of 28.8% on the out-of-domain test splits (compared to 10.5% for GPT-4V). It chooses more useful links (34.1% vs 18.9% seg-F1 ), clicks on more relevant elements (27.1% vs 13.6% IoU ) and formulates more aligned responses (37.5% vs 3.1% chr-F1 ).
[LINK: WebLINX](https://mcgill-nlp.github.io/weblinx/)

## Evaluation

We believe short demo videos showing how well an agent performs is NOT enough to judge an agent. Simply put, we do not know if we have a good agent if we do not have good benchmarks. We need to systematically evaluate agents on wide range of tasks, spanning from simple instruction-following web navigation to complex dialogue-guided browsing.
This is why we chose WebLINX as our first benchmark. In addition to the training split, the benchmark has 4 real-world splits, with the goal of testing multiple dimensions of generalization: new websites, new domains, unseen geographic locations, and scenarios where the user cannot see the screen and relies on dialogue . It also covers 150 websites, including booking, shopping, writing, knowledge lookup, and even complex tasks like manipulating spreadsheets.
[LINK: WebLINX](https://mcgill-nlp.github.io/weblinx/)

## Data

Although the 24K training examples from WebLINX provide a good starting point for training a capable agent, we believe that more data is needed to train agents that can generalize to a wide range of web navigation tasks. Although it has been trained and evaluated on 150 websites, there are millions of websites that has never been seen by the model, with new ones being created every day.
[LINK: WebLINX](https://mcgill-nlp.github.io/weblinx/)
This motivates us to continuously curate, compile and release datasets for training better agents. As an immediate next step, we will be incorporating Mind2Web ’s training data into the equation, which also covers over 100 websites.

## Deployment

We are working hard to make it easy for you to deploy Llama web agents to the web. We want to integrate WebLlama with existing deployment platforms, including Microsoft’s Playwright, ServiceNow Research’s BrowserGym, and other partners.

## Code

The code for finetuning the model and evaluating it on the WebLINX benchmark is available now. You can find the detailed instructions in modeling .
[LINK: WebLINX](https://mcgill-nlp.github.io/weblinx/)
[LINK: modeling](https://github.com/McGill-NLP/webllama/tree/main/modeling)

## Citation

If you use WebLlama in your research, please cite the following paper (upon which the data, training and evaluation are originally based on):

--------------------