# SQLCoder-70B-Alpha
**URL:** https://huggingface.co/defog/sqlcoder-70b-alpha
**Page Title:** defog/sqlcoder-70b-alpha · Hugging Face
--------------------


## Model Card for SQLCoder-70B-Alpha

A capable large language model for natural language to SQL generation. Outperforms all generalist models (including GPT-4) on text to SQL.

## Model Details

### Model Description

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.
- Developed by: Defog, Inc
- Model type: [Text to SQL]
- License: [CC-by-SA-4.0]
- Finetuned from model: [CodeLlama-70B]

### Model Sources [optional]

- HuggingFace:
- GitHub:
[LINK: GitHub:](https://github.com/defog-ai/sqlcoder)
- Demo:

## Uses

This model is intended to be used by non-technical users to understand data inside their SQL databases. It is meant as an analytics tool, and not as a database admin tool.
This model has not been trained to reject malicious requests from users with write access to databases, and should only be used by users with read-only access.

## How to Get Started with the Model

Use the code here to get started with the model.
[LINK: here](https://github.com/defog-ai/sqlcoder/blob/main/inference.py)

## Evaluation

This model was evaluated on SQL-Eval , a PostgreSQL based evaluation framework developed by Defog for testing and alignment of model capabilities.
[LINK: SQL-Eval](https://github.com/defog-ai/sql-eval)
You can read more about the methodology behind SQLEval here .

### Results

We classified each generated question into one of 6 categories. The table displays the percentage of questions answered correctly by each model, broken down by category.

## Using SQLCoder

## Model Card Authors

- Rishabh Srivastava
- Wendy Aw
- Wong Jing Ping

## Model Card Contact

Contact us on X at @defogdata , or on email at founders@defog.ai

## Model tree for defog/sqlcoder-70b-alpha

## Spaces using defog/sqlcoder-70b-alpha 14


--------------------