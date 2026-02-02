# **KnowEdit**
**URL:** https://huggingface.co/datasets/zjunlp/KnowEdit
**Page Title:** zjunlp/KnowEdit · Datasets at Hugging Face
--------------------

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer , and open a discussion for direct support.
[LINK: how to configure the dataset viewer](https://huggingface.co/docs/hub/datasets-data-files-configuration)
[LINK: open a discussion](/datasets/zjunlp/KnowEdit/discussions/new?title=Dataset+Viewer+issue%3A+DatasetGenerationCastError&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AError+code%3A+++DatasetGenerationCastError%0AException%3A++++DatasetGenerationCastError%0AMessage%3A++++++An+error+occurred+while+generating+the+dataset%0A%0AAll+the+data+files+must+have+the+same+columns%2C+but+at+some+point+there+are+3+new+columns+%28%7B%27neg%27%2C+%27ent%27%2C+%27pos%27%7D%29+and+6+missing+columns+%28%7B%27ground_truth%27%2C+%27prompt%27%2C+%27portability%27%2C+%27target_new%27%2C+%27subject%27%2C+%27locality%27%7D%29.%0A%0AThis+happened+while+the+json+dataset+builder+was+generating+data+using%0A%0Ahf%3A%2F%2Fdatasets%2Fzjunlp%2FKnowEdit%2Fbenchmark%2FConvsent%2Fblender_train.json+%28at+revision+6d218881e60c7c8be836bd2befd598eb3b318be4%29%0A%0APlease+either+edit+the+data+files+to+have+matching+columns%2C+or+separate+them+into+different+configurations+%28see+docs+at+https%3A%2F%2Fhf.co%2Fdocs%2Fhub%2Fdatasets-manual-configuration%23multiple-configurations%29%0ATraceback%3A++++Traceback+%28most+recent+call+last%29%3A%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+2011%2C+in+_prepare_split_single%0A++++++++++++++++++writer.write_table%28table%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Farrow_writer.py%22%2C+line+585%2C+in+write_table%0A++++++++++++++++++pa_table+%3D+table_cast%28pa_table%2C+self._schema%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Ftable.py%22%2C+line+2302%2C+in+table_cast%0A++++++++++++++++++return+cast_table_to_schema%28table%2C+schema%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Ftable.py%22%2C+line+2256%2C+in+cast_table_to_schema%0A++++++++++++++++++raise+CastError%28%0A++++++++++++++datasets.table.CastError%3A+Couldn%27t+cast%0A++++++++++++++neg%3A+list%3Citem%3A+string%3E%0A++++++++++++++++child+0%2C+item%3A+string%0A++++++++++++++ent%3A+string%0A++++++++++++++pos%3A+list%3Citem%3A+string%3E%0A++++++++++++++++child+0%2C+item%3A+string%0A++++++++++++++to%0A++++++++++++++%7B%27ground_truth%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27prompt%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27portability%27%3A+%7B%27Logical_Generalization%27%3A+%5B%7B%27ground_truth%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27prompt%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%7D%5D%2C+%27Reasoning%27%3A+%5B%7B%27ground_truth%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27prompt%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%7D%5D%2C+%27Subject_Aliasing%27%3A+%5B%7B%27ground_truth%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27prompt%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%7D%5D%7D%2C+%27target_new%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27subject%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27locality%27%3A+%7B%27Forgetfulness%27%3A+%5B%7B%27ground_truth%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27prompt%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%7D%5D%2C+%27Relation_Specificity%27%3A+%5B%7B%27ground_truth%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%2C+%27prompt%27%3A+Value%28dtype%3D%27string%27%2C+id%3DNone%29%7D%5D%7D%7D%0A++++++++++++++because+column+names+don%27t+match%0A++++++++++++++%0A++++++++++++++During+handling+of+the+above+exception%2C+another+exception+occurred%3A%0A++++++++++++++%0A++++++++++++++Traceback+%28most+recent+call+last%29%3A%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2Fsrc%2Fworker%2Fjob_runners%2Fconfig%2Fparquet_and_info.py%22%2C+line+1321%2C+in+compute_config_parquet_and_info_response%0A++++++++++++++++++parquet_operations+%3D+convert_to_parquet%28builder%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2Fsrc%2Fworker%2Fjob_runners%2Fconfig%2Fparquet_and_info.py%22%2C+line+935%2C+in+convert_to_parquet%0A++++++++++++++++++builder.download_and_prepare%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+1027%2C+in+download_and_prepare%0A++++++++++++++++++self._download_and_prepare%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+1122%2C+in+_download_and_prepare%0A++++++++++++++++++self._prepare_split%28split_generator%2C+**prepare_split_kwargs%29%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+1882%2C+in+_prepare_split%0A++++++++++++++++++for+job_id%2C+done%2C+content+in+self._prepare_split_single%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fbuilder.py%22%2C+line+2013%2C+in+_prepare_split_single%0A++++++++++++++++++raise+DatasetGenerationCastError.from_cast_error%28%0A++++++++++++++datasets.exceptions.DatasetGenerationCastError%3A+An+error+occurred+while+generating+the+dataset%0A++++++++++++++%0A++++++++++++++All+the+data+files+must+have+the+same+columns%2C+but+at+some+point+there+are+3+new+columns+%28%7B%27neg%27%2C+%27ent%27%2C+%27pos%27%7D%29+and+6+missing+columns+%28%7B%27ground_truth%27%2C+%27prompt%27%2C+%27portability%27%2C+%27target_new%27%2C+%27subject%27%2C+%27locality%27%7D%29.%0A++++++++++++++%0A++++++++++++++This+happened+while+the+json+dataset+builder+was+generating+data+using%0A++++++++++++++%0A++++++++++++++hf%3A%2F%2Fdatasets%2Fzjunlp%2FKnowEdit%2Fbenchmark%2FConvsent%2Fblender_train.json+%28at+revision+6d218881e60c7c8be836bd2befd598eb3b318be4%29%0A++++++++++++++%0A++++++++++++++Please+either+edit+the+data+files+to+have+matching+columns%2C+or+separate+them+into+different+configurations+%28see+docs+at+https%3A%2F%2Fhf.co%2Fdocs%2Fhub%2Fdatasets-manual-configuration%23multiple-configurations%29%0A%60%60%60%0A%0A%0Acc+%40albertvillanova+%40lhoestq+%40severo.)

## KnowEdit: A Benchmark of Knowledge Editing for LLMs

This README is about reproducing the paper A Comprehensive Study of Knowledge Editing for Large Language Models .
You can use EasyEdit to load and use this benchmark.
[LINK: EasyEdit](https://github.com/zjunlp/EasyEdit)
❗️❗️ To be noted, KnowEdit is constructed by re-organizing and extending exsiting datasests including WikiBio , ZsRE , WikiData Counterfact , WikiData Recent , convsent , Sanitation to make a comprehensive evaluation for knowledge editing. Special thanks to the builders and maintainers of the those datasets.
Please note that Counterfact and WikiData Counterfact are not the same dataset.
This README explains how to use EasyEdit with the KnowEdit dataset. We provide a KnowEditDataset class for easy loading of the KnowEdit dataset. To use it, simply write:
[LINK: EasyEdit](https://github.com/zjunlp/EasyEdit)

## Dataset Structure

KnowEdit is tailored for knowledge editing tasks. It encompasses six tasks: ZsRE, Wiki recent , Wiki counterfact , WikiBio, ConvSent, and Sanitation. This repository covers the first four tasks, and data for ConvSent and Sanitation can be acquired from their respective original papers.
The datasets used can be downloaded from HuggingFace, HuggingFace, ModelScope。
Unzip the file and put it to ./data
Different JSON files have distinct data types. To correctly load our data, it's crucial to select the appropriate data type for each. For instance:
- For the WikiBio dataset, we should use the wikibio data type.
- For the ZsRE dataset, we should use the zsre data type.
- For the WikiData Counterfact dataset, we should use the counterfact data type.
- For the WikiData Recent dataset, we should use the recent data type.
- For the convsent dataset, we should use the run_convsent_llama2.py
- For the Sanitation dataset, we should use the run_trivia_llama2.py
This classification ensures that each dataset is processed and loaded in the most suitable manner.
The file structure for KnowEdit is as follows:

## Get started quickly

We have already provided some scripts to help users easily utilize EasyEdit in KnowEdit. Different JSONs require different scripts. Please select the appropriate script to edit your model.
Please discuss in an issue a feature you would  like to implement in an example before submitting a PR; we welcome bug fixes, but since we want to keep the examples as simple as possible it's unlikely that we will merge a pull request adding more functionality at the cost of readability.
[LINK: issue](https://github.com/zjunlp/EasyEdit/issues)

### ROME

For WikiBio,ZsRE,wiki_counterfact,wiki_recent dataset,we use the following command:
For convsent dataset,we use the following command:
For Sanitation dataset ,we use the following command:

### MEMIT

For convsent dataset,we use the following command:
For Sanitation dataset ,we use the following command:
For convsent dataset,we use the following command:
For Sanitation dataset ,we use the following command:

### MEND

For convsent dataset,we use the following command:
For Sanitation dataset ,we use the following command:
For convsent dataset,we use the following command:
For Sanitation dataset ,we use the following command:

### IKE

For convsent dataset,we use the following command:
For Sanitation dataset ,we use the following command:

### LoRA

For convsent dataset,we use the following command:
For Sanitation dataset ,we use the following command:

## Training an Editor with KnowEdit

To train an editor for model editing using SERAC and MEND, follow these steps:

## Running Examples of Using KnowEdit

After loading the dataset with:
The data structure will be as follows:
Each JSON file has a unique structure. Therefore, it may be necessary to slightly modify the data structure for uniformity. For instance, in benchmark_wiki_counterfact_test_cf.json , the structure of portability_r is:
However, in EasyEdit, we require the data structure as shown below:
Thus, you may need to adjust the data structure in different JSON files accordingly.

## Performence

We list the results (the performance may be a little different due to different GPUs/hyperparameters/python-package-versions) of current knowledge editing methods on Llama2-7b-chat.

## The Composition of Dataset

## WikiData_recent

## Wiki counterfact

## WikiBio

## ZsRE

## Sanitation

## Citation

Please cite these papers if you use KnowEdit in your work.

## Space using zjunlp/KnowEdit 1

## Collection including zjunlp/KnowEdit

## Papers for zjunlp/KnowEdit


--------------------