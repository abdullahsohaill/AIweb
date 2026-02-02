# vfusion3d
**URL:** https://huggingface.co/jadechoghari/vfusion3d
**Page Title:** jadechoghari/vfusion3d · Hugging Face
--------------------


## [ECCV 2024] VFusion3D: Learning Scalable 3D Generative Models from Video Diffusion Models

Porject page , Paper link
[LINK: Porject page](https://junlinhan.github.io/projects/vfusion3d.html)
VFusion3D is a large, feed-forward 3D generative model trained with a small amount of 3D data and a large volume of synthetic multi-view data. It is the first work exploring scalable 3D generative/reconstruction models as a step towards a 3D foundation.
VFusion3D: Learning Scalable 3D Generative Models from Video Diffusion Models Junlin Han , Filippos Kokkinos , Philip Torr GenAI, Meta and TVG, University of Oxford European Conference on Computer Vision (ECCV), 2024
[LINK: VFusion3D: Learning Scalable 3D Generative Models from Video Diffusion Models](https://junlinhan.github.io/projects/vfusion3d.html)
[LINK: Junlin Han](https://junlinhan.github.io/)

## News

- [08.08.2024] HF Demo is available, big thanks to Jade Choghari 's help for making it possible.
[LINK: Jade Choghari](https://github.com/jadechoghari)
- [25.07.2024] Release weights and inference code for VFusion3D.

## Quick Start

Getting started with VFusion3D is super easy! 🤗 Here’s how you can use the model with Hugging Face:

### Install Dependencies (Optional)

Depending on your needs, you may want to enable specific features like mesh generation or video rendering. We've got you covered with these additional packages:

### Load model directly

- Default (Planes): By default, VFusion3D outputs planes—ideal for further 3D operations.
- Export Mesh: Want a 3D mesh? Just set export_mesh=True , and you'll get a .obj file ready to roll. You can also customize the mesh resolution by adjusting the mesh_size parameter.
- Export Video: Fancy a 3D video? Set export_video=True , and you'll receive a beautifully rendered video from multiple angles. You can tweak render_size and fps to get the video just right.
Check out our demo app to see VFusion3D in action! 🤗

## Results and Comparisons

### 3D Generation Results

### User Study Results

## Acknowledgement

- This inference code of VFusion3D heavily borrows from OpenLRM .
[LINK: OpenLRM](https://github.com/3DTopia/OpenLRM)

## Citation

If you find this work useful, please cite us:

## License

- The majority of VFusion3D is licensed under CC-BY-NC, however portions of the project are available under separate license terms: OpenLRM as a whole is licensed under the Apache License, Version 2.0, while certain components are covered by NVIDIA's proprietary license.
- The model weights of VFusion3D is also licensed under CC-BY-NC.
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Spaces using jadechoghari/vfusion3d 5

## Paper for jadechoghari/vfusion3d


--------------------