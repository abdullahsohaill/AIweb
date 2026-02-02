# Waltti-datan
**URL:** https://opendata.waltti.fi/docs
**Page Title:** Documentation | Waltti GTFS Realtime
--------------------


## Contents

## GTFS Realtime

## Introduction

This document describes what data is available and can be expected in the GTFS Realtime feeds.
More information about the interface can be found from https://developers.google.com/transit/gtfs-realtime/
[LINK: https://developers.google.com/transit/gtfs-realtime/](https://developers.google.com/transit/gtfs-realtime/)
The provided feed is in binary format providing full dataset . The GTFS Realtime specification version 2.0 is supported.
Maximum rates for the REST API (per server or device) are:
- Trip Updates every 30 seconds
- Service Alerts every 60 seconds
- Vehicle Positions every 1 seconds

## Supported cities

Currently the API supports following cities:
In order to use the API, replace /:city/ with the desired city's value (for example /jyvaskyla/api/gtfsrealtime/v1.0/feed/tripupdate ).

## GTFS Realtime - TripUpdate

Available for currently running trips. Cancelled trips exist in the feed until the trip is scheduled to arrive to the last stop.

## GTFS Realtime - VehiclePosition

## GTFS Realtime - Alert

## Static packages

## Static GTFS packages

This API also offers static GTFS packages in zip format. They are refreshed every night at 01:00 (EET). The packages are available under CC4.0BY license
Zipped package can be accessed here (replace XXX with the desired value):
Currently the API supports following values:

## Static NeTEx packages

Similar to the static GTFS packages, you can access NeTEx packages by appending _netex to the authority id.

--------------------