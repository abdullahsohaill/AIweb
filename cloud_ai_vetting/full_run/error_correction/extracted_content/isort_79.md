# isort
**URL:** https://pycqa.github.io/isort
**Page Title:** isort
--------------------


## Home

Read Latest Documentation - Browse GitHub Code Repository
[LINK: Read Latest Documentation](https://pycqa.github.io/isort/)
[LINK: Browse GitHub Code Repository](https://github.com/pycqa/isort/)
isort your imports, so you don't have to.
isort is a Python utility / library to sort imports alphabetically, and
automatically separated into sections and by type. It provides a command line
utility, Python library and plugins for various
editors to
quickly sort all your imports. It requires Python 3.7+ to run but
supports formatting Python 2 code too.
[LINK: plugins for various
editors](https://github.com/pycqa/isort/wiki/isort-Plugins)
- Try isort now from your browser!
[LINK: Try isort now from your browser!](https://pycqa.github.io/isort/docs/quick_start/0.-try.html)
- Using black? See the isort and black compatibility guide.
[LINK: Using black? See the isort and black compatibility guide.](https://pycqa.github.io/isort/docs/configuration/black_compatibility.html)
- isort has official support for pre-commit!
[LINK: isort has official support for pre-commit!](https://pycqa.github.io/isort/docs/configuration/pre-commit.html)
Before isort:
After isort:

## Installing isort

Installing isort is as simple as:
Install isort with requirements.txt support:
Install isort with Pipfile support:
Install isort with both formats support:

## Using isort

From the command line :
To run on specific files:
To apply recursively:
If globstar is enabled, isort . is equivalent to:
To view proposed changes without applying them:
Finally, to atomically run isort against a project, only applying
changes if they don't introduce syntax errors:
(Note: this is disabled by default, as it prevents isort from
running against code written using a different version of Python.)
From within Python :
or:

## Installing isort's for your preferred text editor

Several plugins have been written that enable to use isort from within a
variety of text-editors. You can find a full list of them on the isort
wiki .
Additionally, I will enthusiastically accept pull requests that include
plugins for other text editors and add documentation for them as I am
notified.
[LINK: on the isort
wiki](https://github.com/pycqa/isort/wiki/isort-Plugins)

## Multi line output modes

You will notice above the \"multi_line_output\" setting. This setting
defines how from imports wrap when they extend past the line_length
limit and has 12 possible settings .
[LINK: 12 possible settings](https://pycqa.github.io/isort/docs/configuration/multi_line_output_modes.html)

## Indentation

To change the how constant indents appear - simply change the
indent property with the following accepted formats:
- Number of spaces you would like. For example: 4 would cause standard
    4 space indentation.
- Tab
- A verbatim string with quotes around it.
For example:
is equivalent to 4.
For the import styles that use parentheses, you can control whether or
not to include a trailing comma after the last import with the include_trailing_comma option (defaults to False ).

## Intelligently Balanced Multi-line Imports

As of isort 3.1.0 support for balanced multi-line imports has been
added. With this enabled isort will dynamically change the import length
to the one that produces the most balanced grid, while staying below the
maximum import length defined.
Example:
Will be produced instead of:
To enable this set balanced_wrapping to True in your config or pass
the -e option into the command line utility.

## Custom Sections and Ordering

isort provides configuration options to change almost every aspect of how
imports are organized, ordered, or grouped together in sections.
Click here for an overview of all these options.
[LINK: Click here](https://pycqa.github.io/isort/docs/configuration/custom_sections_and_ordering.html)

## Skip processing of imports (outside of configuration)

To make isort ignore a single import simply add a comment at the end of
the import line containing the text isort:skip :
or:
To make isort skip an entire file simply add isort:skip_file to the
module's doc string:

## Adding or removing an import from multiple files

isort can be ran or configured to add / remove imports automatically.
See a complete guide here.
[LINK: See a complete guide here.](https://pycqa.github.io/isort/docs/configuration/add_or_remove_imports.html)

## Using isort to verify code

## The --check-only option

isort can also be used to verify that code is correctly formatted
by running it with -c . Any files that contain incorrectly sorted
and/or formatted imports will be outputted to stderr .
One great place this can be used is with a pre-commit git hook, such as
this one by \@acdha:
https://gist.github.com/acdha/8717683
[LINK: https://gist.github.com/acdha/8717683](https://gist.github.com/acdha/8717683)
This can help to ensure a certain level of code quality throughout a
project.

## Git hook

isort provides a hook function that can be integrated into your Git
pre-commit script to check Python code before committing.
More info here.
[LINK: More info here.](https://pycqa.github.io/isort/docs/configuration/git_hook.html)

## Setuptools integration

Upon installation, isort enables a setuptools command that checks
Python files declared by your project.
More info here.
[LINK: More info here.](https://pycqa.github.io/isort/docs/configuration/setuptools_integration.html)

## Spread the word

Place this badge at the top of your repository to let others know your project uses isort.
For README.md:
Or README.rst:

## Security contact information

To report a security vulnerability, please use the Tidelift security
contact . Tidelift will coordinate the
fix and disclosure.

## Why isort?

isort simply stands for import sort. It was originally called
"sortImports" however I got tired of typing the extra characters and
came to the realization camelCase is not pythonic.
I wrote isort because in an organization I used to work in the manager
came in one day and decided all code must have alphabetically sorted
imports. The code base was huge - and he meant for us to do it by hand.
However, being a programmer - I\'m too lazy to spend 8 hours mindlessly
performing a function, but not too lazy to spend 16 hours automating it.
I was given permission to open source sortImports and here we are :)
Get professionally supported isort with the Tidelift
Subscription
Professional support for isort is available as part of the Tidelift
Subscription .
Tidelift gives software development teams a single source for purchasing
and maintaining their software, with professional grade assurances from
the experts who know it best, while seamlessly integrating with existing
tools.
Thanks and I hope you find isort useful!
~Timothy Crosley

--------------------