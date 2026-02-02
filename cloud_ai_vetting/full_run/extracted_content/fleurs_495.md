# FLEURS
**URL:** https://huggingface.co/datasets/google/xtreme_s
**Page Title:** google/xtreme_s · Datasets at Hugging Face
--------------------

The viewer is disabled because this dataset repo requires arbitrary Python code execution. Please consider
			removing the loading script and relying on automated data support (you can use convert_to_parquet from the datasets library). If this is not possible, please open a discussion for direct help.
[LINK: loading script](https://huggingface.co/docs/datasets/dataset_script)
[LINK: automated data support](https://huggingface.co/docs/datasets/repository_structure)
[LINK: convert_to_parquet](https://huggingface.co/docs/datasets/main/en/cli#convert-to-parquet)
[LINK: open a discussion](/datasets/google/xtreme_s/discussions/new?title=Dataset+Viewer+issue%3A+DatasetWithScriptNotSupportedError&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AError+code%3A+++DatasetWithScriptNotSupportedError%0A%0A%60%60%60%0A%0A%0A---%0A%0A%F0%9F%91%8B+Before+opening+the+discussion%2C+have+you+considered+removing+the+%5Bloading+script%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fdataset_script%29+and+relying+on+%5Bautomated+data+support%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Frepository_structure%29%3F%0A%0AYou+can+use+%5Bconvert_to_parquet%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fmain%2Fen%2Fcli%23convert-to-parquet%29+from+the+datasets+library.%0A%0A---%0A%0A%0Acc+%40albertvillanova+%40lhoestq+%40severo.)

## XTREME-S

The Cross-lingual TRansfer Evaluation of Multilingual Encoders for Speech (XTREME-S) benchmark is a benchmark designed to evaluate speech representations across languages, tasks, domains and data regimes. It covers 102 languages from 10+ language families, 3 different domains and 4 task families: speech recognition, translation, classification and retrieval.
TLDR; XTREME-S is the first speech benchmark that is both diverse, fully accessible, and reproducible. All datasets can be downloaded with a single line of code. 
An easy-to-use and flexible fine-tuning script is provided and actively maintained.
XTREME-S covers speech recognition with Fleurs, Multilingual LibriSpeech (MLS) and VoxPopuli, speech translation with CoVoST-2, speech classification with LangID (Fleurs) and intent classification (MInds-14) and finally speech(-text) retrieval with Fleurs. Each of the tasks covers a subset of the 102 languages included in XTREME-S, from various regions:
- Western Europe : Asturian, Bosnian, Catalan, Croatian, Danish, Dutch, English, Finnish, French, Galician, German, Greek, Hungarian, Icelandic, Irish, Italian, Kabuverdianu, Luxembourgish, Maltese, Norwegian, Occitan, Portuguese, Spanish, Swedish, Welsh
- Eastern Europe : Armenian, Belarusian, Bulgarian, Czech, Estonian, Georgian, Latvian, Lithuanian, Macedonian, Polish, Romanian, Russian, Serbian, Slovak, Slovenian, Ukrainian
- Central-Asia/Middle-East/North-Africa : Arabic, Azerbaijani, Hebrew, Kazakh, Kyrgyz, Mongolian, Pashto, Persian, Sorani-Kurdish, Tajik, Turkish, Uzbek
- Sub-Saharan Africa : Afrikaans, Amharic, Fula, Ganda, Hausa, Igbo, Kamba, Lingala, Luo, Northern-Sotho, Nyanja, Oromo, Shona, Somali, Swahili, Umbundu, Wolof, Xhosa, Yoruba, Zulu
- South-Asia : Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Oriya, Punjabi, Sindhi, Tamil, Telugu, Urdu
- South-East Asia : Burmese, Cebuano, Filipino, Indonesian, Javanese, Khmer, Lao, Malay, Maori, Thai, Vietnamese
- CJK languages : Cantonese and Mandarin Chinese, Japanese, Korean

## Design principles

### Diversity

XTREME-S aims for task, domain and language
diversity. Tasks should be diverse and cover several domains to
provide a reliable evaluation of model generalization and
robustness to noisy naturally-occurring speech in different
environments. Languages should be diverse to ensure that
models can adapt to a wide range of linguistic and phonological
phenomena.

### Accessibility

The sub-dataset for each task can be downloaded 
with a single line of code as shown in Supported Tasks .
Each task is available under a permissive license that allows the use and redistribution 
of the data for research purposes. Tasks have been selected based on their usage by 
pre-existing multilingual pre-trained models, for simplicity.

### Reproducibility

We produce fully open-sourced, maintained and easy-to-use fine-tuning scripts 
for each task as shown under Fine-tuning Example .
XTREME-S encourages submissions that leverage publicly available speech and text datasets. Users should detail which data they use. 
In general, we encourage settings that can be reproduced by the community, but also encourage the exploration of new frontiers for speech representation learning.

## Fine-tuning and Evaluation Example

We provide a fine-tuning script under research-projects/xtreme-s .
The fine-tuning script is written in PyTorch and allows one to fine-tune and evaluate any Hugging Face model on XTREME-S.
The example script is actively maintained by @anton-l and @patrickvonplaten . Feel free 
to reach out via issues or pull requests on GitHub if you have any questions.
[LINK: research-projects/xtreme-s](https://github.com/huggingface/transformers/tree/master/examples/research_projects/xtreme-s)
[LINK: @anton-l](https://github.com/anton-l)
[LINK: @patrickvonplaten](https://github.com/patrickvonplaten)

## Leaderboards

The leaderboard for the XTREME-S benchmark can be found at this address (TODO(PVP)) .

## Supported Tasks

Note that the suppoprted tasks are focused particularly on linguistic aspect of speech,
while nonlinguistic/paralinguistic aspects of speech relevant to e.g. speech synthesis or voice conversion are not evaluated.

### 1. Speech Recognition (ASR)

We include three speech recognition datasets: FLEURS-ASR, MLS and VoxPopuli (optionally BABEL). Multilingual fine-tuning is used for these three datasets.
FLEURS-ASR is the speech version of the FLORES machine translation benchmark, covering 2000 n-way parallel sentences in n=102 languages.
MLS is a large multilingual corpus derived from read audiobooks from LibriVox and consists of 8 languages. For this challenge the training data is limited to 10-hours splits.
VoxPopuli is a large-scale multilingual speech corpus for representation learning and semi-supervised learning, from which we use the speech recognition dataset. The raw data is collected from 2009-2020 European Parliament event recordings. We acknowledge the European Parliament for creating and sharing these materials.
VoxPopuli has to download the whole dataset 100GB since languages 
are entangled into each other - maybe not worth testing here due to the size
BABEL from IARPA is a conversational speech recognition dataset in low-resource languages. First, download LDC2016S06, LDC2016S12, LDC2017S08, LDC2017S05 and LDC2016S13. BABEL is the only dataset in our benchmark who is less easily accessible, so you will need to sign in to get access to it on LDC. Although not officially part of the XTREME-S ASR datasets, BABEL is often used for evaluating speech representations on a difficult domain (phone conversations).
The above command is expected to fail with a nice error message,
explaining how to download BABEL
The following should work:

### 2. Speech Translation (ST)

We include the CoVoST-2 dataset for automatic speech translation.
The CoVoST-2 benchmark has become a commonly used dataset for evaluating automatic speech translation. It covers language pairs from English into 15 languages, as well as 21 languages into English. We use only the "X->En" direction to evaluate cross-lingual representations. The amount of supervision varies greatly in this setting, from one hour for Japanese->English to 180 hours for French->English. This makes pretraining particularly useful to enable such few-shot learning. We enforce multiligual fine-tuning for simplicity. Results are splitted in high/med/low-resource language pairs as explained in the [paper (TODO(PVP))].

### 3. Speech Classification

We include two multilingual speech classification datasets: FLEURS-LangID and Minds-14.
LangID can often be a domain classification, but in the case of FLEURS-LangID, recordings are done in a similar setting across languages and the utterances correspond to n-way parallel sentences, in the exact same domain, making this task particularly relevant for evaluating LangID. The setting is simple, FLEURS-LangID is splitted in train/valid/test for each language. We simply create a single train/valid/test for LangID by merging all.
Minds-14 is an intent classification made from e-banking speech datasets in 14 languages, with 14 intent labels. We impose a single multilingual fine-tuning to increase the size of the train and test sets and reduce the variance associated with the small size of the dataset per language.

### 4. (Optionally) Speech Retrieval

We optionally include one speech retrieval dataset: FLEURS-Retrieval as explained in the FLEURS paper .
FLEURS-Retrieval provides n-way parallel speech and text data. Similar to how XTREME for text leverages Tatoeba to evaluate bitext mining a.k.a sentence translation retrieval, we use FLEURS-Retrieval to evaluate the quality of fixed-size representations of speech utterances. Our goal is to incentivize the creation of fixed-size speech encoder for speech retrieval. The system has to retrieve the English "key" utterance corresponding to the speech translation of "queries" in 15 languages. Results have to be reported on the test sets of FLEURS-Retrieval whose utterances are used as queries (and keys for English). We augment the English keys with a large number of utterances to make the task more difficult.
Users can leverage the training (and dev) sets of FLEURS-Retrieval with a ranking loss to build better cross-lingual fixed-size representations of speech.

## Dataset Structure

The XTREME-S benchmark is composed of the following datasets:
- FLEURS
- Multilingual Librispeech (MLS) Note that for MLS, XTREME-S uses path instead of file and transcription instead of text .
- Voxpopuli
- Minds14
- Covost2 Note that for Covost2, XTREME-S uses path instead of file and transcription instead of sentence .
- BABEL
Please click on the link of the dataset cards to get more information about its dataset structure.

## Dataset Creation

The XTREME-S benchmark is composed of the following datasets:
- FLEURS
- Multilingual Librispeech (MLS)
- Voxpopuli
- Minds14
- Covost2
- BABEL
Please visit the corresponding dataset cards to get more information about the source data.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is meant to encourage the development of speech technology in a lot more languages of the world. One of the goal is to give equal access to technologies like speech recognition or speech translation to everyone, meaning better dubbing or better access to content from the internet (like podcasts, streaming or videos).

### Discussion of Biases

Most datasets have a fair distribution of gender utterances (e.g. the newly introduced FLEURS dataset). While many languages are covered from various regions of the world, the benchmark misses many languages that are all equally important. We believe technology built through XTREME-S should generalize to all languages.

### Other Known Limitations

The benchmark has a particular focus on read-speech because common evaluation benchmarks like CoVoST-2 or LibriSpeech evaluate on this type of speech. There is sometimes a known mismatch between performance obtained in a read-speech setting and a more noisy setting (in production for instance). Given the big progress that remains to be made on many languages, we believe better performance on XTREME-S should still correlate well with actual progress made for speech understanding.

## Additional Information

All datasets are licensed under the Creative Commons license (CC-BY) .

### Citation Information

### Contributions

Thanks to @patrickvonplaten , @anton-l , @aconneau for adding this dataset
[LINK: @patrickvonplaten](https://github.com/patrickvonplaten)
[LINK: @anton-l](https://github.com/anton-l)
[LINK: @aconneau](https://github.com/aconneau)
[LINK: Fine-Tuning script: research-projects/xtreme-s](https://github.com/huggingface/transformers/tree/master/examples/research_projects/xtreme-s)

## Models trained or fine-tuned on google/xtreme_s

## Papers for google/xtreme_s


--------------------