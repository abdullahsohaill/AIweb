# llama-3-firefunction-v2
**URL:** https://huggingface.co/fireworks-ai/llama-3-firefunction-v2
**Page Title:** fireworks-ai/llama-3-firefunction-v2 · Hugging Face
--------------------


## FireFunction V2: Fireworks Function Calling Model

Try on Fireworks | API Docs | Demo App | Discord
[LINK: API Docs](https://readme.fireworks.ai/docs/function-calling)
FireFunction is a state-of-the-art function calling model with a commercially viable license. View detailed info in our announcement blog . Key info and highlights:
Comparison with other models:
- Competitive with GPT-4o at function-calling, scoring 0.81 vs 0.80 on a medley of public evaluations
- Trained on Llama 3 and retains Llama 3’s conversation and instruction-following capabilities, scoring 0.84 vs Llama 3’s 0.89 on MT bench
- Significant quality improvements over FireFunction v1 across the broad range of metrics
General info:
🐾 Successor of the FireFunction model
🔆 Support of parallel function calling (unlike FireFunction v1) and good instruction following
💡 Hosted on the Fireworks platform at < 10% of the cost of GPT 4o and 2x the speed

## Intended Use and Limitations

### Supported usecases

The model was tuned to perfom well on a range of usecases including:
- general instruction following
- multi-turn chat mixing vanilla messages with function calls
- single- and parallel function calling
- up to 20 function specs supported at once
- structured information extraction
The model has an 8k context window, like Llama 3

### Out-of-Scope Use

The model was not optimized for the following use cases:
- 100+ function specs
- nested function calling

## Metrics

## Example Usage

See documentation for more detail.
[LINK: documentation](https://readme.fireworks.ai/docs/function-calling)

## Resources

- Fireworks discord with function calling channel
- Documentation
[LINK: Documentation](https://readme.fireworks.ai/docs/function-calling)
- Demo app
- Try in Fireworks prompt playground UI

## Model tree for fireworks-ai/llama-3-firefunction-v2

## Space using fireworks-ai/llama-3-firefunction-v2 1

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
fireworks-ai/llama-3-firefunction-v2 is supported by the following Inference Providers:

--------------------