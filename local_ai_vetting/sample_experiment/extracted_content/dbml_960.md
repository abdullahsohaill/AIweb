# DBML
**URL:** https://dbml.dbdiagram.io/home
**Page Title:** Home | DBML
--------------------

Open source

## Intro ​

DBML (Database Markup Language) is an open-source DSL language designed to define and document database schemas and structures. It is designed to be simple, consistent and highly-readable.
It also comes with command-line tool and open-source module to help you convert between DBML and SQL.
See the above dbml doc visualized on dbdiagram and dbdocs
[LINK: dbdocs](https://dbdocs.io/Holistics/Ecommerce)
For full DBML syntax documentation, refer to the Syntax section.
[LINK: Syntax](/docs)
Note: DBML is not to be confused with Microsoft's DBML file extension (XML format).

## Benefits ​

DBML is born to solve the frustrations of developers working on large, complex software projects:
- Difficulty building up a mental "big picture" of an entire project's database structure.
- Trouble understanding tables and what their fields mean, and which feature are they related to.
- The existing ER diagram and/or SQL DDL code is poorly written and hard to read (and usually outdated).
Our recommended best practices is to have a database.dbml file in your root repository (similar to other config and/or boilerplate files, eg. packages.json or README.md )

## Is this similar to SQL DDL? ​

Not quite. Despite its name (data "definition" language), DDL is designed mainly
to help physically create, modify or remove tables, not to define them. In other
words, DDL is imperative, while DBML is declarative . This makes DBML so much
easier to write, read and maintain.
DDL is also database specific (Oracle, PostgreSQL, etc), while DBML is
database-agnostic and designed for the high-level database architecting
instead of low-level database creation.

## What can I do now? ​

DBML comes with:
- A free database visualiser at dbdiagram.io .
- A free database documentation builder at dbdocs.io .
[LINK: dbdocs.io](https://dbdocs.io?utm_source=dbml)
- A free SQL playground at runsql.com .
- A command-line tool to help to convert SQL to DBML files and vice versa.
- An open-source JS library (NPM package) for you to programmatically convert between DBML and SQL DDL.

### dbdiagram ​

dbdiagram.io is a free tool to help you visualize database diagrams from DBML code.

### dbdocs ​

dbdocs.io is a free tool to help you build database documents from DBML code.
[LINK: dbdocs.io](https://dbdocs.io?utm_source=dbml)

### RunSQL ​

runsql.com is a free & simple tool to create mock database environments to validate your SQL queries.

### Command-line Tool (CLI) ​

A simple command-line tool to help you convert between SQL (DDL) and DBML. Refer to CLI docs for more info.

## DBML History ​

DBML was born out from dbdiagram.io , a simple database diagram visualizer. At the time (Aug 2018) we were looking for a simple tool to design database structure but couldn't come up with one we liked. So we decided to build one.
After 1 year and over 100k diagrams created by 60k internet users later, we realized the syntax we designed for users to draw diagram is very received and one of the key values of the tool. That's how DBML is born. Our aim is to make DBML a good and simple way for developers to design and document database structures.

## DBML Statistics ​

- 2.5M DBML docs created via dbdiagram.io and dbdocs.io (as of Feb 2025).
- 1.4M users using DBML (as of Feb 2025).

## Who's behind DBML? ​

DBML is created and maintained by Holistics , an analytics platform company.

## Community ​

- DBML is being open-sourced on Github .
[LINK: being open-sourced on Github](https://github.com/holistics/dbml/)
- Have a question, suggestion or want to contribute? Use the dbml issues page .
[LINK: the dbml issues page](https://github.com/holistics/dbml/issues)

## Community Contributions ​

- Emacs Mode for DBML by ccod
[LINK: Emacs Mode for DBML by ccod](https://github.com/ccod/dbd-mode)
- Vim Plugin for DBML by jidn
[LINK: Vim Plugin for DBML by jidn](https://github.com/jidn/vim-dbml)
- VSCode Plugin for DBML by duynvu
- Python parser for DBML by Vanderhoof
[LINK: Python parser for DBML by Vanderhoof](https://github.com/Vanderhoof/PyDBML)
- FloorPlan: Android's Room to DBML by julioz
[LINK: FloorPlan: Android's Room to DBML by julioz](https://github.com/julioz/FloorPlan)
- Go parser for DBML by duythinht
[LINK: Go parser for DBML by duythinht](https://github.com/duythinht/dbml-go)
- DbmlForDjango: Converter between Django models.py and DBML
[LINK: DbmlForDjango: Converter between Django models.py and DBML](https://github.com/hamedsj/DbmlForDjango)
- parseServerSchema2dbml: Converter between ParseServer MongoDB _SCHEMA collection and DBML by stepanic
[LINK: parseServerSchema2dbml: Converter between ParseServer MongoDB _SCHEMA collection and DBML by stepanic](https://github.com/stepanic/parse-server-SCHEMA-to-DBML)
- dbml-renderer: A DBML CLI renderer
[LINK: dbml-renderer: A DBML CLI renderer](https://github.com/softwaretechnik-berlin/dbml-renderer)
- dbml-parser: A DBML parser written on PHP8 by Butschster
[LINK: dbml-parser: A DBML parser written on PHP8 by Butschster](https://github.com/butschster/dbml-parser)
- Kacher: Laravel's Database Schemas to DBML by Arsanandha Aphisitworachorch
[LINK: Kacher: Laravel's Database Schemas to DBML by Arsanandha Aphisitworachorch](https://github.com/aphisitworachorch/kacher)
- d365fo-entity-schema: Generate DBML from Dynamics 365 Finance and Operations
[LINK: d365fo-entity-schema: Generate DBML from Dynamics 365 Finance and Operations](https://github.com/noakesey/d365fo-entity-schema)
- Treesitter for DBML
[LINK: Treesitter for DBML](https://github.com/dynamotn/tree-sitter-dbml)
- DB2Code: Generate DBML from Maven
[LINK: DB2Code: Generate DBML from Maven](https://github.com/alberlau/DB2Code)
- dbml-java: A DBML parser written on Java 17 by Nils Wende
[LINK: dbml-java: A DBML parser written on Java 17 by Nils Wende](https://github.com/nilswende/dbml-java)
- SchemaToDbml: A gem that generates DBML from Rails schema.rb by Ricardo Ribeiro
[LINK: SchemaToDbml: A gem that generates DBML from Rails schema.rb by Ricardo Ribeiro](https://github.com/ricardojcribeiro/schema_to_dbml)
- Snowflake DBML Generator by Ryan Rozich
[LINK: Snowflake DBML Generator by Ryan Rozich](https://github.com/ryanrozich/snowflake-dbml-generator)
- prisma-dbml-generator: Generate DBML schema from Prisma Schema by Marc Stammerjohann
[LINK: prisma-dbml-generator: Generate DBML schema from Prisma Schema by Marc Stammerjohann](https://github.com/notiz-dev/prisma-dbml-generator)
- C# parser for Dbml by Niels Bosma
[LINK: C# parser for Dbml by Niels Bosma](https://github.com/Ivy-Interactive/Ivy.Dbml.Parser)
- Scafoldr: DBML-Powered Code Scaffolding Tool
- Intro
- Benefits
- Is this similar to SQL DDL?
- What can I do now? dbdiagram dbdocs RunSQL Command-line Tool (CLI)
- dbdiagram
- dbdocs
[LINK: dbdocs](#dbdocs)
- RunSQL
- Command-line Tool (CLI)
- DBML History
- DBML Statistics
- Who's behind DBML?
- Community
- Community Contributions

--------------------