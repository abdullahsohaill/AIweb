# Pygmalion AI
**URL:** https://pygmalion.chat
**Page Title:** PygmalionAI
--------------------


## Pygmalion AI

Pygmalion
Chats, Roleplays, Adventures, and more!

## 101,200+

Users

## 3950+

Characters/Cards

## 1130+

Creators

## 35,000+

Open Chats

## Features

Highlights from what we have to offer you

### Tailored Chat

Chat with any and all characters/Cards you want, without any limits. Customize page visuals, model parameters, conversation styles, and much more. Chat privately, and back up or delete your data whenever you wish.

### Open Platform for Characters/Cards

Browse a large collection of Cards made by passionate creators. Make your own Cards with our Card creator, add lorebooks/world info, extra images, chat backgrounds, and more, then share with the community. Import/export your Cards as you wish without lock-in.

### Unrestricted Models

In-house developed and curated models, hosted by us to provide you unlimited access to all the Cards you love, without any restrictions. Use presets to change the style of dialogue.

### Welcoming Community

Star Cards, follow creators, and be notified of their new creations. Join the Discord to engage with everyone.

## Timeline

Be up to date with upcoming features and the latest improvements
9/14/2025

### Update 1.5

### Additions

- - Updated grimoire integration, added new memory entries, and a graph for entity relationships.
- - Added proper duplication for group chats
- - Added option for chat duplication without messages
- - Added more message selection options: select above and select below

### Fixes

- - Fixed wrong card replying in chat on swipe
- - Fixed minor safari cropping issues
- - Fixed reversed message order when copying
- - Fixed chat v1 schema imports not working
- - Fixed signup page crash on reload
- - Fixed multiple duplicate notifications showing on chat page (for samplers and models)
- - Fixed main chat card not being changeable
- - Fixed problems with viewing chat lorebook entries
- - Fixed lorebook editor errors not being noticeable
- - Fixed system prompt field blocking card creation when too high (by trimming it)
- - Fixed importing ST Sampler files with DRY Sequence Breakers

### Changes

- - Increased greeting and alt greeting character limits
- - Improved collection pages
9/2/2025

### Maintenance Concludes

### Maintenance period is now over!

Sorry for the ups and downs with the models but after much effort, we managed to bring our infrastructure locally without relying on rental hardware entirely.
This is going to be a short announcement as the previous announcement covered what I wanted to say.
For all users, Imp is having issues with being deployed. We are working with the model creator on how to fix this. Since this is a model specific issue (not infrastructure), it will require some time.
For paying users, I am left with a choice on which "Big Model" to run. Judging by what people has been requested, I will be bringing back Big-Magnum back to the site and putting Big-Plesio on a machine that has more ups and downs. This means Big-Plesio will have less availability compared to Big-Magnum for now (this will take more additional time to run both at the same time reliably). I will work with the team on how to optimally run both (other large models as well) in the future with our new infrastructure.
8/17/2025

### Regarding the Maintenance

I wanted to write an update with the on-going maintenance work with the models on the site. As it appears it is taking unusually long compared to our other quick updates.

### What happened?

There are two on-going work at the same time. 
Stop using rental machines and moving all the model deployments locally to machines we personally own
Update all machines to the latest aphrodite-engine version
Both have not been a smooth experience. Originally, the plan was to me to purchase the components, build the machine, install the latest engine update and swap the traffic from rental machines to it gradually. Unfortunately, I ran into hardware and software issues so there was delays on getting it operating. The delay caused the machine running Big-Magnum to expire, which was a surprise, as it was expected for it to expire near the end of the month, not in the middle. Proceeding that was our attempts to get everything running again while figuring out the quirks and errors of the new engine update. Sometimes, we'll resolve a machine specific issue, only to encounter an engine issue that needed to be fixed. Thankfully, we are nearly finished with migrating the models to our local hardware.

### Why local?

We were bleeding money renting GPUs on a monthly basis. A couple thousand of dollars (USD) gone. It took a while but by migrating our GPUs locally, we will only need to pay for the power consumption. Dropping down the GPU expenditure from thousands to hundreds (around a 90% reduction). This basically cut the site operations cost in half and make us more comfortable to use the money we have on improvements and paying development more. From a pure maintenance point of view, the site is sustainable with these reductions. Which makes me happy since we'll have more time and money to improve the site and tackle other cool projects.

### What changed?

- - All models will be running on Aphrodite-engine version 0.8.3 for preparations of the eventual 0.9.0 release (link to our engine: https://github.com/aphrodite-engine/aphrodite-engine )
[LINK: https://github.com/aphrodite-engine/aphrodite-engine](https://github.com/aphrodite-engine/aphrodite-engine)
- - Limited Free Tier and Slower But Smarter tier will have two new models added after I finish the maintenance work. The current models should be running fine. Should take a day or two after this announcement.
- - Big-Magnum unfortunately is not compatible with version 0.8.3 at the moment and we're busy fixing that. For now, we'll be running Big-Plesio, which should perform the same or better compared to Big-Magnum. If people like this over Big-Magnum, then we'll be running it instead long term. Hopefully, compatibility issues will be fixed soon, as I would like to run both models at the same limited time for better testing. Feedback on Plesio will be greatly appreciated.

### Refund

I feel bad that the maintenance took longer than expected, especially with the paid models going down longer than usual. I think that's unacceptable as a service provider. So, if you feel like you have wasted your subscription this month due to this. Send an email over at support@pygmalion.chat and I'll sort out a refund for you.
I would also use this opportunity to talk more about things too.

### Survey Response

The survey has been concluded for a while and I was working on the response for that before I needed to urgently build a local machine. There will be a response to the survey coming when this maintenance period is over. The roadmap will be posted after the survey response. Sorry for the delay about this. I can only work on so many things at a time.

### Another Update Soon

There has been a bunch of reported issues (especially with the lorebooks) on the site. An update will be coming out this month (hopefully!) to both the site and Grimoire. For the Grimoire update, refer to the attached video since this will be the memory relationship update. I think it looks super cool! Other bugs and issues will be sorted out. I recommend joining the Discord to communicate the issues best, however feel free to send emails at tav@pygmalion.chat .
Thank you for your patience. Things will be much better for us in the long run once this bumpy period is over.
7/8/2025

### Survey - 8th July

Hello!
We are conducting an important survey for all the people using our site.
The link is here: https://forms.gle/yYojV9h3NpvPcdVC8
We highly recommend doing this survey to communicate everything you want us to do. We will be taking this survey seriously and will be making another blogpost about the results and our plans going forward.
We're a community driven company and we can be flexible on the things we can work on next. So, tell us what you want, and what areas we can improve on, and we'll add it to our future roadmaps!
The survey should take around 10-15 minutes to do. We appreciate you all!
~PygmalionAI team
7/1/2025

### Update 1.4

### Additions

- - Added support for lorebook entry depths
- - Added section for persona listing and editing in user page
- - Added ability to send message without auto response (allowing manual picking of which card replies in group chats)
- - Added follower count on user pages
- - Added updated chat import/export, with support for the latest features including group chats
- - Added support for other cards' lorebooks in group chats
- - Added minor visual improvements

### Fixes

- - Fixed tildas (~) causing issues in messages formatting
- - Fixed issue where user could not set default version in private cards
- - Fixed delete button being visible on default versions
- - Fixed grimoire not working on cancelled plans (only those which still have a period of deactivation)
- - Fixed alt greetings not being clearable
- - Fixed lorebook menu causing page crash on mobile
- - Fixed ChubAI cards not being importable
Additional Info
Another announcement will be going up regardfing a big survey to help us plan out the rest of the year on what people want.
5/13/2025

### Update 1.3

- - Added new payment integration with support for Paypal
- - Added improved model selector (quickly view model notes and daily limits)
- - Added labels and new fields in lorebook form (only usable new field is delay)
- - Added experimental themes (press the theme icon in the user menu or go to settings page)
- - Fix minor issues in lorebook ui
- - Fixed character search not finding partial words correctly
- - Fixed CAI tools tavern file import
- - Fixed client exception in chat page for older browsers
IMPORTANT PAYPAL INFO
We have added the much requested PayPal service to the site.
In order to use this service, there are some steps:
- - Go to the Plans Page located in your profile
- - Press the ★PayPal button at the top of the page
- - Press "Confirm" in the pop-up
- - New page should be shown, the Subscribe button will now show Authorize and PayPal as options
Some benefits of PayPal:
- - No processing times compared to Authorize
- - Able to subscribe and cancel immediately without losing the subscription
We will be treating Authorize as our backup payment processor.
3/21/2025

### Update 1.2.1

- - Added group chats (you can now add other cards as participants)
- - Added version selection in character view dialog
- - Added ability to search through cards from the chat page
- - Added limited support for displaying images in chat messages (paste an image link into the message text, or use markdown image markup)
- - Added better handling of errors caused by google translate, including workarounds to reduce the issue frequency
- - Added saving of the generated text when error happens mid-response
- - Fixed message continues lacking the starting space (resulting in no space between the continue and the original text)
- - Fixed minor spelling mistakes
- - Fixed new chat button being hidden when character name is too long on left sidebar on chat page
- - Fixed issue with ST chat imports (showing failed to fetch error)
- - Fixed minor visual issues
GROUP CHAT FEATURES TO BE ADDED:
- - Usage of other characters' lorebooks other than the main character
- - Ability to import/export group chats
3/3/2025

### Patch 1.1.2

- - Fixed payment page address autocomplete not working
- - Fixed issues with ST chat import and increased limits
- - Added potential fix to textarea "scrolling on typing" issue
- - Fixed bug with character stars being spammed
- - Fixed wrong last update date being used
2/23/2025

### Update 1.1.1

### Additions

- - Added dry range support
- - Added ability to import SillyTavern chats
- - Added token/character counting for input fields in the character editor

### Fixes

- - Fixed future date (e.g. 42458y) displayed on newly sent message in chat
- - Fixed issue with unsubscribing from plans
2/16/2025

### Update 1.0.5

### Fixes

- - Fixed privacy and terms signup links to point to the correct pages
- - Fixed inconsistency between explore listing sections' heights
- - Fixed OAuth fail not showing a warning
- - Fixed chat background not clearing, when changing from card with a background, to one without
- - Fixed character editor tag input not scrolling user to itself on error when submitting
- - Fixed character editor hint text being horizontal
- - Added improvements to authentication logic

### In-Progress

- - Group Chats
- - PayPal
No dates on these features. Group chats should be added before PayPal.

### Website has a PWA!

If your mobile browser supports downloading PWA, please open your browser menu while on the site to install it.
Steps on Chrome
- - Navigate to the vertical triple dot menu on the top right
- - Scroll down to "Add to Home Screen"
- - Choose the first option of "Install"
- - Allow it to download and install
- - App is now available on your home menus with the other apps

### We recommend you look up instructions for other browsers. Searching with "Installing PWA on <browser>" should work fine.

For help, please send emails over at support@pygmalion.chat .
2/12/2025

### Official Launch of the Site

Our website has finally moved out of Beta!
Thank you for everyone's support in getting us here.
For the occasion, we wrote a blogpost found here - https://blog.pygmalion.chat/posts/website_update/
We will provide more updates regularly from now on officially!

## Subscription Plans

Support us and get cool perks
Free
Default Plan for Everyone
$0.00
/ month
Unlimited Access to free models
Reduced memory size for free models (16K > 8K)
No access to memory system
No access to premium models
May be subjected to ads
May have inconsistent generation times
Low-Cost
Bite-sized Try-out Plan
$6.50
/ month
Access to memory system - Grimoire
Access to higher context (16K)
Faster generation times
Limited access to premium model - 150 messages
Premium
For the Best Experience
$17.99
/ month
Access to our memory system - Grimoire
Access to higher context (16K+)
Unlimited access to all models
Fastest generation times

## FAQ

Know more about us or get answers to questions you need
What is PygmalionAI about?
Our company focuses on building fun models and applications for anyone to use. If there is anything that can combine AI and fun, then we will be interested. Our focus in the AI space is solely text generations. While we are happy to explore other domains of generative AI, this will be more of a collaborative matter with other groups.
Who makes up the PygmalionAI team?
What does PygmalionAI specialize in?
Why should I use PygmalionAI's platforn?
Does PygmalionAI have any investors?
What is the stance on NSFW content?

## Connect with Us

Join the community, get help, and ask questions
An open-source project dedicated to creating large language models for chat and role-play purposes.
- Project
- Updates
- Guidelines
- Privacy Policy
- Terms of Service
- About Us
- Connect
- Discord
[LINK: GitHub](https://github.com/PygmalionAI)
Copyright 2026 - PygmalionAI Project. All rights reserved.

--------------------