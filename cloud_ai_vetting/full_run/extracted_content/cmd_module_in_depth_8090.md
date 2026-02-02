# cmd module in depth
**URL:** http://pymotw.com/2/cmd
**Page Title:** cmd – Create line-oriented command processors - Python Module of the Week
--------------------


## PyMOTW

- Home
- Blog
- The Book
- About
- Site Index
If you find this information useful, consider picking up a copy of my book, The Python Standard Library By
      Example .

### Page Contents

- cmd – Create line-oriented command processors Processing Commands Command Arguments Live Help Auto-Completion Overriding Base Class Methods Configuring Cmd Through Attributes Shelling Out Alternative Inputs Commands from sys.argv
- Processing Commands
- Command Arguments
- Live Help
- Auto-Completion
- Overriding Base Class Methods
- Configuring Cmd Through Attributes
- Shelling Out
- Alternative Inputs
- Commands from sys.argv

### Navigation

Table of Contents Previous: Program Frameworks Next: shlex – Lexical analysis of shell-style syntaxes.

### This Page

Show Source

### Examples

The output from all the example programs from PyMOTW has been
generated with Python 2.7.8, unless otherwise noted. Some
of the features described here may not be available in earlier
versions of Python.
If you are looking for examples that work under Python 3, please
refer to the PyMOTW-3 section of the site.
Now available for Python 3!
Buy the book!

### Navigation

- index
- modules |
- next |
- previous |
- PyMOTW »
- Program Frameworks »

## cmd – Create line-oriented command processors ¶

The cmd module contains one public class, Cmd ,
designed to be used as a base class for command processors such as
interactive shells and other command interpreters. By default it uses readline for interactive prompt handling, command line editing,
and command completion.

## Processing Commands ¶

The interpreter uses a loop to read all lines from its input, parse
them, and then dispatch the command to an appropriate command
handler. Input lines are parsed into two parts. The command, and any
other text on the line. If the user enters a command foo bar , and
your class includes a method named do_foo() , it is called with "bar" as the only argument.
The end-of-file marker is dispatched to do_EOF() . If a command
handler returns a true value, the program will exit cleanly. So to
give a clean way to exit your interpreter, make sure to implement do_EOF() and have it return True.
This simple example program supports the “greet” command:
By running it interactively, we can demonstrate how commands are dispatched as
well as show of some of the features included in Cmd for free.
The first thing to notice is the command prompt, (Cmd) . The
prompt can be configured through the attribute prompt. If the prompt
changes as the result of a command processor, the new value is used to
query for the next command.
The help command is built into Cmd . With no arguments, it
shows the list of commands available. If you include a command you
want help on, the output is more verbose and restricted to details of
that command, when available.
If we use the greet command, do_greet() is invoked to handle it:
If your class does not include a specific command processor for a
command, the method default() is called with the entire input
line as an argument. The built-in implementation of default() reports an error.
Since do_EOF() returns True, typing Ctrl-D will drop us out of
the interpreter.
Notice that no newline is printed, so the results are a little messy.

## Command Arguments ¶

This version of the example includes a few enhancements to eliminate some of
the annoyances and add help for the greet command.
First, let’s look at the help. The docstring added to do_greet() becomes the help text for the command:
The output shows one optional argument to the greet command, person . Although the argument is optional to the command, there is a
distinction between the command and the callback method. The method
always takes the argument, but sometimes the value is an empty
string. It is left up to the command processor to determine if an
empty argument is valid, or do any further parsing and processing of
the command. In this example, if a person’s name is provided then the
greeting is personalized.
Whether an argument is given by the user or not, the value passed to the
command processor does not include the command itself. That simplifies parsing
in the command processor, if multiple arguments are needed.

## Live Help ¶

In the previous example, the formatting of the help text leaves
something to be desired. Since it comes from the docstring, it retains
the indentation from our source. We could edit the source to remove
the extra white-space, but that would leave our application looking
poorly formatted. An alternative solution is to implement a help
handler for the greet command, named help_greet() . When
present, the help handler is called on to produce help text for the
named command.
In this simple example, the text is static but formatted more nicely. It would
also be possible to use previous command state to tailor the contents of the
help text to the current context.
It is up to the help handler to actually output the help message, and not
simply return the help text for handling elsewhere.

## Auto-Completion ¶

Cmd includes support for command completion based on the
names of the commands with processor methods. The user triggers
completion by hitting the tab key at an input prompt. When multiple
completions are possible, pressing tab twice prints a list of the
options.
Once the command is known, argument completion is handled by methods with the
prefix complete_ . This allows you to assemble a list of possible completions
using your own criteria (query a database, look at at a file or directory on
the filesystem, etc.). In this case, the program has a hard-coded set of
“friends” who receive a less formal greeting than named or anonymous
strangers. A real program would probably save the list somewhere, and either
read it once and cache the contents to be scanned as needed.
When there is input text, complete_greet() returns a list of
friends that match. Otherwise, the full list of friends is returned.
If the name given is not in the list of friends, the formal greeting is given.

## Overriding Base Class Methods ¶

Cmd includes several methods that can be overridden as hooks for taking
actions or altering the base class behavior. This example is not exhaustive,
but contains many of the methods commonly useful.
cmdloop() is the main processing loop of the interpreter. You
can override it, but it is usually not necessary, since the preloop() and postloop() hooks are available.
Each iteration through cmdloop() calls onecmd() to
dispatch the command to its processor. The actual input line is parsed
with parseline() to create a tuple containing the command, and
the remaining portion of the line.
If the line is empty, emptyline() is called. The default
implementation runs the previous command again. If the line contains a
command, first precmd() is called then the processor is looked
up and invoked. If none is found, default() is called
instead. Finally postcmd() is called.
Here’s an example session with print statements added:

## Configuring Cmd Through Attributes ¶

In addition to the methods described above, there are several attributes for
controlling command interpreters.
prompt can be set to a string to be printed each time the user is asked for a
new command.
intro is the “welcome” message printed at the start of the program. cmdloop()
takes an argument for this value, or you can set it on the class directly.
When printing help, the doc_header , misc_header , undoc_header , and ruler attributes are used to format the
output.
This example class shows a command processor to let the user control the
prompt for the interactive session.

## Shelling Out ¶

To supplement the standard command processing, Cmd includes 2
special command prefixes. A question mark ( ? ) is equivalent to the
built-in help command, and can be used in the same way. An exclamation
point ( ! ) maps to do_shell() , and is intended for shelling
out to run other commands, as in this example.

## Alternative Inputs ¶

While the default mode for Cmd() is to interact with the user
through the readline library, it is also possible to pass a
series of commands in to standard input using standard Unix shell
redirection.
If you would rather have your program read the script file directly, a
few other changes may be needed. Since readline interacts with
the terminal/tty device, rather than the standard input stream, you
should disable it if you know your script is going to be reading from
a file. Also, to avoid printing superfluous prompts, you can set the
prompt to an empty string. This example shows how to open a file and
pass it as input to a modified version of the HelloWorld example.
With use_rawinput set to False and prompt set to an empty string,
we can call the script on this input file:
to produce output like:

## Commands from sys.argv ¶

You can also process command line arguments to the program as a
command for your interpreter class, instead of reading commands from
stdin or a file.  To use the command line arguments, you can call onecmd() directly, as in this example.
Since onecmd() takes a single string as input, the arguments
to the program need to be joined together before being passed in.
See also
[LINK: cmd](http://docs.python.org/2.7/library/cmd.html)

### Navigation

- index
- modules |
- next |
- previous |
- PyMOTW »
- Program Frameworks »
© Copyright Doug Hellmann .
    | | Last updated on Jul 11, 2020.
   | Created using Sphinx .
   | Design based on "Leaves" by SmallPark |

--------------------