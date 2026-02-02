# Databricks
**URL:** https://docs.databricks.com/en/machine-learning/foundation-models/index.html
**Page Title:** Databricks Foundation Model APIs | Databricks on AWS
--------------------

This article provides an overview of Foundation Model APIs on Databricks . It includes requirements for use, supported models, and limitations.

## What are Databricks Foundation Model APIs? ​

Mosaic AI Model Serving now supports Foundation Model APIs which allow you to access and query state-of-the-art open models from a serving endpoint. These models are hosted by Databricks and you can quickly and easily build applications that use them without maintaining your own model deployment. Foundation Model APIs is a Databricks Designated Service , which means that it uses Databricks Geos to manage data residency when processing customer content.
The Foundation Model APIs are provided in the following modes:
- Pay-per-token: This is the easiest way to start accessing foundation models on Databricks and is recommended for beginning your journey with Foundation Model APIs. This mode is not designed for high-throughput applications, but can be used for production workloads.
- Provisioned throughput: This mode is recommended for all production workloads, especially those that require high throughput, performance guarantees, fine-tuned models, or have additional security requirements. Provisioned throughput endpoints are available with compliance certifications like HIPAA.
- AI Functions optimized models: This mode is recommended for batch inference workloads. You can choose to run batch inference using any generative AI or ML model using AI Functions.
See Use Foundation Model APIs for guidance on how to use these modes and the supported models.
[LINK: Use Foundation Model APIs](#use-foundation-apis)
Using the Foundation Model APIs you can do the following:
- Query a generalized LLM to verify a project's validity before investing more resources.
- Query a generalized LLM to create a quick proof-of-concept for an LLM-based application before investing in training and deploying a custom model.
- Use a foundation model, along with a vector index, to build a chatbot using retrieval augmented generation (RAG).
- Replace proprietary models with open alternatives to optimize for cost and performance.
- Efficiently compare LLMs to see the best candidate for your use case, or swap a production model with a better performing one.
- Build an LLM application for development or production on top of a scalable, SLA-backed LLM serving solution that can support your production traffic spikes.

## Requirements ​

- Databricks API token to authenticate endpoint requests.
- Serverless compute (for provisioned throughput models).
- A workspace in one of the following supported regions: Pay-per-token regions . Provisioned throughput regions .
- Pay-per-token regions .
- Provisioned throughput regions .

## Use Foundation Model APIs ​

You have multiple options for using the Foundation Model APIs.
The APIs are compatible with OpenAI, so you can use the OpenAI client for querying. You can also use the UI, the Foundation Models APIs Python SDK, the MLflow Deployments SDK, or the REST API for querying supported models. Databricks recommends using the OpenAI client SDK or API for extended interactions and the UI for trying out the feature.
See Use foundation models for scoring examples.

### Pay-per-token Foundation Model APIs ​

Preconfigured endpoints that serve the pay-per-token models are accessible in your Databricks workspace. These pay-per-token models are recommended for getting started. To access them in your workspace, navigate to the Serving tab in the left sidebar. The Foundation Model APIs are located at the top of the Endpoints list view.
- Supported pay-per-token models .
- See Use foundation models for guidance on how to query Foundation Model APIs.
- See Foundation model REST API reference for required parameters and syntax.
[LINK: Foundation model REST API reference](/aws/en/machine-learning/foundation-model-apis/api-reference)

### Provisioned throughput Foundation Model APIs ​

Provisioned throughput provides endpoints with optimized inference for foundation model workloads that require performance guarantees. Databricks recommends provisioned throughput for production workloads.
- Provisioned throughput supported model architectures .
- See Provisioned throughput Foundation Model APIs for a step-by-step guide on how to deploy Foundation Model APIs in provisioned throughout mode.
[LINK: Provisioned throughput Foundation Model APIs](/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)
Provisioned throughput support includes:
- Base models of all sizes . Base models can be accessed using the Databricks Marketplace, or you can alternatively download them from Hugging Face or another external source and register them in the Unity Catalog . The latter approach works with any fine-tuned variant of the supported models.
- Fine-tuned variants of base models , such as models that are fine-tuned on proprietary data.
- Fully custom weights and tokenizers , such as those trained from scratch or continued pre-trained or other variations using the base model architecture (for example, CodeLlama).

### AI Functions for batch inference ​

See Apply AI on data using Databricks AI Functions .
See Deploy batch inference pipelines for how to create batch inference pipelines using AI Functions.

## Limitations ​

See Foundation Model APIs limits .
[LINK: Foundation Model APIs limits](/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits)

## Additional resources ​

- Use foundation models
- Provisioned throughput Foundation Model APIs
[LINK: Provisioned throughput Foundation Model APIs](/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)
- Foundation model REST API reference
[LINK: Foundation model REST API reference](/aws/en/machine-learning/foundation-model-apis/api-reference)
- Deploy batch inference pipelines
- Databricks-hosted foundation models available in Foundation Model APIs
[LINK: Databricks-hosted foundation models available in Foundation Model APIs](/aws/en/machine-learning/foundation-model-apis/supported-models)
- What are Databricks Foundation Model APIs?
[LINK: What are Databricks Foundation Model APIs?](#what-are-databricks-foundation-model-apis)
- Requirements
- Use Foundation Model APIs Pay-per-token Foundation Model APIs Provisioned throughput Foundation Model APIs AI Functions for batch inference
[LINK: Use Foundation Model APIs](#use-foundation-model-apis)
- Pay-per-token Foundation Model APIs
[LINK: Pay-per-token Foundation Model APIs](#pay-per-token-foundation-model-apis)
- Provisioned throughput Foundation Model APIs
[LINK: Provisioned throughput Foundation Model APIs](#provisioned-throughput-foundation-model-apis)
- AI Functions for batch inference
- Limitations
- Additional resources

## We Care About Your Privacy

## Privacy Preference Center

## Privacy Preference Center

- Your Privacy

### Your Privacy

- Strictly Necessary Cookies

### Strictly Necessary Cookies

- Performance Cookies

### Performance Cookies

- Functional Cookies

### Functional Cookies

- Targeting Cookies

### Targeting Cookies

- TOTHR

### TOTHR

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. Opting out of sales, sharing, and targeted advertising Depending on your location, you may have the right to opt out of the “sale” or “sharing” of your personal information or the processing of your personal information for purposes of online “targeted advertising.” You can opt out based on cookies and similar identifiers by disabling optional cookies here. To opt out based on other identifiers (such as your email address), submit a request in our Privacy Request Center . More information
These cookies are necessary for the website to function and cannot be switched off in our systems. They assist with essential site functionality such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will no longer work.
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site.
These cookies enable the website to provide enhanced functionality and personalization. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List

- checkbox label label

--------------------