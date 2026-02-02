# Spider (Yale University)
**URL:** https://yale-lily.github.io/spider
**Page Title:** Spider: Yale Semantic Parsing and Text-to-SQL Challenge
--------------------


## Spider 1.0

## Yale Semantic Parsing and Text-to-SQL Challenge

## What is Spider?

Nov 12, 2024: We have released Spider 2.0 full paper , data and code . Follow the guideline to submit your scores to the leaderboard !
[LINK: Spider 2.0](https://spider2-sql.github.io/)
[LINK: data](https://github.com/xlang-ai/Spider2/blob/main/spider2/README.md)
[LINK: code](https://github.com/xlang-ai/Spider2)
[LINK: guideline](https://docs.google.com/document/d/1sCobAqJZcko-Vl3biOycwvCIR7kTwBPrhsgVfvaX1Fg/edit?tab=t.0)
[LINK: leaderboard](https://spider2-sql.github.io/)
Aug 28, 2024: The early access version of Spider 2.0 (a more realistic and challenging text-to-SQL task) is now available! We expect to release the whole dataset in 1-2 weeks. As this is a preliminary release, there may be errors. Your feedback would be invaluable in refining the dataset!
[LINK: Spider 2.0](https://spider2-sql.github.io/)
[LINK: Spider 2.0 Text-to-SQL (ICLR 25)](https://spider2-sql.github.io/)
[LINK: Spider2-V (NeurIPS 24)](https://spider2-v.github.io/)
[LINK: OSWorld (NeurIPS 24)](https://os-world.github.io/)
[LINK: DS-1000 Challenge (ICML'23)](https://ds1000-code-gen.github.io/)
[LINK: Binder Framework (ICLR '23)](https://lm-code-binder.github.io/)
[LINK: UnifiedSKG Framework (EMNLP'22)](https://github.com/hkunlp/unifiedskg)
[LINK: SParC Challenge (ACL'19)](https://yale-lily.github.io/sparc)
[LINK: CoSQL Challenge (EMNLP'19)](https://yale-lily.github.io/cosql)

## News

- 11/12/2024 We have released Spider 2.0 full paper , data and code . Follow the guideline to submit your scores to the leaderboard .
[LINK: Spider 2.0](https://spider2-sql.github.io/)
[LINK: data](https://github.com/xlang-ai/Spider2/blob/main/spider2/README.md)
[LINK: code](https://github.com/xlang-ai/Spider2)
[LINK: guideline](https://docs.google.com/document/d/1sCobAqJZcko-Vl3biOycwvCIR7kTwBPrhsgVfvaX1Fg/edit?tab=t.0)
[LINK: leaderboard](https://spider2-sql.github.io/)
- 08/28/2024 The early access version of Spider 2.0 (a more realistic and challenging text-to-SQL task) is now available! As this is a preliminary release, there may be errors. Your feedback would be invaluable in refining the dataset!
[LINK: Spider 2.0](https://spider2-sql.github.io/)
- 07/15/2024 Spider 2.0-vision (Benchmarking Multimodal Agents on Automating Data Science and Engineering Workflows) is out! Spider 2.0-SQL (much more realistic and challenging than Spider 1.0!) will be released in August.
[LINK: Spider 2.0-vision (Benchmarking Multimodal Agents on Automating Data Science and Engineering Workflows)](https://spider2-v.github.io/)
- 02/05/2024 We will no longer accept submissions for Spider 1.0 evaluations or update its leaderboard. The test set of Spider 1.0 has already been released (check the Spider dataset link below). Look forward to the release of Spider 2.0, a more realistic and challenging benchmark in the era of LLMs, expected this March June . Stay tuned!
- 08/10/2023 Please check out XLANG Lab for Building LLM/VLM Agents !
- 05/27/2023 Please check out Dr.Spider, a robustness evaluation benchmark based on Spider, from AWS AI Lab for studying robustness in semantic parsing!
- 11/20/2022 Please check out our recent work DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation . Please check out examples, data, and code on the DS-1000 project site !!
[LINK: DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation](https://ds1000-code-gen.github.io/)
[LINK: DS-1000 project site](https://ds1000-code-gen.github.io/)
- 10/18/2022 Please check out our recent work Binder: an easy but sota neural-symbolic built on GPT-3 Codex & SQL/Python interpreter . It injects GPT-3 Codex prompt API calls in programming languages! Please check out Binder demo, code, paper, and video on the Binder project site !!
[LINK: Binder: an easy but sota neural-symbolic built on GPT-3 Codex & SQL/Python interpreter](https://lm-code-binder.github.io/)
[LINK: Binder project site]([https://github.com/hkunlp/unifiedskg](https://lm-code-binder.github.io/))
- 01/18/2022 Please check out our recent work UnifiedSKG: Unifying and Multi-Tasking Structured Knowledge Grounding with Text-to-Text Language Models . We open-sourced simple but SOTA/strong models for 21 tasks including text-to-SQL! Please check out our code in the UnifiedSKG repo !!
[LINK: UnifiedSKG repo](https://github.com/hkunlp/unifiedskg)
- 03/11/2021 Please check out a nice work from Google Research (including new Spider splits ) for studying compositional generalization in semantic parsing!
[LINK: new Spider splits](https://github.com/google-research/language/tree/master/language/nqg)
- 11/15/2020 We will use Test Suite Accuracy as our official evaluation metric for Spider, SParC, and CoSQL. Please find the evaluation code from here . Also, Notice that Test results after May 02, 2020 are reported on the new release (collected some annotation errors).
[LINK: here](https://github.com/taoyds/test-suite-sql-eval)
- 08/03/2020 Corrected "column_name" and "column_name_original" mismatches in 2 dbs ("scholar" and "formula_1") in tables.json, and reparsed SQL queries (this only affects some models (e.g. RATSQL) which use our parsed SQL as the SQL input). Please download the Spider dataset from this page again.
- 06/07/2020 We corrected some annotation errors and label mismatches (not errors) in Spider dev and test sets (~4% of dev examples updated, click here for more details). Please download the Spider dataset from this page again.
[LINK: here](https://github.com/taoyds/spider/commit/25fcd85d9b6e94acaeb5e9172deadeefeed83f5e#diff-18b0a730a7b0d29b0a78a5070d971d49)
- 01/16/2020 For value prediction (in order to compute the execution accuracy), your model should be able to 1) copy from the question inputs, 2) retrieve from the database content (database content is available), or 3) generate numbers (e.g. 3 in "LIMIT 3").
- 9/24/2019 (Min et al., EMNLP 2019) translated Spider to Chinese! Check out the Chinese challenge page .
[LINK: (Min et al., EMNLP 2019)](https://frcchang.github.io/pub/emnlp2019.2.pdf)
[LINK: the Chinese challenge page](https://taolusi.github.io/CSpider-explorer/)
- 5/17/2019 Our paper SParC: Cross-Domain Semantic Parsing in Context with Salesforce Research was accepted to ACL 2019! It introduces the context-dependent version of the Spider challenge: SParC !
[LINK: SParC](https://yale-lily.github.io/sparc)
- 5/17/2019 Please report any annotation errors here , we really appreciate your help and will update the data release in this summer!
[LINK: annotation errors here](https://github.com/taoyds/spider/issues/24)
- 1/14/2019 The submission tutorial is out!.
- 12/17/2018 We updated 7 sqlite database files ( issue 14 ). Please download the Spider dataset from this page again.
[LINK: issue 14](https://github.com/taoyds/spider/issues/14)
- 10/25/2018 The evaluation script and results were updated ( issue 5 ). Please download the lastest versions of the script and papers. Also, please follow instructions in issue 3 to generate the latest SQL parsing results (fixed a bug).
[LINK: issue 5](https://github.com/taoyds/spider/issues/5)
[LINK: issue 3](https://github.com/taoyds/spider/issues/3)

## Why Spider?

- ATIS, Geo, Academic : Each of them contains only a single database with a limited number of SQL queries, and has exact same SQL queries in train and test splits.
[LINK: ATIS, Geo, Academic](https://github.com/jkkummerfeld/text2sql-data)
- WikiSQL : The numbers of SQL queries and tables are significantly large. But all SQL queries are simple, and each database is only a simple table without any foreign key.
[LINK: WikiSQL](https://github.com/salesforce/WikiSQL)

## Getting Started

[LINK: Spider GitHub Page](https://github.com/taoyds/spider)

## Data Examples

## Have Questions or Want to Contribute ?

[LINK: Github issues page](https://github.com/taoyds/spider/issues)
[LINK: Tao Yu](https://taoyds.github.io/)
[LINK: Rui Zhang](https://ryanzhumich.github.io/)
[LINK: Michihiro Yasunaga](https://michiyasunaga.github.io/)

## Acknowledgement

[LINK: Pranav Rajpurkar](https://rajpurkar.github.io/)
[LINK: SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)

## Leaderboard - Execution with Values

Anonymous
Alibaba Group
[LINK: code](https://github.com/BeachWang/DAIL-SQL)
Alibaba Group
[LINK: code](https://github.com/BeachWang/DAIL-SQL)
Anonymous
University of Alberta
[LINK: code](https://github.com/MohammadrezaPourreza/Few-shot-NL2SQL-with-prompting)
Anonymous
Zhejiang University & Hundsun
[LINK: code](https://github.com/bigbigwatermalon/C3SQL)
Anonymous
Renmin University of China
[LINK: code](https://github.com/RUCKBReasoning/RESDSQL)
Anonymous
University of Alberta
[LINK: code](https://github.com/MohammadrezaPourreza/Few-shot-NL2SQL-with-prompting)
George Mason University & MIT
[LINK: code](https://github.com/Dakingrai/ood-generalization-semantic-boundary-techniques)
Anonymous
Alibaba DAMO & HKU STAR & SIAT
[LINK: code](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/graphix)
AWS AI Labs
Anonymous
Alexa AI
SJTU LUMIA & Netmind.AI
[LINK: code](https://github.com/JiexingQi/RASAT)
Anonymous
Anonymous
Element AI, a ServiceNow company
[LINK: code](https://github.com/ElementAI/picard)
Anonymous
Anonymous
Queen Mary University of London
[LINK: code](https://github.com/ygan/NatSQL)
George Mason University & MIT
[LINK: code](https://github.com/Dakingrai/ood-generalization-semantic-boundary-techniques)
Tel-Aviv University & Allen Institute for AI
[LINK: code](https://github.com/OhadRubin/SmBop)
Ant Group, ZhiXiaoBao & Ada
Salesforce Research
[LINK: code](https://github.com/salesforce/TabularSemanticParsing)
Novelis.io Research
Anonymous
Salesforce Research
[LINK: code](https://github.com/salesforce/TabularSemanticParsing)
Anonymous
Salesforce Research
[LINK: code](https://github.com/salesforce/TabularSemanticParsing)
University of Washington & Facebook AI Research

## Leaderboard - Exact Set Match without Values

[LINK: the Github page](https://github.com/taoyds/spider/tree/master/evaluation_examples)
Anonymous
Alibaba DAMO & HKU STAR & SIAT
[LINK: code](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/graphix)
Anonymous
AWS AI Labs
Southeast University & Tencent Cloud Xiaowei
Anonymous
Anonymous
Alexa AI
Alibaba DAMO
[LINK: code](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/s2sql)
Renmin University of China
[LINK: code](https://github.com/RUCKBReasoning/RESDSQL)
SJTU X-LANCE Lab & AISpeech
[LINK: code](https://github.com/rhythmcao/text2sql-lgesql)
Element AI, a ServiceNow company
[LINK: code](https://github.com/ElementAI/picard)
Anonymous
SJTU LUMIA & Netmind.AI
[LINK: code](https://github.com/JiexingQi/RASAT)
Borealis AI
[LINK: code](https://github.com/BorealisAI/DT-Fixup)
Anonymous
Anonymous
DMIR Lab
[LINK: code](https://github.com/DMIRLAB-Group/SADGA)
OCFT Gamma Big Data Lab
University of Waterloo & AWS AI Labs
[LINK: code](https://github.com/awslabs/gap-text2sql)
Anonymous
Yale & Salesforce Research
Tel-Aviv University & Allen Institute for AI
[LINK: code](https://github.com/OhadRubin/SmBop)
Ant Group, ZhiXiaoBao & Ada
Queen Mary University of London
[LINK: code](https://github.com/ygan/NatSQL)
Microsoft Research & OSU
SJTU X-LANCE Lab & AISpeech
[LINK: code](https://github.com/rhythmcao/text2sql-lgesql)
Novelis.io Research
Salesforce Research
[LINK: code](https://github.com/salesforce/TabularSemanticParsing)
SJTU X-LANCE Lab & AISpeech
Anonymous
Microsoft Research
[LINK: code](https://github.com/Microsoft/rat-sql)
Anonymous
Anonymous
Microsoft Research Asia
Salesforce Research
[LINK: code](https://github.com/salesforce/TabularSemanticParsing)
Anonymous
Anonymous
Anonymous
SJTU X-LANCE Lab & AISpeech
[LINK: code](https://github.com/rhythmcao/text2sql-lgesql)
Anonymous
Microsoft Research
[LINK: code](https://github.com/Microsoft/rat-sql)
Anonymous
Kakao Enterprise
Tel-Aviv University & Allen Institute for AI
Anonymous
University of Alberta
[LINK: code](https://github.com/MohammadrezaPourreza/Few-shot-NL2SQL-with-prompting)
Salesforce Research
[LINK: code](https://github.com/salesforce/TabularSemanticParsing)
Kakao Enterprise
Microsoft Research
[LINK: code](https://github.com/Microsoft/rat-sql)
University of Alberta
[LINK: code](https://github.com/MohammadrezaPourreza/Few-shot-NL2SQL-with-prompting)
National University of Singapore
[LINK: code](https://github.com/WING-NUS/slsql)
Anonymous
Microsoft Research Asia
Anonymous
Microsoft Research Asia
[LINK: code](https://github.com/microsoft/IRNet)
Got It R&D
[LINK: code](https://github.com/amolk/Bertrand-DR)
Anonymous
Anonymous
Yale University & Salesforce Research
[LINK: code](https://github.com/ryanzhumich/editsql)
University of Washington & Facebook AI Research
Anonymous
Anonymous
Microsoft Research Asia
Tel-Aviv University & Allen Institute for AI
[LINK: code](https://github.com/benbogin/spider-schema-gnn-global)
Anonymous
Anonymous
Microsoft Research Asia
[LINK: code](https://github.com/microsoft/IRNet)
Anonymous
Anonymous
Anonymous
Anonymous
Anonymous
Tel-Aviv University & Allen Institute for AI
[LINK: code](https://github.com/benbogin/spider-schema-gnn)
Anonymous
Allen Institute for AI
Yale University & Salesforce Research
[LINK: code](https://github.com/ryanzhumich/editsql)
Anonymous
Yale University
[LINK: code](https://github.com/taoyds/syntaxSQL)
SAP Labs Korea
Yale University
[LINK: code](https://github.com/taoyds/syntaxSQL)
Shanghai Jiao Tong University (modified by Yale)
[LINK: code](https://github.com/taoyds/spider/tree/master/baselines/sqlnet)
Yale University
[LINK: code](https://github.com/taoyds/spider/tree/master/baselines/typesql)
University of Edinburgh (modified by Yale)
[LINK: code](https://github.com/taoyds/spider/tree/master/baselines/seq2seq_attention_copy)
- (Wang et al., KDD 2022) , Alibaba DAMO
- (Ma et al., VLDB 2022) , HKUST
- (Qin et al., COLING 2022) , Alibaba DAMO
- (Usta et al., VLDB 2021) , Bilkent University
- (Min et al., EMNLP 2019) , Westlake University, Spider in Chinese
[LINK: (Min et al., EMNLP 2019)](https://frcchang.github.io/pub/emnlp2019.2.pdf)
- (Yao et al., EMNLP 2019) , OSU & Facebook AI Research
[LINK: (Yao et al., EMNLP 2019)](http://web.cse.ohio-state.edu/~sun.397/docs/MISP.pdf)
- (Shaw et al., ACL 2019) , Google
- (Shin et al., NeurlPS 2019) , UC Berkeley & MSR
- (Weir et al., SIGMOD 2019) , Brown University & TU Darmstadt
- (Baik et al., ICDE 2019) , U of Michigan & IBM

--------------------