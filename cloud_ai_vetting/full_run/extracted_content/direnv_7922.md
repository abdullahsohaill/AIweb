# Direnv
**URL:** https://direnv.net
**Page Title:** direnv – unclutter your .profile | direnv
--------------------


## direnv

## direnv – unclutter your .profile

direnv is an extension for your shell. It augments existing shells with a
new feature that can load and unload environment variables depending on the
current directory.

## Use cases

- Load 12factor apps environment variables
- Create per-project isolated development environments
- Load secrets for deployment

## How it works

Before each prompt, direnv checks for the existence of a .envrc file (and optionally a .env file) in the current
and parent directories. If the file exists (and is authorized), it is loaded
into a bash sub-shell and all exported variables are then captured by
direnv and then made available to the current shell.
It supports hooks for all the common shells like bash, zsh, tcsh and fish.
This allows project-specific environment variables without cluttering the ~/.profile file.
Because direnv is compiled into a single static executable, it is fast enough
to be unnoticeable on each prompt. It is also language-agnostic and can be
used to build solutions similar to rbenv, pyenv and phpenv.

## Getting Started

### Prerequisites

- Unix-like operating system (macOS, Linux, …)
- A supported shell (bash, zsh, tcsh, fish, elvish, powershell, murex, nushell)

### Basic Installation

- direnv is packaged in most distributions already. See the installation documentation for details.
[LINK: the installation documentation](/docs/installation.html)
- hook direnv into your shell .
[LINK: hook direnv into your shell](/docs/hook.html)
Now restart your shell.

### Quick demo

To follow along in your shell once direnv is installed.

### The stdlib

Exporting variables by hand is a bit repetitive so direnv provides a set of
utility functions that are made available in the context of the .envrc file.
As an example, the PATH_add function is used to expand and prepend a path to
the $PATH environment variable. Instead of export PATH=$PWD/bin:$PATH you
can write PATH_add bin . It’s shorter and avoids a common mistake where $PATH=bin .
To find the documentation for all available functions check the direnv-stdlib(1) man page .
It’s also possible to create your own extensions by creating a bash file at ~/.config/direnv/direnvrc or ~/.config/direnv/lib/*.sh . This file is
loaded before your .envrc and thus allows you to make your own extensions to
direnv.
Note that this functionality is not supported in .env files. If the
coexistence of both is needed, one can use .envrc for leveraging stdlib and
append dotenv at the end of it to instruct direnv to also read the .env file next.

## Docs

- Install direnv
[LINK: Install direnv](/docs/installation.html)
- Hook into your shell
[LINK: Hook into your shell](/docs/hook.html)
- Develop for direnv
[LINK: Develop for direnv](/docs/development.html)
- Manage your rubies with direnv and ruby-install
[LINK: Manage your rubies with direnv and ruby-install](/docs/ruby.html)
- Using direnv with GitHub Actions
[LINK: Using direnv with GitHub Actions](/docs/github-actions.html)
- Community Wiki
[LINK: Community Wiki](https://github.com/direnv/direnv/wiki)
Make sure to take a look at the wiki! It contains all sorts of useful
information such as common recipes, editor integration, tips-and-tricks.

### Man pages

- direnv(1) man page
- direnv-fetchurl(1) man page
- direnv-stdlib(1) man page
- direnv.toml(1) man page

### FAQ

Based on GitHub issues interactions, here are the top things that have been
confusing for users:
- direnv has a standard library of functions, a collection of utilities that
I found useful to have and accumulated over the years. You can find it
here: https://github.com/direnv/direnv/blob/master/stdlib.sh
direnv has a standard library of functions, a collection of utilities that
I found useful to have and accumulated over the years. You can find it
here: https://github.com/direnv/direnv/blob/master/stdlib.sh
[LINK: https://github.com/direnv/direnv/blob/master/stdlib.sh](https://github.com/direnv/direnv/blob/master/stdlib.sh)
- It’s possible to override the stdlib with your own set of function by
adding a bash file to ~/.config/direnv/direnvrc . This file is loaded and
its content made available to any .envrc file.
It’s possible to override the stdlib with your own set of function by
adding a bash file to ~/.config/direnv/direnvrc . This file is loaded and
its content made available to any .envrc file.
- direnv is not loading the .envrc into the current shell. It’s creating a
new bash sub-process to load the stdlib, direnvrc and .envrc , and only
exports the environment diff back to the original shell. This allows direnv
to record the environment changes accurately and also work with all sorts
of shells. It also means that aliases and functions are not exportable
right now.
direnv is not loading the .envrc into the current shell. It’s creating a
new bash sub-process to load the stdlib, direnvrc and .envrc , and only
exports the environment diff back to the original shell. This allows direnv
to record the environment changes accurately and also work with all sorts
of shells. It also means that aliases and functions are not exportable
right now.

## Contributing

Bug reports, contributions and forks are welcome. All bugs or other forms of
discussion happen on http://github.com/direnv/direnv/issues .
[LINK: http://github.com/direnv/direnv/issues](http://github.com/direnv/direnv/issues)
Or drop by on Matrix to
have a chat. If you ask a question make sure to stay around as not everyone is
active all day.

### Testing

To run our tests, use these commands: (you may need to install homebrew )

## Complementary projects

Here is a list of projects you might want to look into if you are using direnv.
- starship - A cross-shell prompt.
- Projects for Nix integration - choose from one of a variety of projects offering improvements over Direnv’s built-in use_nix implementation.
[LINK: Projects for Nix integration](https://github.com/direnv/direnv/wiki/Nix)

## Related projects

Here is a list of other projects found in the same design space. Feel free to
submit new ones.
- Environment Modules - one of the oldest (in a good way) environment-loading systems
- autoenv - older, popular, and lightweight.
[LINK: autoenv](https://github.com/hyperupcall/autoenv)
- zsh-autoenv - a feature-rich mixture of autoenv and smartcd : enter/leave events, nesting, stashing (Zsh-only).
[LINK: zsh-autoenv](https://github.com/Tarrasch/zsh-autoenv)
[LINK: smartcd](https://github.com/cxreg/smartcd)
- asdf - a pure bash solution that has a plugin system. The asdf-direnv plugin allows using asdf managed tools with direnv.
[LINK: asdf](https://github.com/asdf-vm/asdf)
[LINK: asdf-direnv](https://github.com/asdf-community/asdf-direnv)
- ondir - OnDir is a small program to automate tasks specific to certain directories
[LINK: ondir](https://github.com/alecthomas/ondir)
- shadowenv - uses an s-expression format to define environment changes that should be executed
[LINK: shadowenv](https://shopify.github.io/shadowenv/)
- quickenv - an alternative loader for .envrc files that does not hook into your shell and favors speed over convenience.
[LINK: quickenv](https://github.com/untitaker/quickenv)
- mise - direnv, make and asdf all in one tool.
[LINK: mise](https://github.com/jdx/mise)

## Commercial support

Looking for help or customization?
Get in touch with Numtide to get a quote. We make it easy for companies to
work with Open Source projects: https://numtide.com/contact

## COPYRIGHT

MIT licence - Copyright (C) 2019 @zimbatm and contributors
[LINK: @zimbatm](https://github.com/zimbatm)
[LINK: contributors](https://github.com/direnv/direnv/graphs/contributors)
[LINK: Improve this page](https://github.com/direnv/direnv/edit/master/README.md)

--------------------