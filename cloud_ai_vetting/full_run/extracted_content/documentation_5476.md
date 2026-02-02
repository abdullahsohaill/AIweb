# Documentation
**URL:** https://docs.gumloop.com/getting-started/introduction
**Page Title:** Getting Started with Gumloop
--------------------

[LINK: API Reference](/api-reference/authentication)
- Welcome to Gumloop 👋
- Getting Started
- Agents Using Agents in Slack Agent Node Custom Slack App Integration
- Agents
- Using Agents in Slack
- Agent Node
- Custom Slack App Integration
- Custom User Roles
- Usage Data Export
- Audit Logging
- AI Model Governance & Configuration
- Type Mismatch Errors
- List Size Mismatch Errors
- Join List Items vs Loop Mode
- Start Learning
- Build your first agent
- Build your first flow
Show Video Transcript
Before every meeting, I receive this in-depth report preparing me for whoever I’m meeting. It’s got information from
my CRM, recent news, and anything in previous conversations I need to bring up. I actually have nothing to do with
these. A Gumloop agent does all the work for me.
But I did build that agent. You can too. Let’s create it together and learn the basics of Gumloop while we’re at it.
Two steps. First, we’ll build an agent that gets all of the information we need from the various systems we work in
and sends me the report. Then we’ll create an automation that wakes that agent up 15 minutes before every meeting so
it can prepare the report for us.
So step one, let’s build an agent. Now I’m in the Gumloop hub and I’m going to agent and let’s create a new one.
Let’s call it sales preparation. Agents are kind of like super smart interns in Gumloop. You can give them access to
specific tools and data sources and explain how they should use them so they can do the work for you exactly as you
want them to.
All tools are included in your Gumloop subscription. Now for instructions, I’ll keep it pretty simple guiding the
agent to what I want it to do. You are a sales preparation meeting agent. You’ll be given an email, prepare a brief
report summarizing contact details from HubSpot and get recent news using XA. Email me a beautiful report.
Once it’s ready, we can now test this agent out by prompting it with “Prepare me for my meeting with billgates@microsoft.com ” and it follows its instructions and generates the report directly in my inbox. And I can
keep using this agent in the Gumloop UI, right where I am right now, or bring it into Slack for my whole team to
use. Now anyone can prepare themselves for their meetings as well using the agent that I’ve built.
Now, this is cool, but it’s not automated. What we want is 15 minutes before each meeting to wake our agent up, who
can do the work, and then shoot us an email with the report.
That’s a two step sequential automation. When a meeting is starting soon, help my agent who I’m meeting with. But
that information lives in the Google Calendar node. To pass information across nodes, I need to connect them and
then pass the attendee information over to the agent’s prompt.
Now, if I save this, that’s it. My automation is built. 15 minutes before each meeting, the Google Calendar node
will pass along the attendee information to the agent that’s gonna go ahead and grab all the information, generate
the report, and email it to me just with two nodes.
We’ve built an automation that works for all my meetings. Now there’s so much more we could do. We can improve our
agent to ignore meetings that are fully internal, add additional data sources, make the report better. And this is
only one example of what you can do with Gumloop.
Any task that you find yourself doing manually, you can now build an agent that can automate at least part of it.
Now I’m gonna link to a template for this meeting preparation agent. You can copy and start using today along with
additional resources to get started on your automation journey.

## ​ Start Learning

### ​ Build your first agent

Create an AI assistant that intelligently orchestrates your tools to solve complex tasks

### ​ Build your first flow

Create visual, drag-and-drop automations with 100+ pre-built nodes and integrations
Was this page helpful?

--------------------