# VideoAuteur
**URL:** https://videoauteur.github.io
**Page Title:** Towards Long Narrative Video Generation
--------------------


## VideoAuteur:

## Towards Long Narrative Video Generation

[LINK: Junfei Xiao](https://lambert-x.github.io)
[LINK: Feng Cheng](https://klauscc.github.io/)
[LINK: Project Page](https://videoauteur.github.io)
Disclaimer: This is a research prototype and not an officially supported ByteDance product.
Special Thanks: We give special thanks to Kelly Zhang, Ziyan Zhang, Yang Zhao, and Jiaming Han for their support and discussion.

## Abstract

Recent video generation models have shown promising results in producing high-quality video clips lasting several seconds. 
                However, these models face challenges in generating long sequences that convey clear and informative events, limiting 
                their ability to support coherent narrations. In this paper, we present a large-scale cooking video dataset designed 
                to advance long-form narrative generation in the cooking domain. We validate the quality of our proposed dataset in 
                terms of visual fidelity and textual caption accuracy using state-of-the-art Vision-Language Models (VLMs) and video 
                generation models, respectively. We further introduce a Long Narrative Video Director to enhance both visual and semantic 
                coherence in generated videos and emphasize the role of aligning visual embeddings to achieve improved overall video 
                quality. Our method demonstrates substantial improvements in generating visually detailed and semantically aligned 
                keyframes, supported by finetuning techniques that integrate text and image embeddings within the video generation process.

## Long Narrative Video Generation Demos

Tesla Car Product Video AI-generated advertisement showcasing our model's automotive narrative capabilities. Process from storyline to video clips is fully AI-powered. Enhanced with CapCut for dynamic pacing. Only audio and logo added manually, with editing taking just 30 minutes.

## Demo Overview

Demos below showcase our long narrative video generation capabilities through three main sections:

### 1. Interleaved Auto-regressive Director Generation

Showcasing our core method that uses interleaved visual embeddings to generate coherent cooking videos with strong temporal consistency.

### 2. Language-Centric Director Generation

Demonstrating an alternative approach using FLUX.1-Schnell for high-quality frame generation guided by textual descriptions.

### 3. Pipeline Extension

Exploring broader applications beyond cooking, including a Tesla car advertisement, a Batman vs. Ironman movie trailer, and a Netflix-style animal documentary trailer.

## Interleaved Auto-regressive Director Generation

Our Long Narrative Video Director uses interleaved visual embeddings as conditions for Video Generation. 
        This approach emphasizes visual alignment throughout the generation process, resulting in more realistic 
        and consistent cooking demonstrations. The generated content maintains better temporal coherence and visual 
        consistency across steps.

## How to cook Fried Chicken?

Action: Combine chicken puree, eggs, and milk in a bowl.
Caption: A close-up shot of a bowl of mixed chicken puree being combined with wet ingredients like eggs and milk. in a bright kitchen, the focus is on the transformation of the mixture as it prepares to be cooked.
Action: Add spices and seasonings to the dry mixture.
Caption: A close-up shot of a hand is seen preparing a dry mixture in a bowl, adding various spices and seasonings. in a bright kitchen, the focus is on the methodical process of blending ingredients.
Action: Coat sliced chicken with the seasoned flour.
Caption: A close-up shot of a hand is seen preparing a wet mixture in a bowl, combining sliced chicken with the seasoned flour. in a bright kitchen, the focus is on combining the vital components for cooking.
Action: Place chicken piece into hot oil.
Caption: A close-up shot of a single chicken piece being placed into a frying pan with hot oil. The focus is on the action of lifting and dipping the chicken into the oil, showcasing the frying process.
Action: Fry chicken pieces until golden brown.
Caption: A close-up shot of multiple chicken pieces frying in a pan of hot oil. The focus is on the frying process, with individual chicken pieces sizzling and browning as they cook.
Action: Drizzle fried chicken with sauce and sprinkle herbs.
Caption: A close-up shot of a plate of fried chicken pieces, ready to be drizzled with sauce and sprinkled with herbs. The focus is on the golden brown, crispy chicken contrasting with the vibrant sauce and herbs.

## Language-Centric Director Generation

This approach leverages generated captions to create keyframes using the SOTA Text-to-Image model 
        (FLUX.1-Schnell). While this method produces more aesthetically pleasing individual frames, it may 
        show less visual consistency between steps. The result emphasizes artistic quality while maintaining 
        strong alignment with textual descriptions.

## How to cook Blt Sandwich?

Action: Place bread slice into toaster.
Caption: A close-up shot of a cook's hand placing a slice of fresh bread into a toaster. The scene focuses on the initial stage of toasting, capturing the bread's texture and the beginning sizzle as it contrasts with the dark background.
Action: Add layer of lettuce on toasted bread.
Caption: A close-up shot of a layer of lettuce being placed on a toasted bread slice.
Action: Spread mayonnaise on lettuce-topped bread.
Caption: A close-up shot of a cook spreading mayonnaise on the lettuce-topped bread.
Action: Place bacon slice on lettuce.
Caption: A close-up shot of a cook placing a slice of bacon on the lettuce sandwich.
Action: Add tomato slices on bacon-lettuce sandwich.
Caption: A close-up shot of the cook placing tomato slices on the bacon- lettuce sandwiches.
Action: Drizzle barbecue sauce over sandwich.
Caption: A medium shot of the cook drizzling barbecue sauce over the toasted sandwich in the same cozy kitchen. The warm lighting creates a homely atmosphere.
Action: Drizzle dressing on top of sandwich.
Caption: A medium shot of the cook adding the final touches to the sandwich by drizzling dressing on top of the sandwich in the same cozy kitchen environment.
Action: Present completed sandwich.
Caption: A medium shot of the cook presenting the completed sandwich, now drizzled with dressing, in the same warm kitchen.

## Pipeline Extension to Broader Scenarios

In this section, we also provide two more demos to show the potential of our pipeline to broader scenarios: Tesla Car Product Video and Animal Documentary Trailer .
Tesla Car Product Video AI-generated advertisement demonstrates our model's create original automotive narratives. The entire process—from storyline development to keyframe generation and video clips—is AI-powered. The final video is enhanced using CapCut for dynamic pacing, with some sequences sped up or shortened. Only the audio and final logo clip are manually added, with basic editing taking approximately 30 minutes.

## CookGen Dataset

CookGen contains long narrative videos annotated with actions and captions. Each source video is cut into clips 
            and matched with labeled "actions". We use refined pseudo labels from ASR for Howto100M videos and manual 
            annotations for Youcook2 videos. High-quality captions are generated using state-of-the-art VLMs (GPT-4 and a 
            finetuned video captioner) for all video clips.
Dataset annotation and curation pipeline: We collect cooking videos from Howto100M and Youcook2, 
                segment them into clips, and annotate them with actions and captions using a combination of ASR, 
                manual annotation, and SoTA VLMs.
Video Data Statistics: Our dataset features videos ranging from 30-150 seconds in length, 
                  with individual clips spanning 5-30 seconds. Each video is divided into 4-12 clips, providing a balanced 
                  distribution that ensures comprehensive coverage of cooking procedures.
Text Annotation Statistics: The dataset includes detailed text annotations with actions 
                  containing 10-25 words and comprehensive captions spanning 40-70 words. When tokenized, actions typically 
                  contain 20-60 tokens, while captions can extend up to 120 tokens, providing rich descriptive content.
These statistics demonstrate the high quality and suitability of our dataset for long narrative video generation. 
                The balanced distribution of video lengths and clip counts ensures proper narrative structure, while the detailed 
                text annotations provide rich contextual information for each segment. This comprehensive annotation approach 
                enables well-aligned and contextually rich representations of the video content.

## VideoAuteur Pipeline

Given the text input, the task of long narrative video generation aims at generating a coherent long video that aligns with the progression of the text input sequentially. To achieve this, we propose VideoAuteur , a pipeline that involves two main components: a long narrative video director and visual-conditioned video generation.

### Long Narrative Video Director

We use an interleaved auto-regressive model to generate sequential outputs including captions, actions, and visual states. The model employs an interleaved generation approach, where each step's output informs subsequent generations. Key architectural innovations include optimized visual latent space representation, specialized regression loss functions for visual embedding accuracy, and refined regression task formulation for enhanced temporal coherence.

### Visual-Conditioned Video Generation

The Visual-Conditioned Video Generation framework integrates action sequences (aₜ), captions (cₜ), and visual states (zₜ) from the narrative director to synthesize coherent long-form videos. The architecture advances beyond traditional Image-to-Video approaches by implementing continuous visual latent conditioning throughout the sequence generation process. The model incorporates robust error handling mechanisms to address potential regression artifacts in visual embeddings, ensuring stable and high-quality video output despite input variations.

## BibTeX


--------------------