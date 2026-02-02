# Homepage - SillyTavern
**URL:** https://sillytavernai.com
**Page Title:** Beginner’s Guide to SillyTavern - How To Install and Use
--------------------


## Beginner’s Guide to SillyTavern

SillyTavern is a powerful, locally-run user interface for AI chat and roleplay that connects to a variety of language models, both cloud-based (OpenAI, Anthropic, etc.) and local (KoboldAI, oobabooga, etc.). This guide will walk you through installing SillyTavern on Windows , macOS, or Linux, setting up different LLM API options (remote and local), managing character cards , and adjusting presets and prompt formatting. It’s written with beginners in mind – no prior experience with AI chat UIs is assumed.

### Installation on Windows, macOS, and Linux

If you’re on Windows and prefer a simpler, menu-driven setup, you can use the SillyTavern Launcher to handle installation , updates, and optional components automatically. It’s beginner-friendly and requires minimal manual steps.
See the SillyTavern Launcher Guide for instructions.
Before installing, make sure you have Node.js (v18+) and Git on your system (Node.js is required to run SillyTavern’s server ). Below are platform-specific installation steps.
1. Install Prerequisites: Install the latest Node.js LTS and Git for Windows.
2. Choose Install Location : Create or navigate to a folder not protected by Windows (avoid Program Files, System32, etc.). For example, create C:\SillyTavern\ for the files.
3. Download SillyTavern: Open a Command Prompt in that folder (you can click the Explorer address bar, type cmd, and press Enter). Run the Git clone command for the stable release:
git clone https://github.com/SillyTavern/SillyTavern -b release
This will download the SillyTavern code into a subfolder. (Advanced users can use the -b staging branch for the latest features, but beginners should stick to the release branch for stability.)
4. Run SillyTavern: In the new SillyTavern folder, double-click Start.bat. This will install necessary Node.js packages and launch the SillyTavern server. A console window will open, and after a moment SillyTavern’s interface should automatically open in your web browser (if it doesn’t, you can manually open http://localhost:8000 in your browser).
5. Access the UI: Once running, the SillyTavern UI appears in your browser. You’ll use this web app to configure APIs, load characters, and chat. (Leave the console window open while using SillyTavern — closing it will shut down the server.)
Alternate Windows Installation Options: If you prefer a more guided approach, you can use the SillyTavern Launcher or GitHub Desktop. The Launcher is a separate helper that can automate some steps: for example, you can run a one-line command to clone the launcher repo and start its installer . GitHub Desktop can also clone the repository via a GUI – after cloning, you still run Start.bat to launch SillyTavern. These methods achieve the same result, so use whichever you find easiest.
See the SillyTavern Launcher Guide for instructions.
1. Install Prerequisites: Ensure you have Node.js and Git installed on your system. On macOS, an easy way is using Homebrew (brew install node git), and on Linux use your distro’s package manager (e.g. apt or yum).
2. Download SillyTavern: Open a Terminal. Clone the SillyTavern repository (release branch) with Git:
git clone https://github.com/SillyTavern/SillyTavern -b release
This creates a SillyTavern directory in your current folder.
3. Run SillyTavern: Change into the new directory: cd SillyTavern. Then run the startup script: bash start.sh (or ./start.sh). This will install dependencies and start the server.
4. Access the UI: After the script finishes, SillyTavern will be running. Open http://localhost:8000 in your browser to see the interface (the terminal will also display the local URL). Keep the terminal session open while using the app.
Note : On macOS, you might be prompted by security settings when running the script the first time. If so, you may need to allow the script in System Preferences. Also, macOS/Linux users can optionally use the SillyTavern Launcher for a menu-driven install (similar to Windows). On Linux, cloning and running the Launcher's install.sh will guide you through installing SillyTavern and any optional components. On macOS, you can install Homebrew, then use it to install Git, and run the Launcher’s install script similarly. These tools simplify the process, but using Git and the startup script as above is perfectly fine for most users.

### Connecting to an LLM API (Remote or Local)

Once SillyTavern is up and running, the next step is to connect it to a language model backend. SillyTavern itself doesn’t run a language model – it’s a frontend that sends your messages to a model and returns the responses. You have two primary options for models:
- Cloud-based APIs (hosted models) – e.g. OpenAI’s GPT-3.5/GPT-4, Anthropic’s Claude, etc. These run on remote servers. They often require API keys (and usually paid credits) but offer high-quality outputs.
- Local APIs (self-hosted models) – e.g. running a model like Pygmalion or Llama 2 on your own PC via a local backend such as KoboldAI or oobabooga. These are free to use and private (no filters) but require downloading large model files and having enough hardware to run them.
In the SillyTavern UI, click the “API” button (plug icon in the top bar) to open the API Connections panel. Here you can choose an API type and configure it. SillyTavern supports two API structures: Chat Completion (for chat-oriented models like ChatGPT/Claude) and Text Completion (for raw completion models or local backends). For beginners, the main difference is that you should select Chat for OpenAI/Claude and Text for most local servers or older-style models. Below are step-by-step setups for each scenario:
SillyTavern’s “Connection Profile” panel, where you select and connect to an AI model API. In this example, the user has chosen a local Ollama server (Ollama is a local LLM backend) as the API Type. You would use this panel to select “OpenAI” or “Claude” for remote APIs, or “Oobabooga”, “KoboldCpp”, etc. for local APIs. Then you enter the API URL (for local servers) or paste the API key (for cloud services) and click Connect.

### Using a Remote LLM API (NanoGPT, OpenAI, Anthropic, etc.)

Remote APIs are the quickest way to get started if you have an API key. SillyTavern supports a wide range of providers out of the box. Here we’ll use OpenAI’s GPT as an example, but the process is similar for others:
1.	Obtain an API Key: Sign up for the service and get your private API key. For OpenAI, log in to the OpenAI Platform dashboard and create a new secret key under your account’s API keys section. Copy this key. For Anthropic’s Claude, you’d sign up at Anthropic’s console and generate a key. (Each provider’s documentation will show how to create API keys – see also SillyTavern’s docs for provider-specific guidance.)
2.	Select the API in SillyTavern: In the SillyTavern API Connections panel, set API = “Chat Completion” (for chat-centric models) and then choose the Source or API Type from the dropdown. For example, select OpenAI (ChatGPT) for GPT-3.5/GPT-4 models. For Anthropic, choose Claude. There are also options for AI21, Cohere, Google’s Vertex/Gemini, etc., which you can choose if you have those keys.
3.	Enter Credentials: When you select a cloud API, fields will appear to input your API key (and sometimes model choice or other options). Paste your API key into the appropriate field. For OpenAI, you can also select which model to use (e.g. gpt-3.5-turbo or gpt-
4.	Connect: Click the Connect button. SillyTavern will validate the key and attempt a test connection. If successful, you’ll see a green “connected” indicator or the model name. You can now start chatting using this model.
5.	Considerations: Cloud models like OpenAI and Claude have content filters (they may refuse certain requests) and usage costs (pay per token or monthly). However, they generally produce very fluent and coherent responses. Make sure to monitor your API usage to avoid unexpected charges. If you run into issues, double-check that you copied the entire API key correctly and that your account has sufficient credit or is within rate limits.
Tip: One easy free option is AI Horde, a crowdsourced service that doesn’t require an API key at all. If you select AI Horde in SillyTavern, you can start using it immediately – your requests will be handled by volunteer-run GPUs. The downside is that generation speed and quality can vary. But it’s a good zero-cost way to experiment before investing in a paid API.

### Using NanoGPT as a Remote API Provider

By default, SillyTavern needs to connect to an AI model to generate text. While you can use big-name APIs (like OpenAI) or run a model locally, a budget-friendly alternative is NanoGPT – a third-party service that provides access to a wide range of AI models through a single API. NanoGPT offers 125+ advanced models (for text generation and even image or audio generation) without requiring separate subscriptions to each. It operates on a flexible pay-as-
you-go basis (with very small deposits, even as low as $0.10) so you only pay for what you use or a simple low cost monthly subscription. Unlike some cloud providers, NanoGPT also prioritizes privacy: it does not store your prompts or conversations on their servers, keeping your data on your device. This makes it a compelling option for SillyTavern users who want powerful models with minimal hassle.
1.	Create a NanoGPT account and get an API key: Go to nano-gpt.com and sign up for an account ( you can use the invite link provided on AICC for a small discount , or sign up directly). Once logged in, navigate to the API section of the NanoGPT dashboard (you can click the “API” link in the sidebar). There, click the “Generate” button to create a new API key (give it a name if prompted) and copy the key to your clipboard. This key is a long string of letters/numbers that will authorize SillyTavern to use the NanoGPT service.
2. Open SillyTavern’s connection settings: In the SillyTavern interface, find the Connection Settings (look for a plug icon in the top bar). This is where you configure which AI API SillyTavern will use.
3. Select NanoGPT as the provider: In the Connection settings panel, set the API Type to “Chat Completion” (NanoGPT uses an OpenAI-compatible chat API format, so Chat Completion is the correct mode). Next, find the Chat Completion Source dropdown and choose “NanoGPT” from the list. You will see a field to enter an API key – paste the NanoGPT API key you copied in step 1 into this field.
4. Important: Make sure you choose the Chat Completion interface and not the older “text completion” mode. NanoGPT’s API expects a chat-style conversation format (similar to ChatGPT’s API), so using the Chat Completion setting ensures your messages are sent in the correct format. SillyTavern will automatically include your API key in the authorization header of requests (as a Bearer token) once you’ve entered it, so no extra headers are needed on your part.
5. Pick a model and test the connection: After entering the key, you can select which NanoGPT model you want to use from the model dropdown. NanoGPT gives you access to many models – from powerful closed-source models (comparable to GPT-4 or other cutting-edge models) to fast open-source models – all through the same interface. Choose a model that fits your needs (for example, a high-end model for the best quality, or a smaller one if you want faster/cheaper responses). Now click the “Test Message” button in SillyTavern’s connection settings. This will send a quick test query to NanoGPT to confirm everything is working. If configured correctly, you should get a success confirmation or a sample reply from the model.
That’s it! You’ve connected SillyTavern to NanoGPT. Now you can start a chat with any character and the replies will come from the NanoGPT model you selected.

### Using a Local LLM API (KoboldAI, oobabooga, Pygmalion, etc.)

Running a model locally gives you privacy and flexibility (no filters or pay-per-use), but it involves more setup and decently powerful local hardware. You’ll need to: (a) install a local backend server, (b) download at least one model to run, and (c) connect SillyTavern to that server. SillyTavern is compatible with many local backends, including KoboldAI/KoboldCPP, Oobabooga’s Text Generation Web UI, Tabby, llama.cpp/Ollama, and others. Here we outline a generic local setup:
Install a Backend: Two popular choices are:
- KoboldCPP – a lightweight app (just a single executable on Windows/Mac/Linux) for running GPT4All/LLAMA-based models (GGUF format) with CPU or GPU offloading. This is great if you don’t have a powerful GPU, as it can use CPU-only (slow but works). No complicated install; you download the .exe (or binary) and run it.
- Oobabooga Text Generation Web UI – a full-featured web UI that supports many model types (GPTQ, ExLlama, etc.) with streaming output. It requires a bit more setup but has one-click installers and a GUI. Use this if you plan to try various models and want an interface to manage them.
For example, to install Oobabooga’s web UI: you’d clone its GitHub repo and run the start_windows.bat (or install.sh on Linux) which will set up the environment. It will ask you about your GPU. Once installed, you place model files into its models folder. Alternatively, Oobabooga provides an installer EXE that automates these steps. For KoboldCPP, you simply download the appropriate binary from their site (choose the version that matches your system, e.g. with CUDA for modern Nvidia GPUs), and no installation is needed beyond that.
1.	Download a Model: Models can be huge (several GB), and you need a model file to run locally. Popular model repositories include Hugging Face – you can find models like Pygmalion (an older 6B parameter model tuned for chat), or newer LLaMA-2 variants, etc. For instance, a good starter model is a 7B parameter model in GGUF format (which works with KoboldCPP). SillyTavern’s docs suggest “Kunoichi-DPO-v2-7B,” a fine-tuned Mistral 7B model requiring ~7GB RAM. Download the model file (usually .gguf or .safetensors) from a trusted source – often Hugging Face. Ensure the model format is supported by your chosen backend (GGUF for KoboldCPP, or a GPTQ/ExLlama model for oobabooga, etc.).
2.	Run the Model Server: Launch your backend and load the model:
3.	For KoboldCPP, open the application and use its interface to select the downloaded .gguf model file and launch it. KoboldCPP will start a local server (by default on port 5001) and even provides a simple UI to test the model output.
4.	For Oobabooga, run its start script with API mode enabled. The easiest way: edit the CMD_FLAGS.txt in oobabooga’s folder and add --api (then restart the web UI). This makes Oobabooga serve an OpenAI-compatible API on port 5000. Verify it’s working by visiting http://127.0.0.1:5000/docs – you should see the API documentation page if it’s running properly. Also, in the oobabooga web UI, ensure you load your model in the Model tab before trying to connect.
5.	Connect SillyTavern to the Local API: In SillyTavern’s API Connections panel, set API = “Text Completion” (since most local backends behave like text completion). Then select the appropriate API Type:
6.	If you’re using Oobabooga, choose “Default (Oobabooga)” as the type. The default server URL is http://127.0.0.1:5000/. Enter that (or the port you configured) in the URL field. Leave “Legacy API” unchecked (it’s for older KoboldAI APIs). Click Connect. SillyTavern should link up and even display the name of the loaded model if all is well.
7.	If using KoboldCPP, choose KoboldCpp as the API type. The default URL is http://127.0.0.1:5001/ (unless KoboldCPP showed a different port/link). Enter that and Connect. You should see a success message or model name on connect.
8.	For KoboldAI (Classic) or other servers, select the matching option (KoboldAI, llama.cpp, etc.) and provide the URL/port they’re running on. KoboldAI (old version) typically runs on localhost:5000 but note that it’s largely deprecated in favor of the newer solutions.
9.	Test the Connection: After connecting, try typing a prompt in the chat. If the model responds, congratulations – you have a local model running through SillyTavern! If there’s no response or an error, double-check the backend console for any errors (e.g. model not loaded, out of memory, etc.), and ensure the URL/port is correct.
Using local models can be complex due to hardware limitations. Smaller models (6B-13B parameters) can run on a strong CPU or mid-range GPU, but larger ones (30B-70B) need a high-end GPU or a lot of RAM with quantization. Don’t be discouraged by initial complexity – once set up, local models offer freedom to experiment. Communities around KoboldAI and oobabooga have plenty of tutorials if you get stuck. And remember, you only need to set up a given backend once; afterward, you can launch it and reconnect SillyTavern any time.

### Character Cards: Downloading, Importing, and Editing Characters

SillyTavern revolves around character cards – these are profiles that define an AI character’s personality, background, and behavior in chat. A character card typically contains the character’s name, a detailed description, a scenario or context, and example dialogue (including an initial greeting message). Think of it as creating a persona for the AI to role-play, whether it’s an original character, a fictional character, or a specific assistant persona. You can have many character cards and switch between them or even have multiple characters in one chat (group chat).
Where to Find Character Cards: There is a vibrant community creating and sharing character cards: - The SillyTavern Discord and subreddit often share cards or directories. There are also dedicated repositories, like our site, aicharactercards.com , where creators upload character cards (in PNG format with metadata). You can also create your own card from scratch within SillyTavern.
Recommended Formats: SillyTavern supports Character Card v2 format (JSON or PNG). The most common format for sharing is a PNG image with embedded JSON metadata – this allows the card to include an avatar picture as well as the textual profile. You might also encounter .json card files. Both work in SillyTavern. If using PNGs, ensure the file is truly a PNG with embedded data (occasionally, a misnamed file can cause import errors – e.g. a renamed webp will fail). When downloading from community sites, use the provided download button which usually gives you the correctly formatted file.
Importing a Character Card: In the SillyTavern interface, click the Characters icon (person icon in the top bar) to open the Character Management panel. At the top of this panel you’ll see options including “Create New Character”, “Import Character”, and “External Import”. To import a card you’ve downloaded:
- Click Import Character, then select the file (PNG or JSON) from your computer. SillyTavern will load it and add the character to your character list. If the PNG had an image, it will be set as the avatar. All the character’s details (description, etc.) are now stored in SillyTavern.
- Alternatively, if you have a URL to a character card (for example, some sites provide a direct link to the raw .json), you can use External Import and paste the URL. SillyTavern will fetch the card from the internet and import it.
- Once imported, you’ll see the character listed by name. Click the character’s name to start a chat with them or to view/edit their profile.
Our site, AICharacterCards.com (AICC), is a popular hub for downloading high-quality SillyTavern character cards.
Here’s how to use it to expand your character roster:
1.	Browse and select a character: Visit aicharactercards.com and explore the categories or search for a character that interests you. Click on a character’s card to open its detail page.
2.	Download the character card: On the character’s page, click the “Download Card” button to save the card to your device. This will typically download a PNG image file that has the character’s data embedded in it. (In some cases, the site may also offer a JSON download. SillyTavern supports importing either a PNG card or a JSON file, so you can use whichever format you prefer.)
3.	Import into SillyTavern: Open SillyTavern and go to the Character Management panel (the icon that looks like a persons or characters list). In the character list, choose Import Character to load a character from a file. Select the PNG or JSON file you just downloaded. The character will be added to your SillyTavern character list with its avatar image, description, and first message ready to go.
4.	Tip: SillyTavern also has an External Import option. Instead of downloading the file, you can copy the ST Card ID from the AICC character page (there’s a clipboard icon next to the ID) and paste that ID into SillyTavern’s external importer. SillyTavern will then fetch and import the card automatically from AICC.

### Editing a Character Card

After importing (or creating a new character), you can tweak the character’s settings to your liking. Clicking on a character and then the “Edit” (pencil) icon will bring up the character edit panel.
Here are key fields you can edit:
- Avatar Image : You can upload a different profile picture for the character if you want.
- Name : The name of the character, it will be used in chat messages so make sure to make it something simple like "John" not "John - the muscular blacksmith"
- Description : A text box for the character’s description/appearance/background. This is where you write who the character is, their backstory, traits, appearance, etc. This description is always included in the prompt sent to the AI, so it heavily influences the AI’s behavior.
- Personality : Some cards have a separate field for a succinct list of traits or a persona summary. This can be used to reinforce key aspects (e.g. “Kind, protective, speaks in old English”).
- Scenario : You can describe the situation or world context here, if applicable (e.g. “You are on a spaceship and this is the ship’s AI.”).
- First Message : This is the greeting the character will send as the first message when a new chat is started. It helps establish the character’s voice. For example, a character might greet you with, “Hello, I’ve been expecting you. Welcome to my shop!”.
- Example Messages : You can provide sample chat exchanges demonstrating how the character should talk. These example messages help the model mimic the character’s style. They are included at the start of a chat (and can be retained until the conversation grows too long, at which point older examples drop out of context).
- Alternate Greetings : You can add multiple possible first messages (greetings). SillyTavern will let you “swipe” between them when starting a new chat.
- Advanced Fields : By clicking Advanced Definitions, you can set more nuanced prompts like a custom system prompt or post-history instructions specific to this character. As a beginner you can ignore these until you get comfortable; they’re there for fine-tuning how the AI is cued (for instance, you could override the global system prompt with a character-specific one, if you enable the corresponding user setting).
Editing is as simple as typing in these fields SillyTavern will auto-save. The changes update immediately for new messages. Feel free to experiment: you can always export the character to save a backup (there’s an Export option in the character’s menu) or duplicate the character if you want to try variations. Tip: Keep an eye on the token count shown for the character’s definition. Extremely long descriptions or many example messages can consume a lot of the model’s context window, which might shorten how much conversation history can be remembered.

### Using and Editing Presets & Prompt Formatting

One of SillyTavern’s strengths is the level of control it gives you over text generation settings and prompt formatting. For newcomers, you can get by with default settings, but as you gain experience you’ll likely want to tweak parameters or use community-made presets to optimize your AI’s output. This section explains what presets and prompt formatting are, and how to use them.
These are sets of parameters that control how the AI generates text – things like temperature, top-p, presence penalty, etc. These affect the style and randomness of the output. SillyTavern’s UI (under the Advanced settings or Text Generation panel) exposes these sliders. Presets are simply saved configurations of these sliders that you can switch between quickly. For example, a “creative writing” preset might have a higher temperature (making output more varied and imaginative) and a lower repetition penalty (allowing more freedom), whereas a “precise/analytical” preset might use a lower temperature and higher penalties to keep the AI on topic and avoid rambling. SillyTavern comes with some default presets (often labeled as “Default” or others tuned for certain model types), and the community has shared many preset files for different models or styles.
Screenshot of SillyTavern’s interface showing the Text Generation settings (left panel) and an example chat (right). In the left “Text Completion presets” panel, you can adjust parameters like Temperature, Top K, Top P, etc., or select a preset from the top dropdown. Community presets often target specific models or use-cases (e.g. “Storytelling” vs “Concise”). On the right, the character card fields (Description, First message) are visible, as well as a sample conversation with the AI assistant.
In practice, you might load a preset appropriate for your model: for instance, a preset tuned for a 7B Pygmalion model might increase repetition penalties and reduce output length to compensate for the model’s tendency to loop, whereas a preset for GPT-4 would be different. Using a Preset: In the SillyTavern UI, find the preset dropdown in the text generation panel (the left side panel with all the sliders). Select a preset name from the list – the sliders will jump to those values. You can also adjust sliders manually and then save your current settings as a new preset (there’s usually an icon to save). This way, you could make a “MyFantasyChat” preset, for example, and reuse it whenever you roleplay a fantasy scenario.
Many community-created presets are available. These often come as JSON files (sometimes called “sampler settings” or “master presets”). To use one, you can either place the JSON files in SillyTavern’s data/default-user directory (e.g. TextGen Settings/ for sampler presets, and context/ or instruct/ for prompt templates) as indicated in documentation, or import them via the UI. In the UI’s Advanced Formatting or Prompt Manager section (look for a button or menu to import presets), you can upload a “master preset” JSON which contains a full set of settings. Once imported, the preset will appear in your list. Always make sure the preset you use matches your model’s requirements – for example, some presets are designed for specific model families (LLaMA 2 vs Mistral, etc.). The good news is SillyTavern can automatically pick up certain model cues: it can detect if you connect to a known model and offer the recommended preset for it (via a hash match against known templates).
Besides sampling settings, how the conversation is formatted before it’s sent to the AI is crucial. SillyTavern handles a lot of this under the hood. For Chat Completion APIs (like OpenAI’s GPT), SillyTavern constructs the conversation with system/user/assistant roles as expected by the API. For Text Completion APIs (like local models), it uses prompt templates to format the conversation into a single text block. This is where Instruct Mode and prompt templates come in. Instruct Mode in SillyTavern lets you select a template that matches your model’s training format.
For example, some models expect prompts like:
### Instruction: <user message> ### Response: <assistant message>
while others might use a simpler roleplay style like:
User: <user message> Assistant: <assistant message>
SillyTavern provides preset templates for many formats (Alpaca, Llama2-chat, Vicuna, etc.). When you connect to a local model, you should choose the instruct template that the model was trained on. If you’re using a known model from Hugging Face, its model card often mentions the expected prompt format – sometimes even providing a SillyTavern JSON template. To set this, go to Advanced Formatting -> Instruct Mode in SillyTavern, enable Instruct Mode, and pick the template (there’s a dropdown of templates like Alpaca, Vanilla, etc.). From there, SillyTavern will wrap your character card and chat history with the appropriate prefixes/suffixes automatically when sending to the model. You can even customize these templates or create new ones if you have special formatting needs (the UI allows editing the sequences for user/assistant prefixes, etc., but that’s an advanced topic).
Examples: If you’re chatting with a local model that isn’t a chat-tuned model (say the original Pygmalion 6B), you might enable Instruct Mode with a simple template that uses “You:” and the character’s name as prefixes for each turn, emulating a chat log – this helps the model understand the conversation format. On the other hand, if you use OpenAI’s GPT-4 via API, you don’t need to worry about instruct mode at all; SillyTavern will use the chat completion style and you can simply edit the System Prompt if desired. The System Prompt (called “Main Prompt” in SillyTavern’s interface) is a hidden instruction that defines the AI’s role or behavior globally. By default, SillyTavern has a generic system prompt (or none), but you can set your own (e.g. “You are a helpful and verbose assistant…”) in the settings. This is usually not necessary if you’re using character cards, since the character card acts as the role prompt. However, for fine control, SillyTavern lets you override or prepend things in the prompt via settings or character advanced definitions.
In summary, presets let you quickly change how the model generates text, and prompt formatting settings let you change how the conversation is presented to the model. As a beginner, try using some well-regarded community presets for your model and stick to the provided prompt templates. As you get comfortable, you can experiment with these controls to see their effect – for instance, bump up the temperature if the AI is too bland, or edit the system prompt if you want the AI to follow a specific rule. SillyTavern’s philosophy is to empower the user with as much control as possible, so have fun tinkering!

### Official Resources and Community

Starting out with SillyTavern is much easier when you know where to find help and updates. Here are some official resources and communities:
- Official Documentation: The SillyTavern docs site is an excellent reference for all features and setup steps. It contains guides (like the installation and API pages referenced in this guide) and explanations of advanced concepts. Whenever you’re unsure about a feature, the docs should be your first stop.
- sillytavern.app
- GitHub Repository: SillyTavern is open-source (AGPL license) and the code is on GitHub: https://github.com/SillyTavern/SillyTavern. The GitHub README also links the docs and has basic info. You can check the Issues there for known bugs or report new ones (after searching for duplicates).
- https://github.com/SillyTavern/SillyTavern
[LINK: https://github.com/SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern)
- Discord Community: The official SillyTavern Discord is very active and beginner-friendly. You can ask for help, share characters and presets, and stay up-to-date with announcements. The developers (cohee, rossascends, Wolfsblvt, etc.) hang out there along with many experienced users. It’s one of the best places to learn tips or troubleshoot problems in real time.
- https://discord.gg/sillytavern
- Reddit Community: There’s an /r/SillyTavernAI subreddit where users discuss updates, share creations, and help each other. Browsing it can be useful to find Q&A threads or fun ideas on how to use SillyTavern.
- https://www.reddit.com/r/SillyTavernAI/
- AICharacterCards.com Guides: Our site hosts a wide range of ever expanding guides on general and niche SillyTavern topics. (You're reading one right now!)
- https://aicharactercards.com/sillytavern-guides/
- https://aicharactercards.com/articles/
- Related Communities: If you’re using local models, the KoboldAI and PygmalionAI communities (on Reddit or Discord) have lots of advice on running models and fine-tuning characters for roleplay. Similarly, Oobabooga’s GitHub and Discord can assist with backend-specific issues.
Lastly, remember that SillyTavern is a community-driven project built by hobbyists for free, offering fun and freedom in AI roleplay. It’s updated frequently with new features. Don’t hesitate to reach out on official channels if you need help or have suggestions.
Click show to see the JSON Schema
Allowed JSON Schema
"name" : "Demo Character Name" ,
"description" : "Describe your character's physical and mental traits here." ,
"personality" : "A brief description of the personality" ,
"scenario" : "Circumstances and context of the interaction" ,
"first_mes" : "This will be the first message from the character that starts every chat." ,
"mes_example" : "Examples of chat dialog. Begin each example with START on a new line." ,
"creatorcomment" : "Describe the bot, give use tips, or list the chat models it has been tested on. This will be displayed in the character list." ,
"avatar" : "none" ,
"chat" : "Demo Card - 2024-4-14 @15h 59m 44s 913ms" ,
"talkativeness" : "0.5" ,
"fav" : false ,
"tags" : [
"Write a comma-separated list of tags"
"spec" : "chara_card_v2" ,
"spec_version" : "2.0" ,
"data" : {
"name" : "Demo Character Name" ,
"description" : "Describe your character's physical and mental traits here." ,
"personality" : "A brief description of the personality" ,
"scenario" : "Circumstances and context of the interaction" ,
"first_mes" : "This will be the first message from the character that starts every chat." ,
"mes_example" : "Examples of chat dialog. Begin each example with START on a new line." ,
"creator_notes" : "Describe the bot, give use tips, or list the chat models it has been tested on. This will be displayed in the character list." ,
"system_prompt" : "Any contents here will replace the default Main Prompt used for this character. (v2 spec: system_prompt)" ,
"post_history_instructions" : "Any contents here will replace the default Jailbreak Prompt used for this character. (v2 spec: post_history_instructions" ,
"tags" : [
"Write a comma-separated list of tags"
"creator" : "Botmaker's name / Contact Info" ,
"character_version" : "If you want to track character versions" ,
"alternate_greetings" : [],
"extensions" : {
"talkativeness" : "0.5" ,
"fav" : false ,
"world" : "" ,
"depth_prompt" : {
"prompt" : "Text to be inserted in-chat @ designated depth" ,
"depth" : 4
"create_date" : "2024-4-14 @15h 59m 44s 928ms"
Notifications

--------------------