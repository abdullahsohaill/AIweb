# Sana
**URL:** https://nvlabs.github.io/Sana
**Page Title:** SANA
--------------------


## SANA

## Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer

Exploring the Frontiers of Efficient Generative Foundation Models
ICLR 2025 Oral Presentation
Enze Xie 1* , Junsong Chen 1* , Junyu Chen 2,3 , Han Cai 1 , Haotian Tang 2 , Yujun Lin 2 , Zhekai Zhang 2 , Muyang Li 2 , Ligeng Zhu 1 , Yao Lu 1 , Song Han 1,2
[LINK: Enze Xie](https://xieenze.github.io/)
[LINK: Junsong Chen](https://lawrence-cj.github.io/)
[LINK: Han Cai](https://han-cai.github.io//)
1 NVIDIA, 2 MIT, 3 Tsinghua University *Project co-lead
[LINK: Code](https://github.com/NVlabs/Sana)
[LINK: SANA-1.5](https://nvlabs.github.io/Sana/Sana-1.5/)
[LINK: SANA-Sprint](https://nvlabs.github.io/Sana/Sprint/)
[LINK: SANA-Video](https://nvlabs.github.io/Sana/Video/)

## About Sana

We introduce Sana, a text-to-image framework that can efficiently generate images up to 4096 × 4096 resolution.
                    Sana can synthesize high-resolution, high-quality images with strong text-image alignment at a remarkably fast speed,
                    deployable on laptop GPU. Core designs include: Deep compression autoencoder: unlike traditional AEs, which compress images only 8×,
                        we trained an AE that can compress images 32×, effectively reducing the number of latent tokens. Linear DiT: we replace all vanilla attention in DiT with linear attention, which is more efficient at high resolutions without sacrificing quality. Decoder-only text encoder: we replaced T5 with modern decoder-only small LLM as the text encoder and designed
                        complex human instruction with in-context learning to enhance the image-text alignment. Efficient training and sampling: we propose Flow-DPM-Solver to reduce sampling steps,
                        with efficient caption labeling and selection to accelerate convergence. As a result, Sana-0.6B is very competitive with modern giant diffusion model (e.g. Flux-12B),
                    being 20 times smaller and 100+ times faster in measured throughput.
                    Moreover, Sana-0.6B can be deployed on a 16GB laptop GPU, taking less than 1 second to generate a 1024 × 1024 resolution image.
                    Sana enables content creation at low cost.

## Several Core Design Details for Efficiency

• Deep Compression Autoencoder: We introduce a new Deep Compression Autoencoder (DC-AE) that aggressively increases the scaling factor to 32.
              Compared with AE-F8, our AE-F32 outputs 16× fewer latent tokens, which is crucial for efficient training
              and generating ultra-high-resolution images, such as 4K resolution.
• Efficient Linear DiT: We introduce a new linear DiT, replacing vanilla quadratic attention and reducing complexity from O(N 2 ) to O(N)
              Mix-FFN, with 3×3 depth-wise convolution in MLP, enhances the local information of tokens.
              Linear attention achieves comparable results to vanilla, improving 4K generation by 1.7× in latency.
              Mix-FFN also removes the need for positional encoding (NoPE) without quality loss, marking the first DiT without positional embedding. • Decoder-only Small LLM as Text Encoder: We use Gemma, a decoder-only LLM, as the text encoder to enhance understanding and reasoning in prompts.
              Unlike CLIP or T5, Gemma offers superior text comprehension and instruction-following.
              We address training instability and design complex human instructions (CHI) to leverage Gemma’s in-context learning,
              improving image-text alignment.
• Efficient Training and Inference Strategy: We propose automatic labeling and training strategies to improve text-image consistency.
              Multiple VLMs generate diverse re-captions, and a CLIPScore-based strategy selects high-CLIPScore captions to enhance convergence and alignment.
              Additionally, our Flow-DPM-Solver reduces inference steps from 28-50 to 14-20 compared to the Flow-Euler-Solver, with better performance.

## Overall Performance

We compare Sana with the most advanced text-to-image diffusion models in Table 1. For 512 × 512 resolution,
                Sana-0.6 demonstrates a throughput that is 5× faster than PixArt-Σ, which has a similar model size,
                and significantly outperforms it in FID, Clip Score, GenEval, and DPG-Bench. For 1024 × 1024 resolution,
                Sana is considerably stronger than most models with <3B parameters and excels in inference latency.
                Our models achieve competitive performance even when compared to the most advanced large model FLUX-dev.
                For instance, while the accuracy on DPG-Bench is equivalent and slightly lower on GenEval,
                Sana-0.6B’s throughput is 39× faster, and Sana-1.6B is 23× faster.

## Sana-0.6B is Deployable on Laptop GPU

## ComfyUI Usage

We’ve developed a plugin to integrate Sana with ComfyUI. For guidance and sample workflows, please refer to the Sana GitHub .
                Special thanks to city96/ComfyUI_ExtraModels for their open-source contributions.
[LINK: plugin](https://github.com/Efficient-Large-Model/ComfyUI_ExtraModels)
[LINK: Sana GitHub](https://github.com/NVlabs/Sana/blob/main/asset/docs/ComfyUI/comfyui.md)
[LINK: city96/ComfyUI_ExtraModels](https://github.com/city96/ComfyUI_ExtraModels)
[LINK: Sana workflow in ComfyUI](https://github.com/NVlabs/Sana/blob/main/asset/docs/ComfyUI/comfyui.md)
[LINK: Sana + CogVideoX workflow in ComfyUI](https://github.com/NVlabs/Sana/blob/main/asset/docs/ComfyUI/comfyui.md)

## Sana-LoRA Dreambooth

Sana-LoRA is support by 🧨diffusers. Check the our guidance to train your customized models. Original diffusers doc is here .
                We show some samples during Sana-LoRA fine-tuning process below.
[LINK: guidance](https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_lora_dreambooth.md)
[LINK: here](https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_lora_dreambooth.md)
[LINK: Sana-LoRA training samples from 0 to 500 steps](https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_lora_dreambooth.md)

## Sana ControlNet

We implement a ControlNet-Transformer architecture,
                specifically tailored for Transformers, achieving explicit controllability alongside high-quality image generation.
                Try our Demo .
[LINK: Sana-ControlNet architecture](https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_controlnet.md)

## Our Mission

Our mission is to develop efficient, lightweight, and accelerated AI technologies that address practical challenges and deliver fast, open-source solutions.

## BibTeX


--------------------