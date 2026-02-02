# AvatarBooth
**URL:** https://zeng-yifei.github.io/avatarbooth_page
**Page Title:** AvatarBooth: High-Quality and Customizable 3D Human Avatar Generation
--------------------


## AvatarBooth: High-Quality and Customizable 3D Human Avatar Generation

[LINK: Yifei Zeng](https://github.com/zeng-yifei)
[LINK: Yuanxun Lu](https://github.com/YuanxunLu)
[LINK: Xinya Ji](https://github.com/jixinya)
[LINK: Yao Yao](https://yoyo000.github.io/)
[LINK: Code(To be released)](https://github.com/zeng-yifei/AvatarBooth)

## AvatarBooth is a text-to-3D model. It creates an animatable 3D model with your word description. 
          Also, it can generate customized model with 4~6 photos from your phone or a character design generated from diffusion model. 
          You can play with any magic words to change your final character result with fixed identity.

## Abstract

We introduce AvatarBooth, a novel method for generating high-quality 3D avatars using text prompts or specific images.
             Unlike previous approaches that can only synthesize avatars based on simple text descriptions, 
             our method enables the creation of personalized avatars from casually captured face or body images, 
             while still supporting text-based model generation and editing. 
             Our key contribution is the precise avatar generation control by using dual fine-tuned diffusion models separately 
             for the human face and body. This enables us to capture intricate details of facial appearance,
            clothing, and accessories, resulting in highly realistic avatar generations.
Furthermore, we introduce pose-consistent constraint to the optimization process to enhance the multi-view consistency 
            of synthesized head images from the diffusion model and thus eliminate interference from 
            uncontrolled human poses. In addition, we present a multi-resolution rendering strategy that 
            facilitates coarse-to-fine supervision of 3D avatar generation, thereby enhancing the performance 
            of the proposed system. The resulting avatar model can be further edited using additional text 
            descriptions and driven by motion sequences.
Experiments show that AvatarBooth outperforms previous text-to-3D methods in terms of
             rendering and geometric quality from either text prompts or specific images. 
             The code and model will be made available upon publication.

## Video

## Text-to-Avatar

Using AvatarBooth you can create high-quality avatar through a few words. 
            The model both have a satisfying appearance and a detailed mesh.

## Character Personalization

Another AvatarBooth application is that you can create your own model using your personal photos, including selfies and clothes photos. 
              You can add any accessories or effect to your model output using simply a word description.

## Application

### FBX animation

We can also animate the model by turning it into a FBX file.
            Feel free to play with the model.

## Related Links

There's a lot of excellent work that was introduced around the same time as ours.
AvatarCraft also uses NeuS for 3D representation.
[LINK: AvatarCraft](https://avatar-craft.github.io/)
Some works model avatars with Latent-NeRF, such as DreamAvatar
[LINK: DreamAvatar](https://yukangcao.github.io/DreamAvatar/)

## BibTeX


--------------------