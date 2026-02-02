# GitLab Code Suggestions
**URL:** https://docs.gitlab.com/ee/user/project/repository/code_suggestions.html
**Page Title:** Code Suggestions | GitLab Docs
--------------------


## Code Suggestions

- Tier : Premium, Ultimate
- Add-on : GitLab Duo Core, Pro, or Enterprise, GitLab Duo with Amazon Q
- Offering : GitLab.com, GitLab Self-Managed, GitLab Dedicated
- Default LLM
- LLM for Amazon Q: Amazon Q Developer
- Available on GitLab Duo with self-hosted models
- Introduced support for Google Vertex AI Codey APIs in GitLab 16.1.
- Removed support for GitLab native model in GitLab 16.2.
- Introduced support for code generation in GitLab 16.3.
- Generally available in GitLab 16.7.
- Changed to require the GitLab Duo Pro add-on on February 15, 2024. Previously, this feature was included with Premium and Ultimate subscriptions.
- Changed to require the GitLab Duo Pro or GitLab Duo Enterprise add-on for all supported GitLab versions starting October 17, 2024.
- Introduced support for Fireworks AI-hosted Qwen2.5 code completion model in GitLab 17.6, with a flag named fireworks_qwen_code_completion .
- Removed support for Qwen2.5 code completion model in GitLab 17.11.
- Enabled Fireworks hosted Codestral by default via the feature flag use_fireworks_codestral_code_completion in GitLab 17.11.
- Changed to include GitLab Duo Core in GitLab 18.0.
- Enabled Fireworks hosted Codestral as the default model in GitLab 18.1.
- To opt out of Fireworks for a group, the feature flag code_completion_opt_out_fireworks is available.
- Changed the default model for code generation to Claude Sonnet 4 in GitLab 18.2.
- Removed feature flag code_suggestions_context in GitLab 18.6.
Use GitLab Duo Code Suggestions to write code more efficiently by using generative AI to suggest code while you’re developing.
- View a click-through demo .
- Watch an overview

## Prerequisites

To use Code Suggestions:
- If you have the GitLab Duo Core add-on, turn on IDE features .
- Set up Code Suggestions .
GitLab Duo requires GitLab 17.2 or later. For GitLab Duo Core access, and for the best user experience and results, upgrade to GitLab 18.0 or later . Earlier versions might continue to work, however the experience might be degraded.

## Use Code Suggestions

To use Code Suggestions:
- Open your Git project in a supported IDE .
Open your Git project in a supported IDE .
- Add the project as a remote of your local repository using git remote add .
Add the project as a remote of your local repository using git remote add .
- Add your project directory, including the hidden .git/ folder, to your IDE workspace or project.
Add your project directory, including the hidden .git/ folder, to your IDE workspace or project.
- Author your code.
As you type, suggestions are displayed. Code Suggestions provides code snippets
or completes the current line, depending on the cursor position.
Author your code.
As you type, suggestions are displayed. Code Suggestions provides code snippets
or completes the current line, depending on the cursor position.
- Describe the requirements in natural language.
Code Suggestions generates functions and code snippets based on the context provided.
Describe the requirements in natural language.
Code Suggestions generates functions and code snippets based on the context provided.
- When you receive a suggestion, you can do any of the following: To accept a suggestion, press Tab . To accept a partial suggestion, press either Control + Right arrow or Command + Right arrow . To reject a suggestion, press Esc . In Neovim, press Control + E to exit the menu. To ignore a suggestion, keep typing as you usually would.
When you receive a suggestion, you can do any of the following:
- To accept a suggestion, press Tab .
- To accept a partial suggestion, press either Control + Right arrow or Command + Right arrow .
- To reject a suggestion, press Esc . In Neovim, press Control + E to exit the menu.
- To ignore a suggestion, keep typing as you usually would.

## View multiple code suggestions

- Introduced in GitLab 17.1.
For a code completion suggestion in VS Code, multiple suggestion options
might be available. To view all available suggestions:
- Hover over the code completion suggestion.
- Scroll through the alternatives. Either: Use keyboard shortcuts: On a Mac, press Option + [ to view the previous suggestion,
and press Option + ] to view the next suggestion. On Linux and Windows, press Alt + [ to view the previous suggestion,
and press Alt + ] to view the next suggestion. On the dialog that’s displayed, select the right or left arrow to see next or previous options.
- Use keyboard shortcuts: On a Mac, press Option + [ to view the previous suggestion,
and press Option + ] to view the next suggestion. On Linux and Windows, press Alt + [ to view the previous suggestion,
and press Alt + ] to view the next suggestion.
- On a Mac, press Option + [ to view the previous suggestion,
and press Option + ] to view the next suggestion.
- On Linux and Windows, press Alt + [ to view the previous suggestion,
and press Alt + ] to view the next suggestion.
- On the dialog that’s displayed, select the right or left arrow to see next or previous options.
- Press Tab to apply the suggestion you prefer.

## Code completion and generation

Code Suggestions uses code completion and code generation:
Code Suggestions always uses both of these features. You cannot use only code
generation or only code completion.
View a code completion vs. code generation comparison demo .

### Best practices for code generation

To get the best results from code generation:
- Be as specific as possible while remaining concise.
- State the outcome you want to generate (for example, a function)
and provide details on what you want to achieve.
- Add additional information, like the framework or library you want to use.
- Add a space or new line after each comment.
This space tells the code generator that you have completed your instructions.
- Review and adjust the context available to Code Suggestions .
For example, to create a Python web service with some specific requirements,
you might write something like:
AI is non-deterministic, so you may not get the same suggestion every time with the same input.
To generate quality code, write clear, descriptive, specific tasks.
For use cases and best practices, follow the GitLab Duo examples documentation .

## Truncation of file content

Because of LLM limits and performance reasons, the content of the currently
opened file is truncated:
- For code completion: to 32,000 tokens (roughly 128,000 characters).
- For code generation: to 80,000 tokens (roughly 320,000 characters).
Content above the cursor is prioritized over content below the cursor. The content
above the cursor is truncated from the left side, and content below the cursor
is truncated from the right side. These numbers represent the maximum input context
size for Code Suggestions.
Support for increasing the code generation limit is proposed in issue 585841 .

## Output length

Because of LLM limits and for performance reasons, the output of Code Suggestions
is limited:
- For code completion: to 64 tokens (roughly 256 characters).
- For code generation: to 2048 tokens (roughly 7168 characters).

## Accuracy of results

We are continuing to work on the accuracy of overall generated content.
However, Code Suggestions might generate suggestions that are:
- Irrelevant.
- Incomplete.
- Likely to result in failed pipelines.
- Potentially insecure.
- Offensive or insensitive.
When using Code Suggestions, code review best practices still apply.

## Available language models

Different language models can be the source for Code Suggestions.
- On GitLab.com: GitLab hosts the models and connects to them through the cloud-based AI Gateway.
- On GitLab Self-Managed, two options exist: GitLab can host the models and connects to them through the cloud-based AI Gateway . Your organization can use GitLab Duo Self-Hosted ,
which means you host the AI Gateway and language models. You can use GitLab AI vendor models,
other supported language models, or to bring your own compatible model.
- GitLab can host the models and connects to them through the cloud-based AI Gateway .
- Your organization can use GitLab Duo Self-Hosted ,
which means you host the AI Gateway and language models. You can use GitLab AI vendor models,
other supported language models, or to bring your own compatible model.

## How the prompt is built

To learn about the code that builds the prompt, see these files:
- Code generation: ee/lib/api/code_suggestions.rb in the gitlab repository.
[LINK: ee/lib/api/code_suggestions.rb](https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/lib/api/code_suggestions.rb#L76)
- Code completion: ai_gateway/code_suggestions/processing/completions.py in the modelops repository.

## Prompt caching

- Introduced in GitLab 18.0.
Prompt caching is enabled by default to improve Code Suggestions latency. When prompt caching is enabled, code completion prompt data is temporarily stored in memory by the model vendor. Prompt caching significantly improves latency by avoiding the re-processing of cached prompt and input data. The cached data is never logged to any persistent storage.

### Turn off prompt caching

You can turn off prompt caching for top-level groups in the GitLab Duo settings.
This also turns off prompt caching for GitLab Duo Chat (Agentic) .
Prerequisites:
- Administrator access for GitLab Self-Managed.
On GitLab.com:
- On the top bar, select Search or go to and find your group.
- Select Settings > GitLab Duo .
- Select Change configuration .
- Disable the Prompt caching toggle.
- Select Save changes .
On GitLab Self-Managed:
- In the upper-right corner, select Admin .
- On the left sidebar, select GitLab Duo .
- Select Change configuration .
- Under Prompt cache , clear the Turn on prompt caching checkbox.
- Select Save changes .

## Response time

Code Suggestions is powered by a generative AI model.
- For code completion, suggestions are usually low latency and take less than one second.
- For code generation, algorithms or large code blocks might take more than five seconds to generate.
Your personal access token enables a secure API connection to GitLab.com or to your GitLab instance.
This API connection securely transmits a context window from your IDE/editor to the GitLab AI Gateway , a GitLab hosted service. The gateway calls the large language model APIs, and then the generated suggestion is transmitted back to your IDE/editor.

### Streaming

Streaming of code generation responses is supported in JetBrains and Visual Studio, leading to
perceived faster response times.
Other supported IDEs will return the generated code in a single block.
Streaming is not enabled for code completion.

### Direct and indirect connections

- Introduced in GitLab 17.2 with a flag named code_suggestions_direct_access . Disabled by default.
By default, code completion requests are sent from the IDE directly to the AI Gateway to minimize the latency.
For this direct connection to work, the IDE must be able to connect to https://cloud.gitlab.com:443 . If this is not
possible (for example, because of network restrictions), you can disable direct connections for all users. If you do this,
code completion requests are sent indirectly through the GitLab Self-Managed instance, which in turn sends the requests
to the AI Gateway. This might result in your requests having higher latency.
Prerequisites:
- You must be an administrator for the GitLab Self-Managed instance.
- In 17.4 and later
- In 17.3 and earlier
- In the upper-right corner, select Admin .
- Select Settings > General .
- Expand GitLab Duo features .
- Under Connection method , choose an option: To minimize latency for code completion requests, select Direct connections . To disable direct connections for all users, select Indirect connections through GitLab Self-Managed .
- To minimize latency for code completion requests, select Direct connections .
- To disable direct connections for all users, select Indirect connections through GitLab Self-Managed .
- Select Save changes .
- In the upper-right corner, select Admin .
- Select Settings > General .
- Expand AI-native features .
- Choose an option: To enable direct connections and minimize latency for code completion requests, clear the Disable direct connections for code suggestions checkbox. To disable direct connections, select the Disable direct connections for code suggestions checkbox.
- To enable direct connections and minimize latency for code completion requests, clear the Disable direct connections for code suggestions checkbox.
- To disable direct connections, select the Disable direct connections for code suggestions checkbox.

## Feedback

Provide feedback about your Code Suggestions experience in issue 435783 .
- Open in Web IDE . Quickly and easily edit multiple files. View page source Edit this file only. Create an issue Suggest improvements.
- Open in Web IDE . Quickly and easily edit multiple files.
- View page source Edit this file only.
- Create an issue Suggest improvements.

## Privacy Preference Center

## Privacy Preference Center

- Your Privacy

### Your Privacy

- Strictly Necessary Cookies

### Strictly Necessary Cookies

- Functionality Cookies

### Functionality Cookies

- Performance and Analytics Cookies

### Performance and Analytics Cookies

- Targeting and Advertising Cookies

### Targeting and Advertising Cookies

- Ad User Data

### Ad User Data

- Ad Personalization

### Ad Personalization

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. Cookie Policy User ID: 19f31325-2893-4cd7-afe4-87a1c07b31a8 This User ID will be used as a unique identifier while storing and accessing your preferences for future. Timestamp: --
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, enabling you to securely log into the site, filling in forms, or using the customer checkout.  GitLab processes any personal data collected through these cookies on the basis of our legitimate interest.
These cookies enable helpful but non-essential website functions that improve your website experience. By recognizing you when you return to our website, they may, for example, allow us to personalize our content for you or remember your preferences. If you do not allow these cookies then some or all of these services may not function properly.  GitLab processes any personal data collected through these cookies on the basis of your consent
These cookies allow us and our third-party service providers to recognize and count the number of visitors on our websites and to see how visitors move around our websites when they are using it. This helps us improve our products and ensures that users can easily find what they need on our websites. These cookies usually generate aggregate statistics that are not associated with an individual.  To the extent any personal data is collected through these cookies, GitLab processes that data on the basis of your consent.
These cookies enable different advertising related functions.  They may allow us to record information about your visit to our websites, such as pages visited, links followed, and videos viewed so we can make our websites and the advertising displayed on it more relevant to your interests.  They may be set through our website by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other websites. GitLab processes any personal data collected through these cookies on the basis of your consent.
Sets consent for sending user data to Google for advertising purposes.
Sets consent for personalized advertising.

### Cookie List

- checkbox label label

--------------------