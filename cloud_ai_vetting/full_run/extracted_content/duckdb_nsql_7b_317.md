# DuckDB-NSQL-7B
**URL:** https://huggingface.co/motherduckdb/DuckDB-NSQL-7B-v0.1
**Page Title:** motherduckdb/DuckDB-NSQL-7B-v0.1 · Hugging Face
--------------------


## DuckDB-NSQL-7B

## Model Description

NSQL is a family of autoregressive open-source large foundation models (FMs) designed specifically for SQL generation tasks.
In this repository we are introducing a new member of NSQL, DuckDB-NSQL. It's based on Meta's original Llama-2 7B model and further pre-trained on a dataset of general SQL queries and then fine-tuned on a dataset composed of DuckDB text-to-SQL pairs.

## Training Data

200k DuckDB text-to-SQL pairs, synthetically generated using Mixtral-8x7B-Instruct-v0.1 , guided by the DuckDB v0.9.2 documentation. And text-to-SQL pairs from NSText2SQL that were transpiled to DuckDB SQL using sqlglot .
[LINK: sqlglot](https://github.com/tobymao/sqlglot)

## Evaluation Data

We evaluate our models on a DuckDB-specific benchmark that contains 75 text-to-SQL pairs. The benchmark is available here .
[LINK: here](https://github.com/NumbersStationAI/DuckDB-NSQL/)

## Training Procedure

DuckDB-NSQL was trained using cross-entropy loss to maximize the likelihood of sequential inputs. For finetuning on text-to-SQL pairs, we only compute the loss over the SQL portion of the pair. The model is trained using 80GB A100s, leveraging data and model parallelism. We fine-tuned for 10 epochs.

## Intended Use and Limitations

The model was designed for text-to-SQL generation tasks from given table schema and natural language prompts. The model works best with the prompt format defined below and outputs.
In contrast to existing text-to-SQL models, the SQL generation is not contrained to SELECT statements, but can generate any valid DuckDB SQL statement, including statements for official DuckDB extensions.

## How to Use

Example 1:
Example 2:
Example 3:
For more information (e.g., run with your local database), please find examples in this repository .
[LINK: this repository](https://github.com/NumbersStationAI/DuckDB-NSQL)

## Model tree for motherduckdb/DuckDB-NSQL-7B-v0.1

Base model

## Spaces using motherduckdb/DuckDB-NSQL-7B-v0.1 10


--------------------