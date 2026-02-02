# ClipTagger-12b
**URL:** https://huggingface.co/inference-net/ClipTagger-12b
**Page Title:** inference-net/ClipTagger-12b · Hugging Face
--------------------


## ClipTagger-12b

## Model Description

ClipTagger-12b is a 12-billion parameter vision-language model (VLM) designed for video understanding at massive scale. Developed by Inference.net in collaboration with Grass , this model was created to meet the demanding requirements of trillion-scale video frame captioning workloads.
ClipTagger-12b exceeds or matches the performance of GPT-4.1 and Claude 4 Sonnet, while costing 15x less per generation.
The model generates structured, schema-consistent JSON outputs for every video frame, making it ideal for building searchable video databases, content moderation systems, and accessibility tools. It maintains temporal consistency across frames while delivering frontier-quality performance at a fraction of the cost of closed-source alternatives.

### Key Features

- Frontier-quality performance - Comparable to top closed models in captioning quality
- Production-ready - Battle-tested on trillion-scale video frame captioning workloads
- Schema-consistent JSON - Reliable structured output for every frame
- Cost-efficient - Optimized for high-throughput inference
- Open source - Build and deploy without proprietary API dependencies

## Architecture

ClipTagger-12b is based on the Gemma-12B architecture and has been optimized with FP8 quantization for maximum throughput on modern GPUs. The model is specifically tuned for RTX 40-series and H100 GPUs, leveraging native FP8 support for efficient inference.

### Technical Specifications

- Parameters : 12 billion
- Base Architecture : Gemma-12B
- Quantization : FP8 (no quality loss vs bf16)
- Input : Single video frame per request
- Output : Structured JSON with fixed schema
- Supported Formats : JPEG, PNG, WebP, GIF
- Max Image Size : 1MB

## Training

The model was trained on 1 million carefully curated single-frame samples from publicly available video data. Training employed knowledge distillation from a high-quality teacher model to ensure consistent, accurate outputs while maintaining the ability to generalize across diverse video content types.

### Training Process

- Dataset Size : 1M video frames
- Training Method : Teacher-student distillation
- Data Source : Publicly available video content
- Focus : Single-frame understanding with temporal awareness

## Benchmarks

ClipTagger-12b achieves equal or superior performance compared to the leading closed-source models across all major evaluation metrics. Despite being open-source and significantly more cost-effective, our model outperforms Claude 4 Sonnet across every metric and achieves comparable quality to GPT-4.1 .
Performance metrics on our internal evaluation set:
We used Gemini-2.5-Pro as the judge model, which ranks ClipTagger-12b roughly equal to GPT-4.1, and better than Claude 4 Sonnet.
FP8 quantization showed no measurable quality degradation compared to bf16 precision.

## Cost Comparison

ClipTagger-12b delivers frontier-quality performance at a fraction of the cost of closed-source alternatives. Based on typical usage patterns (700 input tokens and 250 output tokens per generation), here's how the costs compare:
ClipTagger-12b offers 15x cost savings compared to GPT-4.1 and 17x cost savings compared to Claude 4 Sonnet, while maintaining comparable quality metrics.

## Usage

### API Access

For production deployments, we recommend using our managed API service which includes advanced features like batch processing, webhooks, and automatic scaling:
Run ClipTagger-12b via Inference.net API →
[LINK: Run ClipTagger-12b via Inference.net API →](https://docs.inference.net/use-cases/video-understanding)

### Required Prompts

The model requires specific system and user prompts for optimal performance. Use these prompts exactly as shown:

### Inference Parameters

- Temperature : 0.1 (recommended for consistency)
- Max Tokens : 2000
- Response Format : {"type": "json_object"}

### Output Schema

The model outputs a fixed JSON structure with the following fields:

## Example Output

Given a nature scene with a wooden boardwalk through grassland:

## Use Cases

- Video Search & Discovery - Build searchable databases with structured metadata
- Content Moderation - Automated content analysis and categorization
- Accessibility - Generate consistent alt-text and scene descriptions
- Ad Verification - Track product visibility and brand appearances
- Video Analytics - Extract insights from large video collections
- Content Management - Automatic tagging and organization of video libraries

## Interested in training your own model?

Contact us at partners@inference.net for a free consultation with our research team.

## Support

- Documentation : docs.inference.net
[LINK: docs.inference.net](https://docs.inference.net/use-cases/video-understanding)
- API Access : Get $25 in free credits when you sign up for an account
- Email : support@inference.net

## License

This model is released under the Apache-2.0 license, allowing for commercial use and modification with proper attribution.

## Space using inference-net/ClipTagger-12b 1

## Evaluation results

- Average Judge Score self-reported 3.530
- ROUGE-1 self-reported 0.674
- ROUGE-L self-reported 0.520
- BLEU self-reported 0.267

--------------------