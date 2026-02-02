# KV-Edit
**URL:** https://xilluill.github.io/projectpages/KV-Edit
**Page Title:** KV-Edit: Training-Free Image Editing for Precise Background Preservation
--------------------


## KV-Edit : Training-Free Image Editing for Precise Background
              Preservation

[LINK: Tianrui Zhu](https://github.com/Xilluill)
[LINK: Shiyi Zhang](https://shiyi-zh0408.github.io)
[LINK: Jiawei Shao](https://shaojiawei07.github.io)
[LINK: Yansong Tang](https://andytang15.github.io)
[LINK: Code](https://github.com/Xilluill/KV-Edit)
[LINK: comfyUI](https://github.com/smthemex/ComfyUI_KV_Edit)

## We propose KV-Edit to address the challenge of background preservation in image
          editing, thereby enhancing the practicality of AI editing. Rather than designing complex mechanisms, we achieve
          impressive results by simplypreserving the key-value pairs of the background. Our method effectively handles
          common semantic editingoperations, including adding, removing, and changing objects.

## 🖼 Results

## 💭 Abstract

Background consistency remains a significant challenge in image editing tasks. Despite extensive
              developments, existing works still face a trade-off between maintaining similarity to the original image
              and generating content that aligns with the target. Here, we propose KV-Edit , a training-free approach that uses KV cache in DiTs to
              maintain background consistency, where background tokens are preserved rather than regenerated,
              eliminating the need for complex mechanism or expensive training, ultimately generating new content that
              seamlessly integrates with the background within user-provided regions. We further explore the memory
              consumption of the KV cache during editing and optimize the space complexity to O(1) using an inversion-free method. Our approach is compatible with
              any DiT-based generative model without additional training. Experiments demonstrate that KV-Edit
              significantly outperforms existing approaches in terms of both background and image quality, even
              surpassing training-based methods.

## ⭐️ Pipeline

We implemented KV Cache in our DiT-based generative model, which stores the key-value pairs of background tokens during the inversion process and concatenates them with foreground content during denoising. Since background tokens are preserved rather than regenerated, KV-Edit can strictly maintain background consistency while generating seamlessly integrated new content.

## 🗒 Quantitative Comparison

Comparison with previous methods on PIE-Bench. VAE * denotes the inherent reconstruction error through direct VAE reconstruction. P2P and MasaCtrl are DDIM-based methods, while RF Inversion and RF Edit are flow-based. BrushEdit and FLUX fill represent training-based methods. NS indicates there is no skip step during inversion. RI indicates the addition of reinitialization strategy. Bold and underlined values denote the best and second-best results respectively.

## Related Links

[1] FLUX
[LINK: FLUX](https://github.com/black-forest-labs/flux/tree/main)
[2] Taming Rectified Flow for Inversion and
            Editing
[LINK: Taming Rectified Flow for Inversion and
            Editing](https://github.com/wangjiangshan0725/RF-Solver-Edit)
[3] BrushEdit: All-In-One Image Inpainting and Editing
[LINK: BrushEdit: All-In-One Image Inpainting and Editing](https://github.com/TencentARC/BrushEdit)
[4] FlowEdit: Inversion-Free Text-Based Editing Using
            Pre-Trained Flow Models
[LINK: FlowEdit: Inversion-Free Text-Based Editing Using
            Pre-Trained Flow Models](https://github.com/fallenshock/FlowEdit)

## BibTeX

If you find our work useful, please cite our paper:

--------------------