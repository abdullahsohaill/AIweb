# FLORES+ Dataset
**URL:** https://huggingface.co/datasets/openlanguagedata/flores_plus
**Page Title:** openlanguagedata/flores_plus · Datasets at Hugging Face
--------------------


## Protecting the integrity of FLORES+ for evaluation

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
Log in or Sign Up to review the conditions and access this dataset content.

## Dataset Card for FLORES+

FLORES+ is an evaluation benchmark dataset for multilingual machine translation.

## Dataset Details

### Dataset Description

FLORES+ is a multilingual machine translation benchmark released under CC BY-SA 4.0 . This dataset was originally released by FAIR researchers at Meta under the name FLORES. Further information about these initial releases can be found in Dataset Sources below. The data is now being managed by OLDI, the Open Language Data Initiative . The + has been added to the name to disambiguate between the original datasets and this new actively developed version.
The data consists of translations primarily from English into over 200 language varieties. The original English sentences were sampled in equal amounts from Wikinews (an international news source), Wikijunior (a collection of age-appropriate non-fiction books), and Wikivoyage (a travel guide).
For each language, the dataset has 997 sentences for the dev split and 1012 sentences for the devtest split. The separate blind test set, originally developed by Meta, is not managed by OLDI and not part of this repository.
- Curated by: The Open Language Data Initiative
- Languages: Currently 225 language varieties, see the full list in the table below .
- License: CC BY-SA 4.0
The current version of the dataset is 4.2 . For the full list of versions, see CHANGELOG.md .

### Dataset Sources

FLORES+ is based on FLORES-200, described in the following paper:
Other authors have since contributed to the dataset. If you use this dataset in your work, please cite the relevant papers listed in bibliography.bib .

## Uses

FLORES+ is intended to be used to evaluate multilingual NLP applications like machine translation. It should not be used as training data.
To load the dataset using Python code, please follow the steps below:
- Install the datasets package: pip install datasets .
[LINK: datasets](https://huggingface.co/docs/datasets)
- Log in on the current website (Huggingface.co).
- Accept the terms of use of the FLORES+ dataset on this page.
- Get your Huggingface access token by clicking on your user icon in the top left corner, choosing "Access Tokens", and creating a token or copying an existing one.
- Make sure you are logged into Hugginface hub in your system by running in Python:
- After having logged in, you can access the full FLORES+ dataset or a part of it as follows:
- You can convert the dataset to a Pandas DataFrame, if this formar is familiar to you (e.g. df = ds_fra_dev.to_pandas() ).
- If you want, you can save the file to disk, e.g. to the csv format ( df.to_csv("flores_plus_fra_dev.csv") ) or other formats supported by Pandas.
But please do not redistribute this file publicly, unless you protect it from automatic scrapping!
[LINK: other formats](https://pandas.pydata.org/docs/user_guide/io.html)

## Dataset Structure

Each instance in the dataset has the structure as the following example:
Each languoid is uniquely identified by a combination of 4 values: iso_639_3 , iso_15924 , glottocode , and variant — roughly speaking, a combination of language, dialect, and orthography.
Within each languoid, the values of id and split uniquely identify a sentence and are aligned across all languoids (i.e. joining any pair of langioids by id and split would result in a parallel dataset).

### Data Fields

- id : ID number for each line of data. Lines with the same ID in the same split are translations of each other.
- text : A line of text in the indicated language.
- iso_639_3 : The ISO 639-3 code indicating the language variety.
- iso_15924 : The ISO 15924 indicating the writing script.
- glottocode : The Glottocode corresponding to the language variety.
- variant : An additional tag for the language variety (usually an empty string; currently used only for Radical Bokmål)
- url : The URL for the English article from which the text was extracted.
- domain : The domain of the text.
- topic : The topic of the text.
- has_image : Whether the original article contains an image.
- has_hyperlink : Whether the text contains a hyperlink.
- last_updated : The FLORES+ version where the given row was last updated.

## Dataset Creation

See the NLLB Nature paper and the longer NLLB technical paper for more details.

### Additional Dataset Cards

The datasets for some language varieties have individual datacards describing their creation. These can be found in the dataset_cards directory.

## Contact

For more information about the FLORES+ dataset, please see oldi.org .

## Contributing

Fixes and new language contributions are most welcome.
By contributing to this project you agree to the Developer Certificate of
Origin (DCO) . This document was created by the Linux Kernel community and is a
simple statement that you, as a contributor, have the legal right to make the
contribution.
In order to show your agreement with the DCO you should include at the end of commit message,
the following line: Signed-off-by: John Doe <john.doe@example.com> , using your real name.
This can be done easily using the -s flag on the git commit .
Please see the Contribution guidelines for further information.

### How to add a pull request

- Go to https://huggingface.co/datasets/openlanguagedata/flores_plus/discussions , press "New pull request".
- In the popup window, enter a branch name and press "Create branch".
- On your computer, do git clone https://huggingface.co/datasets/openlanguagedata/flores_plus .
- Checkout to your newly created branch (e.g. cd flores_plus && git fetch origin refs/pr/4:pr/4 && git checkout pr/4 ).
- Check that you are logged in to the HF CLI tool ( huggingface-cli whoami ). If not, please log into it ( huggingface-cli login and enter your token).
- Modify a file (for adding new languages, see the instructions below) and add the changes to git (e.g. git add dev/rus_Cyrl.parquet ).
- Commit with an -s flag (e.g. git commit -s -m "fix a few typos in the Russian dev set" ).
- Push (e.g. git push --set-upstream origin pr/4 ).
- Go to the pull request page and see if it reflects your changes.
- When your pull request is ready, press the "Publish" button in its web interface.
If you find this difficult, please contact us by email info@oldi.org or in our Discord group !

### Testing your changes

After contributing new translations or modifying existing ones, you can check that the data format is OK.
Assuming that you have the Python packages pytest and dataset installed, you can type
in your console (in the flores_plus directory), and the tests will run.
If any of them fails, please inspect the translations, following the hints in the test output.

## Changelog

See CHANGELOG.md for information about the latest changes.

## Language Coverage

[LINK: [1]](https://github.com/openlanguagedata/flores/issues/5)
[LINK: [1]](https://github.com/openlanguagedata/flores/issues/6)

## Models trained or fine-tuned on openlanguagedata/flores_plus

## Spaces using openlanguagedata/flores_plus 3

## Collection including openlanguagedata/flores_plus

## Paper for openlanguagedata/flores_plus


--------------------