# LongCat-Video
**URL:** https://huggingface.co/meituan-longcat/LongCat-Video
**Page Title:** meituan-longcat/LongCat-Video · Hugging Face
--------------------


## LongCat-Video

## Model Introduction

We introduce LongCat-Video, a foundational video generation model with 13.6B parameters, delivering strong performance across Text-to-Video , Image-to-Video , and Video-Continuation generation tasks. It particularly excels in efficient and high-quality long video generation, representing our first step toward world models.

### Key Features

- 🌟 Unified architecture for multiple tasks : LongCat-Video unifies Text-to-Video , Image-to-Video , and Video-Continuation tasks within a single video generation framework. It natively supports all these tasks with a single model and consistently delivers strong performance across each individual task.
- 🌟 Long video generation : LongCat-Video is natively pretrained on Video-Continuation tasks, enabling it to produce minutes-long videos without color drifting or quality degradation.
- 🌟 Efficient inference : LongCat-Video generates $720p$, $30fps$ videos within minutes by employing a coarse-to-fine generation strategy along both the temporal and spatial axes. Block Sparse Attention further enhances efficiency, particularly at high resolutions
- 🌟 Strong performance with multi-reward RLHF : Powered by multi-reward Group Relative Policy Optimization (GRPO), comprehensive evaluations on both internal and public benchmarks demonstrate that LongCat-Video achieves performance comparable to leading open-source video generation models as well as the latest commercial solutions.
For more detail, please refer to the comprehensive LongCat-Video Technical Report .

## 🎥 Teaser Video

## Quick Start

### Installation

Clone the repo:
Install dependencies:
FlashAttention-2 is enabled in the model config by default; you can also change the model config to use FlashAttention-3 or xformers.

### Model Download

Download models using huggingface-cli:

### Run Text-to-Video

### Run Image-to-Video

### Run Video-Continuation

### Run Long-Video Generation

### Run Interactive Video Generation

### Run Streamlit

## Evaluation Results

### Text-to-Video

The Text-to-Video MOS evaluation results on our internal benchmark.

### Image-to-Video

The Image-to-Video MOS evaluation results on our internal benchmark.

## Community Works

Community works are welcome! Please PR or inform us in Issue to add your work.
- CacheDiT offers Fully Cache Acceleration support for LongCat-Video with DBCache and TaylorSeer, achieved nearly 1.7x speedup without obvious loss of precision. Visit their example for more details.
[LINK: CacheDiT](https://github.com/vipshop/cache-dit)
[LINK: example](https://github.com/vipshop/cache-dit/blob/main/examples/pipeline/run_longcat_video.py)

## License Agreement

The model weights are released under the MIT License .
Any contributions to this repository are licensed under the MIT License, unless otherwise stated. This license does not grant any rights to use Meituan trademarks or patents.
See the LICENSE file for the full license text.

## Usage Considerations

This model has not been specifically designed or comprehensively evaluated for every possible downstream application.
Developers should take into account the known limitations of large language models, including performance variations across different languages, and carefully assess accuracy, safety, and fairness before deploying the model in sensitive or high-risk scenarios. 
It is the responsibility of developers and downstream users to understand and comply with all applicable laws and regulations relevant to their use case, including but not limited to data protection, privacy, and content safety requirements.
Nothing in this Model Card should be interpreted as altering or restricting the terms of the MIT License under which the model is released.

## Citation

We kindly encourage citation of our work if you find it useful.

## Acknowledgements

We would like to thank the contributors to the Wan , UMT5-XXL , Diffusers and HuggingFace repositories, for their open research.
[LINK: Diffusers](https://github.com/huggingface/diffusers)

## Contact

Please contact us at longcat-team@meituan.com or join our WeChat Group if you have any questions.

## Model tree for meituan-longcat/LongCat-Video

## Spaces using meituan-longcat/LongCat-Video 100

## Paper for meituan-longcat/LongCat-Video

## Run 15,000+ Models Instantly

Inference Providers let you run inference on thousands of models served by our partners using a simple,
							unified, OpenAI-compatible serverless API ( Learn more ).
[LINK: Learn more](/docs/inference-providers)
meituan-longcat/LongCat-Video is supported by the following Inference Providers:

--------------------