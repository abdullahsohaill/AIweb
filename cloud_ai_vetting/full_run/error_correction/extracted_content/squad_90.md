# SQuAD
**URL:** https://rajpurkar.github.io/SQuAD-explorer
**Page Title:** The Stanford Question Answering Dataset
--------------------

- Home
- Explore 2.0
- Explore 1.1

## SQuAD 2.0

## The Stanford Question Answering Dataset

## What is SQuAD?

S tanford Qu estion A nswering D ataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span , from the corresponding reading passage, or the question might be unanswerable.
SQuAD2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones. To do well on SQuAD2.0, systems must not only answer questions when possible, but also determine when no answer is supported by the paragraph and abstain from answering.
SQuAD 1.1, the previous version of the SQuAD dataset, contains 100,000+ question-answer pairs on 500+ articles.

## Getting Started

We've built a few resources to help you get started with the dataset.
Download a copy of the dataset (distributed under the CC BY-SA 4.0 license):
- Training Set v2.0 (40 MB)
- Dev Set v2.0 (4 MB)
To evaluate your models, we have also made available the evaluation script we will use for official evaluation, along with a sample prediction file that the script will take as input. To run the evaluation, use python evaluate-v2.0.py <path_to_dev-v2.0> <path_to_predictions> .
- Evaluation Script v2.0
- Sample Prediction File (on Dev v2.0)
Once you have a built a model that works to your expectations on the dev set, you submit it to get official scores on the dev and a hidden test set. To preserve the integrity of test results, we do not release the test set to the public. Instead, we require you to submit your model so that we can run it on the test set for you. Here's a tutorial walking you through official evaluation of your model:
Because SQuAD is an ongoing effort, we expect the dataset to evolve.
To keep up to date with major changes to the dataset, please subscribe:

## Have Questions?

Ask us questions at our google group or at robinjia@stanford.edu .

## Leaderboard

SQuAD2.0 tests the ability of a system to not only answer reading comprehension questions, but also abstain when presented with a question that cannot be answered based on the provided paragraph.
Stanford University
RICOH_SRCB_DML
Ant Service Intelligence Team
RICOH_SRCB_DML
QIANXIN
QIANXIN
Shanghai Jiao Tong University
YuYang
Senseforth AI Research
RICOH_SRCB_DML
Hithink RoyalFlush
2digit-david
PINGAN Omni-Sinitic
Anonymous
Shanghai Jiao Tong University
YITU
ensemble
PINGAN Omni-Sinitic
2digit-david
Google Research & TTIC
QIANXIN
Hithink RoyalFlush
Anonymous
Shanghai Jiao Tong University
Anonymous
single model
Midea NLP Team
Midea NLP Team
Ted
single model
SPPD
Senseforth AI Research
Senseforth AI Research
Hithink RoyalFlush
ensemble
CloudWalk
SRCB_DML
QIANXIN
Google Brain & Stanford
Shanghai Jiao Tong University
Tsinghua University
SRCB_DML
Group Data & Analytics Cell | Aditya Birla Group)
Anonymous
Anonymous
Shanghai Jiao Tong University
PINGAN Omni-Sinitic
QIANXIN
CloudWalk
Senseforth AI Research
Google Research & TTIC
HAPTIK AI RESEARCH
Anonymous
Skelter Labs
Shanghai Jiao Tong University & CloudWalk
SPPD
Hithink RoyalFlush
Zheyu Ye
Google Brain & CMU
Group Data & Analytics Cell | Aditya Birla Group)
Anonymous
Studio Ousia & NAIST & RIKEN AIP
Shanghai Jiao Tong University & CloudWalk
Anonymous
Joint Laboratory of HIT and iFLYTEK Research
Facebook AI
Layer 6 AI
Google AI Language
[LINK: https://github.com/google-research/bert](https://github.com/google-research/bert)
Microsoft STCA AIC
single model
Ping An Life Insurance Company AI Team
Microsoft STCA AIC
MST/EOI
Google Brain & CMU
Shanghai Jiao Tong University
Shanghai Jiao Tong University
NEUKG
SAIL
Joint Laboratory of HIT and iFLYTEK Research
FAIR & UW
SAIL
Shanghai Jiao Tong University
Layer 6 AI
Google AI Language
[LINK: https://github.com/google-research/bert](https://github.com/google-research/bert)
PAOS
Microsoft Research Asia
Shanghai Jiao Tong University
VerifiedXiaoPAI
PAII Insight Team
Hanvon_WuHan
Google AI Language
[LINK: https://github.com/google-research/bert](https://github.com/google-research/bert)
Quant Studio
Kyonggi University (ICL) & KISTI
JAIST
FAIR & UW
JAIST
None
Anonymous
PINGAN GammaLab
Layer 6 AI NLP Team
Layer 6 AI NLP Team
single
Microsoft Research Asia
Anonymous
None
Anonymous
Google AI Language
[LINK: https://github.com/google-research/bert](https://github.com/google-research/bert)
FAIR & UW
None
2SAH
2SAH
Anonymous
PINGAN GammaLab
Georgia Institute of Technology
Joint Laboratory of HIT and iFLYTEK Research
Anonymous
AI21 Labs
Anonymous
anonymous
2SAH
Anonymous
Joint Laboratory of HIT and iFLYTEK Research
None
Anonymous
AI21 Labs
2SAH
None
AI21 Labs
None
Single Model
AI21 Labs
Seoul National University & Hyundai Motors
AITRICS
FAIR & UW
Anonymous
vinda msqjmxx
single model
Google AI Language
AI21 Labs
single model
AI21 Labs
Anonymous
NEXYS, DGIST R7
ksai
single model
Layer 6 AI
Anonymous
Quant Studio
Infosys Limited
ByteDance
Seoul National University & Hyundai Motors
single model
Hithink RoyalFlush
ByteDance
Quant Studio
Alibaba DAMO NLP
ByteDance
ByteDance
bert_finetune
single model
Anonymous
TRINITI RESEARCH LABS, Active.ai
Anonymous
Kangwon National University, Natural Language Processing Lab. & ForceWin, KP Lab.
Anonymous
single model
Anonymous
Anonymous
private
Microsoft Research Asia
THU
Single
Anonymous
Dining Philosophers
IBM Research AI
single model
Anonymous
Pingan Tech Olatop Lab
Fudan University & Liulishuo Lab
GreenflyAI
NUDT
Alibaba DAMO NLP
JAIST
Anonymous
Microsoft Business Applications AI Research
Microsoft Business Applications Group AI Research
Chonbuk National University, Cognitive Computing Lab.
Fudan University & Liulishuo Lab
2SAH
Microsoft Business Applications AI Research
UW and FAIR
Kangwon National University, Natural Language Processing Lab.
Kangwon National University in South Korea
Enliple AI
Kakao NLP Team
UW and FAIR
Fudan University & Liulishuo AI Lab
reciTAL.ai
BBD NLP Team
Allen Institute for Artificial Intelligence [modified by Stanford]
Allen Institute for Artificial Intelligence [modified by Stanford]
University of Washington [modified by Stanford]
Carnegie Mellon University

## SQuAD1.1 Leaderboard

Here are the ExactMatch (EM) and F1 scores evaluated on the test set of SQuAD v1.1.
Stanford University
LG AI Research
Studio Ousia & NAIST & RIKEN AIP
Google Brain & CMU
MST/EOI
MST/EOI
FAIR & UW
Xiaoi Research
FAIR & UW
Google AI Language
Anonymous
FAIR & UW
Xiaoi Research
Baidu NLP
Microsoft Research Asia
single model
YeonTaek Oh
Seoul National University & Hyundai Motors
Anonymous
Google AI Language
Anonymous
single model
Microsoft Research Asia
FAIR & UW
Anonymous
Google Brain & CMU
Jerry AGI Ragtag
Anonymous
Microsoft Research Asia
MST/EOI
YUANFUDAO research NLP
Google Brain & CMU
Microsoft Research Asia
YUANFUDAO research NLP
University of North Texas
YUANFUDAO research NLP
Anonymous
Google Brain & CMU
Google Brain & CMU
Joint Laboratory of HIT and iFLYTEK Research
Microsoft Research Asia & NUDT
YUANFUDAO research NLP
Microsoft Research Asia
Alibaba iDST NLP
KTNET
Google Brain & CMU
NUDT and Fudan University
Single
Microsoft Research Asia
TRINITI RESEARCH LABS, Active.ai
Tencent DPDAC NLP
Microsoft Research Asia & NUDT
Microsoft Research Asia
Microsoft Research Asia & NUDT
Kangwon National University, Natural Language Processing Lab.
TU Darmstadt
Google Brain & CMU
Allen Institute for Artificial Intelligence
Microsoft Research Asia & NUDT
THU
Microsoft Research Asia & NUDT
aviqa team
single model
Yiwise NLP Group
Yiwise NLP Group
Joint Laboratory of HIT and iFLYTEK Research
Brno University of Technology
QA geeks
Microsoft Research Asia & NUDT
Microsoft Research Asia
Samsung Research
NUDT and Fudan University
Microsoft Business AI Solutions Team
Alibaba iDST NLP
Joint Laboratory of HIT and iFLYTEK
Kangwon National University, Natural Language Processing Lab.
single model
Microsoft Business AI Solutions Team
Salesforce Research
Kangwon National University, Natural Language Processing Lab.
Allen Institute for Artificial Intelligence
Kakao NLP Team
Alibaba iDST NLP
aviqa team
CMU
UW and FAIR
single model
Zhejiang University
single
Joint Laboratory of HIT and iFLYTEK Research
QA geeks
UW and FAIR
Tencent DPDAC NLP
Tel-Aviv University
Facebook AI Research
CMU
YUANFUDAO research NLP
Kangwon National University in South Korea
Microsoft Business AI Solutions Team
FAIR
in review
Microsoft Research Asia
CMU
Microsoft Business AI Solutions team
Joint Laboratory of HIT and iFLYTEK
York University
Eigen Technology & Zhejiang University
aviqa team
Tel-Aviv University
Tsinghua University
Salesforce Research
Sean
Eigen Technology & Zhejiang University
guotong1988
Salesforce Research
MSR Redmond
Alibaba iDST NLP
Facebook AI Research
CMU
BBD NLP Team
ensemble model
NUDT and Fudan University
Kangwon National University in South Korea
CMU
Tsinghua University
Joint Laboratory of HIT and iFLYTEK Research
Allen Institute for AI & University of Washington
CMU
CMU
Facebook AI Research
IBM Research
USTC & National Research Council Canada & York University
CMU
Peking University
guotong1988
Allen Institute for Artificial Intelligence
aviqa team
Kangwon National University in South Korea
guotong1988
Salesforce Research
NUS
Eigen Technology & Zhejiang University
NUDT and Fudan University
College of Computer & Information Science, SouthWest University, Chongqing, China
Samsung Research
UFL
USTC & National Research Council Canada & York University
New York University
Facebook AI Research
MSR Redmond
German Research Center for Artificial Intelligence
Google NY, Tel-Aviv University
IBM Research
Technical University of Vienna
single model
CMU
KAIST & AIBrain & Crosscert
Peking University
CMU
German Research Center for Artificial Intelligence
Single Model
Allen Institute for AI & University of Washington
Singapore Management University
Allen Institute for AI
Fudan University
single model
Salesforce Research
Singapore Management University
University of Montreal
NLPR, CASIA
Carnegie Mellon University
University of Montreal
University of Montreal
IBM
BUAA & MSRA
Singapore Management University
Singapore Management University
BUAA & MSRA
Anonymous

--------------------