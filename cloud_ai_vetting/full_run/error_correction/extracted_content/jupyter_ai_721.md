# Jupyter AI
**URL:** https://jupyter-ai.readthedocs.io/en/latest
**Page Title:** Jupyter AI v3 (beta) — Jupyter AI documentation
--------------------

- GitHub
[LINK: GitHub](https://github.com/jupyterlab/jupyter-ai)

## Jupyter AI v3 (beta) #

Documentation for v2 is available here .
[LINK: here](https://jupyter-ai.readthedocs.io/en/v2/)
Welcome to Jupyter AI, which brings generative AI to Jupyter. Jupyter AI provides a user-friendly
and powerful way to explore generative AI models in notebooks and improve your productivity
in JupyterLab and the Jupyter Notebook. More specifically, Jupyter AI offers:
- A native chat UI in JupyterLab that enables you to work with generative AI as a conversational assistant, and also enables interaction with the active notebook.
A native chat UI in JupyterLab that enables you to work with generative AI as a conversational assistant, and also enables interaction with the active notebook.
- An %%ai magic that turns the Jupyter notebook into a reproducible generative AI playground.
This works anywhere the IPython kernel runs (JupyterLab, Jupyter Notebook, Google Colab, VSCode, etc.).
An %%ai magic that turns the Jupyter notebook into a reproducible generative AI playground.
This works anywhere the IPython kernel runs (JupyterLab, Jupyter Notebook, Google Colab, VSCode, etc.).
- Support for a wide range of generative model providers and models
(AI21, Amazon, Anthropic, Cohere, Gemini, Hugging Face, MistralAI, OpenAI, NVIDIA, etc.).
Support for a wide range of generative model providers and models
(AI21, Amazon, Anthropic, Cohere, Gemini, Hugging Face, MistralAI, OpenAI, NVIDIA, etc.).
- Multiple editable chat threads are available, each thread saved to a separate Jupyter server document with extension .chat .
Multiple editable chat threads are available, each thread saved to a separate Jupyter server document with extension .chat .
- Real time collaboration (RTC) is enabled in both chat and Jupyter notebook, if cloud deployments support it.
Real time collaboration (RTC) is enabled in both chat and Jupyter notebook, if cloud deployments support it.
- Support for hundreds of LLMs from many additional providers.
Support for hundreds of LLMs from many additional providers.
- Chat personas with agentic capabilities, with a default Jupyternaut persona.
Chat personas with agentic capabilities, with a default Jupyternaut persona.
Below is the look and feel of Jupyter AI v3. You can see the chat panel on the left and the notebooks on the right. The chat panel shows the Jupyternaut persona responding to prompts in the chat, as well as interacting with the code as context from the notebook on the right. The right panel shows the use of the %%ai magics commands.

## JupyterLab support #

Each major version of Jupyter AI supports only one major version of JupyterLab. Jupyter AI 1.x supports
JupyterLab 3.x, and Jupyter AI 2.x supports JupyterLab 4.x. The feature sets of versions 1.0.0 and 2.0.0
are the same. We will maintain support for JupyterLab 3 for as long as it remains maintained. Jupyter AI v3 supports JupyterLab 4.x.
The main branch of Jupyter AI targets the newest supported major version of JupyterLab. All new features and most bug fixes will be
committed to this branch. Features and bug fixes will be backported
to work on JupyterLab 3 only if developers determine that they will add sufficient value. We recommend that JupyterLab users who want the most advanced Jupyter AI functionality upgrade to JupyterLab 4.

## Quickstart #

It is best to install jupyter-ai in an environment. Use conda to create an environment that uses Python 3.13 and the latest version of JupyterLab:
To install both the %%ai magic and the JupyterLab extension, you can run:
Choose the version number, the latest version is 3.0.0b9 .
For an installation with all related packages, use:
To start Jupyter AI in Jupyter Lab, run
You should see an interface similar to the one above. Use the + Chat button in the chat panel to open a chat thread and enter prompts. In the chat box enter @ to see a list of personas, and you can select one before entering your query.
To connect a LLM for use in your chat threads you can select the Settings dropdown menu, select Jupyternaut settings in it to see the settings panel, in which you can select a chat model, specify model parameters if needed, and also add API keys for using LLMs that require it.
To use uv instead of pip :
Create a virtual environment with uv in any folder:
Activate the environment:
Install with
Run with

## Contents #

- Users Prerequisites Installation Uninstallation Model providers The chat interface Attaching context to the prompt Additional details about the chat interface The %ai and %%ai magic commands Configuration
- Prerequisites
- Installation
- Uninstallation
- Model providers
- The chat interface
- Attaching context to the prompt
- Additional details about the chat interface
- The %ai and %%ai magic commands
- Configuration
- Contributors Design principles Prerequisites Development Setup Building documentation Testing
- Design principles
- Prerequisites
- Development Setup
- Building documentation
- Testing
- Developers Entry points API
[LINK: Developers](developers/index.html)
- Entry points API
[LINK: Entry points API](developers/entry_points_api/index.html)

### This Page

- Show Source

--------------------