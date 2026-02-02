# Faraday
**URL:** https://faraday.ai
**Page Title:** Predict customer behavior the speedy way - Faraday
--------------------

We're now featured in the Standard Information App Marketplace !

## When it's time to put down your notebooks

- Data ingress and integrations
- Fully prepared consumer data
- Identity resolution
- Algorithm tuning
- Feature engineering
- Validation & reporting
- Probability calibration for useful scores
- Geonormalization
- Explainability
- Bias detection & mitigation
- Real-time and batch inference
- SOC-2, CCPA, and other regulation
- Lifecycle management

## Faraday is ready

Everything on the left above is included. Just …
- Connect to your existing data sources
- Declare your prediction objectives
- Review automatic reporting
- Deploy your predictions anywhere
- Built-in consumer data: 1,500 attributes
- Built-in ML predictions for key behaviors
- Built-in bias management for safe ML

## Which behavior will you predict?

## Adaptive discounting

## Lead prioritization

## Next best offer

## Repeat purchase readiness

## Thematic personalization

## Let's speedrun with the API

## Create Connections to your data sources

Create Connections to your data sources
[LINK: Connections](/docs/abstractions/connections)
Faraday supports data warehouses like Snowflake and BigQuery , databases like Postgres , and cloud buckets like S3 . Or just start by uploading CSV with POST /uploads .
[LINK: Snowflake](/docs/how-to/connections/snowflake)
[LINK: BigQuery](/docs/how-to/connections/bigquery)
[LINK: Postgres](/docs/how-to/connections/postgres)
[LINK: POST /uploads](/docs/reference/createupload)
[LINK: API POST /connections](/docs/reference/createconnection)

## Create Datasets to import your data

Create Datasets to import your data
[LINK: Datasets](/docs/abstractions/datasets)
You’ll map columns so we can recognize people and extract the 2 necessary events we find in your data.
[LINK: events](/docs/abstractions/events)
[LINK: Signup](/docs/how-to/streams/signup)
[LINK: Transaction](/docs/how-to/streams/transaction)
[LINK: API POST /datasets](/docs/reference/createdataset)

## Create Cohorts to represent key groups

Create Cohorts to represent key groups
[LINK: Cohorts](/docs/abstractions/cohorts)
You'll use the event and trait artifacts produced by your datasets to do this. For this template, you'll need 2 cohorts .
[LINK: Leads](/docs/how-to/cohorts/leads)
[LINK: Customers](/docs/how-to/cohorts/customers)
[LINK: API POST /cohorts](/docs/reference/createcohort)

## Declare your prediction objective

Declare your prediction objective
Faraday has built-in objectives for key customer behaviors. This template uses an outcome to make the necessary predictions.
[LINK: outcome](/docs/abstractions/outcomes)
[LINK: Likelihood to convert](/docs/how-to/predictions/likelihood-to-convert)
[LINK: API POST /outcomes](/docs/reference/createoutcome)

## Use a Scope to make your predictions

Use a Scope to make your predictions
[LINK: Scope](/docs/abstractions/pipelines)
Scopes let you choose a population (using Cohorts) and a payload, including the objective you just created, to prepare for deployment.
[LINK: Lead scoring](/docs/how-to/use-cases/leads/lead-scoring)
[LINK: API POST /scopes](/docs/reference/createscope)

## Use a Target to deploy your predictions

Use a Target to deploy your predictions
[LINK: Target](/docs/abstractions/deployments)
You can add a target to your pipeline for every deployment destination you need for your use case.
[LINK: API POST /targets](/docs/reference/createtarget)
[LINK: End-to-end quickstart](/docs/how-to/use-cases/leads/lead-scoring)

### Ready to ship?

Skip the ML struggle and focus on your downstream application. We have built-in demographic data so you can get started with just your PII.

--------------------