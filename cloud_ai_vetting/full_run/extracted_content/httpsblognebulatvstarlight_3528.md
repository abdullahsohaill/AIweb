# https://blog.nebula.tv/starlight/
**URL:** https://blog.nebula.tv/starlight
**Page Title:** Starlight — Nebula Blog
--------------------


### Nebula Blog

## Starlight

### November 13, 2022

Over the last three and a half years, Nebula’s weakest link has been the streaming video pipeline itself. Nebula is a bootstrapped service that has grown so much faster than any of us had anticipated, so a lot of the early technical decisions were made in the interests of limited time and even more limited resources. The net effect for users has been occasionally (but not predictably) spotty video as we’ve relied on third-party services.
Last year we began working on our own solution, and we’re happy to report that it’s starting to roll out now. Introducing Starlight, our custom in-house transcoding and distribution pipeline.
Starting now, all new 1080p uploads will be handled by Starlight. 4K videos are still going through the old system for now while we work to improve transcoding times. Our goal is to have Starlight handling 4K content by the end of the year. Once that’s up and running, we’ll begin transcoding catalog videos to bring everything in-house. No ETA on that yet. The priority is very high to get this done, but even higher to get it right.
One of the more common support issues we get is complaints that videos get stuck buffering and never play. The reason for this, almost always, is that our current provider uses h.264 for 4K video. Starlight uses h.265 and VP9, resulting in smaller file sizes that won’t cause browsers to choke and die. Once we flip the switch on 4K later this year, that problem should be solved. In the short term, Starlight 1080p means higher-quality video — especially on mobile — with better insight and control of the system when problems arise.
Another common complaint is Cast support. Right now, videos cast in 480p. On a screen larger than your phone, this looks awful. (Honestly it doesn’t even look that great on your phone.) Starlight fixes this, allowing better video quality when casting to your TV. It also adds support for subtitles. An important win for accessibility.
There are other issues we don’t have clear answers for yet because our current provider provides no transparency in their process. (We’re not even allowed to know who the CDN provider is.) Even here, we’re very optimistic that running our own service will allow our team to better track down root causes and solve them for good. No more reaching out to third parties to help diagnose user problems.
For everyone who has run into problems, we appreciate your patience. The team has been hard at work behind the scenes and we’re excited to finally get to share progress.
So much of Nebula’s mission is about allowing the creators — the primary owners of the platform — better opportunity to control their own destiny. With Starlight, we capture a little more of that control on the technical and business sides as well.

--------------------