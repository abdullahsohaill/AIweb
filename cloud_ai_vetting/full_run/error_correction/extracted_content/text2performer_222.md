# Text2Performer
**URL:** https://yumingj.github.io/projects/Text2Performer.html
**Page Title:** Text2Performer
--------------------


## Text2Performer: Text-Driven Human Video Generation

[LINK: Yuming Jiang](https://yumingj.github.io/)
[LINK: Shuai Yang](https://williamyang1991.github.io/)
[LINK: Wayne Wu](https://wywu.github.io/)
[LINK: Ziwei Liu](https://liuziwei7.github.io/)
[LINK: Code](https://github.com/yumingj/Text2Performer)

## Text2Performer studies text-guided human video generation . It takes the text descriptions as the only input.

## Abstract

Text-driven content creation has evolved to be a transformative technique that
      revolutionizes creativity. Here we study the task of text-driven human video generation, where a video sequence is
      synthesized from texts describing the appearance and motions of a target performer. Compared to general
      text-driven video generation, human-centric
      video generation requires maintaining the appearance of synthesized human while performing complex motions. In
      this work, we present Text2Performer to generate vivid human videos with articulated motions from texts.
      Text2Performer has two novel designs: 1) decomposed human representation and 2) diffusion-based motion sampler.
      First, we decompose the VQVAE latent space into human appearance and pose representation in an unsupervised manner
      by utilizing the nature of human videos. In this way, the appearance is well maintained along the generated
      frames. Then, we propose continuous VQ-diffuser to sample a sequence of pose embeddings. Unlike existing VQ-based
      methods that operate in the discrete space, continuous VQ-diffuser directly outputs the continuous pose embeddings
      for better motion modeling. Finally, motion-aware masking strategy is designed to mask the pose embeddings
      spatial-temporally to enhance the temporal coherence. Moreover, to facilitate the task of text-driven human video
      generation, we contribute a Fashion-Text2Video dataset with manually annotated action labels and text
      descriptions. Extensive experiments demonstrate that Text2Performer generates highquality human videos (up to 512
      × 256 resolution) with diverse appearances and flexible motions.

## Methods

Overview of Text2Performer with (a) Sampling from the Decomposed VQ-Space and (b)
      Motion Sampling with
      Continuous VQ-Diffuser.

## Results

## Results

## Results

## Comparison with State-of-the-art

## Comparison with State-of-the-art

## Comparison with State-of-the-art

## Comparison with State-of-the-art

## BibTeX


--------------------