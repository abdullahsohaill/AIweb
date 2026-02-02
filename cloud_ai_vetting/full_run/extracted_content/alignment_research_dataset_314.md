# **Alignment Research Dataset**
**URL:** https://huggingface.co/datasets/StampyAI/alignment-research-dataset
**Page Title:** StampyAI/alignment-research-dataset · Datasets at Hugging Face
--------------------

The viewer is disabled because this dataset repo requires arbitrary Python code execution. Please consider
			removing the loading script and relying on automated data support (you can use convert_to_parquet from the datasets library). If this is not possible, please open a discussion for direct help.
[LINK: loading script](https://huggingface.co/docs/datasets/dataset_script)
[LINK: automated data support](https://huggingface.co/docs/datasets/repository_structure)
[LINK: convert_to_parquet](https://huggingface.co/docs/datasets/main/en/cli#convert-to-parquet)
[LINK: open a discussion](/datasets/StampyAI/alignment-research-dataset/discussions/new?title=Dataset+Viewer+issue%3A+DatasetWithScriptNotSupportedError&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AError+code%3A+++DatasetWithScriptNotSupportedError%0A%0A%60%60%60%0A%0A%0A---%0A%0A%F0%9F%91%8B+Before+opening+the+discussion%2C+have+you+considered+removing+the+%5Bloading+script%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fdataset_script%29+and+relying+on+%5Bautomated+data+support%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Frepository_structure%29%3F%0A%0AYou+can+use+%5Bconvert_to_parquet%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fmain%2Fen%2Fcli%23convert-to-parquet%29+from+the+datasets+library.%0A%0A---%0A%0A%0Acc+%40albertvillanova+%40lhoestq+%40severo.)

## AI Alignment Research Dataset

The AI Alignment Research Dataset is a collection of documents related to AI Alignment and Safety from various books, research papers, and alignment related blog posts. This is a work in progress. Components are still undergoing a cleaning process to be updated more regularly.

## Sources

Here are the list of sources along with sample contents:
- agentmodel
agentmodel
- agisf - recommended readings from AGI Safety Fundamentals
agisf - recommended readings from AGI Safety Fundamentals
- aisafety.info - Stampy's FAQ
aisafety.info - Stampy's FAQ
- alignmentforum
alignmentforum
- alignment_newsletter
alignment_newsletter
- arbital
arbital
- arxiv - relevant research papers
arxiv - relevant research papers
- blogs - entire websites automatically scraped AI Impacts AI Safety Camp carado.moe Cold Takes DeepMind technical blogs DeepMind AI Safety Research EleutherAI generative.ink Gwern Branwen's blog Jack Clark's Import AI MIRI Jacob Steinhardt's blog ML Safety Newsletter Transformer Circuits Thread Open AI Research Victoria Krakovna's blog Eliezer Yudkowsky's blog
blogs - entire websites automatically scraped
- AI Impacts
- AI Safety Camp
- carado.moe
- Cold Takes
- DeepMind technical blogs
- DeepMind AI Safety Research
- EleutherAI
- generative.ink
- Gwern Branwen's blog
- Jack Clark's Import AI
- MIRI
- Jacob Steinhardt's blog
- ML Safety Newsletter
- Transformer Circuits Thread
- Open AI Research
- Victoria Krakovna's blog
- Eliezer Yudkowsky's blog
- distill
distill
- eaforum - selected posts
eaforum - selected posts
- lesswrong - selected posts
lesswrong - selected posts
- special_docs - individual documents curated from various resources Make a suggestion for sources not already in the dataset
special_docs - individual documents curated from various resources
- Make a suggestion for sources not already in the dataset
- youtube - playlists & channels AI Alignment playlist and other lists AI Explained Evan Hubinger's AI Safety Talks AI Safety Reading Group AiTech - TU Delft Rob Miles AI
youtube - playlists & channels
- AI Alignment playlist and other lists
- AI Explained
- Evan Hubinger's AI Safety Talks
- AI Safety Reading Group
- AiTech - TU Delft
- Rob Miles AI

## Keys

All entries contain the following keys:
- id - string of unique identifier
- source - string of data source listed above
- title - string of document title of document
- authors - list of strings
- text - full text of document content
- url - string of valid link to text content
- date_published - in UTC format
Additional keys may be available depending on the source document.

## Usage

Execute the following code to download and parse the files:
To only get the data for a specific source, pass it in as the second argument, e.g.:

## Limitations and Bias

LessWrong posts have overweighted content on doom and existential risk, so please beware in training or finetuning generative language models on the dataset.

## Contributing

The scraper to generate this dataset is open-sourced on GitHub and currently maintained by volunteers at StampyAI / AI Safety Info. Learn more or join us on Discord .
[LINK: GitHub](https://github.com/StampyAI/alignment-research-dataset)

## Rebuilding info

This README contains info about the number of rows and their features which should be rebuilt each time datasets get changed. To do so, run:

## Citing the Dataset

For more information, here is the paper and LessWrong post. Please use the following citation when using the dataset:
Kirchner, J. H., Smith, L., Thibodeau, J., McDonnell, K., and Reynolds, L. "Understanding AI alignment research: A Systematic Analysis." arXiv preprint arXiv:2022.4338861 (2022).

## Paper for StampyAI/alignment-research-dataset


--------------------