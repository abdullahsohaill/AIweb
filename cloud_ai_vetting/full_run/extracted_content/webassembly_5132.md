# WebAssembly
**URL:** https://webassembly.org
**Page Title:** WebAssembly
--------------------

WebAssembly (abbreviated Wasm ) is a binary instruction format for a stack-based virtual machine. Wasm is designed as a portable compilation target for programming languages, enabling deployment on the web for client and server applications.
[LINK: MDN's WebAssembly pages](https://developer.mozilla.org/en-US/docs/WebAssembly)

### Efficient and fast

The Wasm stack machine is designed to be encoded in a size- and load-time-efficient binary format . WebAssembly aims to execute at native speed by taking advantage of common hardware capabilities available on a wide range of platforms.
[LINK: stack machine](https://webassembly.github.io/spec/core/exec/index.html)
[LINK: binary format](https://webassembly.github.io/spec/core/binary/index.html)
[LINK: common hardware capabilities](/docs/portability/#assumptions-for-efficient-execution)

### Safe

WebAssembly describes a memory-safe, sandboxed execution environment that may even be implemented inside existing JavaScript virtual machines. When embedded in the web , WebAssembly will enforce the same-origin and permissions security policies of the browser.
[LINK: execution environment](https://webassembly.github.io/spec/core/exec/index.html#linear-memory)
[LINK: embedded in the web](/docs/web/)

### Open and debuggable

WebAssembly is designed to be pretty-printed in a textual format for debugging, testing, experimenting, optimizing, learning, teaching, and writing programs by hand. The textual format will be used when viewing the source of Wasm modules on the web.
[LINK: textual format](https://webassembly.github.io/spec/core/text/index.html)
[LINK: viewing the source](/docs/faq/#will-webassembly-support-view-source-on-the-web)

### Part of the open web platform

WebAssembly is designed to maintain the versionless, feature-tested, and backwards-compatible nature of the web . WebAssembly modules will be able to call into and out of the JavaScript context and access browser functionality through the same Web APIs accessible from JavaScript. WebAssembly also supports non-web embeddings.
[LINK: nature of the web](/docs/web/)
[LINK: non-web](/docs/non-web/)

--------------------