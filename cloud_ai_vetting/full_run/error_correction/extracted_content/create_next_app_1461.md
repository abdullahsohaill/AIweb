# `create-next-app`
**URL:** https://nextjs.org/docs/app/api-reference/cli/create-next-app
**Page Title:** CLI: create-next-app | Next.js
--------------------

This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
[LINK: API Reference](/docs/app/api-reference)
[LINK: CLI](/docs/app/api-reference/cli)

## create-next-app

The create-next-app CLI allow you to create a new Next.js application using the default template or an example from a public GitHub repository. It is the easiest way to get started with Next.js.
[LINK: example](https://github.com/vercel/next.js/tree/canary/examples)
Basic usage:

## Reference

The following options are available:

## Examples

### With the default template

To create a new app using the default template, run the following command in your terminal:
On installation, you'll see the following prompts:
If you choose to customize settings , you'll see the following prompts:
After the prompts, create-next-app will create a folder with your project name and install the required dependencies.

### Linter Options

ESLint : The traditional and most popular JavaScript linter. Includes Next.js-specific rules from @next/eslint-plugin-next .
Biome : A fast, modern linter and formatter that combines the functionality of ESLint and Prettier. Includes built-in Next.js and React domain support for optimal performance.
None : Skip linter configuration entirely. You can always add a linter later.
Once you've answered the prompts, a new project will be created with your chosen configuration.

### With an official Next.js example

To create a new app using an official Next.js example, use the --example flag. For example:
You can view a list of all available examples along with setup instructions in the Next.js repository .
[LINK: Next.js repository](https://github.com/vercel/next.js/tree/canary/examples)

### With any public GitHub example

To create a new app using any public GitHub example, use the --example option with the GitHub repo's URL. For example:
Was this helpful?

--------------------