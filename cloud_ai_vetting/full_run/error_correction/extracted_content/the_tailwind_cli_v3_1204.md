# the Tailwind CLI (v3)
**URL:** https://v3.tailwindcss.com/docs/installation
**Page Title:** Installation - Tailwind CSS
--------------------

[LINK: Tailwind CSS on GitHub](https://github.com/tailwindlabs/tailwindcss)
- Getting Started
- Installation
[LINK: Tailwind CSS v4.0 is here → Learn more in the upgrade guide.](https://tailwindcss.com/docs/upgrade-guide)
Tailwind CSS v4.0 is here →
Learn more in the upgrade guide.

## Installation

- Tailwind CLI

## Tailwind CLI

[LINK: Tailwind CLI](/docs/installation)
- Using PostCSS

## Using PostCSS

[LINK: Using PostCSS](/docs/installation/using-postcss)
- Framework Guides

## Framework Guides

[LINK: Framework Guides](/docs/installation/framework-guides)
- Play CDN

## Play CDN

[LINK: Play CDN](/docs/installation/play-cdn)

### Installing Tailwind CLI

The simplest and fastest way to get up and running with Tailwind CSS from scratch is with the Tailwind CLI tool. The CLI is also available as a standalone executable if you want to use it without installing Node.js.
- Install Tailwind CSS Install tailwindcss via npm, and create your tailwind.config.js file. Terminal npm install -D tailwindcss@3 npx tailwindcss init
Install tailwindcss via npm, and create your tailwind.config.js file.
- Configure your template paths Add the paths to all of your template files in your tailwind.config.js file. tailwind.config.js /** @type { import ( 'tailwindcss' ) . Config } */ export default { content : [ "./src/**/*.{html,js}" ] , theme : { extend : { } , } , plugins : [ ] , }
Add the paths to all of your template files in your tailwind.config.js file.
- Add the Tailwind directives to your CSS Add the @tailwind directives for each of Tailwind’s layers to your main CSS file. src/input.css @tailwind base ; @tailwind components ; @tailwind utilities ;
Add the @tailwind directives for each of Tailwind’s layers to your main CSS file.
- Start the Tailwind CLI build process Run the CLI tool to scan your template files for classes and build your CSS. Terminal npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
Run the CLI tool to scan your template files for classes and build your CSS.
- Start using Tailwind in your HTML Add your compiled CSS file to the <head> and start using Tailwind’s utility classes to style your content. src/index.html <! doctype html > < html > < head > < meta charset = " UTF-8 " > < meta name = " viewport " content = " width=device-width, initial-scale=1.0 " > < link href = " ./output.css " rel = " stylesheet " > </ head > < body > < h1 class = " text-3xl font-bold underline " > Hello world! </ h1 > </ body > </ html >
Add your compiled CSS file to the <head> and start using Tailwind’s utility classes to style your content.

## What to read next

Get familiar with some of the core concepts that make Tailwind CSS different from writing traditional CSS.
- Utility-First Fundamentals Using a utility-first workflow to build complex components from a constrained set of primitive utilities.

### Utility-First Fundamentals

[LINK: Utility-First Fundamentals](/docs/utility-first)
Using a utility-first workflow to build complex components from a constrained set of primitive utilities.
- Responsive Design Build fully responsive user interfaces that adapt to any screen size using responsive modifiers.

### Responsive Design

[LINK: Responsive Design](/docs/responsive-design)
Build fully responsive user interfaces that adapt to any screen size using responsive modifiers.
- Hover, Focus & Other States Style elements in interactive states like hover, focus, and more using conditional modifiers.

### Hover, Focus & Other States

[LINK: Hover, Focus & Other States](/docs/hover-focus-and-other-states)
Style elements in interactive states like hover, focus, and more using conditional modifiers.
- Dark Mode Optimize your site for dark mode directly in your HTML using the dark mode modifier.

### Dark Mode

[LINK: Dark Mode](/docs/dark-mode)
Optimize your site for dark mode directly in your HTML using the dark mode modifier.
- Reusing Styles Manage duplication and keep your projects maintainable by creating reusable abstractions.

### Reusing Styles

[LINK: Reusing Styles](/docs/reusing-styles)
Manage duplication and keep your projects maintainable by creating reusable abstractions.
- Customizing the Framework Customize the framework to match your brand and extend it with your own custom styles.

### Customizing the Framework

[LINK: Customizing the Framework](/docs/adding-custom-styles)
Customize the framework to match your brand and extend it with your own custom styles.

--------------------