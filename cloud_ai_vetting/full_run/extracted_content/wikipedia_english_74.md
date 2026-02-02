# Wikipedia English
**URL:** https://huggingface.co/datasets/Intelligent-Internet/wikipedia_en
**Page Title:** Intelligent-Internet/wikipedia_en · Datasets at Hugging Face
--------------------


## wikipedia_en

This is a curated Wikipedia English dataset for use with the II-Commons project.
[LINK: II-Commons](https://github.com/Intelligent-Internet/II-Commons)

## Dataset Details

### Dataset Description

This dataset comprises a curated Wikipedia English pages. Data sourced directly from the official English Wikipedia database dump. We extract the pages, chunk them into smaller pieces, and embed them using Snowflake/snowflake-arctic-embed-m-v2.0 . All vector embeddings are 16-bit half-precision vectors optimized for cosine indexing with vectorchord .
[LINK: vectorchord](https://github.com/tensorchord/vectorchord)

### Dataset Sources

Based on the wikipedia dumps . Please check this page for the LICENSE of the page data.

## Dataset Structure

- Metadata Table
- id: A unique identifier for the page.
- revid: The revision ID of the page.
- url: The URL of the page.
- title: The title of the page.
- ignored: Whether the page is ignored.
- created_at: The creation time of the page.
- updated_at: The update time of the page.
- Chunking Table
- id: A unique identifier for the chunk.
- title: The title of the page.
- url: The URL of the page.
- source_id: The source ID of the page.
- chunk_index: The index of the chunk.
- chunk_text: The text of the chunk.
- vector: The vector embedding of the chunk.
- created_at: The creation time of the chunk.
- updated_at: The update time of the chunk.

## Prerequisite

PostgreSQL 17 with extensions: vectorchord and pg_search
[LINK: vectorchord](https://github.com/tensorchord/VectorChord)
[LINK: pg_search](https://github.com/paradedb/paradedb/tree/dev/pg_search)
The easiest way is to use our Docker image , or build your own. Then load the psql_basebackup branch, following the Quick Start
[LINK: Docker image](https://github.com/Intelligent-Internet/II-Commons/tree/main/examples/db)
[LINK: Quick Start](https://github.com/Intelligent-Internet/II-Commons?tab=readme-ov-file#quick-start)
Ensure extensions are enabled, connect to the database using the psql, and run the following SQL:

## Uses

This dataset is available for a wide range of applications.
Here is a demo of how to use the dataset with II-Commons .
[LINK: II-Commons](https://github.com/Intelligent-Internet/II-Commons)

### Create the metadata and chunking tables in PostgreSQL

### Load csv files to database

- Load the dataset from local file system to a remote PostgreSQL server:
- Load the dataset from the PostgreSQL server's file system:

### Create Indexes

You need to create the following indexes for the best performance.
The vector column is a halfvec(768) column, which is a 16-bit half-precision vector optimized for cosine indexing with vectorchord . You can get more information about the vector index from the vectorchord documentation.
[LINK: vectorchord](https://github.com/tensorchord/vectorchord)
[LINK: vectorchord](https://docs.vectorchord.ai/vectorchord/usage/indexing.html)
- Create the metadata table index:
- Create the chunking table index:

### Query with II-Commons

Click this link to learn how to query the dataset with II-Commons .
[LINK: II-Commons](https://github.com/Intelligent-Internet/II-Commons)

## Models trained or fine-tuned on Intelligent-Internet/wikipedia_en

## Collection including Intelligent-Internet/wikipedia_en


--------------------