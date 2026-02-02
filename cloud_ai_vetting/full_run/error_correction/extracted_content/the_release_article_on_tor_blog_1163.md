# the release article on Tor blog
**URL:** https://blog.torproject.org/new-alpha-release-tor-browser-150a4
**Page Title:** New Alpha Release: Tor Browser 15.0a4 | The Tor Project
--------------------


## New Alpha Release: Tor Browser 15.0a4

by morgan | October 16, 2025
Tor Browser 15.0a4 is now available from the Tor Browser download page and also from our distribution directory .
This version includes important security updates to Firefox.

## Release Candidate

If all goes as planned, this will be our last alpha release in the 15.0 series before it is promoted to stable in the last week of October. Next week we will be focusing primarily on QA and ensuring all the various features and scenarios supported in Tor Browser still work as expected. This QA work will be tracked in the following gitlab issues:
- tor-browser#43984 - Tor Browser 15.0 Release QA - Desktop
- tor-browser#43985 - Tor Browser 15.0 Release QA - Android
As we reach the home stretch, now would be a great time to download and try out Tor Browser Alpha! We would appreciate it if the community would evaluate and exercise these following changes:

### 🤖 Removal of Various AI Features

Over the past year Mozilla has been working on integrating various AI features and integrations into Firefox (e.g. the AI chatbot sidebar ). Such machine learning systems and platforms are inherently un-auditable from a security and privacy perspective. We also do not want to imply recommendation or promotion of such systems by including them in Tor Browser. Therefore, we have done what we can to remove such features from the browser.

### ☁️ Rename meek-azure pluggable-transport to just meek

In the past, we have used various cloud platform to host meek pluggable-transport backends including Google, Amazon, and Azure. However, as time passed these backends have moved and migrated and thus the cloud provider-specific name has become an historical artifact. Therefore, we have dropped the Azure part of the name and now just call it meek . Let this be a lesson to you about naming things!

### 🟪 Improved Dark Theme Support in Browser Chrome

We have improved the styling for our various Tor Browser-specific UI components for  dark browser themes. All of our various purple elements should now look like they belong.

### 🦊 Removal/Replacement of New Firefox/Mozilla-specific Branding and Features

As part of ordinary incremental UI updates over the past year and the implementation of new features, Mozilla has added various new brand assets and service integrations. This includes things like those cute little fox graphics, Firefox Home, and the new History Sidebar. As of this release, there should not be any more Firefox or Mozilla specific branding, features, or service integrations accessible in Tor Browser. The new history sidebar in particular has been replaced with the legacy history panel from previous Tor Browser versions.

### 🐧 Updated Emoji Font for Linux

We have included the Noto Color Emoji font with our Linux builds. Linux users should now have all the latest and greatest emoji provided by Noto Emoji .
[LINK: Noto Emoji](https://github.com/googlefonts/noto-emoji/)

### 🈴️ Improved CJK Glyph Rendering

At the suggestion of a cypherpunk , we have swapped out the Noto font family for Jigmo . This should allow more Chinese, Japanese, and Korean graphemes to render accurately in web content.
[LINK: Jigmo](https://kamichikoichi.github.io/jigmo/)

### ✉️ Letterboxing Styling Improvements

We have tweaked our custom styling of the web-content letterboxing feature to confirm with and adapt to Firefox's own styling changes in Firefox 140. These tweaks should also play nicely with upstream's vertical tabs feature.

### 🚫 WebAssembly Restrictions Now Managed by NoScript

Historically, we have disabled WebAssembly globally when the browser is in the Safer and Safest security levels. However, with the latest Firefox version this has proven to be too aggressive, as doing so broke functionality in the built-in PDF reader . We therefore now rely on the NoScript extension built into the browser to handle disabling WebAssembly functionality in web content while the browser is in the Safer and Safest security levels, while also allowing WebAssembly to run unhindered in safe+privileged contexts like the PDF reader.
[LINK: WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly)

### 🔍 Stopped Hiding Protocol in URL on Desktop

Mozilla has reversed course on when the protocol portion (e.g. http or https ) of the URL in the URL bar is hidden since Firefox 128. We used to have logic in one of our patches around Onion Services (which are always end-to-end encrypted regardless of the application-level protocol used) to follow whatever Firefox does for https . However, with the latest changes in Firefox, this patch became a bit gnarly to apply correctly so we took a step back and thought to ourselves, why are we even conditionally hiding this from the user?
So for now, we have decided not to hide the protocol from the user on Desktop platforms using a supported Firefox pref. We continue to follow upstream and always hide the protocol in the URL bar on Android (where horizontal space is at a premium). Users of Tor Browser Android can simply click the icon in the URL bar to get all the info about a websites HTTPS usage.

## Send us your feedback

If you find a bug or have a suggestion for how we could improve this release, please let us know .
⚠️ Reminder : Tor Browser Alpha release channel is for testing only . If you are at risk or need strong anonymity, stick with the stable release channel .

## Full changelog

The full changelog since Tor Browser 15.0a3 is:
[LINK: full changelog](https://gitlab.torproject.org/tpo/applications/tor-browser-build/-/raw/main/projects/browser/Bundle-Data/Docs-TBB/ChangeLog.txt)
- All Platforms Updated NoScript to 13.2.1 Updated OpenSSL to 3.5.4 Bug tor-browser#19741 : Opensearch (contextual search) does not obey FPI Bug tor-browser#43850 : Modify the Contrast Control settings for RFP Bug tor-browser#43869 : Hide pens with RFP Bug tor-browser#44068 : Handle migration from meek-azure to meek built-in bridge type Bug tor-browser#44234 : No images in PDF Bug tor-browser#44240 : Typo on dom.security.https_first_add_exception_on_failure Bug tor-browser#44242 : Hand over Security Level's WebAssembly controls  to NoScript Bug tor-browser#44250 : Rebase Tor Browser Alpha onto 140.4esr Bug tor-browser-build#41574 : Update Snowflake builtin bridge lines
- Updated NoScript to 13.2.1
- Updated OpenSSL to 3.5.4
- Bug tor-browser#19741 : Opensearch (contextual search) does not obey FPI
- Bug tor-browser#43850 : Modify the Contrast Control settings for RFP
- Bug tor-browser#43869 : Hide pens with RFP
- Bug tor-browser#44068 : Handle migration from meek-azure to meek built-in bridge type
- Bug tor-browser#44234 : No images in PDF
- Bug tor-browser#44240 : Typo on dom.security.https_first_add_exception_on_failure
- Bug tor-browser#44242 : Hand over Security Level's WebAssembly controls  to NoScript
- Bug tor-browser#44250 : Rebase Tor Browser Alpha onto 140.4esr
- Bug tor-browser-build#41574 : Update Snowflake builtin bridge lines
- Windows + macOS + Linux Updated Firefox to 140.4.0esr Bug tor-browser#43900 : Open newtab rather than firefoxview when unloading the last tab Bug tor-browser#44101 : Toolbar connection status is not visible when using vertical tabs Bug tor-browser#44107 : Switch tab search action is missing an icon Bug tor-browser#44108 : Fix the new history sidebar Bug tor-browser#44123 : Do not trim protocol off of URLs ever Bug tor-browser#44153 : Test search engines Bug tor-browser#44159 : Change or hide the sidebar settings description Bug tor-browser#44177 : Remove more urlbar actions Bug tor-browser#44178 : Search preservation does not work with duckduckgo in safest security level Bug tor-browser#44184 : Duckduckgo Onion Lite search does not work properly in safest when added as a search engine Bug tor-browser#44187 : TLS session tickets leak Private Browsing mode Bug tor-browser#44192 : Hovering unloaded tab causes console error Bug tor-browser#44213 : Reduce linkability concerns of the "Search with" contextual search action Bug tor-browser#44214 : Update letterboxing to reflect changes in ESR 140 Bug tor-browser#44215 : Hide Firefox home settings in about:preferences Bug tor-browser#44221 : Backport MozBug 1984333 Bump Spoofed Processor Count Bug tor-browser#44239 : DDG HTML page and search results displayed incorrectly with Safest security setting Bug tor-browser#44262 : Disable adding search engines from HTML forms
- Updated Firefox to 140.4.0esr
- Bug tor-browser#43900 : Open newtab rather than firefoxview when unloading the last tab
- Bug tor-browser#44101 : Toolbar connection status is not visible when using vertical tabs
- Bug tor-browser#44107 : Switch tab search action is missing an icon
- Bug tor-browser#44108 : Fix the new history sidebar
- Bug tor-browser#44123 : Do not trim protocol off of URLs ever
- Bug tor-browser#44153 : Test search engines
- Bug tor-browser#44159 : Change or hide the sidebar settings description
- Bug tor-browser#44177 : Remove more urlbar actions
- Bug tor-browser#44178 : Search preservation does not work with duckduckgo in safest security level
- Bug tor-browser#44184 : Duckduckgo Onion Lite search does not work properly in safest when added as a search engine
- Bug tor-browser#44187 : TLS session tickets leak Private Browsing mode
- Bug tor-browser#44192 : Hovering unloaded tab causes console error
- Bug tor-browser#44213 : Reduce linkability concerns of the "Search with" contextual search action
- Bug tor-browser#44214 : Update letterboxing to reflect changes in ESR 140
- Bug tor-browser#44215 : Hide Firefox home settings in about:preferences
- Bug tor-browser#44221 : Backport MozBug 1984333 Bump Spoofed Processor Count
- Bug tor-browser#44239 : DDG HTML page and search results displayed incorrectly with Safest security setting
- Bug tor-browser#44262 : Disable adding search engines from HTML forms
- Linux Bug tor-browser#44227 : Some CJK characters cannot be rendered by Tor which uses the Noto font family Bug tor-browser-build#41586 : Replace Noto CJK with Jigmo on Linux
- Bug tor-browser#44227 : Some CJK characters cannot be rendered by Tor which uses the Noto font family
- Bug tor-browser-build#41586 : Replace Noto CJK with Jigmo on Linux
- Android Updated GeckoView to 140.4.0esr Bug tor-browser#43401 : Replace the constructor of Locale with a builder Bug tor-browser#43643 : Clean out unused tor connect strings Bug tor-browser#43650 : Survey banner behaves like a dialog on Android, rather than a card Bug tor-browser#43676 : Preemptively disable unified trust panel by default so we are tracking for next ESR Bug tor-browser#44031 : Implement YEC 2025 Takeover for Android Stable Bug tor-browser#44218 : Tor Browser Alpha for Android (15.0a2) doesn't work on Huawei devices P20 and P30 Bug tor-browser#44237 : Revoke access to all advertising ids available in Android
- Updated GeckoView to 140.4.0esr
- Bug tor-browser#43401 : Replace the constructor of Locale with a builder
- Bug tor-browser#43643 : Clean out unused tor connect strings
- Bug tor-browser#43650 : Survey banner behaves like a dialog on Android, rather than a card
- Bug tor-browser#43676 : Preemptively disable unified trust panel by default so we are tracking for next ESR
- Bug tor-browser#44031 : Implement YEC 2025 Takeover for Android Stable
- Bug tor-browser#44218 : Tor Browser Alpha for Android (15.0a2) doesn't work on Huawei devices P20 and P30
- Bug tor-browser#44237 : Revoke access to all advertising ids available in Android
- Build System All Platforms Bug tor-browser-build#41568 : Update instructions for manually building 7zip Bug tor-browser-build#41576 : Build expert bundles outside containers Bug tor-browser-build#41579 : Add zip to the list of Tor Browser Build dependencies Bug tor-browser-build#41588 : Restore legacy channel support in projects/release/update_responses_config.yml Bug tor-browser-build#41589 : Backport tor-browser-build-browser#41270: Add updater rewriterules to make 13.5.7 a watershed Windows + macOS + Linux Bug tor-browser-build#41373 : Remove _ALL from mar filenames Bug tor-browser#44131 : Generate torrc-defaults and put it in objdir post-build Windows + Linux + Android Updated Go to 1.24.9 Windows Bug tor-browser#44167 : Move the nsis-uninstall.patch to tor-browser repository macOS Bug tor-browser-build#41571 : Work-around to prevent older 7z versions to break rcodesign. Linux Bug tor-browser-build#41558 : Share descriptions between Linux packages and archives Bug tor-browser-build#41569 : Use var/display_name in .desktop files Android Bug tor-browser#44220 : Disable the JS minifier as it produces invalid JS Bug tor-browser-build#41577 : Minify JS with UglifyJS on Android x86 Bug tor-browser-build#41582 : Drop --pack-dyn-relocs=relr Bug tor-browser-build#41583 : Align tor and PTs to 16kB on Android
- All Platforms Bug tor-browser-build#41568 : Update instructions for manually building 7zip Bug tor-browser-build#41576 : Build expert bundles outside containers Bug tor-browser-build#41579 : Add zip to the list of Tor Browser Build dependencies Bug tor-browser-build#41588 : Restore legacy channel support in projects/release/update_responses_config.yml Bug tor-browser-build#41589 : Backport tor-browser-build-browser#41270: Add updater rewriterules to make 13.5.7 a watershed
- Bug tor-browser-build#41568 : Update instructions for manually building 7zip
- Bug tor-browser-build#41576 : Build expert bundles outside containers
- Bug tor-browser-build#41579 : Add zip to the list of Tor Browser Build dependencies
- Bug tor-browser-build#41588 : Restore legacy channel support in projects/release/update_responses_config.yml
- Bug tor-browser-build#41589 : Backport tor-browser-build-browser#41270: Add updater rewriterules to make 13.5.7 a watershed
- Windows + macOS + Linux Bug tor-browser-build#41373 : Remove _ALL from mar filenames Bug tor-browser#44131 : Generate torrc-defaults and put it in objdir post-build
- Bug tor-browser-build#41373 : Remove _ALL from mar filenames
- Bug tor-browser#44131 : Generate torrc-defaults and put it in objdir post-build
- Windows + Linux + Android Updated Go to 1.24.9
- Updated Go to 1.24.9
- Windows Bug tor-browser#44167 : Move the nsis-uninstall.patch to tor-browser repository
- Bug tor-browser#44167 : Move the nsis-uninstall.patch to tor-browser repository
- macOS Bug tor-browser-build#41571 : Work-around to prevent older 7z versions to break rcodesign.
- Bug tor-browser-build#41571 : Work-around to prevent older 7z versions to break rcodesign.
- Linux Bug tor-browser-build#41558 : Share descriptions between Linux packages and archives Bug tor-browser-build#41569 : Use var/display_name in .desktop files
- Bug tor-browser-build#41558 : Share descriptions between Linux packages and archives
- Bug tor-browser-build#41569 : Use var/display_name in .desktop files
- Android Bug tor-browser#44220 : Disable the JS minifier as it produces invalid JS Bug tor-browser-build#41577 : Minify JS with UglifyJS on Android x86 Bug tor-browser-build#41582 : Drop --pack-dyn-relocs=relr Bug tor-browser-build#41583 : Align tor and PTs to 16kB on Android
- Bug tor-browser#44220 : Disable the JS minifier as it produces invalid JS
- Bug tor-browser-build#41577 : Minify JS with UglifyJS on Android x86
- Bug tor-browser-build#41582 : Drop --pack-dyn-relocs=relr
- Bug tor-browser-build#41583 : Align tor and PTs to 16kB on Android
- applications
- releases

## Comments

We encourage respectful, on-topic comments. Comments that violate our Code of Conduct will be deleted. Off-topic comments may be deleted at the discretion of
	  the moderators. Please do not comment as a way to receive support or to
	  report bugs on a post unrelated to a release. If you are looking for
	  support, please see our FAQ , user support forum or ways to get in touch with us .

--------------------