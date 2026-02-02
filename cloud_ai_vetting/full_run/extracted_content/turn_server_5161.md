# TURN server
**URL:** https://webrtc.org/getting-started/turn-server
**Page Title:** TURN server  |  WebRTC
--------------------

- English
- Deutsch
- Español
- Español – América Latina
- Français
- Indonesia
- Italiano
- Polski
- Português
- Português – Brasil
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어
- WebRTC
- Guides

## TURN server

For most WebRTC applications to function a server is required for relaying the
traffic between peers, since a direct socket is often not possible between the
clients (unless they reside on the same local network). The common way to solve
this is by using a TURN server. The term stands for Traversal Using Relays
around NAT, and it is a protocol for relaying network traffic.
There are currently several options for TURN servers available online, both as
self-hosted applications (like the open-source COTURN project) and as cloud
provided services.
Once you have a TURN server available online, all you need is the correct RTCConfiguration for your client application to use it. The following code
snippet illustrates a sample configuration for a RTCPeerConnection where the
TURN server has the hostname my-turn-server.mycompany.com and is running on
port 19403 . The configuration object also support the username and credential properties for securing the access to the server. These are
required when connecting to a TURN server.
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2023-05-04 UTC.

--------------------