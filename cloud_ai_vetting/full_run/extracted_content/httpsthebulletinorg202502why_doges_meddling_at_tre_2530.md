# https://thebulletin.org/2025/02/why-doges-meddling-at-treasury-could-have-catastrophic-consequences-for-the-us-economy/?utm\_source=pocket\_saves
**URL:** https://thebulletin.org/2025/02/why-doges-meddling-at-treasury-could-have-catastrophic-consequences-for-the-us-economy
**Page Title:** Why DOGE’s meddling at Treasury could have catastrophic consequences for the US economy - Bulletin of the Atomic Scientists
--------------------

- About
- Magazine
- Events
- Contact
- Store
- My Account
- Login
- Donate Give Now Ways To Give What Your Gift Supports Annual Event Einstein Circle Legacy Society Donor-Advised Fund
- Give Now
- Ways To Give
- What Your Gift Supports
- Annual Event
- Einstein Circle
- Legacy Society
- Donor-Advised Fund
Join us for the 2026 Doomsday Clock announcement

## Why DOGE’s meddling at Treasury could have catastrophic consequences for the US economy

By Liz Fong-Jones | February 6, 2025
It’s only a matter of time until DOGE's meddling inadvertently triggers a catastrophic failure of Bureau of the Fiscal Service systems. Image: Thomas Gaulkin / Adobe Stock / depositphotos.com
- Copy link Linked copied
- Email
- Facebook
- Bluesky
- Twitter
- LinkedIn
- WhatsApp
[LINK: WhatsApp](https://api.whatsapp.com/send?text=Why%20DOGE’s%20meddling%20at%20Treasury%20could%20have%20catastrophic%20consequences%20for%20the%20US%20economy%20https%3A%2F%2Fthebulletin.org%2F2025%2F02%2Fwhy-doges-meddling-at-treasury-could-have-catastrophic-consequences-for-the-us-economy%2F%3Futm_source%3DSocialShare%26utm_medium%3DWhatsApp%26utm_campaign%26utm_term)
- Reddit
- Spread
Editor’s note: A federal judge temporarily restricted access by Elon Musk’s Department of Government Efficiency (DOGE) to the Treasury Department’s data systems on Saturday, saying that DOGE access to the systems created an increased risk of leaks and hacking. The judge also ordered any material that DOGE personnel had downloaded from Treasury systems destroyed, the New York Times reported. The order is in effect until a February 14 court hearing in a lawsuit filed by 19 Democratic state attorneys general.
Earlier this week, inexperienced officials from Elon Musk’s Department of Government Efficiency (DOGE) gained administrative access to the core payment systems at the US Treasury’s Bureau of the Fiscal Service (BFS). Like many Americans, I was shocked. Unlike most Americans, I am in a professional position to understand the potential for catastrophic macroeconomic consequences far beyond the privacy and security concerns suggested in the media and by our elected representatives .
One of the officials with admin access to the Bureau of the Fiscal Service was 25-year-old engineer, Marko Elez, who is unlikely to have experience in the arcane, aging COBOL programming language (dating back to 1959) of the bureau’s payment system, and who meets DOGE’s recruitment criteria of having the hunger to make change. Unfortunately, the line between impatience and recklessness is not clear-cut, and any missteps could upend the entirety of public expenditure in the United States.
Elez resigned from DOGE today over allegations of racism, rather than professional competence. His replacement is just as unlikely to have the kind of experience and temperament required to work with the most mission-critical systems in the United States government. DOGE has stated that it wants to recruit risk-takers who want to “ fundamentally remake the federal government ” at all costs.
In my professional opinion, it’s only a matter of time until DOGE’s meddling inadvertently triggers a catastrophic failure of Bureau of the Fiscal Service systems, and the damage may not be reversible, if the safeguards required to run a secure, reliable system have been bypassed. Revoking DOGE’s administrative access to the BFS payment systems and restoring the systems to a known safe state is a sensible, bipartisan action that voters and their representatives on both sides of the aisle should agree on.
For more than 15 years, I have been a practitioner of Site Reliability Engineering (SRE) , the discipline of making software reliable, scalable, and adaptable. As an employee, advisor, and investor, I’ve worked with software companies ranging from five-employee startups to behemoths like Google/Alphabet. I’ve authored books on Site Reliability Engineering practices and served multiple times as editorial chair of conference proceedings for our field. And, once upon a time, I was a 20-year-old, hot-headed new hire at Google determined to make her mark upon the industry and the world, hungry to make an impact.
Google allowed any engineering employee to propose changes to almost any system, subject to peer review and phased deployment, so I wrote code beyond my ordinary duties to improve Google Maps and shared systems that the entire company used. Not all my changes passed initial muster, but patient senior engineers on the responsible teams mentored me, so my contributions could be accepted.
In the wake of the chaotic launch of President Obama’s healthcare.gov initiative, many of my Google colleagues volunteered for the all-hands-on-deck effort to fix it and for the United States Digital Service (USDS) organization that came afterwards and brought industry experts into government. When they returned from their assignments, they impressed upon their colleagues how crucial it was that government systems stay reliable. One United States Digital Service alum shared with us that if the Centers for Medicare and Medicaid Services (CMMS) delayed in submitting its list of approved reimbursements by just 48 hours, it could shave several percent from the US GDP for that year as hospitals failed to make payroll and doctors’ offices closed. That statement stuck with me as an example of how government IT systems can have unexpectedly large ripple effects on American citizens’ daily lives.
I have spent a decade encouraging engineers to test their software in production, performing final validation of proposed changes in the real live serving systems—but with measuring and controlling for risk as part of the equation. According to the “testing in production” philosophy, there are diminishing returns to attempting to exhaustively test changes in pre-production staging environments; increased maturity comes from better controllability and observability of the places where the running code affects real users.
But testing in production does not mean skipping staging environments entirely—or the unit tests, peer review, observability, and circuit breakers that could limit potential harm. I have been assigned many times as a change agent to improve the productivity of existing teams but have never bypassed their controls while doing so. It is crucial that existing change-control processes be followed and reformed to improve efficiency, once outside change makers gain a better understanding of which controls are the most effective.
I have taken risks and gotten egg on my face for breaking production as an enthusiastic but inexperienced developer. But the only damage was to my ego; no one was harmed because I worked within the bounds of change control, and our systems at Google had sufficient safeguards to undo my mistakes. Unfortunately, government financial systems are not nearly as forgiving, and the methods that young DOGE engineer has reportedly employed to make changes directly to live environments without testing or review go far beyond the pale, in my opinion, even for the “move fast and break things” community epitomized by the early Facebook. But even Facebook/Meta ended up changing its motto to “move fast with stable infrastructure.” When the United States economy is at stake, stability ought to be the overriding virtue.
Individual engineers experimenting directly upon real, live systems without first validating their changes or seeking peer review violates every best practice for controlling risk in the industry. Elon Musk says he wants to run the government more like a business, but no business operates this way. For instance, every public company must implement Sarbanes-Oxley (SOX) controls to ensure no single developer can tamper with their financial data and systems. The vast majority of private software companies adhere to Service Organization Control Type 2 (SOC2), and the government’s own Authorization to Operate (ATO) protocols, which likewise prescribe testing processes and forbid employees from unilaterally making changes. These practices ensure safety and reproducibility, which enables software engineering teams to move faster with confidence.
Experts like me train employees to act within their scope of knowledge and to seek assistance when working in unfamiliar languages and codebases. We practice code review and graduated deployment strategies to ensure that we catch errors as early as possible, before they impact too many users. It is an affront to industry best practice on risk management to suggest that the best way to reform a piece of software is through unilaterally making untested changes.
If and when one of DOGE’s changes—or an unforeseen interaction between its code and normal business processes—triggers a malfunction, all payments could fail to be disbursed—not just those that Elon Musk and President Trump disapprove of, but to all payees and creditors of the United States. Medicare reimbursements could fail to go out on time, causing hospitals to shut down and patients to suffer. Social Security checks and tax refunds could not go out. Department of Defense civilian employees and troops could go unpaid. Federal contractors, including Musk’s SpaceX, may not receive payment for their services. Even worse, an “ unintentional operational default on United States treasury securities ” might come into effect.
This scenario is orders of magnitude worse than the potential Medicare payment delay that my Google colleagues worked to avert as United States Digital Service volunteers during the Affordable Care Act rollout. Worst of all, the Treasury collapsing would be a deliberate, self-inflicted wound against United States national security, rather than an unforeseen circumstance. Recent legal consent orders that limit DOGE workers to reading but not modifying records within the payment database are insufficient. The risk is ongoing , so long as any recently-added and untested code is still live in production, or if DOGE workers can push new code to indirectly alter the databases without contravening the legal orders.
Providing visibility into government payments does not mean granting an insufficiently supervised individual or group the ability to delete the entire American economy with one misplaced keystroke. Americans may have voted to reduce government waste, but they certainly did not vote to roll the dice on a catastrophic collapse of our economic system. I urge the House and Senate to assert their oversight authority and appeal to President Trump to rein in Elon Musk before the inevitable catastrophe occurs.

### Together, we make the world safer.

The Bulletin elevates expert voices above the noise. But as an independent nonprofit organization, our operations depend on the support of readers like you. Help us continue to deliver quality journalism that holds leaders accountable. Your support of our work at any level is important . In return, we promise our coverage will be understandable, influential, vigilant, solution-oriented, and fair-minded. Together we can make a difference.
Keywords: DOGE , Elon Musk , Trump , US treasury , economy , software Topics: Disruptive Technologies
- Copy link Linked copied
- Email
- Facebook
- Bluesky
- Twitter
- LinkedIn
- WhatsApp
[LINK: WhatsApp](https://api.whatsapp.com/send?text=Why%20DOGE’s%20meddling%20at%20Treasury%20could%20have%20catastrophic%20consequences%20for%20the%20US%20economy%20https%3A%2F%2Fthebulletin.org%2F2025%2F02%2Fwhy-doges-meddling-at-treasury-could-have-catastrophic-consequences-for-the-us-economy%2F%3Futm_source%3DSocialShare%26utm_medium%3DWhatsApp%26utm_campaign%26utm_term)
- Reddit
- Spread
Thank you for the excellent article. The DOGE team simply lacks the experience needed for these systems, and we must hope they can avoid a catastrophic failure. It is just mind boggling how this has been allowed to happen.
As ever, thoughtful and well presented Liz, thank you. I’m not American, nor in America / governed directly by it’s economy and these issues, but I cannot help hold my head in my hands at the manner in which the new President and his friend Mr Musk are meddling freely in just about anything and everything with seemingly so little thought, let alone knowledge on an alleged mandate of the people to uncover corruption! I can only imagine the US’s equivalent of the UK’s Civil Service – the people that actually ensure the country runs – must be holding their … Read more »
Excellent article, many Americans are certainly aware of the dangers that this maverick effort can cause, but are helpless to stop it.
I also agree the restrictions imposed are insufficient,  unfortunately our elected officials seem not to comprehend this, even when presented with scenarios that point out the additional restrictions that need to be met. Extremely frustrating.
Running a government like a business is utter nonsense. One of the key features of central governments is to provide money to society by public spending, i.e., running public deficits so that there’s a public surplus on the other side of the ledger after taxes are collected.
Liz is a developer advocate, labor and ethics organizer, and Site Reliability Engineer (SRE) with over two decades of experience. She is currently				... Read More

### ‘Greenland belongs to its people’: The US scientists speaking out against Trump’s imperial aggression

### Iran’s internet shutdown tells a larger story: Digital repression is on the rise

### The “Donroe Doctrine” moved to the Arctic. Europe must now redefine burden sharing

### Space trash: Orbit shows where the circular economy breaks down

### What experts can learn by tracking AI harms

### Pandemics & measles & AIDS: Oh my! Where Trump-Kennedy public health policy will lead

## RELATED POSTS

### Iran’s internet shutdown tells a larger story: Digital repression is on the rise

### What experts can learn by tracking AI harms

### Pandemics & measles & AIDS: Oh my! Where Trump-Kennedy public health policy will lead

### January 2026—The fiction issue

### A year in review: How Big Tech redefined governance and the economy in 2025

### Best of 2025: A baker’s dozen of fresh, hot articles from the Bulletin’s magazine

### Receive Email Updates

## Recent Stories

## ‘Greenland belongs to its people’: The US scientists speaking out against Trump’s imperial aggression

By Yarrow Axford

## Iran’s internet shutdown tells a larger story: Digital repression is on the rise

By Steven Feldstein , Shreya Joshi

## The “Donroe Doctrine” moved to the Arctic. Europe must now redefine burden sharing

By Roderich Kiesewetter

## Space trash: Orbit shows where the circular economy breaks down

By Jessica Coria

## What experts can learn by tracking AI harms

By Katie Peek

## Pandemics & measles & AIDS: Oh my! Where Trump-Kennedy public health policy will lead

By Erik English , Matt Field

## January 2026—The fiction issue

By Dan Drollette Jr

## Pulling out of 66 international organizations, Trump turns his back on science, facts, reason

By Benjamin Santer

--------------------