# tree-sitter
**URL:** https://tree-sitter.github.io/tree-sitter
**Page Title:** Introduction - Tree-sitter
--------------------


## Keyboard shortcuts

Press ← or → to navigate between chapters
Press S or / to search in the book
Press ? to show this help
Press Esc to hide this help

## Tree-sitter

## Introduction

Tree-sitter is a parser generator tool and an incremental parsing library. It can build a concrete syntax tree for a source
file and efficiently update the syntax tree as the source file is edited. Tree-sitter aims to be:
- General enough to parse any programming language
- Fast enough to parse on every keystroke in a text editor
- Robust enough to provide useful results even in the presence of syntax errors
- Dependency-free so that the runtime library (which is written in pure C11 )
can be embedded in any application
[LINK: C11](https://github.com/tree-sitter/tree-sitter/tree/master/lib)

## Language Bindings

There are bindings that allow Tree-sitter to be used from the following languages:

### Official

- Haskell
[LINK: Haskell](https://github.com/tree-sitter/haskell-tree-sitter)
- Java (JDK 22+)
[LINK: Java (JDK 22+)](https://github.com/tree-sitter/java-tree-sitter)
- JavaScript (Node.js)
[LINK: JavaScript (Node.js)](https://github.com/tree-sitter/node-tree-sitter)
- JavaScript (Wasm)
[LINK: JavaScript (Wasm)](https://github.com/tree-sitter/tree-sitter/tree/master/lib/binding_web)
- Kotlin
[LINK: Kotlin](https://github.com/tree-sitter/kotlin-tree-sitter)
- Python
[LINK: Python](https://github.com/tree-sitter/py-tree-sitter)
- Rust
[LINK: Rust](https://github.com/tree-sitter/tree-sitter/tree/master/lib/binding_rust)
- Swift
[LINK: Swift](https://github.com/tree-sitter/swift-tree-sitter)
- Zig
[LINK: Zig](https://github.com/tree-sitter/zig-tree-sitter)

### Third-party

- C# (.NET)
[LINK: C# (.NET)](https://github.com/zabbius/dotnet-tree-sitter)
- C++
[LINK: C++](https://github.com/nsumner/cpp-tree-sitter)
- Crystal
[LINK: Crystal](https://github.com/crystal-lang-tools/crystal-tree-sitter)
- Delphi
[LINK: Delphi](https://github.com/modersohn/delphi-tree-sitter)
- ELisp
- Guile
[LINK: Guile](https://github.com/Z572/guile-ts)
- Janet
[LINK: Janet](https://github.com/sogaiu/janet-tree-sitter)
- Java (JDK 8+)
[LINK: Java (JDK 8+)](https://github.com/bonede/tree-sitter-ng)
- Java (JDK 11+)
[LINK: Java (JDK 11+)](https://github.com/seart-group/java-tree-sitter)
- Julia
[LINK: Julia](https://github.com/MichaelHatherly/TreeSitter.jl)
- Lua
[LINK: Lua](https://github.com/euclidianAce/ltreesitter)
- Lua
[LINK: Lua](https://github.com/xcb-xwii/lua-tree-sitter)
- OCaml
[LINK: OCaml](https://github.com/semgrep/ocaml-tree-sitter-core)
- Odin
[LINK: Odin](https://github.com/laytan/odin-tree-sitter)
- Perl
- Pharo
[LINK: Pharo](https://github.com/Evref-BL/Pharo-Tree-Sitter)
- PHP
[LINK: PHP](https://github.com/soulseekah/ext-treesitter)
- Ruby
[LINK: Ruby](https://github.com/Faveod/ruby-tree-sitter)
Keep in mind that some of the bindings may be incomplete or out of date.

## Parsers

The following parsers can be found in the upstream organization:
- Agda
[LINK: Agda](https://github.com/tree-sitter/tree-sitter-agda)
- Bash
[LINK: Bash](https://github.com/tree-sitter/tree-sitter-bash)
- C++
[LINK: C++](https://github.com/tree-sitter/tree-sitter-cpp)
- CSS
[LINK: CSS](https://github.com/tree-sitter/tree-sitter-css)
- ERB / EJS
[LINK: ERB / EJS](https://github.com/tree-sitter/tree-sitter-embedded-template)
- Haskell
[LINK: Haskell](https://github.com/tree-sitter/tree-sitter-haskell)
- HTML
[LINK: HTML](https://github.com/tree-sitter/tree-sitter-html)
- Java
[LINK: Java](https://github.com/tree-sitter/tree-sitter-java)
- JavaScript
[LINK: JavaScript](https://github.com/tree-sitter/tree-sitter-javascript)
- JSDoc
[LINK: JSDoc](https://github.com/tree-sitter/tree-sitter-jsdoc)
- JSON
[LINK: JSON](https://github.com/tree-sitter/tree-sitter-json)
- Julia
[LINK: Julia](https://github.com/tree-sitter/tree-sitter-julia)
- OCaml
[LINK: OCaml](https://github.com/tree-sitter/tree-sitter-ocaml)
- PHP
[LINK: PHP](https://github.com/tree-sitter/tree-sitter-php)
- Python
[LINK: Python](https://github.com/tree-sitter/tree-sitter-python)
- Regex
[LINK: Regex](https://github.com/tree-sitter/tree-sitter-regex)
- Ruby
[LINK: Ruby](https://github.com/tree-sitter/tree-sitter-ruby)
- Rust
[LINK: Rust](https://github.com/tree-sitter/tree-sitter-rust)
- Scala
[LINK: Scala](https://github.com/tree-sitter/tree-sitter-scala)
- TypeScript
[LINK: TypeScript](https://github.com/tree-sitter/tree-sitter-typescript)
- Verilog
[LINK: Verilog](https://github.com/tree-sitter/tree-sitter-verilog)
A list of known parsers can be found in the wiki .
[LINK: wiki](https://github.com/tree-sitter/tree-sitter/wiki/List-of-parsers)

## Talks on Tree-sitter

- Strange Loop 2018
- FOSDEM 2018
- GitHub Universe 2017

## Underlying Research

The design of Tree-sitter was greatly influenced by the following research papers:
- Practical Algorithms for Incremental Software Development Environments
- Context Aware Scanning for Parsing Extensible Languages
- Efficient and Flexible Incremental Parsing
- Incremental Analysis of Real Programming Languages
- Error Detection and Recovery in LR Parsers
- Error Recovery for LR Parsers

--------------------