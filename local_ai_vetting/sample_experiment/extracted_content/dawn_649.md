# Dawn
**URL:** https://dawn.googlesource.com/dawn
**Page Title:** dawn - Git at Google
--------------------


## Dawn, a WebGPU implementation

### Branches

- main
- chromium-gpu-experimental
- chromium/4473
- chromium/4474
- chromium/4475
- chromium/4476
- chromium/4477
- chromium/4478
- chromium/4479
- chromium/4480
- 2b7b0fb Roll Chromium from e5101f14da08 to bfdaa543b755 (681 revisions) by dawn-autoroll · 82 minutes ago main
- 431e2b6 Roll vulkan-deps from 842d54cf4892 to ae18e4e9f317 (16 revisions) by Dawn Autoroller · 3 hours ago
- c00251e Roll ANGLE from 79314d8b7b7f to a98af0b8d0fe (17 revisions) by Dawn Autoroller · 3 hours ago
- 35d0f11 Suppress Snapdragon X Elite FXC failures by Brian Sheedy · 8 hours ago
- 5ac4259 Suppress Snapdragon X Elite failures by Brian Sheedy · 10 hours ago

## Dawn, a WebGPU implementation

Dawn is an open-source and cross-platform implementation of the WebGPU standard. More precisely it implements webgpu.h that is a one-to-one mapping with the WebGPU IDL. Dawn is meant to be integrated as part of a larger system and is the underlying implementation of WebGPU in Chromium.
[LINK: webgpu.h](https://github.com/webgpu-native/webgpu-headers/blob/main/webgpu.h)
Dawn provides several WebGPU building blocks:
- WebGPU C/C++ headers that applications and other building blocks use. The webgpu.h version that Dawn implements. A C++ wrapper for the webgpu.h .
- The webgpu.h version that Dawn implements.
- A C++ wrapper for the webgpu.h .
- A “native” implementation of WebGPU using platforms' GPU APIs: D3D12, Metal, Vulkan and OpenGL. See per API support for more details.
[LINK: per API support](dawn/+/HEAD/docs/support.md)
- A client-server implementation of WebGPU for applications that are in a sandbox without access to native drivers
- Tint is a compiler for the WebGPU Shader Language (WGSL) that can be used in standalone to convert shaders from and to WGSL.
Helpful links:
- Dawn bug tracker if you find issues with Dawn. Create a new issue here .
- Tint bug tracker if you find issues with Tint. Create a new issue here .
- Dawn's mailing list for other discussions related to Dawn.
- Dawn's source code
- Dawn's Matrix chatroom for live discussion around contributing or using Dawn.
- WebGPU's Matrix chatroom
- Tint mirror for standalone usage.

## Documentation table of content

Developer documentation:
- Dawn overview
[LINK: Dawn overview](dawn/+/HEAD/docs/dawn/overview.md)
- Building
[LINK: Building](dawn/+/HEAD/docs/building.md)
- Contributing
- Code of Conduct
- Testing Dawn
[LINK: Testing Dawn](dawn/+/HEAD/docs/dawn/testing.md)
- Testing Tint
[LINK: Testing Tint](dawn/+/HEAD/docs/tint/testing.md)
- Debugging Dawn
[LINK: Debugging Dawn](dawn/+/HEAD/docs/dawn/debugging.md)
- Dawn's infrastructure
[LINK: Dawn's infrastructure](dawn/+/HEAD/docs/dawn/infra.md)
- Dawn errors
[LINK: Dawn errors](dawn/+/HEAD/docs/dawn/errors.md)
- Tint experimental extensions
[LINK: Tint experimental extensions](dawn/+/HEAD/docs/tint/experimental_extensions.md)
- Quickstart with CMake
[LINK: Quickstart with CMake](dawn/+/HEAD/docs/quickstart-cmake.md)
- Becoming a committer
[LINK: Becoming a committer](dawn/+/HEAD/docs/becoming-committer.md)
User documentation: (TODO, figure out what overlaps with the webgpu.h docs)

## License

BSD 3-Clause License, please see LICENSE .

## Disclaimer

This is not an officially supported Google product.

--------------------