# SMERF
**URL:** https://smerf-3d.github.io
**Page Title:** SMERF
--------------------


## SMERF : Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration

- Daniel Duckworth* 1
- Peter Hedman* 2
- Christian Reiser 2,4
[LINK: Christian Reiser 2,4](https://creiser.github.io/)
- Peter Zhizhin 2
- Jean-François Thibert 3
- Mario Lučić 1
- Richard Szeliski 2
- Jonathan T. Barron 2
- Google DeepMind 1
- Google Research 2
- Google Inc. 3
- Tübingen AI Center,  University of Tübingen 4
- equal contribution*
- Paper
- Video
- Demos
- Code
[LINK: Code](https://github.com/google-research/google-research/tree/master/smerf)
- Data

### Abstract

Recent techniques for real-time view synthesis have rapidly advanced in
                fidelity and speed, and modern methods are capable of rendering
                near-photorealistic scenes at interactive frame rates. At the same time, a
                tension has arisen between explicit scene representations amenable to
                rasterization and neural fields built on ray marching, with state-of-the-art
                instances of the latter surpassing the former in quality while being
                prohibitively expensive for real-time applications. In this work, we introduce
                SMERF, a view synthesis approach that achieves state-of-the-art accuracy among
                real-time methods on large scenes with footprints up to 300 m^2 at a volumetric
                resolution of 3.5 mm^3 . Our method is built upon two primary contributions: a
                hierarchical model partitioning scheme, which increases model capacity while
                constraining compute and memory consumption, and a distillation training
                strategy that simultaneously yields high fidelity and internal consistency. Our
                approach enables full six degrees of freedom (6DOF) navigation within a web
                browser and renders in real-time on commodity smartphones and laptops .
                Extensive experiments show that our method exceeds the current state-of-the-art
                in real-time novel view synthesis by 0.78 dB on standard benchmarks and 1.78 dB
                on large scenes , renders frames three orders of magnitude faster than
                state-of-the-art radiance field models, and achieves real-time performance
                across a wide variety of commodity devices, including smartphones.

### Video

### Real-Time Interactive Viewer Demos

- Berlin
- NYC
- Alameda
- London
- Gardenvase
- Bicycle
- Kitchen Lego
- Stump
- Office Bonsai
- Full Living Room
- Kitchen Counter
- Treehill & Flower

### How we boost representation power to handle large scenes

(a) : We model large multi-room scenes with a number of independent submodels, each of which is
                        assigned to a different region of the scene.  During rendering the submodel is picked
                        based on camera origin. (b) : To model complex view-dependent effects, within each submodel
                        we additionally instantiate grid-aligned copies of deferred MLP parameters θ . These
                        parameters are trilinearly interpolated based on camera origin o . (c) : While each submodel represents the entire scene, only the submodel's assiociated grid cell
                        is modelled with high resolution, which is realized by contracting the submodel-specific local coordinates.

### Getting the maximum out of our representation via distillation

We demonstrate that image fidelity can be greatly boosted via distillation. We first train a
                    state-of-the-art offline radiance field (Zip-NeRF). We then use the RGB color predictions c of this teacher
                    model as supervision for our own model. Additionally, we access the volumetric density values τ of the
                    pre-trained teacher by minimizing the discrepancy of volume rendering weights between teacher and student.

### Datasets & Teacher Checkpoints

SMERF models are distilled from Zip-NeRF checkpoints trained on the Mip-NeRF 360 and Zip-NeRF scenes.
          The checkpoints below are used to recreate the quantitative results in the published text.
          Both datasets and checkpoints are released under CC-BY 4.0 license.
          See text for additional details.
[LINK: Download All](https://storage.googleapis.com/gresearch/refraw360/360_checkpoints.zip)
[LINK: Alameda](https://storage.googleapis.com/gresearch/refraw360/zipnerf/alameda.zip)
[LINK: Berlin](https://storage.googleapis.com/gresearch/refraw360/zipnerf/berlin.zip)
[LINK: London](https://storage.googleapis.com/gresearch/refraw360/zipnerf/london.zip)
[LINK: NYC](https://storage.googleapis.com/gresearch/refraw360/zipnerf/nyc.zip)
[LINK: Download All](https://storage.googleapis.com/gresearch/refraw360/zipnerf/checkpoints.zip)
[LINK: Alameda](https://storage.googleapis.com/gresearch/refraw360/zipnerf-undistorted/alameda.zip)
[LINK: Berlin](https://storage.googleapis.com/gresearch/refraw360/zipnerf-undistorted/berlin.zip)
[LINK: London](https://storage.googleapis.com/gresearch/refraw360/zipnerf-undistorted/london.zip)
[LINK: NYC](https://storage.googleapis.com/gresearch/refraw360/zipnerf-undistorted/nyc.zip)
[LINK: Download All](https://storage.googleapis.com/gresearch/refraw360/zipnerf-undistorted/checkpoints.zip)

### Citation

If you want to cite our work, please use:

### Acknowledgements

The website template was borrowed from Michaël
                        Gharbi .
                    Image sliders are based on dics .
[LINK: dics](https://github.com/abelcabezaroman/definitive-image-comparison-slider)

--------------------