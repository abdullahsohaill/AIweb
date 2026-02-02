# stable-fast-3d
**URL:** https://huggingface.co/stabilityai/stable-fast-3d
**Page Title:** stabilityai/stable-fast-3d · Hugging Face
--------------------


## You need to agree to share your contact information to access this model

This repository is publicly accessible, but you have to accept the conditions to access its files and content .
By clicking "Agree", you agree to the License Agreement and acknowledge Stability AI's Privacy Policy .
Log in or Sign Up to review the conditions and access this model content.

## Stable Fast 3D

Stable Fast 3D (SF3D) is a large reconstruction model which takes in a single image of an object and generates a textured UV-unwrapped 3D mesh asset.
Please note: For individuals or organizations generating annual revenue of US $1,000,000 (or local currency equivalent) or more, regardless of the source of that revenue, you must obtain an enterprise commercial license directly from Stability AI before commercially using SF3D or any derivative work of SF3D or its outputs, such as "fine tune" models. You may submit a request for an Enterprise License at https://stability.ai/enterprise . Please refer to Stability AI's Community License, available at https://stability.ai/license , for more information.

### Model Description

- Developed by : Stability AI
- Model type : Transformer image-to-3D model
- Model details : This model is trained to create a 3D model from a single image in under one second. The asset is UV-unwrapped and textured and has a relatively low polygon count. We also perform a delighting step, enabling easier asset usage in downstream applications such as game engines or rendering work. The model also predicts per-object material parameters (roughness, metallic), enhancing reflective behaviors during rendering. The model expects an input size of 512x512 pixels.
Please check our tech report and video summary for details.

### License

- Community License: Free for research, non-commercial, and commercial use by organizations and individuals generating annual revenue of US $1,000,000 (or local currency equivalent) or less, regardless of the source of that revenue. If your annual revenue exceeds US $1M, any commercial use of this model or derivative works thereof requires obtaining an Enterprise License directly from Stability AI. You may submit a request for an Enterprise License at https://stability.ai/enterprise . Please refer to Stability AI's Community License, available at https://stability.ai/license , for more information.

### Model Sources

- Repository : https://github.com/Stability-AI/stable-fast-3d
[LINK: https://github.com/Stability-AI/stable-fast-3d](https://github.com/Stability-AI/stable-fast-3d)
- Tech report : https://arxiv.org/pdf/2408.00653
- Video summary : https://youtu.be/uT96UCBSBko
- Project page : https://stable-fast-3d.github.io
[LINK: https://stable-fast-3d.github.io](https://stable-fast-3d.github.io)
- arXiv page : https://arxiv.org/abs/2408.00653

### Training Dataset

We use renders from the Objaverse dataset, available under the Open Data Commons Attribution License. We utilize our enhanced rendering method, which more closely replicates the distribution of images found in the real world, significantly improving our model's ability to generalize. We filter objects based on the review of licenses and curate a subset suitable for our training needs.

## Usage

For usage instructions, please refer to our GitHub repository
[LINK: GitHub repository](https://github.com/Stability-AI/stable-fast-3d)

### Intended Uses

Intended uses include the following:
- Generation of artworks and use in design and other artistic processes.
- Applications in educational or creative tools.
- Research on reconstruction models, including understanding the limitations of these models.
All uses of the model should be in accordance with our Acceptable Use Policy .

### Out-of-Scope Uses

The model was not trained to be factual or true representations of people or events. As such, using the model to generate such content is out-of-scope of the abilities of this model.

## Safety

As part of our safety-by-design and responsible AI deployment approach, we implement safety measures throughout the development of our models, from the time we begin pre-training a model to the ongoing development, fine-tuning, and deployment of each model. We have implemented a number of safety mitigations that are intended to reduce the risk of severe harms. However, we recommend that developers conduct their own testing and apply additional mitigations based on their specific use cases. For more about our approach to Safety, please visit our Safety page .

### Contact

Please report any issues with the model or contact us:
- Safety issues: safety@stability.ai
- Security issues: security@stability.ai
- Privacy issues: privacy@stability.ai
- License and general: https://stability.ai/license
- Enterprise license: https://stability.ai/enterprise
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Dataset used to train stabilityai/stable-fast-3d

## Spaces using stabilityai/stable-fast-3d 36

## Collection including stabilityai/stable-fast-3d

## Paper for stabilityai/stable-fast-3d


--------------------