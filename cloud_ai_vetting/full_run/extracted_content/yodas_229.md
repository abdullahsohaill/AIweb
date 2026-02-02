# YODAS
**URL:** https://huggingface.co/datasets/espnet/yodas
**Page Title:** espnet/yodas · Datasets at Hugging Face
--------------------

The viewer is disabled because this dataset repo requires arbitrary Python code execution. Please consider
			removing the loading script and relying on automated data support (you can use convert_to_parquet from the datasets library). If this is not possible, please open a discussion for direct help.
[LINK: loading script](https://huggingface.co/docs/datasets/dataset_script)
[LINK: automated data support](https://huggingface.co/docs/datasets/repository_structure)
[LINK: convert_to_parquet](https://huggingface.co/docs/datasets/main/en/cli#convert-to-parquet)
[LINK: open a discussion](/datasets/espnet/yodas/discussions/new?title=Dataset+Viewer+issue%3A+DatasetWithScriptNotSupportedError&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AError+code%3A+++DatasetWithScriptNotSupportedError%0A%0A%60%60%60%0A%0A%0A---%0A%0A%F0%9F%91%8B+Before+opening+the+discussion%2C+have+you+considered+removing+the+%5Bloading+script%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fdataset_script%29+and+relying+on+%5Bautomated+data+support%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Frepository_structure%29%3F%0A%0AYou+can+use+%5Bconvert_to_parquet%5D%28https%3A%2F%2Fhuggingface.co%2Fdocs%2Fdatasets%2Fmain%2Fen%2Fcli%23convert-to-parquet%29+from+the+datasets+library.%0A%0A---%0A%0A%0Acc+%40albertvillanova+%40lhoestq+%40severo.)
Updates
- 2024/07/09: we also uploaded a new version of YODAS as YODAS2 , it provides unsegmented audios and higher sampling rate (24k)

## README

This is the YODAS manual/automatic subset from our YODAS dataset, it has 369,510 hours of speech.
This dataset contains audio utterances and corresponding captions (manual or automatic) from YouTube. Note that manual caption only indicates that it is uploaded by users, but not necessarily transcribed by a human
For more details about YODAS dataset, please refer to our paper

## Usage:

Considering the extremely large size of the entire dataset, we support two modes of dataset loadings:
standard mode : each subset will be downloaded to the local dish before first iterating.
streaming mode most of the files will be streamed instead of downloaded to your local deivce. It can be used to inspect this dataset quickly.

## Subsets/Shards

There are 149 languages in this dataset, each language is sharded into at least 1 shard to make it easy for our processing and uploading purposes. The raw data of each shard contains 500G at most.
Statistics of each shard can be found in the last section.
We distinguish manual caption subset and automatic caption subset by the first digit in each shard's name. The first digit is 0 if it contains manual captions, 1 if it contains automatic captions.
For example, en000 to en005 are the English shards containing manual subsets, and en100 to en127 contains the automatic subsets.

## Reference

## Contact

If you have any questions, feel free to contact us at the following email address.
We made sure that our dataset only consisted of videos with CC licenses during our downloading. But in case you find your video unintentionally included in our dataset and would like to delete it, you can send a delete request to the following email.
Remove the parenthesis () from the following email address
(lixinjian)(1217)@gmail.com

## Statistics

Note that there are no overlappings across different subsets, each audio can be included in the dataset at most once.

## Models trained or fine-tuned on espnet/yodas

## Space using espnet/yodas 1

## Collection including espnet/yodas

## Paper for espnet/yodas


--------------------