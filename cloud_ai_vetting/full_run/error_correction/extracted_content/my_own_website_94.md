# my own website
**URL:** https://red-perfume.github.io
**Page Title:** Red Perfume CSS Atomizer
--------------------


## Red Perfume

## CSS Atomizer and Optimization

Red Perfume is a group of open source projects focused on simplifying CSS Atomization automation.
[LINK: API Docs](#api)

## Intro to CSS Atomization

## What is Atomization?

CSS Atomization is an optimization technique where you take in any CSS stylesheet:
Examine each CSS rule in the style sheet:
Then create new atomized classes based on the property/value pairs:
And associate the original class names to the new atomized classes:
This map of classes is then used to update any markup you have, so this:
automatically becomes this:
Because this is a build step, and the output doesn't need to be human readable, this process can even automatically shrink the class names for you.
And the generated classmap can be used in your JavaScript.
Vue.js example:
Svelte example:
JSX example:

## Why should you automatically atomize your CSS?

During the atomization process, we are essentially looking for patterns and reducing repetition. The end result is that you send much less code. It is all highly dependent on the codebase, but most save around 60%-80%. If you are already pre-atomizing your code, with a tool like Tailwind, then expect to see savings closer to 10-20%. Red Perfume will always do a better job of atomizing your code than if you try to do it by hand, so you can feel free to write your code in any style you want, with any framework, methodology, paradigm, or tooling.
When converting the Facebook.com homepage to use automated CSS atomization, they found it reduced their homepage CSS by 80% . In fact, most major tech websites (Google, Twitter, Facebook) employ this automated optimization technique.

## If the big tech companies are doing it, why isn't everyone else?

It's because, before Red-Perfume, there was no easy way to automate CSS atomization. It was possible, but only by combining dozens of libraries that weren't designed to interconnect specifically to solve this problem. So you had a lot of "glue" you had to manage, and ultimately needed a deeper knowledge of what kinds of CSS you could and couldn't write, as not everything would work with these systems.
Red-Perfume is different. Our goal is to simplify this process so that anyone can easily add atomization to their projects. As part of this approach, the entire atomization process is handled by this library, so that all features are added and all bugs are fixed in one place, resulting in a more optimized tool. The API is designed to be super easy, but fully extendible for any pipeline. And we are aiming to support any arbitrary CSS file.
Currently Red-Perfume is a work in progress, so simple CSS works fine, but more advanced CSS isn't supported yet. But we're working hard to support all of the CSS spec .
[LINK: working hard to support all of the CSS spec](https://github.com/orgs/red-perfume/projects/2)

## Getting Started

- Install Node/npm (lowest supported version not yet known, presumed to work with 12+)
- If you do not have a package.json in your project run npm init -y
- npm install --save-dev red-perfume
- npm pkg set scripts.atomize="node ./atomize.js"
- Create a file called atomize.js and set up Red Perfume in it for your project (example below)
- Then run npm run atomize
Detailed API below.

## Library API Documentation

## red-perfume-task-runner

Subject to change before v1.0.0

### Task Runner Example

You can point to files or pass strings in directly. Tasks are sequential, the output of one can feed into the input of the next. You can output to file or use lifecycle callback hooks (documented in next section).

### API Implementation Status

Status: ALPHA
The documented API is fully implemented and tested. Though there are many edge cases that have not been covered yet (see: project board ), and some features not yet implemented (also: project board ).
[LINK: project board](https://github.com/orgs/red-perfume/projects/2)
[LINK: project board](https://github.com/orgs/red-perfume/projects/2)

### Task Runner API Documentation

Top level/global settings.
Tasks API:
Tasks are an array of objects with the following API.
Styles Task API:
Markup Task API:
Scripts Task API:

### Lifecycle Callback Hooks Example

All the hooks are shown below. Most users will only use the afterOutput hooks as a simple callback to know when something has finished . Perhaps to pass along the atomized string to another plugin (to minify, or generate a report or something). These hooks are primarily for those writing 3rd party plugins. Or for existing 3rd party libraries to add documentation to their repo on how to combine them with Red Perfume.
Hook descriptions:
These are always called and in the same order. For example, afterOutput will still be called even if the out setting was undefined , the output is skipped but the hook is still called if provided.
- Global hooks: beforeValidation - Before the options object is validated and defaulted. The first thing ran before anything else. If a third party tool wants to modify your options object, doing that here first would ensure their modifications pass Red Perfume's internal API validators. afterValidation - Right after the options are validated, they will be in this state for the rest of all the hooks, unless altered by you or a 3rd party in another hook. beforeTasks - Right before we start processing the tasks array afterTasks - After the last task has been processed. This is the final hook called. Nothing else happens after this. Includes an array where each object is the resulting data from a task.
- beforeValidation - Before the options object is validated and defaulted. The first thing ran before anything else. If a third party tool wants to modify your options object, doing that here first would ensure their modifications pass Red Perfume's internal API validators.
- afterValidation - Right after the options are validated, they will be in this state for the rest of all the hooks, unless altered by you or a 3rd party in another hook.
- beforeTasks - Right before we start processing the tasks array
- afterTasks - After the last task has been processed. This is the final hook called. Nothing else happens after this. Includes an array where each object is the resulting data from a task.
- Task hooks beforeTask - Ran right before a task starts. afterTask - Ran right after a task finishes.
- beforeTask - Ran right before a task starts.
- afterTask - Ran right after a task finishes.
- Styles/Markup hooks: beforeRead - Right before we get the string of text from files and/or data . afterRead - Right after we get the string of text from files and/or data . Also right before we atomize the string. afterProcessed - Right after the string has been atomized. Right before we output it to file if out is provided.
- beforeRead - Right before we get the string of text from files and/or data .
- afterRead - Right after we get the string of text from files and/or data . Also right before we atomize the string.
- afterProcessed - Right after the string has been atomized. Right before we output it to file if out is provided.
- Scripts hooks beforeOutput - Right before we write the JSON to disk if out is provided.
- beforeOutput - Right before we write the JSON to disk if out is provided.
- Styles/Markup/Scripts hook afterOutput - Right after the file has been written to disk if out is provided.
- afterOutput - Right after the file has been written to disk if out is provided.
Hook argument definitions:
The arguments defined here will always be the same, in every hook, with the excpection that options will be mutated during validation. However, due to the nature of JavaScript object referencing, it is very possible for 3rd party plugins you use to mutate these object values. This is intentional and allowed. Though we would encourage 3rd party libraries to just add their settings to the options object rather than mutate the data used by Red Perfume when possible, since the validation does not remove undocumented keys.
The order hooks are called in:
- Global: beforeValidation
- Global: afterValidation
- Global: beforeTasks
- Task 1: beforeTask
- Task 1 - Styles: beforeRead
- Task 1 - Styles: afterRead
- Task 1 - Styles: afterProcessed
- Task 1 - Styles: afterOutput
- Task 1 - Markup: beforeRead
- Task 1 - Markup: afterRead
- Task 1 - Markup: afterProcessed
- Task 1 - Markup: afterOutput
- Task 1 - Scripts: beforeOutput
- Task 1 - Scripts: afterOutput
- Task 1: afterTask
- Task 2: beforeTask
- Task 2 - Styles: beforeRead
- Task 2 - Styles: afterRead
- Task 2 - Styles: afterProcessed
- Task 2 - Styles: afterOutput
- Task 2 - Markup: beforeRead
- Task 2 - Markup: afterRead
- Task 2 - Markup: afterProcessed
- Task 2 - Markup: afterOutput
- Task 2 - Scripts: beforeOutput
- Task 2 - Scripts: afterOutput
- Task 2: afterTask
- Global: afterTasks

## red-perfume-css

Library for atomizing strings of CSS. It is completely synchronous.

### Red-Perfume-CSS Usage

- npm install --save-dev red-perfume-css

### CSS API Documentation

Returns: an object containing these keys

## red-perfume-html

Replaces the classes applied in HTML with atomized versions based on a class map generated by red-perfume-css (see example below).

### Red-Perfume-HTML Usage

- npm install --save-dev red-perfume-html

### HTML API Documentation

Returns: an object containing these keys

## Tutorials

As tutorial and blog posts are created relating to Red Perfume, they will be added here.
- Edit the /markdown/tutorials.md file to add to it.
[LINK: /markdown/tutorials.md](https://github.com/red-perfume/red-perfume.github.io/blob/main/markdown/tutorials.md)

## Ecosystem

As plugins and tools are created relating to Red Perfume, they will be added here.
- Edit the /markdown/ecosystem.md file to add to it.
[LINK: /markdown/ecosystem.md](https://github.com/red-perfume/red-perfume.github.io/blob/main/markdown/ecosystem.md)

## Community

- Gitter Chatroom

## About

## Why is it called "Red Perfume"

This library takes in any CSS and breaks it down to pure Atomic CSS. This is a process called "CSS Atomization", and libraries that do this process are called "CSS Atomizers".
Outside of our industry jargon, "Atomizer" already exists as a word.
Atomizer ( NOUN )
- A device for emitting water, perfume, or other liquids as a fine spray.
- Oxford English Dictionary
Though actual atomizers themselves have no consistent size, design, color, or shape. So there is no iconic image that represents them.
And though perfume bottles can also come in many shapes, colors, sizes and designs, they are still recognizable as perfume bottles.

## Contributors

- Library creation, design, maintenance - The Jared Wilcurt
- Library AST Manipulation - Alex Daigre, The Jared Wilcurt, Gwen Faraday
- Task Runner Library - The Jared Wilcurt, Aslam Doctor
- Logo - The Jared Wilcurt, Jason Williams, ngeshlew
- Project Management - The Jared Wilcurt
- Website design/content - The Jared Wilcurt

## License

All Red Perfume projects are open source and MIT licensed.
[LINK: MIT](https://github.com/red-perfume/red-perfume.github.io/blob/main/LICENSE)

## Code of Conduct

All Red Perfume projects use the " No Ideologies " code of conduct.
[LINK: No Ideologies](https://github.com/CodifiedConduct/coc-no-ideologies)

## 🍪 No Cookies here!

This website does not track you in any way or use any cookies.
I'm old enough to remember when that was normal! 👴📣☁️

--------------------