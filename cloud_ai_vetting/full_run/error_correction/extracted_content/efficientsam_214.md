# EfficientSAM
**URL:** https://yformer.github.io/efficient-sam
**Page Title:** EfficientSAM
--------------------


## EfficientSAM:

## Leveraged Masked Image Pretraining for Efficient Segment Anything

[LINK: Lemeng Wu *](https://github.com/klightz/)
[LINK: Dilin Wang](https://wdilin.github.io/)
[LINK: Vikas Chandra](https://v-chandra.github.io/)
[LINK: Code](https://github.com/yformer/EfficientSAM)

## Abstract

Segment Anything Model (SAM) has emerged as a powerful tool for numerous vision applications. A key component that drives the impressive performance for zero-shot transfer and high versatility is a super large Transformer model trained on the extensive high-quality SA-1B dataset. While beneficial, the huge computation cost of SAM model has limited its applications to wider real-world applications. To address this limitation, we propose EfficientSAMs, light-weight SAM models that exhibit decent performance with largely reduced complexity. Our idea is based on leveraging masked image pretraining, SAMI, which learns to reconstruct features from SAM image encoder for effective visual representation learning. Further, we take SAMI-pretrained light-weight image encoders and mask decoder to build EfficientSAMs, and finetune the models on SA-1B for segment anything task. We perform evaluations on multiple vision tasks including image classification, object detection, instance segmentation, and semantic object detection, and find that our proposed pretraining method, SAMI, consistently outperforms other masked image pretraining methods. On segment anything task such as zero-shot instance segmentation, our EfficientSAMs with SAMI-pretrained lightweight image encoders perform favorably with a significant gain (e.g., ~4 AP  on COCO/LVIS) over other fast SAM models.

## Method

Our proposed EfficientSAM contains two stages: SAMI pretraining (top) on ImageNet and SAM finetuning (bottom) on SA-1B.

### The overview of EfficientSAM framework.

The overview of EfficientSAM framework.

## Quantative Results

### Zero-shot instance segmentation results on COCO/LVIS.

Zero-shot instance segmentation results on COCO/LVIS.

## Qualitative Results

### Point prompt instance segmentation: Input (left), SAM (middle), EfficientSAM (right).

Point prompt instance segmentation: Input (left), SAM (middle), EfficientSAM (right).

### Box prompt instance segmentation: Input (left), SAM (middle), EfficientSAM (right).

Box prompt instance segmentation: Input (left), SAM (middle), EfficientSAM (right).

### Segment everything: Input (left), SAM (middle), EfficientSAM (right).

Segment everything: Input (left), SAM (middle), EfficientSAM (right).

### Salient instance segmentation: Input (left), Mask (middle), Segmentation (right).

Salient instance segmentation: Input (left), Mask (middle), Segmentation (right).

## BibTeX

## Acknowledgement

This website is adapted from Nerfies , licensed under a Creative
      Commons Attribution-ShareAlike 4.0 International License .
[LINK: Nerfies](https://github.com/nerfies/nerfies.github.io)

--------------------