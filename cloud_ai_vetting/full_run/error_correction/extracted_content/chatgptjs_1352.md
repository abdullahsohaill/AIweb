# chatgpt.js
**URL:** https://chatgpt.js.org
**Page Title:** chatgpt.js — A powerful client-side JavaScript library for ChatGPT
--------------------

🤖 A Feature-rich Client-SIde javaSCRIpT lIbRaRY FOR CHAtgpT_
GitHub Get Started
[LINK: GitHub](https://github.com/KudoAI/chatgpt.js)
[LINK: 简体中文](https://github.com/KudoAI/chatgpt.js/tree/main/docs/zh-cn#readme)
[LINK: 繁體中文](https://github.com/KudoAI/chatgpt.js/tree/main/docs/zh-tw#readme)
[LINK: 한국인](https://github.com/KudoAI/chatgpt.js/tree/main/docs/ko#readme)
[LINK: हिंदी](https://github.com/KudoAI/chatgpt.js/tree/main/docs/hi#readme)
[LINK: नेपाली](https://github.com/KudoAI/chatgpt.js/tree/main/docs/ne#readme)
[LINK: Deutsch](https://github.com/KudoAI/chatgpt.js/tree/main/docs/de#readme)
[LINK: Español](https://github.com/KudoAI/chatgpt.js/tree/main/docs/es#readme)
[LINK: Français](https://github.com/KudoAI/chatgpt.js/tree/main/docs/fr#readme)
[LINK: Italiano](https://github.com/KudoAI/chatgpt.js/tree/main/docs/it#readme)
[LINK: Nederlands](https://github.com/KudoAI/chatgpt.js/tree/main/docs/nl#readme)
[LINK: Português](https://github.com/KudoAI/chatgpt.js/tree/main/docs/pt#readme)
[LINK: Английский](https://github.com/KudoAI/chatgpt.js/tree/main/docs/ru#readme)
[LINK: Việt](https://github.com/KudoAI/chatgpt.js/tree/main/docs/vi#readme)

### 🤖 A powerful client-side JavaScript library for ChatGPT

## 💡 About

chatgpt.js is a powerful JavaScript library that allows for super easy interaction w/ the ChatGPT DOM.
- Feature-rich
- Object-oriented
- Easy-to-use
- Lightweight (yet optimally performant)

### Supported by:

### Warp, the AI Devtool that lives in your terminal

## ⚡ Importing the library

[!NOTE]
To always import the latest version (not recommended in production!) replace the versioned jsDelivr URL with: https://cdn.jsdelivr.net/npm/@kudoai/chatgpt.js/chatgpt.min.js

### ES11 (2020):

### ES5 (2009):

### Greasemonkey:

[!NOTE]
To use a starter template: kudoai/chatgpt.js-greasemonkey-starter
[LINK: kudoai/chatgpt.js-greasemonkey-starter](https://github.com/KudoAI/chatgpt.js-greasemonkey-starter)

### Chrome:

[!NOTE]
To use a starter template: kudoai/chatgpt.js-chrome-starter
[LINK: kudoai/chatgpt.js-chrome-starter](https://github.com/KudoAI/chatgpt.js-chrome-starter)
Since Google does not allow remote code, importing chatgpt.js locally is required:
- Save https://raw.githubusercontent.com/KudoAI/chatgpt.js/main/chatgpt.js to a subdirectory ( lib in this example)
Save https://raw.githubusercontent.com/KudoAI/chatgpt.js/main/chatgpt.js to a subdirectory ( lib in this example)
[LINK: https://raw.githubusercontent.com/KudoAI/chatgpt.js/main/chatgpt.js](https://raw.githubusercontent.com/KudoAI/chatgpt.js/main/chatgpt.js)
- In project's (V3) manifest.json , add lib/chatgpt.js as a web accessible resource "web_accessible_resources": [{
     "matches": [" < all_urls > "],
     "resources": ["lib/chatgpt.js"]
 }],
In project's (V3) manifest.json , add lib/chatgpt.js as a web accessible resource
- In scripts that need chatgpt.js (foreground/background alike), import it like so: ( async ( ) => { await import ( chrome . runtime . getURL ( 'lib/chatgpt.js' ) ) ; // Your code here... } ) ( ) ;
In scripts that need chatgpt.js (foreground/background alike), import it like so:

## 💾 Downloading via npm:

To download chatgpt.js for local customization, run the following command in your project's root:
After installation, navigate to node_modules/@kudoai/chatgpt.js to find the library source.

## 💻 Usage

chatgpt.js was written w/ ultra flexibility in mind.
For example:
Each call equally fetches the last response. If you think it works, it probably will... so just type it!
If it didn't, check out the extended userguide , or simply submit an issue or PR and it will be integrated, ezpz!
[LINK: userguide](https://github.com/KudoAI/chatgpt.js/blob/v3.9.0/docs/USERGUIDE.md)
[LINK: issue](https://github.com/KudoAI/chatgpt.js/issues)

## 🤖 Made with chatgpt.js

### AmazonGPT

Add AI chat & product/category summaries to Amazon shopping, powered by the latest LLMs! Install / Readme / Discuss
[LINK: Install](https://raw.githubusercontent.com/KudoAI/amazongpt/main/greasemonkey/amazongpt.user.js)
[LINK: Discuss](https://github.com/KudoAI/amazongpt/discussions)

### Autoclear ChatGPT History

Auto-clear your ChatGPT query history for maximum privacy. Install / Readme / Discuss
[LINK: Install](https://docs.autoclearchatgpt.com/#-installation)
[LINK: Readme](https://docs.autoclearchatgpt.com/#readme)
[LINK: Discuss](https://github.com/adamlui/autoclear-chatgpt-history/discussions)

### BraveGPT

Add AI chat & search summaries to Brave Search, powered by the latest LLMs! Install / Readme / Discuss
[LINK: Install](https://docs.bravegpt.com/#-installation)
[LINK: Readme](https://docs.bravegpt.com/#readme)
[LINK: Discuss](https://github.com/KudoAI/bravegpt/discussions)

### ChatGPT Auto-Continue ⏩

Automatically continue generating answers when ChatGPT responses get cut-off. Install / Readme / Discuss
[LINK: Install](https://docs.chatgptautocontinue.com/#-installation)
[LINK: Readme](https://docs.chatgptautocontinue.com/#readme)
[LINK: Discuss](https://github.com/adamlui/chatgpt-auto-continue/discussions)

### ChatGPT Auto-Talk 📣

[LINK: ChatGPT Auto-Talk 📣](https://github.com/adamlui/chatgpt-auto-talk)
Auto-play ChatGPT responses. Install / Readme / Discuss
[LINK: Readme](https://github.com/adamlui/chatgpt-auto-talk#readme)
[LINK: Discuss](https://github.com/adamlui/chatgpt-auto-talk/discussions)

### ChatGPT Auto Refresh ↻

Keeps ChatGPT sessions fresh to eliminate network errors + Cloudflare checks. Install / Readme / Discuss
[LINK: Install](https://docs.chatgptautorefresh.com/#-installation)
[LINK: Readme](https://docs.chatgptautorefresh.com/#readme)
[LINK: Discuss](https://github.com/adamlui/chatgpt-auto-refresh/discussions)

### DuckDuckGPT

Add AI chat & search summaries to DuckDuckGo, powered by the latest LLMs! Install / Readme / Discuss
[LINK: Install](https://docs.ddgpt.com/#-installation)
[LINK: Readme](https://docs.ddgpt.com/#readme)
[LINK: Discuss](https://github.com/KudoAI/duckduckgpt/discussions)

### GoogleGPT

Add AI chat & search summaries to Google Search, powered by the latest LLMs! Install / Readme / Discuss
[LINK: Readme](https://docs.googlegpt.io/#readme)
[LINK: Discuss](https://github.com/KudoAI/googlegpt/discussions)

### ThunderAI

[LINK: ThunderAI](https://micz.it/thunderdbird-addon-thunderai/?utm_source=chatgpt.js-github&utm_medium=referral&utm_content=showcase-link)
Use ChatGPT in Thunderbird to enhance you emails, even with a free account! Install / Readme / Support
[LINK: Readme](https://github.com/micz/ThunderAI#readme)
[LINK: Support](https://github.com/micz/ThunderAI/issues)
If you've made something w/ chatgpt.js you want to share, email showcase@chatgptjs.org or just open a pull request !
[LINK: pull request](https://github.com/KudoAI/chatgpt.js/pulls)

## 🧠 Contributors

This library exists thanks to code, translations, issues & ideas from the following contributors:
chatgpt.js is funded in part by:
Releases / Userguide / Discuss / Back to top ↑
[LINK: Releases](https://github.com/KudoAI/chatgpt.js/releases)
[LINK: Userguide](https://github.com/KudoAI/chatgpt.js/blob/v3.9.0/docs/USERGUIDE.md)
[LINK: Discuss](https://github.com/KudoAI/chatgpt.js/discussions)
[LINK: Docsify](https://docsify.js.org)
[LINK: GitHub](https://github.com)

--------------------