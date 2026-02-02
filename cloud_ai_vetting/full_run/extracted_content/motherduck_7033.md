# MotherDuck
**URL:** https://motherduck.com
**Page Title:** MotherDuck: Ducking Simple Data Warehouse based on DuckDB
--------------------

LEARN HOW TO PREPARE YOUR DATA WAREHOUSE FOR AGENTIC AI WORKLOADS Register for the webinar

## Infrastructure 
for Answers

The data warehouse built for answers, in SQL or natural language.

## "DuckDB In Action" Book for Free

Get the complete book for free in your inbox!

## Data Warehouse + AI

### Hypertenancy Data Warehouse

Scale per-user compute nodes independently, serving sub-second latency without resource contention.

### MotherDuck MCP Server

Turn natural language questions into accurate, traceable SQL queries with fully sandboxed compute.

## Who is it for?

Analytics that works for everyone
[LINK: Software Engineers Who ended up with a big data problem](/product/app-developers)

### Software Engineers

Who ended up with a big data problem

### Data Scientists

Who ended up having to do data engineering

### Data Engineers

With slow, brittle pipelines

## Who is it for?

Analytics that works for everyone
[LINK: Software Engineers Who ended up with a big data problem](/product/app-developers)

### Software Engineers

Who ended up with a big data problem

### Data Scientists

Who ended up having to do data engineering

### Data Engineers

With slow, brittle pipelines

## Use Cases

### Data Warehousing

Is your data all over the place? Start making sense of your business by bringing it together for internal business intelligence and analytics. Build pure SQL pipelines, share data and quickly collaborate with your team.
[LINK: How it Works](/docs/getting-started/data-warehouse/)

### Customer-facing Analytics

Unlike traditional BI, customer-facing analytics is built directly into your product for end users. It delivers near real-time, low-latency insights at scale — think milliseconds, not minutes — and must handle thousands to millions of concurrent queries. MotherDuck's architecture, from per-user tenancy to Wasm support, is designed for the unique requirements of Customer-Facing Analytics to drive increased user engagement directly in your app experience.
[LINK: How it Works](/docs/getting-started/customer-facing-analytics/)

## How We Scale

### Duckling Sizes

A Duckling is a dedicated DuckDB instance for each user, ensuring optimal performance and scalability in data analytics.
Pulse
Our smallest instance, perfect for ad-hoc analytics tasks
Standard
Built to handle common data warehouse workloads, including loads and transforms
Jumbo
For larger data warehouse workloads with many transformations or complex aggregations
Mega
An extremely large instance for when you need complex transformations done quickly
Giga
Largest instances enable the toughest transformations to run faster
Take a closer look at

### Per-user tenancy 
    and vertical scaling

MotherDuck employs a per-user tenancy and vertical scaling strategy. Users connect to their own MotherDuck Ducklings (DuckDB instances), which are sized (pulse, standard, jumbo, mega, giga) to meet their specific needs. There is also the option for additional Ducklings, through read scaling (explained below), to ensure flexible resource allocation. Ultimately, each Duckling establishes a connection with the central Data Warehouse storage.

### Read Scaling

MotherDuck's read scaling capabilities allow users to connect via a BI Tool to dedicated Ducklings that function as read replicas. These read replicas can be provisioned in various sizes (pulse, standard, jumbo, mega or giga) to accommodate different needs. Ultimately, these read replicas connect to the Data Warehouse storage, enabling efficient handling of read operations.

## Ecosystem

Modern Duck Stack

### CLOUD
DATA WAREHOUSE

### Sources

### Business Intelligence

### Ingestion

### Data Science & AI

### Reverse ETL

### Transformation

### Dev Tools

### Orchestration

### Data Quality

We now have a doctor vibe-coding artifacts and tools that can talk to all the data that the company has, run processes, and then actually go and affect them directly.
Greg Inman
Chief Technology Officer
We now have a doctor vibe-coding artifacts and tools that can talk to all the data that the company has, run processes, and then actually go and affect them directly.
MotherDuck is the GOAT
Nate Hamm
Sr Software Developer at Reflex
MotherDuck is the GOAT
MotherDuck is insanely performant, and there’s no infrastructure to manage. The cost of experimentation is incredibly low — which means we can afford to ask more questions and build more features, faster.
[LINK: READ MORE](https://motherduck.com/case-studies/kultura-capital/)
Kristov Paulus
Founder, Chief Investment Officer at Kultura Capital
MotherDuck is insanely performant, and there’s no infrastructure to manage. The cost of experimentation is incredibly low — which means we can afford to ask more questions and build more features, faster.
[LINK: READ MORE](https://motherduck.com/case-studies/kultura-capital/)
We used to do analytics in a MySQL database with all of our daily device, telemetry, and image processing data. There was no way to scale that further using MySQL. With MotherDuck, we’re finally starting to find patterns in our data to help customers grow produce more effectively.
Rob Teeuwen
Data Scientist at Gardyn
We used to do analytics in a MySQL database with all of our daily device, telemetry, and image processing data. There was no way to scale that further using MySQL. With MotherDuck, we’re finally starting to find patterns in our data to help customers grow produce more effectively.
Instant SQL in MotherDuck will save me the misery of having to try and wrangle SQL in my BI tool where iteration speed can be very slow. This lets me get the data right earlier in the process and with faster feedback than waiting for a chart to render, or having to clear an analytics cache.
Mike McClannahan
CTO, DashFuel
Instant SQL in MotherDuck will save me the misery of having to try and wrangle SQL in my BI tool where iteration speed can be very slow. This lets me get the data right earlier in the process and with faster feedback than waiting for a chart to render, or having to clear an analytics cache.
Bringing MotherDuck into our data stack has been a game changer. We're reducing friction and supercharging our dev and ops experience by leveraging the DuckDB interoperability across local and cloud.
Ravi Chandra
CTO at Dexibit
Bringing MotherDuck into our data stack has been a game changer. We're reducing friction and supercharging our dev and ops experience by leveraging the DuckDB interoperability across local and cloud.
Moving to MotherDuck, a billed by-the-second cloud offering is a no-brainer for us, considering the elegance and efficiency of a single node system compared to traditional OLAP solutions.
Nico Ritschel
Director of Engineering at atm.com
Moving to MotherDuck, a billed by-the-second cloud offering is a no-brainer for us, considering the elegance and efficiency of a single node system compared to traditional OLAP solutions.
MotherDuck with DuckDB was by far the fastest of the OLAP platforms we evaluated - both in the cloud and run on our developer's machines - bridging price and performance and greatly increasing productivity.
Jim O’Neill
CTO and Co-founder at FinQore
MotherDuck with DuckDB was by far the fastest of the OLAP platforms we evaluated - both in the cloud and run on our developer's machines - bridging price and performance and greatly increasing productivity.
I just onboarded some non-technical users to MotherDuck, and I can’t imagine having done so in a different system with this level of ease and lack of intimidation. Between the ‘Filter’ button, Column Explorer, and the FROM syntax - they feel empowered to answer many of their own questions! 🙂
Sahil Gupta
Senior Data Engineer at dosomething.org
I just onboarded some non-technical users to MotherDuck, and I can’t imagine having done so in a different system with this level of ease and lack of intimidation. Between the ‘Filter’ button, Column Explorer, and the FROM syntax - they feel empowered to answer many of their own questions! 🙂
MotherDuck proving once again they are not constrained by what is easy or common. Instant SQL will not only enable complex query construction for those who find the task daunting (everyone?), it'll help past me communicate with future me.
SJ Browne
Software Engineer at DashFuel
MotherDuck proving once again they are not constrained by what is easy or common. Instant SQL will not only enable complex query construction for those who find the task daunting (everyone?), it'll help past me communicate with future me.
We found that DuckDB and MotherDuck are amazing tools for small data teams like ours.
Dave Crusoe
VP of Product & Engineering at DoSomething
We found that DuckDB and MotherDuck are amazing tools for small data teams like ours.

## Our Community

Ryan Dolley
MotherDuck ... bringing big innovation to SQL to make it more like a real language and less like a 'groovy ancient programming language from the 70s.' Check it out.
Robert Lancer
The progress on the MotherDuck UI is amazing! It went from minimal utility to my preferred place to write SQL in a matter of months
Caleb Fahlgren
The amount of data I am storing in 
@motherduck rn for a new project is criminal 🤣
Decided to try it out since I am a big 
@duckdb user. Is pretty good so far. Have few hundred million records.
Simon Späti 🏔️
I'm just checking a little about the hosted DuckDB by @motherduck. What a nice user experience. It automatically detects errors, and `accept & run` fixes common errors. Love it.
Jacob Matson
using sql for data cleaning vs excel (reason 879 to learn sql)

levenstein distance between 590strings in excel (350k combinations): 
excel: 25 mins of spinning. 
duckdb: 1.2s
Bob Currier
If you're not familiar with DuckDB, you definitely want to give it a look. I've recently converted all my existing code from using CSV files and SQLite databases for exploratory analysis to parquet files, DuckDB and MotherDuck. The transformation in my workflow has been nothing short of astounding. 10GB of CSV files turned into 1GB of parquet files that are now stored in S3 buckets. Using DuckDB and MotherDuck, I can run exploratory queries seamlessly thanks to the DuckStack with dual execution with local processing and cloud scale. My query development time has decreased by 90%. And I'm loving the team feature of the MotherDuck platform. OCEANCODA is rocking the small data life! #duckdb #python #motherduck #eda #ai #ml (Graphic courtesy of Manning Publications Co. book 'DuckDB in Action.' ) Check it out.
evidence
DuckDB is increasingly being built into every data tool, but DuckDB isn't designed to be used as a cloud data warehouse

@motherduck is solving that problem, and they’re doing it in a delightful, uniquely DuckDB way
Ethan
DuckDB is my new best friend for analytics. It's so fast, makes it easy to manipulate dataframes, ingests anything, and exports it to whatever form I want. 

Parquet, Arrow dataframes, and DuckDB are the future for analytics.
uwe geercken
#duckdb is really impressive: good terminal client, solid, easy and fast import of csv data and impressive speed on a 20mio data set. With automatic schema creation. Easy export to parquet and more. I think I am gonna spend more time on it...
Etienne Posthumus
I have been kicking the tyres of @motherduck - and it is 🤯

Being able to do hybrid queries over local and humongous remote datasets are incredible.

The potential applications are making my head spin with awe and excitement. Well done.
Jamin Ball
Another awesome & insightful post from the @motherduck team. The last few decades have been about scale-out. The next decade will be about scale-up! What you can accomplish with a single machine these days is incredibly impressive
Danny Blumenthal
Our friends at MotherDuck stand out in the data space for how consistently they keep shipping awesome new features.
Nico Ritschel
I just deployed to Rill cloud backed by Motherduck and it worked great— wonderful experience...
    In-browser CLI auth with Rill Cloud, added my Motherduck token, invited some viewers, I'm live. Took 3 minutes.
Damon Cortesi
Because, I don't have enough time on my hands, I created a DuckDB extension that allows you to import data by scanning an Athena table. 

https://github.com/dacort/duckdb-athena-extension
George Fraser
How fast is DuckDB compared to the best commercial data warehouses? I decided to benchmark it myself. Short version: very fast! But it's not (yet) great at scaling up to many cores. https://fivetran.com/blog/how-fast-is-duckdb-really
MotherDuck
@duckdb is empowering machine learning use cases! 🤖
Any good model training starts with some good data exploration.
  
@huggingface now enables SQL queries using DuckDB on any dataset stored on the Hub!
DuckDB
DuckDB Co-Creator @hfmuehleisen and MotherDuck Founder @jrdntgn in this new podcast - among other things about the origin story of DuckDB and later MotherDuck:
Garrett McClintock
just built a pipeline using @dltHub and @motherduck and it's very nice. 10/10 experience once you get the hang of it and very scalable.
Andrew Madson
Instant SQL!  This is one of the highlights of Data Council... Instant SQL caches a sample of your table instantly, and synchronously updates the query results, AS YOU TYPE!
KKovacs [ス]
I don’t want to say that #DuckDB is a silver bullet because there is no such thing, but it’s surprisingly projectile-shaped, very shiny, and killed all the various werewolves (ok, data problems) I’ve thrown at it
evidence
DuckDB is increasingly being built into every data tool, but DuckDB isn't designed to be used as a cloud data warehouse

@motherduck
 is solving that problem, and they’re doing it in a delightful, uniquely DuckDB way...
Zach Wilson
Matt Martin and I did a runtime benchmark of Apache Spark vs DuckDB (by MotherDuck)
We found that data sets under 20 gigabytes ran about 100 times faster on DuckDB than they did on Apache Spark!

This benchmark uses plain parquet files and COUNT distinct to truly measure performance without skipping any data so we know the differences are correct.

Here's the complete writeup: https://lnkd.in/gXuWGWyy
Daniel Beach
This MotherDuck thingy is such a beauty it brings a tear to me old eye. You have no idea how many new tools (maybe you do) I agonize over while trying to bring you the good, the bad, and the ugly.
FOLLOW US

## Join the flock

## SUBSCRIBE

### Subscribe to our newsletter

MotherDuck
[LINK: Docs](/docs/)
Product
[LINK: Customer-facing Analytics](/product/app-developers/)
Community
Company

--------------------