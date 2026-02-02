# Running Neural Networks Inside the Web Browser? Only if You Know How! | From Poland With Dev
**URL:** https://frompolandwithdev.com/case-studies/neural-network-performance
**Page Title:** Running Neural Networks Inside the Web Browser? Only if You Know How! | From Poland With Dev
--------------------

Manage Cookie Consent
Cookie Policy
We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.
The cookies that are categorized as "Necessary" are stored on your browser as they are essential for enabling the basic functionalities of the site. ...
Necessary cookies are required to enable the basic features of this site, such as providing secure log-in or adjusting your consent preferences. These cookies do not store any personally identifiable data.
- Cookie __cf_bm
- Duration 1 hour
- Description This cookie, set by Cloudflare, is used to support Cloudflare Bot Management.
- Cookie _cfuvid
- Duration session
- Description Cloudflare sets this cookie to track users across sessions to optimize user experience by maintaining session consistency and providing personalized services
- Cookie cookieyes-consent
- Duration 1 year
- Description CookieYes sets this cookie to remember users' consent preferences so that their preferences are respected on subsequent visits to this site. It does not collect or store any personal information about the site visitors.
Functional cookies help perform certain functionalities like sharing the content of the website on social media platforms, collecting feedback, and other third-party features.
- Cookie li_gc
- Duration 6 months
- Description Linkedin set this cookie for storing visitor's consent regarding using cookies for non-essential purposes.
- Cookie lidc
- Duration 1 day 1 minute
- Description LinkedIn sets the lidc cookie to facilitate data center selection.
Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics such as the number of visitors, bounce rate, traffic source, etc.
- Cookie _gcl_au
- Duration 3 months
- Description Google Tag Manager sets the cookie to experiment advertisement efficiency of websites using their services.
- Cookie CLID
- Duration 1 year
- Description Microsoft Clarity set this cookie to store information about how visitors interact with the website. The cookie helps to provide an analysis report. The data collection includes the number of visitors, where they visit the website, and the pages visited.
- Cookie _ga_*
- Duration 1 year 1 month 4 days 1 minute
- Description Google Analytics sets this cookie to store and count page views.
- Cookie _ga
- Duration 1 year 1 month 4 days 1 minute
- Description Google Analytics sets this cookie to calculate visitor, session and campaign data and track site usage for the site's analytics report. The cookie stores information anonymously and assigns a randomly generated number to recognise unique visitors.
- Cookie _fbp
- Duration 3 months
- Description Facebook sets this cookie to display advertisements when either on Facebook or on a digital platform powered by Facebook advertising after visiting the website.
- Cookie _clck
- Duration 1 year
- Description Microsoft Clarity sets this cookie to retain the browser's Clarity User ID and settings exclusive to that website. This guarantees that actions taken during subsequent visits to the same website will be linked to the same user ID.
- Cookie SM
- Duration session
- Description Microsoft Clarity cookie set this cookie for synchronizing the MUID across Microsoft domains.
- Cookie _clsk
- Duration 1 day 1 minute
- Description Microsoft Clarity sets this cookie to store and consolidate a user's pageviews into a single session recording.
- Cookie MR
- Duration 7 days 1 minute
- Description This cookie, set by Bing, is used to collect user information for analytics purposes.
Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors.
- Cookie SRM_B
- Duration 1 year 24 days 1 minute
- Description Used by Microsoft Advertising as a unique ID for visitors.
Advertisement cookies are used to provide visitors with customized advertisements based on the pages you visited previously and to analyze the effectiveness of the ad campaigns.
- Cookie bcookie
- Duration 1 year
- Description LinkedIn sets this cookie from LinkedIn share buttons and ad tags to recognize browser IDs.
- Cookie MUID
- Duration 1 year 24 days 1 minute
- Description Bing sets this cookie to recognise unique web browsers visiting Microsoft sites. This cookie is used for advertising, site analytics, and other operations.
- Cookie ANONCHK
- Duration 11 minutes
- Description The ANONCHK cookie, set by Bing, is used to store a user's session ID and verify ads' clicks on the Bing search engine. The cookie helps in reporting and personalization as well.
- Cookie test_cookie
- Duration 16 minutes
- Description doubleclick.net sets this cookie to determine if the user's browser supports cookies.
Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.
No cookies to display.

## Running Neural Networks Inside the Web Browser? Only if You Know How!

How we enabled ShareTheBoard’s on‑device neural network to run smoothly in the browser

## Client Overview

ShareTheBoard is an educational technology platform that transforms handwritten whiteboard content into clear, accessible digital visuals, using intelligent transcription and real‑time vectorization to support learning in any modality.

## Challenges

- High server‑side GPU costs made traditional real‑time neural network inference impractical.
- Requirement to run neural network inference client‑side within standard web browsers.
- Existing technologies (WebAssembly, WebGL/WebGPU) struggled with models using high res images as input and output.
- Early implementations caused the browser to freeze for seconds, making the app unusable.
- Framework‑level tools like TensorFlow.js and ONNX.js created UI blocking or were too slow.
- WebGPU worked only on high‑end devices and degraded performance on older hardware.

## Solutions

- Developed a proprietary JavaScript library using WebGL + GLSL shaders.
- Broke model execution into smaller layer‑level steps to allow browser rendering simultaneous with inference.

### Work we’ve delivered

### Tech Stack

## Results

- Successfully released the convolutional neural network with FullHD resolution for input and output inside a fully functional web application.
- Real‑time content detection and digitization without browser freezes.
- Smooth performance across diverse hardware configurations—from older laptops to modern devices.
- Enabled ShareTheBoard’s commercialization by reducing hosting costs and increasing accessibility.

## Conclusion

We took ShareTheBoard’s powerful neural network from server‑side prototype to polished, browser‑native solution by building a custom inference library with WebGL and shader‑based layer execution. This approach addressed performance bottlenecks, eliminated UI freezing, and ensured compatibility across devices. The result: real‑time handwritten content detection fully embedded in a web app, delighting users and enabling scalability.

## Meet the minds behind the project

We're the brains and the heart behind the code. A quirky bunch of passionate pros who love turning ideas into reality. Here, every project is a team sport, and we’re all about building software – and relationships – that last, one line of code at a time.
Dawid Skurzok
Jerzy Nowiński
Marcin (Martin) Demkowicz

## Case study

You’re the center of our work
Your satisfaction is our main metric. Join hundreds of clients from across the globe and experience quality as a non-negotiable
Available for projects

## Your next idea starts here!

Let’s partner up and build, grow, and maintain your product together.

--------------------