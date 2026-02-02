# https://qagentur.github.io/texttunnel/
**URL:** https://qagentur.github.io/texttunnel
**Page Title:** texttunnel: Efficient text processing with GPT-3.5 and GPT-4 — texttunnel 0.2.1 documentation
--------------------

- texttunnel: Efficient text processing with GPT-3.5 and GPT-4
- View page source

## texttunnel: Efficient text processing with GPT-3.5 and GPT-4 

This package offers a straightforward interface for integrating the GPT-3.5 and GPT-4 models into your natural language processing pipelines. It is optimally designed for the following scenario:
Suppose you possess a corpus of text data that you want to analyze using the GPT-3.5 or GPT-4 models. The goal is to perform extractive NLP tasks such as classification, named entity recognition, translation, summarization, question answering, or sentiment analysis. In this context, the package prioritizes efficiency and tidiness to provide you streamlined results.
Features:
- 📄 Output Schema: Utilizes JSON Schema alongside OpenAI’s function calling schema to define the output data structure.
📄 Output Schema: Utilizes JSON Schema alongside OpenAI’s function calling schema to define the output data structure.
- ✔️ Input Validation: Ensures well-structured and error-free API requests by validating input data.
✔️ Input Validation: Ensures well-structured and error-free API requests by validating input data.
- ✅ Output Validation: Checks the response data from OpenAI’s API against the expected schema to maintain data integrity.
✅ Output Validation: Checks the response data from OpenAI’s API against the expected schema to maintain data integrity.
- 🚀 Efficient Batching: Supports bulk processing by packing multiple input texts into a single request for the OpenAI’s API.
🚀 Efficient Batching: Supports bulk processing by packing multiple input texts into a single request for the OpenAI’s API.
- 🚦 Asynchronous Requests: Facilitates speedy data processing by sending simultaneous requests to OpenAI’s API, while maintaining API rate limits.
🚦 Asynchronous Requests: Facilitates speedy data processing by sending simultaneous requests to OpenAI’s API, while maintaining API rate limits.
- 💰 Cost Estimation: Aims for transparency in API utilization cost by providing cost estimates before sending API requests.
💰 Cost Estimation: Aims for transparency in API utilization cost by providing cost estimates before sending API requests.
- 💾 Caching: Uses aiohttp_client_cach to avoid redundant requests and reduce cost by caching previous requests. Supports SQLite, MongoDB, DynamoDB and Redis cache backends.
💾 Caching: Uses aiohttp_client_cach to avoid redundant requests and reduce cost by caching previous requests. Supports SQLite, MongoDB, DynamoDB and Redis cache backends.
- 📝 Request Logging: Implements Python’s native logging framework for tracking and logging all API requests.
📝 Request Logging: Implements Python’s native logging framework for tracking and logging all API requests.
To get started, check the examples: https://github.com/qagentur/texttunnel/tree/main/examples
[LINK: https://github.com/qagentur/texttunnel/tree/main/examples](https://github.com/qagentur/texttunnel/tree/main/examples)
OpenAI’s function calling guide is also a useful resource: https://platform.openai.com/docs/guides/gpt/function-calling
[LINK: https://platform.openai.com/docs/guides/gpt/function-calling](https://platform.openai.com/docs/guides/gpt/function-calling)

## Modules 

## Chat Module 

A chat. Used to prompt a model for a response.
The first message must be from the system, and the last message must be from the user.
messages – A list of ChatMessage objects.
Adds a message to the end of the chat.
message – The message to add.
Return the number of tokens used.
Note that this depends on the model used. Models that are not versioned
with a date can change over time, causing an inaccurate token count
by this function.
model – The name of the model to use. Defaults to “gpt-3.5-turbo-0613”.
The number of tokens used.
Returns a list of dictionaries representing the chat messages.
This is the format expected by the OpenAI API.
Defines a request for a chat completion.
- chat – The chat to which the assistant should respond with a function call.
chat – The chat to which the assistant should respond with a function call.
- model – The name of the OpenAI ChatCompletion model to use for completion.
model – The name of the OpenAI ChatCompletion model to use for completion.
- function – The function definition to use for the assistant’s response.
Must be a dictionary that describes a valid JSON schema.
See https://platform.openai.com/docs/guides/gpt/function-calling
function – The function definition to use for the assistant’s response.
Must be a dictionary that describes a valid JSON schema.
See https://platform.openai.com/docs/guides/gpt/function-calling
[LINK: https://platform.openai.com/docs/guides/gpt/function-calling](https://platform.openai.com/docs/guides/gpt/function-calling)
- params – Object of class Parameters. See models.Parameters for details.
params – Object of class Parameters. See models.Parameters for details.
Counts the number of tokens that will be used as output of the model.
Assumes that the model will return the maximum number of tokens allowed
by the max_tokens parameter.
Counts the number of tokens that will be used as input to the model.
This includes the chat messages and the function call.
Counts the total number of tokens that will be used as input and output
of the model. Assumes that the model will return the maximum number of
tokens allowed by the max_tokens parameter.
Estimates the cost of the request in USD. Assumes that the model will
return the maximum number of tokens allowed by the max_tokens parameter.
The estimate is the upper bound on the cost, since the model may return
fewer tokens than the maximum allowed.
Returns the hash of the request. Can be used as a cache key.
Returns a dictionary representation of the request. Only includes
the elements that are required by the OpenAI API. Model parameters
are flattened into the top-level dictionary.
A chat message, to be used in a chat.
- role – The role of the message. Must be one of “system”, “user”, or “assistant”.
role – The role of the message. Must be one of “system”, “user”, or “assistant”.
- content – The content of the message.
content – The content of the message.
Returns a dict representation of the message.
Builds a list of ChatCompletionRequests from a list of texts.
If possible, multiple texts will be combined into a single ChatCompletionRequest.
This can reduce the number of tokens spent on overheads like the system message
and function definition.
The requests can then be passed to processor.process_api_requests().
- model – The model to use for completion.
model – The model to use for completion.
- function – The function definition to use for the assistant’s response.
Must be a dictionary that describes a valid JSON schema.
See https://platform.openai.com/docs/guides/gpt/function-calling
function – The function definition to use for the assistant’s response.
Must be a dictionary that describes a valid JSON schema.
See https://platform.openai.com/docs/guides/gpt/function-calling
[LINK: https://platform.openai.com/docs/guides/gpt/function-calling](https://platform.openai.com/docs/guides/gpt/function-calling)
- system_message – The message to include at the beginning of each chat.
system_message – The message to include at the beginning of each chat.
- texts – A list of texts to binpack into chats. Duplicates are not allowed.
texts – A list of texts to binpack into chats. Duplicates are not allowed.
- params – Object of class Parameters. See models.Parameters for details.
params – Object of class Parameters. See models.Parameters for details.
- max_tokens_per_request – The maximum number of tokens allowed in one request.
Defaults to 90% of the model’s context size. The 10% buffer makes
sure that mistakes in token counting don’t cause the request to fail.
max_tokens_per_request – The maximum number of tokens allowed in one request.
Defaults to 90% of the model’s context size. The 10% buffer makes
sure that mistakes in token counting don’t cause the request to fail.
- max_texts_per_request – The maximum number of texts allowed in one request.
Defaults to None, which means there is no limit.
max_texts_per_request – The maximum number of texts allowed in one request.
Defaults to None, which means there is no limit.
- binpacking_function – The function to use for binpacking.
Must take a list of texts and return a list of lists of texts.
Defaults to binpack_texts_in_order().
binpacking_function – The function to use for binpacking.
Must take a list of texts and return a list of lists of texts.
Defaults to binpack_texts_in_order().
- formatter_function – The function to use for formatting the texts.
Must take a list of texts and return a single string.
Defaults to format_texts_as_json().
formatter_function – The function to use for formatting the texts.
Must take a list of texts and return a single string.
Defaults to format_texts_as_json().
- encoding_name – The name of the encoding to use for tokenization.
Defaults to “cl100k_base”.
encoding_name – The name of the encoding to use for tokenization.
Defaults to “cl100k_base”.
- long_text_handling – Passed to the binpacking function. Defaults to
“error”, which means that an error will be raised if a text is too
long to fit in a single chat.
long_text_handling – Passed to the binpacking function. Defaults to
“error”, which means that an error will be raised if a text is too
long to fit in a single chat.
A list of ChatCompletionRequests.
Builds a list of ChatCompletionRequests from a list of texts.
The requests can then be passed to processor.process_api_requests().
- model – The model to use for completion.
model – The model to use for completion.
- function – The function definition to use for the assistant’s response.
Must be a dictionary that describes a valid JSON schema.
See https://platform.openai.com/docs/guides/gpt/function-calling
function – The function definition to use for the assistant’s response.
Must be a dictionary that describes a valid JSON schema.
See https://platform.openai.com/docs/guides/gpt/function-calling
[LINK: https://platform.openai.com/docs/guides/gpt/function-calling](https://platform.openai.com/docs/guides/gpt/function-calling)
- system_message – The message to include at the beginning of each chat.
system_message – The message to include at the beginning of each chat.
- params – Object of class Parameters. See models.Parameters for details.
params – Object of class Parameters. See models.Parameters for details.
- texts – A list of texts to binpack into chats. Duplicates are not allowed.
texts – A list of texts to binpack into chats. Duplicates are not allowed.
- encoding_name – The name of the encoding to use for tokenization.
Defaults to “cl100k_base”.
encoding_name – The name of the encoding to use for tokenization.
Defaults to “cl100k_base”.
- long_text_handling – Passed to the binpacking function. Defaults to
“error”, which means that an error will be raised if a text is too
long to fit in a single chat.
long_text_handling – Passed to the binpacking function. Defaults to
“error”, which means that an error will be raised if a text is too
long to fit in a single chat.
A list of ChatCompletionRequests.
Checks if a function definition is valid for use in a ChatCompletionRequest.
Note that the parameter properties are not validated to allow for custom properties.
Check the OpenAI API documentation for more information: https://platform.openai.com/docs/guides/gpt/function-calling
[LINK: https://platform.openai.com/docs/guides/gpt/function-calling](https://platform.openai.com/docs/guides/gpt/function-calling)
function – The function definition to validate.

## Models Module 

Information about an OpenAI ChatCompletion model.
Check prices here: https://openai.com/pricing
Note that rate limits differ between OpenAI accounts.
Check them here: https://platform.openai.com/account/rate-limits
- name – The name of the model, e.g. “gpt-3.5-turbo”.
name – The name of the model, e.g. “gpt-3.5-turbo”.
- context_size – The maximum number of tokens that can be passed to the model.
context_size – The maximum number of tokens that can be passed to the model.
- input_token_price_per_1k – The price in USD per 1000 tokens for input.
input_token_price_per_1k – The price in USD per 1000 tokens for input.
- output_token_price_per_1k – The price in USD per 1000 tokens for output.
output_token_price_per_1k – The price in USD per 1000 tokens for output.
- tokens_per_minute – The maximum number of tokens that can be processed per minute.
Note that this may differ between OpenAI accounts. Override the default
models’ values with your own values.
tokens_per_minute – The maximum number of tokens that can be processed per minute.
Note that this may differ between OpenAI accounts. Override the default
models’ values with your own values.
- requests_per_minute – The maximum number of requests that can be made per minute.
Note that this may differ between OpenAI accounts. Override the default
models’ values with your own values.
requests_per_minute – The maximum number of requests that can be made per minute.
Note that this may differ between OpenAI accounts. Override the default
models’ values with your own values.
Set of parameters that can be passed to an API request.
The parameters are explained in the OpenAI API documentation: https://platform.openai.com/docs/api-reference/chat/create
[LINK: https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create)
- max_tokens – The maximum number of tokens to generate. Note:
This can’t be greater than the model’s context size and should be at least
long enough to fit the whole expected JSON output. This parameter is used
to estimate the cost of the request.
max_tokens – The maximum number of tokens to generate. Note:
This can’t be greater than the model’s context size and should be at least
long enough to fit the whole expected JSON output. This parameter is used
to estimate the cost of the request.
- temperature – What sampling temperature to use, between 0 and 2.
Higher values like 0.8 will make the output more random, while
lower values like 0.2 will make it more focused and deterministic.
Defaults to 0.0 because this package is designed for deterministic
JSON-schema compliant output.
temperature – What sampling temperature to use, between 0 and 2.
Higher values like 0.8 will make the output more random, while
lower values like 0.2 will make it more focused and deterministic.
Defaults to 0.0 because this package is designed for deterministic
JSON-schema compliant output.
- presence_penalty – Number between -2.0 and 2.0. Positive values penalize
new tokens based on whether they appear in the text so far,
increasing the model’s likelihood to talk about new topics. Defaults to 0.0.
presence_penalty – Number between -2.0 and 2.0. Positive values penalize
new tokens based on whether they appear in the text so far,
increasing the model’s likelihood to talk about new topics. Defaults to 0.0.
- frequency_penalty – Number between -2.0 and 2.0. Positive values penalize
new tokens based on their existing frequency in the text so far,
decreasing the model’s likelihood to repeat the same line verbatim.
Defaults to 0.0.
frequency_penalty – Number between -2.0 and 2.0. Positive values penalize
new tokens based on their existing frequency in the text so far,
decreasing the model’s likelihood to repeat the same line verbatim.
Defaults to 0.0.
- seed – Integer seed for random number generation. Defaults to 42.
seed – Integer seed for random number generation. Defaults to 42.
Parameters that are not listed here are not supported by this package. The
reason is that they’re not relevant for the use case of this package.
A dictionary representation of the parameters.
Models that are not included here can be created as custom instances of the Model class. Only chat models are supported; “instruct” models are not supported.
Preview models can be used, but will not be added as default models to the package. To use a preview model, create a custom instance of the Model class. Models that OpenAI deprecates will be removed from the package. This primarily affects date-versioned models.
Note that the model class attributes tokens_per_minute (TPM) and requests_per_minute (RPM) are based on tier 1 usage limits. See https://platform.openai.com/docs/guides/rate-limits?context=tier-free for more details. If your account has a higher usage tier, override the class attributes with your own values.
[LINK: https://platform.openai.com/docs/guides/rate-limits?context=tier-free](https://platform.openai.com/docs/guides/rate-limits?context=tier-free)
texttunnel does not track tokens_per_day (TPD) limits and assumes that it is the only process that is using your model quota.

## Processor Module 

Stores an API request’s inputs, outputs, and other metadata.
Contains a method to make an API call.
Calls the OpenAI API and appends the request and result to a JSONL file.
If a cache provided, the result will be stored in the cache.
The cache key is the hash of the request.
- request_url – The URL to send the request to.
request_url – The URL to send the request to.
- request_header – The header to send with the request.
request_header – The header to send with the request.
- retry_queue – A queue of requests that need to be retried.
Will be populated if the request fails.
retry_queue – A queue of requests that need to be retried.
Will be populated if the request fails.
- output_filepath – The path to the file where the results will be saved.
output_filepath – The path to the file where the results will be saved.
- status_tracker – A StatusTracker object that tracks the greater
request loop’s progress.
status_tracker – A StatusTracker object that tracks the greater
request loop’s progress.
- cache – A aiohttp_client_cache.CacheBackend object that stores API
responses. If provided, the response will be stored in the cache.
cache – A aiohttp_client_cache.CacheBackend object that stores API
responses. If provided, the response will be stored in the cache.
- timeout_seconds – The number of seconds to wait for a response before
timing out. Defaults to 120 seconds.
timeout_seconds – The number of seconds to wait for a response before
timing out. Defaults to 120 seconds.
Stores metadata about the script’s progress. Only one instance is created.
Append a json payload to the end of a jsonl file.
- data – The data to append.
data – The data to append.
- filename – The file to append to.
filename – The file to append to.
Make asynchronous requests to the OpenAI API while
throttling to stay under rate limits.
Features:
- Makes requests concurrently, to maximize throughput
- Throttles request and token usage, to stay under rate limits
- Retries failed requests up to {max_attempts} times, to avoid missing data
- Logs errors, to diagnose problems with requests
- requests – List[ChatCompletionRequest]
The requests to process, see ChatCompletionRequest class for details.
Duplicate requests are not allowed.
requests – List[ChatCompletionRequest]
The requests to process, see ChatCompletionRequest class for details.
Duplicate requests are not allowed.
- output_filepath – str, optional
Path to the file where the results will be saved
file will be a jsonl file, where each line is an array with the original
request plus the API response e.g.,
[{“model”: “gpt-4”, “messages”: “…”}, {…}]
if omitted, the results will be saved to a temporary file.
output_filepath – str, optional
Path to the file where the results will be saved
file will be a jsonl file, where each line is an array with the original
request plus the API response e.g.,
[{“model”: “gpt-4”, “messages”: “…”}, {…}]
if omitted, the results will be saved to a temporary file.
- keep_file – bool, optional
Whether to keep the results file after the script finishes, in addition
to the results being returned by the function.
Defaults to False, so the file will be deleted after the script finishes.
Setting this to True is not compatible with output_filepath=None.
keep_file – bool, optional
Whether to keep the results file after the script finishes, in addition
to the results being returned by the function.
Defaults to False, so the file will be deleted after the script finishes.
Setting this to True is not compatible with output_filepath=None.
- max_attempts – int, optional
Number of times to retry a failed request before giving up
if omitted, defaults to 5.
max_attempts – int, optional
Number of times to retry a failed request before giving up
if omitted, defaults to 5.
- rate_limit_headroom_factor – float, optional
Factor to multiply the rate limit by to guarantee that the script
stays under the limit if omitted, defaults to 0.75.
(75% of the rate limit).
rate_limit_headroom_factor – float, optional
Factor to multiply the rate limit by to guarantee that the script
stays under the limit if omitted, defaults to 0.75.
(75% of the rate limit).
- api_key – str, optional
API key to use. If omitted, the function will attempt to read it
from an environment variable OPENAI_API_KEY. If that fails, an error
will be raised, unless all requests are cached.
api_key – str, optional
API key to use. If omitted, the function will attempt to read it
from an environment variable OPENAI_API_KEY. If that fails, an error
will be raised, unless all requests are cached.
- cache – aiohttp_client_cache.CacheBackend, optional
If provided, API responses will be served from the cache if available.
New responses will be saved to the cache.
Check the aiohttp_client_cache documentation for details on the
available cache backends and how to configure them. See https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html .
Each backend has different dependencies. For example, the SQLite
backend requires the package “aiosqlite” to be installed.
cache – aiohttp_client_cache.CacheBackend, optional
If provided, API responses will be served from the cache if available.
New responses will be saved to the cache.
Check the aiohttp_client_cache documentation for details on the
available cache backends and how to configure them. See https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html .
Each backend has different dependencies. For example, the SQLite
backend requires the package “aiosqlite” to be installed.
[LINK: https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html](https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html)
- the original request
the original request
- the API response
the API response
List[Dict[str, Any]]
Check that the cache is configured correctly to work with texttunnel.
Raises a ValueError if the cache is not configured correctly.
cache – The cache to check.
Fetch the API key from the environment variable OPENAI_API_KEY. Raises a
ValueError if the API key is not found.
The API key.
Fetch a response from the cache if it exists.
- cache – Cache to fetch from.
cache – Cache to fetch from.
- url – URL that was requested.
url – URL that was requested.
- request_json – JSON payload that was sent with the request.
request_json – JSON payload that was sent with the request.
The cached response JSON if it exists, otherwise None.
Check if a response conforms to the response JSON schema.
Extract the function call arguments from a response.
response – The response to parse. It should be a list of length 2, where the
first element is the request and the second element is the response.
The function call arguments.
Extract the token usage from a response.
response – The response to parse. It should be a list of length 2, where the
first element is the request and the second element is the response.
The token usage.
Validates the output_filepath and returns a Path object. Uses a temporary file
if output_filepath is None.
- output_filepath – The path to save the results to. If None, a temporary file
will be used.
output_filepath – The path to save the results to. If None, a temporary file
will be used.
- keep_file – Whether to keep the file after the function returns. If True,
output_filepath must not be None.
keep_file – Whether to keep the file after the function returns. If True,
output_filepath must not be None.
A Path object representing the output_filepath.
Make requests to OpenAI. This function is a wrapper around
aprocess_api_requests() that executes it within asyncio.run, saving you the
trouble of having to use asyncio directly.
Note that if you’re running this function in a Jupyter notebook, the function
will automatically import nest_asyncio and call nest_asyncio.apply() to allow
a second event loop to run in the same process. This is necessary because
Jupyter notebooks already run an event loop in the background.
If you require more control over the event loop, use the coroutine
aprocess_api_requests() instead.
- requests – List[ChatCompletionRequest]
The requests to process, see ChatCompletionRequest class for details.
Duplicate requests are not allowed.
requests – List[ChatCompletionRequest]
The requests to process, see ChatCompletionRequest class for details.
Duplicate requests are not allowed.
- output_filepath – str, optional
Path to the file where the results will be saved
file will be a jsonl file, where each line is an array with the original
request plus the API response e.g.,
[{“model”: “gpt-4”, “messages”: “…”}, {…}]
if omitted, the results will be saved to a temporary file.
output_filepath – str, optional
Path to the file where the results will be saved
file will be a jsonl file, where each line is an array with the original
request plus the API response e.g.,
[{“model”: “gpt-4”, “messages”: “…”}, {…}]
if omitted, the results will be saved to a temporary file.
- keep_file – bool, optional
Whether to keep the results file after the script finishes, in addition
to the results being returned by the function.
Defaults to False, so the file will be deleted after the script finishes.
Setting this to True is not compatible with output_filepath=None.
keep_file – bool, optional
Whether to keep the results file after the script finishes, in addition
to the results being returned by the function.
Defaults to False, so the file will be deleted after the script finishes.
Setting this to True is not compatible with output_filepath=None.
- max_attempts – int, optional
Number of times to retry a failed request before giving up
if omitted, will default to 5
max_attempts – int, optional
Number of times to retry a failed request before giving up
if omitted, will default to 5
- rate_limit_headroom_factor – float, optional
Factor to multiply the rate limit by to guarantee that the script
stays under the limit if omitted, will default to 0.75
(75% of the rate limit)
rate_limit_headroom_factor – float, optional
Factor to multiply the rate limit by to guarantee that the script
stays under the limit if omitted, will default to 0.75
(75% of the rate limit)
- api_key – str, optional
API key to use. If omitted, the function will attempt to read it
from an environment variable OPENAI_API_KEY. If that fails, an error
will be raised, unless all requests are cached.
api_key – str, optional
API key to use. If omitted, the function will attempt to read it
from an environment variable OPENAI_API_KEY. If that fails, an error
will be raised, unless all requests are cached.
- cache – aiohttp_client_cache.CacheBackend, optional
If provided, API responses will be served from the cache if available.
New responses will be saved to the cache.
Check the aiohttp_client_cache documentation for details on the
available cache backends and how to configure them. See https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html .
Each backend requires different dependencies. For example, the SQLite
backend requires the package “aiosqlite” to be installed.
cache – aiohttp_client_cache.CacheBackend, optional
If provided, API responses will be served from the cache if available.
New responses will be saved to the cache.
Check the aiohttp_client_cache documentation for details on the
available cache backends and how to configure them. See https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html .
Each backend requires different dependencies. For example, the SQLite
backend requires the package “aiosqlite” to be installed.
[LINK: https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html](https://aiohttp-client-cache.readthedocs.io/en/stable/backends.html)
- the original request
the original request
- the API response
the API response
List[Dict[str, Any]]
Run the main loop that processes API requests. Save results to a file.
- requests_queue – A queue of requests to process.
requests_queue – A queue of requests to process.
- request_url – The URL to send the requests to.
request_url – The URL to send the requests to.
- output_filepath – The path to the file where the results will be saved.
output_filepath – The path to the file where the results will be saved.
- cache – A aiohttp_client_cache.CacheBackend object that stores API
responses. If provided, the response will be stored in the cache.
cache – A aiohttp_client_cache.CacheBackend object that stores API
responses. If provided, the response will be stored in the cache.
- max_attempts – Number of times to retry a failed request before giving up.
max_attempts – Number of times to retry a failed request before giving up.
- rate_limit_headroom_factor – Factor to multiply the rate limit by to
guarantee that the script stays under the limit.
rate_limit_headroom_factor – Factor to multiply the rate limit by to
guarantee that the script stays under the limit.
- api_key – API key to use. If omitted, the function will attempt to read it
from an environment variable OPENAI_API_KEY. If that fails, an error
will be raised, unless all requests are cached.
api_key – API key to use. If omitted, the function will attempt to read it
from an environment variable OPENAI_API_KEY. If that fails, an error
will be raised, unless all requests are cached.
Generate integers 0, 1, 2, and so on.
A generator that yields integers.
Convert token usage to cost in USD.
- usage – The token usage. Retrieve it with parse_token_usage().
usage – The token usage. Retrieve it with parse_token_usage().
- model – The model used to generate the response.
model – The model used to generate the response.
The cost in USD.

## Utils Module 

Binpacks a list of texts into a list of lists of texts, such that each list of texts
has a total number of tokens less than or equal to max_tokens_per_bin and each list of texts
has a number of texts less than or equal to max_texts_per_bin.
The binpacking uses a naive greedy algorithm that maintains the order of the texts.
- texts – List of texts to binpack. Empty texts are accepted, counted as 0 tokens
each and count against max_texts_per_bin.
texts – List of texts to binpack. Empty texts are accepted, counted as 0 tokens
each and count against max_texts_per_bin.
- formatter_function – A function that takes a list of texts and returns a single
text. Defaults to None, which means that the texts are joined with spaces.
This function is used to include the overhead of the formatter function in
the binpacking. It is not used to format the output. Make sure to use
the same formatter function when formatting the output for the model.
formatter_function – A function that takes a list of texts and returns a single
text. Defaults to None, which means that the texts are joined with spaces.
This function is used to include the overhead of the formatter function in
the binpacking. It is not used to format the output. Make sure to use
the same formatter function when formatting the output for the model.
- max_tokens_per_bin – The maximum number of tokens per bin of formatted texts.
Leave some room for relative to the model’s context size to account for the tokens in the
system message, function call, and function return.
max_tokens_per_bin – The maximum number of tokens per bin of formatted texts.
Leave some room for relative to the model’s context size to account for the tokens in the
system message, function call, and function return.
- max_texts_per_bin – The maximum number of texts per list of texts. Defaults to None, which
means that there is no limit on the number of texts per list of texts.
max_texts_per_bin – The maximum number of texts per list of texts. Defaults to None, which
means that there is no limit on the number of texts per list of texts.
- encoding_name – The name of the encoding to use. Defaults to “cl100k_base”.
encoding_name – The name of the encoding to use. Defaults to “cl100k_base”.
- long_text_handling – How to handle texts that are longer than max_tokens_per_bin. Defaults
to “error”, which means that an error is raised. Can also be set to
“truncate”, which means that the text is truncated to max_tokens_per_bin.
It is possible that more tokens are truncated than absolutely necessary
due to overhead of the formatter function caused by escaping characters.
long_text_handling – How to handle texts that are longer than max_tokens_per_bin. Defaults
to “error”, which means that an error is raised. Can also be set to
“truncate”, which means that the text is truncated to max_tokens_per_bin.
It is possible that more tokens are truncated than absolutely necessary
due to overhead of the formatter function caused by escaping characters.
A list of lists of texts. The order of the texts is preserved.
Formats a list of texts into a single string to be used as a user message.
Each text is assigned an ID, starting from 0. The returned JSON format
helps the model distinguish between different texts, at the cost of
increasing the number of tokens used.
The token overhead for a single text that doesn’t require escaping characters
is 12 tokens. Escaping characters like quotes increases the overhead.
The format is a JSON list of dictionaries, where each dictionary has an
“id” key and a “text” key. The “id” key is an integer, and the “text” key
is a string. This array of maps structure is easiest to parse by GPT models
and handles edge cases like newlines in the text.
texts – A list of texts to format.
A formatted string that can be used as a user message.
Simple formatter that joins texts with spaces.
Hashes a dictionary using sha256.
Returns the number of tokens in a string.
- text – The text to count tokens in.
text – The text to count tokens in.
- encoding_name – The name of the token encoding to use. Defaults to “cl100k_base”.
encoding_name – The name of the token encoding to use. Defaults to “cl100k_base”.
The number of tokens in the string.
Truncates a text to a maximum number of tokens.
- text – The text to truncate.
text – The text to truncate.
- max_tokens – The maximum number of tokens to truncate the text to.
max_tokens – The maximum number of tokens to truncate the text to.
- encoding – The encoding to use.
encoding – The encoding to use.
The truncated text.

## Logging 

The package uses the standard logging library and creates a logger named “texttunnel”.
To enable logging, add the following code to your script:

## Indices and tables 

- Index
Index
- Module Index
Module Index
- Search Page
Search Page

--------------------