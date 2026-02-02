# XLM-RoBERTa
**URL:** https://huggingface.co/docs/transformers/model_doc/xlm-roberta
**Page Title:** XLM-RoBERTa
--------------------

Transformers documentation
XLM-RoBERTa

## Transformers

[LINK: 155,740](https://github.com/huggingface/transformers)
and get access to the augmented documentation experience
to get started
This model was released on 2019-11-05 and added to Hugging Face Transformers on 2020-11-16.

## XLM-RoBERTa

XLM-RoBERTa is a large multilingual masked language model trained on 2.5TB of filtered CommonCrawl data across 100 languages. It shows that scaling the model provides strong performance gains on high-resource and low-resource languages. The model uses the RoBERTa pretraining objectives on the XLM model.
You can find all the original XLM-RoBERTa checkpoints under the Facebook AI community organization.
Click on the XLM-RoBERTa models in the right sidebar for more examples of how to apply XLM-RoBERTa to different cross-lingual tasks like classification, translation, and question answering.
The example below demonstrates how to predict the <mask> token with Pipeline , AutoModel , and from the command line.
[LINK: Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline)
[LINK: AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel)
Quantization reduces the memory burden of large models by representing the weights in a lower precision. Refer to the quantization guide overview for more available quantization backends.
The example below uses bitsandbytes the quantive the weights to 4 bits

## Notes

- Unlike some XLM models, XLM-RoBERTa doesn’t require lang tensors to understand what language is being used. It automatically determines the language from the input IDs

## Resources

A list of official Hugging Face and community (indicated by 🌎) resources to help you get started with XLM-RoBERTa. If you’re interested in submitting a resource to be included here, please feel free to open a Pull Request and we’ll review it! The resource should ideally demonstrate something new instead of duplicating an existing resource.
- A blog post on how to finetune XLM RoBERTa for multiclass classification with Habana Gaudi on AWS
- XLMRobertaForSequenceClassification is supported by this example script and notebook ..
[LINK: XLMRobertaForSequenceClassification](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForSequenceClassification)
[LINK: example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/text-classification)
[LINK: notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification.ipynb)
- Text classification chapter of the 🤗 Hugging Face Task Guides.
[LINK: Text classification](https://huggingface.co/docs/transformers/tasks/sequence_classification)
- Text classification task guide
- XLMRobertaForTokenClassification is supported by this example script and notebook .
[LINK: XLMRobertaForTokenClassification](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForTokenClassification)
[LINK: example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/token-classification)
[LINK: notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/token_classification.ipynb)
- Token classification chapter of the 🤗 Hugging Face Course.
- Token classification task guide
- XLMRobertaForCausalLM is supported by this example script and notebook .
[LINK: XLMRobertaForCausalLM](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForCausalLM)
[LINK: example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/language-modeling)
[LINK: notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/language_modeling.ipynb)
- Causal language modeling chapter of the 🤗 Hugging Face Task Guides.
[LINK: Causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)
- Causal language modeling task guide
- XLMRobertaForMaskedLM is supported by this example script and notebook .
[LINK: XLMRobertaForMaskedLM](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForMaskedLM)
[LINK: example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/language-modeling#robertabertdistilbert-and-masked-language-modeling)
[LINK: notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/language_modeling.ipynb)
- Masked language modeling chapter of the 🤗 Hugging Face Course.
- Masked language modeling
- XLMRobertaForQuestionAnswering is supported by this example script and notebook .
[LINK: XLMRobertaForQuestionAnswering](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForQuestionAnswering)
[LINK: example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/question-answering)
[LINK: notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/question_answering.ipynb)
- Question answering chapter of the 🤗 Hugging Face Course.
- Question answering task guide
Multiple choice
- XLMRobertaForMultipleChoice is supported by this example script and notebook .
[LINK: XLMRobertaForMultipleChoice](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForMultipleChoice)
[LINK: example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/multiple-choice)
[LINK: notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/multiple_choice.ipynb)
- Multiple choice task guide
🚀 Deploy
- A blog post on how to Deploy Serverless XLM RoBERTa on AWS Lambda .
This implementation is the same as RoBERTa. Refer to the documentation of RoBERTa for usage examples as well as the information relative to the inputs and outputs.

## XLMRobertaConfig

### class transformers. XLMRobertaConfig

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/configuration_xlm_roberta.py#L24)
( vocab_size = 30522 hidden_size = 768 num_hidden_layers = 12 num_attention_heads = 12 intermediate_size = 3072 hidden_act = 'gelu' hidden_dropout_prob = 0.1 attention_probs_dropout_prob = 0.1 max_position_embeddings = 512 type_vocab_size = 2 initializer_range = 0.02 layer_norm_eps = 1e-12 pad_token_id = 1 bos_token_id = 0 eos_token_id = 2 use_cache = True classifier_dropout = None is_decoder = False add_cross_attention = False tie_word_embeddings = True **kwargs )
Parameters
- vocab_size ( int , optional , defaults to 30522) —
Vocabulary size of the XLM-RoBERTa model. Defines the number of different tokens that can be represented by
the inputs_ids passed when calling XLMRobertaModel .
[LINK: XLMRobertaModel](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaModel)
- hidden_size ( int , optional , defaults to 768) —
Dimensionality of the encoder layers and the pooler layer.
- num_hidden_layers ( int , optional , defaults to 12) —
Number of hidden layers in the Transformer encoder.
- num_attention_heads ( int , optional , defaults to 12) —
Number of attention heads for each attention layer in the Transformer encoder.
- intermediate_size ( int , optional , defaults to 3072) —
Dimensionality of the “intermediate” (often named feed-forward) layer in the Transformer encoder.
- hidden_act ( str or Callable , optional , defaults to "gelu" ) —
The non-linear activation function (function or string) in the encoder and pooler. If string, "gelu" , "relu" , "silu" and "gelu_new" are supported.
- hidden_dropout_prob ( float , optional , defaults to 0.1) —
The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
- attention_probs_dropout_prob ( float , optional , defaults to 0.1) —
The dropout ratio for the attention probabilities.
- max_position_embeddings ( int , optional , defaults to 512) —
The maximum sequence length that this model might ever be used with. Typically set this to something large
just in case (e.g., 512 or 1024 or 2048).
- type_vocab_size ( int , optional , defaults to 2) —
The vocabulary size of the token_type_ids passed when calling XLMRobertaModel .
[LINK: XLMRobertaModel](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaModel)
- initializer_range ( float , optional , defaults to 0.02) —
The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
- layer_norm_eps ( float , optional , defaults to 1e-12) —
The epsilon used by the layer normalization layers.
- is_decoder ( bool , optional , defaults to False ) —
Whether the model is used as a decoder or not. If False , the model is used as an encoder.
- use_cache ( bool , optional , defaults to True ) —
Whether or not the model should return the last key/values attentions (not used by all models). Only
relevant if config.is_decoder=True .
- classifier_dropout ( float , optional ) —
The dropout ratio for the classification head.
This is the configuration class to store the configuration of a XLMRobertaModel . It
is used to instantiate a XLM-RoBERTa model according to the specified arguments, defining the model architecture.
Instantiating a configuration with the defaults will yield a similar configuration to that of the XLMRoBERTa FacebookAI/xlm-roberta-base architecture.
[LINK: XLMRobertaModel](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaModel)
Configuration objects inherit from PreTrainedConfig and can be used to control the model outputs. Read the
documentation from PreTrainedConfig for more information.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig)
Examples:

## XLMRobertaTokenizer

### class transformers. XLMRobertaTokenizer

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py#L28)
( vocab : str | list[tuple[str, float]] | None = None add_prefix_space : bool = True bos_token : str = '<s>' eos_token : str = '</s>' sep_token : str = '</s>' cls_token : str = '<s>' unk_token : str = '<unk>' pad_token : str = '<pad>' mask_token : str = '<mask>' **kwargs )
Parameters
- vocab_file ( str , optional) — Path to the vocabulary file.
- merges_file ( str , optional) — Path to the merges file.
- tokenizer_file ( str , optional) — Path to a tokenizers JSON file containing the serialization of a tokenizer.
- bos_token ( str , optional, defaults to "<s>" ) — The beginning of sequence token.
- eos_token ( str , optional, defaults to "</s>" ) — The end of sequence token.
- sep_token ( str , optional, defaults to "</s>" ) — The separator token.
- cls_token ( str , optional, defaults to "<s>" ) — The classifier token.
- unk_token ( str , optional, defaults to "<unk>" ) — The unknown token.
- pad_token ( str , optional, defaults to "<pad>" ) — The padding token.
- mask_token ( str , optional, defaults to "<mask>" ) — The mask token.
- add_prefix_space ( bool , optional, defaults to True ) — Whether to add an initial space.
- vocab ( str , dict or list , optional) — Custom vocabulary dictionary.
Construct an XLM-RoBERTa tokenizer (backed by HuggingFace’s tokenizers library). Based on SentencePiece.
This tokenizer inherits from TokenizersBackend which contains most of the main methods. Users should refer to
this superclass for more information regarding those methods.
[LINK: TokenizersBackend](/docs/transformers/v5.0.0/en/main_classes/tokenizer#transformers.TokenizersBackend)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/tokenization_utils_base.py#L1330)
( token_ids_0 : list[int] token_ids_1 : list[int] | None = None already_has_special_tokens : bool = False ) → A list of integers in the range [0, 1]
Parameters
- token_ids_0 — List of IDs for the (possibly already formatted) sequence.
- token_ids_1 — Unused when already_has_special_tokens=True . Must be None in that case.
- already_has_special_tokens — Whether the sequence is already formatted with special tokens.
Returns
A list of integers in the range [0, 1]
1 for a special token, 0 for a sequence token.
1 for a special token, 0 for a sequence token.
Retrieve sequence ids from a token list that has no special tokens added.
For fast tokenizers, data collators call this with already_has_special_tokens=True to build a mask over an
already-formatted sequence. In that case, we compute the mask by checking membership in all_special_ids .
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/tokenization_utils_tokenizers.py#L408)
( save_directory : str filename_prefix : str | None = None )

## XLMRobertaTokenizerFast

### class transformers. XLMRobertaTokenizer

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py#L28)
( vocab : str | list[tuple[str, float]] | None = None add_prefix_space : bool = True bos_token : str = '<s>' eos_token : str = '</s>' sep_token : str = '</s>' cls_token : str = '<s>' unk_token : str = '<unk>' pad_token : str = '<pad>' mask_token : str = '<mask>' **kwargs )
Parameters
- vocab_file ( str , optional) — Path to the vocabulary file.
- merges_file ( str , optional) — Path to the merges file.
- tokenizer_file ( str , optional) — Path to a tokenizers JSON file containing the serialization of a tokenizer.
- bos_token ( str , optional, defaults to "<s>" ) — The beginning of sequence token.
- eos_token ( str , optional, defaults to "</s>" ) — The end of sequence token.
- sep_token ( str , optional, defaults to "</s>" ) — The separator token.
- cls_token ( str , optional, defaults to "<s>" ) — The classifier token.
- unk_token ( str , optional, defaults to "<unk>" ) — The unknown token.
- pad_token ( str , optional, defaults to "<pad>" ) — The padding token.
- mask_token ( str , optional, defaults to "<mask>" ) — The mask token.
- add_prefix_space ( bool , optional, defaults to True ) — Whether to add an initial space.
- vocab ( str , dict or list , optional) — Custom vocabulary dictionary.
Construct an XLM-RoBERTa tokenizer (backed by HuggingFace’s tokenizers library). Based on SentencePiece.
This tokenizer inherits from TokenizersBackend which contains most of the main methods. Users should refer to
this superclass for more information regarding those methods.
[LINK: TokenizersBackend](/docs/transformers/v5.0.0/en/main_classes/tokenizer#transformers.TokenizersBackend)

## XLMRobertaModel

### class transformers. XLMRobertaModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L579)
( config add_pooling_layer = True )
Parameters
- config ( XLMRobertaModel ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: XLMRobertaModel](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaModel)
[LINK: from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
- add_pooling_layer ( bool , optional , defaults to True ) —
Whether to add a pooling layer
The bare Xlm Roberta Model outputting raw hidden-states without any specific head on top.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L605)
( input_ids : torch.Tensor | None = None attention_mask : torch.Tensor | None = None token_type_ids : torch.Tensor | None = None position_ids : torch.Tensor | None = None inputs_embeds : torch.Tensor | None = None encoder_hidden_states : torch.Tensor | None = None encoder_attention_mask : torch.Tensor | None = None past_key_values : transformers.cache_utils.Cache | None = None use_cache : bool | None = None cache_position : torch.Tensor | None = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions)
Parameters
- input_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- token_type_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0, 1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
What are token type IDs?
- position_ids ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- inputs_embeds ( torch.Tensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- encoder_hidden_states ( torch.Tensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
if the model is configured as a decoder.
- encoder_attention_mask ( torch.Tensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
the cross-attention if the model is configured as a decoder. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked .
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
- past_key_values ( ~cache_utils.Cache , optional ) —
Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
blocks) that can be used to speed up sequential decoding. This typically consists in the past_key_values returned by the model at a previous stage of decoding, when use_cache=True or config.use_cache=True . Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default. The model will output the same cache format that is fed as input. If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default.
[LINK: Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
[LINK: DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache)
The model will output the same cache format that is fed as input.
If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
- use_cache ( bool , optional ) —
If set to True , past_key_values key value states are returned and can be used to speed up decoding (see past_key_values ).
- cache_position ( torch.Tensor of shape (sequence_length) , optional ) —
Indices depicting the position of the input sequence tokens in the sequence. Contrarily to position_ids ,
this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
the complete sequence length.
Returns
transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions)
A transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs. last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model. pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining. hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads. cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True and config.add_cross_attention=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the
weighted average in the cross-attention heads. past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
A transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs.
[LINK: transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions)
[LINK: XLMRobertaConfig](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaConfig)
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
- cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True and config.add_cross_attention=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the
weighted average in the cross-attention heads.
cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True and config.add_cross_attention=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) .
Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the
weighted average in the cross-attention heads.
- past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide .
[LINK: Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
The XLMRobertaModel forward method, overrides the __call__ special method.
[LINK: XLMRobertaModel](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

## XLMRobertaForCausalLM

### class transformers. XLMRobertaForCausalLM

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L724)
( config )
Parameters
- config ( XLMRobertaForCausalLM ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: XLMRobertaForCausalLM](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForCausalLM)
[LINK: from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
XLM-RoBERTa Model with a language modeling head on top for CLM fine-tuning.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L747)
( input_ids : torch.LongTensor | None = None attention_mask : torch.FloatTensor | None = None token_type_ids : torch.LongTensor | None = None position_ids : torch.LongTensor | None = None inputs_embeds : torch.FloatTensor | None = None encoder_hidden_states : torch.FloatTensor | None = None encoder_attention_mask : torch.FloatTensor | None = None labels : torch.LongTensor | None = None past_key_values : tuple[tuple[torch.FloatTensor]] | None = None use_cache : bool | None = None logits_to_keep : int | torch.Tensor = 0 **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- token_type_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0,1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size.
= 2. All the value in this tensor should be always < type_vocab_size.
What are token type IDs?
- position_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- inputs_embeds ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- encoder_hidden_states ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
if the model is configured as a decoder.
- encoder_attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
the cross-attention if the model is configured as a decoder. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked .
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the left-to-right language modeling loss (next word prediction). Indices should be in [-100, 0, ..., config.vocab_size] (see input_ids docstring) Tokens with indices set to -100 are
ignored (masked), the loss is only computed for the tokens with labels in [0, ..., config.vocab_size]
- past_key_values ( tuple , optional ) —
Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
blocks) that can be used to speed up sequential decoding. This typically consists in the past_key_values returned by the model at a previous stage of decoding, when use_cache=True or config.use_cache=True . Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default. The model will output the same cache format that is fed as input. If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
Only Cache instance is allowed as input, see our kv cache guide .
If no past_key_values are passed, DynamicCache will be initialized by default.
[LINK: Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
[LINK: DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache)
The model will output the same cache format that is fed as input.
If past_key_values are used, the user is expected to input only unprocessed input_ids (those that don’t
have their past key value states given to this model) of shape (batch_size, unprocessed_length) instead of all input_ids of shape (batch_size, sequence_length) .
- use_cache ( bool , optional ) —
If set to True , past_key_values key value states are returned and can be used to speed up decoding (see past_key_values ).
- logits_to_keep ( Union[int, torch.Tensor] , optional , defaults to 0 ) —
If an int , compute logits for the last logits_to_keep tokens. If 0 , calculate logits for all input_ids (special case). Only last token logits are needed for generation, and calculating them only for that
token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
If a torch.Tensor , must be 1D corresponding to the indices to keep in the sequence length dimension.
This is useful when using packed tensor format (single dimension for batch and sequence length).
Returns
transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
A transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Language modeling loss (for next-token prediction). logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads. cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Cross attentions weights after the attention softmax, used to compute the weighted average in the
cross-attention heads. past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
A transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs.
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
[LINK: XLMRobertaConfig](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaConfig)
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
[LINK: Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
Contains pre-computed hidden-states (key and values in the attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
The XLMRobertaForCausalLM forward method, overrides the __call__ special method.
[LINK: XLMRobertaForCausalLM](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForCausalLM)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## XLMRobertaForMaskedLM

### class transformers. XLMRobertaForMaskedLM

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L832)
( config )
Parameters
- config ( XLMRobertaForMaskedLM ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: XLMRobertaForMaskedLM](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForMaskedLM)
[LINK: from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Xlm Roberta Model with a language modeling head on top.”
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L859)
( input_ids : torch.LongTensor | None = None attention_mask : torch.FloatTensor | None = None token_type_ids : torch.LongTensor | None = None position_ids : torch.LongTensor | None = None inputs_embeds : torch.FloatTensor | None = None encoder_hidden_states : torch.FloatTensor | None = None encoder_attention_mask : torch.FloatTensor | None = None labels : torch.LongTensor | None = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.MaskedLMOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- token_type_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0,1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size.
= 2. All the value in this tensor should be always < type_vocab_size.
What are token type IDs?
- position_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- inputs_embeds ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- encoder_hidden_states ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
if the model is configured as a decoder.
- encoder_attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
the cross-attention if the model is configured as a decoder. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked .
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the masked language modeling loss. Indices should be in [-100, 0, ..., config.vocab_size] (see input_ids docstring) Tokens with indices set to -100 are ignored (masked), the
loss is only computed for the tokens with labels in [0, ..., config.vocab_size]
Returns
transformers.modeling_outputs.MaskedLMOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
A transformers.modeling_outputs.MaskedLMOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Masked language modeling (MLM) loss. logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.MaskedLMOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs.
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
[LINK: XLMRobertaConfig](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaConfig)
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
The XLMRobertaForMaskedLM forward method, overrides the __call__ special method.
[LINK: XLMRobertaForMaskedLM](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForMaskedLM)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## XLMRobertaForSequenceClassification

### class transformers. XLMRobertaForSequenceClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L945)
( config )
Parameters
- config ( XLMRobertaForSequenceClassification ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: XLMRobertaForSequenceClassification](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForSequenceClassification)
[LINK: from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
XLM-RoBERTa Model transformer with a sequence classification/regression head on top (a linear layer on top of the
pooled output) e.g. for GLUE tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L957)
( input_ids : torch.LongTensor | None = None attention_mask : torch.FloatTensor | None = None token_type_ids : torch.LongTensor | None = None position_ids : torch.LongTensor | None = None inputs_embeds : torch.FloatTensor | None = None labels : torch.LongTensor | None = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.SequenceClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- token_type_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0,1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size.
= 2. All the value in this tensor should be always < type_vocab_size.
What are token type IDs?
- position_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- inputs_embeds ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the sequence classification/regression loss. Indices should be in [0, ..., config.num_labels - 1] . If config.num_labels == 1 a regression loss is computed (Mean-Square loss), If config.num_labels > 1 a classification loss is computed (Cross-Entropy).
Returns
transformers.modeling_outputs.SequenceClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
A transformers.modeling_outputs.SequenceClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss. logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.SequenceClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs.
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
[LINK: XLMRobertaConfig](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaConfig)
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
The XLMRobertaForSequenceClassification forward method, overrides the __call__ special method.
[LINK: XLMRobertaForSequenceClassification](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForSequenceClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example of single-label classification:
Example of multi-label classification:

## XLMRobertaForMultipleChoice

### class transformers. XLMRobertaForMultipleChoice

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L1030)
( config )
Parameters
- config ( XLMRobertaForMultipleChoice ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: XLMRobertaForMultipleChoice](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForMultipleChoice)
[LINK: from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Xlm Roberta Model with a multiple choice classification head on top (a linear layer on top of the pooled output and a
softmax) e.g. for RocStories/SWAG tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L1041)
( input_ids : torch.LongTensor | None = None token_type_ids : torch.LongTensor | None = None attention_mask : torch.FloatTensor | None = None labels : torch.LongTensor | None = None position_ids : torch.LongTensor | None = None inputs_embeds : torch.FloatTensor | None = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.MultipleChoiceModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, num_choices, sequence_length) ) —
Indices of input sequence tokens in the vocabulary. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- token_type_ids ( torch.LongTensor of shape (batch_size, num_choices, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0,1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size.
= 2. All the value in this tensor should be always < type_vocab_size.
What are token type IDs?
- attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the multiple choice classification loss. Indices should be in [0, ..., num_choices-1] where num_choices is the size of the second dimension of the input tensors. (See input_ids above)
- position_ids ( torch.LongTensor of shape (batch_size, num_choices, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.max_position_embeddings - 1] . What are position IDs?
What are position IDs?
- inputs_embeds ( torch.FloatTensor of shape (batch_size, num_choices, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
Returns
transformers.modeling_outputs.MultipleChoiceModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
A transformers.modeling_outputs.MultipleChoiceModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification loss. logits ( torch.FloatTensor of shape (batch_size, num_choices) ) — num_choices is the second dimension of the input tensors. (see input_ids above). Classification scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.MultipleChoiceModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs.
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
[LINK: XLMRobertaConfig](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaConfig)
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
The XLMRobertaForMultipleChoice forward method, overrides the __call__ special method.
[LINK: XLMRobertaForMultipleChoice](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForMultipleChoice)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## XLMRobertaForTokenClassification

### class transformers. XLMRobertaForTokenClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L1127)
( config )
Parameters
- config ( XLMRobertaForTokenClassification ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: XLMRobertaForTokenClassification](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForTokenClassification)
[LINK: from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Xlm Roberta transformer with a token classification head on top (a linear layer on top of the hidden-states
output) e.g. for Named-Entity-Recognition (NER) tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L1142)
( input_ids : torch.LongTensor | None = None attention_mask : torch.FloatTensor | None = None token_type_ids : torch.LongTensor | None = None position_ids : torch.LongTensor | None = None inputs_embeds : torch.FloatTensor | None = None labels : torch.LongTensor | None = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- token_type_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0,1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size.
= 2. All the value in this tensor should be always < type_vocab_size.
What are token type IDs?
- position_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
- inputs_embeds ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the token classification loss. Indices should be in [0, ..., config.num_labels - 1] .
Returns
transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided)  — Classification loss. logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.num_labels) ) — Classification scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs.
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
[LINK: XLMRobertaConfig](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaConfig)
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
The XLMRobertaForTokenClassification forward method, overrides the __call__ special method.
[LINK: XLMRobertaForTokenClassification](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForTokenClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## XLMRobertaForQuestionAnswering

### class transformers. XLMRobertaForQuestionAnswering

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L1198)
( config )
Parameters
- config ( XLMRobertaForQuestionAnswering ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: XLMRobertaForQuestionAnswering](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForQuestionAnswering)
[LINK: from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Xlm Roberta transformer with a span classification head on top for extractive question-answering tasks like
SQuAD (a linear layer on top of the hidden-states output to compute span start logits and span end logits ).
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py#L1209)
( input_ids : torch.LongTensor | None = None attention_mask : torch.FloatTensor | None = None token_type_ids : torch.LongTensor | None = None position_ids : torch.LongTensor | None = None inputs_embeds : torch.FloatTensor | None = None start_positions : torch.LongTensor | None = None end_positions : torch.LongTensor | None = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
Parameters
- input_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of input sequence tokens in the vocabulary. Padding will be ignored by default. Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details. What are input IDs?
Indices can be obtained using AutoTokenizer . See PreTrainedTokenizer.encode() and PreTrainedTokenizer. call () for details.
[LINK: AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer)
[LINK: PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode)
[LINK: PreTrainedTokenizer. call ()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__)
What are input IDs?
- attention_mask ( torch.FloatTensor of shape (batch_size, sequence_length) , optional ) —
Mask to avoid performing attention on padding token indices. Mask values selected in [0, 1] : 1 for tokens that are not masked , 0 for tokens that are masked . What are attention masks?
- 1 for tokens that are not masked ,
- 0 for tokens that are masked .
What are attention masks?
- token_type_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0,1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
This parameter can only be used when the model is initialized with type_vocab_size parameter with value = 2. All the value in this tensor should be always < type_vocab_size.
= 2. All the value in this tensor should be always < type_vocab_size.
What are token type IDs?
- position_ids ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.n_positions - 1] . What are position IDs?
What are position IDs?
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
Returns
transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Total span extraction loss is the sum of a Cross-Entropy for the start and end positions. start_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-start scores (before SoftMax). end_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-end scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( XLMRobertaConfig ) and inputs.
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
[LINK: XLMRobertaConfig](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaConfig)
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
The XLMRobertaForQuestionAnswering forward method, overrides the __call__ special method.
[LINK: XLMRobertaForQuestionAnswering](/docs/transformers/v5.0.0/en/model_doc/xlm-roberta#transformers.XLMRobertaForQuestionAnswering)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:
[LINK: Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/xlm-roberta.md)
[LINK: ← XLM](/docs/transformers/model_doc/xlm)
[LINK: XLM-RoBERTa-XL →](/docs/transformers/model_doc/xlm-roberta-xl)

--------------------