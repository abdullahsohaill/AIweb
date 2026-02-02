# Chromium updates
**URL:** https://blog.chromium.org
**Page Title:** Chromium Blog
--------------------


## Chromium Blog

## Reducing notification overload for a quieter browsing experience in Chrome

We're constantly working to improve your browsing experience. To help you cut through the noise and reduce notification overload, we’re launching a new feature to automatically remove notification permission for sites you haven't interacted with recently. Today, Chrome’s Safety Check already does this for other permissions such as camera and location. The feature will be launched in Chrome on Android and desktop.
We're constantly working to improve your browsing experience. To help you cut through the noise and reduce notification overload, we’re launching a new feature to automatically remove notification permission for sites you haven't interacted with recently. Today, Chrome’s Safety Check already does this for other permissions such as camera and location. The feature will be launched in Chrome on Android and desktop.
Data indicates that users frequently receive a high volume of notifications, resulting in minimal engagement and high disruption. Less than 1% of all notifications receive any interaction from users.
But notifications can be genuinely valuable and helpful. Therefore, this feature will only revoke permissions for sites when there is very low user engagement and a high volume of notifications being sent. This feature does not revoke notifications for any installed web apps .
Chrome will inform you when notification permissions are removed. If you prefer to keep getting notifications from a particular website, you can easily re-grant the permission at any time through Safety Check or alternatively by visiting the site and enabling notifications again. You can also choose to turn off the auto-revocation feature entirely.
We've already been testing this feature. Our test results show a significant reduction in notification overload with only a minimal change in total notification clicks. Our experiments also indicate that websites that send a lower volume of notifications are actually seeing an increase in clicks.
This launch is part of our ongoing commitment to user safety, privacy, and control. We believe this change will lead to a cleaner, more focused browsing experience, and we’ll continue to invest in ways to help you manage your online interactions and reduce distractions, so you can make the most of your time online.

## Introducing Skia Graphite: Chrome's rasterization backend for the future

Today's The Fast and the Curious post covers the launch of Skia's new rasterization backend, Graphite, in Chrome on Apple Silicon Macs. Graphite is instrumental in helping Chrome achieve exceptional scores on Motionmark 1.3 and is key to unlocking a ton of future improvements in Chrome Graphics.
Today's The Fast and the Curious post covers the launch of Skia's new rasterization backend, Graphite, in Chrome on Apple Silicon Macs. Graphite is instrumental in helping Chrome achieve exceptional scores on Motionmark 1.3 and is key to unlocking a ton of future improvements in Chrome Graphics.

## A brief history of Skia in Chrome

In Chrome, Skia is used to render paint commands from Blink and the browser UI into pixels on your screen, a process called rasterization. Skia has powered Chrome Graphics since the very beginning . Skia eventually ran into performance issues as the web evolved and became more complex, which led Chrome and Skia to invest in a GPU accelerated rasterization backend called Ganesh.
[LINK: since the very beginning](https://www.google.com/url?q=https://blog.chromium.org/2008/10/graphics-in-google-chrome.html&sa=D&source=docs&ust=1744655288075052&usg=AOvVaw2iZg3ILJvcyGeG8RDYzVNv)
Over the years, Ganesh matured into a solid highly performant rasterization backend and GPU rasterization launched on all platforms in Chrome on top of GL (via ANGLE on Windows D3D9/11). However, Ganesh always had a GL-centric design with too many specialized code paths and the team was hitting a wall when trying to implement optimizations that took advantage of modern graphics APIs in a principled manner.
This set the stage for the team to rethink GPU rasterization from the ground up in the form of a new rasterization backend, Graphite. Graphite was developed from the start to be principled by having fewer and more comprehensible code paths. This forward looking design helps take advantage of modern graphics APIs like Metal, Vulkan and D3D12 and paradigms like compute based path rasterization, and is multithreaded by default.

## Results

With Graphite in Chrome, we increased our Motionmark 1.3 scores by almost 15% on a Macbook Pro M3. At the same time, we improved real world metrics like INP (interaction to next paint time), LCP (time to largest contentful paint),  graphics smoothness (percent dropped frames), GPU process malloc memory usage, and others. This all means substantially smoother interactions, less stutter when scrolling, and less time waiting for sites to show.

## Differences between Graphite and Ganesh

### Modern graphics APIs

Ganesh was originally implemented on OpenGL ES, which had minimal support for multi-threading or GPU capabilities like compute shaders. Since then, modern graphics APIs like Vulkan, Metal and D3D12 have evolved to take advantage of multithreading and expose new GPU capabilities. They allow applications to have much more control over when and how expensive work such as allocating GPU resources is performed and scheduled, while utilizing both the CPU and the GPU effectively.
While we were able to adapt Ganesh to support modern graphics APIs, it had accumulated enough technical debt that it became hard to fully take advantage of the multi-threading and GPU compute capabilities of modern graphics APIs.
For Graphite in Chrome, we chose to use Chrome's WebGPU implementation, Dawn , as the abstraction layer for platform native graphics APIs like Metal, Vulkan and D3D. Dawn provides a baseline for capabilities common in modern graphics APIs and helps us reduce the long term maintenance burden by leveraging Dawn's mature well tested native backends instead of implementing them from scratch for Graphite.

### 2D depth(?!) testing

A core part of the GPU rendering pipeline is depth testing, which can reduce or eliminate overdraw by drawing opaque objects in front to back order, followed by translucent objects back to front. In graphics, "overdraw" refers to the unnecessary rendering of the same pixels multiple times, which can negatively impact performance and battery life, especially on mobile devices.
Ganesh never utilized the depth testing capabilities of graphics cards, which was admittedly intended for rendering 3D content and not accelerating 2D graphics. Ganesh suffers from overdraw due to its reliance on adhering to strict painters order when drawing both opaque and translucent objects.
Graphite extends Skia’s GPU rendering to take advantage of the depth test by assigning each “draw” a z value defining its painter’s ordering index. While transparent effects and images must still be drawn from back to front, opaque objects in the foreground can now automatically eliminate overdraw. This means opaque draws can be re-ordered to minimize expensive GPU state changes while relying on the depth buffer to produce correct output.
Depth testing is also used to implement clipping in Graphite by treating clip shapes as depth only draws as opposed to maintaining a clip stack like in Ganesh. Besides reducing algorithmic complexity, a significant benefit to this approach is that the shader program required to render a “draw” does not also depend on the state of the clip stack.
Left: Frame from Motionmark Suits Right: Depth buffer for the same frame.

### Multithreading

Chromium is a complex multi-process application, with render processes issuing commands to a shared GPU process that is responsible for actually displaying everything in a webpage, tab, and even the browser UI. The GPU process main thread is the primary driver of all rendering work and is where all GPU commands are issued.
Due to the single threaded nature of Ganesh and OpenGL, only a limited set of work could be moved to other threads, making it easy to overload the main thread causing increased jank and latency ultimately hurting user experience.
In contrast, Graphite's API is designed to take advantage of multithreading capabilities of modern graphics APIs. Graphite’s new core API is centered around independent Recorders that can produce Recordings on multiple threads, with minimal need to synchronize between them. Even though the Recordings are submitted to the GPU on the main thread, more expensive work is moved to other threads when producing Recordings , keeping the GPU main thread free.

### Performance cliffs and pipeline compilation

When Ganesh was initially implemented, the programmable capabilities of graphics cards were quite limited, and branching in particular was expensive. To work around this, Ganesh had many specialized shader pipelines to handle common cases. These specializations are hard to predict and depend on a large number of factors related to each individual draw, leading to an explosion of different pipelines for essentially the same page content. Since these pipelines must each be compiled, it doesn't work well for modern web content which might have effects and animations trigger new pipelines at any moment, causing noticeable jank.
Graphite’s design philosophy is instead to consolidate the number of rendering pipelines as much as possible while still preserving performance.  This reduces the number of pipelines that have to be compiled, and makes it possible for Chrome to ensure they are compiled at startup so they do not interrupt active browsing. Ganesh’s specialization approach also led to surprising performance cliffs. For example, while it could handle simple cases, real page content was often a complex mix. By consolidating pipelines, complex content can be rendered as effectively as simple content.

## Future Plans

### Multithreaded Rasterization

Currently, Graphite is integrated into Chromium using two Recorders: one handles web content tiles and Canvas2D on the main thread, while the other is for compositing.  In the future, this model will open up a number of exciting possibilities to further improve Chrome’s performance.  Instead of saturating the main GPU thread with the tasks from each renderer process, rasterization can be forked across multiple threads.
Current:
Future:

### Reducing GPU memory for simple content

Graphite recordings can also be re-issued to the GPU with certain dynamic changes such as translation. This can be used to accelerate scrolling while eliminating the unnecessary work to re-issue rendering commands.  This lets us automatically reduce the amount of GPU memory required to cache web content as tiles. If the content is simple enough, the performance difference between drawing a cached image and drawing its content can be worth skipping allocating a tile for it and just re-rendering it each frame.

### GPU Compute Path Rasterization

In the landscape of 2D graphics rendering, GPU compute-based path rasterization is very much en vogue with recent implementations like Pathfinder and vello . We would like to implement these ideas in Skia, possibly using a hybrid approach . Currently, Graphite relies on MSAA where it can, but in many cases we can't due to poor performance on older integrated GPUs or high memory overhead on non-tiling GPUs, and we have to fallback to CPU path rasterization using an atlas for caching. GPU compute based path rasterization would allow us to improve over both the visual quality of MSAA which is often limited to 4 samples per pixel and over the performance of CPU rasterization.
[LINK: GPU compute-based path rasterization](https://raphlinus.github.io/rust/graphics/gpu/2020/06/13/fast-2d-rendering.html)
[LINK: Pathfinder](https://github.com/pcwalton/pathfinder)
[LINK: vello](https://github.com/linebender/vello)
[LINK: hybrid approach](https://docs.google.com/document/d/1gEqf7ehTzd89Djf_VpkL0B_Fb15e0w5fuv_UzyacAPU/preview)
These are future directions the Chrome Graphics team plans to pursue, and we are excited to see how far we can push the needle.

## Chrome achieves highest score ever on Speedometer 3.1, saving users millions of hours

Update (6/10/2025): This blog was updated to reflect that testing was done using the Speedometer 3.1 benchmark, and resulted in a 22% performance improvement. The previous version incorrectly noted that the performance improvement was 10% and that the benchmark was Speedometer 3.
Update (6/10/2025): This blog was updated to reflect that testing was done using the Speedometer 3.1 benchmark, and resulted in a 22% performance improvement. The previous version incorrectly noted that the performance improvement was 10% and that the benchmark was Speedometer 3.
Performance has always been one of the core pillars of Chrome and it’s something we’ve never stopped investing in.  Publicly available and open benchmarks, which we create in open collaboration with other browsers, are useful tools for tracking our overall progress, understanding new areas of improvement, and validating potential optimizations. In today’s The Fast and the Curious post,  we’d like to go through Chrome’s recent work that enabled it to achieve the highest score ever on the Speedometer benchmark.
For Speedometer, these optimizations have resulted in a 22% improvement since August 2024. That 22% improvement leads to better browser experiences, higher conversions for businesses, and deeper enjoyment of what the web has to offer. If each Chrome user used Chrome for just 10 minutes a day, these improvements collectively save 116 million hours or roughly 166 lifetimes worth of waiting around for websites to load and do things.
Speedometer 3.1 score measured on Apple Macbook Pro M4 with MacOS 15
Speedometer is a benchmark created in open collaboration with other browsers and measures web application responsiveness through workloads that cover a large variety of different areas of the Blink rendering engine used in Chrome:
- HTML parsing
- JavaScript and JSON processing
- JavaScript and Document Object Model (DOM) interaction
- DOM manipulations (element insertion and removal)
- Text size computation (font shaping)
- Cascading Style Sheet (CSS) application and layout calculation
- Pixel rendering
In essence, Speedometer tests critical components of the entire rendering pipeline. For a deeper dive into these individual parts, we recommend the presentation Life of a Script at Chrome University .
Achieving exceptional web performance requires a multifaceted approach, and optimizing for Speedometer is a testament to overall product excellence. Over the past year, our team has focused on refining fundamental rendering paths across the entire stack. Here are some notable optimization examples.
The team heavily optimized memory layouts of many internal data structures across DOM, CSS, layout, and painting components. Blink now avoids a lot of useless churn on system memory by keeping state where it belongs with respect to access patterns, maximizing utilization of CPU caches. Where internal memory was already relying on garbage collection in Oilpan, e.g. DOM, the usage was expanded by converting types from using malloc to Oilpan. This generally speeds up the affected areas as it packs memory nicely in Oilpan’s backend.
Strings in the renderer improved quite a bit over the last year by avoiding costly representations where possible and switching hashing to rapidhash. More generally, lots of data structures were equipped with better hashes, filters, and probing algorithms.
Where rendering becomes inherently expensive, e.g., for computing CSS styles across various elements, caches are now used much more effectively with better hit rates. At the same time we cache fewer things that are not relevant. Another area where rendering becomes expensive is font shaping; the team significantly improved Apple  Advanced Typography font shaping performance which is relevant everywhere text is rendered.
Posted by Thomas Nattestad

## Fighting Unwanted Notifications with Machine Learning in Chrome

Notifications in Chrome are a useful feature to keep up with updates from your favorite sites. However, we know that some notifications may be spammy or even deceptive. We’ve received reports of notifications diverting you to download suspicious software, tricking you into sharing personal information or asking you to make purchases on potentially fraudulent online store fronts.
Notifications in Chrome are a useful feature to keep up with updates from your favorite sites. However, we know that some notifications may be spammy or even deceptive. We’ve received reports of notifications diverting you to download suspicious software, tricking you into sharing personal information or asking you to make purchases on potentially fraudulent online store fronts.
To defend against these threats, Chrome is launching warnings of unwanted notifications on Android. This new feature uses on-device machine learning to detect and warn you about potentially deceptive or spammy notifications, giving you an extra level of control over the information displayed on your device.
When a notification is flagged by Chrome, you’ll see the name of the site sending the notification, a message warning that the contents of the notification are potentially deceptive or spammy, and the option to either unsubscribe from the site or see the flagged content.
An example of a notification flagged as possibly spam.
If you choose to see the notification you will still see the option to unsubscribe or you can choose to always allow notifications from that site and not see warnings in the future.
What you see when viewing a flagged notification.
How It Works
Chrome uses a local, on-device machine learning model to analyze notification content. This model identifies notifications that are likely to be unwanted. The model is trained on the textual contents of the notification, like the title, body, and action button texts.
Notifications are end to end encrypted. The analysis of each message is done on-device and notification contents are not sent to Google, to protect user privacy. Due to the sensitive nature of notifications content, the model was trained using synthetic data generated by the Gemini large language model (LLM). The training data was evaluated against real notifications Chrome security team collected by subscribing to a variety of websites that were then classified by human experts. To start, this feature is only available on Android as the majority of notifications are sent to mobile devices, however we will evaluate expanding to other platforms in the future.
This feature is just one of many ways Chrome works to reduce the number of potentially harmful notifications you receive. Other ways Chrome protects against potentially harmful notifications include:
- Revoking Notification Permissions from Abusive Sites: When Google Safe Browsing identifies a site engaging in abusive behavior Chrome will automatically revoke the site’s notification permissions. You can find a list of revoked notification permissions in Chrome Safety Check. Learn more about how Safety Check takes proactive steps to keep you safe here . In Safety Check you can review any notification permission revocations One Tap Unsubscribe on Android: You have the option to unsubscribe from notifications with one click on any Chrome notification sent to an Android phone, whether the notification contents are benign or potentially harmful. Limiting notifications from sites you no longer want updates from can reduce the amount of data and battery life you use daily. If you ever want to review what sites have the ability to send you notifications you can visit Chrome Settings-> Privacy and Security->Site Settings->Notifications. Notification warnings are an important step in Chrome's ongoing commitment to user safety. The Chrome Security team in partnership with Google Safe Browsing continually monitors threats to our users in order to evolve our defenses against abusive activity across the web. Keep an eye on our blog for updates on how we are helping you stay one step ahead of online threats. Posted by Hannah Buonomo & Sarah Krakowiak Criel, Chrome Security
In Safety Check you can review any notification permission revocations
- One Tap Unsubscribe on Android: You have the option to unsubscribe from notifications with one click on any Chrome notification sent to an Android phone, whether the notification contents are benign or potentially harmful. Limiting notifications from sites you no longer want updates from can reduce the amount of data and battery life you use daily. If you ever want to review what sites have the ability to send you notifications you can visit Chrome Settings-> Privacy and Security->Site Settings->Notifications.
Notification warnings are an important step in Chrome's ongoing commitment to user safety. The Chrome Security team in partnership with Google Safe Browsing continually monitors threats to our users in order to evolve our defenses against abusive activity across the web. Keep an eye on our blog for updates on how we are helping you stay one step ahead of online threats.

## Announcing Supporters of Chromium-based Browsers

Since Google announced the Chromium project in 2008, we have been excited to build on the great foundations of open-source web browsers and contribute to the continued development of a rich web platform. Today, Chromium is used by hundreds of different projects globally, including big browsers like Chrome, home electronics from LG, application frameworks like Electron and even custom applications like Bloomberg terminals and SpaceX capsule control software.
Since Google announced the Chromium project in 2008, we have been excited to build on the great foundations of open-source web browsers and contribute to the continued development of a rich web platform. Today, Chromium is used by hundreds of different projects globally, including big browsers like Chrome, home electronics from LG, application frameworks like Electron and even custom applications like Bloomberg terminals and SpaceX capsule control software.
In 2024, Google made over 100,000 commits to Chromium, accounting for ~94 percent of contributions. While we have no intention of reducing this investment, we continue to welcome others stepping up to invest more.
Google also continues to invest heavily in the shared infrastructure of the Open Source project to "keep the lights on", including having thousands of servers endlessly running millions of tests, responding to hundreds of incoming bugs per day, ensuring the important ones get fixed, and constantly investing in code health to keep the whole project maintainable. This work represents hundreds of millions of US dollars in annual investment just for maintenance costs before any new feature, innovation or other business priorities can be addressed.
Sustainable funding of critical open source infrastructure remains a hot industry-wide topic of discussion and over the years we’ve heard from many companies and developers about how critical the Chromium project is to their work. They’ve also shared how they would like to support the continued health of the project, beyond direct engineering support.
Today Google is pleased to announce our partnership with The Linux Foundation and the launch of the Supporters of Chromium-based Browsers . The goal of this initiative is to foster a sustainable environment of open-source contributions towards the health of the Chromium ecosystem and financially support a community of developers who want to contribute to the project, encouraging widespread support and continued technological progress for Chromium embedders.
The Supporters of Chromium-based Browsers fund will be managed by the Linux Foundation , following their long established practices for open governance, prioritizing transparency, inclusivity, and community-driven development. We’re thrilled to have Meta, Microsoft, and Opera on-board as the initial members to pledge their support.
We welcome this additional investment into Chromium’s commons and we’re looking forward to working with the other members of the Supporters of Chromium-based Browsers to ensure that it meets the needs of the wider Chromium community. At the same time, we remain committed to being the responsible steward of the Chromium project and to the massive investment necessary to keep Chromium working well for the entire web industry.

## Making Chrome QUICer

In October 2020, Chrome enabled HTTP/3 by default . HTTP/3 ( RFC 9114 ) runs over IETF QUIC ( RFC9000 ). Default-enabling HTTP/3 in Chrome resulted in improved performance compared not only HTTP/1 and HTTP/2, but also Google QUIC. Benefits included reduced Google search latency and fewer rebuffers for YouTube.
In October 2020, Chrome enabled HTTP/3 by default . HTTP/3 ( RFC 9114 ) runs over IETF QUIC ( RFC9000 ). Default-enabling HTTP/3 in Chrome resulted in improved performance compared not only HTTP/1 and HTTP/2, but also Google QUIC. Benefits included reduced Google search latency and fewer rebuffers for YouTube.
The journey to optimizing performance did not end when HTTP/3 was default enabled. Recent advancements include the implementation of the HTTP/3 ORIGIN frame ( RFC 9412 ) and Server's Preferred Address ( RFC 9000 Section 9.6 ). The former enhances connection coalescing, while the latter reduces a connection's round trip time (RTT). Both features have been enabled by default in M131, which was released to Stable on 11/19.

### ORIGIN Frame

When a connection is established for a specific hostname, the server’s certificate typically contains numerous other hostnames for which the server is authoritative. However, a client cannot immediately send requests for those other hostnames on that connection without first performing a DNS lookup for the other hostname and verifying that the IP address of the connection matches the resolved address. This additional DNS resolution introduces latency and significantly reduces the likelihood of connection pooling due to potential IP mismatches. The metrics from Chrome indicate that nearly 20% of HTTP/3 connections would be unnecessary if not for this IP mismatch.
Creating a new connection, even with QUIC 0-RTT, is expensive in terms of latency, memory, and CPU usage. This is because:
- DNS resolution adds latency unless cached locally in Chrome’s DNS cache.
- Both client and server must send multiple packets to complete a QUIC handshake.
- TLS necessitates CPU-intensive asymmetric cryptography on both ends.
- The congestion controller begins in its default state, potentially leading to under or over-sending.
- 0-RTT might fail.
- Non-safe requests aren't sent via 0-RTT.
- More connections consume more memory.
Additionally, features like HTTP priorities ( RFC 9218 ) are only effective if there are multiple simultaneous responses to send.
The HTTP/3 ORIGIN Frame ( RFC 9412 ) enables a server to indicate what domains it would like to pool onto a connection. Additionally, once the frame is received, it indicates other domains should not be pooled onto that connection, even if they are in the certificate.

### Server’s Preferred Address

In some cases, the initial server address to which the client connects is not the most efficient route. It might be behind an L4 load balancer, and connecting directly could increase stability. Particularly when using Anycast, it’s possible the server is distant from where traffic enters the network, creating a 3-legged path that increases the round trip time.
Once the handshake is confirmed, Server’s Preferred Address allows a server to indicate it would like the client to migrate to a different server IP. Though a QUIC connection is not bound to a single 4-tuple like TCP, this is the only type of migration in RFC9000 where the server can change its address.
So far, only Google’s Media CDN has widely enabled advertising an alternative address, but we expect more servers to adopt it soon. Testing has shown that this migration is successful over 99% of the time in Chrome and reduces average RTT by 40-80%.
[LINK: Media CDN](https://cloud.google.com/media-cdn/docs/overview)

## How Chrome doubled its Speedometer scores on Android

Today’s The Fast and the Curious post covers how Chrome achieved best-in-class Speedometer scores on mobile devices, resulting in faster and smoother web experiences for Android users.
Chrome has always been about speed. Whether it's loading pages quickly, running complex web apps smoothly, or delivering a seamless browsing experience, performance is at the heart of our browser. And we're always looking for ways to make Chrome even faster.
Today’s The Fast and the Curious post covers how Chrome achieved best-in-class Speedometer scores on mobile devices, resulting in faster and smoother web experiences for Android users.
Chrome has always been about speed. Whether it's loading pages quickly, running complex web apps smoothly, or delivering a seamless browsing experience, performance is at the heart of our browser. And we're always looking for ways to make Chrome even faster.
Over the last two years, we have been hard at work on a number of performance improvements for Android devices . We're excited to share some of the progress we've made.

## Speedometer on Android

One of the key metrics we use to track Chrome's performance is the Speedometer benchmark . This benchmark is developed in collaboration with other major web browser engines and measures how quickly Chrome can complete interactions with web pages, including parsing/rendering HTML or CSS and running JavaScript.
Since the release of Chrome M112, we've seen a significant increase in Speedometer 2.1 scores on Android devices [1] . In fact, on many devices, scores more than doubled, with the newest Snapdragon® 8 Elite Mobile Platform setting new records for Speedometer performance on mobile devices! These huge accomplishments are a testament to the work not only of the Chrome and Android teams, but also our silicon and SoC partners.
Since Chrome M112, Speedometer 2.1 scores have more than doubled on many Android devices. [1]

## How Did We Do It?

The improvements resulted from several changes, including:
- Build optimizations: We've made a number of changes to the way Chrome is built, which has resulted in faster code execution tuned to modern premium Android devices and SoCs.
- V8 and Blink improvements: Many improvements to the JavaScript engine (V8) and the rendering engine (Blink) have further boosted performance.
- Scheduling, OS and SoCs: We worked closely with Android partners to optimize the way Chrome interacts with the operating system and its thread scheduling to make the best use of the silicon on the devices.
Let's take a closer look at each of these areas.

## Build optimizations

The Android device ecosystem is very diverse. From entry-level phones to the newest premium ones, Chrome needs to run well on all devices. Up until last year, we shipped the same Chrome build to all these different Android devices. The memory and disk size constraints on entry-level devices resulted in Chrome having to prioritize a small binary size. Consequently, many modern build optimizations were out of reach, as they resulted in much larger binaries.
With M113, Chrome was finally able to ship a separate higher-performance build targeting premium Android devices via the Google Play Store. While we still ship a more binary-size-constrained build to other devices, this approach allowed us to land some of those modern optimizations into the new premium build:
- By targeting 64-bit Arm instead of 32-bit Arm, we can make use of more efficient Arm instruction set features and larger 64-bit operations.
- Since binary size is less relevant on premium devices with large disks and sufficient memory, we can now compile C++ code optimized for speed (-O2 / -O3) rather than size (-Oz).
- Furthermore, we tweaked the inlining thresholds used by the compiler to enable more inlining in hot code ( within and across modules ), while updating the model and policy used by another compiler pass (MLGO) to reduce inlining in cold code .
- We now also apply profile-guided optimization (PGO) techniques to the build to further improve the code layout and optimization level for hot code.
[LINK: profile-guided optimization](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/pgo.md)
- Finally, we improved cross-function code ordering by aligning Chrome's orderfile generation with the new 64-bit build. We also now include Speedometer 3 , the latest version of the industry-standard browser speed benchmark, in the workloads used to generate the orderfile.
[LINK: orderfile](https://chromium.googlesource.com/chromium/src/+/main/docs/orderfile.md)
Together, these build optimizations account for more than half of the overall Speedometer score improvements. This progress was facilitated by our collaboration with Arm, who contributed valuable insights and improvements, including to identify and address inefficiencies in Chrome's PGO setup and inlining.

## V8 and Blink improvements

Chrome continuously improves the performance of its JavaScript and web rendering engines, V8 and Blink. Most optimizations are small in individual impact, but stacked together, these improvements add up and contributed most of the remaining Speedometer impact! Notable ones include:
- We now utilize an optimized fast-path HTML parser to parse innerHTML attributes.
- V8 launched its Sparkplug compiler tier, a super fast baseline compiler that sits right above its Ignition interpreter and generates non-optimized code very quickly. Later, V8 also launched Maglev , a new mid-tier compiler that generates semi-optimized code. It takes longer to do so than Sparkplug, but much less time than Turbofan , V8's ultra-optimizing compiler tier. All together, this new tiering hierarchy allows V8 to tier up more gradually, improving both performance and power consumption.
- We tuned our heuristics that decide when garbage collection occurs, targeting times when the rendering engine is idle or when users navigate away from pages .
- We landed many other incremental optimizations, e.g. to V8 and our parsing, style, layout, and text rendering engines.

## Scheduling and OS

To achieve the best possible performance, Android partners invest heavily in tuning the operating system's thread scheduling and frequency scaling policies, as well as improving the performance of the Silicon itself.
We worked closely with our partners to improve their tuning for Chrome and Speedometer. In particular, our collaboration with Qualcomm was very fruitful: By combining optimized scheduling policies with improved hardware performance, their newest Snapdragon 8 Elite mobile platform realized a 60-80% improvement in Speedometer 3.0 compared to its predecessor, resulting in class-leading web performance. This collaboration also highlighted important bottlenecks in Chrome's code, such as the need for improved PGO and opportunities in V8.
Speedometer 3.0 on Snapdragon 8 Gen 3 (left) compared to Snapdragon 8 Elite (right), Chrome M131

## Why do these improvements matter?

Faster Speedometer scores translate to improvements in real user interactions with web content, such as faster page loads and interactions. Back at M112, loading a Google Docs document on Pixel Tablet took more than 50% longer than it does today -- that's the effect of a doubled Speedometer score!
Chrome M112 vs. M129 on Pixel Tablet, loading a Google Doc (frame count)
[LINK: Google Doc](https://docs.google.com/document/d/1-8CM2KW9OWUlsgUjXRrqYQ0dbCHoDytl7_JfeuHYFFw/edit)
[1] Speedometer 3 was released during M122, so results from Speedometer 2.1 are provided for a full picture. Measurements shown in graphs were taken on Pixel Tablet.

## Labels

- $200K 1
- 10th birthday 4
- abusive ads 1
- abusive notifications 2
- accessibility 3
- ad blockers 1
- ad blocking 2
- advanced capabilities 1
- android 2
- anti abuse 1
- anti-deception 1
- background periodic sync 1
- badging 1
- benchmarks 1
- beta 83
- better ads standards 1
- billing 1
- birthday 4
- blink 2
- browser 2
- browser interoperability 1
- bundles 1
- capabilities 6
- capable web 1
- cds 1
- cds18 2
- cds2018 1
- chrome 35
- chrome 81 1
- chrome 83 2
- chrome 84 2
- chrome ads 1
- chrome apps 5
- Chrome dev 1
- chrome dev summit 1
- chrome dev summit 2018 1
- chrome dev summit 2019 1
- chrome developer 1
[LINK: chrome developer](https://blog.chromium.org/search/label/chrome%20developer)
- Chrome Developer Center 1
[LINK: Chrome Developer Center](https://blog.chromium.org/search/label/Chrome%20Developer%20Center)
- chrome developer summit 1
[LINK: chrome developer summit](https://blog.chromium.org/search/label/chrome%20developer%20summit)
- chrome devtools 1
- Chrome extension 1
- chrome extensions 3
- Chrome Frame 1
- Chrome lite 1
- Chrome on Android 2
- chrome on ios 1
- Chrome on Mac 1
- Chrome OS 1
- chrome privacy 4
- chrome releases 1
- chrome security 10
- chrome web store 32
- chromedevtools 1
- chromeframe 3
- chromeos 4
- chromeos.dev 1
- chromium 9
- cloud print 1
- coalition 1
- coalition for better ads 1
- contact picker 1
- content indexing 1
- cookies 1
- core web vitals 2
- csrf 1
- css 1
- cumulative layout shift 1
- custom tabs 1
- dart 8
- dashboard 1
- Data Saver 3
- Data saver desktop extension 1
- day 2 1
- deceptive installation 1
- declarative net request api 1
[LINK: declarative net request api](https://blog.chromium.org/search/label/declarative%20net%20request%20api)
- design 2
- developer dashboard 1
[LINK: developer dashboard](https://blog.chromium.org/search/label/developer%20dashboard)
- Developer Program Policy 2
[LINK: Developer Program Policy](https://blog.chromium.org/search/label/Developer%20Program%20Policy)
- developer website 1
[LINK: developer website](https://blog.chromium.org/search/label/developer%20website)
- devtools 13
- digital event 1
- discoverability 1
- DNS-over-HTTPS 4
- DoH 4
- emoji 1
- emscriptem 1
- enterprise 1
- extensions 27
- Fast badging 1
- faster web 1
- features 1
- feedback 2
- field data 1
- first input delay 1
- Follow 1
- fonts 1
- form controls 1
- frameworks 1
- fugu 2
- fund 1
- funding 1
- gdd 1
- google earth 1
- google event 1
- google io 2019 1
- google web developer 1
[LINK: google web developer](https://blog.chromium.org/search/label/google%20web%20developer)
- googlechrome 12
- harmful ads 1
- html5 11
- HTTP/3 1
- HTTPS 4
- iframes 1
- images 1
- incognito 1
- insecure forms 1
- intent to explain 1
- ios 1
- ios Chrome 1
- issue tracker 3
- jank 1
- javascript 5
- lab data 1
- labelling 1
- largest contentful paint 1
- launch 1
- lazy-loading 1
- lighthouse 2
- linux 2
- Lite Mode 2
- Lite pages 1
- loading interventions 1
- loading optimizations 1
- lock icon 1
- long-tail 1
- mac 1
- manifest v3 2
- metrics 2
- microsoft edge 1
- mixed forms 1
- mobile 2
- na 1
- native client 8
- native file system 1
- New Features 5
- notifications 1
- octane 1
- open web 4
- origin trials 2
- pagespeed insights 1
- pagespeedinsights 1
- passwords 1
- payment handler 1
- payment request 1
- payments 2
- performance 20
- performance tools 1
- permission UI 1
- permissions 1
- play store 1
- portals 3
- prefetching 1
- privacy 2
- privacy sandbox 4
- private prefetch proxy 1
- profile guided optimization 1
- progressive web apps 2
- Project Strobe 1
- protection 1
- pwa 1
- QUIC 1
- quieter permissions 1
- releases 3
- removals 1
- rlz 1
- root program 1
- safe browsing 2
- Secure DNS 2
- security 36
- site isolation 1
- slow loading 1
- sms receiver 1
- spam policy 1
- spdy 2
- spectre 1
- speed 4
- ssl 2
- store listing 1
- strobe 2
- subscription pages 1
- suspicious site reporter extension 1
- TCP 1
- the fast and the curious 26
- TLS 1
- tools 1
- tracing 1
- transparency 1
- trusted web activities 1
- twa 2
- user agent string 1
- user data policy 1
- v8 6
- video 2
- wasm 1
- web 1
- web apps 1
- web assembly 2
- web developers 1
[LINK: web developers](https://blog.chromium.org/search/label/web%20developers)
- web intents 1
- web packaging 1
- web payments 1
- web platform 1
- web request api 1
[LINK: web request api](https://blog.chromium.org/search/label/web%20request%20api)
- web vitals 1
- web.dev 1
- web.dev live 1
- webapi 1
[LINK: webapi](https://blog.chromium.org/search/label/webapi)
- webassembly 1
- webaudio 3
- webgl 7
- webkit 5
- WebM 1
- webmaster 1
- webp 5
- webrtc 6
- websockets 5
- webtiming 1
- writable-files 1
- yerba beuna center for the arts 1

## Archive

-   2025 Jan May Jun Jul Oct
- Jan
- May
- Jun
- Jul
- Oct
-   2024 Feb Mar Apr May Jun Aug Dec
- Feb
- Mar
- Apr
- May
- Jun
- Aug
- Dec
-   2023 Feb Apr May Jun Aug Sep Oct Nov
- Feb
- Apr
- May
- Jun
- Aug
- Sep
- Oct
- Nov
-   2022 Jan Feb Mar Apr May Jun Aug Sep Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Aug
- Sep
- Dec
-   2021 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2020 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2019 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2018 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2017 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2016 Jan Feb Mar Apr May Jun Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Aug
- Sep
- Oct
- Nov
- Dec
-   2015 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2014 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2013 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2012 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2011 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2010 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Oct
- Nov
- Dec
-   2009 Jan Feb Mar Apr May Jun Jul Aug Sep Nov Dec
- Jan
- Feb
- Mar
- Apr
- May
- Jun
- Jul
- Aug
- Sep
- Nov
- Dec
-   2008 Sep Oct Nov Dec
- Sep
- Oct
- Nov
- Dec

## Feed

- Google
- Privacy
- Terms

--------------------