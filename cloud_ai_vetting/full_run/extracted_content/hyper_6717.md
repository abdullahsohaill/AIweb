# Hyper
**URL:** https://hyper.is
**Page Title:** Hyper™
--------------------

▲ ~ # Hyper is an Electron-based

## Installation

## Project Goals

The goal of the project is to create a beautiful and extensible experience for command-line interface users, built on open web standards. In the beginning, our focus will be primarily around speed, stability and the development of the correct API for extension authors.
In the future, we anticipate the community will come up with innovative additions to enhance what could be the simplest, most powerful and well-tested interface for productivity.

## Extensions

Extensions are available on npm. We encourage everyone to include hyper in the keywords field in package.json .
Then edit $Env:AppData/Hyper/.hyper.js and add it to plugins
Hyper will show a notification when your modules are installed to $Env:AppData/Hyper/.hyper_plugins .

## Keymaps

All command keys can be changed. In order to change them, edit $Env:AppData/Hyper/.hyper.js and add your desired change to keymaps .
Then Hyper will change the default with your custom change.
Example: 'window:devtools': 'Cmd+Alt+O'
[LINK: Windows](https://github.com/vercel/hyper/blob/master/app/keymaps/win32.json)
[LINK: Linux](https://github.com/vercel/hyper/blob/master/app/keymaps/linux.json)
[LINK: macOS](https://github.com/vercel/hyper/blob/master/app/keymaps/darwin.json)

## Configuration

### Config location

Note: config at ~/.hyper.js still supported, but will be ignored, if config in application directory present. Otherwise it will be moved to the application directory at first run.
The config object seen above in .hyper.js admits the following
[LINK: in the default config](https://github.com/vercel/hyper/blob/master/app/utils/colors.js)

## Extensions API

[LINK: Extensions API](#extensions-api)
Extensions are universal Node.js modules loaded by both Electron and the renderer process.
The extension system is designed around composition of the APIs we use to build the terminal: React components and Redux actions.
Instead of exposing a custom API method or parameter for every possible customization point, we allow you to intercept and compose every bit of functionality!
The only knowledge that is therefore required to successfully extend Hyper is that of its underlying open source libraries.
You can find additional details about plugin development in the Hyper repository .
[LINK: in the Hyper repository](https://github.com/vercel/hyper/blob/master/PLUGINS.md)
Your module has to expose at least one of these methods:
Invoked when the app first loads. If a plugin reloads, it's invoked again with the existing app.
Parameters:
Invoked when each window is created. If a plugin reloads, it's invoked again with the existing windows.
Parameters:
Invoked when a plugin is removed by the user.
Parameters:
v0.5.0+ . Allows you to decorate the user's configuration. Useful for themeing or custom parameters for your plugin.
Parameters:
v0.7.0+ . Allows you to decorate the user's environment by returning a modified environment object.
Parameters:
Invoked with the Electron's Menu template. If a plugin reloads, it's called again and the menu is refreshed.
Parameters:
Allows you to decorate Electron's BrowserWindow options when a new window is created.
Parameters:
Invoked when a plugin is first loaded or subsequently reloaded in each window.
Parameters:
A custom Redux middleware that can intercept any action. Subsequently we invoke the thunk middleware, which means your middleware can next thunks.
A custom reducer for the ui , sessions or termgroups state shape.
Passes down props from <Tabs> to the <Header> component. Must return the composed props object.
Passes down props from <Tab> to the <Tabs> component. Must return the composed props object.
Passes down props from <Terms> to the <TermGroup> component. Must return the composed props object.
Passes down props from <TermGroup> to the <Term> component. Must return the composed props object.
A custom mapper for the state properties that container components receive. Note that for children components to get these properties, you have to pass them down using the corresponding methods (like getTermProps ).
[LINK: container components](https://github.com/vercel/hyper/tree/master/lib/containers)
Must return an extended object of the map passed.
A custom mapper for the dispatch properties. Must return an extended object of the map passed.
Invoked with the React Component to decorate. Must return a Higher Order Component.
Parameters:

### Module loading

The user can hot-load and hot-reload plugins by pressing Command + R (refresh). Please strive to make plugins that don't require a complete restart of the application to work.
Plugins affecting the `BrowserWindow` will the effect on new windows after hot-reload.
In the future we might do this automatically.
When developing, you can add your plugin to $Env:AppData/Hyper/.hyper_plugins/local and then specify it under the localPlugins array in .hyper.js . We load new plugins:
- Periodically (every few hours)
- When changes are made to the configuration file ( plugins or localPlugins )
- When the user clicks Plugins > Update all now
The process of reloading involves
- Running npm prune and npm install in .hyper_plugins .
- Pruning the require.cache in both electron and the renderer process
- Invoking on* methods on the existing instances and re-rendering components with the fresh decorations in place.
Note: plugins at ~/.hyper_plugins still supported, but will be ignored, if plugins in application directory present. Otherwise they will be moved to the application directory at first run.
Note: on the main process, plugins are registered as soon as possible (we fire onLoad ). On the browser, it's up to the user to trigger their load by pressing command+R. We put the user in control of the loading in this way to prevent them from losing critical work by extensions that reset state or don't preserve it correctly.

### Decorating components

We give you the ability to provide a higher order component for every piece of the Hyper UI. Its structure is as follows:
All the decorate* methods receive the following references in an object passed as the second parameter:
A helper function that shows a desktop notification. The first parameter is the title, the second is the optional body of the notification, and the third is another optional parameter which can be used to log details to the development console.
To pass these details, simply provide and object with an error property containing the information to log.
All the components accept the following two properties to extend their markup:
Your higher order component can supply a onDecorated property to the decorated component to get a reference to its instance.
Your Term higher order component can supply an onCursorMove handler property that be called when cursor has moved with an object parameter representing its relative position to Term origin:
We encourage you to maintain compatibility with other decorators. Since many can be set, don't assume that yours is the only one.
For example, if you're passing children, compose potential existing values:
Or if you use onDecorated property

### Actions and Effects

All the Redux actions are available for you to handle through your middleware and reducers. For an example, refer to the Hyperpower reference plugin.
[LINK: Redux actions](https://github.com/vercel/hyper/tree/master/lib/actions)
Side effects occur in two fundamental forms:
- Some actions dispatch other actions based on state.
- Some actions do async work by communicating over the RPC channel to the main process
In all cases, the side effect is passed as the effect key in the action and later handled by our middleware.
This means that you can override, compose or completely eliminate effects! In other words, this is how you can change the default functionality or behavior of the app.
As an example, consider the action we use to increase the font size when you press Command+= :

### The underlying terminal

Hyper achieves a lot of its speed and functionality thanks to the power of xterm.js
[LINK: xterm.js](https://github.com/xtermjs/xterm.js/)

### Additional APIs

[LINK: Additional APIs](#additional-apis)
The Electron app objects are extended with the following properties:
Electron BrowserWindow objects are extended with the following parameters:
Renderer windows are similarly extended with:
The rpc object is symmetrical between browser and renderer process. The API is the same as Node.js, with the exception that it only admits a single object as its parameters only:

### Example theme: Hyperyellow

The following extension simply alters the config to add CSS and yellow colors! Here's the code .
[LINK: code](https://github.com/vercel/hyperyellow/blob/29c4ac9748be74d7ad587b7077758ef26f6ce5c2/index.js#L1)
Themes are simply plugins! Only one hook, decorateConfig is needed:
I grabbed the class names by inspecting the term with Devtools, which you can trigger from View -> Toggle Developer Tools . When you do so, notice that some classes are automatically generated and followed by a random nonce (e.g.: term_13hv8io ). Ignore those: they change with every new window!
Notice the emphasis on playing nice with other extensions. Specifically, we create a new object, extend only the keys we are interested in, and we compose the CSS to preserve the user's setting and that of other authors':

### Example extension: Hyperpower

The following extension renders particles as the caret moves:
Let's walk through its code . First, we intercept the Redux action SESSION_ADD_DATA . You can find the full list of actions in the repository .
[LINK: its code](https://github.com/vercel/hyperpower/blob/master/index.js)
[LINK: in the repository](https://github.com/vercel/hyper/tree/master/lib/actions)
Notice that we don't re-dispatch the action, which means we never render the output of the command to the terminal. Instead, we dispatch an action of our own, which we grab in the uiReducer and later map:
We then want to decorate the <Term> component so that we can access the underlying caret.
However, <Term> is not a container that we can map props to. So we use getTermProps to pass the property further down:
The extension then returns a higher order component to wrap <Term> . Notice we pass the onDecorated property to access the base Term component and its DOM ref, and the onCursorMove property to use Hyper cursor API:
[LINK: returns](https://github.com/vercel/hyperpower/blob/master/index.js#L51)

--------------------