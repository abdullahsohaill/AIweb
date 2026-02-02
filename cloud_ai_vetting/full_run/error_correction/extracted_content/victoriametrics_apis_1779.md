# VictoriaMetrics APIs
**URL:** https://docs.victoriametrics.com/victoriametrics/url-examples
**Page Title:** VictoriaMetrics: API examples
--------------------


## API examples #

### /api/v1/admin/tsdb/delete_series #

Deletes time series from VictoriaMetrics
Note that handler accepts any HTTP method, so sending a GET request to /api/v1/admin/tsdb/delete_series will result in deletion of time series.
Single-node VictoriaMetrics:
The expected output should return HTTP Status 204 and will look like:
Cluster version of VictoriaMetrics:
The expected output should return HTTP Status 204 and will look like:
Additional information:
- How to delete time series
- URL format for VictoriaMetrics cluster

### /api/v1/export #

Exports raw samples from VictoriaMetrics in JSON line format
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to export time series
- How to import time series
- How to export data in JSON line format
- URL format for VictoriaMetrics cluster

### /api/v1/export/csv #

Exports raw samples from VictoriaMetrics in CSV format
You must specify the desired format and optionally match[] selectors.
Suppose you have a demo metric with job and instance labels.
The following command exports all time series of the demo metric in CSV format including the job and instance labels.
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to export time series
- How to import time series
- URL format for VictoriaMetrics cluster

### /api/v1/export/native #

Exports raw samples from VictoriaMetrics in native format
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
More information:
- How to export time series
- How to import time series
- URL format for VictoriaMetrics cluster

### /api/v1/import #

Imports data to VictoriaMetrics in JSON line format
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
More information:
- How to import time series
- How to export time series
- URL format for VictoriaMetrics cluster

### /api/v1/import/csv #

Imports CSV data to VictoriaMetrics
You must specify the desired format . Suppose you want to import demo metric exported with /api/v1/export/csv .
The following command imports all time series of the demo metric in CSV format including the job and instance labels.
[LINK: /api/v1/export/csv](/victoriametrics/url-examples/#apiv1exportcsv)
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
A single CSV line can contain multiple metrics. For example, this command imports two metrics ask{ticker="GOOG",market="NYSE"} 1.23 and bid{ticker="GOOG",market="NYSE"} 4.56 :
Additional information:
- How to import time series
- How to export time series
- URL format for VictoriaMetrics cluster

### /api/v1/import/native #

Imports data to VictoriaMetrics in native format
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to import time series
- How to export time series
- URL format for VictoriaMetrics cluster

### /api/v1/import/prometheus #

Imports data to VictoriaMetrics in Prometheus text exposition format
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to import time series
- How to export time series
- URL format for VictoriaMetrics cluster

### /api/v1/labels #

Get a list of label names at the given time range
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
By default, VictoriaMetrics returns labels seen during the last day starting at 00:00 UTC because of performance reasons.
An arbitrary time range can be set via start and end query args .
The specified start..end time range is rounded to UTC day granularity because of performance reasons.
Additional information:
- Getting label names
[LINK: Getting label names](https://prometheus.io/docs/prometheus/latest/querying/api/#getting-label-names)
- Prometheus querying API usage
[LINK: Prometheus querying API usage](/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage)
- URL format for VictoriaMetrics cluster

### /api/v1/label/…/values #

Get a list of values for a particular label on the given time range
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
By default, VictoriaMetrics returns labels values seen during the last day starting at 00:00 UTC because of performance reasons.
An arbitrary time range can be set via start and end query args.
The specified start..end time range is rounded to UTC day granularity because of performance reasons.
Additional information:
- Querying label values
[LINK: Querying label values](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-label-values)
- Prometheus querying API usage
[LINK: Prometheus querying API usage](/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage)
- URL format for VictoriaMetrics cluster

### /api/v1/query #

Performs PromQL/MetricsQL instant query
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- Instant queries
- Prometheus querying API usage
[LINK: Prometheus querying API usage](/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage)
- Query language
- URL format for VictoriaMetrics cluster

### /api/v1/query_range #

Performs PromQL/MetricsQL range query
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- Range queries
- Prometheus querying API usage
[LINK: Prometheus querying API usage](/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage)
- Query language
- URL format for VictoriaMetrics cluster

### /api/v1/series #

Returns series names with their labels on the given time range
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
By default, VictoriaMetrics returns time series seen during the last day starting at 00:00 UTC because of performance reasons.
An arbitrary time range can be set via start and end query args.
The specified start..end time range is rounded to UTC day granularity because of performance reasons.
Additional information:
- Finding series by label matchers
[LINK: Finding series by label matchers](https://prometheus.io/docs/prometheus/latest/querying/api/#finding-series-by-label-matchers)
- Prometheus querying API usage
[LINK: Prometheus querying API usage](/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage)
- URL format for VictoriaMetrics cluster VictoriaMetrics accepts limit query arg for /api/v1/series handlers for limiting the number of returned entries. For example, the query to /api/v1/series?limit=5 returns a sample of up to 5 series, while ignoring the rest. If the provided limit value exceeds the corresponding -search.maxSeries command-line flag values, then limits specified in the command-line flags are used.

### /api/v1/status/tsdb #

Cardinality statistics
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- TSDB Stats
[LINK: TSDB Stats](https://prometheus.io/docs/prometheus/latest/querying/api/#tsdb-stats)
- Prometheus querying API usage
[LINK: Prometheus querying API usage](/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-usage)
- URL format for VictoriaMetrics cluster

### /api/v1/metadata #

Returns stored metrics metadata . metric query arg can be used to filter metadata for specific metrics. limit query arg can be used to limit the number of returned metadata entries.
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- Single-node - Metrics Metadata
- Cluster - Metrics Metadata
- VMAgent - Metrics Metadata

### /datadog #

DataDog URL for Single-node VictoriaMetrics
DataDog URL for Cluster version of VictoriaMetrics

### /datadog/api/v1/series #

Imports data in DataDog v1 format into VictoriaMetrics
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to send data from DataDog agent
- URL format for VictoriaMetrics cluster

### /datadog/api/v2/series #

Imports data in DataDog v2 format into VictoriaMetrics
[LINK: DataDog v2](https://docs.datadoghq.com/api/latest/metrics/#submit-metrics)
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to send data from DataDog agent
- URL format for VictoriaMetrics cluster

### /federate #

Returns federated metrics
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- Federation
- Prometheus-compatible federation data
[LINK: Prometheus-compatible federation data](https://prometheus.io/docs/prometheus/latest/federation/#configuring-federation)
- URL format for VictoriaMetrics cluster

### /graphite/metrics/find #

Searches Graphite metrics in VictoriaMetrics
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- Metrics find API in Graphite
[LINK: Metrics find API in Graphite](https://graphite-api.readthedocs.io/en/latest/api.html#metrics-find)
- Graphite API in VictoriaMetrics
[LINK: Graphite API in VictoriaMetrics](/victoriametrics/integrations/graphite/#graphite-api-usage)
- How to send Graphite data to VictoriaMetrics
- URL Format

### /influx/write #

Writes data with InfluxDB line protocol to VictoriaMetrics
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to send Influx data to VictoriaMetrics
- URL Format

### /internal/resetRollupResultCache #

Resets the response cache for previously served queries. It is recommended to invoke after backfilling procedure.
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
vmselect will propagate this call to the rest of the vmselects listed in its -selectNode cmd-line flag. If this
flag isn’t set, then cache need to be purged from each vmselect individually.

### TCP and UDP #

Turned off by default. Enable OpenTSDB receiver in VictoriaMetrics by setting -opentsdbListenAddr command-line flag. If run from docker, ‘-opentsdbListenAddr’ port should be exposed
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Enable HTTP server for OpenTSDB /api/put requests by setting -opentsdbHTTPListenAddr command-line flag.
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- OpenTSDB http put API
[LINK: OpenTSDB http put API](http://opentsdb.net/docs/build/html/api_http/put.html)
- How to send data OpenTSDB data to VictoriaMetrics
Enable Graphite receiver in VictoriaMetrics by setting -graphiteListenAddr command-line flag.
Single-node VictoriaMetrics:
Cluster version of VictoriaMetrics:
Additional information:
- How to send Graphite data to VictoriaMetrics
- Multitenancy in cluster version of VictoriaMetrics

--------------------