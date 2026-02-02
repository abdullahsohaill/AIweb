# Zeroscope AI
**URL:** https://huggingface.co/cerspense/zeroscope_v2_XL
**Page Title:** cerspense/zeroscope_v2_XL · Hugging Face
--------------------

example outputs (courtesy of dotsimulate )

## zeroscope_v2 XL

A watermark-free Modelscope-based video model capable of generating high quality video at 1024 x 576. This model was trained from the original weights with offset noise using 9,923 clips and 29,769 tagged frames at 24 frames, 1024x576 resolution. zeroscope_v2_XL is specifically designed for upscaling content made with zeroscope_v2_576w using vid2vid in the 1111 text2video extension by kabachuha . Leveraging this model as an upscaler allows for superior overall compositions at higher resolutions, permitting faster exploration in 576x320 (or 448x256) before transitioning to a high-resolution render.
[LINK: 1111 text2video](https://github.com/kabachuha/sd-webui-text2video)
[LINK: kabachuha](https://github.com/kabachuha)
zeroscope_v2_XL uses 15.3gb of vram when rendering 30 frames at 1024x576

### Using it with the 1111 text2video extension

- Download files in the zs2_XL folder.
- Replace the respective files in the 'stable-diffusion-webui\models\ModelScope\t2v' directory.

### Upscaling recommendations

For upscaling, it's recommended to use the 1111 extension. It works best at 1024x576 with a denoise strength between 0.66 and 0.85. Remember to use the same prompt that was used to generate the original clip.

### Usage in 🧨 Diffusers

Let's first install the libraries required:
Now, let's first generate a low resolution video using cerspense/zeroscope_v2_576w .
Next, we can upscale it using cerspense/zeroscope_v2_XL .
Here are some results:

### Known issues

Rendering at lower resolutions or fewer than 24 frames could lead to suboptimal outputs.
Thanks to camenduru , kabachuha , ExponentialML , dotsimulate , VANYA , polyware , tin2tin
[LINK: camenduru](https://github.com/camenduru)
[LINK: kabachuha](https://github.com/kabachuha)
[LINK: ExponentialML](https://github.com/ExponentialML)
[LINK: tin2tin](https://github.com/tin2tin)
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Spaces using cerspense/zeroscope_v2_XL 35


--------------------