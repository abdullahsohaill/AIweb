# Food Data Central API
**URL:** https://fdc.nal.usda.gov/api-guide.html
**Page Title:** API Guide | USDA FoodData Central
--------------------


## FoodData Central API Guide

## Overview

The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.
To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on Data Type Documentation . This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.
Note: The API that was available on the USDA Food Composition Databases Web site is no longer being updated and will be discontinued March 31, 2020. Users are encouraged to begin working with the new FoodData Central API system described on this page. This new API allows users to obtain Standard Reference (SR) Legacy data, provides the most current data from the USDA Global Branded Foods Database, and give users the ability to search for specific foods in Foundation Foods and the Food and Nutrient Database for Dietary Studies (FNDDS) 2019-2020.

## What's Available

The API provides two endpoints: the Food Search endpoint, which returns foods that match desired search criteria, and the Food Details endpoint, which returns details on a particular food.

## Gaining Access

Anyone may access and use the API. However, a data.gov API key must be incorporated into each API request. Sign up to obtain a key , then follow the instructions for how to use your key .
[LINK: Sign up to obtain a key](/api-key-signup)
[LINK: instructions for how to use your key](https://api.data.gov/docs/api-key/)

## Key Responsibility

It is the API Key holder's responsibility to ensure that their key is not made publicly available. Any API keys discovered online, such as those in a code repository, will be deactivated to prevent malicious use.

## Rate Limits

FoodData Central currently limits the number of API requests to a default rate of 1,000 requests per hour per IP address, as this is adequate for most applications. Exceeding this limit will cause the API key to be temporarily blocked for 1 hour. More detailed information on rate limits may be found at https://api.data.gov/docs/rate-limits . Contact FoodData Central if a higher request rate setting is needed.
[LINK: https://api.data.gov/docs/rate-limits](https://api.data.gov/docs/rate-limits)

## Licensing

USDA FoodData Central data are in the public domain and they are not copyrighted. They are published under CC0 1.0 Universal (CC0 1.0)
No permission is needed for their use, but we request that users list FoodData Central as the source of the data, and when possible, notify us of the product that uses the data so we may better track how FDC is being used in the public domain. The suggested citation is:
U.S. Department of Agriculture, Agricultural Research Service. FoodData Central, 2019. fdc.nal.usda.gov.
Note: Release numbers and years change as new versions are released. For more information, please see Download Data .

## API Endpoints

[LINK: GET](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/getFood)
[LINK: GET](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/getFoods)
[LINK: POST](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/postFoods)
[LINK: GET](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/getFoodsList)
[LINK: POST](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/postFoodsList)
[LINK: GET](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/getFoodsSearch)
[LINK: POST](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1#/FDC/postFoodsSearch)

## Sample Calls

Note: These calls use DEMO_KEY for the API key, which can be used for initially exploring the API prior to signing up, but has much lower rate limits. See here for more info on uses and limitations of DEMO_KEY.
[LINK: here](https://api.data.gov/docs/rate-limits)

### GET REQUEST:

The number (######) in the above sample must be a valid FoodData Central ID.

### POST REQUEST:

Note: If using curl on Windows, the body of the POST request (-d option) is enclosed in double quotes (as shown in the above sample).
Note: The "dataType" parameter values need to be specified as an array.

## API Spec

The OpenAPI v3 spec for the API provides a complete specification of the API endpoints, including input parameters and output data. It is available in HTML , JSON , or YAML formats.
[LINK: HTML](https://fdc.nal.usda.gov/api-spec/fdc_api.html)
[LINK: JSON](https://api.nal.usda.gov/fdc/v1/json-spec?api_key=DEMO_KEY)
[LINK: YAML](https://api.nal.usda.gov/fdc/v1/yaml-spec?api_key=DEMO_KEY)

### The spec is also available on SwaggerHub at:

https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1
[LINK: https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1](https://app.swaggerhub.com/apis/fdcnal/food-data_central_api/1.0.1)

--------------------