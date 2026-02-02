# Python Google API Client
**URL:** https://googleapis.dev/python/google-api-core/latest/index.html
**Page Title:** Core — google-api-core documentation
--------------------

[LINK: Python 2 support on Google Cloud](https://cloud.google.com/python/docs/python2-sunset/)
The google-cloud-core package contains helpers common to all google-cloud-* packages. In an attempt to reach a stable API,
much of the functionality has been split out into this package, google-api-core .
Note
Because this client uses grpc library, it is safe to
share instances across threads. In multiprocessing scenarios, the best
practice is to create client instances after the invocation of os.fork() by multiprocessing.pool.Pool or multiprocessing.Process .
[LINK: grpc](https://grpc.github.io/grpc/python/grpc.html#module-grpc)
[LINK: os.fork()](https://docs.python.org/3/library/os.html#os.fork)
[LINK: multiprocessing.pool.Pool](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool)
[LINK: multiprocessing.Process](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process)

## Core ¶

- Authentication Overview Client-Provided Authentication Credential Discovery Precedence Explicit Credentials Google Compute Engine Environment Service Accounts User Accounts (3-legged OAuth 2.0) with a refresh token Troubleshooting Setting up a Service Account Using Google Compute Engine
- Overview
- Client-Provided Authentication Credential Discovery Precedence
- Credential Discovery Precedence
- Explicit Credentials Google Compute Engine Environment Service Accounts User Accounts (3-legged OAuth 2.0) with a refresh token
- Google Compute Engine Environment
- Service Accounts
- User Accounts (3-legged OAuth 2.0) with a refresh token
- Troubleshooting Setting up a Service Account Using Google Compute Engine
- Setting up a Service Account
- Using Google Compute Engine
- Client Information Helpers
- Client Options
- Exceptions
- Futures
- Helpers General Helpers Datetime Helpers gRPC Helpers
- General Helpers
[LINK: General Helpers](helpers.html#module-google.api_core.general_helpers)
- Datetime Helpers
[LINK: Datetime Helpers](helpers.html#module-google.api_core.datetime_helpers)
- gRPC Helpers
[LINK: gRPC Helpers](helpers.html#module-google.api_core.grpc_helpers)
- Identity and Access Management
- Long-Running Operations Long-Running Operations in AsyncIO
- Long-Running Operations in AsyncIO
[LINK: Long-Running Operations in AsyncIO](operation.html#module-google.api_core.operation_async)
- Long-Running Operations Client
- Page Iterators Page Iterators in AsyncIO
- Page Iterators in AsyncIO
[LINK: Page Iterators in AsyncIO](page_iterator.html#module-google.api_core.page_iterator_async)
- Path Templates
- Retry Retry in AsyncIO
- Retry in AsyncIO
- Timeout

## Changelog ¶

- Changelog 2.28.1 (2025-10-28) 2.28.0 (2025-10-24) 2.27.0 (2025-10-22) 2.26.0 (2025-10-08) 2.25.2 (2025-10-01) 2.25.1 (2025-06-02) 2.25.0 (2025-05-06) 2.24.2 (2025-03-06) 2.24.1 (2025-01-24) 2.24.0 (2024-12-06) 2.23.0 (2024-11-11) 2.22.0 (2024-10-25) 2.21.0 (2024-10-07) 2.20.0 (2024-09-18) 2.19.2 (2024-08-16) 2.19.1 (2024-06-19) 2.19.0 (2024-04-29) 2.18.0 (2024-03-20) 2.17.1 (2024-02-13) 2.17.0 (2024-02-06) 2.16.2 (2024-02-02) 2.16.1 (2024-01-30) 2.16.0 (2024-01-29) 2.15.0 (2023-12-07) 2.14.0 (2023-11-09) 2.13.1 (2023-11-09) 2.13.0 (2023-11-03) 2.12.0 (2023-09-07) 2.11.1 (2023-06-12) 2.11.0 (2022-11-10) 2.10.2 (2022-10-08) 2.10.1 (2022-09-14) 2.10.0 (2022-09-02) 2.9.0 (2022-09-01) 2.8.2 (2022-06-13) 2.8.1 (2022-05-26) 2.8.0 (2022-05-18) 2.7.3 (2022-04-29) 2.7.2 (2022-04-13) 2.7.1 (2022-03-09) 2.7.0 (2022-03-08) 2.6.1 (2022-03-05) 2.6.0 (2022-03-03) 2.5.0 (2022-02-02) 2.4.0 (2022-01-11) 2.3.2 (2021-12-16) 2.3.1 (2021-12-15) 2.3.0 (2021-11-25) 2.2.2 (2021-11-02) 2.2.1 (2021-10-26) 2.2.0 (2021-10-25) 2.1.1 (2021-10-13) 2.1.0 (2021-10-05) 2.0.1 (2021-08-31) 2.0.0 (2021-08-18) 2.0.0b1 (2021-08-03) 1.31.1 (2021-07-26) 1.31.0 (2021-07-07) 1.30.0 (2021-06-08) 1.29.0 (2021-06-02) 1.28.0 (2021-05-20) 1.27.0 (2021-05-18) 1.26.3 (2021-03-25) 1.26.2 (2021-03-23) 1.26.1 (2021-02-12) 1.26.0 (2021-02-08) 1.25.1 (2021-01-25) 1.25.0 (2021-01-14) 1.24.1 (2020-12-16) 1.24.0 (2020-12-14) 1.23.0 (2020-10-16) 1.22.4 (2020-10-05) 1.22.3 (2020-10-02) 1.22.2 (2020-09-03) 1.22.1 (2020-08-12) 1.22.0 (2020-07-21) 1.21.0 (2020-06-18) 1.20.1 (2020-06-16) 1.20.0 (2020-06-09) 1.19.1 (2020-06-06) 1.19.0 (2020-06-05) 1.18.0 (2020-06-04) 1.17.0 (2020-04-14) 1.16.0 1.15.0 1.14.3 1.14.2 1.14.1 1.14.0 1.13.0 1.12.0 1.11.1 1.11.0 1.10.0 1.9.0 1.8.2 1.8.1 1.8.0 1.7.0 1.6.0 1.5.2 1.5.1 1.5.0 1.4.1 1.4.0 1.3.0 1.2.1 1.2.0 1.1.2 1.1.1 1.1.0 1.0.0 0.1.4 0.1.3 0.1.2 0.1.1 0.1.0
- 2.28.1 (2025-10-28)
- 2.28.0 (2025-10-24)
- 2.27.0 (2025-10-22)
- 2.26.0 (2025-10-08)
- 2.25.2 (2025-10-01)
- 2.25.1 (2025-06-02)
- 2.25.0 (2025-05-06)
- 2.24.2 (2025-03-06)
- 2.24.1 (2025-01-24)
- 2.24.0 (2024-12-06)
- 2.23.0 (2024-11-11)
- 2.22.0 (2024-10-25)
- 2.21.0 (2024-10-07)
- 2.20.0 (2024-09-18)
- 2.19.2 (2024-08-16)
- 2.19.1 (2024-06-19)
- 2.19.0 (2024-04-29)
- 2.18.0 (2024-03-20)
- 2.17.1 (2024-02-13)
- 2.17.0 (2024-02-06)
- 2.16.2 (2024-02-02)
- 2.16.1 (2024-01-30)
- 2.16.0 (2024-01-29)
- 2.15.0 (2023-12-07)
- 2.14.0 (2023-11-09)
- 2.13.1 (2023-11-09)
- 2.13.0 (2023-11-03)
- 2.12.0 (2023-09-07)
- 2.11.1 (2023-06-12)
- 2.11.0 (2022-11-10)
- 2.10.2 (2022-10-08)
- 2.10.1 (2022-09-14)
- 2.10.0 (2022-09-02)
- 2.9.0 (2022-09-01)
- 2.8.2 (2022-06-13)
- 2.8.1 (2022-05-26)
- 2.8.0 (2022-05-18)
- 2.7.3 (2022-04-29)
- 2.7.2 (2022-04-13)
- 2.7.1 (2022-03-09)
- 2.7.0 (2022-03-08)
- 2.6.1 (2022-03-05)
- 2.6.0 (2022-03-03)
- 2.5.0 (2022-02-02)
- 2.4.0 (2022-01-11)
- 2.3.2 (2021-12-16)
- 2.3.1 (2021-12-15)
- 2.3.0 (2021-11-25)
- 2.2.2 (2021-11-02)
- 2.2.1 (2021-10-26)
- 2.2.0 (2021-10-25)
- 2.1.1 (2021-10-13)
- 2.1.0 (2021-10-05)
- 2.0.1 (2021-08-31)
- 2.0.0 (2021-08-18)
- 2.0.0b1 (2021-08-03)
- 1.31.1 (2021-07-26)
- 1.31.0 (2021-07-07)
- 1.30.0 (2021-06-08)
- 1.29.0 (2021-06-02)
- 1.28.0 (2021-05-20)
- 1.27.0 (2021-05-18)
- 1.26.3 (2021-03-25)
- 1.26.2 (2021-03-23)
- 1.26.1 (2021-02-12)
- 1.26.0 (2021-02-08)
- 1.25.1 (2021-01-25)
- 1.25.0 (2021-01-14)
- 1.24.1 (2020-12-16)
- 1.24.0 (2020-12-14)
- 1.23.0 (2020-10-16)
- 1.22.4 (2020-10-05)
- 1.22.3 (2020-10-02)
- 1.22.2 (2020-09-03)
- 1.22.1 (2020-08-12)
- 1.22.0 (2020-07-21)
- 1.21.0 (2020-06-18)
- 1.20.1 (2020-06-16)
- 1.20.0 (2020-06-09)
- 1.19.1 (2020-06-06)
- 1.19.0 (2020-06-05)
- 1.18.0 (2020-06-04)
- 1.17.0 (2020-04-14)
- 1.16.0
- 1.15.0
- 1.14.3
- 1.14.2
- 1.14.1
- 1.14.0
- 1.13.0
- 1.12.0
- 1.11.1
- 1.11.0
- 1.10.0
- 1.9.0
- 1.8.2
- 1.8.1
- 1.8.0
- 1.7.0
- 1.6.0
- 1.5.2
- 1.5.1
- 1.5.0
- 1.4.1
- 1.4.0
- 1.3.0
- 1.2.1
- 1.2.0
- 1.1.2
- 1.1.1
- 1.1.0
- 1.0.0
- 0.1.4
- 0.1.3
- 0.1.2
- 0.1.1
- 0.1.0

## google-api-core

Google Cloud Client Libraries for google-api-core

### Navigation

- Authentication
- Client Information Helpers
- Client Options
- Exceptions
- Futures
- Helpers
- Identity and Access Management
- Long-Running Operations
- Long-Running Operations Client
- Page Iterators
- Path Templates
- Retry
- Timeout
- Changelog

### Related Topics

- Documentation overview Next: Authentication
- Next: Authentication

### Quick search

[LINK: Alabaster 0.7.16](https://alabaster.readthedocs.io)
Warning: This is not the latest release.
- Permalink
[LINK: Permalink](https://googleapis.dev/python/google-api-core/2.28.1/index.html)
- Report issue
- Product docs
- GitHub
[LINK: GitHub](https://github.com/googleapis/python-api-core)

--------------------