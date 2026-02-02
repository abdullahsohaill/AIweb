# OpenRouter usage accounting
**URL:** https://openrouter.ai/docs/use-cases/usage-accounting
**Page Title:** Usage Accounting | Track AI Model Usage with OpenRouter | OpenRouter | Documentation
--------------------

The OpenRouter API provides built-in Usage Accounting that allows you to track AI model usage without making additional API calls. This feature provides detailed information about token counts, costs, and caching status directly in your API responses.

## Usage Information

OpenRouter automatically returns detailed usage information with every response, including:
- Prompt and completion token counts using the model’s native tokenizer
- Cost in credits
- Reasoning token counts (if applicable)
- Cached token counts (if available)
This information is included in the last SSE message for streaming responses, or in the complete response for non-streaming requests. No additional parameters are required.
The usage: { include: true } and stream_options: { include_usage: true } parameters are deprecated and have no effect. Full usage details are now always included automatically in every response.

## Response Format

Every response includes a usage object with detailed token information:
cached_tokens is the number of tokens that were read from the cache. cache_write_tokens is the number of tokens that were written to the cache (only returned for models with explicit caching and cache write pricing).

## Cost Breakdown

The usage response includes detailed cost information:
- cost : The total amount charged to your account
- cost_details.upstream_inference_cost : The actual cost charged by the upstream AI provider
Note: The upstream_inference_cost field only applies to BYOK (Bring Your Own Key) requests.

## Benefits

- Efficiency : Get usage information without making separate API calls
- Accuracy : Token counts are calculated using the model’s native tokenizer
- Transparency : Track costs and cached token usage in real-time
- Detailed Breakdown : Separate counts for prompt, completion, reasoning, and cached tokens

## Best Practices

- Use the usage data to monitor token consumption and costs
- Consider tracking usage in development to optimize token usage before production
- Use the cached token information to optimize your application’s performance

## Alternative: Getting Usage via Generation ID

You can also retrieve usage information asynchronously by using the generation ID returned from your API calls. This is particularly useful when you want to fetch usage statistics after the completion has finished or when you need to audit historical usage.
To use this method:
- Make your chat completion request as normal
- Note the id field in the response
- Use that ID to fetch usage information via the /generation endpoint
For more details on this approach, see the Get a Generation documentation.
[LINK: Get a Generation](/docs/api-reference/get-a-generation)

## Examples

### Basic Usage with Token Tracking

### Streaming with Usage Information

This example shows how to handle usage information in streaming mode:
Hi, I'm an AI assistant with access to documentation and other content.
Tip: You can toggle this pane with

--------------------