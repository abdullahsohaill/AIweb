# Google AI Studio
**URL:** https://ai.google.dev/gemini-api/docs/api-key
**Page Title:** Using Gemini API keys  |  Google AI for Developers
--------------------

- English
[LINK: English](https://ai.google.dev/gemini-api/docs/api-key)
- Deutsch
[LINK: Deutsch](https://ai.google.dev/gemini-api/docs/api-key?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419)
- Français
[LINK: Français](https://ai.google.dev/gemini-api/docs/api-key?hl=fr)
- Indonesia
[LINK: Indonesia](https://ai.google.dev/gemini-api/docs/api-key?hl=id)
- Italiano
[LINK: Italiano](https://ai.google.dev/gemini-api/docs/api-key?hl=it)
- Polski
[LINK: Polski](https://ai.google.dev/gemini-api/docs/api-key?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br)
- Shqip
[LINK: Shqip](https://ai.google.dev/gemini-api/docs/api-key?hl=sq)
- Tiếng Việt
[LINK: Tiếng Việt](https://ai.google.dev/gemini-api/docs/api-key?hl=vi)
- Türkçe
[LINK: Türkçe](https://ai.google.dev/gemini-api/docs/api-key?hl=tr)
- Русский
[LINK: Русский](https://ai.google.dev/gemini-api/docs/api-key?hl=ru)
- עברית
[LINK: עברית](https://ai.google.dev/gemini-api/docs/api-key?hl=he)
- العربيّة
[LINK: العربيّة](https://ai.google.dev/gemini-api/docs/api-key?hl=ar)
- فارسی
[LINK: فارسی](https://ai.google.dev/gemini-api/docs/api-key?hl=fa)
- हिंदी
[LINK: हिंदी](https://ai.google.dev/gemini-api/docs/api-key?hl=hi)
- বাংলা
[LINK: বাংলা](https://ai.google.dev/gemini-api/docs/api-key?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://ai.google.dev/gemini-api/docs/api-key?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw)
- 日本語
[LINK: 日本語](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)
- 한국어
[LINK: 한국어](https://ai.google.dev/gemini-api/docs/api-key?hl=ko)
[LINK: Get API key](https://aistudio.google.com/apikey)
[LINK: Cookbook](https://github.com/google-gemini/cookbook)
[LINK: Community](https://discuss.ai.google.dev/c/gemini-api/)
[LINK: Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fapi-key&prompt=select_account)
- On this page
- API Keys
[LINK: API Keys](#api-keys)
- Google Cloud projects Default project
- Default project
- Import projects
- Limitations
- Setting the API key as an environment variable
[LINK: Setting the API key as an environment variable](#set-api-env-var)
- Providing the API key explicitly
[LINK: Providing the API key explicitly](#provide-api-key-explicitly)
- Keep your API key secure Critical security rules Best practices
- Critical security rules
- Best practices
- Home
- Gemini API
[LINK: Gemini API](https://ai.google.dev/gemini-api)
- Docs
[LINK: Docs](https://ai.google.dev/gemini-api/docs)

## Using Gemini API keys

- On this page
- API Keys
[LINK: API Keys](#api-keys)
- Google Cloud projects Default project
- Default project
- Import projects
- Limitations
- Setting the API key as an environment variable
[LINK: Setting the API key as an environment variable](#set-api-env-var)
- Providing the API key explicitly
[LINK: Providing the API key explicitly](#provide-api-key-explicitly)
- Keep your API key secure Critical security rules Best practices
- Critical security rules
- Best practices
To use the Gemini API, you need an API key. This page outlines how to create and
manage your keys in Google AI Studio as well as how to set up your environment
to use them in your code.
Create or view a Gemini API Key
[LINK: Create or view a Gemini API Key](https://aistudio.google.com/app/apikey)

## API Keys

You can create and manage all your Gemini API Keys from the Google AI Studio API Keys page.
[LINK: Google AI Studio](https://aistudio.google.com/app/apikey)
Once you have an API key, you have the following options to connect to the
Gemini API:
- Setting your API key as an environment variable
[LINK: Setting your API key as an environment variable](#set-api-env-var)
- Providing your API key explicitly
[LINK: Providing your API key explicitly](#provide-api-key-explicitly)
For initial testing, you can hard code an API key, but this should only be
temporary since it's not secure. You can find examples for hard coding the API
key in Providing API key explicitly section.
[LINK: Providing API key explicitly](#provide-api-key-explicitly)

## Google Cloud projects

Google Cloud projects are fundamental to using Google Cloud services (such as the Gemini API),
managing billing, and controlling collaborators and permissions. Google AI
Studio provides a lightweight interface to your Google Cloud projects.
[LINK: Google Cloud projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
If you don't have
any projects created yet, you must either create a new project or import one
from Google Cloud into Google AI Studio. The Projects page in Google AI
Studio will display all keys that have sufficient permission to use the Gemini
API. Refer to the import projects section for instructions.

### Default project

For new users, after accepting Terms of Service, Google AI Studio creates a
default Google Cloud Project and API Key, for ease of use. You can rename this
project in Google AI Studio by navigating to Projects view in the Dashboard , clicking the 3 dots settings button next to a project and
choosing Rename project . Existing users, or users who already have Google
Cloud Accounts won't have a default project created.

## Import projects

Each Gemini API key is associated with a Google Cloud project. By default,
Google AI Studio does not show all of your Cloud Projects. You must import the
projects you want by searching for the name or project ID in the Import Projects dialog. To view a complete list of projects you have access
to, visit the Cloud Console.
If you don't have any projects imported yet, follow these steps to import a
Google Cloud project and create a key:
- Go to Google AI Studio .
- Open the Dashboard from the left side panel.
- Select Projects .
- Select the Import projects button in the Projects page.
- Search for and select the Google Cloud project you want to import and select
the Import button.
Once a project is imported, go to the API Keys page from the Dashboard menu and create an API key in the project you just imported.

## Limitations

The following are limitations of managing API keys and Google Cloud projects in
Google AI Studio.
- You can create a maximum of 10 project at a time from the Google AI Studio Projects page.
- You can name and rename projects and keys.
- The API keys and Projects pages display a maximum of 100 keys and
50 projects.
- Only API keys that have no restrictions, or are restricted to the Generative
Language API are displayed.
For additional management access to your projects, visit the Google Cloud Console.

## Setting the API key as an environment variable

If you set the environment variable GEMINI_API_KEY or GOOGLE_API_KEY , the
API key will automatically be picked up by the client when using one of the Gemini API libraries . It's recommended that you
set only one of those variables, but if both are set, GOOGLE_API_KEY takes
precedence.
[LINK: Gemini API libraries](/gemini-api/docs/libraries)
If you're using the REST API, or JavaScript on the browser, you will need to
provide the API key explicitly.
Here is how you can set your API key locally as the environment variable GEMINI_API_KEY with different operating systems.
Bash is a common Linux and macOS terminal configuration. You can check if
you have a configuration file for it by running the following command:
If the response is "No such file or directory", you will need to create this
file and open it by running the following commands, or use zsh :
Next, you need to set your API key by adding the following export command:
After saving the file, apply the changes by running:
Zsh is a common Linux and macOS terminal configuration. You can check if
you have a configuration file for it by running the following command:
If the response is "No such file or directory", you will need to create this
file and open it by running the following commands, or use bash :
Next, you need to set your API key by adding the following export command:
After saving the file, apply the changes by running:
- Search for "Environment Variables" in the search bar.
- Choose to modify System Settings . You may have to confirm you want to
do this.
- In the system settings dialog, click the button labeled Environment
Variables .
- Under either User variables (for the current user) or System
variables (applies to all users who use the machine), click New...
- Specify the variable name as GEMINI_API_KEY . Specify your Gemini API
Key as the variable value.
- Click OK to apply the changes.
- Open a new terminal session (cmd or Powershell) to get the new variable.

## Providing the API key explicitly

In some cases, you may want to explicitly provide an API key. For example:
- You're doing a simple API call and prefer hard coding the API key.
- You want explicit control without having to rely on automatic discovery of
environment variables by the Gemini API libraries
- You're using an environment where environment variables are not supported
(e.g web) or you are making REST calls.
Below are examples for how you can provide an API key explicitly:

## Keep your API key secure

Treat your Gemini API key like a password. If compromised, others can use your
project's quota, incur charges (if billing is enabled), and access your
private data, such as files.

### Critical security rules

- Keep keys confidential : API keys for Gemini may access sensitive data your
application depends upon. Never commit API keys to source control. Do not check your API key into version control systems like Git. Never expose API keys on the client-side. Do not use your API key directly
in web or mobile apps in production. Keys in client-side code
(including our JavaScript/TypeScript libraries and REST calls) can be
extracted.
Keep keys confidential : API keys for Gemini may access sensitive data your
application depends upon.
- Never commit API keys to source control. Do not check your API key into version control systems like Git.
Never commit API keys to source control. Do not check your API key into version control systems like Git.
- Never expose API keys on the client-side. Do not use your API key directly
in web or mobile apps in production. Keys in client-side code
(including our JavaScript/TypeScript libraries and REST calls) can be
extracted.
Never expose API keys on the client-side. Do not use your API key directly
in web or mobile apps in production. Keys in client-side code
(including our JavaScript/TypeScript libraries and REST calls) can be
extracted.
- Restrict access : Restrict API key usage to specific IP addresses, HTTP
referrers, or Android/iOS apps where possible.
Restrict access : Restrict API key usage to specific IP addresses, HTTP
referrers, or Android/iOS apps where possible.
- Restrict usage : Enable only the necessary APIs for each key.
Restrict usage : Enable only the necessary APIs for each key.
- Perform regular audits : Regularly audit your API keys and rotate them
periodically.
Perform regular audits : Regularly audit your API keys and rotate them
periodically.

### Best practices

- Use server-side calls with API keys The most secure way to use your API
key is to call the Gemini API from a server-side application where the key
can be kept confidential.
Use server-side calls with API keys The most secure way to use your API
key is to call the Gemini API from a server-side application where the key
can be kept confidential.
- Use ephemeral tokens for client-side access (Live API only): For direct
client-side access to the Live API, you can use ephemeral tokens. They come with
lower security risks and can be suitable for production use. Review ephemeral tokens guide for more information.
Use ephemeral tokens for client-side access (Live API only): For direct
client-side access to the Live API, you can use ephemeral tokens. They come with
lower security risks and can be suitable for production use. Review ephemeral tokens guide for more information.
[LINK: ephemeral tokens](/gemini-api/docs/ephemeral-tokens)
- Consider adding restrictions to your key: You can limit a key's permissions
by adding API key restrictions .
This minimizes the potential damage if the key is ever leaked.
Consider adding restrictions to your key: You can limit a key's permissions
by adding API key restrictions .
This minimizes the potential damage if the key is ever leaked.
[LINK: API key restrictions](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys#add-api-restrictions)
For some general best practices, you can also review this support article .
[LINK: support article](https://support.google.com/googleapi/answer/6310037)
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2026-01-19 UTC.

--------------------