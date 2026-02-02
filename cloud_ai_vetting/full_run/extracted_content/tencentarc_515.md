# TencentARC
**URL:** https://huggingface.co/spaces/TencentARC/PhotoMaker-Style
**Page Title:** PhotoMaker Style - a Hugging Face Space by TencentARC
--------------------


## runtime error

## Exit code: 1. Reason: on3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1240, in hf_hub_download
    return _hf_hub_download_to_cache_dir(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1347, in _hf_hub_download_to_cache_dir
    _raise_on_head_call_error(head_call_error, force_download, local_files_only)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1854, in _raise_on_head_call_error
    raise head_call_error
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1751, in _get_metadata_or_catch_error
    metadata = get_hf_file_metadata(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1673, in get_hf_file_metadata
    r = _request_wrapper(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 376, in _request_wrapper
    response = _request_wrapper(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 400, in _request_wrapper
    hf_raise_for_status(response)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_errors.py", line 352, in hf_raise_for_status
    raise RepositoryNotFoundError(message, response) from e
huggingface_hub.utils._errors.RepositoryNotFoundError: 401 Client Error. (Request ID: Root=1-6800ace5-25cfcddb1f445b5c7ffab614;493715ea-30ee-488f-912b-674c38711e47)

Repository Not Found for url: https://huggingface.co/Paper99/sdxlUnstableDiffusers_v11/resolve/main/sdxlUnstableDiffusers_v11.safetensors.
Please make sure you specified the correct `repo_id` and `repo_type`.
If you are trying to access a private or gated repo, make sure you are authenticated.
Invalid credentials in Authorization header

Container logs:

--------------------