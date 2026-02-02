# Open-Meteo API Docs
**URL:** https://open-meteo.com/en/docs
**Page Title:** 🌦️ Docs | Open-Meteo.com
--------------------


## Weather Forecast API

Seamless integration of high-resolution weather models with up 16 days forecast
[LINK: API Response](#api_response)

## API Response

[LINK: Download XLSX](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&format=xlsx)
[LINK: Download CSV](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&format=csv)
[LINK: Open in new tab](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m)

## Data Sources

Open-Meteo weather forecast APIs use weather models from multiple national weather providers.
			For each location worldwide, the best models will be combined to provide the best possible
			forecast.
Weather models cover different geographic areas at different resolutions and provide different
			weather variables. Depending on the model, data have been interpolated to hourly values or not
			all weather variables are available. With the drop down Weather models (just below
			the hourly variables), you can select and compare individual weather models.
[LINK: model updates documentation](/en/docs/model-updates)
[LINK: ICON](/en/docs/dwd-api)
[LINK: GFS & HRRR](/en/docs/gfs-api)
[LINK: ARPEGE & AROME](/en/docs/meteofrance-api)
[LINK: IFS & AIFS](/en/docs/ecmwf-api)
[LINK: UKMO](/en/docs/ukmo-api)
[LINK: KMA](/en/docs/kma-api)
[LINK: MSM & GSM](/en/docs/jma-api)
[LINK: ICON CH](/en/docs/meteoswiss-api)
[LINK: MET Nordic](/en/docs/metno-api)
[LINK: GEM](/en/docs/gem-api)
[LINK: ACCESS-G](/en/docs/bom-api)
[LINK: GFS GRAPES](/en/docs/cma-api)
[LINK: HARMONIE](/en/docs/knmi-api)
[LINK: HARMONIE](/en/docs/dmi-api)
[LINK: ARPAE](/en/docs/italia-meteo-arpae-api)
[LINK: API Documentation](#api_documentation)

## API Documentation

The API endpoint /v1/forecast accepts a geographical coordinate, a list of
			weather variables and responds with a JSON hourly weather forecast for 7 days. Time always
			starts at 0:00 today and contains 168 hours. If &forecast_days=16 is set, up to 16 days of forecast can be returned. All URL parameters
			are listed below:
Additional optional URL parameters will be added. For API stability, no required parameters
			will be added in the future!

### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given
			as an instantaneous value for the indicated hour. Some variables like precipitation are calculated
			from the preceding hour as an average or sum.

### 15-Minutely Parameter Definition

The parameter &minutely_15= can be used to get 15-minutely data. This data is based
			on NOAA HRRR model for North America and DWD ICON-D2 and Météo-France AROME model for Central Europe.
			If 15-minutely data is requested for other regions data is interpolated from 1-hourly to 15-minutely.
15-minutely data can be requested for other weather variables that are available for hourly
			data, but will use interpolation.

### Pressure Level Variables

Pressure level variables do not have fixed altitudes. Altitude varies with atmospheric
			pressure. 1000 hPa is roughly between 60 and 160 meters above sea level. Estimated altitudes
			are given below. Altitudes are in meters above sea level (not above ground). For precise
			altitudes, geopotential_height can be used.
All pressure levels have valid times of the indicated hour (instant).

### Daily Parameter Definition

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

### JSON Return Object

On success a JSON object will be returned.

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
			object is returned with a HTTP 400 status code.

## Weather variable documentation

### WMO Weather interpretation codes (WW)

(*) Thunderstorm forecast with hail is only available in Central Europe

--------------------