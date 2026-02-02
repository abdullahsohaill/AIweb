# PIXART-α
**URL:** https://pixart-alpha.github.io
**Page Title:** PIXART-α
--------------------


## PIXART-α: Fast Training of Diffusion
                            Transformer for Photorealistic Text-to-Image Synthesis

## ICLR 2024 Spotlight

[LINK: Junsong
                                    Chen](https://lawrence-cj.github.io/)
[LINK: Chongjian
                                    Ge](https://chongjiange.github.io)
[LINK: Enze Xie](https://xieenze.github.io/)
[LINK: Yue Wu](https://yuewuhkust.github.io/)
[LINK: Zhongdao Wang](https://zhongdao.github.io/)
[LINK: Code](https://github.com/PixArt-alpha/PixArt-alpha)
[LINK: 🧨 Diffusers](https://huggingface.co/docs/diffusers/main/en/api/pipelines/pixart)

## Abstract

The most advanced text-to-image (T2I) models require significant training costs (e.g.,
                            millions of GPU hours), seriously hindering the fundamental innovation for the AIGC
                            community while increasing CO 2 emissions. This paper introduces PIXART-α, a
                            Transformer-based T2I diffusion model whose image generation quality is competitive with
                            state-of-the-art image generators (e.g., Imagen, SDXL, and even Midjourney), reaching
                            near-commercial application standards. Additionally, it supports high-resolution image
                            synthesis up to 1024px resolution with low training cost, as shown in Figure 1 and 2. To
                            achieve this goal, three core designs are proposed: (1) Training strategy decomposition: We
                            devise three distinct training steps that separately optimize pixel dependency, text-image
                            alignment, and image aesthetic quality; (2) Efficient T2I Transformer: We incorporate
                            cross-attention modules into Diffusion Transformer (DiT) to inject text conditions and
                            streamline the computation-intensive class-condition branch; (3) High-informative data: We
                            emphasize the significance of concept density in text-image pairs and leverage a large
                            Vision-Language model to auto-label dense pseudo-captions to assist text-image alignment
                            learning. As a result, PIXART-α's training speed markedly surpasses existing
                            large-scale T2I models, e.g., PIXART-α only takes 10.8% of Stable Diffusion v1.5's
                            training time (~675 vs. ~6,250 A100 GPU days), saving nearly $300,000 ($26,000 vs. $320,000)
                            and reducing 90% CO 2 emissions. Moreover, compared with a larger SOTA model,
                            RAPHAEL, our
                            training cost is merely 1%. Extensive experiments demonstrate that PIXART-α excels in
                            image quality, artistry, and semantic control. We hope PIXART-α will provide new
                            insights to the AIGC community and startups to accelerate building their own high-quality
                            yet low-cost generative models from scratch.

## Online Demo

## Training Efficiency

Comparisons of CO 2 emissions and training cost among T2I generators. PIXART-α
                    achieves an exceptionally low training cost of $26,000. Compared to RAPHAEL, our CO 2 emissions
                    and training costs are merely 1.1% and 0.85%, respectively.

## ControlNet

## ControlNet customization samples from PIXART-α. We use the reference images to
                    generate the corresponding HED edge images and use them as the control signal for PIXART-α
                    ControlNet.

## Dreambooth

## PIXART-α can be combined with Dreambooth. Given a few images and text prompts,
                    PIXART-α can generate high-fidelity images, that exhibit natural interactions with the
                    environment, precise modification of the object colors, demonstrating that PIXART-α can
                    generate images with exceptional quality, and has a strong capability in customized extension.

## More Samples

## BibTeX


--------------------