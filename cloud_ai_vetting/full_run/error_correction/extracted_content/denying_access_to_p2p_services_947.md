# denying access to p2p services
**URL:** https://www.eff.org/deeplinks/2007/10/eff-tests-agree-ap-comcast-forging-packets-to-interfere
**Page Title:** EFF tests agree with AP: Comcast is forging packets to interfere with user traffic | Electronic Frontier Foundation
--------------------

- About Contact Press People Opportunities EFF's 35th Anniversary
- Contact
- Press
- People
- Opportunities
- EFF's 35th Anniversary
- Issues Free Speech Privacy Creativity and Innovation Transparency International Security
- Free Speech
- Privacy
- Creativity and Innovation
- Transparency
- International
- Security
- Our Work Deeplinks Blog Press Releases Events Legal Cases Whitepapers Podcast Annual Reports
- Deeplinks Blog
- Press Releases
- Events
- Legal Cases
- Whitepapers
- Podcast
- Annual Reports
- Take Action Action Center Electronic Frontier Alliance Volunteer
- Action Center
- Electronic Frontier Alliance
- Volunteer
- Tools Privacy Badger Surveillance Self-Defense Certbot Atlas of Surveillance Cover Your Tracks Street Level Surveillance apkeep
- Privacy Badger
- Surveillance Self-Defense
- Certbot
- Atlas of Surveillance
- Cover Your Tracks
- Street Level Surveillance
- apkeep
- Donate Donate to EFF Giving Societies Shop Sponsorships Other Ways to Give Membership FAQ
- Donate to EFF
- Giving Societies
- Shop
- Sponsorships
- Other Ways to Give
- Membership FAQ
- Donate Donate to EFF Shop Other Ways to Give
- Donate to EFF
- Shop
- Other Ways to Give
- Copyright (CC BY)
- Trademark
- Privacy Policy
- Thanks

## EFF tests agree with AP: Comcast is forging packets to interfere with user traffic

## EFF tests agree with AP: Comcast is forging packets to interfere with user traffic

This morning the Associated Press reported that Comcast is interfering with users' ability to run file sharing applications over its network.
Since we spoke to Comcast last month and understood them to deny that they are doing this, we've been running our own tests.
The results of our tests have agreed with AP's.  Comcast is forging TCP RST packets which cause connections to drop (a technique also used by Internet censorship systems in China ).  These packets cause software at both ends to believe, mistakenly, that the software on the other side doesn't want to continue communicating.
The TCP RST packet forging seems to be protocol-specific: as AP reported, it at least sometimes happens directly in response to specific BitTorrent protocol events.  This contradicts Comcast's statement to us that their network management does not target or discriminate against particular protocols.  The timing of the injected packets suggests that something on Comcast's network understands the BitTorrent protocol and treats it differently from other protocols.
We confirmed this by trying to download files from Comcast subscribers using BitTorrent.  We disabled any firewall or NAT software and connected the machines at both ends directly to the Internet, and ran Wireshark, a packet capture tool.  This allows us to see exactly what packets each end sent and exactly what packets each end receives.  If ISPs between both points were not forging packets, no packets should have been received by one end that bear the other end's IP address but were not sent by it(*).  (This is comparable to recording a telephone conversation at both ends and then comparing the recordings to see whether the phone company sent the conversation through faithfully and unmodified.)
Unfortunately, the resulting packet traces look drastically different from one another: each user routinely receives huge numbers of TCP RST packets that appear to have been sent by the other user.  But the packet trace at the other end confirms that these packets were never transmitted; they must have been generated and injected by an ISP along the way.
How do we know that Comcast is responsible?  Apart from the large number of reports accusing Comcast, increasingly accompanied by packet traces showing suspicious RST packets, we repeated the experiment with two different Comcast connections (one in San Francisco, and one in Oregon) and saw the RST packets appear in both cases.  When the Comcast user in Oregon -- Robb Topolski, a source for the AP story and one of the first to carefully document the RST forging phenomenon -- switched on a VPN connection that caused his communications to be encrypted and routed through a different ISP, the RST packets completely disappeared.
Comcast keeps telling its users that the problems they're seeing are not its fault.  It's time for Comcast to come clean about what it's doing and take its users' reports seriously.
(*) Note to network experts: IP fragmentation does allow for the possibility that a single packet sent by one end could arrive in multiple fragments, none of which was originally sent in fragmented form.  However, we did not observe any fragmentation at all during our experiments and, in particular, the forged RST packets are clearly not fragments of packets sent by the other end.

## Related Issues

## Related Updates

Last week, the FCC announced the " FCC Open Internet Apps Challenge ," a contest to attract software that helps ordinary users measure whether their Internet services — both mobile broadband and traditional "fixed" broadband — are consistent with open Internet principles. The FCC is also asking for submissions of "research...
In a ruling that imposes important limits on the FCC's authority to regulate the Internet, the D.C. Circuit Court of Appeals today overturned the FCC ruling against Comcast for interfering with the BitTorrent traffic of its subscribers . The court found that the Commission...
Remember what put the debate over net neutrality into high gear? In 2007, EFF and the Associated Press confirmed suspicions that Comcast was clandestinely blocking BitTorrent traffic. It was one of the first clear demonstrations that ISPs are technologically capable of interfering with your Internet connection, and that they...
UPDATE (9/4/14): The net neutrality landscape has changed in the last few years, and not for the better. Here's a discussion about EFF's updated stance and here's our issue page , with links to our most recent blog posts. On Thursday, Federal Communications Commission (FCC) Chairman Julius Genachowski...
Today, the New America Foundation, PlanetLab and Google announced the launch of the Measurement Lab project, an initiative to provide server resources for researchers interested in network neutrality and performance testing. This is good news for the community of academics and activists who are trying to map, measure and...
Late on Friday night, Comcast filed an overview of its new traffic management arrangements with the FCC. This is the long term replacement for its controversial practice of using forged TCP Reset packets to limit the use of peer...
The FCC has finally published its order ( adopted on August 1 ) directing Comcast to stop blocking BitTorrent traffic. The 34-page ruling makes for surprisingly enjoyable reading, at least as FCC publications go. The order follows the basic outline that was explained by Chairman Martin in his statement ...
[LINK: 34-page ruling](http://hraunfoss.fcc.gov/edocs_public/attachmatch/FCC-08-183A1.pdf)
[LINK: statement](http://hraunfoss.fcc.gov/edocs_public/attachmatch/FCC-08-183A2.pdf)
Earlier this month, Internet users welcomed the FCC's ruling against Comcast for interfering with BitTorrent uploads, celebrating the action as a victory for net neutrality. Reigning in Comcast's dishonest behavior was the right thing to do in this case, but many observers are worried that the FCC is establishing...
On Friday, the FCC voted , 3-2, to punish Comcast for its surreptitious interference with BitTorrent uploads (a practice that EFF helped uncover and document in October 2007). The Commission adopted an order (text of which hasn't been released yet) finding that Comcast violated the neutrality principles set out...
[LINK: the FCC voted](http://hraunfoss.fcc.gov/edocs_public/attachmatch/DOC-284286A1.pdf)
San Francisco - Hours before the Federal Communications Commission (FCC) is expected to take action against Comcast for violating the FCC's net neutrality principles, the Electronic Frontier Foundation (EFF) is releasing "Switzerland," a software tool for customers to test the integrity of their Internet communications. The FCC action, expected...

## Related Issues

Back to top

## Follow EFF:

- mastodon
- facebook
- instagram
- Blue Sky
- youtube
- flicker
- linkedin
- tiktok
- threads
Check out our 4-star rating on Charity Navigator .

## Contact

- General
- Legal
- Security
- Membership
- Press

## About

- Calendar
- Volunteer
- Victories
- History
- Internships
- Jobs
- Staff
- Diversity & Inclusion

## Issues

- Free Speech
- Privacy
- Creativity & Innovation
- Transparency
- International
- Security

## Updates

- Blog
- Press Releases
- Events
- Legal Cases
- Whitepapers
- EFFector Newsletter

## Press

- Press Contact

## Donate

- Join or Renew Membership Online
- One-Time Donation Online
- Giving Societies
- Corporate Giving and Sponsorship
- Shop
- Other Ways to Give
- Copyright (CC BY)
- Trademark
- Privacy Policy
- Thanks

--------------------