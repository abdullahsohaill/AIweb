# https://www.openwall.com/john/
**URL:** https://www.openwall.com/john
**Page Title:** John the Ripper password cracker
--------------------

- Products Openwall GNU/*/Linux server OS Linux Kernel Runtime Guard John the Ripper password cracker Free & Open Source for any platform in the cloud Pro for Linux Pro for macOS Wordlists for password cracking passwdqc policy enforcement Free & Open Source for Unix Pro for Windows (Active Directory) yescrypt KDF & password hashing yespower Proof-of-Work (PoW) crypt_blowfish password hashing phpass ditto in PHP tcb better password shadowing Pluggable Authentication Modules scanlogd port scan detector popa3d tiny POP3 daemon blists web interface to mailing lists msulogin single user mode login php_mt_seed mt_rand() cracker
- Openwall GNU/*/Linux server OS
- Linux Kernel Runtime Guard
- John the Ripper password cracker Free & Open Source for any platform in the cloud Pro for Linux Pro for macOS
- Free & Open Source for any platform
- in the cloud
- Pro for Linux
- Pro for macOS
- Wordlists for password cracking
- passwdqc policy enforcement Free & Open Source for Unix Pro for Windows (Active Directory)
- Free & Open Source for Unix
- Pro for Windows (Active Directory)
- yescrypt KDF & password hashing
- yespower Proof-of-Work (PoW)
- crypt_blowfish password hashing
- phpass ditto in PHP
- tcb better password shadowing
- Pluggable Authentication Modules
- scanlogd port scan detector
- popa3d tiny POP3 daemon
- blists web interface to mailing lists
- msulogin single user mode login
- php_mt_seed mt_rand() cracker
- Services
- Publications Articles Presentations
- Articles
- Presentations
- Resources Mailing lists Community wiki Source code repositories (GitHub) File archive & mirrors How to verify digital signatures OVE IDs
- Mailing lists
- Community wiki
- Source code repositories (GitHub)
[LINK: Source code repositories (GitHub)](https://github.com/openwall)
- File archive & mirrors
- How to verify digital signatures
- OVE IDs
- What's new

## John the Ripper password cracker

John the Ripper is an Open Source password security auditing and password recovery tool available for many operating systems. John the Ripper jumbo supports hundreds of hash and cipher types, including for: user passwords of Unix flavors
(Linux, *BSD, Solaris, AIX, QNX, etc.), macOS, Windows, "web apps" (e.g., WordPress), groupware (e.g., Notes/Domino), and
database servers (SQL, LDAP, etc.);
network traffic captures (Windows network authentication, WiFi WPA-PSK, etc.);
encrypted private keys (SSH, GnuPG, cryptocurrency wallets, etc.),
filesystems and disks (macOS .dmg files and "sparse bundles", Windows BitLocker, etc.),
archives (ZIP, RAR, 7z), and document files (PDF, Microsoft Office's, etc.)
These are just some of the examples - there are many more.
John the Ripper is free and Open Source software,
distributed primarily in source code form.
If you would rather use a commercial product, please consider John the Ripper Pro ,
which is distributed primarily in the form of "native" packages
for the target operating systems and in general is meant to be easier to
install and use while delivering optimal performance.
- John the Ripper Pro for Linux
- John the Ripper Pro for macOS
- On Windows, consider Hash Suite (developed by a contributor to John the Ripper)
- On Android, consider Hash Suite Droid
Download the latest John the Ripper jumbo release
( release notes ) or development snapshot:
- 1.9.0-jumbo-1 sources in tar.xz, 33 MB ( signature ) or tar.gz, 43 MB ( signature )
- 1.9.0-jumbo-1 64-bit Windows binaries in 7z, 22 MB ( signature ) or zip, 63 MB ( signature )
- 1.9.0-jumbo-1 32-bit Windows binaries in 7z, 21 MB ( signature ) or zip, 61 MB ( signature )
- Development source code in GitHub repository (download as tar.gz or zip )
[LINK: GitHub repository](https://github.com/openwall/john)
[LINK: tar.gz](https://github.com/openwall/john/archive/bleeding-jumbo.tar.gz)
[LINK: zip](https://github.com/openwall/john/archive/bleeding-jumbo.zip)
Run John the Ripper jumbo in the cloud (AWS):
- John the Ripper in the cloud homepage
Download the latest John the Ripper core release
( release notes ):
- 1.9.0 core sources in tar.xz, 8.6 MB ( signature ) or tar.gz, 13 MB ( signature )
- Development source code in GitHub repository
[LINK: GitHub repository](https://github.com/openwall/john-core)
Get John the Ripper apparel at 0-Day Clothing and support the project
These and older versions of John the Ripper, patches, unofficial builds, and many other related files are also available from the Openwall file archive .
You can browse the documentation for John the Ripper core online , including a summary of changes between core versions .
Also relevant is our presentation on the evolution of password cracking .
There's a collection of wordlists for use with John the Ripper.
It includes lists of common passwords, wordlists for 20+ human languages, and files with the common passwords and
unique words for all the languages combined, also with mangling rules applied and any duplicates purged.
yescrypt and crypt_blowfish are implementations of yescrypt, scrypt, and bcrypt - some of the strong password hashes also found in John the Ripper -
released separately for defensive use in your software or on your servers.
passwdqc is a proactive password/passphrase strength checking and policy enforcement toolset,
which can prevent your users from choosing passwords that would be easily cracked with programs like John the Ripper.
We can help you integrate modern password hashing with yescrypt or crypt_blowfish ,
and/or proactive password strength checking with passwdqc ,
into your OS installs, software, or online services.
Please check out our services .
There's a mailing list where you can share your experience with John the Ripper and ask questions. Please be sure to specify an informative message subject whenever
you post to the list
(that is, something better than "question" or "problem").
To subscribe, enter your e-mail address below or send an empty message to <john-users-subscribe at lists.openwall.com> .
You will be required to confirm your subscription by "replying"
to the automated confirmation request that will be sent to you.
You will be able to unsubscribe at any time and we will not use your e-mail
address for any other purpose or share it with a third party.
However, if you post to the list, other subscribers and those
viewing the archives may see your address(es) as specified on your message. The list archive is available locally and via MARC .
Additionally, there's a list of selected most useful and currently relevant postings on the community wiki .
Contributed resources for John the Ripper:
- Community wiki with custom builds , benchmarks , and more
- Custom builds for Windows (up to 1.8.0.13-jumbo)
- Custom builds for macOS (up to 1.8.0.9-jumbo)
- Custom builds for Solaris (packages up to 1.7.6, non-packaged up to 1.7.8-jumbo-7)
- Custom builds for Android (up to 1.8.0)
- Ubuntu snap package ( documentation , announcement )
[LINK: documentation](https://github.com/openwall/john-packages#snap)
- OpenVMS and SYSUAF.DAT support ( signature )
by Jean-loup Gailly OpenVMS executables for Alpha and VAX ( signature )
- Local copies of the above files by Jean-loup Gailly and a much newer implementation by David Jones
Local copies of these and many other related packages are also available from the Openwall file archive .
John the Ripper is part of Owl ,
Debian GNU/Linux, Fedora Linux, Gentoo Linux, Mandriva Linux, SUSE Linux,
and a number of other Linux distributions.
It is in the ports/packages collections of FreeBSD, NetBSD, and OpenBSD.
John the Ripper is a registered project with Open Hub and it is listed at SecTools .
56104366

--------------------