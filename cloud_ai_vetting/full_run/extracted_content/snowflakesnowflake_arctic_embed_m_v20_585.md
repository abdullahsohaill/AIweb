# Snowflake/snowflake-arctic-embed-m-v2.0
**URL:** https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0
**Page Title:** Snowflake/snowflake-arctic-embed-m-v2.0 · Hugging Face
--------------------


## Snowflake's Arctic-embed-m-v2.0

News | Models | Usage | Evaluation | Contact | FAQ License | Acknowledgement

## News

- 12/11/2024: Release of Technical Report
- 12/04/2024: Release of snowflake-arctic-embed-l-v2.0 and snowflake-arctic-embed-m-v2.0 our newest models with multilingual workloads in mind.

## Models

Snowflake arctic-embed-m-v2.0 is the newest addition to the suite of embedding models Snowflake has released optimizing for retrieval performance and inference efficiency. 
Arctic Embed 2.0 introduces a new standard for multilingual embedding models, combining high-quality multilingual text retrieval without sacrificing performance in English. 
Released under the permissive Apache 2.0 license, Arctic Embed 2.0 is ideal for applications that demand reliable, enterprise-grade multilingual search and retrieval at scale.
Key Features:
- Multilingual without compromise: Excels in English and non-English retrieval, outperforming leading open-source and proprietary models on benchmarks like MTEB Retrieval, CLEF, and MIRACL.
Multilingual without compromise: Excels in English and non-English retrieval, outperforming leading open-source and proprietary models on benchmarks like MTEB Retrieval, CLEF, and MIRACL.
- Inference efficiency: Its 113m non-embedding parameters inference is fast and efficient for any scale.
Inference efficiency: Its 113m non-embedding parameters inference is fast and efficient for any scale.
- Compression-friendly: Achieves high-quality retrieval with embeddings as small as 128 bytes/vector using Matryoshka Representation Learning (MRL) and quantization-aware embedding training. Please note that like our v1.5 model, the MRL for this model is 256 dimensions, and high-quality 128-byte compression is achieved via 4-bit quantization (e.g. using a pq256x4fs fast-scan FAISS index or using the example code published alongside our 1.5 model ).
Compression-friendly: Achieves high-quality retrieval with embeddings as small as 128 bytes/vector using Matryoshka Representation Learning (MRL) and quantization-aware embedding training. Please note that like our v1.5 model, the MRL for this model is 256 dimensions, and high-quality 128-byte compression is achieved via 4-bit quantization (e.g. using a pq256x4fs fast-scan FAISS index or using the example code published alongside our 1.5 model ).
[LINK: pq256x4fs fast-scan FAISS index](https://github.com/facebookresearch/faiss/wiki/The-index-factory#encodings)
[LINK: example code published alongside our 1.5 model](https://github.com/Snowflake-Labs/arctic-embed/blob/main/compressed_embeddings_examples/score_arctic_embed_m_v1dot5_with_quantization.ipynb)
- Long Context Support: arctic-embed-m-v2.0 builds on GTE-multilingual-base which can support a context window of up to 8192 via the use of RoPE.
Long Context Support: arctic-embed-m-v2.0 builds on GTE-multilingual-base which can support a context window of up to 8192 via the use of RoPE.

### Quality Benchmarks

Unlike most other open-source models, Arctic-embed-m-v2.0 excels across English (via MTEB Retrieval) and multilingual (via MIRACL and CLEF). 
You no longer need to support models to empower high-quality English and multilingual retrieval. All numbers mentioned below are the average NDCG@10 across the dataset being discussed.
Aside from high-quality retrieval, arctic delivers embeddings that are easily compressible. By leveraging vector truncation via MRL to decrease vector size by 3x with about 3% degradation in quality. 
Combine MRLed vectors with vector compression (Int4) to power retrieval in 128 bytes per doc.

## Usage

### Using Sentence Transformers

### Using Huggingface Transformers

You can use the transformers package to use Snowflake's arctic-embed model, as shown below. For optimal retrieval quality, use the CLS token to embed each text portion and use the query prefix below (just on the query).

### Using Huggingface Transformers.js

If you haven't already, you can install the Transformers.js JavaScript library from NPM using:
[LINK: Transformers.js](https://huggingface.co/docs/transformers.js)
You can then use the model for retrieval, as follows:

## Contact

Feel free to open an issue or pull request if you have any questions or suggestions about this project.
You also can email Daniel Campos( daniel.campos@snowflake.com ).

## License

Arctic is licensed under the Apache-2 . The released models can be used for commercial purposes free of charge.

## Model tree for Snowflake/snowflake-arctic-embed-m-v2.0

## Spaces using Snowflake/snowflake-arctic-embed-m-v2.0 2

## Collection including Snowflake/snowflake-arctic-embed-m-v2.0

## Paper for Snowflake/snowflake-arctic-embed-m-v2.0

## Evaluation results

- accuracy on MTEB AmazonCounterfactualClassification (en-ext) test set self-reported 66.687
- f1 on MTEB AmazonCounterfactualClassification (en-ext) test set self-reported 55.037
- f1_weighted on MTEB AmazonCounterfactualClassification (en-ext) test set self-reported 73.074
- ap on MTEB AmazonCounterfactualClassification (en-ext) test set self-reported 18.077
- ap_weighted on MTEB AmazonCounterfactualClassification (en-ext) test set self-reported 18.077
- main_score on MTEB AmazonCounterfactualClassification (en-ext) test set self-reported 66.687
- accuracy on MTEB AmazonCounterfactualClassification (en) test set self-reported 66.194
- f1 on MTEB AmazonCounterfactualClassification (en) test set self-reported 60.854
- f1_weighted on MTEB AmazonCounterfactualClassification (en) test set self-reported 69.573
- ap on MTEB AmazonCounterfactualClassification (en) test set self-reported 30.279
- ap_weighted on MTEB AmazonCounterfactualClassification (en) test set self-reported 30.279
- main_score on MTEB AmazonCounterfactualClassification (en) test set self-reported 66.194
- accuracy on MTEB AmazonPolarityClassification (default) test set self-reported 70.359
- f1 on MTEB AmazonPolarityClassification (default) test set self-reported 70.041
- f1_weighted on MTEB AmazonPolarityClassification (default) test set self-reported 70.041
- ap on MTEB AmazonPolarityClassification (default) test set self-reported 64.819
- ap_weighted on MTEB AmazonPolarityClassification (default) test set self-reported 64.819
- main_score on MTEB AmazonPolarityClassification (default) test set self-reported 70.359
- accuracy on MTEB AmazonReviewsClassification (en) test set self-reported 33.766
- f1 on MTEB AmazonReviewsClassification (en) test set self-reported 33.366

--------------------