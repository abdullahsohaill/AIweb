# Chrome Extension API
**URL:** https://developer.chrome.com/docs/extensions/reference/api
**Page Title:** API reference  |  Chrome for Developers
--------------------

- English
[LINK: English](https://developer.chrome.com/docs/extensions/reference/api)
- Deutsch
[LINK: Deutsch](https://developer.chrome.com/docs/extensions/reference/api?hl=de)
- Español – América Latina
[LINK: Español – América Latina](https://developer.chrome.com/docs/extensions/reference/api?hl=es-419)
- Français
[LINK: Français](https://developer.chrome.com/docs/extensions/reference/api?hl=fr)
- Indonesia
[LINK: Indonesia](https://developer.chrome.com/docs/extensions/reference/api?hl=id)
- Italiano
[LINK: Italiano](https://developer.chrome.com/docs/extensions/reference/api?hl=it)
- Nederlands
[LINK: Nederlands](https://developer.chrome.com/docs/extensions/reference/api?hl=nl)
- Polski
[LINK: Polski](https://developer.chrome.com/docs/extensions/reference/api?hl=pl)
- Português – Brasil
[LINK: Português – Brasil](https://developer.chrome.com/docs/extensions/reference/api?hl=pt-br)
- Tiếng Việt
[LINK: Tiếng Việt](https://developer.chrome.com/docs/extensions/reference/api?hl=vi)
- Türkçe
[LINK: Türkçe](https://developer.chrome.com/docs/extensions/reference/api?hl=tr)
- Русский
[LINK: Русский](https://developer.chrome.com/docs/extensions/reference/api?hl=ru)
- עברית
[LINK: עברית](https://developer.chrome.com/docs/extensions/reference/api?hl=he)
- العربيّة
[LINK: العربيّة](https://developer.chrome.com/docs/extensions/reference/api?hl=ar)
- فارسی
[LINK: فارسی](https://developer.chrome.com/docs/extensions/reference/api?hl=fa)
- हिंदी
[LINK: हिंदी](https://developer.chrome.com/docs/extensions/reference/api?hl=hi)
- বাংলা
[LINK: বাংলা](https://developer.chrome.com/docs/extensions/reference/api?hl=bn)
- ภาษาไทย
[LINK: ภาษาไทย](https://developer.chrome.com/docs/extensions/reference/api?hl=th)
- 中文 – 简体
[LINK: 中文 – 简体](https://developer.chrome.com/docs/extensions/reference/api?hl=zh-cn)
- 中文 – 繁體
[LINK: 中文 – 繁體](https://developer.chrome.com/docs/extensions/reference/api?hl=zh-tw)
- 日本語
[LINK: 日本語](https://developer.chrome.com/docs/extensions/reference/api?hl=ja)
- 한국어
[LINK: 한국어](https://developer.chrome.com/docs/extensions/reference/api?hl=ko)
[LINK: Sign in](https://developer.chrome.com/_d/signin?continue=https%3A%2F%2Fdeveloper.chrome.com%2Fdocs%2Fextensions%2Freference%2Fapi&prompt=select_account)
- Chrome Extensions
[LINK: Chrome Extensions](https://developer.chrome.com/docs/extensions)
- Reference
[LINK: Reference](https://developer.chrome.com/docs/extensions/reference)
- API
[LINK: API](https://developer.chrome.com/docs/extensions/reference/api)
- On this page
- Common Extensions API features
[LINK: Common Extensions API features](#common_extensions_api_features)
- Chrome Extension APIs
[LINK: Chrome Extension APIs](#chrome_extension_apis)
- Home
[LINK: Home](https://developer.chrome.com/)
- Docs
[LINK: Docs](https://developer.chrome.com/docs)
- Chrome Extensions
[LINK: Chrome Extensions](https://developer.chrome.com/docs/extensions)
- Reference
[LINK: Reference](https://developer.chrome.com/docs/extensions/reference)
- API
[LINK: API](https://developer.chrome.com/docs/extensions/reference/api)

## API reference Stay organized with collections Save and categorize content based on your preferences.

- On this page
- Common Extensions API features
[LINK: Common Extensions API features](#common_extensions_api_features)
- Chrome Extension APIs
[LINK: Chrome Extension APIs](#chrome_extension_apis)
Most extensions need access to one or more Chrome Extensions APIs to function. This API reference describes the APIs available
for use in extensions and presents example use cases.
Beginning in Chrome 144, all Chrome Extension APIs are also available under the browser namespace (e.g. browser.tabs.create({}) ). This is an alias for the chrome namespace (e.g. chrome.tabs.create({}) ) provided for compatibility
with other browsers that use the browser namespace for their extension APIs.

## Common Extensions API features

An Extensions API consists of a namespace containing methods and properties for doing extensions work, and usually, but not
always, manifest fields for the manifest.json file. For example, the chrome.action namespace requires an "action" object
in the manifest. Many APIs also require permissions in the manifest.
[LINK: permissions](/docs/extensions/mv3/declare_permissions)
Methods in extension APIs are asynchronous unless stated otherwise. Asynchronous methods return immediately, without waiting
for the operation that calls them to finish. Use promises to get the results of these asynchronous methods.
[LINK: promises](https://developer.mozilla.org/docs/Learn/JavaScript/Asynchronous/Promises)

## Chrome Extension APIs

[LINK: accessibilityFeatures](/docs/extensions/reference/api/accessibilityFeatures)
Use the chrome.accessibilityFeatures API to manage Chrome's accessibility features. This API relies on the ChromeSetting prototype of the type API for getting and setting individual accessibility features. In order to get feature states the extension must request accessibilityFeatures.read permission. For modifying feature state, the extension needs accessibilityFeatures.modify permission. Note that accessibilityFeatures.modify does not imply accessibilityFeatures.read permission.
[LINK: ChromeSetting prototype of the type API](https://developer.chrome.com/docs/extensions/reference/types/#ChromeSetting)
[LINK: action](/docs/extensions/reference/api/action)
Use the chrome.action API to control the extension's icon in the Google Chrome toolbar.
[LINK: alarms](/docs/extensions/reference/api/alarms)
Use the chrome.alarms API to schedule code to run periodically or at a specified time in the future.
[LINK: audio](/docs/extensions/reference/api/audio)
The chrome.audio API is provided to allow users to get information about and control the audio devices attached to the system. This API is currently only available in kiosk mode for ChromeOS.
[LINK: bookmarks](/docs/extensions/reference/api/bookmarks)
Use the chrome.bookmarks API to create, organize, and otherwise manipulate bookmarks. Also see Override Pages , which you can use to create a custom Bookmark Manager page.
[LINK: Override Pages](https://developer.chrome.com/docs/extensions/override)
[LINK: browsingData](/docs/extensions/reference/api/browsingData)
Use the chrome.browsingData API to remove browsing data from a user's local profile.
[LINK: certificateProvider](/docs/extensions/reference/api/certificateProvider)
Use this API to expose certificates to the platform which can use these certificates for TLS authentications.
[LINK: commands](/docs/extensions/reference/api/commands)
Use the commands API to add keyboard shortcuts that trigger actions in your extension, for example, an action to open the browser action or send a command to the extension.
[LINK: contentSettings](/docs/extensions/reference/api/contentSettings)
Use the chrome.contentSettings API to change settings that control whether websites can use features such as cookies, JavaScript, and plugins. More generally speaking, content settings allow you to customize Chrome's behavior on a per-site basis instead of globally.
[LINK: contextMenus](/docs/extensions/reference/api/contextMenus)
Use the chrome.contextMenus API to add items to Google Chrome's context menu. You can choose what types of objects your context menu additions apply to, such as images, hyperlinks, and pages.
[LINK: cookies](/docs/extensions/reference/api/cookies)
Use the chrome.cookies API to query and modify cookies, and to be notified when they change.
[LINK: debugger](/docs/extensions/reference/api/debugger)
The chrome.debugger API serves as an alternate transport for Chrome's remote debugging protocol . Use chrome.debugger to attach to one or more tabs to instrument network interaction, debug JavaScript, mutate the DOM and CSS, and more. Use the Debuggee property tabId to target tabs with sendCommand and route events by tabId from onEvent callbacks.
[LINK: remote debugging protocol](https://developer.chrome.com/devtools/docs/debugger-protocol)
[LINK: declarativeContent](/docs/extensions/reference/api/declarativeContent)
Use the chrome.declarativeContent API to take actions depending on the content of a page, without requiring permission to read the page's content.
[LINK: declarativeNetRequest](/docs/extensions/reference/api/declarativeNetRequest)
The chrome.declarativeNetRequest API is used to block or modify network requests by specifying declarative rules. This lets extensions modify network requests without intercepting them and viewing their content, thus providing more privacy.
[LINK: desktopCapture](/docs/extensions/reference/api/desktopCapture)
The Desktop Capture API captures the content of the screen, individual windows, or individual tabs.
[LINK: devtools.inspectedWindow](/docs/extensions/reference/api/devtools/inspectedWindow)
Use the chrome.devtools.inspectedWindow API to interact with the inspected window: obtain the tab ID for the inspected page, evaluate the code in the context of the inspected window, reload the page, or obtain the list of resources within the page.
[LINK: devtools.network](/docs/extensions/reference/api/devtools/network)
Use the chrome.devtools.network API to retrieve the information about network requests displayed by the Developer Tools in the Network panel.
[LINK: devtools.panels](/docs/extensions/reference/api/devtools/panels)
Use the chrome.devtools.panels API to integrate your extension into Developer Tools window UI: create your own panels, access existing panels, and add sidebars.
[LINK: devtools.performance](/docs/extensions/reference/api/devtools/performance)
Use the chrome.devtools.performance API to listen to recording status updates in the Performance panel in DevTools.
[LINK: devtools.recorder](/docs/extensions/reference/api/devtools/recorder)
Use the chrome.devtools.recorder API to customize the Recorder panel in DevTools.
[LINK: dns](/docs/extensions/reference/api/dns)
Use the chrome.dns API for dns resolution.
[LINK: documentScan](/docs/extensions/reference/api/documentScan)
Use the chrome.documentScan API to discover and retrieve images from attached document scanners.
[LINK: dom](/docs/extensions/reference/api/dom)
Use the chrome.dom API to access special DOM APIs for Extensions
[LINK: downloads](/docs/extensions/reference/api/downloads)
Use the chrome.downloads API to programmatically initiate, monitor, manipulate, and search for downloads.
[LINK: enterprise.deviceAttributes](/docs/extensions/reference/api/enterprise/deviceAttributes)
Use the chrome.enterprise.deviceAttributes API to read device attributes. Note: This API is only available to extensions force-installed by enterprise policy.
[LINK: enterprise.hardwarePlatform](/docs/extensions/reference/api/enterprise/hardwarePlatform)
Use the chrome.enterprise.hardwarePlatform API to get the manufacturer and model of the hardware platform where the browser runs. Note: This API is only available to extensions installed by enterprise policy.
[LINK: enterprise.login](/docs/extensions/reference/api/enterprise/login)
Use the chrome.enterprise.login API to exit Managed Guest sessions. Note: This API is only available to extensions installed by enterprise policy in ChromeOS Managed Guest sessions.
[LINK: enterprise.networkingAttributes](/docs/extensions/reference/api/enterprise/networkingAttributes)
Use the chrome.enterprise.networkingAttributes API to read information about your current network. Note: This API is only available to extensions force-installed by enterprise policy.
[LINK: enterprise.platformKeys](/docs/extensions/reference/api/enterprise/platformKeys)
Use the chrome.enterprise.platformKeys API to generate keys and install certificates for these keys. The certificates will be managed by the platform and can be used for TLS authentication, network access or by other extension through chrome.platformKeys.
[LINK: events](/docs/extensions/reference/api/events)
The chrome.events namespace contains common types used by APIs dispatching events to notify you when something interesting happens.
[LINK: extension](/docs/extensions/reference/api/extension)
The chrome.extension API has utilities that can be used by any extension page. It includes support for exchanging messages between an extension and its content scripts or between extensions, as described in detail in Message Passing .
[LINK: Message Passing](https://developer.chrome.com/docs/extensions/messaging)
[LINK: extensionTypes](/docs/extensions/reference/api/extensionTypes)
The chrome.extensionTypes API contains type declarations for Chrome extensions.
[LINK: fileBrowserHandler](/docs/extensions/reference/api/fileBrowserHandler)
Use the chrome.fileBrowserHandler API to extend the Chrome OS file browser. For example, you can use this API to enable users to upload files to your website.
[LINK: fileSystemProvider](/docs/extensions/reference/api/fileSystemProvider)
Use the chrome.fileSystemProvider API to create file systems, that can be accessible from the file manager on Chrome OS.
[LINK: fontSettings](/docs/extensions/reference/api/fontSettings)
Use the chrome.fontSettings API to manage Chrome's font settings.
[LINK: gcm](/docs/extensions/reference/api/gcm)
Use chrome.gcm to enable apps and extensions to send and receive messages through Firebase Cloud Messaging (FCM).
[LINK: Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
[LINK: history](/docs/extensions/reference/api/history)
Use the chrome.history API to interact with the browser's record of visited pages. You can add, remove, and query for URLs in the browser's history. To override the history page with your own version, see Override Pages .
[LINK: Override Pages](https://developer.chrome.com/extensions/develop/ui/override-chrome-pages)
[LINK: i18n](/docs/extensions/reference/api/i18n)
Use the chrome.i18n infrastructure to implement internationalization across your whole app or extension.
[LINK: identity](/docs/extensions/reference/api/identity)
Use the chrome.identity API to get OAuth2 access tokens.
[LINK: idle](/docs/extensions/reference/api/idle)
Use the chrome.idle API to detect when the machine's idle state changes.
[LINK: input.ime](/docs/extensions/reference/api/input/ime)
Use the chrome.input.ime API to implement a custom IME for Chrome OS. This allows your extension to handle keystrokes, set the composition, and manage the candidate window.
[LINK: instanceID](/docs/extensions/reference/api/instanceID)
Use chrome.instanceID to access the Instance ID service.
[LINK: loginState](/docs/extensions/reference/api/loginState)
Use the chrome.loginState API to read and monitor the login state.
[LINK: management](/docs/extensions/reference/api/management)
The chrome.management API provides ways to manage installed apps and extensions.
[LINK: notifications](/docs/extensions/reference/api/notifications)
Use the chrome.notifications API to create rich notifications using templates and show these notifications to users in the system tray.
[LINK: offscreen](/docs/extensions/reference/api/offscreen)
Use the offscreen API to create and manage offscreen documents.
[LINK: omnibox](/docs/extensions/reference/api/omnibox)
The omnibox API allows you to register a keyword with Google Chrome's address bar, which is also known as the omnibox.
[LINK: pageCapture](/docs/extensions/reference/api/pageCapture)
Use the chrome.pageCapture API to save a tab as MHTML.
[LINK: permissions](/docs/extensions/reference/api/permissions)
Use the chrome.permissions API to request declared optional permissions at run time rather than install time, so users understand why the permissions are needed and grant only those that are necessary.
[LINK: declared optional permissions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions)
[LINK: platformKeys](/docs/extensions/reference/api/platformKeys)
Use the chrome.platformKeys API to access client certificates managed by the platform. If the user or policy grants the permission, an extension can use such a certficate in its custom authentication protocol. E.g. this allows usage of platform managed certificates in third party VPNs (see chrome.vpnProvider ).
[LINK: chrome.vpnProvider](/docs/extensions/reference/api/vpnProvider)
[LINK: power](/docs/extensions/reference/api/power)
Use the chrome.power API to override the system's power management features.
[LINK: printerProvider](/docs/extensions/reference/api/printerProvider)
The chrome.printerProvider API exposes events used by print manager to query printers controlled by extensions, to query their capabilities and to submit print jobs to these printers.
[LINK: printing](/docs/extensions/reference/api/printing)
Use the chrome.printing API to send print jobs to printers installed on Chromebook.
[LINK: printingMetrics](/docs/extensions/reference/api/printingMetrics)
Use the chrome.printingMetrics API to fetch data about printing usage.
[LINK: privacy](/docs/extensions/reference/api/privacy)
Use the chrome.privacy API to control usage of the features in Chrome that can affect a user's privacy. This API relies on the ChromeSetting prototype of the type API for getting and setting Chrome's configuration.
[LINK: ChromeSetting prototype of the type API](https://developer.chrome.com/docs/extensions/reference/types/#ChromeSetting)
[LINK: processes](/docs/extensions/reference/api/processes)
Use the chrome.processes API to interact with the browser's processes.
[LINK: proxy](/docs/extensions/reference/api/proxy)
Use the chrome.proxy API to manage Chrome's proxy settings. This API relies on the ChromeSetting prototype of the type API for getting and setting the proxy configuration.
[LINK: ChromeSetting prototype of the type API](https://developer.chrome.com/docs/extensions/reference/api/types#type-ChromeSetting)
[LINK: readingList](/docs/extensions/reference/api/readingList)
Use the chrome.readingList API to read from and modify the items in the Reading List .
[LINK: runtime](/docs/extensions/reference/api/runtime)
Use the chrome.runtime API to retrieve the service worker, return details about the manifest, and listen for and respond to events in the extension lifecycle. You can also use this API to convert the relative path of URLs to fully-qualified URLs.
[LINK: scripting](/docs/extensions/reference/api/scripting)
Use the chrome.scripting API to execute script in different contexts.
[LINK: search](/docs/extensions/reference/api/search)
Use the chrome.search API to search via the default provider.
[LINK: sessions](/docs/extensions/reference/api/sessions)
Use the chrome.sessions API to query and restore tabs and windows from a browsing session.
[LINK: sidePanel](/docs/extensions/reference/api/sidePanel)
Use the chrome.sidePanel API to host content in the browser's side panel alongside the main content of a webpage.
[LINK: storage](/docs/extensions/reference/api/storage)
Use the chrome.storage API to store, retrieve, and track changes to user data.
[LINK: system.cpu](/docs/extensions/reference/api/system/cpu)
Use the system.cpu API to query CPU metadata.
[LINK: system.display](/docs/extensions/reference/api/system/display)
Use the system.display API to query display metadata.
[LINK: system.memory](/docs/extensions/reference/api/system/memory)
The chrome.system.memory API.
[LINK: system.storage](/docs/extensions/reference/api/system/storage)
Use the chrome.system.storage API to query storage device information and be notified when a removable storage device is attached and detached.
[LINK: systemLog](/docs/extensions/reference/api/systemLog)
Use the chrome.systemLog API to record Chrome system logs from extensions.
[LINK: tabCapture](/docs/extensions/reference/api/tabCapture)
Use the chrome.tabCapture API to interact with tab media streams.
[LINK: tabGroups](/docs/extensions/reference/api/tabGroups)
Use the chrome.tabGroups API to interact with the browser's tab grouping system. You can use this API to modify and rearrange tab groups in the browser. To group and ungroup tabs, or to query what tabs are in groups, use the chrome.tabs API.
[LINK: tabs](/docs/extensions/reference/api/tabs)
Use the chrome.tabs API to interact with the browser's tab system. You can use this API to create, modify, and rearrange tabs in the browser.
[LINK: topSites](/docs/extensions/reference/api/topSites)
Use the chrome.topSites API to access the top sites (i.e. most visited sites) that are displayed on the new tab page. These do not include shortcuts customized by the user.
[LINK: tts](/docs/extensions/reference/api/tts)
Use the chrome.tts API to play synthesized text-to-speech (TTS). See also the related ttsEngine API, which allows an extension to implement a speech engine.
[LINK: ttsEngine](/docs/extensions/reference/api/ttsEngine)
[LINK: ttsEngine](/docs/extensions/reference/api/ttsEngine)
Use the chrome.ttsEngine API to implement a text-to-speech(TTS) engine using an extension. If your extension registers using this API, it will receive events containing an utterance to be spoken and other parameters when any extension or Chrome App uses the tts API to generate speech. Your extension can then use any available web technology to synthesize and output the speech, and send events back to the calling function to report the status.
[LINK: tts](/docs/extensions/reference/api/tts)
[LINK: types](/docs/extensions/reference/api/types)
The chrome.types API contains type declarations for Chrome.
[LINK: userScripts](/docs/extensions/reference/api/userScripts)
Use the userScripts API to execute user scripts in the User Scripts context.
[LINK: vpnProvider](/docs/extensions/reference/api/vpnProvider)
Use the chrome.vpnProvider API to implement a VPN client.
[LINK: wallpaper](/docs/extensions/reference/api/wallpaper)
Use the chrome.wallpaper API to change the ChromeOS wallpaper.
[LINK: webAuthenticationProxy](/docs/extensions/reference/api/webAuthenticationProxy)
The chrome.webAuthenticationProxy API lets remote desktop software running on a remote host intercept Web Authentication API (WebAuthn) requests in order to handle them on a local client.
[LINK: webNavigation](/docs/extensions/reference/api/webNavigation)
Use the chrome.webNavigation API to receive notifications about the status of navigation requests in-flight.
[LINK: webRequest](/docs/extensions/reference/api/webRequest)
Use the chrome.webRequest API to observe and analyze traffic and to intercept, block, or modify requests in-flight.
[LINK: windows](/docs/extensions/reference/api/windows)
Use the chrome.windows API to interact with browser windows. You can use this API to create, modify, and rearrange windows in the browser.
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.
[LINK: Google Developers Site Policies](https://developers.google.com/site-policies)
Last updated 2025-12-11 UTC.

--------------------