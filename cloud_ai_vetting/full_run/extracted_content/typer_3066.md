# Typer
**URL:** https://typer.tiangolo.com
**Page Title:** Typer
--------------------

[LINK: Skip to content](https://typer.tiangolo.com/#fastapi-of-clis)

## Typer

Typer, build great CLIs. Easy to code. Based on Python type hints.
Documentation : https://typer.tiangolo.com
Source Code : https://github.com/fastapi/typer
[LINK: https://github.com/fastapi/typer](https://github.com/fastapi/typer)
Typer is a library for building CLI applications that users will love using and developers will love creating . Based on Python type hints.
It's also a command line tool to run scripts, automatically converting them to CLI applications.
The key features are:
- Intuitive to write : Great editor support. Completion everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
- Easy to use : It's easy to use for the final users. Automatic help, and automatic completion for all shells.
- Short : Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Start simple : The simplest example adds only 2 lines of code to your app: 1 import, 1 function call .
- Grow large : Grow in complexity as much as you want, create arbitrarily complex trees of commands and groups of subcommands, with options and arguments.
- Run scripts : Typer includes a typer command/program that you can use to run scripts, automatically converting them to CLIs, even if they don't use Typer internally.

## FastAPI of CLIs ¶

Typer is FastAPI 's little sibling, it's the FastAPI of CLIs.
[LINK: FastAPI](https://fastapi.tiangolo.com)

## Installation ¶

Create and activate a virtual environment and then install Typer :

## Example ¶

### The absolute minimum ¶

- Create a file main.py with:
This script doesn't even use Typer internally. But you can use the typer command to run it as a CLI application.

### Run it ¶

Run your application with the typer command:
This is the simplest use case, not even using Typer internally, but it can already be quite useful for simple scripts.
Note : auto-completion works when you create a Python package and run it with --install-completion or when you use the typer command.

## Use Typer in your code ¶

Now let's start using Typer in your own code, update main.py with:
Now you could run it with Python directly:
Note : you can also call this same script with the typer command, but you don't need to.

## Example upgrade ¶

This was the simplest example possible.
Now let's see one a bit more complex.

### An example with two subcommands ¶

Modify the file main.py .
Create a typer.Typer() app, and create two subcommands with their parameters.
And that will:
- Explicitly create a typer.Typer app. The previous typer.run actually creates one implicitly for you.
- The previous typer.run actually creates one implicitly for you.
- Add two subcommands with @app.command() .
- Execute the app() itself, as if it was a function (instead of typer.run ).

### Run the upgraded example ¶

Check the new help:
Now check the help for the hello command:
And now check the help for the goodbye command:
Now you can try out the new command line application:
Note : If your app only has one command, by default the command name is omitted in usage: python main.py Camila . However, when there are multiple commands, you must explicitly include the command name : python main.py hello Camila . See One or Multiple Commands for more details.

### Recap ¶

In summary, you declare once the types of parameters ( CLI arguments and CLI options ) as function parameters.
You do that with standard modern Python types.
You don't have to learn a new syntax, the methods or classes of a specific library, etc.
Just standard Python .
For example, for an int :
or for a bool flag:
And similarly for files , paths , enums (choices), etc. And there are tools to create groups of subcommands , add metadata, extra validation , etc.
You get : great editor support, including completion and type checks everywhere.
Your users get : automatic --help , auto-completion in their terminal (Bash, Zsh, Fish, PowerShell) when they install your package or when using the typer command.
For a more complete example including more features, see the Tutorial - User Guide .

## Dependencies ¶

Typer stands on the shoulders of a giant. Its only internal required dependency is Click .
By default it also comes with extra standard dependencies:
- rich : to show nicely formatted errors automatically.
[LINK: rich](https://rich.readthedocs.io/en/stable/index.html)
- shellingham : to automatically detect the current shell when installing completion. With shellingham you can just use --install-completion . Without shellingham , you have to pass the name of the shell to install completion for, e.g. --install-completion bash .
[LINK: shellingham](https://github.com/sarugaku/shellingham)
- With shellingham you can just use --install-completion .
- Without shellingham , you have to pass the name of the shell to install completion for, e.g. --install-completion bash .

### typer-slim ¶

If you don't want the extra standard optional dependencies, install typer-slim instead.
When you install with:
...it includes the same code and dependencies as:
The standard extra dependencies are rich and shellingham .
Note : The typer command is only included in the typer package.

## License ¶

This project is licensed under the terms of the MIT license.

--------------------