# 20 requests/minute<br>50 requests/day<br>Up to 1000 requests/day with $10 lifetime topup
**URL:** https://openrouter.ai/docs/api-reference/limits
**Page Title:** API Rate Limits | Configure Usage Limits in OpenRouter | OpenRouter | Documentation
--------------------

Making additional accounts or API keys will not affect your rate limits, as we
govern capacity globally. We do however have different rate limits for
different models, so you can share the load that way if you do run into
issues.

## Rate Limits and Credits Remaining

To check the rate limit or credits left on an API key, make a GET request to https://openrouter.ai/api/v1/key .
If you submit a valid API key, you should get a response of the form:
There are a few rate limits that apply to certain types of requests, regardless of account status:
- Free usage limits: If you’re using a free model variant (with an ID ending in :free ), you can make up to 20 requests per minute. The following per-day limits apply:
- If you have purchased less than 10 credits, you’re limited to 50 :free model requests per day.
If you have purchased less than 10 credits, you’re limited to 50 :free model requests per day.
- If you purchase at least 10 credits, your daily limit is increased to 1000 :free model requests per day.
If you purchase at least 10 credits, your daily limit is increased to 1000 :free model requests per day.
- DDoS protection : Cloudflare’s DDoS protection will block requests that dramatically exceed reasonable usage.
If your account has a negative credit balance, you may see 402 errors, including for free models. Adding credits to put your balance above zero allows you to use those models again.
Hi, I'm an AI assistant with access to documentation and other content.
Tip: You can toggle this pane with

--------------------