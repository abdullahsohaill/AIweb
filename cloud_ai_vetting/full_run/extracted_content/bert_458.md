# BERT
**URL:** https://huggingface.co/docs/transformers/model_doc/bert
**Page Title:** BERT
--------------------

Transformers documentation
BERT

## Transformers

[LINK: 155,712](https://github.com/huggingface/transformers)
and get access to the augmented documentation experience
to get started
This model was released on 2018-10-11 and added to Hugging Face Transformers on 2020-11-16.

## BERT

BERT is a bidirectional transformer pretrained on unlabeled text to predict masked tokens in a sentence and to predict whether one sentence follows another. The main idea is that by randomly masking some tokens, the model can train on text to the left and right, giving it a more thorough understanding. BERT is also very versatile because its learned language representations can be adapted for other NLP tasks by fine-tuning an additional layer or head.
You can find all the original BERT checkpoints under the BERT collection.
Click on the BERT models in the right sidebar for more examples of how to apply BERT to different language tasks.
The example below demonstrates how to predict the [MASK] token with Pipeline , AutoModel , and from the command line.
[LINK: Pipeline](/docs/transformers/v5.0.0rc2/en/main_classes/pipelines#transformers.Pipeline)
[LINK: AutoModel](/docs/transformers/v5.0.0rc2/en/model_doc/auto#transformers.AutoModel)

## Notes

- Inputs should be padded on the right because BERT uses absolute position embeddings.

## BertConfig

### class transformers. BertConfig

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/configuration_bert.py#L25)
( vocab_size = 30522 hidden_size = 768 num_hidden_layers = 12 num_attention_heads = 12 intermediate_size = 3072 hidden_act = 'gelu' hidden_dropout_prob = 0.1 attention_probs_dropout_prob = 0.1 max_position_embeddings = 512 type_vocab_size = 2 initializer_range = 0.02 layer_norm_eps = 1e-12 pad_token_id = 0 use_cache = True classifier_dropout = None **kwargs )
Parameters
- vocab_size ( int , optional , defaults to 30522) —
Vocabulary size of the BERT model. Defines the number of different tokens that can be represented by the inputs_ids passed when calling BertModel .
[LINK: BertModel](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertModel)
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
The vocabulary size of the token_type_ids passed when calling BertModel .
[LINK: BertModel](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertModel)
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
This is the configuration class to store the configuration of a BertModel . It is used to
instantiate a BERT model according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the BERT google-bert/bert-base-uncased architecture.
[LINK: BertModel](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertModel)
Configuration objects inherit from PreTrainedConfig and can be used to control the model outputs. Read the
documentation from PreTrainedConfig for more information.
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
[LINK: PreTrainedConfig](/docs/transformers/v5.0.0rc2/en/main_classes/configuration#transformers.PreTrainedConfig)
Examples:

## BertTokenizer

### class transformers. BertTokenizer

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/tokenization_bert.py#L43)
( vocab : typing.Union[str, dict[str, int], NoneType] = None do_lower_case : bool = False unk_token : str = '[UNK]' sep_token : str = '[SEP]' pad_token : str = '[PAD]' cls_token : str = '[CLS]' mask_token : str = '[MASK]' tokenize_chinese_chars : bool = True strip_accents : typing.Optional[bool] = None **kwargs )
Parameters
- vocab ( str or dict[str, int] , optional ) —
Custom vocabulary dictionary. If not provided, vocabulary is loaded from vocab_file .
- do_lower_case ( bool , optional , defaults to False ) —
Whether or not to lowercase the input when tokenizing.
- unk_token ( str , optional , defaults to "[UNK]" ) —
The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
token instead.
- sep_token ( str , optional , defaults to "[SEP]" ) —
The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
sequence classification or for a text and a question for question answering. It is also used as the last
token of a sequence built with special tokens.
- pad_token ( str , optional , defaults to "[PAD]" ) —
The token used for padding, for example when batching sequences of different lengths.
- cls_token ( str , optional , defaults to "[CLS]" ) —
The classifier token which is used when doing sequence classification (classification of the whole sequence
instead of per-token classification). It is the first token of the sequence when built with special tokens.
- mask_token ( str , optional , defaults to "[MASK]" ) —
The token used for masking values. This is the token used when training this model with masked language
modeling. This is the token which the model will try to predict.
- tokenize_chinese_chars ( bool , optional , defaults to True ) —
Whether or not to tokenize Chinese characters.
- strip_accents ( bool , optional ) —
Whether or not to strip all accents. If this option is not specified, then it will be determined by the
value for lowercase (as in the original BERT).
Construct a BERT tokenizer (backed by HuggingFace’s tokenizers library). Based on WordPiece.
This tokenizer inherits from TokenizersBackend which contains most of the main methods. Users should refer to
this superclass for more information regarding those methods.
[LINK: TokenizersBackend](/docs/transformers/v5.0.0rc2/en/main_classes/tokenizer#transformers.TokenizersBackend)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/tokenization_utils_base.py#L1335)
( token_ids_0 : list[int] token_ids_1 : Optional[list[int]] = None already_has_special_tokens : bool = False ) → A list of integers in the range [0, 1]
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
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/tokenization_utils_tokenizers.py#L405)
( save_directory : str filename_prefix : typing.Optional[str] = None )

## BertTokenizerLegacy

### class transformers. BertTokenizerLegacy

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/tokenization_bert_legacy.py#L51)
( vocab_file do_lower_case = True do_basic_tokenize = True never_split = None unk_token = '[UNK]' sep_token = '[SEP]' pad_token = '[PAD]' cls_token = '[CLS]' mask_token = '[MASK]' tokenize_chinese_chars = True strip_accents = None clean_up_tokenization_spaces = True **kwargs )
Parameters
- vocab_file ( str ) —
File containing the vocabulary.
- do_lower_case ( bool , optional , defaults to True ) —
Whether or not to lowercase the input when tokenizing.
- do_basic_tokenize ( bool , optional , defaults to True ) —
Whether or not to do basic tokenization before WordPiece.
- never_split ( Iterable , optional ) —
Collection of tokens which will never be split during tokenization. Only has an effect when do_basic_tokenize=True
- unk_token ( str , optional , defaults to "[UNK]" ) —
The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
token instead.
- sep_token ( str , optional , defaults to "[SEP]" ) —
The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
sequence classification or for a text and a question for question answering. It is also used as the last
token of a sequence built with special tokens.
- pad_token ( str , optional , defaults to "[PAD]" ) —
The token used for padding, for example when batching sequences of different lengths.
- cls_token ( str , optional , defaults to "[CLS]" ) —
The classifier token which is used when doing sequence classification (classification of the whole sequence
instead of per-token classification). It is the first token of the sequence when built with special tokens.
- mask_token ( str , optional , defaults to "[MASK]" ) —
The token used for masking values. This is the token used when training this model with masked language
modeling. This is the token which the model will try to predict.
- tokenize_chinese_chars ( bool , optional , defaults to True ) —
Whether or not to tokenize Chinese characters. This should likely be deactivated for Japanese (see this issue ).
This should likely be deactivated for Japanese (see this issue ).
[LINK: issue](https://github.com/huggingface/transformers/issues/328)
- strip_accents ( bool , optional ) —
Whether or not to strip all accents. If this option is not specified, then it will be determined by the
value for lowercase (as in the original BERT).
- clean_up_tokenization_spaces ( bool , optional , defaults to True ) —
Whether or not to cleanup spaces after decoding, cleanup consists in removing potential artifacts like
extra spaces.
Construct a BERT tokenizer. Based on WordPiece.
This tokenizer inherits from PreTrainedTokenizer which contains most of the main methods. Users should refer to
this superclass for more information regarding those methods.
[LINK: PreTrainedTokenizer](/docs/transformers/v5.0.0rc2/en/main_classes/tokenizer#transformers.PythonBackend)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/tokenization_bert_legacy.py#L186)
( token_ids_0 : list token_ids_1 : typing.Optional[list[int]] = None ) → List[int]
Parameters
- token_ids_0 ( List[int] ) —
List of IDs to which the special tokens will be added.
- token_ids_1 ( List[int] , optional ) —
Optional second list of IDs for sequence pairs.
Returns
List[int]
List of input IDs with the appropriate special tokens.
List of input IDs with the appropriate special tokens.
Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
adding special tokens. A BERT sequence has the following format:
- single sequence: [CLS] X [SEP]
- pair of sequences: [CLS] A [SEP] B [SEP]
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/tokenization_bert_legacy.py#L181)
( tokens )
Converts a sequence of tokens (string) in a single string.
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/tokenization_bert_legacy.py#L211)
( token_ids_0 : list token_ids_1 : typing.Optional[list[int]] = None already_has_special_tokens : bool = False ) → List[int]
Parameters
- token_ids_0 ( List[int] ) —
List of IDs.
- token_ids_1 ( List[int] , optional ) —
Optional second list of IDs for sequence pairs.
- already_has_special_tokens ( bool , optional , defaults to False ) —
Whether or not the token list is already formatted with special tokens for the model.
Returns
List[int]
A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
Retrieve sequence ids from a token list that has no special tokens added. This method is called when adding
special tokens using the tokenizer prepare_for_model method.

## BertTokenizerFast

### class transformers. BertTokenizer

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/tokenization_bert.py#L43)
( vocab : typing.Union[str, dict[str, int], NoneType] = None do_lower_case : bool = False unk_token : str = '[UNK]' sep_token : str = '[SEP]' pad_token : str = '[PAD]' cls_token : str = '[CLS]' mask_token : str = '[MASK]' tokenize_chinese_chars : bool = True strip_accents : typing.Optional[bool] = None **kwargs )
Parameters
- vocab ( str or dict[str, int] , optional ) —
Custom vocabulary dictionary. If not provided, vocabulary is loaded from vocab_file .
- do_lower_case ( bool , optional , defaults to False ) —
Whether or not to lowercase the input when tokenizing.
- unk_token ( str , optional , defaults to "[UNK]" ) —
The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
token instead.
- sep_token ( str , optional , defaults to "[SEP]" ) —
The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
sequence classification or for a text and a question for question answering. It is also used as the last
token of a sequence built with special tokens.
- pad_token ( str , optional , defaults to "[PAD]" ) —
The token used for padding, for example when batching sequences of different lengths.
- cls_token ( str , optional , defaults to "[CLS]" ) —
The classifier token which is used when doing sequence classification (classification of the whole sequence
instead of per-token classification). It is the first token of the sequence when built with special tokens.
- mask_token ( str , optional , defaults to "[MASK]" ) —
The token used for masking values. This is the token used when training this model with masked language
modeling. This is the token which the model will try to predict.
- tokenize_chinese_chars ( bool , optional , defaults to True ) —
Whether or not to tokenize Chinese characters.
- strip_accents ( bool , optional ) —
Whether or not to strip all accents. If this option is not specified, then it will be determined by the
value for lowercase (as in the original BERT).
Construct a BERT tokenizer (backed by HuggingFace’s tokenizers library). Based on WordPiece.
This tokenizer inherits from TokenizersBackend which contains most of the main methods. Users should refer to
this superclass for more information regarding those methods.
[LINK: TokenizersBackend](/docs/transformers/v5.0.0rc2/en/main_classes/tokenizer#transformers.TokenizersBackend)

## BertModel

### class transformers. BertModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L614)
( config add_pooling_layer = True )
Parameters
- config ( BertModel ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertModel](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertModel)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
- add_pooling_layer ( bool , optional , defaults to True ) —
Whether to add a pooling layer
The model can behave as an encoder (with only self-attention) as well as a decoder, in which case a layer of
cross-attention is added between the self-attention layers, following the architecture described in Attention is
all you need by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit,
Llion Jones, Aidan N. Gomez, Lukasz Kaiser and Illia Polosukhin.
To behave as an decoder the model needs to be initialized with the is_decoder argument of the configuration set
to True . To be used in a Seq2Seq model, the model needs to initialized with both is_decoder argument and add_cross_attention set to True ; an encoder_hidden_states is then expected as an input to the forward pass.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L640)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None encoder_hidden_states : typing.Optional[torch.Tensor] = None encoder_attention_mask : typing.Optional[torch.Tensor] = None past_key_values : typing.Optional[transformers.cache_utils.Cache] = None use_cache : typing.Optional[bool] = None cache_position : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions)
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
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
[LINK: DynamicCache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.DynamicCache)
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
[LINK: transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions)
A transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. last_hidden_state ( torch.FloatTensor of shape (batch_size, sequence_length, hidden_size) ) — Sequence of hidden-states at the output of the last layer of the model. pooler_output ( torch.FloatTensor of shape (batch_size, hidden_size) ) — Last layer hidden-state of the first token of the sequence (classification token) after further processing
through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
the classification token after processing through a linear layer and a tanh activation function. The linear
layer weights are trained from the next sentence prediction (classification) objective during pretraining. hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads. cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True and config.add_cross_attention=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights of the decoder’s cross-attention layer, after the attention softmax, used to compute the
weighted average in the cross-attention heads. past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
A transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
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
[LINK: Cache](/docs/transformers/v5.0.0rc2/en/internal/generation_utils#transformers.Cache)
[LINK: kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache)
Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if config.is_encoder_decoder=True in the cross-attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
The BertModel forward method, overrides the __call__ special method.
[LINK: BertModel](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

## BertForPreTraining

### class transformers. BertForPreTraining

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L760)
( config )
Parameters
- config ( BertForPreTraining ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertForPreTraining](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForPreTraining)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
Bert Model with two heads on top as done during the pretraining: a masked language modeling head and a next sentence prediction (classification) head.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L782)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None next_sentence_label : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.models.bert.modeling_bert.BertForPreTrainingOutput or tuple(torch.FloatTensor)
[LINK: transformers.models.bert.modeling_bert.BertForPreTrainingOutput](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.models.bert.modeling_bert.BertForPreTrainingOutput)
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
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the masked language modeling loss. Indices should be in [-100, 0, ..., config.vocab_size] (see input_ids docstring) Tokens with indices set to -100 are ignored (masked),
the loss is only computed for the tokens with labels in [0, ..., config.vocab_size]
- next_sentence_label ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the next sequence prediction (classification) loss. Input should be a sequence
pair (see input_ids docstring) Indices should be in [0, 1] : 0 indicates sequence B is a continuation of sequence A, 1 indicates sequence B is a random sequence.
- 0 indicates sequence B is a continuation of sequence A,
- 1 indicates sequence B is a random sequence.
Returns
transformers.models.bert.modeling_bert.BertForPreTrainingOutput or tuple(torch.FloatTensor)
[LINK: transformers.models.bert.modeling_bert.BertForPreTrainingOutput](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.models.bert.modeling_bert.BertForPreTrainingOutput)
A transformers.models.bert.modeling_bert.BertForPreTrainingOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. loss ( *optional* , returned when labels is provided, torch.FloatTensor of shape (1,) ) — Total loss as the sum of the masked language modeling loss and the next sequence prediction
(classification) loss. prediction_logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax). seq_relationship_logits ( torch.FloatTensor of shape (batch_size, 2) ) — Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
before SoftMax). hidden_states ( tuple[torch.FloatTensor] , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple[torch.FloatTensor] , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.models.bert.modeling_bert.BertForPreTrainingOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.models.bert.modeling_bert.BertForPreTrainingOutput](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.models.bert.modeling_bert.BertForPreTrainingOutput)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
- loss ( *optional* , returned when labels is provided, torch.FloatTensor of shape (1,) ) — Total loss as the sum of the masked language modeling loss and the next sequence prediction
(classification) loss.
loss ( *optional* , returned when labels is provided, torch.FloatTensor of shape (1,) ) — Total loss as the sum of the masked language modeling loss and the next sequence prediction
(classification) loss.
- prediction_logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
prediction_logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- seq_relationship_logits ( torch.FloatTensor of shape (batch_size, 2) ) — Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
before SoftMax).
seq_relationship_logits ( torch.FloatTensor of shape (batch_size, 2) ) — Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
before SoftMax).
- hidden_states ( tuple[torch.FloatTensor] , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
hidden_states ( tuple[torch.FloatTensor] , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) .
Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- attentions ( tuple[torch.FloatTensor] , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
attentions ( tuple[torch.FloatTensor] , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) .
Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
The BertForPreTraining forward method, overrides the __call__ special method.
[LINK: BertForPreTraining](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForPreTraining)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BertLMHeadModel

### class transformers. BertLMHeadModel

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L857)
( config )
Parameters
- config ( BertLMHeadModel ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertLMHeadModel](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertLMHeadModel)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
Bert Model with a language modeling head on top for CLM fine-tuning.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L882)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None encoder_hidden_states : typing.Optional[torch.Tensor] = None encoder_attention_mask : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None past_key_values : typing.Optional[transformers.cache_utils.Cache] = None use_cache : typing.Optional[bool] = None cache_position : typing.Optional[torch.Tensor] = None logits_to_keep : typing.Union[int, torch.Tensor] = 0 **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
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
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the left-to-right language modeling loss (next word prediction). Indices should be in [-100, 0, ..., config.vocab_size] (see input_ids docstring) Tokens with indices set to -100 are
ignored (masked), the loss is only computed for the tokens with labels n [0, ..., config.vocab_size]
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
- use_cache ( bool , optional ) —
If set to True , past_key_values key value states are returned and can be used to speed up decoding (see past_key_values ).
- cache_position ( torch.Tensor of shape (sequence_length) , optional ) —
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
elements depending on the configuration ( BertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Language modeling loss (for next-token prediction). logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads. cross_attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Cross attentions weights after the attention softmax, used to compute the weighted average in the
cross-attention heads. past_key_values ( Cache , optional , returned when use_cache=True is passed or when config.use_cache=True ) — It is a Cache instance. For more details, see our kv cache guide . Contains pre-computed hidden-states (key and values in the attention blocks) that can be used (see past_key_values input) to speed up sequential decoding.
A transformers.modeling_outputs.CausalLMOutputWithCrossAttentions or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.CausalLMOutputWithCrossAttentions](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithCrossAttentions)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
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
The BertLMHeadModel forward method, overrides the __call__ special method.
[LINK: BertLMHeadModel](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertLMHeadModel)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BertForMaskedLM

### class transformers. BertForMaskedLM

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L944)
( config )
Parameters
- config ( BertForMaskedLM ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertForMaskedLM](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForMaskedLM)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bert Model with a language modeling head on top.”
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L972)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None encoder_hidden_states : typing.Optional[torch.Tensor] = None encoder_attention_mask : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.MaskedLMOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
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
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the masked language modeling loss. Indices should be in [-100, 0, ..., config.vocab_size] (see input_ids docstring) Tokens with indices set to -100 are ignored (masked), the
loss is only computed for the tokens with labels in [0, ..., config.vocab_size]
Returns
transformers.modeling_outputs.MaskedLMOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
A transformers.modeling_outputs.MaskedLMOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Masked language modeling (MLM) loss. logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) — Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.MaskedLMOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.MaskedLMOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MaskedLMOutput)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
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
The BertForMaskedLM forward method, overrides the __call__ special method.
[LINK: BertForMaskedLM](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForMaskedLM)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BertForNextSentencePrediction

### class transformers. BertForNextSentencePrediction

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1049)
( config )
Parameters
- config ( BertForNextSentencePrediction ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertForNextSentencePrediction](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForNextSentencePrediction)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
Bert Model with a next sentence prediction (classification) head on top.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1059)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.NextSentencePredictorOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.NextSentencePredictorOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.NextSentencePredictorOutput)
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
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the next sequence prediction (classification) loss. Input should be a sequence pair
(see input_ids docstring). Indices should be in [0, 1] : 0 indicates sequence B is a continuation of sequence A, 1 indicates sequence B is a random sequence.
- 0 indicates sequence B is a continuation of sequence A,
- 1 indicates sequence B is a random sequence.
Returns
transformers.modeling_outputs.NextSentencePredictorOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.NextSentencePredictorOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.NextSentencePredictorOutput)
A transformers.modeling_outputs.NextSentencePredictorOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when next_sentence_label is provided) — Next sequence prediction (classification) loss. logits ( torch.FloatTensor of shape (batch_size, 2) ) — Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.NextSentencePredictorOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.NextSentencePredictorOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.NextSentencePredictorOutput)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
- loss ( torch.FloatTensor of shape (1,) , optional , returned when next_sentence_label is provided) — Next sequence prediction (classification) loss.
loss ( torch.FloatTensor of shape (1,) , optional , returned when next_sentence_label is provided) — Next sequence prediction (classification) loss.
- logits ( torch.FloatTensor of shape (batch_size, 2) ) — Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
before SoftMax).
logits ( torch.FloatTensor of shape (batch_size, 2) ) — Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
before SoftMax).
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
The BertForNextSentencePrediction forward method, overrides the __call__ special method.
[LINK: BertForNextSentencePrediction](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForNextSentencePrediction)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BertForSequenceClassification

### class transformers. BertForSequenceClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1139)
( config )
Parameters
- config ( BertForSequenceClassification ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertForSequenceClassification](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForSequenceClassification)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
Bert Model transformer with a sequence classification/regression head on top (a linear layer on top of the pooled
output) e.g. for GLUE tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1155)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.SequenceClassifierOutput or tuple(torch.FloatTensor)
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
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the sequence classification/regression loss. Indices should be in [0, ..., config.num_labels - 1] . If config.num_labels == 1 a regression loss is computed (Mean-Square loss), If config.num_labels > 1 a classification loss is computed (Cross-Entropy).
Returns
transformers.modeling_outputs.SequenceClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
A transformers.modeling_outputs.SequenceClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification (or regression if config.num_labels==1) loss. logits ( torch.FloatTensor of shape (batch_size, config.num_labels) ) — Classification (or regression if config.num_labels==1) scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.SequenceClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.SequenceClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.SequenceClassifierOutput)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
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
The BertForSequenceClassification forward method, overrides the __call__ special method.
[LINK: BertForSequenceClassification](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForSequenceClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example of single-label classification:
Example of multi-label classification:

## BertForMultipleChoice

### class transformers. BertForMultipleChoice

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1220)
( config )
Parameters
- config ( BertForMultipleChoice ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertForMultipleChoice](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForMultipleChoice)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bert Model with a multiple choice classification head on top (a linear layer on top of the pooled output and a
softmax) e.g. for RocStories/SWAG tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1234)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.MultipleChoiceModelOutput or tuple(torch.FloatTensor)
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
- token_type_ids ( torch.LongTensor of shape (batch_size, num_choices, sequence_length) , optional ) —
Segment token indices to indicate first and second portions of the inputs. Indices are selected in [0, 1] : 0 corresponds to a sentence A token, 1 corresponds to a sentence B token. What are token type IDs?
- 0 corresponds to a sentence A token,
- 1 corresponds to a sentence B token.
What are token type IDs?
- position_ids ( torch.LongTensor of shape (batch_size, num_choices, sequence_length) , optional ) —
Indices of positions of each input sequence tokens in the position embeddings. Selected in the range [0, config.max_position_embeddings - 1] . What are position IDs?
What are position IDs?
- inputs_embeds ( torch.FloatTensor of shape (batch_size, num_choices, sequence_length, hidden_size) , optional ) —
Optionally, instead of passing input_ids you can choose to directly pass an embedded representation. This
is useful if you want more control over how to convert input_ids indices into associated vectors than the
model’s internal embedding lookup matrix.
- labels ( torch.LongTensor of shape (batch_size,) , optional ) —
Labels for computing the multiple choice classification loss. Indices should be in [0, ..., num_choices-1] where num_choices is the size of the second dimension of the input tensors. (See input_ids above)
Returns
transformers.modeling_outputs.MultipleChoiceModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
A transformers.modeling_outputs.MultipleChoiceModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Classification loss. logits ( torch.FloatTensor of shape (batch_size, num_choices) ) — num_choices is the second dimension of the input tensors. (see input_ids above). Classification scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.MultipleChoiceModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.MultipleChoiceModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.MultipleChoiceModelOutput)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
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
The BertForMultipleChoice forward method, overrides the __call__ special method.
[LINK: BertForMultipleChoice](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForMultipleChoice)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BertForTokenClassification

### class transformers. BertForTokenClassification

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1318)
( config )
Parameters
- config ( BertForTokenClassification ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertForTokenClassification](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForTokenClassification)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bert transformer with a token classification head on top (a linear layer on top of the hidden-states
output) e.g. for Named-Entity-Recognition (NER) tasks.
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1333)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None labels : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
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
- labels ( torch.LongTensor of shape (batch_size, sequence_length) , optional ) —
Labels for computing the token classification loss. Indices should be in [0, ..., config.num_labels - 1] .
Returns
transformers.modeling_outputs.TokenClassifierOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided)  — Classification loss. logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.num_labels) ) — Classification scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.TokenClassifierOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.TokenClassifierOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.TokenClassifierOutput)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
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
The BertForTokenClassification forward method, overrides the __call__ special method.
[LINK: BertForTokenClassification](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForTokenClassification)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## BertForQuestionAnswering

### class transformers. BertForQuestionAnswering

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1378)
( config )
Parameters
- config ( BertForQuestionAnswering ) —
Model configuration class with all the parameters of the model. Initializing with a config file does not
load the weights associated with the model, only the configuration. Check out the from_pretrained() method to load the model weights.
[LINK: BertForQuestionAnswering](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForQuestionAnswering)
[LINK: from_pretrained()](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)
The Bert transformer with a span classification head on top for extractive question-answering tasks like
SQuAD (a linear layer on top of the hidden-states output to compute span start logits and span end logits ).
This model inherits from PreTrainedModel . Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)
[LINK: PreTrainedModel](/docs/transformers/v5.0.0rc2/en/main_classes/model#transformers.PreTrainedModel)
This model is also a PyTorch torch.nn.Module subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.
[LINK: torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L1389)
( input_ids : typing.Optional[torch.Tensor] = None attention_mask : typing.Optional[torch.Tensor] = None token_type_ids : typing.Optional[torch.Tensor] = None position_ids : typing.Optional[torch.Tensor] = None inputs_embeds : typing.Optional[torch.Tensor] = None start_positions : typing.Optional[torch.Tensor] = None end_positions : typing.Optional[torch.Tensor] = None **kwargs : typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs] ) → transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
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
- start_positions ( torch.Tensor of shape (batch_size,) , optional ) —
Labels for position (index) of the start of the labelled span for computing the token classification loss.
Positions are clamped to the length of the sequence ( sequence_length ). Position outside of the sequence
are not taken into account for computing the loss.
- end_positions ( torch.Tensor of shape (batch_size,) , optional ) —
Labels for position (index) of the end of the labelled span for computing the token classification loss.
Positions are clamped to the length of the sequence ( sequence_length ). Position outside of the sequence
are not taken into account for computing the loss.
Returns
transformers.modeling_outputs.QuestionAnsweringModelOutput or tuple(torch.FloatTensor)
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs. loss ( torch.FloatTensor of shape (1,) , optional , returned when labels is provided) — Total span extraction loss is the sum of a Cross-Entropy for the start and end positions. start_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-start scores (before SoftMax). end_logits ( torch.FloatTensor of shape (batch_size, sequence_length) ) — Span-end scores (before SoftMax). hidden_states ( tuple(torch.FloatTensor) , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) — Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs. attentions ( tuple(torch.FloatTensor) , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) — Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
A transformers.modeling_outputs.QuestionAnsweringModelOutput or a tuple of torch.FloatTensor (if return_dict=False is passed or when config.return_dict=False ) comprising various
elements depending on the configuration ( BertConfig ) and inputs.
[LINK: transformers.modeling_outputs.QuestionAnsweringModelOutput](/docs/transformers/v5.0.0rc2/en/main_classes/output#transformers.modeling_outputs.QuestionAnsweringModelOutput)
[LINK: BertConfig](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertConfig)
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
The BertForQuestionAnswering forward method, overrides the __call__ special method.
[LINK: BertForQuestionAnswering](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForQuestionAnswering)
Although the recipe for forward pass needs to be defined within this function, one should call the Module instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.
Example:

## Bert specific outputs

### class transformers.models.bert.modeling_bert. BertForPreTrainingOutput

[LINK: < source >](https://github.com/huggingface/transformers/blob/v5.0.0rc2/src/transformers/models/bert/modeling_bert.py#L583)
( loss : typing.Optional[torch.FloatTensor] = None prediction_logits : typing.Optional[torch.FloatTensor] = None seq_relationship_logits : typing.Optional[torch.FloatTensor] = None hidden_states : typing.Optional[tuple[torch.FloatTensor]] = None attentions : typing.Optional[tuple[torch.FloatTensor]] = None )
Parameters
- loss ( *optional* , returned when labels is provided, torch.FloatTensor of shape (1,) ) —
Total loss as the sum of the masked language modeling loss and the next sequence prediction
(classification) loss.
- prediction_logits ( torch.FloatTensor of shape (batch_size, sequence_length, config.vocab_size) ) —
Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- seq_relationship_logits ( torch.FloatTensor of shape (batch_size, 2) ) —
Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
before SoftMax).
- hidden_states ( tuple[torch.FloatTensor] , optional , returned when output_hidden_states=True is passed or when config.output_hidden_states=True ) —
Tuple of torch.FloatTensor (one for the output of the embeddings, if the model has an embedding layer, +
one for the output of each layer) of shape (batch_size, sequence_length, hidden_size) . Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- attentions ( tuple[torch.FloatTensor] , optional , returned when output_attentions=True is passed or when config.output_attentions=True ) —
Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length, sequence_length) . Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
heads.
Output type of BertForPreTraining .
[LINK: BertForPreTraining](/docs/transformers/v5.0.0rc2/en/model_doc/bert#transformers.BertForPreTraining)
[LINK: Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/bert.md)
[LINK: ← BARTpho](/docs/transformers/model_doc/bartpho)
[LINK: BertGeneration →](/docs/transformers/model_doc/bert-generation)

--------------------