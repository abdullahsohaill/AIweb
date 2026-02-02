# Vite's default
**URL:** https://vite.dev/config/server-options.html
**Page Title:** Server Options | Vite
--------------------

Building Together
ViteConf 2025
View the replays

## Server Options ​

Unless noted, the options in this section are only applied to dev.

## server.host ​

- Type: string | boolean
- Default: 'localhost'
Specify which IP addresses the server should listen on. Set this to 0.0.0.0 or true to listen on all addresses, including LAN and public addresses.
This can be set via the CLI using --host 0.0.0.0 or --host .
NOTE
There are cases when other servers might respond instead of Vite.
The first case is when localhost is used. Node.js under v17 reorders the result of DNS-resolved addresses by default. When accessing localhost , browsers use DNS to resolve the address and that address might differ from the address which Vite is listening to. Vite prints the resolved address when it differs.
You can set dns.setDefaultResultOrder('verbatim') to disable the reordering behavior. Vite will then print the address as localhost .
[LINK: dns.setDefaultResultOrder('verbatim')](https://nodejs.org/api/dns.html#dns_dns_setdefaultresultorder_order)
The second case is when wildcard hosts (e.g. 0.0.0.0 ) are used. This is because servers listening on non-wildcard hosts take priority over those listening on wildcard hosts.
Accessing the server on WSL2 from your LAN
When running Vite on WSL2, it is not sufficient to set host: true to access the server from your LAN. See the WSL document for more details.

## server.allowedHosts ​

- Type: string[] | true
- Default: []
The hostnames that Vite is allowed to respond to. localhost and domains under .localhost and all IP addresses are allowed by default. When using HTTPS, this check is skipped.
If a string starts with . , it will allow that hostname without the . and all subdomains under the hostname. For example, .example.com will allow example.com , foo.example.com , and foo.bar.example.com . If set to true , the server is allowed to respond to requests for any hosts.
Hosts that you have control over which IP addresses they resolve to are safe to add to the list of allowed hosts.
For example, if you own a domain vite.dev , you can add vite.dev and .vite.dev to the list. If you don't own that domain and you cannot trust the owner of that domain, you should not add it.
Especially, you should never add Top-Level Domains like .com to the list. This is because anyone can purchase a domain like example.com and control the IP address it resolves to.
DANGER
Setting server.allowedHosts to true allows any website to send requests to your dev server through DNS rebinding attacks, allowing them to download your source code and content. We recommend always using an explicit list of allowed hosts. See GHSA-vg6x-rcgg-rjx6 for more details.
[LINK: GHSA-vg6x-rcgg-rjx6](https://github.com/vitejs/vite/security/advisories/GHSA-vg6x-rcgg-rjx6)
You can set the environment variable __VITE_ADDITIONAL_SERVER_ALLOWED_HOSTS to add an additional allowed host.

## server.port ​

- Type: number
- Default: 5173
Specify server port. Note if the port is already being used, Vite will automatically try the next available port so this may not be the actual port the server ends up listening on.

## server.strictPort ​

- Type: boolean
Set to true to exit if port is already in use, instead of automatically trying the next available port.

## server.https ​

- Type: https.ServerOptions
Enable TLS + HTTP/2. The value is an options object passed to https.createServer() .
[LINK: options object](https://nodejs.org/api/https.html#https_https_createserver_options_requestlistener)
A valid certificate is needed. For a basic setup, you can add @vitejs/plugin-basic-ssl to the project plugins, which will automatically create and cache a self-signed certificate. But we recommend creating your own certificates.
[LINK: @vitejs/plugin-basic-ssl](https://github.com/vitejs/vite-plugin-basic-ssl)

## server.open ​

- Type: boolean | string
Automatically open the app in the browser on server start. When the value is a string, it will be used as the URL's pathname. If you want to open the server in a specific browser you like, you can set the env process.env.BROWSER (e.g. firefox ). You can also set process.env.BROWSER_ARGS to pass additional arguments (e.g. --incognito ).
BROWSER and BROWSER_ARGS are also special environment variables you can set in the .env file to configure it. See the open package for more details.
[LINK: the open package](https://github.com/sindresorhus/open#app)
Example:

## server.proxy ​

- Type: Record<string, string | ProxyOptions>
Configure custom proxy rules for the dev server. Expects an object of { key: options } pairs. Any requests that request path starts with that key will be proxied to that specified target. If the key starts with ^ , it will be interpreted as a RegExp . The configure option can be used to access the proxy instance. If a request matches any of the configured proxy rules, the request won't be transformed by Vite.
Note that if you are using non-relative base , you must prefix each key with that base .
Extends http-proxy-3 . Additional options are here .
[LINK: http-proxy-3](https://github.com/sagemathinc/http-proxy-3#options)
[LINK: here](https://github.com/vitejs/vite/blob/main/packages/vite/src/node/server/middlewares/proxy.ts#L13)
In some cases, you might also want to configure the underlying dev server (e.g. to add custom middlewares to the internal connect app). In order to do that, you need to write your own plugin and use configureServer function.
[LINK: connect](https://github.com/senchalabs/connect)
[LINK: configureServer](/guide/api-plugin#configureserver)
Example:

## server.cors ​

- Type: boolean | CorsOptions
- Default: { origin: /^https?:\/\/(?:(?:[^:]+\.)?localhost|127\.0\.0\.1|\[::1\])(?::\d+)?$/ } (allows localhost, 127.0.0.1 and ::1 )
Configure CORS for the dev server. Pass an options object to fine tune the behavior or true to allow any origin.
[LINK: options object](https://github.com/expressjs/cors#configuration-options)
DANGER
Setting server.cors to true allows any website to send requests to your dev server and download your source code and content. We recommend always using an explicit list of allowed origins.

## server.headers ​

- Type: OutgoingHttpHeaders
Specify server response headers.

## server.hmr ​

- Type: boolean | { protocol?: string, host?: string, port?: number, path?: string, timeout?: number, overlay?: boolean, clientPort?: number, server?: Server }
Disable or configure HMR connection (in cases where the HMR websocket must use a different address from the http server).
Set server.hmr.overlay to false to disable the server error overlay.
protocol sets the WebSocket protocol used for the HMR connection: ws (WebSocket) or wss (WebSocket Secure).
clientPort is an advanced option that overrides the port only on the client side, allowing you to serve the websocket on a different port than the client code looks for it on.
When server.hmr.server is defined, Vite will process the HMR connection requests through the provided server. If not in middleware mode, Vite will attempt to process HMR connection requests through the existing server. This can be helpful when using self-signed certificates or when you want to expose Vite over a network on a single port.
Check out vite-setup-catalogue for some examples.
[LINK: vite-setup-catalogue](https://github.com/sapphi-red/vite-setup-catalogue)
NOTE
With the default configuration, reverse proxies in front of Vite are expected to support proxying WebSocket. If the Vite HMR client fails to connect WebSocket, the client will fall back to connecting the WebSocket directly to the Vite HMR server bypassing the reverse proxies:
The error that appears in the Browser when the fallback happens can be ignored. To avoid the error by directly bypassing reverse proxies, you could either:
- configure the reverse proxy to proxy WebSocket too
- set server.strictPort = true and set server.hmr.clientPort to the same value with server.port
- set server.hmr.port to a different value from server.port

## server.warmup ​

- Type: { clientFiles?: string[], ssrFiles?: string[] }
- Related: Warm Up Frequently Used Files
Warm up files to transform and cache the results in advance. This improves the initial page load during server starts and prevents transform waterfalls.
clientFiles are files that are used in the client only, while ssrFiles are files that are used in SSR only. They accept an array of file paths or tinyglobby patterns relative to the root .
Make sure to only add files that are frequently used to not overload the Vite dev server on startup.

## server.watch ​

- Type: object | null
File system watcher options to pass on to chokidar .
[LINK: chokidar](https://github.com/paulmillr/chokidar/tree/3.6.0#api)
The Vite server watcher watches the root and skips the .git/ , node_modules/ , test-results/ , and Vite's cacheDir and build.outDir directories by default. When updating a watched file, Vite will apply HMR and update the page only if needed.
If set to null , no files will be watched. server.watcher will provide a compatible event emitter, but calling add or unwatch will have no effect.
[LINK: server.watcher](/guide/api-javascript#vitedevserver)
Watching files in node_modules
It's currently not possible to watch files and packages in node_modules . For further progress and workarounds, you can follow issue #8619 .
[LINK: issue #8619](https://github.com/vitejs/vite/issues/8619)
Using Vite on Windows Subsystem for Linux (WSL) 2
When running Vite on WSL2, file system watching does not work when a file is edited by Windows applications (non-WSL2 process). This is due to a WSL2 limitation . This also applies to running on Docker with a WSL2 backend.
[LINK: a WSL2 limitation](https://github.com/microsoft/WSL/issues/4739)
To fix it, you could either:
- Recommended : Use WSL2 applications to edit your files. It is also recommended to move the project folder outside of a Windows filesystem. Accessing Windows filesystem from WSL2 is slow. Removing that overhead will improve performance.
- It is also recommended to move the project folder outside of a Windows filesystem. Accessing Windows filesystem from WSL2 is slow. Removing that overhead will improve performance.
- Set { usePolling: true } . Note that usePolling leads to high CPU utilization .
- Note that usePolling leads to high CPU utilization .
[LINK: usePolling leads to high CPU utilization](https://github.com/paulmillr/chokidar/tree/3.6.0#performance)

## server.middlewareMode ​

- Type: boolean
- Default: false
Create Vite server in middleware mode.
- Related: appType , SSR - Setting Up the Dev Server
Related: appType , SSR - Setting Up the Dev Server
- Example:
Example:

## server.fs.strict ​

- Type: boolean
- Default: true (enabled by default since Vite 2.7)
Restrict serving files outside of workspace root.

## server.fs.allow ​

- Type: string[]
Restrict files that could be served via /@fs/ . When server.fs.strict is set to true , accessing files outside this directory list that aren't imported from an allowed file will result in a 403.
Both directories and files can be provided.
Vite will search for the root of the potential workspace and use it as default. A valid workspace met the following conditions, otherwise will fall back to the project root .
- contains workspaces field in package.json
- contains one of the following file lerna.json pnpm-workspace.yaml
- lerna.json
- pnpm-workspace.yaml
Accepts a path to specify the custom workspace root. Could be a absolute path or a path relative to project root . For example:
When server.fs.allow is specified, the auto workspace root detection will be disabled. To extend the original behavior, a utility searchForWorkspaceRoot is exposed:

## server.fs.deny ​

- Type: string[]
- Default: ['.env', '.env.*', '*.{crt,pem}', '**/.git/**']
Blocklist for sensitive files being restricted to be served by Vite dev server. This will have higher priority than server.fs.allow . picomatch patterns are supported.
[LINK: picomatch patterns](https://github.com/micromatch/picomatch#globbing-features)
NOTE
This blocklist does not apply to the public directory . All files in the public directory are served without any filtering, since they are copied directly to the output directory during build.

## server.origin ​

- Type: string
Defines the origin of the generated asset URLs during development.

## server.sourcemapIgnoreList ​

- Type: false | (sourcePath: string, sourcemapPath: string) => boolean
- Default: (sourcePath) => sourcePath.includes('node_modules')
Whether or not to ignore source files in the server sourcemap, used to populate the x_google_ignoreList source map extension .
[LINK: x_google_ignoreList source map extension](https://developer.chrome.com/articles/x-google-ignore-list/)
server.sourcemapIgnoreList is the equivalent of build.rollupOptions.output.sourcemapIgnoreList for the dev server. A difference between the two config options is that the rollup function is called with a relative path for sourcePath while server.sourcemapIgnoreList is called with an absolute path. During dev, most modules have the map and the source in the same folder, so the relative path for sourcePath is the file name itself. In these cases, absolute paths makes it convenient to be used instead.
[LINK: build.rollupOptions.output.sourcemapIgnoreList](https://rollupjs.org/configuration-options/#output-sourcemapignorelist)
By default, it excludes all paths containing node_modules . You can pass false to disable this behavior, or, for full control, a function that takes the source path and sourcemap path and returns whether to ignore the source path.
Note
server.sourcemapIgnoreList and build.rollupOptions.output.sourcemapIgnoreList need to be set independently. server.sourcemapIgnoreList is a server only config and doesn't get its default value from the defined rollup options.
[LINK: server.sourcemapIgnoreList](#server-sourcemapignorelist)
[LINK: build.rollupOptions.output.sourcemapIgnoreList](https://rollupjs.org/configuration-options/#output-sourcemapignorelist)

--------------------