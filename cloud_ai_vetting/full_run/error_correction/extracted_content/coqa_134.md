# CoQA
**URL:** https://stanfordnlp.github.io/coqa
**Page Title:** CoQA: A Conversational Question Answering Challenge
--------------------

- Home

## CoQA

## A Conversational Question Answering Challenge

## What is CoQA?

CoQA is a large-scale dataset for building Co nversational Q uestion A nswering systems. The goal of the CoQA challenge is to measure the ability of machines to understand a text passage and answer a series of interconnected questions that appear in a conversation. CoQA is pronounced as coca .
CoQA contains 127,000+ questions with answers collected from 8000+ conversations. 
Each conversation  
is collected by pairing two crowdworkers to chat about a passage in the form of questions and answers. 
The unique features of CoQA include 1) the questions are conversational; 2) the answers can be free-form text; 3) each answer also comes with an evidence subsequence highlighted in the passage; and 4) the passages are collected from seven diverse domains.
CoQA has a lot of challenging phenomena not present in existing reading comprehension datasets, e.g., coreference and pragmatic reasoning.

## Download

Browse the examples in CoQA:
- Browse CoQA
Download a copy of the dataset in json format:
- Download Training Set (47 MB)
- Download Dev Set (9 MB)

## Evaluation

To evaluate your models, use the official evaluation script. To run the evaluation, use python evaluate-v1.0.py --data-file <path_to_dev-v1.0.json> --pred-file <path_to_predictions> .
- Evaluation Script
- Sample Prediction File (on Dev Set)
- FAQ
Once you are satisfied with your model performance on the dev set, you submit it to get the official scores on the test sets. We have two test sets, an in-domain set which constitutes the domains present in the training and the dev sets, and an out-of-domain set which constitutes unseen domains (see the paper for more details). To preserve the integrity of the test results, we do not release the test set to the public. Follow this tutorial on how to submit your model for an official evaluation:
[LINK: Submission Tutorial](https://github.com/stanfordnlp/coqa-baselines/blob/master/codalab.md)

## License

CoQA contains passages from seven domains. We make five of these public under the following licenses:
- Literature and Wikipedia passages are shared under CC BY-SA 4.0 license.
- Children's stories are collected from MCTest which comes with MSR-LA license.
[LINK: MSR-LA](https://github.com/mcobzarenco/mctest/blob/master/data/MCTest/LICENSE.pdf)
- Middle/High school exam passages are collected from RACE which comes with its own license.
- News passages are collected from the DeepMind CNN dataset which comes with Apache license.
[LINK: Apache](https://github.com/deepmind/rc-data/blob/master/LICENSE)

## Questions?

Ask us questions at our google group or at siva.reddy@mila.quebec or danqic@cs.princeton.edu .

## Acknowledgements

We thank the SQuAD team for allowing us to use their code and templates for generating this website.
[LINK: SQuAD team](https://rajpurkar.github.io/SQuAD-explorer/)

## Leaderboard

Stanford University
Zhuiyi Technology
WeChatAI
Zhuiyi Technology
WeChatAI
MSRA + SDRG
WeChatAI
Xiaoming
[LINK: https://github.com/stevezheng23/xlnet_extension_tf](https://github.com/stevezheng23/xlnet_extension_tf)
MSRA + SDRG
Joint Laboratory of HIT and iFLYTEK Research
Microsoft Research Asia
Joint Laboratory of HIT and iFLYTEK Research
Microsoft Research Asia
NEUKG
Beijing Kingsoft AI Lab
Sogou Search AI Group
[LINK: https://github.com/sogou/SMRCToolkit](https://github.com/sogou/SMRCToolkit)
Fudan University NLP Lab
Anonymous
Microsoft Dynamics 365 AI Research
Joint Laboratory of HIT and iFLYTEK Research
Netease Games AI Lab
Anonymous
Microsoft Speech and Dialogue Research Group
[LINK: https://github.com/Microsoft/SDNet](https://github.com/Microsoft/SDNet)
Nanjing University
Northwestern Polytechnical University
NTT Media Intelligence Laboratories
single model
SIAT-NLP
Tsinghua University CoAI Lab
National Taiwan University, MiuLab
RPI and IBM Research
Microsoft Speech and Dialogue Research Group
[LINK: https://github.com/Microsoft/SDNet](https://github.com/Microsoft/SDNet)
SIAT NLP Group
Allen Institute for Artificial Intelligence
single model
Nanjing University
Beijing Normal University
Stanford University
Beijing University of Posts and Telecommunications
Allen Institute for Artificial Intelligence
Fudan University NLP Lab
University of Science and Technology of China
Peking University
Stanford University
Stanford University

--------------------