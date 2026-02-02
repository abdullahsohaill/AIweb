# Hallucinations Leaderboard
**URL:** https://huggingface.co/spaces/hallucinations-leaderboard/leaderboard
**Page Title:** Hallucinations Leaderboard - a Hugging Face Space by hallucinations-leaderboard
--------------------


## runtime error

## Exit code: 1. Reason: nection and try again or make sure your Internet connection is on.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 406, in hf_raise_for_status
    response.raise_for_status()
  File "/usr/local/lib/python3.10/site-packages/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 504 Server Error: Gateway Timeout for url: https://huggingface.co/api/spaces/hallucinations-leaderboard/leaderboard/restart

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/user/app/app.py", line 72, in <module>
    dataset_df, original_df, finished_eval_queue_df, running_eval_queue_df, pending_eval_queue_df = init_space()
  File "/home/user/app/app.py", line 64, in init_space
    ui_snapshot_download(repo_id=QUEUE_REPO, local_dir=EVAL_REQUESTS_PATH, repo_type="dataset", tqdm_class=None, etag_timeout=30)
  File "/home/user/app/app.py", line 52, in ui_snapshot_download
    restart_space()
  File "/home/user/app/app.py", line 56, in restart_space
    API.restart_space(repo_id=REPO_ID, token=H4_TOKEN)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/hf_api.py", line 7468, in restart_space
    hf_raise_for_status(r)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 477, in hf_raise_for_status
    raise _format(HfHubHTTPError, str(e), response) from e
huggingface_hub.errors.HfHubHTTPError: 504 Server Error: Gateway Timeout for url: https://huggingface.co/api/spaces/hallucinations-leaderboard/leaderboard/restart (Request ID: Root=1-689b3a93-2ef26af03c3270226e308c47;17b61197-c4cc-4f9d-b4f2-b51820b4faa4)

The request is taking longer than expected, please try again later.

Container logs:

--------------------