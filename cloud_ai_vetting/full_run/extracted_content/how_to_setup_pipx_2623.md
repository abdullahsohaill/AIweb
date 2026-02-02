# How to setup pipx
**URL:** https://pipx.pypa.io
**Page Title:** pipx
--------------------


## pipx — Install and Run Python Applications in Isolated Environments

Documentation : https://pipx.pypa.io
Source Code : https://github.com/pypa/pipx
[LINK: https://github.com/pypa/pipx](https://github.com/pypa/pipx)
For comparison to other tools including pipsi, see Comparison to Other Tools .

## Install pipx

Warning
It is not recommended to install pipx via pipx . If you'd like to do this anyway, take a look at the pipx-in-pipx project and read about the limitations there.
[LINK: pipx-in-pipx](https://github.com/mattsb42-meta/pipx-in-pipx)

### On macOS

Upgrade pipx with brew update && brew upgrade pipx .

### On Linux

- Ubuntu 23.04 or above
- Fedora:
- Arch:
- Using pip on other distributions:
Upgrade pipx with python3 -m pip install --user --upgrade pipx .

### On Windows

- install via Scoop
Upgrade pipx with scoop update pipx .
- install via pip (requires pip 19.0 or later)
It is possible (even most likely) the above finishes with a WARNING looking similar to this:
If so, go to the mentioned folder, allowing you to run the pipx executable directly. Enter the following line (even if
you did not get the warning):
This will add both the above mentioned path and the %USERPROFILE%\.local\bin folder to your search path. Restart your
terminal session and verify pipx does run.
Upgrade pipx with py -m pip install --user --upgrade pipx .

### Using pipx without installing (via zipapp)

You can also use pipx without installing it. The zipapp can be downloaded from Github releases and you can invoke it with a Python 3.9+ interpreter:
[LINK: Github releases](https://github.com/pypa/pipx/releases)

### Use with pre-commit

pipx has pre-commit support .

### Shell completions

Shell completions are available by following the instructions printed with this command:
For more details, see the installation instructions .

## Overview: What is pipx ?

pipx is a tool to help you install and run end-user applications written in Python. It's roughly similar to macOS's brew , JavaScript's npx , and
Linux's apt .
It's closely related to pip. In fact, it uses pip, but is focused on installing and managing Python packages that can be
run from the command line directly as applications.

### How is it Different from pip?

pip is a general-purpose package installer for both libraries and apps with no environment isolation. pipx is made
specifically for application installation, as it adds isolation yet still makes the apps available in your shell: pipx
creates an isolated environment for each application and its associated packages.
pipx does not ship with pip, but installing it is often an important part of bootstrapping your system.

### Where Does pipx Install Apps From?

By default, pipx uses the same package index as pip, PyPI . pipx can also install from all other
sources pip can, such as a local directory, wheel, git url, etc.
Python and PyPI allow developers to distribute code with "console script entry points". These entry points let users
call into Python code from the command line, effectively acting like standalone applications.
pipx is a tool to install and run any of these thousands of application-containing packages in a safe, convenient, and
reliable way. In a way, it turns Python Package Index (PyPI) into a big app store for Python applications. Not all
Python packages have entry points, but many do.
If you would like to make your package compatible with pipx, all you need to do is add a console scripts entry point. If you're a poetry user, use these instructions . Or,
if you're using hatch, try this .
[LINK: console scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point)
[LINK: these instructions](https://python-poetry.org/docs/pyproject/#scripts)

## Features

pipx enables you to
- Expose CLI entrypoints of packages ("apps") installed to isolated environments with the install command. This
  guarantees no dependency conflicts and clean uninstalls!
- Easily list, upgrade, and uninstall packages that were installed with pipx
- Run the latest version of a Python application in a temporary environment with the run command
Best of all, pipx runs with regular user permissions, never calling sudo pip install (you aren't doing that, are you?
😄).

### Walkthrough: Installing a Package and its Applications With pipx

You can globally install an application by running
This automatically creates a virtual environment, installs the package, and adds the package's associated applications
(entry points) to a location on your PATH . For example, pipx install pycowsay makes the pycowsay command available
globally, but sandboxes the pycowsay package in its own virtual environment. pipx never needs to run as sudo to do
this.
Example:

### Installing from Source Control

You can also install from a git repository. Here, black is used as an example.
The pip syntax with egg must be used when installing extras:

### Inject a package

If an application installed by pipx requires additional packages, you can add them with pipx inject. For example, if you have ipython installed and want to add the matplotlib package to it, you would use:
You can inject multiple packages by specifying them all on the command line,
or by listing them in a text file, with one package per line,
or a combination. For example:

### Walkthrough: Running an Application in a Temporary Virtual Environment

This is an alternative to pipx install .
pipx run downloads and runs the above mentioned Python "apps" in a one-time, temporary environment, leaving your
system untouched afterwards.
This can be handy when you need to run the latest version of an app, but don't necessarily want it installed on your
computer.
You may want to do this when you are initializing a new project and want to set up the right directory structure, when
you want to view the help text of an application, or if you simply want to run an app in a one-off case and leave your
system untouched afterwards.
For example, the blog post How to set up a perfect Python project uses pipx run to kickstart a new project with cookiecutter , a tool
that creates projects from project templates.
[LINK: cookiecutter](https://github.com/cookiecutter/cookiecutter)
A nice side benefit is that you don't have to remember to upgrade the app since pipx run will automatically run a
recent version for you.
Okay, let's see what this looks like in practice!
This will install the package in an isolated, temporary directory and invoke the app. Give it a try:
Notice that you don't need to execute any install commands to run the app .
Any arguments after the application name will be passed directly to the application:

### Ambiguous arguments

Sometimes pipx can consume arguments provided for the application:
To prevent this put double dash -- before APP. It will make pipx to forward the arguments to the right verbatim to the
application:
Re-running the same app is quick because pipx caches Virtual Environments on a per-app basis. The caches only last a few
days, and when they expire, pipx will again use the latest version of the package. This way you can be sure you're
always running a new version of the package without having to manually upgrade.

### Package with multiple apps, or the app name doesn't match the package name

If the app name does not match the package name, you can use the --spec argument to specify the PACKAGE name, and
provide the APP to run separately:
For example, the esptool package doesn't provide an executable with the same
name:
[LINK: esptool](https://github.com/espressif/esptool)
You can instead run the executables that this package provides by using --spec :
Note that the .py extension is not something you append to the executable name. It is part of the executable name, as
provided by the package. This can be anything. For example, when working with the pymodbus package:
[LINK: pymodbus](https://github.com/pymodbus-dev/pymodbus)
You can run the executables like this:

### Running a specific version of a package

The PACKAGE argument above is actually a requirement specifier . Therefore, you can
also specify specific versions, version ranges, or extras. For example:
Notice that some requirement specifiers have to be enclosed in quotes or escaped.

### Running from Source Control

You can also run from a git repository. Here, black is used as an example.

### Running from URL

You can run .py files directly, too.

### Summary

That's it! Those are the most important commands pipx offers. To see all of pipx's documentation, run pipx --help or
see the docs .
[LINK: docs](https://pipx.pypa.io/stable/docs/)

## Testimonials

## Credits

pipx was inspired by pipsi and npx . It was created
by Chad Smith and has had lots of help from contributors . The logo was created by @IrishMorales .
[LINK: pipsi](https://github.com/mitsuhiko/pipsi)
[LINK: npx](https://github.com/npm/npx)
[LINK: Chad Smith](https://github.com/cs01/)
[LINK: contributors](https://github.com/pypa/pipx/graphs/contributors)
[LINK: @IrishMorales](https://github.com/IrishMorales)
pipx is maintained by a team of volunteers (in alphabetical order)
- Bernát Gábor
[LINK: Bernát Gábor](https://github.com/gaborbernat)
- Chad Smith - co-lead maintainer
[LINK: Chad Smith](https://github.com/cs01)
- Chrysle
[LINK: Chrysle](https://github.com/chrysle)
- Jason Lam
[LINK: Jason Lam](https://github.com/dukecat0)
- Matthew Clapp - co-lead maintainer
[LINK: Matthew Clapp](https://github.com/itsayellow)
- Robert Offner
[LINK: Robert Offner](https://github.com/gitznik)
- Tzu-ping Chung
[LINK: Tzu-ping Chung](https://github.com/uranusjr)

## Contributing

Issues and Pull Requests are definitely welcome! Check out Contributing to
get started. Everyone who interacts with the pipx project via codebase, issue tracker, chat rooms, or otherwise is
expected to follow the PSF Code of Conduct .
[LINK: PSF Code of Conduct](https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md)

--------------------