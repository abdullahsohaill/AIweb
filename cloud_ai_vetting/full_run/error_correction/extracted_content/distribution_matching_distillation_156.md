# Distribution Matching Distillation
**URL:** https://tianweiy.github.io/dmd
**Page Title:** One-step Diffusion with Distribution Matching Distillation
--------------------


## One-step Diffusion with Distribution Matching Distillation

[LINK: Tianwei Yin](https://tianweiy.github.io/)
[LINK: Richard Zhang](http://richzhang.github.io)
[LINK: https://tianweiy.github.io/dmd2/](https://tianweiy.github.io/dmd2/)
Diffusion models are known to approximate the score function of the distribution they are trained on. 
            In other words, an unrealistic synthetic image can be directed toward higher probability density region through the denoising process (see SDS ). 
            Our core idea is training two diffusion models to estimate not only the score function of the target real distribution, but also that of the fake distribution. 
            We construct a gradient update to our generator as the difference between the two scores, essentially nudging the generated images toward higher realism as well as lower fakeness (see VSD ). 
            Our method is similar to GANs in that a critic is jointly trained with the generator to minimize a divergence between the real and fake distributions, but differs in that our training does not play an adversarial game that may cause training instability, and our critic can fully leverage the weights of a pretrained diffusion model. 
            Combined with a simple regression loss to match the output of the multi-step diffusion model, our method outperforms all published few-step diffusion approaches, reaching 2.62 FID on ImageNet 64x64 and 11.49 FID on zero-shot COCO-30k, comparable to Stable Diffusion but orders of magnitude faster. 
            Utilizing FP16 inference, our model generates images at 20 FPS on modern hardware.
[LINK: SDS](https://dreamfusion3d.github.io)

## DMD Method Overview

We train one-step generator G θ to map random noise z into a realistic image. 
        To match the multi-step sampling outputs of the diffusion model, we pre-compute a collection of noise--image pairs, and occasionally load the noise from the collection and enforce LPIPS regression loss between our one-step generator and the diffusion output. 
        Furthermore, we provide distribution matching gradient ∇ θ D KL to the fake image to enhance realism. 
        We inject a random amount of noise to the fake image and pass it to two diffusion models, one pretrained on the real data and the other continually trained on the fake images with a diffusion loss , to obtain its denoised versions. The denoising scores (visualized as mean prediction in the plot) indicate directions to make the images more realistic or fake. The difference between the two represents the direction toward more realism and less fakeness and is backpropagated to the one-step generator.

## Comparison to Stable Diffusion

Medium shot side profile portrait photo of a warrior
          chief, sharp facial features, with tribal panther makeup
          in blue on red, looking away, serious but clear eyes,
          50mm portrait, photography, hard rim lighting photography
SD (50 steps) 2590ms
Ours (1 step) 90ms
a hyperrealistic photo of a fox astronaut; perfect face,
          artstation
SD (50 steps) 2590ms
Ours (1 step) 90ms
a DSLR photo of a golden retriever in heavy snow
SD (50 steps) 2590ms
Ours (1 step) 90ms
a Lightshow at the Dolomities
SD (50 steps) 2590ms
Ours (1 step) 90ms
the giant magical deer god of the forest, sniffing flowers on the forest floor. Fireflies evereywhere. A spring of water. Long moss hanging from the
          tree branches. Moonlight. Photorealism, cinematic shot, cinematic lighting, National Geographic, analagous colors, Award-winning photography
SD (50 steps) 2590ms
Ours (1 step) 90ms
3D render baby parrot, Chibi, adorable big eyes. In a garden with butterflies, greenery, lush, whimsical and soft, magical, octane render, fairy dust
SD (50 steps) 2590ms
Ours (1 step) 90ms

## Comparison to Other Diffusion Distillation Methods

close-up photo of a unicorn in a forest, in a style of movie still
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms
amazing photograph of a labrador retriever chasing a tennis ball under water, fisheye lens, close up portrait, crazy image
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms
wise old man with a white beard in the enchanted and magical forest
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms
macro photo of a miniature toy sloth drinking a soda, shot on a light pastel cyclorama
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms
Astronaut on a camel on mars
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms
a high-resolution photo of an orange Porsche under sunshine
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms
an underwater photo portrait of a beautiful fluffy white cat, hair floating. In a dynamic swimming pose.
          The sun rays filters through the water. High-angle shot. Shot on Fujifilm X
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms
3D animation cinematic style young caveman kid, in its natural environment
SD (50 steps) 2590ms
Instaflow (1 step) 90ms
LCMv1.5 (2 steps) 120ms
Ours (1 step) 90ms

## BibTeX


--------------------