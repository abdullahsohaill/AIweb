# Project
**URL:** https://vertexregen.github.io
**Page Title:** VertexRegen: Mesh Generation with Continuous Level of Detail
--------------------


## VertexRegen : Mesh Generation with Continuous Level of Detail

[LINK: Yawar Siddiqui](https://nihalsid.github.io/)
[LINK: Chris Xie](https://chrisdxie.github.io/)
[LINK: Jakob Engel](https://jakobengel.github.io/)
[LINK: Henry Howard-Jenkins](https://henryhj.github.io/)
[LINK: Code](https://github.com/zx1239856/VertexRegen)

## Generation Demo

### Generation Steps: 189 / 303

## VertexRegen generates mesh from coarse-to-fine with increasing level of detail.

## Abstract

We introduce VertexRegen , a novel mesh generation framework that enables generation at a continuous level of detail. Existing autoregressive methods generate meshes in a partial-to-complete manner and thus intermediate steps of generation represent incomplete structures. VertexRegen takes inspiration from progressive meshes and reformulates the process as the reversal of edge collapse, i.e. vertex split, learned through a generative model. Experimental results demonstrate that VertexRegen produces meshes of comparable quality to state-of-the-art methods while uniquely offering anytime generation with the flexibility to halt at any step to yield valid meshes with varying levels of detail.

## Method Overview

VertexRegen leverages edge collapse to generate training data, where the generation process can be achieved by reversing the edge collapse operation, i.e. vertex split.

## Quantitative Evaluations

VertexRegen achieves comparable quality to state-of-the-art methods.
Unconditional generation under face count constraints. VertexRegen achieves significantly better COV, MMD, and 1-NNA in early stages of generation.

## BibTeX


--------------------