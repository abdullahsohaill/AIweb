# Snowflake Arctic Instruct
**URL:** https://huggingface.co/Snowflake/snowflake-arctic-instruct
**Page Title:** Snowflake/snowflake-arctic-instruct · Hugging Face
--------------------


## Model Details

Arctic is a dense-MoE Hybrid transformer architecture pre-trained from scratch by the Snowflake AI 
Research Team. We are releasing model checkpoints for both the base and instruct-tuned versions of 
Arctic under an Apache-2.0 license. This means you can use them freely in your own research, 
prototypes, and products. Please see our blog Snowflake Arctic: The Best LLM for Enterprise AI — Efficiently Intelligent, Truly Open for more information on Arctic and links to other relevant resources such as our series of cookbooks 
covering topics around training your own custom MoE models, how to produce high-quality training data, 
and much more.
- Arctic-Base
- Arctic-Instruct
For the latest details about Snowflake Arctic including tutorials, etc., please refer to our GitHub repo:
- https://github.com/Snowflake-Labs/snowflake-arctic
[LINK: https://github.com/Snowflake-Labs/snowflake-arctic](https://github.com/Snowflake-Labs/snowflake-arctic)
Try a live demo with our Streamlit app .
Model developers Snowflake AI Research Team
License Apache-2.0
Input Models input text only.
Output Models generate text and code only.
Model Release Date April, 24th 2024.

## Model Architecture

Arctic combines a 10B dense transformer model with a residual 128x3.66B MoE MLP resulting in 480B 
total and 17B active parameters chosen using a top-2 gating. For more details about Arctic's model
Architecture, training process, data, etc. see our series of cookbooks .

## Usage

Arctic is currently supported with transformers by leveraging the custom code feature , 
to use this you simply need to add trust_remote_code=True to your AutoTokenizer and AutoModelForCausalLM calls.
However, we recommend that you use a transformers version at or above 4.39:
[LINK: custom code feature](https://huggingface.co/docs/transformers/en/custom_models#using-a-model-with-custom-code)
Arctic leverages several features from DeepSpeed , you will need to 
install the DeepSpeed 0.14.2 or higher to get all of these required features:
[LINK: DeepSpeed](https://github.com/microsoft/DeepSpeed)

### Inference examples

Due to the model size we recommend using a single 8xH100 instance from your
favorite cloud provider such as: AWS p5.48xlarge , 
Azure ND96isr_H100_v5 , etc.
In this example we are using FP8 quantization provided by DeepSpeed in the backend, we can also use FP6 
quantization by specifying q_bits=6 in the QuantizationConfig config. The "150GiB" setting 
for max_memory is required until we can get DeepSpeed's FP quantization supported natively as a HFQuantizer which we 
are actively working on.
[LINK: HFQuantizer](https://huggingface.co/docs/transformers/main/en/hf_quantizer#build-a-new-hfquantizer-class)
The Arctic GitHub page has additional code snippets and examples around running inference:
- Example with pure-HF: https://github.com/Snowflake-Labs/snowflake-arctic/blob/main/inference
[LINK: https://github.com/Snowflake-Labs/snowflake-arctic/blob/main/inference](https://github.com/Snowflake-Labs/snowflake-arctic/blob/main/inference)
- Tutorial using vLLM: https://github.com/Snowflake-Labs/snowflake-arctic/tree/main/inference/vllm
[LINK: https://github.com/Snowflake-Labs/snowflake-arctic/tree/main/inference/vllm](https://github.com/Snowflake-Labs/snowflake-arctic/tree/main/inference/vllm)

## Model tree for Snowflake/snowflake-arctic-instruct

## Spaces using Snowflake/snowflake-arctic-instruct 14

## Collection including Snowflake/snowflake-arctic-instruct


--------------------