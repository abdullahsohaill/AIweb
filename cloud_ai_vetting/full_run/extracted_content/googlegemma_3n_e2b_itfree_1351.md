# google/gemma-3n-e2b-it:free
**URL:** https://openrouter.ai/google/gemma-3n-e2b-it:free
**Page Title:** Gemma 3n 2B (free) - API, Providers, Stats | OpenRouter
--------------------

[LINK: Send traces to your favorite observability platforms with Broadcast (now GA).](/docs/guides/features/broadcast)

## Google: Gemma 3n 2B (free)

### google /gemma-3n-e2b-it:free

Gemma 3n E2B IT is a multimodal, instruction-tuned model developed by Google DeepMind, designed to operate efficiently at an effective parameter size of 2B while leveraging a 6B architecture. Based on the MatFormer architecture, it supports nested submodels and modular composition via the Mix-and-Match framework. Gemma 3n models are optimized for low-resource deployment, offering 32K context length and strong multilingual and reasoning performance across common benchmarks. This variant is trained on a diverse corpus including code, math, web, and multimodal data.

## Providers for Gemma 3n 2B (free)

### OpenRouter routes requests to the best providers that are able to handle your prompt size and parameters, with fallbacks to maximize uptime .

[LINK: routes requests](/docs/provider-routing)

## Performance for Gemma 3n 2B (free)

### Compare different providers across OpenRouter

### Throughput

### Latency

### E2E Latency

## Apps using Gemma 3n 2B (free)

### Top public apps this month

[LINK: Fortytwo Completion Service](/apps?url=https%3A%2F%2Fgithub.com%2Fanomali%2F42)

## Recent activity on Gemma 3n 2B (free)

### Total usage per day on OpenRouter

Prompt tokens measure input size. Reasoning tokens show internal thinking before a response. Completion tokens reflect total output length.

## Uptime stats for Gemma 3n 2B (free)

### Uptime stats for Gemma 3n 2B (free) on the only provider

When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access uptime data programmatically through the Endpoints API
[LINK: Endpoints API](/docs/api/api-reference/endpoints/list-endpoints)
Learn more about our load balancing and customization options.
[LINK: Learn more](/docs/provider-routing)

## Sample code and API for Gemma 3n 2B (free)

### OpenRouter normalizes requests and responses across providers for you.

OpenRouter provides an OpenAI-compatible completion API to 300+ models & providers that you can call directly, or using the OpenAI SDK. Additionally, some third-party SDKs are available.
In the examples below, the OpenRouter-specific headers are optional. Setting them allows your app to appear on the OpenRouter leaderboards.
[LINK: OpenRouter-specific headers](/docs/requests#request-headers)

## Using third-party SDKs

For information about using third-party SDKs and frameworks with OpenRouter, please see our frameworks documentation .
[LINK: frameworks documentation](/docs/guides/community/frameworks-and-integrations-overview)
See the Request docs for all possible fields, and Parameters for explanations of specific sampling parameters.
[LINK: Request docs](/docs/api-reference/overview)
[LINK: Parameters](/docs/api-reference/parameters)

## More models from Google

Gemini 3 Flash Preview is a high speed, high value thinking model designed for agentic workflows, multi turn chat, and coding assistance. It delivers near Pro level reasoning and tool use performance with substantially lower latency than larger Gemini variants, making it well suited for interactive development, long running agent loops, and collaborative coding tasks. Compared to Gemini 2.5 Flash, it provides broad quality improvements across reasoning, multimodal understanding, and reliability.
The model supports a 1M token context window and multimodal inputs including text, images, audio, video, and PDFs, with text output. It includes configurable reasoning via thinking levels (minimal, low, medium, high), structured output, tool use, and automatic context caching. Gemini 3 Flash Preview is optimized for users who want strong reasoning and agentic behavior without the cost or latency of full scale frontier models.
Nano Banana Pro is Google’s most advanced image-generation and editing model, built on Gemini 3 Pro. It extends the original Nano Banana with significantly improved multimodal reasoning, real-world grounding, and high-fidelity visual synthesis. The model generates context-rich graphics, from infographics and diagrams to cinematic composites, and can incorporate real-time information via Search grounding.
It offers industry-leading text rendering in images (including long passages and multilingual layouts), consistent multi-image blending, and accurate identity preservation across up to five subjects. Nano Banana Pro adds fine-grained creative controls such as localized edits, lighting and focus adjustments, camera transformations, and support for 2K/4K outputs and flexible aspect ratios. It is designed for professional-grade design, product visualization, storyboarding, and complex multi-element compositions while remaining efficient for general image creation workflows.
Gemini 3 Pro is Google’s flagship frontier model for high-precision multimodal reasoning, combining strong performance across text, image, video, audio, and code with a 1M-token context window. Reasoning Details must be preserved when using multi-turn tool calling, see our docs here: https://openrouter.ai/docs/use-cases/reasoning-tokens#preserving-reasoning-blocks . It delivers state-of-the-art benchmark results in general reasoning, STEM problem solving, factual QA, and multimodal understanding, including leading scores on LMArena, GPQA Diamond, MathArena Apex, MMMU-Pro, and Video-MMMU. Interactions emphasize depth and interpretability: the model is designed to infer intent with minimal prompting and produce direct, insight-focused responses.
Built for advanced development and agentic workflows, Gemini 3 Pro provides robust tool-calling, long-horizon planning stability, and strong zero-shot generation for complex UI, visualization, and coding tasks. It excels at agentic coding (SWE-Bench Verified, Terminal-Bench 2.0), multimodal analysis, and structured long-form tasks such as research synthesis, planning, and interactive learning experiences. Suitable applications include autonomous agents, coding assistants, multimodal analytics, scientific reasoning, and high-context information processing.
gemini-embedding-001 provides a unified cutting edge experience across domains, including science, legal, finance, and coding. This embedding model has consistently held a top spot on the Massive Text Embedding Benchmark (MTEB) Multilingual leaderboard since the experimental launch in March.
Gemini 2.5 Flash Image, a.k.a. "Nano Banana," is now generally available. It is a state of the art image generation model with contextual understanding. It is capable of image generation, edits, and multi-turn conversations. Aspect ratios can be controlled with the image_config API Parameter
Gemini 2.5 Flash Preview September 2025 Checkpoint is Google's state-of-the-art workhorse model, specifically designed for advanced reasoning, coding, mathematics, and scientific tasks. It includes built-in "thinking" capabilities, enabling it to provide responses with greater accuracy and nuanced context handling.
Additionally, Gemini 2.5 Flash is configurable through the "max tokens for reasoning" parameter, as described in the documentation ( https://openrouter.ai/docs/use-cases/reasoning-tokens#max-tokens-for-reasoning ).
Gemini 2.5 Flash-Lite is a lightweight reasoning model in the Gemini 2.5 family, optimized for ultra-low latency and cost efficiency. It offers improved throughput, faster token generation, and better performance across common benchmarks compared to earlier Flash models. By default, "thinking" (i.e. multi-pass reasoning) is disabled to prioritize speed, but developers can enable it via the Reasoning API parameter to selectively trade off cost for intelligence.
Gemini 2.5 Flash Image Preview, a.k.a. "Nano Banana," is a state of the art image generation model with contextual understanding. It is capable of image generation, edits, and multi-turn conversations.
Gemini 2.5 Flash-Lite is a lightweight reasoning model in the Gemini 2.5 family, optimized for ultra-low latency and cost efficiency. It offers improved throughput, faster token generation, and better performance across common benchmarks compared to earlier Flash models. By default, "thinking" (i.e. multi-pass reasoning) is disabled to prioritize speed, but developers can enable it via the Reasoning API parameter to selectively trade off cost for intelligence.
Gemma 3n E2B IT is a multimodal, instruction-tuned model developed by Google DeepMind, designed to operate efficiently at an effective parameter size of 2B while leveraging a 6B architecture. Based on the MatFormer architecture, it supports nested submodels and modular composition via the Mix-and-Match framework. Gemma 3n models are optimized for low-resource deployment, offering 32K context length and strong multilingual and reasoning performance across common benchmarks. This variant is trained on a diverse corpus including code, math, web, and multimodal data.
Gemini 2.5 Flash is Google's state-of-the-art workhorse model, specifically designed for advanced reasoning, coding, mathematics, and scientific tasks. It includes built-in "thinking" capabilities, enabling it to provide responses with greater accuracy and nuanced context handling.
Additionally, Gemini 2.5 Flash is configurable through the "max tokens for reasoning" parameter, as described in the documentation ( https://openrouter.ai/docs/use-cases/reasoning-tokens#max-tokens-for-reasoning ).
Gemini 2.5 Pro is Google’s state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs “thinking” capabilities, enabling it to reason through responses with enhanced accuracy and nuanced context handling. Gemini 2.5 Pro achieves top-tier performance on multiple benchmarks, including first-place positioning on the LMArena leaderboard, reflecting superior human-preference alignment and complex problem-solving abilities.
Gemini 2.5 Pro is Google’s state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs “thinking” capabilities, enabling it to reason through responses with enhanced accuracy and nuanced context handling. Gemini 2.5 Pro achieves top-tier performance on multiple benchmarks, including first-place positioning on the LMArena leaderboard, reflecting superior human-preference alignment and complex problem-solving abilities.
Gemma 1 2B by Google is an open model built from the same research and technology used to create the Gemini models .
Gemma models are well-suited for a variety of text generation tasks, including question answering, summarization, and reasoning.
Usage of Gemma is subject to Google's Gemma Terms of Use .
Gemma 3n E4B-it is optimized for efficient execution on mobile and low-resource devices, such as phones, laptops, and tablets. It supports multimodal inputs—including text, visual data, and audio—enabling diverse tasks such as text generation, speech recognition, translation, and image analysis. Leveraging innovations like Per-Layer Embedding (PLE) caching and the MatFormer architecture, Gemma 3n dynamically manages memory usage and computational load by selectively activating model parameters, significantly reducing runtime resource requirements.
This model supports a wide linguistic range (trained in over 140 languages) and features a flexible 32K token context window. Gemma 3n can selectively load parameters, optimizing memory and computational efficiency based on the task or device capabilities, making it well-suited for privacy-focused, offline-capable applications and on-device AI solutions. Read more in the blog post
Gemma 3n E4B-it is optimized for efficient execution on mobile and low-resource devices, such as phones, laptops, and tablets. It supports multimodal inputs—including text, visual data, and audio—enabling diverse tasks such as text generation, speech recognition, translation, and image analysis. Leveraging innovations like Per-Layer Embedding (PLE) caching and the MatFormer architecture, Gemma 3n dynamically manages memory usage and computational load by selectively activating model parameters, significantly reducing runtime resource requirements.
This model supports a wide linguistic range (trained in over 140 languages) and features a flexible 32K token context window. Gemma 3n can selectively load parameters, optimizing memory and computational efficiency based on the task or device capabilities, making it well-suited for privacy-focused, offline-capable applications and on-device AI solutions. Read more in the blog post
Gemini 2.5 Pro is Google’s state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs “thinking” capabilities, enabling it to reason through responses with enhanced accuracy and nuanced context handling. Gemini 2.5 Pro achieves top-tier performance on multiple benchmarks, including first-place positioning on the LMArena leaderboard, reflecting superior human-preference alignment and complex problem-solving abilities.
This model has been deprecated by Google in favor of the (paid Preview model)[google/gemini-2.5-pro-preview]
 
Gemini 2.5 Pro is Google’s state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs “thinking” capabilities, enabling it to reason through responses with enhanced accuracy and nuanced context handling. Gemini 2.5 Pro achieves top-tier performance on multiple benchmarks, including first-place positioning on the LMArena leaderboard, reflecting superior human-preference alignment and complex problem-solving abilities.
Gemma 3 1B is the smallest of the new Gemma 3 family. It handles context windows up to 32k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling. Note: Gemma 3 1B is not multimodal. For the smallest multimodal Gemma 3 model, please see Gemma 3 4B
Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling.
Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling.
Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling. Gemma 3 12B is the second largest in the family of Gemma 3 models after Gemma 3 27B
Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling. Gemma 3 12B is the second largest in the family of Gemma 3 models after Gemma 3 27B
Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling. Gemma 3 27B is Google's latest open source model, successor to Gemma 2
Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling. Gemma 3 27B is Google's latest open source model, successor to Gemma 2
Gemini 2.0 Flash Lite offers a significantly faster time to first token (TTFT) compared to Gemini Flash 1.5 , while maintaining quality on par with larger models like Gemini Pro 1.5 , all at extremely economical token prices.
Gemini Flash 2.0 offers a significantly faster time to first token (TTFT) compared to Gemini Flash 1.5 , while maintaining quality on par with larger models like Gemini Pro 1.5 . It introduces notable enhancements in multimodal understanding, coding capabilities, complex instruction following, and function calling. These advancements come together to deliver more seamless and robust agentic experiences.
Gemini Flash 2.0 offers a significantly faster time to first token (TTFT) compared to Gemini Flash 1.5 , while maintaining quality on par with larger models like Gemini Pro 1.5 . It introduces notable enhancements in multimodal understanding, coding capabilities, complex instruction following, and function calling. These advancements come together to deliver more seamless and robust agentic experiences.
Experimental release (November 21st, 2024) of Gemini.
Gemini 11-14 (2024) experimental model features "quality" improvements.
Gemini Flash 1.5 8B is optimized for speed and efficiency, offering enhanced performance in small prompt tasks like chat, transcription, and translation. With reduced latency, it is highly effective for real-time and large-scale operations. This model focuses on cost-effective solutions while maintaining high-quality results.
Click here to learn more about this model .
Usage of Gemini is subject to Google's Gemini Terms of Use .
Gemini 1.5 Flash Experimental is an experimental version of the Gemini 1.5 Flash model.
Usage of Gemini is subject to Google's Gemini Terms of Use .
#multimodal
Note: This model is experimental and not suited for production use-cases. It may be removed or redirected to another model in the future.
Gemini 1.5 Pro Experimental is a bleeding-edge version of the Gemini 1.5 Pro model. Because it's currently experimental, it will be heavily rate-limited by Google.
Usage of Gemini is subject to Google's Gemini Terms of Use .
#multimodal
Gemma 2 27B by Google is an open model built from the same research and technology used to create the Gemini models .
Gemma models are well-suited for a variety of text generation tasks, including question answering, summarization, and reasoning.
See the launch announcement for more details. Usage of Gemma is subject to Google's Gemma Terms of Use .
Gemma 2 9B by Google is an advanced, open-source language model that sets a new standard for efficiency and performance in its size class.
Designed for a wide variety of tasks, it empowers developers and researchers to build innovative applications, while maintaining accessibility, safety, and cost-effectiveness.
See the launch announcement for more details. Usage of Gemma is subject to Google's Gemma Terms of Use .
Gemini 1.5 Flash is a foundation model that performs well at a variety of multimodal tasks such as visual understanding, classification, summarization, and creating content from image, audio and video. It's adept at processing visual and text inputs such as photographs, documents, infographics, and screenshots.
Gemini 1.5 Flash is designed for high-volume, high-frequency tasks where cost and latency matter. On most common tasks, Flash achieves comparable quality to other Gemini Pro models at a significantly reduced cost. Flash is well-suited for applications like chat assistants and on-demand content generation where speed and scale matter.
Usage of Gemini is subject to Google's Gemini Terms of Use .
#multimodal
Google's latest multimodal model, supports image and video[0] in text or chat prompts.
Optimized for language tasks including:
Usage of Gemini is subject to Google's Gemini Terms of Use .
Gemma by Google is an advanced, open-source language model family, leveraging the latest in decoder-only, text-to-text technology. It offers English language capabilities across text generation tasks like question answering, summarization, and reasoning. The Gemma 7B variant is comparable in performance to leading open source models.
Usage of Gemma is subject to Google's Gemma Terms of Use .
PaLM 2 fine-tuned for chatbot conversations that help with code-related questions.
PaLM 2 is a language model by Google with improved multilingual, reasoning and coding capabilities.
PaLM 2 fine-tuned for chatbot conversations that help with code-related questions.
PaLM 2 is a language model by Google with improved multilingual, reasoning and coding capabilities.

--------------------