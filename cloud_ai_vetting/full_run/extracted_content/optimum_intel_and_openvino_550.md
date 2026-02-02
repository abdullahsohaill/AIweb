# Optimum-intel and OpenVINO
**URL:** https://huggingface.co/docs/optimum/intel/openvino/export
**Page Title:** Export your model
--------------------

Optimum Intel documentation
Export your model

## Optimum Intel

[LINK: 529](https://github.com/huggingface/optimum-intel)
and get access to the augmented documentation experience
to get started

## Export your model

To export a model hosted on the Hub you can use our space . After conversion, a repository will be pushed under your namespace, this repository can be either public or private.
[LINK: model](https://huggingface.co/docs/optimum/main/en/intel/openvino/models)

## Using the CLI

To export your model to the OpenVINO IR format with the CLI :
[LINK: OpenVINO IR](https://docs.openvino.ai/2024/documentation/openvino-ir-format.html)
To export a private model or a model that requires access, you can either run huggingface-cli login to log in permanently, or set the environment variable HF_TOKEN to a token with access to the model. See the authentication documentation for more information.
[LINK: authentication documentation](https://huggingface.co/docs/huggingface_hub/quick-start#authentication)
The model argument can either be the model ID of a model hosted on the Hub or a path to a model hosted locally. For local models, you need to specify the task for which the model should be loaded before export, among the list of the supported tasks .
[LINK: supported tasks](https://huggingface.co/docs/optimum/main/en/exporters/task_manager)
Check out the help for more options:
You can also apply fp16, 8-bit or 4-bit weight-only quantization on the Linear, Convolutional and Embedding layers when exporting your model by setting --weight-format to respectively fp16 , int8 or int4 .
Export with INT8 weights compression:
Export with INT4 weights compression:
Export with INT4 weights compression and data-free AWQ algorithm:
Export with INT4 weights compression and data-aware AWQ and Scale Estimation algorithms:
For more information on the quantization parameters checkout the documentation
Models larger than 1 billion parameters are exported to the OpenVINO format with 8-bit weights by default. You can disable it with --weight-format fp32 .
Besides weight-only quantization, you can also apply full model quantization including activations by setting --quant-mode to preferred precision. This will quantize both weights and activations of Linear, Convolutional and some other layers to selected mode. Please see example below.
For some models we maintain a set of default quantization configs ( link ). To apply a default 4-bit weight-only quantization one should provide --weight-format int4 without any additional arguments. For int8 weight & activation quantization it should be --quant-mode int8 . For example:
[LINK: link](https://github.com/huggingface/optimum-intel/blob/main/optimum/intel/openvino/configuration.py)

### Decoder models

For models with a decoder, we enable the re-use of past keys and values by default. This allows to avoid recomputing the same intermediate activations at each generation step. To export the model without, you will need to remove the -with-past suffix when specifying the task.

### Diffusion models

When Stable Diffusion models are exported to the OpenVINO format, they are decomposed into different components that are later combined during inference:
- Text encoder(s)
- U-Net
- VAE encoder
- VAE decoder
To export your Stable Diffusion XL model to the OpenVINO IR format with the CLI you can do as follows:
You can also apply hybrid quantization during model export. For example:
For more information about hybrid quantization, take a look at this jupyter notebook .
[LINK: notebook](https://github.com/huggingface/optimum-intel/blob/main/notebooks/openvino/stable_diffusion_hybrid_quantization.ipynb)

## When loading your model

You can also load your PyTorch checkpoint and convert it to the OpenVINO format on-the-fly, by setting export=True when loading your model.
To easily save the resulting model, you can use the save_pretrained() method, which will save both the BIN and XML files describing the graph. It is useful to save the tokenizer to the same directory, to enable easy loading of the tokenizer for the model.

## After loading your model

Once the model is exported, you can now load your OpenVINO model by replacing the AutoModelForXxx class with the corresponding OVModelForXxx class.

## Troubleshooting

Some models do not work with the latest transformers release. You may see an error message with a maximum supported version. To export these models, install a transformers version that supports the model, for example pip install transformers==4.53.3 .
The supported transformers versions compatible with each optimum-intel release are listed on the Github releases page .
[LINK: Github releases page](https://github.com/huggingface/optimum-intel/releases/)
[LINK: ← Installation](/docs/optimum-intel/installation)
[LINK: Inference →](/docs/optimum-intel/openvino/inference)

--------------------