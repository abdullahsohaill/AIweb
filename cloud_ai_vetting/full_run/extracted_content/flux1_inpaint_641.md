# FLUX.1-inpaint
**URL:** https://huggingface.co/spaces/SkalskiP/FLUX.1-inpaint
**Page Title:** FLUX.1 [Inpainting] - a Hugging Face Space by SkalskiP
--------------------


## runtime error

## Exit code: 1. Reason: utils.py", line 1242, in download
    config_file = hf_hub_download(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1010, in hf_hub_download
    return _hf_hub_download_to_cache_dir(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1117, in _hf_hub_download_to_cache_dir
    _raise_on_head_call_error(head_call_error, force_download, local_files_only)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1658, in _raise_on_head_call_error
    raise head_call_error
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1546, in _get_metadata_or_catch_error
    metadata = get_hf_file_metadata(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1463, in get_hf_file_metadata
    r = _request_wrapper(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 286, in _request_wrapper
    response = _request_wrapper(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 310, in _request_wrapper
    hf_raise_for_status(response)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 426, in hf_raise_for_status
    raise _format(GatedRepoError, message, response) from e
huggingface_hub.errors.GatedRepoError: 401 Client Error. (Request ID: Root=1-68b00a37-4b73acf52854a7c5533b10c6;fab93df8-9b3c-4fe0-b93c-b21696955a39)

Cannot access gated repo for url https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/model_index.json.
Access to model black-forest-labs/FLUX.1-schnell is restricted. You must have access to it and be authenticated to access it. Please log in.

Container logs:

--------------------