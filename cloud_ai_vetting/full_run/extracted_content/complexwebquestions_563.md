# **ComplexWebQuestions**
**URL:** https://huggingface.co/datasets/drt/complex_web_questions
**Page Title:** drt/complex_web_questions · Datasets at Hugging Face
--------------------


## Dataset Card for Dataset Name

### Dataset Summary

A dataset for answering complex questions that require reasoning over multiple web snippets
ComplexWebQuestions is a new dataset that contains a large set of complex questions in natural language, and can be used in multiple ways:
- By interacting with a search engine, which is the focus of our paper (Talmor and Berant, 2018);
- As a reading comprehension task: we release 12,725,989 web snippets that are relevant for the questions, and were collected during the development of our model;
- As a semantic parsing task: each question is paired with a SPARQL query that can be executed against Freebase to retrieve the answer.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

- English

## Dataset Structure

QUESTION FILES
The dataset contains 34,689 examples divided into 27,734 train, 3,480 dev, 3,475 test.
each containing:
NOTE: test set does not contain “answer” field. For test evaluation please send email to alontalmor@mail.tau.ac.il .
WEB SNIPPET FILES
The snippets files consist of 12,725,989 snippets each containing
PLEASE DON”T USE CHROME WHEN DOWNLOADING THESE FROM DROPBOX (THE UNZIP COULD FAIL)
"question_ID”: the ID of related question, containing at least 3 instances of the same ID (full question, split1, split2); 
"question": The natural language complex question; 
"web_query": Query sent to the search engine. 
“split_source”: 'noisy supervision split' or ‘ptrnet split’, please train on examples containing “ptrnet split” when comparing to Split+Decomp  from https://arxiv.org/abs/1807.09623 “split_type”: 'full_question' or ‘split_part1' or ‘split_part2’ please use ‘composition_answer’ in question of type composition and split_type: “split_part1” when training a reading comprehension model on splits as in Split+Decomp  from https://arxiv.org/abs/1807.09623 (in the rest of the cases use the original answer).
"web_snippets": ~100 web snippets per query. Each snippet includes Title,Snippet. They are ordered according to Google results.
With a total of
10,035,571 training set snippets
1,350,950 dev set snippets
1,339,468 test set snippets

### Source Data

The original files can be found at this dropbox link

### Licensing Information

Not specified

### Citation Information

### Contributions

Thanks for yuancu for contributing this dataset.
[LINK: yuancu](https://github.com/yuancu)
[LINK: Repository: github.com](https://github.com/alontalmor/WebAsKB)

## Models trained or fine-tuned on drt/complex_web_questions

## Papers for drt/complex_web_questions


--------------------