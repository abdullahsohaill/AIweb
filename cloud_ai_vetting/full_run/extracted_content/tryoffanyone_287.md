# TryOffAnyone
**URL:** https://huggingface.co/spaces/1aurent/TryOffAnyone
**Page Title:** TryOffAnyone - a Hugging Face Space by 1aurent
--------------------


## runtime error

## Exit code: 1. Reason: config.json:   0%|          | 0.00/547 [00:00<?, ?B/s][Aconfig.json: 100%|██████████| 547/547 [00:00<00:00, 5.39MB/s]

diffusion_pytorch_model.safetensors:   0%|          | 0.00/335M [00:00<?, ?B/s][A
diffusion_pytorch_model.safetensors:  20%|██        | 67.1M/335M [00:01<00:05, 49.7MB/s][Adiffusion_pytorch_model.safetensors: 100%|██████████| 335M/335M [00:01<00:00, 217MB/s]  

config.json:   0%|          | 0.00/748 [00:00<?, ?B/s][Aconfig.json: 100%|██████████| 748/748 [00:00<00:00, 7.43MB/s]

unet/diffusion_pytorch_model.fp16.safete(…):   0%|          | 0.00/1.72G [00:00<?, ?B/s][A
unet/diffusion_pytorch_model.fp16.safete(…):   4%|▍         | 67.0M/1.72G [00:01<00:41, 40.0MB/s][A
unet/diffusion_pytorch_model.fp16.safete(…):  96%|█████████▌| 1.65G/1.72G [00:06<00:00, 295MB/s] [Aunet/diffusion_pytorch_model.fp16.safete(…): 100%|██████████| 1.72G/1.72G [00:06<00:00, 254MB/s]

model.safetensors:   0%|          | 0.00/1.07G [00:00<?, ?B/s][A
model.safetensors:   6%|▌         | 63.0M/1.07G [00:01<00:24, 41.5MB/s][A
model.safetensors: 100%|██████████| 1.07G/1.07G [00:03<00:00, 394MB/s] [Amodel.safetensors: 100%|██████████| 1.07G/1.07G [00:03<00:00, 342MB/s]
The safetensors archive passed at /home/user/.cache/huggingface/hub/models--ixarchakos--tryOffAnyone/snapshots/141ca652718a1414908b68cee1f0fc55d72d8cec/model.safetensors does not contain metadata. Make sure to save your model with the `save_pretrained` method. Defaulting to 'pt' metadata.
Traceback (most recent call last):
  File "/home/user/app/src/app.py", line 36, in <module>
    mask_processor = diffusers.image_processor.VaeImageProcessor(
  File "/usr/local/lib/python3.10/site-packages/diffusers/utils/import_utils.py", line 946, in __getattr__
    raise AttributeError(f"module {self.__name__} has no attribute {name}")
AttributeError: module diffusers has no attribute image_processor

Container logs:

--------------------