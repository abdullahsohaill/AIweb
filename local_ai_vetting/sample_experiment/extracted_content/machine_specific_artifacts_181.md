# machine-specific artifacts
**URL:** https://gpuweb.github.io/gpuweb
**Page Title:** WebGPU
--------------------

↑ Jump to Table of Contents ← Collapse Sidebar light dark auto

## WebGPU

Editor’s Draft , 19 January 2026
[LINK: https://gpuweb.github.io/gpuweb/](https://gpuweb.github.io/gpuweb/)
[LINK: https://github.com/gpuweb/gpuweb/blob/586e9b9debdea9843204304396a9d333e39868a1/spec/index.bs](https://github.com/gpuweb/gpuweb/blob/586e9b9debdea9843204304396a9d333e39868a1/spec/index.bs)
[LINK: GitHub](https://github.com/gpuweb/gpuweb/issues/)
[LINK: File an issue](https://github.com/gpuweb/gpuweb/issues/new)
[LINK: open issues](https://github.com/gpuweb/gpuweb/issues)
[LINK: WebGPU CTS](https://github.com/gpuweb/cts)
Copyright © 2026 World Wide Web Consortium . W3C ® liability , trademark and permissive document license rules apply.

## Abstract

WebGPU exposes an API for performing operations, such as rendering and computation, on a Graphics Processing Unit.

## Status of this document

This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the W3C standards and drafts index .
Feedback and comments on this specification are welcome. GitHub Issues are preferred for discussion on this specification. Alternatively, you can send comments to the GPU for the Web Working Group’s mailing-list, public-gpu@w3.org ( archives ).
  This draft highlights some of the pending issues that are still to be discussed in the working group.
  No decision has been taken on the outcome of these issues including whether they are valid.
[LINK: GitHub Issues](https://github.com/gpuweb/gpuweb/issues)
This document was published by the GPU for the Web Working Group as an Editor’s Draft.
The group expects to demonstrate implementation of each feature in at least two deployed browsers on top of modern GPU system APIs. The test suite will be used to build an implementation report.
This document is maintained and updated at any time. Some parts of this document are work in progress.
This document was produced by a group operating under the W3C Patent Policy . W3C maintains a public list of any patent disclosures made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent that the individual believes contains Essential Claim(s) must disclose the information in accordance with section 6 of the W3C Patent Policy .
This document is governed by the 18 August 2025 W3C Process Document .

## 1. Introduction

This section is non-normative.
Graphics Processing Units , or GPUs for short,
have been essential in enabling rich rendering and computational applications in personal computing.
WebGPU is an API that exposes the capabilities of GPU hardware for the Web.
The API is designed from the ground up to efficiently map to (post-2014) native GPU APIs.
WebGPU is not related to WebGL and does not explicitly target OpenGL ES.
WebGPU sees physical GPU hardware as GPUAdapter s. It provides a connection to an adapter via GPUDevice , which manages resources, and the device’s GPUQueue s, which execute commands. GPUDevice may have its own memory with high-speed access to the processing units. GPUBuffer and GPUTexture are the physical resources backed by GPU memory. GPUCommandBuffer and GPURenderBundle are containers for user-recorded commands. GPUShaderModule contains shader code. The other resources,
such as GPUSampler or GPUBindGroup , configure the way physical resources are used by the GPU.
GPUs execute commands encoded in GPUCommandBuffer s by feeding data through a pipeline ,
which is a mix of fixed-function and programmable stages. Programmable stages execute shaders , which are special programs designed to run on GPU hardware.
Most of the state of a pipeline is defined by
a GPURenderPipeline or a GPUComputePipeline object. The state not included
in these pipeline objects is set during encoding with commands,
such as beginRenderPass() or setBlendConstant() .

## 2. Malicious use considerations

This section is non-normative. It describes the risks associated with exposing this API on the Web.

### 2.1. Security Considerations

The security requirements for WebGPU are the same as ever for the web, and are likewise non-negotiable.
The general approach is strictly validating all the commands before they reach GPU,
ensuring that a page can only work with its own data.
A WebGPU implementation translates the workloads issued by the user into API commands specific
to the target platform. Native APIs specify the valid usage for the commands
(for example, see vkCreateDescriptorSetLayout )
and generally don’t guarantee any outcome if the valid usage rules are not followed.
This is called "undefined behavior", and it can be exploited by an attacker to access memory
they don’t own, or force the driver to execute arbitrary code.
In order to disallow insecure usage, the range of allowed WebGPU behaviors is defined for any input.
An implementation has to validate all the input from the user and only reach the driver
with the valid workloads. This document specifies all the error conditions and handling semantics.
For example, specifying the same buffer with intersecting ranges in both "source" and "destination"
of copyBufferToBuffer() results in GPUCommandEncoder generating an error, and no other operation occurring.
See § 22 Errors & Debugging for more information about error handling.
WebGPU shader s are executed by the compute units inside GPU hardware. In native APIs,
some of the shader instructions may result in undefined behavior on the GPU.
In order to address that, the shader instruction set and its defined behaviors are
strictly defined by WebGPU. When a shader is provided to createShaderModule() ,
the WebGPU implementation has to validate it
before doing any translation (to platform-specific shaders) or transformation passes.
Generally, allocating new memory may expose the leftover data of other applications running on the system.
In order to address that, WebGPU conceptually initializes all the resources to zero, although in practice
an implementation may skip this step if it sees the developer initializing the contents manually.
This includes variables and shared workgroup memory inside shaders.
The precise mechanism of clearing the workgroup memory can differ between platforms.
If the native API does not provide facilities to clear it, the WebGPU implementation transforms the compute
shader to first do a clear across all invocations, synchronize them, and continue executing developer’s code.
As a result, all implementations should issue a developer console warning about this
    potential performance penalty, even if there is no penalty in that implementation.
Shader s can access physical resource s either directly
(for example, as a "uniform" GPUBufferBinding ), or via texture unit s,
which are fixed-function hardware blocks that handle texture coordinate conversions.
Validation in the WebGPU API can only guarantee that all the inputs to the shader are provided and
they have the correct usage and types.
The WebGPU API can not guarantee that the data is accessed within bounds
if the texture unit s are not involved.
In order to prevent the shaders from accessing GPU memory an application doesn’t own,
the WebGPU implementation may enable a special mode (called "robust buffer access") in the driver
that guarantees that the access is limited to buffer bounds.
Alternatively, an implementation may transform the shader code by inserting manual bounds checks.
When this path is taken, the out-of-bound checks only apply to array indexing. They aren’t needed
for plain field access of shader structures due to the minBindingSize validation on the host side.
If the shader attempts to load data outside of physical resource bounds,
the implementation is allowed to:
- return a value at a different location within the resource bounds
return a value at a different location within the resource bounds
- return a value vector of "(0, 0, 0, X)" with any "X"
return a value vector of "(0, 0, 0, X)" with any "X"
- partially discard the draw or dispatch call
partially discard the draw or dispatch call
If the shader attempts to write data outside of physical resource bounds,
the implementation is allowed to:
- write the value to a different location within the resource bounds
write the value to a different location within the resource bounds
- discard the write operation
discard the write operation
- partially discard the draw or dispatch call
partially discard the draw or dispatch call
When uploading floating-point data from CPU to GPU,
or generating it on the GPU, we may end up with a binary representation that doesn’t correspond
to a valid number, such as infinity or NaN (not-a-number). The GPU behavior in this case is
subject to the accuracy of the GPU hardware implementation of the IEEE-754 standard.
WebGPU guarantees that introducing invalid floating-point numbers would only affect the results
of arithmetic computations and will not have other side effects.
GPU drivers are subject to bugs like any other software. If a bug occurs, an attacker
could possibly exploit the incorrect behavior of the driver to get access to unprivileged data.
In order to reduce the risk, the WebGPU working group will coordinate with GPU vendors
to integrate the WebGPU Conformance Test Suite (CTS) as part of their driver testing process,
like it was done for WebGL.
WebGPU implementations are expected to have workarounds for some of the discovered bugs,
and disable WebGPU on drivers with known bugs that can’t be worked around.
WebGPU does not expose new states to JavaScript (the content timeline ) which are
shared between agents in an agent cluster . Content timeline states such as [[mapping]] only change during
explicit content timeline tasks, like in plain JavaScript.
Writable storage buffers and other cross-invocation communication may be usable to construct
high-precision timers on the queue timeline .
The optional "timestamp-query" feature also provides high precision
timing of GPU operations. To mitigate security and privacy concerns, the timing query
values are aligned to a lower precision: see current queue timestamp . Note in particular:
- The device timeline typically runs in a process that is shared by multiple
origins, so cross-origin isolation (provided by COOP/COEP) does not provide
isolation of device/queue-timeline timers.
The device timeline typically runs in a process that is shared by multiple
origins, so cross-origin isolation (provided by COOP/COEP) does not provide
isolation of device/queue-timeline timers.
- Queue timeline work is issued from the device timeline, and may execute on GPU hardware that
does not provide the isolation expected of CPU processes (such as Meltdown mitigations).
Queue timeline work is issued from the device timeline, and may execute on GPU hardware that
does not provide the isolation expected of CPU processes (such as Meltdown mitigations).
- GPU hardware is not typically susceptible to Spectre-style attacks, but WebGPU may be
implemented in software, and software implementations may run in a shared process, preventing
isolation-based mitigations.
GPU hardware is not typically susceptible to Spectre-style attacks, but WebGPU may be
implemented in software, and software implementations may run in a shared process, preventing
isolation-based mitigations.
Row hammer is a class of attacks that exploit the
leaking of states in DRAM cells. It could be used on GPU .
WebGPU does not have any specific mitigations in place, and relies on platform-level solutions,
such as reduced memory refresh intervals.
WebGPU applications have access to GPU memory and compute units. A WebGPU implementation may limit
the available GPU memory to an application, in order to keep other applications responsive.
For GPU processing time, a WebGPU implementation may set up "watchdog" timer that makes sure an
application doesn’t cause GPU unresponsiveness for more than a few seconds.
These measures are similar to those used in WebGL.
WebGPU provides access to constrained global resources shared between different programs
(and web pages) running on the same machine. An application can try to indirectly probe
how constrained these global resources are, in order to reason about workloads performed
by other open web pages, based on the patterns of usage of these shared resources.
These issues are generally analogous to issues with Javascript,
such as system memory and CPU execution throughput. WebGPU does not provide any additional
mitigations for this.
WebGPU exposes fallible allocations from machine-global memory heaps, such as VRAM.
This allows for probing the size of the system’s remaining available memory
(for a given heap type) by attempting to allocate and watching for allocation failures.
GPUs internally have one or more (typically only two) heaps of memory
shared by all running applications. When a heap is depleted, WebGPU would fail to create a resource.
This is observable, which may allow a malicious application to guess what heaps
are used by other applications, and how much they allocate from them.
If one site uses WebGPU at the same time as another, it may observe the increase
in time it takes to process some work. For example, if a site constantly submits
compute workloads and tracks completion of work on the queue,
it may observe that something else also started using the GPU.
A GPU has many parts that can be tested independently, such as the arithmetic units,
texture sampling units, atomic units, etc. A malicious application may sense when
some of these units are stressed, and attempt to guess the workload of another
application by analyzing the stress patterns. This is analogous to the realities
of CPU execution of Javascript.
Malicious sites could abuse the capabilities exposed by WebGPU to run
computations that don’t benefit the user or their experience and instead only
benefit the site. Examples would be hidden crypto-mining, password cracking
or rainbow tables computations.
It is not possible to guard against these types of uses of the API because the
browser is not able to distinguish between valid workloads and abusive
workloads. This is a general problem with all general-purpose computation
capabilities on the Web: JavaScript, WebAssembly or WebGL. WebGPU only makes
some workloads easier to implement, or slightly more efficient to run than
using WebGL.
To mitigate this form of abuse, browsers can throttle operations on background
tabs, could warn that a tab is using a lot of resource, and restrict which
contexts are allowed to use WebGPU.
User agents can heuristically issue warnings to users about high power use,
especially due to potentially malicious usage.
If a user agent implements such a warning, it should include WebGPU usage in
its heuristics, in addition to JavaScript, WebAssembly, WebGL, and so on.

### 2.2. Privacy Considerations

The privacy considerations for WebGPU are similar to those of WebGL. GPU APIs are complex and must
expose various aspects of a device’s capabilities out of necessity in order to enable developers to
take advantage of those capabilities effectively. The general mitigation approach involves
normalizing or binning potentially identifying information and enforcing uniform behavior where
possible.
A user agent must not reveal more than 32 distinguishable configurations or buckets.
WebGPU can expose a lot of detail on the underlying GPU architecture and the device geometry.
This includes available physical adapters, many limits on the GPU and CPU resources
that could be used (such as the maximum texture size), and any optional hardware-specific
capabilities that are available.
User agents are not obligated to expose the real hardware limits, they are in full control of
how much the machine specifics are exposed. One strategy to reduce fingerprinting is binning
all the target platforms into a few number of bins. In general, the privacy impact of exposing
the hardware limits matches the one of WebGL.
The default limits are also deliberately high enough
to allow most applications to work without requesting higher limits.
All the usage of the API is validated according to the requested limits,
so the actual hardware capabilities are not exposed to the users by accident.
There are some machine-specific rasterization/precision artifacts and performance differences
that can be observed roughly in the same way as in WebGL. This applies to rasterization coverage
and patterns, interpolation precision of the varyings between shader stages, compute unit scheduling,
and more aspects of execution.
Generally, rasterization and precision fingerprints are identical across most or all
of the devices of each vendor. Performance differences are relatively intractable,
but also relatively low-signal (as with JS execution performance).
Privacy-critical applications and user agents should utilize software implementations to eliminate
such artifacts.
Another factor for differentiating users is measuring the performance of specific
operations on the GPU. Even with low precision timing, repeated execution of an operation
can show if the user’s machine is fast at specific workloads.
This is a fairly common vector (present in both WebGL and Javascript),
but it’s also low-signal and relatively intractable to truly normalize.
WebGPU compute pipelines expose access to GPU unobstructed by the fixed-function hardware.
This poses an additional risk for unique device fingerprinting. User agents can take steps
to dissociate logical GPU invocations with actual compute units to reduce this risk.
This specification doesn’t define any additional user-agent state for an origin.
However it is expected that user agents will have compilation caches for the result of expensive
compilation like GPUShaderModule , GPURenderPipeline and GPUComputePipeline .
These caches are important to improve the loading time of WebGPU applications after the first
visit.
For the specification, these caches are indifferentiable from incredibly fast compilation, but
for applications it would be easy to measure how long createComputePipelineAsync() takes to resolve. This can leak information across origins (like "did the user access a site with
this specific shader") so user agents should follow the best practices in storage partitioning .
[LINK: storage partitioning](https://github.com/privacycg/storage-partitioning)
The system’s GPU driver may also have its own cache of compiled shaders and pipelines. User agents
may want to disable these when at all possible, or add per-partition data to shaders in ways that
will make the GPU driver consider them different.
In addition to the concerns outlined in Security Considerations , driver
bugs may introduce differences in behavior that can be observed as a method of differentiating
users. The mitigations mentioned in Security Considerations apply here as well, including
coordinating with GPU vendors and implementing workarounds for known issues in the user agent.
Past experience with WebGL has demonstrated that developers have a legitimate need to be able to
identify the GPU their code is running on in order to create and maintain robust GPU-based content.
For example, to identify adapters with known driver bugs in order to work around them or to avoid
features that perform more poorly than expected on a given class of hardware.
But exposing adapter identifiers also naturally expands the amount of fingerprinting information
available, so there’s a desire to limit the precision with which we identify the adapter.
There are several mitigations that can be applied to strike a balance between enabling robust
content and preserving privacy. First is that user agents can reduce the burden on developers by
identifying and working around known driver issues, as they have since browsers began making use of
GPUs.
When adapter identifiers are exposed by default they should be as broad as possible while still
being useful. Possibly identifying, for example, the adapter’s vendor and general architecture
without identifying the specific adapter in use. Similarly, in some cases identifiers for an adapter
that is considered a reasonable proxy for the actual adapter may be reported.
In cases where full and detailed information about the adapter is useful (for example: when filing
bug reports) the user can be asked for consent to reveal additional information about their hardware
to the page.
Finally, the user agent will always have the discretion to not report adapter identifiers at all if
it considers it appropriate, such as in enhanced privacy modes.

## 3. Fundamentals

### 3.1. Conventions

In this specification, the following syntactic shorthands are used:
The phrasing " Foo.Bar " means "the Bar member of the value (or interface) Foo ."
If Foo is an ordered map and Bar does not exist in Foo , returns undefined .
The phrasing " Foo.Bar is provided " means
"the Bar member exists in the map value Foo "
The phrasing " Foo?.Bar " means
"if Foo is null or undefined or Bar does not exist in Foo , undefined ; otherwise, Foo.Bar ".
For example, where buffer is a GPUBuffer , buffer?.\[[device]].\[[adapter]] means
"if buffer is null or undefined , then undefined ; otherwise,
the \[[adapter]] internal slot of the \[[device]] internal slot of buffer .
The phrasing " x ?? y " means " x , if x is not null or undefined, and y otherwise".
A WebIDL attribute which is backed by an internal slot of the same name.
It may or may not be mutable.
A WebGPU object consists of a WebGPU Interface and an internal object .
The WebGPU interface defines the public interface and state of the WebGPU object .
It can be used on the content timeline where it was created, where it is a JavaScript-exposed
WebIDL interface.
Any interface which includes GPUObjectBase is a WebGPU interface .
The internal object tracks the state of the WebGPU object on the device timeline .
All reads/writes to the mutable state of an internal object occur from steps executing on a
single well-ordered device timeline .
The following special property types can be defined on WebGPU objects :
A read-only slot set during initialization of the object. It can be accessed from any timeline.
Note: Since the slot is immutable, implementations may have a copy on multiple timelines, as needed. Immutable properties are defined in this way to avoid describing multiple copies in this spec.
If named [[with brackets]] , it is an internal slot. If named withoutBrackets , it is a readonly slot-backed attribute of the WebGPU interface .
A property which is only accessible from the content timeline where the object was created.
If named [[with brackets]] , it is an internal slot. If named withoutBrackets , it is a slot-backed attribute of the WebGPU interface .
A property which tracks state of the internal object and is only accessible from the device timeline where the object was created. device timeline properties may be mutable.
Device timeline properties are named [[with brackets]] , and are internal slots.
A property which tracks state of the internal object and is only accessible from the queue timeline where the object was created. queue timeline properties may be mutable.
Queue timeline properties are named [[with brackets]] , and are internal slots.
- Let device be parent . [[device]] .
Let device be parent . [[device]] .
- Let object be a new instance of T .
Let object be a new instance of T .
- Set object . [[device]] to device .
Set object . [[device]] to device .
- Set object . label to descriptor . label .
Set object . label to descriptor . label .
- Return object .
Return object .
GPUObjectBase has the following immutable properties :
The device that owns the internal object .
Operations on the contents of this object assert they are running on the device timeline , and that the device is valid .
GPUObjectBase has the following content timeline properties :
A developer-provided label which is used in an implementation-defined way.
It can be used by the browser, OS, or other tools to help
identify the underlying internal object to the developer.
Examples include displaying the label in GPUError messages, console warnings,
browser developer tools, and platform debugging utilities.
However, this need not be the only way of identifying objects:
    implementations should also use other available information,
    especially when no label is available. For example:
- The label of the parent GPUTexture when printing a GPUTextureView .
The label of the parent GPUTexture when printing a GPUTextureView .
- The label of the parent GPUCommandEncoder when printing a GPURenderPassEncoder or GPUComputePassEncoder .
The label of the parent GPUCommandEncoder when printing a GPURenderPassEncoder or GPUComputePassEncoder .
- The label of the source GPUCommandEncoder when printing a GPUCommandBuffer .
The label of the source GPUCommandEncoder when printing a GPUCommandBuffer .
- The label of the source GPURenderBundleEncoder when printing a GPURenderBundle .
The label of the source GPURenderBundleEncoder when printing a GPURenderBundle .
This means one underlying object could be associated with multiple labels.
    This specification does not define how the label is propagated to the device timeline .
    How labels are used is completely implementation-defined : error messages could
    show the most recently set label, all known labels, or no labels at all.
It is defined as a USVString because some user agents may
    supply it to the debug facilities of the underlying native APIs.
GPUObjectBase has the following device timeline properties :
If true , indicates that the internal object is valid to use.
As a result, developers should assume that a WebGPU interface may remain live
    until all child objects of that interface have also been garbage collected, causing some
    resources to remain allocated longer than anticipated.
Calling the destroy method on a WebGPU interface (such as GPUDevice . destroy() or GPUBuffer . destroy() ) should be
    favored over relying on garbage collection if predictable release of allocated resources is
    needed.
An object descriptor holds the information needed to create an object,
which is typically done via one of the create* methods of GPUDevice .
GPUObjectDescriptorBase has the following members:
The initial value of GPUObjectBase.label .

### 3.2. Asynchrony

Object creation operations in WebGPU don’t return promises, but nonetheless are internally
asynchronous. Returned objects refer to internal objects which are manipulated on a device timeline . Rather than fail with exceptions or rejections, most errors that occur on a device timeline are communicated through GPUError s generated on the associated device .
Internal objects are either valid or invalid .
An invalid object will never become valid at a later time,
but some valid objects may be invalidated .
Objects are invalid from creation if it wasn’t possible to create them.
This can happen, for example, if the object descriptor doesn’t describe a valid
object, or if there is not enough memory to allocate a resource.
It can also happen if an object is created with or from another invalid object
(for example calling createView() on an invalid GPUTexture )
(for example the GPUTexture of a createView() call):
this case is referred to as contagious invalidity .
Internal objects of most types cannot become invalid after they are created, but still
may become unusable, e.g. if the owning device is lost or destroyed , or the object has a special internal state,
like buffer state " destroyed ".
Internal objects of some types can become invalid after they are created; specifically, devices , adapters , GPUCommandBuffer s, and command/pass/bundle encoders.
- object . [[valid]] must be true .
object . [[valid]] must be true .
- object . [[device]] . [[valid]] must be true .
object . [[device]] . [[valid]] must be true .
- object . [[device]] must equal targetObject . [[device]] .
object . [[device]] must equal targetObject . [[device]] .
- object . [[valid]] to false .
object . [[valid]] to false .
Several operations in WebGPU return promises.
- GPU . requestAdapter()
GPU . requestAdapter()
- GPUAdapter . requestDevice()
GPUAdapter . requestDevice()
- GPUDevice . createComputePipelineAsync()
GPUDevice . createComputePipelineAsync()
- GPUDevice . createRenderPipelineAsync()
GPUDevice . createRenderPipelineAsync()
- GPUShaderModule . getCompilationInfo()
GPUShaderModule . getCompilationInfo()
- GPUQueue . onSubmittedWorkDone()
GPUQueue . onSubmittedWorkDone()
- GPUBuffer . mapAsync()
GPUBuffer . mapAsync()
- GPUDevice . lost
GPUDevice . lost
- GPUDevice . popErrorScope()
GPUDevice . popErrorScope()
WebGPU does not make any guarantees about the order in which these promises settle
(resolve or reject), except for the following:
- For some GPUQueue q ,
    if p1 = q . onSubmittedWorkDone() is called before p2 = q . onSubmittedWorkDone() ,
    then p1 must settle before p2 .
- For some GPUQueue q and GPUBuffer b on the same GPUDevice ,
    if p1 = b . mapAsync() is called before p2 = q . onSubmittedWorkDone() ,
    then p1 must settle before p2 .
Applications must not rely on any other promise settlement ordering.

### 3.3. Coordinate Systems

Rendering operations use the following coordinate systems:
- Normalized device coordinates (or NDC) have three dimensions, where: -1.0 ≤ x ≤ 1.0 -1.0 ≤ y ≤ 1.0 0.0 ≤ z ≤ 1.0 The bottom-left corner is at (-1.0, -1.0, z). Normalized device coordinates. Note: Whether z = 0 or z = 1 is treated as the near plane is application specific. The above diagram presents z = 0 as the near plane but the observed behavior is determined by a combination of the projection matrices
used by shaders, the depthClearValue , and the depthCompare function.
Normalized device coordinates (or NDC) have three dimensions, where:
- -1.0 ≤ x ≤ 1.0
-1.0 ≤ x ≤ 1.0
- -1.0 ≤ y ≤ 1.0
-1.0 ≤ y ≤ 1.0
- 0.0 ≤ z ≤ 1.0
0.0 ≤ z ≤ 1.0
- The bottom-left corner is at (-1.0, -1.0, z).
The bottom-left corner is at (-1.0, -1.0, z).
Note: Whether z = 0 or z = 1 is treated as the near plane is application specific. The above diagram presents z = 0 as the near plane but the observed behavior is determined by a combination of the projection matrices
used by shaders, the depthClearValue , and the depthCompare function.
- Clip space coordinates have four dimensions: (x, y, z, w) Clip space coordinates are used for the the clip position of a vertex (i.e. the position output of a vertex shader),
and for the clip volume . Normalized device coordinates and clip space coordinates are related as follows:
If point p = (p.x, p.y, p.z, p.w) is in the clip volume , then its normalized device coordinates are ( p.x ÷ p.w , p.y ÷ p.w , p.z ÷ p.w ).
Clip space coordinates have four dimensions: (x, y, z, w)
- Clip space coordinates are used for the the clip position of a vertex (i.e. the position output of a vertex shader),
and for the clip volume .
Clip space coordinates are used for the the clip position of a vertex (i.e. the position output of a vertex shader),
and for the clip volume .
[LINK: position](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-position)
- Normalized device coordinates and clip space coordinates are related as follows:
If point p = (p.x, p.y, p.z, p.w) is in the clip volume , then its normalized device coordinates are ( p.x ÷ p.w , p.y ÷ p.w , p.z ÷ p.w ).
Normalized device coordinates and clip space coordinates are related as follows:
If point p = (p.x, p.y, p.z, p.w) is in the clip volume , then its normalized device coordinates are ( p.x ÷ p.w , p.y ÷ p.w , p.z ÷ p.w ).
- Framebuffer coordinates address the pixels in the framebuffer They have two dimensions. Each pixel extends 1 unit in x and y dimensions. The top-left corner is at (0.0, 0.0). x increases to the right. y increases down. See § 17 Render Passes and § 23.2.5 Rasterization . Framebuffer coordinates.
Framebuffer coordinates address the pixels in the framebuffer
- They have two dimensions.
They have two dimensions.
- Each pixel extends 1 unit in x and y dimensions.
Each pixel extends 1 unit in x and y dimensions.
- The top-left corner is at (0.0, 0.0).
The top-left corner is at (0.0, 0.0).
- x increases to the right.
x increases to the right.
- y increases down.
y increases down.
- See § 17 Render Passes and § 23.2.5 Rasterization .
See § 17 Render Passes and § 23.2.5 Rasterization .
- Viewport coordinates combine framebuffer coordinates in x and y dimensions,
with depth in z. Normally 0.0 ≤ z ≤ 1.0, but this can be modified by setting [[viewport]] . minDepth and maxDepth via setViewport()
Viewport coordinates combine framebuffer coordinates in x and y dimensions,
with depth in z.
- Normally 0.0 ≤ z ≤ 1.0, but this can be modified by setting [[viewport]] . minDepth and maxDepth via setViewport()
Normally 0.0 ≤ z ≤ 1.0, but this can be modified by setting [[viewport]] . minDepth and maxDepth via setViewport()
- Fragment coordinates match viewport coordinates .
Fragment coordinates match viewport coordinates .
- Texture coordinates , sometimes called "UV coordinates" in 2D, are used to sample
textures and have a number of components matching the texture dimension . 0 ≤ u ≤ 1.0 0 ≤ v ≤ 1.0 0 ≤ w ≤ 1.0 (0.0, 0.0, 0.0) is in the first texel in texture memory address order. (1.0, 1.0, 1.0) is in the last texel texture memory address order. 2D Texture coordinates.
Texture coordinates , sometimes called "UV coordinates" in 2D, are used to sample
textures and have a number of components matching the texture dimension .
- 0 ≤ u ≤ 1.0
0 ≤ u ≤ 1.0
- 0 ≤ v ≤ 1.0
0 ≤ v ≤ 1.0
- 0 ≤ w ≤ 1.0
0 ≤ w ≤ 1.0
- (0.0, 0.0, 0.0) is in the first texel in texture memory address order.
(0.0, 0.0, 0.0) is in the first texel in texture memory address order.
- (1.0, 1.0, 1.0) is in the last texel texture memory address order.
(1.0, 1.0, 1.0) is in the last texel texture memory address order.
- Window coordinates , or present coordinates ,
match framebuffer coordinates , and are used when interacting with
an external display or conceptually similar interface.
Window coordinates , or present coordinates ,
match framebuffer coordinates , and are used when interacting with
an external display or conceptually similar interface.
Note: WebGPU’s coordinate systems match DirectX’s coordinate systems in a graphics pipeline.

### 3.4. Programming Model

WebGPU’s behavior is described in terms of "timelines".
Each operation (defined as algorithms) occurs on a timeline.
Timelines clearly define both the order of operations, and which state is
available to which operations.
Note: This "timeline" model describes the constraints of the multi-process models of
browser engines (typically with a "content process" and "GPU process"), as well
as the GPU itself as a separate execution unit in many implementations.
Implementing WebGPU does not require timelines to execute in parallel, so does
not require multiple processes, or even multiple threads.
(It does require concurrency for cases like get a copy of the image contents of a context which synchronously blocks on another timeline to complete.)
Associated with the execution of the Web script.
It includes calling all methods described by this specification.
To issue steps to the content timeline from an operation on GPUDevice device , queue a global task for GPUDevice device with those steps.
Associated with the GPU device operations
that are issued by the user agent.
It includes creation of adapters, devices, and GPU resources
and state objects, which are typically synchronous operations from the point
of view of the user agent part that controls the GPU,
but can live in a separate OS process.
Associated with the execution of operations
on the compute units of the GPU. It includes actual draw, copy,
and compute jobs that run on the GPU.
Associated with any of the above timelines
Steps may be issued to any timeline if they only operate on immutable properties or
arguments passed from the calling steps.
Can be used on any timeline.
Can only be used on the content timeline .
Can only be used on the device timeline .
Can only be used on the queue timeline .
Immutable value example term usage.
Immutable value example term usage. Content-timeline example term usage.
Immutable value example term usage. Device-timeline example term usage.
Immutable value example term usage. Queue-timeline example term usage.
In this specification, asynchronous operations are used when the return value
depends on work that happens on any timeline other than the Content timeline .
They are represented by promises and events in API.
- User encodes a dispatchWorkgroups command by calling a method of the GPUComputePassEncoder which happens on the Content timeline .
User encodes a dispatchWorkgroups command by calling a method of the GPUComputePassEncoder which happens on the Content timeline .
- User issues GPUQueue.submit() that hands over
the GPUCommandBuffer to the user agent, which processes it
on the Device timeline by calling the OS driver to do a low-level submission.
User issues GPUQueue.submit() that hands over
the GPUCommandBuffer to the user agent, which processes it
on the Device timeline by calling the OS driver to do a low-level submission.
- The submit gets dispatched by the GPU invocation scheduler onto the
actual compute units for execution, which happens on the Queue timeline .
The submit gets dispatched by the GPU invocation scheduler onto the
actual compute units for execution, which happens on the Queue timeline .
- User fills out a GPUBufferDescriptor and creates a GPUBuffer with it,
which happens on the Content timeline .
User fills out a GPUBufferDescriptor and creates a GPUBuffer with it,
which happens on the Content timeline .
- User agent creates a low-level buffer on the Device timeline .
User agent creates a low-level buffer on the Device timeline .
- User requests to map a GPUBuffer on the Content timeline and
gets a promise in return.
User requests to map a GPUBuffer on the Content timeline and
gets a promise in return.
- User agent checks if the buffer is currently used by the GPU
and makes a reminder to itself to check back when this usage is over.
User agent checks if the buffer is currently used by the GPU
and makes a reminder to itself to check back when this usage is over.
- After the GPU operating on Queue timeline is done using the buffer,
the user agent maps it to memory and resolves the promise.
After the GPU operating on Queue timeline is done using the buffer,
the user agent maps it to memory and resolves the promise.
This section is non-normative.
Once a GPUDevice has been obtained during an application initialization routine,
we can describe the WebGPU platform as consisting of the following layers:
- User agent implementing the specification.
User agent implementing the specification.
- Operating system with low-level native API drivers for this device.
Operating system with low-level native API drivers for this device.
- Actual CPU and GPU hardware.
Actual CPU and GPU hardware.
Each layer of the WebGPU platform may have different memory types
that the user agent needs to consider when implementing the specification:
- The script-owned memory, such as an ArrayBuffer created by the script,
is generally not accessible by a GPU driver.
The script-owned memory, such as an ArrayBuffer created by the script,
is generally not accessible by a GPU driver.
- A user agent may have different processes responsible for running
the content and communication to the GPU driver.
In this case, it uses inter-process shared memory to transfer data.
A user agent may have different processes responsible for running
the content and communication to the GPU driver.
In this case, it uses inter-process shared memory to transfer data.
- Dedicated GPUs have their own memory with high bandwidth,
while integrated GPUs typically share memory with the system.
Dedicated GPUs have their own memory with high bandwidth,
while integrated GPUs typically share memory with the system.
Most physical resources are allocated in the memory of type
that is efficient for computation or rendering by the GPU.
When the user needs to provide new data to the GPU,
the data may first need to cross the process boundary in order to reach
the user agent part that communicates with the GPU driver.
Then it may need to be made visible to the driver,
which sometimes requires a copy into driver-allocated staging memory.
Finally, it may need to be transferred to the dedicated GPU memory,
potentially changing the internal layout into one
that is most efficient for GPUs to operate on.
All of these transitions are done by the WebGPU implementation of the user agent.
Note: This example describes the worst case, while in practice
the implementation might not need to cross the process boundary,
or may be able to expose the driver-managed memory directly to
the user behind an ArrayBuffer , thus avoiding any data copies.
A physical resource can be used with an internal usage by a GPU command :
Buffer with input data for draw or dispatch calls. Preserves the contents.
Allowed by buffer INDEX , buffer VERTEX , or buffer INDIRECT .
Resource bindings that are constant from the shader point of view. Preserves the contents.
Allowed by buffer UNIFORM or texture TEXTURE_BINDING .
Read/write storage resource binding.
Allowed by buffer STORAGE or texture STORAGE_BINDING .
Read-only storage resource bindings. Preserves the contents.
Allowed by buffer STORAGE or texture STORAGE_BINDING .
Texture used as a read/write output attachment or
write-only resolve target in a render pass.
Allowed by texture RENDER_ATTACHMENT .
Texture used as a read-only attachment in a render pass. Preserves the contents.
Allowed by texture RENDER_ATTACHMENT .
We define subresource to be either a whole buffer, or a texture subresource .
- Each usage in U is input , constant , storage-read , or attachment-read .
Each usage in U is input , constant , storage-read , or attachment-read .
- Each usage in U is storage . Multiple such usages are allowed even though they are writable.
This is the usage scope storage exception .
Each usage in U is storage .
Multiple such usages are allowed even though they are writable.
This is the usage scope storage exception .
- Each usage in U is attachment . Multiple such usages are allowed even though they are writable.
This is the usage scope attachment exception .
Each usage in U is attachment .
Multiple such usages are allowed even though they are writable.
This is the usage scope attachment exception .
Enforcing that the usages are only combined into a compatible usage list allows the API to limit when data races can occur in working with memory.
That property makes applications written against
WebGPU more likely to run without modification on different platforms.
- attachment-read As a depth/stencil attachment with all aspects marked read-only
(using depthReadOnly and/or stencilReadOnly as necessary).
attachment-read
As a depth/stencil attachment with all aspects marked read-only
(using depthReadOnly and/or stencilReadOnly as necessary).
- constant As a texture binding to a draw call.
constant
As a texture binding to a draw call.
- A buffer or texture may be bound as storage to two
different draw calls in a render pass.
A buffer or texture may be bound as storage to two
different draw calls in a render pass.
- Disjoint ranges of a single buffer may be bound to two different binding
points as storage . Overlapping ranges must not be bound to a single dispatch/draw call;
this is checked by " Encoder bind groups alias a writable resource ".
Disjoint ranges of a single buffer may be bound to two different binding
points as storage .
Overlapping ranges must not be bound to a single dispatch/draw call;
this is checked by " Encoder bind groups alias a writable resource ".
One slice must not be bound twice for two different attachments;
    this is checked by beginRenderPass() .
A usage scope is a map from subresource to list < internal usage >>.
Each usage scope covers a range of operations which may execute in a concurrent
fashion with each other, and therefore may only use subresources in consistent compatible usage lists within the scope.
- If usageScope [ subresource ] does not exist , set it to [] .
If usageScope [ subresource ] does not exist , set it to [] .
- Append usage to usageScope [ subresource ].
Append usage to usageScope [ subresource ].
- For each [ subresource , usage ] in A : Add subresource to B with usage usage .
For each [ subresource , usage ] in A :
- Add subresource to B with usage usage .
Add subresource to B with usage usage .
Usage scopes are constructed and validated during encoding:
- in dispatchWorkgroups()
in dispatchWorkgroups()
- in dispatchWorkgroupsIndirect()
in dispatchWorkgroupsIndirect()
- at GPURenderPassEncoder.end()
at GPURenderPassEncoder.end()
- at GPURenderBundleEncoder.finish()
at GPURenderBundleEncoder.finish()
The usage scopes are as follows:
- In a compute pass, each dispatch command ( dispatchWorkgroups() or dispatchWorkgroupsIndirect() ) is one usage scope. A subresource is used in the usage scope if it is
potentially accessible by the dispatched invocations, including: All subresources referenced by bind groups in slots used by the current GPUComputePipeline ’s [[layout]] Buffers used directly by dispatch calls (such as indirect buffers) Note: State-setting compute pass commands, like setBindGroup() ,
do not contribute their bound resources directly to a usage scope: they only change the
state that is checked in dispatch commands.
In a compute pass, each dispatch command ( dispatchWorkgroups() or dispatchWorkgroupsIndirect() ) is one usage scope.
A subresource is used in the usage scope if it is
potentially accessible by the dispatched invocations, including:
- All subresources referenced by bind groups in slots used by the current GPUComputePipeline ’s [[layout]]
All subresources referenced by bind groups in slots used by the current GPUComputePipeline ’s [[layout]]
- Buffers used directly by dispatch calls (such as indirect buffers)
Buffers used directly by dispatch calls (such as indirect buffers)
Note: State-setting compute pass commands, like setBindGroup() ,
do not contribute their bound resources directly to a usage scope: they only change the
state that is checked in dispatch commands.
- One render pass is one usage scope. A subresource is used in the usage scope if it’s referenced by any command,
including state-setting commands (unlike in compute passes), including: Buffers set by setVertexBuffer() Buffers set by setIndexBuffer() All subresources referenced by bind groups set by setBindGroup() Buffers used directly by draw calls (such as indirect buffers)
One render pass is one usage scope.
A subresource is used in the usage scope if it’s referenced by any command,
including state-setting commands (unlike in compute passes), including:
- Buffers set by setVertexBuffer()
Buffers set by setVertexBuffer()
- Buffers set by setIndexBuffer()
Buffers set by setIndexBuffer()
- All subresources referenced by bind groups set by setBindGroup()
All subresources referenced by bind groups set by setBindGroup()
- Buffers used directly by draw calls (such as indirect buffers)
Buffers used directly by draw calls (such as indirect buffers)
Note: Copy commands are standalone operations and don’t use usage scopes for validation.
They implement their own validation to prevent self-races.
- In a render pass, subresources used in any setBindGroup() call, regardless of whether the currently bound pipeline’s
shader or layout actually depends on these bindings,
or the bind group is shadowed by another 'set' call.
In a render pass, subresources used in any setBindGroup() call, regardless of whether the currently bound pipeline’s
shader or layout actually depends on these bindings,
or the bind group is shadowed by another 'set' call.
- A buffer used in any setVertexBuffer() call, regardless of whether any draw call depends on this buffer,
or whether this buffer is shadowed by another 'set' call.
A buffer used in any setVertexBuffer() call, regardless of whether any draw call depends on this buffer,
or whether this buffer is shadowed by another 'set' call.
- A buffer used in any setIndexBuffer() call, regardless of whether any draw call depends on this buffer,
or whether this buffer is shadowed by another 'set' call.
A buffer used in any setIndexBuffer() call, regardless of whether any draw call depends on this buffer,
or whether this buffer is shadowed by another 'set' call.
- A texture subresource used as a color attachment, resolve attachment, or
depth/stencil attachment in GPURenderPassDescriptor by beginRenderPass() ,
regardless of whether the shader actually depends on these attachments.
A texture subresource used as a color attachment, resolve attachment, or
depth/stencil attachment in GPURenderPassDescriptor by beginRenderPass() ,
regardless of whether the shader actually depends on these attachments.
- Resources used in bind group entries with visibility 0, or visible only
to the compute stage but used in a render pass (or vice versa).
Resources used in bind group entries with visibility 0, or visible only
to the compute stage but used in a render pass (or vice versa).

### 3.5. Core Internal Objects

An adapter identifies an implementation of WebGPU on the system:
both an instance of compute/rendering functionality on the
platform underlying a browser, and an instance of a browser’s implementation of
WebGPU on top of that functionality.
Adapters are exposed via GPUAdapter .
Adapters do not uniquely represent underlying implementations:
calling requestAdapter() multiple times returns a different adapter object each time.
Each adapter object can only be used to create one device :
upon a successful requestDevice() call, the adapter’s [[state]] changes to "consumed" .
Additionally, adapter objects may expire at any time.
Note: This ensures applications use the latest system state for adapter selection when creating a device.
It also encourages robustness to more scenarios by making them look similar: first initialization,
reinitialization due to an unplugged adapter, reinitialization due to a test GPUDevice.destroy() call, etc.
An adapter may be considered a fallback adapter if it has significant performance
caveats in exchange for some combination of wider compatibility, more predictable behavior, or
improved privacy. It is not required that a fallback adapter is available on every system.
adapter has the following immutable properties :
The features which can be used to create devices on this adapter.
The best limits which can be used to create devices on this adapter.
Each adapter limit must be the same or better than its default value
in supported limits .
If set to true indicates that the adapter is a fallback adapter .
If set to true indicates that the adapter was requested with compatibility with WebXR sessions .
Indicates the default feature level of devices created from this adapter.
adapter has the following device timeline properties :
The adapter can be used to create a device.
The adapter has already been used to create a device, and cannot be used again.
The adapter has expired for some other reason.
- Set adapter . [[adapter]] . [[state]] to "expired" .
Set adapter . [[adapter]] . [[state]] to "expired" .
A device is the logical instantiation of an adapter ,
through which internal objects are created.
Devices are exposed via GPUDevice .
A device is the exclusive owner of all internal objects created from it:
when the device becomes invalid (is lost or destroyed ),
it and all objects created on it (directly, e.g. createTexture() , or indirectly, e.g. createView() ) become
implicitly unusable .
device has the following immutable properties :
The adapter from which this device was created.
The features which can be used on this device, as computed at creation .
No additional features can be used, even if the underlying adapter can support them.
The limits which can be used on this device, as computed at creation .
No better limits can be used, even if the underlying adapter can support them.
device has the following content timeline properties :
The Content timeline GPUDevice interface which this device is associated with.
- Let features be the set of values in descriptor . requiredFeatures .
Let features be the set of values in descriptor . requiredFeatures .
- If features contains "texture-formats-tier2" : Append "texture-formats-tier1" to features .
If features contains "texture-formats-tier2" :
- Append "texture-formats-tier1" to features .
Append "texture-formats-tier1" to features .
- If features contains "texture-formats-tier1" : Append "rg11b10ufloat-renderable" to features .
If features contains "texture-formats-tier1" :
- Append "rg11b10ufloat-renderable" to features .
Append "rg11b10ufloat-renderable" to features .
- Append any default GPUFeatureName s to features as defined by the adapter . [[default feature level]] .
Append any default GPUFeatureName s to features as defined by the adapter . [[default feature level]] .
- Let limits be a new supported limits object with the default limits
as defined by the adapter . [[default feature level]] .
Let limits be a new supported limits object with the default limits
as defined by the adapter . [[default feature level]] .
- For each ( key , value ) pair in descriptor . requiredLimits : If value is not undefined and value is better than limits [ key ]: Set limits [ key ] to value .
For each ( key , value ) pair in descriptor . requiredLimits :
- If value is not undefined and value is better than limits [ key ]: Set limits [ key ] to value .
If value is not undefined and value is better than limits [ key ]:
- Set limits [ key ] to value .
Set limits [ key ] to value .
- Set limits . maxStorageBuffersPerShaderStage to max( limits . maxStorageBuffersPerShaderStage , limits . maxStorageBuffersInVertexStage , limits . maxStorageBuffersInFragmentStage ).
Set limits . maxStorageBuffersPerShaderStage to max( limits . maxStorageBuffersPerShaderStage , limits . maxStorageBuffersInVertexStage , limits . maxStorageBuffersInFragmentStage ).
- Set limits . maxStorageTexturesPerShaderStage to max( limits . maxStorageTexturesPerShaderStage , limits . maxStorageTexturesInVertexStage , limits . maxStorageTexturesInFragmentStage ).
Set limits . maxStorageTexturesPerShaderStage to max( limits . maxStorageTexturesPerShaderStage , limits . maxStorageTexturesInVertexStage , limits . maxStorageTexturesInFragmentStage ).
- If features contains "core-features-and-limits" : Set limits . maxStorageBuffersInVertexStage and limits . maxStorageBuffersInFragmentStage to limits . maxStorageBuffersPerShaderStage . Set limits . maxStorageTexturesInVertexStage and limits . maxStorageTexturesInFragmentStage to limits . maxStorageTexturesPerShaderStage .
If features contains "core-features-and-limits" :
- Set limits . maxStorageBuffersInVertexStage and limits . maxStorageBuffersInFragmentStage to limits . maxStorageBuffersPerShaderStage .
Set limits . maxStorageBuffersInVertexStage and limits . maxStorageBuffersInFragmentStage to limits . maxStorageBuffersPerShaderStage .
- Set limits . maxStorageTexturesInVertexStage and limits . maxStorageTexturesInFragmentStage to limits . maxStorageTexturesPerShaderStage .
Set limits . maxStorageTexturesInVertexStage and limits . maxStorageTexturesInFragmentStage to limits . maxStorageTexturesPerShaderStage .
- Let device be a device object.
Let device be a device object.
- Set device . [[adapter]] to adapter .
Set device . [[adapter]] to adapter .
- Set device . [[features]] to features .
Set device . [[features]] to features .
- Set device . [[limits]] to limits .
Set device . [[limits]] to limits .
- Return device .
Return device .
Any time the user agent needs to revoke access to a device, it calls lose the device ( device , "unknown" ) on the device’s device timeline ,
potentially ahead of other operations currently queued on that timeline.
If an operation fails with side effects that would observably change the state
of objects on the device or potentially corrupt internal implementation/driver state,
the device should be lost to prevent these changes from being observable.
Note: For all device losses not initiated by the application (via destroy() ),
user agents should consider issuing developer-visible warnings unconditionally ,
even if the lost promise is handled.
These scenarios should be rare, and the signal is vital to developers because most of the WebGPU
API tries to behave like nothing is wrong to avoid interrupting the runtime flow of the application:
no validation errors are raised, most promises resolve normally, etc.
- Invalidate device .
Invalidate device .
- Issue the following steps on the content timeline of device . [[content device]] : Resolve device . lost with a new GPUDeviceLostInfo with reason set to reason and message set to an implementation-defined value. Note: message should not disclose unnecessary user/system
information and should never be parsed by applications.
Issue the following steps on the content timeline of device . [[content device]] :
- Resolve device . lost with a new GPUDeviceLostInfo with reason set to reason and message set to an implementation-defined value. Note: message should not disclose unnecessary user/system
information and should never be parsed by applications.
Resolve device . lost with a new GPUDeviceLostInfo with reason set to reason and message set to an implementation-defined value.
Note: message should not disclose unnecessary user/system
information and should never be parsed by applications.
- Complete any outstanding steps that are waiting until device becomes lost .
Complete any outstanding steps that are waiting until device becomes lost .
Note: No errors are generated from a device which is lost.
    See § 22 Errors & Debugging .
- If or when the device timeline has been informed of the completion of event , or
If or when the device timeline has been informed of the completion of event , or
- If device is lost already, or when it becomes lost :
If device is lost already, or when it becomes lost :
Then issue steps on timeline .

### 3.6. Optional Capabilities

WebGPU adapters and devices have capabilities , which
describe WebGPU functionality that differs between different implementations,
typically due to hardware or system software constraints.
A capability is either a feature or a limit .
A user agent must not reveal more than 32 distinguishable configurations or buckets.
The capabilities of an adapter must conform to § 4.2.1 Adapter Capability Guarantees .
Only supported capabilities may be requested in requestDevice() ;
requesting unsupported capabilities results in failure.
The capabilities of a device are determined in " a new device " by starting with the adapter’s
defaults (no features and the default supported limits )
and adding capabilities as requested in requestDevice() .
These capabilities are enforced regardless of the capabilities of the adapter .
For privacy considerations, see § 2.2.1 Machine-specific features and limits .
A feature is a set of optional WebGPU functionality that is not supported
on all implementations, typically due to hardware or system software constraints.
All features are optional, but adapters make some guarantees about their availability
(see § 4.2.1 Adapter Capability Guarantees ).
A device supports the exact set of features determined at creation (see § 3.6 Optional Capabilities ).
API calls perform validation according to these features (not the adapter ’s features):
- Using existing API surfaces in a new way typically results in a validation error .
Using existing API surfaces in a new way typically results in a validation error .
- There are several types of optional API surface : Using a new method or enum value always throws a TypeError . Using a new dictionary member with a (correctly-typed) non-default value typically results in a validation error . Using a new WGSL enable directive always results in a createShaderModule() validation error .
There are several types of optional API surface :
- Using a new method or enum value always throws a TypeError .
Using a new method or enum value always throws a TypeError .
- Using a new dictionary member with a (correctly-typed) non-default value typically results in a validation error .
Using a new dictionary member with a (correctly-typed) non-default value typically results in a validation error .
- Using a new WGSL enable directive always results in a createShaderModule() validation error .
Using a new WGSL enable directive always results in a createShaderModule() validation error .
See the Feature Index for a description of the functionality each feature enables.
Note: Even where supported, enabling features is not necessarily desirable, as doing so may have a performance impact.
Because of this, and to improve portability across devices and implementations,
applications should generally only request features that they may actually require.
Each limit is a numeric limit on the usage of WebGPU on a device.
Note: Even where supported, setting "better" limits is not necessarily desirable, as doing so may have a performance impact.
Because of this, and to improve portability across devices and implementations, applications should
generally only request limits better than the defaults if they may actually require them.
Each limit has a default value and a compatibility mode default .
Adapters are always guaranteed to support the defaults or better (see § 4.2.1 Adapter Capability Guarantees ).
A device supports the exact set of limits determined at creation (see § 3.6 Optional Capabilities ).
API calls perform validation according to these limits (not the adapter ’s limits),
no better or worse.
For any given limit, some values are better than others.
A better limit value always relaxes validation, enabling strictly
more programs to be valid. For each limit class , "better" is defined.
Different limits have different limit classes :
The limit enforces a maximum on some value passed into the API.
Higher values are better .
May only be set to values ≥ the default .
Lower values are clamped to the default .
The limit enforces a minimum alignment on some value passed into the API; that is,
the value must be a multiple of the limit.
Lower values are better .
May only be set to powers of 2 which are ≤ the default .
Values which are not powers of 2 are invalid.
Higher powers of 2 are clamped to the default .
A supported limits object has a value for every limit defined by WebGPU:
Note: This limit is normative, but arbitrary.
        With the default binding slot limits , it is impossible
        to use 1000 bindings in one bind group, but this allows GPUBindGroupLayoutEntry . binding values up to 999.
        This limit allows implementations to treat binding space as an array,
        within reasonable memory space, rather than a sparse map structure.
Note: This limit applies to all stages. At device initialization , it is normalized with maxStorageBuffersInVertexStage and maxStorageBuffersInFragmentStage so that in the validation algorithm, each stage can be checked against just one of the three limits.
Note: This limit applies to all stages. At device initialization , it is normalized with maxStorageTexturesInVertexStage and maxStorageTexturesInFragmentStage so that in the validation algorithm, each stage can be checked against just one of the three limits.
[LINK: workgroup](https://gpuweb.github.io/gpuweb/wgsl/#address-spaces-workgroup)
GPUSupportedLimits exposes an adapter or device’s supported limits .
See GPUAdapter.limits and GPUDevice.limits .
GPUSupportedFeatures is a setlike interface. Its set entries are
the GPUFeatureName values of the features supported by an adapter or
device. It must only contain strings from the GPUFeatureName enum.
WGSLLanguageFeatures is the setlike interface of navigator.gpu. wgslLanguageFeatures .
Its set entries are the string names of the WGSL language extensions supported by the implementation (regardless of the adapter or device).
[LINK: language extensions](https://gpuweb.github.io/gpuweb/wgsl/#language-extension)
GPUAdapterInfo exposes various identifying information about an adapter.
None of the members in GPUAdapterInfo are guaranteed to be populated with any particular value;
if no value is provided, the attribute will return the empty string "" . It is at the user
agent’s discretion which values to reveal, and it is likely that on some devices none of the values
will be populated. As such, applications must be able to handle any possible GPUAdapterInfo values,
including the absence of those values.
The GPUAdapterInfo for an adapter is exposed via GPUAdapter.info and GPUDevice.adapterInfo ).
This info is immutable:
for a given adapter, each GPUAdapterInfo attribute will return the same value every time it’s accessed.
Note: Though the GPUAdapterInfo attributes are immutable once accessed , an implementation may delay the decision on
what to expose for each attribute until the first time it is accessed.
Note: Other GPUAdapter instances, even if they represent the same physical adapter, may expose
different values in GPUAdapterInfo .
However, they should expose the same values unless a specific
event has increased the amount of identifying information the page is allowed to access.
(No such events are defined by this specification.)
For privacy considerations, see § 2.2.6 Adapter Identifiers .
GPUAdapterInfo has the following attributes:
The name of the vendor of the adapter , if available. Empty string otherwise.
The name of the family or class of GPUs the adapter belongs to, if available. Empty
string otherwise.
A vendor-specific identifier for the adapter , if available. Empty string otherwise.
Note: This is a value that represents the type of adapter. For example, it may be a PCI device ID . It does not uniquely identify a given piece of
hardware like a serial number.
A human readable string describing the adapter as reported by the driver, if available.
Empty string otherwise.
Note: Because no formatting is applied to description attempting to parse
this value is not recommended. Applications which change their behavior based on the GPUAdapterInfo , such as applying workarounds for known driver issues, should rely on the
other fields when possible.
If the "subgroups" feature is supported, the minimum
supported subgroup size for the adapter .
[LINK: subgroup size](https://gpuweb.github.io/gpuweb/wgsl/#subgroup-size)
If the "subgroups" feature is supported, the maximum
supported subgroup size for the adapter .
[LINK: subgroup size](https://gpuweb.github.io/gpuweb/wgsl/#subgroup-size)
Whether the adapter is a fallback adapter .
- Let adapterInfo be a new GPUAdapterInfo .
Let adapterInfo be a new GPUAdapterInfo .
- If the vendor is known, set adapterInfo . vendor to the name of adapter ’s vendor as a normalized identifier string . To preserve privacy, the user
agent may instead set adapterInfo . vendor to the empty string or a
reasonable approximation of the vendor as a normalized identifier string .
If the vendor is known, set adapterInfo . vendor to the name of adapter ’s vendor as a normalized identifier string . To preserve privacy, the user
agent may instead set adapterInfo . vendor to the empty string or a
reasonable approximation of the vendor as a normalized identifier string .
- If |the architecture is known, set adapterInfo . architecture to a normalized identifier string representing the family or class of adapters to which adapter belongs. To preserve privacy, the user agent may instead set adapterInfo . architecture to the empty string or a reasonable
approximation of the architecture as a normalized identifier string .
If |the architecture is known, set adapterInfo . architecture to a normalized identifier string representing the family or class of adapters to which adapter belongs. To preserve privacy, the user agent may instead set adapterInfo . architecture to the empty string or a reasonable
approximation of the architecture as a normalized identifier string .
- If the device is known, set adapterInfo . device to a normalized identifier string representing a vendor-specific identifier for adapter .
To preserve privacy, the user agent may instead set adapterInfo . device to to the empty string or a reasonable approximation of a vendor-specific identifier as a normalized identifier string .
If the device is known, set adapterInfo . device to a normalized identifier string representing a vendor-specific identifier for adapter .
To preserve privacy, the user agent may instead set adapterInfo . device to to the empty string or a reasonable approximation of a vendor-specific identifier as a normalized identifier string .
- If a description is known, set adapterInfo . description to a description
of the adapter as reported by the driver. To preserve privacy, the user agent may
instead set adapterInfo . description to the empty string or a
reasonable approximation of a description.
If a description is known, set adapterInfo . description to a description
of the adapter as reported by the driver. To preserve privacy, the user agent may
instead set adapterInfo . description to the empty string or a
reasonable approximation of a description.
- If "subgroups" is supported, set subgroupMinSize to the smallest supported subgroup size. Otherwise, set this value to 4. Note: To preserve privacy, the user agent may choose to not support some features or provide values
for the property which do not distinguish different devices, but are still usable
(e.g. use the default value of 4 for all devices).
If "subgroups" is supported, set subgroupMinSize to the smallest supported subgroup size. Otherwise, set this value to 4.
Note: To preserve privacy, the user agent may choose to not support some features or provide values
for the property which do not distinguish different devices, but are still usable
(e.g. use the default value of 4 for all devices).
- If "subgroups" is supported, set subgroupMaxSize to the largest supported subgroup size. Otherwise, set this value to 128. Note: To preserve privacy, the user agent may choose to not support some features or provide values
for the property which do not distinguish different devices, but are still usable
(e.g. use the default value of 128 for all devices).
If "subgroups" is supported, set subgroupMaxSize to the largest supported subgroup size. Otherwise, set this value to 128.
Note: To preserve privacy, the user agent may choose to not support some features or provide values
for the property which do not distinguish different devices, but are still usable
(e.g. use the default value of 128 for all devices).
- Set adapterInfo . isFallbackAdapter to adapter . [[fallback]] .
Set adapterInfo . isFallbackAdapter to adapter . [[fallback]] .
- Return adapterInfo .
Return adapterInfo .
[a-z0-9]+(-[a-z0-9]+)*
- gpu
gpu
- 0x3b2f
0x3b2f
- next-gen
next-gen
- series-x20-ultra
series-x20-ultra

### 3.7. Feature Detection

This section is non-normative.
Fully implementing this specification requires implementation of everything it specifies, except
where otherwise stated (like § 3.6 Optional Capabilities ).
However, since new "core" additions are added to this specification before being exposed by
implementations, many features are designed to be feature-detectable by applications:
- Interface support can be detected with typeof InterfaceName !== 'undefined' .
Interface support can be detected with typeof InterfaceName !== 'undefined' .
- Method and attribute support can be detected with 'itemName' in InterfaceName.prototype .
Method and attribute support can be detected with 'itemName' in InterfaceName.prototype .
- New dictionary members, if they need to be detectable, generally document a specific
mechanism for feature detection. For example: unclippedDepth support is part of a device feature, "depth-clip-control" . Canvas support for toneMapping is detected using getConfiguration() .
New dictionary members, if they need to be detectable, generally document a specific
mechanism for feature detection. For example:
- unclippedDepth support is part of a device feature, "depth-clip-control" .
unclippedDepth support is part of a device feature, "depth-clip-control" .
- Canvas support for toneMapping is detected using getConfiguration() .
Canvas support for toneMapping is detected using getConfiguration() .

### 3.8. Extension Documents

"Extension Documents" are additional documents which describe new functionality which is
non-normative and not part of the WebGPU/WGSL specifications .
They describe functionality that builds upon these specifications, often including one or more new
API feature flags and/or WGSL enable directives, or interactions with other draft
web specifications.
WebGPU implementations must not expose extension functionality; doing so is a spec violation.
New functionality does not become part of the WebGPU standard until it is integrated
into the WebGPU specification (this document) and/or WGSL specification.

### 3.9. Origin Restrictions

WebGPU allows accessing image data stored in images, videos, and canvases.
Restrictions are imposed on the use of cross-domain media, because shaders can be used to
indirectly deduce the contents of textures which have been uploaded to the GPU.
WebGPU disallows uploading an image source if it is not origin-clean .
This also implies that the origin-clean flag for a
canvas rendered using WebGPU will never be set to false .
For more information on issuing CORS requests for image and video elements, consult:
- HTML § 2.5.4 CORS settings attributes
HTML § 2.5.4 CORS settings attributes
- HTML § 4.8.3 The img element img
HTML § 4.8.3 The img element img
- HTML § 4.8.11 Media elements HTMLMediaElement
HTML § 4.8.11 Media elements HTMLMediaElement

### 3.10. Task Sources

WebGPU defines a new task source called the WebGPU task source .
It is used for the uncapturederror event and GPUDevice . lost .
[LINK: task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source)
- Queue a global task on the WebGPU task source , with the global object that was used
to create device , and the steps steps .
Queue a global task on the WebGPU task source , with the global object that was used
to create device , and the steps steps .
[LINK: Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task)
WebGPU defines a new task source called the automatic expiry task source .
It is used for the automatic, timed expiry (destruction) of certain objects:
[LINK: task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source)
- GPUTexture s returned by getCurrentTexture()
GPUTexture s returned by getCurrentTexture()
- GPUExternalTexture s created from HTMLVideoElement s
GPUExternalTexture s created from HTMLVideoElement s
- Queue a global task on the automatic expiry task source , with the global object that
was used to create device , and the steps steps .
Queue a global task on the automatic expiry task source , with the global object that
was used to create device , and the steps steps .
[LINK: Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task)
Tasks from the automatic expiry task source should be processed with high priority; in
particular, once queued, they should run before user-defined (JavaScript) tasks.
Implementation note:
    It is valid to implement a high-priority expiry "task" by instead inserting additional steps at
    a fixed point inside the event loop processing model rather than running an actual task.
[LINK: event loop processing model](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model)

### 3.11. Color Spaces and Encoding

WebGPU does not provide color management. All values within WebGPU (such as texture elements)
are raw numeric values, not color-managed color values.
WebGPU does interface with color-managed outputs (via GPUCanvasConfiguration ) and inputs
(via copyExternalImageToTexture() and importExternalTexture() ).
Thus, color conversion must be performed between the WebGPU numeric values and the external color values.
Each such interface point locally defines an encoding (color space, transfer function, and alpha
premultiplication) in which the WebGPU numeric values are to be interpreted.
WebGPU allows all of the color spaces in the PredefinedColorSpace enum.
Note, each color space is defined over an extended range, as defined by the referenced CSS definitions,
to represent color values outside of its space (in both chrominance and luminance).
However, -srgb texture formats do have gamma-encoding/decoding properties which are
    algorithmically close to those used for gamma encoding in "srgb" and "display-p3" . For example, a fragment
    shader can output an "sRGB-linear"-encoded (physically linear) color value into an -srgb format texture, which will gamma-encode the value when it is written.
    Then, the value in the texture will be correctly encoded for use on a "srgb" -tagged (approximately perceptually-linear) canvas.
It is similarly possible to take advantage of these properties using copyExternalImageToTexture() ; see its description for additional information.
An out-of-gamut premultiplied RGBA value is one where any of the R/G/B channel values
exceeds the alpha channel value. For example, the premultiplied sRGB RGBA value [1.0, 0, 0, 0.5]
represents the (unpremultiplied) color [2, 0, 0] with 50% alpha, written rgb(srgb 2 0 0 / 50%) in CSS.
Just like any color value outside the sRGB color gamut, this is a well defined point in the extended color space
(except when alpha is 0, in which case there is no color).
However, when such values are output to a visible canvas, the result is undefined
(see GPUCanvasAlphaMode "premultiplied" ).
A color is converted between spaces by translating its representation in one space to a
representation in another according to the definitions above.
If the source value has fewer than 4 RGBA channels, the missing green/blue/alpha channels are set to 0, 0, 1 , respectively, before converting for color space/encoding and alpha premultiplication.
After conversion, if the destination needs fewer than 4 channels, the additional channels
are ignored.
Note: Grayscale images generally represent RGB values (V, V, V) , or RGBA values (V, V, V, A) in their color space.
Colors are not lossily clamped during conversion: converting from one color space to another
will result in values outside the range [0, 1] if the source color values were outside the range
of the destination color space’s gamut. For an sRGB destination, for example, this can occur if the
source is rgba16float, in a wider color space like Display-P3, or is premultiplied and contains out-of-gamut values .
Similarly, if the source value has a high bit depth (e.g. PNG with 16 bits per component) or
extended range (e.g. canvas with float16 storage), these colors are preserved through color space
conversion, with intermediate computations having at least the precision of the source.
If the source and destination of a color space/encoding conversion are the same, then conversion
is not necessary. In general, if any given step of the conversion is an identity function (no-op),
implementations should elide it, for performance.
For optimal performance, applications should set their color space and encoding
options so that the number of necessary conversions is minimized throughout the process.
For various image sources of GPUCopyExternalImageSourceInfo :
- ImageBitmap : Premultiplication is controlled via premultiplyAlpha . Color space is controlled via colorSpaceConversion .
ImageBitmap :
- Premultiplication is controlled via premultiplyAlpha .
Premultiplication is controlled via premultiplyAlpha .
- Color space is controlled via colorSpaceConversion .
Color space is controlled via colorSpaceConversion .
- 2d canvas: Always premultiplied . Color space is controlled via the colorSpace context creation attribute.
2d canvas:
- Always premultiplied .
Always premultiplied .
- Color space is controlled via the colorSpace context creation attribute.
Color space is controlled via the colorSpace context creation attribute.
- WebGL canvas: Premultiplication is controlled via the premultipliedAlpha option in WebGLContextAttributes . Color space is controlled via the WebGLRenderingContextBase ’s drawingBufferColorSpace state.
WebGL canvas:
- Premultiplication is controlled via the premultipliedAlpha option in WebGLContextAttributes .
Premultiplication is controlled via the premultipliedAlpha option in WebGLContextAttributes .
- Color space is controlled via the WebGLRenderingContextBase ’s drawingBufferColorSpace state.
Color space is controlled via the WebGLRenderingContextBase ’s drawingBufferColorSpace state.
Note: Check browser implementation support for these features before relying on them.

### 3.12. Numeric conversions from JavaScript to WGSL

Several parts of the WebGPU API ( pipeline-overridable constants and
render pass clear values) take numeric values from WebIDL ( double or float ) and convert
them to WGSL values ( bool , i32 , u32 , f32 , f16 ).
[LINK: pipeline-overridable](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable)
Note: This TypeError is generated in the device timeline and never surfaced to JavaScript.
- Assert idlValue is a finite value, since it is not unrestricted double or unrestricted float .
Assert idlValue is a finite value, since it is not unrestricted double or unrestricted float .
- Let v be the ECMAScript Number resulting from ! converting idlValue to an ECMAScript value .
Let v be the ECMAScript Number resulting from ! converting idlValue to an ECMAScript value .
- If T is bool Return the WGSL bool value corresponding to the result of ! converting v to an IDL value of type boolean . Note: This algorithm is called after the conversion from an ECMAScript value to an IDL double or float value. If the original ECMAScript value was a non-numeric,
non-boolean value like [] or {} , then the WGSL bool result may be different
than if the ECMAScript value had been converted to IDL boolean directly. If T is i32 Return the WGSL i32 value corresponding to the result of ? converting v to an IDL value of type [ EnforceRange ] long . If T is u32 Return the WGSL u32 value corresponding to the result of ? converting v to an IDL value of type [ EnforceRange ] unsigned long . If T is f32 Return the WGSL f32 value corresponding to the result of ? converting v to an IDL value of type float . If T is f16 Let wgslF32 be the WGSL f32 value corresponding to the result of ? converting v to an IDL value of type float . Return f16( wgslF32 ) , the result of ! converting the WGSL f32 value
to f16 as defined in WGSL floating point conversion . Note: As long as the value is in-range of f32 , no error is thrown, even if the
value is out-of-range of f16 .
Return the WGSL bool value corresponding to the result of ! converting v to an IDL value of type boolean .
Note: This algorithm is called after the conversion from an ECMAScript value to an IDL double or float value. If the original ECMAScript value was a non-numeric,
non-boolean value like [] or {} , then the WGSL bool result may be different
than if the ECMAScript value had been converted to IDL boolean directly.
Return the WGSL i32 value corresponding to the result of ? converting v to an IDL value of type [ EnforceRange ] long .
Return the WGSL u32 value corresponding to the result of ? converting v to an IDL value of type [ EnforceRange ] unsigned long .
Return the WGSL f32 value corresponding to the result of ? converting v to an IDL value of type float .
- Let wgslF32 be the WGSL f32 value corresponding to the result of ? converting v to an IDL value of type float .
Let wgslF32 be the WGSL f32 value corresponding to the result of ? converting v to an IDL value of type float .
- Return f16( wgslF32 ) , the result of ! converting the WGSL f32 value
to f16 as defined in WGSL floating point conversion .
Return f16( wgslF32 ) , the result of ! converting the WGSL f32 value
to f16 as defined in WGSL floating point conversion .
[LINK: WGSL floating point conversion](https://gpuweb.github.io/gpuweb/wgsl/#floating-point-conversion)
Note: As long as the value is in-range of f32 , no error is thrown, even if the
value is out-of-range of f16 .
Note: This TypeError is generated in the device timeline and never surfaced to JavaScript.
- If the components of format ( assert they all have the same type) are: floating-point types or normalized types Let T be f32 . signed integer types Let T be i32 . unsigned integer types Let T be u32 .
If the components of format ( assert they all have the same type) are:
Let T be f32 .
Let T be i32 .
Let T be u32 .
- Let wgslColor be a WGSL value of type vec4< T > , where the 4
components are the RGBA channels of color , each ? converted to WGSL type T .
Let wgslColor be a WGSL value of type vec4< T > , where the 4
components are the RGBA channels of color , each ? converted to WGSL type T .
- Convert wgslColor to format using the same conversion rules as the § 23.2.7 Output Merging step, and return the result. Note: For non-integer types, the exact choice of value is implementation-defined .
For normalized types, the value is clamped to the range of the type.
Convert wgslColor to format using the same conversion rules as the § 23.2.7 Output Merging step, and return the result.
Note: For non-integer types, the exact choice of value is implementation-defined .
For normalized types, the value is clamped to the range of the type.
Note: In other words, the value written will be as if it was written by a WGSL shader that
    outputs the value represented as a vec4 of f32 , i32 , or u32 .

## 4. Initialization

### 4.1. navigator.gpu

A GPU object is available in the Window and WorkerGlobalScope contexts through the Navigator and WorkerNavigator interfaces respectively and is exposed via navigator.gpu :
[LINK: Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window)
NavigatorGPU has the following attributes:
A global singleton providing top-level entry points like requestAdapter() .

### 4.2. GPU

GPU is the entry point to WebGPU.
GPU has the following methods:
Requests an adapter from the user agent.
The user agent chooses whether to return an adapter, and, if so,
chooses according to the provided options.
Arguments:
Returns: Promise < GPUAdapter ?>
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- Let promise be a new promise .
Let promise be a new promise .
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return promise .
Return promise .
- All of the requirements in the following steps must be met. options . featureLevel must be
a feature level string . If any are unmet: Let adapter be null , issue the resolution steps on contentTimeline , and return.
All of the requirements in the following steps must be met.
- options . featureLevel must be
a feature level string .
options . featureLevel must be
a feature level string .
If any are unmet:
- Let adapter be null , issue the resolution steps on contentTimeline , and return.
Let adapter be null , issue the resolution steps on contentTimeline , and return.
- If options . featureLevel is "compatibility" : Set options . featureLevel to "compatibility" if the user agent chooses
to support it, or "core" if not. Note: This doesn’t modify the JavaScript object passed by the application.
If options . featureLevel is "compatibility" :
- Set options . featureLevel to "compatibility" if the user agent chooses
to support it, or "core" if not. Note: This doesn’t modify the JavaScript object passed by the application.
Set options . featureLevel to "compatibility" if the user agent chooses
to support it, or "core" if not.
Note: This doesn’t modify the JavaScript object passed by the application.
- Set adapter to either: A new adapter object chosen according to
the rules in § 4.2.2 Adapter Selection and the criteria in options ,
adhering to § 4.2.1 Adapter Capability Guarantees , with the capabilities
determined in an implementation-defined way by the user agent. null , if the user agent is unable to return an adapter, or makes an implementation-defined choice not to return an adapter. If an adapter is returned, initialize its properties according to their
definitions. Set adapter . [[limits]] and adapter . [[features]] according to the supported capabilities of the adapter. If adapter meets the criteria of a fallback adapter set adapter . [[fallback]] to true . Otherwise, set it to false . Set adapter . [[xrCompatible]] to options . xrCompatible . Set adapter . [[default feature level]] to options . featureLevel .
Set adapter to either:
- A new adapter object chosen according to
the rules in § 4.2.2 Adapter Selection and the criteria in options ,
adhering to § 4.2.1 Adapter Capability Guarantees , with the capabilities
determined in an implementation-defined way by the user agent.
A new adapter object chosen according to
the rules in § 4.2.2 Adapter Selection and the criteria in options ,
adhering to § 4.2.1 Adapter Capability Guarantees , with the capabilities
determined in an implementation-defined way by the user agent.
- null , if the user agent is unable to return an adapter, or makes an implementation-defined choice not to return an adapter.
null , if the user agent is unable to return an adapter, or makes an implementation-defined choice not to return an adapter.
If an adapter is returned, initialize its properties according to their
definitions.
- Set adapter . [[limits]] and adapter . [[features]] according to the supported capabilities of the adapter.
Set adapter . [[limits]] and adapter . [[features]] according to the supported capabilities of the adapter.
- If adapter meets the criteria of a fallback adapter set adapter . [[fallback]] to true . Otherwise, set it to false .
If adapter meets the criteria of a fallback adapter set adapter . [[fallback]] to true . Otherwise, set it to false .
- Set adapter . [[xrCompatible]] to options . xrCompatible .
Set adapter . [[xrCompatible]] to options . xrCompatible .
- Set adapter . [[default feature level]] to options . featureLevel .
Set adapter . [[default feature level]] to options . featureLevel .
- Issue the resolution steps on contentTimeline .
Issue the resolution steps on contentTimeline .
- If adapter is not null : Resolve promise with a new GPUAdapter encapsulating adapter . Otherwise: Resolve promise with null .
If adapter is not null :
- Resolve promise with a new GPUAdapter encapsulating adapter .
Resolve promise with a new GPUAdapter encapsulating adapter .
Otherwise:
- Resolve promise with null .
Resolve promise with null .
Returns an optimal GPUTextureFormat for displaying 8-bit depth, standard dynamic range
content on this system. Must only return "rgba8unorm" or "bgra8unorm" .
The returned value can be passed as the format to configure() calls on a GPUCanvasContext to ensure the associated
canvas is able to display its contents efficiently.
Note: Canvases which are not displayed to the screen may or may not benefit from using this
format.
Returns: GPUTextureFormat
Content timeline steps:
- Return either "rgba8unorm" or "bgra8unorm" , depending on which format is optimal for
displaying WebGPU canvases on this system.
Return either "rgba8unorm" or "bgra8unorm" , depending on which format is optimal for
displaying WebGPU canvases on this system.
GPU has the following attributes:
The names of supported WGSL language extensions .
Supported language extensions are automatically enabled.
[LINK: language extensions](https://gpuweb.github.io/gpuweb/wgsl/#language-extension)
Adapters may expire at any time. Upon any change in the system’s state that could affect
the result of any requestAdapter() call, the user agent should expire all
previously-returned adapters . For example:
- A physical adapter is added/removed (via plug/unplug, driver update, hang recovery, etc.)
A physical adapter is added/removed (via plug/unplug, driver update, hang recovery, etc.)
- The system’s power configuration has changed (laptop unplugged, power settings changed, etc.)
The system’s power configuration has changed (laptop unplugged, power settings changed, etc.)
Note: User agents may choose to expire adapters often, even when there has been no system
state change (e.g. seconds or minutes after the adapter was created).
This can help obfuscate real system state changes, and make developers more aware that calling requestAdapter() again is always necessary before calling requestDevice() .
If an application does encounter this situation, standard device-loss recovery
handling should allow it to recover.
Any GPUAdapter returned by requestAdapter() must provide the following guarantees:
- At least one of the following must be true: "texture-compression-bc" is supported. Both "texture-compression-etc2" and "texture-compression-astc" are supported.
At least one of the following must be true:
- "texture-compression-bc" is supported.
"texture-compression-bc" is supported.
- Both "texture-compression-etc2" and "texture-compression-astc" are supported.
Both "texture-compression-etc2" and "texture-compression-astc" are supported.
- If "texture-compression-bc-sliced-3d" is supported, then "texture-compression-bc" must be supported.
If "texture-compression-bc-sliced-3d" is supported, then "texture-compression-bc" must be supported.
- If "texture-compression-astc-sliced-3d" is supported, then "texture-compression-astc" must be supported.
If "texture-compression-astc-sliced-3d" is supported, then "texture-compression-astc" must be supported.
- All supported limits must be either the default value or better .
All supported limits must be either the default value or better .
- All alignment-class limits must be powers of 2.
All alignment-class limits must be powers of 2.
- maxBindingsPerBindGroup must be must be ≥
( max bindings per shader stage × max shader stages per pipeline ), where: max bindings per shader stage is
( maxSampledTexturesPerShaderStage + maxSamplersPerShaderStage + maxStorageBuffersPerShaderStage + maxStorageTexturesPerShaderStage + maxUniformBuffersPerShaderStage ). max shader stages per pipeline is 2 , because a GPURenderPipeline supports both a vertex and fragment shader. Note: maxBindingsPerBindGroup does not reflect a fundamental limit;
implementations should raise it to conform to this requirement, rather than lowering the
other limits.
maxBindingsPerBindGroup must be must be ≥
( max bindings per shader stage × max shader stages per pipeline ), where:
- max bindings per shader stage is
( maxSampledTexturesPerShaderStage + maxSamplersPerShaderStage + maxStorageBuffersPerShaderStage + maxStorageTexturesPerShaderStage + maxUniformBuffersPerShaderStage ).
max bindings per shader stage is
( maxSampledTexturesPerShaderStage + maxSamplersPerShaderStage + maxStorageBuffersPerShaderStage + maxStorageTexturesPerShaderStage + maxUniformBuffersPerShaderStage ).
- max shader stages per pipeline is 2 , because a GPURenderPipeline supports both a vertex and fragment shader.
max shader stages per pipeline is 2 , because a GPURenderPipeline supports both a vertex and fragment shader.
Note: maxBindingsPerBindGroup does not reflect a fundamental limit;
implementations should raise it to conform to this requirement, rather than lowering the
other limits.
- maxBindGroups must be ≤ maxBindGroupsPlusVertexBuffers .
maxBindGroups must be ≤ maxBindGroupsPlusVertexBuffers .
- maxVertexBuffers must be ≤ maxBindGroupsPlusVertexBuffers .
maxVertexBuffers must be ≤ maxBindGroupsPlusVertexBuffers .
- minUniformBufferOffsetAlignment and minStorageBufferOffsetAlignment must both be ≥ 32 bytes. Note: 32 bytes would be the alignment of vec4<f64> . See WebGPU Shading Language § 14.4.1 Alignment and Size .
minUniformBufferOffsetAlignment and minStorageBufferOffsetAlignment must both be ≥ 32 bytes.
Note: 32 bytes would be the alignment of vec4<f64> . See WebGPU Shading Language § 14.4.1 Alignment and Size .
[LINK: WebGPU Shading Language § 14.4.1 Alignment and Size](https://gpuweb.github.io/gpuweb/wgsl/#alignment-and-size)
- maxUniformBufferBindingSize must be ≤ maxBufferSize .
maxUniformBufferBindingSize must be ≤ maxBufferSize .
- maxStorageBufferBindingSize must be ≤ maxBufferSize .
maxStorageBufferBindingSize must be ≤ maxBufferSize .
- maxStorageBufferBindingSize must be a multiple of 4 bytes.
maxStorageBufferBindingSize must be a multiple of 4 bytes.
- maxVertexBufferArrayStride must be a multiple of 4 bytes.
maxVertexBufferArrayStride must be a multiple of 4 bytes.
- maxComputeWorkgroupSizeX must be ≤ maxComputeInvocationsPerWorkgroup .
maxComputeWorkgroupSizeX must be ≤ maxComputeInvocationsPerWorkgroup .
- maxComputeWorkgroupSizeY must be ≤ maxComputeInvocationsPerWorkgroup .
maxComputeWorkgroupSizeY must be ≤ maxComputeInvocationsPerWorkgroup .
- maxComputeWorkgroupSizeZ must be ≤ maxComputeInvocationsPerWorkgroup .
maxComputeWorkgroupSizeZ must be ≤ maxComputeInvocationsPerWorkgroup .
- maxComputeInvocationsPerWorkgroup must be ≤ maxComputeWorkgroupSizeX × maxComputeWorkgroupSizeY × maxComputeWorkgroupSizeZ .
maxComputeInvocationsPerWorkgroup must be ≤ maxComputeWorkgroupSizeX × maxComputeWorkgroupSizeY × maxComputeWorkgroupSizeZ .
GPURequestAdapterOptions provides hints to the user agent indicating what
configuration is suitable for the application.
GPURequestAdapterOptions has the following members:
Requests an adapter that supports at least a particular set of capabilities .
This influences the [[default feature level]] of devices created
from this adapter. The capabilities for each level are defined below, and the exact
steps are defined in requestAdapter() and " a new device ".
If the implementation or system does not support all of the capabilities in the
requested feature level, requestAdapter() will return null .
Note: Applications should typically make a single requestAdapter() call with the lowest
feature level they support, then inspect the adapter for additional capabilities they can
use optionally, and request those in requestDevice() .
The allowed feature level string values are:
The following set of capabilities:
- The Default limits.
The Default limits.
- "core-features-and-limits" .
"core-features-and-limits" .
Note: Adapters with this [[default feature level]] may
conventionally be referred to as "Core-defaulting".
The following set of capabilities:
- The Compatibility Mode Default limits.
The Compatibility Mode Default limits.
- No features. (It excludes the "core-features-and-limits" feature.)
No features. (It excludes the "core-features-and-limits" feature.)
If the implementation cannot enforce the stricter "Compatibility Mode"
validation rules, requestAdapter() will ignore this request and
treat it as a request for "core" .
Note: Adapters with this [[default feature level]] may
conventionally be referred to as "Compatibility-defaulting".
Optionally provides a hint indicating what class of adapter should be selected from
the system’s available adapters.
The value of this hint may influence which adapter is chosen, but it must not
influence whether an adapter is returned or not.
Note: The primary utility of this hint is to influence which GPU is used in a multi-GPU system.
For instance, some laptops have a low-power integrated GPU and a high-performance
discrete GPU. This hint may also affect the power configuration of the selected GPU to
match the requested power preference.
Note: Depending on the exact hardware configuration, such as battery status and attached displays
or removable GPUs, the user agent may select different adapters given the same power
preference.
Typically, given the same hardware configuration and state and powerPreference , the user agent is likely to select the same adapter.
It must be one of the following values:
Provides no hint to the user agent.
Indicates a request to prioritize power savings over performance.
Note: Generally, content should use this if it is unlikely to be constrained by drawing
performance; for example, if it renders only one frame per second, draws only relatively
simple geometry with simple shaders, or uses a small HTML canvas element.
Developers are encouraged to use this value if their content allows, since it may
significantly improve battery life on portable devices.
Indicates a request to prioritize performance over power consumption.
Note: By choosing this value, developers should be aware that, for devices created on the
resulting adapter, user agents are more likely to force device loss, in order to save
power by switching to a lower-power adapter.
Developers are encouraged to only specify this value if they believe it is absolutely
necessary, since it may significantly decrease battery life on portable devices.
When set to true indicates that only a fallback adapter may be returned. If the user
agent does not support a fallback adapter , will cause requestAdapter() to
resolve to null .
Note: requestAdapter() may still return a fallback adapter if forceFallbackAdapter is set to false and either no
other appropriate adapter is available or the user agent chooses to return a fallback adapter . Developers that wish to prevent their applications from running on fallback adapters should check the info . isFallbackAdapter attribute prior
to requesting a GPUDevice .
When set to true indicates that the best adapter for rendering to a WebXR session must be returned. If the user agent or system does not support WebXR sessions then
adapter selection may ignore this value.
Note: If xrCompatible is not set to true when the adapter is
requested, GPUDevice s created from the adapter cannot be used to render for WebXR sessions .

### 4.3. GPUAdapter

A GPUAdapter encapsulates an adapter ,
and describes its capabilities ( features and limits ).
To get a GPUAdapter , use requestAdapter() .
GPUAdapter has the following immutable properties
The set of values in this . [[adapter]] . [[features]] .
The limits in this . [[adapter]] . [[limits]] .
Information about the physical adapter underlying this GPUAdapter .
For a given GPUAdapter , the GPUAdapterInfo values exposed are constant over time.
The same object is returned each time. To create that object for the first time:
Returns: GPUAdapterInfo
Content timeline steps:
- Return a new adapter info for this . [[adapter]] .
Return a new adapter info for this . [[adapter]] .
The adapter to which this GPUAdapter refers.
GPUAdapter has the following methods:
Requests a device from the adapter .
This is a one-time action: if a device is returned successfully,
the adapter becomes "consumed" .
Arguments:
Returns: Promise < GPUDevice >
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- Let promise be a new promise .
Let promise be a new promise .
- Let adapter be this . [[adapter]] .
Let adapter be this . [[adapter]] .
- Issue the initialization steps to the Device timeline of this .
Issue the initialization steps to the Device timeline of this .
- Return promise .
Return promise .
- If any of the following requirements are unmet: The set of values in descriptor . requiredFeatures must be a subset of those in adapter . [[features]] . Then issue the following steps on contentTimeline and return: Content timeline steps: Reject promise with a TypeError . Note: This is the same error that is produced if a feature name isn’t known
by the browser at all (in its GPUFeatureName definition).
This converges the behavior when the browser doesn’t support a feature
with the behavior when a particular adapter doesn’t support a feature.
If any of the following requirements are unmet:
- The set of values in descriptor . requiredFeatures must be a subset of those in adapter . [[features]] .
The set of values in descriptor . requiredFeatures must be a subset of those in adapter . [[features]] .
Then issue the following steps on contentTimeline and return:
- Reject promise with a TypeError .
Reject promise with a TypeError .
Note: This is the same error that is produced if a feature name isn’t known
by the browser at all (in its GPUFeatureName definition).
This converges the behavior when the browser doesn’t support a feature
with the behavior when a particular adapter doesn’t support a feature.
- All of the requirements in the following steps must be met. adapter . [[state]] must not be "consumed" . For each [ key , value ] in descriptor . requiredLimits for which value is not undefined : key must be the name of a member of supported limits . value must be no better than adapter . [[limits]] [ key ]. If key ’s class is alignment , value must be a power of 2 less than 2 32 . Note: User agents should consider issuing developer-visible warnings when key is not recognized, even when value is undefined . If any are unmet, issue the following steps on contentTimeline and return: Content timeline steps: Reject promise with an OperationError .
All of the requirements in the following steps must be met.
- adapter . [[state]] must not be "consumed" .
adapter . [[state]] must not be "consumed" .
- For each [ key , value ] in descriptor . requiredLimits for which value is not undefined : key must be the name of a member of supported limits . value must be no better than adapter . [[limits]] [ key ]. If key ’s class is alignment , value must be a power of 2 less than 2 32 . Note: User agents should consider issuing developer-visible warnings when key is not recognized, even when value is undefined .
For each [ key , value ] in descriptor . requiredLimits for which value is not undefined :
- key must be the name of a member of supported limits .
key must be the name of a member of supported limits .
- value must be no better than adapter . [[limits]] [ key ].
value must be no better than adapter . [[limits]] [ key ].
- If key ’s class is alignment , value must be a power of 2 less than 2 32 .
If key ’s class is alignment , value must be a power of 2 less than 2 32 .
Note: User agents should consider issuing developer-visible warnings when key is not recognized, even when value is undefined .
If any are unmet, issue the following steps on contentTimeline and return:
- Reject promise with an OperationError .
Reject promise with an OperationError .
- If adapter . [[state]] is "expired" or the user agent otherwise cannot fulfill the request: Let device be a new device . Lose the device ( device , "unknown" ). Assert adapter . [[state]] is "expired" . Note: User agents should consider issuing developer-visible warnings in
most or all cases when this occurs. Applications should perform
reinitialization logic starting with requestAdapter() . Otherwise: Let device be the result of creating a new device from adapter with descriptor . Expire adapter .
If adapter . [[state]] is "expired" or the user agent otherwise cannot fulfill the request:
- Let device be a new device .
Let device be a new device .
- Lose the device ( device , "unknown" ).
Lose the device ( device , "unknown" ).
- Assert adapter . [[state]] is "expired" . Note: User agents should consider issuing developer-visible warnings in
most or all cases when this occurs. Applications should perform
reinitialization logic starting with requestAdapter() .
Assert adapter . [[state]] is "expired" .
Note: User agents should consider issuing developer-visible warnings in
most or all cases when this occurs. Applications should perform
reinitialization logic starting with requestAdapter() .
Otherwise:
- Let device be the result of creating a new device from adapter with descriptor .
Let device be the result of creating a new device from adapter with descriptor .
- Expire adapter .
Expire adapter .
- Issue the subsequent steps on contentTimeline .
Issue the subsequent steps on contentTimeline .
- Let gpuDevice be a new GPUDevice instance.
Let gpuDevice be a new GPUDevice instance.
- Set gpuDevice . [[device]] to device .
Set gpuDevice . [[device]] to device .
- Set device . [[content device]] to gpuDevice .
Set device . [[content device]] to gpuDevice .
- Set gpuDevice . label to descriptor . label .
Set gpuDevice . label to descriptor . label .
- Resolve promise with gpuDevice . Note: If the device is already lost because the adapter could not fulfill the request, device . lost has already resolved before promise resolves.
Resolve promise with gpuDevice .
Note: If the device is already lost because the adapter could not fulfill the request, device . lost has already resolved before promise resolves.
GPUDeviceDescriptor describes a device request.
GPUDeviceDescriptor has the following members:
Specifies the features that are required by the device request.
The request will fail if the adapter cannot provide these features.
Exactly the specified set of features, and no more or less, will be allowed in validation
of API calls on the resulting device.
Specifies the limits that are required by the device request.
The request will fail if the adapter cannot provide these limits.
Each key with a non- undefined value must be the name of a member of supported limits .
API calls on the resulting device perform validation according to the exact limits of the
device (not the adapter; see § 3.6.2 Limits ).
The descriptor for the default GPUQueue .
Each GPUFeatureName identifies a set of functionality which, if available,
allows additional usages of WebGPU that would have otherwise been invalid.

### 4.4. GPUDevice

A GPUDevice encapsulates a device and exposes
the functionality of that device.
GPUDevice is the top-level interface through which WebGPU interfaces are created.
To get a GPUDevice , use requestDevice() .
GPUDevice has the following immutable properties :
A set containing the GPUFeatureName values of the features
supported by the device ( [[device]] . [[features]] ).
The limits supported by the device ( [[device]] . [[limits]] ).
The primary GPUQueue for this device.
Information about the physical adapter which created the device that this GPUDevice refers to.
For a given GPUDevice , the GPUAdapterInfo values exposed are constant over time.
The same object is returned each time. To create that object for the first time:
Returns: GPUAdapterInfo
Content timeline steps:
- Return a new adapter info for this . [[device]] . [[adapter]] .
Return a new adapter info for this . [[device]] . [[adapter]] .
The [[device]] for a GPUDevice is the device that the GPUDevice refers
to.
GPUDevice has the following methods:
Destroys the device , preventing further operations on it.
Outstanding asynchronous operations will fail.
Note: It is valid to destroy a device multiple times.
Content timeline steps:
- unmap() all GPUBuffer s from this device.
unmap() all GPUBuffer s from this device.
- Issue the subsequent steps on the Device timeline of this .
Issue the subsequent steps on the Device timeline of this .
- Lose the device ( this . [[device]] , "destroyed" ).
Lose the device ( this . [[device]] , "destroyed" ).
Note: Since no further operations can be enqueued on this device, implementations can abort
outstanding asynchronous operations immediately and free resource allocations, including
mapped memory that was just unmapped.
- Always allowed: MAP_READ , MAP_WRITE , COPY_SRC , COPY_DST , INDEX , VERTEX , UNIFORM , STORAGE , INDIRECT , QUERY_RESOLVE
Always allowed: MAP_READ , MAP_WRITE , COPY_SRC , COPY_DST , INDEX , VERTEX , UNIFORM , STORAGE , INDIRECT , QUERY_RESOLVE
- Always allowed: COPY_SRC , COPY_DST , TEXTURE_BINDING , STORAGE_BINDING , RENDER_ATTACHMENT , TRANSIENT_ATTACHMENT
Always allowed: COPY_SRC , COPY_DST , TEXTURE_BINDING , STORAGE_BINDING , RENDER_ATTACHMENT , TRANSIENT_ATTACHMENT

### 4.5. Example

## 5. Buffers

### 5.1. GPUBuffer

A GPUBuffer represents a block of memory that can be used in GPU operations.
Data is stored in linear layout, meaning that each byte of the allocation can be
addressed by its offset from the start of the GPUBuffer , subject to alignment
restrictions depending on the operation. Some GPUBuffers can be
mapped which makes the block of memory accessible via an ArrayBuffer called
its mapping.
GPUBuffer s are created via createBuffer() .
Buffers may be mappedAtCreation .
GPUBuffer has the following immutable properties :
The length of the GPUBuffer allocation in bytes.
The allowed usages for this GPUBuffer .
GPUBuffer has the following content timeline properties :
The current GPUBufferMapState of the buffer:
The buffer is not mapped for use by this . getMappedRange() .
A mapping of the buffer has been requested, but is pending.
It may succeed, or fail validation in mapAsync() .
The buffer is mapped and this . getMappedRange() may be used.
The getter steps are:
- If this . [[mapping]] is not null ,
return "mapped" .
If this . [[mapping]] is not null ,
return "mapped" .
- If this . [[pending_map]] is not null ,
return "pending" .
If this . [[pending_map]] is not null ,
return "pending" .
- Return "unmapped" .
Return "unmapped" .
The Promise returned by the currently-pending mapAsync() call.
There is never more than one pending map, because mapAsync() will refuse immediately if a request is already in flight.
Set if and only if the buffer is currently mapped for use by getMappedRange() .
Null otherwise (even if there is a [[pending_map]] ).
An active buffer mapping is a structure with the following fields:
The mapping for this GPUBuffer . This data is accessed through ArrayBuffer s
which are views onto this data, returned by getMappedRange() and
stored in views .
The GPUMapModeFlags of the map, as specified in the corresponding call to mapAsync() or createBuffer() .
The range of this GPUBuffer that is mapped.
The ArrayBuffer s returned via getMappedRange() to the application.
They are tracked so they can be detached when unmap() is called.
- Let size be range [1] - range [0].
Let size be range [1] - range [0].
- Let data be ? CreateByteDataBlock ( size ). NOTE: This may result in a RangeError being thrown.
    For consistency and predictability: For any size at which new ArrayBuffer() would succeed at a given moment,
this allocation should succeed at that moment. For any size at which new ArrayBuffer() deterministically throws a RangeError , this allocation should as well.
Let data be ? CreateByteDataBlock ( size ).
- For any size at which new ArrayBuffer() would succeed at a given moment,
this allocation should succeed at that moment.
For any size at which new ArrayBuffer() would succeed at a given moment,
this allocation should succeed at that moment.
- For any size at which new ArrayBuffer() deterministically throws a RangeError , this allocation should as well.
For any size at which new ArrayBuffer() deterministically throws a RangeError , this allocation should as well.
- Return an active buffer mapping with: data set to data . mode set to mode . range set to range . views set to [] .
Return an active buffer mapping with:
- data set to data .
data set to data .
- mode set to mode .
mode set to mode .
- range set to range .
range set to range .
- views set to [] .
views set to [] .
GPUBuffer has the following device timeline properties :
The current internal state of the buffer:
The buffer can be used in queue operations (unless it is invalid ).
The buffer cannot be used in queue operations due to being mapped.
The buffer cannot be used in any operations due to being destroy() ed.
GPUBufferDescriptor has the following members:
The size of the buffer in bytes.
The allowed usages for the buffer.
If true creates the buffer in an already mapped state, allowing getMappedRange() to be called immediately. It is valid to set mappedAtCreation to true even if usage does not contain MAP_READ or MAP_WRITE . This can be
used to set the buffer’s initial data.
Guarantees that even if the buffer creation eventually fails, it will still appear as if the
mapped range can be written/read to until it is unmapped.
The GPUBufferUsage flags determine how a GPUBuffer may be used after its creation:
The buffer can be mapped for reading. (Example: calling mapAsync() with GPUMapMode.READ )
May only be combined with COPY_DST .
The buffer can be mapped for writing. (Example: calling mapAsync() with GPUMapMode.WRITE )
May only be combined with COPY_SRC .
The buffer can be used as the source of a copy operation. (Examples: as the source argument of a copyBufferToBuffer() or copyBufferToTexture() call.)
The buffer can be used as the destination of a copy or write operation. (Examples: as the destination argument of a copyBufferToBuffer() or copyTextureToBuffer() call, or as the target of a writeBuffer() call.)
The buffer can be used as an index buffer. (Example: passed to setIndexBuffer() .)
The buffer can be used as a vertex buffer. (Example: passed to setVertexBuffer() .)
The buffer can be used as a uniform buffer. (Example: as a bind group entry for a GPUBufferBindingLayout with a buffer . type of "uniform" .)
The buffer can be used as a storage buffer. (Example: as a bind group entry for a GPUBufferBindingLayout with a buffer . type of "storage" or "read-only-storage" .)
The buffer can be used as to store indirect command arguments. (Examples: as the indirectBuffer argument of a drawIndirect() or dispatchWorkgroupsIndirect() call.)
The buffer can be used to capture query results. (Example: as the destination argument of
a resolveQuerySet() call.)
Creates a GPUBuffer .
Arguments:
Returns: GPUBuffer
Content timeline steps:
- Let b be ! create a new WebGPU object ( this , GPUBuffer , descriptor ).
Let b be ! create a new WebGPU object ( this , GPUBuffer , descriptor ).
- Set b . size to descriptor . size .
Set b . size to descriptor . size .
- Set b . usage to descriptor . usage .
Set b . usage to descriptor . usage .
- If descriptor . mappedAtCreation is true : If descriptor . size is not a multiple of 4,
throw a RangeError . Set b . [[mapping]] to ? initialize an active buffer mapping with mode WRITE and range [0, descriptor . size ] .
If descriptor . mappedAtCreation is true :
- If descriptor . size is not a multiple of 4,
throw a RangeError .
If descriptor . size is not a multiple of 4,
throw a RangeError .
- Set b . [[mapping]] to ? initialize an active buffer mapping with mode WRITE and range [0, descriptor . size ] .
Set b . [[mapping]] to ? initialize an active buffer mapping with mode WRITE and range [0, descriptor . size ] .
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return b .
Return b .
- If any of the following requirements are unmet, generate a validation error , invalidate b and return. this must not be lost . descriptor . usage must not be 0. descriptor . usage must be a subset of the allowed buffer usages for this . If descriptor . usage contains MAP_READ : descriptor . usage must contain no other flags
except COPY_DST . If descriptor . usage contains MAP_WRITE : descriptor . usage must contain no other flags
except COPY_SRC . If descriptor . size must be ≤ this . [[device]] . [[limits]] . maxBufferSize .
If any of the following requirements are unmet, generate a validation error , invalidate b and return.
- this must not be lost .
this must not be lost .
- descriptor . usage must not be 0.
descriptor . usage must not be 0.
- descriptor . usage must be a subset of the allowed buffer usages for this .
descriptor . usage must be a subset of the allowed buffer usages for this .
- If descriptor . usage contains MAP_READ : descriptor . usage must contain no other flags
except COPY_DST .
If descriptor . usage contains MAP_READ :
- descriptor . usage must contain no other flags
except COPY_DST .
descriptor . usage must contain no other flags
except COPY_DST .
- If descriptor . usage contains MAP_WRITE : descriptor . usage must contain no other flags
except COPY_SRC .
If descriptor . usage contains MAP_WRITE :
- descriptor . usage must contain no other flags
except COPY_SRC .
descriptor . usage must contain no other flags
except COPY_SRC .
- If descriptor . size must be ≤ this . [[device]] . [[limits]] . maxBufferSize .
If descriptor . size must be ≤ this . [[device]] . [[limits]] . maxBufferSize .
Note: If buffer creation fails, and descriptor . mappedAtCreation is false ,
        any calls to mapAsync() will reject, so any resources allocated to enable mapping can
        and may be discarded or recycled.
- If descriptor . mappedAtCreation is true : Set b . [[internal state]] to " unavailable ". Otherwise: Set b . [[internal state]] to " available ".
If descriptor . mappedAtCreation is true :
- Set b . [[internal state]] to " unavailable ".
Set b . [[internal state]] to " unavailable ".
Otherwise:
- Set b . [[internal state]] to " available ".
Set b . [[internal state]] to " available ".
- Create a device allocation for b where each byte is zero. If the allocation fails without side-effects, generate an out-of-memory error , invalidate b , and return.
Create a device allocation for b where each byte is zero.
If the allocation fails without side-effects, generate an out-of-memory error , invalidate b , and return.
An application that no longer requires a GPUBuffer can choose to lose
access to it before garbage collection by calling destroy() . Destroying a buffer also
unmaps it, freeing any memory allocated for the mapping.
Note: This allows the user agent to reclaim the GPU memory associated with the GPUBuffer once all previously submitted operations using it are complete.
GPUBuffer has the following methods:
Destroys the GPUBuffer .
Note: It is valid to destroy a buffer multiple times.
Returns: undefined
Content timeline steps:
- Call this . unmap() .
Call this . unmap() .
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Set this . [[internal state]] to
" destroyed ".
Set this . [[internal state]] to
" destroyed ".
Note: Since no further operations can be enqueued using this buffer, implementations can
free resource allocations, including mapped memory that was just unmapped.

### 5.2. Buffer Mapping

An application can request to map a GPUBuffer so that they can access its
content via ArrayBuffer s that represent part of the GPUBuffer ’s
allocations. Mapping a GPUBuffer is requested asynchronously with mapAsync() so that the user agent can ensure the GPU
finished using the GPUBuffer before the application can access its content.
A mapped GPUBuffer cannot be used by the GPU and must be unmapped using unmap() before
work using it can be submitted to the Queue timeline .
Once the GPUBuffer is mapped, the application can synchronously ask for access
to ranges of its content with getMappedRange() .
The returned ArrayBuffer can only be detached by unmap() (directly, or via GPUBuffer . destroy() or GPUDevice . destroy() ),
and cannot be transferred .
A TypeError is thrown by any other operation that attempts to do so.
The GPUMapMode flags determine how a GPUBuffer is mapped when calling mapAsync() :
Only valid with buffers created with the MAP_READ usage.
Once the buffer is mapped, calls to getMappedRange() will return an ArrayBuffer containing the buffer’s current values. Changes to the returned ArrayBuffer will be discarded after unmap() is called.
Only valid with buffers created with the MAP_WRITE usage.
Once the buffer is mapped, calls to getMappedRange() will return an ArrayBuffer containing the buffer’s current values. Changes to the returned ArrayBuffer will be stored in the GPUBuffer after unmap() is called.
Note: Since the MAP_WRITE buffer usage may only be combined with the COPY_SRC buffer usage, mapping for writing can never return values
produced by the GPU, and the returned ArrayBuffer will only ever contain the default
initialized data (zeros) or data written by the webpage during a previous mapping.
GPUBuffer has the following methods:
Maps the given range of the GPUBuffer and resolves the returned Promise when the GPUBuffer ’s content is ready to be accessed with getMappedRange() .
The resolution of the returned Promise only indicates that the buffer has been mapped.
It does not guarantee the completion of any other operations visible to the content timeline ,
and in particular does not imply that any other Promise returned from onSubmittedWorkDone() or mapAsync() on other GPUBuffer s
have resolved.
The resolution of the Promise returned from onSubmittedWorkDone() does imply the completion of mapAsync() calls made prior to that call,
on GPUBuffer s last used exclusively on that queue.
Arguments:
Returns: Promise < undefined >
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- If this . mapState is not "unmapped" : Issue the early-reject steps on the Device timeline of this . [[device]] . Return a promise rejected with OperationError .
If this . mapState is not "unmapped" :
- Issue the early-reject steps on the Device timeline of this . [[device]] .
Issue the early-reject steps on the Device timeline of this . [[device]] .
- Return a promise rejected with OperationError .
Return a promise rejected with OperationError .
- Let p be a new Promise .
Let p be a new Promise .
- Set this . [[pending_map]] to p .
Set this . [[pending_map]] to p .
- Issue the validation steps on the Device timeline of this . [[device]] .
Issue the validation steps on the Device timeline of this . [[device]] .
- Return p .
Return p .
- Generate a validation error .
Generate a validation error .
- Return.
Return.
- If size is undefined : Let rangeSize be max(0, this . size - offset ). Otherwise: Let rangeSize be size .
If size is undefined :
- Let rangeSize be max(0, this . size - offset ).
Let rangeSize be max(0, this . size - offset ).
Otherwise:
- Let rangeSize be size .
Let rangeSize be size .
- If any of the following conditions are unsatisfied: this must be valid . Set deviceLost to true . Issue the map failure steps on contentTimeline . Return.
If any of the following conditions are unsatisfied:
- this must be valid .
this must be valid .
- Set deviceLost to true .
Set deviceLost to true .
- Issue the map failure steps on contentTimeline .
Issue the map failure steps on contentTimeline .
- Return.
Return.
- If any of the following conditions are unsatisfied: this . [[internal state]] is " available ". offset is a multiple of 8. rangeSize is a multiple of 4. offset + rangeSize ≤ this . size mode contains only bits defined in GPUMapMode . mode contains exactly one of READ or WRITE . If mode contains READ then this . usage must contain MAP_READ . If mode contains WRITE then this . usage must contain MAP_WRITE . Then: Set deviceLost to false . Issue the map failure steps on contentTimeline . Generate a validation error . Return.
If any of the following conditions are unsatisfied:
- this . [[internal state]] is " available ".
this . [[internal state]] is " available ".
- offset is a multiple of 8.
offset is a multiple of 8.
- rangeSize is a multiple of 4.
rangeSize is a multiple of 4.
- offset + rangeSize ≤ this . size
offset + rangeSize ≤ this . size
- mode contains only bits defined in GPUMapMode .
mode contains only bits defined in GPUMapMode .
- mode contains exactly one of READ or WRITE .
mode contains exactly one of READ or WRITE .
- If mode contains READ then this . usage must contain MAP_READ .
If mode contains READ then this . usage must contain MAP_READ .
- If mode contains WRITE then this . usage must contain MAP_WRITE .
If mode contains WRITE then this . usage must contain MAP_WRITE .
Then:
- Set deviceLost to false .
Set deviceLost to false .
- Issue the map failure steps on contentTimeline .
Issue the map failure steps on contentTimeline .
- Generate a validation error .
Generate a validation error .
- Return.
Return.
- Set this . [[internal state]] to " unavailable ". Note: Since the buffer is mapped, its contents cannot change between this step and unmap() .
Set this . [[internal state]] to " unavailable ".
Note: Since the buffer is mapped, its contents cannot change between this step and unmap() .
- When either of the following events occur (whichever comes first),
or if either has already occurred: The device timeline becomes informed of the completion of an unspecified queue timeline point: after the completion of currently-enqueued operations that use this and no later than the completion of all currently-enqueued operations (regardless of whether they use this ). this . [[device]] becomes lost . Then issue the subsequent steps on the device timeline of this . [[device]] .
When either of the following events occur (whichever comes first),
or if either has already occurred:
- The device timeline becomes informed of the completion of an unspecified queue timeline point: after the completion of currently-enqueued operations that use this and no later than the completion of all currently-enqueued operations (regardless of whether they use this ).
The device timeline becomes informed of the completion of an unspecified queue timeline point:
- after the completion of currently-enqueued operations that use this
after the completion of currently-enqueued operations that use this
- and no later than the completion of all currently-enqueued operations (regardless of whether they use this ).
and no later than the completion of all currently-enqueued operations (regardless of whether they use this ).
- this . [[device]] becomes lost .
this . [[device]] becomes lost .
Then issue the subsequent steps on the device timeline of this . [[device]] .
- Set deviceLost to true if this . [[device]] is lost ,
and false otherwise. Note: The device could have been lost between the previous block of steps and this one.
Set deviceLost to true if this . [[device]] is lost ,
and false otherwise.
Note: The device could have been lost between the previous block of steps and this one.
- If deviceLost : Issue the map failure steps on contentTimeline . Otherwise: Let internalStateAtCompletion be this . [[internal state]] . Note: If, and only if, at this point the buffer has become " available "
again due to an unmap() call, then [[pending_map]] != p below,
so mapping will not succeed in the steps below. Let dataForMappedRegion be the contents of this starting at offset offset , for rangeSize bytes. Issue the map success steps on the contentTimeline .
If deviceLost :
- Issue the map failure steps on contentTimeline .
Issue the map failure steps on contentTimeline .
Otherwise:
- Let internalStateAtCompletion be this . [[internal state]] . Note: If, and only if, at this point the buffer has become " available "
again due to an unmap() call, then [[pending_map]] != p below,
so mapping will not succeed in the steps below.
Let internalStateAtCompletion be this . [[internal state]] .
Note: If, and only if, at this point the buffer has become " available "
again due to an unmap() call, then [[pending_map]] != p below,
so mapping will not succeed in the steps below.
- Let dataForMappedRegion be the contents of this starting at offset offset , for rangeSize bytes.
Let dataForMappedRegion be the contents of this starting at offset offset , for rangeSize bytes.
- Issue the map success steps on the contentTimeline .
Issue the map success steps on the contentTimeline .
- If this . [[pending_map]] != p : Note: The map has been cancelled by unmap() . Assert p is rejected. Return.
If this . [[pending_map]] != p :
Note: The map has been cancelled by unmap() .
- Assert p is rejected.
Assert p is rejected.
- Return.
Return.
- Assert p is pending.
Assert p is pending.
- Assert internalStateAtCompletion is " unavailable ".
Assert internalStateAtCompletion is " unavailable ".
- Let mapping be initialize an active buffer mapping with mode mode and range [ offset , offset + rangeSize ] . If this allocation fails: Set this . [[pending_map]] to null ,
and reject p with a RangeError . Return.
Let mapping be initialize an active buffer mapping with mode mode and range [ offset , offset + rangeSize ] .
If this allocation fails:
- Set this . [[pending_map]] to null ,
and reject p with a RangeError .
Set this . [[pending_map]] to null ,
and reject p with a RangeError .
- Return.
Return.
- Set the content of mapping . data to dataForMappedRegion .
Set the content of mapping . data to dataForMappedRegion .
- Set this . [[mapping]] to mapping .
Set this . [[mapping]] to mapping .
- Set this . [[pending_map]] to null ,
and resolve p .
Set this . [[pending_map]] to null ,
and resolve p .
- If this . [[pending_map]] != p : Note: The map has been cancelled by unmap() . Assert p is already rejected. Return.
If this . [[pending_map]] != p :
Note: The map has been cancelled by unmap() .
- Assert p is already rejected.
Assert p is already rejected.
- Return.
Return.
- Assert p is still pending.
Assert p is still pending.
- Set this . [[pending_map]] to null .
Set this . [[pending_map]] to null .
- If deviceLost : Reject p with an AbortError . Note: This is the same error type produced by cancelling the map using unmap() . Otherwise: Reject p with an OperationError .
If deviceLost :
- Reject p with an AbortError . Note: This is the same error type produced by cancelling the map using unmap() .
Reject p with an AbortError .
Note: This is the same error type produced by cancelling the map using unmap() .
Otherwise:
- Reject p with an OperationError .
Reject p with an OperationError .
Returns an ArrayBuffer with the contents of the GPUBuffer in the given mapped range.
Arguments:
Returns: ArrayBuffer
Content timeline steps:
- If size is missing: Let rangeSize be max(0, this . size - offset ). Otherwise, let rangeSize be size .
If size is missing:
- Let rangeSize be max(0, this . size - offset ).
Let rangeSize be max(0, this . size - offset ).
Otherwise, let rangeSize be size .
- If any of the following conditions are unsatisfied, throw an OperationError and return. this . [[mapping]] is not null . offset is a multiple of 8. rangeSize is a multiple of 4. offset ≥ this . [[mapping]] . range [0]. offset + rangeSize ≤ this . [[mapping]] . range [1]. [ offset , offset + rangeSize ) does not overlap another range in this . [[mapping]] . views . Note: It is always valid to get mapped ranges of a GPUBuffer that is mappedAtCreation , even if it is invalid , because
    the Content timeline might not know it is invalid.
If any of the following conditions are unsatisfied, throw an OperationError and return.
- this . [[mapping]] is not null .
this . [[mapping]] is not null .
- offset is a multiple of 8.
offset is a multiple of 8.
- rangeSize is a multiple of 4.
rangeSize is a multiple of 4.
- offset ≥ this . [[mapping]] . range [0].
offset ≥ this . [[mapping]] . range [0].
- offset + rangeSize ≤ this . [[mapping]] . range [1].
offset + rangeSize ≤ this . [[mapping]] . range [1].
- [ offset , offset + rangeSize ) does not overlap another range in this . [[mapping]] . views .
[ offset , offset + rangeSize ) does not overlap another range in this . [[mapping]] . views .
Note: It is always valid to get mapped ranges of a GPUBuffer that is mappedAtCreation , even if it is invalid , because
    the Content timeline might not know it is invalid.
- Let data be this . [[mapping]] . data .
Let data be this . [[mapping]] . data .
- Let view be ! create an ArrayBuffer of size rangeSize ,
but with its pointer mutably referencing the content of data at offset
( offset - [[mapping]] . range [0]). Note: A RangeError cannot be thrown here, because the data has already
been allocated during mapAsync() or createBuffer() .
Let view be ! create an ArrayBuffer of size rangeSize ,
but with its pointer mutably referencing the content of data at offset
( offset - [[mapping]] . range [0]).
Note: A RangeError cannot be thrown here, because the data has already
been allocated during mapAsync() or createBuffer() .
- Set view . [[ArrayBufferDetachKey]] to "WebGPUBufferMapping". Note: This causes a TypeError to be thrown if an attempt is made to DetachArrayBuffer , except by unmap() .
Set view . [[ArrayBufferDetachKey]] to "WebGPUBufferMapping".
Note: This causes a TypeError to be thrown if an attempt is made to DetachArrayBuffer , except by unmap() .
- Append view to this . [[mapping]] . views .
Append view to this . [[mapping]] . views .
- Return view .
Return view .
Note: User agents should consider issuing a developer-visible warning if getMappedRange() succeeds without having checked the status of
        the map, by waiting for mapAsync() to succeed, querying a mapState of "mapped" , or waiting for a
        later onSubmittedWorkDone() call to succeed.
Unmaps the mapped range of the GPUBuffer and makes its contents available for use by the
GPU again.
Returns: undefined
Content timeline steps:
- If this . [[pending_map]] is not null : Reject this . [[pending_map]] with an AbortError . Set this . [[pending_map]] to null .
If this . [[pending_map]] is not null :
- Reject this . [[pending_map]] with an AbortError .
Reject this . [[pending_map]] with an AbortError .
- Set this . [[pending_map]] to null .
Set this . [[pending_map]] to null .
- If this . [[mapping]] is null : Return.
If this . [[mapping]] is null :
- Return.
Return.
- For each ArrayBuffer ab in this . [[mapping]] . views : Perform DetachArrayBuffer ( ab , "WebGPUBufferMapping").
For each ArrayBuffer ab in this . [[mapping]] . views :
- Perform DetachArrayBuffer ( ab , "WebGPUBufferMapping").
Perform DetachArrayBuffer ( ab , "WebGPUBufferMapping").
- Let bufferUpdate be null .
Let bufferUpdate be null .
- If this . [[mapping]] . mode contains WRITE : Set bufferUpdate to { data : this . [[mapping]] . data , offset : this . [[mapping]] . range [0]
}. Note: When a buffer is mapped without the WRITE mode, then
unmapped, any local modifications done by the application to the mapped ranges ArrayBuffer are discarded and will not affect the content of later mappings.
If this . [[mapping]] . mode contains WRITE :
- Set bufferUpdate to { data : this . [[mapping]] . data , offset : this . [[mapping]] . range [0]
}.
Set bufferUpdate to { data : this . [[mapping]] . data , offset : this . [[mapping]] . range [0]
}.
Note: When a buffer is mapped without the WRITE mode, then
unmapped, any local modifications done by the application to the mapped ranges ArrayBuffer are discarded and will not affect the content of later mappings.
- Set this . [[mapping]] to null .
Set this . [[mapping]] to null .
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- If any of the following conditions are unsatisfied, return. this is valid to use with this . [[device]] .
If any of the following conditions are unsatisfied, return.
- this is valid to use with this . [[device]] .
this is valid to use with this . [[device]] .
- Assert this . [[internal state]] is " unavailable ".
Assert this . [[internal state]] is " unavailable ".
- If bufferUpdate is not null : Issue the following steps on the Queue timeline of this . [[device]] . queue : Queue timeline steps: Update the contents of this at offset bufferUpdate . offset with the data bufferUpdate . data .
If bufferUpdate is not null :
- Issue the following steps on the Queue timeline of this . [[device]] . queue : Queue timeline steps: Update the contents of this at offset bufferUpdate . offset with the data bufferUpdate . data .
Issue the following steps on the Queue timeline of this . [[device]] . queue :
- Update the contents of this at offset bufferUpdate . offset with the data bufferUpdate . data .
Update the contents of this at offset bufferUpdate . offset with the data bufferUpdate . data .
- Set this . [[internal state]] to " available ".
Set this . [[internal state]] to " available ".

## 6. Textures and Texture Views

### 6.1. GPUTexture

A texture is made up of 1d , 2d ,
or 3d arrays of data which can contain multiple values per-element to
represent things like colors. Textures can be read and written in many ways, depending on the GPUTextureUsage they are created with. For example, textures can be sampled, read, and written
from render and compute pipeline shaders, and they can be written by render pass outputs.
Internally, textures are often stored in GPU memory with a layout optimized for
multidimensional access rather than linear access.
One texture consists of one or more texture subresources ,
each uniquely identified by a mipmap level and,
for 2d textures only, array layer and aspect .
A texture subresource is a subresource : each can be used in different internal usages within a single usage scope .
Each subresource in a mipmap level is approximately half the size,
in each spatial dimension, of the corresponding resource in the lesser level
(see logical miplevel-specific texture extent ).
The subresource in level 0 has the dimensions of the texture itself.
Smaller levels are typically used to store lower resolution versions of the same image. GPUSampler and WGSL provide facilities for selecting and interpolating between levels of detail , explicitly or automatically.
A "2d" texture may be an array of array layer s.
Each subresource in a layer is the same size as the corresponding resources in other layers.
For non-2d textures, all subresources have an array layer index of 0.
Each subresource has an aspect .
Color textures have just one aspect: color . Depth-or-stencil format textures may have multiple aspects:
a depth aspect,
a stencil aspect, or both, and may be used in special ways, such as in depthStencilAttachment and in "depth" bindings.
A "3d" texture may have multiple slice s, each being the
two-dimensional image at a particular z value in the texture.
Slices are not separate subresources.
GPUTexture has the following immutable properties :
The width of this GPUTexture .
The height of this GPUTexture .
The depth or layer count of this GPUTexture .
The number of mip levels of this GPUTexture .
The number of sample count of this GPUTexture .
The dimension of the set of texel for each of this GPUTexture ’s subresources.
The format of this GPUTexture .
The allowed usages for this GPUTexture .
The set of GPUTextureFormat s that can be used as the GPUTextureViewDescriptor . format when creating views on this GPUTexture .
On devices with "core-features-and-limits" ,
this is undefined , and there is no such restriction.
GPUTexture has the following device timeline properties :
If the texture is destroyed, it can no longer be used in any operation,
and its underlying memory can be freed.
Arguments:
- GPUExtent3D baseSize
GPUExtent3D baseSize
- GPUSize32 mipLevel
GPUSize32 mipLevel
Returns: GPUExtent3DDict
Device timeline steps:
- Let extent be a new GPUExtent3DDict object.
Let extent be a new GPUExtent3DDict object.
- Set extent . width to max(1, baseSize . width ≫ mipLevel ).
Set extent . width to max(1, baseSize . width ≫ mipLevel ).
- Set extent . height to max(1, baseSize . height ≫ mipLevel ).
Set extent . height to max(1, baseSize . height ≫ mipLevel ).
- Set extent . depthOrArrayLayers to 1.
Set extent . depthOrArrayLayers to 1.
- Return extent .
Return extent .
The logical miplevel-specific texture extent of a texture is the size of the texture in texels at a specific miplevel. It is calculated by this procedure:
Arguments:
- GPUTextureDescriptor descriptor
GPUTextureDescriptor descriptor
- GPUSize32 mipLevel
GPUSize32 mipLevel
Returns: GPUExtent3DDict
- Let extent be a new GPUExtent3DDict object.
Let extent be a new GPUExtent3DDict object.
- If descriptor . dimension is: "1d" Set extent . width to max(1, descriptor . size . width ≫ mipLevel ). Set extent . height to 1. Set extent . depthOrArrayLayers to 1. "2d" Set extent . width to max(1, descriptor . size . width ≫ mipLevel ). Set extent . height to max(1, descriptor . size . height ≫ mipLevel ). Set extent . depthOrArrayLayers to descriptor . size . depthOrArrayLayers . "3d" Set extent . width to max(1, descriptor . size . width ≫ mipLevel ). Set extent . height to max(1, descriptor . size . height ≫ mipLevel ). Set extent . depthOrArrayLayers to max(1, descriptor . size . depthOrArrayLayers ≫ mipLevel ).
If descriptor . dimension is:
- Set extent . width to max(1, descriptor . size . width ≫ mipLevel ).
Set extent . width to max(1, descriptor . size . width ≫ mipLevel ).
- Set extent . height to 1.
Set extent . height to 1.
- Set extent . depthOrArrayLayers to 1.
Set extent . depthOrArrayLayers to 1.
- Set extent . width to max(1, descriptor . size . width ≫ mipLevel ).
Set extent . width to max(1, descriptor . size . width ≫ mipLevel ).
- Set extent . height to max(1, descriptor . size . height ≫ mipLevel ).
Set extent . height to max(1, descriptor . size . height ≫ mipLevel ).
- Set extent . depthOrArrayLayers to descriptor . size . depthOrArrayLayers .
Set extent . depthOrArrayLayers to descriptor . size . depthOrArrayLayers .
- Set extent . width to max(1, descriptor . size . width ≫ mipLevel ).
Set extent . width to max(1, descriptor . size . width ≫ mipLevel ).
- Set extent . height to max(1, descriptor . size . height ≫ mipLevel ).
Set extent . height to max(1, descriptor . size . height ≫ mipLevel ).
- Set extent . depthOrArrayLayers to max(1, descriptor . size . depthOrArrayLayers ≫ mipLevel ).
Set extent . depthOrArrayLayers to max(1, descriptor . size . depthOrArrayLayers ≫ mipLevel ).
- Return extent .
Return extent .
The physical miplevel-specific texture extent of a texture is the size of the texture in texels at a specific miplevel that includes the possible extra padding
to form complete texel blocks in the texture . It is calculated by this procedure:
Arguments:
- GPUTextureDescriptor descriptor
GPUTextureDescriptor descriptor
- GPUSize32 mipLevel
GPUSize32 mipLevel
Returns: GPUExtent3DDict
- Let extent be a new GPUExtent3DDict object.
Let extent be a new GPUExtent3DDict object.
- Let logicalExtent be logical miplevel-specific texture extent ( descriptor , mipLevel ).
Let logicalExtent be logical miplevel-specific texture extent ( descriptor , mipLevel ).
- If descriptor . dimension is: "1d" Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width . Set extent . height to 1. Set extent . depthOrArrayLayers to 1. "2d" Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width . Set extent . height to logicalExtent . height rounded up to the nearest multiple of descriptor ’s texel block height . Set extent . depthOrArrayLayers to logicalExtent . depthOrArrayLayers . "3d" Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width . Set extent . height to logicalExtent . height rounded up to the nearest multiple of descriptor ’s texel block height . Set extent . depthOrArrayLayers to logicalExtent . depthOrArrayLayers .
If descriptor . dimension is:
- Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width .
Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width .
- Set extent . height to 1.
Set extent . height to 1.
- Set extent . depthOrArrayLayers to 1.
Set extent . depthOrArrayLayers to 1.
- Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width .
Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width .
- Set extent . height to logicalExtent . height rounded up to the nearest multiple of descriptor ’s texel block height .
Set extent . height to logicalExtent . height rounded up to the nearest multiple of descriptor ’s texel block height .
- Set extent . depthOrArrayLayers to logicalExtent . depthOrArrayLayers .
Set extent . depthOrArrayLayers to logicalExtent . depthOrArrayLayers .
- Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width .
Set extent . width to logicalExtent . width rounded up to the nearest multiple of descriptor ’s texel block width .
- Set extent . height to logicalExtent . height rounded up to the nearest multiple of descriptor ’s texel block height .
Set extent . height to logicalExtent . height rounded up to the nearest multiple of descriptor ’s texel block height .
- Set extent . depthOrArrayLayers to logicalExtent . depthOrArrayLayers .
Set extent . depthOrArrayLayers to logicalExtent . depthOrArrayLayers .
- Return extent .
Return extent .
GPUTextureDescriptor has the following members:
The width, height, and depth or layer count of the texture.
The number of mip levels the texture will contain.
The sample count of the texture. A sampleCount > 1 indicates
a multisampled texture.
Whether the texture is one-dimensional, an array of two-dimensional layers, or three-dimensional.
The format of the texture.
The allowed usages for the texture.
Specifies what view format values will be allowed when calling createView() on this texture (in addition to the texture’s actual format ).
The actual performance impact is highly dependent on the target system; developers must
    test various systems to find out the impact on their particular application.
    For example, on some systems any texture with a format or viewFormats entry including "rgba8unorm-srgb" will perform less optimally than a "rgba8unorm" texture which does not.
    Similar caveats exist for other formats and pairs of formats on other systems.
Formats in this list must be texture view format compatible with the texture format.
- format equals viewFormat , or
format equals viewFormat , or
- format and viewFormat differ only in whether they are srgb formats (have the -srgb suffix) and device . [[features]] contains "core-features-and-limits" .
format and viewFormat differ only in whether they are srgb formats (have the -srgb suffix) and device . [[features]] contains "core-features-and-limits" .
On devices with "core-features-and-limits" ,
this is ignored, and there is no such restriction.
Specifies a texture that has one dimension, width. "1d" textures
cannot have mipmaps, be multisampled, use compressed or depth/stencil formats, or be used as
a render target.
Specifies a texture that has a width and height, and may have layers.
Specifies a texture that has a width, height, and depth. "3d" textures cannot be multisampled, and their format must support 3d textures
(all plain color formats and some packed/compressed formats ).
The GPUTextureUsage flags determine how a GPUTexture may be used after its creation:
The texture can be used as the source of a copy operation. (Examples: as the source argument of a copyTextureToTexture() or copyTextureToBuffer() call.)
The texture can be used as the destination of a copy or write operation. (Examples: as the destination argument of a copyTextureToTexture() or copyBufferToTexture() call, or as the target of a writeTexture() call.)
The texture can be bound for use as a sampled texture in a shader (Example: as a bind group
entry for a GPUTextureBindingLayout .)
The texture can be bound for use as a storage texture in a shader (Example: as a bind group
entry for a GPUStorageTextureBindingLayout .)
The texture can be used as a color or depth/stencil attachment in a render pass.
(Example: as a GPURenderPassColorAttachment . view or GPURenderPassDepthStencilAttachment . view .)
The texture is intended to be temporary (a hint for optimization), as it is only used within
a render pass.
Arguments:
- GPUTextureDimension dimension
GPUTextureDimension dimension
- GPUTextureDimension size
GPUTextureDimension size
- Calculate the max dimension value m : If dimension is: "1d" Return 1. "2d" Let m = max( size . width , size . height ). "3d" Let m = max(max( size . width , size . height ), size . depthOrArrayLayers ).
Calculate the max dimension value m :
- If dimension is: "1d" Return 1. "2d" Let m = max( size . width , size . height ). "3d" Let m = max(max( size . width , size . height ), size . depthOrArrayLayers ).
If dimension is:
Return 1.
Let m = max( size . width , size . height ).
Let m = max(max( size . width , size . height ), size . depthOrArrayLayers ).
- Return floor(log 2 ( m )) + 1.
Return floor(log 2 ( m )) + 1.
Creates a GPUTexture .
Arguments:
Returns: GPUTexture
Content timeline steps:
- ? validate GPUExtent3D shape ( descriptor . size ).
? validate GPUExtent3D shape ( descriptor . size ).
- ? Validate texture format required features of descriptor . format with this . [[device]] .
? Validate texture format required features of descriptor . format with this . [[device]] .
- ? Validate texture format required features of each element of descriptor . viewFormats with this . [[device]] .
? Validate texture format required features of each element of descriptor . viewFormats with this . [[device]] .
- Let t be ! create a new WebGPU object ( this , GPUTexture , descriptor ).
Let t be ! create a new WebGPU object ( this , GPUTexture , descriptor ).
- Set t . width to descriptor . size . width .
Set t . width to descriptor . size . width .
- Set t . height to descriptor . size . height .
Set t . height to descriptor . size . height .
- Set t . depthOrArrayLayers to descriptor . size . depthOrArrayLayers .
Set t . depthOrArrayLayers to descriptor . size . depthOrArrayLayers .
- Set t . mipLevelCount to descriptor . mipLevelCount .
Set t . mipLevelCount to descriptor . mipLevelCount .
- Set t . sampleCount to descriptor . sampleCount .
Set t . sampleCount to descriptor . sampleCount .
- Set t . dimension to descriptor . dimension .
Set t . dimension to descriptor . dimension .
- Set t . format to descriptor . format .
Set t . format to descriptor . format .
- Set t . usage to descriptor . usage .
Set t . usage to descriptor . usage .
- If t . [[device]] . [[features]] does not contain "core-features-and-limits" : If descriptor . textureBindingViewDimension is provided : Set t . textureBindingViewDimension to descriptor . textureBindingViewDimension . Otherwise, if descriptor . dimension is: "1d" Set t . textureBindingViewDimension to "1d" . "2d" If the array layer count of t is 1: Set t . textureBindingViewDimension to "2d" . Otherwise: Set t . textureBindingViewDimension to "2d-array" . "3d" Set t . textureBindingViewDimension to "3d" .
- If descriptor . textureBindingViewDimension is provided : Set t . textureBindingViewDimension to descriptor . textureBindingViewDimension . Otherwise, if descriptor . dimension is: "1d" Set t . textureBindingViewDimension to "1d" . "2d" If the array layer count of t is 1: Set t . textureBindingViewDimension to "2d" . Otherwise: Set t . textureBindingViewDimension to "2d-array" . "3d" Set t . textureBindingViewDimension to "3d" .
If descriptor . textureBindingViewDimension is provided :
- Set t . textureBindingViewDimension to descriptor . textureBindingViewDimension .
Set t . textureBindingViewDimension to descriptor . textureBindingViewDimension .
Otherwise, if descriptor . dimension is:
Set t . textureBindingViewDimension to "1d" .
If the array layer count of t is 1:
- Set t . textureBindingViewDimension to "2d" .
Set t . textureBindingViewDimension to "2d" .
Otherwise:
- Set t . textureBindingViewDimension to "2d-array" .
Set t . textureBindingViewDimension to "2d-array" .
Set t . textureBindingViewDimension to "3d" .
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return t .
Return t .
- If any of the following conditions are unsatisfied generate a validation error , invalidate t and return. validating GPUTextureDescriptor ( this , descriptor ) returns true .
If any of the following conditions are unsatisfied generate a validation error , invalidate t and return.
- validating GPUTextureDescriptor ( this , descriptor ) returns true .
validating GPUTextureDescriptor ( this , descriptor ) returns true .
- Set t . [[viewFormats]] to descriptor . viewFormats .
Set t . [[viewFormats]] to descriptor . viewFormats .
- Create a device allocation for t where each block has an equivalent texel representation to a block with a bit representation of zero. If the allocation fails without side-effects, generate an out-of-memory error , invalidate t , and return.
Create a device allocation for t where each block has an equivalent texel representation to a block with a bit representation of zero.
If the allocation fails without side-effects, generate an out-of-memory error , invalidate t , and return.
Arguments:
- GPUDevice this
GPUDevice this
- GPUTextureDescriptor descriptor
GPUTextureDescriptor descriptor
Device timeline steps:
- Let limits be this . [[limits]] .
Let limits be this . [[limits]] .
- Return true if all of the following requirements are met, and false otherwise: this must not be lost . descriptor . usage must not be 0. descriptor . usage must contain only bits present in this ’s allowed texture usages . descriptor . size . width , descriptor . size . height ,
and descriptor . size . depthOrArrayLayers must be > zero. descriptor . mipLevelCount must be > zero. descriptor . sampleCount must be either 1 or 4. If descriptor . dimension is: "1d" descriptor . size . width must be ≤ limits . maxTextureDimension1D . descriptor . size . height must be 1. descriptor . size . depthOrArrayLayers must be 1. descriptor . sampleCount must be 1. descriptor . format must not be a compressed format or depth-or-stencil format . "2d" descriptor . size . width must be ≤ limits . maxTextureDimension2D . descriptor . size . height must be ≤ limits . maxTextureDimension2D . descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureArrayLayers . "3d" descriptor . size . width must be ≤ limits . maxTextureDimension3D . descriptor . size . height must be ≤ limits . maxTextureDimension3D . descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureDimension3D . descriptor . sampleCount must be 1. descriptor . format must support "3d" textures according to § 26.1 Texture Format Capabilities . If this . [[features]] does not contain "core-features-and-limits" : If descriptor . textureBindingViewDimension is "2d" , this . size . depthOrArrayLayers must be 1. if descriptor . textureBindingViewDimension is "cube" , this . size . depthOrArrayLayers must be 6. descriptor . textureBindingViewDimension must not be "cube-array" . Note: this validation only applies to a user-specified textureBindingViewDimension. If no value is provided, the texture’s textureBindingViewDimension is set as described in createTexture() . That algorithm cannot produce invalid values, so the above validation is not required. descriptor . size . width must be multiple of texel block width . descriptor . size . height must be multiple of texel block height . If descriptor . sampleCount > 1: descriptor . mipLevelCount must be 1. descriptor . size . depthOrArrayLayers must be 1. descriptor . usage must not include the STORAGE_BINDING bit. descriptor . usage must include the RENDER_ATTACHMENT bit. descriptor . format must support multisampling according to § 26.1 Texture Format Capabilities . descriptor . mipLevelCount must be ≤ maximum mipLevel count ( descriptor . dimension , descriptor . size ). If descriptor . usage includes the RENDER_ATTACHMENT bit: descriptor . format must be a renderable format . descriptor . dimension must be either "2d" or "3d" . If descriptor . usage includes the STORAGE_BINDING bit: descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode. If descriptor . usage includes the TRANSIENT_ATTACHMENT bit: descriptor . usage must be equal to TRANSIENT_ATTACHMENT | RENDER_ATTACHMENT . descriptor . dimension must be equal to "2d" . descriptor . mipLevelCount must be 1. descriptor . size . depthOrArrayLayers must be 1. For each viewFormat in descriptor . viewFormats , descriptor . format and viewFormat must be texture view format compatible on device this . NOTE: Implementations may consider issuing a developer-visible warning if viewFormat is not compatible with any of the
    given usage bits, as that viewFormat will be unusable.
Return true if all of the following requirements are met, and false otherwise:
- this must not be lost .
this must not be lost .
- descriptor . usage must not be 0.
descriptor . usage must not be 0.
- descriptor . usage must contain only bits present in this ’s allowed texture usages .
descriptor . usage must contain only bits present in this ’s allowed texture usages .
- descriptor . size . width , descriptor . size . height ,
and descriptor . size . depthOrArrayLayers must be > zero.
descriptor . size . width , descriptor . size . height ,
and descriptor . size . depthOrArrayLayers must be > zero.
- descriptor . mipLevelCount must be > zero.
descriptor . mipLevelCount must be > zero.
- descriptor . sampleCount must be either 1 or 4.
descriptor . sampleCount must be either 1 or 4.
- If descriptor . dimension is: "1d" descriptor . size . width must be ≤ limits . maxTextureDimension1D . descriptor . size . height must be 1. descriptor . size . depthOrArrayLayers must be 1. descriptor . sampleCount must be 1. descriptor . format must not be a compressed format or depth-or-stencil format . "2d" descriptor . size . width must be ≤ limits . maxTextureDimension2D . descriptor . size . height must be ≤ limits . maxTextureDimension2D . descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureArrayLayers . "3d" descriptor . size . width must be ≤ limits . maxTextureDimension3D . descriptor . size . height must be ≤ limits . maxTextureDimension3D . descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureDimension3D . descriptor . sampleCount must be 1. descriptor . format must support "3d" textures according to § 26.1 Texture Format Capabilities .
If descriptor . dimension is:
- descriptor . size . width must be ≤ limits . maxTextureDimension1D .
descriptor . size . width must be ≤ limits . maxTextureDimension1D .
- descriptor . size . height must be 1.
descriptor . size . height must be 1.
- descriptor . size . depthOrArrayLayers must be 1.
descriptor . size . depthOrArrayLayers must be 1.
- descriptor . sampleCount must be 1.
descriptor . sampleCount must be 1.
- descriptor . format must not be a compressed format or depth-or-stencil format .
descriptor . format must not be a compressed format or depth-or-stencil format .
- descriptor . size . width must be ≤ limits . maxTextureDimension2D .
descriptor . size . width must be ≤ limits . maxTextureDimension2D .
- descriptor . size . height must be ≤ limits . maxTextureDimension2D .
descriptor . size . height must be ≤ limits . maxTextureDimension2D .
- descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureArrayLayers .
descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureArrayLayers .
- descriptor . size . width must be ≤ limits . maxTextureDimension3D .
descriptor . size . width must be ≤ limits . maxTextureDimension3D .
- descriptor . size . height must be ≤ limits . maxTextureDimension3D .
descriptor . size . height must be ≤ limits . maxTextureDimension3D .
- descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureDimension3D .
descriptor . size . depthOrArrayLayers must be ≤ limits . maxTextureDimension3D .
- descriptor . sampleCount must be 1.
descriptor . sampleCount must be 1.
- descriptor . format must support "3d" textures according to § 26.1 Texture Format Capabilities .
descriptor . format must support "3d" textures according to § 26.1 Texture Format Capabilities .
- If this . [[features]] does not contain "core-features-and-limits" : If descriptor . textureBindingViewDimension is "2d" , this . size . depthOrArrayLayers must be 1. if descriptor . textureBindingViewDimension is "cube" , this . size . depthOrArrayLayers must be 6. descriptor . textureBindingViewDimension must not be "cube-array" . Note: this validation only applies to a user-specified textureBindingViewDimension. If no value is provided, the texture’s textureBindingViewDimension is set as described in createTexture() . That algorithm cannot produce invalid values, so the above validation is not required.
- If descriptor . textureBindingViewDimension is "2d" , this . size . depthOrArrayLayers must be 1.
If descriptor . textureBindingViewDimension is "2d" , this . size . depthOrArrayLayers must be 1.
- if descriptor . textureBindingViewDimension is "cube" , this . size . depthOrArrayLayers must be 6.
if descriptor . textureBindingViewDimension is "cube" , this . size . depthOrArrayLayers must be 6.
- descriptor . textureBindingViewDimension must not be "cube-array" .
descriptor . textureBindingViewDimension must not be "cube-array" .
Note: this validation only applies to a user-specified textureBindingViewDimension. If no value is provided, the texture’s textureBindingViewDimension is set as described in createTexture() . That algorithm cannot produce invalid values, so the above validation is not required.
- descriptor . size . width must be multiple of texel block width .
descriptor . size . width must be multiple of texel block width .
- descriptor . size . height must be multiple of texel block height .
descriptor . size . height must be multiple of texel block height .
- If descriptor . sampleCount > 1: descriptor . mipLevelCount must be 1. descriptor . size . depthOrArrayLayers must be 1. descriptor . usage must not include the STORAGE_BINDING bit. descriptor . usage must include the RENDER_ATTACHMENT bit. descriptor . format must support multisampling according to § 26.1 Texture Format Capabilities .
If descriptor . sampleCount > 1:
- descriptor . mipLevelCount must be 1.
descriptor . mipLevelCount must be 1.
- descriptor . size . depthOrArrayLayers must be 1.
descriptor . size . depthOrArrayLayers must be 1.
- descriptor . usage must not include the STORAGE_BINDING bit.
descriptor . usage must not include the STORAGE_BINDING bit.
- descriptor . usage must include the RENDER_ATTACHMENT bit.
descriptor . usage must include the RENDER_ATTACHMENT bit.
- descriptor . format must support multisampling according to § 26.1 Texture Format Capabilities .
descriptor . format must support multisampling according to § 26.1 Texture Format Capabilities .
- descriptor . mipLevelCount must be ≤ maximum mipLevel count ( descriptor . dimension , descriptor . size ).
descriptor . mipLevelCount must be ≤ maximum mipLevel count ( descriptor . dimension , descriptor . size ).
- If descriptor . usage includes the RENDER_ATTACHMENT bit: descriptor . format must be a renderable format . descriptor . dimension must be either "2d" or "3d" .
If descriptor . usage includes the RENDER_ATTACHMENT bit:
- descriptor . format must be a renderable format .
descriptor . format must be a renderable format .
- descriptor . dimension must be either "2d" or "3d" .
descriptor . dimension must be either "2d" or "3d" .
- If descriptor . usage includes the STORAGE_BINDING bit: descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode.
If descriptor . usage includes the STORAGE_BINDING bit:
- descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode.
descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode.
- If descriptor . usage includes the TRANSIENT_ATTACHMENT bit: descriptor . usage must be equal to TRANSIENT_ATTACHMENT | RENDER_ATTACHMENT . descriptor . dimension must be equal to "2d" . descriptor . mipLevelCount must be 1. descriptor . size . depthOrArrayLayers must be 1.
If descriptor . usage includes the TRANSIENT_ATTACHMENT bit:
- descriptor . usage must be equal to TRANSIENT_ATTACHMENT | RENDER_ATTACHMENT .
descriptor . usage must be equal to TRANSIENT_ATTACHMENT | RENDER_ATTACHMENT .
- descriptor . dimension must be equal to "2d" .
descriptor . dimension must be equal to "2d" .
- descriptor . mipLevelCount must be 1.
descriptor . mipLevelCount must be 1.
- descriptor . size . depthOrArrayLayers must be 1.
descriptor . size . depthOrArrayLayers must be 1.
- For each viewFormat in descriptor . viewFormats , descriptor . format and viewFormat must be texture view format compatible on device this . NOTE: Implementations may consider issuing a developer-visible warning if viewFormat is not compatible with any of the
    given usage bits, as that viewFormat will be unusable.
For each viewFormat in descriptor . viewFormats , descriptor . format and viewFormat must be texture view format compatible on device this .
An application that no longer requires a GPUTexture can choose to lose access to it before
garbage collection by calling destroy() .
Note: This allows the user agent to reclaim the GPU memory associated with the GPUTexture once
all previously submitted operations using it are complete.
GPUTexture has the following methods:
Destroys the GPUTexture .
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the device timeline .
Issue the subsequent steps on the device timeline .
- Set this . [[destroyed]] to true.
Set this . [[destroyed]] to true.

### 6.2. GPUTextureView

A GPUTextureView is a view onto some subset of the texture subresources defined by
a particular GPUTexture .
GPUTextureView has the following immutable properties :
The GPUTexture into which this is a view.
The GPUTextureViewDescriptor describing this texture view.
All optional fields of GPUTextureViewDescriptor are defined.
For renderable views, this is the effective GPUExtent3DDict for rendering.
Note: this extent depends on the baseMipLevel .
- The mipmap level of s is ≥ desc . baseMipLevel and < desc . baseMipLevel + desc . mipLevelCount .
The mipmap level of s is ≥ desc . baseMipLevel and < desc . baseMipLevel + desc . mipLevelCount .
- The array layer of s is ≥ desc . baseArrayLayer and < desc . baseArrayLayer + desc . arrayLayerCount .
The array layer of s is ≥ desc . baseArrayLayer and < desc . baseArrayLayer + desc . arrayLayerCount .
- The aspect of s is in the set of aspects of desc . aspect .
The aspect of s is in the set of aspects of desc . aspect .
Two GPUTextureView objects are texture-view-aliasing if and only if
    their sets of subresources intersect.
GPUTextureViewDescriptor has the following members:
The format of the texture view. Must be either the format of the
texture or one of the viewFormats specified during its creation.
The dimension to view the texture as.
The allowed usage(s) for the texture view. Must be a subset of the usage flags of the texture. If 0, defaults to the full set of usage flags of the texture.
Note: If the view’s format doesn’t support all of the
texture’s usage s, the default will fail,
and the view’s usage must be specified explicitly.
Which aspect(s) of the texture are accessible to the texture view.
The first (most detailed) mipmap level accessible to the texture view.
How many mipmap levels, starting with baseMipLevel , are accessible to
the texture view.
The index of the first array layer accessible to the texture view.
How many array layers, starting with baseArrayLayer , are accessible
to the texture view.
A string of length four, with each character mapping to the texture view’s red/green/blue/alpha
channels, respectively.
When accessed by a shader, the red/green/blue/alpha channels are replaced by the value
corresponding to the component specified in swizzle[0] , swizzle[1] , swizzle[2] , and swizzle[3] , respectively:
- "r" : Take its value from the red channel of the texture.
"r" : Take its value from the red channel of the texture.
- "g" : Take its value from the green channel of the texture.
"g" : Take its value from the green channel of the texture.
- "b" : Take its value from the blue channel of the texture.
"b" : Take its value from the blue channel of the texture.
- "a" : Take its value from the alpha channel of the texture.
"a" : Take its value from the alpha channel of the texture.
- "0" : Force its value to 0.
"0" : Force its value to 0.
- "1" : Force its value to 1.
"1" : Force its value to 1.
Requires the "texture-component-swizzle" feature to be enabled.
The texture is viewed as a 1-dimensional image.
Corresponding WGSL types:
- texture_1d
texture_1d
- texture_storage_1d
texture_storage_1d
The texture is viewed as a single 2-dimensional image.
Corresponding WGSL types:
- texture_2d
texture_2d
- texture_storage_2d
texture_storage_2d
- texture_multisampled_2d
texture_multisampled_2d
- texture_depth_2d
texture_depth_2d
- texture_depth_multisampled_2d
texture_depth_multisampled_2d
The texture view is viewed as an array of 2-dimensional images.
Corresponding WGSL types:
- texture_2d_array
texture_2d_array
- texture_storage_2d_array
texture_storage_2d_array
- texture_depth_2d_array
texture_depth_2d_array
The texture is viewed as a cubemap.
The view has 6 array layers, each corresponding to a face of the cube in the order [+X, -X, +Y, -Y, +Z, -Z] and the following orientations:
Note: When viewed from the inside, this results in a left-handed coordinate system
where +X is right, +Y is up, and +Z is forward.
Sampling is done seamlessly across the faces of the cubemap.
Corresponding WGSL types:
- texture_cube
texture_cube
- texture_depth_cube
texture_depth_cube
The texture is viewed as a packed array of n cubemaps,
each with 6 array layers behaving like one "cube" view,
for 6 n array layers in total.
Corresponding WGSL types:
- texture_cube_array
texture_cube_array
- texture_depth_cube_array
texture_depth_cube_array
The texture is viewed as a 3-dimensional image.
Corresponding WGSL types:
- texture_3d
texture_3d
- texture_storage_3d
texture_storage_3d
Each GPUTextureAspect value corresponds to a set of aspects .
The set of aspects are defined for each value below.
All available aspects of the texture format will be accessible to the texture view. For
color formats the color aspect will be accessible. For combined depth-stencil format s both the depth and stencil aspects will be accessible. Depth-or-stencil format s with a single aspect will only make that aspect accessible.
The set of aspects is [ color , depth , stencil ].
Only the stencil aspect of a depth-or-stencil format format will be accessible to the
texture view.
The set of aspects is [ stencil ].
Only the depth aspect of a depth-or-stencil format format will be accessible to the
texture view.
The set of aspects is [ depth ].
Creates a GPUTextureView .
For textures created from sources where the layer count is unknown at the
    time of development it is recommended that calls to createView() are provided
    with an explicit dimension to ensure shader compatibility.
Arguments:
Returns: view , of type GPUTextureView .
Content timeline steps:
- ? Validate texture format required features of descriptor . format with this . [[device]] .
? Validate texture format required features of descriptor . format with this . [[device]] .
- ? Validate swizzle string of descriptor . swizzle .
? Validate swizzle string of descriptor . swizzle .
- Let view be ! create a new WebGPU object ( this , GPUTextureView , descriptor ).
Let view be ! create a new WebGPU object ( this , GPUTextureView , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return view .
Return view .
- Set descriptor to the result of resolving GPUTextureViewDescriptor defaults for this with descriptor .
Set descriptor to the result of resolving GPUTextureViewDescriptor defaults for this with descriptor .
- If any of the following conditions are unsatisfied generate a validation error , invalidate view and return. this is valid to use with this . [[device]] . descriptor . aspect must be present in this . format . If the descriptor . aspect is "all" : descriptor . format must equal either this . format or one
    of the formats in this . [[viewFormats]] . Otherwise: descriptor . format must equal the result of resolving GPUTextureAspect ( this . format , descriptor . aspect ). If descriptor . swizzle is not "rgba" , "texture-component-swizzle" must be enabled for this . [[device]] . descriptor . usage must be a subset of this . usage . If descriptor . usage includes the RENDER_ATTACHMENT bit: descriptor . format must be a renderable format . If descriptor . usage includes the STORAGE_BINDING bit: descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode. descriptor . mipLevelCount must be > 0. descriptor . baseMipLevel + descriptor . mipLevelCount must be ≤ this . mipLevelCount . descriptor . arrayLayerCount must be > 0. descriptor . baseArrayLayer + descriptor . arrayLayerCount must be ≤
the array layer count of this . If this . sampleCount > 1, descriptor . dimension must be "2d" . If descriptor . dimension is: "1d" this . dimension must be "1d" . descriptor . arrayLayerCount must be 1 . "2d" this . dimension must be "2d" . descriptor . arrayLayerCount must be 1 . "2d-array" this . dimension must be "2d" . "cube" this . dimension must be "2d" . descriptor . arrayLayerCount must be 6 . this . width must equal this . height . "cube-array" this . dimension must be "2d" . descriptor . arrayLayerCount must be a multiple of 6 . this . width must equal this . height . [[device]] . [[features]] must contain "core-features-and-limits" . "3d" this . dimension must be "3d" . descriptor . arrayLayerCount must be 1 .
If any of the following conditions are unsatisfied generate a validation error , invalidate view and return.
- this is valid to use with this . [[device]] .
this is valid to use with this . [[device]] .
- descriptor . aspect must be present in this . format .
descriptor . aspect must be present in this . format .
- If the descriptor . aspect is "all" : descriptor . format must equal either this . format or one
    of the formats in this . [[viewFormats]] . Otherwise: descriptor . format must equal the result of resolving GPUTextureAspect ( this . format , descriptor . aspect ).
If the descriptor . aspect is "all" :
- descriptor . format must equal either this . format or one
    of the formats in this . [[viewFormats]] .
descriptor . format must equal either this . format or one
    of the formats in this . [[viewFormats]] .
Otherwise:
- descriptor . format must equal the result of resolving GPUTextureAspect ( this . format , descriptor . aspect ).
descriptor . format must equal the result of resolving GPUTextureAspect ( this . format , descriptor . aspect ).
- If descriptor . swizzle is not "rgba" , "texture-component-swizzle" must be enabled for this . [[device]] .
If descriptor . swizzle is not "rgba" , "texture-component-swizzle" must be enabled for this . [[device]] .
- descriptor . usage must be a subset of this . usage .
descriptor . usage must be a subset of this . usage .
- If descriptor . usage includes the RENDER_ATTACHMENT bit: descriptor . format must be a renderable format .
If descriptor . usage includes the RENDER_ATTACHMENT bit:
- descriptor . format must be a renderable format .
descriptor . format must be a renderable format .
- If descriptor . usage includes the STORAGE_BINDING bit: descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode.
If descriptor . usage includes the STORAGE_BINDING bit:
- descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode.
descriptor . format must be listed in § 26.1.1 Plain color formats table
with STORAGE_BINDING capability for at least one access mode.
- descriptor . mipLevelCount must be > 0.
descriptor . mipLevelCount must be > 0.
- descriptor . baseMipLevel + descriptor . mipLevelCount must be ≤ this . mipLevelCount .
descriptor . baseMipLevel + descriptor . mipLevelCount must be ≤ this . mipLevelCount .
- descriptor . arrayLayerCount must be > 0.
descriptor . arrayLayerCount must be > 0.
- descriptor . baseArrayLayer + descriptor . arrayLayerCount must be ≤
the array layer count of this .
descriptor . baseArrayLayer + descriptor . arrayLayerCount must be ≤
the array layer count of this .
- If this . sampleCount > 1, descriptor . dimension must be "2d" .
If this . sampleCount > 1, descriptor . dimension must be "2d" .
- If descriptor . dimension is: "1d" this . dimension must be "1d" . descriptor . arrayLayerCount must be 1 . "2d" this . dimension must be "2d" . descriptor . arrayLayerCount must be 1 . "2d-array" this . dimension must be "2d" . "cube" this . dimension must be "2d" . descriptor . arrayLayerCount must be 6 . this . width must equal this . height . "cube-array" this . dimension must be "2d" . descriptor . arrayLayerCount must be a multiple of 6 . this . width must equal this . height . [[device]] . [[features]] must contain "core-features-and-limits" . "3d" this . dimension must be "3d" . descriptor . arrayLayerCount must be 1 .
If descriptor . dimension is:
- this . dimension must be "1d" .
this . dimension must be "1d" .
- descriptor . arrayLayerCount must be 1 .
descriptor . arrayLayerCount must be 1 .
- this . dimension must be "2d" .
this . dimension must be "2d" .
- descriptor . arrayLayerCount must be 1 .
descriptor . arrayLayerCount must be 1 .
- this . dimension must be "2d" .
this . dimension must be "2d" .
- this . dimension must be "2d" .
this . dimension must be "2d" .
- descriptor . arrayLayerCount must be 6 .
descriptor . arrayLayerCount must be 6 .
- this . width must equal this . height .
this . width must equal this . height .
- this . dimension must be "2d" .
this . dimension must be "2d" .
- descriptor . arrayLayerCount must be a multiple of 6 .
descriptor . arrayLayerCount must be a multiple of 6 .
- this . width must equal this . height .
this . width must equal this . height .
- [[device]] . [[features]] must contain "core-features-and-limits" .
- this . dimension must be "3d" .
this . dimension must be "3d" .
- descriptor . arrayLayerCount must be 1 .
descriptor . arrayLayerCount must be 1 .
- Let view be a new GPUTextureView object.
Let view be a new GPUTextureView object.
- Set view . [[texture]] to this .
Set view . [[texture]] to this .
- Set view . [[descriptor]] to descriptor .
Set view . [[descriptor]] to descriptor .
- If descriptor . usage contains RENDER_ATTACHMENT : Let renderExtent be compute render extent ([ this . width , this . height , this . depthOrArrayLayers ], descriptor . baseMipLevel ). Set view . [[renderExtent]] to renderExtent .
If descriptor . usage contains RENDER_ATTACHMENT :
- Let renderExtent be compute render extent ([ this . width , this . height , this . depthOrArrayLayers ], descriptor . baseMipLevel ).
Let renderExtent be compute render extent ([ this . width , this . height , this . depthOrArrayLayers ], descriptor . baseMipLevel ).
- Set view . [[renderExtent]] to renderExtent .
Set view . [[renderExtent]] to renderExtent .
- Let resolved be a copy of descriptor .
Let resolved be a copy of descriptor .
- If resolved . format is not provided : Let format be the result of resolving GPUTextureAspect ( format , descriptor . aspect ). If format is null : Set resolved . format to texture . format . Otherwise: Set resolved . format to format .
If resolved . format is not provided :
- Let format be the result of resolving GPUTextureAspect ( format , descriptor . aspect ).
Let format be the result of resolving GPUTextureAspect ( format , descriptor . aspect ).
- If format is null : Set resolved . format to texture . format . Otherwise: Set resolved . format to format .
If format is null :
- Set resolved . format to texture . format .
Set resolved . format to texture . format .
Otherwise:
- Set resolved . format to format .
Set resolved . format to format .
- If resolved . mipLevelCount is not provided :
set resolved . mipLevelCount to texture . mipLevelCount − resolved . baseMipLevel .
If resolved . mipLevelCount is not provided :
set resolved . mipLevelCount to texture . mipLevelCount − resolved . baseMipLevel .
- If resolved . dimension is not provided and texture . dimension is: "1d" Set resolved . dimension to "1d" . "2d" If the array layer count of texture is 1: Set resolved . dimension to "2d" . Otherwise: Set resolved . dimension to "2d-array" . "3d" Set resolved . dimension to "3d" .
If resolved . dimension is not provided and texture . dimension is:
Set resolved . dimension to "1d" .
If the array layer count of texture is 1:
- Set resolved . dimension to "2d" .
Set resolved . dimension to "2d" .
Otherwise:
- Set resolved . dimension to "2d-array" .
Set resolved . dimension to "2d-array" .
Set resolved . dimension to "3d" .
- If resolved . arrayLayerCount is not provided and resolved . dimension is: "1d" , "2d" , or "3d" Set resolved . arrayLayerCount to 1 . "cube" Set resolved . arrayLayerCount to 6 . "2d-array" or "cube-array" Set resolved . arrayLayerCount to the array layer count of texture − resolved . baseArrayLayer .
If resolved . arrayLayerCount is not provided and resolved . dimension is:
Set resolved . arrayLayerCount to 1 .
Set resolved . arrayLayerCount to 6 .
Set resolved . arrayLayerCount to the array layer count of texture − resolved . baseArrayLayer .
- If resolved . usage is 0 :
set resolved . usage to texture . usage .
If resolved . usage is 0 :
set resolved . usage to texture . usage .
- Return resolved .
Return resolved .
- If texture . dimension is: "1d" or "3d" Return 1 . "2d" Return texture . depthOrArrayLayers .
If texture . dimension is:
Return 1 .
Return texture . depthOrArrayLayers .
- If swizzle does not match the [ECMAScript] regexp ^[rgba01]{4}$ : Throw a TypeError .
If swizzle does not match the [ECMAScript] regexp ^[rgba01]{4}$ :
- Throw a TypeError .
Throw a TypeError .

### 6.3. Texture Formats

The name of the format specifies the order of components, bits per component,
and data type for the component.
- r , g , b , a = red, green, blue, alpha
r , g , b , a = red, green, blue, alpha
- unorm = unsigned normalized
unorm = unsigned normalized
- snorm = signed normalized
snorm = signed normalized
- uint = unsigned int
uint = unsigned int
- sint = signed int
sint = signed int
- float = floating point
float = floating point
If the format has the -srgb suffix, then sRGB conversions from gamma to linear
and vice versa are applied during the reading and writing of color values in the
shader. Compressed texture formats are provided by features . Their naming
should follow the convention here, with the texture name as a prefix. e.g. etc2-rgba8unorm .
The texel block is a single addressable element of the textures in pixel-based GPUTextureFormat s,
and a single compressed block of the textures in block-based compressed GPUTextureFormat s.
The texel block width and texel block height specifies the dimension of one texel block .
- For pixel-based GPUTextureFormat s, the texel block width and texel block height are always 1.
For pixel-based GPUTextureFormat s, the texel block width and texel block height are always 1.
- For block-based compressed GPUTextureFormat s, the texel block width is the number of texels in each row of one texel block ,
and the texel block height is the number of texel rows in one texel block . See § 26.1 Texture Format Capabilities for an exhaustive list
of values for every texture format.
For block-based compressed GPUTextureFormat s, the texel block width is the number of texels in each row of one texel block ,
and the texel block height is the number of texel rows in one texel block . See § 26.1 Texture Format Capabilities for an exhaustive list
of values for every texture format.
The texel block copy footprint of an aspect of a GPUTextureFormat is the number of
bytes one texel block occupies during a texel copy , if applicable.
Note: The texel block memory cost of a GPUTextureFormat is the number of
bytes needed to store one texel block . It is not fully defined for all formats. This value is informative and non-normative.
The depth component of the "depth24plus" and "depth24plus-stencil8" formats may be implemented as either a 24-bit depth value or a "depth32float" value.
The stencil8 format may be implemented as
either a real "stencil8", or "depth24stencil8", where the depth aspect is
hidden and inaccessible.
- For 24-bit depth , 1 ULP has a constant value of 1 / (2 24 − 1).
For 24-bit depth , 1 ULP has a constant value of 1 / (2 24 − 1).
- For depth32float, 1 ULP has a variable value no greater than 1 / (2 24 ).
For depth32float, 1 ULP has a variable value no greater than 1 / (2 24 ).
A format is renderable if it is either a color renderable format , or a depth-or-stencil format .
If a format is listed in § 26.1.1 Plain color formats with RENDER_ATTACHMENT capability, it is a
color renderable format. Any other format is not a color renderable format.
All depth-or-stencil formats are renderable.
A renderable format is also blendable if it can be used with render pipeline blending.
See § 26.1 Texture Format Capabilities .
A format is filterable if it supports the GPUTextureSampleType "float" (not just "unfilterable-float" );
that is, it can be used with "filtering" GPUSampler s.
See § 26.1 Texture Format Capabilities .
Arguments:
- GPUTextureFormat format
GPUTextureFormat format
- GPUTextureAspect aspect
GPUTextureAspect aspect
Returns: GPUTextureFormat or null
- If aspect is: "all" Return format . "depth-only" "stencil-only" If format is a depth-stencil-format:
Return the aspect-specific format of format according to § 26.1.2 Depth-stencil formats or null if
    the aspect is not present in format .
If aspect is:
Return format .
If format is a depth-stencil-format:
Return the aspect-specific format of format according to § 26.1.2 Depth-stencil formats or null if
    the aspect is not present in format .
- Return null .
Return null .
Use of some texture formats require a feature to be enabled on the GPUDevice . Because new
formats can be added to the specification, those enum values might not be known by the implementation.
In order to normalize behavior across implementations, attempting to use a format that requires a
feature will throw an exception if the associated feature is not enabled on the device. This makes
the behavior the same as when the format is unknown to the implementation.
See § 26.1 Texture Format Capabilities for information about which GPUTextureFormat s require features.
- If format requires a feature and device . [[features]] does not contain the feature: Throw a TypeError .
If format requires a feature and device . [[features]] does not contain the feature:
- Throw a TypeError .
Throw a TypeError .

### 6.4. GPUExternalTexture

A GPUExternalTexture is a sampleable 2D texture wrapping an external video frame.
It is an immutable snapshot; its contents cannot change over time, either from inside WebGPU
(it is only sampleable) or from outside WebGPU (e.g. due to video frame advancement).
GPUExternalTexture s can be bound into bind groups via the externalTexture bind group layout entry member.
Note that member uses several binding slots, as defined there.
The underlying representation of an external texture is unobservable
    (except for precise sampling behavior), but typically may include:
- Up to three 2D planes of data (e.g. RGBA, Y+UV, Y+U+V).
Up to three 2D planes of data (e.g. RGBA, Y+UV, Y+U+V).
- Metadata for converting coordinates before reading from those planes (crop and rotation).
Metadata for converting coordinates before reading from those planes (crop and rotation).
- Metadata for converting values into the specified output color space (matrices, gammas, 3D LUT).
Metadata for converting values into the specified output color space (matrices, gammas, 3D LUT).
The configuration used internally by an implementation may be inconsistent across time,
    systems, user agents, media sources, or even frames within a single video source.
    In order to account for many possible representations,
    the binding conservatively uses the following, for each external texture:
- three sampled texture bindings (for up to 3 planes),
three sampled texture bindings (for up to 3 planes),
- one sampled texture binding for a 3D LUT,
one sampled texture binding for a 3D LUT,
- one sampler binding to sample the 3D LUT, and
one sampler binding to sample the 3D LUT, and
- one uniform buffer binding for metadata.
one uniform buffer binding for metadata.
GPUExternalTexture has the following immutable properties :
The descriptor with which the texture was created.
GPUExternalTexture has the following immutable properties :
Indicates whether the object has expired (can no longer be used).
Note: Unlike [[destroyed]] slots, which are similar, this can change from true back to false .
An external texture is created from an external video object
using importExternalTexture() .
An external texture created from an HTMLVideoElement expires (is destroyed) automatically in a
task after it is imported, instead of manually or upon garbage collection like other resources.
When an external texture expires, its [[expired]] slot changes to true .
An external texture created from a VideoFrame expires (is destroyed) when, and only when,
the source VideoFrame is closed ,
either explicitly by close() , or by other means.
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
[LINK: close()](https://w3c.github.io/webcodecs/#dom-videoframe-close)
Note: As noted in decode() , authors should call close() on output VideoFrame s to avoid decoder stalls.
If an imported VideoFrame is dropped without being closed, the imported GPUExternalTexture object will keep it alive until it is also dropped.
The VideoFrame cannot be garbage collected until both objects are dropped.
Garbage collection is unpredictable, so this may still stall the video decoder.
[LINK: decode()](https://w3c.github.io/webcodecs/#dom-videodecoder-decode)
[LINK: close()](https://w3c.github.io/webcodecs/#dom-videoframe-close)
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
Once the GPUExternalTexture expires, importExternalTexture() must be called again.
However, the user agent may un-expire and return the same GPUExternalTexture again, instead of
creating a new one. This will commonly happen unless the execution of the application is scheduled
to match the video’s frame rate (e.g. using requestVideoFrameCallback() ).
If the same object is returned again, it will compare equal, and GPUBindGroup s, GPURenderBundle s, etc. referencing the previous object can still be used.
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
GPUExternalTextureDescriptor dictionaries have the following members:
The video source to import the external texture from. Source size is determined as described
by the external source dimensions table.
The color space the image contents of source will be
converted into when reading.
Creates a GPUExternalTexture wrapping the provided image source.
Arguments:
Returns: GPUExternalTexture
Content timeline steps:
- Let source be descriptor . source .
Let source be descriptor . source .
- If the current image contents of source are the same as the most recent importExternalTexture() call with the same descriptor (ignoring label ),
and the user agent chooses to reuse it: Let previousResult be the GPUExternalTexture returned previously. Set previousResult . [[expired]] to false ,
renewing ownership of the underlying resource. Let result be previousResult . Note: This allows the application to detect duplicate imports and avoid re-creating
dependent objects (such as GPUBindGroup s).
Implementations still need to be able to handle a single frame being wrapped by
multiple GPUExternalTexture , since import metadata like colorSpace can change even for the same frame. Otherwise: If source is not origin-clean ,
throw a SecurityError and return. Let usability be ? check the usability of the image argument ( source ). If usability is not good : Generate a validation error . Return an invalidated GPUExternalTexture . Let data be the result of converting the current image contents of source into
the color space descriptor . colorSpace with unpremultiplied alpha. This may result in values outside of the range [0, 1].
If clamping is desired, it may be performed after sampling. Note: This is described like a copy, but may be implemented as a reference to
read-only underlying data plus appropriate metadata to perform conversion later. Let result be a new GPUExternalTexture object wrapping data .
If the current image contents of source are the same as the most recent importExternalTexture() call with the same descriptor (ignoring label ),
and the user agent chooses to reuse it:
- Let previousResult be the GPUExternalTexture returned previously.
Let previousResult be the GPUExternalTexture returned previously.
- Set previousResult . [[expired]] to false ,
renewing ownership of the underlying resource.
Set previousResult . [[expired]] to false ,
renewing ownership of the underlying resource.
- Let result be previousResult .
Let result be previousResult .
Note: This allows the application to detect duplicate imports and avoid re-creating
dependent objects (such as GPUBindGroup s).
Implementations still need to be able to handle a single frame being wrapped by
multiple GPUExternalTexture , since import metadata like colorSpace can change even for the same frame.
Otherwise:
- If source is not origin-clean ,
throw a SecurityError and return.
If source is not origin-clean ,
throw a SecurityError and return.
- Let usability be ? check the usability of the image argument ( source ).
Let usability be ? check the usability of the image argument ( source ).
- If usability is not good : Generate a validation error . Return an invalidated GPUExternalTexture .
If usability is not good :
- Generate a validation error .
Generate a validation error .
- Return an invalidated GPUExternalTexture .
Return an invalidated GPUExternalTexture .
- Let data be the result of converting the current image contents of source into
the color space descriptor . colorSpace with unpremultiplied alpha. This may result in values outside of the range [0, 1].
If clamping is desired, it may be performed after sampling. Note: This is described like a copy, but may be implemented as a reference to
read-only underlying data plus appropriate metadata to perform conversion later.
Let data be the result of converting the current image contents of source into
the color space descriptor . colorSpace with unpremultiplied alpha.
This may result in values outside of the range [0, 1].
If clamping is desired, it may be performed after sampling.
Note: This is described like a copy, but may be implemented as a reference to
read-only underlying data plus appropriate metadata to perform conversion later.
- Let result be a new GPUExternalTexture object wrapping data .
Let result be a new GPUExternalTexture object wrapping data .
- If source is an HTMLVideoElement , queue an automatic expiry task with device this and the following steps: Set result . [[expired]] to true ,
releasing ownership of the underlying resource. Note: An HTMLVideoElement should be imported in the same task that samples the texture
(which should generally be scheduled using requestVideoFrameCallback or requestAnimationFrame() depending on the application).
Otherwise, a texture could get destroyed by these steps before the
application is finished using it.
If source is an HTMLVideoElement , queue an automatic expiry task with device this and the following steps:
- Set result . [[expired]] to true ,
releasing ownership of the underlying resource.
Set result . [[expired]] to true ,
releasing ownership of the underlying resource.
Note: An HTMLVideoElement should be imported in the same task that samples the texture
(which should generally be scheduled using requestVideoFrameCallback or requestAnimationFrame() depending on the application).
Otherwise, a texture could get destroyed by these steps before the
application is finished using it.
- If source is a VideoFrame , then when source is closed , run the following steps: Set result . [[expired]] to true .
If source is a VideoFrame , then when source is closed , run the following steps:
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
- Set result . [[expired]] to true .
Set result . [[expired]] to true .
- Set result . label to descriptor . label .
Set result . label to descriptor . label .
- Return result .
Return result .

### 6.5. Sampling External Texture Bindings

The externalTexture binding point allows binding GPUExternalTexture objects (from dynamic image sources like videos). It also supports GPUTexture and GPUTextureView .
Note: When a GPUTexture or a GPUTextureView is bound to an externalTexture binding, it is like a GPUExternalTexture with a single RGBA plane and no crop, rotation, or color
conversion.
External textures are represented in WGSL with texture_external and may be read using textureLoad and textureSampleBaseClampToEdge .
The sampler provided to textureSampleBaseClampToEdge is used to sample the underlying textures.
When the binding resource type is a GPUExternalTexture , the result is in the color space set
by colorSpace .
It is implementation-dependent whether, for any given external texture, the sampler (and filtering)
is applied before or after conversion from underlying values into the specified color space.
Note: If the internal representation is an RGBA plane, sampling behaves as on a regular 2D texture.
If there are several underlying planes (e.g. Y+UV), the sampler is used to sample each
underlying texture separately, prior to conversion from YUV to the specified color space.

## 7. Samplers

### 7.1. GPUSampler

A GPUSampler encodes transformations and filtering information that can
be used in a shader to interpret texture resource data.
GPUSampler s are created via createSampler() .
GPUSampler has the following immutable properties :
The GPUSamplerDescriptor with which the GPUSampler was created.
Whether the GPUSampler is used as a comparison sampler.
Whether the GPUSampler weights multiple samples of a texture.
A GPUSamplerDescriptor specifies the options to use to create a GPUSampler .
Specifies the address modes for the texture width, height, and depth
coordinates, respectively.
Specifies the sampling behavior when the sampled area is smaller than or equal to one
texel.
Specifies the sampling behavior when the sampled area is larger than one texel.
Specifies behavior for sampling between mipmap levels.
Specifies the minimum and maximum levels of detail , respectively, used internally when
sampling a texture.
When provided the sampler will be a comparison sampler with the specified GPUCompareFunction .
Note: Comparison samplers may use filtering, but the sampling results will be
implementation-dependent and may differ from the normal filtering rules.
Specifies the maximum anisotropy value clamp used by the sampler. Anisotropic filtering is
enabled when maxAnisotropy is > 1 and the implementation supports it.
Anisotropic filtering improves the image quality of textures sampled at oblique viewing
angles. Higher maxAnisotropy values indicate the maximum ratio of
anisotropy supported when filtering.
The precise filtering behavior is implementation-dependent.
Level of detail (LOD) describes which mip level(s) are selected when sampling a
texture. It may be specified explicitly through shader methods like textureSampleLevel or implicitly determined from
the texture coordinate derivatives.
[LINK: textureSampleLevel](https://gpuweb.github.io/gpuweb/wgsl/#texturesamplelevel)
Note: See Scale Factor Operation, LOD Operation and Image Level Selection in
the Vulkan 1.3 spec for an example of how implicit LODs may be calculated.
GPUAddressMode describes the behavior of the sampler if the sampled texels extend beyond the
bounds of the sampled texture.
Texture coordinates are clamped between 0.0 and 1.0, inclusive.
Texture coordinates wrap to the other side of the texture.
Texture coordinates wrap to the other side of the texture, but the texture is flipped
when the integer part of the coordinate is odd.
GPUFilterMode and GPUMipmapFilterMode describe the behavior of the sampler if the sampled
area does not cover exactly one texel.
Note: See Texel Filtering in the Vulkan 1.3 spec for an example of how
samplers may determine which texels are sampled from for the various filtering modes.
Return the value of the texel nearest to the texture coordinates.
Select two texels in each dimension and return a linear interpolation between their values.
GPUCompareFunction specifies the behavior of a comparison sampler. If a comparison sampler is
used in a shader, the depth_ref is compared to the fetched texel value, and the result of this
comparison test is generated ( 1.0f for pass, or 0.0f for fail).
After comparison, if texture filtering is enabled, the filtering step occurs, so that comparison
results are mixed together resulting in values in the range [0, 1] . Filtering should behave
as usual, however it may be computed with lower precision or not mix results at all.
Comparison tests never pass.
A provided value passes the comparison test if it is less than the sampled value.
A provided value passes the comparison test if it is equal to the sampled value.
A provided value passes the comparison test if it is less than or equal to the sampled value.
A provided value passes the comparison test if it is greater than the sampled value.
A provided value passes the comparison test if it is not equal to the sampled value.
A provided value passes the comparison test if it is greater than or equal to the sampled value.
Comparison tests always pass.
Creates a GPUSampler .
Arguments:
Returns: GPUSampler
Content timeline steps:
- Let s be ! create a new WebGPU object ( this , GPUSampler , descriptor ).
Let s be ! create a new WebGPU object ( this , GPUSampler , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return s .
Return s .
- If any of the following conditions are unsatisfied generate a validation error , invalidate s and return. this must not be lost . descriptor . lodMinClamp ≥ 0. descriptor . lodMaxClamp ≥ descriptor . lodMinClamp . descriptor . maxAnisotropy ≥ 1. Note: Most implementations support maxAnisotropy values in range between 1 and 16, inclusive. The provided maxAnisotropy value will be clamped to the
maximum value that the platform supports. If descriptor . maxAnisotropy > 1: descriptor . magFilter , descriptor . minFilter ,
and descriptor . mipmapFilter must be "linear" .
If any of the following conditions are unsatisfied generate a validation error , invalidate s and return.
- this must not be lost .
this must not be lost .
- descriptor . lodMinClamp ≥ 0.
descriptor . lodMinClamp ≥ 0.
- descriptor . lodMaxClamp ≥ descriptor . lodMinClamp .
descriptor . lodMaxClamp ≥ descriptor . lodMinClamp .
- descriptor . maxAnisotropy ≥ 1. Note: Most implementations support maxAnisotropy values in range between 1 and 16, inclusive. The provided maxAnisotropy value will be clamped to the
maximum value that the platform supports.
descriptor . maxAnisotropy ≥ 1.
Note: Most implementations support maxAnisotropy values in range between 1 and 16, inclusive. The provided maxAnisotropy value will be clamped to the
maximum value that the platform supports.
- If descriptor . maxAnisotropy > 1: descriptor . magFilter , descriptor . minFilter ,
and descriptor . mipmapFilter must be "linear" .
If descriptor . maxAnisotropy > 1:
- descriptor . magFilter , descriptor . minFilter ,
and descriptor . mipmapFilter must be "linear" .
descriptor . magFilter , descriptor . minFilter ,
and descriptor . mipmapFilter must be "linear" .
- Set s . [[descriptor]] to descriptor .
Set s . [[descriptor]] to descriptor .
- Set s . [[isComparison]] to false if the compare attribute
    of s . [[descriptor]] is null or undefined. Otherwise, set it to true .
Set s . [[isComparison]] to false if the compare attribute
    of s . [[descriptor]] is null or undefined. Otherwise, set it to true .
- Set s . [[isFiltering]] to false if none of minFilter , magFilter , or mipmapFilter has the value of "linear" . Otherwise, set it to true .
Set s . [[isFiltering]] to false if none of minFilter , magFilter , or mipmapFilter has the value of "linear" . Otherwise, set it to true .

## 8. Resource Binding

### 8.1. GPUBindGroupLayout

A GPUBindGroupLayout defines the interface between a set of resources bound in a GPUBindGroup and their accessibility in shader stages.
GPUBindGroupLayout has the following immutable properties :
A GPUBindGroupLayout is created via GPUDevice.createBindGroupLayout() .
GPUBindGroupLayoutDescriptor dictionaries have the following members:
A list of entries describing the shader resource bindings for a bind group.
A GPUBindGroupLayoutEntry describes a single shader resource binding to be included in a GPUBindGroupLayout .
GPUBindGroupLayoutEntry dictionaries have the following members:
A unique identifier for a resource binding within the GPUBindGroupLayout , corresponding
to a GPUBindGroupEntry.binding and a @binding attribute in the GPUShaderModule .
[LINK: @binding](https://gpuweb.github.io/gpuweb/wgsl/#attribute-binding)
A bitset of the members of GPUShaderStage .
Each set bit indicates that a GPUBindGroupLayoutEntry ’s resource
will be accessible from the associated shader stage.
Exactly one of these members must be set, indicating the binding type.
The contents of the member specify options specific to that type.
The corresponding resource in createBindGroup() requires
the corresponding binding resource type for this binding.
GPUShaderStage contains the following flags, which describe which shader stages a
corresponding GPUBindGroupEntry for this GPUBindGroupLayoutEntry will be visible to:
The bind group entry will be accessible to vertex shaders.
The bind group entry will be accessible to fragment shaders.
The bind group entry will be accessible to compute shaders.
The binding member of a GPUBindGroupLayoutEntry is determined by which member of the GPUBindGroupLayoutEntry is defined: buffer , sampler , texture , storageTexture , or externalTexture .
Only one may be defined for any given GPUBindGroupLayoutEntry .
Each member has an associated GPUBindingResource type and each binding type has an associated internal usage , given by this table:
Device timeline steps:
- For each entry in entries , if: entry . buffer ?. type is "uniform" and entry . buffer ?. hasDynamicOffset is true Consider 1 maxDynamicUniformBuffersPerPipelineLayout slot to be used. entry . buffer ?. type is "storage" and entry . buffer ?. hasDynamicOffset is true Consider 1 maxDynamicStorageBuffersPerPipelineLayout slot to be used.
For each entry in entries , if:
Consider 1 maxDynamicUniformBuffersPerPipelineLayout slot to be used.
Consider 1 maxDynamicStorageBuffersPerPipelineLayout slot to be used.
- For each shader stage stage in
« VERTEX , FRAGMENT , COMPUTE »: For each entry in entries for which entry . visibility contains stage , if: entry . buffer ?. type is "uniform" Consider 1 maxUniformBuffersPerShaderStage slot to be used. entry . buffer ?. type is "storage" or "read-only-storage" If stage is: VERTEX Consider 1 maxStorageBuffersInVertexStage slot to be used. FRAGMENT Consider 1 maxStorageBuffersInFragmentStage slot to be used. COMPUTE Consider 1 maxStorageBuffersPerShaderStage slot to be used. entry . sampler is provided Consider 1 maxSamplersPerShaderStage slot to be used. entry . texture is provided Consider 1 maxSampledTexturesPerShaderStage slot to be used. entry . storageTexture is provided If stage is: VERTEX Consider 1 maxStorageTexturesInVertexStage slot to be used. FRAGMENT Consider 1 maxStorageTexturesInFragmentStage slot to be used. COMPUTE Consider 1 maxStorageTexturesPerShaderStage slot to be used. entry . externalTexture is provided Consider
4 maxSampledTexturesPerShaderStage slot,
1 maxSamplersPerShaderStage slot, and
1 maxUniformBuffersPerShaderStage slot
to be used. Note: See GPUExternalTexture for an explanation of this behavior.
For each shader stage stage in
« VERTEX , FRAGMENT , COMPUTE »:
- For each entry in entries for which entry . visibility contains stage , if: entry . buffer ?. type is "uniform" Consider 1 maxUniformBuffersPerShaderStage slot to be used. entry . buffer ?. type is "storage" or "read-only-storage" If stage is: VERTEX Consider 1 maxStorageBuffersInVertexStage slot to be used. FRAGMENT Consider 1 maxStorageBuffersInFragmentStage slot to be used. COMPUTE Consider 1 maxStorageBuffersPerShaderStage slot to be used. entry . sampler is provided Consider 1 maxSamplersPerShaderStage slot to be used. entry . texture is provided Consider 1 maxSampledTexturesPerShaderStage slot to be used. entry . storageTexture is provided If stage is: VERTEX Consider 1 maxStorageTexturesInVertexStage slot to be used. FRAGMENT Consider 1 maxStorageTexturesInFragmentStage slot to be used. COMPUTE Consider 1 maxStorageTexturesPerShaderStage slot to be used. entry . externalTexture is provided Consider
4 maxSampledTexturesPerShaderStage slot,
1 maxSamplersPerShaderStage slot, and
1 maxUniformBuffersPerShaderStage slot
to be used. Note: See GPUExternalTexture for an explanation of this behavior.
For each entry in entries for which entry . visibility contains stage , if:
Consider 1 maxUniformBuffersPerShaderStage slot to be used.
If stage is:
Consider 1 maxStorageBuffersInVertexStage slot to be used.
Consider 1 maxStorageBuffersInFragmentStage slot to be used.
Consider 1 maxStorageBuffersPerShaderStage slot to be used.
Consider 1 maxSamplersPerShaderStage slot to be used.
Consider 1 maxSampledTexturesPerShaderStage slot to be used.
If stage is:
Consider 1 maxStorageTexturesInVertexStage slot to be used.
Consider 1 maxStorageTexturesInFragmentStage slot to be used.
Consider 1 maxStorageTexturesPerShaderStage slot to be used.
Consider
4 maxSampledTexturesPerShaderStage slot,
1 maxSamplersPerShaderStage slot, and
1 maxUniformBuffersPerShaderStage slot
to be used.
Note: See GPUExternalTexture for an explanation of this behavior.
GPUBufferBindingLayout dictionaries have the following members:
Indicates the type required for buffers bound to this binding.
Indicates whether this binding requires a dynamic offset.
Indicates the minimum size of a buffer binding used with this bind point.
Bindings are always validated against this size in createBindGroup() .
If this is not 0 , pipeline creation additionally validates that this value ≥ the minimum buffer binding size of the variable.
If this is 0 , it is ignored by pipeline creation, and instead draw/dispatch commands validate that each binding in the GPUBindGroup satisfies the minimum buffer binding size of the variable.
Note: Similar execution-time validation is theoretically possible for other
binding-related fields specified for early validation, like sampleType and format ,
which currently can only be validated in pipeline creation.
However, such execution-time validation could be costly or unnecessarily complex, so it is
available only for minBindingSize which is expected to have the
most ergonomic impact.
GPUSamplerBindingLayout dictionaries have the following members:
Indicates the required type of a sampler bound to this binding.
GPUTextureBindingLayout dictionaries have the following members:
Indicates the type required for texture views bound to this binding.
Indicates the required dimension for texture views bound to
this binding.
Indicates whether or not texture views bound to this binding must be multisampled.
GPUStorageTextureBindingLayout dictionaries have the following members:
The access mode for this binding, indicating readability and writability.
The required format of texture views bound to this binding.
Indicates the required dimension for texture views bound to
this binding.
A GPUBindGroupLayout object has the following device timeline properties :
The map of binding indices pointing to the GPUBindGroupLayoutEntry s,
which this GPUBindGroupLayout describes.
The number of buffer bindings with dynamic offsets in this GPUBindGroupLayout .
The pipeline that created this GPUBindGroupLayout , if it was created as part of a default pipeline layout . If not null , GPUBindGroup s
created with this GPUBindGroupLayout can only be used with the specified GPUPipelineBase .
Creates a GPUBindGroupLayout .
Arguments:
Returns: GPUBindGroupLayout
Content timeline steps:
- For each GPUBindGroupLayoutEntry entry in descriptor . entries : If entry . storageTexture is provided : ? Validate texture format required features for entry . storageTexture . format with this . [[device]] .
For each GPUBindGroupLayoutEntry entry in descriptor . entries :
- If entry . storageTexture is provided : ? Validate texture format required features for entry . storageTexture . format with this . [[device]] .
If entry . storageTexture is provided :
- ? Validate texture format required features for entry . storageTexture . format with this . [[device]] .
? Validate texture format required features for entry . storageTexture . format with this . [[device]] .
- Let layout be ! create a new WebGPU object ( this , GPUBindGroupLayout , descriptor ).
Let layout be ! create a new WebGPU object ( this , GPUBindGroupLayout , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return layout .
Return layout .
- If any of the following conditions are unsatisfied generate a validation error , invalidate layout and return. this must not be lost . Let limits be this . [[device]] . [[limits]] . The binding of each entry in descriptor is unique. The binding of each entry in descriptor must be < limits . maxBindingsPerBindGroup . descriptor . entries must not exceed the binding slot limits of limits . For each GPUBindGroupLayoutEntry entry in descriptor . entries : Exactly one of entry . buffer , entry . sampler , entry . texture , entry . storageTexture , and entry . externalTexture is provided . entry . visibility contains only bits defined in GPUShaderStage . If entry . visibility includes VERTEX : If entry . buffer is provided , entry . buffer . type must be "uniform" or "read-only-storage" . If entry . storageTexture is provided , entry . storageTexture . access must be "read-only" . If entry . texture ?. multisampled is true : entry . texture . viewDimension is "2d" . entry . texture . sampleType is not "float" . If entry . storageTexture is provided : entry . storageTexture . viewDimension is not "cube" or "cube-array" . entry . storageTexture . format must be a format
which can support storage usage for the given entry . storageTexture . access according to the § 26.1.1 Plain color formats table.
If any of the following conditions are unsatisfied generate a validation error , invalidate layout and return.
- this must not be lost .
this must not be lost .
- Let limits be this . [[device]] . [[limits]] .
Let limits be this . [[device]] . [[limits]] .
- The binding of each entry in descriptor is unique.
The binding of each entry in descriptor is unique.
- The binding of each entry in descriptor must be < limits . maxBindingsPerBindGroup .
The binding of each entry in descriptor must be < limits . maxBindingsPerBindGroup .
- descriptor . entries must not exceed the binding slot limits of limits .
descriptor . entries must not exceed the binding slot limits of limits .
- For each GPUBindGroupLayoutEntry entry in descriptor . entries : Exactly one of entry . buffer , entry . sampler , entry . texture , entry . storageTexture , and entry . externalTexture is provided . entry . visibility contains only bits defined in GPUShaderStage . If entry . visibility includes VERTEX : If entry . buffer is provided , entry . buffer . type must be "uniform" or "read-only-storage" . If entry . storageTexture is provided , entry . storageTexture . access must be "read-only" . If entry . texture ?. multisampled is true : entry . texture . viewDimension is "2d" . entry . texture . sampleType is not "float" . If entry . storageTexture is provided : entry . storageTexture . viewDimension is not "cube" or "cube-array" . entry . storageTexture . format must be a format
which can support storage usage for the given entry . storageTexture . access according to the § 26.1.1 Plain color formats table.
For each GPUBindGroupLayoutEntry entry in descriptor . entries :
- Exactly one of entry . buffer , entry . sampler , entry . texture , entry . storageTexture , and entry . externalTexture is provided .
Exactly one of entry . buffer , entry . sampler , entry . texture , entry . storageTexture , and entry . externalTexture is provided .
- entry . visibility contains only bits defined in GPUShaderStage .
entry . visibility contains only bits defined in GPUShaderStage .
- If entry . visibility includes VERTEX : If entry . buffer is provided , entry . buffer . type must be "uniform" or "read-only-storage" . If entry . storageTexture is provided , entry . storageTexture . access must be "read-only" .
If entry . visibility includes VERTEX :
- If entry . buffer is provided , entry . buffer . type must be "uniform" or "read-only-storage" .
If entry . buffer is provided , entry . buffer . type must be "uniform" or "read-only-storage" .
- If entry . storageTexture is provided , entry . storageTexture . access must be "read-only" .
If entry . storageTexture is provided , entry . storageTexture . access must be "read-only" .
- If entry . texture ?. multisampled is true : entry . texture . viewDimension is "2d" . entry . texture . sampleType is not "float" .
If entry . texture ?. multisampled is true :
- entry . texture . viewDimension is "2d" .
entry . texture . viewDimension is "2d" .
- entry . texture . sampleType is not "float" .
entry . texture . sampleType is not "float" .
- If entry . storageTexture is provided : entry . storageTexture . viewDimension is not "cube" or "cube-array" . entry . storageTexture . format must be a format
which can support storage usage for the given entry . storageTexture . access according to the § 26.1.1 Plain color formats table.
If entry . storageTexture is provided :
- entry . storageTexture . viewDimension is not "cube" or "cube-array" .
entry . storageTexture . viewDimension is not "cube" or "cube-array" .
- entry . storageTexture . format must be a format
which can support storage usage for the given entry . storageTexture . access according to the § 26.1.1 Plain color formats table.
entry . storageTexture . format must be a format
which can support storage usage for the given entry . storageTexture . access according to the § 26.1.1 Plain color formats table.
- Set layout . [[descriptor]] to descriptor .
Set layout . [[descriptor]] to descriptor .
- Set layout . [[dynamicOffsetCount]] to the number of
entries in descriptor where buffer is provided and buffer . hasDynamicOffset is true .
Set layout . [[dynamicOffsetCount]] to the number of
entries in descriptor where buffer is provided and buffer . hasDynamicOffset is true .
- Set layout . [[exclusivePipeline]] to null .
Set layout . [[exclusivePipeline]] to null .
- For each GPUBindGroupLayoutEntry entry in descriptor . entries : Insert entry into layout . [[entryMap]] with the key of entry . binding .
For each GPUBindGroupLayoutEntry entry in descriptor . entries :
- Insert entry into layout . [[entryMap]] with the key of entry . binding .
Insert entry into layout . [[entryMap]] with the key of entry . binding .
- a . [[exclusivePipeline]] == b . [[exclusivePipeline]] .
a . [[exclusivePipeline]] == b . [[exclusivePipeline]] .
- for any binding number binding , one of the following conditions is satisfied: it’s missing from both a . [[entryMap]] and b . [[entryMap]] . a . [[entryMap]] [ binding ] == b . [[entryMap]] [ binding ]
for any binding number binding , one of the following conditions is satisfied:
- it’s missing from both a . [[entryMap]] and b . [[entryMap]] .
it’s missing from both a . [[entryMap]] and b . [[entryMap]] .
- a . [[entryMap]] [ binding ] == b . [[entryMap]] [ binding ]
a . [[entryMap]] [ binding ] == b . [[entryMap]] [ binding ]
If bind groups layouts are group-equivalent they can be interchangeably used in all contents.

### 8.2. GPUBindGroup

A GPUBindGroup defines a set of resources to be bound together in a group
and how the resources are used in shader stages.
GPUBindGroup has the following device timeline properties :
The GPUBindGroupLayout associated with this GPUBindGroup .
The set of GPUBindGroupEntry s this GPUBindGroup describes.
The set of buffer and texture subresource s used by this bind group,
associated with lists of the internal usage flags.
- Let result be a new set <( GPUBindGroupLayoutEntry , GPUBufferBinding )>.
Let result be a new set <( GPUBindGroupLayoutEntry , GPUBufferBinding )>.
- Let dynamicOffsetIndex be 0.
Let dynamicOffsetIndex be 0.
- For each GPUBindGroupEntry bindGroupEntry in bindGroup . [[entries]] ,
sorted by bindGroupEntry . binding : Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ]. If bindGroupLayoutEntry . buffer is not provided , continue . Let bound be get as buffer binding ( bindGroupEntry . resource ). If bindGroupLayoutEntry . buffer . hasDynamicOffset : Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ]. Increment dynamicOffsetIndex by 1. Append ( bindGroupLayoutEntry , bound ) to result .
For each GPUBindGroupEntry bindGroupEntry in bindGroup . [[entries]] ,
sorted by bindGroupEntry . binding :
- Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ].
Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ].
- If bindGroupLayoutEntry . buffer is not provided , continue .
If bindGroupLayoutEntry . buffer is not provided , continue .
- Let bound be get as buffer binding ( bindGroupEntry . resource ).
Let bound be get as buffer binding ( bindGroupEntry . resource ).
- If bindGroupLayoutEntry . buffer . hasDynamicOffset : Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ]. Increment dynamicOffsetIndex by 1.
If bindGroupLayoutEntry . buffer . hasDynamicOffset :
- Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ].
Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ].
- Increment dynamicOffsetIndex by 1.
Increment dynamicOffsetIndex by 1.
- Append ( bindGroupLayoutEntry , bound ) to result .
Append ( bindGroupLayoutEntry , bound ) to result .
- Return result .
Return result .
A GPUBindGroup is created via GPUDevice.createBindGroup() .
GPUBindGroupDescriptor dictionaries have the following members:
The GPUBindGroupLayout the entries of this bind group will conform to.
A list of entries describing the resources to expose to the shader for each binding
described by the layout .
A GPUBindGroupEntry describes a single resource to be bound in a GPUBindGroup , and has the
following members:
A unique identifier for a resource binding within the GPUBindGroup , corresponding to a GPUBindGroupLayoutEntry.binding and a @binding attribute in the GPUShaderModule .
[LINK: @binding](https://gpuweb.github.io/gpuweb/wgsl/#attribute-binding)
The resource to bind, which may be a GPUSampler , GPUTexture , GPUTextureView , GPUBuffer , GPUBufferBinding , or GPUExternalTexture .
GPUBindGroupEntry has the following device timeline properties :
Whether or not this binding entry had its buffer size validated at time of creation.
A GPUBufferBinding describes a buffer and optional range to bind as a resource, and has the
following members:
The GPUBuffer to bind.
The offset, in bytes, from the beginning of buffer to the
beginning of the range exposed to the shader by the buffer binding.
The size, in bytes, of the buffer binding.
If not provided , specifies the range starting at offset and ending at the end of buffer .
Creates a GPUBindGroup .
Arguments:
Returns: GPUBindGroup
Content timeline steps:
- Let bindGroup be ! create a new WebGPU object ( this , GPUBindGroup , descriptor ).
Let bindGroup be ! create a new WebGPU object ( this , GPUBindGroup , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return bindGroup .
Return bindGroup .
- Let limits be this . [[device]] . [[limits]] .
Let limits be this . [[device]] . [[limits]] .
- If any of the following conditions are unsatisfied generate a validation error , invalidate bindGroup and return. descriptor . layout is valid to use with this . The number of entries of descriptor . layout is exactly equal to
the number of descriptor . entries . For each GPUBindGroupEntry bindingDescriptor in descriptor . entries : Let resource be bindingDescriptor . resource . There is exactly one GPUBindGroupLayoutEntry layoutBinding in descriptor . layout . entries such that layoutBinding . binding equals to bindingDescriptor . binding . If the defined binding member for layoutBinding is: sampler resource is a GPUSampler . resource is valid to use with this . If layoutBinding . sampler . type is: "filtering" resource . [[isComparison]] is false . "non-filtering" resource . [[isFiltering]] is false . resource . [[isComparison]] is false . "comparison" resource . [[isComparison]] is true . texture resource is either a GPUTexture or a GPUTextureView . resource is valid to use with this . Let textureView be get as texture view ( resource ). Let texture be textureView . [[texture]] . layoutBinding . texture . viewDimension is equal to textureView ’s dimension . layoutBinding . texture . sampleType is compatible with textureView ’s format . textureView . [[descriptor]] . usage includes TEXTURE_BINDING . If layoutBinding . texture . multisampled is true , texture ’s sampleCount > 1 , Otherwise texture ’s sampleCount is 1 . If texture . textureBindingViewDimension is not undefined : Assert this . [[device]] . [[features]] does not contain "core-features-and-limits" . texture . textureBindingViewDimension must be equal to textureView . dimension . storageTexture resource is either a GPUTexture or a GPUTextureView . resource is valid to use with this . Let storageTextureView be get as texture view ( resource ). Let texture be storageTextureView . [[texture]] . layoutBinding . storageTexture . viewDimension is equal to storageTextureView ’s dimension . layoutBinding . storageTexture . format is equal to storageTextureView . [[descriptor]] . format . storageTextureView . [[descriptor]] . usage includes STORAGE_BINDING . storageTextureView . [[descriptor]] . mipLevelCount must be 1. storageTextureView . [[descriptor]] . swizzle must be "rgba" . buffer resource is either a GPUBuffer or a GPUBufferBinding . Let bufferBinding be get as buffer binding ( resource ). bufferBinding . buffer is valid to use with this . The bound part designated by bufferBinding . offset and bufferBinding . size resides inside the buffer and has non-zero size. effective buffer binding size ( bufferBinding ) ≥ layoutBinding . buffer . minBindingSize . If layoutBinding . buffer . type is "uniform" bufferBinding . buffer . usage includes UNIFORM . effective buffer binding size ( bufferBinding ) ≤ limits . maxUniformBufferBindingSize . bufferBinding . offset is a multiple of limits . minUniformBufferOffsetAlignment . "storage" or "read-only-storage" bufferBinding . buffer . usage includes STORAGE . effective buffer binding size ( bufferBinding ) ≤ limits . maxStorageBufferBindingSize . effective buffer binding size ( bufferBinding ) is a multiple of 4. bufferBinding . offset is a multiple of limits . minStorageBufferOffsetAlignment . externalTexture resource is either a GPUExternalTexture , a GPUTexture , or a GPUTextureView . resource is valid to use with this . If resource is a: GPUTexture or GPUTextureView Let view be get as texture view ( resource ). view . [[descriptor]] . usage must include TEXTURE_BINDING . view . [[descriptor]] . dimension must be "2d" . view . [[descriptor]] . mipLevelCount must be 1. view . [[descriptor]] . format must be "rgba8unorm" , "bgra8unorm" , or "rgba16float" . view . [[texture]] . sampleCount must be 1. If this . [[device]] . [[features]] does not contain "core-features-and-limits" : For each GPUBindGroupEntry bindGroupEntry in descriptor . entries : If bindGroupEntry . resource is a GPUTextureView : Let textureView be bindGroupEntry . resource . Let descriptor be textureView . [[descriptor]] . descriptor . baseArrayLayer must be 0 . descriptor . arrayLayerCount must be equal to textureView . [[texture]] . depthOrArrayLayers .
If any of the following conditions are unsatisfied generate a validation error , invalidate bindGroup and return.
- descriptor . layout is valid to use with this .
descriptor . layout is valid to use with this .
- The number of entries of descriptor . layout is exactly equal to
the number of descriptor . entries .
The number of entries of descriptor . layout is exactly equal to
the number of descriptor . entries .
For each GPUBindGroupEntry bindingDescriptor in descriptor . entries :
- Let resource be bindingDescriptor . resource .
Let resource be bindingDescriptor . resource .
- There is exactly one GPUBindGroupLayoutEntry layoutBinding in descriptor . layout . entries such that layoutBinding . binding equals to bindingDescriptor . binding .
There is exactly one GPUBindGroupLayoutEntry layoutBinding in descriptor . layout . entries such that layoutBinding . binding equals to bindingDescriptor . binding .
- If the defined binding member for layoutBinding is: sampler resource is a GPUSampler . resource is valid to use with this . If layoutBinding . sampler . type is: "filtering" resource . [[isComparison]] is false . "non-filtering" resource . [[isFiltering]] is false . resource . [[isComparison]] is false . "comparison" resource . [[isComparison]] is true . texture resource is either a GPUTexture or a GPUTextureView . resource is valid to use with this . Let textureView be get as texture view ( resource ). Let texture be textureView . [[texture]] . layoutBinding . texture . viewDimension is equal to textureView ’s dimension . layoutBinding . texture . sampleType is compatible with textureView ’s format . textureView . [[descriptor]] . usage includes TEXTURE_BINDING . If layoutBinding . texture . multisampled is true , texture ’s sampleCount > 1 , Otherwise texture ’s sampleCount is 1 . If texture . textureBindingViewDimension is not undefined : Assert this . [[device]] . [[features]] does not contain "core-features-and-limits" . texture . textureBindingViewDimension must be equal to textureView . dimension . storageTexture resource is either a GPUTexture or a GPUTextureView . resource is valid to use with this . Let storageTextureView be get as texture view ( resource ). Let texture be storageTextureView . [[texture]] . layoutBinding . storageTexture . viewDimension is equal to storageTextureView ’s dimension . layoutBinding . storageTexture . format is equal to storageTextureView . [[descriptor]] . format . storageTextureView . [[descriptor]] . usage includes STORAGE_BINDING . storageTextureView . [[descriptor]] . mipLevelCount must be 1. storageTextureView . [[descriptor]] . swizzle must be "rgba" . buffer resource is either a GPUBuffer or a GPUBufferBinding . Let bufferBinding be get as buffer binding ( resource ). bufferBinding . buffer is valid to use with this . The bound part designated by bufferBinding . offset and bufferBinding . size resides inside the buffer and has non-zero size. effective buffer binding size ( bufferBinding ) ≥ layoutBinding . buffer . minBindingSize . If layoutBinding . buffer . type is "uniform" bufferBinding . buffer . usage includes UNIFORM . effective buffer binding size ( bufferBinding ) ≤ limits . maxUniformBufferBindingSize . bufferBinding . offset is a multiple of limits . minUniformBufferOffsetAlignment . "storage" or "read-only-storage" bufferBinding . buffer . usage includes STORAGE . effective buffer binding size ( bufferBinding ) ≤ limits . maxStorageBufferBindingSize . effective buffer binding size ( bufferBinding ) is a multiple of 4. bufferBinding . offset is a multiple of limits . minStorageBufferOffsetAlignment . externalTexture resource is either a GPUExternalTexture , a GPUTexture , or a GPUTextureView . resource is valid to use with this . If resource is a: GPUTexture or GPUTextureView Let view be get as texture view ( resource ). view . [[descriptor]] . usage must include TEXTURE_BINDING . view . [[descriptor]] . dimension must be "2d" . view . [[descriptor]] . mipLevelCount must be 1. view . [[descriptor]] . format must be "rgba8unorm" , "bgra8unorm" , or "rgba16float" . view . [[texture]] . sampleCount must be 1.
If the defined binding member for layoutBinding is:
- resource is a GPUSampler .
resource is a GPUSampler .
- resource is valid to use with this .
resource is valid to use with this .
- If layoutBinding . sampler . type is: "filtering" resource . [[isComparison]] is false . "non-filtering" resource . [[isFiltering]] is false . resource . [[isComparison]] is false . "comparison" resource . [[isComparison]] is true .
If layoutBinding . sampler . type is:
resource . [[isComparison]] is false .
resource . [[isFiltering]] is false . resource . [[isComparison]] is false .
resource . [[isComparison]] is true .
- resource is either a GPUTexture or a GPUTextureView .
resource is either a GPUTexture or a GPUTextureView .
- resource is valid to use with this .
resource is valid to use with this .
- Let textureView be get as texture view ( resource ).
Let textureView be get as texture view ( resource ).
- Let texture be textureView . [[texture]] .
Let texture be textureView . [[texture]] .
- layoutBinding . texture . viewDimension is equal to textureView ’s dimension .
layoutBinding . texture . viewDimension is equal to textureView ’s dimension .
- layoutBinding . texture . sampleType is compatible with textureView ’s format .
layoutBinding . texture . sampleType is compatible with textureView ’s format .
- textureView . [[descriptor]] . usage includes TEXTURE_BINDING .
textureView . [[descriptor]] . usage includes TEXTURE_BINDING .
- If layoutBinding . texture . multisampled is true , texture ’s sampleCount > 1 , Otherwise texture ’s sampleCount is 1 .
If layoutBinding . texture . multisampled is true , texture ’s sampleCount > 1 , Otherwise texture ’s sampleCount is 1 .
- If texture . textureBindingViewDimension is not undefined : Assert this . [[device]] . [[features]] does not contain "core-features-and-limits" . texture . textureBindingViewDimension must be equal to textureView . dimension .
- Assert this . [[device]] . [[features]] does not contain "core-features-and-limits" .
Assert this . [[device]] . [[features]] does not contain "core-features-and-limits" .
- texture . textureBindingViewDimension must be equal to textureView . dimension .
texture . textureBindingViewDimension must be equal to textureView . dimension .
- resource is either a GPUTexture or a GPUTextureView .
resource is either a GPUTexture or a GPUTextureView .
- resource is valid to use with this .
resource is valid to use with this .
- Let storageTextureView be get as texture view ( resource ).
Let storageTextureView be get as texture view ( resource ).
- Let texture be storageTextureView . [[texture]] .
Let texture be storageTextureView . [[texture]] .
- layoutBinding . storageTexture . viewDimension is equal to storageTextureView ’s dimension .
layoutBinding . storageTexture . viewDimension is equal to storageTextureView ’s dimension .
- layoutBinding . storageTexture . format is equal to storageTextureView . [[descriptor]] . format .
layoutBinding . storageTexture . format is equal to storageTextureView . [[descriptor]] . format .
- storageTextureView . [[descriptor]] . usage includes STORAGE_BINDING .
storageTextureView . [[descriptor]] . usage includes STORAGE_BINDING .
- storageTextureView . [[descriptor]] . mipLevelCount must be 1.
storageTextureView . [[descriptor]] . mipLevelCount must be 1.
- storageTextureView . [[descriptor]] . swizzle must be "rgba" .
storageTextureView . [[descriptor]] . swizzle must be "rgba" .
- resource is either a GPUBuffer or a GPUBufferBinding .
resource is either a GPUBuffer or a GPUBufferBinding .
- Let bufferBinding be get as buffer binding ( resource ).
Let bufferBinding be get as buffer binding ( resource ).
- bufferBinding . buffer is valid to use with this .
bufferBinding . buffer is valid to use with this .
- The bound part designated by bufferBinding . offset and bufferBinding . size resides inside the buffer and has non-zero size.
The bound part designated by bufferBinding . offset and bufferBinding . size resides inside the buffer and has non-zero size.
- effective buffer binding size ( bufferBinding ) ≥ layoutBinding . buffer . minBindingSize .
effective buffer binding size ( bufferBinding ) ≥ layoutBinding . buffer . minBindingSize .
- If layoutBinding . buffer . type is "uniform" bufferBinding . buffer . usage includes UNIFORM . effective buffer binding size ( bufferBinding ) ≤ limits . maxUniformBufferBindingSize . bufferBinding . offset is a multiple of limits . minUniformBufferOffsetAlignment . "storage" or "read-only-storage" bufferBinding . buffer . usage includes STORAGE . effective buffer binding size ( bufferBinding ) ≤ limits . maxStorageBufferBindingSize . effective buffer binding size ( bufferBinding ) is a multiple of 4. bufferBinding . offset is a multiple of limits . minStorageBufferOffsetAlignment .
If layoutBinding . buffer . type is
- bufferBinding . buffer . usage includes UNIFORM .
bufferBinding . buffer . usage includes UNIFORM .
- effective buffer binding size ( bufferBinding ) ≤ limits . maxUniformBufferBindingSize .
effective buffer binding size ( bufferBinding ) ≤ limits . maxUniformBufferBindingSize .
- bufferBinding . offset is a multiple of limits . minUniformBufferOffsetAlignment .
bufferBinding . offset is a multiple of limits . minUniformBufferOffsetAlignment .
- bufferBinding . buffer . usage includes STORAGE .
bufferBinding . buffer . usage includes STORAGE .
- effective buffer binding size ( bufferBinding ) ≤ limits . maxStorageBufferBindingSize .
effective buffer binding size ( bufferBinding ) ≤ limits . maxStorageBufferBindingSize .
- effective buffer binding size ( bufferBinding ) is a multiple of 4.
effective buffer binding size ( bufferBinding ) is a multiple of 4.
- bufferBinding . offset is a multiple of limits . minStorageBufferOffsetAlignment .
bufferBinding . offset is a multiple of limits . minStorageBufferOffsetAlignment .
- resource is either a GPUExternalTexture , a GPUTexture , or a GPUTextureView .
resource is either a GPUExternalTexture , a GPUTexture , or a GPUTextureView .
- resource is valid to use with this .
resource is valid to use with this .
- If resource is a: GPUTexture or GPUTextureView Let view be get as texture view ( resource ). view . [[descriptor]] . usage must include TEXTURE_BINDING . view . [[descriptor]] . dimension must be "2d" . view . [[descriptor]] . mipLevelCount must be 1. view . [[descriptor]] . format must be "rgba8unorm" , "bgra8unorm" , or "rgba16float" . view . [[texture]] . sampleCount must be 1.
If resource is a:
- Let view be get as texture view ( resource ).
Let view be get as texture view ( resource ).
- view . [[descriptor]] . usage must include TEXTURE_BINDING .
view . [[descriptor]] . usage must include TEXTURE_BINDING .
- view . [[descriptor]] . dimension must be "2d" .
view . [[descriptor]] . dimension must be "2d" .
- view . [[descriptor]] . mipLevelCount must be 1.
view . [[descriptor]] . mipLevelCount must be 1.
- view . [[descriptor]] . format must be "rgba8unorm" , "bgra8unorm" , or "rgba16float" .
view . [[descriptor]] . format must be "rgba8unorm" , "bgra8unorm" , or "rgba16float" .
- view . [[texture]] . sampleCount must be 1.
view . [[texture]] . sampleCount must be 1.
- If this . [[device]] . [[features]] does not contain "core-features-and-limits" : For each GPUBindGroupEntry bindGroupEntry in descriptor . entries : If bindGroupEntry . resource is a GPUTextureView : Let textureView be bindGroupEntry . resource . Let descriptor be textureView . [[descriptor]] . descriptor . baseArrayLayer must be 0 . descriptor . arrayLayerCount must be equal to textureView . [[texture]] . depthOrArrayLayers .
- For each GPUBindGroupEntry bindGroupEntry in descriptor . entries : If bindGroupEntry . resource is a GPUTextureView : Let textureView be bindGroupEntry . resource . Let descriptor be textureView . [[descriptor]] . descriptor . baseArrayLayer must be 0 . descriptor . arrayLayerCount must be equal to textureView . [[texture]] . depthOrArrayLayers .
For each GPUBindGroupEntry bindGroupEntry in descriptor . entries :
- If bindGroupEntry . resource is a GPUTextureView : Let textureView be bindGroupEntry . resource . Let descriptor be textureView . [[descriptor]] . descriptor . baseArrayLayer must be 0 . descriptor . arrayLayerCount must be equal to textureView . [[texture]] . depthOrArrayLayers .
If bindGroupEntry . resource is a GPUTextureView :
- Let textureView be bindGroupEntry . resource .
Let textureView be bindGroupEntry . resource .
- Let descriptor be textureView . [[descriptor]] .
Let descriptor be textureView . [[descriptor]] .
- descriptor . baseArrayLayer must be 0 .
descriptor . baseArrayLayer must be 0 .
- descriptor . arrayLayerCount must be equal to textureView . [[texture]] . depthOrArrayLayers .
descriptor . arrayLayerCount must be equal to textureView . [[texture]] . depthOrArrayLayers .
- Let bindGroup . [[layout]] = descriptor . layout .
Let bindGroup . [[layout]] = descriptor . layout .
- Let bindGroup . [[entries]] = descriptor . entries .
Let bindGroup . [[entries]] = descriptor . entries .
- Let bindGroup . [[usedResources]] = {}.
Let bindGroup . [[usedResources]] = {}.
- For each GPUBindGroupEntry bindingDescriptor in descriptor . entries : Let internalUsage be the binding usage for layoutBinding . Each subresource seen by resource is added to [[usedResources]] as internalUsage . Let bindingDescriptor . [[prevalidatedSize]] be false if the defined binding member for layoutBinding is buffer and layoutBinding . buffer . minBindingSize is 0 , and true otherwise.
For each GPUBindGroupEntry bindingDescriptor in descriptor . entries :
- Let internalUsage be the binding usage for layoutBinding .
Let internalUsage be the binding usage for layoutBinding .
- Each subresource seen by resource is added to [[usedResources]] as internalUsage .
Each subresource seen by resource is added to [[usedResources]] as internalUsage .
- Let bindingDescriptor . [[prevalidatedSize]] be false if the defined binding member for layoutBinding is buffer and layoutBinding . buffer . minBindingSize is 0 , and true otherwise.
Let bindingDescriptor . [[prevalidatedSize]] be false if the defined binding member for layoutBinding is buffer and layoutBinding . buffer . minBindingSize is 0 , and true otherwise.
Arguments:
- GPUBindingResource resource
GPUBindingResource resource
Returns: GPUTextureView
- Assert resource is either a GPUTexture or a GPUTextureView .
Assert resource is either a GPUTexture or a GPUTextureView .
- If resource is a: GPUTexture Return resource . createView() . GPUTextureView Return resource .
If resource is a:
- Return resource . createView() .
Return resource . createView() .
- Return resource .
Return resource .
Arguments:
- GPUBindingResource resource
GPUBindingResource resource
Returns: GPUBufferBinding
- Assert resource is either a GPUBuffer or a GPUBufferBinding .
Assert resource is either a GPUBuffer or a GPUBufferBinding .
- If resource is a: GPUBuffer Let bufferBinding a new GPUBufferBinding . Set bufferBinding . buffer to resource . Return bufferBinding . GPUBufferBinding Return resource .
If resource is a:
- Let bufferBinding a new GPUBufferBinding .
Let bufferBinding a new GPUBufferBinding .
- Set bufferBinding . buffer to resource .
Set bufferBinding . buffer to resource .
- Return bufferBinding .
Return bufferBinding .
- Return resource .
Return resource .
Arguments:
- GPUBufferBinding binding
GPUBufferBinding binding
Returns: GPUSize64
- If binding . size is not provided : Return max(0, binding . buffer . size - binding . offset );
If binding . size is not provided :
- Return max(0, binding . buffer . size - binding . offset );
Return max(0, binding . buffer . size - binding . offset );
- Return binding . size .
Return binding . size .
- a . buffer == b . buffer
a . buffer == b . buffer
- The range formed by a . offset and a . size intersects
the range formed by b . offset and b . size ,
where if a size is unspecified ,
the range goes to the end of the buffer.
The range formed by a . offset and a . size intersects
the range formed by b . offset and b . size ,
where if a size is unspecified ,
the range goes to the end of the buffer.
Note: When doing this calculation, any dynamic offsets have already been applied to the ranges.

### 8.3. GPUPipelineLayout

A GPUPipelineLayout defines the mapping between resources of all GPUBindGroup objects set up during command encoding in setBindGroup() , and the shaders of the pipeline set by GPURenderCommandsMixin.setPipeline or GPUComputePassEncoder.setPipeline .
The full binding address of a resource can be defined as a trio of:
- shader stage mask, to which the resource is visible
shader stage mask, to which the resource is visible
- bind group index
bind group index
- binding number
binding number
The components of this address can also be seen as the binding space of a pipeline. A GPUBindGroup (with the corresponding GPUBindGroupLayout ) covers that space for a fixed bind group index. The contained bindings need to be a superset of the resources used by the shader at this bind group index.
GPUPipelineLayout has the following device timeline properties :
The GPUBindGroupLayout objects provided at creation in GPUPipelineLayoutDescriptor.bindGroupLayouts .
Note: using the same GPUPipelineLayout for many GPURenderPipeline or GPUComputePipeline pipelines guarantees that the user agent doesn’t need to rebind any resources internally when there is a switch between these pipelines.
- setBindGroup (0, ...)
setBindGroup (0, ...)
- setBindGroup (1, ...)
setBindGroup (1, ...)
- setBindGroup (2, ...)
setBindGroup (2, ...)
- setPipeline (X)
setPipeline (X)
- dispatchWorkgroups ()
dispatchWorkgroups ()
- setBindGroup (1, ...)
setBindGroup (1, ...)
- setPipeline (Y)
setPipeline (Y)
- dispatchWorkgroups ()
dispatchWorkgroups ()
In this scenario, the user agent would have to re-bind the group slot 2 for the second dispatch, even though neither the GPUBindGroupLayout at index 2 of GPUPipelineLayout.bindGroupLayouts , or the GPUBindGroup at slot 2, change.
Note: the expected usage of the GPUPipelineLayout is placing the most common and the least frequently changing bind groups at the "bottom" of the layout, meaning lower bind group slot numbers, like 0 or 1. The more frequently a bind group needs to change between draw calls, the higher its index should be. This general guideline allows the user agent to minimize state changes between draw calls, and consequently lower the CPU overhead.
A GPUPipelineLayout is created via GPUDevice.createPipelineLayout() .
GPUPipelineLayoutDescriptor dictionaries define all the GPUBindGroupLayout s used by a
pipeline, and have the following members:
A list of optional GPUBindGroupLayout s the pipeline will use. Each element corresponds
to a @group attribute in the GPUShaderModule , with the N th element corresponding
with @group(N) .
[LINK: @group](https://gpuweb.github.io/gpuweb/wgsl/#attribute-group)
Creates a GPUPipelineLayout .
Arguments:
Returns: GPUPipelineLayout
Content timeline steps:
- Let pl be ! create a new WebGPU object ( this , GPUPipelineLayout , descriptor ).
Let pl be ! create a new WebGPU object ( this , GPUPipelineLayout , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return pl .
Return pl .
- Let limits be this . [[device]] . [[limits]] .
Let limits be this . [[device]] . [[limits]] .
- Let bindGroupLayouts be a list of null GPUBindGroupLayout s with size equal to limits . maxBindGroups .
Let bindGroupLayouts be a list of null GPUBindGroupLayout s with size equal to limits . maxBindGroups .
- For each bindGroupLayout at index i in descriptor . bindGroupLayouts : If bindGroupLayout is not null and bindGroupLayout . [[descriptor]] . entries is not empty : Set bindGroupLayouts [ i ] to bindGroupLayout .
For each bindGroupLayout at index i in descriptor . bindGroupLayouts :
- If bindGroupLayout is not null and bindGroupLayout . [[descriptor]] . entries is not empty : Set bindGroupLayouts [ i ] to bindGroupLayout .
If bindGroupLayout is not null and bindGroupLayout . [[descriptor]] . entries is not empty :
- Set bindGroupLayouts [ i ] to bindGroupLayout .
Set bindGroupLayouts [ i ] to bindGroupLayout .
- Let allEntries be the result of concatenating bgl . [[descriptor]] . entries for all non- null bgl in bindGroupLayouts .
Let allEntries be the result of concatenating bgl . [[descriptor]] . entries for all non- null bgl in bindGroupLayouts .
- If any of the following conditions are unsatisfied generate a validation error , invalidate pl and return. Every non- null GPUBindGroupLayout in bindGroupLayouts must be valid to use with this and have a [[exclusivePipeline]] of null . The size of descriptor . bindGroupLayouts must be ≤ limits . maxBindGroups . allEntries must not exceed the binding slot limits of limits .
If any of the following conditions are unsatisfied generate a validation error , invalidate pl and return.
- Every non- null GPUBindGroupLayout in bindGroupLayouts must be valid to use with this and have a [[exclusivePipeline]] of null .
Every non- null GPUBindGroupLayout in bindGroupLayouts must be valid to use with this and have a [[exclusivePipeline]] of null .
- The size of descriptor . bindGroupLayouts must be ≤ limits . maxBindGroups .
The size of descriptor . bindGroupLayouts must be ≤ limits . maxBindGroups .
- allEntries must not exceed the binding slot limits of limits .
allEntries must not exceed the binding slot limits of limits .
- Set the pl . [[bindGroupLayouts]] to bindGroupLayouts .
Set the pl . [[bindGroupLayouts]] to bindGroupLayouts .
Note: two GPUPipelineLayout objects are considered equivalent for any usage
if their internal [[bindGroupLayouts]] sequences contain GPUBindGroupLayout objects that are group-equivalent .

### 8.4. Example

## 9. Shader Modules

### 9.1. GPUShaderModule

GPUShaderModule is a reference to an internal shader module object.
The WGSL source code for the shader
module.
[LINK: WGSL](https://gpuweb.github.io/gpuweb/wgsl/)
A list of GPUShaderModuleCompilationHint s.
Any hint provided by an application should contain information about one entry point of
a pipeline that will eventually be created from the entry point.
Implementations should use any information present in the GPUShaderModuleCompilationHint to perform as much compilation as is possible within createShaderModule() .
Aside from type-checking, these hints are not validated in any way.
Because a single shader module can hold multiple entry points, and multiple pipelines
    can be created from a single shader module, it can be more performant for an
    implementation to do as much compilation as possible once in createShaderModule() rather than multiple times in the multiple calls to createComputePipeline() or createRenderPipeline() .
Hints are only applied to the entry points they explicitly name.
    Unlike GPUProgrammableStage.entryPoint ,
    there is no default, even if only one entry point is present in the module.
Note: Hints are not validated in an observable way, but user agents may surface identifiable
errors (like unknown entry point names or incompatible pipeline layouts) to developers,
for example in the browser developer console.
Creates a GPUShaderModule .
Arguments:
Returns: GPUShaderModule
Content timeline steps:
- Let sm be ! create a new WebGPU object ( this , GPUShaderModule , descriptor ).
Let sm be ! create a new WebGPU object ( this , GPUShaderModule , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return sm .
Return sm .
- Let error be any error that results from shader module creation with the
WGSL source descriptor . code , or null if no
errors occured.
Let error be any error that results from shader module creation with the
WGSL source descriptor . code , or null if no
errors occured.
[LINK: shader module creation](https://gpuweb.github.io/gpuweb/wgsl/#shader-module-creation)
- If any of the following requirements are unmet, generate a validation error , invalidate sm , and return. this must not be lost . error must not be a shader-creation program error . For each enable extension in descriptor . code ,
the corresponding GPUFeatureName must be enabled
(see the Feature Index ). Note: Uncategorized errors cannot arise from shader module creation.
Implementations which detect such errors during shader module creation
must behave as if the shader module is valid, and defer surfacing the
error until pipeline creation.
If any of the following requirements are unmet, generate a validation error , invalidate sm , and return.
- this must not be lost .
this must not be lost .
- error must not be a shader-creation program error .
error must not be a shader-creation program error .
[LINK: shader-creation](https://gpuweb.github.io/gpuweb/wgsl/#shader-creation-error)
[LINK: program error](https://gpuweb.github.io/gpuweb/wgsl/#program-error)
- For each enable extension in descriptor . code ,
the corresponding GPUFeatureName must be enabled
(see the Feature Index ).
For each enable extension in descriptor . code ,
the corresponding GPUFeatureName must be enabled
(see the Feature Index ).
Note: Uncategorized errors cannot arise from shader module creation.
Implementations which detect such errors during shader module creation
must behave as if the shader module is valid, and defer surfacing the
error until pipeline creation.
[LINK: Uncategorized errors](https://gpuweb.github.io/gpuweb/wgsl/#uncategorized-error)
As shader compilation errors should be rare in production applications, user agents
            could choose to surface them to developers regardless of error handling ( GPU error scopes or uncapturederror event handlers), e.g. as an expandable warning.
            If not, they should provide and document another way for developers to access
            human-readable error details, for example by adding a checkbox to show errors
            unconditionally, or by showing human-readable details when logging a GPUCompilationInfo object to the console.
Shader module compilation hints are optional, additional information indicating how a given GPUShaderModule entry point is intended to be used in the future. For some implementations this
information may aid in compiling the shader module earlier, potentially increasing performance.
A GPUPipelineLayout that the GPUShaderModule may be used with in a future createComputePipeline() or createRenderPipeline() call.
If set to "auto" the layout will be the default pipeline layout for the entry point associated with this hint will be used.
If an application is unable to provide hint information at the time of calling createShaderModule() , it should usually not delay calling createShaderModule() , but instead just omit the unknown information from
    the compilationHints sequence or the individual members of GPUShaderModuleCompilationHint . Omitting this information
    may cause compilation to be deferred to createComputePipeline() / createRenderPipeline() .
If an author is not confident that the hint information passed to createShaderModule() will match the information later passed to createComputePipeline() / createRenderPipeline() with that same module, they should avoid passing that
    information to createShaderModule() , as passing mismatched information to createShaderModule() may cause unnecessary compilations to occur.
A GPUCompilationMessage is an informational, warning, or error message generated by the GPUShaderModule compiler. The messages are intended to be human readable to help developers
diagnose issues with their shader code . Each message may correspond to
a single point or range of the shader source, or may be unassociated with any specific part of the code.
GPUCompilationMessage has the following attributes:
The human-readable, localizable text for this compilation message.
Note: The message should follow the best practices for language and direction information . This includes making use of any future standards which may
emerge regarding the reporting of string language and direction metadata.
[LINK: best practices for language and direction information](https://w3c.github.io/string-meta/#bp_and-reco)
Editorial note: At the time of this writing, no language/direction recommendation is available that provides
compatibility and consistency with legacy APIs, but when there is, adopt it formally.
The severity level of the message.
If the type is "error" , it
corresponds to a shader-creation error .
[LINK: shader-creation error](https://gpuweb.github.io/gpuweb/wgsl/#shader-creation-error)
The line number in the shader code the message corresponds to. Value is one-based, such that a lineNum of 1 indicates the first line of the shader code . Lines are
delimited by line breaks .
[LINK: line breaks](https://gpuweb.github.io/gpuweb/wgsl/#line-break)
If the message corresponds to a substring this points to
the line on which the substring begins. Must be 0 if the message does not correspond to any specific point in the shader code .
The offset, in UTF-16 code units, from the beginning of line lineNum of the shader code to the point or beginning of the substring
that the message corresponds to. Value is one-based, such that a linePos of 1 indicates the first code unit of the line.
If message corresponds to a substring this points to the
first UTF-16 code unit of the substring. Must be 0 if the message does not correspond to any specific point in the shader code .
The offset from the beginning of the shader code in UTF-16
code units to the point or beginning of the substring that message corresponds to. Must reference the same position as lineNum and linePos . Must be 0 if the message does not correspond to any specific point in the shader code .
The number of UTF-16 code units in the substring that message corresponds to. If the message does not correspond with a substring then length must be 0.
Note: GPUCompilationMessage . lineNum and GPUCompilationMessage . linePos are one-based since the most common use
for them is expected to be printing human readable messages that can be correlated with the line and
column numbers shown in many text editors.
Note: GPUCompilationMessage . offset and GPUCompilationMessage . length are appropriate to pass to substr() in order to retrieve the substring of the shader code the message corresponds to.
Returns any messages generated during the GPUShaderModule ’s compilation.
The locations, order, and contents of messages are implementation-defined .
In particular, messages aren’t necessarily ordered by lineNum .
Returns: Promise < GPUCompilationInfo >
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- Let promise be a new promise .
Let promise be a new promise .
- Issue the synchronization steps on the Device timeline of this .
Issue the synchronization steps on the Device timeline of this .
- Return promise .
Return promise .
- Let event occur upon the (successful or unsuccessful) completion of shader module creation for this .
Let event occur upon the (successful or unsuccessful) completion of shader module creation for this .
[LINK: shader module creation](https://gpuweb.github.io/gpuweb/wgsl/#shader-module-creation)
- Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on contentTimeline .
Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on contentTimeline .
- Let info be a new GPUCompilationInfo .
Let info be a new GPUCompilationInfo .
- Let messages be a list of any errors, warnings, or informational messages
generated during shader module creation for this , or the empty list [] if the device was lost.
Let messages be a list of any errors, warnings, or informational messages
generated during shader module creation for this , or the empty list [] if the device was lost.
[LINK: shader module creation](https://gpuweb.github.io/gpuweb/wgsl/#shader-module-creation)
- For each message in messages : Let m be a new GPUCompilationMessage . Set m . message to be the text of message . If message is a shader-creation error : Set m . type to "error" If message is a warning: Set m . type to "warning" Otherwise: Set m . type to "info" If message is associated with a specific substring or position
within the shader code : Set m . lineNum to the one-based number
of the first line that the message refers to. Set m . linePos to the one-based number
of the first UTF-16 code units on m . lineNum that the message refers to, or 1 if the message refers to
the entire line. Set m . offset to the number of UTF-16
code units from the beginning of the shader to beginning of the
substring or position that message refers to. Set m . length the length of the
substring in UTF-16 code units that message refers to, or 0
if message refers to a position Otherwise: Set m . lineNum to 0 . Set m . linePos to 0 . Set m . offset to 0 . Set m . length to 0 . Append m to info . messages .
For each message in messages :
- Let m be a new GPUCompilationMessage .
Let m be a new GPUCompilationMessage .
- Set m . message to be the text of message .
Set m . message to be the text of message .
- If message is a shader-creation error : Set m . type to "error" If message is a warning: Set m . type to "warning" Otherwise: Set m . type to "info"
[LINK: shader-creation error](https://gpuweb.github.io/gpuweb/wgsl/#shader-creation-error)
Set m . type to "error"
Set m . type to "warning"
Set m . type to "info"
- If message is associated with a specific substring or position
within the shader code : Set m . lineNum to the one-based number
of the first line that the message refers to. Set m . linePos to the one-based number
of the first UTF-16 code units on m . lineNum that the message refers to, or 1 if the message refers to
the entire line. Set m . offset to the number of UTF-16
code units from the beginning of the shader to beginning of the
substring or position that message refers to. Set m . length the length of the
substring in UTF-16 code units that message refers to, or 0
if message refers to a position Otherwise: Set m . lineNum to 0 . Set m . linePos to 0 . Set m . offset to 0 . Set m . length to 0 .
- Set m . lineNum to the one-based number
of the first line that the message refers to.
Set m . lineNum to the one-based number
of the first line that the message refers to.
- Set m . linePos to the one-based number
of the first UTF-16 code units on m . lineNum that the message refers to, or 1 if the message refers to
the entire line.
Set m . linePos to the one-based number
of the first UTF-16 code units on m . lineNum that the message refers to, or 1 if the message refers to
the entire line.
- Set m . offset to the number of UTF-16
code units from the beginning of the shader to beginning of the
substring or position that message refers to.
Set m . offset to the number of UTF-16
code units from the beginning of the shader to beginning of the
substring or position that message refers to.
- Set m . length the length of the
substring in UTF-16 code units that message refers to, or 0
if message refers to a position
Set m . length the length of the
substring in UTF-16 code units that message refers to, or 0
if message refers to a position
- Set m . lineNum to 0 .
Set m . lineNum to 0 .
- Set m . linePos to 0 .
Set m . linePos to 0 .
- Set m . offset to 0 .
Set m . offset to 0 .
- Set m . length to 0 .
Set m . length to 0 .
- Append m to info . messages .
Append m to info . messages .
- Resolve promise with info .
Resolve promise with info .

## 10. Pipelines

A pipeline , be it GPUComputePipeline or GPURenderPipeline ,
represents the complete function done by a combination of the GPU hardware, the driver,
and the user agent, that process the input data in the shape of bindings and vertex buffers,
and produces some output, like the colors in the output render targets.
Structurally, the pipeline consists of a sequence of programmable stages (shaders)
and fixed-function states, such as the blending modes.
Note: Internally, depending on the target platform,
the driver may convert some of the fixed-function states into shader code,
and link it together with the shaders provided by the user.
This linking is one of the reason the object is created as a whole.
This combination state is created as a single object
(a GPUComputePipeline or GPURenderPipeline )
and switched using one command
( GPUComputePassEncoder . setPipeline() or GPURenderCommandsMixin . setPipeline() respectively).
There are two ways to create pipelines:
createComputePipeline() and createRenderPipeline() return a pipeline object which can be used immediately in a pass encoder.
When this fails, the pipeline object will be invalid and the call will generate either a validation error or an internal error .
Note: A handle object is returned immediately, but actual pipeline creation is not synchronous.
If pipeline creation takes a long time, this can incur a stall in the device timeline at some point between the creation call and execution of the submit() in which it is first used.
The point is unspecified, but most likely to be one of: at creation, at the first usage of the
pipeline in setPipeline() , at the corresponding finish() of that GPUCommandEncoder or GPURenderBundleEncoder , or at submit() of that GPUCommandBuffer .
createComputePipelineAsync() and createRenderPipelineAsync() return a Promise which resolves to a pipeline object when creation of the pipeline has
completed.
When this fails, the Promise rejects with a GPUPipelineError .
GPUPipelineError describes a pipeline creation failure.
GPUPipelineError constructor:
Content timeline steps:
- Set this . name to "GPUPipelineError" .
Set this . name to "GPUPipelineError" .
- Set this . message to message .
Set this . message to message .
- Set this . reason to options . reason .
Set this . reason to options . reason .
GPUPipelineError has the following attributes:
A read-only slot-backed attribute exposing the type of error encountered in pipeline creation
as a GPUPipelineErrorReason :
- "validation" : A validation error .
"validation" : A validation error .
- "internal" : An internal error .
"internal" : An internal error .
GPUPipelineError objects are serializable objects .
- Run the DOMException serialization steps given value and serialized .
Run the DOMException serialization steps given value and serialized .
- Run the DOMException deserialization steps given value and serialized .
Run the DOMException deserialization steps given value and serialized .

### 10.1. Base pipelines

The GPUPipelineLayout for this pipeline, or "auto" to generate
the pipeline layout automatically.
Note: If "auto" is used the pipeline cannot share GPUBindGroup s
with any other pipelines.
GPUPipelineBase has the following device timeline properties :
The definition of the layout of resources which can be used with this .
GPUPipelineBase has the following methods:
Gets a GPUBindGroupLayout that is compatible with the GPUPipelineBase ’s GPUBindGroupLayout at index .
Arguments:
Returns: GPUBindGroupLayout
Content timeline steps:
- Let layout be a new GPUBindGroupLayout object.
Let layout be a new GPUBindGroupLayout object.
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return layout .
Return layout .
- Let limits be this . [[device]] . [[limits]] .
Let limits be this . [[device]] . [[limits]] .
- If any of the following conditions are unsatisfied generate a validation error , invalidate layout and return. this must be valid . index < limits . maxBindGroups .
If any of the following conditions are unsatisfied generate a validation error , invalidate layout and return.
- this must be valid .
this must be valid .
- index < limits . maxBindGroups .
index < limits . maxBindGroups .
- Initialize layout so it is a copy of this . [[layout]] . [[bindGroupLayouts]] [ index ]. Note: GPUBindGroupLayout is only ever used by-value, not by-reference,
so this is equivalent to returning the same internal object with a new WebGPU interface .
A new GPUBindGroupLayout WebGPU interface is returned each time to avoid a round-trip
between the Content timeline and the Device timeline .
Initialize layout so it is a copy of this . [[layout]] . [[bindGroupLayouts]] [ index ].
Note: GPUBindGroupLayout is only ever used by-value, not by-reference,
so this is equivalent to returning the same internal object with a new WebGPU interface .
A new GPUBindGroupLayout WebGPU interface is returned each time to avoid a round-trip
between the Content timeline and the Device timeline .
A GPUPipelineBase object that was created with a layout set to "auto" has a default layout created and used instead.
Note: Default layouts are provided as a convenience for simple pipelines, but use of explicit layouts
is recommended in most cases. Bind groups created from default layouts cannot be used with other
pipelines, and the structure of the default layout may change when altering shaders, causing
unexpected bind group creation errors.
To create a default pipeline layout for GPUPipelineBase pipeline ,
run the following device timeline steps:
- Let groupCount be 0.
Let groupCount be 0.
- Let groupDescs be a sequence of device . [[limits]] . maxBindGroups new GPUBindGroupLayoutDescriptor objects.
Let groupDescs be a sequence of device . [[limits]] . maxBindGroups new GPUBindGroupLayoutDescriptor objects.
- For each groupDesc in groupDescs : Set groupDesc . entries to an empty sequence .
For each groupDesc in groupDescs :
- Set groupDesc . entries to an empty sequence .
Set groupDesc . entries to an empty sequence .
- For each GPUProgrammableStage stageDesc in the descriptor used to create pipeline : Let shaderStage be the GPUShaderStageFlags for the shader stage
at which stageDesc is used in pipeline . Let entryPoint be get the entry point ( shaderStage , stageDesc ). Assert entryPoint is not null . For each resource resource statically used by entryPoint : Let group be resource ’s "group" decoration. Let binding be resource ’s "binding" decoration. Let entry be a new GPUBindGroupLayoutEntry . Set entry . binding to binding . Set entry . visibility to shaderStage . If resource is for a sampler binding: Let samplerLayout be a new GPUSamplerBindingLayout . Set entry . sampler to samplerLayout . If resource is for a comparison sampler binding: Let samplerLayout be a new GPUSamplerBindingLayout . Set samplerLayout . type to "comparison" . Set entry . sampler to samplerLayout . If resource is for a buffer binding: Let bufferLayout be a new GPUBufferBindingLayout . Set bufferLayout . minBindingSize to resource ’s minimum buffer binding size . If resource is for a read-only storage buffer: Set bufferLayout . type to "read-only-storage" . If resource is for a storage buffer: Set bufferLayout . type to "storage" . Set entry . buffer to bufferLayout . If resource is for a sampled texture binding: Let textureLayout be a new GPUTextureBindingLayout . If resource is a depth texture binding: Set textureLayout . sampleType to "depth" Otherwise, if the sampled type of resource is: f32 and there exists a static use of resource by stageDesc in a texture builtin function call that also uses a sampler Set textureLayout . sampleType to "float" f32 otherwise Set textureLayout . sampleType to "unfilterable-float" i32 Set textureLayout . sampleType to "sint" u32 Set textureLayout . sampleType to "uint" Set textureLayout . viewDimension to resource ’s dimension. If resource is for a multisampled texture: Set textureLayout . multisampled to true . Set entry . texture to textureLayout . If resource is for a storage texture binding: Let storageTextureLayout be a new GPUStorageTextureBindingLayout . Set storageTextureLayout . format to resource ’s format. Set storageTextureLayout . viewDimension to resource ’s dimension. If the access mode is: read Set textureLayout . access to "read-only" . write Set textureLayout . access to "write-only" . read_write Set textureLayout . access to "read-write" . Set entry . storageTexture to storageTextureLayout . Set groupCount to max( groupCount , group + 1). If groupDescs [ group ] has an entry previousEntry with binding equal to binding : If entry has different visibility than previousEntry : Add the bits set in entry . visibility into previousEntry . visibility If resource is for a buffer binding and entry has greater buffer . minBindingSize than previousEntry : Set previousEntry . buffer . minBindingSize to entry . buffer . minBindingSize . If resource is a sampled texture binding and entry has different texture . sampleType than previousEntry and both entry and previousEntry have texture . sampleType of either "float" or "unfilterable-float" : Set previousEntry . texture . sampleType to "float" . If any other property is unequal between entry and previousEntry : Return null (which will cause the creation of the pipeline to fail). If resource is a storage texture binding, entry . storageTexture . access is "read-write" , previousEntry . storageTexture . access is "write-only" , and previousEntry . storageTexture . format is compatible with STORAGE_BINDING and "read-write" according to the § 26.1.1 Plain color formats table: Set previousEntry . storageTexture . access to "read-write" . Otherwise: Append entry to groupDescs [ group ].
For each GPUProgrammableStage stageDesc in the descriptor used to create pipeline :
- Let shaderStage be the GPUShaderStageFlags for the shader stage
at which stageDesc is used in pipeline .
Let shaderStage be the GPUShaderStageFlags for the shader stage
at which stageDesc is used in pipeline .
- Let entryPoint be get the entry point ( shaderStage , stageDesc ). Assert entryPoint is not null .
Let entryPoint be get the entry point ( shaderStage , stageDesc ). Assert entryPoint is not null .
- For each resource resource statically used by entryPoint : Let group be resource ’s "group" decoration. Let binding be resource ’s "binding" decoration. Let entry be a new GPUBindGroupLayoutEntry . Set entry . binding to binding . Set entry . visibility to shaderStage . If resource is for a sampler binding: Let samplerLayout be a new GPUSamplerBindingLayout . Set entry . sampler to samplerLayout . If resource is for a comparison sampler binding: Let samplerLayout be a new GPUSamplerBindingLayout . Set samplerLayout . type to "comparison" . Set entry . sampler to samplerLayout . If resource is for a buffer binding: Let bufferLayout be a new GPUBufferBindingLayout . Set bufferLayout . minBindingSize to resource ’s minimum buffer binding size . If resource is for a read-only storage buffer: Set bufferLayout . type to "read-only-storage" . If resource is for a storage buffer: Set bufferLayout . type to "storage" . Set entry . buffer to bufferLayout . If resource is for a sampled texture binding: Let textureLayout be a new GPUTextureBindingLayout . If resource is a depth texture binding: Set textureLayout . sampleType to "depth" Otherwise, if the sampled type of resource is: f32 and there exists a static use of resource by stageDesc in a texture builtin function call that also uses a sampler Set textureLayout . sampleType to "float" f32 otherwise Set textureLayout . sampleType to "unfilterable-float" i32 Set textureLayout . sampleType to "sint" u32 Set textureLayout . sampleType to "uint" Set textureLayout . viewDimension to resource ’s dimension. If resource is for a multisampled texture: Set textureLayout . multisampled to true . Set entry . texture to textureLayout . If resource is for a storage texture binding: Let storageTextureLayout be a new GPUStorageTextureBindingLayout . Set storageTextureLayout . format to resource ’s format. Set storageTextureLayout . viewDimension to resource ’s dimension. If the access mode is: read Set textureLayout . access to "read-only" . write Set textureLayout . access to "write-only" . read_write Set textureLayout . access to "read-write" . Set entry . storageTexture to storageTextureLayout . Set groupCount to max( groupCount , group + 1). If groupDescs [ group ] has an entry previousEntry with binding equal to binding : If entry has different visibility than previousEntry : Add the bits set in entry . visibility into previousEntry . visibility If resource is for a buffer binding and entry has greater buffer . minBindingSize than previousEntry : Set previousEntry . buffer . minBindingSize to entry . buffer . minBindingSize . If resource is a sampled texture binding and entry has different texture . sampleType than previousEntry and both entry and previousEntry have texture . sampleType of either "float" or "unfilterable-float" : Set previousEntry . texture . sampleType to "float" . If any other property is unequal between entry and previousEntry : Return null (which will cause the creation of the pipeline to fail). If resource is a storage texture binding, entry . storageTexture . access is "read-write" , previousEntry . storageTexture . access is "write-only" , and previousEntry . storageTexture . format is compatible with STORAGE_BINDING and "read-write" according to the § 26.1.1 Plain color formats table: Set previousEntry . storageTexture . access to "read-write" . Otherwise: Append entry to groupDescs [ group ].
For each resource resource statically used by entryPoint :
- Let group be resource ’s "group" decoration.
Let group be resource ’s "group" decoration.
- Let binding be resource ’s "binding" decoration.
Let binding be resource ’s "binding" decoration.
- Let entry be a new GPUBindGroupLayoutEntry .
Let entry be a new GPUBindGroupLayoutEntry .
- Set entry . binding to binding .
Set entry . binding to binding .
- Set entry . visibility to shaderStage .
Set entry . visibility to shaderStage .
- If resource is for a sampler binding: Let samplerLayout be a new GPUSamplerBindingLayout . Set entry . sampler to samplerLayout .
If resource is for a sampler binding:
- Let samplerLayout be a new GPUSamplerBindingLayout .
Let samplerLayout be a new GPUSamplerBindingLayout .
- Set entry . sampler to samplerLayout .
Set entry . sampler to samplerLayout .
- If resource is for a comparison sampler binding: Let samplerLayout be a new GPUSamplerBindingLayout . Set samplerLayout . type to "comparison" . Set entry . sampler to samplerLayout .
If resource is for a comparison sampler binding:
- Let samplerLayout be a new GPUSamplerBindingLayout .
Let samplerLayout be a new GPUSamplerBindingLayout .
- Set samplerLayout . type to "comparison" .
Set samplerLayout . type to "comparison" .
- Set entry . sampler to samplerLayout .
Set entry . sampler to samplerLayout .
- If resource is for a buffer binding: Let bufferLayout be a new GPUBufferBindingLayout . Set bufferLayout . minBindingSize to resource ’s minimum buffer binding size . If resource is for a read-only storage buffer: Set bufferLayout . type to "read-only-storage" . If resource is for a storage buffer: Set bufferLayout . type to "storage" . Set entry . buffer to bufferLayout .
If resource is for a buffer binding:
- Let bufferLayout be a new GPUBufferBindingLayout .
Let bufferLayout be a new GPUBufferBindingLayout .
- Set bufferLayout . minBindingSize to resource ’s minimum buffer binding size .
Set bufferLayout . minBindingSize to resource ’s minimum buffer binding size .
- If resource is for a read-only storage buffer: Set bufferLayout . type to "read-only-storage" .
If resource is for a read-only storage buffer:
- Set bufferLayout . type to "read-only-storage" .
Set bufferLayout . type to "read-only-storage" .
- If resource is for a storage buffer: Set bufferLayout . type to "storage" .
If resource is for a storage buffer:
- Set bufferLayout . type to "storage" .
Set bufferLayout . type to "storage" .
- Set entry . buffer to bufferLayout .
Set entry . buffer to bufferLayout .
- If resource is for a sampled texture binding: Let textureLayout be a new GPUTextureBindingLayout . If resource is a depth texture binding: Set textureLayout . sampleType to "depth" Otherwise, if the sampled type of resource is: f32 and there exists a static use of resource by stageDesc in a texture builtin function call that also uses a sampler Set textureLayout . sampleType to "float" f32 otherwise Set textureLayout . sampleType to "unfilterable-float" i32 Set textureLayout . sampleType to "sint" u32 Set textureLayout . sampleType to "uint" Set textureLayout . viewDimension to resource ’s dimension. If resource is for a multisampled texture: Set textureLayout . multisampled to true . Set entry . texture to textureLayout .
If resource is for a sampled texture binding:
- Let textureLayout be a new GPUTextureBindingLayout .
Let textureLayout be a new GPUTextureBindingLayout .
- If resource is a depth texture binding: Set textureLayout . sampleType to "depth" Otherwise, if the sampled type of resource is: f32 and there exists a static use of resource by stageDesc in a texture builtin function call that also uses a sampler Set textureLayout . sampleType to "float" f32 otherwise Set textureLayout . sampleType to "unfilterable-float" i32 Set textureLayout . sampleType to "sint" u32 Set textureLayout . sampleType to "uint"
If resource is a depth texture binding:
- Set textureLayout . sampleType to "depth"
Set textureLayout . sampleType to "depth"
Otherwise, if the sampled type of resource is:
Set textureLayout . sampleType to "float"
Set textureLayout . sampleType to "unfilterable-float"
Set textureLayout . sampleType to "sint"
Set textureLayout . sampleType to "uint"
- Set textureLayout . viewDimension to resource ’s dimension.
Set textureLayout . viewDimension to resource ’s dimension.
- If resource is for a multisampled texture: Set textureLayout . multisampled to true .
If resource is for a multisampled texture:
- Set textureLayout . multisampled to true .
Set textureLayout . multisampled to true .
- Set entry . texture to textureLayout .
Set entry . texture to textureLayout .
- If resource is for a storage texture binding: Let storageTextureLayout be a new GPUStorageTextureBindingLayout . Set storageTextureLayout . format to resource ’s format. Set storageTextureLayout . viewDimension to resource ’s dimension. If the access mode is: read Set textureLayout . access to "read-only" . write Set textureLayout . access to "write-only" . read_write Set textureLayout . access to "read-write" . Set entry . storageTexture to storageTextureLayout .
If resource is for a storage texture binding:
- Let storageTextureLayout be a new GPUStorageTextureBindingLayout .
Let storageTextureLayout be a new GPUStorageTextureBindingLayout .
- Set storageTextureLayout . format to resource ’s format.
Set storageTextureLayout . format to resource ’s format.
- Set storageTextureLayout . viewDimension to resource ’s dimension.
Set storageTextureLayout . viewDimension to resource ’s dimension.
- If the access mode is: read Set textureLayout . access to "read-only" . write Set textureLayout . access to "write-only" . read_write Set textureLayout . access to "read-write" .
If the access mode is:
Set textureLayout . access to "read-only" .
Set textureLayout . access to "write-only" .
Set textureLayout . access to "read-write" .
- Set entry . storageTexture to storageTextureLayout .
Set entry . storageTexture to storageTextureLayout .
- Set groupCount to max( groupCount , group + 1).
Set groupCount to max( groupCount , group + 1).
- If groupDescs [ group ] has an entry previousEntry with binding equal to binding : If entry has different visibility than previousEntry : Add the bits set in entry . visibility into previousEntry . visibility If resource is for a buffer binding and entry has greater buffer . minBindingSize than previousEntry : Set previousEntry . buffer . minBindingSize to entry . buffer . minBindingSize . If resource is a sampled texture binding and entry has different texture . sampleType than previousEntry and both entry and previousEntry have texture . sampleType of either "float" or "unfilterable-float" : Set previousEntry . texture . sampleType to "float" . If any other property is unequal between entry and previousEntry : Return null (which will cause the creation of the pipeline to fail). If resource is a storage texture binding, entry . storageTexture . access is "read-write" , previousEntry . storageTexture . access is "write-only" , and previousEntry . storageTexture . format is compatible with STORAGE_BINDING and "read-write" according to the § 26.1.1 Plain color formats table: Set previousEntry . storageTexture . access to "read-write" . Otherwise: Append entry to groupDescs [ group ].
If groupDescs [ group ] has an entry previousEntry with binding equal to binding :
- If entry has different visibility than previousEntry : Add the bits set in entry . visibility into previousEntry . visibility
If entry has different visibility than previousEntry :
- Add the bits set in entry . visibility into previousEntry . visibility
Add the bits set in entry . visibility into previousEntry . visibility
- If resource is for a buffer binding and entry has greater buffer . minBindingSize than previousEntry : Set previousEntry . buffer . minBindingSize to entry . buffer . minBindingSize .
If resource is for a buffer binding and entry has greater buffer . minBindingSize than previousEntry :
- Set previousEntry . buffer . minBindingSize to entry . buffer . minBindingSize .
Set previousEntry . buffer . minBindingSize to entry . buffer . minBindingSize .
- If resource is a sampled texture binding and entry has different texture . sampleType than previousEntry and both entry and previousEntry have texture . sampleType of either "float" or "unfilterable-float" : Set previousEntry . texture . sampleType to "float" .
If resource is a sampled texture binding and entry has different texture . sampleType than previousEntry and both entry and previousEntry have texture . sampleType of either "float" or "unfilterable-float" :
- Set previousEntry . texture . sampleType to "float" .
Set previousEntry . texture . sampleType to "float" .
- If any other property is unequal between entry and previousEntry : Return null (which will cause the creation of the pipeline to fail).
If any other property is unequal between entry and previousEntry :
- Return null (which will cause the creation of the pipeline to fail).
Return null (which will cause the creation of the pipeline to fail).
- If resource is a storage texture binding, entry . storageTexture . access is "read-write" , previousEntry . storageTexture . access is "write-only" , and previousEntry . storageTexture . format is compatible with STORAGE_BINDING and "read-write" according to the § 26.1.1 Plain color formats table: Set previousEntry . storageTexture . access to "read-write" . Otherwise: Append entry to groupDescs [ group ].
If resource is a storage texture binding, entry . storageTexture . access is "read-write" , previousEntry . storageTexture . access is "write-only" , and previousEntry . storageTexture . format is compatible with STORAGE_BINDING and "read-write" according to the § 26.1.1 Plain color formats table:
- Set previousEntry . storageTexture . access to "read-write" .
Set previousEntry . storageTexture . access to "read-write" .
Otherwise:
- Append entry to groupDescs [ group ].
Append entry to groupDescs [ group ].
- Let groupLayouts be a new list .
Let groupLayouts be a new list .
- For each i from 0 to groupCount - 1, inclusive: Let groupDesc be groupDescs [ i ]. Let bindGroupLayout be the result of calling device . createBindGroupLayout() ( groupDesc ). Set bindGroupLayout . [[exclusivePipeline]] to pipeline . Append bindGroupLayout to groupLayouts .
For each i from 0 to groupCount - 1, inclusive:
- Let groupDesc be groupDescs [ i ].
Let groupDesc be groupDescs [ i ].
- Let bindGroupLayout be the result of calling device . createBindGroupLayout() ( groupDesc ).
Let bindGroupLayout be the result of calling device . createBindGroupLayout() ( groupDesc ).
- Set bindGroupLayout . [[exclusivePipeline]] to pipeline .
Set bindGroupLayout . [[exclusivePipeline]] to pipeline .
- Append bindGroupLayout to groupLayouts .
Append bindGroupLayout to groupLayouts .
- Let desc be a new GPUPipelineLayoutDescriptor .
Let desc be a new GPUPipelineLayoutDescriptor .
- Set desc . bindGroupLayouts to groupLayouts .
Set desc . bindGroupLayouts to groupLayouts .
- Return device . createPipelineLayout() ( desc ).
Return device . createPipelineLayout() ( desc ).
A GPUProgrammableStage describes the entry point in the user-provided GPUShaderModule that controls one of the programmable stages of a pipeline .
Entry point names follow the rules defined in WGSL identifier comparison .
[LINK: WGSL identifier comparison](https://gpuweb.github.io/gpuweb/wgsl/#identifier-comparison)
GPUProgrammableStage has the following members:
The GPUShaderModule containing the code that this programmable stage will execute.
The name of the function in module that this stage will use to
perform its work.
NOTE: Since the entryPoint dictionary member is
not required, methods which consume a GPUProgrammableStage must use the
" get the entry point " algorithm to determine which entry point
it refers to.
Specifies the values of pipeline-overridable constants in the shader module module .
[LINK: pipeline-overridable](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable)
Each such pipeline-overridable constant is uniquely identified by a single pipeline-overridable constant identifier string , representing the pipeline constant ID of the constant if its declaration specifies one, and otherwise the
constant’s identifier name.
[LINK: pipeline-overridable](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable)
[LINK: pipeline-overridable constant identifier string](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable-constant-identifier-string)
[LINK: pipeline constant ID](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-constant-id)
The key of each key-value pair must equal the identifier string of one such constant, with the comparison performed
according to the rules for WGSL identifier comparison .
When the pipeline is executed, that constant will have the specified value.
[LINK: identifier string](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable-constant-identifier-string)
[LINK: WGSL identifier comparison](https://gpuweb.github.io/gpuweb/wgsl/#identifier-comparison)
Values are specified as GPUPipelineConstantValue , which is a double .
They are converted to WGSL type of the pipeline-overridable constant ( bool / i32 / u32 / f32 / f16 ).
If conversion fails, a validation error is generated.
Corresponding JavaScript code, providing only the overrides which are required
    (have no defaults):
Corresponding JavaScript code, overriding all constants:
- If descriptor . entryPoint is provided : If descriptor . module contains an entry point
whose name equals descriptor . entryPoint ,
and whose shader stage equals stage ,
return that entry point. Otherwise, return null . Otherwise: If there is exactly one entry point in descriptor . module whose shader stage equals stage , return that entry point. Otherwise, return null .
If descriptor . entryPoint is provided :
- If descriptor . module contains an entry point
whose name equals descriptor . entryPoint ,
and whose shader stage equals stage ,
return that entry point. Otherwise, return null .
If descriptor . module contains an entry point
whose name equals descriptor . entryPoint ,
and whose shader stage equals stage ,
return that entry point.
Otherwise, return null .
Otherwise:
- If there is exactly one entry point in descriptor . module whose shader stage equals stage , return that entry point. Otherwise, return null .
If there is exactly one entry point in descriptor . module whose shader stage equals stage , return that entry point.
Otherwise, return null .
Arguments:
- GPUShaderStage stage
GPUShaderStage stage
- GPUProgrammableStage descriptor
GPUProgrammableStage descriptor
- GPUPipelineLayout layout
GPUPipelineLayout layout
- GPUDevice device
GPUDevice device
All of the requirements in the following steps must be met.
    If any are unmet, return false ; otherwise, return true .
- descriptor . module must be valid to use with device .
descriptor . module must be valid to use with device .
- Let entryPoint be get the entry point ( stage , descriptor ).
Let entryPoint be get the entry point ( stage , descriptor ).
- entryPoint must not be null .
entryPoint must not be null .
- For each binding that is statically used by entryPoint : validating shader binding ( binding , layout ) must return true .
For each binding that is statically used by entryPoint :
- validating shader binding ( binding , layout ) must return true .
validating shader binding ( binding , layout ) must return true .
- For each call call to a texture builtin function in any of the functions in the shader stage rooted at entryPoint : Let textureBinding be the texture binding used in call . If textureBinding is of type sampled texture or depth texture and call uses a sampler binding samplerBinding of type sampler (excluding sampler_comparison ): Let texture be the GPUBindGroupLayoutEntry corresponding to textureBinding . Let sampler be the GPUBindGroupLayoutEntry corresponding to samplerBinding . If sampler . type is "filtering" ,
then texture . sampleType must be "float" . Note: "comparison" samplers can also only be used with "depth" textures, because they are the only texture type that can
be bound to WGSL texture_depth_* bindings. If device . [[features]] does not contain "core-features-and-limits" : If call is a call to textureLoad , textureBinding must not be of type depth texture . If call uses a sampler binding samplerBinding and textureBinding is of type depth texture , samplerBinding must be of sampler_comparison type.
For each call call to a texture builtin function in any of the functions in the shader stage rooted at entryPoint :
[LINK: functions in the shader stage](https://gpuweb.github.io/gpuweb/wgsl/#functions-in-a-shader-stage)
- Let textureBinding be the texture binding used in call .
Let textureBinding be the texture binding used in call .
- If textureBinding is of type sampled texture or depth texture and call uses a sampler binding samplerBinding of type sampler (excluding sampler_comparison ): Let texture be the GPUBindGroupLayoutEntry corresponding to textureBinding . Let sampler be the GPUBindGroupLayoutEntry corresponding to samplerBinding . If sampler . type is "filtering" ,
then texture . sampleType must be "float" . Note: "comparison" samplers can also only be used with "depth" textures, because they are the only texture type that can
be bound to WGSL texture_depth_* bindings.
If textureBinding is of type sampled texture or depth texture and call uses a sampler binding samplerBinding of type sampler (excluding sampler_comparison ):
[LINK: sampled texture](https://gpuweb.github.io/gpuweb/wgsl/#type-sampled-texture)
[LINK: depth texture](https://gpuweb.github.io/gpuweb/wgsl/#type-depth-texture)
- Let texture be the GPUBindGroupLayoutEntry corresponding to textureBinding .
Let texture be the GPUBindGroupLayoutEntry corresponding to textureBinding .
- Let sampler be the GPUBindGroupLayoutEntry corresponding to samplerBinding .
Let sampler be the GPUBindGroupLayoutEntry corresponding to samplerBinding .
- If sampler . type is "filtering" ,
then texture . sampleType must be "float" .
If sampler . type is "filtering" ,
then texture . sampleType must be "float" .
Note: "comparison" samplers can also only be used with "depth" textures, because they are the only texture type that can
be bound to WGSL texture_depth_* bindings.
- If device . [[features]] does not contain "core-features-and-limits" : If call is a call to textureLoad , textureBinding must not be of type depth texture . If call uses a sampler binding samplerBinding and textureBinding is of type depth texture , samplerBinding must be of sampler_comparison type.
- If call is a call to textureLoad , textureBinding must not be of type depth texture .
If call is a call to textureLoad , textureBinding must not be of type depth texture .
[LINK: depth texture](https://gpuweb.github.io/gpuweb/wgsl/#type-depth-texture)
- If call uses a sampler binding samplerBinding and textureBinding is of type depth texture , samplerBinding must be of sampler_comparison type.
If call uses a sampler binding samplerBinding and textureBinding is of type depth texture , samplerBinding must be of sampler_comparison type.
[LINK: depth texture](https://gpuweb.github.io/gpuweb/wgsl/#type-depth-texture)
- For each key → value in descriptor . constants : key must equal the pipeline-overridable constant identifier string of
some pipeline-overridable constant defined in the shader module descriptor . module by the rules defined in WGSL identifier comparison .
The pipeline-overridable constant is not required to be statically used by entryPoint .
Let the type of that constant be T . Converting the IDL value value to WGSL type T must not throw a TypeError .
For each key → value in descriptor . constants :
- key must equal the pipeline-overridable constant identifier string of
some pipeline-overridable constant defined in the shader module descriptor . module by the rules defined in WGSL identifier comparison .
The pipeline-overridable constant is not required to be statically used by entryPoint .
Let the type of that constant be T .
key must equal the pipeline-overridable constant identifier string of
some pipeline-overridable constant defined in the shader module descriptor . module by the rules defined in WGSL identifier comparison .
The pipeline-overridable constant is not required to be statically used by entryPoint .
Let the type of that constant be T .
[LINK: pipeline-overridable constant identifier string](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable-constant-identifier-string)
[LINK: pipeline-overridable](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable)
[LINK: WGSL identifier comparison](https://gpuweb.github.io/gpuweb/wgsl/#identifier-comparison)
- Converting the IDL value value to WGSL type T must not throw a TypeError .
Converting the IDL value value to WGSL type T must not throw a TypeError .
- For each pipeline-overridable constant identifier string key which is statically used by entryPoint : If the pipeline-overridable constant identified by key does not have a default value , descriptor . constants must contain key .
For each pipeline-overridable constant identifier string key which is statically used by entryPoint :
[LINK: pipeline-overridable constant identifier string](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable-constant-identifier-string)
- If the pipeline-overridable constant identified by key does not have a default value , descriptor . constants must contain key .
If the pipeline-overridable constant identified by key does not have a default value , descriptor . constants must contain key .
[LINK: does not have a default value](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable-constant-default-value)
- Pipeline-creation program errors must not
result from the rules of the [WGSL] specification.
Pipeline-creation program errors must not
result from the rules of the [WGSL] specification.
[LINK: Pipeline-creation](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-creation-error)
[LINK: program errors](https://gpuweb.github.io/gpuweb/wgsl/#program-error)
- If device . [[features]] does not contain "core-features-and-limits" : Let sum be 0. For each unique texture or external texture binding textureBinding that is used in any call to a texture builtin in any of the functions in the shader stage rooted at entryPoint : Let samplerBindings be the set of sampler bindings used together with textureBinding in any call to a texture builtin in any of the functions in the shader stage rooted at entryPoint . Let numPairs be max(1, number of elements of samplerBindings ) . If textureBinding is an external texture binding: Let numPairs be 1 + 3 * numPairs . Let sum be sum + numPairs . sum must be ≤ device .limits. maxSampledTexturesPerShaderStage . sum must be ≤ device .limits. maxSamplersPerShaderStage .
- Let sum be 0.
Let sum be 0.
- For each unique texture or external texture binding textureBinding that is used in any call to a texture builtin in any of the functions in the shader stage rooted at entryPoint : Let samplerBindings be the set of sampler bindings used together with textureBinding in any call to a texture builtin in any of the functions in the shader stage rooted at entryPoint . Let numPairs be max(1, number of elements of samplerBindings ) . If textureBinding is an external texture binding: Let numPairs be 1 + 3 * numPairs . Let sum be sum + numPairs .
For each unique texture or external texture binding textureBinding that is used in any call to a texture builtin in any of the functions in the shader stage rooted at entryPoint :
[LINK: functions in the shader stage](https://gpuweb.github.io/gpuweb/wgsl/#functions-in-a-shader-stage)
- Let samplerBindings be the set of sampler bindings used together with textureBinding in any call to a texture builtin in any of the functions in the shader stage rooted at entryPoint .
Let samplerBindings be the set of sampler bindings used together with textureBinding in any call to a texture builtin in any of the functions in the shader stage rooted at entryPoint .
[LINK: functions in the shader stage](https://gpuweb.github.io/gpuweb/wgsl/#functions-in-a-shader-stage)
- Let numPairs be max(1, number of elements of samplerBindings ) .
Let numPairs be max(1, number of elements of samplerBindings ) .
- If textureBinding is an external texture binding: Let numPairs be 1 + 3 * numPairs .
If textureBinding is an external texture binding:
- Let numPairs be 1 + 3 * numPairs .
Let numPairs be 1 + 3 * numPairs .
- Let sum be sum + numPairs .
Let sum be sum + numPairs .
- sum must be ≤ device .limits. maxSampledTexturesPerShaderStage .
sum must be ≤ device .limits. maxSampledTexturesPerShaderStage .
- sum must be ≤ device .limits. maxSamplersPerShaderStage .
sum must be ≤ device .limits. maxSamplersPerShaderStage .
Arguments:
- shader binding declaration variable , a module-scope variable declaration reflected from a shader module
shader binding declaration variable , a module-scope variable declaration reflected from a shader module
- GPUPipelineLayout layout
GPUPipelineLayout layout
Let bindGroup be the bind group index, and bindIndex be the binding index,
    of the shader binding declaration variable .
Return true if all of the following conditions are satisfied:
- layout . [[bindGroupLayouts]] [ bindGroup ] contains
a GPUBindGroupLayoutEntry entry whose entry . binding == bindIndex .
layout . [[bindGroupLayouts]] [ bindGroup ] contains
a GPUBindGroupLayoutEntry entry whose entry . binding == bindIndex .
- If the defined binding member for entry is: buffer If entry . buffer . type is: "uniform" variable is declared with address space uniform . "storage" variable is declared with address space storage and access mode read_write . "read-only-storage" variable is declared with address space storage and access mode read . If entry . buffer . minBindingSize is not 0 ,
then it must be at least the minimum buffer binding size for the associated
buffer binding variable in the shader. sampler If entry . sampler . type is: "filtering" or "non-filtering" variable has type sampler . "comparison" variable has type sampler_comparison . texture If, and only if, entry . texture . multisampled is true , variable has type texture_multisampled_2d<T> or texture_depth_multisampled_2d<T> . If entry . texture . sampleType is: "float" , "unfilterable-float" , "sint" or "uint" variable has one of the types: texture_1d<T> texture_2d<T> texture_2d_array<T> texture_cube<T> texture_cube_array<T> texture_3d<T> texture_multisampled_2d<T> If entry . texture . sampleType is: "float" or "unfilterable-float" The sampled type T is f32 . "sint" The sampled type T is i32 . "uint" The sampled type T is u32 . "depth" variable has one of the types: texture_2d<T> texture_2d_array<T> texture_cube<T> texture_cube_array<T> texture_multisampled_2d<T> texture_depth_2d texture_depth_2d_array texture_depth_cube texture_depth_cube_array texture_depth_multisampled_2d where the sampled type T is f32 . If entry . texture . viewDimension is: "1d" variable has type texture_1d<T> . "2d" variable has type texture_2d<T> or texture_multisampled_2d<T> . "2d-array" variable has type texture_2d_array<T> . "cube" variable has type texture_cube<T> . "cube-array" variable has type texture_cube_array<T> . "3d" variable has type texture_3d<T> . storageTexture If entry . storageTexture . viewDimension is: "1d" variable has type texture_storage_1d<T, A> . "2d" variable has type texture_storage_2d<T, A> . "2d-array" variable has type texture_storage_2d_array<T, A> . "3d" variable has type texture_storage_3d<T, A> . If entry . storageTexture . access is: "write-only" The access mode A is write . "read-only" The access mode A is read . "read-write" The access mode A is read_write or write . The texel format T equals entry . storageTexture . format .
If the defined binding member for entry is:
If entry . buffer . type is:
variable is declared with address space uniform .
variable is declared with address space storage and access mode read_write .
variable is declared with address space storage and access mode read .
If entry . buffer . minBindingSize is not 0 ,
then it must be at least the minimum buffer binding size for the associated
buffer binding variable in the shader.
If entry . sampler . type is:
variable has type sampler .
variable has type sampler_comparison .
If, and only if, entry . texture . multisampled is true , variable has type texture_multisampled_2d<T> or texture_depth_multisampled_2d<T> .
If entry . texture . sampleType is:
variable has one of the types:
- texture_1d<T>
texture_1d<T>
- texture_2d<T>
texture_2d<T>
- texture_2d_array<T>
texture_2d_array<T>
- texture_cube<T>
texture_cube<T>
- texture_cube_array<T>
texture_cube_array<T>
- texture_3d<T>
texture_3d<T>
- texture_multisampled_2d<T>
texture_multisampled_2d<T>
If entry . texture . sampleType is:
The sampled type T is f32 .
The sampled type T is i32 .
The sampled type T is u32 .
variable has one of the types:
- texture_2d<T>
texture_2d<T>
- texture_2d_array<T>
texture_2d_array<T>
- texture_cube<T>
texture_cube<T>
- texture_cube_array<T>
texture_cube_array<T>
- texture_multisampled_2d<T>
texture_multisampled_2d<T>
- texture_depth_2d
texture_depth_2d
- texture_depth_2d_array
texture_depth_2d_array
- texture_depth_cube
texture_depth_cube
- texture_depth_cube_array
texture_depth_cube_array
- texture_depth_multisampled_2d
texture_depth_multisampled_2d
where the sampled type T is f32 .
If entry . texture . viewDimension is:
variable has type texture_1d<T> .
variable has type texture_2d<T> or texture_multisampled_2d<T> .
variable has type texture_2d_array<T> .
variable has type texture_cube<T> .
variable has type texture_cube_array<T> .
variable has type texture_3d<T> .
If entry . storageTexture . viewDimension is:
variable has type texture_storage_1d<T, A> .
variable has type texture_storage_2d<T, A> .
variable has type texture_storage_2d_array<T, A> .
variable has type texture_storage_3d<T, A> .
If entry . storageTexture . access is:
The access mode A is write .
The access mode A is read .
The access mode A is read_write or write .
The texel format T equals entry . storageTexture . format .
- Let T be the store type of var .
Let T be the store type of var .
[LINK: store type](https://gpuweb.github.io/gpuweb/wgsl/#store-type)
- If T is a runtime-sized array, or contains a runtime-sized array, replace
that array<E> with array<E, 1> . Note: This ensures there’s always enough memory for one element, which allows array
indices to be clamped to the length of the array resulting in an in-memory access.
If T is a runtime-sized array, or contains a runtime-sized array, replace
that array<E> with array<E, 1> .
[LINK: runtime-sized](https://gpuweb.github.io/gpuweb/wgsl/#runtime-sized)
Note: This ensures there’s always enough memory for one element, which allows array
indices to be clamped to the length of the array resulting in an in-memory access.
- Return SizeOf ( T ).
Return SizeOf ( T ).
[LINK: SizeOf](https://gpuweb.github.io/gpuweb/wgsl/#sizeof)
Note: Enforcing this lower bound ensures reads and writes via the buffer variable only access memory locations
    within the bound region of the buffer.
[LINK: pipeline-overridable](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-overridable)
[LINK: interface of the shader stage](https://gpuweb.github.io/gpuweb/wgsl/#interface-of-a-shader)

### 10.2. GPUComputePipeline

A GPUComputePipeline is a kind of pipeline that controls the compute shader stage,
and can be used in GPUComputePassEncoder .
Compute inputs and outputs are all contained in the bindings,
according to the given GPUPipelineLayout .
The outputs correspond to buffer bindings with a type of "storage" and storageTexture bindings with a type of "write-only" or "read-write" .
Stages of a compute pipeline :
- Compute shader
Compute shader
A GPUComputePipelineDescriptor describes a compute pipeline . See § 23.1 Computing for additional details.
GPUComputePipelineDescriptor has the following members:
Describes the compute shader entry point of the pipeline .
Creates a GPUComputePipeline using immediate pipeline creation .
Arguments:
Returns: GPUComputePipeline
Content timeline steps:
- Let pipeline be ! create a new WebGPU object ( this , GPUComputePipeline , descriptor ).
Let pipeline be ! create a new WebGPU object ( this , GPUComputePipeline , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return pipeline .
Return pipeline .
- Let layout be a new default pipeline layout for pipeline if descriptor . layout is "auto" ,
and descriptor . layout otherwise.
Let layout be a new default pipeline layout for pipeline if descriptor . layout is "auto" ,
and descriptor . layout otherwise.
- All of the requirements in the following steps must be met.
If any are unmet, generate a validation error , invalidate pipeline and return. layout must be valid to use with this . validating GPUProgrammableStage ( COMPUTE , descriptor . compute , layout , this ) must succeed. Let entryPoint be get the entry point ( COMPUTE , descriptor . compute ). Assert entryPoint is not null . Let workgroupStorageUsed be the sum of roundUp (16, SizeOf ( T )) over each
type T of all variables with address space " workgroup " statically used by entryPoint . workgroupStorageUsed must be ≤ device .limits. maxComputeWorkgroupStorageSize . entryPoint must use ≤ device .limits. maxComputeInvocationsPerWorkgroup per
workgroup. Each component of entryPoint ’s workgroup_size attribute must be ≤ the corresponding component in
[ device .limits. maxComputeWorkgroupSizeX , device .limits. maxComputeWorkgroupSizeY , device .limits. maxComputeWorkgroupSizeZ ].
All of the requirements in the following steps must be met.
If any are unmet, generate a validation error , invalidate pipeline and return.
- layout must be valid to use with this .
layout must be valid to use with this .
- validating GPUProgrammableStage ( COMPUTE , descriptor . compute , layout , this ) must succeed.
validating GPUProgrammableStage ( COMPUTE , descriptor . compute , layout , this ) must succeed.
- Let entryPoint be get the entry point ( COMPUTE , descriptor . compute ). Assert entryPoint is not null .
Let entryPoint be get the entry point ( COMPUTE , descriptor . compute ).
Assert entryPoint is not null .
- Let workgroupStorageUsed be the sum of roundUp (16, SizeOf ( T )) over each
type T of all variables with address space " workgroup " statically used by entryPoint . workgroupStorageUsed must be ≤ device .limits. maxComputeWorkgroupStorageSize .
Let workgroupStorageUsed be the sum of roundUp (16, SizeOf ( T )) over each
type T of all variables with address space " workgroup " statically used by entryPoint .
[LINK: roundUp](https://gpuweb.github.io/gpuweb/wgsl/#roundup)
[LINK: SizeOf](https://gpuweb.github.io/gpuweb/wgsl/#sizeof)
[LINK: workgroup](https://gpuweb.github.io/gpuweb/wgsl/#address-spaces-workgroup)
workgroupStorageUsed must be ≤ device .limits. maxComputeWorkgroupStorageSize .
- entryPoint must use ≤ device .limits. maxComputeInvocationsPerWorkgroup per
workgroup.
entryPoint must use ≤ device .limits. maxComputeInvocationsPerWorkgroup per
workgroup.
- Each component of entryPoint ’s workgroup_size attribute must be ≤ the corresponding component in
[ device .limits. maxComputeWorkgroupSizeX , device .limits. maxComputeWorkgroupSizeY , device .limits. maxComputeWorkgroupSizeZ ].
Each component of entryPoint ’s workgroup_size attribute must be ≤ the corresponding component in
[ device .limits. maxComputeWorkgroupSizeX , device .limits. maxComputeWorkgroupSizeY , device .limits. maxComputeWorkgroupSizeZ ].
- If any pipeline-creation uncategorized errors result from the implementation of pipeline creation, generate an internal error , invalidate pipeline and return. Note: Even if the implementation detected uncategorized errors in shader module
creation, the error is surfaced here.
If any pipeline-creation uncategorized errors result from the implementation of pipeline creation, generate an internal error , invalidate pipeline and return.
[LINK: pipeline-creation](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-creation-error)
[LINK: uncategorized errors](https://gpuweb.github.io/gpuweb/wgsl/#uncategorized-error)
Note: Even if the implementation detected uncategorized errors in shader module
creation, the error is surfaced here.
[LINK: uncategorized errors](https://gpuweb.github.io/gpuweb/wgsl/#uncategorized-error)
- Set pipeline . [[layout]] to layout .
Set pipeline . [[layout]] to layout .
Creates a GPUComputePipeline using async pipeline creation .
The returned Promise resolves when the created pipeline
is ready to be used without additional delay.
If pipeline creation fails, the returned Promise rejects with an GPUPipelineError .
(A GPUError is not dispatched to the device.)
Note: Use of this method is preferred whenever possible, as it prevents blocking the queue timeline work on pipeline compilation.
Arguments:
Returns: Promise < GPUComputePipeline >
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- Let promise be a new promise .
Let promise be a new promise .
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return promise .
Return promise .
- Let pipeline be a new GPUComputePipeline created as if this . createComputePipeline() was called with descriptor ,
except capturing any errors as error , rather than dispatching them to the device.
Let pipeline be a new GPUComputePipeline created as if this . createComputePipeline() was called with descriptor ,
except capturing any errors as error , rather than dispatching them to the device.
- Let event occur upon the (successful or unsuccessful) completion of pipeline creation for pipeline .
Let event occur upon the (successful or unsuccessful) completion of pipeline creation for pipeline .
[LINK: pipeline creation](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-creation)
- Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on the device timeline of this .
Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on the device timeline of this .
- If pipeline is valid or this is lost : Issue the following steps on contentTimeline : Content timeline steps: Resolve promise with pipeline . Return. Note: No errors are generated from a device which is lost.
See § 22 Errors & Debugging .
If pipeline is valid or this is lost :
- Issue the following steps on contentTimeline : Content timeline steps: Resolve promise with pipeline .
Issue the following steps on contentTimeline :
- Resolve promise with pipeline .
Resolve promise with pipeline .
- Return.
Return.
Note: No errors are generated from a device which is lost.
See § 22 Errors & Debugging .
- If pipeline is invalid and error is an internal error ,
issue the following steps on contentTimeline , and return. Content timeline steps: Reject promise with a GPUPipelineError with reason "internal" .
If pipeline is invalid and error is an internal error ,
issue the following steps on contentTimeline , and return.
- Reject promise with a GPUPipelineError with reason "internal" .
Reject promise with a GPUPipelineError with reason "internal" .
- If pipeline is invalid and error is a validation error ,
issue the following steps on contentTimeline , and return. Content timeline steps: Reject promise with a GPUPipelineError with reason "validation" .
If pipeline is invalid and error is a validation error ,
issue the following steps on contentTimeline , and return.
- Reject promise with a GPUPipelineError with reason "validation" .
Reject promise with a GPUPipelineError with reason "validation" .

### 10.3. GPURenderPipeline

A GPURenderPipeline is a kind of pipeline that controls the vertex
and fragment shader stages, and can be used in GPURenderPassEncoder as well as GPURenderBundleEncoder .
Render pipeline inputs are:
- bindings, according to the given GPUPipelineLayout
bindings, according to the given GPUPipelineLayout
- vertex and index buffers, described by GPUVertexState
vertex and index buffers, described by GPUVertexState
- the color attachments, described by GPUColorTargetState
the color attachments, described by GPUColorTargetState
- optionally, the depth-stencil attachment, described by GPUDepthStencilState
optionally, the depth-stencil attachment, described by GPUDepthStencilState
Render pipeline outputs are:
- buffer bindings with a type of "storage"
buffer bindings with a type of "storage"
- storageTexture bindings with a access of "write-only" or "read-write"
storageTexture bindings with a access of "write-only" or "read-write"
- the color attachments, described by GPUColorTargetState
the color attachments, described by GPUColorTargetState
- optionally, depth-stencil attachment, described by GPUDepthStencilState
optionally, depth-stencil attachment, described by GPUDepthStencilState
A render pipeline is comprised of the following render stages :
- Vertex fetch, controlled by GPUVertexState.buffers
Vertex fetch, controlled by GPUVertexState.buffers
- Vertex shader, controlled by GPUVertexState
Vertex shader, controlled by GPUVertexState
- Primitive assembly, controlled by GPUPrimitiveState
Primitive assembly, controlled by GPUPrimitiveState
- Rasterization, controlled by GPUPrimitiveState , GPUDepthStencilState , and GPUMultisampleState
Rasterization, controlled by GPUPrimitiveState , GPUDepthStencilState , and GPUMultisampleState
- Fragment shader, controlled by GPUFragmentState
Fragment shader, controlled by GPUFragmentState
- Stencil test and operation, controlled by GPUDepthStencilState
Stencil test and operation, controlled by GPUDepthStencilState
- Depth test and write, controlled by GPUDepthStencilState
Depth test and write, controlled by GPUDepthStencilState
- Output merging, controlled by GPUFragmentState.targets
Output merging, controlled by GPUFragmentState.targets
GPURenderPipeline has the following device timeline properties :
The GPURenderPipelineDescriptor describing this pipeline.
All optional fields of GPURenderPipelineDescriptor are defined.
True if the pipeline writes to the depth component of the depth/stencil attachment
True if the pipeline writes to the stencil component of the depth/stencil attachment
A GPURenderPipelineDescriptor describes a render pipeline by configuring each
of the render stages . See § 23.2 Rendering for additional details.
GPURenderPipelineDescriptor has the following members:
Describes the vertex shader entry point of the pipeline and its input buffer layouts.
Describes the primitive-related properties of the pipeline .
Describes the optional depth-stencil properties, including the testing, operations, and bias.
Describes the multi-sampling properties of the pipeline .
Describes the fragment shader entry point of the pipeline and its output colors. If
not provided , the § 23.2.8 No Color Output mode is enabled.
Creates a GPURenderPipeline using immediate pipeline creation .
Arguments:
Returns: GPURenderPipeline
Content timeline steps:
- If descriptor . fragment is provided : For each non- null colorState of descriptor . fragment . targets : ? Validate texture format required features of colorState . format with this . [[device]] .
If descriptor . fragment is provided :
- For each non- null colorState of descriptor . fragment . targets : ? Validate texture format required features of colorState . format with this . [[device]] .
For each non- null colorState of descriptor . fragment . targets :
- ? Validate texture format required features of colorState . format with this . [[device]] .
? Validate texture format required features of colorState . format with this . [[device]] .
- If descriptor . depthStencil is provided : ? Validate texture format required features of descriptor . depthStencil . format with this . [[device]] .
If descriptor . depthStencil is provided :
- ? Validate texture format required features of descriptor . depthStencil . format with this . [[device]] .
? Validate texture format required features of descriptor . depthStencil . format with this . [[device]] .
- Let pipeline be ! create a new WebGPU object ( this , GPURenderPipeline , descriptor ).
Let pipeline be ! create a new WebGPU object ( this , GPURenderPipeline , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return pipeline .
Return pipeline .
- Let layout be a new default pipeline layout for pipeline if descriptor . layout is "auto" ,
and descriptor . layout otherwise.
Let layout be a new default pipeline layout for pipeline if descriptor . layout is "auto" ,
and descriptor . layout otherwise.
- All of the requirements in the following steps must be met.
If any are unmet, generate a validation error , invalidate pipeline , and return. layout must be valid to use with this . validating GPURenderPipelineDescriptor ( descriptor , layout , this ) must succeed. Let vertexBufferCount be the index of the last non-null entry in descriptor . vertex . buffers ,
plus 1; or 0 if there are none. layout . [[bindGroupLayouts]] . size + vertexBufferCount must be ≤ this . [[device]] . [[limits]] . maxBindGroupsPlusVertexBuffers .
All of the requirements in the following steps must be met.
If any are unmet, generate a validation error , invalidate pipeline , and return.
- layout must be valid to use with this .
layout must be valid to use with this .
- validating GPURenderPipelineDescriptor ( descriptor , layout , this ) must succeed.
validating GPURenderPipelineDescriptor ( descriptor , layout , this ) must succeed.
- Let vertexBufferCount be the index of the last non-null entry in descriptor . vertex . buffers ,
plus 1; or 0 if there are none.
Let vertexBufferCount be the index of the last non-null entry in descriptor . vertex . buffers ,
plus 1; or 0 if there are none.
- layout . [[bindGroupLayouts]] . size + vertexBufferCount must be ≤ this . [[device]] . [[limits]] . maxBindGroupsPlusVertexBuffers .
layout . [[bindGroupLayouts]] . size + vertexBufferCount must be ≤ this . [[device]] . [[limits]] . maxBindGroupsPlusVertexBuffers .
- If any pipeline-creation uncategorized errors result from the implementation of pipeline creation, generate an internal error , invalidate pipeline and return. Note: Even if the implementation detected uncategorized errors in shader module
creation, the error is surfaced here.
If any pipeline-creation uncategorized errors result from the implementation of pipeline creation, generate an internal error , invalidate pipeline and return.
[LINK: pipeline-creation](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-creation-error)
[LINK: uncategorized errors](https://gpuweb.github.io/gpuweb/wgsl/#uncategorized-error)
Note: Even if the implementation detected uncategorized errors in shader module
creation, the error is surfaced here.
[LINK: uncategorized errors](https://gpuweb.github.io/gpuweb/wgsl/#uncategorized-error)
- Set pipeline . [[descriptor]] to descriptor .
Set pipeline . [[descriptor]] to descriptor .
- Set pipeline . [[writesDepth]] to false.
Set pipeline . [[writesDepth]] to false.
- Set pipeline . [[writesStencil]] to false.
Set pipeline . [[writesStencil]] to false.
- Let depthStencil be descriptor . depthStencil .
Let depthStencil be descriptor . depthStencil .
- If depthStencil is not null: If depthStencil . depthWriteEnabled is provided : Set pipeline . [[writesDepth]] to depthStencil . depthWriteEnabled . If depthStencil . stencilWriteMask is not 0: Let stencilFront be depthStencil . stencilFront . Let stencilBack be depthStencil . stencilBack . Let cullMode be descriptor . primitive . cullMode . If cullMode is not "front" , and any of stencilFront . passOp , stencilFront . depthFailOp , or stencilFront . failOp is not "keep" : Set pipeline . [[writesStencil]] to true. If cullMode is not "back" , and any of stencilBack . passOp , stencilBack . depthFailOp , or stencilBack . failOp is not "keep" : Set pipeline . [[writesStencil]] to true.
If depthStencil is not null:
- If depthStencil . depthWriteEnabled is provided : Set pipeline . [[writesDepth]] to depthStencil . depthWriteEnabled .
If depthStencil . depthWriteEnabled is provided :
- Set pipeline . [[writesDepth]] to depthStencil . depthWriteEnabled .
Set pipeline . [[writesDepth]] to depthStencil . depthWriteEnabled .
- If depthStencil . stencilWriteMask is not 0: Let stencilFront be depthStencil . stencilFront . Let stencilBack be depthStencil . stencilBack . Let cullMode be descriptor . primitive . cullMode . If cullMode is not "front" , and any of stencilFront . passOp , stencilFront . depthFailOp , or stencilFront . failOp is not "keep" : Set pipeline . [[writesStencil]] to true. If cullMode is not "back" , and any of stencilBack . passOp , stencilBack . depthFailOp , or stencilBack . failOp is not "keep" : Set pipeline . [[writesStencil]] to true.
If depthStencil . stencilWriteMask is not 0:
- Let stencilFront be depthStencil . stencilFront .
Let stencilFront be depthStencil . stencilFront .
- Let stencilBack be depthStencil . stencilBack .
Let stencilBack be depthStencil . stencilBack .
- Let cullMode be descriptor . primitive . cullMode .
Let cullMode be descriptor . primitive . cullMode .
- If cullMode is not "front" , and any of stencilFront . passOp , stencilFront . depthFailOp , or stencilFront . failOp is not "keep" : Set pipeline . [[writesStencil]] to true.
If cullMode is not "front" , and any of stencilFront . passOp , stencilFront . depthFailOp , or stencilFront . failOp is not "keep" :
- Set pipeline . [[writesStencil]] to true.
Set pipeline . [[writesStencil]] to true.
- If cullMode is not "back" , and any of stencilBack . passOp , stencilBack . depthFailOp , or stencilBack . failOp is not "keep" : Set pipeline . [[writesStencil]] to true.
If cullMode is not "back" , and any of stencilBack . passOp , stencilBack . depthFailOp , or stencilBack . failOp is not "keep" :
- Set pipeline . [[writesStencil]] to true.
Set pipeline . [[writesStencil]] to true.
- Set pipeline . [[layout]] to layout .
Set pipeline . [[layout]] to layout .
Creates a GPURenderPipeline using async pipeline creation .
The returned Promise resolves when the created pipeline
is ready to be used without additional delay.
If pipeline creation fails, the returned Promise rejects with an GPUPipelineError .
(A GPUError is not dispatched to the device.)
Note: Use of this method is preferred whenever possible, as it prevents blocking the queue timeline work on pipeline compilation.
Arguments:
Returns: Promise < GPURenderPipeline >
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- Let promise be a new promise .
Let promise be a new promise .
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return promise .
Return promise .
- Let pipeline be a new GPURenderPipeline created as if this . createRenderPipeline() was called with descriptor ,
except capturing any errors as error , rather than dispatching them to the device.
Let pipeline be a new GPURenderPipeline created as if this . createRenderPipeline() was called with descriptor ,
except capturing any errors as error , rather than dispatching them to the device.
- Let event occur upon the (successful or unsuccessful) completion of pipeline creation for pipeline .
Let event occur upon the (successful or unsuccessful) completion of pipeline creation for pipeline .
[LINK: pipeline creation](https://gpuweb.github.io/gpuweb/wgsl/#pipeline-creation)
- Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on the device timeline of this .
Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on the device timeline of this .
- If pipeline is valid or this is lost : Issue the following steps on contentTimeline : Content timeline steps: Resolve promise with pipeline . Return. Note: No errors are generated from a device which is lost.
See § 22 Errors & Debugging .
If pipeline is valid or this is lost :
- Issue the following steps on contentTimeline : Content timeline steps: Resolve promise with pipeline .
Issue the following steps on contentTimeline :
- Resolve promise with pipeline .
Resolve promise with pipeline .
- Return.
Return.
Note: No errors are generated from a device which is lost.
See § 22 Errors & Debugging .
- If pipeline is invalid and error is an internal error ,
issue the following steps on contentTimeline , and return. Content timeline steps: Reject promise with a GPUPipelineError with reason "internal" .
If pipeline is invalid and error is an internal error ,
issue the following steps on contentTimeline , and return.
- Reject promise with a GPUPipelineError with reason "internal" .
Reject promise with a GPUPipelineError with reason "internal" .
- If pipeline is invalid and error is a validation error ,
issue the following steps on contentTimeline , and return. Content timeline steps: Reject promise with a GPUPipelineError with reason "validation" .
If pipeline is invalid and error is a validation error ,
issue the following steps on contentTimeline , and return.
- Reject promise with a GPUPipelineError with reason "validation" .
Reject promise with a GPUPipelineError with reason "validation" .
Arguments:
- GPURenderPipelineDescriptor descriptor
GPURenderPipelineDescriptor descriptor
- GPUPipelineLayout layout
GPUPipelineLayout layout
- GPUDevice device
GPUDevice device
Device timeline steps:
- Return true if all of the following conditions are satisfied: validating GPUVertexState ( device , descriptor . vertex , layout ) succeeds. If descriptor . fragment is provided : validating GPUFragmentState ( device , descriptor . fragment , layout ) succeeds. If the sample_mask builtin is a shader stage output of descriptor . fragment : descriptor . multisample . alphaToCoverageEnabled is false . If the frag_depth builtin is a shader stage output of descriptor . fragment : descriptor . depthStencil must be provided , and descriptor . depthStencil . format must have a depth aspect. If device . [[features]] does not contain "core-features-and-limits" : The sample_mask builtin must not be a shader stage input or shader stage output of descriptor . fragment . The sample_index builtin must not be a shader stage input of descriptor . fragment . validating GPUPrimitiveState ( descriptor . primitive , device ) succeeds. If descriptor . depthStencil is provided : validating GPUDepthStencilState ( device , descriptor . depthStencil , descriptor . primitive . topology ) succeeds. validating GPUMultisampleState ( descriptor . multisample ) succeeds. If descriptor . multisample . alphaToCoverageEnabled is true: descriptor . fragment must be provided . descriptor . fragment . targets [0]
must exist and be non-null. descriptor . fragment . targets [0]. format must be a GPUTextureFormat which is blendable and has an alpha channel. There must exist at least one attachment, either: A non- null value in descriptor . fragment . targets , or A descriptor . depthStencil . validating inter-stage interfaces ( device , descriptor ) returns true .
Return true if all of the following conditions are satisfied:
- validating GPUVertexState ( device , descriptor . vertex , layout ) succeeds.
validating GPUVertexState ( device , descriptor . vertex , layout ) succeeds.
- If descriptor . fragment is provided : validating GPUFragmentState ( device , descriptor . fragment , layout ) succeeds. If the sample_mask builtin is a shader stage output of descriptor . fragment : descriptor . multisample . alphaToCoverageEnabled is false . If the frag_depth builtin is a shader stage output of descriptor . fragment : descriptor . depthStencil must be provided , and descriptor . depthStencil . format must have a depth aspect. If device . [[features]] does not contain "core-features-and-limits" : The sample_mask builtin must not be a shader stage input or shader stage output of descriptor . fragment . The sample_index builtin must not be a shader stage input of descriptor . fragment .
If descriptor . fragment is provided :
- validating GPUFragmentState ( device , descriptor . fragment , layout ) succeeds.
validating GPUFragmentState ( device , descriptor . fragment , layout ) succeeds.
- If the sample_mask builtin is a shader stage output of descriptor . fragment : descriptor . multisample . alphaToCoverageEnabled is false .
If the sample_mask builtin is a shader stage output of descriptor . fragment :
[LINK: sample_mask](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-sample_mask)
[LINK: shader stage output](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
- descriptor . multisample . alphaToCoverageEnabled is false .
descriptor . multisample . alphaToCoverageEnabled is false .
- If the frag_depth builtin is a shader stage output of descriptor . fragment : descriptor . depthStencil must be provided , and descriptor . depthStencil . format must have a depth aspect.
If the frag_depth builtin is a shader stage output of descriptor . fragment :
[LINK: frag_depth](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-frag_depth)
[LINK: shader stage output](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
- descriptor . depthStencil must be provided , and descriptor . depthStencil . format must have a depth aspect.
descriptor . depthStencil must be provided , and descriptor . depthStencil . format must have a depth aspect.
- If device . [[features]] does not contain "core-features-and-limits" : The sample_mask builtin must not be a shader stage input or shader stage output of descriptor . fragment . The sample_index builtin must not be a shader stage input of descriptor . fragment .
- The sample_mask builtin must not be a shader stage input or shader stage output of descriptor . fragment .
The sample_mask builtin must not be a shader stage input or shader stage output of descriptor . fragment .
[LINK: sample_mask](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-sample_mask)
[LINK: shader stage input](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-input)
[LINK: shader stage output](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
- The sample_index builtin must not be a shader stage input of descriptor . fragment .
The sample_index builtin must not be a shader stage input of descriptor . fragment .
[LINK: sample_index](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-sample_index)
[LINK: shader stage input](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-input)
- validating GPUPrimitiveState ( descriptor . primitive , device ) succeeds.
validating GPUPrimitiveState ( descriptor . primitive , device ) succeeds.
- If descriptor . depthStencil is provided : validating GPUDepthStencilState ( device , descriptor . depthStencil , descriptor . primitive . topology ) succeeds.
If descriptor . depthStencil is provided :
- validating GPUDepthStencilState ( device , descriptor . depthStencil , descriptor . primitive . topology ) succeeds.
validating GPUDepthStencilState ( device , descriptor . depthStencil , descriptor . primitive . topology ) succeeds.
- validating GPUMultisampleState ( descriptor . multisample ) succeeds.
validating GPUMultisampleState ( descriptor . multisample ) succeeds.
- If descriptor . multisample . alphaToCoverageEnabled is true: descriptor . fragment must be provided . descriptor . fragment . targets [0]
must exist and be non-null. descriptor . fragment . targets [0]. format must be a GPUTextureFormat which is blendable and has an alpha channel.
If descriptor . multisample . alphaToCoverageEnabled is true:
- descriptor . fragment must be provided .
descriptor . fragment must be provided .
- descriptor . fragment . targets [0]
must exist and be non-null.
descriptor . fragment . targets [0]
must exist and be non-null.
- descriptor . fragment . targets [0]. format must be a GPUTextureFormat which is blendable and has an alpha channel.
descriptor . fragment . targets [0]. format must be a GPUTextureFormat which is blendable and has an alpha channel.
- There must exist at least one attachment, either: A non- null value in descriptor . fragment . targets , or A descriptor . depthStencil .
There must exist at least one attachment, either:
- A non- null value in descriptor . fragment . targets , or
A non- null value in descriptor . fragment . targets , or
- A descriptor . depthStencil .
A descriptor . depthStencil .
- validating inter-stage interfaces ( device , descriptor ) returns true .
validating inter-stage interfaces ( device , descriptor ) returns true .
Arguments:
- shader binding declaration variable , a module-scope variable declaration reflected from a shader module
shader binding declaration variable , a module-scope variable declaration reflected from a shader module
Returns: boolean
Device timeline steps:
- If the interpolation of the variable is linear , return false .
If the interpolation of the variable is linear , return false .
[LINK: interpolation](https://gpuweb.github.io/gpuweb/wgsl/#interpolation)
[LINK: linear](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-type-linear)
- If the interpolation of the variable is flat and the interpolation sampling is not either , return false .
If the interpolation of the variable is flat and the interpolation sampling is not either , return false .
[LINK: interpolation](https://gpuweb.github.io/gpuweb/wgsl/#interpolation)
[LINK: flat](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-type-flat)
[LINK: interpolation sampling](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-sampling)
[LINK: either](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-sampling-either)
- If the interpolation sampling of the variable is sample , return false .
If the interpolation sampling of the variable is sample , return false .
[LINK: interpolation sampling](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-sampling)
[LINK: sample](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-sampling-sample)
- Return 'true'
Return 'true'
Arguments:
- GPUDevice device
GPUDevice device
- GPURenderPipelineDescriptor descriptor
GPURenderPipelineDescriptor descriptor
Returns: boolean
Device timeline steps:
- Let maxVertexShaderOutputVariables be device .limits. maxInterStageShaderVariables .
Let maxVertexShaderOutputVariables be device .limits. maxInterStageShaderVariables .
- Let maxVertexShaderOutputLocation be device .limits. maxInterStageShaderVariables - 1.
Let maxVertexShaderOutputLocation be device .limits. maxInterStageShaderVariables - 1.
- If descriptor . primitive . topology is "point-list" : Decrement maxVertexShaderOutputVariables by 1.
If descriptor . primitive . topology is "point-list" :
- Decrement maxVertexShaderOutputVariables by 1.
Decrement maxVertexShaderOutputVariables by 1.
- If clip_distances is declared in the output of descriptor . vertex : Let clipDistancesSize be the array size of clip_distances . Decrement maxVertexShaderOutputVariables by ceil( clipDistancesSize / 4). Decrement maxVertexShaderOutputLocation by ceil( clipDistancesSize / 4).
If clip_distances is declared in the output of descriptor . vertex :
[LINK: clip_distances](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-clip_distances)
- Let clipDistancesSize be the array size of clip_distances .
Let clipDistancesSize be the array size of clip_distances .
[LINK: clip_distances](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-clip_distances)
- Decrement maxVertexShaderOutputVariables by ceil( clipDistancesSize / 4).
Decrement maxVertexShaderOutputVariables by ceil( clipDistancesSize / 4).
- Decrement maxVertexShaderOutputLocation by ceil( clipDistancesSize / 4).
Decrement maxVertexShaderOutputLocation by ceil( clipDistancesSize / 4).
- Return false if any of the following requirements are unmet: There must be no more than maxVertexShaderOutputVariables user-defined outputs for descriptor . vertex . The location of each user-defined output of descriptor . vertex must be
≤ maxVertexShaderOutputLocation .
Return false if any of the following requirements are unmet:
- There must be no more than maxVertexShaderOutputVariables user-defined outputs for descriptor . vertex .
There must be no more than maxVertexShaderOutputVariables user-defined outputs for descriptor . vertex .
- The location of each user-defined output of descriptor . vertex must be
≤ maxVertexShaderOutputLocation .
The location of each user-defined output of descriptor . vertex must be
≤ maxVertexShaderOutputLocation .
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
- If device . [[features]] does not contain "core-features-and-limits" : For each user-defined output of descriptor . vertex : If validating Compatibility Mode shader binding ( output ) fails, return false .
If device . [[features]] does not contain "core-features-and-limits" :
- For each user-defined output of descriptor . vertex : If validating Compatibility Mode shader binding ( output ) fails, return false .
For each user-defined output of descriptor . vertex :
- If validating Compatibility Mode shader binding ( output ) fails, return false .
If validating Compatibility Mode shader binding ( output ) fails, return false .
- If descriptor . fragment is provided : Let maxFragmentShaderInputVariables be device .limits. maxInterStageShaderVariables . For each of the Inter-Stage Builtins that are an input of descriptor . fragment : Decrement maxFragmentShaderInputVariables by 1. Return false if any of the following requirements are unmet: For each user-defined input of descriptor . fragment there
must be a user-defined output of descriptor . vertex that location , type, and interpolation of the input. Note: Vertex-only pipelines can have user-defined outputs in the vertex stage;
their values will be discarded. There must be no more than maxFragmentShaderInputVariables user-defined inputs for descriptor . fragment . Assert that the location of each user-defined input of descriptor . fragment is less
than device .limits. maxInterStageShaderVariables .
(This follows from the above rules.) If device . [[features]] does not contain "core-features-and-limits" : For each user-defined input of descriptor . fragment : If validating Compatibility Mode shader binding ( input ) fails, return false .
If descriptor . fragment is provided :
- Let maxFragmentShaderInputVariables be device .limits. maxInterStageShaderVariables .
Let maxFragmentShaderInputVariables be device .limits. maxInterStageShaderVariables .
- For each of the Inter-Stage Builtins that are an input of descriptor . fragment : Decrement maxFragmentShaderInputVariables by 1.
For each of the Inter-Stage Builtins that are an input of descriptor . fragment :
- Decrement maxFragmentShaderInputVariables by 1.
Decrement maxFragmentShaderInputVariables by 1.
- Return false if any of the following requirements are unmet: For each user-defined input of descriptor . fragment there
must be a user-defined output of descriptor . vertex that location , type, and interpolation of the input. Note: Vertex-only pipelines can have user-defined outputs in the vertex stage;
their values will be discarded. There must be no more than maxFragmentShaderInputVariables user-defined inputs for descriptor . fragment .
Return false if any of the following requirements are unmet:
- For each user-defined input of descriptor . fragment there
must be a user-defined output of descriptor . vertex that location , type, and interpolation of the input. Note: Vertex-only pipelines can have user-defined outputs in the vertex stage;
their values will be discarded.
For each user-defined input of descriptor . fragment there
must be a user-defined output of descriptor . vertex that location , type, and interpolation of the input.
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
[LINK: interpolation](https://gpuweb.github.io/gpuweb/wgsl/#interpolation)
Note: Vertex-only pipelines can have user-defined outputs in the vertex stage;
their values will be discarded.
- There must be no more than maxFragmentShaderInputVariables user-defined inputs for descriptor . fragment .
There must be no more than maxFragmentShaderInputVariables user-defined inputs for descriptor . fragment .
- Assert that the location of each user-defined input of descriptor . fragment is less
than device .limits. maxInterStageShaderVariables .
(This follows from the above rules.)
Assert that the location of each user-defined input of descriptor . fragment is less
than device .limits. maxInterStageShaderVariables .
(This follows from the above rules.)
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
- If device . [[features]] does not contain "core-features-and-limits" : For each user-defined input of descriptor . fragment : If validating Compatibility Mode shader binding ( input ) fails, return false .
If device . [[features]] does not contain "core-features-and-limits" :
- For each user-defined input of descriptor . fragment : If validating Compatibility Mode shader binding ( input ) fails, return false .
For each user-defined input of descriptor . fragment :
- If validating Compatibility Mode shader binding ( input ) fails, return false .
If validating Compatibility Mode shader binding ( input ) fails, return false .
- Return true .
Return true .
The following builtins are Inter-Stage Builtins , and count towards the maxInterStageShaderVariables limit when used in a fragment shader:
[LINK: builtins](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- front_facing
front_facing
- sample_index
sample_index
- sample_mask
sample_mask
- primitive_index
primitive_index
- subgroup_invocation_id
subgroup_invocation_id
- subgroup_size
subgroup_size
GPUPrimitiveState has the following members, which describe how a GPURenderPipeline constructs and rasterizes primitives from its vertex inputs:
The type of primitive to be constructed from the vertex inputs.
For pipelines with strip topologies
( "line-strip" or "triangle-strip" ),
this determines the index buffer format and primitive restart value
( "uint16" / 0xFFFF or "uint32" / 0xFFFFFFFF ).
It is not allowed on pipelines with non-strip topologies.
Note: Some implementations require knowledge of the primitive restart value to compile
pipeline state objects.
To use a strip-topology pipeline with an indexed draw call
( drawIndexed() or drawIndexedIndirect() ),
this must be set, and it must match the index buffer format used with the draw call
(set in setIndexBuffer() ).
See § 23.2.3 Primitive Assembly for additional details.
Defines which polygons are considered front-facing .
Defines which polygon orientation will be culled, if any.
If true, indicates that depth clipping is disabled.
Requires the "depth-clip-control" feature to be enabled.
- GPUPrimitiveState descriptor
GPUPrimitiveState descriptor
- GPUDevice device
GPUDevice device
Device timeline steps:
- Return true if all of the following conditions are satisfied: If descriptor . topology is not "line-strip" or "triangle-strip" : descriptor . stripIndexFormat must not be provided . If descriptor . unclippedDepth is true : "depth-clip-control" must be enabled for device .
Return true if all of the following conditions are satisfied:
- If descriptor . topology is not "line-strip" or "triangle-strip" : descriptor . stripIndexFormat must not be provided .
If descriptor . topology is not "line-strip" or "triangle-strip" :
- descriptor . stripIndexFormat must not be provided .
descriptor . stripIndexFormat must not be provided .
- If descriptor . unclippedDepth is true : "depth-clip-control" must be enabled for device .
If descriptor . unclippedDepth is true :
- "depth-clip-control" must be enabled for device .
"depth-clip-control" must be enabled for device .
GPUPrimitiveTopology defines the primitive type draw calls made with a GPURenderPipeline will use. See § 23.2.5 Rasterization for additional details:
Each vertex defines a point primitive.
Each consecutive pair of two vertices defines a line primitive.
Each vertex after the first defines a line primitive between it and the previous vertex.
Each consecutive triplet of three vertices defines a triangle primitive.
Each vertex after the first two defines a triangle primitive between it and the previous
two vertices.
GPUFrontFace defines which polygons are considered front-facing by a GPURenderPipeline .
See § 23.2.5.4 Polygon Rasterization for additional details:
Polygons with vertices whose framebuffer coordinates are given in counter-clockwise order
are considered front-facing .
Polygons with vertices whose framebuffer coordinates are given in clockwise order are
considered front-facing .
GPUPrimitiveTopology defines which polygons will be culled by draw calls made with a GPURenderPipeline . See § 23.2.5.4 Polygon Rasterization for additional details:
No polygons are discarded.
Front-facing polygons are discarded.
Back-facing polygons are discarded.
Note: GPUFrontFace and GPUCullMode have no effect on "point-list" , "line-list" , or "line-strip" topologies.
GPUMultisampleState has the following members, which describe how a GPURenderPipeline interacts with a render pass’s multisampled attachments.
Number of samples per pixel. This GPURenderPipeline will be compatible only
with attachment textures ( colorAttachments and depthStencilAttachment )
with matching sampleCount s.
Mask determining which samples are written to.
When true indicates that a fragment’s alpha channel should be used to generate a sample
coverage mask.
- GPUMultisampleState descriptor
GPUMultisampleState descriptor
Device timeline steps:
- Return true if all of the following conditions are satisfied: descriptor . count must be either 1 or 4. If descriptor . alphaToCoverageEnabled is true : descriptor . count > 1.
Return true if all of the following conditions are satisfied:
- descriptor . count must be either 1 or 4.
descriptor . count must be either 1 or 4.
- If descriptor . alphaToCoverageEnabled is true : descriptor . count > 1.
If descriptor . alphaToCoverageEnabled is true :
- descriptor . count > 1.
descriptor . count > 1.
A list of GPUColorTargetState defining the formats and behaviors of the color targets
this pipeline writes to.
Arguments:
- GPUDevice device
GPUDevice device
- GPUFragmentState descriptor
GPUFragmentState descriptor
- GPUPipelineLayout layout
GPUPipelineLayout layout
Device timeline steps:
- Return true if all of the following requirements are met: validating GPUProgrammableStage ( FRAGMENT , descriptor , layout , device ) succeeds. descriptor . targets . size must be ≤ device . [[limits]] . maxColorAttachments . For each shader stage output output : output ’s location must be < device . [[limits]] . maxColorAttachments . Let entryPoint be get the entry point ( FRAGMENT , descriptor ). Let usesDualSourceBlending be false . For each index of the indices of descriptor . targets containing a non- null value colorState : colorState . format must be listed in § 26.1.1 Plain color formats with RENDER_ATTACHMENT capability. colorState . writeMask must be < 16. If colorState . blend is provided : The colorState . format must be blendable . colorState . blend . color must be a valid GPUBlendComponent . colorState . blend . alpha must be a valid GPUBlendComponent . If colorState . blend . color . srcFactor or colorState . blend . color . dstFactor or colorState . blend . alpha . srcFactor or colorState . blend . alpha . dstFactor uses the second input of the corresponding blending unit (is any of "src1" , "one-minus-src1" , "src1-alpha" , "one-minus-src1-alpha" ), then: Set usesDualSourceBlending to true . For each shader stage output value output with location attribute equal to index in entryPoint : For each component in colorState . format , there must be a
corresponding component in output .
(That is, RGBA requires vec4, RGB requires vec3 or vec4, RG requires vec2 or vec3 or vec4.) If the GPUTextureSampleType s for colorState . format (defined in § 26.1 Texture Format Capabilities ) are: "float" and/or "unfilterable-float" output must have a floating-point scalar type. "sint" output must have a signed integer scalar type. "uint" output must have an unsigned integer scalar type. If colorState . blend is provided and colorState . blend . color . srcFactor or . dstFactor uses the source alpha
(is any of "src-alpha" , "one-minus-src-alpha" , "src-alpha-saturated" , "src1-alpha" or "one-minus-src1-alpha" ), then: output must have an alpha channel (that is, it must be a vec4). If colorState . writeMask is not 0: entryPoint must have a shader stage output with location equal to index and blend_src omitted or equal to 0. If usesDualSourceBlending is true : descriptor . targets . size must be 1. All the shader stage outputs with location in entryPoint must be in one
struct and use dual source blending . Validating GPUFragmentState’s color attachment bytes per sample ( device , descriptor . targets ) succeeds. If device . [[features]] does not contain "core-features-and-limits" : All non-null GPUColorTargetState s colorState in descriptor . targets must have equal values for each
of the following members: colorState . blend . color colorState . blend . alpha colorState . writeMask For each function in the functions in the shader stage rooted at entryPoint : function must not be dpdxFine , dpdyFine , or fwidthFine .
Return true if all of the following requirements are met:
- validating GPUProgrammableStage ( FRAGMENT , descriptor , layout , device ) succeeds.
validating GPUProgrammableStage ( FRAGMENT , descriptor , layout , device ) succeeds.
- descriptor . targets . size must be ≤ device . [[limits]] . maxColorAttachments .
descriptor . targets . size must be ≤ device . [[limits]] . maxColorAttachments .
- For each shader stage output output : output ’s location must be < device . [[limits]] . maxColorAttachments .
For each shader stage output output :
[LINK: shader stage output](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
- output ’s location must be < device . [[limits]] . maxColorAttachments .
output ’s location must be < device . [[limits]] . maxColorAttachments .
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
- Let entryPoint be get the entry point ( FRAGMENT , descriptor ).
Let entryPoint be get the entry point ( FRAGMENT , descriptor ).
- Let usesDualSourceBlending be false .
Let usesDualSourceBlending be false .
- For each index of the indices of descriptor . targets containing a non- null value colorState : colorState . format must be listed in § 26.1.1 Plain color formats with RENDER_ATTACHMENT capability. colorState . writeMask must be < 16. If colorState . blend is provided : The colorState . format must be blendable . colorState . blend . color must be a valid GPUBlendComponent . colorState . blend . alpha must be a valid GPUBlendComponent . If colorState . blend . color . srcFactor or colorState . blend . color . dstFactor or colorState . blend . alpha . srcFactor or colorState . blend . alpha . dstFactor uses the second input of the corresponding blending unit (is any of "src1" , "one-minus-src1" , "src1-alpha" , "one-minus-src1-alpha" ), then: Set usesDualSourceBlending to true . For each shader stage output value output with location attribute equal to index in entryPoint : For each component in colorState . format , there must be a
corresponding component in output .
(That is, RGBA requires vec4, RGB requires vec3 or vec4, RG requires vec2 or vec3 or vec4.) If the GPUTextureSampleType s for colorState . format (defined in § 26.1 Texture Format Capabilities ) are: "float" and/or "unfilterable-float" output must have a floating-point scalar type. "sint" output must have a signed integer scalar type. "uint" output must have an unsigned integer scalar type. If colorState . blend is provided and colorState . blend . color . srcFactor or . dstFactor uses the source alpha
(is any of "src-alpha" , "one-minus-src-alpha" , "src-alpha-saturated" , "src1-alpha" or "one-minus-src1-alpha" ), then: output must have an alpha channel (that is, it must be a vec4). If colorState . writeMask is not 0: entryPoint must have a shader stage output with location equal to index and blend_src omitted or equal to 0.
For each index of the indices of descriptor . targets containing a non- null value colorState :
- colorState . format must be listed in § 26.1.1 Plain color formats with RENDER_ATTACHMENT capability.
colorState . format must be listed in § 26.1.1 Plain color formats with RENDER_ATTACHMENT capability.
- colorState . writeMask must be < 16.
colorState . writeMask must be < 16.
- If colorState . blend is provided : The colorState . format must be blendable . colorState . blend . color must be a valid GPUBlendComponent . colorState . blend . alpha must be a valid GPUBlendComponent . If colorState . blend . color . srcFactor or colorState . blend . color . dstFactor or colorState . blend . alpha . srcFactor or colorState . blend . alpha . dstFactor uses the second input of the corresponding blending unit (is any of "src1" , "one-minus-src1" , "src1-alpha" , "one-minus-src1-alpha" ), then: Set usesDualSourceBlending to true .
If colorState . blend is provided :
- The colorState . format must be blendable .
The colorState . format must be blendable .
- colorState . blend . color must be a valid GPUBlendComponent .
colorState . blend . color must be a valid GPUBlendComponent .
- colorState . blend . alpha must be a valid GPUBlendComponent .
colorState . blend . alpha must be a valid GPUBlendComponent .
- If colorState . blend . color . srcFactor or colorState . blend . color . dstFactor or colorState . blend . alpha . srcFactor or colorState . blend . alpha . dstFactor uses the second input of the corresponding blending unit (is any of "src1" , "one-minus-src1" , "src1-alpha" , "one-minus-src1-alpha" ), then: Set usesDualSourceBlending to true .
If colorState . blend . color . srcFactor or colorState . blend . color . dstFactor or colorState . blend . alpha . srcFactor or colorState . blend . alpha . dstFactor uses the second input of the corresponding blending unit (is any of "src1" , "one-minus-src1" , "src1-alpha" , "one-minus-src1-alpha" ), then:
- Set usesDualSourceBlending to true .
Set usesDualSourceBlending to true .
- For each shader stage output value output with location attribute equal to index in entryPoint : For each component in colorState . format , there must be a
corresponding component in output .
(That is, RGBA requires vec4, RGB requires vec3 or vec4, RG requires vec2 or vec3 or vec4.) If the GPUTextureSampleType s for colorState . format (defined in § 26.1 Texture Format Capabilities ) are: "float" and/or "unfilterable-float" output must have a floating-point scalar type. "sint" output must have a signed integer scalar type. "uint" output must have an unsigned integer scalar type. If colorState . blend is provided and colorState . blend . color . srcFactor or . dstFactor uses the source alpha
(is any of "src-alpha" , "one-minus-src-alpha" , "src-alpha-saturated" , "src1-alpha" or "one-minus-src1-alpha" ), then: output must have an alpha channel (that is, it must be a vec4).
For each shader stage output value output with location attribute equal to index in entryPoint :
[LINK: shader stage output](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
- For each component in colorState . format , there must be a
corresponding component in output .
(That is, RGBA requires vec4, RGB requires vec3 or vec4, RG requires vec2 or vec3 or vec4.)
For each component in colorState . format , there must be a
corresponding component in output .
(That is, RGBA requires vec4, RGB requires vec3 or vec4, RG requires vec2 or vec3 or vec4.)
- If the GPUTextureSampleType s for colorState . format (defined in § 26.1 Texture Format Capabilities ) are: "float" and/or "unfilterable-float" output must have a floating-point scalar type. "sint" output must have a signed integer scalar type. "uint" output must have an unsigned integer scalar type.
If the GPUTextureSampleType s for colorState . format (defined in § 26.1 Texture Format Capabilities ) are:
output must have a floating-point scalar type.
output must have a signed integer scalar type.
output must have an unsigned integer scalar type.
- If colorState . blend is provided and colorState . blend . color . srcFactor or . dstFactor uses the source alpha
(is any of "src-alpha" , "one-minus-src-alpha" , "src-alpha-saturated" , "src1-alpha" or "one-minus-src1-alpha" ), then: output must have an alpha channel (that is, it must be a vec4).
If colorState . blend is provided and colorState . blend . color . srcFactor or . dstFactor uses the source alpha
(is any of "src-alpha" , "one-minus-src-alpha" , "src-alpha-saturated" , "src1-alpha" or "one-minus-src1-alpha" ), then:
- output must have an alpha channel (that is, it must be a vec4).
output must have an alpha channel (that is, it must be a vec4).
- If colorState . writeMask is not 0: entryPoint must have a shader stage output with location equal to index and blend_src omitted or equal to 0.
If colorState . writeMask is not 0:
- entryPoint must have a shader stage output with location equal to index and blend_src omitted or equal to 0.
entryPoint must have a shader stage output with location equal to index and blend_src omitted or equal to 0.
[LINK: shader stage output](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
[LINK: blend_src](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
- If usesDualSourceBlending is true : descriptor . targets . size must be 1. All the shader stage outputs with location in entryPoint must be in one
struct and use dual source blending .
If usesDualSourceBlending is true :
- descriptor . targets . size must be 1.
descriptor . targets . size must be 1.
- All the shader stage outputs with location in entryPoint must be in one
struct and use dual source blending .
All the shader stage outputs with location in entryPoint must be in one
struct and use dual source blending .
[LINK: shader stage outputs](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
[LINK: use dual source blending](https://gpuweb.github.io/gpuweb/wgsl/#use-dual-source-blending)
- Validating GPUFragmentState’s color attachment bytes per sample ( device , descriptor . targets ) succeeds.
Validating GPUFragmentState’s color attachment bytes per sample ( device , descriptor . targets ) succeeds.
- If device . [[features]] does not contain "core-features-and-limits" : All non-null GPUColorTargetState s colorState in descriptor . targets must have equal values for each
of the following members: colorState . blend . color colorState . blend . alpha colorState . writeMask For each function in the functions in the shader stage rooted at entryPoint : function must not be dpdxFine , dpdyFine , or fwidthFine .
- All non-null GPUColorTargetState s colorState in descriptor . targets must have equal values for each
of the following members: colorState . blend . color colorState . blend . alpha colorState . writeMask
All non-null GPUColorTargetState s colorState in descriptor . targets must have equal values for each
of the following members:
- colorState . blend . color
colorState . blend . color
- colorState . blend . alpha
colorState . blend . alpha
- colorState . writeMask
colorState . writeMask
- For each function in the functions in the shader stage rooted at entryPoint : function must not be dpdxFine , dpdyFine , or fwidthFine .
For each function in the functions in the shader stage rooted at entryPoint :
[LINK: functions in the shader stage](https://gpuweb.github.io/gpuweb/wgsl/#functions-in-a-shader-stage)
- function must not be dpdxFine , dpdyFine , or fwidthFine .
function must not be dpdxFine , dpdyFine , or fwidthFine .
[LINK: dpdxFine](https://gpuweb.github.io/gpuweb/wgsl/#dpdxFine-builtin)
[LINK: dpdyFine](https://gpuweb.github.io/gpuweb/wgsl/#dpdyFine-builtin)
[LINK: fwidthFine](https://gpuweb.github.io/gpuweb/wgsl/#fwidthFine-builtin)
Arguments:
- GPUDevice device
GPUDevice device
- sequence < GPUColorTargetState ?> targets
sequence < GPUColorTargetState ?> targets
Device timeline steps:
- Let formats be an empty list < GPUTextureFormat ?>
Let formats be an empty list < GPUTextureFormat ?>
- For each target in targets : If target is undefined , continue. Append target . format to formats .
For each target in targets :
- If target is undefined , continue.
If target is undefined , continue.
- Append target . format to formats .
Append target . format to formats .
- Calculating color attachment bytes per sample ( formats ) must be ≤ device . [[limits]] . maxColorAttachmentBytesPerSample .
Calculating color attachment bytes per sample ( formats ) must be ≤ device . [[limits]] . maxColorAttachmentBytesPerSample .
Note: The fragment shader may output more values than what the pipeline uses. If that is the case
the values are ignored.
- If component . operation is "min" or "max" : component . srcFactor and component . dstFactor must both be "one" .
If component . operation is "min" or "max" :
- component . srcFactor and component . dstFactor must both be "one" .
component . srcFactor and component . dstFactor must both be "one" .
- If component . srcFactor or component . dstFactor requires a feature according to the GPUBlendFactor table and device . [[features]] does not contain the feature: Throw a TypeError .
If component . srcFactor or component . dstFactor requires a feature according to the GPUBlendFactor table and device . [[features]] does not contain the feature:
- Throw a TypeError .
Throw a TypeError .
The GPUTextureFormat of this color target. The pipeline will only be compatible with GPURenderPassEncoder s which use a GPUTextureView of this format in the
corresponding color attachment.
The blending behavior for this color target. If left undefined, disables blending for this
color target.
Bitmask controlling which channels are are written to when drawing to this color target.
Defines the blending behavior of the corresponding render target for color channels.
Defines the blending behavior of the corresponding render target for the alpha channel.
GPUBlendComponent has the following members, which describe how the color or alpha components
of a fragment are blended:
Defines the GPUBlendOperation used to calculate the values written to the target
attachment components.
Defines the GPUBlendFactor operation to be performed on values from the fragment shader.
Defines the GPUBlendFactor operation to be performed on values from the target attachment.
The following tables use this notation to describe color components for a given fragment
location:
[LINK: "@blend_src" attribute](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
GPUBlendFactor defines how either a source or destination blend factors is calculated:
GPUBlendOperation defines the algorithm used to combine source and destination blend factors:
GPUDepthStencilState has the following members, which describe how a GPURenderPipeline will affect a render pass’s depthStencilAttachment :
The format of depthStencilAttachment this GPURenderPipeline will be compatible with.
Indicates if this GPURenderPipeline can modify depthStencilAttachment depth values.
The comparison operation used to test fragment depths against depthStencilAttachment depth values.
Defines how stencil comparisons and operations are performed for front-facing primitives.
Defines how stencil comparisons and operations are performed for back-facing primitives.
Bitmask controlling which depthStencilAttachment stencil value
bits are read when performing stencil comparison tests.
Bitmask controlling which depthStencilAttachment stencil value
bits are written to when performing stencil operations.
Constant depth bias added to each triangle fragment. See biased fragment depth for details.
Depth bias that scales with the triangle fragment’s slope. See biased fragment depth for details.
The maximum depth bias of a triangle fragment. See biased fragment depth for details.
Note: depthBias , depthBiasSlopeScale , and depthBiasClamp have no effect on "point-list" , "line-list" , and "line-strip" primitives, and
must be 0.
- Let format be attachment . view . format .
Let format be attachment . view . format .
- Let r be the minimum positive representable value > 0 in the format converted to a 32-bit float.
Let r be the minimum positive representable value > 0 in the format converted to a 32-bit float.
- Let maxDepthSlope be the maximum of the horizontal and vertical slopes of the fragment’s depth value.
Let maxDepthSlope be the maximum of the horizontal and vertical slopes of the fragment’s depth value.
- If format is a unorm format: Let bias be (float) state . depthBias * r + state . depthBiasSlopeScale * maxDepthSlope . Otherwise, if format is a float format: Let bias be (float) state . depthBias * 2^(exp(max depth in primitive) - r ) + state . depthBiasSlopeScale * maxDepthSlope .
If format is a unorm format:
- Let bias be (float) state . depthBias * r + state . depthBiasSlopeScale * maxDepthSlope .
Let bias be (float) state . depthBias * r + state . depthBiasSlopeScale * maxDepthSlope .
Otherwise, if format is a float format:
- Let bias be (float) state . depthBias * 2^(exp(max depth in primitive) - r ) + state . depthBiasSlopeScale * maxDepthSlope .
Let bias be (float) state . depthBias * 2^(exp(max depth in primitive) - r ) + state . depthBiasSlopeScale * maxDepthSlope .
- If state . depthBiasClamp > 0 : Set bias to min( state . depthBiasClamp , bias ) . Otherwise, if state . depthBiasClamp < 0 : Set bias to max( state . depthBiasClamp , bias ) .
If state . depthBiasClamp > 0 :
- Set bias to min( state . depthBiasClamp , bias ) .
Set bias to min( state . depthBiasClamp , bias ) .
Otherwise, if state . depthBiasClamp < 0 :
- Set bias to max( state . depthBiasClamp , bias ) .
Set bias to max( state . depthBiasClamp , bias ) .
- If state . depthBias ≠ 0 or state . depthBiasSlopeScale ≠ 0 : Set the fragment depth value to fragment depth value + bias
If state . depthBias ≠ 0 or state . depthBiasSlopeScale ≠ 0 :
- Set the fragment depth value to fragment depth value + bias
Set the fragment depth value to fragment depth value + bias
Arguments:
- GPUDevice device
GPUDevice device
- GPUDepthStencilState descriptor
GPUDepthStencilState descriptor
- GPUPrimitiveTopology topology
GPUPrimitiveTopology topology
Device timeline steps:
- Return true if, and only if, all of the following conditions are satisfied: descriptor . format is a depth-or-stencil format . If descriptor . depthWriteEnabled is true or descriptor . depthCompare is provided and not "always" : descriptor . format must have a depth component. If descriptor . stencilFront or descriptor . stencilBack are not the default values: descriptor . format must have a stencil component. If descriptor . format has a depth component: descriptor . depthWriteEnabled must be provided . descriptor . depthCompare must be provided if: descriptor . depthWriteEnabled is true , or descriptor . stencilFront . depthFailOp is not "keep" , or descriptor . stencilBack . depthFailOp is not "keep" . If topology is "point-list" , "line-list" , or "line-strip" : descriptor . depthBias must be 0. descriptor . depthBiasSlopeScale must be 0. descriptor . depthBiasClamp must be 0. If device . [[features]] does not contain "core-features-and-limits" : descriptor . depthBiasClamp must be 0.
Return true if, and only if, all of the following conditions are satisfied:
- descriptor . format is a depth-or-stencil format .
descriptor . format is a depth-or-stencil format .
- If descriptor . depthWriteEnabled is true or descriptor . depthCompare is provided and not "always" : descriptor . format must have a depth component.
If descriptor . depthWriteEnabled is true or descriptor . depthCompare is provided and not "always" :
- descriptor . format must have a depth component.
descriptor . format must have a depth component.
- If descriptor . stencilFront or descriptor . stencilBack are not the default values: descriptor . format must have a stencil component.
If descriptor . stencilFront or descriptor . stencilBack are not the default values:
- descriptor . format must have a stencil component.
descriptor . format must have a stencil component.
- If descriptor . format has a depth component: descriptor . depthWriteEnabled must be provided . descriptor . depthCompare must be provided if: descriptor . depthWriteEnabled is true , or descriptor . stencilFront . depthFailOp is not "keep" , or descriptor . stencilBack . depthFailOp is not "keep" .
If descriptor . format has a depth component:
- descriptor . depthWriteEnabled must be provided .
descriptor . depthWriteEnabled must be provided .
- descriptor . depthCompare must be provided if: descriptor . depthWriteEnabled is true , or descriptor . stencilFront . depthFailOp is not "keep" , or descriptor . stencilBack . depthFailOp is not "keep" .
descriptor . depthCompare must be provided if:
- descriptor . depthWriteEnabled is true , or
descriptor . depthWriteEnabled is true , or
- descriptor . stencilFront . depthFailOp is not "keep" , or
descriptor . stencilFront . depthFailOp is not "keep" , or
- descriptor . stencilBack . depthFailOp is not "keep" .
descriptor . stencilBack . depthFailOp is not "keep" .
- If topology is "point-list" , "line-list" , or "line-strip" : descriptor . depthBias must be 0. descriptor . depthBiasSlopeScale must be 0. descriptor . depthBiasClamp must be 0.
If topology is "point-list" , "line-list" , or "line-strip" :
- descriptor . depthBias must be 0.
descriptor . depthBias must be 0.
- descriptor . depthBiasSlopeScale must be 0.
descriptor . depthBiasSlopeScale must be 0.
- descriptor . depthBiasClamp must be 0.
descriptor . depthBiasClamp must be 0.
- If device . [[features]] does not contain "core-features-and-limits" : descriptor . depthBiasClamp must be 0.
- descriptor . depthBiasClamp must be 0.
descriptor . depthBiasClamp must be 0.
GPUStencilFaceState has the following members, which describe how stencil comparisons and
operations are performed:
The GPUCompareFunction used when testing the [[stencilReference]] value
against the fragment’s depthStencilAttachment stencil values.
The GPUStencilOperation performed if the fragment stencil comparison test described by compare fails.
The GPUStencilOperation performed if the fragment depth comparison described by depthCompare fails.
The GPUStencilOperation performed if the fragment stencil comparison test described by compare passes.
GPUStencilOperation defines the following operations:
Keep the current stencil value.
Set the stencil value to 0 .
Set the stencil value to [[stencilReference]] .
Bitwise-invert the current stencil value.
Increments the current stencil value, clamping to the maximum representable value of the depthStencilAttachment ’s stencil aspect.
Decrement the current stencil value, clamping to 0 .
Increments the current stencil value, wrapping to zero if the value exceeds the maximum
representable value of the depthStencilAttachment ’s stencil
aspect.
Decrement the current stencil value, wrapping to the maximum representable value of the depthStencilAttachment ’s stencil aspect if the value goes below 0 .
The index format determines both the data type of index values in a buffer and, when used with
strip primitive topologies ( "line-strip" or "triangle-strip" ) also specifies the primitive restart value. The primitive restart value indicates which index value indicates that a new primitive
should be started rather than continuing to construct the triangle strip with the prior indexed
vertices.
GPUPrimitiveState s that specify a strip primitive topology must specify a stripIndexFormat if they are used for indexed draws
so that the primitive restart value that will be used is known at pipeline
creation time. GPUPrimitiveState s that specify a list primitive
topology will use the index format passed to setIndexBuffer() when doing indexed rendering.
The GPUVertexFormat of a vertex attribute indicates how data from a vertex buffer will
be interpreted and exposed to the shader. The name of the format specifies the order of components,
bits per component, and vertex data type for the component.
Each vertex data type can map to any WGSL scalar type of the same base type,
regardless of the bits per component:
[LINK: WGSL scalar type](https://gpuweb.github.io/gpuweb/wgsl/#scalar-types)
The multi-component formats specify the number of components after "x". Mismatches in the number of
components between the vertex format and shader type are allowed, with components being either
dropped or filled with default values to compensate.
See § 23.2.2 Vertex Processing for additional information about how vertex formats are exposed in the
shader.
The step mode configures how an address for vertex buffer data is computed, based on the
current vertex or instance index:
The address is advanced by arrayStride for each vertex,
and reset between instances.
The address is advanced by arrayStride for each instance.
A list of GPUVertexBufferLayout s, each defining the layout of vertex attribute data in a
vertex buffer used by this pipeline.
A vertex buffer is, conceptually, a view into buffer memory as an array of structures . arrayStride is the stride, in bytes, between elements of that array.
Each element of a vertex buffer is like a structure with a memory layout defined by its attributes , which describe the members of the structure.
Each GPUVertexAttribute describes its format and its offset , in bytes, within the structure.
Each attribute appears as a separate input in a vertex shader, each bound by a numeric location ,
which is specified by shaderLocation .
Every location must be unique within the GPUVertexState .
The stride, in bytes, between elements of this array.
Whether each element of this array represents per-vertex data or per-instance data
An array defining the layout of the vertex attributes within each element.
The GPUVertexFormat of the attribute.
The offset, in bytes, from the beginning of the element to the data for the attribute.
The numeric location associated with this attribute, which will correspond with a "@location" attribute declared in the vertex . module .
[LINK: "@location" attribute](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
Arguments:
- GPUDevice device
GPUDevice device
- GPUVertexBufferLayout descriptor
GPUVertexBufferLayout descriptor
Device timeline steps:
- Return true , if and only if, all of the following conditions are satisfied: descriptor . arrayStride ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride . descriptor . arrayStride is a multiple of 4. For each attribute attrib in the list descriptor . attributes : If descriptor . arrayStride is zero: attrib . offset + byteSize ( attrib . format ) ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride . Otherwise: attrib . offset + byteSize ( attrib . format ) ≤ descriptor . arrayStride . attrib . offset is a multiple of the minimum of 4 and byteSize ( attrib . format ). attrib . shaderLocation is < device . [[device]] . [[limits]] . maxVertexAttributes .
Return true , if and only if, all of the following conditions are satisfied:
- descriptor . arrayStride ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride .
descriptor . arrayStride ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride .
- descriptor . arrayStride is a multiple of 4.
descriptor . arrayStride is a multiple of 4.
- For each attribute attrib in the list descriptor . attributes : If descriptor . arrayStride is zero: attrib . offset + byteSize ( attrib . format ) ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride . Otherwise: attrib . offset + byteSize ( attrib . format ) ≤ descriptor . arrayStride . attrib . offset is a multiple of the minimum of 4 and byteSize ( attrib . format ). attrib . shaderLocation is < device . [[device]] . [[limits]] . maxVertexAttributes .
For each attribute attrib in the list descriptor . attributes :
- If descriptor . arrayStride is zero: attrib . offset + byteSize ( attrib . format ) ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride . Otherwise: attrib . offset + byteSize ( attrib . format ) ≤ descriptor . arrayStride .
If descriptor . arrayStride is zero:
- attrib . offset + byteSize ( attrib . format ) ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride .
attrib . offset + byteSize ( attrib . format ) ≤ device . [[device]] . [[limits]] . maxVertexBufferArrayStride .
Otherwise:
- attrib . offset + byteSize ( attrib . format ) ≤ descriptor . arrayStride .
attrib . offset + byteSize ( attrib . format ) ≤ descriptor . arrayStride .
- attrib . offset is a multiple of the minimum of 4 and byteSize ( attrib . format ).
attrib . offset is a multiple of the minimum of 4 and byteSize ( attrib . format ).
- attrib . shaderLocation is < device . [[device]] . [[limits]] . maxVertexAttributes .
attrib . shaderLocation is < device . [[device]] . [[limits]] . maxVertexAttributes .
Arguments:
- GPUDevice device
GPUDevice device
- GPUVertexState descriptor
GPUVertexState descriptor
- GPUPipelineLayout layout
GPUPipelineLayout layout
Device timeline steps:
- Let entryPoint be get the entry point ( VERTEX , descriptor ).
Let entryPoint be get the entry point ( VERTEX , descriptor ).
- Assert entryPoint is not null .
Assert entryPoint is not null .
- All of the requirements in the following steps must be met. validating GPUProgrammableStage ( VERTEX , descriptor , layout , device ) must succeed. descriptor . buffers . size must be ≤ device . [[device]] . [[limits]] . maxVertexBuffers . Each vertexBuffer layout descriptor in the list descriptor . buffers must pass validating GPUVertexBufferLayout ( device , vertexBuffer ). Let totalEffectiveVertexAttributes be the sum of vertexBuffer . attributes . size ,
over every vertexBuffer in descriptor . buffers . If device . [[features]] does not contain "core-features-and-limits" : If the vertex_index builtin is a shader stage input of descriptor . vertex : Add 1 to totalEffectiveVertexAttributes If the instance_index builtin is a shader stage input of descriptor . vertex : Add 1 to totalEffectiveVertexAttributes totalEffectiveVertexAttributes must be ≤ device . [[device]] . [[limits]] . maxVertexAttributes . For every vertex attribute declaration (at location location with type T ) that is statically used by entryPoint , there must be exactly one pair ( i , j ) for which descriptor . buffers [ i ]?. attributes [ j ]. shaderLocation == location . Let attrib be that GPUVertexAttribute . T must be compatible with attrib . format ’s vertex data type : "unorm", "snorm", or "float" T must be f32 or vecN<f32> . "uint" T must be u32 or vecN<u32> . "sint" T must be i32 or vecN<i32> .
All of the requirements in the following steps must be met.
- validating GPUProgrammableStage ( VERTEX , descriptor , layout , device ) must succeed.
validating GPUProgrammableStage ( VERTEX , descriptor , layout , device ) must succeed.
- descriptor . buffers . size must be ≤ device . [[device]] . [[limits]] . maxVertexBuffers .
descriptor . buffers . size must be ≤ device . [[device]] . [[limits]] . maxVertexBuffers .
- Each vertexBuffer layout descriptor in the list descriptor . buffers must pass validating GPUVertexBufferLayout ( device , vertexBuffer ).
Each vertexBuffer layout descriptor in the list descriptor . buffers must pass validating GPUVertexBufferLayout ( device , vertexBuffer ).
- Let totalEffectiveVertexAttributes be the sum of vertexBuffer . attributes . size ,
over every vertexBuffer in descriptor . buffers .
Let totalEffectiveVertexAttributes be the sum of vertexBuffer . attributes . size ,
over every vertexBuffer in descriptor . buffers .
- If device . [[features]] does not contain "core-features-and-limits" : If the vertex_index builtin is a shader stage input of descriptor . vertex : Add 1 to totalEffectiveVertexAttributes If the instance_index builtin is a shader stage input of descriptor . vertex : Add 1 to totalEffectiveVertexAttributes
- If the vertex_index builtin is a shader stage input of descriptor . vertex : Add 1 to totalEffectiveVertexAttributes
If the vertex_index builtin is a shader stage input of descriptor . vertex :
[LINK: vertex_index](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-vertex_index)
[LINK: shader stage input](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-input)
- Add 1 to totalEffectiveVertexAttributes
Add 1 to totalEffectiveVertexAttributes
- If the instance_index builtin is a shader stage input of descriptor . vertex : Add 1 to totalEffectiveVertexAttributes
If the instance_index builtin is a shader stage input of descriptor . vertex :
[LINK: instance_index](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-instance_index)
[LINK: shader stage input](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-input)
- Add 1 to totalEffectiveVertexAttributes
Add 1 to totalEffectiveVertexAttributes
- totalEffectiveVertexAttributes must be ≤ device . [[device]] . [[limits]] . maxVertexAttributes .
totalEffectiveVertexAttributes must be ≤ device . [[device]] . [[limits]] . maxVertexAttributes .
- For every vertex attribute declaration (at location location with type T ) that is statically used by entryPoint , there must be exactly one pair ( i , j ) for which descriptor . buffers [ i ]?. attributes [ j ]. shaderLocation == location . Let attrib be that GPUVertexAttribute .
For every vertex attribute declaration (at location location with type T ) that is statically used by entryPoint , there must be exactly one pair ( i , j ) for which descriptor . buffers [ i ]?. attributes [ j ]. shaderLocation == location .
Let attrib be that GPUVertexAttribute .
- T must be compatible with attrib . format ’s vertex data type : "unorm", "snorm", or "float" T must be f32 or vecN<f32> . "uint" T must be u32 or vecN<u32> . "sint" T must be i32 or vecN<i32> .
T must be compatible with attrib . format ’s vertex data type :
T must be f32 or vecN<f32> .
T must be u32 or vecN<u32> .
T must be i32 or vecN<i32> .

## 11. Copies

### 11.1. Buffer Copies

Buffer copy operations operate on raw bytes.
WebGPU provides "buffered" GPUCommandEncoder commands:
- copyBufferToBuffer()
copyBufferToBuffer()
- clearBuffer()
clearBuffer()
and "immediate" GPUQueue operations:
- writeBuffer() , for ArrayBuffer -to- GPUBuffer writes
writeBuffer() , for ArrayBuffer -to- GPUBuffer writes

### 11.2. Texel Copies

Texel copy operations operate on texture/"image" data, rather than bytes.
WebGPU provides "buffered" GPUCommandEncoder commands:
- copyTextureToTexture()
copyTextureToTexture()
- copyBufferToTexture()
copyBufferToTexture()
- copyTextureToBuffer()
copyTextureToBuffer()
and "immediate" GPUQueue operations:
- writeTexture() , for ArrayBuffer -to- GPUTexture writes
writeTexture() , for ArrayBuffer -to- GPUTexture writes
- copyExternalImageToTexture() , for copies from Web Platform image sources to textures
copyExternalImageToTexture() , for copies from Web Platform image sources to textures
Texel copies only guarantee that valid, finite, non-subnormal numeric values
    in the source have the same numeric value in the destination.
    Specifically, the texel block may be decoded and re-encoded in a way that
    preserves only those values.
    Where multiple byte representations are possible, the choice of representation is implementation-defined.
- Any floating-point zero value may be represented as either -0.0 or +0.0.
Any floating-point zero value may be represented as either -0.0 or +0.0.
- Any floating-point subnormal value may be either preserved or replaced by -0.0 or +0.0.
Any floating-point subnormal value may be either preserved or replaced by -0.0 or +0.0.
- Any floating-point NaN or Infinity value may be replaced by an indeterminate value .
Any floating-point NaN or Infinity value may be replaced by an indeterminate value .
[LINK: indeterminate value](https://gpuweb.github.io/gpuweb/wgsl/#indeterminate-values)
- Packed formats and snorm formats may change bit-representation as long
as the represented values follow the rules above, for example: snorm formats may represent -1.0 as either -127 or -128. Formats like "rgb9e5ufloat" have multiple bit-representations of some values.
Packed formats and snorm formats may change bit-representation as long
as the represented values follow the rules above, for example:
- snorm formats may represent -1.0 as either -127 or -128.
snorm formats may represent -1.0 as either -127 or -128.
- Formats like "rgb9e5ufloat" have multiple bit-representations of some values.
Formats like "rgb9e5ufloat" have multiple bit-representations of some values.
Note: For formats supporting RENDER_ATTACHMENT or STORAGE_BINDING , this can be thought of as similar to,
    and may be implemented as, writing the texture using a WGSL shader.
    In general, any WGSL floating point behaviors may be observed.
[LINK: WGSL floating point behaviors](https://gpuweb.github.io/gpuweb/wgsl/#differences-from-ieee754)
The following definitions are used by these methods:
" GPUTexelCopyBufferLayout " describes the " layout " of texels in a " buffer " of bytes
( GPUBuffer or AllowSharedBufferSource ) in a " texel copy " operation.
A texel image is comprised of one or more rows of texel blocks , referred to here
as texel block row s. Each texel block row of a texel image must contain the
same number of texel blocks , and all texel blocks in a texel image are of the same GPUTextureFormat .
A GPUTexelCopyBufferLayout is a layout of texel images within some linear memory.
It’s used when copying data between a texture and a GPUBuffer , or when scheduling a
write into a texture from the GPUQueue .
- For 2d textures, data is copied between one or multiple contiguous texel images and array layers .
For 2d textures, data is copied between one or multiple contiguous texel images and array layers .
- For 3d textures, data is copied between one or multiple contiguous texel images and depth slices .
For 3d textures, data is copied between one or multiple contiguous texel images and depth slices .
Operations that copy between byte arrays and textures always operate on whole texel block .
It’s not possible to update only a part of a texel block .
Texel blocks are tightly packed within each texel block row in the linear memory layout of a texel copy , with each subsequent texel block immediately following the previous texel block ,
with no padding.
This includes copies to/from specific aspects of depth-or-stencil format textures:
stencil values are tightly packed in an array of bytes;
depth values are tightly packed in an array of the appropriate type ("depth16unorm" or "depth32float").
The offset, in bytes, from the beginning of the texel data source (such as a GPUTexelCopyBufferInfo.buffer ) to the start of the texel data
within that source.
The stride, in bytes, between the beginning of each texel block row and the subsequent texel block row .
Required if there are multiple texel block rows (i.e. the copy height or depth is more
than one block).
Number of texel block rows per single texel image of the texture . rowsPerImage × bytesPerRow is the stride, in bytes, between the beginning of each texel image of data and the subsequent texel image .
Required if there are multiple texel images (i.e. the copy depth is more than one).
" GPUTexelCopyBufferInfo " describes the " info " ( GPUBuffer and GPUTexelCopyBufferLayout )
about a " buffer " source or destination of a " texel copy " operation.
Together with the copySize , it describes the footprint of a region of texels in a GPUBuffer .
A buffer which either contains texel data to be copied or will store the texel data being
copied, depending on the method it is being passed to.
Arguments:
- GPUTexelCopyBufferInfo imageCopyBuffer
GPUTexelCopyBufferInfo imageCopyBuffer
Returns: boolean
Device timeline steps:
- Return true if and only if all of the following conditions are satisfied: imageCopyBuffer . buffer must be a valid GPUBuffer . imageCopyBuffer . bytesPerRow must be a multiple of 256.
Return true if and only if all of the following conditions are satisfied:
- imageCopyBuffer . buffer must be a valid GPUBuffer .
imageCopyBuffer . buffer must be a valid GPUBuffer .
[LINK: valid](https://w3c.github.io/i18n-glossary/#dfn-valid)
- imageCopyBuffer . bytesPerRow must be a multiple of 256.
imageCopyBuffer . bytesPerRow must be a multiple of 256.
" GPUTexelCopyTextureInfo " describes the " info " ( GPUTexture , etc.)
about a " texture " source or destination of a " texel copy " operation.
Together with the copySize , it describes a sub-region of a texture
(spanning one or more contiguous texture subresources at the same mip-map level).
Texture to copy to/from.
Mip-map level of the texture to copy to/from.
Defines the origin of the copy - the minimum corner of the texture sub-region to copy to/from.
Together with copySize , defines the full copy sub-region.
Defines which aspects of the texture to copy to/from.
- Let texture be copyTexture . texture .
Let texture be copyTexture . texture .
- If texture . dimension is: 1d Assert index is 0 Let depthSliceOrLayer be texture 2d Let depthSliceOrLayer be array layer index of texture 3d Let depthSliceOrLayer be depth slice index of texture
If texture . dimension is:
- Assert index is 0
Assert index is 0
- Let depthSliceOrLayer be texture
Let depthSliceOrLayer be texture
Let depthSliceOrLayer be array layer index of texture
Let depthSliceOrLayer be depth slice index of texture
- Let textureMip be mip level copyTexture . mipLevel of depthSliceOrLayer .
Let textureMip be mip level copyTexture . mipLevel of depthSliceOrLayer .
- Return aspect copyTexture . aspect of textureMip .
Return aspect copyTexture . aspect of textureMip .
- Let blockBytes be the texel block copy footprint of texture . format .
Let blockBytes be the texel block copy footprint of texture . format .
- Let imageOffset be ( z × bufferLayout . rowsPerImage × bufferLayout . bytesPerRow ) + bufferLayout . offset .
Let imageOffset be ( z × bufferLayout . rowsPerImage × bufferLayout . bytesPerRow ) + bufferLayout . offset .
- Let rowOffset be ( y × bufferLayout . bytesPerRow ) + imageOffset .
Let rowOffset be ( y × bufferLayout . bytesPerRow ) + imageOffset .
- Let blockOffset be ( x × blockBytes ) + rowOffset .
Let blockOffset be ( x × blockBytes ) + rowOffset .
- Return blockOffset .
Return blockOffset .
Arguments:
- GPUTexelCopyTextureInfo texelCopyTextureInfo
GPUTexelCopyTextureInfo texelCopyTextureInfo
- GPUExtent3D copySize
GPUExtent3D copySize
Returns: boolean
Device timeline steps:
- Let blockWidth be the texel block width of texelCopyTextureInfo . texture . format .
Let blockWidth be the texel block width of texelCopyTextureInfo . texture . format .
- Let blockHeight be the texel block height of texelCopyTextureInfo . texture . format .
Let blockHeight be the texel block height of texelCopyTextureInfo . texture . format .
- Return true if and only if all of the following conditions apply: validating texture copy range ( texelCopyTextureInfo , copySize ) returns true . texelCopyTextureInfo . texture must be a valid GPUTexture . texelCopyTextureInfo . mipLevel must be < texelCopyTextureInfo . texture . mipLevelCount . texelCopyTextureInfo . origin . x must be a multiple of blockWidth . texelCopyTextureInfo . origin . y must be a multiple of blockHeight . The GPUTexelCopyTextureInfo physical subresource size of texelCopyTextureInfo is equal to copySize if either of
the following conditions is true: texelCopyTextureInfo . texture . format is a depth-stencil format. texelCopyTextureInfo . texture . sampleCount > 1.
Return true if and only if all of the following conditions apply:
- validating texture copy range ( texelCopyTextureInfo , copySize ) returns true .
validating texture copy range ( texelCopyTextureInfo , copySize ) returns true .
- texelCopyTextureInfo . texture must be a valid GPUTexture .
texelCopyTextureInfo . texture must be a valid GPUTexture .
[LINK: valid](https://w3c.github.io/i18n-glossary/#dfn-valid)
- texelCopyTextureInfo . mipLevel must be < texelCopyTextureInfo . texture . mipLevelCount .
texelCopyTextureInfo . mipLevel must be < texelCopyTextureInfo . texture . mipLevelCount .
- texelCopyTextureInfo . origin . x must be a multiple of blockWidth .
texelCopyTextureInfo . origin . x must be a multiple of blockWidth .
- texelCopyTextureInfo . origin . y must be a multiple of blockHeight .
texelCopyTextureInfo . origin . y must be a multiple of blockHeight .
- The GPUTexelCopyTextureInfo physical subresource size of texelCopyTextureInfo is equal to copySize if either of
the following conditions is true: texelCopyTextureInfo . texture . format is a depth-stencil format. texelCopyTextureInfo . texture . sampleCount > 1.
The GPUTexelCopyTextureInfo physical subresource size of texelCopyTextureInfo is equal to copySize if either of
the following conditions is true:
- texelCopyTextureInfo . texture . format is a depth-stencil format.
texelCopyTextureInfo . texture . format is a depth-stencil format.
- texelCopyTextureInfo . texture . sampleCount > 1.
texelCopyTextureInfo . texture . sampleCount > 1.
Arguments:
- GPUTexelCopyTextureInfo texelCopyTextureInfo
GPUTexelCopyTextureInfo texelCopyTextureInfo
- GPUTexelCopyBufferLayout bufferLayout
GPUTexelCopyBufferLayout bufferLayout
- GPUSize64Out dataLength
GPUSize64Out dataLength
- GPUExtent3D copySize
GPUExtent3D copySize
- GPUTextureUsage textureUsage
GPUTextureUsage textureUsage
- boolean aligned
boolean aligned
Returns: boolean
Device timeline steps:
- Let texture be texelCopyTextureInfo . texture
Let texture be texelCopyTextureInfo . texture
- Let aspectSpecificFormat = texture . format .
Let aspectSpecificFormat = texture . format .
- Let offsetAlignment = texel block copy footprint of texture . format .
Let offsetAlignment = texel block copy footprint of texture . format .
- Return true if and only if all of the following conditions apply: validating GPUTexelCopyTextureInfo ( texelCopyTextureInfo , copySize ) returns true . texture . sampleCount is 1. texture . usage contains textureUsage . If texture . format is a depth-or-stencil format format: texelCopyTextureInfo . aspect must refer to a single aspect of texture . format . If textureUsage is: COPY_SRC That aspect must be a valid texel copy source according to § 26.1.2 Depth-stencil formats . COPY_DST That aspect must be a valid texel copy destination according to § 26.1.2 Depth-stencil formats . Set aspectSpecificFormat to the aspect-specific format according to § 26.1.2 Depth-stencil formats . Set offsetAlignment to 4. If aligned is true : bufferLayout . offset is a multiple of offsetAlignment . validating linear texture data ( bufferLayout , dataLength , aspectSpecificFormat , copySize ) succeeds.
Return true if and only if all of the following conditions apply:
- validating GPUTexelCopyTextureInfo ( texelCopyTextureInfo , copySize ) returns true .
validating GPUTexelCopyTextureInfo ( texelCopyTextureInfo , copySize ) returns true .
- texture . sampleCount is 1.
texture . sampleCount is 1.
- texture . usage contains textureUsage .
texture . usage contains textureUsage .
- If texture . format is a depth-or-stencil format format: texelCopyTextureInfo . aspect must refer to a single aspect of texture . format . If textureUsage is: COPY_SRC That aspect must be a valid texel copy source according to § 26.1.2 Depth-stencil formats . COPY_DST That aspect must be a valid texel copy destination according to § 26.1.2 Depth-stencil formats . Set aspectSpecificFormat to the aspect-specific format according to § 26.1.2 Depth-stencil formats . Set offsetAlignment to 4.
If texture . format is a depth-or-stencil format format:
- texelCopyTextureInfo . aspect must refer to a single aspect of texture . format .
texelCopyTextureInfo . aspect must refer to a single aspect of texture . format .
- If textureUsage is: COPY_SRC That aspect must be a valid texel copy source according to § 26.1.2 Depth-stencil formats . COPY_DST That aspect must be a valid texel copy destination according to § 26.1.2 Depth-stencil formats .
If textureUsage is:
That aspect must be a valid texel copy source according to § 26.1.2 Depth-stencil formats .
That aspect must be a valid texel copy destination according to § 26.1.2 Depth-stencil formats .
- Set aspectSpecificFormat to the aspect-specific format according to § 26.1.2 Depth-stencil formats .
Set aspectSpecificFormat to the aspect-specific format according to § 26.1.2 Depth-stencil formats .
- Set offsetAlignment to 4.
Set offsetAlignment to 4.
- If aligned is true : bufferLayout . offset is a multiple of offsetAlignment .
If aligned is true :
- bufferLayout . offset is a multiple of offsetAlignment .
bufferLayout . offset is a multiple of offsetAlignment .
- validating linear texture data ( bufferLayout , dataLength , aspectSpecificFormat , copySize ) succeeds.
validating linear texture data ( bufferLayout , dataLength , aspectSpecificFormat , copySize ) succeeds.
WebGPU textures hold raw numeric data, and are not tagged with semantic metadata describing colors.
However, copyExternalImageToTexture() copies from sources that describe colors.
" GPUCopyExternalImageDestInfo " describes the " info " about the " dest ination" of a
" copyExternalImage ToTexture() " operation.
It is a GPUTexelCopyTextureInfo which is additionally tagged with
color space/encoding and alpha-premultiplication metadata, so that semantic color data may be
preserved during copies.
This metadata affects only the semantics of the copy operation
operation, not the state or semantics of the destination texture object.
Describes the color space and encoding used to encode data into the destination texture.
This may result in values outside of the range [0, 1]
being written to the target texture, if its format can represent them.
Otherwise, the results are clamped to the target texture format’s range.
Note: If colorSpace matches the source image,
conversion might not be necessary. See § 3.11.2 Color Space Conversion Elision .
Describes whether the data written into the texture should have its RGB channels
premultiplied by the alpha channel, or not.
If this option is set to true and the source is also
premultiplied, the source RGB values must be preserved even if they exceed their
corresponding alpha values.
Note: If premultipliedAlpha matches the source image,
conversion might not be necessary. See § 3.11.2 Color Space Conversion Elision .
" GPUCopyExternalImageSourceInfo " describes the " info " about the " source " of a
" copyExternalImage ToTexture() " operation.
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
GPUCopyExternalImageSourceInfo has the following members:
The source of the texel copy . The copy source data is captured at the moment that copyExternalImageToTexture() is issued. Source size is determined as described
by the external source dimensions table.
Defines the origin of the copy - the minimum (top-left) corner of the source sub-region to copy from.
Together with copySize , defines the full copy sub-region.
Describes whether the source image is vertically flipped, or not.
If this option is set to true , the copy is flipped vertically: the bottom row of the source
region is copied into the first row of the destination region, and so on.
The origin option is still relative to the top-left corner
of the source image, increasing downward.
When external sources are used when creating or copying to textures, the external source dimensions are defined by the source type, given by this table:
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
[LINK: VideoFrame.displayWidth](https://w3c.github.io/webcodecs/#dom-videoframe-displaywidth)
[LINK: VideoFrame.displayHeight](https://w3c.github.io/webcodecs/#dom-videoframe-displayheight)
Arguments:
- GPUTexelCopyTextureInfo texelCopyTextureInfo
GPUTexelCopyTextureInfo texelCopyTextureInfo
Returns: GPUExtent3D
The GPUTexelCopyTextureInfo physical subresource size of texelCopyTextureInfo is calculated as follows:
Its width , height and depthOrArrayLayers are the width, height, and depth, respectively,
    of the physical miplevel-specific texture extent of texelCopyTextureInfo . texture subresource at mipmap level texelCopyTextureInfo . mipLevel .
Arguments:
Layout of the linear texture data.
Total size of the linear data, in bytes.
Format of the texture.
Extent of the texture to copy.
Device timeline steps:
- Let: widthInBlocks be copyExtent . width ÷ the texel block width of format . Assert this is an integer. heightInBlocks be copyExtent . height ÷ the texel block height of format . Assert this is an integer. bytesInLastRow be widthInBlocks × the texel block copy footprint of format .
Let:
- widthInBlocks be copyExtent . width ÷ the texel block width of format . Assert this is an integer.
widthInBlocks be copyExtent . width ÷ the texel block width of format . Assert this is an integer.
- heightInBlocks be copyExtent . height ÷ the texel block height of format . Assert this is an integer.
heightInBlocks be copyExtent . height ÷ the texel block height of format . Assert this is an integer.
- bytesInLastRow be widthInBlocks × the texel block copy footprint of format .
bytesInLastRow be widthInBlocks × the texel block copy footprint of format .
- Fail if the following input validation requirements are not met: If heightInBlocks > 1, layout . bytesPerRow must be specified. If copyExtent . depthOrArrayLayers > 1, layout . bytesPerRow and layout . rowsPerImage must be specified. If specified, layout . bytesPerRow must be ≥ bytesInLastRow . If specified, layout . rowsPerImage must be ≥ heightInBlocks .
Fail if the following input validation requirements are not met:
- If heightInBlocks > 1, layout . bytesPerRow must be specified.
If heightInBlocks > 1, layout . bytesPerRow must be specified.
- If copyExtent . depthOrArrayLayers > 1, layout . bytesPerRow and layout . rowsPerImage must be specified.
If copyExtent . depthOrArrayLayers > 1, layout . bytesPerRow and layout . rowsPerImage must be specified.
- If specified, layout . bytesPerRow must be ≥ bytesInLastRow .
If specified, layout . bytesPerRow must be ≥ bytesInLastRow .
- If specified, layout . rowsPerImage must be ≥ heightInBlocks .
If specified, layout . rowsPerImage must be ≥ heightInBlocks .
- Let: bytesPerRow be layout . bytesPerRow ?? 0. rowsPerImage be layout . rowsPerImage ?? 0. Note: These default values have no effect, as they’re always multiplied by 0.
Let:
- bytesPerRow be layout . bytesPerRow ?? 0.
bytesPerRow be layout . bytesPerRow ?? 0.
- rowsPerImage be layout . rowsPerImage ?? 0.
rowsPerImage be layout . rowsPerImage ?? 0.
Note: These default values have no effect, as they’re always multiplied by 0.
- Let requiredBytesInCopy be 0.
Let requiredBytesInCopy be 0.
- If copyExtent . depthOrArrayLayers > 0: Increment requiredBytesInCopy by bytesPerRow × rowsPerImage × ( copyExtent . depthOrArrayLayers − 1). If heightInBlocks > 0: Increment requiredBytesInCopy by bytesPerRow × ( heightInBlocks − 1) + bytesInLastRow .
If copyExtent . depthOrArrayLayers > 0:
- Increment requiredBytesInCopy by bytesPerRow × rowsPerImage × ( copyExtent . depthOrArrayLayers − 1).
Increment requiredBytesInCopy by bytesPerRow × rowsPerImage × ( copyExtent . depthOrArrayLayers − 1).
- If heightInBlocks > 0: Increment requiredBytesInCopy by bytesPerRow × ( heightInBlocks − 1) + bytesInLastRow .
If heightInBlocks > 0:
- Increment requiredBytesInCopy by bytesPerRow × ( heightInBlocks − 1) + bytesInLastRow .
Increment requiredBytesInCopy by bytesPerRow × ( heightInBlocks − 1) + bytesInLastRow .
- Fail if the following condition is not satisfied: The layout fits inside the linear data: layout . offset + requiredBytesInCopy ≤ byteSize .
Fail if the following condition is not satisfied:
- The layout fits inside the linear data: layout . offset + requiredBytesInCopy ≤ byteSize .
The layout fits inside the linear data: layout . offset + requiredBytesInCopy ≤ byteSize .
Arguments:
The texture subresource being copied into and copy origin.
The size of the texture.
Device timeline steps:
- Let blockWidth be the texel block width of texelCopyTextureInfo . texture . format .
Let blockWidth be the texel block width of texelCopyTextureInfo . texture . format .
- Let blockHeight be the texel block height of texelCopyTextureInfo . texture . format .
Let blockHeight be the texel block height of texelCopyTextureInfo . texture . format .
- Let subresourceSize be the GPUTexelCopyTextureInfo physical subresource size of texelCopyTextureInfo .
Let subresourceSize be the GPUTexelCopyTextureInfo physical subresource size of texelCopyTextureInfo .
- Return whether all the conditions below are satisfied: ( texelCopyTextureInfo . origin . x + copySize . width ) ≤ subresourceSize . width ( texelCopyTextureInfo . origin . y + copySize . height ) ≤ subresourceSize . height ( texelCopyTextureInfo . origin . z + copySize . depthOrArrayLayers ) ≤ subresourceSize . depthOrArrayLayers copySize . width must be a multiple of blockWidth . copySize . height must be a multiple of blockHeight . Note: The texture copy range is validated against the physical (rounded-up)
    size for compressed formats , allowing copies to access texture
    blocks which are not fully inside the texture.
Return whether all the conditions below are satisfied:
- ( texelCopyTextureInfo . origin . x + copySize . width ) ≤ subresourceSize . width
( texelCopyTextureInfo . origin . x + copySize . width ) ≤ subresourceSize . width
- ( texelCopyTextureInfo . origin . y + copySize . height ) ≤ subresourceSize . height
( texelCopyTextureInfo . origin . y + copySize . height ) ≤ subresourceSize . height
- ( texelCopyTextureInfo . origin . z + copySize . depthOrArrayLayers ) ≤ subresourceSize . depthOrArrayLayers
( texelCopyTextureInfo . origin . z + copySize . depthOrArrayLayers ) ≤ subresourceSize . depthOrArrayLayers
- copySize . width must be a multiple of blockWidth .
copySize . width must be a multiple of blockWidth .
- copySize . height must be a multiple of blockHeight .
copySize . height must be a multiple of blockHeight .
Note: The texture copy range is validated against the physical (rounded-up)
    size for compressed formats , allowing copies to access texture
    blocks which are not fully inside the texture.
- format1 equals format2 , or
format1 equals format2 , or
- format1 and format2 differ only in whether they are srgb formats (have the -srgb suffix).
format1 and format2 differ only in whether they are srgb formats (have the -srgb suffix).
- The mipmap level of s equals texelCopyTextureInfo . mipLevel .
The mipmap level of s equals texelCopyTextureInfo . mipLevel .
- The aspect of s is in the set of aspects of texelCopyTextureInfo . aspect .
The aspect of s is in the set of aspects of texelCopyTextureInfo . aspect .
- If texture . dimension is "2d" : The array layer of s is ≥ texelCopyTextureInfo . origin . z and < texelCopyTextureInfo . origin . z + copySize . depthOrArrayLayers .
If texture . dimension is "2d" :
- The array layer of s is ≥ texelCopyTextureInfo . origin . z and < texelCopyTextureInfo . origin . z + copySize . depthOrArrayLayers .
The array layer of s is ≥ texelCopyTextureInfo . origin . z and < texelCopyTextureInfo . origin . z + copySize . depthOrArrayLayers .

## 12. Command Buffers

Command buffers are pre-recorded lists of GPU commands (blocks of queue timeline steps) that can be submitted to a GPUQueue for execution.
Each GPU command represents a task to be performed on the queue timeline , such as setting state, drawing, copying resources, etc.
A GPUCommandBuffer can only be submitted once, at which point it becomes invalidated .
To reuse rendering commands across multiple submissions, use GPURenderBundle .

### 12.1. GPUCommandBuffer

GPUCommandBuffer has the following device timeline properties :
A list of GPU commands to be executed on the Queue timeline when this command
buffer is submitted.
The current state used by any render pass commands being executed.
A set of all GPUBindGroup s used by this command buffer.

## 13. Command Encoding

### 13.1. GPUCommandsMixin

GPUCommandsMixin defines state common to all interfaces which encode commands.
It has no methods.
GPUCommandsMixin has the following device timeline properties :
The current state of the encoder.
A list of GPU commands to be executed on the Queue timeline when a GPUCommandBuffer containing these commands is submitted.
A set of all GPUBindGroup s set with setBindGroup() during command encoding.
The encoder state may be one of the following:
The encoder is available to encode new commands.
The encoder cannot be used, because it is locked by a child encoder: it is a GPUCommandEncoder , and a GPURenderPassEncoder or GPUComputePassEncoder is active.
The encoder becomes " open " again when the pass is ended.
Any command issued in this state invalidates the encoder.
The encoder has been ended and new commands can no longer be encoded.
Any command issued in this state will generate a validation error .
- If encoder . [[state]] is: " open " Return true . " locked " Invalidate encoder and return false . " ended " Generate a validation error , and return false .
If encoder . [[state]] is:
Return true .
Invalidate encoder and return false .
Generate a validation error , and return false .
- Append command to encoder . [[commands]] .
Append command to encoder . [[commands]] .
- When command is executed as part of a GPUCommandBuffer : Issue the steps of command .
When command is executed as part of a GPUCommandBuffer :
- Issue the steps of command .
Issue the steps of command .

### 13.2. GPUCommandEncoder

Creates a GPUCommandEncoder .
Arguments:
Returns: GPUCommandEncoder
Content timeline steps:
- Let e be ! create a new WebGPU object ( this , GPUCommandEncoder , descriptor ).
Let e be ! create a new WebGPU object ( this , GPUCommandEncoder , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return e .
Return e .
- If any of the following conditions are unsatisfied generate a validation error , invalidate e and return. this must not be lost .
If any of the following conditions are unsatisfied generate a validation error , invalidate e and return.
- this must not be lost .
this must not be lost .

### 13.3. Pass Encoding

Begins encoding a render pass described by descriptor .
Arguments:
Returns: GPURenderPassEncoder
Content timeline steps:
- For each non- null colorAttachment in descriptor . colorAttachments : If colorAttachment . clearValue is provided : ? validate GPUColor shape ( colorAttachment . clearValue ).
For each non- null colorAttachment in descriptor . colorAttachments :
- If colorAttachment . clearValue is provided : ? validate GPUColor shape ( colorAttachment . clearValue ).
If colorAttachment . clearValue is provided :
- ? validate GPUColor shape ( colorAttachment . clearValue ).
? validate GPUColor shape ( colorAttachment . clearValue ).
- Let pass be a new GPURenderPassEncoder object.
Let pass be a new GPURenderPassEncoder object.
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return pass .
Return pass .
- Validate the encoder state of this .
If it returns false, invalidate pass and return.
Validate the encoder state of this .
If it returns false, invalidate pass and return.
- Set this . [[state]] to " locked ".
Set this . [[state]] to " locked ".
- Let attachmentRegions be a list of [ texture subresource , depthSlice ?]
pairs, initially empty. Each pair describes the region of the texture to be rendered to, which
includes a single depth slice for "3d" textures only.
Let attachmentRegions be a list of [ texture subresource , depthSlice ?]
pairs, initially empty. Each pair describes the region of the texture to be rendered to, which
includes a single depth slice for "3d" textures only.
- For each non- null colorAttachment in descriptor . colorAttachments : Add [ colorAttachment . view , colorAttachment . depthSlice ?? null ] to attachmentRegions . If colorAttachment . resolveTarget is not null : Add [ colorAttachment . resolveTarget , undefined ] to attachmentRegions .
For each non- null colorAttachment in descriptor . colorAttachments :
- Add [ colorAttachment . view , colorAttachment . depthSlice ?? null ] to attachmentRegions .
Add [ colorAttachment . view , colorAttachment . depthSlice ?? null ] to attachmentRegions .
- If colorAttachment . resolveTarget is not null : Add [ colorAttachment . resolveTarget , undefined ] to attachmentRegions .
If colorAttachment . resolveTarget is not null :
- Add [ colorAttachment . resolveTarget , undefined ] to attachmentRegions .
Add [ colorAttachment . resolveTarget , undefined ] to attachmentRegions .
- If any of the following requirements are unmet, invalidate pass and return. descriptor must meet the Valid Usage rules
given device this . [[device]] . The set of texture regions in attachmentRegions must be pairwise disjoint.
That is, no two texture regions may overlap.
If any of the following requirements are unmet, invalidate pass and return.
- descriptor must meet the Valid Usage rules
given device this . [[device]] .
descriptor must meet the Valid Usage rules
given device this . [[device]] .
- The set of texture regions in attachmentRegions must be pairwise disjoint.
That is, no two texture regions may overlap.
The set of texture regions in attachmentRegions must be pairwise disjoint.
That is, no two texture regions may overlap.
- Add each texture subresource in attachmentRegions to pass . [[usage scope]] with usage attachment .
Add each texture subresource in attachmentRegions to pass . [[usage scope]] with usage attachment .
- Let depthStencilAttachment be descriptor . depthStencilAttachment .
Let depthStencilAttachment be descriptor . depthStencilAttachment .
- If depthStencilAttachment is not null : Let depthStencilView be depthStencilAttachment . view . Add the depth subresource of depthStencilView , if any,
to pass . [[usage scope]] with usage attachment-read if depthStencilAttachment . depthReadOnly is true,
or attachment otherwise. Add the stencil subresource of depthStencilView , if any,
to pass . [[usage scope]] with usage attachment-read if depthStencilAttachment . stencilReadOnly is true,
or attachment otherwise. Set pass . [[depthReadOnly]] to depthStencilAttachment . depthReadOnly . Set pass . [[stencilReadOnly]] to depthStencilAttachment . stencilReadOnly .
If depthStencilAttachment is not null :
- Let depthStencilView be depthStencilAttachment . view .
Let depthStencilView be depthStencilAttachment . view .
- Add the depth subresource of depthStencilView , if any,
to pass . [[usage scope]] with usage attachment-read if depthStencilAttachment . depthReadOnly is true,
or attachment otherwise.
Add the depth subresource of depthStencilView , if any,
to pass . [[usage scope]] with usage attachment-read if depthStencilAttachment . depthReadOnly is true,
or attachment otherwise.
- Add the stencil subresource of depthStencilView , if any,
to pass . [[usage scope]] with usage attachment-read if depthStencilAttachment . stencilReadOnly is true,
or attachment otherwise.
Add the stencil subresource of depthStencilView , if any,
to pass . [[usage scope]] with usage attachment-read if depthStencilAttachment . stencilReadOnly is true,
or attachment otherwise.
- Set pass . [[depthReadOnly]] to depthStencilAttachment . depthReadOnly .
Set pass . [[depthReadOnly]] to depthStencilAttachment . depthReadOnly .
- Set pass . [[stencilReadOnly]] to depthStencilAttachment . stencilReadOnly .
Set pass . [[stencilReadOnly]] to depthStencilAttachment . stencilReadOnly .
- Set pass . [[layout]] to derive render targets layout from pass ( descriptor ).
Set pass . [[layout]] to derive render targets layout from pass ( descriptor ).
- If descriptor . timestampWrites is provided : Let timestampWrites be descriptor . timestampWrites . If timestampWrites . beginningOfPassWriteIndex is provided , append a GPU command to this . [[commands]] with the following steps: Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet . If timestampWrites . endOfPassWriteIndex is provided , set pass . [[endTimestampWrite]] to a GPU command with the following steps: After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .
If descriptor . timestampWrites is provided :
- Let timestampWrites be descriptor . timestampWrites .
Let timestampWrites be descriptor . timestampWrites .
- If timestampWrites . beginningOfPassWriteIndex is provided , append a GPU command to this . [[commands]] with the following steps: Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet .
If timestampWrites . beginningOfPassWriteIndex is provided , append a GPU command to this . [[commands]] with the following steps:
- Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet .
Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet .
- If timestampWrites . endOfPassWriteIndex is provided , set pass . [[endTimestampWrite]] to a GPU command with the following steps: After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .
If timestampWrites . endOfPassWriteIndex is provided , set pass . [[endTimestampWrite]] to a GPU command with the following steps:
- After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .
After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .
- Set pass . [[drawCount]] to 0.
Set pass . [[drawCount]] to 0.
- Set pass . [[maxDrawCount]] to descriptor . maxDrawCount .
Set pass . [[maxDrawCount]] to descriptor . maxDrawCount .
- Set pass . [[maxDrawCount]] to descriptor . maxDrawCount .
Set pass . [[maxDrawCount]] to descriptor . maxDrawCount .
- Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
- Let the [[renderState]] of the currently executing GPUCommandBuffer be a new RenderState .
Let the [[renderState]] of the currently executing GPUCommandBuffer be a new RenderState .
- Set [[renderState]] . [[colorAttachments]] to descriptor . colorAttachments .
Set [[renderState]] . [[colorAttachments]] to descriptor . colorAttachments .
- Set [[renderState]] . [[depthStencilAttachment]] to descriptor . depthStencilAttachment .
Set [[renderState]] . [[depthStencilAttachment]] to descriptor . depthStencilAttachment .
- For each non- null colorAttachment in descriptor . colorAttachments : Let colorView be colorAttachment . view . If colorView . [[descriptor]] . dimension is: "3d" Let colorSubregion be colorAttachment . depthSlice of colorView . Otherwise Let colorSubregion be colorView . If colorAttachment . loadOp is: "load" Ensure the contents of colorSubregion are loaded into the framebuffer memory associated with colorSubregion . "clear" Set every texel of the framebuffer memory associated with colorSubregion to colorAttachment . clearValue .
For each non- null colorAttachment in descriptor . colorAttachments :
- Let colorView be colorAttachment . view .
Let colorView be colorAttachment . view .
- If colorView . [[descriptor]] . dimension is: "3d" Let colorSubregion be colorAttachment . depthSlice of colorView . Otherwise Let colorSubregion be colorView .
If colorView . [[descriptor]] . dimension is:
Let colorSubregion be colorAttachment . depthSlice of colorView .
Let colorSubregion be colorView .
- If colorAttachment . loadOp is: "load" Ensure the contents of colorSubregion are loaded into the framebuffer memory associated with colorSubregion . "clear" Set every texel of the framebuffer memory associated with colorSubregion to colorAttachment . clearValue .
If colorAttachment . loadOp is:
Ensure the contents of colorSubregion are loaded into the framebuffer memory associated with colorSubregion .
Set every texel of the framebuffer memory associated with colorSubregion to colorAttachment . clearValue .
- If depthStencilAttachment is not null : If depthStencilAttachment . depthLoadOp is: Not provided Assert that depthStencilAttachment . depthReadOnly is true and ensure the contents of the depth subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "load" Ensure the contents of the depth subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "clear" Set every texel of the framebuffer memory associated with the depth subresource of depthStencilView to depthStencilAttachment . depthClearValue . If depthStencilAttachment . stencilLoadOp is: Not provided Assert that depthStencilAttachment . stencilReadOnly is true and ensure the contents of the stencil subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "load" Ensure the contents of the stencil subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "clear" Set every texel of the framebuffer memory associated with the stencil subresource depthStencilView to depthStencilAttachment . stencilClearValue .
If depthStencilAttachment is not null :
- If depthStencilAttachment . depthLoadOp is: Not provided Assert that depthStencilAttachment . depthReadOnly is true and ensure the contents of the depth subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "load" Ensure the contents of the depth subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "clear" Set every texel of the framebuffer memory associated with the depth subresource of depthStencilView to depthStencilAttachment . depthClearValue .
If depthStencilAttachment . depthLoadOp is:
Assert that depthStencilAttachment . depthReadOnly is true and ensure the contents of the depth subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView .
Ensure the contents of the depth subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView .
Set every texel of the framebuffer memory associated with the depth subresource of depthStencilView to depthStencilAttachment . depthClearValue .
- If depthStencilAttachment . stencilLoadOp is: Not provided Assert that depthStencilAttachment . stencilReadOnly is true and ensure the contents of the stencil subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "load" Ensure the contents of the stencil subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView . "clear" Set every texel of the framebuffer memory associated with the stencil subresource depthStencilView to depthStencilAttachment . stencilClearValue .
If depthStencilAttachment . stencilLoadOp is:
Assert that depthStencilAttachment . stencilReadOnly is true and ensure the contents of the stencil subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView .
Ensure the contents of the stencil subresource of depthStencilView are loaded into the framebuffer memory associated with depthStencilView .
Set every texel of the framebuffer memory associated with the stencil subresource depthStencilView to depthStencilAttachment . stencilClearValue .
Note: Read-only depth-stencil attachments are implicitly treated as though the "load" operation was used. Validation that requires the load op to not be provided for read-only attachments
        is done in GPURenderPassDepthStencilAttachment Valid Usage .
Begins encoding a compute pass described by descriptor .
Arguments:
Returns: GPUComputePassEncoder
Content timeline steps:
- Let pass be a new GPUComputePassEncoder object.
Let pass be a new GPUComputePassEncoder object.
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return pass .
Return pass .
- Validate the encoder state of this .
If it returns false, invalidate pass and return.
Validate the encoder state of this .
If it returns false, invalidate pass and return.
- Set this . [[state]] to " locked ".
Set this . [[state]] to " locked ".
- If any of the following requirements are unmet, invalidate pass and return. If descriptor . timestampWrites is provided : Validate timestampWrites ( this . [[device]] , descriptor . timestampWrites )
must return true.
If any of the following requirements are unmet, invalidate pass and return.
- If descriptor . timestampWrites is provided : Validate timestampWrites ( this . [[device]] , descriptor . timestampWrites )
must return true.
If descriptor . timestampWrites is provided :
- Validate timestampWrites ( this . [[device]] , descriptor . timestampWrites )
must return true.
Validate timestampWrites ( this . [[device]] , descriptor . timestampWrites )
must return true.
- If descriptor . timestampWrites is provided : Let timestampWrites be descriptor . timestampWrites . If timestampWrites . beginningOfPassWriteIndex is provided , append a GPU command to this . [[commands]] with the following steps: Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet . If timestampWrites . endOfPassWriteIndex is provided , set pass . [[endTimestampWrite]] to a GPU command with the following steps: After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .
If descriptor . timestampWrites is provided :
- Let timestampWrites be descriptor . timestampWrites .
Let timestampWrites be descriptor . timestampWrites .
- If timestampWrites . beginningOfPassWriteIndex is provided , append a GPU command to this . [[commands]] with the following steps: Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet .
If timestampWrites . beginningOfPassWriteIndex is provided , append a GPU command to this . [[commands]] with the following steps:
- Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet .
Before the pass commands begin executing,
write the current queue timestamp into index timestampWrites . beginningOfPassWriteIndex of timestampWrites . querySet .
- If timestampWrites . endOfPassWriteIndex is provided , set pass . [[endTimestampWrite]] to a GPU command with the following steps: After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .
If timestampWrites . endOfPassWriteIndex is provided , set pass . [[endTimestampWrite]] to a GPU command with the following steps:
- After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .
After the pass commands finish executing,
write the current queue timestamp into index timestampWrites . endOfPassWriteIndex of timestampWrites . querySet .

### 13.4. Buffer Copy Commands

copyBufferToBuffer() has two overloads:
Shorthand, equivalent to copyBufferToBuffer(source, 0, destination, 0, size) .
Encode a command into the GPUCommandEncoder that copies data from a sub-region of a GPUBuffer to a sub-region of another GPUBuffer .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If size is undefined , set it to source . size − sourceOffset .
If size is undefined , set it to source . size − sourceOffset .
- If any of the following conditions are unsatisfied, invalidate this and return. source is valid to use with this . destination is valid to use with this . source . usage contains COPY_SRC . destination . usage contains COPY_DST . size is a multiple of 4. sourceOffset is a multiple of 4. destinationOffset is a multiple of 4. source . size ≥ ( sourceOffset + size ). destination . size ≥ ( destinationOffset + size ). source and destination are not the same GPUBuffer .
If any of the following conditions are unsatisfied, invalidate this and return.
- source is valid to use with this .
source is valid to use with this .
- destination is valid to use with this .
destination is valid to use with this .
- source . usage contains COPY_SRC .
source . usage contains COPY_SRC .
- destination . usage contains COPY_DST .
destination . usage contains COPY_DST .
- size is a multiple of 4.
size is a multiple of 4.
- sourceOffset is a multiple of 4.
sourceOffset is a multiple of 4.
- destinationOffset is a multiple of 4.
destinationOffset is a multiple of 4.
- source . size ≥ ( sourceOffset + size ).
source . size ≥ ( sourceOffset + size ).
- destination . size ≥ ( destinationOffset + size ).
destination . size ≥ ( destinationOffset + size ).
- source and destination are not the same GPUBuffer .
source and destination are not the same GPUBuffer .
- Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
- Copy size bytes of source , beginning at sourceOffset , into destination ,
beginning at destinationOffset .
Copy size bytes of source , beginning at sourceOffset , into destination ,
beginning at destinationOffset .
Encode a command into the GPUCommandEncoder that fills a sub-region of a GPUBuffer with zeros.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If size is missing, set size to max(0, buffer . size - offset ) .
If size is missing, set size to max(0, buffer . size - offset ) .
- If any of the following conditions are unsatisfied, invalidate this and return. buffer is valid to use with this . buffer . usage contains COPY_DST . size is a multiple of 4. offset is a multiple of 4. buffer . size ≥ ( offset + size ).
If any of the following conditions are unsatisfied, invalidate this and return.
- buffer is valid to use with this .
buffer is valid to use with this .
- buffer . usage contains COPY_DST .
buffer . usage contains COPY_DST .
- size is a multiple of 4.
size is a multiple of 4.
- offset is a multiple of 4.
offset is a multiple of 4.
- buffer . size ≥ ( offset + size ).
buffer . size ≥ ( offset + size ).
- Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
- Set size bytes of buffer to 0 starting at offset .
Set size bytes of buffer to 0 starting at offset .

### 13.5. Texel Copy Commands

Encode a command into the GPUCommandEncoder that copies data from a sub-region of a GPUBuffer to a sub-region of one or multiple continuous texture subresources .
Arguments:
Returns: undefined
Content timeline steps:
- ? validate GPUOrigin3D shape ( destination . origin ).
? validate GPUOrigin3D shape ( destination . origin ).
- ? validate GPUExtent3D shape ( copySize ).
? validate GPUExtent3D shape ( copySize ).
- Issue the subsequent steps on the Device timeline of this . [[device]] :
Issue the subsequent steps on the Device timeline of this . [[device]] :
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let aligned be true .
Let aligned be true .
- Let dataLength be source . buffer . size .
Let dataLength be source . buffer . size .
- If any of the following conditions are unsatisfied, invalidate this and return. validating GPUTexelCopyBufferInfo ( source ) returns true . source . buffer . usage contains COPY_SRC . validating texture buffer copy ( destination , source , dataLength , copySize , COPY_DST , aligned ) returns true .
If any of the following conditions are unsatisfied, invalidate this and return.
- validating GPUTexelCopyBufferInfo ( source ) returns true .
validating GPUTexelCopyBufferInfo ( source ) returns true .
- source . buffer . usage contains COPY_SRC .
source . buffer . usage contains COPY_SRC .
- validating texture buffer copy ( destination , source , dataLength , copySize , COPY_DST , aligned ) returns true .
validating texture buffer copy ( destination , source , dataLength , copySize , COPY_DST , aligned ) returns true .
- Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
- Let blockWidth be the texel block width of destination . texture .
Let blockWidth be the texel block width of destination . texture .
- Let blockHeight be the texel block height of destination . texture .
Let blockHeight be the texel block height of destination . texture .
- Let dstOrigin be destination . origin .
Let dstOrigin be destination . origin .
- Let dstBlockOriginX be ( dstOrigin . x ÷ blockWidth ).
Let dstBlockOriginX be ( dstOrigin . x ÷ blockWidth ).
- Let dstBlockOriginY be ( dstOrigin . y ÷ blockHeight ).
Let dstBlockOriginY be ( dstOrigin . y ÷ blockHeight ).
- Let blockColumns be ( copySize . width ÷ blockWidth ).
Let blockColumns be ( copySize . width ÷ blockWidth ).
- Let blockRows be ( copySize . height ÷ blockHeight ).
Let blockRows be ( copySize . height ÷ blockHeight ).
- Assert that dstBlockOriginX , dstBlockOriginY , blockColumns , and blockRows are integers.
Assert that dstBlockOriginX , dstBlockOriginY , blockColumns , and blockRows are integers.
- For each z in the range [0, copySize . depthOrArrayLayers − 1]: Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination . For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of source for ( x , y , z ) of destination . texture . Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by source . buffer at offset blockOffset .
For each z in the range [0, copySize . depthOrArrayLayers − 1]:
- Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination .
Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination .
- For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of source for ( x , y , z ) of destination . texture . Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by source . buffer at offset blockOffset .
For each y in the range [0, blockRows − 1]:
- For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of source for ( x , y , z ) of destination . texture . Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by source . buffer at offset blockOffset .
For each x in the range [0, blockColumns − 1]:
- Let blockOffset be the texel block byte offset of source for ( x , y , z ) of destination . texture .
Let blockOffset be the texel block byte offset of source for ( x , y , z ) of destination . texture .
- Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by source . buffer at offset blockOffset .
Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by source . buffer at offset blockOffset .
Encode a command into the GPUCommandEncoder that copies data from a sub-region of one or
multiple continuous texture subresources to a sub-region of a GPUBuffer .
Arguments:
Returns: undefined
Content timeline steps:
- ? validate GPUOrigin3D shape ( source . origin ).
? validate GPUOrigin3D shape ( source . origin ).
- ? validate GPUExtent3D shape ( copySize ).
? validate GPUExtent3D shape ( copySize ).
- Issue the subsequent steps on the Device timeline of this . [[device]] :
Issue the subsequent steps on the Device timeline of this . [[device]] :
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let aligned be true .
Let aligned be true .
- Let dataLength be destination . buffer . size .
Let dataLength be destination . buffer . size .
- If any of the following conditions are unsatisfied, invalidate this and return. validating GPUTexelCopyBufferInfo ( destination ) returns true . destination . buffer . usage contains COPY_DST . validating texture buffer copy ( source , destination , dataLength , copySize , COPY_SRC , aligned ) returns true . If device. [[features]] does not contain "core-features-and-limits" : source . texture . format must not be a compressed format .
If any of the following conditions are unsatisfied, invalidate this and return.
- validating GPUTexelCopyBufferInfo ( destination ) returns true .
validating GPUTexelCopyBufferInfo ( destination ) returns true .
- destination . buffer . usage contains COPY_DST .
destination . buffer . usage contains COPY_DST .
- validating texture buffer copy ( source , destination , dataLength , copySize , COPY_SRC , aligned ) returns true .
validating texture buffer copy ( source , destination , dataLength , copySize , COPY_SRC , aligned ) returns true .
- If device. [[features]] does not contain "core-features-and-limits" : source . texture . format must not be a compressed format .
- source . texture . format must not be a compressed format .
source . texture . format must not be a compressed format .
- Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
- Let blockWidth be the texel block width of source . texture .
Let blockWidth be the texel block width of source . texture .
- Let blockHeight be the texel block height of source . texture .
Let blockHeight be the texel block height of source . texture .
- Let srcOrigin be source . origin .
Let srcOrigin be source . origin .
- Let srcBlockOriginX be ( srcOrigin . x ÷ blockWidth ).
Let srcBlockOriginX be ( srcOrigin . x ÷ blockWidth ).
- Let srcBlockOriginY be ( srcOrigin . y ÷ blockHeight ).
Let srcBlockOriginY be ( srcOrigin . y ÷ blockHeight ).
- Let blockColumns be ( copySize . width ÷ blockWidth ).
Let blockColumns be ( copySize . width ÷ blockWidth ).
- Let blockRows be ( copySize . height ÷ blockHeight ).
Let blockRows be ( copySize . height ÷ blockHeight ).
- Assert that srcBlockOriginX , srcBlockOriginY , blockColumns , and blockRows are integers.
Assert that srcBlockOriginX , srcBlockOriginY , blockColumns , and blockRows are integers.
- For each z in the range [0, copySize . depthOrArrayLayers − 1]: Let srcSubregion be texture copy sub-region ( z + srcOrigin . z ) of source . For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of destination for ( x , y , z ) of source . texture . Set destination . buffer at offset blockOffset to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
For each z in the range [0, copySize . depthOrArrayLayers − 1]:
- Let srcSubregion be texture copy sub-region ( z + srcOrigin . z ) of source .
Let srcSubregion be texture copy sub-region ( z + srcOrigin . z ) of source .
- For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of destination for ( x , y , z ) of source . texture . Set destination . buffer at offset blockOffset to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
For each y in the range [0, blockRows − 1]:
- For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of destination for ( x , y , z ) of source . texture . Set destination . buffer at offset blockOffset to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
For each x in the range [0, blockColumns − 1]:
- Let blockOffset be the texel block byte offset of destination for ( x , y , z ) of source . texture .
Let blockOffset be the texel block byte offset of destination for ( x , y , z ) of source . texture .
- Set destination . buffer at offset blockOffset to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
Set destination . buffer at offset blockOffset to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
Encode a command into the GPUCommandEncoder that copies data from a sub-region of one
or multiple contiguous texture subresources to another sub-region of one or
multiple continuous texture subresources .
Arguments:
Returns: undefined
Content timeline steps:
- ? validate GPUOrigin3D shape ( source . origin ).
? validate GPUOrigin3D shape ( source . origin ).
- ? validate GPUOrigin3D shape ( destination . origin ).
? validate GPUOrigin3D shape ( destination . origin ).
- ? validate GPUExtent3D shape ( copySize ).
? validate GPUExtent3D shape ( copySize ).
- Issue the subsequent steps on the Device timeline of this . [[device]] :
Issue the subsequent steps on the Device timeline of this . [[device]] :
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. Let srcTexture be source . texture . Let dstTexture be destination . texture . validating GPUTexelCopyTextureInfo ( source , copySize ) returns true . srcTexture . usage contains COPY_SRC . validating GPUTexelCopyTextureInfo ( destination , copySize ) returns true . dstTexture . usage contains COPY_DST . srcTexture . sampleCount is equal to dstTexture . sampleCount . srcTexture . format and dstTexture . format must be copy-compatible . If srcTexture . format is a depth-stencil format: source . aspect and destination . aspect must both refer to all aspects of srcTexture . format and dstTexture . format , respectively. The set of subresources for texture copy ( source , copySize ) and
the set of subresources for texture copy ( destination , copySize ) are disjoint. If device. [[features]] does not contain "core-features-and-limits" : source . texture . format must not be a compressed format . destination . texture . format must not be a compressed format . source . texture . sampleCount and destination . texture . sampleCount must be 1.
If any of the following conditions are unsatisfied, invalidate this and return.
- Let srcTexture be source . texture .
Let srcTexture be source . texture .
- Let dstTexture be destination . texture .
Let dstTexture be destination . texture .
- validating GPUTexelCopyTextureInfo ( source , copySize ) returns true .
validating GPUTexelCopyTextureInfo ( source , copySize ) returns true .
- srcTexture . usage contains COPY_SRC .
srcTexture . usage contains COPY_SRC .
- validating GPUTexelCopyTextureInfo ( destination , copySize ) returns true .
validating GPUTexelCopyTextureInfo ( destination , copySize ) returns true .
- dstTexture . usage contains COPY_DST .
dstTexture . usage contains COPY_DST .
- srcTexture . sampleCount is equal to dstTexture . sampleCount .
srcTexture . sampleCount is equal to dstTexture . sampleCount .
- srcTexture . format and dstTexture . format must be copy-compatible .
srcTexture . format and dstTexture . format must be copy-compatible .
- If srcTexture . format is a depth-stencil format: source . aspect and destination . aspect must both refer to all aspects of srcTexture . format and dstTexture . format , respectively.
If srcTexture . format is a depth-stencil format:
- source . aspect and destination . aspect must both refer to all aspects of srcTexture . format and dstTexture . format , respectively.
source . aspect and destination . aspect must both refer to all aspects of srcTexture . format and dstTexture . format , respectively.
- The set of subresources for texture copy ( source , copySize ) and
the set of subresources for texture copy ( destination , copySize ) are disjoint.
The set of subresources for texture copy ( source , copySize ) and
the set of subresources for texture copy ( destination , copySize ) are disjoint.
- If device. [[features]] does not contain "core-features-and-limits" : source . texture . format must not be a compressed format . destination . texture . format must not be a compressed format . source . texture . sampleCount and destination . texture . sampleCount must be 1.
- source . texture . format must not be a compressed format .
source . texture . format must not be a compressed format .
- destination . texture . format must not be a compressed format .
destination . texture . format must not be a compressed format .
- source . texture . sampleCount and destination . texture . sampleCount must be 1.
source . texture . sampleCount and destination . texture . sampleCount must be 1.
- Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
- Let blockWidth be the texel block width of source . texture .
Let blockWidth be the texel block width of source . texture .
- Let blockHeight be the texel block height of source . texture .
Let blockHeight be the texel block height of source . texture .
- Let srcOrigin be source . origin .
Let srcOrigin be source . origin .
- Let srcBlockOriginX be ( srcOrigin . x ÷ blockWidth ).
Let srcBlockOriginX be ( srcOrigin . x ÷ blockWidth ).
- Let srcBlockOriginY be ( srcOrigin . y ÷ blockHeight ).
Let srcBlockOriginY be ( srcOrigin . y ÷ blockHeight ).
- Let dstOrigin be destination . origin .
Let dstOrigin be destination . origin .
- Let dstBlockOriginX be ( dstOrigin . x ÷ blockWidth ).
Let dstBlockOriginX be ( dstOrigin . x ÷ blockWidth ).
- Let dstBlockOriginY be ( dstOrigin . y ÷ blockHeight ).
Let dstBlockOriginY be ( dstOrigin . y ÷ blockHeight ).
- Let blockColumns be ( copySize . width ÷ blockWidth ).
Let blockColumns be ( copySize . width ÷ blockWidth ).
- Let blockRows be ( copySize . height ÷ blockHeight ).
Let blockRows be ( copySize . height ÷ blockHeight ).
- Assert that srcBlockOriginX , srcBlockOriginY , dstBlockOriginX , dstBlockOriginY , blockColumns , and blockRows are integers.
Assert that srcBlockOriginX , srcBlockOriginY , dstBlockOriginX , dstBlockOriginY , blockColumns , and blockRows are integers.
- For each z in the range [0, copySize . depthOrArrayLayers − 1]: Let srcSubregion be texture copy sub-region ( z + srcOrigin . z ) of source . Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination . For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
For each z in the range [0, copySize . depthOrArrayLayers − 1]:
- Let srcSubregion be texture copy sub-region ( z + srcOrigin . z ) of source .
Let srcSubregion be texture copy sub-region ( z + srcOrigin . z ) of source .
- Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination .
Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination .
- For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
For each y in the range [0, blockRows − 1]:
- For each x in the range [0, blockColumns − 1]: Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
For each x in the range [0, blockColumns − 1]:
- Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .
Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to texel block ( srcBlockOriginX + x , srcBlockOriginY + y ) of srcSubregion .

### 13.6. Queries

Resolves query results from a GPUQuerySet out into a range of a GPUBuffer .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. querySet is valid to use with this . destination is valid to use with this . destination . usage contains QUERY_RESOLVE . firstQuery < the number of queries in querySet . ( firstQuery + queryCount ) ≤ the number of queries in querySet . destinationOffset is a multiple of 256. destinationOffset + 8 × queryCount ≤ destination . size .
If any of the following conditions are unsatisfied, invalidate this and return.
- querySet is valid to use with this .
querySet is valid to use with this .
- destination is valid to use with this .
destination is valid to use with this .
- destination . usage contains QUERY_RESOLVE .
destination . usage contains QUERY_RESOLVE .
- firstQuery < the number of queries in querySet .
firstQuery < the number of queries in querySet .
- ( firstQuery + queryCount ) ≤ the number of queries in querySet .
( firstQuery + queryCount ) ≤ the number of queries in querySet .
- destinationOffset is a multiple of 256.
destinationOffset is a multiple of 256.
- destinationOffset + 8 × queryCount ≤ destination . size .
destinationOffset + 8 × queryCount ≤ destination . size .
- Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
Enqueue a command on this which issues the subsequent steps on the Queue timeline when executed.
- Let queryIndex be firstQuery .
Let queryIndex be firstQuery .
- Let offset be destinationOffset .
Let offset be destinationOffset .
- While queryIndex < firstQuery + queryCount : Set 8 bytes of destination , beginning at offset , to be the value of querySet at queryIndex . Set queryIndex to be queryIndex + 1. Set offset to be offset + 8.
While queryIndex < firstQuery + queryCount :
- Set 8 bytes of destination , beginning at offset , to be the value of querySet at queryIndex .
Set 8 bytes of destination , beginning at offset , to be the value of querySet at queryIndex .
- Set queryIndex to be queryIndex + 1.
Set queryIndex to be queryIndex + 1.
- Set offset to be offset + 8.
Set offset to be offset + 8.

### 13.7. Finalization

A GPUCommandBuffer containing the commands recorded by the GPUCommandEncoder can be created
by calling finish() . Once finish() has been called the
command encoder can no longer be used.
Completes recording of the commands sequence and returns a corresponding GPUCommandBuffer .
Arguments:
Returns: GPUCommandBuffer
Content timeline steps:
- Let commandBuffer be a new GPUCommandBuffer .
Let commandBuffer be a new GPUCommandBuffer .
- Issue the finish steps on the Device timeline of this . [[device]] .
Issue the finish steps on the Device timeline of this . [[device]] .
- Return commandBuffer .
Return commandBuffer .
- Let validationSucceeded be true if all of the following requirements are met, and false otherwise. this must be valid . this . [[state]] must be " open ". this . [[debug_group_stack]] must be empty .
Let validationSucceeded be true if all of the following requirements are met, and false otherwise.
- this must be valid .
this must be valid .
- this . [[state]] must be " open ".
this . [[state]] must be " open ".
- this . [[debug_group_stack]] must be empty .
this . [[debug_group_stack]] must be empty .
- Set this . [[state]] to " ended ".
Set this . [[state]] to " ended ".
- If validationSucceeded is false , then: Generate a validation error . Return an invalidated GPUCommandBuffer .
If validationSucceeded is false , then:
- Generate a validation error .
Generate a validation error .
- Return an invalidated GPUCommandBuffer .
Return an invalidated GPUCommandBuffer .
- Set commandBuffer . [[command_list]] to this . [[commands]] .
Set commandBuffer . [[command_list]] to this . [[commands]] .
- Set commandBuffer . [[used_bind_groups]] to this . [[used_bind_groups]] .
Set commandBuffer . [[used_bind_groups]] to this . [[used_bind_groups]] .

## 14. Programmable Passes

GPUBindingCommandsMixin assumes the presence of GPUObjectBase and GPUCommandsMixin members on the same object.
It must only be included by interfaces which also include those mixins.
GPUBindingCommandsMixin has the following device timeline properties :
The current GPUBindGroup for each index.
The current dynamic offsets for each [[bind_groups]] entry.

### 14.1. Bind Groups

setBindGroup() has two overloads:
Sets the current GPUBindGroup for the given index.
Arguments:
The index to set the bind group at.
Bind group to use for subsequent render or compute commands.
Array containing buffer offsets in bytes for each entry in bindGroup marked as buffer . hasDynamicOffset ,
ordered by GPUBindGroupLayoutEntry . binding .
See note for additional details.
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let dynamicOffsetCount be 0 if bindGroup is null , or bindGroup . [[layout]] . [[dynamicOffsetCount]] if not.
Let dynamicOffsetCount be 0 if bindGroup is null , or bindGroup . [[layout]] . [[dynamicOffsetCount]] if not.
- If any of the following requirements are unmet, invalidate this and return. index must be < this . [[device]] . [[limits]] . maxBindGroups . dynamicOffsets . size must equal dynamicOffsetCount .
If any of the following requirements are unmet, invalidate this and return.
- index must be < this . [[device]] . [[limits]] . maxBindGroups .
index must be < this . [[device]] . [[limits]] . maxBindGroups .
- dynamicOffsets . size must equal dynamicOffsetCount .
dynamicOffsets . size must equal dynamicOffsetCount .
- If bindGroup is null : Remove this . [[bind_groups]] [ index ]. Remove this . [[dynamic_offsets]] [ index ]. Otherwise: If any of the following requirements are unmet, invalidate this and return. bindGroup must be valid to use with this . For each dynamic binding ( bufferBinding , bufferLayout , dynamicOffsetIndex ) in bindGroup : bufferBinding . offset + dynamicOffsets [ dynamicOffsetIndex ] + bufferLayout . minBindingSize must be ≤ bufferBinding . buffer . size . If bufferLayout . type is "uniform" : dynamicOffset must be a multiple of minUniformBufferOffsetAlignment . If bufferLayout . type is "storage" or "read-only-storage" : dynamicOffset must be a multiple of minStorageBufferOffsetAlignment . Set this . [[bind_groups]] [ index ] to be bindGroup . Set this . [[dynamic_offsets]] [ index ] to be a copy of dynamicOffsets . Append bindGroup to this . [[used_bind_groups]] . If this is a GPURenderCommandsMixin : For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
If bindGroup is null :
- Remove this . [[bind_groups]] [ index ].
Remove this . [[bind_groups]] [ index ].
- Remove this . [[dynamic_offsets]] [ index ].
Remove this . [[dynamic_offsets]] [ index ].
Otherwise:
- If any of the following requirements are unmet, invalidate this and return. bindGroup must be valid to use with this . For each dynamic binding ( bufferBinding , bufferLayout , dynamicOffsetIndex ) in bindGroup : bufferBinding . offset + dynamicOffsets [ dynamicOffsetIndex ] + bufferLayout . minBindingSize must be ≤ bufferBinding . buffer . size . If bufferLayout . type is "uniform" : dynamicOffset must be a multiple of minUniformBufferOffsetAlignment . If bufferLayout . type is "storage" or "read-only-storage" : dynamicOffset must be a multiple of minStorageBufferOffsetAlignment .
If any of the following requirements are unmet, invalidate this and return.
- bindGroup must be valid to use with this .
bindGroup must be valid to use with this .
- For each dynamic binding ( bufferBinding , bufferLayout , dynamicOffsetIndex ) in bindGroup : bufferBinding . offset + dynamicOffsets [ dynamicOffsetIndex ] + bufferLayout . minBindingSize must be ≤ bufferBinding . buffer . size . If bufferLayout . type is "uniform" : dynamicOffset must be a multiple of minUniformBufferOffsetAlignment . If bufferLayout . type is "storage" or "read-only-storage" : dynamicOffset must be a multiple of minStorageBufferOffsetAlignment .
For each dynamic binding ( bufferBinding , bufferLayout , dynamicOffsetIndex ) in bindGroup :
- bufferBinding . offset + dynamicOffsets [ dynamicOffsetIndex ] + bufferLayout . minBindingSize must be ≤ bufferBinding . buffer . size .
bufferBinding . offset + dynamicOffsets [ dynamicOffsetIndex ] + bufferLayout . minBindingSize must be ≤ bufferBinding . buffer . size .
- If bufferLayout . type is "uniform" : dynamicOffset must be a multiple of minUniformBufferOffsetAlignment .
If bufferLayout . type is "uniform" :
- dynamicOffset must be a multiple of minUniformBufferOffsetAlignment .
dynamicOffset must be a multiple of minUniformBufferOffsetAlignment .
- If bufferLayout . type is "storage" or "read-only-storage" : dynamicOffset must be a multiple of minStorageBufferOffsetAlignment .
If bufferLayout . type is "storage" or "read-only-storage" :
- dynamicOffset must be a multiple of minStorageBufferOffsetAlignment .
dynamicOffset must be a multiple of minStorageBufferOffsetAlignment .
- Set this . [[bind_groups]] [ index ] to be bindGroup .
Set this . [[bind_groups]] [ index ] to be bindGroup .
- Set this . [[dynamic_offsets]] [ index ] to be a copy of dynamicOffsets .
Set this . [[dynamic_offsets]] [ index ] to be a copy of dynamicOffsets .
- Append bindGroup to this . [[used_bind_groups]] .
Append bindGroup to this . [[used_bind_groups]] .
- If this is a GPURenderCommandsMixin : For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
If this is a GPURenderCommandsMixin :
- For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
Sets the current GPUBindGroup for the given index, specifying dynamic offsets as a subset
of a Uint32Array .
Arguments:
Returns: undefined
Content timeline steps:
- If any of the following requirements are unmet, throw a RangeError and return. dynamicOffsetsDataStart must be ≥ 0. dynamicOffsetsDataStart + dynamicOffsetsDataLength must be ≤ dynamicOffsetsData . length .
If any of the following requirements are unmet, throw a RangeError and return.
- dynamicOffsetsDataStart must be ≥ 0.
dynamicOffsetsDataStart must be ≥ 0.
- dynamicOffsetsDataStart + dynamicOffsetsDataLength must be ≤ dynamicOffsetsData . length .
dynamicOffsetsDataStart + dynamicOffsetsDataLength must be ≤ dynamicOffsetsData . length .
- Let dynamicOffsets be a list containing the range, starting at index dynamicOffsetsDataStart , of dynamicOffsetsDataLength elements of a copy of dynamicOffsetsData .
Let dynamicOffsets be a list containing the range, starting at index dynamicOffsetsDataStart , of dynamicOffsetsDataLength elements of a copy of dynamicOffsetsData .
- Call this . setBindGroup ( index , bindGroup , dynamicOffsets ).
Call this . setBindGroup ( index , bindGroup , dynamicOffsets ).
This means that if dynamic bindings is the list of each GPUBindGroupLayoutEntry in the GPUBindGroupLayout with buffer ?. hasDynamicOffset set to true , sorted by GPUBindGroupLayoutEntry . binding , then dynamic offset[i] , as supplied to setBindGroup() , will correspond to dynamic bindings[i] .
Used by a GPUBindGroup created with the following call:
And bound with the following call:
The following buffer offsets will be applied:
- Let dynamicOffsetIndex be 0 .
Let dynamicOffsetIndex be 0 .
- Let layout be bindGroup . [[layout]] .
Let layout be bindGroup . [[layout]] .
- For each GPUBindGroupEntry entry in bindGroup . [[entries]] ordered in increasing values of entry . binding : Let bindingDescriptor be the GPUBindGroupLayoutEntry at layout . [[entryMap]] [ entry . binding ]: If bindingDescriptor . buffer ?. hasDynamicOffset is true : Let bufferBinding be get as buffer binding ( entry . resource ). Let bufferLayout be bindingDescriptor . buffer . Call steps with bufferBinding , bufferLayout , and dynamicOffsetIndex . Let dynamicOffsetIndex be dynamicOffsetIndex + 1
For each GPUBindGroupEntry entry in bindGroup . [[entries]] ordered in increasing values of entry . binding :
- Let bindingDescriptor be the GPUBindGroupLayoutEntry at layout . [[entryMap]] [ entry . binding ]:
Let bindingDescriptor be the GPUBindGroupLayoutEntry at layout . [[entryMap]] [ entry . binding ]:
- If bindingDescriptor . buffer ?. hasDynamicOffset is true : Let bufferBinding be get as buffer binding ( entry . resource ). Let bufferLayout be bindingDescriptor . buffer . Call steps with bufferBinding , bufferLayout , and dynamicOffsetIndex . Let dynamicOffsetIndex be dynamicOffsetIndex + 1
If bindingDescriptor . buffer ?. hasDynamicOffset is true :
- Let bufferBinding be get as buffer binding ( entry . resource ).
Let bufferBinding be get as buffer binding ( entry . resource ).
- Let bufferLayout be bindingDescriptor . buffer .
Let bufferLayout be bindingDescriptor . buffer .
- Call steps with bufferBinding , bufferLayout , and dynamicOffsetIndex .
Call steps with bufferBinding , bufferLayout , and dynamicOffsetIndex .
- Let dynamicOffsetIndex be dynamicOffsetIndex + 1
Let dynamicOffsetIndex be dynamicOffsetIndex + 1
Arguments:
Encoder whose bind groups are being validated.
Pipeline to validate encoder s bind groups are compatible with.
Device timeline steps:
- If any of the following conditions are unsatisfied, return false : Let bindGroupLayouts be pipeline . [[layout]] . [[bindGroupLayouts]] . pipeline must not be null . All bind groups used by the pipeline must be set and compatible with the pipeline layout, determined as follows: For each pair of ( GPUIndex32 index , GPUBindGroupLayout bindGroupLayout ) in bindGroupLayouts : If bindGroupLayout is null , continue . Let bindGroup be encoder . [[bind_groups]] [ index ]. Let dynamicOffsets be encoder . [[dynamic_offsets]] [ index ]. bindGroup must not be null . bindGroup . [[layout]] must be group-equivalent with bindGroupLayout . Let dynamicOffsetIndex be 0. For each GPUBindGroupEntry bindGroupEntry in bindGroup . [[entries]] ,
sorted by bindGroupEntry . binding : Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ]. If bindGroupLayoutEntry . buffer is not provided , continue . Let bound be get as buffer binding ( bindGroupEntry . resource ). If bindGroupLayoutEntry . buffer . hasDynamicOffset : Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ]. Increment dynamicOffsetIndex by 1. If bindGroupEntry . [[prevalidatedSize]] is false : effective buffer binding size ( bound ) must be ≥ minimum buffer binding size of the binding variable in pipeline ’s shader that corresponds to bindGroupEntry . Encoder bind groups alias a writable resource ( encoder , pipeline ) must be false . If encoder . [[device]] . [[features]] does not contain "core-features-and-limits" : All bindings referring to the same GPUTexture must have compatible GPUTextureView s, determined as follows: For each pair of ( GPUIndex32 index1 , GPUBindGroupLayout bindGroupLayout1 ) in bindGroupLayouts : If bindGroupLayout1 is null , continue . Let bindGroup1 be encoder . [[bind_groups]] [ index1 ]. For each GPUBindGroupEntry bindGroupEntry1 in bindGroup1 . [[entries]] : If bindGroupEntry1 . resource is not a GPUTextureView , continue . Let descriptor1 be bindGroupEntry1 . resource . [[descriptor]] . For each pair of ( GPUIndex32 index2 , GPUBindGroupLayout bindGroupLayout2 ) in bindGroupLayouts : If bindGroupLayout2 is null , continue . Let bindGroup2 be encoder . [[bind_groups]] [ index2 ]. For each GPUBindGroupEntry bindGroupEntry2 in bindGroup2 . [[entries]] : If bindGroupEntry2 . resource is not a GPUTextureView , continue . If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue . Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] . descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel . descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount . descriptor2 . aspect must be equal to descriptor1 . aspect . descriptor2 . swizzle must be equal to descriptor1 . swizzle .
If any of the following conditions are unsatisfied, return false :
- Let bindGroupLayouts be pipeline . [[layout]] . [[bindGroupLayouts]] .
Let bindGroupLayouts be pipeline . [[layout]] . [[bindGroupLayouts]] .
- pipeline must not be null .
pipeline must not be null .
- All bind groups used by the pipeline must be set and compatible with the pipeline layout, determined as follows: For each pair of ( GPUIndex32 index , GPUBindGroupLayout bindGroupLayout ) in bindGroupLayouts : If bindGroupLayout is null , continue . Let bindGroup be encoder . [[bind_groups]] [ index ]. Let dynamicOffsets be encoder . [[dynamic_offsets]] [ index ]. bindGroup must not be null . bindGroup . [[layout]] must be group-equivalent with bindGroupLayout . Let dynamicOffsetIndex be 0. For each GPUBindGroupEntry bindGroupEntry in bindGroup . [[entries]] ,
sorted by bindGroupEntry . binding : Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ]. If bindGroupLayoutEntry . buffer is not provided , continue . Let bound be get as buffer binding ( bindGroupEntry . resource ). If bindGroupLayoutEntry . buffer . hasDynamicOffset : Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ]. Increment dynamicOffsetIndex by 1. If bindGroupEntry . [[prevalidatedSize]] is false : effective buffer binding size ( bound ) must be ≥ minimum buffer binding size of the binding variable in pipeline ’s shader that corresponds to bindGroupEntry .
All bind groups used by the pipeline must be set and compatible with the pipeline layout, determined as follows:
For each pair of ( GPUIndex32 index , GPUBindGroupLayout bindGroupLayout ) in bindGroupLayouts :
- If bindGroupLayout is null , continue .
If bindGroupLayout is null , continue .
- Let bindGroup be encoder . [[bind_groups]] [ index ].
Let bindGroup be encoder . [[bind_groups]] [ index ].
- Let dynamicOffsets be encoder . [[dynamic_offsets]] [ index ].
Let dynamicOffsets be encoder . [[dynamic_offsets]] [ index ].
- bindGroup must not be null .
bindGroup must not be null .
- bindGroup . [[layout]] must be group-equivalent with bindGroupLayout .
bindGroup . [[layout]] must be group-equivalent with bindGroupLayout .
- Let dynamicOffsetIndex be 0.
Let dynamicOffsetIndex be 0.
- For each GPUBindGroupEntry bindGroupEntry in bindGroup . [[entries]] ,
sorted by bindGroupEntry . binding : Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ]. If bindGroupLayoutEntry . buffer is not provided , continue . Let bound be get as buffer binding ( bindGroupEntry . resource ). If bindGroupLayoutEntry . buffer . hasDynamicOffset : Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ]. Increment dynamicOffsetIndex by 1. If bindGroupEntry . [[prevalidatedSize]] is false : effective buffer binding size ( bound ) must be ≥ minimum buffer binding size of the binding variable in pipeline ’s shader that corresponds to bindGroupEntry .
For each GPUBindGroupEntry bindGroupEntry in bindGroup . [[entries]] ,
sorted by bindGroupEntry . binding :
- Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ].
Let bindGroupLayoutEntry be bindGroup . [[layout]] . [[entryMap]] [ bindGroupEntry . binding ].
- If bindGroupLayoutEntry . buffer is not provided , continue .
If bindGroupLayoutEntry . buffer is not provided , continue .
- Let bound be get as buffer binding ( bindGroupEntry . resource ).
Let bound be get as buffer binding ( bindGroupEntry . resource ).
- If bindGroupLayoutEntry . buffer . hasDynamicOffset : Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ]. Increment dynamicOffsetIndex by 1.
If bindGroupLayoutEntry . buffer . hasDynamicOffset :
- Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ].
Increment bound . offset by dynamicOffsets [ dynamicOffsetIndex ].
- Increment dynamicOffsetIndex by 1.
Increment dynamicOffsetIndex by 1.
- If bindGroupEntry . [[prevalidatedSize]] is false : effective buffer binding size ( bound ) must be ≥ minimum buffer binding size of the binding variable in pipeline ’s shader that corresponds to bindGroupEntry .
If bindGroupEntry . [[prevalidatedSize]] is false :
- effective buffer binding size ( bound ) must be ≥ minimum buffer binding size of the binding variable in pipeline ’s shader that corresponds to bindGroupEntry .
effective buffer binding size ( bound ) must be ≥ minimum buffer binding size of the binding variable in pipeline ’s shader that corresponds to bindGroupEntry .
- Encoder bind groups alias a writable resource ( encoder , pipeline ) must be false .
Encoder bind groups alias a writable resource ( encoder , pipeline ) must be false .
- If encoder . [[device]] . [[features]] does not contain "core-features-and-limits" : All bindings referring to the same GPUTexture must have compatible GPUTextureView s, determined as follows: For each pair of ( GPUIndex32 index1 , GPUBindGroupLayout bindGroupLayout1 ) in bindGroupLayouts : If bindGroupLayout1 is null , continue . Let bindGroup1 be encoder . [[bind_groups]] [ index1 ]. For each GPUBindGroupEntry bindGroupEntry1 in bindGroup1 . [[entries]] : If bindGroupEntry1 . resource is not a GPUTextureView , continue . Let descriptor1 be bindGroupEntry1 . resource . [[descriptor]] . For each pair of ( GPUIndex32 index2 , GPUBindGroupLayout bindGroupLayout2 ) in bindGroupLayouts : If bindGroupLayout2 is null , continue . Let bindGroup2 be encoder . [[bind_groups]] [ index2 ]. For each GPUBindGroupEntry bindGroupEntry2 in bindGroup2 . [[entries]] : If bindGroupEntry2 . resource is not a GPUTextureView , continue . If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue . Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] . descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel . descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount . descriptor2 . aspect must be equal to descriptor1 . aspect . descriptor2 . swizzle must be equal to descriptor1 . swizzle .
- All bindings referring to the same GPUTexture must have compatible GPUTextureView s, determined as follows: For each pair of ( GPUIndex32 index1 , GPUBindGroupLayout bindGroupLayout1 ) in bindGroupLayouts : If bindGroupLayout1 is null , continue . Let bindGroup1 be encoder . [[bind_groups]] [ index1 ]. For each GPUBindGroupEntry bindGroupEntry1 in bindGroup1 . [[entries]] : If bindGroupEntry1 . resource is not a GPUTextureView , continue . Let descriptor1 be bindGroupEntry1 . resource . [[descriptor]] . For each pair of ( GPUIndex32 index2 , GPUBindGroupLayout bindGroupLayout2 ) in bindGroupLayouts : If bindGroupLayout2 is null , continue . Let bindGroup2 be encoder . [[bind_groups]] [ index2 ]. For each GPUBindGroupEntry bindGroupEntry2 in bindGroup2 . [[entries]] : If bindGroupEntry2 . resource is not a GPUTextureView , continue . If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue . Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] . descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel . descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount . descriptor2 . aspect must be equal to descriptor1 . aspect . descriptor2 . swizzle must be equal to descriptor1 . swizzle .
All bindings referring to the same GPUTexture must have compatible GPUTextureView s, determined as follows:
For each pair of ( GPUIndex32 index1 , GPUBindGroupLayout bindGroupLayout1 ) in bindGroupLayouts :
- If bindGroupLayout1 is null , continue .
If bindGroupLayout1 is null , continue .
- Let bindGroup1 be encoder . [[bind_groups]] [ index1 ].
Let bindGroup1 be encoder . [[bind_groups]] [ index1 ].
- For each GPUBindGroupEntry bindGroupEntry1 in bindGroup1 . [[entries]] : If bindGroupEntry1 . resource is not a GPUTextureView , continue . Let descriptor1 be bindGroupEntry1 . resource . [[descriptor]] . For each pair of ( GPUIndex32 index2 , GPUBindGroupLayout bindGroupLayout2 ) in bindGroupLayouts : If bindGroupLayout2 is null , continue . Let bindGroup2 be encoder . [[bind_groups]] [ index2 ]. For each GPUBindGroupEntry bindGroupEntry2 in bindGroup2 . [[entries]] : If bindGroupEntry2 . resource is not a GPUTextureView , continue . If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue . Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] . descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel . descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount . descriptor2 . aspect must be equal to descriptor1 . aspect . descriptor2 . swizzle must be equal to descriptor1 . swizzle .
For each GPUBindGroupEntry bindGroupEntry1 in bindGroup1 . [[entries]] :
- If bindGroupEntry1 . resource is not a GPUTextureView , continue .
If bindGroupEntry1 . resource is not a GPUTextureView , continue .
- Let descriptor1 be bindGroupEntry1 . resource . [[descriptor]] .
Let descriptor1 be bindGroupEntry1 . resource . [[descriptor]] .
- For each pair of ( GPUIndex32 index2 , GPUBindGroupLayout bindGroupLayout2 ) in bindGroupLayouts : If bindGroupLayout2 is null , continue . Let bindGroup2 be encoder . [[bind_groups]] [ index2 ]. For each GPUBindGroupEntry bindGroupEntry2 in bindGroup2 . [[entries]] : If bindGroupEntry2 . resource is not a GPUTextureView , continue . If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue . Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] . descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel . descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount . descriptor2 . aspect must be equal to descriptor1 . aspect . descriptor2 . swizzle must be equal to descriptor1 . swizzle .
For each pair of ( GPUIndex32 index2 , GPUBindGroupLayout bindGroupLayout2 ) in bindGroupLayouts :
- If bindGroupLayout2 is null , continue .
If bindGroupLayout2 is null , continue .
- Let bindGroup2 be encoder . [[bind_groups]] [ index2 ].
Let bindGroup2 be encoder . [[bind_groups]] [ index2 ].
- For each GPUBindGroupEntry bindGroupEntry2 in bindGroup2 . [[entries]] : If bindGroupEntry2 . resource is not a GPUTextureView , continue . If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue . Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] . descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel . descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount . descriptor2 . aspect must be equal to descriptor1 . aspect . descriptor2 . swizzle must be equal to descriptor1 . swizzle .
For each GPUBindGroupEntry bindGroupEntry2 in bindGroup2 . [[entries]] :
- If bindGroupEntry2 . resource is not a GPUTextureView , continue .
If bindGroupEntry2 . resource is not a GPUTextureView , continue .
- If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue .
If bindGroupEntry1 . resource . [[texture]] is not equal to bindGroupEntry2 . resource . [[texture]] , continue .
- Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] .
Let descriptor2 be bindGroupEntry2 . resource . [[descriptor]] .
- descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel .
descriptor2 . baseMipLevel must be equal to descriptor1 . baseMipLevel .
- descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount .
descriptor2 . mipLevelCount must be equal to descriptor1 . mipLevelCount .
- descriptor2 . aspect must be equal to descriptor1 . aspect .
descriptor2 . aspect must be equal to descriptor1 . aspect .
- descriptor2 . swizzle must be equal to descriptor1 . swizzle .
descriptor2 . swizzle must be equal to descriptor1 . swizzle .
Otherwise return true .
Note: This algorithm limits the use of the usage scope storage exception .
Arguments:
Encoder whose bind groups are being validated.
Pipeline to validate encoder s bind groups are compatible with.
Device timeline steps:
- For each stage in [ VERTEX , FRAGMENT , COMPUTE ]: Let bufferBindings be a list of ( GPUBufferBinding , boolean ) pairs,
where the latter indicates whether the resource was used as writable. Let textureViews be a list of ( GPUTextureView , boolean ) pairs,
where the latter indicates whether the resource was used as writable. For each pair of ( GPUIndex32 bindGroupIndex , GPUBindGroupLayout bindGroupLayout ) in pipeline . [[layout]] . [[bindGroupLayouts]] : Let bindGroup be encoder . [[bind_groups]] [ bindGroupIndex ]. Let bindGroupLayoutEntries be bindGroupLayout . [[descriptor]] . entries . Let bufferRanges be the bound buffer ranges of bindGroup ,
given dynamic offsets encoder . [[dynamic_offsets]] [ bindGroupIndex ] For each ( GPUBindGroupLayoutEntry bindGroupLayoutEntry , GPUBufferBinding resource ) in bufferRanges , in which bindGroupLayoutEntry . visibility contains stage : Let resourceWritable be ( bindGroupLayoutEntry . buffer . type == "storage" ). For each pair ( GPUBufferBinding pastResource , boolean pastResourceWritable ) in bufferBindings : If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource are buffer-binding-aliasing , return true . Append ( resource , resourceWritable ) to bufferBindings . For each GPUBindGroupLayoutEntry bindGroupLayoutEntry in bindGroupLayoutEntries , and corresponding GPUTextureView resource in bindGroup , in which bindGroupLayoutEntry . visibility contains stage : If bindGroupLayoutEntry . storageTexture is not provided , continue . Let resourceWritable be whether bindGroupLayoutEntry . storageTexture . access is a writable access mode. For each pair ( GPUTextureView pastResource , boolean pastResourceWritable ) in textureViews , If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource is texture-view-aliasing , return true . Append ( resource , resourceWritable ) to textureViews .
For each stage in [ VERTEX , FRAGMENT , COMPUTE ]:
- Let bufferBindings be a list of ( GPUBufferBinding , boolean ) pairs,
where the latter indicates whether the resource was used as writable.
Let bufferBindings be a list of ( GPUBufferBinding , boolean ) pairs,
where the latter indicates whether the resource was used as writable.
- Let textureViews be a list of ( GPUTextureView , boolean ) pairs,
where the latter indicates whether the resource was used as writable.
Let textureViews be a list of ( GPUTextureView , boolean ) pairs,
where the latter indicates whether the resource was used as writable.
- For each pair of ( GPUIndex32 bindGroupIndex , GPUBindGroupLayout bindGroupLayout ) in pipeline . [[layout]] . [[bindGroupLayouts]] : Let bindGroup be encoder . [[bind_groups]] [ bindGroupIndex ]. Let bindGroupLayoutEntries be bindGroupLayout . [[descriptor]] . entries . Let bufferRanges be the bound buffer ranges of bindGroup ,
given dynamic offsets encoder . [[dynamic_offsets]] [ bindGroupIndex ] For each ( GPUBindGroupLayoutEntry bindGroupLayoutEntry , GPUBufferBinding resource ) in bufferRanges , in which bindGroupLayoutEntry . visibility contains stage : Let resourceWritable be ( bindGroupLayoutEntry . buffer . type == "storage" ). For each pair ( GPUBufferBinding pastResource , boolean pastResourceWritable ) in bufferBindings : If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource are buffer-binding-aliasing , return true . Append ( resource , resourceWritable ) to bufferBindings . For each GPUBindGroupLayoutEntry bindGroupLayoutEntry in bindGroupLayoutEntries , and corresponding GPUTextureView resource in bindGroup , in which bindGroupLayoutEntry . visibility contains stage : If bindGroupLayoutEntry . storageTexture is not provided , continue . Let resourceWritable be whether bindGroupLayoutEntry . storageTexture . access is a writable access mode. For each pair ( GPUTextureView pastResource , boolean pastResourceWritable ) in textureViews , If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource is texture-view-aliasing , return true . Append ( resource , resourceWritable ) to textureViews .
For each pair of ( GPUIndex32 bindGroupIndex , GPUBindGroupLayout bindGroupLayout ) in pipeline . [[layout]] . [[bindGroupLayouts]] :
- Let bindGroup be encoder . [[bind_groups]] [ bindGroupIndex ].
Let bindGroup be encoder . [[bind_groups]] [ bindGroupIndex ].
- Let bindGroupLayoutEntries be bindGroupLayout . [[descriptor]] . entries .
Let bindGroupLayoutEntries be bindGroupLayout . [[descriptor]] . entries .
- Let bufferRanges be the bound buffer ranges of bindGroup ,
given dynamic offsets encoder . [[dynamic_offsets]] [ bindGroupIndex ]
Let bufferRanges be the bound buffer ranges of bindGroup ,
given dynamic offsets encoder . [[dynamic_offsets]] [ bindGroupIndex ]
- For each ( GPUBindGroupLayoutEntry bindGroupLayoutEntry , GPUBufferBinding resource ) in bufferRanges , in which bindGroupLayoutEntry . visibility contains stage : Let resourceWritable be ( bindGroupLayoutEntry . buffer . type == "storage" ). For each pair ( GPUBufferBinding pastResource , boolean pastResourceWritable ) in bufferBindings : If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource are buffer-binding-aliasing , return true . Append ( resource , resourceWritable ) to bufferBindings .
For each ( GPUBindGroupLayoutEntry bindGroupLayoutEntry , GPUBufferBinding resource ) in bufferRanges , in which bindGroupLayoutEntry . visibility contains stage :
- Let resourceWritable be ( bindGroupLayoutEntry . buffer . type == "storage" ).
Let resourceWritable be ( bindGroupLayoutEntry . buffer . type == "storage" ).
- For each pair ( GPUBufferBinding pastResource , boolean pastResourceWritable ) in bufferBindings : If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource are buffer-binding-aliasing , return true .
For each pair ( GPUBufferBinding pastResource , boolean pastResourceWritable ) in bufferBindings :
- If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource are buffer-binding-aliasing , return true .
If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource are buffer-binding-aliasing , return true .
- Append ( resource , resourceWritable ) to bufferBindings .
Append ( resource , resourceWritable ) to bufferBindings .
- For each GPUBindGroupLayoutEntry bindGroupLayoutEntry in bindGroupLayoutEntries , and corresponding GPUTextureView resource in bindGroup , in which bindGroupLayoutEntry . visibility contains stage : If bindGroupLayoutEntry . storageTexture is not provided , continue . Let resourceWritable be whether bindGroupLayoutEntry . storageTexture . access is a writable access mode. For each pair ( GPUTextureView pastResource , boolean pastResourceWritable ) in textureViews , If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource is texture-view-aliasing , return true . Append ( resource , resourceWritable ) to textureViews .
For each GPUBindGroupLayoutEntry bindGroupLayoutEntry in bindGroupLayoutEntries , and corresponding GPUTextureView resource in bindGroup , in which bindGroupLayoutEntry . visibility contains stage :
- If bindGroupLayoutEntry . storageTexture is not provided , continue .
If bindGroupLayoutEntry . storageTexture is not provided , continue .
- Let resourceWritable be whether bindGroupLayoutEntry . storageTexture . access is a writable access mode.
Let resourceWritable be whether bindGroupLayoutEntry . storageTexture . access is a writable access mode.
- For each pair ( GPUTextureView pastResource , boolean pastResourceWritable ) in textureViews , If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource is texture-view-aliasing , return true .
For each pair ( GPUTextureView pastResource , boolean pastResourceWritable ) in textureViews ,
- If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource is texture-view-aliasing , return true .
If ( resourceWritable or pastResourceWritable ) is true, and pastResource and resource is texture-view-aliasing , return true .
- Append ( resource , resourceWritable ) to textureViews .
Append ( resource , resourceWritable ) to textureViews .
- Return false .
Return false .
Note: Implementations are strongly encouraged to optimize this algorithm.

## 15. Debug Markers

GPUDebugCommandsMixin provides methods to apply debug labels to groups
of commands or insert a single label into the command sequence.
Debug groups can be nested to create a hierarchy of labeled commands, and must be well-balanced.
Like object labels , these labels have no required behavior, but may be shown
in error messages and browser developer tools, and may be passed to native API backends.
GPUDebugCommandsMixin assumes the presence of GPUObjectBase and GPUCommandsMixin members on the same object.
It must only be included by interfaces which also include those mixins.
GPUDebugCommandsMixin has the following device timeline properties :
A stack of active debug group labels.
GPUDebugCommandsMixin has the following methods:
Begins a labeled debug group containing subsequent commands.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Push groupLabel onto this . [[debug_group_stack]] .
Push groupLabel onto this . [[debug_group_stack]] .
Ends the labeled debug group most recently started by pushDebugGroup() .
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following requirements are unmet, invalidate this and return. this . [[debug_group_stack]] must not be empty .
If any of the following requirements are unmet, invalidate this and return.
- this . [[debug_group_stack]] must not be empty .
this . [[debug_group_stack]] must not be empty .
- Pop an entry off of this . [[debug_group_stack]] .
Pop an entry off of this . [[debug_group_stack]] .
Marks a point in a stream of commands with a label.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.

## 16. Compute Passes

### 16.1. GPUComputePassEncoder

GPUComputePassEncoder has the following device timeline properties :
The GPUCommandEncoder that created this compute pass encoder.
GPU command , if any, writing a timestamp when the pass ends.
The current GPUComputePipeline .
The GPUQuerySet , of type "timestamp" , that the query results will be
written to.
If defined, indicates the query index in querySet into
which the timestamp at the beginning of the compute pass will be written.
If defined, indicates the query index in querySet into
which the timestamp at the end of the compute pass will be written.
Note: Timestamp query values are written in nanoseconds, but how the value is determined is implementation-defined . See § 20.4 Timestamp Query for details.
Defines which timestamp values will be written for this pass, and where to write them to.
Sets the current GPUComputePipeline .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. pipeline is valid to use with this .
If any of the following conditions are unsatisfied, invalidate this and return.
- pipeline is valid to use with this .
pipeline is valid to use with this .
- Set this . [[pipeline]] to be pipeline .
Set this . [[pipeline]] to be pipeline .
Dispatch work to be performed with the current GPUComputePipeline .
See § 23.1 Computing for the detailed specification.
Arguments:
This means that if a GPUShaderModule defines an entry point with @workgroup_size(4, 4) , and work is dispatched to it with the call computePass.dispatchWorkgroups(8, 8); the entry point will be invoked 1024 times
            total: Dispatching a 4x4 workgroup 8 times along both the X and Y axes.
            ( 4*4*8*8=1024 )
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let usageScope be an empty usage scope .
Let usageScope be an empty usage scope .
- For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
- If any of the following conditions are unsatisfied, invalidate this and return. usageScope must satisfy usage scope validation . Validate encoder bind groups ( this , this . [[pipeline]] )
is true . all of workgroupCountX , workgroupCountY and workgroupCountZ are ≤ this .device.limits. maxComputeWorkgroupsPerDimension .
If any of the following conditions are unsatisfied, invalidate this and return.
- usageScope must satisfy usage scope validation .
usageScope must satisfy usage scope validation .
- Validate encoder bind groups ( this , this . [[pipeline]] )
is true .
Validate encoder bind groups ( this , this . [[pipeline]] )
is true .
- all of workgroupCountX , workgroupCountY and workgroupCountZ are ≤ this .device.limits. maxComputeWorkgroupsPerDimension .
all of workgroupCountX , workgroupCountY and workgroupCountZ are ≤ this .device.limits. maxComputeWorkgroupsPerDimension .
- Let bindingState be a snapshot of this ’s current state.
Let bindingState be a snapshot of this ’s current state.
- Enqueue a command on this which issues the subsequent steps on the Queue timeline .
Enqueue a command on this which issues the subsequent steps on the Queue timeline .
- Execute a grid of workgroups with dimensions [ workgroupCountX , workgroupCountY , workgroupCountZ ] with bindingState . [[pipeline]] using bindingState . [[bind_groups]] .
Execute a grid of workgroups with dimensions [ workgroupCountX , workgroupCountY , workgroupCountZ ] with bindingState . [[pipeline]] using bindingState . [[bind_groups]] .
Dispatch work to be performed with the current GPUComputePipeline using parameters read
from a GPUBuffer .
See § 23.1 Computing for the detailed specification.
The indirect dispatch parameters encoded in the buffer must be a tightly
packed block of three 32-bit unsigned integer values (12 bytes total) ,
given in the same order as the arguments for dispatchWorkgroups() .
For example:
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let usageScope be an empty usage scope .
Let usageScope be an empty usage scope .
- For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
For each bindGroup in this . [[bind_groups]] , merge bindGroup . [[usedResources]] into this . [[usage scope]]
- Add indirectBuffer to usageScope with usage input .
Add indirectBuffer to usageScope with usage input .
- If any of the following conditions are unsatisfied, invalidate this and return. usageScope must satisfy usage scope validation . Validate encoder bind groups ( this , this . [[pipeline]] )
is true . indirectBuffer is valid to use with this . indirectBuffer . usage contains INDIRECT . indirectOffset + sizeof( indirect dispatch parameters ) ≤ indirectBuffer . size . indirectOffset is a multiple of 4.
If any of the following conditions are unsatisfied, invalidate this and return.
- usageScope must satisfy usage scope validation .
usageScope must satisfy usage scope validation .
- Validate encoder bind groups ( this , this . [[pipeline]] )
is true .
Validate encoder bind groups ( this , this . [[pipeline]] )
is true .
- indirectBuffer is valid to use with this .
indirectBuffer is valid to use with this .
- indirectBuffer . usage contains INDIRECT .
indirectBuffer . usage contains INDIRECT .
- indirectOffset + sizeof( indirect dispatch parameters ) ≤ indirectBuffer . size .
indirectOffset + sizeof( indirect dispatch parameters ) ≤ indirectBuffer . size .
- indirectOffset is a multiple of 4.
indirectOffset is a multiple of 4.
- Let bindingState be a snapshot of this ’s current state.
Let bindingState be a snapshot of this ’s current state.
- Enqueue a command on this which issues the subsequent steps on the Queue timeline .
Enqueue a command on this which issues the subsequent steps on the Queue timeline .
- Let workgroupCountX be an unsigned 32-bit integer read from indirectBuffer at indirectOffset bytes.
Let workgroupCountX be an unsigned 32-bit integer read from indirectBuffer at indirectOffset bytes.
- Let workgroupCountY be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 4) bytes.
Let workgroupCountY be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 4) bytes.
- Let workgroupCountZ be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 8) bytes.
Let workgroupCountZ be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 8) bytes.
- If workgroupCountX , workgroupCountY , or workgroupCountZ is greater than this .device.limits. maxComputeWorkgroupsPerDimension ,
return.
If workgroupCountX , workgroupCountY , or workgroupCountZ is greater than this .device.limits. maxComputeWorkgroupsPerDimension ,
return.
- Execute a grid of workgroups with dimensions [ workgroupCountX , workgroupCountY , workgroupCountZ ] with bindingState . [[pipeline]] using bindingState . [[bind_groups]] .
Execute a grid of workgroups with dimensions [ workgroupCountX , workgroupCountY , workgroupCountZ ] with bindingState . [[pipeline]] using bindingState . [[bind_groups]] .
The compute pass encoder can be ended by calling end() once the user
has finished recording commands for the pass. Once end() has been
called the compute pass encoder can no longer be used.
Completes recording of the compute pass commands sequence.
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Let parentEncoder be this . [[command_encoder]] .
Let parentEncoder be this . [[command_encoder]] .
- If any of the following requirements are unmet, generate a validation error and return. this . [[state]] must be " open ". parentEncoder . [[state]] must be " locked ".
If any of the following requirements are unmet, generate a validation error and return.
- this . [[state]] must be " open ".
this . [[state]] must be " open ".
- parentEncoder . [[state]] must be " locked ".
parentEncoder . [[state]] must be " locked ".
- Set this . [[state]] to " ended ".
Set this . [[state]] to " ended ".
- Set parentEncoder . [[state]] to " open ".
Set parentEncoder . [[state]] to " open ".
- Extend parentEncoder . [[used_bind_groups]] with this . [[used_bind_groups]] .
Extend parentEncoder . [[used_bind_groups]] with this . [[used_bind_groups]] .
- If any of the following requirements are unmet, invalidate parentEncoder and return. this must be valid . this . [[debug_group_stack]] must be empty .
If any of the following requirements are unmet, invalidate parentEncoder and return.
- this must be valid .
this must be valid .
- this . [[debug_group_stack]] must be empty .
this . [[debug_group_stack]] must be empty .
- Extend parentEncoder . [[commands]] with this . [[commands]] .
Extend parentEncoder . [[commands]] with this . [[commands]] .
- If this . [[endTimestampWrite]] is not null : Extend parentEncoder . [[commands]] with this . [[endTimestampWrite]] .
If this . [[endTimestampWrite]] is not null :
- Extend parentEncoder . [[commands]] with this . [[endTimestampWrite]] .
Extend parentEncoder . [[commands]] with this . [[endTimestampWrite]] .

## 17. Render Passes

### 17.1. GPURenderPassEncoder

GPURenderPassEncoder has the following device timeline properties :
The GPUCommandEncoder that created this render pass encoder.
Set to the following extents:
- width, height = the dimensions of the pass’s render attachments
width, height = the dimensions of the pass’s render attachments
The GPUQuerySet to store occlusion query results for the pass, which is initialized with GPURenderPassDescriptor . occlusionQuerySet at pass creation time.
GPU command , if any, writing a timestamp when the pass ends.
The maximum number of draws allowed in this pass.
Whether the pass’s [[occlusion_query_set]] is being written.
When executing encoded render pass commands as part of a GPUCommandBuffer , an internal RenderState object is used to track the current state required for rendering.
RenderState has the following queue timeline properties :
The index into [[occlusion_query_set]] at which to store the
occlusion query results.
Current viewport rectangle and depth range. Initially set to the following values:
- x, y = 0.0, 0.0
x, y = 0.0, 0.0
- width, height = the dimensions of the pass’s render targets
width, height = the dimensions of the pass’s render targets
- minDepth, maxDepth = 0.0, 1.0
minDepth, maxDepth = 0.0, 1.0
Current scissor rectangle. Initially set to the following values:
- x, y = 0, 0
x, y = 0, 0
- width, height = the dimensions of the pass’s render targets
width, height = the dimensions of the pass’s render targets
Current blend constant value, initially [0, 0, 0, 0] .
Current stencil reference value, initially 0 .
The color attachments and state for this render pass.
The depth/stencil attachment and state for this render pass.
Render passes also have framebuffer memory , which contains the texel data associated with
each attachment that is written into by draw commands and read from for blending and depth/stencil testing.
Note: Depending on the GPU hardware, framebuffer memory may be the memory allocated by the attachment textures or
may be a separate area of memory that the texture data is copied to and from, such as with tile-based architectures.
The GPUQuerySet , of type "timestamp" , that the query results will be
written to.
If defined, indicates the query index in querySet into
which the timestamp at the beginning of the render pass will be written.
If defined, indicates the query index in querySet into
which the timestamp at the end of the render pass will be written.
Note: Timestamp query values are written in nanoseconds, but how the value is determined is implementation-defined . See § 20.4 Timestamp Query for details.
The set of GPURenderPassColorAttachment values in this sequence defines which
color attachments will be output to when executing this render pass.
Due to usage compatibility , no color attachment
may alias another attachment or any resource used inside the render pass.
The GPURenderPassDepthStencilAttachment value that defines the depth/stencil
attachment that will be output to and tested against when executing this render pass.
Due to usage compatibility , no writable depth/stencil attachment
may alias another attachment or any resource used inside the render pass.
The GPUQuerySet value defines where the occlusion query results will be stored for this pass.
Defines which timestamp values will be written for this pass, and where to write them to.
The maximum number of draw calls that will be done in the render pass. Used by some
implementations to size work injected before the render pass. Keeping the default value
is a good default, unless it is known that more draw calls will be done.
Given a GPUDevice device and GPURenderPassDescriptor this , the following validation rules apply:
- this . colorAttachments . size must be ≤ device . [[limits]] . maxColorAttachments .
this . colorAttachments . size must be ≤ device . [[limits]] . maxColorAttachments .
- For each non- null colorAttachment in this . colorAttachments : colorAttachment . view must be valid to use with device . If colorAttachment . resolveTarget is provided : colorAttachment . resolveTarget must be valid to use with device . colorAttachment must meet the GPURenderPassColorAttachment Valid Usage rules.
For each non- null colorAttachment in this . colorAttachments :
- colorAttachment . view must be valid to use with device .
colorAttachment . view must be valid to use with device .
- If colorAttachment . resolveTarget is provided : colorAttachment . resolveTarget must be valid to use with device .
If colorAttachment . resolveTarget is provided :
- colorAttachment . resolveTarget must be valid to use with device .
colorAttachment . resolveTarget must be valid to use with device .
- colorAttachment must meet the GPURenderPassColorAttachment Valid Usage rules.
colorAttachment must meet the GPURenderPassColorAttachment Valid Usage rules.
- If this . depthStencilAttachment is provided : this . depthStencilAttachment . view must be valid to use with device . this . depthStencilAttachment must meet the GPURenderPassDepthStencilAttachment Valid Usage rules.
If this . depthStencilAttachment is provided :
- this . depthStencilAttachment . view must be valid to use with device .
this . depthStencilAttachment . view must be valid to use with device .
- this . depthStencilAttachment must meet the GPURenderPassDepthStencilAttachment Valid Usage rules.
this . depthStencilAttachment must meet the GPURenderPassDepthStencilAttachment Valid Usage rules.
- There must exist at least one attachment, either: A non- null value in this . colorAttachments , or A this . depthStencilAttachment .
There must exist at least one attachment, either:
- A non- null value in this . colorAttachments , or
A non- null value in this . colorAttachments , or
- A this . depthStencilAttachment .
A this . depthStencilAttachment .
- Validating GPURenderPassDescriptor’s color attachment bytes per sample ( device , this . colorAttachments ) succeeds.
Validating GPURenderPassDescriptor’s color attachment bytes per sample ( device , this . colorAttachments ) succeeds.
- All view s in non- null members of this . colorAttachments ,
and this . depthStencilAttachment . view if present, must have equal sampleCount s.
All view s in non- null members of this . colorAttachments ,
and this . depthStencilAttachment . view if present, must have equal sampleCount s.
- For each view in non- null members of this . colorAttachments and this . depthStencilAttachment . view ,
if present, the [[renderExtent]] must match.
For each view in non- null members of this . colorAttachments and this . depthStencilAttachment . view ,
if present, the [[renderExtent]] must match.
- If this . occlusionQuerySet is provided : this . occlusionQuerySet must be valid to use with device . this . occlusionQuerySet . type must be occlusion .
If this . occlusionQuerySet is provided :
- this . occlusionQuerySet must be valid to use with device .
this . occlusionQuerySet must be valid to use with device .
- this . occlusionQuerySet . type must be occlusion .
this . occlusionQuerySet . type must be occlusion .
- If this . timestampWrites is provided : Validate timestampWrites ( device , this . timestampWrites )
must return true.
If this . timestampWrites is provided :
- Validate timestampWrites ( device , this . timestampWrites )
must return true.
Validate timestampWrites ( device , this . timestampWrites )
must return true.
Arguments:
- GPUDevice device
GPUDevice device
- sequence < GPURenderPassColorAttachment ?> colorAttachments
sequence < GPURenderPassColorAttachment ?> colorAttachments
Device timeline steps:
- Let formats be an empty list < GPUTextureFormat ?>
Let formats be an empty list < GPUTextureFormat ?>
- For each colorAttachment in colorAttachments : If colorAttachment is undefined , continue. Append colorAttachment . view . [[descriptor]] . format to formats .
For each colorAttachment in colorAttachments :
- If colorAttachment is undefined , continue.
If colorAttachment is undefined , continue.
- Append colorAttachment . view . [[descriptor]] . format to formats .
Append colorAttachment . view . [[descriptor]] . format to formats .
- Calculating color attachment bytes per sample ( formats ) must be ≤ device . [[limits]] . maxColorAttachmentBytesPerSample .
Calculating color attachment bytes per sample ( formats ) must be ≤ device . [[limits]] . maxColorAttachmentBytesPerSample .
Describes the texture subresource that will be output to for this color attachment.
The subresource is determined by calling get as texture view ( view ).
Indicates the depth slice index of "3d" view that will be output to for this color attachment.
Describes the texture subresource that will receive the resolved output for this color
attachment if view is multisampled.
The subresource is determined by calling get as texture view ( resolveTarget ).
Indicates the value to clear view to prior to executing the
render pass. If not provided , defaults to {r: 0, g: 0, b: 0, a: 0} . Ignored
if loadOp is not "clear" .
The components of clearValue are all double values.
They are converted to a texel value of texture format matching the render attachment.
If conversion fails, a validation error is generated.
Indicates the load operation to perform on view prior to
executing the render pass.
Note: It is recommended to prefer clearing; see "clear" for details.
The store operation to perform on view after executing the render pass.
Given a GPURenderPassColorAttachment this :
- Let renderViewDescriptor be this . view . [[descriptor]] .
Let renderViewDescriptor be this . view . [[descriptor]] .
- Let renderTexture be this . view . [[texture]] .
Let renderTexture be this . view . [[texture]] .
- All of the requirements in the following steps must be met. renderViewDescriptor . format must be a color renderable format . this . view must be a renderable texture view . If renderViewDescriptor . dimension is "3d" : this . depthSlice must be provided and must be < the depthOrArrayLayers of the logical miplevel-specific texture extent of the renderTexture subresource at mipmap level renderViewDescriptor . baseMipLevel . Otherwise: this . depthSlice must not be provided . If renderViewDescriptor . usage includes the TRANSIENT_ATTACHMENT bit: this . loadOp must be "clear" . this . storeOp must be "discard" . If this . loadOp is "clear" : Converting the IDL value this . clearValue to a texel value of texture format renderViewDescriptor . format must not throw a TypeError . Note: An error is not thrown if the value is out-of-range for the format but in-range for
the corresponding WGSL primitive type ( f32 , i32 , or u32 ). If this . resolveTarget is provided : Let resolveViewDescriptor be this . resolveTarget . [[descriptor]] . Let resolveTexture be this . resolveTarget . [[texture]] . renderTexture . sampleCount must be > 1. resolveTexture . sampleCount must be 1. this . resolveTarget must be a non-3d renderable texture view . this . resolveTarget . [[renderExtent]] and this . view . [[renderExtent]] must match. resolveViewDescriptor . format must equal renderViewDescriptor . format . resolveTexture . format must equal renderTexture . format . resolveViewDescriptor . format must support resolve according to § 26.1.1 Plain color formats .
All of the requirements in the following steps must be met.
- renderViewDescriptor . format must be a color renderable format .
renderViewDescriptor . format must be a color renderable format .
- this . view must be a renderable texture view .
this . view must be a renderable texture view .
- If renderViewDescriptor . dimension is "3d" : this . depthSlice must be provided and must be < the depthOrArrayLayers of the logical miplevel-specific texture extent of the renderTexture subresource at mipmap level renderViewDescriptor . baseMipLevel . Otherwise: this . depthSlice must not be provided .
If renderViewDescriptor . dimension is "3d" :
- this . depthSlice must be provided and must be < the depthOrArrayLayers of the logical miplevel-specific texture extent of the renderTexture subresource at mipmap level renderViewDescriptor . baseMipLevel .
this . depthSlice must be provided and must be < the depthOrArrayLayers of the logical miplevel-specific texture extent of the renderTexture subresource at mipmap level renderViewDescriptor . baseMipLevel .
Otherwise:
- this . depthSlice must not be provided .
this . depthSlice must not be provided .
- If renderViewDescriptor . usage includes the TRANSIENT_ATTACHMENT bit: this . loadOp must be "clear" . this . storeOp must be "discard" .
If renderViewDescriptor . usage includes the TRANSIENT_ATTACHMENT bit:
- this . loadOp must be "clear" .
this . loadOp must be "clear" .
- this . storeOp must be "discard" .
this . storeOp must be "discard" .
- If this . loadOp is "clear" : Converting the IDL value this . clearValue to a texel value of texture format renderViewDescriptor . format must not throw a TypeError . Note: An error is not thrown if the value is out-of-range for the format but in-range for
the corresponding WGSL primitive type ( f32 , i32 , or u32 ).
If this . loadOp is "clear" :
- Converting the IDL value this . clearValue to a texel value of texture format renderViewDescriptor . format must not throw a TypeError . Note: An error is not thrown if the value is out-of-range for the format but in-range for
the corresponding WGSL primitive type ( f32 , i32 , or u32 ).
Converting the IDL value this . clearValue to a texel value of texture format renderViewDescriptor . format must not throw a TypeError .
Note: An error is not thrown if the value is out-of-range for the format but in-range for
the corresponding WGSL primitive type ( f32 , i32 , or u32 ).
- If this . resolveTarget is provided : Let resolveViewDescriptor be this . resolveTarget . [[descriptor]] . Let resolveTexture be this . resolveTarget . [[texture]] . renderTexture . sampleCount must be > 1. resolveTexture . sampleCount must be 1. this . resolveTarget must be a non-3d renderable texture view . this . resolveTarget . [[renderExtent]] and this . view . [[renderExtent]] must match. resolveViewDescriptor . format must equal renderViewDescriptor . format . resolveTexture . format must equal renderTexture . format . resolveViewDescriptor . format must support resolve according to § 26.1.1 Plain color formats .
If this . resolveTarget is provided :
- Let resolveViewDescriptor be this . resolveTarget . [[descriptor]] .
Let resolveViewDescriptor be this . resolveTarget . [[descriptor]] .
- Let resolveTexture be this . resolveTarget . [[texture]] .
Let resolveTexture be this . resolveTarget . [[texture]] .
- renderTexture . sampleCount must be > 1.
renderTexture . sampleCount must be > 1.
- resolveTexture . sampleCount must be 1.
resolveTexture . sampleCount must be 1.
- this . resolveTarget must be a non-3d renderable texture view .
this . resolveTarget must be a non-3d renderable texture view .
- this . resolveTarget . [[renderExtent]] and this . view . [[renderExtent]] must match.
this . resolveTarget . [[renderExtent]] and this . view . [[renderExtent]] must match.
- resolveViewDescriptor . format must equal renderViewDescriptor . format .
resolveViewDescriptor . format must equal renderViewDescriptor . format .
- resolveTexture . format must equal renderTexture . format .
resolveTexture . format must equal renderTexture . format .
- resolveViewDescriptor . format must support resolve according to § 26.1.1 Plain color formats .
resolveViewDescriptor . format must support resolve according to § 26.1.1 Plain color formats .
- Let descriptor be view . [[descriptor]] .
Let descriptor be view . [[descriptor]] .
- descriptor . usage must contain RENDER_ATTACHMENT .
descriptor . usage must contain RENDER_ATTACHMENT .
- descriptor . dimension must be "2d" or "2d-array" or "3d" .
descriptor . dimension must be "2d" or "2d-array" or "3d" .
- descriptor . mipLevelCount must be 1.
descriptor . mipLevelCount must be 1.
- descriptor . arrayLayerCount must be 1.
descriptor . arrayLayerCount must be 1.
- descriptor . aspect must refer to all aspects of view . [[texture]] .
descriptor . aspect must refer to all aspects of view . [[texture]] .
- descriptor . swizzle must be "rgba" .
descriptor . swizzle must be "rgba" .
Arguments:
- sequence < GPUTextureFormat ?> formats
sequence < GPUTextureFormat ?> formats
Returns: GPUSize32
- Let total be 0.
Let total be 0.
- For each non-null format in formats Assert : format is a color renderable format . Let renderTargetPixelByteCost be the render target pixel byte cost of format . Let renderTargetComponentAlignment be the render target component alignment of format . Round total up to the smallest multiple of renderTargetComponentAlignment greater than or equal to total . Add renderTargetPixelByteCost to total .
For each non-null format in formats
- Assert : format is a color renderable format .
Assert : format is a color renderable format .
- Let renderTargetPixelByteCost be the render target pixel byte cost of format .
Let renderTargetPixelByteCost be the render target pixel byte cost of format .
- Let renderTargetComponentAlignment be the render target component alignment of format .
Let renderTargetComponentAlignment be the render target component alignment of format .
- Round total up to the smallest multiple of renderTargetComponentAlignment greater than or equal to total .
Round total up to the smallest multiple of renderTargetComponentAlignment greater than or equal to total .
- Add renderTargetPixelByteCost to total .
Add renderTargetPixelByteCost to total .
- Return total .
Return total .
Describes the texture subresource that will be output to and read from for this
depth/stencil attachment.
The subresource is determined by calling get as texture view ( view ).
Indicates the value to clear view ’s depth component
to prior to executing the render pass. Ignored if depthLoadOp is not "clear" . Must be between 0.0 and 1.0, inclusive.
Indicates the load operation to perform on view ’s
depth component prior to executing the render pass.
Note: It is recommended to prefer clearing; see "clear" for details.
The store operation to perform on view ’s
depth component after executing the render pass.
Indicates that the depth component of view is read only.
Indicates the value to clear view ’s stencil component
to prior to executing the render pass. Ignored if stencilLoadOp is not "clear" .
The value will be converted to the type of the stencil aspect of view by taking the same
number of LSBs as the number of bits in the stencil aspect of one texel of view .
Indicates the load operation to perform on view ’s
stencil component prior to executing the render pass.
Note: It is recommended to prefer clearing; see "clear" for details.
The store operation to perform on view ’s
stencil component after executing the render pass.
Indicates that the stencil component of view is read only.
Given a GPURenderPassDepthStencilAttachment this :
- Let format be this . view . [[descriptor]] . format .
Let format be this . view . [[descriptor]] . format .
- Let usage be this . view . [[descriptor]] . usage .
Let usage be this . view . [[descriptor]] . usage .
- All of the requirements in the following steps must be met. this . view must have a depth-or-stencil format . this . view must be a renderable texture view . If this . depthLoadOp is "clear" , this . depthClearValue must be provided and must be between 0.0 and 1.0,
inclusive. If format has a depth aspect and this . depthReadOnly is false : this . depthLoadOp must be provided . this . depthStoreOp must be provided . Otherwise: this . depthLoadOp must not be provided . this . depthStoreOp must not be provided . If format has a stencil aspect and this . stencilReadOnly is false : this . stencilLoadOp must be provided . this . stencilStoreOp must be provided . Otherwise: this . stencilLoadOp must not be provided . this . stencilStoreOp must not be provided . If usage includes the TRANSIENT_ATTACHMENT bit: If format has a depth aspect: this . depthLoadOp must be "clear" . this . depthStoreOp must be "discard" . If format has a stencil aspect: this . stencilLoadOp must be "clear" . this . stencilStoreOp must be "discard" .
All of the requirements in the following steps must be met.
- this . view must have a depth-or-stencil format .
this . view must have a depth-or-stencil format .
- this . view must be a renderable texture view .
this . view must be a renderable texture view .
- If this . depthLoadOp is "clear" , this . depthClearValue must be provided and must be between 0.0 and 1.0,
inclusive.
If this . depthLoadOp is "clear" , this . depthClearValue must be provided and must be between 0.0 and 1.0,
inclusive.
- If format has a depth aspect and this . depthReadOnly is false : this . depthLoadOp must be provided . this . depthStoreOp must be provided . Otherwise: this . depthLoadOp must not be provided . this . depthStoreOp must not be provided .
If format has a depth aspect and this . depthReadOnly is false :
- this . depthLoadOp must be provided .
this . depthLoadOp must be provided .
- this . depthStoreOp must be provided .
this . depthStoreOp must be provided .
Otherwise:
- this . depthLoadOp must not be provided .
this . depthLoadOp must not be provided .
- this . depthStoreOp must not be provided .
this . depthStoreOp must not be provided .
- If format has a stencil aspect and this . stencilReadOnly is false : this . stencilLoadOp must be provided . this . stencilStoreOp must be provided . Otherwise: this . stencilLoadOp must not be provided . this . stencilStoreOp must not be provided .
If format has a stencil aspect and this . stencilReadOnly is false :
- this . stencilLoadOp must be provided .
this . stencilLoadOp must be provided .
- this . stencilStoreOp must be provided .
this . stencilStoreOp must be provided .
Otherwise:
- this . stencilLoadOp must not be provided .
this . stencilLoadOp must not be provided .
- this . stencilStoreOp must not be provided .
this . stencilStoreOp must not be provided .
- If usage includes the TRANSIENT_ATTACHMENT bit: If format has a depth aspect: this . depthLoadOp must be "clear" . this . depthStoreOp must be "discard" . If format has a stencil aspect: this . stencilLoadOp must be "clear" . this . stencilStoreOp must be "discard" .
If usage includes the TRANSIENT_ATTACHMENT bit:
- If format has a depth aspect: this . depthLoadOp must be "clear" . this . depthStoreOp must be "discard" .
If format has a depth aspect:
- this . depthLoadOp must be "clear" .
this . depthLoadOp must be "clear" .
- this . depthStoreOp must be "discard" .
this . depthStoreOp must be "discard" .
- If format has a stencil aspect: this . stencilLoadOp must be "clear" . this . stencilStoreOp must be "discard" .
If format has a stencil aspect:
- this . stencilLoadOp must be "clear" .
this . stencilLoadOp must be "clear" .
- this . stencilStoreOp must be "discard" .
this . stencilStoreOp must be "discard" .
Loads the existing value for this attachment into the render pass.
Loads a clear value for this attachment into the render pass.
Note: On some GPU hardware (primarily mobile), "clear" is significantly cheaper
because it avoids loading data from main memory into tile-local memory.
On other GPU hardware, there isn’t a significant difference. As a result, it is
recommended to use "clear" rather than "load" in cases where the
initial value doesn’t matter (e.g. the render target will be cleared using a skybox).
Stores the resulting value of the render pass for this attachment.
Discards the resulting value of the render pass for this attachment.
Note: Discarded attachments
behave as if they are cleared to zero, but implementations are not required to perform a
clear at the end of the render pass. Implementations which do not explicitly clear discarded
attachments at the end of a pass must lazily clear them prior to the reading the attachment
contents, which occurs via sampling, copies, attaching to a later render pass with "load" , displaying or reading back the canvas
( get a copy of the image contents of a context ), etc.
GPURenderPassLayout declares the layout of the render targets of a GPURenderBundle .
It is also used internally to describe GPURenderPassEncoder layouts and GPURenderPipeline layouts .
It determines compatibility between render passes, render bundles, and render pipelines.
A list of the GPUTextureFormat s of the color attachments for this pass or bundle.
The GPUTextureFormat of the depth/stencil attachment for this pass or bundle.
Number of samples per pixel in the attachments for this pass or bundle.
- Their depthStencilFormat and sampleCount are equal, and
Their depthStencilFormat and sampleCount are equal, and
- Their colorFormats are equal ignoring any trailing null s.
Their colorFormats are equal ignoring any trailing null s.
Arguments:
- GPURenderPassDescriptor descriptor
GPURenderPassDescriptor descriptor
Returns: GPURenderPassLayout
Device timeline steps:
- Let layout be a new GPURenderPassLayout object.
Let layout be a new GPURenderPassLayout object.
- For each colorAttachment in descriptor . colorAttachments : If colorAttachment is not null : Set layout . sampleCount to colorAttachment . view . [[texture]] . sampleCount . Append colorAttachment . view . [[descriptor]] . format to layout . colorFormats . Otherwise: Append null to layout . colorFormats .
For each colorAttachment in descriptor . colorAttachments :
- If colorAttachment is not null : Set layout . sampleCount to colorAttachment . view . [[texture]] . sampleCount . Append colorAttachment . view . [[descriptor]] . format to layout . colorFormats . Otherwise: Append null to layout . colorFormats .
If colorAttachment is not null :
- Set layout . sampleCount to colorAttachment . view . [[texture]] . sampleCount .
Set layout . sampleCount to colorAttachment . view . [[texture]] . sampleCount .
- Append colorAttachment . view . [[descriptor]] . format to layout . colorFormats .
Append colorAttachment . view . [[descriptor]] . format to layout . colorFormats .
Otherwise:
- Append null to layout . colorFormats .
Append null to layout . colorFormats .
- Let depthStencilAttachment be descriptor . depthStencilAttachment .
Let depthStencilAttachment be descriptor . depthStencilAttachment .
- If depthStencilAttachment is not null : Let view be depthStencilAttachment . view . Set layout . sampleCount to view . [[texture]] . sampleCount . Set layout . depthStencilFormat to view . [[descriptor]] . format .
If depthStencilAttachment is not null :
- Let view be depthStencilAttachment . view .
Let view be depthStencilAttachment . view .
- Set layout . sampleCount to view . [[texture]] . sampleCount .
Set layout . sampleCount to view . [[texture]] . sampleCount .
- Set layout . depthStencilFormat to view . [[descriptor]] . format .
Set layout . depthStencilFormat to view . [[descriptor]] . format .
- Return layout .
Return layout .
Arguments:
- GPURenderPipelineDescriptor descriptor
GPURenderPipelineDescriptor descriptor
Returns: GPURenderPassLayout
Device timeline steps:
- Let layout be a new GPURenderPassLayout object.
Let layout be a new GPURenderPassLayout object.
- Set layout . sampleCount to descriptor . multisample . count .
Set layout . sampleCount to descriptor . multisample . count .
- If descriptor . depthStencil is provided : Set layout . depthStencilFormat to descriptor . depthStencil . format .
If descriptor . depthStencil is provided :
- Set layout . depthStencilFormat to descriptor . depthStencil . format .
Set layout . depthStencilFormat to descriptor . depthStencil . format .
- If descriptor . fragment is provided : For each colorTarget in descriptor . fragment . targets : Append colorTarget . format to layout . colorFormats if colorTarget is not null , or append null otherwise.
If descriptor . fragment is provided :
- For each colorTarget in descriptor . fragment . targets : Append colorTarget . format to layout . colorFormats if colorTarget is not null , or append null otherwise.
For each colorTarget in descriptor . fragment . targets :
- Append colorTarget . format to layout . colorFormats if colorTarget is not null , or append null otherwise.
Append colorTarget . format to layout . colorFormats if colorTarget is not null , or append null otherwise.
- Return layout .
Return layout .
The render pass encoder can be ended by calling end() once the user
has finished recording commands for the pass. Once end() has been
called the render pass encoder can no longer be used.
Completes recording of the render pass commands sequence.
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Let parentEncoder be this . [[command_encoder]] .
Let parentEncoder be this . [[command_encoder]] .
- If any of the following requirements are unmet, generate a validation error and return. this . [[state]] must be " open ". parentEncoder . [[state]] must be " locked ".
If any of the following requirements are unmet, generate a validation error and return.
- this . [[state]] must be " open ".
this . [[state]] must be " open ".
- parentEncoder . [[state]] must be " locked ".
parentEncoder . [[state]] must be " locked ".
- Set this . [[state]] to " ended ".
Set this . [[state]] to " ended ".
- Set parentEncoder . [[state]] to " open ".
Set parentEncoder . [[state]] to " open ".
- Extend parentEncoder . [[used_bind_groups]] with this . [[used_bind_groups]] .
Extend parentEncoder . [[used_bind_groups]] with this . [[used_bind_groups]] .
- If any of the following requirements are unmet, invalidate parentEncoder and return. this must be valid . this . [[usage scope]] must satisfy usage scope validation . this . [[debug_group_stack]] must be empty . this . [[occlusion_query_active]] must be false . this . [[drawCount]] must be ≤ this . [[maxDrawCount]] .
If any of the following requirements are unmet, invalidate parentEncoder and return.
- this must be valid .
this must be valid .
- this . [[usage scope]] must satisfy usage scope validation .
this . [[usage scope]] must satisfy usage scope validation .
- this . [[debug_group_stack]] must be empty .
this . [[debug_group_stack]] must be empty .
- this . [[occlusion_query_active]] must be false .
this . [[occlusion_query_active]] must be false .
- this . [[drawCount]] must be ≤ this . [[maxDrawCount]] .
this . [[drawCount]] must be ≤ this . [[maxDrawCount]] .
- Extend parentEncoder . [[commands]] with this . [[commands]] .
Extend parentEncoder . [[commands]] with this . [[commands]] .
- If this . [[endTimestampWrite]] is not null : Extend parentEncoder . [[commands]] with this . [[endTimestampWrite]] .
If this . [[endTimestampWrite]] is not null :
- Extend parentEncoder . [[commands]] with this . [[endTimestampWrite]] .
Extend parentEncoder . [[commands]] with this . [[endTimestampWrite]] .
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- For each non- null colorAttachment in renderState . [[colorAttachments]] : Let colorView be colorAttachment . view . If colorView . [[descriptor]] . dimension is: "3d" Let colorSubregion be colorAttachment . depthSlice of colorView . Otherwise Let colorSubregion be colorView . If colorAttachment . resolveTarget is not null : Resolve the multiple samples of every texel of colorSubregion to a single
sample and copy to colorAttachment . resolveTarget . If colorAttachment . storeOp is: "store" Ensure the contents of the framebuffer memory associated with colorSubregion are stored in colorSubregion . "discard" Set every texel of colorSubregion to zero.
For each non- null colorAttachment in renderState . [[colorAttachments]] :
- Let colorView be colorAttachment . view .
Let colorView be colorAttachment . view .
- If colorView . [[descriptor]] . dimension is: "3d" Let colorSubregion be colorAttachment . depthSlice of colorView . Otherwise Let colorSubregion be colorView .
If colorView . [[descriptor]] . dimension is:
Let colorSubregion be colorAttachment . depthSlice of colorView .
Let colorSubregion be colorView .
- If colorAttachment . resolveTarget is not null : Resolve the multiple samples of every texel of colorSubregion to a single
sample and copy to colorAttachment . resolveTarget .
If colorAttachment . resolveTarget is not null :
- Resolve the multiple samples of every texel of colorSubregion to a single
sample and copy to colorAttachment . resolveTarget .
Resolve the multiple samples of every texel of colorSubregion to a single
sample and copy to colorAttachment . resolveTarget .
- If colorAttachment . storeOp is: "store" Ensure the contents of the framebuffer memory associated with colorSubregion are stored in colorSubregion . "discard" Set every texel of colorSubregion to zero.
If colorAttachment . storeOp is:
Ensure the contents of the framebuffer memory associated with colorSubregion are stored in colorSubregion .
Set every texel of colorSubregion to zero.
- Let depthStencilAttachment be renderState . [[depthStencilAttachment]] .
Let depthStencilAttachment be renderState . [[depthStencilAttachment]] .
- If depthStencilAttachment is not null : If depthStencilAttachment . depthStoreOp is: Not provided Assert that depthStencilAttachment . depthReadOnly is true and leave the depth subresource of depthStencilView unchanged. "store" Ensure the contents of the framebuffer memory associated with the depth subresource of depthStencilView are stored in depthStencilView . "discard" Set every texel in the depth subresource of depthStencilView to zero. If depthStencilAttachment . stencilStoreOp is: Not provided Assert that depthStencilAttachment . stencilReadOnly is true and leave the stencil subresource of depthStencilView unchanged. "store" Ensure the contents of the framebuffer memory associated with the stencil subresource of depthStencilView are stored in depthStencilView . "discard" Set every texel in the stencil subresource depthStencilView to zero.
If depthStencilAttachment is not null :
- If depthStencilAttachment . depthStoreOp is: Not provided Assert that depthStencilAttachment . depthReadOnly is true and leave the depth subresource of depthStencilView unchanged. "store" Ensure the contents of the framebuffer memory associated with the depth subresource of depthStencilView are stored in depthStencilView . "discard" Set every texel in the depth subresource of depthStencilView to zero.
If depthStencilAttachment . depthStoreOp is:
Assert that depthStencilAttachment . depthReadOnly is true and leave the depth subresource of depthStencilView unchanged.
Ensure the contents of the framebuffer memory associated with the depth subresource of depthStencilView are stored in depthStencilView .
Set every texel in the depth subresource of depthStencilView to zero.
- If depthStencilAttachment . stencilStoreOp is: Not provided Assert that depthStencilAttachment . stencilReadOnly is true and leave the stencil subresource of depthStencilView unchanged. "store" Ensure the contents of the framebuffer memory associated with the stencil subresource of depthStencilView are stored in depthStencilView . "discard" Set every texel in the stencil subresource depthStencilView to zero.
If depthStencilAttachment . stencilStoreOp is:
Assert that depthStencilAttachment . stencilReadOnly is true and leave the stencil subresource of depthStencilView unchanged.
Ensure the contents of the framebuffer memory associated with the stencil subresource of depthStencilView are stored in depthStencilView .
Set every texel in the stencil subresource depthStencilView to zero.
- Let renderState be null .
Let renderState be null .
Note: Discarded attachments behave as if they are cleared to zero, but implementations are not required
        to perform a clear at the end of the render pass. See the note on "discard" for
        additional details.
Note: Read-only depth-stencil attachments can be thought of as implicitly using the "store" operation, but since their content is unchanged during the render pass implementations don’t need to
        update the attachment. Validation that requires the store op to not be provided for read-only attachments
        is done in GPURenderPassDepthStencilAttachment Valid Usage .

### 17.2. GPURenderCommandsMixin

GPURenderCommandsMixin defines rendering commands common to GPURenderPassEncoder and GPURenderBundleEncoder .
GPURenderCommandsMixin assumes the presence of GPUObjectBase , GPUCommandsMixin , and GPUBindingCommandsMixin members on the same object.
It must only be included by interfaces which also include those mixins.
GPURenderCommandsMixin has the following device timeline properties :
The layout of the render pass.
If true , indicates that the depth component is not modified.
If true , indicates that the stencil component is not modified.
The usage scope for this render pass or bundle.
The current GPURenderPipeline .
The current buffer to read index data from.
The format of the index data in [[index_buffer]] .
The offset in bytes of the section of [[index_buffer]] currently set.
The size in bytes of the section of [[index_buffer]] currently set,
initially 0 .
The current GPUBuffer s to read vertex data from for each slot.
The size in bytes of the section of GPUBuffer currently set for each slot.
The number of draw commands recorded in this encoder.
- Append command to encoder . [[commands]] .
Append command to encoder . [[commands]] .
- When command is executed as part of a GPUCommandBuffer commandBuffer : Issue the steps of command with commandBuffer . [[renderState]] as renderState .
When command is executed as part of a GPUCommandBuffer commandBuffer :
- Issue the steps of command with commandBuffer . [[renderState]] as renderState .
Issue the steps of command with commandBuffer . [[renderState]] as renderState .
Sets the current GPURenderPipeline .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let pipelineTargetsLayout be derive render targets layout from pipeline ( pipeline . [[descriptor]] ).
Let pipelineTargetsLayout be derive render targets layout from pipeline ( pipeline . [[descriptor]] ).
- If any of the following conditions are unsatisfied, invalidate this and return. pipeline is valid to use with this . this . [[layout]] equals pipelineTargetsLayout . If pipeline . [[writesDepth]] : this . [[depthReadOnly]] must be false . If pipeline . [[writesStencil]] : this . [[stencilReadOnly]] must be false .
If any of the following conditions are unsatisfied, invalidate this and return.
- pipeline is valid to use with this .
pipeline is valid to use with this .
- this . [[layout]] equals pipelineTargetsLayout .
this . [[layout]] equals pipelineTargetsLayout .
- If pipeline . [[writesDepth]] : this . [[depthReadOnly]] must be false .
If pipeline . [[writesDepth]] : this . [[depthReadOnly]] must be false .
- If pipeline . [[writesStencil]] : this . [[stencilReadOnly]] must be false .
If pipeline . [[writesStencil]] : this . [[stencilReadOnly]] must be false .
- Set this . [[pipeline]] to be pipeline .
Set this . [[pipeline]] to be pipeline .
Sets the current index buffer.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If size is missing, set size to max(0, buffer . size - offset ).
If size is missing, set size to max(0, buffer . size - offset ).
- If any of the following conditions are unsatisfied, invalidate this and return. buffer is valid to use with this . buffer . usage contains INDEX . offset is a multiple of indexFormat ’s byte size. offset + size ≤ buffer . size .
If any of the following conditions are unsatisfied, invalidate this and return.
- buffer is valid to use with this .
buffer is valid to use with this .
- buffer . usage contains INDEX .
buffer . usage contains INDEX .
- offset is a multiple of indexFormat ’s byte size.
offset is a multiple of indexFormat ’s byte size.
- offset + size ≤ buffer . size .
offset + size ≤ buffer . size .
- Add buffer to [[usage scope]] with usage input .
Add buffer to [[usage scope]] with usage input .
- Set this . [[index_buffer]] to be buffer .
Set this . [[index_buffer]] to be buffer .
- Set this . [[index_format]] to be indexFormat .
Set this . [[index_format]] to be indexFormat .
- Set this . [[index_buffer_offset]] to be offset .
Set this . [[index_buffer_offset]] to be offset .
- Set this . [[index_buffer_size]] to be size .
Set this . [[index_buffer_size]] to be size .
Sets the current vertex buffer for the given slot.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let bufferSize be 0 if buffer is null , or buffer . size if not.
Let bufferSize be 0 if buffer is null , or buffer . size if not.
- If size is missing, set size to max(0, bufferSize - offset ).
If size is missing, set size to max(0, bufferSize - offset ).
- If any of the following requirements are unmet, invalidate this and return. slot must be < this . [[device]] . [[limits]] . maxVertexBuffers . offset must be a multiple of 4. offset + size must be ≤ bufferSize .
If any of the following requirements are unmet, invalidate this and return.
- slot must be < this . [[device]] . [[limits]] . maxVertexBuffers .
slot must be < this . [[device]] . [[limits]] . maxVertexBuffers .
- offset must be a multiple of 4.
offset must be a multiple of 4.
- offset + size must be ≤ bufferSize .
offset + size must be ≤ bufferSize .
- If buffer is null : Remove this . [[vertex_buffers]] [ slot ]. Remove this . [[vertex_buffer_sizes]] [ slot ]. Otherwise: If any of the following requirements are unmet, invalidate this and return. buffer must be valid to use with this . buffer . usage must contain VERTEX . Add buffer to [[usage scope]] with usage input . Set this . [[vertex_buffers]] [ slot ] to be buffer . Set this . [[vertex_buffer_sizes]] [ slot ] to be size .
If buffer is null :
- Remove this . [[vertex_buffers]] [ slot ].
Remove this . [[vertex_buffers]] [ slot ].
- Remove this . [[vertex_buffer_sizes]] [ slot ].
Remove this . [[vertex_buffer_sizes]] [ slot ].
Otherwise:
- If any of the following requirements are unmet, invalidate this and return. buffer must be valid to use with this . buffer . usage must contain VERTEX .
If any of the following requirements are unmet, invalidate this and return.
- buffer must be valid to use with this .
buffer must be valid to use with this .
- buffer . usage must contain VERTEX .
buffer . usage must contain VERTEX .
- Add buffer to [[usage scope]] with usage input .
Add buffer to [[usage scope]] with usage input .
- Set this . [[vertex_buffers]] [ slot ] to be buffer .
Set this . [[vertex_buffers]] [ slot ] to be buffer .
- Set this . [[vertex_buffer_sizes]] [ slot ] to be size .
Set this . [[vertex_buffer_sizes]] [ slot ] to be size .
Draws primitives.
See § 23.2 Rendering for the detailed specification.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- All of the requirements in the following steps must be met.
If any are unmet, invalidate this and return. It must be valid to draw with this . Let buffers be this . [[pipeline]] . [[descriptor]] . vertex . buffers . For each GPUIndex32 slot from 0 to buffers . size (non-inclusive): If buffers [ slot ] is null , continue . Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ]. Let stride be buffers [ slot ]. arrayStride . Let attributes be buffers [ slot ]. attributes Let lastStride be the maximum value of
( attribute . offset + byteSize ( attribute . format ))
over each attribute in attributes , or 0 if attributes is empty . Let strideCount be computed based on buffers [ slot ]. stepMode : "vertex" firstVertex + vertexCount "instance" firstInstance + instanceCount If strideCount ≠ 0 : ( strideCount − 1 ) × stride + lastStride must be ≤ bufferSize .
All of the requirements in the following steps must be met.
If any are unmet, invalidate this and return.
- It must be valid to draw with this .
It must be valid to draw with this .
- Let buffers be this . [[pipeline]] . [[descriptor]] . vertex . buffers .
Let buffers be this . [[pipeline]] . [[descriptor]] . vertex . buffers .
- For each GPUIndex32 slot from 0 to buffers . size (non-inclusive): If buffers [ slot ] is null , continue . Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ]. Let stride be buffers [ slot ]. arrayStride . Let attributes be buffers [ slot ]. attributes Let lastStride be the maximum value of
( attribute . offset + byteSize ( attribute . format ))
over each attribute in attributes , or 0 if attributes is empty . Let strideCount be computed based on buffers [ slot ]. stepMode : "vertex" firstVertex + vertexCount "instance" firstInstance + instanceCount If strideCount ≠ 0 : ( strideCount − 1 ) × stride + lastStride must be ≤ bufferSize .
For each GPUIndex32 slot from 0 to buffers . size (non-inclusive):
- If buffers [ slot ] is null , continue .
If buffers [ slot ] is null , continue .
- Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ].
Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ].
- Let stride be buffers [ slot ]. arrayStride .
Let stride be buffers [ slot ]. arrayStride .
- Let attributes be buffers [ slot ]. attributes
Let attributes be buffers [ slot ]. attributes
- Let lastStride be the maximum value of
( attribute . offset + byteSize ( attribute . format ))
over each attribute in attributes , or 0 if attributes is empty .
Let lastStride be the maximum value of
( attribute . offset + byteSize ( attribute . format ))
over each attribute in attributes , or 0 if attributes is empty .
- Let strideCount be computed based on buffers [ slot ]. stepMode : "vertex" firstVertex + vertexCount "instance" firstInstance + instanceCount
Let strideCount be computed based on buffers [ slot ]. stepMode :
firstVertex + vertexCount
firstInstance + instanceCount
- If strideCount ≠ 0 : ( strideCount − 1 ) × stride + lastStride must be ≤ bufferSize .
If strideCount ≠ 0 :
- ( strideCount − 1 ) × stride + lastStride must be ≤ bufferSize .
( strideCount − 1 ) × stride + lastStride must be ≤ bufferSize .
- Increment this . [[drawCount]] by 1.
Increment this . [[drawCount]] by 1.
- Let bindingState be a snapshot of this ’s current state.
Let bindingState be a snapshot of this ’s current state.
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of vertexCount vertices, starting with vertex firstVertex ,
with the states from bindingState and renderState .
Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of vertexCount vertices, starting with vertex firstVertex ,
with the states from bindingState and renderState .
Draws indexed primitives.
See § 23.2 Rendering for the detailed specification.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. It is valid to draw indexed with this . firstIndex + indexCount ≤ this . [[index_buffer_size]] ÷ this . [[index_format]] ’s byte size; Let buffers be this . [[pipeline]] . [[descriptor]] . vertex . buffers . For each GPUIndex32 slot from 0 to buffers . size (non-inclusive): If buffers [ slot ] is null , continue . Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ]. Let stride be buffers [ slot ]. arrayStride . Let lastStride be max( attribute . offset + byteSize ( attribute . format ))
for each attribute in buffers [ slot ]. attributes . Let strideCount be firstInstance + instanceCount . If buffers [ slot ]. stepMode is "instance" and strideCount ≠ 0 : Ensure ( strideCount − 1 ) × stride + lastStride ≤ bufferSize .
If any of the following conditions are unsatisfied, invalidate this and return.
- It is valid to draw indexed with this .
It is valid to draw indexed with this .
- firstIndex + indexCount ≤ this . [[index_buffer_size]] ÷ this . [[index_format]] ’s byte size;
firstIndex + indexCount ≤ this . [[index_buffer_size]] ÷ this . [[index_format]] ’s byte size;
- Let buffers be this . [[pipeline]] . [[descriptor]] . vertex . buffers .
Let buffers be this . [[pipeline]] . [[descriptor]] . vertex . buffers .
- For each GPUIndex32 slot from 0 to buffers . size (non-inclusive): If buffers [ slot ] is null , continue . Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ]. Let stride be buffers [ slot ]. arrayStride . Let lastStride be max( attribute . offset + byteSize ( attribute . format ))
for each attribute in buffers [ slot ]. attributes . Let strideCount be firstInstance + instanceCount . If buffers [ slot ]. stepMode is "instance" and strideCount ≠ 0 : Ensure ( strideCount − 1 ) × stride + lastStride ≤ bufferSize .
For each GPUIndex32 slot from 0 to buffers . size (non-inclusive):
- If buffers [ slot ] is null , continue .
If buffers [ slot ] is null , continue .
- Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ].
Let bufferSize be this . [[vertex_buffer_sizes]] [ slot ].
- Let stride be buffers [ slot ]. arrayStride .
Let stride be buffers [ slot ]. arrayStride .
- Let lastStride be max( attribute . offset + byteSize ( attribute . format ))
for each attribute in buffers [ slot ]. attributes .
Let lastStride be max( attribute . offset + byteSize ( attribute . format ))
for each attribute in buffers [ slot ]. attributes .
- Let strideCount be firstInstance + instanceCount .
Let strideCount be firstInstance + instanceCount .
- If buffers [ slot ]. stepMode is "instance" and strideCount ≠ 0 : Ensure ( strideCount − 1 ) × stride + lastStride ≤ bufferSize .
If buffers [ slot ]. stepMode is "instance" and strideCount ≠ 0 :
- Ensure ( strideCount − 1 ) × stride + lastStride ≤ bufferSize .
Ensure ( strideCount − 1 ) × stride + lastStride ≤ bufferSize .
- Increment this . [[drawCount]] by 1.
Increment this . [[drawCount]] by 1.
- Let bindingState be a snapshot of this ’s current state.
Let bindingState be a snapshot of this ’s current state.
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of indexCount indexed vertices, starting with index firstIndex from vertex baseVertex ,
with the states from bindingState and renderState .
Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of indexCount indexed vertices, starting with index firstIndex from vertex baseVertex ,
with the states from bindingState and renderState .
Note: WebGPU applications should never use index data with indices out of bounds of any
    bound vertex buffer that has GPUVertexStepMode "vertex" .
    WebGPU implementations have different ways of handling this,
    and therefore a range of behaviors is allowed.
    Either the whole draw call is discarded, or the access to those attributes
    out of bounds is described by WGSL’s invalid memory reference .
[LINK: invalid memory reference](https://gpuweb.github.io/gpuweb/wgsl/#invalid-memory-reference)
Draws primitives using parameters read from a GPUBuffer .
See § 23.2 Rendering for the detailed specification.
The indirect draw parameters encoded in the buffer must be a tightly
packed block of four 32-bit unsigned integer values (16 bytes total) , given in the same
order as the arguments for draw() . For example:
The value corresponding to firstInstance must be 0, unless the "indirect-first-instance" feature is enabled.  If the "indirect-first-instance" feature is not enabled and firstInstance is not zero the drawIndirect() call will be treated as a no-op.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. It is valid to draw with this . indirectBuffer is valid to use with this . indirectBuffer . usage contains INDIRECT . indirectOffset + sizeof( indirect draw parameters ) ≤ indirectBuffer . size . indirectOffset is a multiple of 4.
If any of the following conditions are unsatisfied, invalidate this and return.
- It is valid to draw with this .
It is valid to draw with this .
- indirectBuffer is valid to use with this .
indirectBuffer is valid to use with this .
- indirectBuffer . usage contains INDIRECT .
indirectBuffer . usage contains INDIRECT .
- indirectOffset + sizeof( indirect draw parameters ) ≤ indirectBuffer . size .
indirectOffset + sizeof( indirect draw parameters ) ≤ indirectBuffer . size .
- indirectOffset is a multiple of 4.
indirectOffset is a multiple of 4.
- Add indirectBuffer to [[usage scope]] with usage input .
Add indirectBuffer to [[usage scope]] with usage input .
- Increment this . [[drawCount]] by 1.
Increment this . [[drawCount]] by 1.
- Let bindingState be a snapshot of this ’s current state.
Let bindingState be a snapshot of this ’s current state.
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Let vertexCount be an unsigned 32-bit integer read from indirectBuffer at indirectOffset bytes.
Let vertexCount be an unsigned 32-bit integer read from indirectBuffer at indirectOffset bytes.
- Let instanceCount be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 4) bytes.
Let instanceCount be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 4) bytes.
- Let firstVertex be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 8) bytes.
Let firstVertex be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 8) bytes.
- Let firstInstance be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 12) bytes.
Let firstInstance be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 12) bytes.
- Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of vertexCount vertices, starting with vertex firstVertex ,
with the states from bindingState and renderState .
Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of vertexCount vertices, starting with vertex firstVertex ,
with the states from bindingState and renderState .
Draws indexed primitives using parameters read from a GPUBuffer .
See § 23.2 Rendering for the detailed specification.
The indirect drawIndexed parameters encoded in the buffer must be a
tightly packed block of five 32-bit values (20 bytes total) , given in the same order as
the arguments for drawIndexed() . The value corresponding to baseVertex is a signed 32-bit integer, and all others are unsigned 32-bit integers.
For example:
The value corresponding to firstInstance must be 0, unless the "indirect-first-instance" feature is enabled.  If the "indirect-first-instance" feature is not enabled and firstInstance is not zero the drawIndexedIndirect() call will be treated as a no-op.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. It is valid to draw indexed with this . indirectBuffer is valid to use with this . indirectBuffer . usage contains INDIRECT . indirectOffset + sizeof( indirect drawIndexed parameters ) ≤ indirectBuffer . size . indirectOffset is a multiple of 4.
If any of the following conditions are unsatisfied, invalidate this and return.
- It is valid to draw indexed with this .
It is valid to draw indexed with this .
- indirectBuffer is valid to use with this .
indirectBuffer is valid to use with this .
- indirectBuffer . usage contains INDIRECT .
indirectBuffer . usage contains INDIRECT .
- indirectOffset + sizeof( indirect drawIndexed parameters ) ≤ indirectBuffer . size .
indirectOffset + sizeof( indirect drawIndexed parameters ) ≤ indirectBuffer . size .
- indirectOffset is a multiple of 4.
indirectOffset is a multiple of 4.
- Add indirectBuffer to [[usage scope]] with usage input .
Add indirectBuffer to [[usage scope]] with usage input .
- Increment this . [[drawCount]] by 1.
Increment this . [[drawCount]] by 1.
- Let bindingState be a snapshot of this ’s current state.
Let bindingState be a snapshot of this ’s current state.
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Let indexCount be an unsigned 32-bit integer read from indirectBuffer at indirectOffset bytes.
Let indexCount be an unsigned 32-bit integer read from indirectBuffer at indirectOffset bytes.
- Let instanceCount be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 4) bytes.
Let instanceCount be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 4) bytes.
- Let firstIndex be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 8) bytes.
Let firstIndex be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 8) bytes.
- Let baseVertex be a signed 32-bit integer read from indirectBuffer at
( indirectOffset + 12) bytes.
Let baseVertex be a signed 32-bit integer read from indirectBuffer at
( indirectOffset + 12) bytes.
- Let firstInstance be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 16) bytes.
Let firstInstance be an unsigned 32-bit integer read from indirectBuffer at
( indirectOffset + 16) bytes.
- Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of indexCount indexed vertices, starting with index firstIndex from vertex baseVertex ,
with the states from bindingState and renderState .
Draw instanceCount instances, starting with instance firstInstance , of
primitives consisting of indexCount indexed vertices, starting with index firstIndex from vertex baseVertex ,
with the states from bindingState and renderState .
- If any of the following conditions are unsatisfied, return false : Validate encoder bind groups ( encoder , encoder . [[pipeline]] )
must be true . Let pipelineDescriptor be encoder . [[pipeline]] . [[descriptor]] . For each GPUIndex32 slot 0 to pipelineDescriptor . vertex . buffers . size : If pipelineDescriptor . vertex . buffers [ slot ] is not null , encoder . [[vertex_buffers]] must contain slot . Validate maxBindGroupsPlusVertexBuffers : Let bindGroupSpaceUsed be
(the maximum key in encoder . [[bind_groups]] ) + 1. Let vertexBufferSpaceUsed be
(the maximum key in encoder . [[vertex_buffers]] ) + 1. bindGroupSpaceUsed + vertexBufferSpaceUsed must be ≤ encoder . [[device]] . [[limits]] . maxBindGroupsPlusVertexBuffers . Otherwise, return true .
If any of the following conditions are unsatisfied, return false :
- Validate encoder bind groups ( encoder , encoder . [[pipeline]] )
must be true .
Validate encoder bind groups ( encoder , encoder . [[pipeline]] )
must be true .
- Let pipelineDescriptor be encoder . [[pipeline]] . [[descriptor]] .
Let pipelineDescriptor be encoder . [[pipeline]] . [[descriptor]] .
- For each GPUIndex32 slot 0 to pipelineDescriptor . vertex . buffers . size : If pipelineDescriptor . vertex . buffers [ slot ] is not null , encoder . [[vertex_buffers]] must contain slot .
For each GPUIndex32 slot 0 to pipelineDescriptor . vertex . buffers . size :
- If pipelineDescriptor . vertex . buffers [ slot ] is not null , encoder . [[vertex_buffers]] must contain slot .
If pipelineDescriptor . vertex . buffers [ slot ] is not null , encoder . [[vertex_buffers]] must contain slot .
- Validate maxBindGroupsPlusVertexBuffers : Let bindGroupSpaceUsed be
(the maximum key in encoder . [[bind_groups]] ) + 1. Let vertexBufferSpaceUsed be
(the maximum key in encoder . [[vertex_buffers]] ) + 1. bindGroupSpaceUsed + vertexBufferSpaceUsed must be ≤ encoder . [[device]] . [[limits]] . maxBindGroupsPlusVertexBuffers .
Validate maxBindGroupsPlusVertexBuffers :
- Let bindGroupSpaceUsed be
(the maximum key in encoder . [[bind_groups]] ) + 1.
Let bindGroupSpaceUsed be
(the maximum key in encoder . [[bind_groups]] ) + 1.
- Let vertexBufferSpaceUsed be
(the maximum key in encoder . [[vertex_buffers]] ) + 1.
Let vertexBufferSpaceUsed be
(the maximum key in encoder . [[vertex_buffers]] ) + 1.
- bindGroupSpaceUsed + vertexBufferSpaceUsed must be ≤ encoder . [[device]] . [[limits]] . maxBindGroupsPlusVertexBuffers .
bindGroupSpaceUsed + vertexBufferSpaceUsed must be ≤ encoder . [[device]] . [[limits]] . maxBindGroupsPlusVertexBuffers .
Otherwise, return true .
- If any of the following conditions are unsatisfied, return false : It must be valid to draw with encoder . encoder . [[index_buffer]] must not be null . Let topology be encoder . [[pipeline]] . [[descriptor]] . primitive . topology . If topology is "line-strip" or "triangle-strip" : encoder . [[index_format]] must equal encoder . [[pipeline]] . [[descriptor]] . primitive . stripIndexFormat . Otherwise, return true .
If any of the following conditions are unsatisfied, return false :
- It must be valid to draw with encoder .
It must be valid to draw with encoder .
- encoder . [[index_buffer]] must not be null .
encoder . [[index_buffer]] must not be null .
- Let topology be encoder . [[pipeline]] . [[descriptor]] . primitive . topology .
Let topology be encoder . [[pipeline]] . [[descriptor]] . primitive . topology .
- If topology is "line-strip" or "triangle-strip" : encoder . [[index_format]] must equal encoder . [[pipeline]] . [[descriptor]] . primitive . stripIndexFormat .
If topology is "line-strip" or "triangle-strip" :
- encoder . [[index_format]] must equal encoder . [[pipeline]] . [[descriptor]] . primitive . stripIndexFormat .
encoder . [[index_format]] must equal encoder . [[pipeline]] . [[descriptor]] . primitive . stripIndexFormat .
Otherwise, return true .
The GPURenderPassEncoder has several methods which affect how draw commands are rasterized to
attachments used by this encoder.
Sets the viewport used during the rasterization stage to linearly map from normalized device coordinates to viewport coordinates .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Let maxViewportRange be this . limits . maxTextureDimension2D × 2 .
Let maxViewportRange be this . limits . maxTextureDimension2D × 2 .
- If any of the following conditions are unsatisfied, invalidate this and return. x ≥ - maxViewportRange y ≥ - maxViewportRange 0 ≤ width ≤ this . limits . maxTextureDimension2D 0 ≤ height ≤ this . limits . maxTextureDimension2D x + width ≤ maxViewportRange − 1 y + height ≤ maxViewportRange − 1 0.0 ≤ minDepth ≤ 1.0 0.0 ≤ maxDepth ≤ 1.0 minDepth ≤ maxDepth
If any of the following conditions are unsatisfied, invalidate this and return.
- x ≥ - maxViewportRange
x ≥ - maxViewportRange
- y ≥ - maxViewportRange
y ≥ - maxViewportRange
- 0 ≤ width ≤ this . limits . maxTextureDimension2D
0 ≤ width ≤ this . limits . maxTextureDimension2D
- 0 ≤ height ≤ this . limits . maxTextureDimension2D
0 ≤ height ≤ this . limits . maxTextureDimension2D
- x + width ≤ maxViewportRange − 1
x + width ≤ maxViewportRange − 1
- y + height ≤ maxViewportRange − 1
y + height ≤ maxViewportRange − 1
- 0.0 ≤ minDepth ≤ 1.0
0.0 ≤ minDepth ≤ 1.0
- 0.0 ≤ maxDepth ≤ 1.0
0.0 ≤ maxDepth ≤ 1.0
- minDepth ≤ maxDepth
minDepth ≤ maxDepth
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Round x , y , width , and height to some uniform precision, no less precise than integer rounding.
Round x , y , width , and height to some uniform precision, no less precise than integer rounding.
- Set renderState . [[viewport]] to the extents x , y , width , height , minDepth , and maxDepth .
Set renderState . [[viewport]] to the extents x , y , width , height , minDepth , and maxDepth .
Sets the scissor rectangle used during the rasterization stage.
After transformation into viewport coordinates any fragments which fall outside the scissor
rectangle will be discarded.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. x + width ≤ this . [[attachment_size]] .width. y + height ≤ this . [[attachment_size]] .height.
If any of the following conditions are unsatisfied, invalidate this and return.
- x + width ≤ this . [[attachment_size]] .width.
x + width ≤ this . [[attachment_size]] .width.
- y + height ≤ this . [[attachment_size]] .height.
y + height ≤ this . [[attachment_size]] .height.
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Set renderState . [[scissorRect]] to the extents x , y , width , and height .
Set renderState . [[scissorRect]] to the extents x , y , width , and height .
Sets the constant blend color and alpha values used with "constant" and "one-minus-constant" GPUBlendFactor s.
Arguments:
Returns: undefined
Content timeline steps:
- ? validate GPUColor shape ( color ).
? validate GPUColor shape ( color ).
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Set renderState . [[blendConstant]] to color .
Set renderState . [[blendConstant]] to color .
Sets the [[stencilReference]] value used during stencil tests with
the "replace" GPUStencilOperation .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Set renderState . [[stencilReference]] to reference .
Set renderState . [[stencilReference]] to reference .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. this . [[occlusion_query_set]] is not null . queryIndex < this . [[occlusion_query_set]] . count . The query at same queryIndex must not have been previously written to in this pass. this . [[occlusion_query_active]] is false .
If any of the following conditions are unsatisfied, invalidate this and return.
- this . [[occlusion_query_set]] is not null .
this . [[occlusion_query_set]] is not null .
- queryIndex < this . [[occlusion_query_set]] . count .
queryIndex < this . [[occlusion_query_set]] . count .
- The query at same queryIndex must not have been previously written to in this pass.
The query at same queryIndex must not have been previously written to in this pass.
- this . [[occlusion_query_active]] is false .
this . [[occlusion_query_active]] is false .
- Set this . [[occlusion_query_active]] to true .
Set this . [[occlusion_query_active]] to true .
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Set renderState . [[occlusionQueryIndex]] to queryIndex .
Set renderState . [[occlusionQueryIndex]] to queryIndex .
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. this . [[occlusion_query_active]] is true .
If any of the following conditions are unsatisfied, invalidate this and return.
- this . [[occlusion_query_active]] is true .
this . [[occlusion_query_active]] is true .
- Set this . [[occlusion_query_active]] to false .
Set this . [[occlusion_query_active]] to false .
- Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
Enqueue a render command on this which issues the subsequent steps on the Queue timeline with renderState when executed.
- Let passingFragments be non-zero if any fragment samples passed all per-fragment
tests since the corresponding beginOcclusionQuery() command was executed, and zero otherwise. Note: If no draw calls occurred, passingFragments is zero.
Let passingFragments be non-zero if any fragment samples passed all per-fragment
tests since the corresponding beginOcclusionQuery() command was executed, and zero otherwise.
Note: If no draw calls occurred, passingFragments is zero.
- Write passingFragments into this . [[occlusion_query_set]] at index renderState . [[occlusionQueryIndex]] .
Write passingFragments into this . [[occlusion_query_set]] at index renderState . [[occlusionQueryIndex]] .
Executes the commands previously recorded into the given GPURenderBundle s as part of
this render pass.
When a GPURenderBundle is executed, it does not inherit the render pass’s pipeline, bind
groups, or vertex and index buffers. After a GPURenderBundle has executed, the render
pass’s pipeline, bind group, and vertex/index buffer state is cleared
(to the initial, empty values).
Note: The state is cleared, not restored to the previous state.
This occurs even if zero GPURenderBundles are executed.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this . [[device]] .
Issue the subsequent steps on the Device timeline of this . [[device]] .
- Validate the encoder state of this . If it returns false, return.
Validate the encoder state of this . If it returns false, return.
- If any of the following conditions are unsatisfied, invalidate this and return. For each bundle in bundles : bundle must be valid to use with this . this . [[layout]] must equal bundle . [[layout]] . If this . [[depthReadOnly]] is true, bundle . [[depthReadOnly]] must be true. If this . [[stencilReadOnly]] is true, bundle . [[stencilReadOnly]] must be true.
If any of the following conditions are unsatisfied, invalidate this and return.
- For each bundle in bundles : bundle must be valid to use with this . this . [[layout]] must equal bundle . [[layout]] . If this . [[depthReadOnly]] is true, bundle . [[depthReadOnly]] must be true. If this . [[stencilReadOnly]] is true, bundle . [[stencilReadOnly]] must be true.
For each bundle in bundles :
- bundle must be valid to use with this .
bundle must be valid to use with this .
- this . [[layout]] must equal bundle . [[layout]] .
this . [[layout]] must equal bundle . [[layout]] .
- If this . [[depthReadOnly]] is true, bundle . [[depthReadOnly]] must be true.
If this . [[depthReadOnly]] is true, bundle . [[depthReadOnly]] must be true.
- If this . [[stencilReadOnly]] is true, bundle . [[stencilReadOnly]] must be true.
If this . [[stencilReadOnly]] is true, bundle . [[stencilReadOnly]] must be true.
- For each bundle in bundles : Increment this . [[drawCount]] by bundle . [[drawCount]] . Merge bundle . [[usage scope]] into this . [[usage scope]] . Extend this . [[used_bind_groups]] with bundle . [[used_bind_groups]] Enqueue a render command on this which issues the following steps on the Queue timeline with renderState when executed: Queue timeline steps: Execute each command in bundle . [[command_list]] with renderState . Note: renderState cannot be changed by executing render bundles. Binding state was
already captured at bundle encoding time, and so isn’t used when executing bundles.
For each bundle in bundles :
- Increment this . [[drawCount]] by bundle . [[drawCount]] .
Increment this . [[drawCount]] by bundle . [[drawCount]] .
- Merge bundle . [[usage scope]] into this . [[usage scope]] .
Merge bundle . [[usage scope]] into this . [[usage scope]] .
- Extend this . [[used_bind_groups]] with bundle . [[used_bind_groups]]
Extend this . [[used_bind_groups]] with bundle . [[used_bind_groups]]
- Enqueue a render command on this which issues the following steps on the Queue timeline with renderState when executed: Queue timeline steps: Execute each command in bundle . [[command_list]] with renderState . Note: renderState cannot be changed by executing render bundles. Binding state was
already captured at bundle encoding time, and so isn’t used when executing bundles.
Enqueue a render command on this which issues the following steps on the Queue timeline with renderState when executed:
- Execute each command in bundle . [[command_list]] with renderState . Note: renderState cannot be changed by executing render bundles. Binding state was
already captured at bundle encoding time, and so isn’t used when executing bundles.
Execute each command in bundle . [[command_list]] with renderState .
Note: renderState cannot be changed by executing render bundles. Binding state was
already captured at bundle encoding time, and so isn’t used when executing bundles.
- Reset the render pass binding state of this .
Reset the render pass binding state of this .
- Clear encoder . [[bind_groups]] .
Clear encoder . [[bind_groups]] .
- Set encoder . [[pipeline]] to null .
Set encoder . [[pipeline]] to null .
- Set encoder . [[index_buffer]] to null .
Set encoder . [[index_buffer]] to null .
- Clear encoder . [[vertex_buffers]] .
Clear encoder . [[vertex_buffers]] .

## 18. Bundles

A bundle is a partial, limited pass that is encoded once and can then be executed multiple times as
part of future pass encoders without expiring after use like typical command buffers. This can
reduce the overhead of encoding and submission of commands which are issued repeatedly without
changing.

### 18.1. GPURenderBundle

A list of GPU commands to be submitted to the GPURenderPassEncoder when the GPURenderBundle is executed.
A set of all GPUBindGroup s used by this render bundle.
The usage scope for this render bundle, stored for later merging into the GPURenderPassEncoder ’s [[usage scope]] in executeBundles() .
The layout of the render bundle.
If true , indicates that the depth component is not modified by executing this render bundle.
If true , indicates that the stencil component is not modified by executing this render bundle.
The number of draw commands in this GPURenderBundle .
Creates a GPURenderBundleEncoder .
Arguments:
Returns: GPURenderBundleEncoder
Content timeline steps:
- ? Validate texture format required features of each non- null element of descriptor . colorFormats with this . [[device]] .
? Validate texture format required features of each non- null element of descriptor . colorFormats with this . [[device]] .
- If descriptor . depthStencilFormat is provided : ? Validate texture format required features of descriptor . depthStencilFormat with this . [[device]] .
If descriptor . depthStencilFormat is provided :
- ? Validate texture format required features of descriptor . depthStencilFormat with this . [[device]] .
? Validate texture format required features of descriptor . depthStencilFormat with this . [[device]] .
- Let e be ! create a new WebGPU object ( this , GPURenderBundleEncoder , descriptor ).
Let e be ! create a new WebGPU object ( this , GPURenderBundleEncoder , descriptor ).
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return e .
Return e .
- If any of the following conditions are unsatisfied generate a validation error , invalidate e and return. this must not be lost . descriptor . colorFormats . size must be ≤ this . [[limits]] . maxColorAttachments . For each non- null colorFormat in descriptor . colorFormats : colorFormat must be a color renderable format . Calculating color attachment bytes per sample ( descriptor . colorFormats )
must be ≤ this . [[limits]] . maxColorAttachmentBytesPerSample . If descriptor . depthStencilFormat is provided : descriptor . depthStencilFormat must be a depth-or-stencil format . There must exist at least one attachment, either: A non- null value in descriptor . colorFormats , or A descriptor . depthStencilFormat .
If any of the following conditions are unsatisfied generate a validation error , invalidate e and return.
- this must not be lost .
this must not be lost .
- descriptor . colorFormats . size must be ≤ this . [[limits]] . maxColorAttachments .
descriptor . colorFormats . size must be ≤ this . [[limits]] . maxColorAttachments .
- For each non- null colorFormat in descriptor . colorFormats : colorFormat must be a color renderable format .
For each non- null colorFormat in descriptor . colorFormats :
- colorFormat must be a color renderable format .
colorFormat must be a color renderable format .
- Calculating color attachment bytes per sample ( descriptor . colorFormats )
must be ≤ this . [[limits]] . maxColorAttachmentBytesPerSample .
Calculating color attachment bytes per sample ( descriptor . colorFormats )
must be ≤ this . [[limits]] . maxColorAttachmentBytesPerSample .
- If descriptor . depthStencilFormat is provided : descriptor . depthStencilFormat must be a depth-or-stencil format .
If descriptor . depthStencilFormat is provided :
- descriptor . depthStencilFormat must be a depth-or-stencil format .
descriptor . depthStencilFormat must be a depth-or-stencil format .
- There must exist at least one attachment, either: A non- null value in descriptor . colorFormats , or A descriptor . depthStencilFormat .
There must exist at least one attachment, either:
- A non- null value in descriptor . colorFormats , or
A non- null value in descriptor . colorFormats , or
- A descriptor . depthStencilFormat .
A descriptor . depthStencilFormat .
- Set e . [[layout]] to a copy of descriptor ’s included GPURenderPassLayout interface.
Set e . [[layout]] to a copy of descriptor ’s included GPURenderPassLayout interface.
- Set e . [[depthReadOnly]] to descriptor . depthReadOnly .
Set e . [[depthReadOnly]] to descriptor . depthReadOnly .
- Set e . [[stencilReadOnly]] to descriptor . stencilReadOnly .
Set e . [[stencilReadOnly]] to descriptor . stencilReadOnly .
- Set e . [[state]] to " open ".
Set e . [[state]] to " open ".
- Set e . [[drawCount]] to 0.
Set e . [[drawCount]] to 0.
If true , indicates that the render bundle does not modify the depth component of the GPURenderPassDepthStencilAttachment of any render pass the render bundle is executed
in.
See read-only depth-stencil .
If true , indicates that the render bundle does not modify the stencil component of the GPURenderPassDepthStencilAttachment of any render pass the render bundle is executed
in.
See read-only depth-stencil .
Completes recording of the render bundle commands sequence.
Arguments:
Returns: GPURenderBundle
Content timeline steps:
- Let renderBundle be a new GPURenderBundle .
Let renderBundle be a new GPURenderBundle .
- Issue the finish steps on the Device timeline of this . [[device]] .
Issue the finish steps on the Device timeline of this . [[device]] .
- Return renderBundle .
Return renderBundle .
- Let validationSucceeded be true if all of the following requirements are met, and false otherwise. this must be valid . this . [[usage scope]] must satisfy usage scope validation . this . [[state]] must be " open ". this . [[debug_group_stack]] must be empty .
Let validationSucceeded be true if all of the following requirements are met, and false otherwise.
- this must be valid .
this must be valid .
- this . [[usage scope]] must satisfy usage scope validation .
this . [[usage scope]] must satisfy usage scope validation .
- this . [[state]] must be " open ".
this . [[state]] must be " open ".
- this . [[debug_group_stack]] must be empty .
this . [[debug_group_stack]] must be empty .
- Set this . [[state]] to " ended ".
Set this . [[state]] to " ended ".
- If validationSucceeded is false , then: Generate a validation error . Return an invalidated GPURenderBundle .
If validationSucceeded is false , then:
- Generate a validation error .
Generate a validation error .
- Return an invalidated GPURenderBundle .
Return an invalidated GPURenderBundle .
- Set renderBundle . [[command_list]] to this . [[commands]] .
Set renderBundle . [[command_list]] to this . [[commands]] .
- Set renderBundle . [[used_bind_groups]] to this . [[used_bind_groups]] .
Set renderBundle . [[used_bind_groups]] to this . [[used_bind_groups]] .
- Set renderBundle . [[usage scope]] to this . [[usage scope]] .
Set renderBundle . [[usage scope]] to this . [[usage scope]] .
- Set renderBundle . [[drawCount]] to this . [[drawCount]] .
Set renderBundle . [[drawCount]] to this . [[drawCount]] .

## 19. Queues

### 19.1. GPUQueueDescriptor

GPUQueueDescriptor describes a queue request.

### 19.2. GPUQueue

GPUQueue has the following methods:
Issues a write operation of the provided data into a GPUBuffer .
Arguments:
Returns: undefined
Content timeline steps:
- If data is an ArrayBuffer or DataView , let the element type be "byte".
Otherwise, data is a TypedArray; let the element type be the type of the TypedArray.
If data is an ArrayBuffer or DataView , let the element type be "byte".
Otherwise, data is a TypedArray; let the element type be the type of the TypedArray.
- Let dataSize be the size of data , in elements.
Let dataSize be the size of data , in elements.
- If size is missing,
let contentsSize be dataSize − dataOffset .
Otherwise, let contentsSize be size .
If size is missing,
let contentsSize be dataSize − dataOffset .
Otherwise, let contentsSize be size .
- If any of the following conditions are unsatisfied,
throw an OperationError and return. contentsSize ≥ 0. dataOffset + contentsSize ≤ dataSize . contentsSize , converted to bytes, is a multiple of 4 bytes.
If any of the following conditions are unsatisfied,
throw an OperationError and return.
- contentsSize ≥ 0.
contentsSize ≥ 0.
- dataOffset + contentsSize ≤ dataSize .
dataOffset + contentsSize ≤ dataSize .
- contentsSize , converted to bytes, is a multiple of 4 bytes.
contentsSize , converted to bytes, is a multiple of 4 bytes.
- Let dataContents be a copy of the bytes held by the buffer source data .
Let dataContents be a copy of the bytes held by the buffer source data .
- Let contents be the contentsSize elements of dataContents starting at
an offset of dataOffset elements.
Let contents be the contentsSize elements of dataContents starting at
an offset of dataOffset elements.
- Issue the subsequent steps on the Device timeline of this .
Issue the subsequent steps on the Device timeline of this .
- If any of the following conditions are unsatisfied, generate a validation error and return. buffer is valid to use with this . buffer . [[internal state]] is " available ". buffer . usage includes COPY_DST . bufferOffset , converted to bytes, is a multiple of 4 bytes. bufferOffset + contentsSize , converted to bytes, ≤ buffer . size bytes.
If any of the following conditions are unsatisfied, generate a validation error and return.
- buffer is valid to use with this .
buffer is valid to use with this .
- buffer . [[internal state]] is " available ".
buffer . [[internal state]] is " available ".
- buffer . usage includes COPY_DST .
buffer . usage includes COPY_DST .
- bufferOffset , converted to bytes, is a multiple of 4 bytes.
bufferOffset , converted to bytes, is a multiple of 4 bytes.
- bufferOffset + contentsSize , converted to bytes, ≤ buffer . size bytes.
bufferOffset + contentsSize , converted to bytes, ≤ buffer . size bytes.
- Issue the subsequent steps on the Queue timeline of this .
Issue the subsequent steps on the Queue timeline of this .
- Write contents into buffer starting at bufferOffset .
Write contents into buffer starting at bufferOffset .
Issues a write operation of the provided data into a GPUTexture .
Arguments:
Returns: undefined
Content timeline steps:
- ? validate GPUOrigin3D shape ( destination . origin ).
? validate GPUOrigin3D shape ( destination . origin ).
- ? validate GPUExtent3D shape ( size ).
? validate GPUExtent3D shape ( size ).
- Let dataBytes be a copy of the bytes held by the buffer source data . Note: This is described as copying all of data to the device timeline,
but in practice data could be much larger than necessary.
Implementations should optimize by copying only the necessary bytes.
Let dataBytes be a copy of the bytes held by the buffer source data .
Note: This is described as copying all of data to the device timeline,
but in practice data could be much larger than necessary.
Implementations should optimize by copying only the necessary bytes.
- Issue the subsequent steps on the Device timeline of this .
Issue the subsequent steps on the Device timeline of this .
- Let aligned be false .
Let aligned be false .
- Let dataLength be dataBytes . length .
Let dataLength be dataBytes . length .
- If any of the following conditions are unsatisfied, generate a validation error and return. destination . texture . [[destroyed]] is false . validating texture buffer copy ( destination , dataLayout , dataLength , size , COPY_DST , aligned ) returns true . Note: unlike GPUCommandEncoder . copyBufferToTexture() ,
    there is no alignment requirement on either dataLayout . bytesPerRow or dataLayout . offset .
If any of the following conditions are unsatisfied, generate a validation error and return.
- destination . texture . [[destroyed]] is false .
destination . texture . [[destroyed]] is false .
- validating texture buffer copy ( destination , dataLayout , dataLength , size , COPY_DST , aligned ) returns true .
validating texture buffer copy ( destination , dataLayout , dataLength , size , COPY_DST , aligned ) returns true .
Note: unlike GPUCommandEncoder . copyBufferToTexture() ,
    there is no alignment requirement on either dataLayout . bytesPerRow or dataLayout . offset .
- Issue the subsequent steps on the Queue timeline of this .
Issue the subsequent steps on the Queue timeline of this .
- Let blockWidth be the texel block width of destination . texture .
Let blockWidth be the texel block width of destination . texture .
- Let blockHeight be the texel block height of destination . texture .
Let blockHeight be the texel block height of destination . texture .
- Let dstOrigin be destination . origin ;
Let dstOrigin be destination . origin ;
- Let dstBlockOriginX be ( dstOrigin . x ÷ blockWidth ).
Let dstBlockOriginX be ( dstOrigin . x ÷ blockWidth ).
- Let dstBlockOriginY be ( dstOrigin . y ÷ blockHeight ).
Let dstBlockOriginY be ( dstOrigin . y ÷ blockHeight ).
- Let blockColumns be ( copySize . width ÷ blockWidth ).
Let blockColumns be ( copySize . width ÷ blockWidth ).
- Let blockRows be ( copySize . height ÷ blockHeight ).
Let blockRows be ( copySize . height ÷ blockHeight ).
- Assert that dstBlockOriginX , dstBlockOriginY , blockColumns , and blockRows are integers.
Assert that dstBlockOriginX , dstBlockOriginY , blockColumns , and blockRows are integers.
- For each z in the range [0, copySize . depthOrArrayLayers − 1]: Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination . For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of dataLayout for ( x , y , z ) of destination . texture . Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by dataBytes at offset blockOffset .
For each z in the range [0, copySize . depthOrArrayLayers − 1]:
- Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination .
Let dstSubregion be texture copy sub-region ( z + dstOrigin . z ) of destination .
- For each y in the range [0, blockRows − 1]: For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of dataLayout for ( x , y , z ) of destination . texture . Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by dataBytes at offset blockOffset .
For each y in the range [0, blockRows − 1]:
- For each x in the range [0, blockColumns − 1]: Let blockOffset be the texel block byte offset of dataLayout for ( x , y , z ) of destination . texture . Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by dataBytes at offset blockOffset .
For each x in the range [0, blockColumns − 1]:
- Let blockOffset be the texel block byte offset of dataLayout for ( x , y , z ) of destination . texture .
Let blockOffset be the texel block byte offset of dataLayout for ( x , y , z ) of destination . texture .
- Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by dataBytes at offset blockOffset .
Set texel block ( dstBlockOriginX + x , dstBlockOriginY + y ) of dstSubregion to be an equivalent texel representation to the texel block described by dataBytes at offset blockOffset .
Issues a copy operation of the contents of a platform image/canvas
into the destination texture.
This operation performs color encoding into the destination
encoding according to the parameters of GPUCopyExternalImageDestInfo .
Copying into a -srgb texture results in the same texture bytes, not the same decoded
values, as copying into the corresponding non- -srgb format.
Thus, after a copy operation, sampling the destination texture has
different results depending on whether its format is -srgb , all else unchanged.
- Issue copyExternalImageToTexture() in the same task with
WebGL rendering operation, to ensure the copy occurs before the WebGL
canvas is presented.
Issue copyExternalImageToTexture() in the same task with
WebGL rendering operation, to ensure the copy occurs before the WebGL
canvas is presented.
[LINK: task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task)
- If not possible, set the preserveDrawingBuffer option in WebGLContextAttributes to true , so that the drawing buffer will
still contain a copy of the frame contents after they’ve been presented.
Note, this extra copy may have a performance cost.
If not possible, set the preserveDrawingBuffer option in WebGLContextAttributes to true , so that the drawing buffer will
still contain a copy of the frame contents after they’ve been presented.
Note, this extra copy may have a performance cost.
Arguments:
Returns: undefined
Content timeline steps:
- ? validate GPUOrigin2D shape ( source . origin ).
? validate GPUOrigin2D shape ( source . origin ).
- ? validate GPUOrigin3D shape ( destination . origin ).
? validate GPUOrigin3D shape ( destination . origin ).
- ? validate GPUExtent3D shape ( copySize ).
? validate GPUExtent3D shape ( copySize ).
- Let sourceImage be source . source
Let sourceImage be source . source
- If sourceImage is not origin-clean ,
throw a SecurityError and return.
If sourceImage is not origin-clean ,
throw a SecurityError and return.
- If any of the following requirements are unmet, throw an OperationError and return. source . origin . x + copySize . width must be ≤ the width of sourceImage . source . origin . y + copySize . height must be ≤ the height of sourceImage . copySize . depthOrArrayLayers must be ≤ 1.
If any of the following requirements are unmet, throw an OperationError and return.
- source . origin . x + copySize . width must be ≤ the width of sourceImage .
source . origin . x + copySize . width must be ≤ the width of sourceImage .
- source . origin . y + copySize . height must be ≤ the height of sourceImage .
source . origin . y + copySize . height must be ≤ the height of sourceImage .
- copySize . depthOrArrayLayers must be ≤ 1.
copySize . depthOrArrayLayers must be ≤ 1.
- Let usability be ? check the usability of the image argument ( source ).
Let usability be ? check the usability of the image argument ( source ).
- Issue the subsequent steps on the Device timeline of this .
Issue the subsequent steps on the Device timeline of this .
- Let texture be destination . texture .
Let texture be destination . texture .
- If any of the following requirements are unmet, generate a validation error and return. usability must be good . texture . [[destroyed]] must be false . texture must be valid to use with this . validating GPUTexelCopyTextureInfo (destination, copySize) must return true . texture . usage must include both RENDER_ATTACHMENT and COPY_DST . texture . dimension must be "2d" . texture . sampleCount must be 1. texture . format must be a plain color format supporting RENDER_ATTACHMENT and be a unorm / unorm-srgb or float / ufloat format (not snorm , uint , or sint ).
If any of the following requirements are unmet, generate a validation error and return.
- usability must be good .
usability must be good .
- texture . [[destroyed]] must be false .
texture . [[destroyed]] must be false .
- texture must be valid to use with this .
texture must be valid to use with this .
- validating GPUTexelCopyTextureInfo (destination, copySize) must return true .
validating GPUTexelCopyTextureInfo (destination, copySize) must return true .
- texture . usage must include both RENDER_ATTACHMENT and COPY_DST .
texture . usage must include both RENDER_ATTACHMENT and COPY_DST .
- texture . dimension must be "2d" .
texture . dimension must be "2d" .
- texture . sampleCount must be 1.
texture . sampleCount must be 1.
- texture . format must be a plain color format supporting RENDER_ATTACHMENT and be a unorm / unorm-srgb or float / ufloat format (not snorm , uint , or sint ).
texture . format must be a plain color format supporting RENDER_ATTACHMENT and be a unorm / unorm-srgb or float / ufloat format (not snorm , uint , or sint ).
- If copySize . depthOrArrayLayers is > 0, issue the subsequent
steps on the Queue timeline of this .
If copySize . depthOrArrayLayers is > 0, issue the subsequent
steps on the Queue timeline of this .
- Assert that the texel block width of destination . texture is 1,
the texel block height of destination . texture is 1, and that copySize . depthOrArrayLayers is 1.
Assert that the texel block width of destination . texture is 1,
the texel block height of destination . texture is 1, and that copySize . depthOrArrayLayers is 1.
- Let srcOrigin be source . origin .
Let srcOrigin be source . origin .
- Let dstOrigin be destination . origin .
Let dstOrigin be destination . origin .
- Let dstSubregion be texture copy sub-region ( dstOrigin . z ) of destination .
Let dstSubregion be texture copy sub-region ( dstOrigin . z ) of destination .
- For each y in the range [0, copySize . height − 1]: Let srcY be y if source . flipY is false and
( copySize . height − 1 − y ) otherwise. For each x in the range [0, copySize . width − 1]: Let srcColor be the color-managed color value of the pixel at
( srcOrigin . x + x , srcOrigin . y + srcY ) of source . source . Let dstColor be the numeric RGBA value resulting from applying any color encoding required by destination . colorSpace and destination . premultipliedAlpha to srcColor . If texture . format is an -srgb format: Set dstColor to the result of applying the sRGB non-linear-to-linear conversion to it. Note: This cancels out the sRGB linear-to-non-linear conversion that occurs
when writing an -srgb format in the next step, so that precision
from an sRGB-like input image is not lost and the linear color values
of the original image can be read from the texture
(as is generally the purpose of using -srgb formats). Set texel block ( dstOrigin . x + x , dstOrigin . y + y ) of dstSubregion to an equivalent texel representation of dstColor .
For each y in the range [0, copySize . height − 1]:
- Let srcY be y if source . flipY is false and
( copySize . height − 1 − y ) otherwise.
Let srcY be y if source . flipY is false and
( copySize . height − 1 − y ) otherwise.
- For each x in the range [0, copySize . width − 1]: Let srcColor be the color-managed color value of the pixel at
( srcOrigin . x + x , srcOrigin . y + srcY ) of source . source . Let dstColor be the numeric RGBA value resulting from applying any color encoding required by destination . colorSpace and destination . premultipliedAlpha to srcColor . If texture . format is an -srgb format: Set dstColor to the result of applying the sRGB non-linear-to-linear conversion to it. Note: This cancels out the sRGB linear-to-non-linear conversion that occurs
when writing an -srgb format in the next step, so that precision
from an sRGB-like input image is not lost and the linear color values
of the original image can be read from the texture
(as is generally the purpose of using -srgb formats). Set texel block ( dstOrigin . x + x , dstOrigin . y + y ) of dstSubregion to an equivalent texel representation of dstColor .
For each x in the range [0, copySize . width − 1]:
- Let srcColor be the color-managed color value of the pixel at
( srcOrigin . x + x , srcOrigin . y + srcY ) of source . source .
Let srcColor be the color-managed color value of the pixel at
( srcOrigin . x + x , srcOrigin . y + srcY ) of source . source .
- Let dstColor be the numeric RGBA value resulting from applying any color encoding required by destination . colorSpace and destination . premultipliedAlpha to srcColor .
Let dstColor be the numeric RGBA value resulting from applying any color encoding required by destination . colorSpace and destination . premultipliedAlpha to srcColor .
- If texture . format is an -srgb format: Set dstColor to the result of applying the sRGB non-linear-to-linear conversion to it. Note: This cancels out the sRGB linear-to-non-linear conversion that occurs
when writing an -srgb format in the next step, so that precision
from an sRGB-like input image is not lost and the linear color values
of the original image can be read from the texture
(as is generally the purpose of using -srgb formats).
If texture . format is an -srgb format:
- Set dstColor to the result of applying the sRGB non-linear-to-linear conversion to it.
Set dstColor to the result of applying the sRGB non-linear-to-linear conversion to it.
Note: This cancels out the sRGB linear-to-non-linear conversion that occurs
when writing an -srgb format in the next step, so that precision
from an sRGB-like input image is not lost and the linear color values
of the original image can be read from the texture
(as is generally the purpose of using -srgb formats).
- Set texel block ( dstOrigin . x + x , dstOrigin . y + y ) of dstSubregion to an equivalent texel representation of dstColor .
Set texel block ( dstOrigin . x + x , dstOrigin . y + y ) of dstSubregion to an equivalent texel representation of dstColor .
Schedules the execution of the command buffers by the GPU on this queue.
Submitted command buffers cannot be used again.
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this :
Issue the subsequent steps on the Device timeline of this :
- If any of the following requirements are unmet, generate a validation error , invalidate each GPUCommandBuffer in commandBuffers and return. Every GPUCommandBuffer in commandBuffers must be unique. For each commandBuffer in commandBuffers : commandBuffer must be valid to use with this For each bindGroup in commandBuffer . [[used_bind_groups]] : For each GPUBindingResource in bindGroup , if the resource type is: GPUBuffer b b . [[internal state]] must
be " available ". GPUTexture t t . [[destroyed]] must be false . GPUExternalTexture et et . [[expired]] must be false . GPUQuerySet qs qs . [[destroyed]] must be false . Note: For occlusion queries, the occlusionQuerySet in beginRenderPass() is not "used" unless
it is also used by beginOcclusionQuery() .
If any of the following requirements are unmet, generate a validation error , invalidate each GPUCommandBuffer in commandBuffers and return.
- Every GPUCommandBuffer in commandBuffers must be unique.
Every GPUCommandBuffer in commandBuffers must be unique.
- For each commandBuffer in commandBuffers : commandBuffer must be valid to use with this For each bindGroup in commandBuffer . [[used_bind_groups]] : For each GPUBindingResource in bindGroup , if the resource type is: GPUBuffer b b . [[internal state]] must
be " available ". GPUTexture t t . [[destroyed]] must be false . GPUExternalTexture et et . [[expired]] must be false . GPUQuerySet qs qs . [[destroyed]] must be false . Note: For occlusion queries, the occlusionQuerySet in beginRenderPass() is not "used" unless
it is also used by beginOcclusionQuery() .
For each commandBuffer in commandBuffers :
- commandBuffer must be valid to use with this
commandBuffer must be valid to use with this
- For each bindGroup in commandBuffer . [[used_bind_groups]] : For each GPUBindingResource in bindGroup , if the resource type is: GPUBuffer b b . [[internal state]] must
be " available ". GPUTexture t t . [[destroyed]] must be false . GPUExternalTexture et et . [[expired]] must be false . GPUQuerySet qs qs . [[destroyed]] must be false .
For each bindGroup in commandBuffer . [[used_bind_groups]] :
- For each GPUBindingResource in bindGroup , if the resource type is: GPUBuffer b b . [[internal state]] must
be " available ". GPUTexture t t . [[destroyed]] must be false . GPUExternalTexture et et . [[expired]] must be false . GPUQuerySet qs qs . [[destroyed]] must be false .
For each GPUBindingResource in bindGroup , if the resource type is:
b . [[internal state]] must
be " available ".
t . [[destroyed]] must be false .
et . [[expired]] must be false .
qs . [[destroyed]] must be false .
Note: For occlusion queries, the occlusionQuerySet in beginRenderPass() is not "used" unless
it is also used by beginOcclusionQuery() .
- For each commandBuffer in commandBuffers : Invalidate commandBuffer .
For each commandBuffer in commandBuffers :
- Invalidate commandBuffer .
Invalidate commandBuffer .
- Issue the subsequent steps on the Queue timeline of this :
Issue the subsequent steps on the Queue timeline of this :
- For each commandBuffer in commandBuffers : Execute each command in commandBuffer . [[command_list]] .
For each commandBuffer in commandBuffers :
- Execute each command in commandBuffer . [[command_list]] .
Execute each command in commandBuffer . [[command_list]] .
Returns a Promise that resolves once this queue finishes processing all the work submitted
up to this moment.
Resolution of this Promise implies the completion of mapAsync() calls made prior to that call,
on GPUBuffer s last used exclusively on that queue.
Returns: Promise < undefined >
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- Let promise be a new promise .
Let promise be a new promise .
- Issue the synchronization steps on the Device timeline of this .
Issue the synchronization steps on the Device timeline of this .
- Return promise .
Return promise .
- Let event occur upon the completion of all currently-enqueued operations .
Let event occur upon the completion of all currently-enqueued operations .
- Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on contentTimeline .
Listen for timeline event event on this . [[device]] , handled by
the subsequent steps on contentTimeline .
- Resolve promise .
Resolve promise .

## 20. Queries

### 20.1. GPUQuerySet

GPUQuerySet has the following immutable properties :
The type of the queries managed by this GPUQuerySet .
The number of queries managed by this GPUQuerySet .
GPUQuerySet has the following device timeline properties :
If the query set is destroyed, it can no longer be used in any operation,
and its underlying memory can be freed.
A GPUQuerySetDescriptor specifies the options to use in creating a GPUQuerySet .
The type of queries managed by GPUQuerySet .
The number of queries managed by GPUQuerySet .
Creates a GPUQuerySet .
Arguments:
Returns: GPUQuerySet
Content timeline steps:
- If descriptor . type is "timestamp" ,
but "timestamp-query" is not enabled for this : Throw a TypeError .
If descriptor . type is "timestamp" ,
but "timestamp-query" is not enabled for this :
- Throw a TypeError .
Throw a TypeError .
- Let q be ! create a new WebGPU object ( this , GPUQuerySet , descriptor ).
Let q be ! create a new WebGPU object ( this , GPUQuerySet , descriptor ).
- Set q . type to descriptor . type .
Set q . type to descriptor . type .
- Set q . count to descriptor . count .
Set q . count to descriptor . count .
- Issue the initialization steps on the Device timeline of this .
Issue the initialization steps on the Device timeline of this .
- Return q .
Return q .
- If any of the following requirements are unmet, generate a validation error , invalidate q and return. this must not be lost . descriptor . count must be ≤ 4096.
If any of the following requirements are unmet, generate a validation error , invalidate q and return.
- this must not be lost .
this must not be lost .
- descriptor . count must be ≤ 4096.
descriptor . count must be ≤ 4096.
- Create a device allocation for q where each entry in the query set is zero. If the allocation fails without side-effects, generate an out-of-memory error , invalidate q , and return.
Create a device allocation for q where each entry in the query set is zero.
If the allocation fails without side-effects, generate an out-of-memory error , invalidate q , and return.
An application that no longer requires a GPUQuerySet can choose to lose access to it before
garbage collection by calling destroy() .
GPUQuerySet has the following methods:
Destroys the GPUQuerySet .
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the device timeline .
Issue the subsequent steps on the device timeline .
- Set this . [[destroyed]] to true .
Set this . [[destroyed]] to true .

### 20.2. QueryType

### 20.3. Occlusion Query

Occlusion query is only available on render passes, to query the number of fragment samples that pass
all the per-fragment tests for a set of drawing commands, including scissor, sample mask, alpha to
coverage, stencil, and depth tests. Any non-zero result value for the query indicates that at least
one sample passed the tests and reached the output merging stage of the render pipeline, 0 indicates
that no samples passed the tests.
When beginning a render pass, GPURenderPassDescriptor . occlusionQuerySet must be set to be able to use occlusion queries during the pass. An occlusion query is begun
and ended by calling beginOcclusionQuery() and endOcclusionQuery() in pairs that cannot be nested, and resolved into a GPUBuffer as a 64-bit unsigned integer by GPUCommandEncoder . resolveQuerySet() .
[LINK: 64-bit unsigned integer](https://gpuweb.github.io/gpuweb/wgsl/#64-bit-integer)

### 20.4. Timestamp Query

Timestamp queries allow applications to write timestamps to a GPUQuerySet , using:
- GPUComputePassDescriptor . timestampWrites
GPUComputePassDescriptor . timestampWrites
- GPURenderPassDescriptor . timestampWrites
GPURenderPassDescriptor . timestampWrites
and then resolve timestamp values (in nanoseconds as a 64-bit unsigned integer ) into
a GPUBuffer , using GPUCommandEncoder . resolveQuerySet() .
[LINK: 64-bit unsigned integer](https://gpuweb.github.io/gpuweb/wgsl/#64-bit-integer)
Timestamp values are implementation-defined .
Applications must handle arbitrary timestamp results, and should not be written in such a way that unexpected
timestamps cause an application failure.
Note: The physical device may reset the timestamp counter occasionally, which can
result in unexpected values such as negative deltas from one timestamp to the next.
These instances should be rare, and these data points can safely be discarded.
Timestamp queries are implemented using high-resolution timers (see § 2.1.7.2 Device/queue-timeline timing ).
To mitigate security and privacy concerns, their precision must be reduced:
- Let fineTimestamp be the current timestamp value of the current queue timeline ,
in nanoseconds, relative to an implementation-defined point in the past.
Let fineTimestamp be the current timestamp value of the current queue timeline ,
in nanoseconds, relative to an implementation-defined point in the past.
- Return the result of calling coarsen time on fineTimestamp with crossOriginIsolatedCapability set to false .
Return the result of calling coarsen time on fineTimestamp with crossOriginIsolatedCapability set to false .
[LINK: coarsen time](https://w3c.github.io/hr-time/#dfn-coarsen-time)
Note: Cross-origin isolation never applies to the device timeline or queue timeline , so crossOriginIsolatedCapability is never set to true .
Arguments:
- GPUDevice device
GPUDevice device
- ( GPUComputePassTimestampWrites or GPURenderPassTimestampWrites ) timestampWrites
( GPUComputePassTimestampWrites or GPURenderPassTimestampWrites ) timestampWrites
Device timeline steps:
- Return true if the following requirements are met, and false if not: "timestamp-query" must be enabled for device . timestampWrites . querySet must be valid to use with device . timestampWrites . querySet . type must be "timestamp" . Of the write index members in timestampWrites ( beginningOfPassWriteIndex , endOfPassWriteIndex ): At least one must be provided . Of those which are provided : No two may be equal. Each must be < timestampWrites . querySet . count .
Return true if the following requirements are met, and false if not:
- "timestamp-query" must be enabled for device .
"timestamp-query" must be enabled for device .
- timestampWrites . querySet must be valid to use with device .
timestampWrites . querySet must be valid to use with device .
- timestampWrites . querySet . type must be "timestamp" .
timestampWrites . querySet . type must be "timestamp" .
- Of the write index members in timestampWrites ( beginningOfPassWriteIndex , endOfPassWriteIndex ): At least one must be provided . Of those which are provided : No two may be equal. Each must be < timestampWrites . querySet . count .
Of the write index members in timestampWrites ( beginningOfPassWriteIndex , endOfPassWriteIndex ):
- At least one must be provided .
At least one must be provided .
- Of those which are provided : No two may be equal. Each must be < timestampWrites . querySet . count .
Of those which are provided :
- No two may be equal.
No two may be equal.
- Each must be < timestampWrites . querySet . count .
Each must be < timestampWrites . querySet . count .

## 21. Canvas Rendering

### 21.1. HTMLCanvasElement.getContext()

A GPUCanvasContext object is created via the getContext() method of an HTMLCanvasElement instance by passing the string literal 'webgpu' as its contextType argument.
Unlike WebGL or 2D context creation, the second argument of HTMLCanvasElement.getContext() or OffscreenCanvas.getContext() ,
the context creation attribute dictionary options , is ignored.
Instead, use GPUCanvasContext.configure() ,
which allows changing the canvas configuration without replacing the canvas.
- Let context be a new GPUCanvasContext .
Let context be a new GPUCanvasContext .
- Set context . canvas to canvas .
Set context . canvas to canvas .
- Replace the drawing buffer of context .
Replace the drawing buffer of context .
- Return context .
Return context .
Note: User agents should consider issuing developer-visible warnings when
    an ignored options argument is provided when calling getContext() to get a WebGPU canvas context.

### 21.2. GPUCanvasContext

GPUCanvasContext has the following content timeline properties :
The canvas this context was created from.
The options this context is currently configured with.
null if the context has not been configured or has been unconfigured .
The currently configured texture descriptor, derived from the [[configuration]] and canvas.
null if the context has not been configured or has been unconfigured .
The drawing buffer is the working-copy image data of the canvas.
It is exposed as writable by [[currentTexture]] (returned by getCurrentTexture() ).
The drawing buffer is used to get a copy of the image contents of a context , which
occurs when the canvas is displayed or otherwise read. It may be transparent, even if [[configuration]] . alphaMode is "opaque" . The alphaMode only affects the
result of the " get a copy of the image contents of a context " algorithm.
The drawing buffer outlives the [[currentTexture]] and contains the
previously-rendered contents even after the canvas has been presented.
It is only cleared in Replace the drawing buffer .
Any time the drawing buffer is read, implementations must ensure that all previously
submitted work (e.g. queue submissions) have completed writing to it via [[currentTexture]] .
The GPUTexture to draw into for the current frame.
It exposes a writable view onto the underlying [[drawingBuffer]] . getCurrentTexture() populates this slot if null , then returns it.
In the steady-state of a visible canvas, any changes to the drawing buffer made through the
currentTexture get presented when updating the rendering of a WebGPU canvas .
At or before that point, the texture is also destroyed
and [[currentTexture]] is set to to null , signalling that
a new one is to be created by the next call to getCurrentTexture() .
Destroying the currentTexture has no effect on the drawing buffer
contents; it only terminates write-access to the drawing buffer early.
During the same frame, getCurrentTexture() continues returning the
same destroyed texture.
Expire the current texture sets the currentTexture to null .
It is called by configure() , resizing the canvas,
presentation, transferToImageBitmap() , and others.
The image most recently presented for this canvas in " updating the rendering of a WebGPU canvas ".
If the device is lost or destroyed, this image may be used as a fallback in
" get a copy of the image contents of a context " in order to prevent the canvas from going blank.
Note: This property only needs to exist in implementations which implement the fallback, which is optional.
GPUCanvasContext has the following methods:
Configures the context for this canvas.
This clears the drawing buffer to transparent black (in Replace the drawing buffer ).
See getConfiguration() for information on feature detection .
Arguments:
Returns: undefined
Content timeline steps:
- Let device be configuration . device .
Let device be configuration . device .
- ? Validate texture format required features of configuration . format with device . [[device]] .
? Validate texture format required features of configuration . format with device . [[device]] .
- ? Validate texture format required features of each element of configuration . viewFormats with device . [[device]] .
? Validate texture format required features of each element of configuration . viewFormats with device . [[device]] .
- If Supported context formats does not contain configuration . format , throw a TypeError .
If Supported context formats does not contain configuration . format , throw a TypeError .
- If configuration . usage includes the TRANSIENT_ATTACHMENT bit, throw a TypeError .
If configuration . usage includes the TRANSIENT_ATTACHMENT bit, throw a TypeError .
- Let descriptor be the GPUTextureDescriptor for the canvas and configuration ( this . canvas , configuration ).
Let descriptor be the GPUTextureDescriptor for the canvas and configuration ( this . canvas , configuration ).
- Set this . [[configuration]] to configuration . Note: This exposes only the members defined in an implementation’s definition of GPUCanvasConfiguration . See the specifications of those members for notes about feature detection .
Set this . [[configuration]] to configuration .
Note: This exposes only the members defined in an implementation’s definition of GPUCanvasConfiguration . See the specifications of those members for notes about feature detection .
- Set this . [[textureDescriptor]] to descriptor .
Set this . [[textureDescriptor]] to descriptor .
- Replace the drawing buffer of this .
Replace the drawing buffer of this .
- Issue the subsequent steps on the Device timeline of device .
Issue the subsequent steps on the Device timeline of device .
- If any of the following requirements are unmet, generate a validation error and return. validating GPUTextureDescriptor ( device , descriptor )
must return true. Note: This early validation remains valid until the next configure() call, except for
validation of the size , which changes when
the canvas is resized.
If any of the following requirements are unmet, generate a validation error and return.
- validating GPUTextureDescriptor ( device , descriptor )
must return true.
validating GPUTextureDescriptor ( device , descriptor )
must return true.
Note: This early validation remains valid until the next configure() call, except for
validation of the size , which changes when
the canvas is resized.
Removes the context configuration. Destroys any textures produced while configured.
Returns: undefined
Content timeline steps:
- Set this . [[configuration]] to null .
Set this . [[configuration]] to null .
- Set this . [[textureDescriptor]] to null .
Set this . [[textureDescriptor]] to null .
- Replace the drawing buffer of this .
Replace the drawing buffer of this .
Returns the context configuration, or null if the context is not configured.
Note: This method exists primarily for feature detection of members (and sub-members) of GPUCanvasConfiguration ; see those members for details.
For supported members, it returns the originally-supplied values.
Returns: GPUCanvasConfiguration or null
Content timeline steps:
- Let configuration be a copy of this . [[configuration]] .
Let configuration be a copy of this . [[configuration]] .
- Return configuration .
Return configuration .
Get the GPUTexture that will be composited to the document by the GPUCanvasContext next.
The expiry task (defined below) is optional to implement.
    Even if implemented, task source priority is not normatively defined, so may happen as
    early as the next task, or as late as after all other task sources are empty
    (see automatic expiry task source ).
    Expiry is only guaranteed when a visible canvas is displayed
    ( updating the rendering of a WebGPU canvas ) and in other
    callers of " Expire the current texture ".
Returns: GPUTexture
Content timeline steps:
- If this . [[configuration]] is null ,
throw an InvalidStateError and return.
If this . [[configuration]] is null ,
throw an InvalidStateError and return.
- Assert this . [[textureDescriptor]] is not null .
Assert this . [[textureDescriptor]] is not null .
- Let device be this . [[configuration]] . device .
Let device be this . [[configuration]] . device .
- If this . [[currentTexture]] is null : Replace the drawing buffer of this . Set this . [[currentTexture]] to the result of calling device . createTexture() with this . [[textureDescriptor]] ,
except with the GPUTexture ’s underlying storage pointing to this . [[drawingBuffer]] . Note: If the texture can’t be created (e.g. due to validation failure or out-of-memory),
this generates and error and returns an invalidated GPUTexture .
Some validation here is redundant with that done in configure() .
Implementations must not skip this redundant validation.
If this . [[currentTexture]] is null :
- Replace the drawing buffer of this .
Replace the drawing buffer of this .
- Set this . [[currentTexture]] to the result of calling device . createTexture() with this . [[textureDescriptor]] ,
except with the GPUTexture ’s underlying storage pointing to this . [[drawingBuffer]] . Note: If the texture can’t be created (e.g. due to validation failure or out-of-memory),
this generates and error and returns an invalidated GPUTexture .
Some validation here is redundant with that done in configure() .
Implementations must not skip this redundant validation.
Set this . [[currentTexture]] to the result of calling device . createTexture() with this . [[textureDescriptor]] ,
except with the GPUTexture ’s underlying storage pointing to this . [[drawingBuffer]] .
Note: If the texture can’t be created (e.g. due to validation failure or out-of-memory),
this generates and error and returns an invalidated GPUTexture .
Some validation here is redundant with that done in configure() .
Implementations must not skip this redundant validation.
- Optionally , queue an automatic expiry task with device device and the following steps: Expire the current texture of this . Note: If this already happened when updating the rendering of a WebGPU canvas , it has no effect.
Optionally , queue an automatic expiry task with device device and the following steps:
- Expire the current texture of this . Note: If this already happened when updating the rendering of a WebGPU canvas , it has no effect.
Expire the current texture of this .
Note: If this already happened when updating the rendering of a WebGPU canvas , it has no effect.
- Return this . [[currentTexture]] .
Return this . [[currentTexture]] .
Note: The same GPUTexture object will be returned by every
call to getCurrentTexture() until " Expire the current texture "
runs, even if that GPUTexture is destroyed, failed validation, or failed to allocate.
Arguments:
- context : the GPUCanvasContext
context : the GPUCanvasContext
Returns: image contents
Content timeline steps:
- Let snapshot be a transparent black image of the same size as context . canvas .
Let snapshot be a transparent black image of the same size as context . canvas .
- Let configuration be context . [[configuration]] .
Let configuration be context . [[configuration]] .
- If configuration is null : Return snapshot . Note: The configuration will be null if the context has not been
configured or has been unconfigured . This is identical to
the behavior when the canvas has no context.
If configuration is null :
- Return snapshot .
Return snapshot .
Note: The configuration will be null if the context has not been
configured or has been unconfigured . This is identical to
the behavior when the canvas has no context.
- Ensure that all submitted work items (e.g. queue submissions) have
completed writing to the image (via context . [[currentTexture]] ).
Ensure that all submitted work items (e.g. queue submissions) have
completed writing to the image (via context . [[currentTexture]] ).
- If configuration . device is found to be valid : Set snapshot to a copy of the context . [[drawingBuffer]] . Otherwise, if context . [[lastPresentedImage]] is not null : Optionally , set snapshot to a copy of context . [[lastPresentedImage]] . Note: This is optional because the [[lastPresentedImage]] may no longer exist,
depending on what caused device loss.
Implementations may choose to skip it even if do they still have access to that image.
If configuration . device is found to be valid :
[LINK: valid](https://w3c.github.io/i18n-glossary/#dfn-valid)
- Set snapshot to a copy of the context . [[drawingBuffer]] .
Set snapshot to a copy of the context . [[drawingBuffer]] .
Otherwise, if context . [[lastPresentedImage]] is not null :
- Optionally , set snapshot to a copy of context . [[lastPresentedImage]] . Note: This is optional because the [[lastPresentedImage]] may no longer exist,
depending on what caused device loss.
Implementations may choose to skip it even if do they still have access to that image.
Optionally , set snapshot to a copy of context . [[lastPresentedImage]] .
Note: This is optional because the [[lastPresentedImage]] may no longer exist,
depending on what caused device loss.
Implementations may choose to skip it even if do they still have access to that image.
- Let alphaMode be configuration . alphaMode .
Let alphaMode be configuration . alphaMode .
- If alphaMode is "opaque" : Clear the alpha channel of snapshot to 1.0. Note: If the [[currentTexture]] , if any, has been destroyed
(for example in " Expire the current texture "), the alpha channel is unobservable,
and implementations may clear the alpha channel in-place. Tag snapshot as being opaque. Otherwise: Tag snapshot with alphaMode .
If alphaMode is "opaque" :
- Clear the alpha channel of snapshot to 1.0. Note: If the [[currentTexture]] , if any, has been destroyed
(for example in " Expire the current texture "), the alpha channel is unobservable,
and implementations may clear the alpha channel in-place.
Clear the alpha channel of snapshot to 1.0.
Note: If the [[currentTexture]] , if any, has been destroyed
(for example in " Expire the current texture "), the alpha channel is unobservable,
and implementations may clear the alpha channel in-place.
- Tag snapshot as being opaque.
Tag snapshot as being opaque.
Otherwise:
- Tag snapshot with alphaMode .
Tag snapshot with alphaMode .
- Tag snapshot with the colorSpace and toneMapping of configuration .
Tag snapshot with the colorSpace and toneMapping of configuration .
- Return snapshot .
Return snapshot .
- Expire the current texture of context .
Expire the current texture of context .
- Let configuration be context . [[configuration]] .
Let configuration be context . [[configuration]] .
- Set context . [[drawingBuffer]] to a transparent black image of the same
size as context . canvas . If configuration is null, the drawing buffer is tagged with the color space "srgb" .
In this case, the drawing buffer will remain blank until the context is configured. If not, the drawing buffer has the specified configuration . format and is tagged with the specified configuration . colorSpace and configuration . toneMapping . Note: configuration . alphaMode is ignored until
" get a copy of the image contents of a context ". NOTE: A newly replaced drawing buffer image behaves as if it is cleared to transparent black,
    but, like after "discard" , an implementation can clear it lazily only
    if it becomes necessary. Note: This will often be a no-op, if the drawing buffer is already cleared
and has the correct configuration.
Set context . [[drawingBuffer]] to a transparent black image of the same
size as context . canvas .
- If configuration is null, the drawing buffer is tagged with the color space "srgb" .
In this case, the drawing buffer will remain blank until the context is configured.
If configuration is null, the drawing buffer is tagged with the color space "srgb" .
In this case, the drawing buffer will remain blank until the context is configured.
- If not, the drawing buffer has the specified configuration . format and is tagged with the specified configuration . colorSpace and configuration . toneMapping .
If not, the drawing buffer has the specified configuration . format and is tagged with the specified configuration . colorSpace and configuration . toneMapping .
Note: configuration . alphaMode is ignored until
" get a copy of the image contents of a context ".
Note: This will often be a no-op, if the drawing buffer is already cleared
and has the correct configuration.
- If context . [[currentTexture]] is not null : Call context . [[currentTexture]] . destroy() (without destroying context . [[drawingBuffer]] )
to terminate write access to the image. Set context . [[currentTexture]] to null .
If context . [[currentTexture]] is not null :
- Call context . [[currentTexture]] . destroy() (without destroying context . [[drawingBuffer]] )
to terminate write access to the image.
Call context . [[currentTexture]] . destroy() (without destroying context . [[drawingBuffer]] )
to terminate write access to the image.
- Set context . [[currentTexture]] to null .
Set context . [[currentTexture]] to null .

### 21.3. HTML Specification Hooks

The following algorithms "hook" into algorithms in the HTML specification, and must run at the
specified points.
- Return a copy of the image contents of context .
Return a copy of the image contents of context .
- When an HTMLCanvasElement has its rendering updated. Including when the canvas is the placeholder canvas element of an OffscreenCanvas .
When an HTMLCanvasElement has its rendering updated.
- Including when the canvas is the placeholder canvas element of an OffscreenCanvas .
Including when the canvas is the placeholder canvas element of an OffscreenCanvas .
- When transferToImageBitmap() creates an ImageBitmap from the bitmap.
(See also transferToImageBitmap from WebGPU .)
When transferToImageBitmap() creates an ImageBitmap from the bitmap.
(See also transferToImageBitmap from WebGPU .)
- When WebGPU canvas contents are read using other Web APIs, like drawImage() , texImage2D() , texSubImage2D() , toDataURL() , toBlob() , and so on.
When WebGPU canvas contents are read using other Web APIs, like drawImage() , texImage2D() , texSubImage2D() , toDataURL() , toBlob() , and so on.
If alphaMode is "opaque" ,
        this incurs a clear of the alpha channel. Implementations may skip this step when
        they are able to read or display images in a way that ignores the alpha channel.
If an application needs a canvas only for interop (not presentation), avoid "opaque" if it is not needed.
[LINK: event loop processing model](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model)
- "update the rendering or user interface of that Document "
"update the rendering or user interface of that Document "
- "update the rendering of that dedicated worker"
"update the rendering of that dedicated worker"
Note: Service and Shared workers do not have "update the rendering" steps
    because they cannot render to user-visible canvases. requestAnimationFrame() is not exposed in ServiceWorkerGlobalScope and SharedWorkerGlobalScope , and OffscreenCanvas es from transferControlToOffscreen() cannot be sent to these workers .
[LINK: ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope)
[LINK: cannot be sent to these workers](https://github.com/whatwg/html/issues/10112)
Run the following content timeline steps:
- Expire the current texture of context . Note: If this already happened in the task queued by getCurrentTexture() , it has no effect.
Expire the current texture of context .
Note: If this already happened in the task queued by getCurrentTexture() , it has no effect.
- Set context . [[lastPresentedImage]] to context . [[drawingBuffer]] . Note: This is just a reference, not a copy; the drawing buffer’s contents can’t change
in-place after the current texture has expired.
Set context . [[lastPresentedImage]] to context . [[drawingBuffer]] .
Note: This is just a reference, not a copy; the drawing buffer’s contents can’t change
in-place after the current texture has expired.
Note: This does not happen for standalone OffscreenCanvas es (created by new OffscreenCanvas() ).
When transferToImageBitmap() is called on a canvas with GPUCanvasContext context , after creating an ImageBitmap from the canvas’s bitmap,
    run the following content timeline steps:
- Replace the drawing buffer of context .
Replace the drawing buffer of context .
Note: This makes transferToImageBitmap() equivalent to "moving" (and possibly alpha-clearing) the image contents into the
    ImageBitmap, without a copy.
- The update the canvas size algorithm.
The update the canvas size algorithm.

### 21.4. GPUCanvasConfiguration

The supported context formats are the set of GPUTextureFormat s:
« "bgra8unorm" , "rgba8unorm" , "rgba16float" ». These formats must be supported when specified as a GPUCanvasConfiguration . format regardless of the given GPUCanvasConfiguration . device .
Note: Canvas configuration cannot use srgb formats like "bgra8unorm-srgb" .
Instead, use the non- srgb equivalent ( "bgra8unorm" ), specify the srgb format in the viewFormats , and use createView() to create
a view with an srgb format.
GPUCanvasConfiguration has the following members:
The GPUDevice that textures returned by getCurrentTexture() will be
compatible with.
The format that textures returned by getCurrentTexture() will have.
Must be one of the Supported context formats .
The usage that textures returned by getCurrentTexture() will have. RENDER_ATTACHMENT is the default, but is not automatically included
if the usage is explicitly set. Be sure to include RENDER_ATTACHMENT when setting a custom usage if you wish to use textures returned by getCurrentTexture() as color targets for a render pass.
The formats that views created from textures returned by getCurrentTexture() may use.
The color space that values written into textures returned by getCurrentTexture() should be displayed with.
The tone mapping determines how the content of textures returned by getCurrentTexture() are to be displayed.
This is especially important in implementations which otherwise have HDR capabilities
    (where a dynamic-range of high would be
    exposed).
If an implementation exposes this member and a high dynamic range, it should render the
    canvas as an HDR element, not clamp values to the SDR range of the HDR display.
Determines the effect that alpha values will have on the content of textures returned by getCurrentTexture() when read, displayed, or used as an image source.
- size : [ canvas .width, canvas .height, 1].
size : [ canvas .width, canvas .height, 1].
- format : configuration . format .
format : configuration . format .
- usage : configuration . usage .
usage : configuration . usage .
- viewFormats : configuration . viewFormats .
viewFormats : configuration . viewFormats .
and other members set to their defaults.
canvas .width refers to HTMLCanvasElement . width or OffscreenCanvas . width . canvas .height refers to HTMLCanvasElement . height or OffscreenCanvas . height .
During presentation, the color values in the canvas are converted to the color
space of the screen.
The toneMapping determines the handling of values
outside of the [0, 1] interval in the color space of the screen.
All canvas configuration is set in configure() except for the resolution
of the canvas, which is set by the canvas’s width and height .
Note: Like WebGL and 2d canvas, resizing a WebGPU canvas loses the current contents of the drawing buffer.
In WebGPU, it does so by replacing the drawing buffer .
- Replace the drawing buffer of context .
Replace the drawing buffer of context .
- Let configuration be context . [[configuration]]
Let configuration be context . [[configuration]]
- If configuration is not null : Set context . [[textureDescriptor]] to the GPUTextureDescriptor for the canvas and configuration ( canvas , configuration ).
If configuration is not null :
- Set context . [[textureDescriptor]] to the GPUTextureDescriptor for the canvas and configuration ( canvas , configuration ).
Set context . [[textureDescriptor]] to the GPUTextureDescriptor for the canvas and configuration ( canvas , configuration ).
Note: This may result in a GPUTextureDescriptor which exceeds the maxTextureDimension2D of the device. In this case,
    validation will fail inside getCurrentTexture() .
Note: This algorithm is run any time the canvas width or height attributes are set, even
    if their value is not changed.

### 21.5. GPUCanvasToneMappingMode

This enum specifies how color values are displayed to the screen.
Color values within the standard dynamic range of the screen are unchanged, and
all other color values are projected to the standard dynamic range of the screen.
Note: This projection is often accomplished by clamping color values in the color space
of the screen to the [0, 1] interval.
If this is presented to an sRGB screen, then this will be converted to sRGB
    (which is a no-op, because the canvas is sRGB), then projected into the display’s space.
    Using component-wise clamping, this results in the sRGB value (1.0, 0.0, 0.0) .
If this is presented to a Display P3 screen, then this will be converted to
    the value (0.948, 0.106, 0.01) in the Display P3 color space, and no
    clamping will be needed.
Color values in the extended dynamic range of the screen are unchanged, and all
other color values are projected to the extended dynamic range of the screen.
Note: This projection is often accomplished by clamping color values in the color space of
the screen to the interval of values that the screen is capable of displaying,
which may include values greater than 1 .
If this is presented to an sRGB screen that is capable of displaying values
    in the [0, 4] interval in sRGB space, then this will be converted to sRGB
    (which is a no-op, because the canvas is sRGB), then projected into the display’s space.
    If using component-wise clamping, this results in the sRGB value (2.5, 0.0, 0.0) .
If this is presented to a Display P3 screen that is capable of displaying
    values in the [0, 2] interval in Display P3 space, then this will be
    converted to the value (2.3, 0.545, 0.386) in the Display P3 color space,
    then projected into the display’s space.
    If using component-wise clamping, this results in the Display P3 value (2.0, 0.545, 0.386) .

### 21.6. GPUCanvasAlphaMode

This enum selects how the contents of the canvas will be interpreted when read, when displayed to the screen or used as an image source (in drawImage, toDataURL, etc.)
Below, src is a value in the canvas texture, and dst is an image that the canvas
is being composited into (e.g. an HTML page rendering, or a 2D canvas).
Read RGB as opaque and ignore alpha values.
If the content is not already opaque, the alpha channel is cleared to 1.0
in " get a copy of the image contents of a context ".
Read RGBA as premultiplied: color values are premultiplied by their alpha value.
100% red at 50% alpha is [0.5, 0, 0, 0.5] .
If the canvas texture contains out-of-gamut premultiplied RGBA values at the time the
canvas contents are read, the behavior depends on whether the canvas is:
Values are preserved, as described in color space conversion .
Compositing results are undefined.
Note: This is true even if color space conversion would produce in-gamut values before
compositing, because the intermediate format for compositing is not specified.

## 22. Errors & Debugging

During the normal course of operation of WebGPU, errors are raised via dispatch error .
After a device is lost , errors are no longer surfaced, where possible.
After this point, implementations do not need to run validation or error tracking:
- The validity of objects on the device becomes unobservable.
The validity of objects on the device becomes unobservable.
- popErrorScope() and uncapturederror stop reporting errors.
(No errors are generated by the device loss itself.
Instead, the GPUDevice . lost promise resolves to indicate the device is lost.)
popErrorScope() and uncapturederror stop reporting errors.
(No errors are generated by the device loss itself.
Instead, the GPUDevice . lost promise resolves to indicate the device is lost.)
- All operations which send a message back to the content timeline will skip their usual steps.
Most will appear to succeed, except for mapAsync() , which produces an error
because it is impossible to provide the correct mapped data after the device has been lost. This makes it unobservable whether other types of operations (that don’t send messages back)
actually execute or not.
All operations which send a message back to the content timeline will skip their usual steps.
Most will appear to succeed, except for mapAsync() , which produces an error
because it is impossible to provide the correct mapped data after the device has been lost.
This makes it unobservable whether other types of operations (that don’t send messages back)
actually execute or not.

### 22.1. Fatal Errors

GPUDevice has the following additional attributes:
A slot-backed attribute holding a promise which is created with the device, remains
pending for the lifetime of the device, then resolves when the device is lost.
Upon initialization, it is set to a new promise .

### 22.2. GPUError

GPUError is the base interface for all errors surfaced from popErrorScope() and the uncapturederror event.
Errors must only be generated for operations that explicitly state the conditions one may
be generated under in their respective algorithms, and the subtype of error that is generated.
No errors are generated from a device which is lost.
See § 22 Errors & Debugging .
Note: GPUError may gain new subtypes in future versions of this spec. Applications should handle
this possibility, using only the error’s message when possible, and specializing using instanceof . Use error.constructor.name when it’s necessary to serialize an error (e.g. into
JSON, for a debug report).
GPUError has the following immutable properties :
A human-readable, localizable text message providing information about the error that
occurred.
Note: This message is generally intended for application developers to debug their
applications and capture information for debug reports, not to be surfaced to end-users.
Note: User agents should not include potentially machine-parsable details in this message,
such as free system memory on "out-of-memory" or other details about the
conditions under which memory was exhausted.
Note: The message should follow the best practices for language and direction information . This includes making use of any future standards which may emerge
regarding the reporting of string language and direction metadata.
[LINK: best practices for language and direction information](https://w3c.github.io/string-meta/#bp_and-reco)
Editorial note: At the time of this writing, no language/direction recommendation is available that provides
compatibility and consistency with legacy APIs, but when there is, adopt it formally.
GPUValidationError is a subtype of GPUError which indicates that an operation did not
satisfy all validation requirements. Validation errors are always indicative of an application
error, and is expected to fail the same way across all devices assuming the same [[features]] and [[limits]] are in use.
Device timeline steps:
- Let error be a new GPUValidationError with an appropriate error message.
Let error be a new GPUValidationError with an appropriate error message.
- Dispatch error error to device .
Dispatch error error to device .
GPUOutOfMemoryError is a subtype of GPUError which indicates that there was not enough free
memory to complete the requested operation. The operation may succeed if attempted again with a
lower memory requirement (like using smaller texture dimensions), or if memory used by other
resources is released first.
Device timeline steps:
- Let error be a new GPUOutOfMemoryError with an appropriate error message.
Let error be a new GPUOutOfMemoryError with an appropriate error message.
- Dispatch error error to device .
Dispatch error error to device .
GPUInternalError is a subtype of GPUError which indicates than an operation failed for a
system or implementation-specific reason even when all validation requirements have been satisfied.
For example, the operation may exceed the capabilities of the implementation in a way not easily
captured by the supported limits . The same operation may succeed on other devices or under
difference circumstances.
Device timeline steps:
- Let error be a new GPUInternalError with an appropriate error message.
Let error be a new GPUInternalError with an appropriate error message.
- Dispatch error error to device .
Dispatch error error to device .

### 22.3. Error Scopes

A GPU error scope captures GPUError s that were generated while the GPU error scope was current. Error scopes are used to isolate errors that occur within a set
of WebGPU calls, typically for debugging purposes or to make an operation more fault tolerant.
GPU error scope has the following device timeline properties :
The GPUError s, if any, observed while the GPU error scope was current.
Determines what type of GPUError this GPU error scope observes.
GPUErrorFilter defines the type of errors that should be caught when calling pushErrorScope() :
Indicates that the error scope will catch a GPUValidationError .
Indicates that the error scope will catch a GPUOutOfMemoryError .
Indicates that the error scope will catch a GPUInternalError .
GPUDevice has the following device timeline properties :
A stack of GPU error scopes that have been pushed to the GPUDevice .
Device timeline steps:
- If error is an instance of: GPUValidationError Let type be "validation". GPUOutOfMemoryError Let type be "out-of-memory". GPUInternalError Let type be "internal".
If error is an instance of:
Let type be "validation".
Let type be "out-of-memory".
Let type be "internal".
- Let scope be the last item of device . [[errorScopeStack]] .
Let scope be the last item of device . [[errorScopeStack]] .
- While scope is not undefined : If scope . [[filter]] is type , return scope . Set scope to the previous item of device . [[errorScopeStack]] .
While scope is not undefined :
- If scope . [[filter]] is type , return scope .
If scope . [[filter]] is type , return scope .
- Set scope to the previous item of device . [[errorScopeStack]] .
Set scope to the previous item of device . [[errorScopeStack]] .
- Return undefined .
Return undefined .
Note: No errors are generated from a device which is lost.
        If this algorithm is called while device is lost , it will not be observable to the application.
        See § 22 Errors & Debugging .
- Let scope be the current error scope for error and device .
Let scope be the current error scope for error and device .
- If scope is not undefined : Append error to scope . [[errors]] . Return. Otherwise, issue the following steps to the content timeline :
If scope is not undefined :
- Append error to scope . [[errors]] .
Append error to scope . [[errors]] .
- Return.
Return.
Otherwise, issue the following steps to the content timeline :
- If the user agent chooses, queue a global task for GPUDevice device with the following steps: Fire a GPUUncapturedErrorEvent named " uncapturederror " on device , with an error of error .
If the user agent chooses, queue a global task for GPUDevice device with the following steps:
- Fire a GPUUncapturedErrorEvent named " uncapturederror " on device , with an error of error .
Fire a GPUUncapturedErrorEvent named " uncapturederror " on device , with an error of error .
Note: After dispatching the event, user agents should surface uncaptured errors to
        developers, for example as warnings in the browser’s developer console, unless the event’s defaultPrevented is true. In other words, calling preventDefault() on the event should silence the console warning.
Note: The user agent may choose to throttle or limit the number of GPUUncapturedErrorEvent s
    that a GPUDevice can raise to prevent an excessive amount of error handling or logging from
    impacting performance.
Pushes a new GPU error scope onto the [[errorScopeStack]] for this .
Arguments:
Returns: undefined
Content timeline steps:
- Issue the subsequent steps on the Device timeline of this .
Issue the subsequent steps on the Device timeline of this .
- Let scope be a new GPU error scope .
Let scope be a new GPU error scope .
- Set scope . [[filter]] to filter .
Set scope . [[filter]] to filter .
- Push scope onto this . [[errorScopeStack]] .
Push scope onto this . [[errorScopeStack]] .
Pops a GPU error scope off the [[errorScopeStack]] for this and resolves to any GPUError observed by the error scope, or null if none.
There is no guarantee of the ordering of promise resolution.
Returns: Promise < GPUError ?>
Content timeline steps:
- Let contentTimeline be the current Content timeline .
Let contentTimeline be the current Content timeline .
- Let promise be a new promise .
Let promise be a new promise .
- Issue the check steps on the Device timeline of this .
Issue the check steps on the Device timeline of this .
- Return promise .
Return promise .
- If this is lost : Issue the following steps on contentTimeline : Content timeline steps: Resolve promise with null . Return. Note: No errors are generated from a device which is lost.
See § 22 Errors & Debugging .
If this is lost :
- Issue the following steps on contentTimeline : Content timeline steps: Resolve promise with null .
Issue the following steps on contentTimeline :
- Resolve promise with null .
Resolve promise with null .
- Return.
Return.
Note: No errors are generated from a device which is lost.
See § 22 Errors & Debugging .
- If any of the following requirements are unmet: this . [[errorScopeStack]] . size must be > 0. Then issue the following steps on contentTimeline and return: Content timeline steps: Reject promise with an OperationError .
If any of the following requirements are unmet:
- this . [[errorScopeStack]] . size must be > 0.
this . [[errorScopeStack]] . size must be > 0.
Then issue the following steps on contentTimeline and return:
- Reject promise with an OperationError .
Reject promise with an OperationError .
- Let scope be the result of popping an item off of this . [[errorScopeStack]] .
Let scope be the result of popping an item off of this . [[errorScopeStack]] .
- Let error be any one of the items in scope . [[errors]] ,
or null if there are none. For any two errors E1 and E2 in the list, if E2 was caused by E1, E2 should
not be the one selected. Note: For example, if E1 comes from t = createTexture() , and
E2 comes from t . createView() because t was invalid ,
E1 should be be preferred since it will be easier for a developer to understand
what went wrong.
Since both of these are GPUValidationError s, the only difference will be in
the message field, which is meant only to be read by humans anyway.
Let error be any one of the items in scope . [[errors]] ,
or null if there are none.
For any two errors E1 and E2 in the list, if E2 was caused by E1, E2 should
not be the one selected.
Note: For example, if E1 comes from t = createTexture() , and
E2 comes from t . createView() because t was invalid ,
E1 should be be preferred since it will be easier for a developer to understand
what went wrong.
Since both of these are GPUValidationError s, the only difference will be in
the message field, which is meant only to be read by humans anyway.
- At an unspecified point now or in the future ,
issue the subsequent steps on contentTimeline . Note: By allowing popErrorScope() calls to resolve in any order, with
any of the errors observed by the scope, this spec allows validation to complete
out of order, as long as any state observations are made at the appropriate
point in adherence to this spec. For example, this allows implementations to
perform shader compilation, which depends only on non-stateful inputs, to be
completed on a background thread in parallel with other device-timeline work,
and report any resulting errors later.
At an unspecified point now or in the future ,
issue the subsequent steps on contentTimeline .
Note: By allowing popErrorScope() calls to resolve in any order, with
any of the errors observed by the scope, this spec allows validation to complete
out of order, as long as any state observations are made at the appropriate
point in adherence to this spec. For example, this allows implementations to
perform shader compilation, which depends only on non-stateful inputs, to be
completed on a background thread in parallel with other device-timeline work,
and report any resulting errors later.
- Resolve promise with error .
Resolve promise with error .
For example: An error scope that only contains the creation of a single resource, such as a texture
or buffer, can be used to detect failures such as out of memory conditions, in which case the
application may try freeing some resources and trying the allocation again.
Error scopes do not identify which command failed, however. So, for instance, wrapping all the
commands executed while loading a model in a single error scope will not offer enough granularity to
determine if the issue was due to memory constraints. As a result freeing resources would usually
not be a productive response to a failure of that scope. A more appropriate response would be to
allow the application to fall back to a different model or produce a warning that the model could
not be loaded. If responding to memory constraints is desired, the operations allocating memory can
always be wrapped in a smaller nested error scope.

### 22.4. Telemetry

When a GPUError is generated that is not observed by any GPU error scope , the user agent may fire an event named uncapturederror at a GPUDevice using GPUUncapturedErrorEvent .
Note: uncapturederror events are intended to be used for telemetry and reporting
unexpected errors. They won’t necessarily be dispatched for all uncaptured errors (for example, there may be a limit on the number of errors surfaced), so they should not be used for handling known error cases that may occur during
normal operation of an application. Prefer using pushErrorScope() and popErrorScope() in those cases.
GPUUncapturedErrorEvent has the following attributes:
A slot-backed attribute holding an object representing the error that was uncaptured.
This has the same type as errors returned by popErrorScope() .
[LINK: EventHandler](https://html.spec.whatwg.org/multipage/webappapis.html#eventhandler)
GPUDevice has the following content timeline properties :
[LINK: EventHandler](https://html.spec.whatwg.org/multipage/webappapis.html#eventhandler)
An event handler IDL attribute for the uncapturederror event type.
[LINK: event handler IDL attribute](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes)

## 23. Detailed Operations

This section describes the details of various GPU operations.

### 23.1. Computing

Computing operations provide direct access to GPU’s programmable hardware.
Compute shaders do not have shader stage inputs or outputs; their results are
side effects from writing data into storage bindings bound either as GPUBufferBindingLayout with GPUBufferBindingType "storage" or as GPUStorageTextureBindingLayout .
These operations are encoded within GPUComputePassEncoder as:
- dispatchWorkgroups()
dispatchWorkgroups()
- dispatchWorkgroupsIndirect()
dispatchWorkgroupsIndirect()
The main compute algorithm:
Arguments:
- descriptor : Description of the current GPUComputePipeline .
descriptor : Description of the current GPUComputePipeline .
- dispatchCall : The dispatch call parameters. May come from function arguments or an INDIRECT buffer.
dispatchCall : The dispatch call parameters. May come from function arguments or an INDIRECT buffer.
- Let computeInvocations be an empty list .
Let computeInvocations be an empty list .
- Let computeStage be descriptor . compute .
Let computeStage be descriptor . compute .
- Let workgroupSize be the computed workgroup size for computeStage . entryPoint after
applying computeStage . constants to computeStage . module .
Let workgroupSize be the computed workgroup size for computeStage . entryPoint after
applying computeStage . constants to computeStage . module .
- For workgroupX in range [0, dispatchCall . workgroupCountX ] : For workgroupY in range [0, dispatchCall . workgroupCountY ] : For workgroupZ in range [0, dispatchCall . workgroupCountZ ] : For localX in range [0, workgroupSize . x ] : For localY in range [0, workgroupSize . y ] : For localZ in range [0, workgroupSize . y ] : Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ } Append invocation to computeInvocations .
For workgroupX in range [0, dispatchCall . workgroupCountX ] :
- For workgroupY in range [0, dispatchCall . workgroupCountY ] : For workgroupZ in range [0, dispatchCall . workgroupCountZ ] : For localX in range [0, workgroupSize . x ] : For localY in range [0, workgroupSize . y ] : For localZ in range [0, workgroupSize . y ] : Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ } Append invocation to computeInvocations .
For workgroupY in range [0, dispatchCall . workgroupCountY ] :
- For workgroupZ in range [0, dispatchCall . workgroupCountZ ] : For localX in range [0, workgroupSize . x ] : For localY in range [0, workgroupSize . y ] : For localZ in range [0, workgroupSize . y ] : Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ } Append invocation to computeInvocations .
For workgroupZ in range [0, dispatchCall . workgroupCountZ ] :
- For localX in range [0, workgroupSize . x ] : For localY in range [0, workgroupSize . y ] : For localZ in range [0, workgroupSize . y ] : Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ } Append invocation to computeInvocations .
For localX in range [0, workgroupSize . x ] :
- For localY in range [0, workgroupSize . y ] : For localZ in range [0, workgroupSize . y ] : Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ } Append invocation to computeInvocations .
For localY in range [0, workgroupSize . y ] :
- For localZ in range [0, workgroupSize . y ] : Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ } Append invocation to computeInvocations .
For localZ in range [0, workgroupSize . y ] :
- Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ }
Let invocation be { computeStage , workgroupX , workgroupY , workgroupZ , localX , localY , localZ }
- Append invocation to computeInvocations .
Append invocation to computeInvocations .
- For every invocation in computeInvocations , in any order the device chooses, including in parallel: Set the shader builtins : Set the num_workgroups builtin, if any, to ( dispatchCall . workgroupCountX , dispatchCall . workgroupCountY , dispatchCall . workgroupCountZ ) Set the workgroup_id builtin, if any, to ( invocation . workgroupX , invocation . workgroupY , invocation . workgroupZ ) Set the local_invocation_id builtin, if any, to ( invocation . localX , invocation . localY , invocation . localZ ) Set the global_invocation_id builtin, if any, to ( invocation . workgroupX * workgroupSize . x + invocation . localX , invocation . workgroupY * workgroupSize . y + invocation . localY , invocation . workgroupZ * workgroupSize . z + invocation . localZ ) . Set the local_invocation_index builtin, if any, to invocation . localX + ( invocation . localY * workgroupSize . x ) +
( invocation . localZ * workgroupSize . x * workgroupSize . y ) Invoke the compute shader entry point described by invocation . computeStage .
For every invocation in computeInvocations , in any order the device chooses, including in parallel:
- Set the shader builtins : Set the num_workgroups builtin, if any, to ( dispatchCall . workgroupCountX , dispatchCall . workgroupCountY , dispatchCall . workgroupCountZ ) Set the workgroup_id builtin, if any, to ( invocation . workgroupX , invocation . workgroupY , invocation . workgroupZ ) Set the local_invocation_id builtin, if any, to ( invocation . localX , invocation . localY , invocation . localZ ) Set the global_invocation_id builtin, if any, to ( invocation . workgroupX * workgroupSize . x + invocation . localX , invocation . workgroupY * workgroupSize . y + invocation . localY , invocation . workgroupZ * workgroupSize . z + invocation . localZ ) . Set the local_invocation_index builtin, if any, to invocation . localX + ( invocation . localY * workgroupSize . x ) +
( invocation . localZ * workgroupSize . x * workgroupSize . y )
Set the shader builtins :
[LINK: builtins](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- Set the num_workgroups builtin, if any, to ( dispatchCall . workgroupCountX , dispatchCall . workgroupCountY , dispatchCall . workgroupCountZ )
Set the num_workgroups builtin, if any, to ( dispatchCall . workgroupCountX , dispatchCall . workgroupCountY , dispatchCall . workgroupCountZ )
[LINK: num_workgroups](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-num_workgroups)
- Set the workgroup_id builtin, if any, to ( invocation . workgroupX , invocation . workgroupY , invocation . workgroupZ )
Set the workgroup_id builtin, if any, to ( invocation . workgroupX , invocation . workgroupY , invocation . workgroupZ )
[LINK: workgroup_id](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-workgroup_id)
- Set the local_invocation_id builtin, if any, to ( invocation . localX , invocation . localY , invocation . localZ )
Set the local_invocation_id builtin, if any, to ( invocation . localX , invocation . localY , invocation . localZ )
[LINK: local_invocation_id](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-local_invocation_id)
- Set the global_invocation_id builtin, if any, to ( invocation . workgroupX * workgroupSize . x + invocation . localX , invocation . workgroupY * workgroupSize . y + invocation . localY , invocation . workgroupZ * workgroupSize . z + invocation . localZ ) .
Set the global_invocation_id builtin, if any, to ( invocation . workgroupX * workgroupSize . x + invocation . localX , invocation . workgroupY * workgroupSize . y + invocation . localY , invocation . workgroupZ * workgroupSize . z + invocation . localZ ) .
[LINK: global_invocation_id](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-global_invocation_id)
- Set the local_invocation_index builtin, if any, to invocation . localX + ( invocation . localY * workgroupSize . x ) +
( invocation . localZ * workgroupSize . x * workgroupSize . y )
Set the local_invocation_index builtin, if any, to invocation . localX + ( invocation . localY * workgroupSize . x ) +
( invocation . localZ * workgroupSize . x * workgroupSize . y )
[LINK: local_invocation_index](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-local_invocation_index)
- Invoke the compute shader entry point described by invocation . computeStage .
Invoke the compute shader entry point described by invocation . computeStage .
Note: Shader invocations have no guaranteed order, and will generally run in parallel according to device
    capabilities. Developers should not assume that any given invocation or workgroup will complete before any
    other one is started. Some devices may appear to execute in a consistent order, but this behavior should not
    be relied on as it will not perform identically across all devices. Shaders that require synchronization
    across invocations must use Synchronization Built-in Functions to coordinate execution.
[LINK: Synchronization Built-in Functions](https://gpuweb.github.io/gpuweb/wgsl/#sync-builtin-functions)
The device may become lost if shader execution does not end in a reasonable amount of time, as determined by the user agent.
[LINK: shader execution does not end](https://gpuweb.github.io/gpuweb/wgsl/#shader-execution-end)

### 23.2. Rendering

Rendering is done by a set of GPU operations that are executed within GPURenderPassEncoder ,
and result in modifications of the texture data, viewed by the render pass attachments.
These operations are encoded with:
- draw()
draw()
- drawIndexed() ,
drawIndexed() ,
- drawIndirect()
drawIndirect()
- drawIndexedIndirect() .
drawIndexedIndirect() .
Note: rendering is the traditional use of GPUs, and is supported by multiple fixed-function
blocks in hardware.
The main rendering algorithm:
Arguments:
- pipeline : The current GPURenderPipeline .
pipeline : The current GPURenderPipeline .
- drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
- state : RenderState of the GPURenderCommandsMixin where the draw call is issued.
state : RenderState of the GPURenderCommandsMixin where the draw call is issued.
- Let descriptor be pipeline . [[descriptor]] .
Let descriptor be pipeline . [[descriptor]] .
- Resolve indices . See § 23.2.1 Index Resolution . Let vertexList be the result of resolve indices ( drawCall , state ).
Resolve indices . See § 23.2.1 Index Resolution .
Let vertexList be the result of resolve indices ( drawCall , state ).
- Process vertices . See § 23.2.2 Vertex Processing . Execute process vertices ( vertexList , drawCall , descriptor . vertex , state ).
Process vertices . See § 23.2.2 Vertex Processing .
Execute process vertices ( vertexList , drawCall , descriptor . vertex , state ).
- Assemble primitives . See § 23.2.3 Primitive Assembly . Execute assemble primitives ( vertexList , drawCall , descriptor . primitive ).
Assemble primitives . See § 23.2.3 Primitive Assembly .
Execute assemble primitives ( vertexList , drawCall , descriptor . primitive ).
- Clip primitives . See § 23.2.4 Primitive Clipping . Let primitiveList be the result of this stage.
Clip primitives . See § 23.2.4 Primitive Clipping .
Let primitiveList be the result of this stage.
- Rasterize . See § 23.2.5 Rasterization . Let rasterizationList be the result of rasterize ( primitiveList , state ).
Rasterize . See § 23.2.5 Rasterization .
Let rasterizationList be the result of rasterize ( primitiveList , state ).
- Process fragments . See § 23.2.6 Fragment Processing . Gather a list of fragments , resulting from executing process fragment ( rasterPoint , descriptor , state )
for each rasterPoint in rasterizationList .
Process fragments . See § 23.2.6 Fragment Processing .
Gather a list of fragments , resulting from executing process fragment ( rasterPoint , descriptor , state )
for each rasterPoint in rasterizationList .
- Write pixels . See § 23.2.7 Output Merging . For each non-null fragment of fragments : Execute process depth stencil ( fragment , pipeline , state ). Execute process color attachments ( fragment , pipeline , state ).
Write pixels . See § 23.2.7 Output Merging .
For each non-null fragment of fragments :
- Execute process depth stencil ( fragment , pipeline , state ).
Execute process depth stencil ( fragment , pipeline , state ).
- Execute process color attachments ( fragment , pipeline , state ).
Execute process color attachments ( fragment , pipeline , state ).
At the first stage of rendering, the pipeline builds
a list of vertices to process for each instance.
Arguments:
- drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
- state : The snapshot of the GPURenderCommandsMixin state at the time of the draw call.
state : The snapshot of the GPURenderCommandsMixin state at the time of the draw call.
Returns: list of integer indices.
- Let vertexIndexList be an empty list of indices.
Let vertexIndexList be an empty list of indices.
- If drawCall is an indexed draw call: Initialize the vertexIndexList with drawCall .indexCount integers. For i in range 0 .. drawCall .indexCount (non-inclusive): Let relativeVertexIndex be fetch index ( i + drawCall . firstIndex , state . [[index_buffer]] ). If relativeVertexIndex has the special value "out of bounds" ,
return the empty list. Note: Implementations may choose to display a warning when this occurs,
especially when it is easy to detect (like in non-indirect indexed draw calls). Append drawCall . baseVertex + relativeVertexIndex to the vertexIndexList . Otherwise: Initialize the vertexIndexList with drawCall .vertexCount integers. Set each vertexIndexList item i to the value drawCall .firstVertex + i .
If drawCall is an indexed draw call:
- Initialize the vertexIndexList with drawCall .indexCount integers.
Initialize the vertexIndexList with drawCall .indexCount integers.
- For i in range 0 .. drawCall .indexCount (non-inclusive): Let relativeVertexIndex be fetch index ( i + drawCall . firstIndex , state . [[index_buffer]] ). If relativeVertexIndex has the special value "out of bounds" ,
return the empty list. Note: Implementations may choose to display a warning when this occurs,
especially when it is easy to detect (like in non-indirect indexed draw calls). Append drawCall . baseVertex + relativeVertexIndex to the vertexIndexList .
For i in range 0 .. drawCall .indexCount (non-inclusive):
- Let relativeVertexIndex be fetch index ( i + drawCall . firstIndex , state . [[index_buffer]] ).
Let relativeVertexIndex be fetch index ( i + drawCall . firstIndex , state . [[index_buffer]] ).
- If relativeVertexIndex has the special value "out of bounds" ,
return the empty list. Note: Implementations may choose to display a warning when this occurs,
especially when it is easy to detect (like in non-indirect indexed draw calls).
If relativeVertexIndex has the special value "out of bounds" ,
return the empty list.
Note: Implementations may choose to display a warning when this occurs,
especially when it is easy to detect (like in non-indirect indexed draw calls).
- Append drawCall . baseVertex + relativeVertexIndex to the vertexIndexList .
Append drawCall . baseVertex + relativeVertexIndex to the vertexIndexList .
Otherwise:
- Initialize the vertexIndexList with drawCall .vertexCount integers.
Initialize the vertexIndexList with drawCall .vertexCount integers.
- Set each vertexIndexList item i to the value drawCall .firstVertex + i .
Set each vertexIndexList item i to the value drawCall .firstVertex + i .
- Return vertexIndexList .
Return vertexIndexList .
Note: in the case of indirect draw calls, the indexCount , vertexCount ,
    and other properties of drawCall are read from the indirect buffer
    instead of the draw command itself.
Arguments:
- i : Index of a vertex index to fetch.
i : Index of a vertex index to fetch.
- state : The snapshot of the GPURenderCommandsMixin state at the time of the draw call.
state : The snapshot of the GPURenderCommandsMixin state at the time of the draw call.
Returns: unsigned integer or "out of bounds"
- Let indexSize be defined by the state . [[index_format]] : "uint16" 2 "uint32" 4
Let indexSize be defined by the state . [[index_format]] :
- If state . [[index_buffer_offset]] +
|i + 1| × indexSize > state . [[index_buffer_size]] ,
return the special value "out of bounds" .
If state . [[index_buffer_offset]] +
|i + 1| × indexSize > state . [[index_buffer_size]] ,
return the special value "out of bounds" .
- Interpret the data in state . [[index_buffer]] , starting at offset state . [[index_buffer_offset]] + i × indexSize ,
of size indexSize bytes, as an unsigned integer and return it.
Interpret the data in state . [[index_buffer]] , starting at offset state . [[index_buffer_offset]] + i × indexSize ,
of size indexSize bytes, as an unsigned integer and return it.
Vertex processing stage is a programmable stage of the render pipeline that
processes the vertex attribute data, and produces
clip space positions for § 23.2.4 Primitive Clipping , as well as other data for the § 23.2.6 Fragment Processing .
Arguments:
- vertexIndexList : List of vertex indices to process (mutable, passed by reference).
vertexIndexList : List of vertex indices to process (mutable, passed by reference).
- drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
- desc : The descriptor of type GPUVertexState .
desc : The descriptor of type GPUVertexState .
- state : The snapshot of the GPURenderCommandsMixin state at the time of the draw call.
state : The snapshot of the GPURenderCommandsMixin state at the time of the draw call.
Each vertex vertexIndex in the vertexIndexList ,
    in each instance of index rawInstanceIndex , is processed independently.
    The rawInstanceIndex is in range from 0 to drawCall .instanceCount - 1, inclusive.
    This processing happens in parallel, and any side effects, such as
    writes into GPUBufferBindingType "storage" bindings,
    may happen in any order.
- Let instanceIndex be rawInstanceIndex + drawCall .firstInstance.
Let instanceIndex be rawInstanceIndex + drawCall .firstInstance.
- For each non- null vertexBufferLayout in the list of desc . buffers : Let i be the index of the buffer layout in this list. Let vertexBuffer , vertexBufferOffset , and vertexBufferBindingSize be the
buffer, offset, and size at slot i of state . [[vertex_buffers]] . Let vertexElementIndex be dependent on vertexBufferLayout . stepMode : "vertex" vertexIndex "instance" instanceIndex Let drawCallOutOfBounds be false . For each attributeDesc in vertexBufferLayout . attributes : Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset . If attributeOffset + byteSize ( attributeDesc . format ) > vertexBufferOffset + vertexBufferBindingSize : Set drawCallOutOfBounds to true . Optionally ( implementation-defined ) , empty vertexIndexList and return, cancelling the draw call. Note: This allows implementations to detect out-of-bounds values in the index buffer
before issuing a draw call, instead of using invalid memory reference behavior. For each attributeDesc in vertexBufferLayout . attributes : If drawCallOutOfBounds is true : Load the attribute data according to WGSL’s invalid memory reference behavior, from vertexBuffer . Note: Invalid memory reference allows several behaviors, including actually
loading the "correct" result for an attribute that is in-bounds, even when
the draw-call-wide drawCallOutOfBounds is true . Otherwise: Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset . Load the attribute data of format attributeDesc . format from vertexBuffer starting at offset attributeOffset .
The components are loaded in the order x , y , z , w from buffer memory. Convert the data into a shader-visible format, according to channel formats rules. An attribute of type "snorm8x2" and byte values of [0x70, 0xD0] will be converted to vec2<f32>(0.88, -0.38) in WGSL. Adjust the data size to the shader type: if both are scalar, or both are vectors of the same dimensionality, no adjustment is needed. if data is vector but the shader type is scalar, then only the first component is extracted. if both are vectors, and data has a higher dimension, the extra components are dropped. An attribute of type "float32x3" and value vec3<f32>(1.0, 2.0, 3.0) will exposed to the shader as vec2<f32>(1.0, 2.0) if a 2-component vector is expected. if the shader type is a vector of higher dimensionality, or the data is a scalar,
then the missing components are filled from vec4<*>(0, 0, 0, 1) value. An attribute of type "sint32" and value 5 will be exposed
    to the shader as vec4<i32>(5, 0, 0, 1) if a 4-component vector is expected. Bind the data to vertex shader input
location attributeDesc . shaderLocation .
For each non- null vertexBufferLayout in the list of desc . buffers :
- Let i be the index of the buffer layout in this list.
Let i be the index of the buffer layout in this list.
- Let vertexBuffer , vertexBufferOffset , and vertexBufferBindingSize be the
buffer, offset, and size at slot i of state . [[vertex_buffers]] .
Let vertexBuffer , vertexBufferOffset , and vertexBufferBindingSize be the
buffer, offset, and size at slot i of state . [[vertex_buffers]] .
- Let vertexElementIndex be dependent on vertexBufferLayout . stepMode : "vertex" vertexIndex "instance" instanceIndex
Let vertexElementIndex be dependent on vertexBufferLayout . stepMode :
vertexIndex
instanceIndex
- Let drawCallOutOfBounds be false .
Let drawCallOutOfBounds be false .
- For each attributeDesc in vertexBufferLayout . attributes : Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset . If attributeOffset + byteSize ( attributeDesc . format ) > vertexBufferOffset + vertexBufferBindingSize : Set drawCallOutOfBounds to true . Optionally ( implementation-defined ) , empty vertexIndexList and return, cancelling the draw call. Note: This allows implementations to detect out-of-bounds values in the index buffer
before issuing a draw call, instead of using invalid memory reference behavior.
For each attributeDesc in vertexBufferLayout . attributes :
- Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset .
Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset .
- If attributeOffset + byteSize ( attributeDesc . format ) > vertexBufferOffset + vertexBufferBindingSize : Set drawCallOutOfBounds to true . Optionally ( implementation-defined ) , empty vertexIndexList and return, cancelling the draw call. Note: This allows implementations to detect out-of-bounds values in the index buffer
before issuing a draw call, instead of using invalid memory reference behavior.
If attributeOffset + byteSize ( attributeDesc . format ) > vertexBufferOffset + vertexBufferBindingSize :
- Set drawCallOutOfBounds to true .
Set drawCallOutOfBounds to true .
- Optionally ( implementation-defined ) , empty vertexIndexList and return, cancelling the draw call. Note: This allows implementations to detect out-of-bounds values in the index buffer
before issuing a draw call, instead of using invalid memory reference behavior.
Optionally ( implementation-defined ) , empty vertexIndexList and return, cancelling the draw call.
Note: This allows implementations to detect out-of-bounds values in the index buffer
before issuing a draw call, instead of using invalid memory reference behavior.
[LINK: invalid memory reference](https://gpuweb.github.io/gpuweb/wgsl/#invalid-memory-reference)
- For each attributeDesc in vertexBufferLayout . attributes : If drawCallOutOfBounds is true : Load the attribute data according to WGSL’s invalid memory reference behavior, from vertexBuffer . Note: Invalid memory reference allows several behaviors, including actually
loading the "correct" result for an attribute that is in-bounds, even when
the draw-call-wide drawCallOutOfBounds is true . Otherwise: Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset . Load the attribute data of format attributeDesc . format from vertexBuffer starting at offset attributeOffset .
The components are loaded in the order x , y , z , w from buffer memory. Convert the data into a shader-visible format, according to channel formats rules. An attribute of type "snorm8x2" and byte values of [0x70, 0xD0] will be converted to vec2<f32>(0.88, -0.38) in WGSL. Adjust the data size to the shader type: if both are scalar, or both are vectors of the same dimensionality, no adjustment is needed. if data is vector but the shader type is scalar, then only the first component is extracted. if both are vectors, and data has a higher dimension, the extra components are dropped. An attribute of type "float32x3" and value vec3<f32>(1.0, 2.0, 3.0) will exposed to the shader as vec2<f32>(1.0, 2.0) if a 2-component vector is expected. if the shader type is a vector of higher dimensionality, or the data is a scalar,
then the missing components are filled from vec4<*>(0, 0, 0, 1) value. An attribute of type "sint32" and value 5 will be exposed
    to the shader as vec4<i32>(5, 0, 0, 1) if a 4-component vector is expected. Bind the data to vertex shader input
location attributeDesc . shaderLocation .
For each attributeDesc in vertexBufferLayout . attributes :
- If drawCallOutOfBounds is true : Load the attribute data according to WGSL’s invalid memory reference behavior, from vertexBuffer . Note: Invalid memory reference allows several behaviors, including actually
loading the "correct" result for an attribute that is in-bounds, even when
the draw-call-wide drawCallOutOfBounds is true . Otherwise: Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset . Load the attribute data of format attributeDesc . format from vertexBuffer starting at offset attributeOffset .
The components are loaded in the order x , y , z , w from buffer memory.
If drawCallOutOfBounds is true :
- Load the attribute data according to WGSL’s invalid memory reference behavior, from vertexBuffer . Note: Invalid memory reference allows several behaviors, including actually
loading the "correct" result for an attribute that is in-bounds, even when
the draw-call-wide drawCallOutOfBounds is true .
Load the attribute data according to WGSL’s invalid memory reference behavior, from vertexBuffer .
[LINK: invalid memory reference](https://gpuweb.github.io/gpuweb/wgsl/#invalid-memory-reference)
Note: Invalid memory reference allows several behaviors, including actually
loading the "correct" result for an attribute that is in-bounds, even when
the draw-call-wide drawCallOutOfBounds is true .
[LINK: Invalid memory reference](https://gpuweb.github.io/gpuweb/wgsl/#invalid-memory-reference)
Otherwise:
- Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset .
Let attributeOffset be vertexBufferOffset + vertexElementIndex * vertexBufferLayout . arrayStride + attributeDesc . offset .
- Load the attribute data of format attributeDesc . format from vertexBuffer starting at offset attributeOffset .
The components are loaded in the order x , y , z , w from buffer memory.
Load the attribute data of format attributeDesc . format from vertexBuffer starting at offset attributeOffset .
The components are loaded in the order x , y , z , w from buffer memory.
- Convert the data into a shader-visible format, according to channel formats rules. An attribute of type "snorm8x2" and byte values of [0x70, 0xD0] will be converted to vec2<f32>(0.88, -0.38) in WGSL.
Convert the data into a shader-visible format, according to channel formats rules.
[LINK: channel formats](https://gpuweb.github.io/gpuweb/wgsl/#channel-formats)
- Adjust the data size to the shader type: if both are scalar, or both are vectors of the same dimensionality, no adjustment is needed. if data is vector but the shader type is scalar, then only the first component is extracted. if both are vectors, and data has a higher dimension, the extra components are dropped. An attribute of type "float32x3" and value vec3<f32>(1.0, 2.0, 3.0) will exposed to the shader as vec2<f32>(1.0, 2.0) if a 2-component vector is expected. if the shader type is a vector of higher dimensionality, or the data is a scalar,
then the missing components are filled from vec4<*>(0, 0, 0, 1) value. An attribute of type "sint32" and value 5 will be exposed
    to the shader as vec4<i32>(5, 0, 0, 1) if a 4-component vector is expected.
Adjust the data size to the shader type:
- if both are scalar, or both are vectors of the same dimensionality, no adjustment is needed.
if both are scalar, or both are vectors of the same dimensionality, no adjustment is needed.
- if data is vector but the shader type is scalar, then only the first component is extracted.
if data is vector but the shader type is scalar, then only the first component is extracted.
- if both are vectors, and data has a higher dimension, the extra components are dropped. An attribute of type "float32x3" and value vec3<f32>(1.0, 2.0, 3.0) will exposed to the shader as vec2<f32>(1.0, 2.0) if a 2-component vector is expected.
if both are vectors, and data has a higher dimension, the extra components are dropped.
- if the shader type is a vector of higher dimensionality, or the data is a scalar,
then the missing components are filled from vec4<*>(0, 0, 0, 1) value. An attribute of type "sint32" and value 5 will be exposed
    to the shader as vec4<i32>(5, 0, 0, 1) if a 4-component vector is expected.
if the shader type is a vector of higher dimensionality, or the data is a scalar,
then the missing components are filled from vec4<*>(0, 0, 0, 1) value.
- Bind the data to vertex shader input
location attributeDesc . shaderLocation .
Bind the data to vertex shader input
location attributeDesc . shaderLocation .
- For each GPUBindGroup group at index in state . [[bind_groups]] : For each resource GPUBindingResource in the bind group: Let entry be the corresponding GPUBindGroupLayoutEntry for this resource. If entry . visibility includes VERTEX : Bind the resource to the shader under group index and binding GPUBindGroupLayoutEntry.binding .
For each GPUBindGroup group at index in state . [[bind_groups]] :
- For each resource GPUBindingResource in the bind group: Let entry be the corresponding GPUBindGroupLayoutEntry for this resource. If entry . visibility includes VERTEX : Bind the resource to the shader under group index and binding GPUBindGroupLayoutEntry.binding .
For each resource GPUBindingResource in the bind group:
- Let entry be the corresponding GPUBindGroupLayoutEntry for this resource.
Let entry be the corresponding GPUBindGroupLayoutEntry for this resource.
- If entry . visibility includes VERTEX : Bind the resource to the shader under group index and binding GPUBindGroupLayoutEntry.binding .
If entry . visibility includes VERTEX :
- Bind the resource to the shader under group index and binding GPUBindGroupLayoutEntry.binding .
Bind the resource to the shader under group index and binding GPUBindGroupLayoutEntry.binding .
- Set the shader builtins : Set the vertex_index builtin, if any, to vertexIndex . Set the instance_index builtin, if any, to instanceIndex .
Set the shader builtins :
[LINK: builtins](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- Set the vertex_index builtin, if any, to vertexIndex .
Set the vertex_index builtin, if any, to vertexIndex .
- Set the instance_index builtin, if any, to instanceIndex .
Set the instance_index builtin, if any, to instanceIndex .
- Invoke the vertex shader entry point described by desc . Note: The target platform caches the results of vertex shader invocations.
There is no guarantee that any vertexIndex that repeats more than once will
result in multiple invocations. Similarly, there is no guarantee that a single vertexIndex will only be processed once. The device may become lost if shader execution does not end in a reasonable amount of time, as determined by the user agent.
Invoke the vertex shader entry point described by desc .
Note: The target platform caches the results of vertex shader invocations.
There is no guarantee that any vertexIndex that repeats more than once will
result in multiple invocations. Similarly, there is no guarantee that a single vertexIndex will only be processed once.
The device may become lost if shader execution does not end in a reasonable amount of time, as determined by the user agent.
[LINK: shader execution does not end](https://gpuweb.github.io/gpuweb/wgsl/#shader-execution-end)
Primitives are assembled by a fixed-function stage of GPUs.
Arguments:
- vertexIndexList : List of vertex indices to process.
vertexIndexList : List of vertex indices to process.
- drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
drawCall : The draw call parameters. May come from function arguments or an INDIRECT buffer.
- desc : The descriptor of type GPUPrimitiveState .
desc : The descriptor of type GPUPrimitiveState .
For each instance, the primitives get assembled from the vertices that have been
    processed by the shaders, based on the vertexIndexList .
- First, if the primitive topology is a strip, (which means that desc . stripIndexFormat is not undefined)
and the drawCall is indexed, the vertexIndexList is split into
sub-lists using the maximum value of desc . stripIndexFormat as a separator. Example: a vertexIndexList with values [1, 2, 65535, 4, 5, 6] of type "uint16" will be split in sub-lists [1, 2] and [4, 5, 6] .
First, if the primitive topology is a strip, (which means that desc . stripIndexFormat is not undefined)
and the drawCall is indexed, the vertexIndexList is split into
sub-lists using the maximum value of desc . stripIndexFormat as a separator.
Example: a vertexIndexList with values [1, 2, 65535, 4, 5, 6] of type "uint16" will be split in sub-lists [1, 2] and [4, 5, 6] .
- For each of the sub-lists vl , primitive generation is done according to the desc . topology : "line-list" Line primitives are composed from ( vl .0, vl .1),
then ( vl .2, vl .3), then ( vl .4 to vl .5), etc.
Each subsequent primitive takes 2 vertices. "line-strip" Line primitives are composed from ( vl .0, vl .1),
then ( vl .1, vl .2), then ( vl .2, vl .3), etc.
Each subsequent primitive takes 1 vertex. "triangle-list" Triangle primitives are composed from ( vl .0, vl .1, vl .2),
then ( vl .3, vl .4, vl .5), then ( vl .6, vl .7, vl .8), etc.
Each subsequent primitive takes 3 vertices. "triangle-strip" Triangle primitives are composed from ( vl .0, vl .1, vl .2),
then ( vl .2, vl .1, vl .3), then ( vl .2, vl .3, vl .4),
then ( vl .4, vl .3, vl .5), etc.
Each subsequent primitive takes 1 vertices. Any incomplete primitives are dropped.
For each of the sub-lists vl , primitive generation is done according to the desc . topology :
Line primitives are composed from ( vl .0, vl .1),
then ( vl .2, vl .3), then ( vl .4 to vl .5), etc.
Each subsequent primitive takes 2 vertices.
Line primitives are composed from ( vl .0, vl .1),
then ( vl .1, vl .2), then ( vl .2, vl .3), etc.
Each subsequent primitive takes 1 vertex.
Triangle primitives are composed from ( vl .0, vl .1, vl .2),
then ( vl .3, vl .4, vl .5), then ( vl .6, vl .7, vl .8), etc.
Each subsequent primitive takes 3 vertices.
Triangle primitives are composed from ( vl .0, vl .1, vl .2),
then ( vl .2, vl .1, vl .3), then ( vl .2, vl .3, vl .4),
then ( vl .4, vl .3, vl .5), etc.
Each subsequent primitive takes 1 vertices.
Any incomplete primitives are dropped.
Vertex shaders have to produce a built-in position (of type vec4<f32> ),
which denotes the clip position of a vertex in clip space coordinates .
[LINK: position](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-position)
Primitives are clipped to the clip volume , which, for any clip position p inside a primitive, is defined by the following inequalities:
- − p .w ≤ p .x ≤ p .w
− p .w ≤ p .x ≤ p .w
- − p .w ≤ p .y ≤ p .w
− p .w ≤ p .y ≤ p .w
- 0 ≤ p .z ≤ p .w ( depth clipping )
0 ≤ p .z ≤ p .w ( depth clipping )
When the "clip-distances" feature is enabled, this clip volume can
be further restricted by user-defined half-spaces by declaring clip_distances in the
output of vertex stage. Each value in the clip_distances array will be linearly
interpolated across the primitive, and the portion of the primitive with interpolated distances less
than 0 will be clipped.
[LINK: clip_distances](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-clip_distances)
[LINK: clip_distances](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-clip_distances)
If descriptor . primitive . unclippedDepth is true , depth clipping is not applied: the clip volume is not bounded in the z dimension.
A primitive passes through this stage unchanged if every one of its edges
lie entirely inside the clip volume .
If the edges of a primitives intersect the boundary of the clip volume ,
the intersecting edges are reconnected by new edges that lie along the boundary of the clip volume .
For triangular primitives ( descriptor . primitive . topology is "triangle-list" or "triangle-strip" ), this reconnection
may result in introduction of new vertices into the polygon, internally.
If a primitive intersects an edge of the clip volume ’s boundary,
the clipped polygon must include a point on this boundary edge.
If the vertex shader outputs other floating-point values (scalars and vectors), qualified with
"perspective" interpolation, they also get clipped.
The output values associated with a vertex that lies within the clip volume are unaffected by clipping.
If a primitive is clipped, however, the output values assigned to vertices produced by clipping are clipped.
Considering an edge between vertices a and b that got clipped, resulting in the vertex c ,
let’s define t to be the ratio between the edge vertices: c .p = t × a .p + (1 − t ) × b .p,
where x .p is the output clip position of a vertex x .
For each vertex output value "v" with a corresponding fragment input, a .v and b .v would be the outputs for a and b vertices respectively.
The clipped shader output c .v is produced based on the interpolation qualifier:
[LINK: flat](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-type-flat)
Flat interpolation is unaffected, and is based on the provoking vertex ,
which is determined by the interpolation sampling mode declared in the shader. The
output value is the same for the whole primitive, and matches the vertex output of the provoking vertex .
[LINK: interpolation sampling](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-sampling)
[LINK: linear](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-type-linear)
The interpolation ratio gets adjusted against the perspective coordinates of the clip position s, so that the result of interpolation is linear in screen space.
[LINK: perspective](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-type-perspective)
The value is linearly interpolated in clip space, producing perspective-correct values.
The result of primitive clipping is a new set of primitives, which are contained
within the clip volume .
Rasterization is the hardware processing stage that maps the generated primitives
to the 2-dimensional rendering area of the framebuffer -
the set of render attachments in the current GPURenderPassEncoder .
This rendering area is split into an even grid of pixels.
The framebuffer coordinates start from the top-left corner of the render targets.
Each unit corresponds exactly to one pixel. See § 3.3 Coordinate Systems for more information.
Rasterization determines the set of pixels affected by a primitive. In case of multi-sampling,
each pixel is further split into descriptor . multisample . count samples.
The standard sample patterns are as follows,
with positions in framebuffer coordinates relative to the top-left corner of the pixel,
such that the pixel ranges from (0, 0) to (1, 1):
Implementations must use the standard sample pattern for the given multisample . count when performing rasterization.
Let’s define a FragmentDestination to contain:
the 2D pixel position using framebuffer coordinates
an integer in case § 23.2.10 Per-Sample Shading is active,
or null otherwise
We’ll also use a notion of normalized device coordinates , or NDC.
In this coordinate system, the viewport bounds range in X and Y from -1 to 1, and in Z from 0 to 1.
Rasterization produces a list of RasterizationPoint s, each containing the following data:
refers to FragmentDestination
refers to multisample coverage mask (see § 23.2.11 Sample Masking )
is true if it’s a point on the front face of a primitive
refers to interpolated 1.0 ÷ W across the primitive
refers to the depth in viewport coordinates ,
i.e. between the [[viewport]] minDepth and maxDepth .
refers to the list of vertex outputs forming the primitive
refers to § 23.2.5.3 Barycentric coordinates
Arguments:
- primitiveList : List of primitives to rasterize.
primitiveList : List of primitives to rasterize.
- state : The active RenderState .
state : The active RenderState .
Returns: list of RasterizationPoint .
Each primitive in primitiveList is processed independently.
    However, the order of primitives affects later stages, such as depth/stencil operations and pixel writes.
- First, the clipped vertices are transformed into NDC - normalized device coordinates.
Given the output position p , the NDC position and perspective divisor are: ndc( p ) = vector( p .x ÷ p .w, p .y ÷ p .w, p .z ÷ p .w) divisor( p ) = 1.0 ÷ p .w
First, the clipped vertices are transformed into NDC - normalized device coordinates.
Given the output position p , the NDC position and perspective divisor are:
ndc( p ) = vector( p .x ÷ p .w, p .y ÷ p .w, p .z ÷ p .w)
divisor( p ) = 1.0 ÷ p .w
- Let vp be state . [[viewport]] .
Map the NDC position n into viewport coordinates : Compute framebuffer coordinates from the render target offset and size: framebufferCoords( n ) = vector( vp . x + 0.5 × ( n .x + 1) × vp . width , vp . y + 0.5 × (− n .y + 1) × vp . height ) Compute depth by linearly mapping [0,1] to the viewport depth range: depth( n ) = vp . minDepth + n . z × ( vp . maxDepth - vp . minDepth )
Let vp be state . [[viewport]] .
Map the NDC position n into viewport coordinates :
- Compute framebuffer coordinates from the render target offset and size: framebufferCoords( n ) = vector( vp . x + 0.5 × ( n .x + 1) × vp . width , vp . y + 0.5 × (− n .y + 1) × vp . height )
Compute framebuffer coordinates from the render target offset and size:
framebufferCoords( n ) = vector( vp . x + 0.5 × ( n .x + 1) × vp . width , vp . y + 0.5 × (− n .y + 1) × vp . height )
- Compute depth by linearly mapping [0,1] to the viewport depth range: depth( n ) = vp . minDepth + n . z × ( vp . maxDepth - vp . minDepth )
Compute depth by linearly mapping [0,1] to the viewport depth range:
depth( n ) = vp . minDepth + n . z × ( vp . maxDepth - vp . minDepth )
- Let rasterizationPoints be the list of points, each having its attributes ( divisor(p) , framebufferCoords(n) , depth(n) , etc.) interpolated according to its position on the
primitive, using the same interpolation as § 23.2.4 Primitive Clipping . If the attribute is
user-defined (not a built-in output value ) then the interpolation type specified by
the @interpolate WGSL attribute is used.
Let rasterizationPoints be the list of points, each having its attributes ( divisor(p) , framebufferCoords(n) , depth(n) , etc.) interpolated according to its position on the
primitive, using the same interpolation as § 23.2.4 Primitive Clipping . If the attribute is
user-defined (not a built-in output value ) then the interpolation type specified by
the @interpolate WGSL attribute is used.
[LINK: built-in output value](https://gpuweb.github.io/gpuweb/wgsl/#built-in-output-value)
[LINK: interpolation type](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-type)
[LINK: @interpolate](https://gpuweb.github.io/gpuweb/wgsl/#interpolate-attr)
- Proceed with a specific rasterization algorithm,
depending on primitive . topology : "point-list" The point, if not filtered by § 23.2.4 Primitive Clipping , goes into § 23.2.5.1 Point Rasterization . "line-list" or "line-strip" The line cut by § 23.2.4 Primitive Clipping goes into § 23.2.5.2 Line Rasterization . "triangle-list" or "triangle-strip" The polygon produced in § 23.2.4 Primitive Clipping goes into § 23.2.5.4 Polygon Rasterization .
Proceed with a specific rasterization algorithm,
depending on primitive . topology :
The point, if not filtered by § 23.2.4 Primitive Clipping , goes into § 23.2.5.1 Point Rasterization .
The line cut by § 23.2.4 Primitive Clipping goes into § 23.2.5.2 Line Rasterization .
The polygon produced in § 23.2.4 Primitive Clipping goes into § 23.2.5.4 Polygon Rasterization .
- Remove all the points rp from rasterizationPoints that have rp . destination . position outside of state . [[scissorRect]] .
Remove all the points rp from rasterizationPoints that have rp . destination . position outside of state . [[scissorRect]] .
- Return rasterizationPoints .
Return rasterizationPoints .
A single FragmentDestination is selected within the pixel containing the framebuffer coordinates of the point.
The coverage mask depends on multi-sampling mode:
coverageMask = 1 ≪ sampleIndex
coverageMask = 1 ≪ descriptor . multisample . count − 1
coverageMask = 1
The exact algorithm used for line rasterization is not defined, and may differ between
implementations. For example, the line may be drawn using § 23.2.5.4 Polygon Rasterization of a 1px-width
rectangle around the line segment, or using Bresenham’s line algorithm to select the FragmentDestination s.
Note: See Basic Line Segment Rasterization and Bresenham Line Segment Rasterization in the Vulkan 1.3 spec for more details of how line these line rasterization algorithms may be implemented.
Barycentric coordinates is a list of n numbers b i ,
defined for a point p inside a convex polygon with n vertices v i in framebuffer space.
Each b i is in range 0 to 1, inclusive, and represents the proximity to vertex v i .
Their sum is always constant:
∑ ( b i ) = 1
These coordinates uniquely specify any point p within the polygon (or on its boundary) as:
p = ∑ ( b i × p i )
For a polygon with 3 vertices - a triangle,
barycentric coordinates of any point p can be computed as follows:
A polygon = A( v 1 , v 2 , v 3 ) b 1 = A( p , b 2 , b 3 ) ÷ A polygon b 2 = A( b 1 , p , b 3 ) ÷ A polygon b 3 = A( b 1 , b 2 , p ) ÷ A polygon
Where A(list of points) is the area of the polygon with the given set of vertices.
For polygons with more than 3 vertices, the exact algorithm is implementation-dependent.
One of the possible implementations is to triangulate the polygon and compute the barycentrics
of a point based on the triangle it falls into.
A polygon is front-facing if it’s oriented towards the projection.
Otherwise, the polygon is back-facing .
Arguments:
Returns: list of RasterizationPoint .
- Let rasterizationPoints be an empty list.
Let rasterizationPoints be an empty list.
- Let v ( i ) be the framebuffer coordinates for the clipped vertex number i (starting with 1)
in a rasterized polygon of n vertices. Note: this section uses the term "polygon" instead of a "triangle",
since § 23.2.4 Primitive Clipping stage may have introduced additional vertices.
This is non-observable by the application.
Let v ( i ) be the framebuffer coordinates for the clipped vertex number i (starting with 1)
in a rasterized polygon of n vertices.
Note: this section uses the term "polygon" instead of a "triangle",
since § 23.2.4 Primitive Clipping stage may have introduced additional vertices.
This is non-observable by the application.
- Determine if the polygon is front-facing,
which depends on the sign of the area occupied by the polygon in framebuffer coordinates: area = 0.5 × (( v 1 .x × v n .y − v n .x × v 1 .y) + ∑ ( v i +1 .x × v i .y − v i .x × v i +1 .y)) The sign of area is interpreted based on the primitive . frontFace : "ccw" area > 0 is considered front-facing , otherwise back-facing "cw" area < 0 is considered front-facing , otherwise back-facing
Determine if the polygon is front-facing,
which depends on the sign of the area occupied by the polygon in framebuffer coordinates:
area = 0.5 × (( v 1 .x × v n .y − v n .x × v 1 .y) + ∑ ( v i +1 .x × v i .y − v i .x × v i +1 .y))
The sign of area is interpreted based on the primitive . frontFace :
area > 0 is considered front-facing , otherwise back-facing
area < 0 is considered front-facing , otherwise back-facing
- Cull based on primitive . cullMode : "none" All polygons pass this test. "front" The front-facing polygons are discarded,
and do not process in later stages of the render pipeline. "back" The back-facing polygons are discarded.
Cull based on primitive . cullMode :
All polygons pass this test.
The front-facing polygons are discarded,
and do not process in later stages of the render pipeline.
The back-facing polygons are discarded.
- Determine a set of fragments inside the polygon in framebuffer space -
these are locations scheduled for the per-fragment operations.
This operation is known as "point sampling".
The logic is based on descriptor . multisample : disabled Fragment s are associated with pixel centers. That is, all the points with coordinates C , where
fract( C ) = vector2(0.5, 0.5) in the framebuffer space, enclosed into the polygon, are included.
If a pixel center is on the edge of the polygon, whether or not it’s included is not defined. Note: this becomes a subject of precision for the rasterizer. enabled Each pixel is associated with descriptor . multisample . count locations, which are implementation-defined .
The locations are ordered, and the list is the same for each pixel of the framebuffer .
Each location corresponds to one fragment in the multisampled framebuffer . The rasterizer builds a mask of locations being hit inside each pixel and provides is as "sample-mask"
built-in to the fragment shader.
Determine a set of fragments inside the polygon in framebuffer space -
these are locations scheduled for the per-fragment operations.
This operation is known as "point sampling".
The logic is based on descriptor . multisample :
Fragment s are associated with pixel centers. That is, all the points with coordinates C , where
fract( C ) = vector2(0.5, 0.5) in the framebuffer space, enclosed into the polygon, are included.
If a pixel center is on the edge of the polygon, whether or not it’s included is not defined.
Note: this becomes a subject of precision for the rasterizer.
Each pixel is associated with descriptor . multisample . count locations, which are implementation-defined .
The locations are ordered, and the list is the same for each pixel of the framebuffer .
Each location corresponds to one fragment in the multisampled framebuffer .
The rasterizer builds a mask of locations being hit inside each pixel and provides is as "sample-mask"
built-in to the fragment shader.
- For each produced fragment of type FragmentDestination : Let rp be a new RasterizationPoint object Compute the list b as § 23.2.5.3 Barycentric coordinates of that fragment.
Set rp . barycentricCoordinates to b . Let d i be the depth value of v i . Set rp . depth to ∑ ( b i × d i ) Append rp to rasterizationPoints .
For each produced fragment of type FragmentDestination :
- Let rp be a new RasterizationPoint object
Let rp be a new RasterizationPoint object
- Compute the list b as § 23.2.5.3 Barycentric coordinates of that fragment.
Set rp . barycentricCoordinates to b .
Compute the list b as § 23.2.5.3 Barycentric coordinates of that fragment.
Set rp . barycentricCoordinates to b .
- Let d i be the depth value of v i .
Let d i be the depth value of v i .
- Set rp . depth to ∑ ( b i × d i )
Set rp . depth to ∑ ( b i × d i )
- Append rp to rasterizationPoints .
Append rp to rasterizationPoints .
- Return rasterizationPoints .
Return rasterizationPoints .
The fragment processing stage is a programmable stage of the render pipeline that
computes the fragment data (often a color) to be written into render targets.
This stage produces a Fragment for each RasterizationPoint :
- destination refers to FragmentDestination .
destination refers to FragmentDestination .
- frontFacing is true if it’s a fragment on the front face of a primitive.
frontFacing is true if it’s a fragment on the front face of a primitive.
- coverageMask refers to multisample coverage mask (see § 23.2.11 Sample Masking ).
coverageMask refers to multisample coverage mask (see § 23.2.11 Sample Masking ).
- depth refers to the depth in viewport coordinates ,
i.e. between the [[viewport]] minDepth and maxDepth .
depth refers to the depth in viewport coordinates ,
i.e. between the [[viewport]] minDepth and maxDepth .
- colors refers to the list of color values,
one for each target in colorAttachments .
colors refers to the list of color values,
one for each target in colorAttachments .
- depthPassed is true if the fragment passed the depthCompare operation.
depthPassed is true if the fragment passed the depthCompare operation.
- stencilPassed is true if  the fragment passed the stencil compare operation.
stencilPassed is true if  the fragment passed the stencil compare operation.
Arguments:
- rp : The RasterizationPoint , produced by § 23.2.5 Rasterization .
rp : The RasterizationPoint , produced by § 23.2.5 Rasterization .
- descriptor : The descriptor of type GPURenderPipelineDescriptor .
descriptor : The descriptor of type GPURenderPipelineDescriptor .
- state : The active RenderState .
state : The active RenderState .
Returns: Fragment or null .
- Let fragmentDesc be descriptor . fragment .
Let fragmentDesc be descriptor . fragment .
- Let depthStencilDesc be descriptor . depthStencil .
Let depthStencilDesc be descriptor . depthStencil .
- Let fragment be a new Fragment object.
Let fragment be a new Fragment object.
- Set fragment . destination to rp . destination .
Set fragment . destination to rp . destination .
- Set fragment . frontFacing to rp . frontFacing .
Set fragment . frontFacing to rp . frontFacing .
- Set fragment . coverageMask to rp . coverageMask .
Set fragment . coverageMask to rp . coverageMask .
- Set fragment . depth to rp . depth .
Set fragment . depth to rp . depth .
- If frag_depth builtin is not produced by the shader: Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ).
If frag_depth builtin is not produced by the shader:
[LINK: builtin](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ).
Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ).
- Set stencilState to depthStencilDesc ?. stencilFront if rp . frontFacing is true and depthStencilDesc ?. stencilBack otherwise.
Set stencilState to depthStencilDesc ?. stencilFront if rp . frontFacing is true and depthStencilDesc ?. stencilBack otherwise.
- Set fragment . stencilPassed to the result of compare fragment ( fragment . destination , state . [[stencilReference]] , " stencil ", state . [[depthStencilAttachment]] , stencilState ?. compare ).
Set fragment . stencilPassed to the result of compare fragment ( fragment . destination , state . [[stencilReference]] , " stencil ", state . [[depthStencilAttachment]] , stencilState ?. compare ).
- If fragmentDesc is not null : If fragment . depthPassed is false , the frag_depth builtin is not produced by the
shader entry point, and the shader entry point does not write to any storage bindings,
the following steps may be skipped. Set the shader input builtins . For each non-composite argument of the entry point,
annotated as a builtin , set its value based on the annotation: position vec4<f32> ( rp . destination . position , rp . depth , rp . perspectiveDivisor ) front_facing rp . frontFacing sample_index rp . destination . sampleIndex sample_mask rp . coverageMask For each user-specified shader stage input of the fragment stage: Let value be the interpolated fragment input,
based on rp . barycentricCoordinates , rp . primitiveVertices ,
and the interpolation qualifier on the input. Set the corresponding fragment shader location input to value . Invoke the fragment shader entry point described by fragmentDesc . The device may become lost if shader execution does not end in a reasonable amount of time, as determined by the user agent. If the fragment issued discard , return null . Set fragment . colors to the user-specified shader stage output values from the shader. Take the shader output builtins : If frag_depth builtin is produced by the shader as value : Let vp be state . [[viewport]] . Set fragment . depth to clamp( value , vp . minDepth , vp . maxDepth ). Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ). If sample_mask builtin is produced by the shader as value : Set fragment . coverageMask to fragment . coverageMask ∧ value . Otherwise we are in § 23.2.8 No Color Output mode, and fragment . colors is empty.
If fragmentDesc is not null :
- If fragment . depthPassed is false , the frag_depth builtin is not produced by the
shader entry point, and the shader entry point does not write to any storage bindings,
the following steps may be skipped.
If fragment . depthPassed is false , the frag_depth builtin is not produced by the
shader entry point, and the shader entry point does not write to any storage bindings,
the following steps may be skipped.
[LINK: builtin](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- Set the shader input builtins . For each non-composite argument of the entry point,
annotated as a builtin , set its value based on the annotation: position vec4<f32> ( rp . destination . position , rp . depth , rp . perspectiveDivisor ) front_facing rp . frontFacing sample_index rp . destination . sampleIndex sample_mask rp . coverageMask
Set the shader input builtins . For each non-composite argument of the entry point,
annotated as a builtin , set its value based on the annotation:
[LINK: builtins](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
[LINK: builtin](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
vec4<f32> ( rp . destination . position , rp . depth , rp . perspectiveDivisor )
rp . frontFacing
rp . destination . sampleIndex
rp . coverageMask
- For each user-specified shader stage input of the fragment stage: Let value be the interpolated fragment input,
based on rp . barycentricCoordinates , rp . primitiveVertices ,
and the interpolation qualifier on the input. Set the corresponding fragment shader location input to value .
For each user-specified shader stage input of the fragment stage:
[LINK: shader stage input](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-input)
- Let value be the interpolated fragment input,
based on rp . barycentricCoordinates , rp . primitiveVertices ,
and the interpolation qualifier on the input.
Let value be the interpolated fragment input,
based on rp . barycentricCoordinates , rp . primitiveVertices ,
and the interpolation qualifier on the input.
[LINK: interpolation](https://gpuweb.github.io/gpuweb/wgsl/#interpolation)
- Set the corresponding fragment shader location input to value .
Set the corresponding fragment shader location input to value .
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
- Invoke the fragment shader entry point described by fragmentDesc . The device may become lost if shader execution does not end in a reasonable amount of time, as determined by the user agent.
Invoke the fragment shader entry point described by fragmentDesc .
The device may become lost if shader execution does not end in a reasonable amount of time, as determined by the user agent.
[LINK: shader execution does not end](https://gpuweb.github.io/gpuweb/wgsl/#shader-execution-end)
- If the fragment issued discard , return null .
If the fragment issued discard , return null .
- Set fragment . colors to the user-specified shader stage output values from the shader.
Set fragment . colors to the user-specified shader stage output values from the shader.
[LINK: shader stage output](https://gpuweb.github.io/gpuweb/wgsl/#shader-stage-output)
- Take the shader output builtins : If frag_depth builtin is produced by the shader as value : Let vp be state . [[viewport]] . Set fragment . depth to clamp( value , vp . minDepth , vp . maxDepth ). Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ).
Take the shader output builtins :
[LINK: builtins](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- If frag_depth builtin is produced by the shader as value : Let vp be state . [[viewport]] . Set fragment . depth to clamp( value , vp . minDepth , vp . maxDepth ). Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ).
If frag_depth builtin is produced by the shader as value :
[LINK: builtin](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- Let vp be state . [[viewport]] .
Let vp be state . [[viewport]] .
- Set fragment . depth to clamp( value , vp . minDepth , vp . maxDepth ).
Set fragment . depth to clamp( value , vp . minDepth , vp . maxDepth ).
- Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ).
Set fragment . depthPassed to the result of compare fragment ( fragment . destination , fragment . depth , " depth ", state . [[depthStencilAttachment]] , depthStencilDesc ?. depthCompare ).
- If sample_mask builtin is produced by the shader as value : Set fragment . coverageMask to fragment . coverageMask ∧ value .
If sample_mask builtin is produced by the shader as value :
[LINK: builtin](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
- Set fragment . coverageMask to fragment . coverageMask ∧ value .
Set fragment . coverageMask to fragment . coverageMask ∧ value .
Otherwise we are in § 23.2.8 No Color Output mode, and fragment . colors is empty.
- Return fragment .
Return fragment .
Arguments:
- destination : The FragmentDestination .
destination : The FragmentDestination .
- value : The value to be compared.
value : The value to be compared.
- aspect : The aspect of attachment to sample values from.
aspect : The aspect of attachment to sample values from.
- attachment : The attachment to be compared against.
attachment : The attachment to be compared against.
- compareFunc : The GPUCompareFunction to use, or undefined .
compareFunc : The GPUCompareFunction to use, or undefined .
Returns: true if the comparison passes, or false otherwise
- If attachment is undefined or does not have aspect , return true .
If attachment is undefined or does not have aspect , return true .
- If compareFunc is undefined or "always" , return true .
If compareFunc is undefined or "always" , return true .
- Let attachmentValue be the value of aspect of attachment at destination .
Let attachmentValue be the value of aspect of attachment at destination .
- Return true if comparing value with attachmentValue using compareFunc succeeds, and false otherwise.
Return true if comparing value with attachmentValue using compareFunc succeeds, and false otherwise.
Processing of fragments happens in parallel, while any side effects,
such as writes into GPUBufferBindingType "storage" bindings,
may happen in any order.
Output merging is a fixed-function stage of the render pipeline that
outputs the fragment color, depth and stencil data to be written into the render pass attachments.
Arguments:
- fragment : The Fragment , produced by § 23.2.6 Fragment Processing .
fragment : The Fragment , produced by § 23.2.6 Fragment Processing .
- pipeline : The current GPURenderPipeline .
pipeline : The current GPURenderPipeline .
- state : The active RenderState .
state : The active RenderState .
- Let depthStencilDesc be pipeline . [[descriptor]] . depthStencil .
Let depthStencilDesc be pipeline . [[descriptor]] . depthStencil .
- If pipeline . [[writesDepth]] is true and fragment . depthPassed is true : Set the value of the depth aspect of state . [[depthStencilAttachment]] at fragment . destination to fragment . depth .
If pipeline . [[writesDepth]] is true and fragment . depthPassed is true :
- Set the value of the depth aspect of state . [[depthStencilAttachment]] at fragment . destination to fragment . depth .
Set the value of the depth aspect of state . [[depthStencilAttachment]] at fragment . destination to fragment . depth .
- If pipeline . [[writesStencil]] is true: Set stencilState to depthStencilDesc . stencilFront if fragment . frontFacing is true and depthStencilDesc . stencilBack otherwise. If fragment . stencilPassed is false : Let stencilOp be stencilState . failOp . Otherwise, if fragment . depthPassed is false : Let stencilOp be stencilState . depthFailOp . Otherwise: Let stencilOp be stencilState . passOp . Update the value of the stencil aspect of state . [[depthStencilAttachment]] at fragment . destination by performing the operation described by stencilOp .
If pipeline . [[writesStencil]] is true:
- Set stencilState to depthStencilDesc . stencilFront if fragment . frontFacing is true and depthStencilDesc . stencilBack otherwise.
Set stencilState to depthStencilDesc . stencilFront if fragment . frontFacing is true and depthStencilDesc . stencilBack otherwise.
- If fragment . stencilPassed is false : Let stencilOp be stencilState . failOp . Otherwise, if fragment . depthPassed is false : Let stencilOp be stencilState . depthFailOp . Otherwise: Let stencilOp be stencilState . passOp .
If fragment . stencilPassed is false :
- Let stencilOp be stencilState . failOp .
Let stencilOp be stencilState . failOp .
Otherwise, if fragment . depthPassed is false :
- Let stencilOp be stencilState . depthFailOp .
Let stencilOp be stencilState . depthFailOp .
Otherwise:
- Let stencilOp be stencilState . passOp .
Let stencilOp be stencilState . passOp .
- Update the value of the stencil aspect of state . [[depthStencilAttachment]] at fragment . destination by performing the operation described by stencilOp .
Update the value of the stencil aspect of state . [[depthStencilAttachment]] at fragment . destination by performing the operation described by stencilOp .
The depth input to this stage, if any, is clamped to the current [[viewport]] depth
range (regardless of whether the fragment shader stage writes the frag_depth builtin).
Arguments:
- fragment : The Fragment , produced by § 23.2.6 Fragment Processing .
fragment : The Fragment , produced by § 23.2.6 Fragment Processing .
- pipeline : The current GPURenderPipeline .
pipeline : The current GPURenderPipeline .
- state : The active RenderState .
state : The active RenderState .
- If fragment . depthPassed is false or fragment . stencilPassed is false , return.
If fragment . depthPassed is false or fragment . stencilPassed is false , return.
- Let targets be pipeline . [[descriptor]] . fragment . targets .
Let targets be pipeline . [[descriptor]] . fragment . targets .
- For each attachment of state . [[colorAttachments]] : Let color be the value from fragment . colors that corresponds with attachment . Let targetDesc be the targets entry that corresponds with attachment . If targetDesc . blend is provided : Let colorBlend be targetDesc . blend . color . Let alphaBlend be targetDesc . blend . alpha . Set the RGB components of color to the value computed by performing the operation described by colorBlend . operation with the values described by colorBlend . srcFactor and colorBlend . dstFactor . Set the alpha component of color to the value computed by performing the operation described by alphaBlend . operation with the values described by alphaBlend . srcFactor and alphaBlend . dstFactor . Set the value of attachment at fragment . destination to color .
For each attachment of state . [[colorAttachments]] :
- Let color be the value from fragment . colors that corresponds with attachment .
Let color be the value from fragment . colors that corresponds with attachment .
- Let targetDesc be the targets entry that corresponds with attachment .
Let targetDesc be the targets entry that corresponds with attachment .
- If targetDesc . blend is provided : Let colorBlend be targetDesc . blend . color . Let alphaBlend be targetDesc . blend . alpha . Set the RGB components of color to the value computed by performing the operation described by colorBlend . operation with the values described by colorBlend . srcFactor and colorBlend . dstFactor . Set the alpha component of color to the value computed by performing the operation described by alphaBlend . operation with the values described by alphaBlend . srcFactor and alphaBlend . dstFactor .
If targetDesc . blend is provided :
- Let colorBlend be targetDesc . blend . color .
Let colorBlend be targetDesc . blend . color .
- Let alphaBlend be targetDesc . blend . alpha .
Let alphaBlend be targetDesc . blend . alpha .
- Set the RGB components of color to the value computed by performing the operation described by colorBlend . operation with the values described by colorBlend . srcFactor and colorBlend . dstFactor .
Set the RGB components of color to the value computed by performing the operation described by colorBlend . operation with the values described by colorBlend . srcFactor and colorBlend . dstFactor .
- Set the alpha component of color to the value computed by performing the operation described by alphaBlend . operation with the values described by alphaBlend . srcFactor and alphaBlend . dstFactor .
Set the alpha component of color to the value computed by performing the operation described by alphaBlend . operation with the values described by alphaBlend . srcFactor and alphaBlend . dstFactor .
- Set the value of attachment at fragment . destination to color .
Set the value of attachment at fragment . destination to color .
In no-color-output mode, pipeline does not produce any color attachment outputs.
The pipeline still performs rasterization and produces depth values
based on the vertex position output. The depth testing and stencil operations can still be used.
In alpha-to-coverage mode, an additional alpha-to-coverage mask of MSAA samples is generated based on the alpha component of the
fragment shader output value at @location(0) .
The algorithm of producing the extra mask is platform-dependent and can vary for different pixels.
It guarantees that:
- if alpha ≤ 0.0, the result is 0x0
if alpha ≤ 0.0, the result is 0x0
- if alpha ≥ 1.0, the result is 0xFFFFFFFF
if alpha ≥ 1.0, the result is 0xFFFFFFFF
- intermediate alpha values should result in a proportionate number of bits set to 1 in the mask.
Not all platforms guarantee that the number of bits set to 1 in the mask monotonically
increases as alpha increases for a given pixel.
intermediate alpha values should result in a proportionate number of bits set to 1 in the mask.
Not all platforms guarantee that the number of bits set to 1 in the mask monotonically
increases as alpha increases for a given pixel.
When rendering into multisampled render attachments, fragment shaders can be run once per-pixel or once per-sample.
Fragment shaders must run once per-sample if either the sample_index builtin or sample interpolation sampling is used and contributes to the shader output. Otherwise fragment shaders may run once per-pixel with the result
broadcast out to each of the samples included in the final sample mask .
[LINK: builtin](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)
[LINK: interpolation sampling](https://gpuweb.github.io/gpuweb/wgsl/#interpolation-sampling)
When using per-sample shading, the color output for sample N is produced by the fragment shader execution
with sample_index == N for the current pixel.
The final sample mask for a pixel is computed as: rasterization mask & mask & shader-output mask .
Only the lower count bits of the mask are considered.
If the least-significant bit at position N of the final sample mask has value of "0",
the sample color outputs (corresponding to sample N ) to all attachments of the fragment shader are discarded.
Also, no depth test or stencil operations are executed on the relevant samples of the depth-stencil attachment.
The rasterization mask is produced by the rasterization stage,
based on the shape of the rasterized polygon. The samples included in the shape get the relevant
bits 1 in the mask.
The shader-output mask takes the output value of "sample_mask" builtin in the fragment shader.
If the builtin is not output from the fragment shader, and alphaToCoverageEnabled is enabled, the shader-output mask becomes the alpha-to-coverage mask . Otherwise, it defaults to 0xFFFFFFFF.
[LINK: builtin](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values)

## 24. Type Definitions

### 24.1. Colors & Vectors

Note: double is large enough to precisely hold 32-bit signed/unsigned
integers and single-precision floats.
The red channel value.
The green channel value.
The blue channel value.
The alpha channel value.
- color . r refers to
either GPUColorDict . r or the first item of the sequence ( asserting there is such an item).
color . r refers to
either GPUColorDict . r or the first item of the sequence ( asserting there is such an item).
- color . g refers to
either GPUColorDict . g or the second item of the sequence ( asserting there is such an item).
color . g refers to
either GPUColorDict . g or the second item of the sequence ( asserting there is such an item).
- color . b refers to
either GPUColorDict . b or the third item of the sequence ( asserting there is such an item).
color . b refers to
either GPUColorDict . b or the third item of the sequence ( asserting there is such an item).
- color . a refers to
either GPUColorDict . a or the fourth item of the sequence ( asserting there is such an item).
color . a refers to
either GPUColorDict . a or the fourth item of the sequence ( asserting there is such an item).
Arguments:
- color : The GPUColor to validate.
color : The GPUColor to validate.
Returns: undefined
Content timeline steps:
- Throw a TypeError if color is a sequence and color . size ≠ 4.
Throw a TypeError if color is a sequence and color . size ≠ 4.
- origin . x refers to
either GPUOrigin2DDict . x or the first item of the sequence (0 if not present).
origin . x refers to
either GPUOrigin2DDict . x or the first item of the sequence (0 if not present).
- origin . y refers to
either GPUOrigin2DDict . y or the second item of the sequence (0 if not present).
origin . y refers to
either GPUOrigin2DDict . y or the second item of the sequence (0 if not present).
Arguments:
- origin : The GPUOrigin2D to validate.
origin : The GPUOrigin2D to validate.
Returns: undefined
Content timeline steps:
- Throw a TypeError if origin is a sequence and origin . size > 2.
Throw a TypeError if origin is a sequence and origin . size > 2.
- origin . x refers to
either GPUOrigin3DDict . x or the first item of the sequence (0 if not present).
origin . x refers to
either GPUOrigin3DDict . x or the first item of the sequence (0 if not present).
- origin . y refers to
either GPUOrigin3DDict . y or the second item of the sequence (0 if not present).
origin . y refers to
either GPUOrigin3DDict . y or the second item of the sequence (0 if not present).
- origin . z refers to
either GPUOrigin3DDict . z or the third item of the sequence (0 if not present).
origin . z refers to
either GPUOrigin3DDict . z or the third item of the sequence (0 if not present).
Arguments:
- origin : The GPUOrigin3D to validate.
origin : The GPUOrigin3D to validate.
Returns: undefined
Content timeline steps:
- Throw a TypeError if origin is a sequence and origin . size > 3.
Throw a TypeError if origin is a sequence and origin . size > 3.
The width of the extent.
The height of the extent.
The depth of the extent or the number of array layers it contains.
If used with a GPUTexture with a GPUTextureDimension of "3d" defines the depth of the texture. If used with a GPUTexture with a GPUTextureDimension of "2d" defines the number of array layers in the texture.
- extent . width refers to
either GPUExtent3DDict . width or the first item of the sequence ( asserting there is such an item).
extent . width refers to
either GPUExtent3DDict . width or the first item of the sequence ( asserting there is such an item).
- extent . height refers to
either GPUExtent3DDict . height or the second item of the sequence (1 if not present).
extent . height refers to
either GPUExtent3DDict . height or the second item of the sequence (1 if not present).
- extent . depthOrArrayLayers refers to
either GPUExtent3DDict . depthOrArrayLayers or the third item of the sequence (1 if not present).
extent . depthOrArrayLayers refers to
either GPUExtent3DDict . depthOrArrayLayers or the third item of the sequence (1 if not present).
Arguments:
- extent : The GPUExtent3D to validate.
extent : The GPUExtent3D to validate.
Returns: undefined
Content timeline steps:
- Throw a TypeError if:
Throw a TypeError if:
- extent is a sequence, and
extent is a sequence, and
- extent . size < 1 or extent . size > 3.
extent . size < 1 or extent . size > 3.

## 25. Feature Index

### 25.1. "core-features-and-limits"

Allows all Core WebGPU features and limits to be used.
This is always available unless featureLevel is set to "compatibility" ,
in which case it may or may not be available (see those definitions for information).

### 25.2. "depth-clip-control"

Allows depth clipping to be disabled.
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New GPUPrimitiveState dictionary members: unclippedDepth
New GPUPrimitiveState dictionary members:
- unclippedDepth
unclippedDepth

### 25.3. "depth32float-stencil8"

Allows for explicit creation of textures of format "depth32float-stencil8" .
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New GPUTextureFormat enum values: "depth32float-stencil8"
New GPUTextureFormat enum values:
- "depth32float-stencil8"
"depth32float-stencil8"

### 25.4. "texture-compression-bc"

Allows for explicit creation of textures of BC compressed formats which include the "S3TC",
"RGTC", and "BPTC" formats. Only supports 2D textures.
Note: Adapters which support "texture-compression-bc" do not
always support "texture-compression-bc-sliced-3d" .
To use "texture-compression-bc-sliced-3d" , "texture-compression-bc" must be enabled explicitly as this feature
does not enable the BC formats.
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New GPUTextureFormat enum values: "bc1-rgba-unorm" "bc1-rgba-unorm-srgb" "bc2-rgba-unorm" "bc2-rgba-unorm-srgb" "bc3-rgba-unorm" "bc3-rgba-unorm-srgb" "bc4-r-unorm" "bc4-r-snorm" "bc5-rg-unorm" "bc5-rg-snorm" "bc6h-rgb-ufloat" "bc6h-rgb-float" "bc7-rgba-unorm" "bc7-rgba-unorm-srgb"
New GPUTextureFormat enum values:
- "bc1-rgba-unorm"
"bc1-rgba-unorm"
- "bc1-rgba-unorm-srgb"
"bc1-rgba-unorm-srgb"
- "bc2-rgba-unorm"
"bc2-rgba-unorm"
- "bc2-rgba-unorm-srgb"
"bc2-rgba-unorm-srgb"
- "bc3-rgba-unorm"
"bc3-rgba-unorm"
- "bc3-rgba-unorm-srgb"
"bc3-rgba-unorm-srgb"
- "bc4-r-unorm"
"bc4-r-unorm"
- "bc4-r-snorm"
"bc4-r-snorm"
- "bc5-rg-unorm"
"bc5-rg-unorm"
- "bc5-rg-snorm"
"bc5-rg-snorm"
- "bc6h-rgb-ufloat"
"bc6h-rgb-ufloat"
- "bc6h-rgb-float"
"bc6h-rgb-float"
- "bc7-rgba-unorm"
"bc7-rgba-unorm"
- "bc7-rgba-unorm-srgb"
"bc7-rgba-unorm-srgb"

### 25.5. "texture-compression-bc-sliced-3d"

Allows the 3d dimension for textures with BC compressed formats .
Note: Adapters which support "texture-compression-bc" do not
always support "texture-compression-bc-sliced-3d" .
To use "texture-compression-bc-sliced-3d" , "texture-compression-bc" must be enabled explicitly as this feature
does not enable the BC formats.
This feature adds no optional API surfaces .
[LINK: optional API surfaces](#optional-api-surface)

### 25.6. "texture-compression-etc2"

Allows for explicit creation of textures of ETC2 compressed formats . Only supports 2D textures.
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New GPUTextureFormat enum values: "etc2-rgb8unorm" "etc2-rgb8unorm-srgb" "etc2-rgb8a1unorm" "etc2-rgb8a1unorm-srgb" "etc2-rgba8unorm" "etc2-rgba8unorm-srgb" "eac-r11unorm" "eac-r11snorm" "eac-rg11unorm" "eac-rg11snorm"
New GPUTextureFormat enum values:
- "etc2-rgb8unorm"
"etc2-rgb8unorm"
- "etc2-rgb8unorm-srgb"
"etc2-rgb8unorm-srgb"
- "etc2-rgb8a1unorm"
"etc2-rgb8a1unorm"
- "etc2-rgb8a1unorm-srgb"
"etc2-rgb8a1unorm-srgb"
- "etc2-rgba8unorm"
"etc2-rgba8unorm"
- "etc2-rgba8unorm-srgb"
"etc2-rgba8unorm-srgb"
- "eac-r11unorm"
"eac-r11unorm"
- "eac-r11snorm"
"eac-r11snorm"
- "eac-rg11unorm"
"eac-rg11unorm"
- "eac-rg11snorm"
"eac-rg11snorm"

### 25.7. "texture-compression-astc"

Allows for explicit creation of textures of ASTC compressed formats . Only supports 2D textures.
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New GPUTextureFormat enum values: "astc-4x4-unorm" "astc-4x4-unorm-srgb" "astc-5x4-unorm" "astc-5x4-unorm-srgb" "astc-5x5-unorm" "astc-5x5-unorm-srgb" "astc-6x5-unorm" "astc-6x5-unorm-srgb" "astc-6x6-unorm" "astc-6x6-unorm-srgb" "astc-8x5-unorm" "astc-8x5-unorm-srgb" "astc-8x6-unorm" "astc-8x6-unorm-srgb" "astc-8x8-unorm" "astc-8x8-unorm-srgb" "astc-10x5-unorm" "astc-10x5-unorm-srgb" "astc-10x6-unorm" "astc-10x6-unorm-srgb" "astc-10x8-unorm" "astc-10x8-unorm-srgb" "astc-10x10-unorm" "astc-10x10-unorm-srgb" "astc-12x10-unorm" "astc-12x10-unorm-srgb" "astc-12x12-unorm" "astc-12x12-unorm-srgb"
New GPUTextureFormat enum values:
- "astc-4x4-unorm"
"astc-4x4-unorm"
- "astc-4x4-unorm-srgb"
"astc-4x4-unorm-srgb"
- "astc-5x4-unorm"
"astc-5x4-unorm"
- "astc-5x4-unorm-srgb"
"astc-5x4-unorm-srgb"
- "astc-5x5-unorm"
"astc-5x5-unorm"
- "astc-5x5-unorm-srgb"
"astc-5x5-unorm-srgb"
- "astc-6x5-unorm"
"astc-6x5-unorm"
- "astc-6x5-unorm-srgb"
"astc-6x5-unorm-srgb"
- "astc-6x6-unorm"
"astc-6x6-unorm"
- "astc-6x6-unorm-srgb"
"astc-6x6-unorm-srgb"
- "astc-8x5-unorm"
"astc-8x5-unorm"
- "astc-8x5-unorm-srgb"
"astc-8x5-unorm-srgb"
- "astc-8x6-unorm"
"astc-8x6-unorm"
- "astc-8x6-unorm-srgb"
"astc-8x6-unorm-srgb"
- "astc-8x8-unorm"
"astc-8x8-unorm"
- "astc-8x8-unorm-srgb"
"astc-8x8-unorm-srgb"
- "astc-10x5-unorm"
"astc-10x5-unorm"
- "astc-10x5-unorm-srgb"
"astc-10x5-unorm-srgb"
- "astc-10x6-unorm"
"astc-10x6-unorm"
- "astc-10x6-unorm-srgb"
"astc-10x6-unorm-srgb"
- "astc-10x8-unorm"
"astc-10x8-unorm"
- "astc-10x8-unorm-srgb"
"astc-10x8-unorm-srgb"
- "astc-10x10-unorm"
"astc-10x10-unorm"
- "astc-10x10-unorm-srgb"
"astc-10x10-unorm-srgb"
- "astc-12x10-unorm"
"astc-12x10-unorm"
- "astc-12x10-unorm-srgb"
"astc-12x10-unorm-srgb"
- "astc-12x12-unorm"
"astc-12x12-unorm"
- "astc-12x12-unorm-srgb"
"astc-12x12-unorm-srgb"

### 25.8. "texture-compression-astc-sliced-3d"

Allows the 3d dimension for textures with ASTC compressed formats .
Note: Adapters which support "texture-compression-astc" do not
always support "texture-compression-astc-sliced-3d" .
To use "texture-compression-astc-sliced-3d" , "texture-compression-astc" must be enabled explicitly as this feature
does not enable the ASTC formats.
This feature adds no optional API surfaces .
[LINK: optional API surfaces](#optional-api-surface)

### 25.9. "timestamp-query"

Adds the ability to query timestamps from GPU command buffers. See § 20.4 Timestamp Query .
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New GPUQueryType values: "timestamp"
New GPUQueryType values:
- "timestamp"
"timestamp"
- New GPUComputePassDescriptor members: timestampWrites
New GPUComputePassDescriptor members:
- timestampWrites
timestampWrites
- New GPURenderPassDescriptor members: timestampWrites
New GPURenderPassDescriptor members:
- timestampWrites
timestampWrites

### 25.10. "indirect-first-instance"

Allows the use of non-zero firstInstance values in indirect draw parameters and indirect drawIndexed parameters .
This feature adds no optional API surfaces .
[LINK: optional API surfaces](#optional-api-surface)

### 25.11. "shader-f16"

Allows the use of the half-precision floating-point type f16 in WGSL.
[LINK: f16](https://gpuweb.github.io/gpuweb/wgsl/#f16)
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New WGSL extensions: f16
New WGSL extensions:
- f16
f16
[LINK: f16](https://gpuweb.github.io/gpuweb/wgsl/#extension-f16)

### 25.12. "rg11b10ufloat-renderable"

Allows the RENDER_ATTACHMENT usage on textures with format "rg11b10ufloat" ,
and also allows textures of that format to be blended, multisampled, and resolved.
Implicitly allows "rg11b10ufloat" as a destination format in copyExternalImageToTexture() .
This feature adds no optional API surfaces .
[LINK: optional API surfaces](#optional-api-surface)
Note: This feature is automatically enabled by "texture-formats-tier1" ,
which is automatically enabled by "texture-formats-tier2" .

### 25.13. "bgra8unorm-storage"

Allows the STORAGE_BINDING usage on textures with format "bgra8unorm" .
This feature adds no optional API surfaces .
[LINK: optional API surfaces](#optional-api-surface)

### 25.14. "float32-filterable"

Makes textures with formats "r32float" , "rg32float" , and "rgba32float" filterable .

### 25.15. "float32-blendable"

Makes textures with formats "r32float" , "rg32float" , and "rgba32float" blendable .

### 25.16. "clip-distances"

Allows the use of clip_distances in WGSL.
[LINK: clip_distances](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-clip_distances)
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New WGSL extensions: clip_distances
New WGSL extensions:
- clip_distances
clip_distances
[LINK: clip_distances](https://gpuweb.github.io/gpuweb/wgsl/#extension-clip_distances)

### 25.17. "dual-source-blending"

Allows the use of blend_src in WGSL and simultaneously using both pixel shader outputs
( @blend_src(0) and @blend_src(1) ) as inputs to a blending operation with the single color
attachment at location 0 .
[LINK: blend_src](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
[LINK: location](https://gpuweb.github.io/gpuweb/wgsl/#input-output-locations)
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- Allows the use of the below GPUBlendFactor s: "src1" "one-minus-src1" "src1-alpha" "one-minus-src1-alpha"
Allows the use of the below GPUBlendFactor s:
- "src1"
"src1"
- "one-minus-src1"
"one-minus-src1"
- "src1-alpha"
"src1-alpha"
- "one-minus-src1-alpha"
"one-minus-src1-alpha"
- New WGSL extensions: dual_source_blending
New WGSL extensions:
- dual_source_blending
dual_source_blending
[LINK: dual_source_blending](https://gpuweb.github.io/gpuweb/wgsl/#extension-dual_source_blending)

### 25.18. "subgroups"

Allows the use of the subgroup and quad operations in WGSL.
This feature adds no optional API surfaces , but the following entries of GPUAdapterInfo expose real values whenever the feature is available on the adapter:
[LINK: optional API surfaces](#optional-api-surface)
- subgroupMinSize
subgroupMinSize
- subgroupMaxSize
subgroupMaxSize
- New WGSL extensions: subgroups
New WGSL extensions:
- subgroups
subgroups
[LINK: subgroups](https://gpuweb.github.io/gpuweb/wgsl/#extension-subgroups)

### 25.19. "texture-formats-tier1"

Enabling "texture-formats-tier1" at device creation will enable "rg11b10ufloat-renderable" . The following items are in addition to that.
Supports the below new GPUTextureFormat s with the RENDER_ATTACHMENT , blendable , multisampling capabilities and the STORAGE_BINDING capability
with the "read-only" and "write-only" GPUStorageTextureAccess es:
- "r16unorm"
"r16unorm"
- "r16snorm"
"r16snorm"
- "rg16unorm"
"rg16unorm"
- "rg16snorm"
"rg16snorm"
- "rgba16unorm"
"rgba16unorm"
- "rgba16snorm"
"rgba16snorm"
Allows the RENDER_ATTACHMENT , blendable , multisampling and resolve capabilities on below GPUTextureFormat s:
- "r8snorm"
"r8snorm"
- "rg8snorm"
"rg8snorm"
- "rgba8snorm"
"rgba8snorm"
Allows the "read-only" or "write-only" GPUStorageTextureAccess on below GPUTextureFormat s:
- "r8unorm"
"r8unorm"
- "r8snorm"
"r8snorm"
- "r8uint"
"r8uint"
- "r8sint"
"r8sint"
- "rg8unorm"
"rg8unorm"
- "rg8snorm"
"rg8snorm"
- "rg8uint"
"rg8uint"
- "rg8sint"
"rg8sint"
- "r16uint"
"r16uint"
- "r16sint"
"r16sint"
- "r16float"
"r16float"
- "rg16uint"
"rg16uint"
- "rg16sint"
"rg16sint"
- "rg16float"
"rg16float"
- "rgb10a2uint"
"rgb10a2uint"
- "rgb10a2unorm"
"rgb10a2unorm"
- "rg11b10ufloat"
"rg11b10ufloat"
Implicitly allows the following new destination formats in copyExternalImageToTexture() :
- "r16unorm"
"r16unorm"
- "rg16unorm"
"rg16unorm"
- "rgba16unorm"
"rgba16unorm"
Note: This feature is automatically enabled by "texture-formats-tier2" .

### 25.20. "texture-formats-tier2"

Enabling "texture-formats-tier2" at device creation will enable "texture-formats-tier1" . The following items are in addition to that.
Allows the "read-write" GPUStorageTextureAccess on below GPUTextureFormat s:
- "r8unorm"
"r8unorm"
- "r8uint"
"r8uint"
- "r8sint"
"r8sint"
- "rgba8unorm"
"rgba8unorm"
- "rgba8uint"
"rgba8uint"
- "rgba8sint"
"rgba8sint"
- "r16uint"
"r16uint"
- "r16sint"
"r16sint"
- "r16float"
"r16float"
- "rgba16uint"
"rgba16uint"
- "rgba16sint"
"rgba16sint"
- "rgba16float"
"rgba16float"
- "rgba32uint"
"rgba32uint"
- "rgba32sint"
"rgba32sint"
- "rgba32float"
"rgba32float"

### 25.21. "primitive-index"

Allows the use of primitive_index in WGSL.
[LINK: primitive_index](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-primitive_index)
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New WGSL extensions: primitive_index
New WGSL extensions:
- primitive_index
primitive_index
[LINK: primitive_index](https://gpuweb.github.io/gpuweb/wgsl/#extension-primitive_index)

### 25.22. "texture-component-swizzle"

Allows GPUTextureView s to rearrange or replace the color components from texture’s red/green/blue/alpha channels
when used as a TEXTURE_BINDING .
Also defines previously-implementation-defined behavior when § 26.1.2.1 Reading and Sampling Depth/Stencil Textures .
This feature adds the following optional API surfaces :
[LINK: optional API surfaces](#optional-api-surface)
- New GPUTextureViewDescriptor dictionary members: swizzle
New GPUTextureViewDescriptor dictionary members:
- swizzle
swizzle

## 26. Appendices

### 26.1. Texture Format Capabilities

All supported plain color formats support usages COPY_SRC , COPY_DST , and TEXTURE_BINDING , and dimension "3d" .
The RENDER_ATTACHMENT and STORAGE_BINDING columns
specify support for GPUTextureUsage.RENDER_ATTACHMENT and GPUTextureUsage.STORAGE_BINDING usage respectively.
The render target pixel byte cost and render target component alignment are used to validate the maxColorAttachmentBytesPerSample limit.
Note: The texel block memory cost of each of these formats is the same as its texel block copy footprint .
"float" if "float32-filterable" is enabled
"unfilterable-float"
"float" if "float32-filterable" is enabled
"unfilterable-float"
"float" if "float32-filterable" is enabled
"unfilterable-float"
A depth-or-stencil format is any format with depth and/or stencil aspects.
A combined depth-stencil format is a depth-or-stencil format that has both
depth and stencil aspects.
All depth-or-stencil formats support the COPY_SRC , COPY_DST , TEXTURE_BINDING , and RENDER_ATTACHMENT usages.
All of these formats support multisampling.
However, certain copy operations also restrict the source and destination formats, and none of
these formats support textures with "3d" dimension.
Depth textures cannot be used with "filtering" samplers, but can always
be used with "comparison" samplers even if they use filtering.
24-bit depth refers to a 24-bit unsigned normalized depth format with a range from
0.0 to 1.0, which would be spelled "depth24unorm" if exposed.
It is possible to bind a depth-aspect GPUTextureView to either a texture_depth_* binding or a binding with other non-depth 2d/cube texture types.
A stencil-aspect GPUTextureView must be bound to a normal texture binding type.
The sampleType in the GPUBindGroupLayout must be "uint" .
If the "texture-component-swizzle" feature is enabled, reading or sampling the
depth or stencil aspect of a texture behaves as if the texture contains the values (V, 0, 0, 1) where V is the actual depth or stencil value. Otherwise, the values are (V, X, X, X) where each X
is an implementation-defined unspecified value.
To reduce compatibility issues in practice, implementations should provide (V, 0, 0, 1) wherever possible, even if the "texture-component-swizzle" feature is not
enabled.
For depth-aspect bindings, the unspecified values are not visible through bindings with texture_depth_* types.
- textureSample(tex, ...) will return vec4<f32>(D, X, X, X) .
textureSample(tex, ...) will return vec4<f32>(D, X, X, X) .
- textureGather(0, tex, ...) will return vec4<f32>(D1, D2, D3, D4) .
textureGather(0, tex, ...) will return vec4<f32>(D1, D2, D3, D4) .
- textureGather(2, tex, ...) will return vec4<f32>(X1, X2, X3, X4) (a completely unspecified value).
textureGather(2, tex, ...) will return vec4<f32>(X1, X2, X3, X4) (a completely unspecified value).
Note: Short of adding a new more constrained stencil sampler type (like depth), it’s infeasible for
implementations to efficiently paper over the driver differences for depth/stencil reads.
As this was not a portability pain point for WebGL, it’s not expected to be problematic in WebGPU.
In practice, expect either (V, V, V, V) or (V, 0, 0, 1) (where V is the depth or stencil
value), depending on hardware.
The depth aspects of depth32float formats
( "depth32float" and "depth32float-stencil8" have a limited range.
As a result, copies into such textures are only valid from other textures of the same format.
The depth aspects of depth24plus formats
( "depth24plus" and "depth24plus-stencil8" )
have opaque representations (implemented as either 24-bit depth or "depth32float" ).
As a result, depth-aspect texel copies are not allowed with these formats.
- All of these formats can be written in a render pass using a fragment shader that outputs
depth values via the frag_depth output.
All of these formats can be written in a render pass using a fragment shader that outputs
depth values via the frag_depth output.
- Textures with "depth24plus" formats can be read as shader textures, and
written to a texture (as a render pass attachment) or
buffer (via a storage buffer binding in a compute shader).
Textures with "depth24plus" formats can be read as shader textures, and
written to a texture (as a render pass attachment) or
buffer (via a storage buffer binding in a compute shader).
All packed texture formats support COPY_SRC , COPY_DST ,
and TEXTURE_BINDING usages.
All of these formats are filterable .
None of these formats are renderable or support multisampling.
A compressed format is any format with a block size greater than 1×1.
Note: The texel block memory cost of each of these formats is the same as its texel block copy footprint .

## Conformance

### Document conventions

Conformance requirements are expressed
    with a combination of descriptive assertions
    and RFC 2119 terminology.
    The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL”
    in the normative parts of this document
    are to be interpreted as described in RFC 2119.
    However, for readability,
    these words do not appear in all uppercase letters in this specification.
All of the text of this specification is normative
    except sections explicitly marked as non-normative, examples, and notes. [RFC2119]
Examples in this specification are introduced with the words “for example”
    or are set apart from the normative text
    with class="example" ,
    like this:
This is an example of an informative example.
Informative notes begin with the word “Note”
    and are set apart from the normative text
    with class="note" ,
    like this:
Note, this is an informative note.

### Conformant Algorithms

Requirements phrased in the imperative as part of algorithms
    (such as "strip any leading space characters"
    or "return false and abort these steps")
    are to be interpreted with the meaning of the key word
    ("must", "should", "may", etc)
    used in introducing the algorithm.
Conformance requirements phrased as algorithms or specific steps
    can be implemented in any manner,
    so long as the end result is equivalent.
    In particular, the algorithms defined in this specification
    are intended to be easy to understand
    and are not intended to be performant.
    Implementers are encouraged to optimize.

## Index

### Terms defined by this specification

- "1d" enum-value for GPUTextureDimension , in § 6.1.1 enum-value for GPUTextureViewDimension , in § 6.2.1
- enum-value for GPUTextureDimension , in § 6.1.1
- enum-value for GPUTextureViewDimension , in § 6.2.1
- 24-bit depth , in § 26.1.2
- "2d" enum-value for GPUTextureDimension , in § 6.1.1 enum-value for GPUTextureViewDimension , in § 6.2.1
- enum-value for GPUTextureDimension , in § 6.1.1
- enum-value for GPUTextureViewDimension , in § 6.2.1
- "2d-array" , in § 6.2.1
- "3d" enum-value for GPUTextureDimension , in § 6.1.1 enum-value for GPUTextureViewDimension , in § 6.2.1
- enum-value for GPUTextureDimension , in § 6.1.1
- enum-value for GPUTextureViewDimension , in § 6.2.1
- a dfn for GPUColor , in § 24.1 dict-member for GPUColorDict , in § 24.1
- dfn for GPUColor , in § 24.1
- dict-member for GPUColorDict , in § 24.1
- access , in § 8.1.1
- active buffer mapping , in § 5.1
- [[adapter]] attribute for GPUAdapter , in § 4.3 attribute for device , in § 3.5.2
- attribute for GPUAdapter , in § 4.3
- attribute for device , in § 3.5.2
- adapter , in § 3.5.1
- adapterInfo , in § 4.4
- "add" , in § 10.3.5.1
- Add , in § 3.4.4
- add , in § 3.4.4
- addressModeU , in § 7.1.1
- addressModeV , in § 7.1.1
- addressModeW , in § 7.1.1
- alignment , in § 3.6.2
- "all" , in § 6.2.1
- ALL , in § 10.3.5
- allowed buffer usages , in § 4.4
- allowed texture usages , in § 4.4
- ALPHA , in § 10.3.5
- alpha , in § 10.3.5
- alphaMode , in § 21.4
- alphaToCoverageEnabled , in § 10.3.3
- alpha-to-coverage mask , in § 23.2.9
- "always" , in § 7.1.1
- a new device , in § 3.5.2
- architecture , in § 3.6.2.4
- array layer , in § 6.1
- array layer count , in § 6.2.1
- arrayLayerCount , in § 6.2.1
- arrayStride , in § 10.3.7.1
- aspect definition of , in § 6.1 dict-member for GPUTexelCopyTextureInfo , in § 11.2.3 dict-member for GPUTextureViewDescriptor , in § 6.2.1
- definition of , in § 6.1
- dict-member for GPUTexelCopyTextureInfo , in § 11.2.3
- dict-member for GPUTextureViewDescriptor , in § 6.2.1
- Aspect-specific format , in § 26.1.2
- assemble primitives , in § 23.2.3
- "astc-10x10-unorm" , in § 6.3
- "astc-10x10-unorm-srgb" , in § 6.3
- "astc-10x5-unorm" , in § 6.3
- "astc-10x5-unorm-srgb" , in § 6.3
- "astc-10x6-unorm" , in § 6.3
- "astc-10x6-unorm-srgb" , in § 6.3
- "astc-10x8-unorm" , in § 6.3
- "astc-10x8-unorm-srgb" , in § 6.3
- "astc-12x10-unorm" , in § 6.3
- "astc-12x10-unorm-srgb" , in § 6.3
- "astc-12x12-unorm" , in § 6.3
- "astc-12x12-unorm-srgb" , in § 6.3
- "astc-4x4-unorm" , in § 6.3
- "astc-4x4-unorm-srgb" , in § 6.3
- "astc-5x4-unorm" , in § 6.3
- "astc-5x4-unorm-srgb" , in § 6.3
- "astc-5x5-unorm" , in § 6.3
- "astc-5x5-unorm-srgb" , in § 6.3
- "astc-6x5-unorm" , in § 6.3
- "astc-6x5-unorm-srgb" , in § 6.3
- "astc-6x6-unorm" , in § 6.3
- "astc-6x6-unorm-srgb" , in § 6.3
- "astc-8x5-unorm" , in § 6.3
- "astc-8x5-unorm-srgb" , in § 6.3
- "astc-8x6-unorm" , in § 6.3
- "astc-8x6-unorm-srgb" , in § 6.3
- "astc-8x8-unorm" , in § 6.3
- "astc-8x8-unorm-srgb" , in § 6.3
- async pipeline creation , in § 10
- attachment , in § 3.4.3
- attachment-read , in § 3.4.3
- [[attachment_size]] , in § 17.1
- attributes , in § 10.3.7.1
- "auto" , in § 10.1
- Automatic Expiry Task Source , in § 3.10.1
- available , in § 5.1
- b dfn for GPUColor , in § 24.1 dict-member for GPUColorDict , in § 24.1
- dfn for GPUColor , in § 24.1
- dict-member for GPUColorDict , in § 24.1
- "back" , in § 10.3.2
- back-facing , in § 23.2.5.4
- barycentricCoordinates , in § 23.2.5
- baseArrayLayer , in § 6.2.1
- baseMipLevel , in § 6.2.1
- "bc1-rgba-unorm" , in § 6.3
- "bc1-rgba-unorm-srgb" , in § 6.3
- "bc2-rgba-unorm" , in § 6.3
- "bc2-rgba-unorm-srgb" , in § 6.3
- "bc3-rgba-unorm" , in § 6.3
- "bc3-rgba-unorm-srgb" , in § 6.3
- "bc4-r-snorm" , in § 6.3
- "bc4-r-unorm" , in § 6.3
- "bc5-rg-snorm" , in § 6.3
- "bc5-rg-unorm" , in § 6.3
- "bc6h-rgb-float" , in § 6.3
- "bc6h-rgb-ufloat" , in § 6.3
- "bc7-rgba-unorm" , in § 6.3
- "bc7-rgba-unorm-srgb" , in § 6.3
- becomes lost , in § 3.5.2
- beginComputePass() , in § 13.3
- beginComputePass(descriptor) , in § 13.3
- beginningOfPassWriteIndex dict-member for GPUComputePassTimestampWrites , in § 16.1.1 dict-member for GPURenderPassTimestampWrites , in § 17.1.1
- dict-member for GPUComputePassTimestampWrites , in § 16.1.1
- dict-member for GPURenderPassTimestampWrites , in § 17.1.1
- beginOcclusionQuery(queryIndex) , in § 17.2.3
- beginRenderPass(descriptor) , in § 13.3
- better , in § 3.6.2
- "bgra8unorm" , in § 6.3
- "bgra8unorm-srgb" , in § 6.3
- "bgra8unorm-storage" , in § 25.12
- biased fragment depth , in § 10.3.6
- [[bindGroupLayouts]] , in § 8.3
- bindGroupLayouts , in § 8.3.1
- [[bind_groups]] , in § 14
- binding dict-member for GPUBindGroupEntry , in § 8.2.1 dict-member for GPUBindGroupLayoutEntry , in § 8.1.1
- dict-member for GPUBindGroupEntry , in § 8.2.1
- dict-member for GPUBindGroupLayoutEntry , in § 8.1.1
- Binding member , in § 8.1.1
- Binding Resource Type , in § 8.1.1
- Binding type , in § 8.1.1
- Binding usage , in § 8.1.1
- blend , in § 10.3.5
- blendable , in § 6.3
- blendable format , in § 6.3
- [[blendConstant]] , in § 17.1
- BLUE , in § 10.3.5
- bound buffer ranges , in § 8.2
- buffer dict-member for GPUBindGroupLayoutEntry , in § 8.1.1 dict-member for GPUBufferBinding , in § 8.2.1 dict-member for GPUTexelCopyBufferInfo , in § 11.2.2
- dict-member for GPUBindGroupLayoutEntry , in § 8.1.1
- dict-member for GPUBufferBinding , in § 8.2.1
- dict-member for GPUTexelCopyBufferInfo , in § 11.2.2
- buffer-binding-aliasing , in § 8.2.1
- buffers , in § 10.3.7.1
- byteSize , in § 10.3.7.1
- bytesPerRow , in § 11.2.1
- Calculating color attachment bytes per sample , in § 17.1.1.1
- canvas , in § 21.2
- capabilities , in § 3.6
- "ccw" , in § 10.3.2
- "clamp-to-edge" , in § 7.1.1
- "clear" , in § 17.1.1.3
- clearBuffer(buffer) , in § 13.4
- clearBuffer(buffer, offset) , in § 13.4
- clearBuffer(buffer, offset, size) , in § 13.4
- clearValue , in § 17.1.1.1
- "clip-distances" , in § 25.15
- clip position , in § 23.2.4
- Clip space coordinates , in § 3.3
- clip volume , in § 23.2.4
- code , in § 9.1.1
- color dfn for aspect , in § 6.1 dict-member for GPUBlendState , in § 10.3.5
- dfn for aspect , in § 6.1
- dict-member for GPUBlendState , in § 10.3.5
- [[colorAttachments]] , in § 17.1
- colorAttachments , in § 17.1.1
- colorFormats , in § 17.1.1.4
- color renderable format , in § 6.3
- colors , in § 23.2.6
- colorSpace dict-member for GPUCanvasConfiguration , in § 21.4 dict-member for GPUCopyExternalImageDestInfo , in § 11.2.4 dict-member for GPUExternalTextureDescriptor , in § 6.4.1
- dict-member for GPUCanvasConfiguration , in § 21.4
- dict-member for GPUCopyExternalImageDestInfo , in § 11.2.4
- dict-member for GPUExternalTextureDescriptor , in § 6.4.1
- combined depth-stencil format , in § 26.1.2
- [[command_encoder]] attribute for GPUComputePassEncoder , in § 16.1 attribute for GPURenderPassEncoder , in § 17.1
- attribute for GPUComputePassEncoder , in § 16.1
- attribute for GPURenderPassEncoder , in § 17.1
- [[command_list]] attribute for GPUCommandBuffer , in § 12.1 attribute for GPURenderBundle , in § 18.1
- attribute for GPUCommandBuffer , in § 12.1
- attribute for GPURenderBundle , in § 18.1
- [[commands]] , in § 13.1
- compare dict-member for GPUSamplerDescriptor , in § 7.1.1 dict-member for GPUStencilFaceState , in § 10.3.6
- dict-member for GPUSamplerDescriptor , in § 7.1.1
- dict-member for GPUStencilFaceState , in § 10.3.6
- compare fragment , in § 23.2.6
- "comparison" , in § 8.1.1
- "compatibility" , in § 4.2.2
- compatibility mode default , in § 3.6.2
- compatible usage list , in § 3.4.3
- compilationHints , in § 9.1.1
- compressed format , in § 26.1.3
- COMPUTE , in § 8.1.1
- compute (abstract-op) , in § 23.1 dict-member for GPUComputePipelineDescriptor , in § 10.2.1
- (abstract-op) , in § 23.1
- dict-member for GPUComputePipelineDescriptor , in § 10.2.1
- compute render extent , in § 6.1
- [[configuration]] , in § 21.2
- configure(configuration) , in § 21.2
- "constant" , in § 10.3.5.1
- constant , in § 3.4.3
- constants , in § 10.1.2
- constructor() , in § 10
- constructor(message) constructor for GPUInternalError , in § 22.2 constructor for GPUOutOfMemoryError , in § 22.2 constructor for GPUPipelineError , in § 10 constructor for GPUValidationError , in § 22.2
- constructor for GPUInternalError , in § 22.2
- constructor for GPUOutOfMemoryError , in § 22.2
- constructor for GPUPipelineError , in § 10
- constructor for GPUValidationError , in § 22.2
- constructor(message, options) , in § 10
- constructor(type, gpuUncapturedErrorEventInitDict) , in § 22.4
- "consumed" , in § 3.5.1
- contagious invalidity , in § 3.2.1
- [[content device]] , in § 3.5.2
- Content timeline , in § 3.4.1
- Content-timeline example term , in § 3.4.1
- content timeline property , in § 3.1.2
- copyBufferToBuffer() , in § 13.4
- copyBufferToBuffer(source, destination) , in § 13.4
- copyBufferToBuffer(source, destination, size) , in § 13.4
- copyBufferToBuffer(source, sourceOffset, destination, destinationOffset) , in § 13.4
- copyBufferToBuffer(source, sourceOffset, destination, destinationOffset, size) , in § 13.4
- copyBufferToTexture(source, destination, copySize) , in § 13.5
- copy-compatible , in § 11.2.6
- COPY_DST const for GPUBufferUsage , in § 5.1.2 const for GPUTextureUsage , in § 6.1.2
- const for GPUBufferUsage , in § 5.1.2
- const for GPUTextureUsage , in § 6.1.2
- copyExternalImageToTexture(source, destination, copySize) , in § 19.2
- COPY_SRC const for GPUBufferUsage , in § 5.1.2 const for GPUTextureUsage , in § 6.1.2
- const for GPUBufferUsage , in § 5.1.2
- const for GPUTextureUsage , in § 6.1.2
- copyTextureToBuffer(source, destination, copySize) , in § 13.5
- copyTextureToTexture(source, destination, copySize) , in § 13.5
- "core" , in § 4.2.2
- "core-features-and-limits" , in § 25
- count attribute for GPUQuerySet , in § 20.1 dict-member for GPUMultisampleState , in § 10.3.3 dict-member for GPUQuerySetDescriptor , in § 20.1.1
- attribute for GPUQuerySet , in § 20.1
- dict-member for GPUMultisampleState , in § 10.3.3
- dict-member for GPUQuerySetDescriptor , in § 20.1.1
- coverageMask dfn for Fragment , in § 23.2.6 dfn for RasterizationPoint , in § 23.2.5
- dfn for Fragment , in § 23.2.6
- dfn for RasterizationPoint , in § 23.2.5
- create a new WebGPU object , in § 3.1.2
- create a 'webgpu' context on a canvas , in § 21.1
- createBindGroup(descriptor) , in § 8.2.1
- createBindGroupLayout(descriptor) , in § 8.1.1
- createBuffer(descriptor) , in § 5.1.3
- createCommandEncoder() , in § 13.2.1
- createCommandEncoder(descriptor) , in § 13.2.1
- createComputePipelineAsync(descriptor) , in § 10.2.1
- createComputePipeline(descriptor) , in § 10.2.1
- createPipelineLayout(descriptor) , in § 8.3.1
- createQuerySet(descriptor) , in § 20.1.1
- createRenderBundleEncoder(descriptor) , in § 18.1.1
- createRenderPipelineAsync(descriptor) , in § 10.3.1
- createRenderPipeline(descriptor) , in § 10.3.1
- createSampler() , in § 7.1.2
- createSampler(descriptor) , in § 7.1.2
- createShaderModule(descriptor) , in § 9.1.1
- createTexture(descriptor) , in § 6.1.3
- createView() , in § 6.2.1
- createView(descriptor) , in § 6.2.1
- "cube" , in § 6.2.1
- "cube-array" , in § 6.2.1
- cullMode , in § 10.3.2
- current error scope , in § 22.3
- current queue timestamp , in § 20.4
- [[currentTexture]] , in § 21.2
- "cw" , in § 10.3.2
- data , in § 5.1
- [[debug_group_stack]] , in § 15
- "decrement-clamp" , in § 10.3.6
- "decrement-wrap" , in § 10.3.6
- default , in § 3.6.2
- [[default feature level]] , in § 3.5.1
- default pipeline layout , in § 10.1.1
- defaultQueue , in § 4.3.1
- "depth" , in § 8.1.1
- depth dfn for Fragment , in § 23.2.6 dfn for RasterizationPoint , in § 23.2.5 dfn for aspect , in § 6.1
- dfn for Fragment , in § 23.2.6
- dfn for RasterizationPoint , in § 23.2.5
- dfn for aspect , in § 6.1
- "depth16unorm" , in § 6.3
- "depth24plus" , in § 6.3
- "depth24plus-stencil8" , in § 6.3
- "depth32float" , in § 6.3
- "depth32float-stencil8" enum-value for GPUFeatureName , in § 25.2 enum-value for GPUTextureFormat , in § 6.3
- enum-value for GPUFeatureName , in § 25.2
- enum-value for GPUTextureFormat , in § 6.3
- depthBias , in § 10.3.6
- depthBiasClamp , in § 10.3.6
- depthBiasSlopeScale , in § 10.3.6
- depthClearValue , in § 17.1.1.2
- "depth-clip-control" , in § 25.1
- depth clipping , in § 23.2.4
- depthCompare , in § 10.3.6
- depthFailOp , in § 10.3.6
- depthLoadOp , in § 17.1.1.2
- "depth-only" , in § 6.2.1
- depthOrArrayLayers attribute for GPUTexture , in § 6.1 dfn for GPUExtent3D , in § 24.1 dict-member for GPUExtent3DDict , in § 24.1
- attribute for GPUTexture , in § 6.1
- dfn for GPUExtent3D , in § 24.1
- dict-member for GPUExtent3DDict , in § 24.1
- depth-or-stencil format , in § 26.1.2
- depthPassed , in § 23.2.6
- [[depthReadOnly]] attribute for GPURenderBundle , in § 18.1 attribute for GPURenderCommandsMixin , in § 17.2
- attribute for GPURenderBundle , in § 18.1
- attribute for GPURenderCommandsMixin , in § 17.2
- depthReadOnly dict-member for GPURenderBundleEncoderDescriptor , in § 18.1.2 dict-member for GPURenderPassDepthStencilAttachment , in § 17.1.1.2
- dict-member for GPURenderBundleEncoderDescriptor , in § 18.1.2
- dict-member for GPURenderPassDepthStencilAttachment , in § 17.1.1.2
- depthSlice , in § 17.1.1.1
- depthStencil , in § 10.3.1
- [[depthStencilAttachment]] , in § 17.1
- depthStencilAttachment , in § 17.1.1
- depthStencilFormat , in § 17.1.1.4
- depthStoreOp , in § 17.1.1.2
- depthWriteEnabled , in § 10.3.6
- derive render targets layout from pass , in § 17.1.1.4
- derive render targets layout from pipeline , in § 17.1.1.4
- description , in § 3.6.2.4
- [[descriptor]] attribute for GPUBindGroupLayout , in § 8.1 attribute for GPUExternalTexture , in § 6.4 attribute for GPURenderPipeline , in § 10.3 attribute for GPUSampler , in § 7.1 attribute for GPUTextureView , in § 6.2
- attribute for GPUBindGroupLayout , in § 8.1
- attribute for GPUExternalTexture , in § 6.4
- attribute for GPURenderPipeline , in § 10.3
- attribute for GPUSampler , in § 7.1
- attribute for GPUTextureView , in § 6.2
- destination dfn for Fragment , in § 23.2.6 dfn for RasterizationPoint , in § 23.2.5
- dfn for Fragment , in § 23.2.6
- dfn for RasterizationPoint , in § 23.2.5
- destroy() method for GPUBuffer , in § 5.1.4 method for GPUDevice , in § 4.4 method for GPUQuerySet , in § 20.1.2 method for GPUTexture , in § 6.1.4
- method for GPUBuffer , in § 5.1.4
- method for GPUDevice , in § 4.4
- method for GPUQuerySet , in § 20.1.2
- method for GPUTexture , in § 6.1.4
- "destroyed" , in § 22.1
- [[destroyed]] attribute for GPUQuerySet , in § 20.1 attribute for GPUTexture , in § 6.1
- attribute for GPUQuerySet , in § 20.1
- attribute for GPUTexture , in § 6.1
- destroyed , in § 5.1
- [[device]] , in § 3.1.2
- device attribute for GPUAdapterInfo , in § 3.6.2.4 definition of , in § 3.5.2 dict-member for GPUCanvasConfiguration , in § 21.4
- attribute for GPUAdapterInfo , in § 3.6.2.4
- definition of , in § 3.5.2
- dict-member for GPUCanvasConfiguration , in § 21.4
- Device timeline , in § 3.4.1
- Device-timeline example term , in § 3.4.1
- device timeline property , in § 3.1.2
- dimension attribute for GPUTexture , in § 6.1 dict-member for GPUTextureDescriptor , in § 6.1.1 dict-member for GPUTextureViewDescriptor , in § 6.2.1
- attribute for GPUTexture , in § 6.1
- dict-member for GPUTextureDescriptor , in § 6.1.1
- dict-member for GPUTextureViewDescriptor , in § 6.2.1
- "discard" , in § 17.1.1.3
- Dispatch error , in § 22.3
- dispatch error , in § 22.3
- dispatchWorkgroupsIndirect(indirectBuffer, indirectOffset) , in § 16.1.2
- dispatchWorkgroups(workgroupCountX) , in § 16.1.2
- dispatchWorkgroups(workgroupCountX, workgroupCountY) , in § 16.1.2
- dispatchWorkgroups(workgroupCountX, workgroupCountY, workgroupCountZ) , in § 16.1.2
- [[drawCount]] attribute for GPURenderBundle , in § 18.1 attribute for GPURenderCommandsMixin , in § 17.2
- attribute for GPURenderBundle , in § 18.1
- attribute for GPURenderCommandsMixin , in § 17.2
- drawIndexed(indexCount) , in § 17.2.1
- drawIndexed(indexCount, instanceCount) , in § 17.2.1
- drawIndexed(indexCount, instanceCount, firstIndex) , in § 17.2.1
- drawIndexed(indexCount, instanceCount, firstIndex, baseVertex) , in § 17.2.1
- drawIndexed(indexCount, instanceCount, firstIndex, baseVertex, firstInstance) , in § 17.2.1
- drawIndexedIndirect(indirectBuffer, indirectOffset) , in § 17.2.1
- drawIndirect(indirectBuffer, indirectOffset) , in § 17.2.1
- [[drawingBuffer]] , in § 21.2
- draw(vertexCount) , in § 17.2.1
- draw(vertexCount, instanceCount) , in § 17.2.1
- draw(vertexCount, instanceCount, firstVertex) , in § 17.2.1
- draw(vertexCount, instanceCount, firstVertex, firstInstance) , in § 17.2.1
- "dst" , in § 10.3.5.1
- "dst-alpha" , in § 10.3.5.1
- dstFactor , in § 10.3.5.1
- "dual-source-blending" , in § 25.16
- [[dynamicOffsetCount]] , in § 8.1.1
- [[dynamic_offsets]] , in § 14
- "eac-r11snorm" , in § 6.3
- "eac-r11unorm" , in § 6.3
- "eac-rg11snorm" , in § 6.3
- "eac-rg11unorm" , in § 6.3
- effective buffer binding size , in § 8.2.1
- enabled for , in § 3.6.1
- Encoder bind groups alias a writable resource , in § 14.1
- encoder state , in § 13.1
- end() method for GPUComputePassEncoder , in § 16.1.3 method for GPURenderPassEncoder , in § 17.1.2
- method for GPUComputePassEncoder , in § 16.1.3
- method for GPURenderPassEncoder , in § 17.1.2
- ended , in § 13.1
- endOcclusionQuery() , in § 17.2.3
- endOfPassWriteIndex dict-member for GPUComputePassTimestampWrites , in § 16.1.1 dict-member for GPURenderPassTimestampWrites , in § 17.1.1
- dict-member for GPUComputePassTimestampWrites , in § 16.1.1
- dict-member for GPURenderPassTimestampWrites , in § 17.1.1
- [[endTimestampWrite]] attribute for GPUComputePassEncoder , in § 16.1 attribute for GPURenderPassEncoder , in § 17.1
- attribute for GPUComputePassEncoder , in § 16.1
- attribute for GPURenderPassEncoder , in § 17.1
- Enqueue a command , in § 13.1
- Enqueue a render command , in § 17.2
- [[entries]] , in § 8.2
- entries dict-member for GPUBindGroupDescriptor , in § 8.2.1 dict-member for GPUBindGroupLayoutDescriptor , in § 8.1.1
- dict-member for GPUBindGroupDescriptor , in § 8.2.1
- dict-member for GPUBindGroupLayoutDescriptor , in § 8.1.1
- [[entryMap]] , in § 8.1.1
- entryPoint dict-member for GPUProgrammableStage , in § 10.1.2 dict-member for GPUShaderModuleCompilationHint , in § 9.1.1.1
- dict-member for GPUProgrammableStage , in § 10.1.2
- dict-member for GPUShaderModuleCompilationHint , in § 9.1.1.1
- "equal" , in § 7.1.1
- equal , in § 17.1.1.4
- equals , in § 17.1.1.4
- equivalent texel representation , in § 11.2
- "error" , in § 9.1.2
- error attribute for GPUUncapturedErrorEvent , in § 22.4 dict-member for GPUUncapturedErrorEventInit , in § 22.4
- attribute for GPUUncapturedErrorEvent , in § 22.4
- dict-member for GPUUncapturedErrorEventInit , in § 22.4
- [[errors]] , in § 22.3
- [[errorScopeStack]] , in § 22.3
- "etc2-rgb8a1unorm" , in § 6.3
- "etc2-rgb8a1unorm-srgb" , in § 6.3
- "etc2-rgb8unorm" , in § 6.3
- "etc2-rgb8unorm-srgb" , in § 6.3
- "etc2-rgba8unorm" , in § 6.3
- "etc2-rgba8unorm-srgb" , in § 6.3
- exceeds the binding slot limits , in § 8.1.1
- [[exclusivePipeline]] , in § 8.1.1
- executeBundles(bundles) , in § 17.2.4
- Expire , in § 3.5.1
- expire , in § 3.5.1
- "expired" , in § 3.5.1
- [[expired]] , in § 6.4
- expires , in § 3.5.1
- Expire the current texture , in § 21.2
- "extended" , in § 21.5
- external source dimensions , in § 11.2.5
- externalTexture , in § 8.1.1
- failOp , in § 10.3.6
- [[fallback]] , in § 3.5.1
- fallback adapter , in § 3.5.1
- feature , in § 3.6.1
- Feature Detection , in § 3.6.2.4
- featureLevel , in § 4.2.2
- feature level string , in § 4.2.2
- [[features]] attribute for adapter , in § 3.5.1 attribute for device , in § 3.5.2
- attribute for adapter , in § 3.5.1
- attribute for device , in § 3.5.2
- features attribute for GPUAdapter , in § 4.3 attribute for GPUDevice , in § 4.4
- attribute for GPUAdapter , in § 4.3
- attribute for GPUDevice , in § 4.4
- fetch index , in § 23.2.1
- [[filter]] , in § 22.3
- filterable , in § 6.3
- filterable format , in § 6.3
- "filtering" , in § 8.1.1
- final sample mask , in § 23.2.11
- finish() method for GPUCommandEncoder , in § 13.7 method for GPURenderBundleEncoder , in § 18.1.3
- method for GPUCommandEncoder , in § 13.7
- method for GPURenderBundleEncoder , in § 18.1.3
- finish(descriptor) method for GPUCommandEncoder , in § 13.7 method for GPURenderBundleEncoder , in § 18.1.3
- method for GPUCommandEncoder , in § 13.7
- method for GPURenderBundleEncoder , in § 18.1.3
- flipY , in § 11.2.5
- "float" , in § 8.1.1
- "float16" , in § 10.3.7.1
- "float16x2" , in § 10.3.7.1
- "float16x4" , in § 10.3.7.1
- "float32" , in § 10.3.7.1
- "float32-blendable" , in § 25.14
- "float32-filterable" , in § 25.13
- "float32x2" , in § 10.3.7.1
- "float32x3" , in § 10.3.7.1
- "float32x4" , in § 10.3.7.1
- forceFallbackAdapter , in § 4.2.2
- format attribute for GPUTexture , in § 6.1 dict-member for GPUCanvasConfiguration , in § 21.4 dict-member for GPUColorTargetState , in § 10.3.5 dict-member for GPUDepthStencilState , in § 10.3.6 dict-member for GPUStorageTextureBindingLayout , in § 8.1.1 dict-member for GPUTextureDescriptor , in § 6.1.1 dict-member for GPUTextureViewDescriptor , in § 6.2.1 dict-member for GPUVertexAttribute , in § 10.3.7.1
- attribute for GPUTexture , in § 6.1
- dict-member for GPUCanvasConfiguration , in § 21.4
- dict-member for GPUColorTargetState , in § 10.3.5
- dict-member for GPUDepthStencilState , in § 10.3.6
- dict-member for GPUStorageTextureBindingLayout , in § 8.1.1
- dict-member for GPUTextureDescriptor , in § 6.1.1
- dict-member for GPUTextureViewDescriptor , in § 6.2.1
- dict-member for GPUVertexAttribute , in § 10.3.7.1
- FRAGMENT , in § 8.1.1
- Fragment , in § 23.2.6
- fragment , in § 10.3.1
- Fragment coordinates , in § 3.3
- FragmentDestination , in § 23.2.5
- framebuffer , in § 23.2.5
- Framebuffer coordinates , in § 3.3
- framebuffer memory , in § 17.1
- "front" , in § 10.3.2
- frontFace , in § 10.3.2
- front-facing , in § 23.2.5.4
- frontFacing dfn for Fragment , in § 23.2.6 dfn for RasterizationPoint , in § 23.2.5
- dfn for Fragment , in § 23.2.6
- dfn for RasterizationPoint , in § 23.2.5
- g dfn for GPUColor , in § 24.1 dict-member for GPUColorDict , in § 24.1
- dfn for GPUColor , in § 24.1
- dict-member for GPUColorDict , in § 24.1
- Generate an internal error , in § 22.2
- generate an internal error , in § 22.2
- Generate an out-of-memory error , in § 22.2
- generate an out-of-memory error , in § 22.2
- Generate a validation error , in § 22.2
- generate a validation error , in § 22.2
- get a copy of the image contents of a context , in § 21.2
- get as buffer binding , in § 8.2.1
- get as texture view , in § 8.2.1
- getBindGroupLayout(index) , in § 10.1
- getCompilationInfo() , in § 9.1.2
- getConfiguration() , in § 21.2
- getCurrentTexture() , in § 21.2
- getMappedRange() , in § 5.2
- getMappedRange(offset) , in § 5.2
- getMappedRange(offset, size) , in § 5.2
- getPreferredCanvasFormat() , in § 4.2
- get the entry point , in § 10.1.2
- GPU , in § 4.2
- gpu , in § 4.1
- GPUAdapter , in § 4.2.2
- GPUAdapterInfo , in § 3.6.2.3
- GPUAddressMode , in § 7.1.1
- GPUAutoLayoutMode , in § 10.1
- GPUBindGroup , in § 8.1.2
- GPUBindGroupDescriptor , in § 8.2.1
- GPUBindGroupEntry , in § 8.2.1
- GPUBindGroupLayout , in § 8
- GPUBindGroupLayoutDescriptor , in § 8.1.1
- GPUBindGroupLayoutEntry , in § 8.1.1
- GPUBindingCommandsMixin , in § 14
- GPUBindingResource , in § 8.2.1
- GPUBlendComponent , in § 10.3.5.1
- GPUBlendFactor , in § 10.3.5.1
- GPUBlendOperation , in § 10.3.5.1
- GPUBlendState , in § 10.3.5
- GPUBuffer , in § 5
- GPUBufferBinding , in § 8.2.1
- GPUBufferBindingLayout , in § 8.1.1
- GPUBufferBindingType , in § 8.1.1
- GPUBufferDescriptor , in § 5.1
- GPUBufferDynamicOffset , in § 24
- GPUBufferMapState , in § 5.1
- GPUBufferUsage , in § 5.1.2
- GPUBufferUsageFlags , in § 5.1.2
- GPUCanvasAlphaMode , in § 21.5
- GPUCanvasConfiguration , in § 21.4
- GPUCanvasContext , in § 21.2
- GPUCanvasToneMapping , in § 21.4
- GPUCanvasToneMappingMode , in § 21.4.2
- GPUColor , in § 24.1
- GPUColorDict , in § 24.1
- GPUColorTargetState , in § 10.3.5
- GPUColorWrite , in § 10.3.5
- GPUColorWriteFlags , in § 10.3.5
- GPU command , in § 12
- GPUCommandBuffer , in § 12
- GPUCommandBufferDescriptor , in § 12.1.1
- GPUCommandEncoder , in § 13.1
- GPUCommandEncoderDescriptor , in § 13.2.1
- GPUCommandsMixin , in § 13
- GPUCompareFunction , in § 7.1.1
- GPUCompilationInfo , in § 9.1.2
- GPUCompilationMessage , in § 9.1.2
- GPUCompilationMessageType , in § 9.1.2
- GPUComputePassDescriptor , in § 16.1.1
- GPUComputePassEncoder , in § 16
- GPUComputePassTimestampWrites , in § 16.1.1
- GPUComputePipeline , in § 10.1.2
- GPUComputePipelineDescriptor , in § 10.2.1
- GPUCopyExternalImageDestInfo , in § 11.2.3
- GPUCopyExternalImageSource , in § 11.2.5
- GPUCopyExternalImageSourceInfo , in § 11.2.4
- GPUCullMode , in § 10.3.2
- GPUDebugCommandsMixin , in § 15
- GPUDepthBias , in § 24
- GPUDepthStencilState , in § 10.3.6
- GPUDevice , in § 4.3.1.1
- GPUDeviceDescriptor , in § 4.3
- GPUDeviceLostInfo , in § 22.1
- GPUDeviceLostReason , in § 22.1
- GPUError , in § 22.1
- GPUErrorFilter , in § 22.3
- GPU error scope , in § 22.3
- GPUExtent3D , in § 24.1
- GPUExtent3DDict , in § 24.1
- GPUExternalTexture , in § 6.3
- GPUExternalTextureBindingLayout , in § 8.1.1
- GPUExternalTextureDescriptor , in § 6.4.1
- GPUFeatureName , in § 4.3.1
- GPUFilterMode , in § 7.1.1
- GPUFlagsConstant , in § 24
- GPUFragmentState , in § 10.3.4
- GPUFrontFace , in § 10.3.2
- GPUIndex32 , in § 24
- GPUIndexFormat , in § 10.3.7
- GPUIntegerCoordinate , in § 24
- GPUIntegerCoordinateOut , in § 24
- GPUInternalError , in § 22.2
- GPUInternalError(message) , in § 22.2
- GPULoadOp , in § 17.1.1.3
- GPUMapMode , in § 5.2
- GPUMapModeFlags , in § 5.2
- GPUMipmapFilterMode , in § 7.1.1
- GPUMultisampleState , in § 10.3.3
- GPUObjectBase , in § 3.1.2
- GPUObjectDescriptorBase , in § 3.1.3
- GPUOrigin2D , in § 24.1
- GPUOrigin2DDict , in § 24.1
- GPUOrigin3D , in § 24.1
- GPUOrigin3DDict , in § 24.1
- GPUOutOfMemoryError , in § 22.2
- GPUOutOfMemoryError(message) , in § 22.2
- GPUPipelineBase , in § 10.1
- GPUPipelineConstantValue , in § 10.1.2
- GPUPipelineDescriptorBase , in § 10.1
- GPUPipelineError , in § 10
- GPUPipelineError() , in § 10
- GPUPipelineErrorInit , in § 10
- GPUPipelineError(message) , in § 10
- GPUPipelineError(message, options) , in § 10
- GPUPipelineErrorReason , in § 10
- GPUPipelineLayout , in § 8.2.1
- GPUPipelineLayoutDescriptor , in § 8.3.1
- GPUPowerPreference , in § 4.2.2
- GPUPrimitiveState , in § 10.3.2
- GPUPrimitiveTopology , in § 10.3.2
- GPUProgrammableStage , in § 10.1.1
- GPUQuerySet , in § 20
- GPUQuerySetDescriptor , in § 20.1.1
- GPUQueryType , in § 20.2
- GPUQueue , in § 19.1
- GPUQueueDescriptor , in § 19
- GPURenderBundle , in § 18
- GPURenderBundleDescriptor , in § 18.1.1
- GPURenderBundleEncoder , in § 18.1.1
- GPURenderBundleEncoderDescriptor , in § 18.1.2
- GPURenderCommandsMixin , in § 17.1.2
- GPURenderPassColorAttachment , in § 17.1.1.1
- GPURenderPassColorAttachment Valid Usage , in § 17.1.1.1
- GPURenderPassDepthStencilAttachment , in § 17.1.1.2
- GPURenderPassDepthStencilAttachment Valid Usage , in § 17.1.1.2
- GPURenderPassDescriptor , in § 17.1.1
- GPURenderPassEncoder , in § 17
- GPURenderPassLayout , in § 17.1.1.4
- GPURenderPassTimestampWrites , in § 17.1.1
- GPURenderPipeline , in § 10.2.1
- GPURenderPipelineDescriptor , in § 10.3.1
- GPURequestAdapterOptions , in § 4.2.2
- GPUSampleMask , in § 24
- GPUSampler , in § 7
- GPUSamplerBindingLayout , in § 8.1.1
- GPUSamplerBindingType , in § 8.1.1
- GPUSamplerDescriptor , in § 7.1.1
- GPUShaderModule , in § 9
- GPUShaderModuleCompilationHint , in § 9.1.1.1
- GPUShaderModuleDescriptor , in § 9.1.1
- GPUShaderStage , in § 8.1.1
- GPUShaderStageFlags , in § 8.1.1
- GPUSignedOffset32 , in § 24
- GPUSize32 , in § 24
- GPUSize32Out , in § 24
- GPUSize64 , in § 24
- GPUSize64Out , in § 24
- GPUStencilFaceState , in § 10.3.6
- GPUStencilOperation , in § 10.3.6
- GPUStencilValue , in § 24
- GPUStorageTextureAccess , in § 8.1.1
- GPUStorageTextureBindingLayout , in § 8.1.1
- GPUStoreOp , in § 17.1.1.3
- GPUSupportedFeatures , in § 3.6.2.1
- GPUSupportedLimits , in § 3.6.2
- GPUTexelCopyBufferInfo , in § 11.2.1
- GPUTexelCopyBufferLayout , in § 11.2
- GPUTexelCopyTextureInfo , in § 11.2.2
- GPUTexelCopyTextureInfo physical subresource size , in § 11.2.6
- GPUTexture , in § 6
- GPUTextureAspect , in § 6.2.1
- GPUTextureBindingLayout , in § 8.1.1
- GPUTextureDescriptor , in § 6.1
- GPUTextureDescriptor for the canvas and configuration , in § 21.4
- GPUTextureDimension , in § 6.1.1
- GPUTextureFormat , in § 6.3
- GPUTextureSampleType , in § 8.1.1
- GPUTextureUsage , in § 6.1.2
- GPUTextureUsageFlags , in § 6.1.2
- GPUTextureView , in § 6.1.4
- GPUTextureViewDescriptor , in § 6.2.1
- GPUTextureViewDimension , in § 6.2.1
- GPUUncapturedErrorEvent , in § 22.4
- GPUUncapturedErrorEventInit , in § 22.4
- GPUUncapturedErrorEvent(type, gpuUncapturedErrorEventInitDict) , in § 22.4
- GPUValidationError , in § 22.2
- GPUValidationError(message) , in § 22.2
- GPUVertexAttribute , in § 10.3.7.1
- GPUVertexBufferLayout , in § 10.3.7.1
- GPUVertexFormat , in § 10.3.7.1
- GPUVertexState , in § 10.3.7.1
- GPUVertexStepMode , in § 10.3.7.1
- "greater" , in § 7.1.1
- "greater-equal" , in § 7.1.1
- GREEN , in § 10.3.5
- group-equivalent , in § 8.1.2
- hasDynamicOffset , in § 8.1.1
- height attribute for GPUTexture , in § 6.1 dfn for GPUExtent3D , in § 24.1 dict-member for GPUExtent3DDict , in § 24.1
- attribute for GPUTexture , in § 6.1
- dfn for GPUExtent3D , in § 24.1
- dict-member for GPUExtent3DDict , in § 24.1
- "high-performance" , in § 4.2.2
- immediate pipeline creation , in § 10
- immutable property , in § 3.1.2
- Immutable value example term , in § 3.4.1
- importExternalTexture(descriptor) , in § 6.4.1
- "increment-clamp" , in § 10.3.6
- "increment-wrap" , in § 10.3.6
- INDEX , in § 5.1.2
- [[index_buffer]] , in § 17.2
- [[index_buffer_offset]] , in § 17.2
- [[index_buffer_size]] , in § 17.2
- [[index_format]] , in § 17.2
- INDIRECT , in § 5.1.2
- indirect dispatch parameters , in § 16.1.2
- indirect drawIndexed parameters , in § 17.2.1
- indirect draw parameters , in § 17.2.1
- "indirect-first-instance" , in § 25.9
- "info" , in § 9.1.2
- info , in § 4.3
- initialize an active buffer mapping , in § 5.1
- input , in § 3.4.3
- insertDebugMarker(markerLabel) , in § 15
- "instance" , in § 10.3.7.1
- "internal" enum-value for GPUErrorFilter , in § 22.3 enum-value for GPUPipelineErrorReason , in § 10
- enum-value for GPUErrorFilter , in § 22.3
- enum-value for GPUPipelineErrorReason , in § 10
- internal error , in § 22.2
- internal object , in § 3.1.2
- [[internal state]] , in § 5.1
- internal usage , in § 3.4.3
- Inter-Stage Builtins , in § 10.3.1
- invalid , in § 3.2.1
- Invalidate , in § 3.2.1
- invalidate , in § 3.2.1
- invalidated , in § 3.2.1
- invalidates , in § 3.2.1
- "invert" , in § 10.3.6
- [[isComparison]] , in § 7.1
- isFallbackAdapter , in § 3.6.2.4
- [[isFiltering]] , in § 7.1
- Iterate over each dynamic binding offset , in § 14.1
- "keep" , in § 10.3.6
- label attribute for GPUObjectBase , in § 3.1.2 dict-member for GPUObjectDescriptorBase , in § 3.1.3
- attribute for GPUObjectBase , in § 3.1.2
- dict-member for GPUObjectDescriptorBase , in § 3.1.3
- [[lastPresentedImage]] , in § 21.2
- [[layout]] attribute for GPUBindGroup , in § 8.2 attribute for GPUPipelineBase , in § 10.1 attribute for GPURenderBundle , in § 18.1 attribute for GPURenderCommandsMixin , in § 17.2
- attribute for GPUBindGroup , in § 8.2
- attribute for GPUPipelineBase , in § 10.1
- attribute for GPURenderBundle , in § 18.1
- attribute for GPURenderCommandsMixin , in § 17.2
- layout dict-member for GPUBindGroupDescriptor , in § 8.2.1 dict-member for GPUPipelineDescriptorBase , in § 10.1 dict-member for GPUShaderModuleCompilationHint , in § 9.1.1.1
- dict-member for GPUBindGroupDescriptor , in § 8.2.1
- dict-member for GPUPipelineDescriptorBase , in § 10.1
- dict-member for GPUShaderModuleCompilationHint , in § 9.1.1.1
- length , in § 9.1.2
- "less" , in § 7.1.1
- "less-equal" , in § 7.1.1
- levels of detail , in § 7.1.1
- limit , in § 3.6.2
- limit class , in § 3.6.2
- [[limits]] attribute for adapter , in § 3.5.1 attribute for device , in § 3.5.2
- attribute for adapter , in § 3.5.1
- attribute for device , in § 3.5.2
- limits attribute for GPUAdapter , in § 4.3 attribute for GPUDevice , in § 4.4
- attribute for GPUAdapter , in § 4.3
- attribute for GPUDevice , in § 4.4
- "linear" enum-value for GPUFilterMode , in § 7.1.1 enum-value for GPUMipmapFilterMode , in § 7.1.1
- enum-value for GPUFilterMode , in § 7.1.1
- enum-value for GPUMipmapFilterMode , in § 7.1.1
- "line-list" , in § 10.3.2
- lineNum , in § 9.1.2
- linePos , in § 9.1.2
- "line-strip" , in § 10.3.2
- Listen for timeline event , in § 3.5.2
- "load" , in § 17.1.1.3
- loadOp , in § 17.1.1.1
- locked , in § 13.1
- lod , in § 7.1.1
- lodMaxClamp , in § 7.1.1
- lodMinClamp , in § 7.1.1
- Logical miplevel-specific texture extent , in § 6.1
- logical miplevel-specific texture extent , in § 6.1
- lose the device , in § 3.5.2
- lost , in § 22.1
- "low-power" , in § 4.2.2
- magFilter , in § 7.1.1
- mapAsync(mode) , in § 5.2
- mapAsync(mode, offset) , in § 5.2
- mapAsync(mode, offset, size) , in § 5.2
- "mapped" , in § 5.1
- mappedAtCreation , in § 5.1.1
- [[mapping]] , in § 5.1
- MAP_READ , in § 5.1.2
- mapState , in § 5.1
- MAP_WRITE , in § 5.1.2
- mask , in § 10.3.3
- "max" , in § 10.3.5.1
- maxAnisotropy , in § 7.1.1
- maxBindGroups attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxBindGroupsPlusVertexBuffers attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxBindingsPerBindGroup attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- max bindings per shader stage , in § 4.2.1
- maxBufferSize attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxColorAttachmentBytesPerSample attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxColorAttachments attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxComputeInvocationsPerWorkgroup attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxComputeWorkgroupSizeX attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxComputeWorkgroupSizeY attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxComputeWorkgroupSizeZ attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxComputeWorkgroupsPerDimension attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxComputeWorkgroupStorageSize attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- [[maxDrawCount]] , in § 17.1
- maxDrawCount , in § 17.1.1
- maxDynamicStorageBuffersPerPipelineLayout attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxDynamicUniformBuffersPerPipelineLayout attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maximum , in § 3.6.2
- maximum mipLevel count , in § 6.1.2
- maxInterStageShaderVariables attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxSampledTexturesPerShaderStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxSamplersPerShaderStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- max shader stages per pipeline , in § 4.2.1
- maxStorageBufferBindingSize attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxStorageBuffersInFragmentStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxStorageBuffersInVertexStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxStorageBuffersPerShaderStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxStorageTexturesInFragmentStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxStorageTexturesInVertexStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxStorageTexturesPerShaderStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxTextureArrayLayers attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxTextureDimension1D attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxTextureDimension2D attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxTextureDimension3D attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxUniformBufferBindingSize attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxUniformBuffersPerShaderStage attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxVertexAttributes attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxVertexBufferArrayStride attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- maxVertexBuffers attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- Merge , in § 3.4.4
- merge , in § 3.4.4
- message attribute for GPUCompilationMessage , in § 9.1.2 attribute for GPUDeviceLostInfo , in § 22.1 attribute for GPUError , in § 22.2
- attribute for GPUCompilationMessage , in § 9.1.2
- attribute for GPUDeviceLostInfo , in § 22.1
- attribute for GPUError , in § 22.2
- messages , in § 9.1.2
- "min" , in § 10.3.5.1
- minBindingSize , in § 8.1.1
- minFilter , in § 7.1.1
- minimum buffer binding size , in § 10.1.2
- minStorageBufferOffsetAlignment attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- minUniformBufferOffsetAlignment attribute for GPUSupportedLimits , in § 3.6.2.1 attribute for supported limits , in § 3.6.2
- attribute for GPUSupportedLimits , in § 3.6.2.1
- attribute for supported limits , in § 3.6.2
- mipLevel , in § 11.2.3
- mipLevelCount attribute for GPUTexture , in § 6.1 dict-member for GPUTextureDescriptor , in § 6.1.1 dict-member for GPUTextureViewDescriptor , in § 6.2.1
- attribute for GPUTexture , in § 6.1
- dict-member for GPUTextureDescriptor , in § 6.1.1
- dict-member for GPUTextureViewDescriptor , in § 6.2.1
- mipmapFilter , in § 7.1.1
- mipmap level , in § 6.1
- "mirror-repeat" , in § 7.1.1
- mode dfn for active buffer mapping , in § 5.1 dict-member for GPUCanvasToneMapping , in § 21.4
- dfn for active buffer mapping , in § 5.1
- dict-member for GPUCanvasToneMapping , in § 21.4
- module , in § 10.1.2
- multisample , in § 10.3.1
- multisampled , in § 8.1.1
- NavigatorGPU , in § 4.1
- NDC , in § 3.3
- "nearest" enum-value for GPUFilterMode , in § 7.1.1 enum-value for GPUMipmapFilterMode , in § 7.1.1
- enum-value for GPUFilterMode , in § 7.1.1
- enum-value for GPUMipmapFilterMode , in § 7.1.1
- "never" , in § 7.1.1
- new adapter info , in § 3.6.2.4
- "none" , in § 10.3.2
- "non-filtering" , in § 8.1.1
- normalized identifier string , in § 3.6.2.4
- "not-equal" , in § 7.1.1
- object descriptor , in § 3.1.3
- "occlusion" , in § 20.2
- [[occlusion_query_active]] , in § 17.1
- [[occlusionQueryIndex]] , in § 17.1
- [[occlusion_query_set]] , in § 17.1
- occlusionQuerySet , in § 17.1.1
- offset attribute for GPUCompilationMessage , in § 9.1.2 dict-member for GPUBufferBinding , in § 8.2.1 dict-member for GPUTexelCopyBufferLayout , in § 11.2.1 dict-member for GPUVertexAttribute , in § 10.3.7.1
- attribute for GPUCompilationMessage , in § 9.1.2
- dict-member for GPUBufferBinding , in § 8.2.1
- dict-member for GPUTexelCopyBufferLayout , in § 11.2.1
- dict-member for GPUVertexAttribute , in § 10.3.7.1
- "one" , in § 10.3.5.1
- "one-minus-constant" , in § 10.3.5.1
- "one-minus-dst" , in § 10.3.5.1
- "one-minus-dst-alpha" , in § 10.3.5.1
- "one-minus-src" , in § 10.3.5.1
- "one-minus-src1" , in § 10.3.5.1
- "one-minus-src1-alpha" , in § 10.3.5.1
- "one-minus-src-alpha" , in § 10.3.5.1
- onSubmittedWorkDone() , in § 19.2
- onuncapturederror , in § 22.4
- "opaque" , in § 21.6
- open , in § 13.1
- operation , in § 10.3.5.1
- optional API surface , in § 3.6.1
[LINK: optional API surface](#optional-api-surface)
- origin dict-member for GPUCopyExternalImageSourceInfo , in § 11.2.5 dict-member for GPUTexelCopyTextureInfo , in § 11.2.3
- dict-member for GPUCopyExternalImageSourceInfo , in § 11.2.5
- dict-member for GPUTexelCopyTextureInfo , in § 11.2.3
- out-of-gamut premultiplied RGBA value , in § 3.11
- "out-of-memory" , in § 22.3
- out-of-memory error , in § 22.2
- passOp , in § 10.3.6
- "pending" , in § 5.1
- [[pending_map]] , in § 5.1
- perspectiveDivisor , in § 23.2.5
- Physical miplevel-specific texture extent , in § 6.1
- physical miplevel-specific texture extent , in § 6.1
- physical resources , in § 1
- [[pipeline]] attribute for GPUComputePassEncoder , in § 16.1 attribute for GPURenderCommandsMixin , in § 17.2
- attribute for GPUComputePassEncoder , in § 16.1
- attribute for GPURenderCommandsMixin , in § 17.2
- pipeline , in § 10
- "point-list" , in § 10.3.2
- popDebugGroup() , in § 15
- popErrorScope() , in § 22.3
- position , in § 23.2.5
- powerPreference , in § 4.2.2
- "premultiplied" , in § 21.6
- premultipliedAlpha , in § 11.2.4
- present coordinates , in § 3.3
- [[prevalidatedSize]] , in § 8.2.1
- primitive , in § 10.3.1
- "primitive-index" , in § 25.20
- primitive restart value , in § 10.3.7
- primitiveVertices , in § 23.2.5
- process color attachments , in § 23.2.7
- process depth stencil , in § 23.2.7
- process fragment , in § 23.2.6
- process vertices , in § 23.2.2
- provoking vertex , in § 23.2.4
- pushDebugGroup(groupLabel) , in § 15
- pushErrorScope(filter) , in § 22.3
- QUERY_RESOLVE , in § 5.1.2
- querySet dict-member for GPUComputePassTimestampWrites , in § 16.1.1 dict-member for GPURenderPassTimestampWrites , in § 17.1.1
- dict-member for GPUComputePassTimestampWrites , in § 16.1.1
- dict-member for GPURenderPassTimestampWrites , in § 17.1.1
- queue , in § 4.4
- queue a global task for GPUDevice , in § 3.10.1
- queue an automatic expiry task , in § 3.10.2
- Queue timeline , in § 3.4.1
- Queue-timeline example term , in § 3.4.1
- queue timeline property , in § 3.1.2
- r dfn for GPUColor , in § 24.1 dict-member for GPUColorDict , in § 24.1
- dfn for GPUColor , in § 24.1
- dict-member for GPUColorDict , in § 24.1
- "r16float" , in § 6.3
- "r16sint" , in § 6.3
- "r16snorm" , in § 6.3
- "r16uint" , in § 6.3
- "r16unorm" , in § 6.3
- "r32float" , in § 6.3
- "r32sint" , in § 6.3
- "r32uint" , in § 6.3
- "r8sint" , in § 6.3
- "r8snorm" , in § 6.3
- "r8uint" , in § 6.3
- "r8unorm" , in § 6.3
- range , in § 5.1
- rasterization mask , in § 23.2.11
- RasterizationPoint , in § 23.2.5
- rasterize , in § 23.2.5
- rasterize polygon , in § 23.2.5.4
- READ , in § 5.2
- "read-only" , in § 8.1.1
- read-only depth-stencil , in § 3.4.3
- "read-only-storage" , in § 8.1.1
- "read-write" , in § 8.1.1
- reason attribute for GPUDeviceLostInfo , in § 22.1 attribute for GPUPipelineError , in § 10 dict-member for GPUPipelineErrorInit , in § 10
- attribute for GPUDeviceLostInfo , in § 22.1
- attribute for GPUPipelineError , in § 10
- dict-member for GPUPipelineErrorInit , in § 10
- RED , in § 10.3.5
- render , in § 23.2
- renderable , in § 6.3
- renderable format , in § 6.3
- renderable texture view , in § 17.1.1.1
- RENDER_ATTACHMENT , in § 6.1.2
- [[renderExtent]] , in § 6.2
- render stages , in § 10.3
- [[renderState]] , in § 12.1
- RenderState , in § 17.1
- render target component alignment , in § 26.1.1
- render target pixel byte cost , in § 26.1.1
- "repeat" , in § 7.1.1
- "replace" , in § 10.3.6
- Replace the drawing buffer , in § 21.2
- requestAdapter() , in § 4.2
- requestAdapter(options) , in § 4.2
- requestDevice() , in § 4.3
- requestDevice(descriptor) , in § 4.3
- requiredFeatures , in § 4.3.1
- requiredLimits , in § 4.3.1
- Reset the render pass binding state , in § 17.2.4
- resolve indices , in § 23.2.1
- resolveQuerySet(querySet, firstQuery, queryCount, destination, destinationOffset) , in § 13.6
- resolveTarget , in § 17.1.1.1
- resolving GPUTextureAspect , in § 6.3
- resolving GPUTextureViewDescriptor defaults , in § 6.2.1
- resource , in § 8.2.1
- "reverse-subtract" , in § 10.3.5.1
- "rg11b10ufloat" , in § 6.3
- "rg11b10ufloat-renderable" , in § 25.11
- "rg16float" , in § 6.3
- "rg16sint" , in § 6.3
- "rg16snorm" , in § 6.3
- "rg16uint" , in § 6.3
- "rg16unorm" , in § 6.3
- "rg32float" , in § 6.3
- "rg32sint" , in § 6.3
- "rg32uint" , in § 6.3
- "rg8sint" , in § 6.3
- "rg8snorm" , in § 6.3
- "rg8uint" , in § 6.3
- "rg8unorm" , in § 6.3
- "rgb10a2uint" , in § 6.3
- "rgb10a2unorm" , in § 6.3
- "rgb9e5ufloat" , in § 6.3
- "rgba16float" , in § 6.3
- "rgba16sint" , in § 6.3
- "rgba16snorm" , in § 6.3
- "rgba16uint" , in § 6.3
- "rgba16unorm" , in § 6.3
- "rgba32float" , in § 6.3
- "rgba32sint" , in § 6.3
- "rgba32uint" , in § 6.3
- "rgba8sint" , in § 6.3
- "rgba8snorm" , in § 6.3
- "rgba8uint" , in § 6.3
- "rgba8unorm" , in § 6.3
- "rgba8unorm-srgb" , in § 6.3
- rowsPerImage , in § 11.2.1
- sampleCount attribute for GPUTexture , in § 6.1 dict-member for GPURenderPassLayout , in § 17.1.1.4 dict-member for GPUTextureDescriptor , in § 6.1.1
- attribute for GPUTexture , in § 6.1
- dict-member for GPURenderPassLayout , in § 17.1.1.4
- dict-member for GPUTextureDescriptor , in § 6.1.1
- sampleIndex , in § 23.2.5
- sampler , in § 8.1.1
- sampleType , in § 8.1.1
- [[scissorRect]] , in § 17.1
- setBindGroup() , in § 14.1
- setBindGroup(index, bindGroup) , in § 14.1
- setBindGroup(index, bindGroup, dynamicOffsets) , in § 14.1
- setBindGroup(index, bindGroup, dynamicOffsetsData, dynamicOffsetsDataStart, dynamicOffsetsDataLength) , in § 14.1
- setBlendConstant(color) , in § 17.2.2
- setIndexBuffer(buffer, indexFormat) , in § 17.2.1
- setIndexBuffer(buffer, indexFormat, offset) , in § 17.2.1
- setIndexBuffer(buffer, indexFormat, offset, size) , in § 17.2.1
- set of aspects , in § 6.2.1
- set of subresources for texture copy , in § 11.2.6
- setPipeline(pipeline) method for GPUComputePassEncoder , in § 16.1.2 method for GPURenderCommandsMixin , in § 17.2.1
- method for GPUComputePassEncoder , in § 16.1.2
- method for GPURenderCommandsMixin , in § 17.2.1
- setScissorRect(x, y, width, height) , in § 17.2.2
- setStencilReference(reference) , in § 17.2.2
- setVertexBuffer(slot, buffer) , in § 17.2.1
- setVertexBuffer(slot, buffer, offset) , in § 17.2.1
- setVertexBuffer(slot, buffer, offset, size) , in § 17.2.1
- setViewport(x, y, width, height, minDepth, maxDepth) , in § 17.2.2
- "shader-f16" , in § 25.10
- shaderLocation , in § 10.3.7.1
- shader-output mask , in § 23.2.11
- shaders , in § 1
- "sint" , in § 8.1.1
- "sint16" , in § 10.3.7.1
- "sint16x2" , in § 10.3.7.1
- "sint16x4" , in § 10.3.7.1
- "sint32" , in § 10.3.7.1
- "sint32x2" , in § 10.3.7.1
- "sint32x3" , in § 10.3.7.1
- "sint32x4" , in § 10.3.7.1
- "sint8" , in § 10.3.7.1
- "sint8x2" , in § 10.3.7.1
- "sint8x4" , in § 10.3.7.1
- size attribute for GPUBuffer , in § 5.1 dict-member for GPUBufferBinding , in § 8.2.1 dict-member for GPUBufferDescriptor , in § 5.1.1 dict-member for GPUTextureDescriptor , in § 6.1.1
- attribute for GPUBuffer , in § 5.1
- dict-member for GPUBufferBinding , in § 8.2.1
- dict-member for GPUBufferDescriptor , in § 5.1.1
- dict-member for GPUTextureDescriptor , in § 6.1.1
- slice , in § 6.1
- slot-backed attribute , in § 3.1.1
- "snorm16" , in § 10.3.7.1
- "snorm16x2" , in § 10.3.7.1
- "snorm16x4" , in § 10.3.7.1
- "snorm8" , in § 10.3.7.1
- "snorm8x2" , in § 10.3.7.1
- "snorm8x4" , in § 10.3.7.1
- source dict-member for GPUCopyExternalImageSourceInfo , in § 11.2.5 dict-member for GPUExternalTextureDescriptor , in § 6.4.1
- dict-member for GPUCopyExternalImageSourceInfo , in § 11.2.5
- dict-member for GPUExternalTextureDescriptor , in § 6.4.1
- "src" , in § 10.3.5.1
- "src1" , in § 10.3.5.1
- "src1-alpha" , in § 10.3.5.1
- "src-alpha" , in § 10.3.5.1
- "src-alpha-saturated" , in § 10.3.5.1
- srcFactor , in § 10.3.5.1
- "standard" , in § 21.5
- standard sample patterns , in § 23.2.5
- [[state]] attribute for GPUCommandsMixin , in § 13.1 attribute for adapter , in § 3.5.1
- attribute for GPUCommandsMixin , in § 13.1
- attribute for adapter , in § 3.5.1
- statically used , in § 10.1.2
- static use , in § 10.1.2
- stencil , in § 6.1
- "stencil8" , in § 6.3
- stencilBack , in § 10.3.6
- stencilClearValue , in § 17.1.1.2
- stencilFront , in § 10.3.6
- stencilLoadOp , in § 17.1.1.2
- "stencil-only" , in § 6.2.1
- stencilPassed , in § 23.2.6
- stencilReadMask , in § 10.3.6
- [[stencilReadOnly]] attribute for GPURenderBundle , in § 18.1 attribute for GPURenderCommandsMixin , in § 17.2
- attribute for GPURenderBundle , in § 18.1
- attribute for GPURenderCommandsMixin , in § 17.2
- stencilReadOnly dict-member for GPURenderBundleEncoderDescriptor , in § 18.1.2 dict-member for GPURenderPassDepthStencilAttachment , in § 17.1.1.2
- dict-member for GPURenderBundleEncoderDescriptor , in § 18.1.2
- dict-member for GPURenderPassDepthStencilAttachment , in § 17.1.1.2
- [[stencilReference]] , in § 17.1
- stencilStoreOp , in § 17.1.1.2
- stencilWriteMask , in § 10.3.6
- stepMode , in § 10.3.7.1
- "storage" , in § 8.1.1
- STORAGE , in § 5.1.2
- storage , in § 3.4.3
- STORAGE_BINDING , in § 6.1.2
- storage-read , in § 3.4.3
- storageTexture , in § 8.1.1
- "store" , in § 17.1.1.3
- storeOp , in § 17.1.1.1
- stripIndexFormat , in § 10.3.2
- subgroupMaxSize , in § 3.6.2.4
- subgroupMinSize , in § 3.6.2.4
- "subgroups" , in § 25.17
- submit(commandBuffers) , in § 19.2
- subresource , in § 3.4.3
- subresources , in § 6.2
- "subtract" , in § 10.3.5.1
- supported context formats , in § 21.4
- supported limits , in § 3.6.2
- swizzle , in § 6.2.1
- targets , in § 10.3.4
- texel block , in § 6.3
- texel block byte offset , in § 11.2.3
- texel block copy footprint , in § 6.3
- texel block height , in § 6.3
- texel block memory cost , in § 6.3
- texel block row , in § 11.2.1
- texel block width , in § 6.3
- Texel copy , in § 11.2
- texel image , in § 11.2.1
- [[texture]] , in § 6.2
- texture definition of , in § 6.1 dict-member for GPUBindGroupLayoutEntry , in § 8.1.1 dict-member for GPUTexelCopyTextureInfo , in § 11.2.3
- definition of , in § 6.1
- dict-member for GPUBindGroupLayoutEntry , in § 8.1.1
- dict-member for GPUTexelCopyTextureInfo , in § 11.2.3
- TEXTURE_BINDING , in § 6.1.2
- textureBindingViewDimension attribute for GPUTexture , in § 6.1 dict-member for GPUTextureDescriptor , in § 6.1.1
- attribute for GPUTexture , in § 6.1
- dict-member for GPUTextureDescriptor , in § 6.1.1
- "texture-component-swizzle" , in § 25.21
- "texture-compression-astc" , in § 25.6
- "texture-compression-astc-sliced-3d" , in § 25.7
- "texture-compression-bc" , in § 25.3
- "texture-compression-bc-sliced-3d" , in § 25.4
- "texture-compression-etc2" , in § 25.5
- Texture coordinates , in § 3.3
- texture copy sub-region , in § 11.2.3
- [[textureDescriptor]] , in § 21.2
- "texture-formats-tier1" , in § 25.18
- "texture-formats-tier2" , in § 25.19
- texture subresources , in § 6.1
- texture unit , in § 2.1.4
- texture-view-aliasing , in § 6.2
- texture view format compatible , in § 6.1.1
- Timeline-agnostic , in § 3.4.1
- "timestamp" , in § 20.2
- "timestamp-query" , in § 25.8
- timestampWrites dict-member for GPUComputePassDescriptor , in § 16.1.1 dict-member for GPURenderPassDescriptor , in § 17.1.1
- dict-member for GPUComputePassDescriptor , in § 16.1.1
- dict-member for GPURenderPassDescriptor , in § 17.1.1
- to a texel value of texture format , in § 3.12
- toneMapping , in § 21.4
- topology , in § 10.3.2
- to WGSL type , in § 3.12
- transferToImageBitmap from WebGPU , in § 21.3
- TRANSIENT_ATTACHMENT , in § 6.1.2
- "triangle-list" , in § 10.3.2
- "triangle-strip" , in § 10.3.2
- type attribute for GPUCompilationMessage , in § 9.1.2 attribute for GPUQuerySet , in § 20.1 dict-member for GPUBufferBindingLayout , in § 8.1.1 dict-member for GPUQuerySetDescriptor , in § 20.1.1 dict-member for GPUSamplerBindingLayout , in § 8.1.1
- attribute for GPUCompilationMessage , in § 9.1.2
- attribute for GPUQuerySet , in § 20.1
- dict-member for GPUBufferBindingLayout , in § 8.1.1
- dict-member for GPUQuerySetDescriptor , in § 20.1.1
- dict-member for GPUSamplerBindingLayout , in § 8.1.1
- "uint" , in § 8.1.1
- "uint16" enum-value for GPUIndexFormat , in § 10.3.7 enum-value for GPUVertexFormat , in § 10.3.7.1
- enum-value for GPUIndexFormat , in § 10.3.7
- enum-value for GPUVertexFormat , in § 10.3.7.1
- "uint16x2" , in § 10.3.7.1
- "uint16x4" , in § 10.3.7.1
- "uint32" enum-value for GPUIndexFormat , in § 10.3.7 enum-value for GPUVertexFormat , in § 10.3.7.1
- enum-value for GPUIndexFormat , in § 10.3.7
- enum-value for GPUVertexFormat , in § 10.3.7.1
- "uint32x2" , in § 10.3.7.1
- "uint32x3" , in § 10.3.7.1
- "uint32x4" , in § 10.3.7.1
- "uint8" , in § 10.3.7.1
- "uint8x2" , in § 10.3.7.1
- "uint8x4" , in § 10.3.7.1
- unavailable , in § 5.1
- uncapturederror , in § 22.4
- unclippedDepth , in § 10.3.2
- unconfigure() , in § 21.2
- "unfilterable-float" , in § 8.1.1
- "uniform" , in § 8.1.1
- UNIFORM , in § 5.1.2
- "unknown" , in § 22.1
- unmap() , in § 5.2
- "unmapped" , in § 5.1
- "unorm10-10-10-2" , in § 10.3.7.1
- "unorm16" , in § 10.3.7.1
- "unorm16x2" , in § 10.3.7.1
- "unorm16x4" , in § 10.3.7.1
- "unorm8" , in § 10.3.7.1
- "unorm8x2" , in § 10.3.7.1
- "unorm8x4" , in § 10.3.7.1
- "unorm8x4-bgra" , in § 10.3.7.1
- update the canvas size , in § 21.4.2
- updating the rendering of a WebGPU canvas , in § 21.3
- usage attribute for GPUBuffer , in § 5.1 attribute for GPUTexture , in § 6.1 dict-member for GPUBufferDescriptor , in § 5.1.1 dict-member for GPUCanvasConfiguration , in § 21.4 dict-member for GPUTextureDescriptor , in § 6.1.1 dict-member for GPUTextureViewDescriptor , in § 6.2.1
- attribute for GPUBuffer , in § 5.1
- attribute for GPUTexture , in § 6.1
- dict-member for GPUBufferDescriptor , in § 5.1.1
- dict-member for GPUCanvasConfiguration , in § 21.4
- dict-member for GPUTextureDescriptor , in § 6.1.1
- dict-member for GPUTextureViewDescriptor , in § 6.2.1
- [[usage scope]] attribute for GPURenderBundle , in § 18.1 attribute for GPURenderCommandsMixin , in § 17.2
- attribute for GPURenderBundle , in § 18.1
- attribute for GPURenderCommandsMixin , in § 17.2
- usage scope , in § 3.4.4
- usage scope attachment exception , in § 3.4.3
- usage scope storage exception , in § 3.4.3
- usage scope validation , in § 3.4.4
- [[used_bind_groups]] attribute for GPUCommandBuffer , in § 12.1 attribute for GPUCommandsMixin , in § 13.1 attribute for GPURenderBundle , in § 18.1
- attribute for GPUCommandBuffer , in § 12.1
- attribute for GPUCommandsMixin , in § 13.1
- attribute for GPURenderBundle , in § 18.1
- [[usedResources]] , in § 8.2
- "valid" , in § 3.5.1
- [[valid]] , in § 3.1.2
- valid , in § 3.2.1
- Validate encoder bind groups , in § 14.1
- validate GPUColor shape , in § 24.1
- validate GPUExtent3D shape , in § 24.1
- validate GPUOrigin2D shape , in § 24.1
- validate GPUOrigin3D shape , in § 24.1
- Validate swizzle string , in § 6.2.1
- Validate texture format required features , in § 6.3
- Validate the encoder state , in § 13.1
- Validate timestampWrites , in § 20.4
- validating Compatibility Mode shader binding , in § 10.3.1
- validating GPUDepthStencilState , in § 10.3.6
- validating GPUFragmentState , in § 10.3.4
- Validating GPUFragmentState’s color attachment bytes per sample , in § 10.3.4
- validating GPUMultisampleState , in § 10.3.3
- validating GPUPrimitiveState , in § 10.3.2
- validating GPUProgrammableStage , in § 10.1.2
- Validating GPURenderPassDescriptor’s color attachment bytes per sample , in § 17.1.1
- validating GPURenderPipelineDescriptor , in § 10.3.1
- validating GPUTexelCopyBufferInfo , in § 11.2.2
- validating GPUTexelCopyTextureInfo , in § 11.2.3
- validating GPUTextureDescriptor , in § 6.1.3
- validating GPUVertexBufferLayout , in § 10.3.7.1
- validating GPUVertexState , in § 10.3.7.1
- validating inter-stage interfaces , in § 10.3.1
- validating linear texture data , in § 11.2.6
- validating shader binding , in § 10.1.2
- validating texture buffer copy , in § 11.2.3
- validating texture copy range , in § 11.2.6
- "validation" enum-value for GPUErrorFilter , in § 22.3 enum-value for GPUPipelineErrorReason , in § 10
- enum-value for GPUErrorFilter , in § 22.3
- enum-value for GPUPipelineErrorReason , in § 10
- validation error , in § 22.2
- valid GPUBlendComponent , in § 10.3.4
- valid to draw , in § 17.2.1
- valid to draw indexed , in § 17.2.1
- valid to use with , in § 3.2.1
- Valid Usage , in § 17.1.1
- vendor , in § 3.6.2.4
- "vertex" , in § 10.3.7.1
- VERTEX const for GPUBufferUsage , in § 5.1.2 const for GPUShaderStage , in § 8.1.1
- const for GPUBufferUsage , in § 5.1.2
- const for GPUShaderStage , in § 8.1.1
- vertex , in § 10.3.1
- vertex buffer , in § 10.3.7.1
- [[vertex_buffers]] , in § 17.2
- [[vertex_buffer_sizes]] , in § 17.2
- vertex data type , in § 10.3.7.1
- view dict-member for GPURenderPassColorAttachment , in § 17.1.1.1 dict-member for GPURenderPassDepthStencilAttachment , in § 17.1.1.2
- dict-member for GPURenderPassColorAttachment , in § 17.1.1.1
- dict-member for GPURenderPassDepthStencilAttachment , in § 17.1.1.2
- viewDimension dict-member for GPUStorageTextureBindingLayout , in § 8.1.1 dict-member for GPUTextureBindingLayout , in § 8.1.1
- dict-member for GPUStorageTextureBindingLayout , in § 8.1.1
- dict-member for GPUTextureBindingLayout , in § 8.1.1
- [[viewFormats]] , in § 6.1
- viewFormats dict-member for GPUCanvasConfiguration , in § 21.4 dict-member for GPUTextureDescriptor , in § 6.1.1
- dict-member for GPUCanvasConfiguration , in § 21.4
- dict-member for GPUTextureDescriptor , in § 6.1.1
- [[viewport]] , in § 17.1
- Viewport coordinates , in § 3.3
- views , in § 5.1
- visibility , in § 8.1.1
- "warning" , in § 9.1.2
- WebGPU interface , in § 3.1.2
- WebGPU object , in § 3.1.2
- WebGPU platform , in § 3.4.2
- WebGPU task source , in § 3.10.1
- WGSLLanguageFeatures , in § 3.6.2.2
- wgslLanguageFeatures , in § 4.2
- width attribute for GPUTexture , in § 6.1 dfn for GPUExtent3D , in § 24.1 dict-member for GPUExtent3DDict , in § 24.1
- attribute for GPUTexture , in § 6.1
- dfn for GPUExtent3D , in § 24.1
- dict-member for GPUExtent3DDict , in § 24.1
- Window coordinates , in § 3.3
- WRITE , in § 5.2
- writeBuffer(buffer, bufferOffset, data) , in § 19.2
- writeBuffer(buffer, bufferOffset, data, dataOffset) , in § 19.2
- writeBuffer(buffer, bufferOffset, data, dataOffset, size) , in § 19.2
- writeMask , in § 10.3.5
- "write-only" , in § 8.1.1
- [[writesDepth]] , in § 10.3
- [[writesStencil]] , in § 10.3
- writeTexture(destination, data, dataLayout, size) , in § 19.2
- x dfn for GPUOrigin2D , in § 24.1 dfn for GPUOrigin3D , in § 24.1 dict-member for GPUOrigin2DDict , in § 24.1 dict-member for GPUOrigin3DDict , in § 24.1
- dfn for GPUOrigin2D , in § 24.1
- dfn for GPUOrigin3D , in § 24.1
- dict-member for GPUOrigin2DDict , in § 24.1
- dict-member for GPUOrigin3DDict , in § 24.1
- [[xrCompatible]] , in § 3.5.1
- xrCompatible , in § 4.2.2
- y dfn for GPUOrigin2D , in § 24.1 dfn for GPUOrigin3D , in § 24.1 dict-member for GPUOrigin2DDict , in § 24.1 dict-member for GPUOrigin3DDict , in § 24.1
- dfn for GPUOrigin2D , in § 24.1
- dfn for GPUOrigin3D , in § 24.1
- dict-member for GPUOrigin2DDict , in § 24.1
- dict-member for GPUOrigin3DDict , in § 24.1
- z dfn for GPUOrigin3D , in § 24.1 dict-member for GPUOrigin3DDict , in § 24.1
- dfn for GPUOrigin3D , in § 24.1
- dict-member for GPUOrigin3DDict , in § 24.1
- "zero" enum-value for GPUBlendFactor , in § 10.3.5.1 enum-value for GPUStencilOperation , in § 10.3.6
- enum-value for GPUBlendFactor , in § 10.3.5.1
- enum-value for GPUStencilOperation , in § 10.3.6

### Terms defined by reference

- [CSS-COLOR-4] defines the following terms: srgb srgb-linear
- srgb
- srgb-linear
- [DOM] defines the following terms: Event EventInit EventTarget defaultPrevented fire an event preventDefault()
- Event
- EventInit
- EventTarget
- defaultPrevented
- fire an event
- preventDefault()
- [ECMAScript] defines the following terms: ! ? CreateByteDataBlock DetachArrayBuffer [[ArrayBufferDetachKey]] agent agent cluster Data Block
- CreateByteDataBlock
- DetachArrayBuffer
- [[ArrayBufferDetachKey]]
- agent
- agent cluster
- Data Block
- [HR-TIME-3] defines the following terms: coarsen time
- coarsen time
- [HTML] defines the following terms: CanvasRenderingContext2D EventHandler HTMLCanvasElement HTMLImageElement HTMLMediaElement HTMLVideoElement ImageBitmap ImageBitmapRenderingContext ImageData Navigator OffscreenCanvas PredefinedColorSpace Serializable SharedWorkerGlobalScope Window WorkerGlobalScope WorkerNavigator check the usability of the image argument colorSpace colorSpaceConversion deserialization steps display-p3 drawImage() event handler IDL attribute event loop processing model getContext(contextId, options) (for HTMLCanvasElement) getContext(contextId, options) (for OffscreenCanvas) height (for HTMLCanvasElement) height (for ImageBitmap) height (for ImageData) height (for OffscreenCanvas) img intrinsic height intrinsic width is not origin-clean naturalHeight naturalWidth origin-clean placeholder canvas element premultiplyAlpha queue a global task requestAnimationFrame(callback) serialization steps srgb task task source toBlob(callback, type, quality) toDataURL(type, quality) transferControlToOffscreen() transferToImageBitmap() width (for HTMLCanvasElement) width (for ImageBitmap) width (for ImageData) width (for OffscreenCanvas)
- CanvasRenderingContext2D
- EventHandler
- HTMLCanvasElement
- HTMLImageElement
- HTMLMediaElement
- HTMLVideoElement
- ImageBitmap
- ImageBitmapRenderingContext
- ImageData
- Navigator
- OffscreenCanvas
- PredefinedColorSpace
- Serializable
- SharedWorkerGlobalScope
- Window
- WorkerGlobalScope
- WorkerNavigator
- check the usability of the image argument
- colorSpace
- colorSpaceConversion
- deserialization steps
- display-p3
- drawImage()
- event handler IDL attribute
- event loop processing model
- getContext(contextId, options) (for HTMLCanvasElement)
- getContext(contextId, options) (for OffscreenCanvas)
- height (for HTMLCanvasElement)
- height (for ImageBitmap)
- height (for ImageData)
- height (for OffscreenCanvas)
- img
- intrinsic height
- intrinsic width
- is not origin-clean
- naturalHeight
- naturalWidth
- origin-clean
- placeholder canvas element
- premultiplyAlpha
- queue a global task
- requestAnimationFrame(callback)
- serialization steps
- srgb
- task
- task source
- toBlob(callback, type, quality)
- toDataURL(type, quality)
- transferControlToOffscreen()
- transferToImageBitmap()
- width (for HTMLCanvasElement)
- width (for ImageBitmap)
- width (for ImageData)
- width (for OffscreenCanvas)
- [I18N-GLOSSARY] defines the following terms: valid
- valid
- [INFRA] defines the following terms: append (for list) append (for set) assert clear contain (for list) contain (for map) continue empty exist (for list) exist (for map) extend (for list) extend (for set) for each implementation-defined indices is empty item length list map ordered map ordered set pop push remove set size stack
- append (for list)
- append (for set)
- assert
- clear
- contain (for list)
- contain (for map)
- continue
- empty
- exist (for list)
- exist (for map)
- extend (for list)
- extend (for set)
- for each
- implementation-defined
- indices
- is empty
- item
- length
- list
- map
- ordered map
- ordered set
- pop
- push
- remove
- set
- size
- stack
- [INTERNATIONALIZATION GLOSSARY] defines the following terms: localizable text
- localizable text
- [KHRONOS DATA FORMAT SPECIFICATION] defines the following terms: ASTC compressed formats BC compressed formats ETC2 compressed formats
- ASTC compressed formats
- BC compressed formats
- ETC2 compressed formats
- [MEDIAQUERIES-5] defines the following terms: dynamic-range high
- dynamic-range
- high
- [SERVICE-WORKERS] defines the following terms: ServiceWorkerGlobalScope
- ServiceWorkerGlobalScope
- [STRINGS ON THE WEB] defines the following terms: best practices for language and direction information
- best practices for language and direction information
- [WEBCODECS] defines the following terms: VideoFrame Close VideoFrame close() decode(chunk) displayHeight displayWidth
- VideoFrame
- Close VideoFrame
- close()
- decode(chunk)
- displayHeight
- displayWidth
- [WEBGL-1] defines the following terms: WebGLContextAttributes WebGLRenderingContextBase drawingBufferColorSpace drawingBufferHeight drawingBufferWidth WebGL Drawing Buffer
- WebGLContextAttributes
- WebGLRenderingContextBase
- drawingBufferColorSpace
- drawingBufferHeight
- drawingBufferWidth
- WebGL Drawing Buffer
- [WEBIDL] defines the following terms: AbortError AllowShared AllowSharedBufferSource ArrayBuffer Clamp DOMException DOMString DataView EnforceRange Exposed FrozenArray InvalidStateError NewObject OperationError Promise RangeError SameObject SecureContext SecurityError TypeError USVString Uint32Array a new promise a promise rejected with boolean converted to an ECMAScript value converted to an IDL value create detach double float get a copy of the buffer source getter steps long message name record reject resolve sequence set entries setlike this transfer undefined unrestricted double unrestricted float unsigned long unsigned long long unsigned short
- AbortError
- AllowShared
- AllowSharedBufferSource
- ArrayBuffer
- Clamp
- DOMException
- DOMString
- DataView
- EnforceRange
- Exposed
- FrozenArray
- InvalidStateError
- NewObject
- OperationError
- Promise
- RangeError
- SameObject
- SecureContext
- SecurityError
- TypeError
- USVString
- Uint32Array
- a new promise
- a promise rejected with
- boolean
- converted to an ECMAScript value
- converted to an IDL value
- create
- detach
- double
- float
- get a copy of the buffer source
- getter steps
- long
- message
- name
- record
- reject
- resolve
- sequence
- set entries
- setlike
- this
- transfer
- undefined
- unrestricted double
- unrestricted float
- unsigned long
- unsigned long long
- unsigned short
- [WEBXR] defines the following terms: WebXR session
- WebXR session
- [WGSL] defines the following terms: 64-bit unsigned integer @binding @group @interpolate SizeOf blend_src built-in output value builtin channel formats clip_distances (for builtin) clip_distances (for extension) depth texture dual_source_blending either f16 f16 (for extension) flat frag_depth functions in the shader stage global_invocation_id indeterminate value instance_index interface of a shader stage interpolation interpolation sampling interpolation type invalid memory reference language extension line break linear local_invocation_id local_invocation_index location num_workgroups perspective pipeline constant ID pipeline creation pipeline-creation error pipeline-overridable pipeline-overridable constant default value pipeline-overridable constant identifier string position builtin primitive_index (for builtin) primitive_index (for extension) program error roundUp runtime-sized sample sample_index sample_mask sampled texture shader execution end shader module creation shader stage input shader stage output shader-creation error store type subgroup size subgroups Synchronization Built-in Functions textureSampleLevel uncategorized error use dual source blending vertex_index WGSL floating point behaviors WGSL floating point conversion WGSL identifier comparison WGSL scalar type workgroup workgroup_id
- 64-bit unsigned integer
- @binding
- @group
- @interpolate
- SizeOf
- blend_src
- built-in output value
- builtin
- channel formats
- clip_distances (for builtin)
- clip_distances (for extension)
- depth texture
- dual_source_blending
- either
- f16
- f16 (for extension)
- flat
- frag_depth
- functions in the shader stage
- global_invocation_id
- indeterminate value
- instance_index
- interface of a shader stage
- interpolation
- interpolation sampling
- interpolation type
- invalid memory reference
- language extension
- line break
- linear
- local_invocation_id
- local_invocation_index
- location
- num_workgroups
- perspective
- pipeline constant ID
- pipeline creation
- pipeline-creation error
- pipeline-overridable
- pipeline-overridable constant default value
- pipeline-overridable constant identifier string
- position builtin
- primitive_index (for builtin)
- primitive_index (for extension)
- program error
- roundUp
- runtime-sized
- sample
- sample_index
- sample_mask
- sampled texture
- shader execution end
- shader module creation
- shader stage input
- shader stage output
- shader-creation error
- store type
- subgroup size
- subgroups
- Synchronization Built-in Functions
- textureSampleLevel
- uncategorized error
- use dual source blending
- vertex_index
- WGSL floating point behaviors
- WGSL floating point conversion
- WGSL identifier comparison
- WGSL scalar type
- workgroup
- workgroup_id

## References

### Normative References

[LINK: High Resolution Time](https://w3c.github.io/hr-time/)
[LINK: https://w3c.github.io/hr-time/](https://w3c.github.io/hr-time/)
[LINK: Internationalization Glossary](https://w3c.github.io/i18n-glossary/)
[LINK: https://w3c.github.io/i18n-glossary/](https://w3c.github.io/i18n-glossary/)
[LINK: WebCodecs](https://w3c.github.io/webcodecs/)
[LINK: https://w3c.github.io/webcodecs/](https://w3c.github.io/webcodecs/)
[LINK: WebXR Device API](https://immersive-web.github.io/webxr/)
[LINK: https://immersive-web.github.io/webxr/](https://immersive-web.github.io/webxr/)
[LINK: WebGPU Shading Language](https://gpuweb.github.io/gpuweb/wgsl/)
[LINK: https://gpuweb.github.io/gpuweb/wgsl/](https://gpuweb.github.io/gpuweb/wgsl/)

### Informative References

[LINK: Service Workers Nightly](https://w3c.github.io/ServiceWorker/)
[LINK: https://w3c.github.io/ServiceWorker/](https://w3c.github.io/ServiceWorker/)

## IDL Index

[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
[LINK: VideoFrame](https://w3c.github.io/webcodecs/#videoframe)
[LINK: EventHandler](https://html.spec.whatwg.org/multipage/webappapis.html#eventhandler)

--------------------