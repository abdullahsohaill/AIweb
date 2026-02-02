# Prompt Toolkit
**URL:** https://python-prompt-toolkit.readthedocs.io
**Page Title:** Python Prompt Toolkit 3.0 — prompt_toolkit 3.0.52 documentation
--------------------


## Python Prompt Toolkit 3.0 ¶

prompt_toolkit is a library for building powerful interactive command line
and terminal applications in Python.
It can be a very advanced pure Python replacement for GNU readline , but it can also be
used for building full screen applications.
Some features:
- Syntax highlighting of the input while typing. (For instance, with a Pygments lexer.)
Syntax highlighting of the input while typing. (For instance, with a Pygments lexer.)
- Multi-line input editing.
Multi-line input editing.
- Advanced code completion.
Advanced code completion.
- Selecting text for copy/paste. (Both Emacs and Vi style.)
Selecting text for copy/paste. (Both Emacs and Vi style.)
- Mouse support for cursor positioning and scrolling.
Mouse support for cursor positioning and scrolling.
- Auto suggestions. (Like fish shell .)
Auto suggestions. (Like fish shell .)
- No global state.
No global state.
Like readline:
- Both Emacs and Vi key bindings.
Both Emacs and Vi key bindings.
- Reverse and forward incremental search.
Reverse and forward incremental search.
- Works well with Unicode double width characters. (Chinese input.)
Works well with Unicode double width characters. (Chinese input.)
Works everywhere:
- Pure Python. Runs on all Python versions starting at Python 3.6.
(Python 2.6 - 3.x is supported in prompt_toolkit 2.0; not 3.0).
Pure Python. Runs on all Python versions starting at Python 3.6.
(Python 2.6 - 3.x is supported in prompt_toolkit 2.0; not 3.0).
- Runs on Linux, OS X, OpenBSD and Windows systems.
Runs on Linux, OS X, OpenBSD and Windows systems.
- Lightweight, the only dependencies are Pygments and wcwidth.
Lightweight, the only dependencies are Pygments and wcwidth.
- No assumptions about I/O are made. Every prompt_toolkit application should
also run in a telnet/ssh server or an asyncio process.
No assumptions about I/O are made. Every prompt_toolkit application should
also run in a telnet/ssh server or an asyncio process.
[LINK: asyncio](https://docs.python.org/3/library/asyncio.html)
Have a look at the gallery to get an idea of what is possible.

## Getting started ¶

Go to getting started and build your first prompt.
Issues are tracked on the Github project .
[LINK: on the Github project](https://github.com/prompt-toolkit/python-prompt-toolkit)

## Thanks to: ¶

A special thanks to all the contributors for making prompt_toolkit possible.
[LINK: all the contributors](https://github.com/prompt-toolkit/python-prompt-toolkit/graphs/contributors)
Also, a special thanks to the Pygments and wcwidth libraries.
[LINK: wcwidth](https://github.com/jquast/wcwidth)

## Table of contents ¶

- Gallery Ptpython, a Python REPL Pyvim, a Vim clone Pymux, a terminal multiplexer (like tmux) in Python
- Ptpython, a Python REPL
- Pyvim, a Vim clone
- Pymux, a terminal multiplexer (like tmux) in Python
- Getting started Installation Several use cases: prompts versus full screen terminal applications A simple prompt Learning prompt_toolkit
- Installation
- Several use cases: prompts versus full screen terminal applications
- A simple prompt
- Learning prompt_toolkit
- Upgrading Upgrading to prompt_toolkit 2.0 Upgrading to prompt_toolkit 3.0
- Upgrading to prompt_toolkit 2.0
- Upgrading to prompt_toolkit 3.0
- Printing (and using) formatted text Printing plain text Formatted text
- Printing plain text
- Formatted text
- Asking for input (prompts) Hello world The PromptSession object Syntax highlighting Colors Autocompletion Input validation History Auto suggestion Adding a bottom toolbar Adding a right prompt Vi input mode Adding custom key bindings Other prompt options Cursor shapes Adding a frame Prompt in an asyncio application Reading keys from stdin, one key at a time, but without a prompt
- Hello world
- The PromptSession object
- Syntax highlighting
- Colors
- Autocompletion
- Input validation
- History
- Auto suggestion
- Adding a bottom toolbar
- Adding a right prompt
- Vi input mode
- Adding custom key bindings
- Other prompt options
- Cursor shapes
- Adding a frame
- Prompt in an asyncio application
- Reading keys from stdin, one key at a time, but without a prompt
- Asking for a choice Coloring the options Adding a frame Adding a bottom toolbar
- Coloring the options
- Adding a frame
- Adding a bottom toolbar
- Dialogs Message box Input box Yes/No confirmation dialog Button dialog Radio list dialog Checkbox list dialog Styling of dialogs Styling reference sheet
- Message box
- Input box
- Yes/No confirmation dialog
- Button dialog
- Radio list dialog
- Checkbox list dialog
- Styling of dialogs
- Styling reference sheet
- Progress bars Simple progress bar Multiple parallel tasks Adding a title and label Formatting the progress bar Adding key bindings and toolbar
- Simple progress bar
- Multiple parallel tasks
- Adding a title and label
- Formatting the progress bar
- Adding key bindings and toolbar
- Building full screen applications A simple application I/O objects The layout Key bindings More about the Window class More about buffers and BufferControl
- A simple application
- I/O objects
- The layout
- Key bindings
- More about the Window class
- More about buffers and BufferControl
- Tutorials Tutorial: Build an SQLite REPL
- Tutorial: Build an SQLite REPL
- Advanced topics More about key bindings More about styling Filters The rendering flow Running on top of the asyncio event loop Unit testing Input hooks Architecture The rendering pipeline
- More about key bindings
- More about styling
- Filters
- The rendering flow
- Running on top of the asyncio event loop
- Unit testing
- Input hooks
- Architecture
- The rendering pipeline
- Reference Application Formatted text Buffer Selection Clipboard Auto completion Document Enums History Keys Style Shortcuts Validation Auto suggestion Renderer Lexers Layout Widgets Filters Key binding Eventloop Input Output Data structures Patch stdout
- Application
- Formatted text
- Buffer
- Selection
- Clipboard
- Auto completion
- Document
- Enums
- History
- Keys
- Style
- Shortcuts
- Validation
- Auto suggestion
- Renderer
- Lexers
- Layout
- Widgets
- Filters
- Key binding
- Eventloop
- Input
- Output
- Data structures
- Patch stdout
- Related projects

## Indices and tables ¶

- Index
Index
- Module Index
Module Index
- Search Page
Search Page
Prompt_toolkit was created by Jonathan Slenders .
[LINK: Jonathan Slenders](http://github.com/prompt-toolkit/)

--------------------