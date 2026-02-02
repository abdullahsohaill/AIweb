# ChatGPT Detector
**URL:** https://huggingface.co/spaces/Hello-SimpleAI/chatgpt-detector-single
**Page Title:** Chatgpt Detector Single - a Hugging Face Space by Hello-SimpleAI
--------------------


## runtime error

## Exit code: 1. Reason: _hub_download_to_cache_dir
    _download_to_tmp_and_move(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1545, in _download_to_tmp_and_move
    http_get(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 368, in http_get
    r = _request_wrapper(
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 300, in _request_wrapper
    response = get_session().request(method=method, url=url, **params)
  File "/usr/local/lib/python3.10/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.10/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 93, in send
    return super().send(request, *args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/requests/adapters.py", line 688, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: (MaxRetryError("HTTPSConnectionPool(host='cas-bridge-direct.xethub.hf.co', port=443): Max retries exceeded with url: /xet-bridge-us/63c8209df7cd81d306d0edc6/f0746ba2e55da74e3bda81e379099ae79877904475d032f49d031aa9910b5cf5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=cas%2F20251020%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251020T172205Z&X-Amz-Expires=3600&X-Amz-Signature=9fba012d4d09c56b9deafd747f7128be53b31e22b2b27e5351dddabfa0950ab8&X-Amz-SignedHeaders=host&X-Xet-Cas-Uid=public&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27pytorch_model.bin%3B%20filename%3D%22pytorch_model.bin%22%3B&response-content-type=application%2Foctet-stream&x-id=GetObject (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x7ff51bc754e0>, 'Connection to cas-bridge-direct.xethub.hf.co timed out. (connect timeout=10)'))"), '(Request ID: 41e849a6-ad47-4a75-8567-2f0ac737fe0e)')

Container logs:

--------------------