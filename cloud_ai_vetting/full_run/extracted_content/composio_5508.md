# Composio
**URL:** https://dub.composio.dev/composio
**Page Title:** Composio - Skills that evolve with your Agents
--------------------

Stay updated.
Join discord
Compare
Vs pipedream
product
pricing
startups
enterprise
agent auth
MCP GAteway
resources
docs
[LINK: docs](https://docs.composio.dev/getting-started/welcome)
blog
cookbooks
OAuth2 guides
Case Studies
Toolkits
COMPANY
Careers
trust
Support
Terms
Privacy Policy
©  Composio 2025

## Skills that evolve with

your Agents
More than just integrations, 10,000+ tools that
can adapt — turning automation into intuition.
get started for free
[LINK: Explore docs](https://docs.composio.dev/getting-started/welcome)
Explore docs
Used by Agents from
Muscle Memory
for Intelligence
In a world with countries of geniuses in datacenters , we believe the most important thing is for them to be able to take complex actions and learn from them in realtime — to
build intuitions, to build skills, they can plug & play to create real economic value. We are creating that layer that lets intelligence build intuition .
the results
[LINK: 18,370+ Stars on GitHub](https://github.com/composiohq/composio/)
Stars on GitHub
Customers
Developers
Successful Calls
Building agents that take action is hard
building integrations
optimising JSON schema for agents
scaling to millions of tools execution
managing auth and permissions for tools
Composio erases that drag in one call
Use an
AI Agent
to detect bugs in Slack, auto-log them
to GitHub and Notion
Product Manager
Use an
AI Agent
to detect bugs in Slack, auto-log them
to GitHub and Notion
Product Manager
Tools
Onboard and assign issues
Detect bugs and auto-log them
LLM
Implement Slack, GitHub, and Notion APIs
# ---- GitHub ----
def create_github_issue(repo, title, body, token):
url = f"https://api.github.com/repos/{repo}/issues"
headers = {"Authorization": f"token {token}"}
data = {"title": title, "body": body}
return requests.post(url, json=data, headers=headers)
# ---- Notion ----
def log_to_notion(database_id, title, github_url, notion_token):
url = "https://api.notion.com/v1/pages"
headers = {
"Authorization": f"Bearer {notion_token}",
"Content-Type": "application/json",
"Notion-Version": "2022-06-28"
# ---- Slack ----
def reply_in_slack(channel, thread_ts, text, slack_token):
url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": f"Bearer {slack_token}"}
data = {
"channel": channel,
"thread_ts": thread_ts,
"text": text
return requests.post(url, json=data, headers=headers)
Manage 3 Different OAuth Flows (Slack, GitHub, Notion)
# Redirect user to GitHub's OAuth URL
github_oauth_url = f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=repo"
# User is redirected back with a ?code=xyz
# Exchange code for access token
def exchange_github_code_for_token(code):
response = requests.post(
"https://github.com/login/oauth/access_token",
headers={"Accept": "application/json"},
data={
"client_id": CLIENT_ID,
"client_secret": CLIENT_SECRET,
"code": code,
return response.json().get("access_token")
Create a Slack Event Subscription and Webhook Endpoint
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/slack/events", methods=["POST"])
def handle_event():
data = request.json
# Slack verification challenge
if data.get("type") == "url_verification":
return jsonify({"challenge": data["challenge"]})
event = data.get("event", {})
if event.get("type") == "message"
hrs
without Composio
with Composio
Turn bugs on Discord thread into Github issues and sync with Calendar events.
Toolkits required
bug details extracted
issues created
'bug bash' event added
notifications sent
time taken  →
time taken  →
time taken  →
time taken  →
Composio
An all in one seamless layer that lets LLMs and agents reliably interact with tools in the real world.
Authentication
Manage triggers
Set tools and actions
Use multi-agents
LLM
Composio listens to your LLM’s function or tool calls, handles authentication, maps the call to a real-world API, and executes it reliably.
AI Agent
Connect with over 25 agentic frameworks, allowing AI agents to autonomously plan, coordinate, and execute actions across tools while your agent focuses on planning and execution is handled seamlessly.
Tools
Onboard and assign issues
Detect bugs and auto-log them
AI Agent
Lang Chain
Lang Graph
AutoGen
Vercel
CrewAI
Lang Graph
Crew AI
Vercel
Lang Chain
Auto Gen
LLM
Open AI
Claude
Gemini
Grok
Open AI
Claude
Gemini
Grok
Turn bugs on Discord thread into Github issues and sync with Calendar events.
Toolkits required
bug details extracted
issues created
'bug bash' events added
notifications sent
time taken  →
Composio
An all in one seamless layer that lets LLMs and agents reliably interact with tools in the real world.
Authentication
Manage triggers
Set tools and actions
Use multi-agents
LLM
Composio listens to your LLM’s function or tool calls, handles authentication, maps the call to a real-world API, and executes it reliably.
AI Agent
Connect with over 25 agentic frameworks, allowing AI agents to autonomously plan, coordinate, and execute actions across tools while your agent focuses on planning and execution is handled seamlessly.
0.5

### Karan skipped his own birthday party to fix our critical issue. It was 10 pm and he diverted his Waymo to help us instead. This really sets the bar, shows you the commitment you need to have when users rely on your software

### We chose Composio over Pipedream because it delivered depth where it mattered. It supported niche tools and tricky edge cases that other platforms simply ignored. Giving us confidence to scale without compromising .

### " Before partnering with Composio, adding tool integrations was a slow, resource-intensive process . Each integration could take weeks or months of engineering time, and maintaining them meant constantly keeping up with API changes."

### A lot of students tell us that the moment their connected tools start talking to each other inside Opennote feels almost magical. The agent just knows them, and it has immensely helped in keeping new users on the platform .

### Tool Router turned integrations into a truly plug‑and‑play experience ; it just worked with our agent out of the box. We stopped burning time on one-off integrations because auth and connections were already handled , allowing us to stay focused on building Saga.

Customer Stories
Built for Agents
Our easy-to-use APIs make it effortless to ship agents.
*Developers welcome
25K +
stars on Github
[LINK: EXPLORE DOCS 2 min setup](https://docs.composio.dev/getting-started/welcome)
EXPLORE DOCS
2 min setup
Agent Auth
Let us manage all the headaches of auth for your tools
Tool Observability
Track every tool execution and trigger event in real-time from a single, unified dashboard.
Plug and Play
You can use with any language, any llm and all the frameworks you love (or hate)
Quick to Start — Effortless to Scale
We can help you scale to billions of tool calls effortlessly
Agent First Documentation
Our docs and examples are agent first should be easy enough for humans
Agent Auth
Let us manage all the headaches of auth for your tools
Tool Observability
Track every tool execution and trigger event in real-time from a single, unified dashboard.
Built a workflow that used to take 3 services and 2 meetings.
Built a workflow that used to take 3 services and 2 meetings.
- Slava Kurilyak Composio has set out to empower AI Agents with essential tools. It allows you to plug 90 + tools into your AI agents. Ship super fast without worrying about integrations. Yohei core loop is activity selection and execution, which kicks off after configuring your character and choosing an LLM auth into composio tools for dynamic skills or add your own in the skill folder. then build activities that use these skills!
Slava Kurilyak
Composio has set out to empower AI Agents with essential tools. It allows you to plug 90 + tools into your AI agents. Ship super fast without worrying about integrations.
Yohei
core loop is activity selection and execution, which kicks off after configuring your character and choosing an LLM auth into composio tools for dynamic skills or add your own in the skill folder. then build activities that use these skills!
- Tereza Tizkova Nice, yes I think Composio is an important "puzzle piece" in the ecosystem! Tom Osman got to  @composiohq  and one click get a MCP url for 100+ apps.
Tereza Tizkova
Nice, yes I think Composio is an important "puzzle piece" in the ecosystem!
Tom Osman
got to  @composiohq  and one click get a MCP url for 100+ apps.
- Jerry Liu Automatic powerpoint generation is a HUGE enterprise agent use case.  Check out this stack with  @llama_index ,  @composiohq , and @e2b_dev below. Huge shoutout to  @KaranVaidya6   👇 Burca Paul Big shoutout to  @composiohq !   This team excels at handling not just issues, but our internal requirements too.   I've never seen problems resolved so quickly. 💪 #CustomerSupport #AssistaAI
Jerry Liu
Automatic powerpoint generation is a HUGE enterprise agent use case.  Check out this stack with  @llama_index ,  @composiohq , and @e2b_dev below. Huge shoutout to  @KaranVaidya6   👇
Burca Paul
Big shoutout to  @composiohq !   This team excels at handling not just issues, but our internal requirements too.   I've never seen problems resolved so quickly. 💪 #CustomerSupport #AssistaAI
- João Moura Composio is set out to build better tools for AI Agents and guess what they have a native integration with crewAI! I met a user that is using them today and am dying to give it a try! Together AI Together and  @composiohq  are partnering to bring an easy way for developers to build agents!  • Use the top open source LLMs on Together AI along with 250+ tools from Composio  • Your LLMs on Together can now use everything.
João Moura
Composio is set out to build better tools for AI Agents and guess what they have a native integration with crewAI! I met a user that is using them today and am dying to give it a try!
Together AI
Together and  @composiohq  are partnering to bring an easy way for developers to build agents!  • Use the top open source LLMs on Together AI along with 250+ tools from Composio  • Your LLMs on Together can now use everything.
- Slava Kurilyak Composio has set out to empower AI Agents with essential tools. It allows you to plug 90 + tools into your AI agents. Ship super fast without worrying about integrations. Yohei core loop is activity selection and execution, which kicks off after configuring your character and choosing an LLM auth into composio tools for dynamic skills or add your own in the skill folder. then build activities that use these skills!
Slava Kurilyak
Composio has set out to empower AI Agents with essential tools. It allows you to plug 90 + tools into your AI agents. Ship super fast without worrying about integrations.
Yohei
core loop is activity selection and execution, which kicks off after configuring your character and choosing an LLM auth into composio tools for dynamic skills or add your own in the skill folder. then build activities that use these skills!
- Tereza Tizkova Nice, yes I think Composio is an important "puzzle piece" in the ecosystem! Tom Osman got to  @composiohq  and one click get a MCP url for 100+ apps.
Tereza Tizkova
Nice, yes I think Composio is an important "puzzle piece" in the ecosystem!
Tom Osman
got to  @composiohq  and one click get a MCP url for 100+ apps.
- Jerry Liu Automatic powerpoint generation is a HUGE enterprise agent use case.  Check out this stack with  @llama_index ,  @composiohq , and @e2b_dev below. Huge shoutout to  @KaranVaidya6   👇 Burca Paul Big shoutout to  @composiohq !   This team excels at handling not just issues, but our internal requirements too.   I've never seen problems resolved so quickly. 💪 #CustomerSupport #AssistaAI
Jerry Liu
Automatic powerpoint generation is a HUGE enterprise agent use case.  Check out this stack with  @llama_index ,  @composiohq , and @e2b_dev below. Huge shoutout to  @KaranVaidya6   👇
Burca Paul
Big shoutout to  @composiohq !   This team excels at handling not just issues, but our internal requirements too.   I've never seen problems resolved so quickly. 💪 #CustomerSupport #AssistaAI
- João Moura Composio is set out to build better tools for AI Agents and guess what they have a native integration with crewAI! I met a user that is using them today and am dying to give it a try! Together AI Together and  @composiohq  are partnering to bring an easy way for developers to build agents!  • Use the top open source LLMs on Together AI along with 250+ tools from Composio  • Your LLMs on Together can now use everything.
João Moura
Composio is set out to build better tools for AI Agents and guess what they have a native integration with crewAI! I met a user that is using them today and am dying to give it a try!
Together AI
Together and  @composiohq  are partnering to bring an easy way for developers to build agents!  • Use the top open source LLMs on Together AI along with 250+ tools from Composio  • Your LLMs on Together can now use everything.
- Slava Kurilyak Composio has set out to empower AI Agents with essential tools. It allows you to plug 90 + tools into your AI agents. Ship super fast without worrying about integrations. Yohei core loop is activity selection and execution, which kicks off after configuring your character and choosing an LLM auth into composio tools for dynamic skills or add your own in the skill folder. then build activities that use these skills!
Slava Kurilyak
Composio has set out to empower AI Agents with essential tools. It allows you to plug 90 + tools into your AI agents. Ship super fast without worrying about integrations.
Yohei
core loop is activity selection and execution, which kicks off after configuring your character and choosing an LLM auth into composio tools for dynamic skills or add your own in the skill folder. then build activities that use these skills!
- Tereza Tizkova Nice, yes I think Composio is an important "puzzle piece" in the ecosystem! Tom Osman got to  @composiohq  and one click get a MCP url for 100+ apps.
Tereza Tizkova
Nice, yes I think Composio is an important "puzzle piece" in the ecosystem!
Tom Osman
got to  @composiohq  and one click get a MCP url for 100+ apps.
- Jerry Liu Automatic powerpoint generation is a HUGE enterprise agent use case.  Check out this stack with  @llama_index ,  @composiohq , and @e2b_dev below. Huge shoutout to  @KaranVaidya6   👇 Burca Paul Big shoutout to  @composiohq !   This team excels at handling not just issues, but our internal requirements too.   I've never seen problems resolved so quickly. 💪 #CustomerSupport #AssistaAI
Jerry Liu
Automatic powerpoint generation is a HUGE enterprise agent use case.  Check out this stack with  @llama_index ,  @composiohq , and @e2b_dev below. Huge shoutout to  @KaranVaidya6   👇
Burca Paul
Big shoutout to  @composiohq !   This team excels at handling not just issues, but our internal requirements too.   I've never seen problems resolved so quickly. 💪 #CustomerSupport #AssistaAI
- João Moura Composio is set out to build better tools for AI Agents and guess what they have a native integration with crewAI! I met a user that is using them today and am dying to give it a try! Together AI Together and  @composiohq  are partnering to bring an easy way for developers to build agents!  • Use the top open source LLMs on Together AI along with 250+ tools from Composio  • Your LLMs on Together can now use everything.
João Moura
Composio is set out to build better tools for AI Agents and guess what they have a native integration with crewAI! I met a user that is using them today and am dying to give it a try!
Together AI
Together and  @composiohq  are partnering to bring an easy way for developers to build agents!  • Use the top open source LLMs on Together AI along with 250+ tools from Composio  • Your LLMs on Together can now use everything.
Power of Thousands of Tools
in the palm of your agent’s hands.
Agent Auth
We handle the fun stuff like auth so you can make agents faster.
Evolving Skills
Our skills improve over time as more agents use them
Composio MCP
Access fully-managed MCP servers from a single dashboard
Accurate Tool Calls
With tool calls that just work, your agents perform 30% better.
SOC 2 Type ||
Safe-guard your data from SKYNET ;)
Usage based Pricing
Composio is built to help you scale. From the birth of your first agent to your IPO, we’re there to grow with you.
compare plans
Totally Free
No credit card required
20k tool calls/mo
Community support
No usage based
/ month
Ridiculously Cheap
No need to talk to humans
200k tool calls/mo
Email support
$0.299/1K additional calls
$29
/ month
Serious Business
Maybe talk to humans?
2M tool calls/mo
Slack support (1k+/month)
$0.249/1K Additional Calls
$229
/ month
For Enterprise
Secure, reliable and accurate LLM integrations at scale.
Custom user accounts
Custom API volume
Dedicated SLA & SOC-2
VPC/on-prem option
Contact for custom quote
Book a call
Life rewards action not intelligence
curl -fsSL https://composio.dev/install | bash
SIGN IN
[LINK: Explore docs](https://docs.composio.dev/getting-started/welcome)
Explore docs
Stay updated.
Join discord
Compare
Vs pipedream
product
pricing
startups
enterprise
agent auth
MCP GAteway
resources
docs
[LINK: docs](https://docs.composio.dev/getting-started/welcome)
blog
cookbooks
OAuth2 guides
Case Studies
Toolkits
COMPANY
Careers
trust
Support
Terms
Privacy Policy
©  Composio 2025
RUBE(MCP)
pricing
blog
[LINK: docs](https://docs.composio.dev/getting-started/welcome)
docs
Toolkits
Solutions
Sign in

--------------------