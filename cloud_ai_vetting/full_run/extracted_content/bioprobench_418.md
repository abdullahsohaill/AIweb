# BioProBench
**URL:** https://huggingface.co/datasets/GreatCaptainNemo/BioProBench
**Page Title:** GreatCaptainNemo/BioProBench · Datasets at Hugging Face
--------------------

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer , and open a discussion for direct support.
[LINK: how to configure the dataset viewer](https://huggingface.co/docs/hub/datasets-data-files-configuration)
[LINK: open a discussion](/datasets/GreatCaptainNemo/BioProBench/discussions/new?title=Dataset+Viewer+issue%3A+DatasetGenerationCastError&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AError+code%3A+++DatasetGenerationCastError%0AException%3A++++DatasetGenerationCastError%0AMessage%3A++++++An+error+occurred+while+generating+the+dataset%0A%0AAll+the+data+files+must+have+the+same+columns%2C+but+at+some+point+there+are+4+new+columns+%28%7B%27instruction%27%2C+%27system_prompt%27%2C+%27input%27%2C+%27output%27%7D%29+and+5+missing+columns+%28%7B%27context%27%2C+%27corrupted_text%27%2C+%27error_description%27%2C+%27corrected_text%27%2C+%27is_correct%27%7D%29.%0A%0AThis+happened+while+the+json+dataset+builder+was+generating+data+using%0A%0Ahf%3A%2F%2Fdatasets%2FGreatCaptainNemo%2FBioProBench%2FGEN_test.json+%28at+revision+69b0bd533367c45bdca9973a1dfb36e02b5e6336%29%0A%0APlease+either+edit+the+data+files+to+have+matching+columns%2C+or+separate+them+into+different+configurations+%28see+docs+at+https%3A%2F%2Fhf.co%2Fdocs%2Fhub%2Fdatasets-manual-configuration%23multiple-configurations%29%0ATraceback%3A++++Traceback+%28most+recent+call+last%29%3A%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+1871%2C+in+_prepare_split_single%0A++++++++++++++++++writer.write_table%28table%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Farrow_writer.py%22%2C+line+643%2C+in+write_table%0A++++++++++++++++++pa_table+%3D+table_cast%28pa_table%2C+self._schema%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Ftable.py%22%2C+line+2293%2C+in+table_cast%0A++++++++++++++++++return+cast_table_to_schema%28table%2C+schema%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Ftable.py%22%2C+line+2241%2C+in+cast_table_to_schema%0A++++++++++++++++++raise+CastError%28%0A++++++++++++++datasets.table.CastError%3A+Couldn%27t+cast%0A++++++++++++++system_prompt%3A+string%0A++++++++++++++instruction%3A+string%0A++++++++++++++input%3A+string%0A++++++++++++++output%3A+list%3Citem%3A+string%3E%0A++++++++++++++++child+0%2C+item%3A+string%0A++++++++++++++id%3A+string%0A++++++++++++++type%3A+string%0A++++++++++++++--+schema+metadata+--%0A++++++++++++++pandas%3A+%27%7B%22index_columns%22%3A+%5B%5D%2C+%22column_indexes%22%3A+%5B%5D%2C+%22columns%22%3A+%5B%7B%22name%22%3A%27+%2B+808%0A++++++++++++++to%0A++++++++++++++%7B%27context%27%3A+%7B%27next_step%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27prior_step%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27purpose%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%7D%2C+%27corrupted_text%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27corrected_text%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27is_correct%27%3A+Value%28dtype%3D%27bool%27%2C+id%3DNone%29%2C+%27type%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27error_description%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27id%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%7D%0A++++++++++++++because+column+names+don%27t+match%0A++++++++++++++%0A++++++++++++++During+handling+of+the+above+exception%2C+another+exception+occurred%3A%0A++++++++++++++%0A++++++++++++++Traceback+%28most+recent+call+last%29%3A%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2Fsrc%2Fworker%2Fjob_runners%2Fconfig%2Fparquet_and_info.py%22%2C+line+1433%2C+in+compute_config_parquet_and_info_response%0A++++++++++++++++++parquet_operations+%3D+convert_to_parquet%28builder%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2Fsrc%2Fworker%2Fjob_runners%2Fconfig%2Fparquet_and_info.py%22%2C+line+1050%2C+in+convert_to_parquet%0A++++++++++++++++++builder.download_and_prepare%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+925%2C+in+download_and_prepare%0A++++++++++++++++++self._download_and_prepare%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+1001%2C+in+_download_and_prepare%0A++++++++++++++++++self._prepare_split%28split_generator%2C+**prepare_split_kwargs%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+1742%2C+in+_prepare_split%0A++++++++++++++++++for+job_id%2C+done%2C+content+in+self._prepare_split_single%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+1873%2C+in+_prepare_split_single%0A++++++++++++++++++raise+DatasetGenerationCastError.from_cast_error%28%0A++++++++++++++datasets.exceptions.DatasetGenerationCastError%3A+An+error+occurred+while+generating+the+dataset%0A++++++++++++++%0A++++++++++++++All+the+data+files+must+have+the+same+columns%2C+but+at+some+point+there+are+4+new+columns+%28%7B%27instruction%27%2C+%27system_prompt%27%2C+%27input%27%2C+%27output%27%7D%29+and+5+missing+columns+%28%7B%27context%27%2C+%27corrupted_text%27%2C+%27error_description%27%2C+%27corrected_text%27%2C+%27is_correct%27%7D%29.%0A++++++++++++++%0A++++++++++++++This+happened+while+the+json+dataset+builder+was+generating+data+using%0A++++++++++++++%0A++++++++++++++hf%3A%2F%2Fdatasets%2FGreatCaptainNemo%2FBioProBench%2FGEN_test.json+%28at+revision+69b0bd533367c45bdca9973a1dfb36e02b5e6336%29%0A++++++++++++++%0A++++++++++++++Please+either+edit+the+data+files+to+have+matching+columns%2C+or+separate+them+into+different+configurations+%28see+docs+at+https%3A%2F%2Fhf.co%2Fdocs%2Fhub%2Fdatasets-manual-configuration%23multiple-configurations%29%0A%60%60%60%0A%0A%0Acc+%40albertvillanova+%40lhoestq+%40severo.)

## BioProBench: Comprehensive Dataset and Benchmark in Biological Protocol Understanding and Reasoning

Paper
BioProBench is the first large-scale, integrated multi-task benchmark for biological protocol understanding and reasoning, specifically designed for large language models (LLMs). It moves beyond simple QA to encompass a comprehensive suite of tasks critical for procedural text comprehension.
Biological protocols are the fundamental bedrock of reproducible and safe life science research. While LLMs have shown remarkable capabilities on general tasks, their systematic evaluation on highly specialized, accuracy-critical, and inherently procedural texts like biological protocols remains limited. BioProBench fills this gap by providing a robust framework to evaluate LLMs on diverse aspects of protocol understanding and reasoning.
BioProBench features:
- 📚 Large-scale Data: Built upon 27K original biological protocols , yielding nearly 556K high-quality structured instances .
- 🎯 Comprehensive Tasks: A suite of ** five core tasks** challenging LLMs on different facets of procedural understanding and generation: Protocol Question Answering (PQA) Step Ordering (ORD) Error Correction (ERR) Protocol Generation (GEN) Protocol Reasoning (REA)
- Protocol Question Answering (PQA)
- Step Ordering (ORD)
- Error Correction (ERR)
- Protocol Generation (GEN)
- Protocol Reasoning (REA)
- 🧬 Broad Domain Coverage: Data sourced from 6 major repositories and covering 16 biological subdomains .
- 🔬 Standardized Evaluation: A robust framework combining standard NLP metrics with novel domain-specific measures for accurate performance quantification.

## 🚀 Motivation

Biological protocols are the operational blueprint for experiments. As biological research increasingly leverages automation and AI, the ability of AI systems to understand and reason about these complex procedures is paramount. Current LLMs, while powerful, face significant challenges:
- Limited Procedural Understanding: LLMs struggle with the temporal dependencies, conditional logic, and specific requirements embedded within protocols.
- Lack of Systematic Evaluation: There has been a lack of large-scale, multi-task benchmarks specifically designed to diagnose LLMs' limitations on procedural biological texts.
- Bridging the Gap: Developing AI systems capable of safely automating and even optimizing experiments requires models that can reliably interpret and generate protocols.
BioProBench addresses these challenges by providing the necessary data and tasks for comprehensive evaluation and driving the development of more capable models.

## 📊 Dataset Structure

BioProBench provides a layered data design to support various model development stages:
- A raw corpus of 27K protocols for pretraining or RAG applications.
- A substantial downstream training set of over 550K structured instances across the five fine-grained tasks for model adaptation.
- A held-out test set of 1,000 examples per task for standardized benchmarking.
The dataset and code are publicly available:
- Code Repository: https://github.com/YuyangSunshine/bioprotocolbench
[LINK: https://github.com/YuyangSunshine/bioprotocolbench](https://github.com/YuyangSunshine/bioprotocolbench/)
- Hugging Face Dataset: https://huggingface.co/datasets/GreatCaptainNemo/BioProBench

### 🧪 Evaluation Metrics

We employ a hybrid evaluation framework that combines standard NLP metrics with novel domain-specific measures to accurately quantify model performance across all tasks.
Each task in BioProBench includes a standalone evaluation script within the Metrics/ directory. To evaluate your model outputs:
Each task corresponds to one script:
Open the corresponding evaluation script (e.g., ERR.py ) and manually set the file path to your model’s output JSON file:
Example:
Then run the script:
Each script prints evaluation results such as:
- Accuracy, Precision, Recall, F1
- Step-level metrics (e.g., Step Recall, Redundancy Penalty)
- Ordering metrics (e.g., Kendall’s Tau)
- Parsing failure rates
We evaluated 12 mainstream open-source and closed-source LLMs on BioProBench. Our key findings reveal significant insights into the current capabilities and limitations of LLMs on biological protocols:
- Surface vs. Deep Understanding: While top models perform reasonably well on tasks requiring surface understanding like Protocol Question Answering (e.g., ~70% PQA-Acc.) and Error Correction (e.g., >64% ERR F1), they struggle significantly with tasks demanding deeper procedural understanding and structured generation.
- Challenges in Reasoning and Generation: Performance drops considerably on Step Ordering (e.g., ORD-EM ~50%) and Protocol Generation (e.g., GEN-BLEU <15%), highlighting the difficulty for LLMs in managing temporal dependencies and generating coherent, accurate procedures.
- Model Variances: Comparisons show diverse performance across models. Certain open-source models approach the performance of closed-source models on some tasks, while smaller, bio-specific models often lag behind general LLMs on complex procedural content, suggesting limitations in capacity for capturing intricate dependencies.
Overall, our findings underscore that robust procedural reasoning within biological protocols represents a significant challenge for current LLMs.

## 🤝 Contributing

We welcome contributions to enhance BioProBench, including:
- New protocol sources
- 🧪 Additional biological domains
- 🧠 Novel evaluation tasks
- 📝 Annotation improvements

## 📜 Citation

## 📧 Contact

For dataset access or collaboration inquiries: sunshineliuyuyang@gmail.com

## Paper for GreatCaptainNemo/BioProBench


--------------------