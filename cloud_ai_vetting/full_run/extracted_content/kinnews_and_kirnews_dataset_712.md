# KINNEWS and KIRNEWS Dataset
**URL:** https://huggingface.co/datasets/andreniyongabo/kinnews_kirnews
**Page Title:** andreniyongabo/kinnews_kirnews · Datasets at Hugging Face
--------------------

The viewer is disabled because this dataset repo requires arbitrary Python code execution. Please consider
			removing the loading script and relying on automated data support (you can use convert_to_parquet from the datasets library). If this is not possible, please open a discussion for direct help.
[LINK: loading script](https://huggingface.co/docs/datasets/dataset_script)
[LINK: automated data support](https://huggingface.co/docs/datasets/repository_structure)
[LINK: convert_to_parquet](https://huggingface.co/docs/datasets/main/en/cli#convert-to-parquet)
[LINK: open a discussion](/datasets/andreniyongabo/kinnews_kirnews/discussions/new?title=Dataset+Viewer+issue%3A+DatasetWithScriptNotSupportedError&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AError+code%3A+++DatasetWithScriptNotSupportedError%0A%0A%60%60%60%0A%0A%0A---%0A%0A%F0%9F%91%8B+Before+opening+the+discussion%2C+have+you+considered+removing+the+%5Bloading+script%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fdataset_script%29+and+relying+on+%5Bautomated+data+support%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Frepository_structure%29%3F%0A%0AYou+can+use+%5Bconvert_to_parquet%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fmain%2Fen%2Fcli%23convert-to-parquet%29+from+the+datasets+library.%0A%0A---%0A%0A%0Acc+%40albertvillanova+%40lhoestq+%40severo.)

## Dataset Card for kinnews_kirnews

### Dataset Summary

Kinyarwanda and Kirundi news classification datasets (KINNEWS and KIRNEWS,respectively), which were both collected from Rwanda and Burundi news websites and newspapers, for low-resource monolingual and cross-lingual multiclass classification tasks.

### Supported Tasks and Leaderboards

This dataset can be used for text classification of news articles in Kinyarwadi and Kirundi languages. Each news article can be classified into one of the 14 possible classes. The classes are:
- politics
- sport
- economy
- health
- entertainment
- history
- technology
- culture
- religion
- environment
- education
- relationship

### Languages

Kinyarwanda and Kirundi

## Dataset Structure

### Data Instances

Here is an example from the dataset:

### Data Fields

The raw version of the data for Kinyarwanda language consists of these fields
- label: The category of the news article
- kin_label/kir_label: The associated label in Kinyarwanda/Kirundi language
- en_label: The associated label in English
- url: The URL of the news article
- title: The title of the news article
- content: The content of the news article
The cleaned version contains only the label , title and the content fields

### Data Splits

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

[More Information Needed]
[More Information Needed]

### Annotations

[More Information Needed]
[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

### Contributions

Thanks to @saradhix for adding this dataset.
[LINK: @saradhix](https://github.com/saradhix)
[LINK: Repository: github.com](https://github.com/Andrews2017/KINNEWS-and-KIRNEWS-Corpus)

## Models trained or fine-tuned on andreniyongabo/kinnews_kirnews

## Paper for andreniyongabo/kinnews_kirnews


--------------------