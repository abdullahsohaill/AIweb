# https://docs.openwebui.com/
**URL:** https://docs.openwebui.com
**Page Title:** 🏡 Home | Open WebUI
--------------------

Open WebUI is an extensible , feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It is built around universal standards, supporting Ollama and OpenAI-compatible Protocols (specifically Chat Completions). This protocol-first approach makes it a powerful, provider-agnostic AI deployment solution for both local and cloud-based models.
[LINK: extensible](https://docs.openwebui.com/features/plugin/)
Passionate about open-source AI? Join our team →
Looking for an Enterprise Plan ? — Speak with Our Sales Team Today!
[LINK: Enterprise Plan](https://docs.openwebui.com/enterprise)
[LINK: Speak with Our Sales Team Today!](https://docs.openwebui.com/enterprise)
Get enhanced capabilities , including custom theming and branding , Service Level Agreement (SLA) support , Long-Term Support (LTS) versions , and more!
Upgrade to a licensed plan for enhanced capabilities, including custom theming and branding, and dedicated support.

## Quick Start with Docker 🐳 ​

WebSocket support is required for Open WebUI to function correctly. Ensure that your network configuration allows WebSocket connections.
If Ollama is on your computer , use this command:
To run Open WebUI with Nvidia GPU support , use this command:
For environments with limited storage or bandwidth, Open WebUI offers slim image variants that exclude pre-bundled models. These images are significantly smaller but download required models on first use:

### Open WebUI Bundled with Ollama ​

This installation method uses a single container image that bundles Open WebUI with Ollama, allowing for a streamlined setup via a single command. Choose the appropriate command based on your hardware setup:
- With GPU Support :
Utilize GPU resources by running the following command: docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
With GPU Support :
Utilize GPU resources by running the following command:
- For CPU Only :
If you're not using a GPU, use this command instead: docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
For CPU Only :
If you're not using a GPU, use this command instead:
Both commands facilitate a built-in, hassle-free installation of both Open WebUI and Ollama, ensuring that you can get everything up and running swiftly.
After installation, you can access Open WebUI at http://localhost:3000 . Enjoy! 😄

### Using image tags in production ​

If you want to always run the latest version of Open WebUI, you can use the :main , :cuda , or :ollama image tags, depending on your setup, as shown in the examples above.
For production environments where stability and reproducibility are important, it is recommended to pin a specific release version instead of using these floating tags. Versioned images follow this format:
Examples (pinned versions for illustration purposes only):

### Using the Dev Branch 🌙 ​

We encourage users to run the development branch! Testing dev builds is one of the most valuable ways to contribute to Open WebUI. By running the latest development version, you help us catch bugs early, validate new features, and ensure stable releases for everyone.
We cannot deliver high-quality software without community testing. When issues are only discovered after a stable release, it creates a poor experience for everyone. Your feedback on the dev branch directly improves the next release.
The :dev branch contains the latest features and changes before they reach a stable release. While it may occasionally have bugs or incomplete features, it's generally usable for day-to-day testing.
Standard dev image:
Slim variant (excludes bundled models):
How to help:
- Run the dev image on a test instance (not your primary production setup)
- Keep it updated regularly — the dev branch moves fast! Pull the latest image frequently or see Updating Open WebUI below
- Report issues on GitHub with clear reproduction steps
[LINK: GitHub](https://github.com/open-webui/open-webui/issues)
- Join our Discord to discuss findings
If Docker doesn't work for your environment, you can also run the latest development code using the Local Development Guide . Conversely, if you prefer Docker over a local setup, the dev image is the easiest way to test.
Never share your database or data volume between dev and production setups. Dev builds may include database migrations that are not backward-compatible. If a dev migration runs on your production data and you later need to roll back, your production setup may break.
Always use a separate data volume (e.g., -v open-webui-dev:/app/backend/data ) for testing.

### Updating Open WebUI ​

To update Open WebUI container easily, follow these steps:
Use Watchtower to update your Docker container manually:
[LINK: Watchtower](https://github.com/nickfedor/watchtower)
Keep your container updated automatically every 5 minutes:
🔧 Note : Replace open-webui with your container name if it's different.

## Manual Installation ​

### Platform Compatibility ​

Open WebUI works on macOS, Linux (x86_64 and ARM64, including Raspberry Pi and other ARM boards like NVIDIA DGX Spark), and Windows.
There are two main ways to install and run Open WebUI: using the uv runtime manager or Python's pip . While both methods are effective, we strongly recommend using uv as it simplifies environment management and minimizes potential conflicts.

### Installation with uv (Recommended) ​

The uv runtime manager ensures seamless Python environment management for applications like Open WebUI. Follow these steps to get started:
Pick the appropriate installation command for your operating system:
- macOS/Linux : curl -LsSf https://astral.sh/uv/install.sh | sh
macOS/Linux :
- Windows : powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Windows :
Once uv is installed, running Open WebUI is a breeze. Use the command below, ensuring to set the DATA_DIR environment variable to avoid data loss. Example paths are provided for each platform:
- macOS/Linux : DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
macOS/Linux :
- Windows : $env:DATA_DIR="C:\open-webui\data"; uvx --python 3.11 open-webui@latest serve
Windows :
For PostgreSQL Support:
The default installation now uses a slimmed-down package. If you need PostgreSQL support , install with all optional dependencies:

### Installation with pip ​

For users installing Open WebUI with Python's package manager pip , it is strongly recommended to use Python runtime managers like uv or conda . These tools help manage Python environments effectively and avoid conflicts.
Python 3.11 is the development environment. Python 3.12 seems to work but has not been thoroughly tested. Python 3.13 is entirely untested and some dependencies do not work with Python 3.13 yet— use at your own risk .
- Install Open WebUI : Open your terminal and run the following command: pip install open-webui
Install Open WebUI :
Open your terminal and run the following command:
- Start Open WebUI : Once installed, start the server using: open-webui serve
Start Open WebUI :
Once installed, start the server using:

### Updating Open WebUI ​

To update to the latest version, simply run:
This method installs all necessary dependencies and starts Open WebUI, allowing for a simple and efficient setup. After installation, you can access Open WebUI at http://localhost:8080 . Enjoy! 😄

## Other Installation Methods ​

We offer various installation alternatives, including non-Docker native installation methods, Docker Compose, Kustomize, and Helm. Visit our Open WebUI Documentation or join our Discord community for comprehensive guidance.
[LINK: Open WebUI Documentation](https://docs.openwebui.com/getting-started/)
Continue with the full getting started guide .

### Desktop App ​

We also have an experimental desktop app, which is actively a work in progress (WIP) . While it offers a convenient way to run Open WebUI natively on your system without Docker or manual setup, it is not yet stable .
👉 For stability and production use, we strongly recommend installing via Docker or Python ( uv or pip ) .

## Sponsors 🙌 ​

We are incredibly grateful for the generous support of our sponsors. Their contributions help us to maintain and improve our project, ensuring we can continue to deliver quality work to our community. Thank you!

## Acknowledgements 🙏 ​

We are deeply grateful for the generous grant support provided by:
[LINK: GitHub Accelerator 2024](https://github.com/accelerator)
- Quick Start with Docker 🐳 Open WebUI Bundled with Ollama Using image tags in production Using the Dev Branch 🌙 Updating Open WebUI
- Open WebUI Bundled with Ollama
- Using image tags in production
- Using the Dev Branch 🌙
- Updating Open WebUI
- Manual Installation Platform Compatibility Installation with uv (Recommended) Installation with pip Updating Open WebUI
- Platform Compatibility
- Installation with uv (Recommended)
- Installation with pip
- Updating Open WebUI
- Other Installation Methods Desktop App
- Desktop App
- Sponsors 🙌
- Acknowledgements 🙏

--------------------