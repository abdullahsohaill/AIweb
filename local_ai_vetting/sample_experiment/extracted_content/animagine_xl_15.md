# Animagine XL
**URL:** https://civitai.com/models/260267/animagine-xl-v3
**Page Title:** Animagine XL V3.1 - v3.1 | Stable Diffusion XL Checkpoint | Civitai
--------------------


## Animagine XL V3.1

18.1k
250.7k
10.6k
Updated: Feb 15, 2025
[LINK: Download (6.46 GB)](/api/download/models/403131?type=Model&format=SafeTensor&size=full&fp=fp16)
Download (6.46 GB)
Verified: 2 years ago
SafeTensor
This checkpoint recommends a VAE , download and place it in the VAE folder.
[LINK: VAE](/api/download/models/403131?type=VAE)
Type
Stats
150,579
2,172,796
2.2m
Reviews
(11,598)
Published
Base Model
SDXL 1.0
Training
Usage Tips
Hash
Full Model fp16 (6.46 GB)
[LINK: Download](/api/download/models/403131?type=Model&format=SafeTensor&size=full&fp=fp16)
Verified: 2 years ago
SafeTensor
VAE (319.14 MB)
[LINK: Download](/api/download/models/403131?type=VAE&format=SafeTensor)
Verified: 2 years ago
SafeTensor
3.6k
22.3k
CagliostroLab
Joined Jan 10, 2024
License:
[LINK: CreativeML Open RAIL++-M](https://github.com/Stability-AI/generative-models/blob/main/model_licenses/LICENSE-SDXL1.0)
Animagine XL 3.1 is an update in the Animagine XL V3 series, enhancing the previous version, Animagine XL 3.0. This open-source, anime-themed text-to-image model has been improved for generating anime-style images with higher quality. It includes a broader range of characters from well-known anime series, an optimized dataset, and new aesthetic tags for better image creation. Built on Stable Diffusion XL, Animagine XL 3.1 aims to be a valuable resource for anime fans, artists, and content creators by producing accurate and detailed representations of anime characters.

## Model Details

- Developed by : Cagliostro Research Lab
Developed by : Cagliostro Research Lab
- In collaboration with : SeaArt.ai
In collaboration with : SeaArt.ai
- Model type : Diffusion-based text-to-image generative model
Model type : Diffusion-based text-to-image generative model
- Model Description : Animagine XL 3.1 generates high-quality anime images from textual prompts. It boasts enhanced hand anatomy, improved concept understanding, and advanced prompt interpretation.
Model Description : Animagine XL 3.1 generates high-quality anime images from textual prompts. It boasts enhanced hand anatomy, improved concept understanding, and advanced prompt interpretation.
- License : Fair AI Public License 1.0-SD
License : Fair AI Public License 1.0-SD
- Fine-tuned from : Animagine XL 3.0
Fine-tuned from : Animagine XL 3.0

## Usage Guidelines

### Tag Ordering

For optimal results, it's recommended to follow the structured prompt template because we train the model like this:

## Special Tags

Animagine XL 3.1 utilizes special tags to steer the result toward quality, rating, creation date and aesthetic. While the model can generate images without these tags, using them can help achieve better results.

### Quality Modifiers

Quality tags now consider both scores and post ratings to ensure a balanced quality distribution. We've refined labels for greater clarity, such as changing 'high quality' to 'great quality'.

### Rating Modifiers

We've also streamlined our rating tags for simplicity and clarity, aiming to establish global rules that can be applied across different models. For example, the tag 'rating: general' is now simply 'general', and 'rating: sensitive' has been condensed to 'sensitive'.

### Year Modifier

We've also redefined the year range to steer results towards specific modern or vintage anime art styles more accurately. This update simplifies the range, focusing on relevance to current and past eras.

### Aesthetic Tags

We've enhanced our tagging system with aesthetic tags to refine content categorization based on visual appeal. These tags are derived from evaluations made by a specialized ViT (Vision Transformer) image classification model, specifically trained on anime data. For this purpose, we utilized the model shadowlilac/aesthetic-shadow-v2 , which assesses the aesthetic value of content before it undergoes training. This ensures that each piece of content is not only relevant and accurate but also visually appealing.

## Recommended settings

To guide the model towards generating high-aesthetic images, use negative prompts like:
For higher quality outcomes, prepend prompts with:
it’s recommended to use a lower classifier-free guidance (CFG Scale) of around 5-7, sampling steps below 30, and to use Euler Ancestral (Euler a) as a sampler.

### Multi Aspect Resolution

This model supports generating images at the following dimensions:

### Acknowledgements

The development and release of Animagine XL 3.1 would not have been possible without the invaluable contributions and support from the following individuals and organizations:
- SeaArt.ai : Our collaboration partner and sponsor.
SeaArt.ai : Our collaboration partner and sponsor.
- Shadow Lilac : For providing the aesthetic classification model, aesthetic-shadow-v2 .
Shadow Lilac : For providing the aesthetic classification model, aesthetic-shadow-v2 .
- Derrian Distro : For their custom learning rate scheduler, adapted from LoRA Easy Training Scripts .
Derrian Distro : For their custom learning rate scheduler, adapted from LoRA Easy Training Scripts .
[LINK: Derrian Distro](https://github.com/derrian-distro)
[LINK: LoRA Easy Training Scripts](https://github.com/derrian-distro/LoRA_Easy_Training_Scripts/blob/main/custom_scheduler/LoraEasyCustomOptimizer/CustomOptimizers.py)
- Kohya SS : For their comprehensive training scripts.
Kohya SS : For their comprehensive training scripts.
[LINK: Kohya SS](https://github.com/kohya-ss)
- Cagliostrolab Collaborators : For their dedication to model training, project management, and data curation.
Cagliostrolab Collaborators : For their dedication to model training, project management, and data curation.
- Early Testers : For their valuable feedback and quality assurance efforts.
Early Testers : For their valuable feedback and quality assurance efforts.
- NovelAI : For their innovative approach to aesthetic tagging, which served as an inspiration for our implementation.
NovelAI : For their innovative approach to aesthetic tagging, which served as an inspiration for our implementation.
Thank you all for your support and expertise in pushing the boundaries of anime-style image generation.

## Limitations

While Animagine XL 3.1 represents a significant advancement in anime-style image generation, it is important to acknowledge its limitations:
- Anime-Focused : This model is specifically designed for generating anime-style images and is not suitable for creating realistic photos.
Anime-Focused : This model is specifically designed for generating anime-style images and is not suitable for creating realistic photos.
- Prompt Complexity : This model may not be suitable for users who expect high-quality results from short or simple prompts. The training focus was on concept understanding rather than aesthetic refinement, which may require more detailed and specific prompts to achieve the desired output.
Prompt Complexity : This model may not be suitable for users who expect high-quality results from short or simple prompts. The training focus was on concept understanding rather than aesthetic refinement, which may require more detailed and specific prompts to achieve the desired output.
- Prompt Format : Animagine XL 3.1 is optimized for Danbooru-style tags rather than natural language prompts. For best results, users are encouraged to format their prompts using the appropriate tags and syntax.
Prompt Format : Animagine XL 3.1 is optimized for Danbooru-style tags rather than natural language prompts. For best results, users are encouraged to format their prompts using the appropriate tags and syntax.
- Anatomy and Hand Rendering : Despite the improvements made in anatomy and hand rendering, there may still be instances where the model produces suboptimal results in these areas.
Anatomy and Hand Rendering : Despite the improvements made in anatomy and hand rendering, there may still be instances where the model produces suboptimal results in these areas.
- Dataset Size : The dataset used for training Animagine XL 3.1 consists of approximately 870,000 images. When combined with the previous iteration's dataset (1.2 million), the total training data amounts to around 2.1 million images. While substantial, this dataset size may still be considered limited in scope for an "ultimate" anime model.
Dataset Size : The dataset used for training Animagine XL 3.1 consists of approximately 870,000 images. When combined with the previous iteration's dataset (1.2 million), the total training data amounts to around 2.1 million images. While substantial, this dataset size may still be considered limited in scope for an "ultimate" anime model.
- NSFW Content : Animagine XL 3.1 has been designed to generate more balanced NSFW content. However, it is important to note that the model may still produce NSFW results, even if not explicitly prompted.
NSFW Content : Animagine XL 3.1 has been designed to generate more balanced NSFW content. However, it is important to note that the model may still produce NSFW results, even if not explicitly prompted.
By acknowledging these limitations, we aim to provide transparency and set realistic expectations for users of Animagine XL 3.1. Despite these constraints, we believe that the model represents a significant step forward in anime-style image generation and offers a powerful tool for artists, designers, and enthusiasts alike.

## License

Based on Animagine XL 3.0, Animagine XL 3.1 falls under Fair AI Public License 1.0-SD license, which is compatible with Stable Diffusion models’ license. Key points:
- Modification Sharing: If you modify Animagine XL 3.1, you must share both your changes and the original license.
Modification Sharing: If you modify Animagine XL 3.1, you must share both your changes and the original license.
- Source Code Accessibility: If your modified version is network-accessible, provide a way (like a download link) for others to get the source code. This applies to derived models too.
Source Code Accessibility: If your modified version is network-accessible, provide a way (like a download link) for others to get the source code. This applies to derived models too.
- Distribution Terms: Any distribution must be under this license or another with similar rules.
Distribution Terms: Any distribution must be under this license or another with similar rules.
- Compliance: Non-compliance must be fixed within 30 days to avoid license termination, emphasizing transparency and adherence to open-source values.
Compliance: Non-compliance must be fixed within 30 days to avoid license termination, emphasizing transparency and adherence to open-source values.
The choice of this license aims to keep Animagine XL 3.1 open and modifiable, aligning with open source community spirit. It protects contributors and users, encouraging a collaborative, ethical open-source community. This ensures the model not only benefits from communal input but also respects open-source development freedoms. Finally Cagliostro Lab Server open to public https://discord.gg/cqh9tZgbGc
Feel free to join our discord server. If you want to donate or buy us a coffee you can donate Here
Thank you very much ^_^

## Discussion

CheeseGake
What happened? Why can't i use this lora anymore?
Yusup321
why can't I use this model in generator?
liyvpeng
Have anyone noticed that all characters are in back light/side light? It is so hard to create girl just in front light......
viktorrios
Which VAE is recommended for this model? I have SDXL and Grapefruit VAEs.
Sherry745
Please fix this model issue, I can't make images!
Matriarch_Red
Why can't we use this model to make images??
Selirus
Hello. Why is this model unavailable in generator? (btw not only this one) There weren't problems previously though
haokaibo
I tried this with DiffusionBee. It always generate 6 fingers. How to avoid it?

--------------------