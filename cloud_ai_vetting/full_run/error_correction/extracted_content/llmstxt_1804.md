# llms.txt
**URL:** https://docs.datafold.com/llms.txt
**Page Title:** 
--------------------

### (Raw Extraction Fallback)

# Datafold

## Docs

- [Get Audit Logs](https://docs.datafold.com/api-reference/audit-logs/get-audit-logs.md)
- [Create a DBT BI integration](https://docs.datafold.com/api-reference/bi/create-a-dbt-bi-integration.md)
- [Create a Hightouch integration](https://docs.datafold.com/api-reference/bi/create-a-hightouch-integration.md)
- [Create a Looker integration](https://docs.datafold.com/api-reference/bi/create-a-looker-integration.md)
- [Create a Mode Analytics integration](https://docs.datafold.com/api-reference/bi/create-a-mode-analytics-integration.md)
- [Create a Power BI integration](https://docs.datafold.com/api-reference/bi/create-a-power-bi-integration.md)
- [Create a Tableau integration](https://docs.datafold.com/api-reference/bi/create-a-tableau-integration.md)
- [Get an integration](https://docs.datafold.com/api-reference/bi/get-an-integration.md): Returns the integration for Mode/Tableau/Looker/HighTouch by its id.
- [List all integrations](https://docs.datafold.com/api-reference/bi/list-all-integrations.md): Return all integrations for Mode/Tableau/Looker
- [Remove an integration](https://docs.datafold.com/api-reference/bi/remove-an-integration.md)
- [Sync a BI integration](https://docs.datafold.com/api-reference/bi/sync-a-bi-integration.md): Start an unscheduled synchronization of the integration.
- [Update a DBT BI integration](https://docs.datafold.com/api-reference/bi/update-a-dbt-bi-integration.md): Returns the integration with changed fields.
- [Update a Hightouch integration](https://docs.datafold.com/api-reference/bi/update-a-hightouch-integration.md): It can only update the schedule. Returns the integration with changed fields.
- [Update a Looker integration](https://docs.datafold.com/api-reference/bi/update-a-looker-integration.md): It can only update the schedule. Returns the integration with changed fields.
- [Update a Mode Analytics integration](https://docs.datafold.com/api-reference/bi/update-a-mode-analytics-integration.md): It can only update the schedule. Returns the integration with changed fields.
- [Update a Power BI integration](https://docs.datafold.com/api-reference/bi/update-a-power-bi-integration.md): Updates the integration configuration. Returns the integration with changed fields.
- [Update a Tableau integration](https://docs.datafold.com/api-reference/bi/update-a-tableau-integration.md): It can only update the schedule. Returns the integration with changed fields.
- [List CI runs](https://docs.datafold.com/api-reference/ci/list-ci-runs.md)
- [Trigger a PR/MR run](https://docs.datafold.com/api-reference/ci/trigger-a-prmr-run.md)
- [Upload PR/MR changes](https://docs.datafold.com/api-reference/ci/upload-prmr-changes.md)
- [Create a data diff](https://docs.datafold.com/api-reference/data-diffs/create-a-data-diff.md): Launches a new data diff to compare two datasets (tables or queries).

A data diff identifies differences between two datasets by comparing:
- Row-level changes (added, removed, modified rows)
- Schema differences
- Column-level statistics

The diff runs asynchronously. Use the returned diff ID to poll for status and retrieve results.
- [Get a data diff](https://docs.datafold.com/api-reference/data-diffs/get-a-data-diff.md)
- [Get a data diff summary](https://docs.datafold.com/api-reference/data-diffs/get-a-data-diff-summary.md)
- [Get a human-readable summary of a DataDiff comparison](https://docs.datafold.com/api-reference/data-diffs/get-a-human-readable-summary-of-a-datadiff-comparison.md): Retrieves a comprehensive, human-readable summary of a completed data diff.

This endpoint provides the most useful information for understanding diff results:
- Overall status and result (success/failure)
- Human-readable feedback explaining the differences found
- Key statistics (row counts, differences, match rates)
- Configuration details (tables compared, primary keys used)
- Error messages if the diff failed

Use this after a diff completes to get actionable insights. For diffs still running,
check status with get_datadiff first.
- [List data diffs](https://docs.datafold.com/api-reference/data-diffs/list-data-diffs.md): All fields support multiple items, using just comma delimiter
Date fields also support ranges using the following syntax:

- ``<DATETIME`` = before DATETIME
- ``>DATETIME`` = after DATETIME
- ``DATETIME`` = between DATETIME and DATETIME + 1 MINUTE
- ``DATE`` = start of that DATE until DATE + 1 DAY
- ``DATETIME1<<DATETIME2`` = between DATETIME1 and DATETIME2
- ``DATE1<<DATE2`` = between DATE1 and DATE2
- [Update a data diff](https://docs.datafold.com/api-reference/data-diffs/update-a-data-diff.md)
- [Create a data source](https://docs.datafold.com/api-reference/data-sources/create-a-data-source.md)
- [Execute a SQL query against a data source](https://docs.datafold.com/api-reference/data-sources/execute-a-sql-query-against-a-data-source.md): Executes a SQL query against the specified data source and returns the results.

This endpoint allows you to run ad-hoc SQL queries for data exploration, validation, or analysis.
The query is executed using the data source's native query runner with the appropriate credentials.

**Streaming mode**: Use query parameter `?stream=true` or set `X-Stream-Response: true` header.
Streaming is only supported for certain data sources (e.g., Databricks).
When streaming, results are sent incrementally as valid JSON for memory efficiency.

Returns:
- Query results as rows with column metadata (name, type, description)
- Limited to a reasonable number of rows for performance
- [Get a data source](https://docs.datafold.com/api-reference/data-sources/get-a-data-source.md)
- [Get a data source summary](https://docs.datafold.com/api-reference/data-sources/get-a-data-source-summary.md)
- [Get data source testing results](https://docs.datafold.com/api-reference/data-sources/get-data-source-testing-results.md)
- [List data source types](https://docs.datafold.com/api-reference/data-sources/list-data-source-types.md)
- [List data sources](https://docs.datafold.com/api-reference/data-sources/list-data-sources.md): Retrieves all data sources accessible to the authenticated user.

Returns active data sources (not deleted, hidden, or draft) that the user has permission to access.
For non-admin users, only data sources belonging to their assigned groups are returned.
- [Test a data source connection](https://docs.datafold.com/api-reference/data-sources/test-a-data-source-connection.md)
- [Datafold API](https://docs.datafold.com/api-reference/datafold-api.md)
- [Datafold SDK](https://docs.datafold.com/api-reference/datafold-sdk.md)
- [Get translation projects](https://docs.datafold.com/api-reference/dma/get-translation-projects.md): Get all translation projects for an organization.
This is used for DMA v1 and v2, since it's TranslationProject is a SQLAlchemy model.
Version is used to track if it's a DMA v1 or v2 project.
- [Check status of a DMA translation job](https://docs.datafold.com/api-reference/dma_v2/check-status-of-a-dma-translation-job.md): Get the current status and results of a DMA translation job.

Poll this endpoint to monitor translation progress and retrieve results when complete.
Translation jobs can run for several minutes to hours depending on project size.
- [Get translation summaries for all transforms in a project](https://docs.datafold.com/api-reference/dma_v2/get-translation-summaries-for-all-transforms-in-a-project.md): Get translation summaries for all transforms in a project.

Returns a list of transform summaries including transform group metadata,
validation status, and execution results. Use this to monitor translation
progress and identify failed transforms.
- [Start a DMA translation job](https://docs.datafold.com/api-reference/dma_v2/start-a-dma-translation-job.md): Start a translation job for a DMA project.

Executes the DMA translation pipeline to convert source SQL code to target dialect.
The pipeline processes code through multiple stages (file operations, reference extraction,
template creation, SQL translation, validation, and bundling).

This endpoint launches a long-running background workflow and returns immediately with
a job_id. Use the get_translation_status endpoint to poll for progress and results.
- [Get column downstreams](https://docs.datafold.com/api-reference/explore/get-column-downstreams.md): Retrieve a list of columns or tables which depend on the given column.
- [Get column upstreams](https://docs.datafold.com/api-reference/explore/get-column-upstreams.md): Retrieve a list of columns or tables which the given column depends on.
- [Get table downstreams](https://docs.datafold.com/api-reference/explore/get-table-downstreams.md): Retrieve a list of tables which depend on the given table.
- [Get table upstreams](https://docs.datafold.com/api-reference/explore/get-table-upstreams.md): Retrieve a list of tables which the given table depends on.
- [Introduction](https://docs.datafold.com/api-reference/introduction.md)
- [Execute custom Cypher queries against the lineage graph](https://docs.datafold.com/api-reference/lineagev2/execute-custom-cypher-queries-against-the-lineage-graph.md): Execute custom Cypher queries for advanced lineage analysis.

Allows running arbitrary Cypher queries against the Memgraph lineage database.
Returns results in both tabular format and graph format (nodes and edges).

WARNING: This is a power-user endpoint. All queries are logged for audit purposes.

Use this for custom analysis beyond the standard lineage endpoints, such as:
- Finding circular dependencies
- Complex multi-hop patterns
- Aggregation queries across lineage paths
- Custom graph algorithms
- [Get all columns for a specific table](https://docs.datafold.com/api-reference/lineagev2/get-all-columns-for-a-specific-table.md): List all columns in a dataset with metadata.

Returns the complete schema of a table/view including column names, data types,
usage statistics, and popularity scores. Useful for exploring table structure
before diving into column-level lineage.
- [Get available type filters for search](https://docs.datafold.com/api-reference/lineagev2/get-available-type-filters-for-search.md): Returns available type filters for narrowing search results (e.g., type:table, type:column).
- [Get column-level lineage (field-level data flow)](https://docs.datafold.com/api-reference/lineagev2/get-column-level-lineage-field-level-data-flow.md): Get the lineage graph for a specific column.

Returns upstream source columns (where this column's data originates) and downstream
dependent columns (where this column's data flows to). Provides fine-grained lineage
tracking at the field level.

Use this for precise impact analysis, data quality root cause analysis, and understanding
transformations applied to specific fields.
- [Get column-level lineage for a dataset](https://docs.datafold.com/api-reference/lineagev2/get-column-level-lineage-for-a-dataset.md): Get column-level lineage for a dataset (table, PowerBI visual, tile, etc.).

For PowerBI visuals/tiles: shows columns they USES and their DERIVED_FROM lineage.
For regular tables: shows columns that BELONGS_TO the table and their DERIVED_FROM lineage.

This endpoint is particularly useful for PowerBI assets that use columns from multiple tables.
- [Get Column Lineage](https://docs.datafold.com/api-reference/lineagev2/get-column-lineage.md): Get column-level lineage.

Args:
    column_id: Full column identifier (format: database.schema.table.column or similar path)
    direction: Lineage direction - "upstream", "downstream", or "both" (default: "both")
    depth: Maximum traversal depth (default: configured system depth, typically 3-5 hops)

Returns:
    ColumnLineageResponse containing:
    - column: The requested column with table context and metadata
    - upstream: List of source columns this column derives from
    - downstream: List of dependent columns derived from this column
    - edges: DERIVED_FROM relationships between all returned columns

Example:
    - Get full column lineage: column_id="analytics.fact_orders.customer_id", direction="both"
    - Trace column origin: column_id="analytics.dim_customer.email", direction="upstream"
    - Find column usage: column_id="raw.users.user_id", direction="downstream", depth=3

Note: depth parameter is interpolated into Cypher query using f-string because
Cypher does not support parameterized variable-length path patterns (*1..{depth}).
Input is validated as int by FastAPI.
- [Get Config](https://docs.datafold.com/api-reference/lineagev2/get-config.md): Get client-side configuration values.
- [Get Dataset Column Lineage](https://docs.datafold.com/api-reference/lineagev2/get-dataset-column-lineage.md): Get column-level lineage for a dataset.
- [Get lineage configuration settings](https://docs.datafold.com/api-reference/lineagev2/get-lineage-configuration-settings.md): Returns configuration values used by the lineage system.
- [Get lineage for a specific query](https://docs.datafold.com/api-reference/lineagev2/get-lineage-for-a-specific-query.md): Returns tables and columns used by a query with lineage relationships.
- [Get lineage graph statistics and health metrics](https://docs.datafold.com/api-reference/lineagev2/get-lineage-graph-statistics-and-health-metrics.md): Get overall statistics about the lineage graph.

Returns counts of all major entities in the lineage graph including datasets,
columns, relationships, queries, and source files. Useful for understanding
the scope and health of the lineage data.

Use this to get a quick overview before exploring specific lineage paths.
- [Get Queries](https://docs.datafold.com/api-reference/lineagev2/get-queries.md): Get top queries by execution count.
- [Get queries that read from a table](https://docs.datafold.com/api-reference/lineagev2/get-queries-that-read-from-a-table.md): Returns queries that read from this table, ordered by execution count.
- [Get Query Lineage Endpoint](https://docs.datafold.com/api-reference/lineagev2/get-query-lineage-endpoint.md): Get tables and columns used by a query.
- [Get Search Types Endpoint](https://docs.datafold.com/api-reference/lineagev2/get-search-types-endpoint.md): Get available type filters for search autocomplete.
- [Get Stats](https://docs.datafold.com/api-reference/lineagev2/get-stats.md): Get graph statistics.

Returns:
    StatsResponse containing:
    - datasets: Total number of tables and views in the graph
    - columns: Total number of columns tracked
    - relationships: Total number of lineage edges (DEPENDS_ON + DERIVED_FROM)
    - queries: Total number of SELECT queries analyzed
    - sourceFiles: Total number of source SQL/dbt files processed

Example response:
    {
        "datasets": 1250,
        "columns": 15680,
        "relationships": 8932,
        "queries": 4521,
        "sourceFiles": 892
    }

Use this to assess lineage coverage and data quality.
- [Get Table Columns](https://docs.datafold.com/api-reference/lineagev2/get-table-columns.md): Get all columns for a table.

Args:
    table_id: Full table identifier (format: database.schema.table or similar path)

Returns:
    TableColumnsResponse containing:
    - columns: List of all columns in the table with:
        - id: Unique column identifier
        - name: Column name
        - dataType: Column data type (if available)
        - totalQueries30d: Number of queries using this column in last 30 days
        - popularity: Relative popularity score (0-100) based on query usage

Example:
    - List table schema: table_id="analytics.fact_orders"
    - Returns all columns like order_id, customer_id, amount, created_at with their metadata

Use this to understand table structure and identify important columns before
exploring column-level lineage.
- [Get table-level lineage (upstream and downstream dependencies)](https://docs.datafold.com/api-reference/lineagev2/get-table-level-lineage-upstream-and-downstream-dependencies.md): Get the lineage graph for a specific dataset (table or view).

Returns upstream sources (tables this dataset depends on) and downstream consumers
(tables that depend on this dataset), along with dependency edges. Supports configurable
traversal depth and direction.

Use this to understand data flow and impact analysis at the table level.
- [Get Table Lineage](https://docs.datafold.com/api-reference/lineagev2/get-table-lineage.md): Get upstream/downstream table lineage.

Args:
    table_id: Full table identifier (format: database.schema.table or similar path)
    direction: Lineage direction - "upstream", "downstream", or "both" (default: "both")
    depth: Maximum traversal depth (default: configured system depth, typically 3-5 hops)

Returns:
    TableLineageResponse containing:
    - dataset: The requested table/view with metadata
    - upstream: List of source tables this dataset depends on
    - downstream: List of dependent tables that use this dataset
    - edges: Dependency relationships between all returned datasets

Example:
    - Get full lineage: table_id="analytics.fact_orders", direction="both"
    - Get only sources: table_id="analytics.fact_orders", direction="upstream", depth=2
    - Get only consumers: table_id="raw.customers", direction="downstream"

Note: depth parameter is interpolated into Cypher query using f-string because
Cypher does not support parameterized variable-length path patterns (*1..{depth}).
Input is validated as int by FastAPI.
- [Get Table Queries](https://docs.datafold.com/api-reference/lineagev2/get-table-queries.md): Get queries that read from this table.
- [Get top queries by execution count](https://docs.datafold.com/api-reference/lineagev2/get-top-queries-by-execution-count.md): Returns the most frequently executed queries with metadata.
- [Run Cypher](https://docs.datafold.com/api-reference/lineagev2/run-cypher.md): Execute arbitrary Cypher query and return results.

Args:
    request: CypherRequest with query string

Returns:
    CypherResponse containing:
    - columns: List of column names returned by the query
    - results: List of result rows as dictionaries (tabular view)
    - nodes: All graph nodes returned by the query
    - edges: All graph edges/relationships returned by the query

Example queries:
    - Find all tables: "MATCH (t:Dataset) RETURN t.name LIMIT 10"
    - Find circular dependencies: "MATCH (t:Dataset)-[:DEPENDS_ON*]->(t) RETURN t"
    - Count by type: "MATCH (d:Dataset) RETURN d.asset_type, count(*) as count"
    - Complex lineage: "MATCH path=(c1:Column)-[:DERIVED_FROM*1..3]->(c2:Column) RETURN path"

WARNING: This endpoint executes arbitrary Cypher queries. It is intended for
internal debugging and power users only. All queries are logged for audit purposes.

Note: Results include both tabular data (for displaying in tables) and graph data
(nodes/edges for graph visualization).
- [Search Entities](https://docs.datafold.com/api-reference/lineagev2/search-entities.md): Search for datasets and columns by name.

Args:
    q: Search query string (minimum 2 characters). Searches in dataset/column names and IDs.
    limit: Maximum number of results to return per type (default: 50)

Returns:
    SearchResponse containing:
    - datasets: List of matching tables/views with metadata (asset type, column count, row count, popularity)
    - columns: List of matching columns with table context and popularity

Example:
    - Search for tables: q="customer" returns all datasets with "customer" in the name
    - Search for columns: q="email" returns all columns with "email" in the name
- [Search for datasets and columns in the lineage graph](https://docs.datafold.com/api-reference/lineagev2/search-for-datasets-and-columns-in-the-lineage-graph.md): Search for datasets (tables, views) and columns by name in the lineage graph.

Returns matching datasets and columns with metadata including popularity scores,
query counts, and structural information. Results are ranked by name match.

Use this to discover data assets before exploring their lineage relationships.
- [Create a Data Diff Monitor](https://docs.datafold.com/api-reference/monitors/create-a-data-diff-monitor.md)
- [Create a Data Test Monitor](https://docs.datafold.com/api-reference/monitors/create-a-data-test-monitor.md)
- [Create a Metric Monitor](https://docs.datafold.com/api-reference/monitors/create-a-metric-monitor.md)
- [Create a Schema Change Monitor](https://docs.datafold.com/api-reference/monitors/create-a-schema-change-monitor.md)
- [Delete a Monitor](https://docs.datafold.com/api-reference/monitors/delete-a-monitor.md)
- [Get Monitor](https://docs.datafold.com/api-reference/monitors/get-monitor.md)
- [Get Monitor Run](https://docs.datafold.com/api-reference/monitors/get-monitor-run.md)
- [List Monitor Runs](https://docs.datafold.com/api-reference/monitors/list-monitor-runs.md)
- [List Monitors](https://docs.datafold.com/api-reference/monitors/list-monitors.md)
- [Toggle a Monitor](https://docs.datafold.com/api-reference/monitors/toggle-a-monitor.md)
- [Trigger a run](https://docs.datafold.com/api-reference/monitors/trigger-a-run.md)
- [Update a Monitor](https://docs.datafold.com/api-reference/monitors/update-a-monitor.md)
- [Best Practices](https://docs.datafold.com/data-diff/cross-database-diffing/best-practices.md): When dealing with large datasets, it's crucial to approach diffing with specific optimization strategies in mind. We share best practices that will help you get the most accurate and efficient results from your data diffs.
- [Creating a New Data Diff](https://docs.datafold.com/data-diff/cross-database-diffing/creating-a-new-data-diff.md): Datafold's Data Diff can compare data across databases (e.g., PostgreSQL <> Snowflake, or between two SQL Server instances) to validate migrations, meet regulatory and compliance requirements, or ensure data is flowing successfully from source to target.
- [Results](https://docs.datafold.com/data-diff/cross-database-diffing/results.md): Once your data diff is complete, Datafold provides a concise, high-level summary of the detected changes in the Overview tab.
- [How Datafold Diffs Data](https://docs.datafold.com/data-diff/how-datafold-diffs-data.md): Data diffs allow you to perform value-level comparisons between any two datasets within the same database, across different databases, or even between files.
- [Best Practices](https://docs.datafold.com/data-diff/in-database-diffing/best-practices.md): We share best practices that will help you get the most accurate and efficient results from your data diffs.
- [Creating a New Data Diff](https://docs.datafold.com/data-diff/in-database-diffing/creating-a-new-data-diff.md): Setting up a new data diff in Datafold is straightforward.
- [Results](https://docs.datafold.com/data-diff/in-database-diffing/results.md): Once your data diff is complete, Datafold provides a concise, high-level summary of the detected changes in the Overview tab
- [What's a Data Diff?](https://docs.datafold.com/data-diff/what-is-data-diff.md): A data diff is the value-level comparison between two tables, used to identify critical changes to your data and guarantee data quality.
- [dbt Metadata Sync](https://docs.datafold.com/data-explorer/best-practices/dbt-metadata-sync.md): Datafold can automatically ingest dbt metadata from your production environment and display it in Data Explorer.
- [How It Works](https://docs.datafold.com/data-explorer/how-it-works.md): The UI visually maps workflows and tracks column-level or tabular lineages, helping users understand the impact of upstream changes.
- [Lineage](https://docs.datafold.com/data-explorer/lineage.md): Datafold offers a column-level and tabular lineage view.
- [Profile](https://docs.datafold.com/data-explorer/profile.md): View a data profile that summarizes key table and column-level statistics, and any upstream dependencies.
- [Monitor Types](https://docs.datafold.com/data-monitoring/monitor-types.md): Monitoring your data for unexpected changes is one of the cornerstones of data observability.
- [Monitors as Code](https://docs.datafold.com/data-monitoring/monitors-as-code.md): Manage Datafold monitors via version-controlled YAML for greater scalability, governance, and flexibility in code-based workflows.
- [Data Diff Monitors](https://docs.datafold.com/data-monitoring/monitors/data-diff-monitors.md): Data Diff monitors compare datasets across or within databases, identifying row and column discrepancies with customizable scheduling and notifications.
- [Data Test Monitors](https://docs.datafold.com/data-monitoring/monitors/data-test-monitors.md): Data Tests validate your data against off-the-shelf checks or custom business rules.
- [Metric Monitors](https://docs.datafold.com/data-monitoring/monitors/metric-monitors.md): Metric monitors detect anomalies in your data using ML-based algorithms or manual thresholds, supporting standard and custom metrics for tables or columns.
- [Schema Change Monitors](https://docs.datafold.com/data-monitoring/monitors/schema-change-monitors.md): Schema Change monitors notify you when a table’s schema changes, such as when columns are added, removed, or data types are modified.
- [Deployment Options](https://docs.datafold.com/datafold-deployment/datafold-deployment-options.md): Datafold is a web-based application with multiple deployment options, including multi-tenant SaaS and dedicated cloud (either customer- or Datafold-hosted).
- [Datafold VPC Deployment on AWS](https://docs.datafold.com/datafold-deployment/dedicated-cloud/aws.md): Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on AWS.
- [Datafold VPC Deployment on Azure](https://docs.datafold.com/datafold-deployment/dedicated-cloud/azure.md): Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on Azure.
- [Datafold VPC Deployment on GCP](https://docs.datafold.com/datafold-deployment/dedicated-cloud/gcp.md): Learn how to deploy Datafold in a Virtual Private Cloud (VPC) on GCP.
- [Handling Data Drift](https://docs.datafold.com/deployment-testing/best-practices/handling-data-drift.md): Ensuring Datafold in CI executes apples-to-apples comparison between staging and production environments.
- [Slim Diff](https://docs.datafold.com/deployment-testing/best-practices/slim-diff.md): Choose which downstream tables to diff to optimize time, cost, and performance.
- [Configuration](https://docs.datafold.com/deployment-testing/configuration.md): Explore configuration options for CI/CD testing in Datafold.
- [Column Remapping](https://docs.datafold.com/deployment-testing/configuration/column-remapping.md): Specify column renaming in your git commit message so Datafold can map renamed columns to their original counterparts in production for accurate comparison.
- [Running Data Diff for Specific PRs/MRs](https://docs.datafold.com/deployment-testing/configuration/datafold-ci/on-demand.md): By default, Datafold CI runs on every new pull/merge request and commits to existing ones.
- [Running Data Diff on Specific Branches](https://docs.datafold.com/deployment-testing/configuration/datafold-ci/specifc.md): By default, Datafold CI runs on every new pull/merge request and commits to existing ones.
- [Diff Timeline](https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/diff-timeline.md): Specify a `time_column` to visualize match rates between tables for each column over time.
- [Excluding Models](https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/excluding-models.md): Use `never_diff` to exclude a model or subdirectory of models from data diffs.
- [Including/Excluding Columns](https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/including-excluding-columns.md): Specify columns to include or exclude from the data diff using `include_columns` and `exclude_columns`.
- [SQL Filters](https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/sql-filters.md): Use dbt YAML configuration to set model-specific filters for Datafold CI.
- [Time Travel](https://docs.datafold.com/deployment-testing/configuration/model-specific-ci/time-travel.md): Use `prod_time_travel` and `pr_time_travel` to diff tables from specific points in time.
- [Primary Key Inference](https://docs.datafold.com/deployment-testing/configuration/primary-key.md): Datafold requires a primary key to perform data diffs. Using dbt metadata, Datafold identifies the column to use as the primary key for accurate data diffs.
- [Getting Started with CI/CD Testing](https://docs.datafold.com/deployment-testing/getting-started.md): Learn how to set up CI/CD testing with Datafold by integrating your data connections, code repositories, and CI pipeline for automated testing.
- [API](https://docs.datafold.com/deployment-testing/getting-started/universal/api.md): Learn how to set up and configure Datafold's API for CI/CD testing.
- [No-Code](https://docs.datafold.com/deployment-testing/getting-started/universal/no-code.md): Set up Datafold's No-Code CI integration to create and manage Data Diffs without writing code.
- [How Datafold in CI Works](https://docs.datafold.com/deployment-testing/how-it-works.md): Learn how Datafold integrates with your Continuous Integration (CI) process to create Data Diffs for all SQL code changes, catching issues before they make it into production.
- [CI/CD Testing](https://docs.datafold.com/faq/ci-cd-testing.md)
- [Data Diffing](https://docs.datafold.com/faq/data-diffing.md)
- [Data Monitoring and Observability](https://docs.datafold.com/faq/data-monitoring-observability.md)
- [Data Reconciliation](https://docs.datafold.com/faq/data-reconciliation.md)
- [Data Storage and Security](https://docs.datafold.com/faq/data-storage-and-security.md)
- [Integrating Datafold with dbt](https://docs.datafold.com/faq/datafold-with-dbt.md)
- [Overview](https://docs.datafold.com/faq/overview.md): Get answers to the most common questions regarding our product.
- [Performance and Scalability](https://docs.datafold.com/faq/performance-and-scalability.md)
- [Resource Management](https://docs.datafold.com/faq/resource-management.md)
- [Hightouch](https://docs.datafold.com/integrations/bi-data-apps/hightouch.md): Navigate to Settings > Integrations > Data Apps and add a Hightouch Integration.
- [Looker](https://docs.datafold.com/integrations/bi-data-apps/looker.md)
- [Mode](https://docs.datafold.com/integrations/bi-data-apps/mode.md)
- [Power BI](https://docs.datafold.com/integrations/bi-data-apps/power-bi.md): Include Power BI entities in Data Explorer and column-level lineage.
- [Tableau](https://docs.datafold.com/integrations/bi-data-apps/tableau.md): Visualize downstream Tableau dependencies and understand how warehouse changes impact your BI layer.
- [Tracking Jobs](https://docs.datafold.com/integrations/bi-data-apps/tracking-jobs.md): Track the completion and success of your data app integration syncs.
- [Integrate with Code Repositories](https://docs.datafold.com/integrations/code-repositories.md): Connect your code repositories with Datafold.
- [Azure DevOps](https://docs.datafold.com/integrations/code-repositories/azure-devops.md)
- [Bitbucket](https://docs.datafold.com/integrations/code-repositories/bitbucket.md)
- [GitHub](https://docs.datafold.com/integrations/code-repositories/github.md)
- [GitLab](https://docs.datafold.com/integrations/code-repositories/gitlab.md)
- [Set Up Your Data Connection](https://docs.datafold.com/integrations/databases.md): Set up your Data Connection with Datafold.
- [Athena](https://docs.datafold.com/integrations/databases/athena.md)
- [BigQuery](https://docs.datafold.com/integrations/databases/bigquery.md)
- [Databricks](https://docs.datafold.com/integrations/databases/databricks.md)
- [Dremio](https://docs.datafold.com/integrations/databases/dremio.md)
- [MySQL](https://docs.datafold.com/integrations/databases/mysql.md)
- [Netezza](https://docs.datafold.com/integrations/databases/netezza.md)
- [Oracle](https://docs.datafold.com/integrations/databases/oracle.md)
- [PostgreSQL](https://docs.datafold.com/integrations/databases/postgresql.md)
- [Redshift](https://docs.datafold.com/integrations/databases/redshift.md)
- [SAP HANA](https://docs.datafold.com/integrations/databases/sap-hana.md)
- [Snowflake](https://docs.datafold.com/integrations/databases/snowflake.md)
- [Microsoft SQL Server](https://docs.datafold.com/integrations/databases/sql-server.md)
- [Starburst](https://docs.datafold.com/integrations/databases/starburst.md)
- [Teradata](https://docs.datafold.com/integrations/databases/teradata.md)
- [OAuth Support](https://docs.datafold.com/integrations/oauth.md): Set up OAuth App Connections in your supported data warehouses to securely execute data diffs on behalf of your users.
- [Integrate with Orchestrators](https://docs.datafold.com/integrations/orchestrators.md): Integrate Datafold with dbt Core, dbt Cloud, Airflow, or custom orchestrators to streamline your data workflows with automated monitoring, testing, and seamless CI integration.
- [Custom Integrations](https://docs.datafold.com/integrations/orchestrators/custom-integrations.md): Integrate Datafold with your custom orchestration using the Datafold SDK and REST API.
- [dbt Cloud](https://docs.datafold.com/integrations/orchestrators/dbt-cloud.md): Integrate Datafold with dbt Cloud to automate Data Diffs in your CI pipeline, leveraging dbt jobs to detect changes and ensure data quality before merging.
- [dbt Core](https://docs.datafold.com/integrations/orchestrators/dbt-core.md): Set up Datafold’s integration with dbt Core to automate Data Diffs in your CI pipeline.
- [Compliance & Trust Center](https://docs.datafold.com/security/compilance-trust-center.md)
- [Securing Connections](https://docs.datafold.com/security/securing-connections.md): Datafold supports multiple options to secure connections between your resources (e.g., databases and BI tools) and Datafold.
- [Single Sign-On](https://docs.datafold.com/security/single-sign-on.md): Set up Single Sign-On with one of the following options.
- [Google OAuth](https://docs.datafold.com/security/single-sign-on/google-oauth.md)
- [Okta (OIDC)](https://docs.datafold.com/security/single-sign-on/okta.md)
- [SAML](https://docs.datafold.com/security/single-sign-on/saml.md): SAML (Security Assertion Markup Language) is a protocol that enables secure user authentication by integrating Identity Providers (IdPs) with Service Providers (SPs).
- [Google](https://docs.datafold.com/security/single-sign-on/saml/examples/google.md)
- [Microsoft Entra ID](https://docs.datafold.com/security/single-sign-on/saml/examples/microsoft-entra-id-configuration.md)
- [Okta](https://docs.datafold.com/security/single-sign-on/saml/examples/okta.md)
- [null](https://docs.datafold.com/security/single-sign-on/saml/group-provisioning.md): Automatically sync group membership with your SAML Identity Provider (IdP).
- [FAQ](https://docs.datafold.com/support/faq-redirect.md)
- [Support](https://docs.datafold.com/support/support.md): Datafold offers multiple support channels to assist users with troubleshooting and inquiries.
- [Welcome](https://docs.datafold.com/welcome.md): Datafold is the unified platform proactive data quality that combines automated data testing, data reconciliation, and observability to help data teams prevent data quality issues and accelerate their development velocity.

## Optional

- [About Datafold](https://www.datafold.com/)
- [Blog](https://www.datafold.com/blog?)


--------------------