# Cortex State of Developer Report
**URL:** https://www.cortex.io/report/the-2024-state-of-developer-productivity
**Page Title:** The 2024 State of Developer Productivity | Cortex
--------------------

Webinar: Reclaim Your Roadmap from Backstage → Register Now

## The 2024 State of Developer Productivity

November 19, 2024

## Introduction

The topic of developer productivity isn’t new, but the environment in which it’s now discussed has changed dramatically. In late 2023, new tension over how to measure and improve productivity put us in a stalemate over which metrics really matter. But instead of debating whether deployment frequency is a good measure, what if we asked what’s keeping teams from deploying frequently to begin with?
[LINK: new tension](https://www.cortex.io/post/the-developer-productivity-debate)
To better understand how teams perceive blockers to productivity, Cortex conducted a survey of 50 engineering leaders at companies with more than 500 employees in North America, Europe, and AsiaPac. The survey included free-text and multiple choice questions pertaining to productivity blockers, and future plans. This report contains an analysis of these results as well as suggestions for how to reframe your thinking about productivity at your organization.

## Survey demographics

## Key Themes

There are five key themes to unpack in the survey results, which also reflect broader market trends and conversations.
- 1 58% of respondents say more than 5 hours per developer per week are lost to unproductive work. When asked “How many hours per dev per week are lost to unproductive work (work that can be automated, optimized, or eliminated)?” Most respondents estimated between 5-15 hours per dev per week, while only 10% said less than 3 hours. 31% of those that cited 5-15 hours lost also say their developers most often cite time required to gather context as a top blocker.
58% of respondents say more than 5 hours per developer per week are lost to unproductive work.
When asked “How many hours per dev per week are lost to unproductive work (work that can be automated, optimized, or eliminated)?” Most respondents estimated between 5-15 hours per dev per week, while only 10% said less than 3 hours. 31% of those that cited 5-15 hours lost also say their developers most often cite time required to gather context as a top blocker.
- 2 90% of respondents say improving productivity is a top initiative this year (7-10 rating), with 20% rating it 10 out of 10. When asked how important it is to improve developer productivity this year, most respondents selected 9 out of 10, with an 8.2 average. 55% of those stating 9 or 10 also said their team loses 5-15 hours per dev per week to unproductive work—which certainly warrants priority attention. And while only two respondents said productivity was not a major focus, both still estimated weekly time lost to unproductive work to be 3-5 hours and 5-15 hours respectively.
90% of respondents say improving productivity is a top initiative this year (7-10 rating), with 20% rating it 10 out of 10.
When asked how important it is to improve developer productivity this year, most respondents selected 9 out of 10, with an 8.2 average. 55% of those stating 9 or 10 also said their team loses 5-15 hours per dev per week to unproductive work—which certainly warrants priority attention. And while only two respondents said productivity was not a major focus, both still estimated weekly time lost to unproductive work to be 3-5 hours and 5-15 hours respectively.
- 3 Time spent gathering project context and time spent waiting on approvals (26%) tied for areas of biggest productivity leak. When asked, “Where in the value stream listed above do you think has the largest productivity leak? (Most room for improvement/automation),” respondents primarily identified time spent waiting on approvals and gathering context. Even those citing fewer than 5 hours a week of productivity loss still pointed to time lost in gathering context, and fixing bugs.
Time spent gathering project context and time spent waiting on approvals (26%) tied for areas of biggest productivity leak.
When asked, “Where in the value stream listed above do you think has the largest productivity leak? (Most room for improvement/automation),” respondents primarily identified time spent waiting on approvals and gathering context. Even those citing fewer than 5 hours a week of productivity loss still pointed to time lost in gathering context, and fixing bugs.
- 4 72% of respondents say it takes more than 1 month for new hires to submit their first 3 meaningful PRs, with 18% citing over 3 months. When asked, “How long, on average, does it take for a newly hired developer to submit their first 3 meaningful PRs?” The most frequently cited duration was between 1 and 3 months (54%). Those that cited more than 3 months also most often pointed to “gathering project context” as the #1 productivity leak in the entire software development value chain.
72% of respondents say it takes more than 1 month for new hires to submit their first 3 meaningful PRs, with 18% citing over 3 months.
When asked, “How long, on average, does it take for a newly hired developer to submit their first 3 meaningful PRs?” The most frequently cited duration was between 1 and 3 months (54%). Those that cited more than 3 months also most often pointed to “gathering project context” as the #1 productivity leak in the entire software development value chain.
- 5 Teams without an IDP report more frustration with data and context finding, though 86% of Backstage users also struggle with the latter. Some IDPs can ease access to information, though complexity introduced with others can worsen the problem. When asked “What impediments to productivity do your developers complain about?” Zero IDP users reported issues with data consistency, compared to 21% of non-IDP users. But while 24% of IDP users say time to find context is a primary impediment, that number pales in comparison to the 48% of non-IDP users, and 86% of Backstage users (an open source platform for building IDPs) complaining about the same.
Teams without an IDP report more frustration with data and context finding, though 86% of Backstage users also struggle with the latter.
Some IDPs can ease access to information, though complexity introduced with others can worsen the problem. When asked “What impediments to productivity do your developers complain about?” Zero IDP users reported issues with data consistency, compared to 21% of non-IDP users. But while 24% of IDP users say time to find context is a primary impediment, that number pales in comparison to the 48% of non-IDP users, and 86% of Backstage users (an open source platform for building IDPs) complaining about the same.

## Developer Productivity: Definitions, Measurement Frameworks, and Open Questions

We asked survey participants to briefly describe how they define developer productivity, and what—if any— frameworks they use to define and/or measure. A few key themes emerged:
- 1 Diverse Framework Adoption: Many organizations have customized their own frameworks by weaving together other established standards.
Diverse Framework Adoption: Many organizations have customized their own frameworks by weaving together other established standards.
"We use DORA heavily and built our own flavor of DevEx with some SPACE influences, like regular sentiment surveys. We’re working to boost our organization’s developer experience by creating a work environment where our development team members thrive, and make it easier for developers to do their jobs."
Andrei | Software Engineering Manager, Ecommerce | 10K+ employees
- 1 Use of Internal Developer Portals: Several respondents mentioned investigation of Internal Developer Portals to improve developer experience and productivity.
Use of Internal Developer Portals: Several respondents mentioned investigation of Internal Developer Portals to improve developer experience and productivity.
“This is a long term problem to solve, but we have identified the features our teams are using and are mapping them to IDPs for them to use. Success will be measured by onboarding.”
Randy | Director, Cloud Engineering, Pharmaceuticals | 10K+ employees
- 1 Framework Struggles and Adaptations: Several respondents mentioned challenges in fully implementing these frameworks, including getting team buy-in or organizational alignment.
Framework Struggles and Adaptations: Several respondents mentioned challenges in fully implementing these frameworks, including getting team buy-in or organizational alignment.
“We define developer productivity as the amount of story points the developer can clear per cycle vs the number of issues discovered in these during the QA cycle, however we do not track these in any formal framework such as DORA perceived overhead of adapting such systems is higher than the usefulness of these towards process improvement.”
Greg | Director, Engineering, Saas/software | 1K - 5K employees
- 1 Focus on velocity: Several respondents not following particular methodologies still mentioned using internal tools to gather metrics related to engineering velocity.
Focus on velocity: Several respondents not following particular methodologies still mentioned using internal tools to gather metrics related to engineering velocity.
“We are using a custom framework for developer productivity. The key aspects that we cover in the framework include velocity, quality of deliverables including amount of post development defects/bugs, frequency of deployments, and automation scripts that are built in during the development process.”
Sriganesh | Senior Director & Engineering Delivery Head, IT services & It consulting | 5K - 10K employees
- 1 Use of project management tools: Tools like Jira and GitHub were cited for their useful in tracking sprints, and measuring throughput.
Use of project management tools: Tools like Jira and GitHub were cited for their useful in tracking sprints, and measuring throughput.
“All of our dev teams have moved over to Jira for work tracking and productivity, so we tend to focus on throughput and value drops.”
Ron | Sr. Engineering Manager, Apparel & fashion | 5K - 10K employees
- 1 Combining sources for quality measurements: Many noted the difficulty of measuring productivity in general, but noted use of tools that enabled them to keep tabs on contributions.
Combining sources for quality measurements: Many noted the difficulty of measuring productivity in general, but noted use of tools that enabled them to keep tabs on contributions.
“We are not using any frameworks today that track specific developer productivity. We do have an internally built tool and some third party tools (SonarQube, etc.) where we monitor the quality of specific projects (test coverage, how long pull requests stay open, etc.). We do also look at GitHub contributions for developers to track their skill level and expertise growth, but it is more a manual process.”
Amber | Software Engineering Manager, Saas/software | 10K+ employees
- 1 Outcome-Based Measurement: Some organizations mentioned measuring developer productivity by business impact, such as new features that drive user engagement or sales.
Outcome-Based Measurement: Some organizations mentioned measuring developer productivity by business impact, such as new features that drive user engagement or sales.
“We are not currently using a framework. I personally define developer productivity through outcomes rather than output.”
Boydell | Sr Director of Software Engineering, Saas/software, E-learning providers | 501 - 1K employees
- 1 Quality as a proxy for productivity: Some respondents track the quality of code and the stability of deployments to assess the overall robustness of the software.
Quality as a proxy for productivity: Some respondents track the quality of code and the stability of deployments to assess the overall robustness of the software.
"We don't use any frameworks to measure developer productivity, but do assess the quality of code through peer reviews. We look for high-quality code which should be clean, well-documented, and should maintain consistency. We regularly check for the number of bugs reported in their code. knowledge sharing etc, and monitor team dynamics and collaboration, communication, mentorship and training new joiners etc."
Divya | Senior Manager SQA Engineering, Hospitals & healthcare | 10K+ employees
- 1 Satisfaction as a proxy of productivity: Some respondents mentioned focusing on dev satisfaction, recognizing that a positive work environment leads to greater productivity.
Satisfaction as a proxy of productivity: Some respondents mentioned focusing on dev satisfaction, recognizing that a positive work environment leads to greater productivity.
“I personally like SPACE, but at the org level we rely on DORA mostly. With my team I use other dimensions taken from SPACE, namely around team satisfaction via regular feedback cycles and specific activities.”
João | Software Engineering Manager, Financial services |1K - 5K employees

## Sizing the productivity problem

Survey respondents were asked several questions about how they perceive productivity at their organization, and whether or not they plan to dedicate resources to solving this year.

### Confidence in team productivity

When asked, “On a scale of 1-10, with 1 being extremely unproductive/efficient, and 10 being extremely productive/efficient, how productive/efficient do you think your software developers are?” The average score was 6.65, with the most selected answer being 7. While no leader scored their team below a 5, it should be noted that 90% of these same respondents also said improving productivity is a top priority this year (addressed in next section).

### Productivity as a business priority

When asked “On a scale of 1-10, with 1 being "not at all important," and 10 being "the most important," how important is it for your engineering team to improve developer productivity this year?” The average rating was 8.2, with 9 being the most frequent selection. 52% of those rating a 9 or 10 estimate weekly time lost to unproductive work to be between 5-15 hours (addressed in next section). Only two respondents scored this question under a 5 (one 2 and one 3), though each still estimated weekly time lost to unproductive work to be 3-5 hours and 5-15 hours respectively.

## Understanding detractors of productivity

In this section we’ll dive into what’s driving a team’s ability to be productive, and what might be slowing them down. Participants were asked questions about where developers are getting stuck, how much time they believe is lost to unproductive work.

### The source and impact of unproductive work

Participants were asked where developers tend to attribute dip in productivity, and time lost as a result.
Survey participants were asked, “What impediments to productivity do your developers tend to highlight most?” Top responses reflect the consequences of system sprawl—too much time spent on duplicate work when unsure what else exists, and too much time spent searching for context topped the list of complaints.
While unreliable data was near the bottom of the list, it should be noted that this blocker floats much higher for companies not using Internal Developer Portals. In fact, while no IDP users report data consistency as a blocker to productivity, 21% of leaders in companies without IDPs do believe this is a primary pain for developers.
Leaders were asked, “How long, on average, does it take for a newly hired developer to submit their first 3 meaningful PRs?” Most cited 1-3 months, which can be interpreted as the amount of time developers typically need to get access to the tools and information they need to be successful. The only participant to claim more than 9 months of onboarding time per developer also noted in another question that they believe the top impediment to their team’s productivity is how long it takes developers to find project context. This theme of slow “time-to-find” seems relevant to multiple productivity sub-topics.
Respondents were asked, “How many developer hours do you believe are lost to unproductive work (work that can be automated, obviated, or eliminated)?” 58% of respondents say at least 5 hours per dev per week are lost to unproductive work, with the top response (54%) falling in the 5-15 hour per dev per week range. Very few participants think more than 15 hours per dev per week are lost to unproductive work, but respondents in this category did have something in common—none use an Internal Developer Portal—a technology which findings above correlate with faster time to find, and higher data trust.

### Perceived productivity leaks and investments for improving

Survey respondents were asked several questions about what phases of onboarding and software development take the most time, and where the largest productivity leaks are hiding.
Survey participants were asked to stack rank time developers allocate to each phase of development, from the most time spent to the least. “Writing code” appears to be the area that takes the most time for the most respondents, but as we learn in the next section, this isn’t necessarily viewed as a problem.
Leaders were asked, “Where in the value stream listed above do you think has the largest productivity leak (most room for improvement/automation)?” Highest response rates related to KTLO—Keep the Lights On—activities like gathering context, waiting on approvals, and maintenance or bug fix work. This is also corroborated by what leaders hear most often from their teams—that they spend too much time hunting for the right information.
We can infer that the more operationally sound areas (comparatively speaking) are responding to incidents, reviewing PRs, gaining system access, and writing code, as these were less likely to be identified as the top areas of productivity leak.
When comparing two graphs above—productivity leaks and confidence in developer productivity—we see that the least confident teams are more likely to struggle with things like access to information, approval processes, and excessive maintenance. The most confident teams by contrast may have sorted those three issues, and are left with a final bridge to cross—optimizing the code writing process.
If we look forward to areas of investment, we’d expect to see that “elite” (most confident in productivity) organizations are planning to invest more in AI-coding assistants, while others (least confident in productivity) may be better off investing in reducing time to find information, easing maintenance work, and increasing developer self-service.
However, that isn’t quite what the data shows.
Participants were asked, “Which tool(s) do you plan to invest in this year that you expect to have a positive impact on developer productivity?” Interestingly, while “writing code” was not rated an area of high productivity leak—except by those with the highest confidence in their team’s existing level of productivity, coding assistants are rated as the #1 area of investment, even for teams with below-average confidence in productivity, and those rating time to gather context as a top productivity leak.
Results like these tend to indicate a situation where respondents may not know that a pain they’re feeling is solvable with new technologies.
In terms of appetite for each tool type by confidence in current productivity, the slight disparities between planned investments for the most and least confident teams may be useful in indicating which tools are appropriate next steps for certain phases of productivity maturity. For instance, the most confident teams are unlikely to be struggling with rudimentary problems like access to information, and may turn attention to tooling just tuned to measure productivity rather than improve it. Whereas less confident teams, still struggling with the basic pillars of productivity may be more focused on tools that help shore up complexity and improve visibility, like Internal Developer Portals.
This data also surfaces an important distinction between tools that help track output, and tools that improve outcomes. The question specifically asked which planned investments are thought to improve productivity, and while stand-alone engineering intelligence and survey tools may claim that benefit, this group of survey participants may disagree, with only 26% and 15% selecting those options as both planned investments and drivers of change.

## How Internal Developer Portals like Cortex improve developer productivity

Through this survey we’ve learned that teams not yet using Internal Developer Portals tend to struggle most with data trust, time to find information, and time spent waiting on approvals. In this section, we’ll explain why we believe the 33% of leaders in this survey say investing in Internal Developer Portals will make the biggest impact on developer productivity, and exactly how an IDP like Cortex can help.

### What is Cortex, and how can it help?

Cortex is an Internal Developer Portal built to address all three pillars of productivity in software development: how developers find context, reduce error, and speed creation of new software. Let’s take a look at exactly what goes into each value stream.
These survey results indicate that trouble finding context is the most often cited pain for developers (40%), while also being the top perceived area of productivity leak for managers (26%). Cortex’s IDP was designed to reduce time to find information during onboarding, in org designs, during incident response, or just as part of everyday efforts to maintain ownership of software created.
Fully custom catalogs , 50+ out of the box integrations , and the ability to bring in custom data mean that anything that details how software is built, by whom, when, and how, can be captured by catalogs segmented by software type like services, resources, APIs, infrastructure, etc.
[LINK: custom data](https://docs.cortex.io/docs/reference/basics/custom-data)
26% of leaders say maintenance and bug fix activities are now a top area of productivity leak, indicating a need to both improve software quality from the start, as well as insert a way of investing in quality improvements that reduce likelihood of unexpected issues down the road.
Because Cortex knows all of your data and documentation, it can continuously monitor alignment to software standards you define. So if code is updated, ownership changes, new tools are adopted, or old packages hit end-of-life, Cortex alerts developers to what needs attention, when.
26% of leaders identified “waiting on approvals” as a top productivity leak, and may be one of the main drivers for 37% of leaders citing upcoming investment in build and test optimization tools, and the 33% investing in Internal Developer Portals. Internal Developer Portals like Cortex enable teams to create libraries of scaffolding with boilerplate code that reduces time to code, accelerates launch, and improves quality from the start.
Teams can even speed onboarding, incident response, and infrastructure deployments with self-initiated workflows built from multiple actions or approvals chained together.

## Conclusions

Productivity is top of mind for all engineering leaders. While approach in tackling appears to vary widely across teams, underlying symptoms and impact are extremely similar:
- 1 Finding and acting upon the right information at the right time is a universal challenge as teams scale, and often the largest perceived productivity leak for both managers, and developers.
Finding and acting upon the right information at the right time is a universal challenge as teams scale, and often the largest perceived productivity leak for both managers, and developers.
- 2 While bug fixes and vulnerabilities are an inevitability for software development, lack of on-going attention to preventative health results in unplanned maintenance that drains productivity.
While bug fixes and vulnerabilities are an inevitability for software development, lack of on-going attention to preventative health results in unplanned maintenance that drains productivity.
- 3 Excessive manual approval processes disrupt flow state for developers and consume the (often even more expensive) time of managers and team leads
Excessive manual approval processes disrupt flow state for developers and consume the (often even more expensive) time of managers and team leads
Internal Developer Portals are a strong choice for teams wanting to tackle all three pillars of productivity, without compromising on scalability or developer experience. Improve time to value, reduce time to find, and unblock developers from the work that’s most valuable to them, and the organization as a whole.
A new study finds that Cortex customers realize 20% improvement to engineering productivity on tasks like gathering context and deploying new services and resources.
For more information on how Cortex’s Internal Developer Portal can improve your team’s productivity, read The Total Economic Impact™ Of Cortex IDP study , check out our self-guided tour , or connect with us for a personalized demonstration.

## Get started with Cortex


--------------------