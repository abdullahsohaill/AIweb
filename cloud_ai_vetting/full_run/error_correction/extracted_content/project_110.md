# Project
**URL:** https://samxuxiang.github.io/skexgen
**Page Title:** SkexGen: Autoregressive Generation of CAD Construction Sequences with Disentangled Codebooks
--------------------


## SkexGen: Autoregressive Generation of CAD Construction Sequences with Disentangled Codebooks

Xiang Xu , Karl D.D. Willis , Joseph G. Lambourne , Chin-Yi Cheng , Pradeep Kumar Jayaraman , Yasutaka Furukawa , ICML 2022
[LINK: Xiang Xu](https://samxuxiang.github.io/)
[LINK: Code](https://github.com/samxuxiang/SkexGen)

## Abstract

This paper presents a novel autoregressive generative model for computer-aided design (CAD) construction sequences, in particular,
        sketch-and-extrude operations. Our model SkexGen utilizes distinct Transformer architectures to encode topological and geometric variations of
        construction sequences into disentangled codebooks. Autoregressive Transformer decoders generate CAD construction sequences sharing certain
        topological and geometric properties specified by the codebook vectors. Extensive experimental validations demonstrate that our 
        disentangled codebook representation generates diverse and high-quality CAD models, enhances user control, and
        enables efficient exploration of the design space.

## Video

## Framework

SkexGen architecture has two branches. The sketch branch (left) has two encoders that learn topological and geometric variations
        of sketches in two codebooks. An autoregressive decoder generates the code subsequence given codebook vectors. The extrude branch
        (right) has an encoder and a decoder that learns variations of extrude and binary solid operations. Two branches are trained independently.
        Another autoregressive decoder learns to select effective combinations of quantized codes from the three codebooks.

## Random Generation Result

Codes are randomly sampled based on code prior and then pass to SkexGen decoders for autoregressive generation. We demonstrate that SkexGen can generate high-quality and diverse sketch-and-extrude CAD construction sequences (rendered here for visualization).

## Conditional Generation Result

Conditioned on the same code, SkexGen can generate diverse shapes with similar topology, geometry, or extrusion features.

## Design Exploration Result

SkexGen supports efficient design exploration where codes from different models are mixed to create a new one.

## Latent Interpolation Result

SkexGen can generate intermediate CAD models by performing latent interpolation in the code space.  Topology, geometry, and extrude codes are interpolated together.  Left-most column is the source and right-most column is the target shape

## Bibtex

## Acknowledgement

This research is supported by NSERC Discovery Grants, NSERC Discovery Grants Accelerator Supplements, and DND/NSERC Discovery Grants.

--------------------