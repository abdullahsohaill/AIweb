# TryOnDiffusion
**URL:** https://tryondiffusion.github.io
**Page Title:** TryOnDiffusion: A Tale of Two UNets
--------------------

Person
Garment
Try-on

## TryOnDiffusion: A Tale of Two UNets

Luyang Zhu 1,2 , Dawei Yang 2 , Tyler Zhu 2 , Fitsum Reda 2 , William Chan 2 , Chitwan Saharia 2 , Mohammad Norouzi 2 , Ira Kemelmacher-Shlizerman 1,2
[LINK: Fitsum Reda](https://fitsumreda.github.io/)
[LINK: Mohammad Norouzi](https://norouzi.github.io/)
1 University of Washington 2 Google Research
IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2023
Given two images depicting a person and a garment worn by another person,
          our goal is to generate a visualization of how the garment might look on the input person.
          A key challenge is to synthesize a photorealistic detail-preserving visualization of the garment,
          while warping the garment to accommodate a significant body pose and shape change across the subjects.
          Previous methods either focus on garment detail preservation without effective pose and shape variation,
          or allow try-on with the desired shape and pose but lack garment details.
          In this paper, we propose a diffusion-based architecture that unifies two UNets (referred to as Parallel-UNet),
          which allows us to preserve garment details and warp the garment for significant pose and body change in a single network.
          The key ideas behind Parallel-UNet include: 1) garment is warped implicitly via a cross attention mechanism,
          2) garment warp and person blend happen as part of a unified process as opposed to a sequence of two separate tasks.
          Experimental results indicate that TryOnDiffusion achieves state-of-the-art performance both qualitatively and quantitatively.

## Approach

Overall Pipeline: During preprocessing step, the target person is segmented out of the person image creating “clothing agnostic RGB” image,
            the target garment is segmented out of the garment image, and pose is computed for both person and garment images.
            These inputs are taken into 128×128 Parallel-UNet (key contribution) to create the 128x128 try-on image
            which is further sent as input to the 256×256 Parallel-UNet together with the try-on conditional inputs.
            Output from 256×256 Parallel-UNet is sent to standard super resolution diffusion to create the 1024×1024 image
The architecture of 128×128 Parallel-UNet.
            The person-UNet (top) takes the clothing-agnostic RGB and the noisy image as input.
            Since both inputs are pixel-wise aligned,
            we directly concatenate them along the channel dimension at the beginning of UNet processing.
            The garment-UNet (bottom) takes the segmented garment image as input.
            The garment features are fused to the target image via cross attentions.
            To save model parameters, we early stop the garment-UNet after the 32×32 upsampling block,
            where the final cross attention module in person-UNet is done.
            The person and garment poses are first fed into the linear layers to compute pose embeddings separately.
            The pose embeddings are then fused to the person-UNet through the attention mechanism.
            Besides, they are used to modulate features for both UNets using FiLM across all scales.

## Multiple people try-on same garment

## Same person try-on different garments

## Interactive Try-on demo

Person
Try-on
Garment

## Comparison to State-of-the-art Methods

## Qualitative comparison on challenging cases (extreme body pose and shape differences)

Input
TryOnGAN
SDAFN
HR-VITON
Ours
Input
TryOnGAN
SDAFN
HR-VITON
Ours

## Qualitative comparison on simple cases (minimum garment warp and simple texture pattern)

Input
TryOnGAN
SDAFN
HR-VITON
Ours
Input
TryOnGAN
SDAFN
HR-VITON
Ours

## Limitations

There are several limitations for TryOnDiffusion.
          First, our method exhibits garment leaking artifacts in case of errors in segmentation maps and pose estimations during preprocessing.
          Fortunately, those became quite accurate in recent years and this does not happen often.
          Second, representing identity via clothing-agnostic RGB is not ideal, since sometimes it may preserve only part of the identity,
          e.g., tatooes won't be visible in this representation, or specific muscle structure.
          Third, our train and test datasets have mostly clean uniform background so it is unknown how the method performs with more complex backgrounds.
          Fourth, we don't promise fit and for now focus only on visualization of the try on.
          Finally, this work focused on upper body clothing and we have not experimented with full body try-on, which is left for future work.

## BibTex

@InProceedings{Zhu_2023_CVPR_tryondiffusion, author={Zhu, Luyang and Yang, Dawei and Zhu, Tyler and Reda, Fitsum and Chan, William and Saharia, Chitwan and Norouzi, Mohammad and Kemelmacher-Shlizerman, Ira}, title={TryOnDiffusion: A Tale of Two UNets}, booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year={2023}, pages = {4606-4615} }

## Special Thanks

This work was done when all authors were at Google.
        Special Thank You to Yingwei Li, Hao Peng, Chris A. Lee, Alan Yang, Varsha Ramakrishnan, Srivatsan Varadharajan, David J. Fleet, and Daniel Watson for their insightful suggestions during the creation of this paper.
        We also are grateful for the kind support of the whole Google ARML Commerce organization.

--------------------