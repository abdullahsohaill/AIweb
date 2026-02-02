# left-pad fiasco
**URL:** http://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos
**Page Title:** How one developer just broke Node, Babel and thousands of projects in 11 lines of JavaScript • The Register
--------------------


## Topics

## Special Features

## Vendor Voice

## Resources

This article is more than 1 year old

## How one developer just broke Node, Babel and thousands of projects in 11 lines of JavaScript

## Code pulled from NPM – which everyone was using

Updated Programmers were left staring at broken builds and failed installations on Tuesday after someone toppled the Jenga tower of JavaScript.
A couple of hours ago, Azer Koçulu unpublished more than 250 of his modules from NPM , which is a popular package manager used by JavaScript projects to install dependencies.
Koçulu yanked his source code because, we're told, one of the modules was called Kik and that apparently attracted the attention of lawyers representing the instant-messaging app of the same name.
According to Koçulu, Kik's briefs told him to rename the module, he refused, so the lawyers went to NPM's admins claiming brand infringement. When NPM took Kik away from the developer, he was furious and unpublished all of his NPM-managed modules. "This situation made me realize that NPM is someone’s private land where corporate is more powerful than the people, and I do open source because Power To The People," Koçulu blogged.
Unfortunately, one of those dependencies was left-pad . The code is below. It pads out the lefthand-side of strings with zeroes or spaces. And thousands of projects including Node and Babel relied on it.
[LINK: left-pad](https://github.com/azer/left-pad/blob/master/index.js)
With left-pad removed from NPM, these applications and widely used bits of open-source infrastructure were unable to obtain the dependency, and thus fell over during development and deployment. Thousands, worldwide. Left-pad was fetched 2,486,696 times in just the last month, according to NPM. It was that popular.
You can witness some of the fallout here , here , here and here .
[LINK: here](https://github.com/azer/left-pad/issues/4)
To fix the internet, Laurie Voss, CTO and cofounder of NPM, took the " unprecedented " step of restoring the unpublished left-pad 0.0.3 that apps required. Normally, when a particular version is unpublished, it's gone and cannot be restored. Now NPM has forcibly resurrected that particular version to keep everyone's stuff building and running as expected.
"Un-un-publishing is an unprecedented action that we're taking given the severity and widespread nature of breakage, and isn't done lightly," Voss explained about an hour ago.
"This action puts the wider interests of the community of NPM users at odds with the wishes of one author; we picked the needs of the many. This whole situation sucks. We will be carefully considering the issues raised by and publishing a post-mortem later.
"In the meantime, several thousand open source projects have been repaired, and I'm sleeping fine tonight."
A new maintainer, who stepped forward to look after left-pad on NPM, requested the restoration of version 0.0.3. Meanwhile, Oakland-based Koçulu has hosted his work on GitHub . If your code still won't build after the left-pad revival, try running npm cache clear to catch up with the changes.
[LINK: GitHub](https://github.com/azer)
And that's how JavaScript app development works in 2016. ®

### Updated to add at 1138 PT (1838 UTC) on March 23

A spokesperson for Kik has been in touch to point us toward a blog post by Mike Roberts, the head of messenger at Kik, setting out its side of the story. It was published about 30 minutes ago.
Essentially, the instant-messaging biz says it was going to publish some open-source code including an NPM module also named Kik. That collided with Koçulu's Kik module, which is why the developer was asked to rename his software. As we know, Koçulu refused, and that led to Tuesday's cluster-fsck.
Referring to the emails sent by Kik's lawyer to Koçulu, Roberts said: "The wording we used here was not perfect. We’re sorry for creating any impression that this was anything more than a polite request to use the Kik package name on NPM for an open source project we have been working on that fits the name."
- JavaScript
- NPM

### More about

- JavaScript
- NPM

### Narrower topics

- PHP

### Broader topics

- Programming Language
- JavaScript
- NPM

### More about

- JavaScript
- NPM

### Narrower topics

- PHP

### Broader topics

- Programming Language
Send us news

### Other stories you might like

[LINK: GitHub moves to tighten npm security amid phishing, malware plague Hundreds of compromised packages pulled as registry shifts to 2FA and trusted publishing Security 4 months | 7](/2025/09/23/github_npm_registry_security/?td=keepreading)
The Register Biting the hand that feeds IT
- Contact us
- Advertise with us
- Who we are
- The Next Platform
- DevClass
- Blocks and Files
- Cookies Policy
- Privacy Policy
- Ts & Cs
Copyright. All rights reserved © 1998–2025

--------------------