# HuggingGPT
**URL:** https://huggingface.co/spaces/microsoft/HuggingGPT
**Page Title:** HuggingGPT - a Hugging Face Space by microsoft
--------------------


## runtime error

## Exit code: 1. Reason:         │
│    90 │   def send(self, request: PreparedRequest, *args, **kwargs) -> Respo │
│    91 │   │   """Catch any RequestException to append request id to the erro │
│    92 │   │   try:                                                           │
│ ❱  93 │   │   │   return super().send(request, *args, **kwargs)              │
│    94 │   │   except requests.RequestException as e:                         │
│    95 │   │   │   request_id = request.headers.get(X_AMZN_TRACE_ID)          │
│    96 │   │   │   if request_id is not None:                                 │
│                                                                              │
│ /home/user/.pyenv/versions/3.10.16/lib/python3.10/site-packages/requests/ada │
│ pters.py:713 in send                                                         │
│                                                                              │
│   710 │   │   │   │   # This branch is for urllib3 versions earlier than v1. │
│   711 │   │   │   │   raise SSLError(e, request=request)                     │
│   712 │   │   │   elif isinstance(e, ReadTimeoutError):                      │
│ ❱ 713 │   │   │   │   raise ReadTimeout(e, request=request)                  │
│   714 │   │   │   elif isinstance(e, _InvalidHeader):                        │
│   715 │   │   │   │   raise InvalidHeader(e, request=request)                │
│   716 │   │   │   else:                                                      │
╰──────────────────────────────────────────────────────────────────────────────╯
ReadTimeout: (ReadTimeoutError("HTTPSConnectionPool(host='huggingface.co', 
port=443): Read timed out. (read timeout=10)"), '(Request ID: 
34ff3b3f-a738-4414-afe8-898159f7fb4b)')

Container logs:

--------------------