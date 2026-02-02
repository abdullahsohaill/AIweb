# Snowflake Arctic Embed
**URL:** https://huggingface.co/Snowflake/snowflake-arctic-embed-m
**Page Title:** Snowflake/snowflake-arctic-embed-m · Hugging Face
--------------------


## Snowflake's Arctic-embed-m

News | Models | Usage | Evaluation | Contact | FAQ License | Acknowledgement

## News

12/04/2024: Release of snowflake-arctic-embed-l-v2.0 and snowflake-arctic-embed-m-v2.0 our newest models with multilingual workloads in mind. These models outperform prior versions of Arctic Embed and we suggest these replace prior versions!
07/26/2024: Release preprint [2407.18887] Embedding And Clustering Your Data Can Improve Contrastive Pretraining on arXiv.
07/18/2024: Release of snowflake-arctic-embed-m-v1.5 , capable of producing highly compressible embedding vectors that preserve quality even when squished as small as 128 bytes per vector. Details about the development of this model are available in the launch post on the Snowflake engineering blog .
05/10/2024: Release the technical report on Arctic Embed
04/16/2024: Release the ** snowflake-arctic-embed ** family of text embedding models. The releases are state-of-the-art for Retrieval quality at each of their representative size profiles. Technical Report is coming shortly. For more details, please refer to our Github: Arctic-Text-Embed .
[LINK: Arctic-Text-Embed](https://github.com/Snowflake-Labs/arctic-embed)

## Models

snowflake-arctic-embed is a suite of text embedding models that focuses on creating high-quality retrieval models optimized for performance.
The snowflake-arctic-embedding models achieve state-of-the-art performance on the MTEB/BEIR leaderboard for each of their size variants. Evaluation is performed using these scripts . As shown below, each class of model size achieves SOTA retrieval accuracy compared to other top models.
[LINK: scripts](https://github.com/Snowflake-Labs/snowflake-arctic-embed/tree/main/src)
The models are trained by leveraging existing open-source text representation models, such as bert-base-uncased, and are trained in a multi-stage pipeline to optimize their retrieval performance. First, the models are trained with large batches of query-document pairs where negatives are derived in-batch—pretraining leverages about 400m samples of a mix of public datasets and proprietary web search data. Following pretraining models are further optimized with long training on a smaller dataset (about 1m samples) of triplets of query, positive document, and negative document derived from hard harmful mining. Mining of the negatives and data curation is crucial to retrieval accuracy. A detailed technical report can be found here .
Aside from being great open-source models, the largest model, snowflake-arctic-embed-l , can serve as a natural replacement for closed-source embedding, as shown below.

### snowflake-arctic-embed-xs

This tiny model packs quite the punch. Based on the all-MiniLM-L6-v2 model with only 22m parameters and 384 dimensions, this model should meet even the strictest latency/TCO budgets. Despite its size, its retrieval accuracy is closer to that of models with 100m paramers.

### snowflake-arctic-embed-s

Based on the intfloat/e5-small-unsupervised model, this small model does not trade off retrieval accuracy for its small size. With only 33m parameters and 384 dimensions, this model should easily allow scaling to large datasets.

### snowflake-arctic-embed-m

Based on the intfloat/e5-base-unsupervised model, this medium model is the workhorse that provides the best retrieval performance without slowing down inference.

### snowflake-arctic-embed-m-long

Based on the nomic-ai/nomic-embed-text-v1-unsupervised model, this long-context variant of our medium-sized model is perfect for workloads that can be constrained by the regular 512 token context of our other models. Without the use of RPE, this model supports up to 2048 tokens. With RPE, it can scale to 8192!

### snowflake-arctic-embed-l

Based on the intfloat/e5-large-unsupervised model, this large model is a direct drop-in for closed APIs and delivers the most accurate retrieval experience.

## Usage

### Using Sentence Transformers

You can use the sentence-transformers package to use an snowflake-arctic-embed model, as shown below.
Produces:

### Using Huggingface transformers

You can use the transformers package to use an snowflake-arctic-embed model, as shown below. For optimal retrieval quality, use the CLS token to embed each text portion and use the query prefix below (just on the query).

### Using Transformers.js

If you haven't already, you can install the Transformers.js JavaScript library from NPM by running:
[LINK: Transformers.js](https://huggingface.co/docs/transformers.js)
You can then use the model to compute embeddings as follows:

## Using Infinity

OpenAI compatible API deployment with Infinity and Docker.
[LINK: Infinity](https://github.com/michaelfeil/infinity)

## FAQ

TBD

## Contact

Feel free to open an issue or pull request if you have any questions or suggestions about this project.
You also can email Daniel Campos( daniel.campos@snowflake.com ).

## License

Arctic is licensed under the Apache-2 . The released models can be used for commercial purposes free of charge.

## Acknowledgement

We want to thank the open-source community, which has provided the great building blocks upon which we could make our models.
We thank our modeling engineers, Danmei Xu, Luke Merrick, Gaurav Nuti, and Daniel Campos, for making these great models possible. 
We thank our leadership, Himabindu Pucha, Kelvin So, Vivek Raghunathan, and Sridhar Ramaswamy, for supporting this work. 
We also thank the open-source community for producing the great models we could build on top of and making these releases possible. 
Finally, we thank the researchers who created BEIR and MTEB benchmarks. 
It is largely thanks to their tireless work to define what better looks like that we could improve model performance.

## Model tree for Snowflake/snowflake-arctic-embed-m

## Spaces using Snowflake/snowflake-arctic-embed-m 42

## Collection including Snowflake/snowflake-arctic-embed-m

## Papers for Snowflake/snowflake-arctic-embed-m

## Evaluation results

- accuracy on MTEB AmazonCounterfactualClassification (en) test set self-reported 76.806
- ap on MTEB AmazonCounterfactualClassification (en) test set self-reported 39.312
- f1 on MTEB AmazonCounterfactualClassification (en) test set self-reported 70.482
- accuracy on MTEB AmazonPolarityClassification test set self-reported 82.832
- ap on MTEB AmazonPolarityClassification test set self-reported 77.447
- f1 on MTEB AmazonPolarityClassification test set self-reported 82.772
- accuracy on MTEB AmazonReviewsClassification (en) test set self-reported 38.930
- f1 on MTEB AmazonReviewsClassification (en) test set self-reported 37.980
- map_at_1 on MTEB ArguAna test set self-reported 31.223
- map_at_10 on MTEB ArguAna test set self-reported 47.430
- map_at_100 on MTEB ArguAna test set self-reported 48.208
- map_at_1000 on MTEB ArguAna test set self-reported 48.211
- map_at_3 on MTEB ArguAna test set self-reported 42.579
- map_at_5 on MTEB ArguAna test set self-reported 45.264
- mrr_at_1 on MTEB ArguAna test set self-reported 31.650
- mrr_at_10 on MTEB ArguAna test set self-reported 47.573
- mrr_at_100 on MTEB ArguAna test set self-reported 48.359
- mrr_at_1000 on MTEB ArguAna test set self-reported 48.362
- mrr_at_3 on MTEB ArguAna test set self-reported 42.734
- mrr_at_5 on MTEB ArguAna test set self-reported 45.415

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
Snowflake/snowflake-arctic-embed-m is supported by the following Inference Providers:

--------------------