# GAIA Benchmark
**URL:** https://huggingface.co/datasets/gaia-benchmark/GAIA
**Page Title:** gaia-benchmark/GAIA · Datasets at Hugging Face
--------------------


## You need to agree to share your contact information to access this dataset

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
To avoid contamination and data leakage, you agree to not reshare this dataset outside of a gated or private repository on the HF hub.
Log in or Sign Up to review the conditions and access this dataset content.

## GAIA dataset

GAIA is a benchmark which aims at evaluating next-generation LLMs (LLMs with augmented capabilities due to added tooling, efficient prompting, access to search, etc).
We added gating to prevent bots from scraping the dataset. Please do not reshare the validation or test set in a crawlable format.

## Data and leaderboard

GAIA is made of more than 450 non-trivial question with an unambiguous answer, requiring different levels of tooling and autonomy to solve. It is therefore divided in 3 levels, where level 1 should be breakable by very good LLMs, and level 3 indicate a strong jump in model capabilities. Each level is divided into a fully public dev set for validation, and a test set with private answers and metadata.
GAIA leaderboard can be found in this space ( https://huggingface.co/spaces/gaia-benchmark/leaderboard ).
Questions are contained in metadata.jsonl. Some questions come with an additional file, that can be found in the same folder and whose id is given in the field file_name.
More details in the paper for now and soon here as well.

## Dataset Format update (October 2025)

To keep GAIA compatible with HF datasets 4.x where code-based dataset loaders are deprecated—we now ship Parquet-backed splits that mirror the former JSONL structure:
- metadata.parquet carries the full split, and companion files like metadata.level1.parquet retain the per-level views exposed in the configs.
- Columns remain task_id , Question , Level , Final answer , file_name , file_path , and the struct-valued Annotator Metadata , so existing processing pipelines can continue unchanged.
- file_path keeps pointing to attachments relative to the repository root (for example, 2023/test/<attachment-id>.pdf ), ensuring offline access to PDFs, media, and other auxiliary files.

### Load datasets

## Models trained or fine-tuned on gaia-benchmark/GAIA

## Spaces using gaia-benchmark/GAIA 24

## Collection including gaia-benchmark/GAIA

## Paper for gaia-benchmark/GAIA


--------------------