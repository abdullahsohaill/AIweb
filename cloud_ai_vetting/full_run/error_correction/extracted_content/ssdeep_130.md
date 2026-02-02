# ssdeep
**URL:** https://ssdeep-project.github.io/ssdeep/index.html
**Page Title:** ssdeep - Fuzzy hashing program
--------------------


## Introduction

ssdeep is a program for computing context triggered piecewise hashes (CTPH).
Also called fuzzy hashes, CTPH can match inputs that have homologies.
Such inputs have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both content and length.
A complete explanation of CTPH can be found in Identifying almost identical files using context triggered piecewise hashing from the journal Digital Investigation.
There is a free version of this paper available through the Digital Forensic Research Workshop conference, free version of Identifying almost identical files using context triggered piecewise hashing.
It also provides a library (libfuzzy) to generate/compare fuzzy hashes.
ssdeep hashes are now widely used for simple identification purposes. (e.g. Basic Properties section in VirusTotal )
Although “better fuzzy hashes” are available, ssdeep is still one of the primary choices because of its speed (now about twice as fast as TLSH) and being a de facto standard.

## Platforms

- Windows Download Windows (32-bit) binaries from GitHub project page .
	This binary package is tested on Windows 7 and Windows 10 (version 1703 - Creators Update).
Windows
Download Windows (32-bit) binaries from GitHub project page .
	This binary package is tested on Windows 7 and Windows 10 (version 1703 - Creators Update).
[LINK: GitHub project page](https://github.com/ssdeep-project/ssdeep/releases)
- Ubuntu ssdeep package is available.
Ubuntu
ssdeep package is available.
- Fedora ssdeep package is available.
Fedora
ssdeep package is available.
- Debian ssdeep package is available ( package tracker ).
Debian
ssdeep package is available ( package tracker ).
- CentOS (or other RHEL-based Linux distributions) ssdeep package on EPEL is available.
CentOS (or other RHEL-based Linux distributions)
ssdeep package on EPEL is available.
- Arch Linux ssdeep package (community repository) is available (no longer needs manual compilation!).
Arch Linux
ssdeep package (community repository) is available (no longer needs manual compilation!).
- FreeBSD security/ssdeep package on FreeBSD Ports is available
	(compilation is required but easy).
FreeBSD
security/ssdeep package on FreeBSD Ports is available
	(compilation is required but easy).
- Other *nix platforms If the distribution you use does not provide ssdeep package, you will need to build it yourself.
	Download the source code from GitHub project page and install it.
	It should work at most of GNU Autotools-compatible environment.
Other *nix platforms
If the distribution you use does not provide ssdeep package, you will need to build it yourself.
	Download the source code from GitHub project page and install it.
	It should work at most of GNU Autotools-compatible environment.
[LINK: GitHub project page](https://github.com/ssdeep-project/ssdeep/releases)

## Download

ssdeep is available at GitHub .
The latest version is 2.14.1 (released on 2017-11-07). You can take a look at the complete changelog , but here are the changes in the latest version:
[LINK: GitHub](https://github.com/ssdeep-project/ssdeep)
- Optimizations to the fuzzy hashing engine (hash generator can run as twice as fast and comparison can run 1.5 through 5 times faster [heavily depends on the data and platform] than the previous release)
- Fixed issue when certain memory allocation is failed

## Documentation

- Quick Start
- Manual (manpage of ssdeep.1)
- API Documentation
[LINK: API Documentation](doc/api/html/index.html)

## License / Copying

This program and its library are licensed
under the terms of the GNU General Public License as published by the Free Software Foundation ;
either version 2 of the License, or (at your option) any later version.

## People

Let us introduce some of the people who gave major contributions to the program.

### Jesse Kornblum

ssdeep was originally written by Jesse Kornblum.
He created this useful program based on
original spamsum code by Dr. Andrew Trigdell and
kept this program improved for years.

### Helmut Grohne

He mainly contributed to ssdeep version 2.10 and 2.11.
Thanks to his re-written fuzzy hashing engine, libfuzzy can now be used from multi-threaded programs
and is capable to process streams without seek capabilities.

### Tsukasa OI

He is the current project maintainer and mainly contributed to ssdeep version 2.13 and 2.14.
He improved stability, portability and speed of the fuzzy hashing engine and also fixed major bugs.

## Contact

If you have any questions or issues, please create an issue on GitHub .
[LINK: GitHub](https://github.com/ssdeep-project/ssdeep)
You may also contact the current project maintainer, Tsukasa OI <floss_ssdeep *at irq .dot a4lg .dot com.>.

--------------------