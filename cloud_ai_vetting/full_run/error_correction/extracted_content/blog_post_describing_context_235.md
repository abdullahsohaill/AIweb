# Blog post describing context
**URL:** https://aaronlandy.medium.com/how-i-built-an-open-source-airchat-web-client-for-nextjs-using-their-unofficial-api-8d89b3ea8598
**Page Title:** How to access Airchat’s unofficial API | by Aaron Landy | Medium
--------------------

Sign in
[LINK: Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Faaronlandy.medium.com%2Fhow-i-built-an-open-source-airchat-web-client-for-nextjs-using-their-unofficial-api-8d89b3ea8598&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
Sign in
[LINK: Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Faaronlandy.medium.com%2Fhow-i-built-an-open-source-airchat-web-client-for-nextjs-using-their-unofficial-api-8d89b3ea8598&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

## How to access Airchat’s unofficial API

## Introduction (tl;dr):

Airchat uses the gRPC API framework which derives from .proto files located in its compiled Android apk files. You can use the .proto files to generate client code in any gRPC supported language. Within this blog post, I’ll show you how I found the .proto files and was able to deconstruct the API’s mechanism from clues, then show you how you can use it.

## Background:

A few weeks ago Airchat’s team consisting of Naval Ravikant, Brian N orgard , Sigil Wen to name a few of the 12–15 person team, released a new version of their “social public messenger” app.
How Naval describes Airchat:
“Welcome to AirChat. This is an open and social public messenger. It’s designed for civil and authentic conversations. It’s voice first. You push, talk, release. That’s how you get the message out.”
My friend Eliezer Steinbock invited me and I had a great experience chatting with people all around the world. I immediately saw there was a need for channels where communities can have a space for specific kinds of conversations.
Within the first week, there were no ways to create channels, as the feature had likely not been developed yet.
So I thought maybe there’s an API endpoint that exists within the code which is not available yet for users, with the ability to create channels which has not been released yet, and since the app is rapidly being prototyped, I can poke around and find an endpoint that is either intentionally or unintenntionall does not require permission . In order to do this, I needed to know how their API worked.
This is where my journey began…

## 1. Inspecting HTTP Traffic with Charles Proxy

Firstly, what any AppSec hacker does, I set up an HTTP proxy to inspect traffic from my phone to my computer using Charles Proxy. I added my computer’s IP address with port 8888 to my phone’s Wi-Fi proxy settings and installed the Charles certificates on my iPhone and computer to view SSL-encrypted traffic.
After doing this I was able to view the HTTPS requests being sent from my phone, but no responses would come from the server nor was I able to view the request headers or body.
Unfortunately this did not work as expected since there was something else blocking the SSL from the being recognized.

## 2. Decompiling Airchat’s Android App

Since the HTTP proxying did not work, I next tried installing the raw android app apk file since it is possible to decompile the apk into smali (an assembly language for the Dalvik virual machine which Android runs on). Then from there I converted the smali into java which is more readable than smali.
The decompiled Java code was nearly all obfuscated and looked like this:
After poking around and exploring the codebase, mostly be opening random files and looking for any network requests. I noticed a few things:
- The codebase includes an entire directory tree of .proto files which define the schema of a gRPC API. You can use the .proto files to generate a client SDK in any supported language to interact with the server API. You can view the proto files here.
[LINK: You can view the proto files here.](https://github.com/aaln/airchat-web/tree/main/proto)
2. The client and server utilizes SSL pinning to prevent 3rd parties from hijacking and inspecting traffic with custom SSL certificates. SSL pinning is a technique where the client and the server will only accept a specific pinned SSL certificate from one another.

## 3. Android Emulator with bypassing SSL Pinning

Given I now knew about the SSL pinning, I was ready to bypass it using a tool called frida to start reading the encrypted-ssl-pinned traffic.
[LINK: frida](https://github.com/frida/frida/releases)
The next steps I took were (the order here is important):
- I launched an Android emulator on my Macbook using Genymotion.
2. I installed the airchat apk on the Android device by running:
adb -s 127.0.0.1:6555 install com.wooshinc.getairchat.apk
3. I opened the app and logged in from the emulator.
3. I setup a VPN proxy from the Android emulator to my computer.
4. I setup a frida server on the android emulator by running these commands from my mac:
[LINK: frida](https://github.com/frida/frida/releases)
# install frida pip install frida-tools
# initiate frida server to run on the android emulator adb -s 127.0.0.1:6555 shell “/data/local/tmp/frida-server &”
5. I “depinned” the app by running this command from a new terminal window:
frida — codeshare akabe1/frida-multiple-unpinning -U -f com.wooshinc.getairchat
If you see “[+] Bypassing Trustmanager” within the terminal logs, you were successful. Running the command will open the app and requests made from the app won’t be signed by the pinned certificate.

## Get Aaron Landy’s stories in your inbox

Join Medium for free to get updates from this writer.
After following these steps, I was able to read a good portion of the unencrypted requests sent from the phone to the server. This was useful in linking which requests are made for different features in the app.
Note: Note: While depinning is active, the Airchat app won’t accept HTTP responses. This is likely due to certificate verification after the phone receives the response.

## 4. Replicating successful API calls

After reading the unencrypted client http requests, I pieced together which endpoints from the gRPC schema were necessary for authentication, retrieving user feeds, messages/threads, uploading, etc. Here are a few import endpoint routes with examples:

### Authentication

- Airchat Endpoint: https://api.prod.getairchat.io:443/airchat.auth.v2.Auth
- Example implementation
[LINK: Example implementation](https://github.com/aaln/airchat-web/tree/main/app/api/auth)
- Note: All requests asides for the authentication flow require an access token.

### Get Message Feed

- Airchat Endpoint: https://api.prod.getairchat.io:443/airchat.message.v2.GetMessageFeed
- Example implementation
[LINK: Example implementation](https://github.com/aaln/airchat-web/blob/83688f9639e220b91d85f08ae3de6bf201c2a016/app/api/messagefeed/route.tsx)

### Get Messages

- Airchat Endpoint: https://api.prod.getairchat.io:443/airchat.message.v2. GetMessages
[LINK: https://api.prod.getairchat.io:443/airchat.message.v2.](https://api.prod.getairchat.io:443/airchat.message.v2.MessageAPI/GetMessageThreadDetailsByReference)
- Example implementation
[LINK: Example implementation](https://github.com/aaln/airchat-web/blob/83688f9639e220b91d85f08ae3de6bf201c2a016/app/api/raw/GetMessages/route.tsx)

## 5. Generating the gRPC Javascript client library

Now that I roughly knew which api endpoints are used by the mobile apps. I was ready to start testing endpoints.
To test the endpoints, I first needed to generate a gRPC client. I did so for JavaScript by running
# install the appropriate tools
npm install grpc-tools grpc_tools_node_protoc_ts @grpc/proto-loader
# specifying the proto path, output paths, and Javscript style version
grpc_tools_node_protoc \ — js_out=import_style=commonjs,binary:airchat \ — grpc_out=grpc_js:airchat \ — proto_path=. \ airchat/**/*.proto
This generated code for all the endpoints.

## 6. Building an open source web client

I decided to take I learned about the api and build a web client which replicates the core functionality of the Airchat app which could then enable hobbyists and indie hackers to build on the platform.
https://airchat-web.vercel.app/login
Open source git repository
[LINK: Open source git repository](https://github.com/aaln/airchat-web)
[LINK: GitHub - aaln/airchat-web: An unofficial web client for the innovative Airchat app, designed to… An unofficial web client for the innovative Airchat app, designed to integrate with the unofficial internal Airchat API.… github.com](https://github.com/aaln/airchat-web?source=post_page-----8d89b3ea8598---------------------------------------)

## GitHub - aaln/airchat-web: An unofficial web client for the innovative Airchat app, designed to…

### An unofficial web client for the innovative Airchat app, designed to integrate with the unofficial internal Airchat API.…

github.com

## Written by Aaron Landy

Building ClosingWTF.com

## No responses yet

Write a response
[LINK: What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Faaronlandy.medium.com%2Fhow-i-built-an-open-source-airchat-web-client-for-nextjs-using-their-unofficial-api-8d89b3ea8598&source=---post_responses--8d89b3ea8598---------------------respond_sidebar------------------)
What are your thoughts?

## More from Aaron Landy

Aaron Landy

## LLMs + Mortgage Rates: Building an intuitive financial chatbot in NextJS

### A chatbot that can read/write to a form and make input assumptions. It’s open source and uses NextJS, ClosingWTF, and assistant-ui.

Aaron Landy

## Hacking Hackathon Admissions: Part 2

### The best hackers I know always find a way into hackathons and do not take no for an answer. If you make it there, you belong there.

Aaron Landy

## How to hack hackathon admissions

### As hackathons are becoming more popular, admissions are inevitably becoming more selective.

Aaron Landy

## How to find your Uber passenger rating.

### Edit 4: Uber has removed the public passenger rating again.

## Recommended from Medium

Generative AI
Adham Khaled

## Stanford Just Killed Prompt Engineering With 8 Words (And I Can’t Believe It Worked)

### ChatGPT keeps giving you the same boring response? This new technique unlocks 2× more creativity from ANY AI model — no training required…

Will Lockett

## The AI Bubble Is About To Burst, But The Next Bubble Is Already Growing

### Techbros are preparing their latest bandwagon.

Umesh Kumar Yadav

## Token, Session, Cookie, JWT, OAuth2 — I can’t tell the difference!

### Recently, I’ve noticed that some people easily confuse the concepts of Token, Session, Cookie, JWT, and OAuth2.

Joe Njenga

## I Tried New Claude Code Ollama Workflow ( It’s Wild & Free)

### Claude Code now works with Ollama, which takes the game to the next level for developers who want to work locally or need flexible model…

Write A Catalyst
Dr. Patricia Schmidt

## As a Neuroscientist, I Quit These 5 Morning Habits That Destroy Your Brain

### Most people do #1 within 10 minutes of waking (and it sabotages your entire day)

Coding Nexus
Civil Learning

## I Handed ChatGPT $100 to Trade Stocks — Here’s What Happened in 2 Months.

### What happens when you let a chatbot play Wall Street? It’s up 29% while the S&P 500 lags at 4%.

Help
Status
About
Careers
Press
Blog
Privacy
Rules
Terms
Text to speech

--------------------