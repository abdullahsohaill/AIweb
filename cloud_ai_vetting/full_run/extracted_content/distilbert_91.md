# DistilBERT
**URL:** https://huggingface.co/docs/transformers/en/model_doc/distilbert
**Page Title:** DistilBERT
--------------------

Transformers documentation
DistilBERT

## Transformers

[LINK: 155,701](https://github.com/huggingface/transformers)
and get access to the augmented documentation experience
to get started
This model was released on 2019-10-02 and added to Hugging Face Transformers on 2020-11-16.

## DistilBERT

DistilBERT is pretrained by knowledge distillation to create a smaller model with faster inference and requires less compute to train. Through a triple loss objective during pretraining, language modeling loss, distillation loss, cosine-distance loss, DistilBERT demonstrates similar performance to a larger transformer language model.
You can find all the original DistilBERT checkpoints under the DistilBERT organization.
Click on the DistilBERT models in the right sidebar for more examples of how to apply DistilBERT to different language tasks.
The example below demonstrates how to classify text with Pipeline , AutoModel , and from the command line.
[LINK: Pipeline](/docs/transformers/v5.0.0rc2/en/main_classes/pipelines#transformers.Pipeline)
[LINK: AutoModel](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoModel)

## Notes

- DistilBERT doesn’t have token_type_ids , you don’t need to indicate which token belongs to which segment. Just
separate your segments with the separation token tokenizer.sep_token (or [SEP] ).
- DistilBERT doesn’t have options to select the input positions ( position_ids input). This could be added if
necessary though, just let us know if you need this option.

## DistilBertConfig

### class transformers. DistilBertConfig

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/configuration_distilbert.py#L24)
( vocab_size = 30522 max_position_embeddings = 512 sinusoidal_pos_embds = False n_layers = 6 n_heads = 12 dim = 768 hidden_dim = 3072 dropout = 0.1 attention_dropout = 0.1 activation = 'gelu' initializer_range = 0.02 qa_dropout = 0.1 seq_classif_dropout = 0.2 pad_token_id = 0 **kwargs )
Parameters
- vocab_size ( int , optional , defaults to 30522) —
Vocabulary size of the DistilBERT model. Defines the number of different tokens that can be represented by
the inputs_ids passed when calling DistilBertModel .
[LINK: DistilBertModel](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertModel)
- max_position_embeddings ( int , optional , defaults to 512) —
The maximum sequence length that this model might ever be used with. Typically set this to something large
just in case (e.g., 512 or 1024 or 2048).
- sinusoidal_pos_embds ( boolean , optional , defaults to False ) —
Whether to use sinusoidal positional embeddings.
- n_layers ( int , optional , defaults to 6) —
Number of hidden layers in the Transformer encoder.
- n_heads ( int , optional , defaults to 12) —
Number of attention heads for each attention layer in the Transformer encoder.
- dim ( int , optional , defaults to 768) —
Dimensionality of the encoder layers and the pooler layer.
- hidden_dim ( int , optional , defaults to 3072) —
The size of the “intermediate” (often named feed-forward) layer in the Transformer encoder.
- dropout ( float , optional , defaults to 0.1) —
The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
- attention_dropout ( float , optional , defaults to 0.1) —
The dropout ratio for the attention probabilities.
- activation ( str or Callable , optional , defaults to "gelu" ) —
The non-linear activation function (function or string) in the encoder and pooler. If string, "gelu" , "relu" , "silu" and "gelu_new" are supported.
- initializer_range ( float , optional , defaults to 0.02) —
The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
- qa_dropout ( float , optional , defaults to 0.1) —
The dropout probabilities used in the question answering model DistilBertForQuestionAnswering .
[LINK: DistilBertForQuestionAnswering](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertForQuestionAnswering)
- seq_classif_dropout ( float , optional , defaults to 0.2) —
The dropout probabilities used in the sequence classification and the multiple choice model DistilBertForSequenceClassification .
[LINK: DistilBertForSequenceClassification](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertForSequenceClassification)
This is the configuration class to store the configuration of a DistilBertModel . It
is used to instantiate a DistilBERT model according to the specified arguments, defining the model architecture.
Instantiating a configuration with the defaults will yield a similar configuration to that of the DistilBERT distilbert-base-uncased architecture.
[LINK: DistilBertModel](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertModel)
Configuration objects inherit from PreTrainedConfig and can be used to control the model outputs. Read the
documentation from PreTrainedConfig for more information.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
Examples:

## DistilBertTokenizer

### class transformers. DistilBertTokenizer

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/tokenization_distilbert.py#L23)
( *args do_lower_case : bool = True **kwargs )

## DistilBertTokenizerFast

### class transformers. DistilBertTokenizer

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/tokenization_distilbert.py#L23)
( *args do_lower_case : bool = True **kwargs )

## DistilBertModel

### class transformers. DistilBertModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L322)
( config : PreTrainedConfig )
Parameters
- config ( PreTrainedConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The bare Distilbert Model outputting raw hidden-states without any specific head on top.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L386)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.BaseModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, num_choices) ) —
Indices of input sequence tokens in the vocabulary. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
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
- inputs_embeds ( torch.FloatTensor of shape (batch_size, num_choices, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
Returns
transformers.modeling_outputs.BaseModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput)
A transformers.modeling_outputs.BaseModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs. last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model. hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.BaseModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs.
[LINK: transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput)
[LINK: DistilBertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertConfig)
- last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model.
last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model.
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
The DistilBertModel forward method, overrides the __call__ special method.
[LINK: DistilBertModel](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

## DistilBertForMaskedLM

### class transformers. DistilBertForMaskedLM

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L432)
( config : PreTrainedConfig )
Parameters
- config ( PreTrainedConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
DistilBert Model with a masked language modeling head on top.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L476)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.LongTensor] = None position_ids : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.MaskedLMOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, num_choices) ) —
Indices of input sequence tokens in the vocabulary. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
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
- inputs_embeds ( torch.FloatTensor of shape (batch_size, num_choices, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the masked language modeling loss. Indices should be in [-100, 0, ..., config.vocab_size] (see input_ids docstring) Tokens with indices set to -100 are ignored (masked), the
loss is only computed for the tokens with labels in [0, ..., config.vocab_size] .
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
Returns
transformers.modeling_outputs.MaskedLMOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
A transformers.modeling_outputs.MaskedLMOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Masked language modeling (MLM) loss. logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.MaskedLMOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs.
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
[LINK: DistilBertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Masked language modeling (MLM) loss.
loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Masked language modeling (MLM) loss.
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
The DistilBertForMaskedLM forward method, overrides the __call__ special method.
[LINK: DistilBertForMaskedLM](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertForMaskedLM)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## DistilBertForSequenceClassification

### class transformers. DistilBertForSequenceClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L536)
( config : PreTrainedConfig )
Parameters
- config ( PreTrainedConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
DistilBert Model transformer with a sequence classification/regression head on top (a linear layer on top of the
pooled output) e.g. for GLUE tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L570)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.LongTensor] = None position_ids : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.SequenceClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
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
- inputs_embeds ( torch.Tensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the sequence classification/regression loss. Indices should be in [0, ..., config.num_labels - 1] . If config.num_labels == 1 a regression loss is computed (Mean-Square loss), If config.num_labels > 1 a classification loss is computed (Cross-Entropy).
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
Returns
transformers.modeling_outputs.SequenceClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
A transformers.modeling_outputs.SequenceClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss. logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.SequenceClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs.
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
[LINK: DistilBertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss.
loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss.
- logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax).
logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax).
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
The DistilBertForSequenceClassification forward method, overrides the __call__ special method.
[LINK: DistilBertForSequenceClassification](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertForSequenceClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example of single-label classification:
Example of multi-label classification:

## DistilBertForMultipleChoice

### class transformers. DistilBertForMultipleChoice

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L811)
( config : PreTrainedConfig )
Parameters
- config ( PreTrainedConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Distilbert Model with a multiple choice classification head on top (a linear layer on top of the pooled output and a
softmax) e.g. for RocStories/SWAG tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L843)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.LongTensor] = None position_ids : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.MultipleChoiceModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, num_choices, sequence_length) ) —
Indices of input sequence tokens in the vocabulary. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
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
- inputs_embeds ( torch.FloatTensor of shape (batch_size, num_choices, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the multiple choice classification loss. Indices should be in [0, ..., num_choices-1] where num_choices is the size of the second dimension of the input tensors. (See input_ids above)
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
Returns
transformers.modeling_outputs.MultipleChoiceModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
A transformers.modeling_outputs.MultipleChoiceModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification loss. logits ( torch.FloatTensor of shape (batch_size, num_choices) ) — num_choices is the second dimension of the input tensors. (see input_ids above). Classification scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.MultipleChoiceModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs.
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
[LINK: DistilBertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification loss.
loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification loss.
- logits ( torch.FloatTensor of shape (batch_size, num_choices) ) — num_choices is the second dimension of the input tensors. (see input_ids above). Classification scores (before SoftMax).
logits ( torch.FloatTensor of shape (batch_size, num_choices) ) — num_choices is the second dimension of the input tensors. (see input_ids above).
Classification scores (before SoftMax).
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
The DistilBertForMultipleChoice forward method, overrides the __call__ special method.
[LINK: DistilBertForMultipleChoice](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertForMultipleChoice)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Examples:

## DistilBertForTokenClassification

### class transformers. DistilBertForTokenClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L736)
( config : PreTrainedConfig )
Parameters
- config ( PreTrainedConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Distilbert transformer with a token classification head on top (a linear layer on top of the hidden-states
output) e.g. for Named-Entity-Recognition (NER) tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L768)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.LongTensor] = None position_ids : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
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
- inputs_embeds ( torch.Tensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the token classification loss. Indices should be in [0, ..., config.num_labels - 1] .
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
Returns
transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided)  — Classification loss. logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.num_labels) ) — Classification scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs.
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
[LINK: DistilBertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertConfig)
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
The DistilBertForTokenClassification forward method, overrides the __call__ special method.
[LINK: DistilBertForTokenClassification](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertForTokenClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## DistilBertForQuestionAnswering

### class transformers. DistilBertForQuestionAnswering

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L634)
( config : PreTrainedConfig )
Parameters
- config ( PreTrainedConfig ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Distilbert transformer with a span classification head on top for extractive question-answering tasks like
SQuAD (a linear layer on top of the hidden-states output to compute span start logits and span end logits ).
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/distilbert/modeling_distilbert.py#L668)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None start_positions : typing.Optional[torch.Tensor] = None end_positions : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, num_choices) ) —
Indices of input sequence tokens in the vocabulary. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
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
- inputs_embeds ( torch.FloatTensor of shape (batch_size, num_choices, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- start_positions ( torch.Tensor of shape (batch_size,) , optional ) —
Labels for position (index) of the start of the labelled span for computing the token classification loss.
Positions are clamped to the length of the sequence ( sequence_length ). Position outside of the sequence
are not taken into account for computing the loss.
- end_positions ( torch.Tensor of shape (batch_size,) , optional ) —
Labels for position (index) of the end of the labelled span for computing the token classification loss.
Positions are clamped to the length of the sequence ( sequence_length ). Position outside of the sequence
are not taken into account for computing the loss.
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
Returns
transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Total span extraction loss is the sum of a Cross-Entropy for the start and end positions. start_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-start scores (before SoftMax). end_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-end scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( DistilBertConfig ) and inputs.
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
[LINK: DistilBertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertConfig)
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
The DistilBertForQuestionAnswering forward method, overrides the __call__ special method.
[LINK: DistilBertForQuestionAnswering](/docs/transformers/v5.0.0rc2/en/model_doc/distilbert#transformers.DistilBertForQuestionAnswering)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:
[LINK: Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/distilbert.md)
[LINK: ← DiffLlama](/docs/transformers/en/model_doc/diffllama)
[LINK: Doge →](/docs/transformers/en/model_doc/doge)

--------------------