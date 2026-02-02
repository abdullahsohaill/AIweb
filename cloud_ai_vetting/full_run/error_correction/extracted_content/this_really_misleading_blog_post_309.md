# this really misleading blog post
**URL:** https://android-developers.googleblog.com/2023/11/increasing-trust-for-embedded-media.html
**Page Title:** Android Developers Blog: Increasing trust for embedded media
--------------------

[LINK: Android Developers Blog](https://android-developers.googleblog.com)
[LINK: Android Developers →](https://developer.android.com/)
[LINK: Jetpack](https://developer.android.com/jetpack)
[LINK: Kotlin](https://developer.android.com/kotlin)
[LINK: Docs](https://developer.android.com/docs)
[LINK: News](https://developer.android.com/news)
[LINK: Platform](https://developer.android.com/about)
[LINK: Android Studio](https://developer.android.com/studio)
[LINK: Google Play](https://developer.android.com/distribute)
[LINK: Jetpack](https://developer.android.com/jetpack)
[LINK: Kotlin](https://developer.android.com/kotlin)
[LINK: Docs](https://developer.android.com/docs)
[LINK: News](https://developer.android.com/news)
[LINK: Platform](https://developer.android.com/about)
[LINK: Android Studio](https://developer.android.com/studio)
[LINK: Google Play](https://developer.android.com/distribute)
[LINK: Jetpack](https://developer.android.com/jetpack)
[LINK: Kotlin](https://developer.android.com/kotlin)
[LINK: Docs](https://developer.android.com/docs)
[LINK: News](https://developer.android.com/news)
02 November 2023

## Increasing trust for embedded media

[LINK: LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://android-developers.googleblog.com/2023/11/increasing-trust-for-embedded-media.html&title=Increasing trust for embedded media)
[LINK: Twitter](https://x.com/share?text=Android Developers Blog: Increasing trust for embedded media&url=https://android-developers.googleblog.com/2023/11/increasing-trust-for-embedded-media.html&via=google)
[LINK: Facebook](https://www.facebook.com/sharer.php?u=https://android-developers.googleblog.com/2023/11/increasing-trust-for-embedded-media.html)
[LINK: Email](mailto:?subject=Increasing trust for embedded media&body=https://android-developers.googleblog.com/2023/11/increasing-trust-for-embedded-media.html)
Android WebView is a powerful and flexible API that Android developers can use to embed media in their apps, and continually improving its security and privacy protections is a top priority for our team. For example, embedded media providers should be able to verify that their media is playing in a trusted and safe environment. Android app developers and SDK providers already have solutions for this, including attestation services like the Play Integrity API and Firebase App Check , which preserve user privacy while enabling developers to verify their apps’ server requests. Today, app developers are able to pass information from these attestation services to embedded content providers; however, the current process is neither simple nor scalable. That’s why we’re piloting an experimental Android WebView Media Integrity API with select embedded media providers early next year.
[LINK: security and privacy protections](https://android-developers.googleblog.com/2023/02/improving-user-privacy-by-requiring-opt-in-to-send-x-requested-wih-header-from-webview.html)
[LINK: Play Integrity API](https://developer.android.com/google/play/integrity)
[LINK: Firebase App Check](https://firebase.google.com/docs/app-check)

### How does this relate to the Web Environment Integrity API proposal?

We’ve heard your feedback, and the Web Environment Integrity proposal is no longer being considered by the Chrome team. In contrast, the Android WebView Media Integrity API is narrowly scoped, and only targets WebViews embedded in apps. It simply extends existing functionality on Android devices that have Google Mobile Services (GMS) and there are no plans to offer it beyond embedded media, such as streaming video and audio, or beyond Android WebViews.
[LINK: Web Environment Integrity proposal](https://github.com/RupertBenWiser/Web-Environment-Integrity)

### What is the challenge with Android WebViews?

The Android WebView API lets app developers display web pages which embed media, with increased control over the UI and advanced configuration options to allow a seamless integration in the app. This brings a lot of flexibility, but it can be used as a means for fraud and abuse, because it allows app developers to access web content, and intercept or modify user interactions with it. While this has its benefits when apps embed their own web content, it does not prohibit bad actors from modifying content and, by proxy, misrepresenting its source.

### What functionality are we bringing to embedded Android WebView media?

The new Android WebView Media Integrity API will give embedded media providers access to a tailored integrity response that contains a device and app integrity verdict so that they can ensure their streams are running in a safe and trusted environment, regardless of which app store the embedding app was installed from. These verdicts are simple, low entropy metadata about the app and device and don’t contain any user or device identifiers. Unlike apps and games using Play Integrity API, media providers will not obtain the app’s Play licensing status and apps will also be able to exclude their package name from the verdict if they choose. Our goal for the API is to help sustain a thriving and diverse ecosystem of media content in Android apps, and we’re inviting media content providers to express interest in joining an early access program early next year.
[LINK: express interest](https://docs.google.com/forms/d/e/1FAIpQLSdElIyYvTpbSvw-z_u56RXIjvPCUK11klQVveadiDdnrFd-0g/viewform)
[LINK: Develop](https://android-developers.googleblog.com/search/label/Develop?max-results=12)
[LINK: play](https://android-developers.googleblog.com/search/label/play?max-results=12)
[LINK: Privacy](https://android-developers.googleblog.com/search/label/Privacy?max-results=12)
[LINK: Web](https://android-developers.googleblog.com/search/label/Web?max-results=12)
[LINK: WebView](https://android-developers.googleblog.com/search/label/WebView?max-results=12)
[LINK: WEI](https://android-developers.googleblog.com/search/label/WEI?max-results=12)
[LINK: Newer post](https://android-developers.googleblog.com/2023/11/alpha-release-of-telecom-library.html)
[LINK: Older post](https://android-developers.googleblog.com/2023/11/weareplay-meet-geraldo-from-utah-more.html)

## Google developers blog

[LINK: Google Developers Blog](https://developers.googleblog.com)

## Connect

## Subscribe

[LINK: Feed](https://android-developers.blogspot.com/atom.xml)

## Feed

[LINK: Newsletter](https://developer.android.com/newsletter/index.html)

## Newsletter


--------------------