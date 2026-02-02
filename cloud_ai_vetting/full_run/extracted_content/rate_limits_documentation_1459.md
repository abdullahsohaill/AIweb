# Rate Limits Documentation
**URL:** https://ai.google.dev/gemini-api/docs/rate-limits
**Page Title:** Rate limits  |  Gemini API  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemini-api/docs/rate-limits)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemini-api/docs/rate-limits?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemini-api/docs/rate-limits?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemini-api/docs/rate-limits?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemini-api/docs/rate-limits?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Frate-limits&prompt=select_account)
- On this page
- How rate limits work
- Usage tiers
- Gemini API rate limits
- Batch API rate limits
[LINK: Batch API rate limits](#batch-api)
- How to upgrade to the next tier
- Request a rate limit increase
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- Docs
[LINK: Docs](https://ai.google.dev/gemini-api/docs)

## Rate limits

- On this page
- How rate limits work
- Usage tiers
- Gemini API rate limits
- Batch API rate limits
[LINK: Batch API rate limits](#batch-api)
- How to upgrade to the next tier
- Request a rate limit increase
Rate limits regulate the number of requests you can make to the Gemini API
within a given timeframe. These limits help maintain fair usage, protect against
abuse, and help maintain system performance for all users.
View your active rate limits in AI Studio

## How rate limits work

Rate limits are usually measured across three dimensions:
- Requests per minute ( RPM )
- Tokens per minute (input) ( TPM )
- Requests per day ( RPD )
Your usage is evaluated against each limit, and exceeding any of them will
trigger a rate limit error. For example, if your RPM limit is 20, making 21
requests within a minute will result in an error, even if you haven't exceeded
your TPM or other limits.
Rate limits are applied per project, not per API key. Requests per day ( RPD )
quotas reset at midnight Pacific time.
Limits vary depending on the specific model being used, and some limits only
apply to specific models. For example, Images per minute, or IPM, is only
calculated for models capable of generating images (Nano Banana), but is
conceptually similar to TPM. Other models might have a token per day limit (TPD).
Rate limits are more restricted for experimental and preview models.

## Usage tiers

Rate limits are tied to the project's usage tier. As your API usage and spending
increase, you'll have an option to upgrade to a higher tier with increased rate
limits.
The qualifications for Tiers 2 and 3 are based on the total cumulative spending
on Google Cloud services (including, but not limited to, the Gemini API) for the
billing account linked to your project.
[LINK: eligible countries](/gemini-api/docs/available-regions)
[LINK: linked to the project](/gemini-api/docs/billing#enable-cloud-billing)
When you request an upgrade, our automated abuse protection system performs
additional checks. While meeting the stated qualification criteria is generally
sufficient for approval, in rare cases an upgrade request may be denied based on
other factors identified during the review process.
This system helps maintain the security and integrity of the Gemini API platform
for all users.

## Gemini API rate limits

Rate limits depend on a variety of factors (such as your quota tier) and can be
viewed in Google AI Studio. As your tier and account status change over time, your
rate limits will automatically be updated.
View your active rate limits in AI Studio
Specified rate limits are not guaranteed and actual capacity may vary.

## Batch API rate limits

Batch API requests are subject to their own rate
limits, separate from the non-batch API calls.
[LINK: Batch API](/gemini-api/docs/batch-api)
- Concurrent batch requests: 100
- Input file size limit: 2GB
- File storage limit: 20GB
- Enqueued tokens per model: The Batch enqueued tokens table lists the
maximum number of tokens that can be enqueued for batch processing across
all your active batch jobs for a given model.

## How to upgrade to the next tier

The Gemini API uses Cloud Billing for all billing services. To transition from
the Free tier to a paid tier, you must first enable Cloud Billing for your
Google Cloud project.
Once your project meets the specified criteria, it becomes eligible for an
upgrade to the next tier. To request an upgrade, follow these steps:
- Navigate to the API keys page in AI Studio.
[LINK: API keys page](https://aistudio.google.com/app/apikey)
- Locate the project you want to upgrade and click "Upgrade". The "Upgrade" option
will only show up for projects that meet next tier qualifications .
[LINK: next tier qualifications](/gemini-api/docs/rate-limits#usage-tiers)
After a quick validation, the project will be upgraded to the next tier.

## Request a rate limit increase

Each model variation has an associated rate limit (requests per minute, RPM).
For details on those rate limits, see Gemini models .
Request paid tier rate limit increase
We offer no guarantees about increasing your rate limit, but we'll do our best
to review your request.
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2026-01-22 UTC.

--------------------