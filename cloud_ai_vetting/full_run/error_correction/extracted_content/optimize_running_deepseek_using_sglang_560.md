# optimize running DeepSeek using SGLang
**URL:** https://www.amd.com/en/developer/resources/technical-articles/amd-instinct-gpus-power-deepseek-v3-revolutionizing-ai-development-with-sglang.html
**Page Title:** AMD Instinct™ GPUs Power DeepSeek-V3: Revolutionizing AI Development with SGLang
--------------------


## AMD
Instinct™ GPUs Power DeepSeek-V3: Revolutionizing AI Development with SGLang

Jan 07, 2025

## Overview

AMD is excited to announce the integration of the new DeepSeek-V3 model from DeepSeek on AMD Instinct™ GPUs, optimized for performance powered by SGLang ( https://github.com/sgl-project/sglang/releases ). This integration will help accelerate the development of cutting-edge AI applications and experiences. DeepSeek-V3 is an open-source, multimodal AI model designed to empower developers with unparalleled performance and efficiency. By seamlessly integrating advanced capabilities for processing both text and visual data, DeepSeek-V3 sets a new benchmark for productivity, driving innovation and enabling developers to create cutting-edge AI applications.
[LINK: https://github.com/sgl-project/sglang/releases](https://github.com/sgl-project/sglang/releases)
The DeepSeek-V3 model is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were a part of its predecessor, DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. DeepSeek-V3 allows developers to work with advanced models, leveraging memory capabilities to enable processing text and visual data at once, enabling broad access to the latest advancements, and giving developers more features. DeepSeek-V3 achieves the best performance on most benchmarks, especially on math and code tasks.

## AMD Instinct™ GPU Accelerators and DeepSeek-V3

AMD Instinct™ GPUs accelerators are transforming the landscape of multimodal AI models, such as DeepSeek-V3, which require immense computational resources and memory bandwidth to process text and visual data. AMD Instinct™ accelerators deliver outstanding performance in these areas.
Leveraging AMD ROCm™ software and AMD Instinct™ GPU accelerators across key stages of DeepSeek-V3 development further strengthens a long-standing collaboration with AMD and commitment to an open software approach for AI. Scalable infrastructure from AMD enables developers to build powerful visual reasoning and understanding applications.
Extensive FP8 support in ROCm can significantly improve the process of running AI models, especially on the inference side. It helps solve key issues such as memory bottlenecks and high latency issues related to more read-write formats, enabling larger models or batches to be processed within the same hardware constraints, resulting in a more efficient training and inference process. In addition, FP8 reduced precision calculations can reduce delays in data transmission and calculations. AMD ROCm extends support for FP8 in its ecosystem, enabling performance and efficiency improvements in everything from frameworks to libraries.

## Inference with SGLang on AMD Instinct™ GPUs

SGLang: Fully supports the DeepSeek-V3 model inference modes: https://github.com/sgl-project/sglang/releases
[LINK: https://github.com/sgl-project/sglang/releases](https://github.com/sgl-project/sglang/releases)

### Generic Build for ROCm Docker Image

To build Docker image with ROCm support, follow these steps:
- Launch the Docker Container: docker run -it --ipc=host --cap-add=SYS_PTRACE --network=host \ --device=/dev/kfd --device=/dev/dri --security-opt seccomp=unconfined \ --group-add video --privileged -w /workspace lmsysorg/sglang:v0.4.2.post3-rocm630
- Get Started: Login to Hugging Face: Log in to Hugging Face using the CLI: huggingface-cli login Start the SGLang Server: Launch server to host the DeepSeekV3 FP8 Model on your local machine: python3 -m sglang.launch_server --model-path deepseek-ai/DeepSeek-V3 --port 30000 --tp 8 --trust-remote-code Generate Text: Open another terminal and send requests to generate text after server running: curl http://localhost:30000/generate \ -H "Content-Type: application/json" \ -d '{ "text": "Once upon a time,", "sampling_params": { "max_new_tokens": 16, "temperature": 0 } }'
- Login to Hugging Face: Log in to Hugging Face using the CLI: huggingface-cli login
- Start the SGLang Server: Launch server to host the DeepSeekV3 FP8 Model on your local machine: python3 -m sglang.launch_server --model-path deepseek-ai/DeepSeek-V3 --port 30000 --tp 8 --trust-remote-code
- Generate Text: Open another terminal and send requests to generate text after server running: curl http://localhost:30000/generate \ -H "Content-Type: application/json" \ -d '{ "text": "Once upon a time,", "sampling_params": { "max_new_tokens": 16, "temperature": 0 } }'
- Benchmark: export HSA_NO_SCRATCH_RECLAIM=1 one batch throughput and latency: python3 -m sglang.bench_one_batch --batch-size 32 --input 128 --output 32 --model deepseek-ai/DeepSeek-V3 --tp 8 --trust-remote-code server: python3 -m sglang.launch_server --model deepseek-ai/DeepSeek-V3 --tp 8 --trust-remote-code python3 benchmark/gsm8k/bench_sglang.py --num-questions 2000 --parallel 2000 --num-shots 8 Accuracy: 0.952 Invalid: 0.000
Notes: since FP8 training is natively adopted in DeepSeek-v3 framework, it only provides FP8 weights. If the user requires BF16 weights for experimentation, they can use the provided conversion script to perform the transformation. Here is an example of converting FP8 weights to BF16:
cd inference python fp8_cast_bf16.py --input-fp8-hf-path /path/to/fp8_weights --output-bf16-hf-path /path/to/bf16_weights

## AMD and DeepSeek Collaboration: Day 0 Support Readiness:

With the release of DeepSeek-V3, AMD continues its tradition of fostering innovation through close collaboration with the DeepSeek team. This partnership ensures that developers are fully equipped to leverage the DeepSeek-V3 model on AMD Instinct™ GPUs right from Day-0 providing a broader choice of GPUs hardware and an open software stack ROCm™ for optimized performance and scalability. AMD will continue optimizing DeepSeek-v3 performance with CK-tile based kernels on AMD Instinct™ GPUs. AMD is committed to collaborate with open-source model providers to accelerate AI innovation and empower developers to create the next generation of AI experiences.

## Acknowledgement:

We sincerely appreciate the exceptional support and close collaboration with the DeepSeek and SGLang teams. A special thanks to AMD team members Peng Sun, Bruce Xue, Hai Xiao, David Li, Carlus Huang, Mingtao Gu, Vamsi Alla, Jason F., Vinayak Gok, Wun-guo Huang, Caroline Kang, Gilbert Lei, Soga Lin, Jingning Tang, Fan Wu, George Wang, Anshul Gupta, Shucai Xiao, Lixun Zhang, Xicheng (AK) Feng A and everyone else who contributed to this effort.

## Additional Resources:

- Visit the ⁠ ROCm AI Developer Hub for additional tutorials, blogs, open-source projects, and other resources for AI development on AMD GPUs.
[LINK: ROCm AI Developer Hub](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai.html?utm_source=web&utm_medium=amd&utm_campaign=deepseek_blog)
- Explore AMD ROCm™ Software, an open software stack that includes programming models, tools, compilers, libraries, and runtimes for AI and HPC solution development on AMD GPUs: https://www.amd.com/en/products/software/rocm.html
- Discover AMD Instinct™ Accelerators designed to deliver breakthrough performance for AI and HPC workloads: https://www.amd.com/en/products/accelerators/instinct.html
- Learn more about DeepSeek-V3 on Hugging Face, including its architecture and performance benchmarks: https://huggingface.co/deepseek-ai/DeepSeek-V3
- Chat with DeepSeek-V3 on the DeepSeek official chat platform: chat.deepseek.com
- Access DeepSeek’s OpenAI-compatible API to build and integrate your own applications on the DeepSeek platform: platform.deepseek.com
George Wang
Bruce Xue
Anshul Gupta

## Cookie Notice

## Cookie Settings

### Manage Consent Preferences

These cookies allow us to recognize and count the number of visitors and to see how visitors move around the Sites when they use them. This helps us to understand what areas of the Sites are of interest to you and to improve the way the Sites work, for example, by helping you find what you are looking for easily. We may use third party web analytics providers to help us analyze the use of the Sites, email, and newsletters. These cookies store data such as online identifiers (including IP address and device identifiers), information about your web browser and operating system, website usage activity information (including the frequency of your visits, your actions on the Sites and, if you arrived at any of the Sites from another website, i.e. the URL of that website), and content-related activity (including the email and newsletter content you view and click on).
These cookies record online identifiers (including IP address and device identifiers), information about your web browser and operating system, website usage activity information (such as information about your visit to the Sites, the pages you have visited, content you have viewed, and the links you have followed), and content-related activity (including the email and newsletter content you view and click on). The information is used to try to make the Sites, emails, and newsletters, and the advertising displayed on them and other websites more relevant to your interests. For instance, when you visit the Sites, these targeting cookies are used by third party providers for remarketing purposes to allow them to show you advertisements for our products when you visit other websites on the internet. Our third party providers may collect and combine information collected through the Sites, emails, and newsletters with other information about your visits to other websites and apps over time, if those websites and apps also use the same providers.
These cookies are used to recognize you when you return to the Sites.  This enables us to remember your preferences (for example, your choice of language or region) or when you register on areas of the Sites, such as our web programs or extranets. These cookies store data such as online identifiers (including IP address and device identifiers) along with the information used to provide the function.
These are cookies that are technically required for the operation of the Sites. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging into secure areas of the Sites or filling in forms. These cookies store data such as online identifiers (including IP address and device identifiers) along with the information used to operate the Sites. We may estimate your geographic location based on your IP address to help us display the content available in your location and adjust the operation of the Sites.

### Cookie List

- checkbox label label

--------------------