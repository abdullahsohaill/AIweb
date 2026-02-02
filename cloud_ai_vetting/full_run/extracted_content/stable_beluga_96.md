# Stable Beluga
**URL:** https://huggingface.co/stabilityai/StableBeluga1-Delta
**Page Title:** stabilityai/StableBeluga1-Delta · Hugging Face
--------------------


## Stable Belgua 1

## Model Description

Stable Beluga 1 is a Llama65B model fine-tuned on an Orca style Dataset

## Usage

### Apply Delta Weights

Stable Beluga 1 cannot be used from the stabilityai/StableBeluga1-Delta weights alone. To obtain the correct model, one must add back the difference between LLaMA 65B and stabilityai/StableBeluga1-Delta weights. We provide the apply_delta.py script to automate the conversion, which you can run as:
Start chatting with Stable Beluga 1 using the following code snippet:
Stable Beluga 1 should be used with prompts formatted similarly to Alpaca as below:

## Model Details

- Developed by : Stability AI
- Model type : Stable Beluga 1 is an auto-regressive language model fine-tuned on LLaMA65B.
- Language(s) : English
- Library : HuggingFace Transformers
[LINK: HuggingFace Transformers](https://github.com/huggingface/transformers)
- License : Fine-tuned checkpoints ( StableBeluga1 ) is licensed under the Non-Commercial Creative Commons license ( CC BY-NC-4.0 )
- Contact : For questions and comments about the model, please email lm@stability.ai

### Training Dataset

Stable Beluga 1 is trained on our internal Orca-style dataset

### Training Procedure

Models are learned via supervised fine-tuning on the aforementioned datasets, trained in mixed-precision (BF16), and optimized with AdamW. We outline the following hyperparameters:

## Use and Limitations

### Ethical Considerations and Limitations

Beluga is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Beluga's potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Beluga, developers should perform safety testing and tuning tailored to their specific applications of the model.

## Citations

## Model tree for stabilityai/StableBeluga1-Delta

## Spaces using stabilityai/StableBeluga1-Delta 34

## Papers for stabilityai/StableBeluga1-Delta


--------------------