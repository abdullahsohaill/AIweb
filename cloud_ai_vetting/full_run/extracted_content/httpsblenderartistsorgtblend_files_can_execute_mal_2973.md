# https://blenderartists.org/t/blend-files-can-execute-malware/1591331
**URL:** https://blenderartists.org/t/blend-files-can-execute-malware/1591331
**Page Title:** Blend files can execute malware - General Forums / Latest News - Blender Artists Community
--------------------

- Topics
- FAQ
- New Artwork
- Trending Artwork
- Unanswered Questions
- Artwork
- Support
- Coding
- Game Engine
- Jobs
- General Forums
- All categories
- featured
- nodevember
- All tags

### Cozy ramen

### Rendered similar to black and white film

### Jack Daniel's 3D Render using Blender 3D

### Through the mirror

### Lila - Advanced Character Rigging

### No Fate

## ADVERTISEMENT

## Blend files can execute malware

You have selected 0 posts.
select all
cancel selecting
Blender AdNet - learn more
In case anyone needs another reminder not to click untrusted links on the internet : This week Superhive (formerly Blender Market) vendors were the target of some malicious attacks. Many (myself included) received a legitimate-sounding support ticket asking for help with their product, probably AI-generated to target them specifically.
Attached to the ticket was a seemingly innocent blend file. A chair model. When opening the file, Blender asks if you want to execute “rig_ui.py”. Sure, why not? Many rigs in Blender are made with Python scripts.
Little do you know, this Python script (which even upon vague inspection appears to be a real rig UI) generates itself a Powershell script, and executes it.
The Powershell script embeds and hides itself on your system, running on startup. What does it do? It downloads another script and automatically executes that every few seconds.
What does that script do? The same thing - downloads another script, and executes it. And down the rabbit hole it goes for a few more similar scripts. Each layer is obfuscated, encrypted, and/or in another language (programming or literary), making it hard to tell what it does, other than “something sketchy”.
The last layer I could reach times out so I couldn’t see what this malware actually does, which is not to say it doesn’t do anything, but that the authors can remotely enable the service at any time, which will trigger your machine to run whatever code they want. Instantly. You won’t even know it’s happening.
What’s unnerving is how well it’s targeted at Superhive vendors with plausible DMs, and hidden in a way that’s difficult for most users to detect as part of the rig code. The only thing suspicious is that a static chair model with no armature has a rig script at all. Even the rig script seems plausible until you notice the obfuscated code with arbitrary variable names trying to masquerade as some kind of transform constraint system.
Fun stuff!
TLDR: Don’t click things you don’t trust.
- Virus from a spam email from a sketchy BlenderMarket user 1
- created Apr 2025
- last reply May 2025
- 16 replies
- 9.0k views
- 11 users
- 52 likes
- 3 links
- 3 3 2
Long discussion happening on this…
Thanks for the very useful reminder, Greg. I’ve also posted this warning on Mastodon…
looks like a MS windows issue we ( linux os’s ) do not have that folder layout
Windows is the most used OS in the world for pc’s (apx 70%), this makes it the biggest target.
There are other reasons (OS security handling, etc) but I think that is the main one.
I had the same problem. I hope, I’ve found all related files for this issue. There were several places they were placed. One is the Windows autostart folder. There is a link that starts an exe file that was downloaded before. It will be executed at every system restart. After deleting all files and restarting the system, everything seems to be OK. I didn’t found the entry in the autostart folder again. I hope the tool did not download any other software I haven’t realized yet…
Best regards
I am no security expert, but I wouldn’t trust anymore a Windows install that has run that script. You never know if something somewhere is there, waiting to encrypt your files and blackmail you or enroll your machine in a botnet…
Yeah, I’d be formatting that drive and doing a complete reinstall just in case.
“Ignore” is a terrible choice of wording on that dialogue. It sounds a lot like “ignore the warning and execute anyway”.
Has anyone checked if anti-viruses detect this python script?
Totally agree, it should be “Do not execute” (which I hope is what it does).

## ADVERTISEMENT

Unfortunately, that’s not an option… but I let Windows Defender scan my system. Everything seems okay so far. The downloaded ransomware (?) files are gone too.
Fingers crossed that was it…
After Windows Defender deep scanned my harddrives the whole night, the result was positive. No ransomware, nor viruses or trojans… Hope this was it now.
Not only don’t click links you don’t trust, but don’t download zips and torrent files you don’t trust! Run them through a scanner first since the computer can’t detect malware when either zipped or torrented
I didn’t realize blender creators were being targeted for this as well, seemed really hard to tell the difference between legit and scam until diving into the pyscript
I can’t believe how difficult it was to see it was a scam, gotta be running everything in a Virtual Machine these days!
Linux is a great alt then, especially since blender runs 2x the speed in it. I use Arch w/ VM’s and have faster speeds as well as my PC not overheating (like in windows)
This is a website for humans and human creation, don’t write the majority of a post with AI
Hi,
Thanks for the information. I started using Blender just last year, and it never occurred to me that .blend files could potentially contain malware. So, I asked ChatGPT for advice on how to prevent , detect , and correct such threats. Here’s the list of recommended actions and I also included links that I found on websites:
Preventive - Stop malware before it happens
- Use trusted sources - Only download .blend files and add-ons from reputable sites (Blender Market, Gumroad, official GitHub). Sample case: https://www.reddit.com/r/blender/comments/twp17u/did_i_just_download_a_virus/ 5
- Disable auto-run scripts - Go to Edit > Preferences > Save & Load > Auto Run Python Scripts and disable this option.
- Scan with antivirus - Use antivirus software to scan files before opening them in Blender.
- Keep Blender updated - Regular updates fix known vulnerabilities -”always use the latest official release.
- Educate users/team - Train users to avoid opening unknown or pirated .blend files or suspicious email links. Sample case: Blend files can execute malware
- Use sandbox for testing - Open unfamiliar .blend files in a virtual machine or isolated system.
- Regular file backups - Schedule automatic backups to avoid data loss in case of infection.
Detective - 	Identify malware if it appears
- Monitor abnormal behavior - Watch for lag, CPU spikes, or strange system/network activity after opening a file.
- Inspect embedded scripts - Open Blender’s Text Editor to check for hidden or unexpected Python scripts.
- Use file monitoring tools - Tools like FolderChangesView can detect if a .blend file triggers background file changes.
- Check file hashes - Compare SHA256/MD5 checksums of original and new .blend files to detect tampering.
Corrective - Fix damage after malware is detected
- Quarantine/remove infected files - Immediately isolate suspicious files from shared folders or devices.
- Scan and clean system - Run a full malware scan using Windows Defender, Malwarebytes, or another tool.
- Reinstall Blender - If needed, uninstall and reinstall Blender from the official website.
- Restore from backup - Recover clean project files from your recent backup.
- Notify the source/platform - Report the malicious file to the hosting site or author to prevent wider damage.
If anyone here has an IT background, please feel free to share your knowledge or correct me if I’ve made any mistakes.
Have tried that. And every time I open my own, self-created file with a rigify rig, the popup warns me about security risks.
It gets old…

### New & Unread Topics

### Want to read more? Browse other topics in Latest News or view latest topics .


--------------------