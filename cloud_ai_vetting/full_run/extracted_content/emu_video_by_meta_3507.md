# Emu Video by Meta
**URL:** https://emu-video.metademolab.com
**Page Title:** Emu Video | Meta
--------------------

- Emu Video
- Demo
- Blog
- Paper
- Emu Edit
- Emu Video
- Demo
- Blog
- Paper
- Emu Edit

## Emu Video: Factorizing Text-to-Video Generation by Explicit Image Conditioning

### State-of-the-art text-to-video generation

## Factorizing Text-to-Video Generation by Explicit Image Conditioning

Emu Video is a simple method for text to video generation based on diffusion models, factorizing the generation into two steps:
- First generating an image conditioned on a text prompt
- Then generating a video conditioned on the prompt and the generated image
Factorized generation allows us to train high quality video generation models efficiently. Unlike prior work that requires a deep cascade of models, our approach only requires two diffusion models to generate 512px, 4 second long videos at 16fps.

## State of the Art results

We compared Emu Video against state of the art text-to-video generation models on a varity of prompts, by asking human raters to select the most convincing videos, based on quality and faithfulness to the prompt.
Our 512 pixels, 16 frames per second, 4 second long videos win on both metrics against prior works: Make-a-Video ( MAV ), Imagen-Video ( Imagen ), Align Your Latents ( AYL ), Reuse & Diffuse ( R&D ), Cog Video ( Cog ), Gen2 ( Gen2 ) and Pika Labs ( Pika ).

## Authors

(^): equal first authors (*): equal technical contribution

## Acknowledgments

Baixue Zheng, Baishan Guo, Jeremy Teboul, Milan Zhou, Shenghao Lin, Kunal Pradhan, Jort Gemmeke, Jacob Xu, Dingkang Wang, Samyak Datta, Guan Pang, Symon Perriman, Vivek Pai, Shubho Sengupta for their help with the data and infra. We would like to thank Uriel Singer, Adam Polyak, Shelly Sheynin, Yaniv Taigman, Licheng Yu, Luxin Zhang, Yinan Zhao, David Yan, Yaqiao Luo, Xiaoliang Dai, Zijian He, Peizhao Zhang, Peter Vajda, Roshan Sumbaly, Armen Aghajanyan, Michael Rabbat, and Michal Drozdzal for helpful discussions. We are also grateful to the help from Lauren Cohen, Mo Metanat, Lydia Baillergeau, Amanda Felix, Ana Paula Kirschner Mofarrej, Kelly Freed, Somya Jain. We thank Ahmad Al-Dahle and Manohar Paluri for their support.

--------------------