# How to install uv
**URL:** https://docs.astral.sh/uv/getting-started/installation
**Page Title:** Installation | uv
--------------------

[LINK: Skip to content](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)

## Installing uv

[LINK: Installing uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)

## Installation methods

[LINK: Installation methods](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)
Install uv with our standalone installers or your package manager of choice.

### Standalone installer

[LINK: Standalone installer](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
uv provides a standalone installer to download and install uv:
Use curl to download the script and execute it with sh :
If your system doesn't have curl , you can use wget :
Request a specific version by including it in the URL:
Use irm to download the script and execute it with iex :
Changing the execution policy allows running a script from the internet.
Request a specific version by including it in the URL:
Tip
The installation script may be inspected before use:
Alternatively, the installer or binaries can be downloaded directly from GitHub .
[LINK: GitHub](https://docs.astral.sh/uv/getting-started/installation/#github-releases)
See the reference documentation on the installer for details on
customizing your uv installation.
[LINK: installer](https://docs.astral.sh/uv/reference/installer/)

### PyPI

[LINK: PyPI](https://docs.astral.sh/uv/getting-started/installation/#pypi)
For convenience, uv is published to PyPI .
If installing from PyPI, we recommend installing uv into an isolated environment, e.g., with pipx :
However, pip can also be used:
Note
uv ships with prebuilt distributions (wheels) for many platforms; if a wheel is not available for a given
platform, uv will be built from source, which requires a Rust toolchain. See the contributing setup guide for details on building uv from source.
[LINK: contributing setup guide](https://github.com/astral-sh/uv/blob/main/CONTRIBUTING.md#setup)

### Homebrew

[LINK: Homebrew](https://docs.astral.sh/uv/getting-started/installation/#homebrew)
uv is available in the core Homebrew packages.

### MacPorts

[LINK: MacPorts](https://docs.astral.sh/uv/getting-started/installation/#macports)
uv is available via MacPorts .

### WinGet

[LINK: WinGet](https://docs.astral.sh/uv/getting-started/installation/#winget)
uv is available via WinGet .

### Scoop

[LINK: Scoop](https://docs.astral.sh/uv/getting-started/installation/#scoop)
uv is available via Scoop .

### Docker

[LINK: Docker](https://docs.astral.sh/uv/getting-started/installation/#docker)
uv provides a Docker image at ghcr.io/astral-sh/uv .
[LINK: ghcr.io/astral-sh/uv](https://github.com/astral-sh/uv/pkgs/container/uv)
See our guide on using uv in Docker for more details.
[LINK: using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/)

### GitHub Releases

[LINK: GitHub Releases](https://docs.astral.sh/uv/getting-started/installation/#github-releases)
uv release artifacts can be downloaded directly from GitHub Releases .
[LINK: GitHub Releases](https://github.com/astral-sh/uv/releases)
Each release page includes binaries for all supported platforms as well as instructions for using
the standalone installer via github.com instead of astral.sh .

### Cargo

[LINK: Cargo](https://docs.astral.sh/uv/getting-started/installation/#cargo)
uv is available via crates.io .
Note
This method builds uv from source, which requires a compatible Rust toolchain.

## Upgrading uv

[LINK: Upgrading uv](https://docs.astral.sh/uv/getting-started/installation/#upgrading-uv)
When uv is installed via the standalone installer, it can update itself on-demand:
Tip
Updating uv will re-run the installer and can modify your shell profiles. To disable this
behavior, set UV_NO_MODIFY_PATH=1 .
When another installation method is used, self-updates are disabled. Use the package manager's
upgrade method instead. For example, with pip :

## Shell autocompletion

[LINK: Shell autocompletion](https://docs.astral.sh/uv/getting-started/installation/#shell-autocompletion)
Tip
You can run echo $SHELL to help you determine your shell.
To enable shell autocompletion for uv commands, run one of the following:
To enable shell autocompletion for uvx, run one of the following:
Then restart the shell or source the shell config file.

## Uninstallation

[LINK: Uninstallation](https://docs.astral.sh/uv/getting-started/installation/#uninstallation)
If you need to remove uv from your system, follow these steps:
- Clean up stored data (optional): $ uv cache clean $ rm -r " $( uv python dir ) " $ rm -r " $( uv tool dir ) " Tip Before removing the binaries, you may want to remove any data that uv has stored. See the storage reference for details on where uv stores data.
Clean up stored data (optional):
Tip
Before removing the binaries, you may want to remove any data that uv has stored. See the storage reference for details on where uv stores data.
[LINK: storage reference](https://docs.astral.sh/uv/reference/storage/)
- Remove the uv, uvx, and uvw binaries: macOS and Linux Windows $ rm ~/.local/bin/uv ~/.local/bin/uvx PS> rm $HOME \. local \ bin \ uv . exe PS> rm $HOME \. local \ bin \ uvx . exe PS> rm $HOME \. local \ bin \ uvw . exe Note Prior to 0.5.0, uv was installed into ~/.cargo/bin . The binaries can be removed from there to
uninstall. Upgrading from an older version will not automatically remove the binaries from ~/.cargo/bin .
Remove the uv, uvx, and uvw binaries:
Note
Prior to 0.5.0, uv was installed into ~/.cargo/bin . The binaries can be removed from there to
uninstall. Upgrading from an older version will not automatically remove the binaries from ~/.cargo/bin .

## Next steps

[LINK: Next steps](https://docs.astral.sh/uv/getting-started/installation/#next-steps)
See the first steps or jump straight to the guides to
start using uv.
[LINK: first steps](https://docs.astral.sh/uv/getting-started/first-steps/)
[LINK: guides](https://docs.astral.sh/uv/guides/)

--------------------