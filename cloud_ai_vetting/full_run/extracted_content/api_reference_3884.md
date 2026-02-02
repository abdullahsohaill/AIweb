# API Reference
**URL:** https://dev.hume.ai/reference/empathic-voice-interface-evi/tools/list-tools
**Page Title:** List tools | Hume API
--------------------

Fetches a paginated list of Tools .
Refer to our tool use guide for comprehensive instructions on defining and integrating tools into EVI.
[LINK: tool use](/docs/speech-to-speech-evi/features/tool-use#function-calling)

### Authentication

### Query parameters

Specifies the page number to retrieve, enabling pagination.
This parameter uses zero-based indexing. For example, setting page_number to 0 retrieves the first page of results (items 0-9 if page_size is 10), setting page_number to 1 retrieves the second page (items 10-19), and so on. Defaults to 0, which retrieves the first page.
Specifies the maximum number of results to include per page, enabling pagination. The value must be between 1 and 100, inclusive.
For example, if page_size is set to 10, each page will include up to 10 items. Defaults to 10.
By default, restrict_to_most_recent is set to true, returning only the latest version of each tool. To include all versions of each tool in the list, set restrict_to_most_recent to false.

### Response

The page number of the returned list.
This value corresponds to the page_number parameter specified in the request. Pagination uses zero-based indexing.
The maximum number of items returned per page.
This value corresponds to the page_size parameter specified in the request.
List of tools returned for the specified page_number and page_size .

--------------------