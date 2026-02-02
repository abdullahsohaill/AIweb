# instructions
**URL:** https://huggingface.co/docs/huggingface_hub/en/quick-start
**Page Title:** Quickstart
--------------------

Hub Python Library documentation
Quickstart

## Hub Python Library

[LINK: 3,282](https://github.com/huggingface/huggingface_hub)
and get access to the augmented documentation experience
to get started

## Quickstart

The Hugging Face Hub is the go-to place for sharing machine learning
models, demos, datasets, and metrics. huggingface_hub library helps you interact with
the Hub without leaving your development environment. You can create and manage
repositories easily, download and upload files, and get useful model and dataset
metadata from the Hub.

## Installation

To get started, install the huggingface_hub library:
For more details, check out the installation guide.

## Download files

Repositories on the Hub are git version controlled, and users can download a single file
or the whole repository. You can use the hf_hub_download() function to download files.
This function will download and cache a file on your local disk. The next time you need
that file, it will load from your cache, so you don’t need to re-download it.
[LINK: hf_hub_download()](/docs/huggingface_hub/v1.3.3/en/package_reference/file_download#huggingface_hub.hf_hub_download)
You will need the repository id and the filename of the file you want to download. For
example, to download the Pegasus model
configuration file:
To download a specific version of the file, use the revision parameter to specify the
branch name, tag, or commit hash. If you choose to use the commit hash, it must be the
full-length hash instead of the shorter 7-character commit hash:
For more details and options, see the API reference for hf_hub_download() .
[LINK: hf_hub_download()](/docs/huggingface_hub/v1.3.3/en/package_reference/file_download#huggingface_hub.hf_hub_download)

## Authentication

In a lot of cases, you must be authenticated with a Hugging Face account to interact with
the Hub: download private repos, upload files, create PRs,… Create an account if you don’t already have one, and then sign in
to get your User Access Token from
your Settings page . The User Access Token is
used to authenticate your identity to the Hub.
[LINK: User Access Token](https://huggingface.co/docs/hub/security-tokens)
Tokens can have read or write permissions. Make sure to have a write access token if you want to create or edit a repository. Otherwise, it’s best to generate a read token to reduce risk in case your token is inadvertently leaked.

### Login command

The easiest way to authenticate is to save the token on your machine. You can do that from the terminal using the login() command:
[LINK: login()](/docs/huggingface_hub/v1.3.3/en/package_reference/authentication#huggingface_hub.login)
The command will tell you if you are already logged in and prompt you for your token. The token is then validated and saved in your HF_HOME directory (defaults to ~/.cache/huggingface/token ). Any script or library interacting with the Hub will use this token when sending requests.
Alternatively, you can programmatically log in using login() in a notebook or a script:
[LINK: login()](/docs/huggingface_hub/v1.3.3/en/package_reference/authentication#huggingface_hub.login)
You can only be logged in to one account at a time. Logging in to a new account will automatically log you out of the previous one. To determine your currently active account, simply run the hf auth whoami command.
Once logged in, all requests to the Hub - even methods that don’t necessarily require authentication - will use your access token by default. If you want to disable the implicit use of your token, you should set HF_HUB_DISABLE_IMPLICIT_TOKEN=1 as an environment variable (see reference ).

### Manage multiple tokens locally

You can save multiple tokens on your machine by simply logging in with the login() command with each token. If you need to switch between these tokens locally, you can use the auth switch command:
[LINK: login()](/docs/huggingface_hub/v1.3.3/en/package_reference/authentication#huggingface_hub.login)
This command will prompt you to select a token by its name from a list of saved tokens. Once selected, the chosen token becomes the active token, and it will be used for all interactions with the Hub.
You can list all available access tokens on your machine with hf auth list .

### Environment variable

The environment variable HF_TOKEN can also be used to authenticate yourself. This is especially useful in a Space where you can set HF_TOKEN as a Space secret .
[LINK: Space secret](https://huggingface.co/docs/hub/spaces-overview#managing-secrets)
NEW: Google Colaboratory lets you define private keys for your notebooks. Define a HF_TOKEN secret to be automatically authenticated!
Authentication via an environment variable or a secret has priority over the token stored on your machine.

### Method parameters

Finally, it is also possible to authenticate by passing your token to any method that accepts token as a parameter.
This is usually discouraged except in an environment where you don’t want to store your token permanently or if you need to handle several tokens at once.
Please be careful when passing tokens as a parameter. It is always best practice to load the token from a secure vault instead of hardcoding it in your codebase or notebook. Hardcoded tokens present a major leak risk if you share your code inadvertently.

## Create a repository

Once you’ve registered and logged in, create a repository with the create_repo() function:
[LINK: create_repo()](/docs/huggingface_hub/v1.3.3/en/package_reference/hf_api#huggingface_hub.HfApi.create_repo)
If you want your repository to be private, then:
Private repositories will not be visible to anyone except yourself.
To create a repository or to push content to the Hub, you must provide a User Access
Token that has the write permission. You can choose the permission when creating the
token in your Settings page .

## Upload files

Use the upload_file() function to add a file to your newly created repository. You
need to specify:
[LINK: upload_file()](/docs/huggingface_hub/v1.3.3/en/package_reference/hf_api#huggingface_hub.HfApi.upload_file)
- The path of the file to upload.
- The path of the file in the repository.
- The repository id of where you want to add the file.
To upload more than one file at a time, take a look at the Upload guide
which will introduce you to several methods for uploading files (with or without git).

## Next steps

The huggingface_hub library provides an easy way for users to interact with the Hub
with Python. To learn more about how you can manage your files and repositories on the
Hub, we recommend reading our how-to guides to:
- Manage your repository .
- Download files from the Hub.
- Upload files to the Hub.
- Search the Hub for your desired model or dataset.
- Run Inference across multiple services for models hosted on the Hugging Face Hub.
[LINK: Update on GitHub](https://github.com/huggingface/huggingface_hub/blob/main/docs/source/en/quick-start.md)
[LINK: ← Home](/docs/huggingface_hub/en/index)
[LINK: Installation →](/docs/huggingface_hub/en/installation)

--------------------