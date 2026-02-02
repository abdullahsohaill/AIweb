# Granite-3.3-8b-instruct
**URL:** https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
**Page Title:** ibm-granite/granite-3.3-8b-instruct · Hugging Face
--------------------


## Granite-3.3-8B-Instruct

Model Summary: Granite-3.3-8B-Instruct is a 8-billion parameter 128K context length language model fine-tuned for improved reasoning and instruction-following capabilities. Built on top of Granite-3.3-8B-Base, the model delivers significant gains on benchmarks for measuring generic performance including AlpacaEval-2.0 and Arena-Hard, and improvements in mathematics, coding, and instruction following. It supports structured reasoning through <think></think> and <response></response> tags, providing clear separation between internal thoughts and final outputs. The model has been trained on a carefully balanced combination of permissively licensed data and curated synthetic tasks.
- Developers: Granite Team, IBM
- Website : Granite Docs
[LINK: Granite Docs](https://www.ibm.com/granite/docs/)
- Release Date : April 16th, 2025
- License: Apache 2.0
Supported Languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese. However, users may finetune this Granite model for languages beyond these 12 languages.
Intended Use: This model is designed to handle general instruction-following tasks and can be integrated into AI assistants across various domains, including business applications.
Capabilities
- Thinking
- Summarization
- Text classification
- Text extraction
- Question-answering
- Retrieval Augmented Generation (RAG)
- Code related tasks
- Function-calling tasks
- Multilingual dialog use cases
- Long-context tasks including long document/meeting summarization, long document QA, etc.
Generation: This is a simple example of how to use Granite-3.3-8B-Instruct model.
Install the following libraries:
Then, copy the snippet from the section that is relevant for your use case.
Example Outputs
- thinking=True
- thinking=False
Evaluation Results:
Training Data: Overall, our training data is largely comprised of two key sources: (1) publicly available datasets with permissive license, (2) internal synthetically generated data targeted to enhance reasoning capabilites.
Infrastructure: We train Granite-3.3-8B-Instruct using IBM's super computing cluster, Blue Vela, which is outfitted with NVIDIA H100 GPUs. This cluster provides a scalable and efficient infrastructure for training our models over thousands of GPUs.
Ethical Considerations and Limitations: Granite-3.3-8B-Instruct builds upon Granite-3.3-8B-Base, leveraging both permissively licensed open-source and select proprietary data for enhanced performance. Since it inherits its foundation from the previous model, all ethical considerations and limitations applicable to Granite-3.3-8B-Base remain relevant.
Resources
- ⭐️ Learn about the latest updates with Granite: https://www.ibm.com/granite
- 📄 Get started with tutorials, best practices, and prompt engineering advice: https://www.ibm.com/granite/docs/
[LINK: https://www.ibm.com/granite/docs/](https://www.ibm.com/granite/docs/)
- 💡 Learn about the latest Granite learning resources: https://github.com/ibm-granite-community/
[LINK: https://github.com/ibm-granite-community/](https://github.com/ibm-granite-community/)
[1] Evaluated using OLMES (except AttaQ and Arena-Hard scores)
[LINK: OLMES](https://github.com/allenai/olmes)
[2] Added regex for more efficient asnwer extraction.
[3] Modified the implementation to handle some of the issues mentioned here

## Model tree for ibm-granite/granite-3.3-8b-instruct

Base model

## Spaces using ibm-granite/granite-3.3-8b-instruct 13

## Collection including ibm-granite/granite-3.3-8b-instruct


--------------------