# CLIPSeg
**URL:** https://huggingface.co/docs/transformers/model_doc/clipseg
**Page Title:** CLIPSeg
--------------------

Transformers documentation
CLIPSeg

## Transformers

[LINK: 155,734](https://github.com/huggingface/transformers)
and get access to the augmented documentation experience
to get started
This model was released on 2021-12-18 and added to Hugging Face Transformers on 2022-11-08.

## CLIPSeg

## Overview

The CLIPSeg model was proposed in Image Segmentation Using Text and Image Prompts by Timo Lüddecke
and Alexander Ecker. CLIPSeg adds a minimal decoder on top of a frozen CLIP model for zero-shot and one-shot image segmentation.
The abstract from the paper is the following:
Image segmentation is usually addressed by training a
model for a fixed set of object classes. Incorporating additional classes or more complex queries later is expensive
as it requires re-training the model on a dataset that encompasses these expressions. Here we propose a system
that can generate image segmentations based on arbitrary
prompts at test time. A prompt can be either a text or an
image. This approach enables us to create a unified model
(trained once) for three common segmentation tasks, which
come with distinct challenges: referring expression segmentation, zero-shot segmentation and one-shot segmentation.
We build upon the CLIP model as a backbone which we extend with a transformer-based decoder that enables dense
prediction. After training on an extended version of the
PhraseCut dataset, our system generates a binary segmentation map for an image based on a free-text prompt or on
an additional image expressing the query. We analyze different variants of the latter image-based prompts in detail.
This novel hybrid input allows for dynamic adaptation not
only to the three segmentation tasks mentioned above, but
to any binary segmentation task where a text or image query
can be formulated. Finally, we find our system to adapt well
to generalized queries involving affordances or properties
This model was contributed by nielsr .
The original code can be found here .
[LINK: here](https://github.com/timojl/clipseg)

## Usage tips

- CLIPSegForImageSegmentation adds a decoder on top of CLIPSegModel . The latter is identical to CLIPModel .
[LINK: CLIPSegForImageSegmentation](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegForImageSegmentation)
[LINK: CLIPSegModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegModel)
[LINK: CLIPModel](/docs/transformers/v5.0.0rc2/en/model_doc/clip#transformers.CLIPModel)
- CLIPSegForImageSegmentation can generate image segmentations based on arbitrary prompts at test time. A prompt can be either a text
(provided to the model as input_ids ) or an image (provided to the model as conditional_pixel_values ). One can also provide custom
conditional embeddings (provided to the model as conditional_embeddings ).
[LINK: CLIPSegForImageSegmentation](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegForImageSegmentation)

## Resources

A list of official Hugging Face and community (indicated by 🌎) resources to help you get started with CLIPSeg. If you’re interested in submitting a resource to be included here, please feel free to open a Pull Request and we’ll review it! The resource should ideally demonstrate something new instead of duplicating an existing resource.
- A notebook that illustrates zero-shot image segmentation with CLIPSeg .
[LINK: zero-shot image segmentation with CLIPSeg](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/CLIPSeg/Zero_shot_image_segmentation_with_CLIPSeg.ipynb)

## CLIPSegConfig

### class transformers. CLIPSegConfig

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/configuration_clipseg.py#L207)
( text_config = None vision_config = None projection_dim = 512 logit_scale_init_value = 2.6592 extract_layers = [3, 6, 9] reduce_dim = 64 decoder_num_attention_heads = 4 decoder_attention_dropout = 0.0 decoder_hidden_act = 'quick_gelu' decoder_intermediate_size = 2048 conditional_layer = 0 use_complex_transposed_convolution = False **kwargs )
Parameters
- text_config ( dict , optional ) —
Dictionary of configuration options used to initialize CLIPSegTextConfig .
[LINK: CLIPSegTextConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegTextConfig)
- vision_config ( dict , optional ) —
Dictionary of configuration options used to initialize CLIPSegVisionConfig .
[LINK: CLIPSegVisionConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegVisionConfig)
- projection_dim ( int , optional , defaults to 512) —
Dimensionality of text and vision projection layers.
- logit_scale_init_value ( float , optional , defaults to 2.6592) —
The initial value of the logit_scale parameter. Default is used as per the original CLIPSeg implementation.
- extract_layers ( list[int] , optional , defaults to [3, 6, 9] ) —
Layers to extract when forwarding the query image through the frozen visual backbone of CLIP.
- reduce_dim ( int , optional , defaults to 64) —
Dimensionality to reduce the CLIP vision embedding.
- decoder_num_attention_heads ( int , optional , defaults to 4) —
Number of attention heads in the decoder of CLIPSeg.
- decoder_attention_dropout ( float , optional , defaults to 0.0) —
The dropout ratio for the attention probabilities.
- decoder_hidden_act ( str or function , optional , defaults to "quick_gelu" ) —
The non-linear activation function (function or string) in the encoder and pooler. If string, "gelu" , "relu" , "selu" and "gelu_new" "quick_gelu" are supported.
- decoder_intermediate_size ( int , optional , defaults to 2048) —
Dimensionality of the “intermediate” (i.e., feed-forward) layers in the Transformer decoder.
- conditional_layer ( int , optional , defaults to 0) —
The layer to use of the Transformer encoder whose activations will be combined with the condition
embeddings using FiLM (Feature-wise Linear Modulation). If 0, the last layer is used.
- use_complex_transposed_convolution ( bool , optional , defaults to False ) —
Whether to use a more complex transposed convolution in the decoder, enabling more fine-grained
segmentation.
- kwargs ( optional ) —
Dictionary of keyword arguments.
CLIPSegConfig is the configuration class to store the configuration of a CLIPSegModel . It is used to
instantiate a CLIPSeg model according to the specified arguments, defining the text model and vision model configs.
Instantiating a configuration with the defaults will yield a similar configuration to that of the CLIPSeg CIDAS/clipseg-rd64 architecture.
[LINK: CLIPSegConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegConfig)
[LINK: CLIPSegModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegModel)
Configuration objects inherit from PreTrainedConfig and can be used to control the model outputs. Read the
documentation from PreTrainedConfig for more information.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
Example:

## CLIPSegTextConfig

### class transformers. CLIPSegTextConfig

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/configuration_clipseg.py#L24)
( vocab_size = 49408 hidden_size = 512 intermediate_size = 2048 num_hidden_layers = 12 num_attention_heads = 8 max_position_embeddings = 77 hidden_act = 'quick_gelu' layer_norm_eps = 1e-05 attention_dropout = 0.0 initializer_range = 0.02 initializer_factor = 1.0 pad_token_id = 1 bos_token_id = 49406 eos_token_id = 49407 **kwargs )
Parameters
- vocab_size ( int , optional , defaults to 49408) —
Vocabulary size of the CLIPSeg text model. Defines the number of different tokens that can be represented
by the inputs_ids passed when calling CLIPSegModel .
[LINK: CLIPSegModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegModel)
- hidden_size ( int , optional , defaults to 512) —
Dimensionality of the encoder layers and the pooler layer.
- intermediate_size ( int , optional , defaults to 2048) —
Dimensionality of the “intermediate” (i.e., feed-forward) layer in the Transformer encoder.
- num_hidden_layers ( int , optional , defaults to 12) —
Number of hidden layers in the Transformer encoder.
- num_attention_heads ( int , optional , defaults to 8) —
Number of attention heads for each attention layer in the Transformer encoder.
- max_position_embeddings ( int , optional , defaults to 77) —
The maximum sequence length that this model might ever be used with. Typically set this to something large
just in case (e.g., 512 or 1024 or 2048).
- hidden_act ( str or function , optional , defaults to "quick_gelu" ) —
The non-linear activation function (function or string) in the encoder and pooler. If string, "gelu" , "relu" , "selu" and "gelu_new" "quick_gelu" are supported.
- layer_norm_eps ( float , optional , defaults to 1e-05) —
The epsilon used by the layer normalization layers.
- attention_dropout ( float , optional , defaults to 0.0) —
The dropout ratio for the attention probabilities.
- initializer_range ( float , optional , defaults to 0.02) —
The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
- initializer_factor ( float , optional , defaults to 1.0) —
A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
testing).
- pad_token_id ( int , optional , defaults to 1) —
Padding token id.
- bos_token_id ( int , optional , defaults to 49406) —
Beginning of stream token id.
- eos_token_id ( int , optional , defaults to 49407) —
End of stream token id.
This is the configuration class to store the configuration of a CLIPSegModel . It is used to instantiate an
CLIPSeg model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the CLIPSeg CIDAS/clipseg-rd64 architecture.
[LINK: CLIPSegModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegModel)
Configuration objects inherit from PreTrainedConfig and can be used to control the model outputs. Read the
documentation from PreTrainedConfig for more information.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
Example:

## CLIPSegVisionConfig

### class transformers. CLIPSegVisionConfig

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/configuration_clipseg.py#L119)
( hidden_size = 768 intermediate_size = 3072 num_hidden_layers = 12 num_attention_heads = 12 num_channels = 3 image_size = 224 patch_size = 32 hidden_act = 'quick_gelu' layer_norm_eps = 1e-05 attention_dropout = 0.0 initializer_range = 0.02 initializer_factor = 1.0 **kwargs )
Parameters
- hidden_size ( int , optional , defaults to 768) —
Dimensionality of the encoder layers and the pooler layer.
- intermediate_size ( int , optional , defaults to 3072) —
Dimensionality of the “intermediate” (i.e., feed-forward) layer in the Transformer encoder.
- num_hidden_layers ( int , optional , defaults to 12) —
Number of hidden layers in the Transformer encoder.
- num_attention_heads ( int , optional , defaults to 12) —
Number of attention heads for each attention layer in the Transformer encoder.
- num_channels ( int , optional , defaults to 3) —
The number of input channels.
- image_size ( int , optional , defaults to 224) —
The size (resolution) of each image.
- patch_size ( int , optional , defaults to 32) —
The size (resolution) of each patch.
- hidden_act ( str or function , optional , defaults to "quick_gelu" ) —
The non-linear activation function (function or string) in the encoder and pooler. If string, "gelu" , "relu" , "selu" and "gelu_new" "quick_gelu" are supported.
- layer_norm_eps ( float , optional , defaults to 1e-05) —
The epsilon used by the layer normalization layers.
- attention_dropout ( float , optional , defaults to 0.0) —
The dropout ratio for the attention probabilities.
- initializer_range ( float , optional , defaults to 0.02) —
The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
- initializer_factor ( float , optional , defaults to 1.0) —
A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
testing).
This is the configuration class to store the configuration of a CLIPSegModel . It is used to instantiate an
CLIPSeg model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the CLIPSeg CIDAS/clipseg-rd64 architecture.
[LINK: CLIPSegModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegModel)
Configuration objects inherit from PreTrainedConfig and can be used to control the model outputs. Read the
documentation from PreTrainedConfig for more information.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
Example:

## CLIPSegProcessor

### class transformers. CLIPSegProcessor

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/processing_clipseg.py#L23)
( image_processor = None tokenizer = None **kwargs )
Parameters
- image_processor ( ViTImageProcessor , optional ) —
The image processor is a required input.
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
- tokenizer ( CLIPTokenizerFast , optional ) —
The tokenizer is a required input.
[LINK: CLIPTokenizerFast](/docs/transformers/v5.0.0rc2/en/model_doc/clip#transformers.CLIPTokenizer)
Constructs a CLIPSeg processor which wraps a CLIPSeg image processor and a CLIP tokenizer into a single processor.
CLIPSegProcessor offers all the functionalities of ViTImageProcessor and CLIPTokenizerFast . See the __call__() and decode() for more information.
[LINK: CLIPSegProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegProcessor)
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
[LINK: CLIPTokenizerFast](/docs/transformers/v5.0.0rc2/en/model_doc/clip#transformers.CLIPTokenizer)
[LINK: decode()](/docs/transformers/v5.0.0rc2/en/main_classes/processors#transformers.ProcessorMixin.decode)

## CLIPSegModel

### class transformers. CLIPSegModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L814)
( config : CLIPSegConfig )
Parameters
- config ( CLIPSegConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: CLIPSegConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The bare Clipseg Model outputting raw hidden-states without any specific head on top.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L928)
( input_ids : typing.Optional[torch.LongTensor] = None pixel_values : typing.Optional[torch.FloatTensor] = None attention_mask : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.LongTensor] = None return_loss : typing.Optional[bool] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None interpolate_pos_encoding : bool = True return_dict : typing.Optional[bool] = None **kwargs ) → transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or tuple(torch.FloatTensor)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- pixel_values ( torch.FloatTensor of shape (batch_size, num_channels, image_size, image_size) , optional ) —
The tensors corresponding to the input images. Pixel values can be obtained using ViTImageProcessor . See ViTImageProcessor. call () for details ( CLIPSegProcessor uses ViTImageProcessor for processing images).
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
[LINK: ViTImageProcessor. call ()](/docs/transformers/v5.0.0rc2/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__)
[LINK: CLIPSegProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegProcessor)
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- position_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- return_loss ( bool , optional ) —
Whether or not to return the contrastive loss.
- output_attentions ( bool , optional ) —
Whether or not to return the attentions tensors of all attention layers. See attentions under returned
tensors for more detail.
- output_hidden_states ( bool , optional ) —
Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for
more detail.
- interpolate_pos_encoding ( bool , optional , defaults to True ) —
Whether to interpolate the pre-trained position encodings.
- return_dict ( bool , optional ) —
Whether or not to return a ModelOutput instead of a plain tuple.
[LINK: ModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.utils.ModelOutput)
Returns
transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or tuple(torch.FloatTensor)
A transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when return_loss is True ) — Contrastive loss for image-text similarity. logits_per_image ( torch.FloatTensor of shape (image_batch_size, text_batch_size) ) — The scaled dot product scores between image_embeds and text_embeds . This represents the image-text
similarity scores. logits_per_text ( torch.FloatTensor of shape (text_batch_size, image_batch_size) ) — The scaled dot product scores between text_embeds and image_embeds . This represents the text-image
similarity scores. text_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The text embeddings obtained by applying the projection layer to the pooled output of CLIPSegTextModel . image_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The image embeddings obtained by applying the projection layer to the pooled output of CLIPSegVisionModel . text_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.text_model_output , defaults to None ) — The output of the CLIPSegTextModel . vision_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.vision_model_output , defaults to None ) — The output of the CLIPSegVisionModel .
A transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs.
[LINK: CLIPSegConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when return_loss is True ) — Contrastive loss for image-text similarity.
- logits_per_image ( torch.FloatTensor of shape (image_batch_size, text_batch_size) ) — The scaled dot product scores between image_embeds and text_embeds . This represents the image-text
similarity scores.
- logits_per_text ( torch.FloatTensor of shape (text_batch_size, image_batch_size) ) — The scaled dot product scores between text_embeds and image_embeds . This represents the text-image
similarity scores.
- text_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The text embeddings obtained by applying the projection layer to the pooled output of CLIPSegTextModel .
[LINK: CLIPSegTextModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegTextModel)
- image_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The image embeddings obtained by applying the projection layer to the pooled output of CLIPSegVisionModel .
[LINK: CLIPSegVisionModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegVisionModel)
- text_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.text_model_output , defaults to None ) — The output of the CLIPSegTextModel .
[LINK: CLIPSegTextModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegTextModel)
- vision_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.vision_model_output , defaults to None ) — The output of the CLIPSegVisionModel .
[LINK: CLIPSegVisionModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegVisionModel)
The CLIPSegModel forward method, overrides the __call__ special method.
[LINK: CLIPSegModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Examples:
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L853)
( input_ids : Tensor attention_mask : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None ) → text_features ( torch.FloatTensor of shape (batch_size, output_dim )
Parameters
- input_ids ( torch.Tensor of shape (batch_size, sequence_length) ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
Returns
text_features ( torch.FloatTensor of shape (batch_size, output_dim )
The text embeddings obtained by
applying the projection layer to the pooled output of CLIPSegTextModel .
The text embeddings obtained by
applying the projection layer to the pooled output of CLIPSegTextModel .
[LINK: CLIPSegTextModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegTextModel)
Examples:
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L889)
( pixel_values : FloatTensor interpolate_pos_encoding : bool = True ) → image_features ( torch.FloatTensor of shape (batch_size, output_dim )
Parameters
- pixel_values ( torch.FloatTensor of shape (batch_size, num_channels, image_size, image_size) ) —
The tensors corresponding to the input images. Pixel values can be obtained using ViTImageProcessor . See ViTImageProcessor. call () for details ( CLIPSegProcessor uses ViTImageProcessor for processing images).
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
[LINK: ViTImageProcessor. call ()](/docs/transformers/v5.0.0rc2/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__)
[LINK: CLIPSegProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegProcessor)
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
- interpolate_pos_encoding ( bool , optional , defaults to True ) —
Whether to interpolate the pre-trained position encodings.
Returns
image_features ( torch.FloatTensor of shape (batch_size, output_dim )
The image embeddings obtained by
applying the projection layer to the pooled output of CLIPSegVisionModel .
The image embeddings obtained by
applying the projection layer to the pooled output of CLIPSegVisionModel .
[LINK: CLIPSegVisionModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegVisionModel)
Examples:

## CLIPSegTextModel

### class transformers. CLIPSegTextModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L654)
( config : CLIPSegTextConfig )
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L672)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None return_dict : typing.Optional[bool] = None **kwargs ) → transformers.modeling_outputs.BaseModelOutputWithPooling or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling)
Parameters
- input_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- output_attentions ( bool , optional ) —
Whether or not to return the attentions tensors of all attention layers. See attentions under returned
tensors for more detail.
- output_hidden_states ( bool , optional ) —
Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for
more detail.
- return_dict ( bool , optional ) —
Whether or not to return a ModelOutput instead of a plain tuple.
[LINK: ModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.utils.ModelOutput)
Returns
transformers.modeling_outputs.BaseModelOutputWithPooling or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling)
A transformers.modeling_outputs.BaseModelOutputWithPooling or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs. last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model. pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining. hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.BaseModelOutputWithPooling or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs.
[LINK: transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling)
[LINK: CLIPSegConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegConfig)
- last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model.
last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model.
- pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining.
pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining.
- hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) .
Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) .
Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
The CLIPSegTextModel forward method, overrides the __call__ special method.
[LINK: CLIPSegTextModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegTextModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Examples:

## CLIPSegVisionModel

### class transformers. CLIPSegVisionModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L760)
( config : CLIPSegVisionConfig )
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L774)
( pixel_values : typing.Optional[torch.FloatTensor] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None interpolate_pos_encoding : typing.Optional[bool] = True return_dict : typing.Optional[bool] = None **kwargs ) → transformers.modeling_outputs.BaseModelOutputWithPooling or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling)
Parameters
- pixel_values ( torch.FloatTensor of shape (batch_size, num_channels, image_size, image_size) , optional ) —
The tensors corresponding to the input images. Pixel values can be obtained using ViTImageProcessor . See ViTImageProcessor. call () for details ( CLIPSegProcessor uses ViTImageProcessor for processing images).
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
[LINK: ViTImageProcessor. call ()](/docs/transformers/v5.0.0rc2/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__)
[LINK: CLIPSegProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegProcessor)
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
- output_attentions ( bool , optional ) —
Whether or not to return the attentions tensors of all attention layers. See attentions under returned
tensors for more detail.
- output_hidden_states ( bool , optional ) —
Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for
more detail.
- interpolate_pos_encoding ( bool , optional , defaults to True ) —
Whether to interpolate the pre-trained position encodings.
- return_dict ( bool , optional ) —
Whether or not to return a ModelOutput instead of a plain tuple.
[LINK: ModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.utils.ModelOutput)
Returns
transformers.modeling_outputs.BaseModelOutputWithPooling or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling)
A transformers.modeling_outputs.BaseModelOutputWithPooling or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs. last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model. pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining. hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.BaseModelOutputWithPooling or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs.
[LINK: transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling)
[LINK: CLIPSegConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegConfig)
- last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model.
last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model.
- pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining.
pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining.
- hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) .
Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) .
Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
The CLIPSegVisionModel forward method, overrides the __call__ special method.
[LINK: CLIPSegVisionModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegVisionModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Examples:

## CLIPSegForImageSegmentation

### class transformers. CLIPSegForImageSegmentation

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L1191)
( config : CLIPSegConfig )
Parameters
- config ( CLIPSegConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: CLIPSegConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
CLIPSeg model with a Transformer-based decoder on top for zero-shot and one-shot image segmentation.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/clipseg/modeling_clipseg.py#L1236)
( input_ids : typing.Optional[torch.FloatTensor] = None pixel_values : typing.Optional[torch.FloatTensor] = None conditional_pixel_values : typing.Optional[torch.FloatTensor] = None conditional_embeddings : typing.Optional[torch.FloatTensor] = None attention_mask : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.LongTensor] = None labels : typing.Optional[torch.LongTensor] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None interpolate_pos_encoding : bool = True return_dict : typing.Optional[bool] = None **kwargs ) → transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or tuple(torch.FloatTensor)
Parameters
- input_ids ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- pixel_values ( torch.FloatTensor of shape (batch_size, num_channels, image_size, image_size) , optional ) —
The tensors corresponding to the input images. Pixel values can be obtained using ViTImageProcessor . See ViTImageProcessor. call () for details ( CLIPSegProcessor uses ViTImageProcessor for processing images).
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
[LINK: ViTImageProcessor. call ()](/docs/transformers/v5.0.0rc2/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__)
[LINK: CLIPSegProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegProcessor)
[LINK: ViTImageProcessor](/docs/transformers/v5.0.0rc2/en/model_doc/vit#transformers.ViTImageProcessor)
- conditional_pixel_values ( torch.FloatTensor , optional ) —
The pixel values of the conditional images.
- conditional_embeddings ( torch.FloatTensor of shape (batch_size, config.projection_dim) , optional ) —
The conditional embeddings for the query images. If provided, the model will use this instead of computing
the embeddings from the conditional_pixel_values.
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- position_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the sequence classification/regression loss. Indices should be in [0, ..., config.num_labels - 1] . If config.num_labels == 1 a regression loss is computed (Mean-Square loss), If config.num_labels > 1 a classification loss is computed (Cross-Entropy).
- output_attentions ( bool , optional ) —
Whether or not to return the attentions tensors of all attention layers. See attentions under returned
tensors for more detail.
- output_hidden_states ( bool , optional ) —
Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for
more detail.
- interpolate_pos_encoding ( bool , optional , defaults to True ) —
Whether to interpolate the pre-trained position encodings.
- return_dict ( bool , optional ) —
Whether or not to return a ModelOutput instead of a plain tuple.
[LINK: ModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.utils.ModelOutput)
Returns
transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or tuple(torch.FloatTensor)
A transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when return_loss is True ) — Contrastive loss for image-text similarity. logits_per_image ( torch.FloatTensor of shape (image_batch_size, text_batch_size) ) — The scaled dot product scores between image_embeds and text_embeds . This represents the image-text
similarity scores. logits_per_text ( torch.FloatTensor of shape (text_batch_size, image_batch_size) ) — The scaled dot product scores between text_embeds and image_embeds . This represents the text-image
similarity scores. text_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The text embeddings obtained by applying the projection layer to the pooled output of CLIPSegTextModel . image_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The image embeddings obtained by applying the projection layer to the pooled output of CLIPSegVisionModel . text_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.text_model_output , defaults to None ) — The output of the CLIPSegTextModel . vision_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.vision_model_output , defaults to None ) — The output of the CLIPSegVisionModel .
A transformers.models.clipseg.modeling_clipseg.CLIPSegOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( CLIPSegConfig ) and inputs.
[LINK: CLIPSegConfig](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when return_loss is True ) — Contrastive loss for image-text similarity.
- logits_per_image ( torch.FloatTensor of shape (image_batch_size, text_batch_size) ) — The scaled dot product scores between image_embeds and text_embeds . This represents the image-text
similarity scores.
- logits_per_text ( torch.FloatTensor of shape (text_batch_size, image_batch_size) ) — The scaled dot product scores between text_embeds and image_embeds . This represents the text-image
similarity scores.
- text_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The text embeddings obtained by applying the projection layer to the pooled output of CLIPSegTextModel .
[LINK: CLIPSegTextModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegTextModel)
- image_embeds ( torch.FloatTensor of shape (batch_size, output_dim ) — The image embeddings obtained by applying the projection layer to the pooled output of CLIPSegVisionModel .
[LINK: CLIPSegVisionModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegVisionModel)
- text_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.text_model_output , defaults to None ) — The output of the CLIPSegTextModel .
[LINK: CLIPSegTextModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegTextModel)
- vision_model_output ( <class '~modeling_outputs.BaseModelOutputWithPooling'>.vision_model_output , defaults to None ) — The output of the CLIPSegVisionModel .
[LINK: CLIPSegVisionModel](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegVisionModel)
The CLIPSegForImageSegmentation forward method, overrides the __call__ special method.
[LINK: CLIPSegForImageSegmentation](/docs/transformers/v5.0.0rc2/en/model_doc/clipseg#transformers.CLIPSegForImageSegmentation)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Examples:
[LINK: Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/clipseg.md)
[LINK: ← CLIP](/docs/transformers/model_doc/clip)
[LINK: CLVP →](/docs/transformers/model_doc/clvp)

--------------------