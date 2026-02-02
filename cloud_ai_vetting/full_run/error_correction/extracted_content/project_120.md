# Project
**URL:** https://silent-chen.github.io/PartGen
**Page Title:** PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models
--------------------


## PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models

[LINK: Minghao Chen](https://silent-chen.github.io)
[LINK: Jianyuan Wang](https://jytime.github.io/)
[LINK: David Novotny](https://d-novotny.github.io/)

## CVPR 2025 Highlight

## In this work, we introduce PartGen , a novel method for compositional/part-level 3D generation and reconstruction from various modalities, including text, image, 3D models. PartGen also enables 3D part editing.

## Abstract

Text- or image-to-3D generators and 3D scanners can now produce 3D assets with high-quality shapes and textures.
            These assets typically consist of a single, fused representation, like an implicit neural field, a Gaussian mixture, or a mesh, without any useful structure.
            However, most applications and creative workflows require assets to be made of several meaningful parts that can be manipulated independently.
            To address this gap, we introduce PartGen , a novel approach that generates 3D objects composed of meaningful parts starting from text, an image, or an unstructured 3D object.
            First, given multiple views of a 3D object, generated or rendered, a multi-view diffusion model extracts a set of plausible and view-consistent part segmentations, dividing the object into parts.
            Then, a second multi-view diffusion model takes each part separately, fills in the occlusions, and uses those completed views for 3D reconstruction by feeding them to a 3D reconstruction network.
            This completion process considers the context of the entire object to ensure that the parts integrate cohesively.
            The generative completion model can make up for the information missing due to occlusions; in extreme cases, it can hallucinate entirely invisible parts based on the input 3D asset.
            We evaluate our method on generated and real 3D assets and show that it outperforms segmentation and part-extraction baselines by a large margin.
            We also showcase downstream applications such as 3D part editing.

## Video

## Method

PartGen begins with text, single images, or existing 3D objects to obtain an initial grid view of the
            object. This view is then processed by a diffusion-based segmentation network to achieve multi-view consistent part segmentation. Next,
            the segmented parts, along with contextual information, are input into a multi-view part completion network to generate a fully completed
            view of each part. Finally, a pre-trained reconstruction model generates the 3D parts, which can be assembled according to their spatial location.

## Result

## Part-Aware Text-to-3D

## Part-Aware Image-to-3D

## Real-World 3D Decomposition

## Iteratively Adding Parts

## 3D Part Editing

## BibTeX


--------------------