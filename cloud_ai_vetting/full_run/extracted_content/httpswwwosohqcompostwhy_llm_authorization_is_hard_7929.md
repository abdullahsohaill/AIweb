# https://www.osohq.com/post/why-llm-authorization-is-hard
**URL:** https://www.osohq.com/post/why-llm-authorization-is-hard
**Page Title:** Why LLM Authorization is Hard
--------------------

Recently, the General Analysis blog demonstrated how the Supabase MCP Agent can leak private data without escalating the privileges of either the user or the MCP Agent. The attack relied on three characteristics of the agent: two intrinsic to LLM applications (at least today), the third depressingly common among them:
- The agent accepts untrusted user input
- The agent can’t distinguish data from instructions
- The agent connects to the database with an overprivileged account
In the exploit, the attacker opened a support ticket with a malicious prompt to the agent. When the agent was later used to review the ticket, it interpreted the prompt in the ticket content as instructions to bypass internal controls and dump the contents of a sensitive table into the ticket.
This was the prompt:
To a human, this is obviously suspicious, but how do you block it programmatically? There’s no SQL to sanitize. Nothing that a regex could flag to prevent the attack. The only realistic way to prevent the agent from exposing the data in the integration_tokens table is to forbid it from reading that table in the first place.
In this post, we’ll take a look at why LLMs make that more difficult and build a model for authorization that accounts for their unique behaviors.

## What Makes LLM Applications Different?

Some of the most powerful features of LLMs are the same things that make them hard to authorize.
- They interpret natural language. Just like you and me, they can misunderstand instructions or be tricked into doing the wrong thing.
- They need broad potential permissions but narrow effective permissions. Any time a program acts with permissions it doesn’t need, you open the door to an exploit. When that program can be manipulated (see point 1), it’s basically inevitable.
- They operate on derived data. LLMs use a numerical representation of your data – not the data itself. But your access controls are on your data. You have to make the LLM honor those controls so it doesn’t leak data from its searches.
It’s up to us as builders of LLM applications to build strong authorization into our LLM apps so we can make misunderstandings less likely and minimize the damage when they do happen. Let’s look at each of these issues in more detail to learn how to do that.

## Prompts: Input that can be misunderstood…or worse

LLMs accept natural language as input and respond based on a probabilistic assessment of the text that should follow from the prompt.
Because LLM inputs are natural language, they carry all the ambiguity that any conversation does. If a user sends a prompt like:
What does “clean up” mean? Archive? Delete? Hide from view? Change status? Any of these is possible.
LLMs can also be manipulated. Natural language prompts give bad actors many more options for prompt injection than traditional inputs. That’s exactly what happened in the introductory example. It’s much harder to detect natural language prompt injection than it is to look for HTML or SQL in an input form, which is why it’s becoming more common in the rush to release LLM Agents.
If your application might misunderstand a user’s request, how do you remove the ambiguity without eliminating the natural language interaction that makes LLMs so compelling? How do you write an application that understands when it’s being manipulated when we’re notoriously bad at doing that for ourselves?

## Understanding Effective Permissions

Above, we said that one of the things that makes LLMs different is that they need broad potential permissions but narrow effectiv e permissions. To support all the features Supabase wanted to provide, they may in fact need the agent to use an administrative account. Perhaps it’s intended to back up databases or set up replication.
But for the operation that led to the exploit, it definitely didn’t need those permissions. One way the exploit could have been avoided is if the agent had assumed its user’s permissions while it was acting on their behalf. This is called impersonation , and it gives us a way to distinguish between potential and effective permissions. In authorization terms, it looks like this:
[LINK: impersonation](https://www.osohq.com/docs/modeling-in-polar/relationship-based-access-control-rebac/impersonation)
Typically, the impersonating party assumes all of the permissions of the person they’re impersonating. But this isn’t appropriate for an LLM. Since an LLM can misunderstand requests, it can do the wrong thing, and since it’s software, it can do it fast and forever.
What we need is a way to determine as quickly as possible:
- Who the user is, and
- What their request is
With that information, we can confine the application to the permissions that person has that are related to the request. But how can we do that dynamically, especially when the request might be something like “clean up the expenses”?

### To Share or Not to Share?

If Melody uses your chatbot to pull a report and then asks the chatbot to share the report with Violet, what should the chatbot do?
Does Melody have permission to share the report with Violet? Does Violet have permission to view the data in the report? What if Violet has permission to view some of the data, but not all of it?
We need to decide how to respond to all of these situations. If Melody’s not allowed to share, should we just block her? Should we ask her if she wants to send an approval request to her manager? What if Violet isn’t allowed to see all the data? Should we let Melody share it anyway? Seek approval again? Share a redacted report? All of this is authorization logic that ultimately determines the chatbot’s effective permissions.

### Unattended LLM Operations

You don’t necessarily want an LLM to respond to your prompt right now. You may want it to queue up an intensive operation to run after business hours. You might want to set up a recurring job. What if Melody asks the chatbot something like:
Does Melody have permission to pull the report? Or to archive expenses? What if archiving expenses is a sensitive operation and you only want it to be done by someone during their shift? If she makes the request during her shift, but it won’t be executed until after it ends, what then?
What identity should you use for this task? If you’re writing a script, you could have that script run as a service account that only has permission to view and archive closed expense reports from the previous month. But if your “job” is set up by someone prompting the LLM, should you use that user’s permissions? Should you have a different service account? How do you set its permissions when you don’t know the request ahead of time?

## Closing the Authorization Gap

Retrieval-Augmented Generation (RAG) is the process of sending additional data to an LLM with a user’s prompt. It’s how you can allow an LLM to use sensitive data like Expense Reports. The data that you send an LLM via RAG is called context .
LLMs don’t directly search your internal documents for context data. They’re mathematical models, so they operate over a numerical representation of the source text called an embedding . This separation between your data and the LLM’s view of it affects how you authorize LLM operations.
Your authorization logic is tied to your data, but the chatbot only sees the embeddings. You need to associate the two in order to authorize RAG responses.
When the data is in a third-party system, the gap becomes wider. Now, the embeddings and the data are on opposite sides of an API boundary. So for each embedding, you need to ask the third-party system whether Melody has permission to view the associated data.
How do you close this gap in a way that doesn’t introduce catastrophic latency? Do you try to reproduce the external system’s ACLs in your own system? That’s a lot of data to keep in sync. Do you reproduce the logic? Is it exposed by the system? If not, how will you infer it? Will you know when it changes? How will you update it when it does?

### Doesn’t OAuth solve all this?

A lot of people recommend OAuth for LLM authorization, but effective LLM authorization requires information about individual resources. If you want to know whether your chatbot should delete an expense for Melody, it’s not enough to know whether Melody can delete expenses. You need to know which expenses she can delete.
This is resource-level authorization , and it’s not feasible with OAuth. You’d have to put so much data on the token that you’d either run out of space on the token or you’d spend all your time synchronizing data and tracking down inconsistencies.
Instead, people generally define broad OAuth scopes like view:docs and delete:expense . This is only useful for route-level authorization. If all you need to know is whether Melody can delete expenses at all, that’s fine. But as soon as you need to distinguish the expenses she can delete from the ones she can’t, you have to get closer to your data. What you see with OAuth is that people do both, using OAuth only for the most basic route-level authorization and then pushing all the resource-level authorization down into the app.
So now you have to maintain authorization logic in two places: the route and the application, and you have to maintain authorization data in two different places: the OAuth token and your application database.

## The Model Context Protocol (MCP) – still not enough

The Model Context Protocol, released by Anthropic, defines a standard mechanism for exposing tools to LLM Agents. An MCP Server acts as a bridge between an LLM agent (called an MCP Host) and the external tools that it exposes. MCP Hosts and Clients no longer need to know the implementation details of the tools they use. They only need to know how to speak the MCP protocol. The simplicity of MCP and its clear separation of duties have led to incredibly fast adoption.
Unfortunately, for all that MCP has done to simplify Agent access to tools, it’s hasn’t done enough to help authorize that access. The MCP Server is just a bridge between agents and tools. It doesn’t know anything about the inner workings of the tools. It doesn’t know how access to them is governed, or what data they expose, or how to determine who should have access to that data.
If you have an MCP server that exposes a delete_expense tool, you’re no better off authorizing that task than you were when you were checking OAuth scopes on the API routes. At the MCP server, you can only support very coarse authorization – Melody either can use the delete_expense tool or she can’t. If you need to get any more specific – if Melody can only delete her team’s expenses, or can only delete expenses at the end of a fiscal year – then you need to get closer to the expenses so you can apply resource-level authorization.

### Actually enforce the principle of least privilege

People have been talking about least privilege for years, but in practice we overpermission users for convenience. We’ve let this happen for convenience, but we’re starting to see how much of a problem it is. Broken Access Control is now the #1 item on OWASP’s Top 10 Web Application Security Risks .
LLMs make this an even bigger risk. They lack judgment, they have superhuman speed, and they never tire. An LLM may breach your trust without even knowing it’s doing so, and if it does, you won’t know until it’s much too late. So for any given operation, an LLM should have at most the specific permissions that are required for that operation.
For example, if your LLM has full control of your document store and Sarah asks for a summary of company policies, then the LLM’s effective permissions should be:
- read-only (the LLM only needs to view data)
- on data that Sarah is allowed to view (the LLM is acting on Sarah’s behalf)
- that is related to company policy (Sarah’s not interested in things like vendor agreements)
You can visualize this as a Venn Diagram. For any task, an LLM’s effective permissions are the intersection of
- the LLM’s permissions
- the user’s permissions
- the permissions required for that task
The task should only be authorized if both the LLM and the user have all the necessary permissions.
By following this principle, you can ensure that the LLM’s permissions are always scoped to both the user and the task.
But it’s one thing to draw this in a Venn Diagram. It’s another to pull it off in the real world. One thing we can do right now to get closer to this picture is to implement impersonation in our LLM authorization models. We can identify the user who’s making a request, so we can confine the LLM’s permissions to that user’s permissions.
What’s trickier is confining permissions to the task. First, as we’ve shown, it’s not necessarily trivial even to identify what the task is. Once identified, we may not have a clean mapping of permissions to tasks. We could add LLM-specific task permissions to our authorization policy, but that feels like needless duplication. Ideally we’d reuse the logic we’ve already built. Still, this model shows us where we want to go.

### Authorize LLM operations in the application

This least-privilege model of requires resource-level authorization. Coarse authorization doesn’t cut it. When Melody gives your Agent a task like “Delete Expense Report 123,” it doesn’t matter that she has the delete:expenses scope. You don’t know whether she can delete this expense without information about Melody, Expense Report 123, and the business logic that determines when Expense Reports can be deleted.
To get to that information, you need to close the gap between the LLM and your data. You don’t have the information at the route. You don’t have it in an OAuth token. You don’t have it at the MCP server. You don’t have it in the LLM model.
The application is the only place where you’re close enough to the resources to get the data you need and where you can use the abstractions in your business logic to enforce authorization.

## Conclusion

LLMs represent a fundamentally new model of human/computer interaction. For the entire history of software development, our code has done exactly what we tell it to do. All of our mechanisms for predicting, testing, and debugging application behavior are built on this assumption. But now, for the first time, we’re writing programs that try to interpret what we mean instead of just doing what we say. Nothing in our experience was built for software that can misunderstand.
This isn’t cause for alarm. It’s a call to be thoughtful. By identifying the effective permissions of an LLM operation and closing the authorization gap between LLMs and the resources it exposes, we can enforce true least-privilege authorization in LLM applications. This makes a misunderstanding less likely (the LLM has fewer options) and less harmful (the LLM has less agency). We have our map - we just have to build a couple new roads.
If you’d like to dig into this more deeply, check out our new Authorization Academy chapter on Authorization in LLM applications . If you’d like to talk it over a bit more, come visit us on Slack. If you're ready to start building, try our new SQLAlchemy Extension that does the hard work of closing the authorization gap for you.
LLM applications aren’t going anywhere. They’ve proven too useful and too powerful in too short a time. But that same utility and power make authorizing LLM applications both more urgent and more complicated than traditional applications. These are hard problems, but they’re solvable ones – and they’re the problems we solve at Oso.

## Frequently asked questions

## Greg Sarjeant

### Developer Experience Engineer

## Related content

## Ready to get started?


--------------------