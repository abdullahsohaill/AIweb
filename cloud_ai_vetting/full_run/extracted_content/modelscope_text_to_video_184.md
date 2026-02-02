# ModelScope Text-To-Video
**URL:** https://huggingface.co/spaces/ali-vilab/modelscope-text-to-video-synthesis
**Page Title:** ModelScope Text To Video Synthesis - a Hugging Face Space by ali-vilab
--------------------


## runtime error

## Exit code: 1. Reason: /user/.pyenv/versions/3.10.18/lib/python3.10/contextlib.py", line 135, in __enter__
    return next(self.gen)
  File "/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/accelerate/big_modeling.py", line 74, in init_empty_weights
    with init_on_device(torch.device("meta"), include_buffers=include_buffers) as f:
/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/accelerate/big_modeling.py:74: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.)
  with init_on_device(torch.device("meta"), include_buffers=include_buffers) as f:
Traceback (most recent call last):
  File "/home/user/app/app.py", line 25, in <module>
    pipe = DiffusionPipeline.from_pretrained('damo-vilab/text-to-video-ms-1.7b',
  File "/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/diffusers/pipelines/pipeline_utils.py", line 930, in from_pretrained
    loaded_sub_model = load_sub_model(
  File "/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/diffusers/pipelines/pipeline_utils.py", line 385, in load_sub_model
    loaded_sub_model = load_method(os.path.join(cached_folder, name), **loading_kwargs)
  File "/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/diffusers/schedulers/scheduling_utils.py", line 146, in from_pretrained
    return cls.from_config(config, return_unused_kwargs=return_unused_kwargs, **kwargs)
  File "/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/diffusers/configuration_utils.py", line 218, in from_config
    model = cls(**init_dict)
  File "/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/diffusers/configuration_utils.py", line 596, in inner_init
    init(self, *args, **init_kwargs)
  File "/home/user/.pyenv/versions/3.10.18/lib/python3.10/site-packages/diffusers/schedulers/scheduling_ddim.py", line 176, in __init__
    self.timesteps = torch.from_numpy(np.arange(0, num_train_timesteps)[::-1].copy().astype(np.int64))
RuntimeError: Numpy is not available

Container logs:

--------------------