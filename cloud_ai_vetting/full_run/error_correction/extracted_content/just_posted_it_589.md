# Just posted it
**URL:** https://dethstrobe.substack.com/p/from-agile-to-apathy-why-google-didnt
**Page Title:** From Agile to Apathy: Why Google Didn’t Work for Me.
--------------------


## From Agile to Apathy: Why Google Didn’t Work for Me.

I recently left Google after nearly four years. I wish I could say it lives up to all the hype, but it didn't. I honestly felt like I did some of the worst work of my career there. The environment, the processes, and team dynamics simply didn't align with my approach for how to collaborate and ship software. I've been reflecting on exactly why I wasn't able to make it work for me.
Just to brace you, I know just how ranty this is going to sound. I'm not writing this as a condemnation of Google, because I know there are people that thrive and enjoy working there. This is just my own personal perspective on it. Take it with a grain of salt.

## Agile is a Sin

I come from companies that do agile processes. It's not perfect, but it's empowering and very adaptive to change. I've been told that agile processes do not scale. So when I joined Google, I was extremely interested in learning how and what Google does to ship software. They must be doing something slightly different or better to ship software at scale, right?
Wrong. They quite literally don't have processes around collaboration. It's basically waterfall. Product writes up a doc. Gets buy-in from leadership. Tosses it at engineering. And then we never see them again, so we're left to implement it as we see fit.
It is literally the most expensive and high risk software development I've seen in my entire career. They basically have blind faith they've hired super smart people that will just magically build the perfect product. Which to be fair, they do quite literally have a lot of rock star developers. But relying on purely heroics to ship software is a recipe for burn out and knowledge silos.
Also, they don't ship software. Deadlines are arbitrary. There are so many times when we approach a deadline only for "X" feature needs to absolutely be there on release so we'll just push out the release. I think deadlines are stupid, so I don't want to pretend like I care about them. But I do care about shipping software. The sooner you ship, the sooner you can start to learn and prove that your core assumptions are right or wrong. So to ship sooner, you need to downscope. If your MVP (minimal viable product) requires several really difficult features to implement, maybe it's not an MVP anymore. But then again, I guess no one called it an MVP, but me, who is used to shipping software regularly.

## The Doc Machine

So, if you're not regularly shipping software, how can you possibly measure impact?
Docs.
Endless docs.
Countless docs.
So many docs that it can be impossible to find what doc says what you did.
Google's mission is to "organize the world's information." Internally in Google, they generate a lot of information in docs, and it's very hard to search and find the information you're looking for.
What's the point of docs no one reads? Well, since software doesn't get shipped, I assume it just acts as a laundry list of links when attempting to show impact for your performance reviews or promotions. You might not have shipped anything, but at least you left a paper trail of what you didn't ship.
You want to know the worst part of it? They want you to write a doc on a system you don't understand. So you write it up, make some assumptions and send it out for approval. No one reads it to approve it. Let's say you get your single approver and start implementing. Guess what, your core assumption is wrong. The data isn't in the right place, or the data you thought had what you needed, doesn't. Now you need to rewrite the doc.
What's the point of getting approval? What's the point of a doc that is wrong from the start? What's the point of upfront design that is wrong? Why not just implement and find out what actually is going on and make it work?
The point is, it's just theater to make it look like we're doing our jobs. Why isn't the software the evidence we're doing our job?
I'm not trying to say docs are bad, and everything should just be tribal knowledge. But I am saying docs that need to be rewritten from the get-go are a waste of time.

## Bad docs

Ironically, despite needing to write so many docs to implement things. When you read other people's docs, you might notice something. They're very high-level. They're more like a thesis, then like actual documentation on how to use an API.
What is the point of docs that don't answer how to use an API?
Focusing on the high-level philosophy of a service is honestly distracting and unhelpful. I think I understand why this happens. It's hard to keep docs up to date. So if you keep them high-level, they won't become obsolete or need to be updated. But I don't care about your thesis defense; I just want to use your software to solve my problem.
And I know Google can write good docs. Angular has fantastic documentation. Proto Buffers have great docs. Both of these are made by Google. I guess the difference is they're public facing and Google doesn't prioritize internal docs like they do their external facing ones.

## A Culture of Silence

So, there is a lot of lip service towards how open Google is. Say how they're trying to encourage employees in fireside chats to not ask anonymous questions so that leadership can follow up with the individual to gain more context. (This, by the way, does not prevent people from asking anonymously, which they do.)
There is also a culture of no-blame retrospectives. They don't run regularly, even when I advocate for them. And worst of all, when we finally do run retrospectives, we don't discuss challenges and problems we are encountering. So, what's the point of a retrospective that doesn't talk about pain points and mitigation strategies? From my perspective, it just looks like theater and a way to paint a false view that everything is good and we have nothing to complain about. Or worse, that we are helpless and we really cannot change anything.
Coming from companies with genuinely open cultures where we fostered candid and open discussions, it's baffling to me that no one seems willing to put in the minimal effort to improve everyone's lives.
It is better to be positive about a broken system and keep the status quo than it is to ask people to put in a laughable small level of effort to make everyone's life better. Not everything is going smoothly all the time. And assuming we want it to run smoothly, we should probably discuss the pain points and workarounds or solutions to them. Knowledge silos are bad. More open discussions can reduce knowledge silos which reduces the burden on individuals and gives everyone a balance for job responsibilities.

## A Culture of Bottom-Up (but only if it's top-down)

So, in meetings with leadership. They emphasize that our bottom-up culture is how we do such great work. And by bottom-up , they apparently mean top-down .

## When Bottom-Up Meets Brick Wall

So, let's say our UXR (user experience research team) has come up with an obvious gap in our offerings. What would you do? Perhaps gather some people from multiple disciplines and brainstorm a solution. Or maybe you just get leadership and design in a room and iterate on who knows what behind closed doors for literal months, before you ever even involve engineering. And for those few months, you pull engineering off their current teams in a large-scale reorg and don't give them marching orders instead just give them a bunch of vague ideas of what they might want to build. Like...what is engineering supposed to do? Build against an invisible moving target? The answer is, that is exactly what we do. Not because it's a good use of our time, but because we have nothing better to do and we have no input into the vision of the product.
So let's say, you're an engineer, like yours truly, and you think that process is stupid, and instead you really do want to try to implement a bottoms up initiative. So maybe, see a feature, we originally spec'd out but was dropped because they didn't see the current value in implementing it. But it sounds kind of cool, and shouldn't be that difficult to get an MVP for this feature. Maybe you go to reach out across teams, pull in people that own data you need, a team that works on Android and iOS, and try to get people from the backend team so you can make an e2e MVP to demonstrate this feature is doable. Also, act as a test bed to show smaller agile processes work and probably how we should handle work in the org.
Sounds pretty encouraging, right? But here is the real problem, one of the teams is a no-show. Not only are they a no-show, they also refuse to work with you and ignore your messages. You escalate to your manager and tech lead, and that team also ignores them too. You work with the other teams and implement everything, but say the one thing to tie everything together and make it work e2e. Let's say a backend team refused to work with you. So, naturally, offer to do the work for them. And they tell you to not do that. Because it's not my code base, I'm not on call, and I don't have to maintain it. So what do you do?
What I did was create a video demo that made it look like it should work and presented it to leadership. We were reorged before this demo was even presented, so the feature died on the vine.

## The Only MVP Is Minimum Viable Plausible Deniability

Let's say that you do still believe in the rhetoric that, the organization really does believe in bottom-up . So you take some time and write up a doc (which is an activity you don't enjoy but if that's how the game is played, and you want to play ball, you do it). The doc outlines an open source initiative that is coincidentally attempting to solve the space we just tried to fill. But since there's an open-source community trying to solve the same problem space, maybe we can just leverage that and even help them grow at the same time. Anyway, it was super nice to have leadership hear me out, but they didn't want to go with it, because it turns out that one of the reasons we hamstrung our last project was because we were attempting to skirt a legal definition that the open source project is tackling head on. Suddenly, it made more sense: The original project was destined to fail, not because it was a bad idea, but because they were trying to handicap the implementation to avoid legal scrutiny.
Fundamentally, we're not trying to build good software or solve problems. We're just trying to do something without bringing legal scrutiny to Google.
I understand getting sued sucks, and the law is often weaponized against Google. But why handicap ourselves? There are so many other ideas out there. Why not pursue things that are higher value and lower risk? I cynically believe it could just be virtue signaling to investors, to show Google is trying new things and still taking risks. But their risks seem high-risk, low-reward, compared to the normal practices I'm used to, which focus on mitigating risk and prioritizing high value. Taking risks here seems to be about signaling growth, but are they truly growing? Wouldn't the more obvious path be to take the calculated legal risk to solve a real problem and potentially achieve genuine growth? I don't know; I'm not in leadership. I just had a worm's-eye view of the machine.

## Grassroots Agility, Stomped by Apathy

Let's say you came from an agile background and you even believe it. Because you've seen it solve very obvious communication issues that you see arise in large organizations. You've experienced it firsthand, you know it works. You go and explain it to your manager, they say that there are organization issues and leadership is resistant to change. They don't discourage you from trying, but they kind of set the expectations that nothing will change. But, what else are you supposed to do? Nothing?
So you have a meeting with your skip manager (your manager's manager) once again advocating to adopt agile processes and maybe get more stakeholder buy-in. And they give you the advice to do it locally with your team. You know, "bottom-up" kind of stuff.
You present it to the team. They hate it. They don't want processes. They don't want collaboration or more communication. They say agile practices are dehumanizing and that we are not interchangeable cogs in the machine. A bit of a disservice towards agile processes. But they are willing to try some of the ceremonies.
But literally, for any reason whatsoever, they cancel meetings, like retrospectives or stand-ups. Maybe we need more time to finish a feature, or maybe it's a holiday, or we get reorged. And we never start up the meeting again, at least until I ask for it. Followed by it once again being canceled at the drop of a hat. And no one cares. They don't see the value in it. And to be honest, the ceremonies are toothless because we don't discuss actual problems, we don't discuss work progress to reduce knowledge silos, and action items are never done and are also usually not meaningful anyway.
The reason people don't see the value of agile processes is not that it's not a good framework to address communication gaps, but because just doing the ceremonies without the communication makes them pointless. There is value in the ceremonies if they're being used to address the problems. But actively ignoring the problems, even with ceremonies, means we're now just wasting people's time.

## Bottom-Up, Top-Down, and Going Nowhere

If there is a bottom-up culture at Google, it is self sabotaging. There is so much momentum for the status quo that actual process change is near impossible. The only change that appears to work is a top-down mandate, which they try every year with constant reorgs and get the same results.

## There is No Team in I

So, coming from an agile background (I know I sound like I'm in a cult, with how much I bring it up, but bear with me), I've come to the understanding that I as an individual do not necessarily matter. It's about putting aside ego and working together on a larger goal. This also comes with a nice benefit of distributing responsibility, and reducing burn out.
That's pretty damn ungoogley . At Google, they're rugged cowboys. They pull themselves up by the bootstrap and don't care about your collaboration. You need to own everything. Your work, your feature, your project, your process, your career. No one is here to help you. You need to just do it yourself. Which is ironic, as googley-ness should theoretically not embody it. But the performance evaluation surely doesn't emphasize trying to make teamwork work.
A bus factor of 1 is seen as a positive thing. It means you've made yourself invaluable. You are the sole point of contact, and despite that sounding like a lot of annoying responsibility, it's perceived as good because you own it.
I hate knowledge silos. I do not believe it makes anyone more valuable. I fought against the hoarding of knowledge. I'd include people into meetings to make sure I'm not the only one with context. I'd ask stupid questions and repeat talking points in meetings to make sure I understood and we were aligned. These are all considered negative things at Google. Because it is seen as wasting everyone's time in the meeting. It is better to repeat yourself with several dozen 1:1s (or I guess write yet another doc no one will read) than it is to talk it over in a group and make sure there is no ambiguity.
It could just be me though. But it sure felt like it, when my manager said I was "leaning on others too much." How else am I supposed to read that?
I've never seen such an environment that is literally so hostile to collaboration.

## Performative Theater

I hate 1:1s. I think they're a waste of time. I would even argue that most 1:1s are a waste of time in every context. I'm probably being hyperbolic, as I'm sure there must be cases where 1:1s are beneficial. But I'm struggling to think of one right now.
1:1s are a bottleneck to communication. And judging by how often my 1:1s were canceled with my managers, I'd have to say they don't value them either.
So, I'm a huge advocate for openness and transparency. And after one reorg (I went through 5 reorgs in my 4 years at Google, and been through 7 managers, chaos is the norm) leadership was attempting to be more open and transparent and so allowed anyone to join their meetings. So, since I felt like I did not have enough context to understand their decisions, I joined those meetings.
When they asked if everyone had context on a doc, I was the only person to raise my hand and said I did not. I guess this was a sin to acknowledge my own ignorance, because it turns out after the next meetings I was removed from the subsequent meetings. I asked my manager if I could be brought back to gain more context, and he told me I had enough context to do my job. While probably true, I had a suspicion that my work was not very high priority. Maybe we should work on something else. Anyway, this taught me that it's all optics. I think my manager wanted to control the narrative. If he wasn't there to be a middle man, what is his job? Like, seriously, what is his job? I still don't understand what value he brought.

## Tech Debt Forever

To say Google's code base is complex is an understatement. Not only is it complicated, it's also a mess. Not only is it a mess, but it's also poorly documented. And not only that, but it actively fights you as you make changes and try to understand it.
Cryptic compile errors. Cryptic build errors. Cryptic run time errors. And just when you think you've finally got it working. There are blockers on merging the code because of invisible linting errors you didn't know you were violating. Or there is some weird test case that broke, but only after 3 hours of running tests in the CI pipeline. Or maybe, you just want to delete some code, but it turns out that the code you're trying to delete has a different release schedule, so it cannot be deleted with other code. And the other code is dependent on the first bit of code that you cannot delete being deleted. The code is constantly fighting you. And maybe if we could discuss these issues in a group, we could understand the problems quicker or come up with strategies to mitigate them...but it turns out talking about how much it sucks to write code is frowned upon. So you just need to keep it to yourself. And I'm left wondering, am I the problem? Is my career a lie? Do I have imposter syndrome if I don't actually know what I'm doing? It makes you question everything.
So I talked with my director (the skip’s manager) about my challenges. And I was candid about it. And he said, "It sounds like you need mentorship." And I said, that's exactly what I need. And he said he'd help get me some. I messaged him every week for a few months. He offloaded this responsibility to my manager, who naturally, did nothing. By the time I left, I made the request 8 months prior. I was clearly not getting the mentorship I asked for. My manager's wonderful feedback was, "maybe you should find your own mentorship." And it does make me wonder, "what is your job if it is not to help me do my job better?" Anyway, I also was unable to find mentorship on my own. And it does make me wonder, does anyone truly understand the beast that is Google's complex internally built tech stack with poor documentation? Even the internal AI that is usually pretty good at explaining some of the code, will just straight-up hallucinate how the code works and then it becomes very hard to understand. The AI will tell you a very convincing lie, but you won't know it's a hallucination or how to possibly fix it, because the documentation is poor and the only way to learn how it really works is to reverse-engineer it by performing code archaeology.

## I'm out

So I left Google. It was amicable. This was, of course, also only my personal experience in my particular organization. I've been told different parts of the org and different teams are said to have different cultures. Heck, even some people might even thrive in the culture I described. But it's not for me.
They gave me severance, which was honestly extremely nice. I tried so hard to bring cultural change to Google, but there is no willingness to change. Honestly, with the amount of money they're printing with ads and search, there is no pressure for them to make any changes.
There is a clear cultural mismatch between what I value and what Google values. Even if Google pays lip service that they value the same things I value, their actions clearly show they do not. And so, I am honestly happy to be free from them and given the time to look for a place that values what I want.
I used to believe I was a mercenary for hire to the highest bidder . But you know what? Apparently, within reason. I just want to work, collaborate, and iterate on software. Is that asking for too much? The one thing I can take away from my time at Google is that I now have a clearer understanding of what I'm looking for in my next step.

### Ready for more?


--------------------