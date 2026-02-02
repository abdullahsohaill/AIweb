# marked.js
**URL:** https://marked.js.org
**Page Title:** Marked Documentation
--------------------


## Marked Documentation

Marked is
- built for speed. *
- a low-level markdown compiler for parsing markdown without caching or blocking for long periods of time. **
- light-weight while implementing all markdown features from the supported flavors & specifications. ***
- available as a command line interface (CLI) and running in client- or server-side JavaScript projects.
* Still working on metrics for comparative analysis and definition. ** As few dependencies as possible. *** Strict compliance could result in slower processing when running comparative benchmarking.

## Demo

Checkout the demo page to see marked in action ⛹️
These documentation pages are also rendered using marked 💯

## Installation

CLI: npm install -g marked
In-browser:

## Usage

### Warning: 🚨 Marked does not sanitize the output HTML. If you are processing potentially unsafe strings, it's important to filter for possible XSS attacks. Some filtering options include DOMPurify (recommended), js-xss , sanitize-html and insane on the output HTML! 🚨

[LINK: DOMPurify](https://github.com/cure53/DOMPurify)
[LINK: js-xss](https://github.com/leizongmin/js-xss)
[LINK: sanitize-html](https://github.com/apostrophecms/sanitize-html)
[LINK: insane](https://github.com/bevacqua/insane)
⚠️ Input: special ZERO WIDTH unicode characters (for example \uFEFF ) might interfere with parsing. Some text editors add them at the start of the file (see: #2139 ).
[LINK: #2139](https://github.com/markedjs/marked/issues/2139)
CLI
CLI Config
A config file can be used to configure the marked cli.
If it is a .json file it should be a JSON object that will be passed to marked as options.
If .js is used it should have a default export of a marked options object or a function that takes marked as a parameter.
It can use the marked parameter to install extensions using marked.use .
By default the marked cli will look for a config file in your home directory in the following order.
- ~/.marked.json
- ~/.marked.js
- ~/.marked/index.js
Browser
or import esm module
Node.js
Marked offers advanced configurations and extensibility as well.

## Supported Markdown specifications

We actively support the features of the following Markdown flavors .
[LINK: Markdown flavors](https://github.com/commonmark/CommonMark/wiki/Markdown-Flavors)
By supporting the above Markdown flavors, it's possible that Marked can help you use other flavors as well; however, these are not actively supported by the community.

## List of Tools Using Marked

We actively support the usability of Marked in super-fast markdown transformation, some of Tools using Marked for single-page creations are
[LINK: zero-md](https://zerodevx.github.io/zero-md/)
[LINK: texme](https://github.com/susam/texme)
[LINK: StrapDown.js](https://naereen.github.io/StrapDown.js/)
[LINK: marked_reader](https://github.com/CNOCTAVE/marked_reader)

## Security

The only completely secure system is the one that doesn't exist in the first place. Having said that, we take the security of Marked very seriously.
Therefore, please disclose potential security issues by email to the project committers as well as the listed owners within NPM . We will provide an initial assessment of security reports within 48 hours and should apply patches within 2 weeks (also, feel free to contribute a fix for the issue).
[LINK: listed owners within NPM](https://docs.npmjs.com/cli/owner)

--------------------