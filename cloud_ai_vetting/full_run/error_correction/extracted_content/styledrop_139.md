# StyleDrop
**URL:** https://styledrop.github.io
**Page Title:** StyleDrop: Text-to-Image Generation in Any Style
--------------------

(A style reference image is in white inset box)

## StyleDrop: Text-To-Image Generation in Any Style

Kihyuk Sohn, Nataniel Ruiz, Kimin Lee, Daniel Castro Chin, Irina Blok, Huiwen Chang, Jarred Barber, Lu Jiang, Glenn Entis, Yuanzhen Li, Yuan Hao, Irfan Essa, Michael Rubinstein, Dilip Krishnan
We present StyleDrop that enables the generation of images that faithfully follow a specific style,
        powered by Muse , a text-to-image generative
        vision transformer. StyleDrop is extremely versatile and captures nuances and details of a user-provided style, such as color
        schemes, shading, design patterns, and local and global effects. StyleDrop works by efficiently learning
        a new style by fine-tuning very few trainable parameters (less than 1% of total model parameters), and improving
        the quality via iterative training with either human or automated feedback. Better yet, StyleDrop is able
        to deliver impressive results even when the user supplies only a single image specifying the desired
        style. An extensive study shows that, for the task of style tuning text-to-image models, Styledrop on Muse convincingly outperforms other methods,
        including DreamBooth and Textual
          Inversion on Imagen or Stable Diffusion .
[LINK: Muse](https://muse-model.github.io/)
[LINK: Muse](https://muse-model.github.io/)
[LINK: DreamBooth](https://dreambooth.github.io/)
[LINK: Textual
          Inversion](https://textual-inversion.github.io/)

## Stylized Text-to-image Generation from a Single Image

StyleDrop generates high-quality images from text prompts in
      any style described by a single reference image. A style descriptor in natural language (e.g., " in melting golden 3d rendering style ") is appended to the content descriptors both at training and generation.

## Stylized Character Rendering

StyleDrop generates images of alphabets with a consistent style
      described by a single reference image. A style descriptor in natural language (e.g., " in abstract rainbow colored flowing smoke wave design ") is appended to the content descriptors both at training and generation.

## Collaborate with Your Style Assistant

StyleDrop is easy to train with your own brand assets and helps
      you to quickly prototype ideas in your own style. A style descriptor in natural language is appended to the content descriptors both at training and generation.

## My Subject in My Style

We combine StyleDrop and DreamBooth to generate an image of " my subject " in " my style ".
[LINK: DreamBooth](https://dreambooth.github.io/)
Subject (select one)
Style (select one)

## Comparison to Fine-tuning of Diffusion Models

StyleDrop on Muse, a discrete-token based vision transformer, convincingly outperforms in style-tuning over existing methods based on diffusion (Imagen, Stable Diffusion) models.

## Acknowledgment

First of all, we thank owners of images for sharing their valuable assets. We provide links to image assets used in our experiments. 
      We thank Varun Jampani, Jason Baldridge, Forrester Cole, José Lezama, Steven Hickson, Kfir Aberman for their valuable feedback on our manuscript.
[LINK: links](https://github.com/styledrop/styledrop.github.io/blob/main/images/assets/data.md)

--------------------