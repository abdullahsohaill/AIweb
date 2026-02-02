# Bloom
**URL:** https://huggingface.co/docs/transformers/model_doc/bloom
**Page Title:** BLOOM
--------------------

Transformers documentation
BLOOM

## Transformers

[LINK: 155,733](https://github.com/huggingface/transformers)
and get access to the augmented documentation experience
to get started
This model was released on 2022-11-09 and added to Hugging Face Transformers on 2022-06-09.

## BLOOM

## Overview

The BLOOM model has been proposed with its various versions through the BigScience Workshop . BigScience is inspired by other open science initiatives where researchers have pooled their time and resources to collectively achieve a higher impact.
The architecture of BLOOM is essentially similar to GPT3 (auto-regressive model for next token prediction), but has been trained on 46 different languages and 13 programming languages.
Several smaller versions of the models have been trained on the same dataset. BLOOM is available in the following versions:
- bloom-560m
- bloom-1b1
- bloom-1b7
- bloom-3b
- bloom-7b1
- bloom (176B parameters)

## Resources

A list of official Hugging Face and community (indicated by 🌎) resources to help you get started with BLOOM. If you’re interested in submitting a resource to be included here, please feel free to open a Pull Request and we’ll review it! The resource should ideally demonstrate something new instead of duplicating an existing resource.
- BloomForCausalLM is supported by this causal language modeling example script and notebook .
[LINK: BloomForCausalLM](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomForCausalLM)
[LINK: causal language modeling example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/language-modeling#gpt-2gpt-and-causal-language-modeling)
[LINK: notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/language_modeling.ipynb)
See also:
- Causal language modeling task guide
- Text classification task guide
- Token classification task guide
- Question answering task guide
⚡️ Inference
- A blog on Optimization story: Bloom inference .
- A blog on Incredibly Fast BLOOM Inference with DeepSpeed and Accelerate .
⚙️ Training
- A blog on The Technology Behind BLOOM Training .

## BloomConfig

### class transformers. BloomConfig

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/configuration_bloom.py#L24)
( vocab_size = 250880 hidden_size = 64 n_layer = 2 n_head = 8 layer_norm_epsilon = 1e-05 initializer_range = 0.02 use_cache = True bos_token_id = 1 eos_token_id = 2 apply_residual_connection_post_layernorm = False hidden_dropout = 0.0 attention_dropout = 0.0 pretraining_tp = 1 slow_but_exact = False **kwargs )
Parameters
- vocab_size ( int , optional , defaults to 250880) —
Vocabulary size of the Bloom model. Defines the maximum number of different tokens that can be represented
by the inputs_ids passed when calling BloomModel . Check this
discussion on how the vocab_size has been defined.
[LINK: BloomModel](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomModel)
- hidden_size ( int , optional , defaults to 64) —
Dimensionality of the embeddings and hidden states.
- n_layer ( int , optional , defaults to 2) —
Number of hidden layers in the Transformer encoder.
- n_head ( int , optional , defaults to 8) —
Number of attention heads for each attention layer in the Transformer encoder.
- layer_norm_epsilon ( float , optional , defaults to 1e-5) —
The epsilon to use in the layer normalization layers.
- initializer_range ( float , optional , defaults to 0.02) —
The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
- apply_residual_connection_post_layernorm ( bool , optional , defaults to False ) —
If enabled, use the layer norm of the hidden states as the residual in the transformer blocks
- hidden_dropout ( float , optional , defaults to 0.1) —
Dropout rate of the dropout function on the bias dropout.
- attention_dropout ( float , optional , defaults to 0.1) —
Dropout rate applied to the attention probs
- use_cache ( bool , optional , defaults to True ) —
Whether or not the model should return the last key/values attentions (not used by all models).
- pretraining_tp ( int , optional , defaults to 1 ) —
Experimental feature. Tensor parallelism rank used during pretraining with Megatron. Please refer to this
document to understand more about it. This value is
necessary to ensure exact reproducibility of the pretraining results. Please refer to this
issue . Note also that this is enabled only when slow_but_exact=True .
[LINK: this
document](https://huggingface.co/docs/transformers/parallelism)
[LINK: this
issue](https://github.com/pytorch/pytorch/issues/76232)
- slow_but_exact ( bool , optional , defaults to False ) —
Experimental feature. Whether to use slow but exact implementation of the attention mechanism. While
merging the TP rank tensors, due to slicing operations the results may be slightly different between the
model trained on Megatron and our model. Please refer to this
issue . A solution to obtain more accurate results is to
enable this feature. Enabling this will hurt the computational time of the inference. Will be probably
resolved in the future once the main model has been fine-tuned with TP_rank=1.
[LINK: this
issue](https://github.com/pytorch/pytorch/issues/76232)
This is the configuration class to store the configuration of a BloomModel . It is used to instantiate a Bloom
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to the Bloom architecture bigscience/bloom .
[LINK: BloomModel](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomModel)
Configuration objects inherit from PreTrainedConfig and can be used to control the model outputs. Read the
documentation from PreTrainedConfig for more information.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
Example:

## BloomModel

### class transformers. BloomModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L425)
( config : BloomConfig )
Parameters
- config ( BloomConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The bare Bloom Model outputting raw hidden-states without any specific head on top.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L456)
( input_ids : typing.Optional[torch.LongTensor] = None past_key_values : typing.Optional[transformers.cache_utils.Cache] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.LongTensor] = None use_cache : typing.Optional[bool] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None return_dict : typing.Optional[bool] = None cache_position : typing.Optional[torch.LongTensor] = None **kwargs ) → transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, input_ids_length) ) — input_ids_length = sequence_length if past_key_values is None else past_key_values.get_seq_length() ( sequence_length of input past key value states). Indices of input sequence tokens in the vocabulary. If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids . Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids .
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- past_key_values ( ~cache_utils.Cache , optional ) —
Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
blocks) that can be used to speed up sequential decoding. This typically consists in the past_key_values returned by the model at a previous stage of decoding, when use_cache=True or config.use_cache=True . Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default. The model will output the same cache format that is fed as input. If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default.
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
[LINK: DynamicCache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.DynamicCache)
The model will output the same cache format that is fed as input.
If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- inputs_embeds ( torch.LongTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- use_cache ( bool , optional ) —
If set to True , past_key_values key value states are returned and can be used to speed up decoding (see past_key_values ).
- output_attentions ( bool , optional ) —
Whether or not to return the attentions tensors of all attention layers. See attentions under returned
tensors for more detail.
- output_hidden_states ( bool , optional ) —
Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for
more detail.
- return_dict ( bool , optional ) —
Whether or not to return a ModelOutput instead of a plain tuple.
[LINK: ModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.utils.ModelOutput)
- cache_position ( torch.LongTensor of shape (sequence_length) , optional ) —
Indices depicting the position of the input sequence tokens in the sequence. Contrarily to position_ids ,
this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
the complete sequence length.
Returns
transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions)
A transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs. last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model. If past_key_values is used only the last hidden-state of the sequences of shape (batch_size, 1, hidden_size) is output. past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding. hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads. cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True and config.add_cross_attention=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the
weighted average in the cross-attention heads.
A transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs.
[LINK: transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPastAndCrossAttentions)
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
- last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model. If past_key_values is used only the last hidden-state of the sequences of shape (batch_size, 1, hidden_size) is output.
last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model.
If past_key_values is used only the last hidden-state of the sequences of shape (batch_size, 1, hidden_size) is output.
- past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide .
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
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
- cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True and config.add_cross_attention=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the
weighted average in the cross-attention heads.
cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True and config.add_cross_attention=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) .
Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the
weighted average in the cross-attention heads.
The BloomModel forward method, overrides the __call__ special method.
[LINK: BloomModel](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

## BloomForCausalLM

### class transformers. BloomForCausalLM

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L695)
( config : BloomConfig )
Parameters
- config ( BloomConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bloom Model transformer with a language modeling head on top (linear layer with weights tied to the input
embeddings).
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L746)
( input_ids : typing.Optional[torch.LongTensor] = None past_key_values : typing.Optional[transformers.cache_utils.Cache] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None use_cache : typing.Optional[bool] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None return_dict : typing.Optional[bool] = None cache_position : typing.Optional[torch.LongTensor] = None logits_to_keep : typing.Union[int, torch.Tensor] = 0 **kwargs ) → transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, input_ids_length) ) — input_ids_length = sequence_length if past_key_values is None else past_key_values.get_seq_length() ( sequence_length of input past key value states). Indices of input sequence tokens in the vocabulary. If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids . Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids .
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- past_key_values ( ~cache_utils.Cache , optional ) —
Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
blocks) that can be used to speed up sequential decoding. This typically consists in the past_key_values returned by the model at a previous stage of decoding, when use_cache=True or config.use_cache=True . Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default. The model will output the same cache format that is fed as input. If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default.
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
[LINK: DynamicCache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.DynamicCache)
The model will output the same cache format that is fed as input.
If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- inputs_embeds ( torch.Tensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for language modeling. Note that the labels are shifted inside the model, i.e. you can set labels = input_ids Indices are selected in [-100, 0, ..., config.vocab_size] All labels set to -100 are ignored (masked), the loss is only computed for labels in [0, ..., config.vocab_size]
- use_cache ( bool , optional ) —
If set to True , past_key_values key value states are returned and can be used to speed up decoding (see past_key_values ).
- output_attentions ( bool , optional ) —
Whether or not to return the attentions tensors of all attention layers. See attentions under returned
tensors for more detail.
- output_hidden_states ( bool , optional ) —
Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for
more detail.
- return_dict ( bool , optional ) —
Whether or not to return a ModelOutput instead of a plain tuple.
[LINK: ModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.utils.ModelOutput)
- cache_position ( torch.LongTensor of shape (sequence_length) , optional ) —
Indices depicting the position of the input sequence tokens in the sequence. Contrarily to position_ids ,
this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
the complete sequence length.
- logits_to_keep ( Union[int, torch.Tensor] , optional , defaults to 0 ) —
If an int , compute logits for the last logits_to_keep tokens. If 0 , calculate logits for all input_ids (special case). Only last token logits are needed for generation, and calculating them only for that
token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
If a torch.Tensor , must be 1D corresponding to the indices to keep in the sequence length dimension.
This is useful when using packed tensor format (single dimension for batch and sequence length).
Returns
transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
A transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Language modeling loss (for next-token prediction). logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads. cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Cross attentions weights after the attention softmax, used to compute the weighted average in the
cross-attention heads. past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
A transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs.
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Language modeling loss (for next-token prediction).
loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Language modeling loss (for next-token prediction).
- logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
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
- cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Cross attentions weights after the attention softmax, used to compute the weighted average in the
cross-attention heads.
cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) .
Cross attentions weights after the attention softmax, used to compute the weighted average in the
cross-attention heads.
- past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide .
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
Contains pre-computed hidden-states (key and values in the attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
The BloomForCausalLM forward method, overrides the __call__ special method.
[LINK: BloomForCausalLM](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomForCausalLM)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BloomForSequenceClassification

### class transformers. BloomForSequenceClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L834)
( config : BloomConfig )
Parameters
- config ( BloomConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bloom Model transformer with a sequence classification head on top (linear layer).
BloomForSequenceClassification uses the last token in order to do the classification, as other causal models
(e.g. GPT-1) do.
[LINK: BloomForSequenceClassification](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomForSequenceClassification)
Since it does classification on the last token, it requires to know the position of the last token. If a pad_token_id is defined in the configuration, it finds the last token that is not a padding token in each row. If
no pad_token_id is defined, it simply takes the last value in each row of the batch. Since it cannot guess the
padding tokens when inputs_embeds are passed instead of input_ids , it does the same (take the last value in
each row of the batch).
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L844)
( input_ids : typing.Optional[torch.LongTensor] = None past_key_values : typing.Optional[transformers.cache_utils.Cache] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None use_cache : typing.Optional[bool] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None return_dict : typing.Optional[bool] = None **kwargs ) → transformers.modeling_outputs.SequenceClassifierOutputWithPast or tuple(torch.FloatTensor)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, input_ids_length) ) — input_ids_length = sequence_length if past_key_values is None else past_key_values.get_seq_length() ( sequence_length of input past key value states). Indices of input sequence tokens in the vocabulary. If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids . Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids .
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- past_key_values ( ~cache_utils.Cache , optional ) —
Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
blocks) that can be used to speed up sequential decoding. This typically consists in the past_key_values returned by the model at a previous stage of decoding, when use_cache=True or config.use_cache=True . Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default. The model will output the same cache format that is fed as input. If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default.
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
[LINK: DynamicCache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.DynamicCache)
The model will output the same cache format that is fed as input.
If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- inputs_embeds ( torch.Tensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the sequence classification/regression loss. Indices should be in [0, ..., config.num_labels - 1] . If config.num_labels == 1 a regression loss is computed (Mean-Square loss), If config.num_labels > 1 a classification loss is computed (Cross-Entropy).
- use_cache ( bool , optional ) —
If set to True , past_key_values key value states are returned and can be used to speed up decoding (see past_key_values ).
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
transformers.modeling_outputs.SequenceClassifierOutputWithPast or tuple(torch.FloatTensor)
A transformers.modeling_outputs.SequenceClassifierOutputWithPast or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss. logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax). past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding. hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.SequenceClassifierOutputWithPast or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs.
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss.
loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss.
- logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax).
logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax).
- past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide .
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
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
The BloomForSequenceClassification forward method, overrides the __call__ special method.
[LINK: BloomForSequenceClassification](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomForSequenceClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example of single-label classification:
Example of multi-label classification:

## BloomForTokenClassification

### class transformers. BloomForTokenClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L950)
( config : BloomConfig )
Parameters
- config ( BloomConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bloom transformer with a token classification head on top (a linear layer on top of the hidden-states
output) e.g. for Named-Entity-Recognition (NER) tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L968)
( input_ids : typing.Optional[torch.LongTensor] = None past_key_values : typing.Optional[transformers.cache_utils.Cache] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None use_cache : typing.Optional[bool] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None return_dict : typing.Optional[bool] = None **kwargs ) → transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, input_ids_length) ) — input_ids_length = sequence_length if past_key_values is None else past_key_values.get_seq_length() ( sequence_length of input past key value states). Indices of input sequence tokens in the vocabulary. If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids . Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids .
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- past_key_values ( ~cache_utils.Cache , optional ) —
Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
blocks) that can be used to speed up sequential decoding. This typically consists in the past_key_values returned by the model at a previous stage of decoding, when use_cache=True or config.use_cache=True . Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default. The model will output the same cache format that is fed as input. If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default.
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
[LINK: DynamicCache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.DynamicCache)
The model will output the same cache format that is fed as input.
If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- inputs_embeds ( torch.Tensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the sequence classification/regression loss. Indices should be in [0, ..., config.num_labels - 1] . If config.num_labels == 1 a regression loss is computed (Mean-Square loss), If config.num_labels > 1 a classification loss is computed (Cross-Entropy).
- use_cache ( bool , optional ) —
If set to True , past_key_values key value states are returned and can be used to speed up decoding (see past_key_values ).
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
transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided)  — Classification loss. logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.num_labels) ) — Classification scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs.
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided)  — Classification loss.
loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided)  — Classification loss.
- logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.num_labels) ) — Classification scores (before SoftMax).
logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.num_labels) ) — Classification scores (before SoftMax).
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
The BloomForTokenClassification forward method, overrides the __call__ special method.
[LINK: BloomForTokenClassification](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomForTokenClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BloomForQuestionAnswering

### class transformers. BloomForQuestionAnswering

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L1039)
( config )
Parameters
- config ( BloomForQuestionAnswering ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BloomForQuestionAnswering](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomForQuestionAnswering)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bloom transformer with a span classification head on top for extractive question-answering tasks like
SQuAD (a linear layer on top of the hidden-states output to compute span start logits and span end logits ).
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bloom/modeling_bloom.py#L1048)
( input_ids : typing.Optional[torch.LongTensor] = None attention_mask : typing.Optional[torch.FloatTensor] = None inputs_embeds : typing.Optional[torch.FloatTensor] = None start_positions : typing.Optional[torch.LongTensor] = None end_positions : typing.Optional[torch.LongTensor] = None output_attentions : typing.Optional[bool] = None output_hidden_states : typing.Optional[bool] = None return_dict : typing.Optional[bool] = None **kwargs ) → transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, input_ids_length) ) — input_ids_length = sequence_length if past_key_values is None else past_key_values.get_seq_length() ( sequence_length of input past key value states). Indices of input sequence tokens in the vocabulary. If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids . Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
If past_key_values is used, only input_ids that do not have their past calculated should be passed as input_ids .
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0rc2/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- inputs_embeds ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- start_positions ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for position (index) of the start of the labelled span for computing the token classification loss.
Positions are clamped to the length of the sequence ( sequence_length ). Position outside of the sequence
are not taken into account for computing the loss.
- end_positions ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for position (index) of the end of the labelled span for computing the token classification loss.
Positions are clamped to the length of the sequence ( sequence_length ). Position outside of the sequence
are not taken into account for computing the loss.
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
transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Total span extraction loss is the sum of a Cross-Entropy for the start and end positions. start_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-start scores (before SoftMax). end_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-end scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BloomConfig ) and inputs.
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
[LINK: BloomConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Total span extraction loss is the sum of a Cross-Entropy for the start and end positions.
loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Total span extraction loss is the sum of a Cross-Entropy for the start and end positions.
- start_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-start scores (before SoftMax).
start_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-start scores (before SoftMax).
- end_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-end scores (before SoftMax).
end_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-end scores (before SoftMax).
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
The BloomForQuestionAnswering forward method, overrides the __call__ special method.
[LINK: BloomForQuestionAnswering](/docs/transformers/v5.0.0rc2/en/model_doc/bloom#transformers.BloomForQuestionAnswering)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:
[LINK: Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/bloom.md)
[LINK: ← Blenderbot Small](/docs/transformers/model_doc/blenderbot-small)
[LINK: BLT →](/docs/transformers/model_doc/blt)

--------------------