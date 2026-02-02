# PUG (Photorealistic Unreal Graphics)
**URL:** https://pug.metademolab.com
**Page Title:** Home
--------------------

- Home
- Datasets
- Datasheet
- Research paper
- Home
- Datasets
- Datasheet
- Research paper

## PUG: Animals

The PUG: Animals dataset is for research on out-of-distribution generalization and for studying the representational space of foundation models. It includes:
- 215,040 pre-rendered images using 70 animal assets
- 64 backgrounds
- 3 sizes
- 4 textures
- 4 different camera orientations
By allowing for precise control distribution shifts between training and testing, this dataset can give researchers better insight into how a deep neural network generalizes on held-out variation factors.

## PUG: ImageNet

The PUG: ImageNet dataset provides a novel, useful benchmark for the fine-grained evaluation of the image classifiers’ robustness along several variation factors. It contains:
- 88,328 pre-rendered images using 724 assets
- 151 ImageNet classes
- 64 backgrounds
- 7 sizes
- 10 textures
- 18 camera orientations
- 18 character orientations
- 7 light intensities

## PUG: SPAR

The PUG: SPAR (Scene, Position, Attribute, Relation) dataset is used for the evaluation of vision-language models. It demonstrates how synthetic data can be used to address current benchmarks limitations. It contains:
- 43,560 pre-rendered images
- 10 backgrounds
- 32 animals
- 4 relations (left/right, bottom/top)
- 4 attributes (blue/red, grass/stone)

## Behind the synthetic dataset

We use the Unreal Engine, a powerful game engine well-known in the entertainment industry, to create photorealistic interactive environments from which we can easily sample images with given specifications. The diagram below illustrates how we use the Unreal Engine and sample images to generate PUG datasets.
[LINK: Visit the Github Repository](https://github.com/facebookresearch/PUG)

## Frequently Asked Questions

### What license are these datasets released under?

The PUG family of datasets is released under a CC-BY-NC license with the addenda that they should not be used for Generative AI.

### Can I train generative models on PUG data?

The PUG datasets are intended for model evaluation and discriminative training only and should not be used for training generative models.

### Where do the 3D assets come from?

The data (3D assets) were acquired through the Unreal Engine Marketplace and Sketchfab . Assets were then incorporated into the Unreal Engine to generate realistic 3D scenes and corresponding images. The 3D assets were manually selected to ensure high quality. Visit github for a complete list of assets used.
[LINK: github](https://github.com/facebookresearch/PUG)

### Where can I get more information?

Please check the paper to learn more about our research findings and check the datasheet to learn more about the datasets.

### Research team

Florian Bordes, Shashank Shekhar, Mark Ibrahim, Diane Bouchacourt, Pascal Vincent, Ari S. Morcos

--------------------