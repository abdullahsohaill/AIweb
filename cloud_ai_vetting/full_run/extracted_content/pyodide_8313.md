# Pyodide
**URL:** https://pyodide.org/en/stable
**Page Title:** Pyodide — Version 0.29.2
--------------------

- .rst

## Pyodide

## Contents

## Pyodide #

Pyodide is a Python distribution for the browser and Node.js based on WebAssembly.

## What is Pyodide? #

Pyodide is a port of CPython to WebAssembly/ Emscripten .
Pyodide makes it possible to install and run Python packages in the browser with micropip . Any
pure Python package with a wheel available on PyPi is supported. Many packages
with C, C++, and Rust extensions have also been ported for use with Pyodide.
These include many general-purpose packages such as regex, PyYAML, and
cryptography, and scientific Python packages including NumPy, pandas, SciPy,
Matplotlib, and scikit-learn.
[LINK: micropip](https://pyodide.org/en/stable/usage/api/micropip-api.html)
Pyodide comes with a robust Javascript ⟺ Python foreign function interface so
that you can freely mix these two languages in your code with minimal
friction. This includes full support for error handling (throw an error in one
language, catch it in the other), async/await, and much more.
When used inside a browser, Python has full access to the Web APIs.

## Try Pyodide #

Try Pyodide in a REPL directly in
your browser (no installation needed).

## What should I look at first? #

- If you wish to use a hosted distribution of Pyodide: see the Getting started documentation.
If you wish to use a hosted distribution of Pyodide: see the Getting started documentation.
- If you wish to host Pyodide yourself, you can download Pyodide from the releases
page and serve it with a web server.
If you wish to host Pyodide yourself, you can download Pyodide from the releases
page and serve it with a web server.
[LINK: releases
page](https://github.com/pyodide/pyodide/releases/)
- If you wish to use Pyodide with a bundler, see the documentation on Working with Bundlers .
If you wish to use Pyodide with a bundler, see the documentation on Working with Bundlers .
- If you are a Python package maintainer, see the documentation Building packages for Pyodide .
If you are a Python package maintainer, see the documentation Building packages for Pyodide .
- If you want to add a package to the Pyodide distribution, see the documentation on Adding Packages into Pyodide Distribution .
If you want to add a package to the Pyodide distribution, see the documentation on Adding Packages into Pyodide Distribution .
- If you wish to experiment or contribute back to the Pyodide runtime, see the documentation on Building from source .
If you wish to experiment or contribute back to the Pyodide runtime, see the documentation on Building from source .

## Table of contents #

### Using Pyodide #

- Getting started
- Downloading and deploying Pyodide
- Using Pyodide
- Accessing Files Quick Reference
- Loading packages
- Pyodide Python compatibility
- Type translations
- Interrupting execution
- Redirecting standard streams
- API Reference
[LINK: API Reference](usage/api-reference.html)
- Frequently Asked Questions
- Community Examples

### Development #

The Development section helps Pyodide contributors to find information about the
development process including making packages to support third party libraries.
Development
- Building packages for Pyodide
- Building from source
- Testing and benchmarking
- Debugging tips
- How to Contribute
- Pyodide Platform ABI

### Project #

The Project section gives additional information about the project’s
organization and latest releases.
Project
- What is Pyodide?
- Roadmap
- Code of Conduct
- Governance and Decision-making
- Change Log
- Related Projects

## Communication #

- Blog: blog.pyodide.org
Blog: blog.pyodide.org
- Mailing list: mail.python.org/mailman3/lists/pyodide.python.org/
Mailing list: mail.python.org/mailman3/lists/pyodide.python.org/
- Gitter: gitter.im/pyodide/community
Gitter: gitter.im/pyodide/community
- Twitter: twitter.com/pyodide
Twitter: twitter.com/pyodide
- Stack Overflow: stackoverflow.com/questions/tagged/pyodide
Stack Overflow: stackoverflow.com/questions/tagged/pyodide

--------------------