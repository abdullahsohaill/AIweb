# FullyShardedDataParallelPlugin
**URL:** https://huggingface.co/docs/accelerate/v0.11.0/en/fsdp
**Page Title:** Fully Sharded Data Parallel
--------------------

Accelerate documentation
Fully Sharded Data Parallel

## Accelerate

[LINK: 9,463](https://github.com/huggingface/accelerate)
[LINK: v1.12.0](/docs/accelerate/v1.12.0/fsdp)
and get access to the augmented documentation experience
to get started

## Fully Sharded Data Parallel

To accelerate training huge models on larger batch sizes, we can use a fully sharded data parallel model.
This type of data parallel paradigm enables fitting more data and larger models by sharding the optimizer states, gradients and parameters.
To read more about it and the benefits, check out the Fully Sharded Data Parallel blog .
We have integrated the latest PyTorch’s Fully Sharded Data Parallel (FSDP) training feature.
All you need to do is enable it through the config.
[LINK: Fully Sharded Data Parallel blog](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/)

## How it works out of the box

On your machine(s) just run:
and answer the questions asked. This will generate a config file that will be used automatically to properly set the
default options when doing
For instance, here is how you would run the NLP example (from the root of the repo) with FSDP enabled:
Currently, Accelerate supports the following config through the CLI:

## A few caveats to be aware of

- PyTorch FSDP auto wraps sub-modules, flattens the parameters and shards the parameters in place.
Due to this, any optimizer created before model wrapping gets broken and occupies more memory.
Hence, it is highly recommended and efficient to prepare the model before creating the optimizer. Accelerate will automatically wrap the model and create an optimizer for you in case of single model with a warning message. FSDP Warning: When using FSDP, it is efficient and recommended to call prepare for the model before creating the optimizer
FSDP Warning: When using FSDP, it is efficient and recommended to call prepare for the model before creating the optimizer
However, below is the recommended way to prepare model and optimizer while using FSDP:
- In case of a single model, if you have created the optimizer with multiple parameter groups and called prepare with them together,
then the parameter groups will be lost and the following warning is displayed: FSDP Warning: When using FSDP, several parameter groups will be conflated into
a single one due to nested module wrapping and parameter flattening. This is because parameter groups created before wrapping will have no meaning post wrapping due to parameter flattening of nested FSDP modules into 1D arrays (which can consume many layers).
For instance, below are the named parameters of an FSDP model on GPU 0 (When using 2 GPUs. Around 55M (110M/2) params in 1D arrays as this will have the 1st shard of the parameters).
Here, if one has applied no weight decay for [bias, LayerNorm.weight] the named parameters of an unwrapped BERT model,
it can’t be applied to the below FSDP wrapped model as there are no named parameters with either of those strings and
the parameters of those layers are concatenated with parameters of various other layers. { '_fsdp_wrapped_module.flat_param' : torch .Size ( [494209] ), '_fsdp_wrapped_module._fpw_module.bert.embeddings.word_embeddings._fsdp_wrapped_module.flat_param' : torch .Size ( [11720448] ), '_fsdp_wrapped_module._fpw_module.bert.encoder._fsdp_wrapped_module.flat_param' : torch .Size ( [42527232] )
}
In case of a single model, if you have created the optimizer with multiple parameter groups and called prepare with them together,
then the parameter groups will be lost and the following warning is displayed:
FSDP Warning: When using FSDP, several parameter groups will be conflated into
a single one due to nested module wrapping and parameter flattening.
This is because parameter groups created before wrapping will have no meaning post wrapping due to parameter flattening of nested FSDP modules into 1D arrays (which can consume many layers).
For instance, below are the named parameters of an FSDP model on GPU 0 (When using 2 GPUs. Around 55M (110M/2) params in 1D arrays as this will have the 1st shard of the parameters).
Here, if one has applied no weight decay for [bias, LayerNorm.weight] the named parameters of an unwrapped BERT model,
it can’t be applied to the below FSDP wrapped model as there are no named parameters with either of those strings and
the parameters of those layers are concatenated with parameters of various other layers.
- In case of multiple models, it is necessary to prepare the models before creating optimizers or else it will throw an error.
- Mixed precision is currently not supported with FSDP.
For more control, users can leverage the FullyShardedDataParallelPlugin wherein they can specify auto_wrap_policy , backward_prefetch and ignored_modules .
After creating an instance of this class, users can pass it to the Accelerator class instantiation.
For more information on these options, please refer to the PyTorch FullyShardedDataParallel code.
[LINK: FullyShardedDataParallel](https://github.com/pytorch/pytorch/blob/0df2e863fbd5993a7b9e652910792bd21a516ff3/torch/distributed/fsdp/fully_sharded_data_parallel.py#L236)

### class accelerate. FullyShardedDataParallelPlugin

[LINK: < source >](https://github.com/huggingface/accelerate/blob/v0.11.0/src/accelerate/utils/dataclasses.py#L416)
( sharding_strategy : typing.Any = None backward_prefetch : typing.Any = None mixed_precision_policy : typing.Any = None auto_wrap_policy : typing.Optional[typing.Callable] = None cpu_offload : typing.Any = None ignored_modules : typing.Optional[typing.Iterable[torch.nn.modules.module.Module]] = None )
This plugin is used to enable fully sharded data parallelism.
[LINK: < source >](https://github.com/huggingface/accelerate/blob/v0.11.0/src/accelerate/utils/dataclasses.py#L475)
( module name )
Parameters
- module ( torch.nn.Module ) — The module to get the class from.
- name ( str ) — The name of the class.
Gets a class from a module by its name.
[LINK: ← Experiment Tracking](/docs/accelerate/v0.11.0/en/tracking)
[LINK: Memory Utilities →](/docs/accelerate/v0.11.0/en/memory)

--------------------