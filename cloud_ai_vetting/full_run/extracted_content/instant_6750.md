# Instant
**URL:** https://instantdb.com
**Page Title:** Instant
--------------------


## instant

## instant

[LINK: Docs](/docs)
[LINK: GitHub](https://github.com/instantdb/instant)

## Write your frontend and we handle the rest

Instant is the easy to use backend for your frontend. With Instant you can build delightful apps in less than 10 minutes.
[LINK: Read the docs](/docs)

### Instant is a batteries included client-side database

To build an app you write two kinds of code. The business logic that solves your specific problem, and the generic stuff that most apps have to take care of: authenticating users, making queries, running permissions, uploading files, and executing transactions.
The generic stuff is critical to get right, full of edge cases, and also not the differentiating factor for your app — unless they’re broken
If all this work isn’t differentiating, why work on it?
Instant gives you a database with queries, transactions, auth, permissions, storage, real-time and offline support. All in a simple SDK you can use directly in the browser.
Here we implement chat using three functions: `init` , `useQuery` , and `transact`
" I wanted to build relational capabilities into Firebase (but it would have required us to build another database and we never got around to it). I'm glad to see Instant is doing it. "
" Most generic database query tools like react-query etc. are cached at the browser tab level. So if you rename a file, the tab bar can easily become out of sync unless you have a great local first sync provider... and I got it working easily with Instant. "
" Instant takes care of complex data ops so you can focus on building your product. I wouldn't want to use any other db right now. "
" Deeply nested, GraphQL-like queries that update in realtime are a dream come true. "
" I built a cross-platform app across mobile and React Native. I copy-pasted my data logic, and it all just worked! "
" I built an “email inbox” simulation with user auth/login, permissions, multiple folders (inbox /_ sent), and live updates (including sending across user accounts) in ~50 minutes or so. Very impressive stuff, and a lot of fun! "

### Real-time by default

The best apps today have a common feature set. Every interaction happens instantly, you rarely see loading screens, collaboration is easy and delightful, and the app still works when offline. When you use Instant, you get these features for free .
When apps are at their best, every change a user make should reflect instantly. There should be few spinners, loading states, or refresh buttons.
To do this today, you write custom code for endpoints, logic to apply optimistic updates, and to handle rollbacks.
Databases already know how to apply changes and handle rollbacks. With Instant, you write `transact` , and optimistic updates are handled for you.
Users seek collaborative experiences and sync across devices. To get this right, you need to set up sockets, cache and invalidate queries, and set up permission filters.
Instant takes inspiration from systems like Figma’s LiveGraph and Linear’s sync. We built the infrastructure that listens to transactions, and updates relevant queries.
Users want your app to work even when they're offline. Not only does this make your app available everywhere, it makes your app feel faster. The first time your app loads, users see a loading screen. Every load afterwards gets satisfied by the local cache.
To support this, you need a way to apply changes locally, persist to disk, and reconcile when users come back online.
Instant comes with this logic baked in: the local database knows what is committed to the server and what is pending. No need to deal with queues.

### Built for humans and agents

When we started building Instant we wanted something great for builders. We wanted to offer a generous free tier where projects aren't limited or paused. To make this work we built Instant to be multi-tenant. This means you can spin up a new database in less than 100ms.
Turns out when you make something great for humans, it also works great for agents. Combine a multi-tenant database with a platform SDK and you have infrastructure that lets an agent have a backend for every chat.
We wrote an essay to go deeper on what we mean. If this interests you and your team we'd love to chat.

### About the team

Instant is built by senior and staff engineers from Facebook and Airbnb. We spent multiple years thinking deeply about this problem and have built a product that we believe is the future of application development.
We're backed by YCombinator, SV Angel, and top investors like:
[LINK: GitHub](https://github.com/instantdb/instant)

--------------------