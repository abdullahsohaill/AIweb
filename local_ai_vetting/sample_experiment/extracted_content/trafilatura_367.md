# Trafilatura
**URL:** https://trafilatura.readthedocs.io
**Page Title:** A Python package & command-line tool to gather text on the Web — Trafilatura 2.0.0 documentation
--------------------

- GitHub
[LINK: GitHub](https://github.com/adbar/trafilatura)

## A Python package & command-line tool to gather text on the Web #

## Description #

Trafilatura is a Python package and command-line tool designed to gather text on the Web. It includes discovery, extraction and text processing components. Its main applications are web crawling, downloads, scraping, and extraction of main texts, metadata and comments. It aims at staying handy and modular : no database is required, the output can be converted to commonly used formats.
Going from raw HTML to essential parts can alleviate many problems related to text quality, by avoiding the noise caused by recurring elements like headers and footers and by making sense of the data and metadata with selected information. The extractor strikes a balance between limiting noise (precision) and including all valid parts (recall). It is robust and reasonably fast .
Trafilatura is widely used and integrated into thousands of projects by companies like HuggingFace, IBM, and Microsoft Research as well as institutions like the Allen Institute, Stanford, the Tokyo Institute of Technology, and the University of Munich.
[LINK: thousands of projects](https://github.com/adbar/trafilatura/network/dependents)

### Features #

- Advanced web crawling and text discovery: Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS) Smart crawling and URL management (filtering and deduplication)
- Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
- Smart crawling and URL management (filtering and deduplication)
Smart crawling and URL management (filtering and deduplication)
- Parallel processing of online and offline input: Live URLs, efficient and polite processing of download queues Previously downloaded HTML files and parsed HTML trees
- Live URLs, efficient and polite processing of download queues
Live URLs, efficient and polite processing of download queues
- Previously downloaded HTML files and parsed HTML trees
Previously downloaded HTML files and parsed HTML trees
- Robust and configurable extraction of key elements: Main text (common patterns and generic algorithms like jusText and readability) Metadata (title, author, date, site name, categories and tags) Formatting and structure: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting Optional elements: comments, links, images, tables
- Main text (common patterns and generic algorithms like jusText and readability)
Main text (common patterns and generic algorithms like jusText and readability)
- Metadata (title, author, date, site name, categories and tags)
Metadata (title, author, date, site name, categories and tags)
- Formatting and structure: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting
Formatting and structure: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting
- Optional elements: comments, links, images, tables
Optional elements: comments, links, images, tables
- Multiple output formats: TXT and Markdown CSV JSON HTML, XML and XML-TEI
- TXT and Markdown
TXT and Markdown
- CSV
CSV
- JSON
JSON
- HTML, XML and XML-TEI
HTML, XML and XML-TEI
- Optional add-ons: Language detection on extracted content Speed optimizations
- Language detection on extracted content
Language detection on extracted content
- Speed optimizations
Speed optimizations
- Actively maintained with support from the open-source community: Regular updates, feature additions, and optimizations Comprehensive documentation
- Regular updates, feature additions, and optimizations
Regular updates, feature additions, and optimizations
- Comprehensive documentation
Comprehensive documentation

### Evaluation and alternatives #

Trafilatura consistently outperforms other open-source libraries in text extraction benchmarks, showcasing its efficiency and accuracy in extracting web content. The extractor tries to strike a balance between limiting noise and including all valid parts.
The benchmark section details alternatives and results, the evaluation readme describes how to reproduce the evaluation.
[LINK: evaluation readme](https://github.com/adbar/trafilatura/blob/master/tests/README.rst)

## In a nutshell #

Primary installation method is with a Python package manager: pip install trafilatura (→ installation documentation ).
With Python:
On the command-line:
For more see usage documentation and tutorials .

## License #

This package is distributed under the Apache 2.0 license .
Versions prior to v1.8.0 are under GPLv3+ license.

## Context #

This work started as a PhD project at the crossroads of linguistics and NLP,
this expertise has been instrumental in shaping Trafilatura over the years.
Initially launched to create text databases for research purposes
at the Berlin-Brandenburg Academy of Sciences (DWDS and ZDL units),
this package continues to be maintained but its future depends on community support.
If you value this software or depend on it for your product, consider
sponsoring it and contributing to its codebase . Your support on GitHub or ko-fi.com will help maintain and enhance this popular package.
Visit the Contributing page for more information.
[LINK: on GitHub](https://github.com/sponsors/adbar)
[LINK: Contributing page](https://github.com/adbar/trafilatura/blob/master/CONTRIBUTING.md)
Trafilatura is an Italian word for wire drawing symbolizing the refinement and conversion process. It is also the way shapes of pasta are formed.

### Author #

Reach out via the software repository or the contact page for inquiries, collaborations, or feedback. See also social networks for the latest updates.
- Barbaresi, A. Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction , Proceedings of ACL/IJCNLP 2021: System Demonstrations, 2021, p. 122-131.
Barbaresi, A. Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction , Proceedings of ACL/IJCNLP 2021: System Demonstrations, 2021, p. 122-131.
- Barbaresi, A. “ Generic Web Content Extraction with Open-Source Software ”, Proceedings of KONVENS 2019, Kaleidoscope Abstracts, 2019.
Barbaresi, A. “ Generic Web Content Extraction with Open-Source Software ”, Proceedings of KONVENS 2019, Kaleidoscope Abstracts, 2019.
- Barbaresi, A. “ Efficient construction of metadata-enhanced web corpora ”, Proceedings of the 10th Web as Corpus Workshop (WAC-X) , 2016.
Barbaresi, A. “ Efficient construction of metadata-enhanced web corpora ”, Proceedings of the 10th Web as Corpus Workshop (WAC-X) , 2016.

### Citing Trafilatura #

Trafilatura is widely used in the academic domain, chiefly for data acquisition. Here is how to cite it:

### Software ecosystem #

Jointly developed plugins and additional packages also contribute to the field of web data extraction and analysis:
Corresponding posts can be found on Bits of Language .
The blog covers a range of topics from technical how-tos, updates on new
features, to discussions on text mining challenges and solutions.

## Building the docs #

Starting from the docs/ folder of the repository:
- pip install -r requirements.txt
pip install -r requirements.txt
- sphinx-build -b html . _build/ (where _build is the target directory)
sphinx-build -b html . _build/ (where _build is the target directory)

## Changes #

For version history and changes see the changelog .
[LINK: changelog](https://github.com/adbar/trafilatura/blob/master/HISTORY.md)

## Further documentation #

- Installation Python Trafilatura package Additional functionality
- Python
- Trafilatura package
- Additional functionality
- Usage Quickstart With Python On the command-line With R API Graphical user interface Download web pages Web crawling Settings and customization Deduplication Troubleshooting URL management
- Quickstart
- With Python
- On the command-line
- With R
- API
[LINK: API](usage-api.html)
- Graphical user interface
- Download web pages
- Web crawling
- Settings and customization
- Deduplication
- Troubleshooting
- URL management
- Tutorials Tutorial: Gathering a custom web corpus Tutorial: From a list of links to a frequency list Tutorial: Validation of TEI files Tutorial: Text embedding Tutorial: DWDS-Korpusdaten reproduzieren Blog posts Videos External resources
- Tutorial: Gathering a custom web corpus
- Tutorial: From a list of links to a frequency list
- Tutorial: Validation of TEI files
- Tutorial: Text embedding
- Tutorial: DWDS-Korpusdaten reproduzieren
- Blog posts
- Videos
- External resources
- Evaluation External evaluations Alternatives Description Results (2022-05-18) Older results
- External evaluations
- Alternatives
- Description
- Results (2022-05-18)
- Older results
- Uses & citations Notable projects using this software Citations in papers Publications citing Trafilatura Publications citing Htmldate
- Notable projects using this software
- Citations in papers
- Publications citing Trafilatura
- Publications citing Htmldate
- Core functions Extraction Link discovery Helpers XML processing
- Extraction
- Link discovery
- Helpers
- XML processing
- Background Compendium: Web texts in linguistics and humanities Finding sources for web corpora Working with corpus data
- Compendium: Web texts in linguistics and humanities
- Finding sources for web corpora
- Working with corpus data
Index

### This Page

- Show Source

--------------------