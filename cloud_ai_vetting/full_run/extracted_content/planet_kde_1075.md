# Planet KDE
**URL:** https://planet.kde.org
**Page Title:** English - Planet KDE
--------------------


## Welcome to Planet KDE

### Sunday, 25 January 2026

### Bouncy Ball will always bounce back 🔗

### Saturday, 24 January 2026

### This Week in Plasma: fixing all the things 🔗

Welcome to a new issue of This Week in Plasma!
This week the Plasma team focused almost entirely on bug fixing. And let’s let the results speak for themselves: we fixed 18 high and very high priority Plasma bugs, or 28% of all open ones! Lots of polishing for Plasma 6.6 to make it a great release.

## Notable New Features

### Plasma 6.7.0

Added a dedicated setup UI for configuring shared printers on Windows networks. (Mike Noe, KDE Bugzilla #406211 )

## Notable UI Improvements

### Plasma 6.6.0

Desktop switching and Present Windows shortcuts now use the Meta key by default for more consistent system-wide behavior. (Antti Savolainen, kwin MR #8597 )
Plasma can now report printers’ waste receptacle levels and notify users when they fill up. (Mike Noe, KDE Bugzilla #514525 )
KRunner’s buttons have been reorganized to be consistent with other Plasma widgets, making the interface feel more familiar and coherent. (Taras Oleksyn, plasma-workspace MR #6203 )

### Plasma 6.7.0

System Settings’ Wi-Fi & Networking page now uses clearer Wi-Fi security labels, correctly showing WPA2 and WPA3 support for both Personal and Enterprise networks. (Lynne Megido, KDE Bugzilla #493238 )
There are now keyboard shortcuts for switching virtual desktops and opening the Present Windows effect that use the Meta key, to be consistent with other globally-scoped keyboard shortcuts. (Antti Savolainen, KDE Bugzilla #508187 )

## Frameworks 6.23

Improved the visual fidelity of thumbnail images in open/save dialogs throughout Plasma and KDE apps. (Méven Car, KDE Bugzilla #489298 )

## Notable Bug Fixes

### Plasma 6.5.6

Fixed an issue that could sometimes make KWin crash after periods of idleness. (Vlad Zahorodnii, KDE Bugzilla #513687 )
Fixed an issue that would make Plasma crash when you disabled widgets in the System Tray and clicked the dialog window’s “OK” button rather than the “Apply” button. (David Edmundson, KDE Bugzilla #478625 )
Fixed an issue that could sometimes make KWin crash after repeatedly pressing the “Activate window demanding attention” shortcut ( Meta + Ctrl + A by default) while multiple windows were demanding attention. (Vlad Zahorodnii, KDE Bugzilla #500748 )
Fixed a common case where Plasma could crash after certain games crashed first. (David Edmundson, KDE Bugzilla #506562 )
Fixed a common case where Plasma could crash when configured with a weather station from the Environment Canada source in its Weather Report widget. (Bohdan Onofriichuk, KDE Bugzilla #514553 )
Fixed a case where changing the visibility of the Media Player widget in the System Tray while music was playing could make Plasma crash. (David Edmundson, KDE Bugzilla #514823 )
Spectacle once again remembers the location where you last saved a screenshot the next time you save one. (Noah Davis, KDE Bugzilla #511649 )
Fixed an issue causing 24” 16:9 aspect ratio monitors to get the wrong default resolution. (Anton Golubev, kwin MR #8681 )

### Plasma 6.6.0

Fixed a surprisingly common issue whereby KWin could sometimes crash when you frantically wiggled the pointer to try to stop a monitor from going to sleep. (Vlad Zahorodnii, KDE Bugzilla #487660 )
Fixed a case where KWin could crash when you deleted a virtual desktop that still had windows on it. (Vlad Zahorodnii, kwin MR #8680 )
Fixed another KWin crash, this one more random. (Xaver Hugl, kwin MR #8677 )
Fixed a long-standing issue whereby tooltips opened by buttons in Plasma widget popups could move onto the panel and get stuck there after you closed the widget popups. (Marco Martin, KDE Bugzilla #475646 )
Fixed an issue that made popups of panel widgets undesirably change their size when you moved their panel to an adjacent screen edge. (Christoph Wolk, KDE Bugzilla #512273 )
Fixed an issue making certain sub-menus of Plasma widgets not have transparent backgrounds, which was especially visible with menu blurring turned on. (Marco Martin, KDE Bugzilla #513307 )
Fixed an issue in the HDR calibrator tool that made long pieces of text overflow from their boxes. (Nate Graham and David Edmundson, KDE Bugzilla #514687 )
Fixed an issue that made Plasma forget the IPSec certificate passwords of L2TP VPNs. (Mickaël Thomas, plasma-nm MR #460 )
Fixed an issue causing apps launched using D-Bus activation to be omitted from System Monitor’s Applications table. (Arjen Hiemstra, KDE Bugzilla #510235 )
Fixed an issue in System Monitor that could make the Applications table’s “Details” panel un-scrollable under certain circumstances. (Arjen Hiemstra, KDE Bugzilla #506150 )
Fixed an issue in Discover that could sometimes make Flatpak apps’ languages packages fail to get grouped with the apps. (Harald Sitter, KDE Bugzilla #513111 )

### Plasma 6.7.0

Fixed an issue that broke KRunner’s Activities plugin from actually finding any activities. (Sam Morris, KDE Bugzilla #514000 )
Fixed an issue that caused long boot menu entries to be cut off in the Breeze GRUB Menu styling. (Sébastien Bouchard, KDE Bugzilla #513107 )

### Frameworks 6.23

Fixed an issue that caused a large variety of crashes in Plasma and KDE apps related to devices appearing and disappearing. (Nicolas Fella, solid MR #232 )
Fixed an issue making KWallet crash on OpenSUSE-based operating systems. (Nicolas Fella, KDE Bugzilla #490788 )
Fixed an issue that broke the back button in Kirigami-based System Settings pages and apps when using a right-to-left language like Arabic or Hebrew and you went back and forward and then back again. (Youssef Al-Bor3y, KDE Bugzilla #511295 )

## Notable in Performance & Technical

### Plasma 6.6.0

Plasma’s system monitoring infrastructure received further fixes to improve OpenBSD support. (Rafael Sadowski, libksysguard MR #454 )

### PackageKit 1.3.4

Implemented support for DNF5 in PackageKit, which fixes a huge number of issues relevant to people using Discover on Fedora-based operating systems. (Neal Gompa, packagekit PR #931 )
[LINK: packagekit PR #931](https://github.com/PackageKit/PackageKit/pull/931)

## How You Can Help

“This Week in Plasma” still needs your help! Publishing these posts is time-consuming and needs community assistance to be sustainable. Right now there are two ways to help:
- Help put together the posts using the current mostly manual process
- Help automate the process
Work can be coordinated in the relevant Matrix room .
Beyond that, you can help KDE by directly getting involved in any other projects. Donating time is actually more impactful than donating money. Each contributor makes a huge difference in KDE — you are not a number or a cog in a machine! You don’t have to be a programmer, either; many other opportunities exist.
You can also help out by making a donation! This helps cover operational costs, salaries, travel expenses for contributors, and in general just keep KDE bringing Free Software to the world.

## To get a new Plasma feature or a bugfix mentioned here

Push a commit to the relevant merge request on invent.kde.org .

### Friday, 23 January 2026

### In praise of memory-leak-detection 🔗

Nicolas Fella wrote a bit about enabling memory leak detection in KDE CI ,
and I thought I’d add some comments from a different software engineering environment (e.g. my work-work).

### Guidelines for Memory Management

At work-work, we have a slightly peculiar software environment:
- Bleeding edge C++ use – C++23 if possible, 26 features being experimented-with – and a strong reliance on C++
language and library features. Use C++ containers, std::string (with an *implicit “here be UTF-8-encoded
strings”), std::jthread , business-logic in standard C++ wherever possible.
- Qt 5.6.3, from 2017, for UI code. That’s pre-C++17.
This leads to two guidelines about memory-management in our application:
- Use Qt’s memory model and ownership only for QWidget ’s inheritance tree,
- .. well, ok, incidentally for things inheriting from QObject .
- Use C++ resource management for all other memory-management.
This does mean that depending on where in the codebase you’re working,
you either have to be a “C++ purist” (as Nico puts it)
or a “Qt pragmatist” (as I’ll phrase it).
Note that the guideline is not “use smart pointers”, because that last guideline can
deconstructed a little (it wouldn’t surprise me if this was inspired by Klaus Iglberger):
- If a class manages a resource, then that resource-management should be the only thing it does,
- If an object needs resources, then those resources should be members (sub-objects) of a class as above.
Often that means that memory-management is in the hands of std::unique_ptr , but std::vector does the job also. We have a handful of other classes for resource-management
as well, like a wrapper for FILE * for those places where we need to interact with
C’s stdio library. Granted, FILE * is probably not a source of memory-leaks, but
it is a managed resource, and forgetting one will lead to leaking file-descriptors in the long run.

### Leaky Libraries

Dealing with memory leaks can be difficult particularly when they happen in
libraries not under your control. As an example, I wrote this program (
headers elided for brevity) which is a Qt5 program:
This is, like, the simplest Qt5 program. It sits there for five seconds and then quits.
It also leaks 1662 bytes of memory, in 19 allocations, according to my ASAN output.
They leak from allocations done in libQt5Core . Adding a QLabel and displaying some
text adds leaks in libfontconfig , and the leaks keep accumulating as more libraries enter the mix.
Granted, none of these leaks are large. I’m not even sure that they are impolite,
but they’re there and it makes tracking down leaks in my code harder, because
there’s some baseline of leakage that I need to ignore. Filtering out the
noise becomes a serious undertaking.

### Takeaway

Chasing all the memory-leaks is hard. Chasing any leaks in KDE Frameworks is something
I can only applaud.

### Detecting Memory Leaks in KDE CI 🔗

Leaking memory is impolite. It’s messy, it can suggest logic bugs, and thanks to AI grifters RAM is expensive.
Unfortunately C++ makes it rather easy to leak memory. Fortunately we have tools to find such leaks. One such tool is Leak Sanitizer (LSAN) from the Address Sanitizer (ASAN) family. It’s using compiler-based instrumentation for the code to reports any leaks after the program terminates.
[LINK: Leak Sanitizer](https://clang.llvm.org/docs/LeakSanitizer.html)
KDE’s CI infrastructed has ASAN enabled for a while. However the leak sanitizer part was explicitly disabled, so no leaks were reported as part of the CI build and test run. This is because a number of projects have pre-exisiting memory leaks that would cause the C build to fail. Of course those should be fixed eventually, but in order to do that we need to know where they are. Also, for projects that currently don’t have any leaks we want to enforce keeping it that way.
A few lines of Python later KDE’s CI system now allows to enable LSAN on a per-project basis. The .kde-ci.yml file that governs CI builds in KDE gained a new option enable-lsan . It is off by default for now for compatibility, but we may consider enabling it by default eventually.
If enabled and any memory leak in a test is detected, that test and therefore the whole CI pipeline will fail.
Now once we found a leak, what can we do about it? There’s several options:
- Use good old delete/free(). Works, but is often rather error-prone.
- Use QObject’s parent mechanism. Works, but often frowned upon by C++ purists. Mostly makes sense for widget hierarchies.
- Smart pointers like std::unique_ptr/std::shared_ptr. These are great because they allow to express the ownership on an API level and make ownership transfers explicit. Often the best choice for business logic code.
LSAN is now enabled for some Frameworks CI builds, but ideally it would be enabled for all KDE projects. And of course any leaks found along the way should be fixed.
Happy leak-fixing!

### Web Review, Week 2026-04 🔗

Let’s go for my web review for the week 2026-04.
Tags: tech, europe, politics, foss
Need inspiration for your answer to the European Commission call for evidence on open source? This is a good one.
https://www.more-magic.net/posts/open-source-in-the-eu.html
Tags: tech, web, self-hosting, blog, writing
Get out and write indeed. You can fiddle with the tools later.
https://susam.net/writing-first-tooling-second.html
Tags: tech, social-media, attention-economy, fediverse
There was indeed another path for social media… Let’s hope the Fediverse stay on its current course.
https://susam.net/attention-media-is-not-social-media.html
Tags: tech, social-media, fake-news, attention-economy
Or why the focus on fact checking is doomed to fail. You can’t ignore our biases, the social context, and above all the toxic architecture of the big social medias.
https://theconversation.com/why-people-believe-misinformation-even-when-theyre-told-the-facts-271236
Tags: tech, reading, social-media
Not all reading is born equal. The intent matters quite a lot. Build the skill, it’ll last a life time.
https://theconversation.com/deep-reading-can-boost-your-critical-thinking-and-help-you-resist-misinformation-heres-how-to-build-the-skill-268082
Tags: tech, university, teaching, ai, machine-learning, gpt, ethics, foss
Interesting ideas on how to approach teaching at the university. It gives a few clue on how to deal with chatbots during exams, can be improved but definitely a good start.
https://ploum.net/2026-01-19-exam-with-chatbots.html
Tags: tech, programming, business, leadership, complexity, history
Good historical perspective about the attempts to get rid of developers. This never unfold as envisioned. This is mostly about the intellectual work to build artifacts handling the world complexity, and this doesn’t go away.
https://www.caimito.net/en/blog/2025/12/07/the-recurring-dream-of-replacing-developers.html
[LINK: https://www.caimito.net/en/blog/2025/12/07/the-recurring-dream-of-replacing-developers.html](https://www.caimito.net/en/blog/2025/12/07/the-recurring-dream-of-replacing-developers.html)
Tags: tech, packaging, supply-chain, security
New packaging ecosystems bring their new attack vectors. This is definitely a teething problem which will need to be addressed soon.
https://blog.popey.com/2026/01/malware-purveyors-taking-over-published-snap-email-domains/
Tags: tech, security, ide
Are you sure you want to trust that random project you got provided with? Really?
https://runjak.codes/posts/2026-01-21-adversarial-coding-test/
Tags: tech, ai, machine-learning, speech
Sounds like a very interesting model (pun intended). It’s really nice to pack that much performance in a smaller neural network.
https://kyutai.org/blog/2026-01-13-pocket-tts
Tags: tech, self-hosting, infrastructure
Nice ideas for setting up your own infrastructure at home.
https://linderud.dev/blog/personal-infrastructure-setup-2026/
Tags: tech, databases, postgresql, optimization, performance
When everything obvious fails… there are still optimisation tricks available for your databases.
https://hakibenita.com/postgresql-unconventional-optimizations
Tags: tech, data-science, databases, pandas, duckdb
I definitely would like to have some time to fiddle with DuckDB more. It looks like a really neat alternative to something like pandas.
https://www.robinlinacre.com/recommend_duckdb/
Tags: tech, c++, memory, type-systems
Nice introduction of the C++ ownership system. Nothing new under the sun obviously but since I still encounter developers struggling with this, such introductory material is nice to have handy for sharing.
https://blog.aiono.dev/posts/understanding-c++-ownership-system.html
Tags: tech, rust, culture
This is indeed an important cultural trait in the Rust community. This can bring challenge when integrating Rust code into a context with more ambiguity.
https://www.alilleybrinker.com/mini/rusts-culture-of-semantic-precision/
Tags: tech, architecture, c4, tools
Still young and pretty much a one man show. This could turn into a nice tool to use C4 more productively.
https://likec4.dev/#features
Tags: tech, team, organisation
This is good advice. Going for something extremely small first is a good way to on board in a new project.
https://ankursethi.com/blog/smallest-possible-change/
Tags: tech, tech-lead, leadership, management, product-management, engineering
This is a good overview of what the Staff Engineer can be. There’s of course a lot of variation depending on time, priorities and the culture of the organisation.
https://medium.com/@_davidanderson/a-year-in-the-life-of-a-staff-engineer-84ae9f6963c1
Tags: tech, work, team, culture, leadership
Feels a bit odd to go to such length to put it in numbers. And yet, it’s clear that friendships in the workplace are a must. They should be fostered rather than stifled.
https://www.makeworkbetter.info/p/work-friends-are-the-secret-to-great
Tags: history
Fascinating story. Some people shouldn’t be forgotten.
https://www.youtube.com/watch?v=y2lkVlB96y4
Bye for now!

### Thursday, 22 January 2026

### Tellico 4.1.5 Released 🔗

Tellico 4.1.5 is available , with a couple of updates. This will be the last release that retains compatibility with Qt5.

### Improvements

- Fixed Arxiv ID search to return correct results.
- Updated the Data Crow importer for its new XML format .
- Updated the IGDB source.
- Corrected XML usage for arch with unsigned char, like ARM.
I’ll have the next release out soon, v4.2, with several more updates, and requiring Qt6.

### Wednesday, 21 January 2026

### Pathways to open-source (and from it): one flawed journey exposed 🔗

### Season Of KDE 2026 Projects 🔗

Every year the KDE Community actively helps people to become active community members and
contributors to Free Software through our Season of KDE mentorship programs.
We would like to warmly welcome this year's mentees Aviral Singh, Keshav Nanda, Vishesh
Srivastava, Varun Sajith Dass, Aditya Sarna, Jaimukund Bhan,
Navya Sai Sadu, Kumud Sagar, Arun Rawat, Tanish Kumar, Ajay Singh, Mohit Mishra,
Rohith Vinod, Shivang K Raghuvanshi, Onat Ribar, Hrishikesh Gohain, Aryan Rai,
Advaith SK, CJ Nguyen, Siddharth Chopra, Nitin Pandey, Pavan Kumar S G,
Sayandeep Dutta, Sairam Bisoyi, and J Shiva Shankar. They will be working on 21
projects covering a wide range of apps, frameworks, utilities and software in general to
improve KDE.

## Sok 2026 Projects

## Standardise translation reference paths across all KDE projects

Translators work on PO files that contain the translation data, including the file path to
the file that the specific translation comes from. To understand the purpose of a particular
string, sometimes the translators need to view the translatable strings in the code itself. To
allow KDE to build tooling around the paths, the PO files must be standardised so that all
contain file path references relative to the project root rather than from an arbitrary directory.
This work has been started already but will be finished during this SOK project. Aviral Singh and Keshav Nanda will work under the guidance of Finley Watson on edge cases, testing and
cleaning up the merge requests ready for merging. They will also improve the test script.

## Lokalize tasks

All Lokalize projects will be mentored by Finley Watson.

### Introduce Appium testing

Vishesh Srivastava will be integrating Appium testing in Lokalize. Appium is already used by other KDE software,
and could be very helpful for testing UI changes, including keyboard shortcuts. This task will
include coordinating with other mentees as they modify parts of the UI, as well as writing other
general tests.

### Improving logic consistency and MacOS platform stability

Varun Sajith Dass will work on fixing reported bugs, and improving
string processing in many parts of Lokalize. Varun's aim is to increase the robustness of Lokalize's
existing features, improve the quality of the output, and make following the Human Interface
Guidelines easier for translators. This work will require coordination with other mentees e.g. for
writing tests. Varun also aims to make it possible to build Lokalize on MacOS by fixing bugs related
to this.

### Fix the glossary

The glossary tab in Lokalize is unintuitive and hard to use, and currently crashes Lokalize unless
you manually add the file that saves the glossary data to disk. Aditya
Sarna and Jaimukund Bhan will update the UI so that it is easier to use, improve the glossary's behaviour, fix bugs and
better follow the Human Interface Guidelines. They will work with the translators and visual
designers to ensure their work follow KDE best practices and creates meaningful improvements.

### Jump to next translation unit when sort filters are applied

The editor tab contains a dock widget called "Translation Units" which has the ability to filter and
sort entries in translation files with the search bar. Moving between entries while approving them
by using the shortcut jumps about in the list, rather than working down the sorted list correctly,
one after another. Navya Sai Sadu and Kumud
Sagar will be working together to fix this so the keyboard shortcut
behaves as expected.

### Redesign translation memory tab

The translation memory tab allows you to pick a TM (saved translation pairs from previous
translation jobs / files) to search through, and shows the results in the list below. Arun
Rawat will be redesigning the UI to enable searching multiple
memories at once, with these settings saved per-project. Additionally, the Translation memories
manager will be merged into the tab instead of existing separately e.g. by moving TM-specific
entries into the right-click menu, and adding more general buttons into the TM tab page, or the
toolbar that is specific to the TM tab.

### Standardise menubar

Lokalize uses a KDE framework, KXMLGUI, to manage its menubar and status bar. In Lokalize, KXMLGUI
allows you to define the contents of the menubar for each tab. Right now the tabs have different
ordering of menus with some menus missing in certain tabs.
Tanish Kumar will re-design the menubar so all tabs to offer
the same menubar. Where a tab does not use a menu, the menu will be added, with menu options
disabled.
All Lokalize projects will be mentored by Finley Watson.

## Investigate alternatives to dblatex to convert docbook to pdf

KDE’s documentation build pipeline currently relies on a legacy, copy-pasted fork of
dblatex embedded inside the docs-kde-org repository. While functional, this setup
obscures Git history, complicates upgrades, and makes KDE-specific customizations such as kdestyle difficult to understand and maintain.
Ajay Singh , under Johnny Jazeix guidance, will investigate the
possibility of using other tools than dblatex (such as pandoc)
to create the pdf from docbook. The aim is to see if it fixes the
current issues we have with non-supported non-ascii languages.
And if there is a working alternative, he will work on trying to have
a similar style to what we currently have in the kdestyle.

## Extract dblatex fork from docs-kde-org repo and improve non ascii languages support

we are currently reworking the documentation website .
The first task was to generate the documentation of each repo in a specific job .
[LINK: reworking the documentation website](https://invent.kde.org/websites/docs-kde-org/-/issues/2)
Mohit Mishra will work on extracting the dblatex from the code into its own repo (keeping
the history) and finding out if we can directly clone the original repository instead of having a fork.
Mentored by Johnny Jazeix, the overall goal is to try to use the upstream dblatex (shipped in
distributions) to generate the pdf, experiment with XeTeX PDF generation engine instead of pdfTeX
to create PDF for non supported non-ascii languages (Arabic, Chinese, Japanese, Korean...). If we
can't improve it, extract dblatex fork on a specific repo to ease the maintenance`

## Implement font subsetting when saving files in Okular

Okular supports PDF annotations and form-filling. When a user adds text to a document,
Okular must ensure that the text remains readable on any system irrespective of whether the
font is installed locally or not. Hence the font data is directly embedded into the
document using the PDF rendering library Poppler.
The problem arises due to the lack of proper font subsetting (as Poppler does not support this).
Modern OpenType and TrueType fonts contain thousands of glyphs for various languages and symbols.
Okular approaches this by embedding the entire font file into the document. This causes an
undesirably large file size due to all the extra unused glyphs/symbols being embedded.
Rohith Vinod and Shivang K. Raghuvanshi , under Albert Astals' supervision, will work on
solving this problem using the hb-subset-input-glyph-set API.

## Plasma Setup: mobile support

Plasma Setup is KDE's first run setup wizard, providing a friendly way to create the first user
account and configure basic system settings. Unfortunately it only works on desktop form factors
Under Kristen McWilliam's guidance, Onat Ribar will work on supporting Plasma Setup for Plasma Mobile as well.

## KEcoLab

Recent updates in the lab mean that X11-based emulation tools like xdotool are obsolete. Guided by
Joseph P. De Veaugh-Geiss, Karanjot Singh , and Aakarsh MJ , Hrishikesh Gohain will be tasked with porting existing scripts to a
Wayland-based tool. Once Wayland support is ready, Hrishikesh will prepare test scripts to measure
the KDE Plasma Desktop Environment itself.

## Turning mentorship.kde.org into a proper onboarding platform

mentorship.kde.org currently looks like a website, but does not behave like an onboarding system. Aryan Rai and Advaith SK will be required to convert the site into a guided entry point for
KDE mentorship.
Anish Tak and Paul Brown will be guiding Aryan and Advaith throughout the project.

## Automate Promo data collection

Promo collects data from different sources that measure how our followship grows,
how many outlets are talking about us, what is our level engagement, etc. This
information is currently collected by hand and is a massive time drain. CJ Nguyen ,
mentored by Paul Brown, will create systems to automate the collection, storage
and analysis of this data.

## Markdown and plain text editors for Marknote

Siddharth Chopra will be adding two editors to MarkNote , an app that lets you create
rich text notes and easily organise them into notebooks. The first editor is a raw
markdown editor for .md files and a plain text editor for .txt files.
Siddharth also plans to work on making some improvements to the current markdown editor.
Carl Schwan will be Siddharth's mentor in this project.

## Making Cantor’s existing tests visible, reproducible, and actionable in CI

In this project, Avyakt Jain aims to activate Cantor ’s existing testing infrastructure in a low-risk,
incremental, maintainer-friendly way by (1) producing a clear, factual overview of
current test coverage and gaps, (2) enabling a minimal, MR-scoped CI test job that
provides visible JUnit-based feedback, and (3) improving reproducibility and documentation
for running tests locally. The expected outcome is faster, more reliable feedback for
maintainers and contributors, without enforcing new quality gates or changing Cantor’s
runtime behavior.
Alexander Semke and Stefan Gerlach will be supervising Avyakt's work.

## Call log synchronization and backup in KDE Connect

Nitin Pandey will be working on improving telephony
integration in KDE Connect by implementing call log synchronization and backup from
Android devices to the desktop. Instead of creating a separate desktop client for call
history, the project will integrate call logs directly into the existing KDE Connect
SMS client on the desktop, providing a unified communication view.
Albert Vaca will be mentoring this project.

## Enhancement of KDE Mancala: Engine Parallelization and Digital Asset Creation

Pavan Kumar S G will speed up MankalaEngine by enabling it to use threads, Pavan Kumar SG will also create artwork to be used in the Mankala NextGen GUI .
This project will receive guidance from Benson Muite and Srisharan VS.

## Improve Mankala GUI and add translations for Game variants

Sayandeep Dutta will improve the visual appeal of Mankala NextGen GUI and contribute towards it going through KDE Review. In addition, Tamil translations will be created for MankalaEngine and Mankala NextGen.
Srisharan VS and Benson Muite will support this project.

## XMPP Support in Falkon through WebXDC

Sairam Bisoyi will create a Falkon extension to allow it to be used for chat using the XMPP protocol and its WebXDC extension..
The project advisors are Schimon Jehudah, Juraj Oravec and Benson Muite.

## Adding Vamana Guntalu to Mankala Engine and a WebXDC bookmarking system in Falkon

J Shiva Shankar will add the Vamana Guntalu mancala game to MankalaEngine . J Shiva Shankar will also create a Falkon extension to allow synchronization of website bookmarks across different devices using the XMPP protocol in a WebXDC application.
The project advisors are Schimon Jehudah, Juraj Oravec and Benson Muite.

## Stay in the loop!

You will be able to follow the progress of all mentees through their blog posts on KDE's planet , and by joining the relevant project
communication channels.

### Tuesday, 20 January 2026

### Returning Home and Evolving As Consultant in 2026 🔗

### Skrooge 26.1.20 released 🔗

### Changelog

- Correction bug 512770: some accounts doubled in "amount" vs "today amount"
- Correction bug 513589: QIF import errors
- Correction bug 513016: skrooge-boursorama.py don't work
- Correction bug 514649: Performance issue
- Correction bug 514649: "Open transaction with..." and some other are empty

--------------------