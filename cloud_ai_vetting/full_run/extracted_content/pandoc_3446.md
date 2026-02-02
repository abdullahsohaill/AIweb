# Pandoc
**URL:** https://pandoc.org
**Page Title:** Pandoc - index
--------------------

If you need to convert files from one markup format into
      another, pandoc is your swiss-army knife. Pandoc can convert
      between the following formats:
(← = conversion from; → = conversion to; ↔︎ = conversion from
      and to)
↔︎ Markdown (including CommonMark and GitHub-flavored
      Markdown ) ↔︎ reStructuredText ↔︎ AsciiDoc ↔︎ Emacs Org-Mode ↔︎ Emacs Muse ↔︎ Textile → Markua ← txt2tags ↔︎ djot → BBCode
[LINK: GitHub-flavored
      Markdown](https://github.github.com/gfm/)
[LINK: reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/introduction.html)
↔︎ (X)HTML 4 ↔︎ HTML5 → Chunked HTML
↔︎ EPUB version
      2 or 3 ↔︎ FictionBook2
→ GNU
      TexInfo ← pod ↔︎ Haddock
      markup → Vimdoc
↔︎ roff
      man → roff
      ms ← mdoc
↔︎ LaTeX → ConTeXt
↔︎ DocBook version 4 or
      5 ↔︎ JATS ← BITS → TEI
      Simple → OpenDocument XML
[LINK: TEI
      Simple](https://github.com/TEIC/TEI-Simple)
↔︎ OPML
↔︎ BibTeX ↔︎ BibLaTeX ↔︎ CSL
      JSON ↔︎ CSL YAML ← RIS ← EndNote
      XML
[LINK: BibLaTeX](https://github.com/plk/biblatex)
[LINK: CSL
      JSON](https://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html)
↔︎ Microsoft Word docx ↔︎ Rich Text Format RTF ↔︎ OpenOffice/LibreOffice ODT
↔︎ Jupyter notebook ( ipynb )
[LINK: ipynb](https://nbformat.readthedocs.io/en/latest/)
→ InDesign
      ICML ↔︎ Typst
↔︎ MediaWiki
      markup ↔︎ DokuWiki
      markup ← TikiWiki
      markup ← TWiki
      markup ← Vimwiki markup → XWiki
      markup → ZimWiki
      markup ↔︎ Jira
      wiki markup ← Creole
[LINK: Vimwiki markup](https://vimwiki.github.io)
→ LaTeX Beamer ↔︎ Microsoft PowerPoint → Slidy → reveal.js → Slideous → S5 → DZSlides
← CSV tables ← TSV tables ← Microsoft Excel spreadsheets
→ ANSI -formatted
      text
↔︎ Haskell AST ↔︎ JSON representation of AST ↔︎ XML representation of AST
↔︎ custom readers and writers can be written in Lua
Pandoc understands a number of useful markdown syntax
      extensions, including document metadata (title, author, date);
      footnotes; tables; definition lists; superscript and subscript;
      strikeout; enhanced ordered lists (start number and numbering
      style are significant); running example lists; delimited code
      blocks with syntax highlighting; smart quotes, dashes, and
      ellipses; markdown inside HTML blocks; and inline LaTeX. If strict
      markdown compatibility is desired, all of these extensions can be
      turned off.
LaTeX math (and even macros) can be used in markdown documents.
      Several different methods of rendering math in HTML are provided,
      including MathJax and translation to MathML. LaTeX math is
      converted (as needed by the output format) to unicode, native Word
      equation objects, MathML, or roff eqn.
Pandoc includes a powerful system for automatic citations and
      bibliographies. This means that you can write a citation like
and pandoc will convert it into a properly formatted citation
      using any of hundreds of CSL styles (including
      footnote styles, numerical styles, and author-date styles), and
      add a properly formatted bibliography at the end of the document.
      The bibliographic data may be in BibTeX , BibLaTeX , CSL
      JSON , or CSL YAML format. Citations work in every output
      format.
[LINK: BibLaTeX](https://github.com/plk/biblatex)
[LINK: CSL
      JSON](https://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html)
There are many ways to customize pandoc to fit your needs,
      including a template system and a powerful system for writing
      filters.
Pandoc includes a Haskell library and a standalone command-line
      program. The library includes separate modules for each input and
      output format, so adding a new input or output format just
      requires adding a new module.
Pandoc is free software, released under the GPL . Copyright
      2006–2025 John
      MacFarlane .

--------------------