# CharacterGen
**URL:** https://huggingface.co/spaces/VAST-AI/CharacterGen
**Page Title:** CharacterGen - a Hugging Face Space by VAST-AI
--------------------


## runtime error

## Exit code: 1. Reason: p = self.send(prep, **send_kwargs)
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 93, in send
    return super().send(request, *args, **kwargs)
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/requests/adapters.py", line 690, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: (ReadTimeoutError("HTTPSConnectionPool(host='huggingface.co', port=443): Read timed out. (read timeout=10)"), '(Request ID: 06d0779a-e17c-4f2e-9221-f616201a8b82)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/app/app.py", line 64, in <module>
    hf_hub_download(repo_id, file, local_dir=".")
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/huggingface_hub/utils/_deprecation.py", line 101, in inner_f
    return f(*args, **kwargs)
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1212, in hf_hub_download
    return _hf_hub_download_to_local_dir(
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1461, in _hf_hub_download_to_local_dir
    _raise_on_head_call_error(head_call_error, force_download, local_files_only)
  File "/root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1857, in _raise_on_head_call_error
    raise LocalEntryNotFoundError(
huggingface_hub.errors.LocalEntryNotFoundError: An error happened while trying to locate the file on the Hub and we cannot find the requested files in the local cache. Please check your connection and try again or make sure your Internet connection is on.

Container logs:

--------------------