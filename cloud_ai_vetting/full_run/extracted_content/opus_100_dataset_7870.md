# OPUS-100 Dataset
**URL:** https://opus.nlpl.eu/OPUS-100
**Page Title:** OPUS - Corpora
--------------------

OPUS-100 is an English-centric multilingual corpus covering 100 languages. It was randomly sampled from the OPUS collection [1].
The entire corpus can be downloaded from opus-100-corpus-v1.0.tar.gz . Individual language pairs are also available from http://data.statmt.org/opus-100-corpus/v1.0 or from the OPUS object storage, e.g. https://object.pouta.csc.fi/OPUS-100/v1.0/opus-100-corpus-de-en-v1.0.tar.gz (replace 'de-en' with the language pair you need) and from https://object.pouta.csc.fi/OPUS-100/v1.0/opus-100-corpus-zeroshot-v1.0.tar.gz (all zero-shot language pairs).
OPUS-100 was used for the experiments in the paper "Improving Massively Multilingual Neural Machine Translation and Zero-Shot Translation" [2]. Please cite that paper if you use this corpus and, pleae, also acknowledge OPUS.

## Description

Following [3], OPUS-100 is English-centric, meaning that all training pairs include English on either the source or target side. The corpus covers 100 languages (including English). We selected the languages based on the volume of parallel data available in OPUS.
The OPUS collection is comprised of multiple corpora, ranging from movie subtitles to GNOME documentation to the Bible. We did not curate the data or attempt to balance the representation of different domains, instead opting for the simplest approach of downloading all corpora for each language pair and concatenating them.
The dataset is split into training, development, and test portions. We randomly sampled up to 1M sentence pairs per language pair for training and up to 2000 each for development and test. To ensure that there was no overlap (at the monolingual sentence level) between the training and development/test data, we applied a filter during sampling to exclude sentences that had already been sampled. Note that this was done cross-lingually so that, for instance, an English sentence in the Portuguese-English portion of the training data could not occur in the Hindi-English test set.
OPUS-100 contains approximately 55M sentence pairs. Of the 99 language pairs, 44 have 1M sentence pairs of training data, 73 have at least 100k, and 95 have at least 10k.

## Zero-shot Evaluation Data

To support the evaluation of zero-shot translation, we also sampled data for each of the 15 pairings of Arabic, Chinese, Dutch, French, German, and Russian. Filtering was used to exclude sentences already in OPUS-100.

## Notes on the Scripts

The scripts are provided for reference. They may need modification to work on systems other than our own.
Running the scripts will result in a different corpus each time due to the randomness involved in sampling (and possibly also due to changes to the upstream OPUS collection).
Note that these scripts produce training, development, and test data for the zero-shot pairs as well as the supervised language pairs. The training and development data can be used for training contrastive supervised systems for those pairs, if desired (only the test sets were used in [2]).

## Pre-trained Models

Pre-trained many-to-many models, trained with the zero toolkit, are available here . Detailed results for all translation directions for these models can be found here .
[LINK: zero](https://github.com/bzhangGo/zero)
[LINK: here](https://github.com/bzhangGo/zero/tree/master/docs/multilingual_laln_lalt#pretrained-multilingual-models-many-to-many)
[LINK: here](https://github.com/bzhangGo/zero/blob/master/docs/multilingual_laln_lalt/many-to-many.xlsx)

## Acknowledgements

OPUS-100 was developed with the support of Samsung Electronics Polska sp. z o.o. - Samsung R&D Institute Poland and has received funding from the European Union’s Horizon 2020 Research and Innovation Programme under Grant Agreements 825460 (ELITR). We thank all contributors to the OPUS project.

## References

- [1] Jörg Tiedemann (2012). "Parallel Data, Tools and Interfaces in OPUS." In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC'2012).
- [2] Biao Zhang, Philip Williams, Ivan Titov, Rico Sennrich (2020). "Improving Massively Multilingual Neural Machine Translation and Zero-Shot Translation." In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics.
- [3] Roee Aharoni, Melvin Johnson, and Orhan Firat (2019). "Massively Multilingual Neural Machine Translation." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers).

## Links

More information and scripts that have been used to create this corpus are available from github
[LINK: github](https://github.com/EdinburghNLP/opus-100-corpus)

--------------------