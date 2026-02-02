# this documentation
**URL:** https://react.dev/learn/react-compiler/installation
**Page Title:** Installation – React
--------------------


## Installation

This guide will help you install and configure React Compiler in your React application.

### You will learn

- How to install React Compiler
- Basic configuration for different build tools
- How to verify your setup is working

## Prerequisites

React Compiler is designed to work best with React 19, but it also supports React 17 and 18. Learn more about React version compatibility .

## Installation

Install React Compiler as a devDependency :
Or with Yarn:
Or with pnpm:

## Basic Setup

React Compiler is designed to work by default without any configuration. However, if you need to configure it in special circumstances (for example, to target React versions below 19), refer to the compiler options reference .
The setup process depends on your build tool. React Compiler includes a Babel plugin that integrates with your build pipeline.

### Pitfall

React Compiler must run first in your Babel plugin pipeline. The compiler needs the original source information for proper analysis, so it must process your code before other transformations.

### Babel

Create or update your babel.config.js :

### Vite

If you use Vite, you can add the plugin to vite-plugin-react:
Alternatively, if you prefer a separate Babel plugin for Vite:

### Next.js

Please refer to the Next.js docs for more information.
[LINK: Next.js docs](https://nextjs.org/docs/app/api-reference/next-config-js/reactCompiler)

### React Router

Install vite-plugin-babel , and add the compiler’s Babel plugin to it:

### Webpack

A community webpack loader is now available here .
[LINK: now available here](https://github.com/SukkaW/react-compiler-webpack)

### Expo

Please refer to Expo’s docs to enable and use the React Compiler in Expo apps.
[LINK: Expo’s docs](https://docs.expo.dev/guides/react-compiler/)

### Metro (React Native)

React Native uses Babel via Metro, so refer to the Usage with Babel section for installation instructions.

### Rspack

Please refer to Rspack’s docs to enable and use the React Compiler in Rspack apps.

### Rsbuild

Please refer to Rsbuild’s docs to enable and use the React Compiler in Rsbuild apps.

## ESLint Integration

React Compiler includes an ESLint rule that helps identify code that can’t be optimized. When the ESLint rule reports an error, it means the compiler will skip optimizing that specific component or hook. This is safe: the compiler will continue optimizing other parts of your codebase. You don’t need to fix all violations immediately. Address them at your own pace to gradually increase the number of optimized components.
Install the ESLint plugin:
If you haven’t already configured eslint-plugin-react-hooks, follow the installation instructions in the readme . The compiler rules are available in the recommended-latest preset.
[LINK: installation instructions in the readme](https://github.com/facebook/react/blob/main/packages/eslint-plugin-react-hooks/README.md#installation)
The ESLint rule will:
- Identify violations of the Rules of React
- Show which components can’t be optimized
- Provide helpful error messages for fixing issues

## Verify Your Setup

After installation, verify that React Compiler is working correctly.

### Check React DevTools

Components optimized by React Compiler will show a “Memo ✨” badge in React DevTools:
- Install the React Developer Tools browser extension
[LINK: React Developer Tools](/learn/react-developer-tools)
- Open your app in development mode
- Open React DevTools
- Look for the ✨ emoji next to component names
If the compiler is working:
- Components will show a “Memo ✨” badge in React DevTools
- Expensive calculations will be automatically memoized
- No manual useMemo is required

### Check Build Output

You can also verify the compiler is running by checking your build output. The compiled code will include automatic memoization logic that the compiler adds automatically.

## Troubleshooting

### Opting out specific components

If a component is causing issues after compilation, you can temporarily opt it out using the "use no memo" directive:
This tells the compiler to skip optimization for this specific component. You should fix the underlying issue and remove the directive once resolved.
For more troubleshooting help, see the debugging guide .

## Next Steps

Now that you have React Compiler installed, learn more about:
- React version compatibility for React 17 and 18
- Configuration options to customize the compiler
- Incremental adoption strategies for existing codebases
- Debugging techniques for troubleshooting issues
- Compiling Libraries guide for compiling your React library

--------------------